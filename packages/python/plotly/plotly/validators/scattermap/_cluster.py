import _plotly_utils.basevalidators


class ClusterValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="cluster", parent_name="scattermap", **kwargs):
        super(ClusterValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cluster"),
            **kwargs,
        )
