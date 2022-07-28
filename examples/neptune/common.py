import addict

import streamlit_mock


def run(sm):
    results = sm.run("Main.py", ["--user", "test@example.com", "--launcher", "localhost:50061", "--environment", "environment.json"])
    return results


def select_digest(name):
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    session_state.select_page_radio = "🟥 Select digest"
    session_state.select_digest_digest_name = name
    session_state["FormSubmitter:digest_selection_form-Select"] = True

    results = run(sm)
    assert session_state.selected_digest_count > 0
    result = addict.Dict(session_state)
    return result
