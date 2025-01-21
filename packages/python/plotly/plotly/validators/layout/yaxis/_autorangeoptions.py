import _plotly_utils.basevalidators


class AutorangeoptionsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="autorangeoptions", parent_name="layout.yaxis", **kwargs
    ):
        super(AutorangeoptionsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Autorangeoptions"),
            **kwargs,
        )
