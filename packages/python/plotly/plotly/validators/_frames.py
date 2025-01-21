import _plotly_utils.basevalidators


class FramesValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="frames", parent_name="", **kwargs):
        super(FramesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Frame"),
            **kwargs,
        )
