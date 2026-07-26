import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sign In | ATS Resume Scorer", page_icon="🔐", layout="centered")

# Custom CSS for Modern Fancy UI
st.markdown("""
<style>
    /* Dark blue background for the whole page */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    }

    /* Hide default Streamlit sidebar on Auth page */
    [data-testid="stSidebar"] {
        display: none;
    }

    /* Centered Glassmorphism Card Container */
    .auth-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 20px;
    }

    .auth-header {
        font-size: 26px;
        font-weight: 800;
        color: #1e1b4b;
        margin-bottom: 8px;
    }

    .auth-sub {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 0px;
    }

    /* Make tab labels readable against the dark background */
    .stTabs [data-baseweb="tab-list"] {
        background: #ffffff;
        border-radius: 8px;
        padding: 6px;
    }

    /* Styled Input Fields & Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
        color: white;
        border-radius: 8px;
        padding: 12px;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Main Form Card (header + subtext wrapped inside the card so styling actually applies)
st.markdown("""
<div class="auth-card">
    <div class="auth-header">🔐 Welcome to ATS Resume Scorer</div>
    <div class="auth-sub">Sign in to analyze and optimize your resume</div>
</div>
""", unsafe_allow_html=True)

# Tabs for Sign In & Sign Up
tab_login, tab_signup = st.tabs(["🔑 Sign In", "✨ Create Account"])

with tab_login:
    with st.form("login_form"):
        email = st.text_input("Email Address", placeholder="name@example.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        submit = st.form_submit_button("Sign In to Workspace")

        if submit:
            if email and password:
                st.session_state["logged_in"] = True
                st.session_state["user_email"] = email
                st.success("Successfully logged in!")
                st.switch_page("pages/1_🏠_Home.py")  # Auto redirect after login
            else:
                st.error("Please enter valid credentials")

    st.markdown("---")
    if st.button("🌐 Continue with Google"):
        st.info("Google OAuth flow trigger here")

with tab_signup:
    with st.form("signup_form"):
        new_name = st.text_input("Full Name", placeholder="John Doe")
        new_email = st.text_input("Email Address", placeholder="name@example.com")
        new_pass = st.text_input("Create Password", type="password", placeholder="••••••••")
        signup_submit = st.form_submit_button("Create Account")

        if signup_submit:
            st.success("Account created successfully! Please Sign In.")