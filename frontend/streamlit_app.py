import sys
from pathlib import Path
import streamlit as st

# Put the repo root on sys.path so `from frontend.views import ...` resolves
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configure page
st.set_page_config(
    page_title="ATS Resume Scorer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Auth state. Populated by Supabase sign-in / sign-up / OAuth.
for key, default in [
    ("access_token", None),
    ("refresh_token", None),
    ("user_id", None),       # Supabase auth user id (uuid)
    ("user_email", None),
    ("auth_error", None),
    ("auth_info", None),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# Initialize session state for view management
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'landing'

# Handle Google OAuth redirect code exchange
if (
    not st.session_state.access_token
    and "code" in st.query_params
):
    from frontend.services import supabase_client
    result = supabase_client.exchange_code_for_session(st.query_params["code"])

    st.query_params.clear()
    if "error" in result:
        st.session_state.auth_error = f"Google sign-in failed: {result['error']}"
        st.session_state.current_view = 'auth'
    else:
        st.session_state.access_token  = result["access_token"]
        st.session_state.refresh_token = result["refresh_token"]
        st.session_state.user_id       = result["user_id"]
        st.session_state.user_email    = result["email"]
        st.session_state.current_view   = 'landing'
        st.rerun()

# Load custom CSS
def load_css():
    try:
        css_path = Path(__file__).parent / 'assets' / 'styles.css'
        with open(css_path, 'r') as f:
            return f'<style>{f.read()}</style>'
    except FileNotFoundError:
        return ''

st.markdown(load_css(), unsafe_allow_html=True)


# ── HELPER FUNCTIONS ──
def get_user_display_name():
    email = st.session_state.get("user_email")
    if not email:
        return "User"
    raw_name = email.split('@')[0]
    clean_name = raw_name.replace('.', ' ').replace('_', ' ').split()[0]
    return clean_name.capitalize()


def render_welcome_hero():
    user_name = get_user_display_name()
    
    st.markdown(f"""
    <style>
        .welcome-hero {{
            background: linear-gradient(135deg, rgba(30, 27, 75, 0.88) 0%, rgba(99, 102, 241, 0.85) 100%),
                        url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1200&q=80');
            background-size: cover;
            background-position: center;
            border-radius: 16px;
            padding: 32px 36px;
            color: #ffffff;
            margin-bottom: 24px;
            box-shadow: 0 10px 25px rgba(99, 102, 241, 0.2);
        }}
        .welcome-title {{
            font-size: 28px;
            font-weight: 900;
            margin-bottom: 4px;
            letter-spacing: -0.5px;
        }}
        .welcome-sub {{
            font-size: 14px;
            color: #e0e7ff;
            opacity: 0.95;
        }}
    </style>

    <div class="welcome-hero">
        <div class="welcome-title">Hi, {user_name}! 👋</div>
        <div class="welcome-sub">Welcome back to ATS Resume Scorer. Ready to optimize your resume today?</div>
    </div>
    """, unsafe_allow_html=True)


# ── DEDICATED FULL-SCREEN LIGHT WHITE & BLUE AUTH VIEW ──
def render_auth_view():
    from frontend.services import supabase_client

    # Apply full-screen Light White & Blue background image CSS
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, rgba(238, 242, 255, 0.85) 0%, rgba(224, 231, 255, 0.9) 100%),
                        url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80') !important;
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }

        .auth-card-title {
            text-align: center;
            font-size: 32px;
            font-weight: 900;
            color: #1e1b4b;
            margin-bottom: 4px;
        }

        .auth-card-sub {
            text-align: center;
            font-size: 14px;
            color: #4338ca;
            margin-bottom: 24px;
            font-weight: 500;
        }

        /* Clean White Form Container */
        [data-testid="stForm"] {
            background: #ffffff !important;
            padding: 24px !important;
            border-radius: 16px !important;
            box-shadow: 0 10px 30px rgba(79, 70, 229, 0.08) !important;
            border: 1px solid #e0e7ff !important;
        }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="auth-card-title">Welcome Back 🚀</div>', unsafe_allow_html=True)
        st.markdown('<div class="auth-card-sub">Sign in to optimize your resume with AI</div>', unsafe_allow_html=True)

        if st.session_state.auth_error:
            st.error(st.session_state.auth_error)
            st.session_state.auth_error = None
        if st.session_state.auth_info:
            st.info(st.session_state.auth_info)
            st.session_state.auth_info = None

        tab_in, tab_up = st.tabs(["🔑 Sign In", "✨ Create Account"])

        with tab_in:
            with st.form("signin_form", clear_on_submit=False):
                email = st.text_input("Email Address", key="signin_email", placeholder="name@example.com")
                password = st.text_input("Password", type="password", key="signin_pw", placeholder="••••••••")
                submitted = st.form_submit_button("Sign In", use_container_width=True)
            
            if submitted:
                result = supabase_client.sign_in_with_password(email, password)
                if "error" in result:
                    st.session_state.auth_error = result["error"]
                else:
                    st.session_state.access_token  = result["access_token"]
                    st.session_state.refresh_token = result["refresh_token"]
                    st.session_state.user_id       = result["user_id"]
                    st.session_state.user_email    = result["email"]
                    st.session_state.current_view   = 'landing'
                st.rerun()

        with tab_up:
            with st.form("signup_form", clear_on_submit=False):
                email_up = st.text_input("Email Address", key="signup_email", placeholder="name@example.com")
                password_up = st.text_input("Password (min 6 chars)", type="password", key="signup_pw", placeholder="••••••••")
                submitted_up = st.form_submit_button("Create Account", use_container_width=True)
            
            if submitted_up:
                result = supabase_client.sign_up_with_password(email_up, password_up)
                if "error" in result:
                    st.session_state.auth_error = result["error"]
                elif result.get("pending_confirmation"):
                    st.session_state.auth_info = (
                        f"Check your inbox — confirmation email sent to {result['email']}."
                    )
                else:
                    st.session_state.access_token  = result["access_token"]
                    st.session_state.refresh_token = result["refresh_token"]
                    st.session_state.user_id       = result["user_id"]
                    st.session_state.user_email    = result["email"]
                    st.session_state.current_view   = 'landing'
                st.rerun()

        st.markdown("<div style='text-align:center; margin: 12px 0; color:#6366f1; font-weight: 600;'>OR</div>", unsafe_allow_html=True)

        oauth = supabase_client.google_oauth_url()
        if "error" in oauth:
            st.caption(f"Google sign-in unavailable: {oauth['error']}")
        else:
            st.link_button(
                "🌐 Continue with Google",
                url=oauth["url"],
                use_container_width=True,
            )


