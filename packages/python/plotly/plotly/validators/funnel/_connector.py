import _plotly_utils.basevalidators


class ConnectorValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="connector", parent_name="funnel", **kwargs):
        super(ConnectorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Connector"),
            **kwargs,
        )
