import _plotly_utils.basevalidators


class CandlestickValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="candlestick", parent_name="", **kwargs):
        super(CandlestickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Candlestick"),
            **kwargs,
        )
