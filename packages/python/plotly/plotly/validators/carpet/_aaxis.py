import _plotly_utils.basevalidators


class AaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="aaxis", parent_name="carpet", **kwargs):
        super(AaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Aaxis"),
            **kwargs,
        )
