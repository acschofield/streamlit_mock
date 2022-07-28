import streamlit as st


def main():
    st.title("Input examples")
    st.write(st.button("Button", key="button"))
    st.write(st.download_button("Download some text", """some text""", key="download_button"))
    st.write(st.checkbox("Checkbox", key="checkbox"))
    st.write(st.radio("Radio", ["One", "Two"], key="radio"))
    st.write(st.selectbox("Selectbox", ["One", "Two"], key="selectbox"))
    st.write(st.multiselect("Multiselect", ["One", "Two"], key="multiselect"))
    st.write(st.slider("Slider", key="slider"))
    st.write(st.select_slider("Select slider", [1, 2, 3], key="select_slider"))
    st.write(st.text_input("Text input", key="text_input"))
    st.write(st.number_input("Number input", key="number_input"))
    st.write(st.text_area("Text area", key="text_area"))
    st.write(st.date_input("Date input", key="date_input"))
    st.write(st.time_input("Time input", key="time_input"))
    st.write(st.file_uploader("File uploader", key="file_uploader"))
    st.write(st.camera_input("Camera input", key="camera_input"))
    st.write(st.color_picker("Color picker", key="color_picker"))


main()
