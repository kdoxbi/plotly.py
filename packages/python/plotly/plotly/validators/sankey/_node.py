import _plotly_utils.basevalidators


class NodeValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="node", parent_name="sankey", **kwargs):
        super(NodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Node"),
            **kwargs,
        )
