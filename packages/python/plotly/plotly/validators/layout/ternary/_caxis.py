import _plotly_utils.basevalidators


class CaxisValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="caxis", parent_name="layout.ternary", **kwargs):
        super(CaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Caxis"),
            **kwargs,
        )
