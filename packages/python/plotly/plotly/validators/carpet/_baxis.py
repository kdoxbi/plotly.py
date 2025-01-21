import _plotly_utils.basevalidators


class BaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="baxis", parent_name="carpet", **kwargs):
        super(BaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Baxis"),
            **kwargs,
        )
