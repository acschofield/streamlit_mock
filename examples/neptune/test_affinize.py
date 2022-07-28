import common

import streamlit_mock


def test_affinize_no_input():
    select_digest_session_state = common.select_digest("avsi")
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.update(select_digest_session_state)
    session_state.select_page_radio = "🟥 Affinitize"

    results = common.run(sm)
    assert results.form == ["affinitize_form"]
    assert results.widget_labels == ["Select page", "Metadata name", "Text", "Display raw components", "Notes", "Retain", "Affinitize"]
    assert " ".join(results.text).find("66 documents currently selected from 'avsi'") >= 0


def test_affinize_no_text_specified():
    select_digest_session_state = common.select_digest("avsi")
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.update(select_digest_session_state)
    session_state.select_page_radio = "🟥 Affinitize"
    session_state["FormSubmitter:affinitize_form-Affinitize"] = True

    results = common.run(sm)
    assert results.error == ["No text specified"]


def test_affinize_avsi():
    select_digest_session_state = common.select_digest("avsi")
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.update(select_digest_session_state)
    session_state.select_page_radio = "🟥 Affinitize"
    session_state.affinitize_metadata = "topic"
    session_state.affinitize_text = "electrons and neutrons are fundamental particles"
    session_state.notes = "mock streamlit affinitize test"
    session_state["FormSubmitter:affinitize_form-Affinitize"] = True

    results = common.run(sm)

    print(results)
    assert len(results.dataframe) == 1
    assert len(results.altair_chart) == 1
    assert results.dataframe[0].iloc[4]["component"] > 0.5  # paerticle_physics