# ── 1. SIDEBAR NAVIGATION ──
with st.sidebar:
    st.markdown("## Navigation")
    
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_view = 'landing'
        st.rerun()
    
    if st.button("🎯 ATS Scorer", use_container_width=True):
        st.session_state.current_view = 'scorer'
        st.rerun()
    
    if st.button("📊 History", use_container_width=True):
        st.session_state.current_view = 'history'
        st.rerun()
    
    if st.button("📚 Resources", use_container_width=True):
        st.session_state.current_view = 'resources'
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 👤 Account")

    from frontend.services import supabase_client

    if st.session_state.access_token:
        st.caption(f"Signed in as\n**{st.session_state.user_email}**")
        if st.button("Sign out", use_container_width=True):
            supabase_client.sign_out()
            for k in ("access_token", "refresh_token", "user_id", "user_email"):
                st.session_state[k] = None
            st.session_state.current_view = 'landing'
            st.rerun()
    else:
        st.caption("You are currently offline")
        if st.button("🔐 Sign In / Sign Up", use_container_width=True, type="primary"):
            st.session_state.current_view = 'auth'
            st.rerun()


# ── 2. MAIN CONTENT RENDERER ──
if st.session_state.current_view == 'auth':
    render_auth_view()

elif st.session_state.current_view == 'landing':
    if st.session_state.access_token:
        render_welcome_hero()
        
    from frontend.views import landing
    landing.render()

elif st.session_state.current_view == 'scorer':
    from frontend.views import scorer
    scorer.render()

elif st.session_state.current_view == 'history':
    from frontend.views import history
    history.render()

elif st.session_state.current_view == 'resources':
    from frontend.views import resources
    resources.render()