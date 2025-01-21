import _plotly_utils.basevalidators


class ProjectValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(
        self, plotly_name="project", parent_name="surface.contours.y", **kwargs
    ):
        super(ProjectValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Project"),
            **kwargs,
        )
