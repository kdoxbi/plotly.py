import _plotly_utils.basevalidators


class StartsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="starts", parent_name="streamtube", **kwargs):
        super(StartsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Starts"),
            **kwargs,
        )
