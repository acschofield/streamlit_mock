import streamlit as st


class GridUpdateMode:
    NO_UPDATE = 0b0000
    MANUAL = 0b0001
    VALUE_CHANGED = 0b0010
    SELECTION_CHANGED = 0b0100
    FILTERING_CHANGED = 0b1000
    SORTING_CHANGED = 0b10000
    MODEL_CHANGED = 0b11111


class DataReturnMode:
    AS_INPUT = 0
    FILTERED = 1
    FILTERED_AND_SORTED = 2


def AgGrid(
    dataframe,
    gridOptions=None,
    height=400,
    width=None,
    fit_columns_on_grid_load=False,
    update_mode="value_changed",
    data_return_mode="as_input",
    allow_unsafe_jscode=False,
    enable_enterprise_modules=False,
    license_key=None,
    try_to_convert_back_to_original_types=True,
    conversion_errors="coerce",
    reload_data=False,
    theme="light",
    custom_css=None,
    key=None,
    **default_column_parameters
):
    st._mock._results.aggrid.append(dataframe)
    if key in st.session_state and "selected" in st.session_state[key]:
        selected = st.session_state[key]["selected"]
        return {"data": dataframe, "selected_rows": [dataframe.iloc[selected].to_dict()]}
    return {"data": dataframe, "selected_rows": []}


class GridOptionsBuilder:
    def __init__(self):
        self.__grid_options = {}

    def from_dataframe(dataframe, **default_column_parameters):
        return GridOptionsBuilder()

    def configure_default_column(
        self, min_column_width=5, resizable=True, filterable=True, sorteable=True, editable=False, groupable=False, **other_default_column_properties
    ):
        pass

    def configure_auto_height(self, autoHeight=True):
        pass

    def configure_grid_options(self, **props):
        pass

    def configure_columns(self, column_names=[], **props):
        pass

    def configure_column(self, field, header_name=None, **other_column_properties):
        pass

    def configure_side_bar(self, filters_panel=True, columns_panel=True, defaultToolPanel=""):
        pass

    def configure_selection(
        self,
        selection_mode="single",
        use_checkbox=False,
        pre_selected_rows=None,
        rowMultiSelectWithClick=False,
        suppressRowDeselection=False,
        suppressRowClickSelection=False,
        groupSelectsChildren=True,
        groupSelectsFiltered=True,
    ):
        pass

    def configure_pagination(self, enabled=True, paginationAutoPageSize=True, paginationPageSize=10):
        pass

    def build(self):
        return self.__grid_options
