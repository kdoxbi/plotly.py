import _plotly_utils.basevalidators


class CellsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="cells", parent_name="table", **kwargs):
        super(CellsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cells"),
            **kwargs,
        )
