import streamlit as st


def _footer():
    st.markdown(
        """
        <div style="margin-top:42px; padding-top:18px; border-top:1px solid #E2E8F0;
                    text-align:center; color:#64748B; font-size:12px;">
            Intelligent AI Attendance &nbsp;•&nbsp; Face Recognition + Voice Recognition
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_home():
    _footer()


def footer_dashboard():
    _footer()
