import json
import streamlit as st


def _render_component(*args, **kwargs):
    # TODO: add to results.elements
    # print("_render_component: ", kwargs)
    st._mock._results.element.append(kwargs)
    pass


def declare_component(*args, **kwargs):
    return _render_component


class components:
    def register_widget(*args, **kwargs):
        pass


def html(html, width=None, height=None, scrolling=False):
    st._mock._results.html.append(html)


def iframe(src, width=None, height=None, scrolling=False):
    st._mock._results.iframe.append(src)
