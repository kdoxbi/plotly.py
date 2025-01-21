import _plotly_utils.basevalidators


class SurfaceValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="surface", parent_name="", **kwargs):
        super(SurfaceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Surface"),
            **kwargs,
        )
