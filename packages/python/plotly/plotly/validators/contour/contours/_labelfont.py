import _plotly_utils.basevalidators


class LabelfontValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="labelfont", parent_name="contour.contours", **kwargs
    ):
        super(LabelfontValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Labelfont"),
            **kwargs,
        )
