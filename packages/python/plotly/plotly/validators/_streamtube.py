import _plotly_utils.basevalidators


class StreamtubeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="streamtube", parent_name="", **kwargs):
        super(StreamtubeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Streamtube"),
            **kwargs,
        )
