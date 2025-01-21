import _plotly_utils.basevalidators


class YbinsValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="ybins", parent_name="histogram2dcontour", **kwargs):
        super(YbinsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "YBins"),
            **kwargs,
        )
