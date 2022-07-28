import re
import os

import smart_open

import streamlit_mock


def run(sm):
    results = sm.run("Main.py", ["--user", "test@example.com", "--launcher", "localhost:50061", "--environment", "environment.json"])
    return results


def test_simple_login():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()

    results = run(sm)

    assert re.search("test@example.com", " ".join(results.write))
    assert re.search("Neptune User Manual", " ".join(results.markdown))


def test_select_digest_with_no_selection():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"

    results = run(sm)
    assert results.widget_labels == ["Select page", "Digest", "Enter a condition to select a subset of digest documents", "Select"]


def test_select_digest_avsi():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"
    session_state.select_digest_digest_name = "avsi"
    session_state["FormSubmitter:digest_selection_form-Select"] = True

    results = run(sm)
    assert results.dataframe[0].iloc[0]["name"] == "chapter"
    assert session_state.selected_digest_count == 66
    assert len(session_state.selected_digest_metadata["metadata"]) == 2
