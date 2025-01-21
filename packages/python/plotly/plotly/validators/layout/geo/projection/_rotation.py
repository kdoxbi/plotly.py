import _plotly_utils.basevalidators


class RotationValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="rotation", parent_name="layout.geo.projection", **kwargs
    ):
        super(RotationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rotation"),
            **kwargs,
        )
