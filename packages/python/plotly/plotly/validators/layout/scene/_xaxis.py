import _plotly_utils.basevalidators


class XaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="xaxis", parent_name="layout.scene", **kwargs):
        super(XaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "XAxis"),
            **kwargs,
        )
