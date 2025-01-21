import _plotly_utils.basevalidators


class HeatmapValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="heatmap", parent_name="", **kwargs):
        super(HeatmapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Heatmap"),
            **kwargs,
        )
