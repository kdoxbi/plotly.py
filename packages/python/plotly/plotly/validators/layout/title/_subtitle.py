import _plotly_utils.basevalidators


class SubtitleValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="subtitle", parent_name="layout.title", **kwargs):
        super(SubtitleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Subtitle"),
            **kwargs,
        )
