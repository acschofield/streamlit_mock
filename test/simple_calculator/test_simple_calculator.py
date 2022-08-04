import streamlit_mock


def test_add():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.x_input = 3
    session_state.y_input = 4
    session_state.add_button = True

    sm.run("main_simple_calculator.py")

    results = sm.get_results()
    assert results.title == ["A calculator"]
    assert results.widget_labels == ["X", "Y", "Add", "Subtract"]
    assert results.write == ["3 + 4 = 7"]


def test_subtract():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.x_input = 3
    session_state.y_input = 4
    session_state.subtract_button = True

    sm.run("main_simple_calculator.py")

    results = sm.get_results()
    assert results.write == ["3 - 4 = -1"]
