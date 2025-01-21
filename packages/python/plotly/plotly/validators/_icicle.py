import _plotly_utils.basevalidators


class IcicleValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="icicle", parent_name="", **kwargs):
        super(IcicleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Icicle"),
            **kwargs,
        )
