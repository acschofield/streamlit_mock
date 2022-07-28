import streamlit as st


def main():
    st.title("Containers")
    expander = st.expander("Expander #1")
    expander.write("in expander #1")

    with st.expander("Expander #2"):
        with st.container():
            with st.container():
                st.write("in nested containers")
    container = st.container()
    container.write("in container without context")

    col1, col2 = st.columns(2)
    col1.write("column 1")
    col2.write("column 2")

    col3, col4 = st.columns([1, 1])
    col3.write("column 3")
    col4.write("column 4")

    tab1, tab2 = st.tabs(["A", "B"])
    tab1.write("tab A")
    tab2.write("tab B")

    empty = st.empty()
    empty.write("empty")


main()
