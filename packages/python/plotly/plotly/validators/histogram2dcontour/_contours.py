import _plotly_utils.basevalidators


class ContoursValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="contours", parent_name="histogram2dcontour", **kwargs
    ):
        super(ContoursValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contours"),
            **kwargs,
        )
