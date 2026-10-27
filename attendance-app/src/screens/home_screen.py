import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def _portal_card(role, title, description, icon, button_label):
    st.markdown(
        f"""
        <div style="background:white; border:1px solid #E2E8F0; border-radius:22px;
                    padding:28px; min-height:205px; box-shadow:0 10px 30px rgba(15,23,42,.06);">
            <div style="width:52px; height:52px; border-radius:15px; background:#EEF2FF;
                        display:flex; align-items:center; justify-content:center; font-size:25px;">{icon}</div>
            <div style="font-size:22px; font-weight:800; margin-top:18px; color:#172033;">{title}</div>
            <div style="font-size:13px; color:#64748B; margin-top:7px; line-height:1.55;">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(button_label, type="primary", width="stretch", key=f"portal_{role}"):
        st.session_state["login_type"] = role
        st.rerun()


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    st.markdown(
        """
        <div style="text-align:center; margin:0 auto 30px; max-width:680px;">
            <div style="display:inline-block; background:#E8F7F6; color:#087F7A; padding:6px 11px;
                        border-radius:999px; font-size:12px; font-weight:700;">AI-POWERED ATTENDANCE</div>
            <div style="font-size:16px; color:#64748B; margin-top:12px; line-height:1.6;">
                Fast, contactless attendance using facial recognition and voice recognition.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        _portal_card(
            "student",
            "Student Portal",
            "Sign in with FaceID, view enrolled subjects and track your attendance.",
            "🎓",
            "Continue as Student →",
        )
    with col2:
        _portal_card(
            "teacher",
            "Teacher Portal",
            "Manage subjects and take classroom attendance using AI-powered recognition.",
            "👨‍🏫",
            "Continue as Teacher →",
        )

    st.markdown(
        """
        <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:24px;">
            <span style="background:white; border:1px solid #E2E8F0; padding:8px 12px; border-radius:10px; font-size:12px; color:#475569;">◉ Face Recognition</span>
            <span style="background:white; border:1px solid #E2E8F0; padding:8px 12px; border-radius:10px; font-size:12px; color:#475569;">◉ Voice Recognition</span>
            <span style="background:white; border:1px solid #E2E8F0; padding:8px 12px; border-radius:10px; font-size:12px; color:#475569;">◉ Cloud Records</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    footer_home()
