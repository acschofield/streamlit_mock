import re

import streamlit_mock

import common


def test_elements_initial_page_display():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟪 Elements"

    results = common.run(sm)
    print(results)
