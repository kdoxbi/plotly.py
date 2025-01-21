import _plotly_utils.basevalidators


class CapsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="caps", parent_name="volume", **kwargs):
        super(CapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Caps"),
            **kwargs,
        )
