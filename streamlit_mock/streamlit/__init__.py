import impl.mock
import impl.utils


_mock = impl.mock.Mock()
session_state = _mock.session_state

altair_chart = _mock.altair_chart
area_chart = _mock.area_chart
bar_chart = _mock.bar_chart
bokeh_chart = _mock.bokeh_chart
button = _mock.button
camera_input = _mock.camera_input
caption = _mock.caption
checkbox = _mock.checkbox
code = _mock.code
color_picker = _mock.color_picker
columns = _mock.columns
container = _mock.container
dataframe = _mock.dataframe
date_input = _mock.date_input
download_button = _mock.download_button
empty = _mock.empty
error = _mock.error
expander = _mock.expander
file_uploader = _mock.file_uploader
form = _mock.form
form_submit_button = _mock.form_submit_button
graphviz_chart = _mock.graphviz_chart
header = _mock.header
image = _mock.image
info = _mock.info
json = _mock.json
latex = _mock.latex
line_chart = _mock.line_chart
map = _mock.map
markdown = _mock.markdown
multiselect = _mock.multiselect
number_input = _mock.number_input
plotly_chart = _mock.plotly_chart
progress = _mock.progress
pydeck_chart = _mock.pydeck_chart
pyplot = _mock.pyplot
radio = _mock.radio
select_slider = _mock.select_slider
selectbox = _mock.selectbox
sidebar = _mock
slider = _mock.slider
spinner = _mock.spinner
subheader = _mock.subheader
success = _mock.success
table = _mock.table
tabs = _mock.tabs
text = _mock.text
text_area = _mock.text_area
text_input = _mock.text_input
time_input = _mock.time_input
title = _mock.title
vega_lite_chart = _mock.vega_lite_chart
warning = _mock.warning
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
    raise impl.utils.StreamlitStopException()


def experimental_rerun(**kwargs):
    raise impl.utils.StreamlitRerunException()
