import datetime

import streamlit_mock


def test_input_widgets():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.button = "True"
    session_state.download_button = "True"
    session_state.checkbox = "True"
    session_state.radio = "One"
    session_state.selectbox = "Two"
    session_state.multiselect = ["One", "Two"]
    session_state.slider = 42
    session_state.select_slider = 2
    session_state.text_area = "Some text_area data"
    session_state.text_input = "Some text_input data"
    session_state.select_slider = 2
    session_state.number_input = 42.42
    session_state.date_input = datetime.date(2022, 7, 10)
    session_state.time_input = datetime.time(21, 43)
    session_state.file_uploader = None
    session_state.camera_input = None
    session_state.color_picker = "#123456"

    sm.run("main_inputs.py")

    results = sm.get_results()

    assert results.title == ["Input examples"]

    assert results.widget_labels == [
        "Button",
        "Download some text",
        "Checkbox",
        "Radio",
        "Selectbox",
        "Multiselect",
        "Slider",
        "Select slider",
        "Text input",
        "Number input",
        "Text area",
        "Date input",
        "Time input",
        "File uploader",
        "Camera input",
        "Color picker",
    ]

    assert results.write == [
        "True",
        "True",
        "True",
        "One",
        "Two",
        ["One", "Two"],
        42,
        2,
        "Some text_input data",
        42.42,
        "Some text_area data",
        datetime.date(2022, 7, 10),
        datetime.time(21, 43),
        None,
        None,
        "#123456",
    ]
