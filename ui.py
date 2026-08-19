import streamlit as st
from Fin_advisor import Fin_team

st.title("📈 Finance Advisor")

user_input = st.text_input(
    "Enter your stock comparison question:"
)

if st.button("Analyze"):
    if user_input:
        response = Fin_team.run(user_input)

        st.markdown(response.content)
    else:
        st.warning("Please enter a question.")