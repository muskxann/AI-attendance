import streamlit as st
from src.ui.base_layout import container_layout, dashboard_button, style_layout

style_layout()
dashboard_button()
def subject_card(code,name,section,stats=None,footer_clb=None):
    with st.container(border=True, ):
        st.subheader(name)
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Code:{code}")
            st.write(f'{stats[0][0]}:{stats[0][1]}')
        with col2:
            st.write(f"Section:{section}")
            st.write(f'{stats[1][0]}:{stats[1][1]}')

    with st.container():
        if footer_clb:
            footer_clb()
