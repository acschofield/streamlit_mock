import streamlit as st


def main():
    st.title("A sidebar example")
    with st.sidebar:
        radio = st.radio("Select page", ["One", "Two"], key="radio")
    if radio == "One":
        st.title("Page one")
    else:
        st.title("Page two")


main()
