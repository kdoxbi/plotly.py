import _plotly_utils.basevalidators


class RangefontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="rangefont", parent_name="parcoords", **kwargs):
        super(RangefontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rangefont"),
            **kwargs,
        )
