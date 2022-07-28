import streamlit as st


def main():
    st.title("A calculator using a form")
    with st.form("calculator_form"):
        x = st.number_input("X", key="x_input")
        y = st.number_input("Y", key="y_input")
        if st.form_submit_button("Add"):
            st.write(f"{x} + {y} = {x + y}")
        if st.form_submit_button("Subtract"):
            st.write(f"{x} - {y} = {x - y}")


main()
