import streamlit as st


def main():
    st.title("A calculator")
    x = st.number_input("X", key="x_input")
    y = st.number_input("Y", key="y_input")
    if st.button("Add", key="add_button"):
        st.write(f"{x} + {y} = {x + y}")
    if st.button("Subtract", key="subtract_button"):
        st.write(f"{x} - {y} = {x - y}")


main()
