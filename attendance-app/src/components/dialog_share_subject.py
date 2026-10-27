import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    st.markdown("""
    <style>
    [data-testid="stDialog"] h1,
    [data-testid="stDialog"] h2,
    [data-testid="stDialog"] h3,
    [data-testid="stDialog"] p {
        color: #F8FAFC !important;
    }

    [data-testid="stDialog"] [data-testid="stAlert"] {
        color: #FFFFFF !important;
    }

    [data-testid="stDialog"] code {
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy this link to share on WhatsApp or Email")

    with col2:
        st.markdown("### Scan to Join")
        st.image(out.getvalue(), caption="QR code for class joining")