import _plotly_utils.basevalidators


class CircleValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="circle", parent_name="layout.map.layer", **kwargs):
        super(CircleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Circle"),
            **kwargs,
        )
