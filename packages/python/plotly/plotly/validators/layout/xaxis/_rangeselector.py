import _plotly_utils.basevalidators


class RangeselectorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="rangeselector", parent_name="layout.xaxis", **kwargs
    ):
        super(RangeselectorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rangeselector"),
            **kwargs,
        )
