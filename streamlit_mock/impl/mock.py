import addict
import contextlib


class DictNoDefault(addict.Dict):
    def __missing__(self, key):
        raise KeyError(key)


class Mock(object):
    def __init__(self):
        self.session_state = DictNoDefault()
        self._results = DictNoDefault()
        self._results.aggrid = []
        self._results.altair_chart = []
        self._results.altair_chart = []
        self._results.area_chart = []
        self._results.bar_chart = []
        self._results.bokeh_chart = []
        self._results.caption = []
        self._results.changeable = []
        self._results.clickable = []
        self._results.code = []
        self._results.dataframe = []
        self._results.download = []
        self._results.element = []
        self._results.error = []
        self._results.form = []
        self._results.graphviz_chart = []
        self._results.header = []
        self._results.html = []
        self._results.iframe = []
        self._results.image = []
        self._results.info = []
        self._results.json = []
        self._results.latex = []
        self._results.line_chart = []
        self._results.map = []
        self._results.markdown = []
        self._results.plotly_chart = []
        self._results.progress = []
        self._results.pydeck_chart = []
        self._results.pyplot = []
        self._results.spinner = []
        self._results.subheader = []
        self._results.success = []
        self._results.table = []
        self._results.text = []
        self._results.title = []
        self._results.vega_lite_chart = []
        self._results.warning = []
        self._results.widget_labels = []
        self._results.write = []

    def altair_chart(self, altair_chart, use_container_width=False):
        self._results.altair_chart.append(altair_chart)

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        pass

    def _handle_changeable(self, label, key, initial_value, on_change, args, kwargs):
        self._results.widget_labels.append(label)
        self._results.changeable.append(key)
        value = self.session_state.get(key, initial_value)
        if value != initial_value and on_change:
            optional_args = args if args else []
            optional_kwargs = kwargs if kwargs else {}
            on_change(*optional_args, **optional_kwargs)
        return value

    def _handle_clickable(self, label, key, on_click, args, kwargs):
        self._results.widget_labels.append(label)
        self._results.clickable.append(key)
        value = self.session_state.get(key, False)
        if value and on_click:
            optional_args = args if args else []
            optional_kwargs = kwargs if kwargs else {}
            on_click(*optional_args, **optional_kwargs)
        if key:
            self.session_state[key] = False
        return value

    def altair_chart(self, altair_chart, use_container_width=False):
        self._results.altair_chart.append(altair_chart)

    def area_chart(self, data=None, use_container_width=False):
        self._results.area_chart.append(data)

    def bar_chart(self, data=None, use_container_width=False):
        self._results.bar_chart.append(data)

    def bokeh_chart(self, figure, use_container_width=False):
        self._results.bokeh_chart.append(figure)

    def button(
        self,
        label,
        key=None,
        help=None,
        on_click=None,
        args=None,
        kwargs=None,
        *,
        disabled=False,
    ):
        return self._handle_clickable(label, key, on_click, args, kwargs)

    def camera_input(self, label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, None, on_change, args, kwargs)

    def checkbox(self, label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def caption(self, body, unsafe_allow_html=False):
        self._results.caption.append(body)

    def code(self, body, language="python"):
        self._results.code.append(body)

    def color_picker(self, label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def columns(self, spec, gap="small"):
        count = spec if isinstance(spec, int) else len(spec)
        return [self] * count

    def container(self):
        return self

    def dataframe(self, data=None, width=None, height=None):
        self._results.dataframe.append(data)

    def date_input(self, label, value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def download_button(self, label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False):
        self._results.download.append({"data": data, "file_name": file_name, "mime": mime, "key": key})
        return self._handle_clickable(label, key, on_click, args, kwargs)

    def empty(self):
        return self

    def error(self, body):
        self._results.error.append(body)

    def expander(self, label, expanded=False):
        self._results.widget_labels.append(label)
        return self

    def file_uploader(self, label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, None, on_change, args, kwargs)

    def form(self, name):
        self._results.form.append(name)
        return self

    def form_submit_button(
        self,
        label,
        help=None,
        on_click=None,
        args=None,
        kwargs=None,
    ):
        key = "FormSubmitter:" + self._results.form[-1] + "-" + label
        return self._handle_clickable(label, key, on_click, args, kwargs)

    def graphviz_chart(self, figure_or_dot, use_container_width=False):
        self._results.graphviz_chart.append(figure_or_dot)

    def header(self, body, anchor=None):
        self._results.header.append(body)

    def image(self, image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto"):
        self._results.image.append(image)

    def info(self, body):
        self._results.info.append(body)

    def json(self, body, expanded=True):
        self._results.json.append(body)

    def latex(self, body):
        self._results.latex.append(body)

    def line_chart(self, data=None, use_container_width=False):
        self._results.line_chart.append(data)

    def map(self, data=None, zoom=None, use_container_width=True):
        self._results.map.append(data)

    def markdown(self, body, unsafe_allow_html=False):
        self._results.markdown.append(body)

    def progress(self, body):
        self._results.progress.append(body)

    def multiselect(
        self,
        label,
        options,
        default=None,
        format_func=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        disabled=False,
    ):
        return self._handle_changeable(label, key, default, on_change, args, kwargs)

    def number_input(
        self,
        label,
        min_value=None,
        max_value=None,
        value=None,
        step=None,
        format=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        disabled=False,
    ):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def plotly_chart(self, figure_or_data, use_container_width=False, sharing="streamlit", **kwargs):
        self._results.plotly_chart.append(figure_or_data)

    def pydeck_chart(self, pydeck_obj=None, use_container_width=False):
        self._results.pydeck_chart.append(pydeck_obj)

    def pyplot(self, fig=None, clear_figure=None, **kwargs):
        self._results.pyplot.append(fig)

    def radio(
        self, label, options, index=0, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False
    ):
        return self._handle_changeable(label, key, list(options)[index], on_change, args, kwargs)

    def select_slider(
        self,
        label,
        options=(),
        value=None,
        format_func=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        disabled=False,
    ):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def selectbox(self, label, options, index=0, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, list(options)[index], on_change, args, kwargs)

    def slider(
        self,
        label,
        min_value=None,
        max_value=None,
        value=None,
        step=None,
        format=None,
        key=None,
        help=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        disabled=False,
    ):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    @contextlib.contextmanager
    def spinner(self, text="In progress..."):
        self._results.spinner.append(text)
        resource = {}
        try:
            yield resource
        except:
            pass

    def success(self, body):
        self._results.success.append(body)

    def subheader(self, body, anchor=None):
        self._results.subheader.append(body)

    def table(self, data=None):
        self._results.table.append(data)

    def tabs(self, tabs):
        return [self] * len(tabs)

    def text(self, body):
        self._results.text.append(body)

    def text_area(
        self, label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False
    ):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def text_input(
        self,
        label,
        value="",
        max_chars=None,
        key=None,
        type="default",
        help=None,
        autocomplete=None,
        on_change=None,
        args=None,
        kwargs=None,
        *,
        placeholder=None,
        disabled=False,
    ):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def time_input(self, label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def title(self, body, anchor=None):
        self._results.title.append(body)

    def vega_lite_chart(self, data=None, spec=None, use_container_width=False, **kwargs):
        self._results.vega_lite_chart.append(data)

    def warning(self, body):
        self._results.warning.append(body)

    def write(self, *args, **kwargs):
        self._results.write += args
