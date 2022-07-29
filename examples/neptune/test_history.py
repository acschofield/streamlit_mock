import re

import streamlit_mock

import common


def test_history_initial_page_display():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "⬛ History and Job Control"

    results = common.run(sm)

    assert results.title == ["History and Job Control"]
    assert results.subheader == ["Job Control", "Job History"]
    assert results.changeable == ["select_page_radio", "job_control_radio"]
    assert results.clickable == ["history_refresh"]
    assert len(results.aggrid) == 1
    for column in ["Job Id", "Service", "Status", "Owner", "Retain", "Notes"]:
        assert column in results.aggrid[0].columns


def test_history_first_row_selected():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "⬛ History and Job Control"
    session_state.history_aggrid = {"selected": 0}

    results = common.run(sm)
    assert results.clickable == ["history_refresh", "history_display", "history_retrieve_log", "history_remove"]
