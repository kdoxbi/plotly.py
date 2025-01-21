import _plotly_utils.basevalidators


class OhlcValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="ohlc", parent_name="", **kwargs):
        super(OhlcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Ohlc"),
            **kwargs,
        )
