import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""

    if stats:
        chips = []
        for icon, label, value in stats:
            chips.append(
                f'''<span style="display:inline-flex; align-items:center; gap:5px;
                background:#263449; padding:7px 10px; border-radius:10px;
                color:#CBD5E1; font-size:12px;">
                {icon} <b style="color:#FFFFFF;">{value}</b> {label}</span>'''
            )

        stats_html = '<div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:16px;">' + ''.join(chips) + '</div>'

    st.markdown(
        f"""
        <div style="background:#182235; border:1px solid #334155; border-radius:18px;
                    padding:20px; margin-bottom:10px; box-shadow:0 6px 20px rgba(0,0,0,.15);
                    border-top:4px solid #6385FF;">
            <div style="font-size:18px; font-weight:800; color:#F8FAFC;">{name}</div>
            <div style="margin-top:9px; color:#CBD5E1; font-size:13px;">
                <span style="background:#263B70; color:#C7D5FF; padding:5px 8px; border-radius:7px; font-weight:700;">{code}</span>
                <span style="margin-left:8px;">Section {section}</span>
            </div>
            {stats_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if footer_callback:
        footer_callback()