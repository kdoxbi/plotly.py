import _plotly_utils.basevalidators


class RangebreaksValidator(_plotly_utils.basevalidators.CompoundArrayValidator):
    def __init__(self, plotly_name="rangebreaks", parent_name="layout.xaxis", **kwargs):
        super(RangebreaksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Rangebreak"),
            **kwargs,
        )
