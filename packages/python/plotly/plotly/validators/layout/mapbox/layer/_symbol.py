import _plotly_utils.basevalidators


class SymbolValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="symbol", parent_name="layout.mapbox.layer", **kwargs
    ):
        super(SymbolValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Symbol"),
            **kwargs,
        )
