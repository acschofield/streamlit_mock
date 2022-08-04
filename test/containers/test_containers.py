import streamlit_mock


def test_containers_and_layouts():
    sm = streamlit_mock.StreamlitMock()
    session_state = sm.get_session_state()
    sm.run("main_container.py")

    results = sm.get_results()

    assert results.write == [
        "in expander #1",
        "in nested containers",
        "in container without context",
        "column 1",
        "column 2",
        "column 3",
        "column 4",
        "tab A",
        "tab B",
        "empty",
    ]
    assert results.widget_labels == ["Expander #1", "Expander #2"]
