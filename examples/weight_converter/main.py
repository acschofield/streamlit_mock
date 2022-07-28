import streamlit as st


def _update(scale, from_key, to_key):
    st.session_state[to_key] = scale * st.session_state[from_key]


def main():
    st.title("Weight Converter")
    st.markdown("Enter a weight in either field, the other field will be automatically updated")
    st.number_input("Kilograms", on_change=_update, args=[2.20462, "kilograms", "pounds"], key="kilograms")
    st.number_input("Pounds", on_change=_update, args=[0.453592, "pounds", "kilograms"], key="pounds")


main()
