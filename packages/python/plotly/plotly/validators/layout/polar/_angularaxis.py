import _plotly_utils.basevalidators


class AngularaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="angularaxis", parent_name="layout.polar", **kwargs):
        super(AngularaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "AngularAxis"),
            **kwargs,
        )
