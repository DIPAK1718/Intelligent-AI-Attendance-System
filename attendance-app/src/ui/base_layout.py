import streamlit as st


PRIMARY = "#3157D5"
PRIMARY_DARK = "#1F3FA8"
ACCENT = "#16A6A0"
BG = "#F5F7FB"
TEXT = "#172033"
MUTED = "#64748B"
BORDER = "#E2E8F0"


def style_background_home():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                radial-gradient(circle at 8% 8%, rgba(49,87,213,.10), transparent 28%),
                radial-gradient(circle at 92% 18%, rgba(22,166,160,.09), transparent 25%),
                {BG};
        }}
        .block-container {{ max-width: 1180px !important; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                radial-gradient(circle at 100% 0%, rgba(49,87,213,.07), transparent 24%),
                {BG};
        }}
        .block-container {{ max-width: 1180px !important; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        #MainMenu, footer, header {{ visibility: hidden; }}
        .block-container {{
            padding-top: 1.2rem !important;
            padding-bottom: 2rem !important;
        }}

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif !important;
            color: {TEXT};
        }}

        h1, h2, h3, h4 {{
            font-family: 'Inter', sans-serif !important;
            color: {TEXT} !important;
            font-weight: 800 !important;
            letter-spacing: -0.025em;
        }}
        h1 {{ font-size: 2.35rem !important; }}
        h2 {{ font-size: 1.7rem !important; }}
        h3 {{ font-size: 1.25rem !important; }}
        p, label, .stMarkdown {{ color: {TEXT}; }}

        /* Modern Streamlit buttons */
        .stButton > button {{
            border-radius: 12px !important;
            min-height: 44px !important;
            padding: 0.55rem 1rem !important;
            font-weight: 700 !important;
            border: 1px solid {BORDER} !important;
            box-shadow: 0 2px 7px rgba(15,23,42,.05) !important;
            transition: all .18s ease !important;
        }}
        .stButton > button:hover {{
            transform: translateY(-1px);
            box-shadow: 0 7px 18px rgba(15,23,42,.10) !important;
        }}
        .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, {PRIMARY}, {PRIMARY_DARK}) !important;
            color: white !important;
            border-color: transparent !important;
        }}
        .stButton > button[kind="secondary"] {{
            background: white !important;
            color: {PRIMARY_DARK} !important;
            border-color: #C9D4F4 !important;
        }}
        .stButton > button[kind="tertiary"] {{
            background: #EEF2F7 !important;
            color: #334155 !important;
            border-color: transparent !important;
        }}

        /* Inputs */
        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div,
        div[data-baseweb="textarea"] > div {{
            border-radius: 11px !important;
            border-color: {BORDER} !important;
            background: white !important;
        }}
        div[data-baseweb="input"] > div:focus-within,
        div[data-baseweb="select"] > div:focus-within,
        div[data-baseweb="textarea"] > div:focus-within {{
            border-color: #9DB0EA !important;
            box-shadow: 0 0 0 2px rgba(49,87,213,.10) !important;
        }}

        /* Dividers */
        hr {{ border-color: {BORDER} !important; }}

        /* Streamlit alerts */
        div[data-testid="stAlert"] {{ border-radius: 12px !important; }}

        /* Dialog */
        div[role="dialog"] {{
            border-radius: 20px !important;
            border: 1px solid {BORDER} !important;
            box-shadow: 0 24px 70px rgba(15,23,42,.18) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
