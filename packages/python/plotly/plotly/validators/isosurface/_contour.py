import _plotly_utils.basevalidators


class ContourValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="contour", parent_name="isosurface", **kwargs):
        super(ContourValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contour"),
            **kwargs,
        )
