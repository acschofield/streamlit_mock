import streamlit.mock as mock


_mock = mock.Mock()
session_state = _mock.session_state

button = _mock.button
camera_input = _mock.camera_input
checkbox = _mock.checkbox
color_picker = _mock.color_picker
columns = _mock.columns
container = _mock.container
date_input = _mock.date_input
download_button = _mock.download_button
empty = _mock.empty
expander = _mock.expander
file_uploader = _mock.file_uploader
form = _mock.form
form_submit_button = _mock.form_submit_button
image = _mock.image
markdown = _mock.markdown
multiselect = _mock.multiselect
number_input = _mock.number_input
radio = _mock.radio
selectbox = _mock.selectbox
select_slider = _mock.select_slider
sidebar = _mock
slider = _mock.slider
tabs = _mock.tabs
text_area = _mock.text_area
text_input = _mock.text_input
time_input = _mock.time_input
title = _mock.title
write = _mock.write


def experimental_memo(func=None, *, persist=None, show_spinner=True, suppress_st_warning=False, max_entries=None, ttl=None):
    def inner(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return inner


def cache(suppress_st_warning=False):
    def inner(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return inner


def set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None):
    pass


def experimental_get_query_params():
    return {}


def experimental_set_query_params(**kwargs):
    pass


def stop(**kwargs):
    pass
