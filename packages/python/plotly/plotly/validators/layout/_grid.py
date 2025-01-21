import _plotly_utils.basevalidators


class GridValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="grid", parent_name="layout", **kwargs):
        super(GridValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Grid"),
            **kwargs,
        )
