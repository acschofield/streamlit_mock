import streamlit_mock


def test_bulbasaur():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    # session_state.pokemon = "Bulbasaur"

    sm.run("main.py")

    results = sm.get_results()
    assert str(results.image) == "['bulbasaur.png']"


def test_ivysaur():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.pokemon = "Ivysaur"

    sm.run("main.py")

    results = sm.get_results()
    assert str(results.image) == "['ivysaur.png']"
