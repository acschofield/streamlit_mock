import sys
import pathlib
import importlib
import re
import io
import os

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()))
import streamlit as st
import impl.utils


imported = {}


class UploadedFile(io.BytesIO):
    def __init__(self, upload_filename, test_filename):
        path = pathlib.Path(test_filename).parent.resolve() / pathlib.Path(upload_filename)
        self.name = str(path)
        with open(path, mode="rb") as f:
            content = f.read()
        super(UploadedFile, self).__init__(content)
        pass


class StreamlitMock:
    def __init__(self):
        importlib.reload(st)
        self.session_state = st.session_state
        self.results = st._mock._results

    def get_session_state(self):
        return self.session_state

    def run(self, python_main, args=[]):
        sys.argv = [python_main] + args
        module_name = re.sub(r"\.py$", "", python_main).replace("/", ".")
        global imported
        while True:
            try:
                if module_name in imported:
                    importlib.reload(imported[module_name])
                else:
                    imported[module_name] = importlib.import_module(module_name)
                break
            except impl.utils.StreamlitStopException:
                break
            except impl.utils.StreamlitRerunException:
                continue

        return self.results

    def get_results(self):
        return self.results

    def set_uploaded_file(self, key, upload_filename, test_filename):
        self.session_state[key] = UploadedFile(upload_filename, test_filename="./test.py")
