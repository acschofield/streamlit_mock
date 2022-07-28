import re
import os

import streamlit_mock


def test_simple_login():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    sm.run("Main.py", ["--user", "test@example.com", "--environment", "environment.json"])

    results = sm.get_results()
    assert re.search("test@example.com", " ".join(results.write))
    assert re.search("Neptune User Manual", " ".join(results.markdown))


def test_select_digest():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"
    sm.run("Main.py", ["--user", "test@example.com", "--launcher", "localhost:50061", "--environment", "environment.json"])

    results = sm.get_results()
    print(results)
    print(session_state)
    # assert re.search("test@example.com", " ".join(results.write))
    # assert re.search("Neptune User Manual", " ".join(results.markdown))
