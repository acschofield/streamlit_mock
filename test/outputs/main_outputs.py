import streamlit as st
import bokeh.plotting
import pandas as pd


def main():
    st.altair_chart(pd.DataFrame())
    st.area_chart(pd.DataFrame())
    st.bar_chart(pd.DataFrame())
    st.caption("caption")
    st.code("code")
    st.dataframe(pd.DataFrame())
    st.header("header")
    st.json({"key": "value"})
    st.latex(r"""\sum_{k=0}^{n-1} ar^k""")
    st.line_chart(pd.DataFrame())
    st.map(pd.DataFrame())
    st.markdown("markdown")
    st.subheader("subheader")
    st.table(pd.DataFrame())
    st.text("text")
    st.title("Output examples")

    x = [1, 2, 3]
    y = [1, 4, 9]

    p = bokeh.plotting.figure()

    p.line([1, 2, 3], [1, 4, 9])

    st.bokeh_chart(p)

    st.graphviz_chart(
        """
        digraph {
            run -> stop
        }
    """
    )


main()
