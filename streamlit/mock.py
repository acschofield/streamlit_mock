import addict


class DictNoDefault(addict.Dict):
    def __missing__(self, key):
        raise KeyError(key)


class Mock:
    def __init__(self):
        self.session_state = DictNoDefault()
        self._results = DictNoDefault()
        self._results.form = []
        self._results.image = []
        self._results.markdown = []
        self._results.title = []
        self._results.widget_labels = []
        self._results.write = []

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        pass

    def _handle_changeable(self, label, key, initial_value, on_change, args, kwargs):
        self._results.widget_labels.append(label)
        value = self.session_state.get(key, initial_value)
        if value != initial_value and on_change:
            optional_args = args if args else []
            optional_kwargs = kwargs if kwargs else {}
            on_change(*optional_args, **optional_kwargs)
        return value

    def _handle_clickable(self, label, key, on_click, args, kwargs):
        self._results.widget_labels.append(label)
        value = self.session_state.get(key, False)
        if value and on_click:
            optional_args = args if args else []
            optional_kwargs = kwargs if kwargs else {}
            on_click(*optional_args, **optional_kwargs)
        return value

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

    def color_picker(self, label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def columns(self, spec, gap="small"):
        count = spec if isinstance(spec, int) else len(spec)
        return [self] * count

    def container(self):
        return self

    def date_input(self, label, value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_changeable(label, key, value, on_change, args, kwargs)

    def download_button(self, label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False):
        return self._handle_clickable(label, key, on_click, args, kwargs)

    def empty(self):
        return self

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

    def image(self, image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto"):
        self._results.image.append(image)

    def markdown(self, body, unsafe_allow_html=False):
        self._results.markdown.append(body)

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

    def tabs(self, tabs):
        return [self] * len(tabs)

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

    def write(self, *args, **kwargs):
        self._results.write += args
