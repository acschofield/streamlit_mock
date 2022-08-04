import streamlit as st
from streamlit_javascript import st_javascript
import datetime


def main():
    st.title("streamlit javascript")
    js = """[window.parent.innerHeight, window.parent.document.querySelector('[title="streamlit_javascript.streamlit_javascript"]').getBoundingClientRect()];"""
    return_value = st_javascript(js, key="abc")

    st.markdown(f"Return value was: {return_value}")

    st.write(type(return_value))

    if isinstance(return_value, list):
        st.components.v1.iframe("http://www.acme.com", height=return_value[0] - return_value[1]["y"] - 200)


main()
