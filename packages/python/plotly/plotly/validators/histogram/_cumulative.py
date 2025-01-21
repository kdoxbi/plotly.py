import _plotly_utils.basevalidators


class CumulativeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="cumulative", parent_name="histogram", **kwargs):
        super(CumulativeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cumulative"),
            **kwargs,
        )
