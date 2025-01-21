import _plotly_utils.basevalidators


class MeanlineValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="meanline", parent_name="violin", **kwargs):
        super(MeanlineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Meanline"),
            **kwargs,
        )
