import datetime

import streamlit_mock


def test_input_widgets():
    sm = streamlit_mock.StreamlitMock()

    sm.run("main_outputs.py")

    results = sm.get_results()

    assert results.title == ["Output examples"]

    assert results.markdown == ["markdown"]
    assert results.header == ["header"]
    assert results.subheader == ["subheader"]
    assert results.caption == ["caption"]
    assert results.code == ["code"]
    assert results.text == ["text"]
    assert results.latex == [r"""\sum_{k=0}^{n-1} ar^k"""]
    assert len(results.dataframe) == 1
    assert len(results.table) == 1
    assert results.json == [{"key": "value"}]
    assert len(results.bokeh_chart) == 1
    assert len(results.line_chart) == 1
    assert len(results.area_chart) == 1
    assert len(results.bar_chart) == 1
    assert len(results.map) == 1
    assert len(results.graphviz_chart) == 1
