import requests
import streamlit as st
from datetime import datetime

from frontend.services import api_client


def _show_backend_error(exc: Exception) -> None:
    if isinstance(exc, requests.ConnectionError):
        st.error("Could not reach the backend. Is it running on port 8000?")
    elif isinstance(exc, requests.HTTPError) and exc.response is not None:
        st.error(f"Backend returned {exc.response.status_code}: {exc.response.text}")
    else:
        st.error(f"Unexpected error: {exc}")


def _format_date(date_str: str) -> str:
    """ISO format date ko readable string me convert karta hai."""
    if not date_str:
        return ""
    try:
        # Handles ISO 8601 strings like '2026-07-26T21:54:00Z'
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y • %I:%M %p")
    except Exception:
        return date_str.split("T")[0] if "T" in date_str else date_str


def render() -> None:
    # ── MODERN HEADER BANNER ──
    st.markdown("""
    <style>
        .history-hero {
            background: linear-gradient(135deg, #1e1b4b 0%, #4338ca 100%);
            padding: 30px;
            border-radius: 20px;
            color: #ffffff;
            margin-bottom: 24px;
            box-shadow: 0 10px 25px rgba(67, 56, 202, 0.2);
        }
        .history-hero-title {
            font-size: 28px;
            font-weight: 900;
            margin: 0 0 6px 0;
            letter-spacing: -0.5px;
        }
        .history-hero-sub {
            font-size: 14px;
            color: #c7d2fe;
            margin: 0;
        }
        
        /* Quick Metrics Summary Cards */
        .metric-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 16px 20px;
            border: 1px solid #e0e7ff;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
            text-align: center;
        }
        .metric-val {
            font-size: 26px;
            font-weight: 800;
            color: #3730a3;
        }
        .metric-label {
            font-size: 12px;
            color: #64748b;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
    </style>

    <div class="history-hero">
        <div class="history-hero-title">📊 Analysis History</div>
        <div class="history-hero-sub">Past resume evaluations and detailed breakdown saved against your account.</div>
    </div>
    """, unsafe_allow_html=True)

    access_token = st.session_state.get("access_token")
    if not access_token:
        st.warning("⚠️ Sign in from the sidebar to view your history.")
        return

    try:
        history = api_client.get_history(access_token)
    except requests.RequestException as exc:
        _show_backend_error(exc)
        return

    if not history:
        st.info("No analyses yet for this account. Run a scoring on the ATS Scorer page first.")
        if st.button("🎯 Go to ATS Scorer", type="primary"):
            st.session_state.current_view = "scorer"
            st.rerun()
        return

    # ── CALCULATE QUICK STATS ──
    total_resumes = len(history)
    scores = [float(e.get("ats_score", 0)) for e in history]
    avg_score = sum(scores) / total_resumes if total_resumes > 0 else 0
    highest_score = max(scores) if scores else 0

    # ── DASHBOARD STATS ROW ──
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(f'<div class="metric-card"><div class="metric-val">{total_resumes}</div><div class="metric-label">Total Resumes</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown(f'<div class="metric-card"><div class="metric-val">{avg_score:.0f}%</div><div class="metric-label">Avg Match Score</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown(f'<div class="metric-card"><div class="metric-val">{highest_score:.0f}/100</div><div class="metric-label">Highest Score</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── RESUME HISTORY EXPANDERS ──
    for idx, entry in enumerate(history):
        filename = entry.get("filename", "resume")
        ats_score = float(entry.get("ats_score", 0))
        created_at_raw = entry.get("created_at", "")
        formatted_date = _format_date(created_at_raw)
        analysis = entry.get("analysis_result", {}) or {}

        component_scores = analysis.get("component_scores", {}) or {}
        jd_comparison = analysis.get("jd_comparison") or analysis.get("jd_match_analysis")

        # Clean Expander Label with formatted date
        label = f"📄 {filename}  —  Score: {ats_score:.0f}/100"
        if formatted_date:
            label += f"  ({formatted_date})"

        with st.expander(label):
            st.markdown("### Score Breakdown")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric("Overall Score", f"{ats_score:.0f}/100")
                st.metric("Formatting", f"{component_scores.get('formatting', 0):.0f}/20")
            with c2:
                st.metric("Keywords", f"{component_scores.get('keywords', 0):.0f}/25")
                st.metric("Content Quality", f"{component_scores.get('content', 0):.0f}/25")
            with c3:
                st.metric("Skill Validation", f"{component_scores.get('skill_validation', 0):.0f}/15")
                st.metric("ATS Compatibility", f"{component_scores.get('ats_compatibility', 0):.0f}/15")

            if jd_comparison:
                st.markdown("---")
                jd_score = jd_comparison.get("match_percentage", 0)
                st.markdown(f"🎯 **JD Match:** `{jd_score:.0f}%`")

            st.markdown("---")
            entry_id = entry.get("id")
            if entry_id:
                if st.button("🗑️ Delete Analysis", key=f"delete_{idx}"):
                    try:
                        api_client.delete_history_entry(str(entry_id), access_token)
                        st.success("Analysis deleted.")
                        st.rerun()
                    except requests.RequestException as exc:
                        _show_backend_error(exc)