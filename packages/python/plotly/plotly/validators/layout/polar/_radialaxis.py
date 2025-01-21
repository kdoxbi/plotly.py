import _plotly_utils.basevalidators


class RadialaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="radialaxis", parent_name="layout.polar", **kwargs):
        super(RadialaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "RadialAxis"),
            **kwargs,
        )
