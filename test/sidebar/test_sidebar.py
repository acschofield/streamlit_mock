import streamlit_mock


def test_sidebar_one():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.radio = "One"

    results = sm.run("main_sidebar.py")

    results = sm.get_results()
    assert results.title == ["A sidebar example", "Page one"]


def test_sidebar_two():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.radio = "Two"

    results = sm.run("main_sidebar.py")

    results = sm.get_results()
    assert results.title == ["A sidebar example", "Page two"]
