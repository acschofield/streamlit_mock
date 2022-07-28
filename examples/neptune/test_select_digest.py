import common

import streamlit_mock


def test_select_digest_with_no_selection():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"

    results = common.run(sm)
    assert results.widget_labels == ["Select page", "Digest", "Enter a condition to select a subset of digest documents", "Select"]


def test_select_digest_avsi():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"
    session_state.select_digest_digest_name = "avsi"
    session_state["FormSubmitter:digest_selection_form-Select"] = True

    results = common.run(sm)
    assert results.dataframe[0].iloc[0]["name"] == "chapter"
    assert session_state.selected_digest_count == 66
    assert len(session_state.selected_digest_metadata["metadata"]) == 2


def test_select_digest_common():
    session_state = common.select_digest("avsi")
    assert session_state.selected_digest_count == 66
