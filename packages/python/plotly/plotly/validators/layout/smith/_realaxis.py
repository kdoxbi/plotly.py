import _plotly_utils.basevalidators


class RealaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="realaxis", parent_name="layout.smith", **kwargs):
        super(RealaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Realaxis"),
            **kwargs,
        )
