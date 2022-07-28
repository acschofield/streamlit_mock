import streamlit_mock


def test_kg_to_lb():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.kilograms = 10

    sm.run("main.py")

    assert session_state.pounds == 22.0462
    results = sm.get_results()
    assert results.title == ["Weight Converter"]
    assert results.markdown == ["Enter a weight in either field, the other field will be automatically updated"]
    assert results.widget_labels == ["Kilograms", "Pounds"]


def test_lb_to_kg():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.pounds = 10

    sm.run("main.py")
    assert session_state.kilograms == 4.53592
