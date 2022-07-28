import sys

sys.path.insert(0, "/home/andrew/streamlit-mock")

import streamlit as st

st.session_state.radio = "Two"

import Main

print(st._mock._results)
