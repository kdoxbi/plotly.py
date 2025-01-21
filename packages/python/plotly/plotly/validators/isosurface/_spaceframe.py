import _plotly_utils.basevalidators


class SpaceframeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="spaceframe", parent_name="isosurface", **kwargs):
        super(SpaceframeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Spaceframe"),
            **kwargs,
        )
