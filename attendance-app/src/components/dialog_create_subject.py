import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):

    st.markdown(
        """
        <style>
        [data-testid="stDialog"] p {
            color: #D1D5DB !important;
            font-size: 15px !important;
        }

        [data-testid="stDialog"] label {
            color: #F9FAFB !important;
            font-size: 14px !important;
            font-weight: 600 !important;
        }

        [data-testid="stDialog"] input {
            color: #FFFFFF !important;
            background-color: #1F2937 !important;
            caret-color: #FFFFFF !important;
        }

        [data-testid="stDialog"] input::placeholder {
            color: #9CA3AF !important;
            opacity: 1 !important;
        }

        [data-testid="stDialog"] h2 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        [data-testid="stDialog"] button {
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Enter the details of new subject")

    sub_id = st.text_input(
        "Subject Code",
        placeholder="CS101"
    )

    sub_name = st.text_input(
        "Subject Name",
        placeholder="Introduction to Computer Science"
    )

    sub_section = st.text_input(
        "Section",
        placeholder="A"
    )

    if st.button(
        "Create Subject Now",
        type="primary",
        width="stretch"
    ):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(
                    sub_id,
                    sub_name,
                    sub_section,
                    teacher_id
                )
                st.toast("Subject Created Successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please fill all the fields")