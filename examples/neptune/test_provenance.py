import re

import streamlit_mock

import common


def test_provenance_initial_page_display():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟦 Provenance"

    results = common.run(sm)

    assert results.title == ["JSON File Provenance"]
    assert results.changeable == ["select_page_radio", "provenance_file"]
    print(results)


def test_provenance_after_upload():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟦 Provenance"

    results = common.run(sm)

    assert results.title == ["JSON File Provenance"]
    assert results.changeable == ["select_page_radio", "provenance_file"]
    print(results)