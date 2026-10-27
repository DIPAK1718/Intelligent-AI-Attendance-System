import streamlit as st


def _brand(marketing=False):
    size = "72px" if marketing else "52px"
    title = "INTELLIGENT AI ATTENDANCE" if marketing else "AI ATTENDANCE"
    subtitle = "Face + Voice powered attendance" if marketing else "Smart Attendance System"
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px; margin:{'18px 0 28px' if marketing else '4px 0 8px'};">
            <div style="width:{size}; height:{size}; min-width:{size}; border-radius:18px;
                        background:linear-gradient(135deg,#3157D5,#16A6A0);
                        display:flex; align-items:center; justify-content:center;
                        color:white; font-size:{'24px' if marketing else '18px'}; font-weight:800;
                        box-shadow:0 10px 24px rgba(49,87,213,.20);">AI</div>
            <div>
                <div style="font-size:{'25px' if marketing else '20px'}; font-weight:800; color:#172033; letter-spacing:-.6px;">{title}</div>
                <div style="font-size:13px; color:#64748B; margin-top:3px;">{subtitle}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header_home():
    _brand(marketing=True)


def header_dashboard():
    _brand(marketing=False)
