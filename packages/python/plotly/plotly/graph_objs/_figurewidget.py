from plotly.basewidget import BaseFigureWidget


class FigureWidget(BaseFigureWidget):
    def __init__(
        self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs
    ):
        """
        Create a new :class:FigureWidget instance

        Parameters
        ----------
        data
            The 'data' property is a tuple of trace instances
            that may be specified as:
              - A list or tuple of trace instances
                (e.g. [Scatter(...), Bar(...)])
              - A single trace instance
                (e.g. Scatter(...), Bar(...), etc.)
              - A list or tuple of dicts of string/value properties where:
                - The 'type' property specifies the trace type
                    One of: ['bar', 'barpolar', 'box', 'candlestick',
                             'carpet', 'choropleth', 'choroplethmap',
                             'choroplethmapbox', 'cone', 'contour',
                             'contourcarpet', 'densitymap',
                             'densitymapbox', 'funnel', 'funnelarea',
                             'heatmap', 'histogram', 'histogram2d',
                             'histogram2dcontour', 'icicle', 'image',
                             'indicator', 'isosurface', 'mesh3d', 'ohlc',
                             'parcats', 'parcoords', 'pie', 'sankey',
                             'scatter', 'scatter3d', 'scattercarpet',
                             'scattergeo', 'scattergl', 'scattermap',
                             'scattermapbox', 'scatterpolar',
                             'scatterpolargl', 'scattersmith',
                             'scatterternary', 'splom', 'streamtube',
                             'sunburst', 'surface', 'table', 'treemap',
                             'violin', 'volume', 'waterfall']

                - All remaining properties are passed to the constructor of
                  the specified trace type

                (e.g. [{'type': 'scatter', ...}, {'type': 'bar, ...}])

        layout
            The 'layout' property is an instance of Layout
            that may be specified as:
              - An instance of :class:`plotly.graph_objs.Layout`
              - A dict of string/value properties that will be passed
                to the Layout constructor

                Supported dict properties:

                    activeselection
                        :class:`plotly.graph_objects.layout.Activeselec
                        tion` instance or dict with compatible
                        properties
                    activeshape
                        :class:`plotly.graph_objects.layout.Activeshape
                        ` instance or dict with compatible properties
                    annotations
                        A tuple of
                        :class:`plotly.graph_objects.layout.Annotation`
                        instances or dicts with compatible properties
                    annotationdefaults
                        When used in a template (as
                        layout.template.layout.annotationdefaults),
                        sets the default property values to use for
                        elements of layout.annotations
                    autosize
                        Determines whether or not a layout width or
                        height that has been left undefined by the user
                        is initialized on each relayout. Note that,
                        regardless of this attribute, an undefined
                        layout width or height is always initialized on
                        the first call to plot.
                    autotypenumbers
                        Using "strict" a numeric string in trace data
                        is not converted to a number. Using *convert
                        types* a numeric string in trace data may be
                        treated as a number during automatic axis
                        `type` detection. This is the default value;
                        however it could be overridden for individual
                        axes.
                    barcornerradius
                        Sets the rounding of bar corners. May be an
                        integer number of pixels, or a percentage of
                        bar width (as a string ending in %).
                    bargap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    bargroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    barmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "relative", the bars are stacked
                        on top of one another, with negative values
                        below the axis, positive values above With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to reduce "opacity" to
                        see multiple bars.
                    barnorm
                        Sets the normalization for bar traces on the
                        graph. With "fraction", the value of each bar
                        is divided by the sum of all values at that
                        location coordinate. "percent" is the same but
                        multiplied by 100 to show percentages.
                    boxgap
                        Sets the gap (in plot fraction) between boxes
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    boxgroupgap
                        Sets the gap (in plot fraction) between boxes
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    boxmode
                        Determines how boxes at the same location
                        coordinate are displayed on the graph. If
                        "group", the boxes are plotted next to one
                        another centered around the shared location. If
                        "overlay", the boxes are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple boxes. Has no effect on traces
                        that have "width" set.
                    calendar
                        Sets the default calendar system to use for
                        interpreting and displaying dates throughout
                        the plot.
                    clickmode
                        Determines the mode of single click
                        interactions. "event" is the default value and
                        emits the `plotly_click` event. In addition
                        this mode emits the `plotly_selected` event in
                        drag modes "lasso" and "select", but with no
                        event data attached (kept for compatibility
                        reasons). The "select" flag enables selecting
                        single data points via click. This mode also
                        supports persistent selections, meaning that
                        pressing Shift while clicking, adds to /
                        subtracts from an existing selection. "select"
                        with `hovermode`: "x" can be confusing,
                        consider explicitly setting `hovermode`:
                        "closest" when using this feature. Selection
                        events are sent accordingly as long as "event"
                        flag is set as well. When the "event" flag is
                        missing, `plotly_click` and `plotly_selected`
                        events are not fired.
                    coloraxis
                        :class:`plotly.graph_objects.layout.Coloraxis`
                        instance or dict with compatible properties
                    colorscale
                        :class:`plotly.graph_objects.layout.Colorscale`
                        instance or dict with compatible properties
                    colorway
                        Sets the default trace colors.
                    computed
                        Placeholder for exporting automargin-impacting
                        values namely `margin.t`, `margin.b`,
                        `margin.l` and `margin.r` in "full-json" mode.
                    datarevision
                        If provided, a changed value tells
                        `Plotly.react` that one or more data arrays has
                        changed. This way you can modify arrays in-
                        place rather than making a complete new copy
                        for an incremental change. If NOT provided,
                        `Plotly.react` assumes that data arrays are
                        being treated as immutable, thus any data array
                        with a different identity from its predecessor
                        contains new data.
                    dragmode
                        Determines the mode of drag interactions.
                        "select" and "lasso" apply only to scatter
                        traces with markers or text. "orbit" and
                        "turntable" apply only to 3D scenes.
                    editrevision
                        Controls persistence of user-driven changes in
                        `editable: true` configuration, other than
                        trace names and axis titles. Defaults to
                        `layout.uirevision`.
                    extendfunnelareacolors
                        If `true`, the funnelarea slice colors (whether
                        given by `funnelareacolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendiciclecolors
                        If `true`, the icicle slice colors (whether
                        given by `iciclecolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendpiecolors
                        If `true`, the pie slice colors (whether given
                        by `piecolorway` or inherited from `colorway`)
                        will be extended to three times its original
                        length by first repeating every color 20%
                        lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendsunburstcolors
                        If `true`, the sunburst slice colors (whether
                        given by `sunburstcolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    extendtreemapcolors
                        If `true`, the treemap slice colors (whether
                        given by `treemapcolorway` or inherited from
                        `colorway`) will be extended to three times its
                        original length by first repeating every color
                        20% lighter then each color 20% darker. This is
                        intended to reduce the likelihood of reusing
                        the same color when you have many slices, but
                        you can set `false` to disable. Colors provided
                        in the trace, using `marker.colors`, are never
                        extended.
                    font
                        Sets the global font. Note that fonts used in
                        traces and other layout components inherit from
                        the global font.
                    funnelareacolorway
                        Sets the default funnelarea slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendfunnelareacolors`.
                    funnelgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    funnelgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    funnelmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "stack", the bars are stacked on top of one
                        another With "group", the bars are plotted next
                        to one another centered around the shared
                        location. With "overlay", the bars are plotted
                        over one another, you might need to reduce
                        "opacity" to see multiple bars.
                    geo
                        :class:`plotly.graph_objects.layout.Geo`
                        instance or dict with compatible properties
                    grid
                        :class:`plotly.graph_objects.layout.Grid`
                        instance or dict with compatible properties
                    height
                        Sets the plot's height (in px).
                    hiddenlabels
                        hiddenlabels is the funnelarea & pie chart
                        analog of visible:'legendonly' but it can
                        contain many labels, and can simultaneously
                        hide slices from several pies/funnelarea charts
                    hiddenlabelssrc
                        Sets the source reference on Chart Studio Cloud
                        for `hiddenlabels`.
                    hidesources
                        Determines whether or not a text link citing
                        the data source is placed at the bottom-right
                        cored of the figure. Has only an effect only on
                        graphs that have been generated via forked
                        graphs from the Chart Studio Cloud (at
                        https://chart-studio.plotly.com or on-premise).
                    hoverdistance
                        Sets the default distance (in pixels) to look
                        for data to add hover labels (-1 means no
                        cutoff, 0 means no looking for data). This is
                        only a real distance for hovering on point-like
                        objects, like scatter points. For area-like
                        objects (bars, scatter fills, etc) hovering is
                        on inside the area and off outside, but these
                        objects will not supersede hover on point-like
                        objects in case of conflict.
                    hoverlabel
                        :class:`plotly.graph_objects.layout.Hoverlabel`
                        instance or dict with compatible properties
                    hovermode
                        Determines the mode of hover interactions. If
                        "closest", a single hoverlabel will appear for
                        the "closest" point within the `hoverdistance`.
                        If "x" (or "y"), multiple hoverlabels will
                        appear for multiple points at the "closest" x-
                        (or y-) coordinate within the `hoverdistance`,
                        with the caveat that no more than one
                        hoverlabel will appear per trace. If *x
                        unified* (or *y unified*), a single hoverlabel
                        will appear multiple points at the closest x-
                        (or y-) coordinate within the `hoverdistance`
                        with the caveat that no more than one
                        hoverlabel will appear per trace. In this mode,
                        spikelines are enabled by default perpendicular
                        to the specified axis. If false, hover
                        interactions are disabled.
                    hoversubplots
                        Determines expansion of hover effects to other
                        subplots If "single" just the axis pair of the
                        primary point is included without overlaying
                        subplots. If "overlaying" all subplots using
                        the main axis and occupying the same space are
                        included. If "axis", also include stacked
                        subplots using the same axis when `hovermode`
                        is set to "x", *x unified*, "y" or *y unified*.
                    iciclecolorway
                        Sets the default icicle slice colors. Defaults
                        to the main `colorway` used for trace colors.
                        If you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendiciclecolors`.
                    images
                        A tuple of
                        :class:`plotly.graph_objects.layout.Image`
                        instances or dicts with compatible properties
                    imagedefaults
                        When used in a template (as
                        layout.template.layout.imagedefaults), sets the
                        default property values to use for elements of
                        layout.images
                    legend
                        :class:`plotly.graph_objects.layout.Legend`
                        instance or dict with compatible properties
                    map
                        :class:`plotly.graph_objects.layout.Map`
                        instance or dict with compatible properties
                    mapbox
                        :class:`plotly.graph_objects.layout.Mapbox`
                        instance or dict with compatible properties
                    margin
                        :class:`plotly.graph_objects.layout.Margin`
                        instance or dict with compatible properties
                    meta
                        Assigns extra meta information that can be used
                        in various `text` attributes. Attributes such
                        as the graph, axis and colorbar `title.text`,
                        annotation `text` `trace.name` in legend items,
                        `rangeselector`, `updatemenus` and `sliders`
                        `label` text all support `meta`. One can access
                        `meta` fields using template strings:
                        `%{meta[i]}` where `i` is the index of the
                        `meta` item in question. `meta` can also be an
                        object for example `{key: value}` which can be
                        accessed %{meta[key]}.
                    metasrc
                        Sets the source reference on Chart Studio Cloud
                        for `meta`.
                    minreducedheight
                        Minimum height of the plot with
                        margin.automargin applied (in px)
                    minreducedwidth
                        Minimum width of the plot with
                        margin.automargin applied (in px)
                    modebar
                        :class:`plotly.graph_objects.layout.Modebar`
                        instance or dict with compatible properties
                    newselection
                        :class:`plotly.graph_objects.layout.Newselectio
                        n` instance or dict with compatible properties
                    newshape
                        :class:`plotly.graph_objects.layout.Newshape`
                        instance or dict with compatible properties
                    paper_bgcolor
                        Sets the background color of the paper where
                        the graph is drawn.
                    piecolorway
                        Sets the default pie slice colors. Defaults to
                        the main `colorway` used for trace colors. If
                        you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendpiecolors`.
                    plot_bgcolor
                        Sets the background color of the plotting area
                        in-between x and y axes.
                    polar
                        :class:`plotly.graph_objects.layout.Polar`
                        instance or dict with compatible properties
                    scattergap
                        Sets the gap (in plot fraction) between scatter
                        points of adjacent location coordinates.
                        Defaults to `bargap`.
                    scattermode
                        Determines how scatter points at the same
                        location coordinate are displayed on the graph.
                        With "group", the scatter points are plotted
                        next to one another centered around the shared
                        location. With "overlay", the scatter points
                        are plotted over one another, you might need to
                        reduce "opacity" to see multiple scatter
                        points.
                    scene
                        :class:`plotly.graph_objects.layout.Scene`
                        instance or dict with compatible properties
                    selectdirection
                        When `dragmode` is set to "select", this limits
                        the selection of the drag to horizontal,
                        vertical or diagonal. "h" only allows
                        horizontal selection, "v" only vertical, "d"
                        only diagonal and "any" sets no limit.
                    selectionrevision
                        Controls persistence of user-driven changes in
                        selected points from all traces.
                    selections
                        A tuple of
                        :class:`plotly.graph_objects.layout.Selection`
                        instances or dicts with compatible properties
                    selectiondefaults
                        When used in a template (as
                        layout.template.layout.selectiondefaults), sets
                        the default property values to use for elements
                        of layout.selections
                    separators
                        Sets the decimal and thousand separators. For
                        example, *. * puts a '.' before decimals and a
                        space between thousands. In English locales,
                        dflt is ".," but other locales may alter this
                        default.
                    shapes
                        A tuple of
                        :class:`plotly.graph_objects.layout.Shape`
                        instances or dicts with compatible properties
                    shapedefaults
                        When used in a template (as
                        layout.template.layout.shapedefaults), sets the
                        default property values to use for elements of
                        layout.shapes
                    showlegend
                        Determines whether or not a legend is drawn.
                        Default is `true` if there is a trace to show
                        and any of these: a) Two or more traces would
                        by default be shown in the legend. b) One pie
                        trace is shown in the legend. c) One trace is
                        explicitly given with `showlegend: true`.
                    sliders
                        A tuple of
                        :class:`plotly.graph_objects.layout.Slider`
                        instances or dicts with compatible properties
                    sliderdefaults
                        When used in a template (as
                        layout.template.layout.sliderdefaults), sets
                        the default property values to use for elements
                        of layout.sliders
                    smith
                        :class:`plotly.graph_objects.layout.Smith`
                        instance or dict with compatible properties
                    spikedistance
                        Sets the default distance (in pixels) to look
                        for data to draw spikelines to (-1 means no
                        cutoff, 0 means no looking for data). As with
                        hoverdistance, distance does not apply to area-
                        like objects. In addition, some objects can be
                        hovered on but will not generate spikelines,
                        such as scatter fills.
                    sunburstcolorway
                        Sets the default sunburst slice colors.
                        Defaults to the main `colorway` used for trace
                        colors. If you specify a new list here it can
                        still be extended with lighter and darker
                        colors, see `extendsunburstcolors`.
                    template
                        Default attributes to be applied to the plot.
                        This should be a dict with format: `{'layout':
                        layoutTemplate, 'data': {trace_type:
                        [traceTemplate, ...], ...}}` where
                        `layoutTemplate` is a dict matching the
                        structure of `figure.layout` and
                        `traceTemplate` is a dict matching the
                        structure of the trace with type `trace_type`
                        (e.g. 'scatter'). Alternatively, this may be
                        specified as an instance of
                        plotly.graph_objs.layout.Template.  Trace
                        templates are applied cyclically to traces of
                        each type. Container arrays (eg `annotations`)
                        have special handling: An object ending in
                        `defaults` (eg `annotationdefaults`) is applied
                        to each array item. But if an item has a
                        `templateitemname` key we look in the template
                        array for an item with matching `name` and
                        apply that instead. If no matching `name` is
                        found we mark the item invisible. Any named
                        template item not referenced is appended to the
                        end of the array, so this can be used to add a
                        watermark annotation or a logo image, for
                        example. To omit one of these items on the
                        plot, make an item with matching
                        `templateitemname` and `visible: false`.
                    ternary
                        :class:`plotly.graph_objects.layout.Ternary`
                        instance or dict with compatible properties
                    title
                        :class:`plotly.graph_objects.layout.Title`
                        instance or dict with compatible properties
                    transition
                        Sets transition options used during
                        Plotly.react updates.
                    treemapcolorway
                        Sets the default treemap slice colors. Defaults
                        to the main `colorway` used for trace colors.
                        If you specify a new list here it can still be
                        extended with lighter and darker colors, see
                        `extendtreemapcolors`.
                    uirevision
                        Used to allow user interactions with the plot
                        to persist after `Plotly.react` calls that are
                        unaware of these interactions. If `uirevision`
                        is omitted, or if it is given and it changed
                        from the previous `Plotly.react` call, the
                        exact new figure is used. If `uirevision` is
                        truthy and did NOT change, any attribute that
                        has been affected by user interactions and did
                        not receive a different value in the new figure
                        will keep the interaction value.
                        `layout.uirevision` attribute serves as the
                        default for `uirevision` attributes in various
                        sub-containers. For finer control you can set
                        these sub-attributes directly. For example, if
                        your app separately controls the data on the x
                        and y axes you might set
                        `xaxis.uirevision=*time*` and
                        `yaxis.uirevision=*cost*`. Then if only the y
                        data is changed, you can update
                        `yaxis.uirevision=*quantity*` and the y axis
                        range will reset but the x axis range will
                        retain any user-driven zoom.
                    uniformtext
                        :class:`plotly.graph_objects.layout.Uniformtext
                        ` instance or dict with compatible properties
                    updatemenus
                        A tuple of
                        :class:`plotly.graph_objects.layout.Updatemenu`
                        instances or dicts with compatible properties
                    updatemenudefaults
                        When used in a template (as
                        layout.template.layout.updatemenudefaults),
                        sets the default property values to use for
                        elements of layout.updatemenus
                    violingap
                        Sets the gap (in plot fraction) between violins
                        of adjacent location coordinates. Has no effect
                        on traces that have "width" set.
                    violingroupgap
                        Sets the gap (in plot fraction) between violins
                        of the same location coordinate. Has no effect
                        on traces that have "width" set.
                    violinmode
                        Determines how violins at the same location
                        coordinate are displayed on the graph. If
                        "group", the violins are plotted next to one
                        another centered around the shared location. If
                        "overlay", the violins are plotted over one
                        another, you might need to set "opacity" to see
                        them multiple violins. Has no effect on traces
                        that have "width" set.
                    waterfallgap
                        Sets the gap (in plot fraction) between bars of
                        adjacent location coordinates.
                    waterfallgroupgap
                        Sets the gap (in plot fraction) between bars of
                        the same location coordinate.
                    waterfallmode
                        Determines how bars at the same location
                        coordinate are displayed on the graph. With
                        "group", the bars are plotted next to one
                        another centered around the shared location.
                        With "overlay", the bars are plotted over one
                        another, you might need to reduce "opacity" to
                        see multiple bars.
                    width
                        Sets the plot's width (in px).
                    xaxis
                        :class:`plotly.graph_objects.layout.XAxis`
                        instance or dict with compatible properties
                    yaxis
                        :class:`plotly.graph_objects.layout.YAxis`
                        instance or dict with compatible properties

        frames
            The 'frames' property is a tuple of instances of
            Frame that may be specified as:
              - A list or tuple of instances of plotly.graph_objs.Frame
              - A list or tuple of dicts of string/value properties that
                will be passed to the Frame constructor

                Supported dict properties:

                    baseframe
                        The name of the frame into which this frame's
                        properties are merged before applying. This is
                        used to unify properties and avoid needing to
                        specify the same values for the same properties
                        in multiple frames.
                    data
                        A list of traces this frame modifies. The
                        format is identical to the normal trace
                        definition.
                    group
                        An identifier that specifies the group to which
                        the frame belongs, used by animate to select a
                        subset of frames.
                    layout
                        Layout properties which this frame modifies.
                        The format is identical to the normal layout
                        definition.
                    name
                        A label by which to identify the frame
                    traces
                        A list of trace indices that identify the
                        respective traces in the data attribute

        skip_invalid: bool
            If True, invalid properties in the figure specification will be
            skipped silently. If False (default) invalid properties in the
            figure specification will result in a ValueError

        Raises
        ------
        ValueError
            if a property in the specification of data, layout, or frames
            is invalid AND skip_invalid is False
        """
        super(FigureWidget, self).__init__(data, layout, frames, skip_invalid, **kwargs)

    def update(self, dict1=None, overwrite=False, **kwargs) -> "FigureWidget":
        """

        Update the properties of the figure with a dict and/or with
        keyword arguments.

        This recursively updates the structure of the figure
        object with the values in the input dict / keyword arguments.

        Parameters
        ----------
        dict1 : dict
            Dictionary of properties to be updated
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        kwargs :
            Keyword/value pair of properties to be updated

        Examples
        --------
        >>> import plotly.graph_objs as go
        >>> fig = go.Figure(data=[{'y': [1, 2, 3]}])
        >>> fig.update(data=[{'y': [4, 5, 6]}]) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.to_plotly_json() # doctest: +SKIP
            {'data': [{'type': 'scatter',
               'uid': 'e86a7c7a-346a-11e8-8aa8-a0999b0c017b',
               'y': array([4, 5, 6], dtype=int32)}],
             'layout': {}}

        >>> fig = go.Figure(layout={'xaxis':
        ...                         {'color': 'green',
        ...                          'range': [0, 1]}})
        >>> fig.update({'layout': {'xaxis': {'color': 'pink'}}}) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.to_plotly_json() # doctest: +SKIP
            {'data': [],
             'layout': {'xaxis':
                        {'color': 'pink',
                         'range': [0, 1]}}}

        Returns
        -------
        BaseFigure
            Updated figure

        """
        return super(FigureWidget, self).update(dict1, overwrite, **kwargs)

    def update_traces(
        self,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        overwrite=False,
        **kwargs,
    ) -> "FigureWidget":
        """

        Perform a property update operation on all traces that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all traces that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all traces are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each trace and those for which the function returned True
            will be in the selection. If an int N, the Nth trace matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of traces to select.
            To select traces by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  If None
            (the default), all traces are selected.
        secondary_y: boolean or None (default None)
            * If True, only select traces associated with the secondary
              y-axis of the subplot.
            * If False, only select traces associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter traces based on secondary
              y-axis.

            To select traces by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        **kwargs
            Additional property updates to apply to each selected trace. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on

        """
        return super(FigureWidget, self).update_traces(
            patch, selector, row, col, secondary_y, overwrite, **kwargs
        )

    def update_layout(self, dict1=None, overwrite=False, **kwargs) -> "FigureWidget":
        """

        Update the properties of the figure's layout with a dict and/or with
        keyword arguments.

        This recursively updates the structure of the original
        layout with the values in the input dict / keyword arguments.

        Parameters
        ----------
        dict1 : dict
            Dictionary of properties to be updated
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        kwargs :
            Keyword/value pair of properties to be updated

        Returns
        -------
        BaseFigure
            The Figure object that the update_layout method was called on

        """
        return super(FigureWidget, self).update_layout(dict1, overwrite, **kwargs)

    def for_each_trace(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ) -> "FigureWidget":
        """

        Apply a function to all traces that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single trace object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all traces are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each trace and those for which the function returned True
            will be in the selection. If an int N, the Nth trace matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of traces to select.
            To select traces by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  If None
            (the default), all traces are selected.
        secondary_y: boolean or None (default None)
            * If True, only select traces associated with the secondary
              y-axis of the subplot.
            * If False, only select traces associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter traces based on secondary
              y-axis.

            To select traces by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on

        """
        return super(FigureWidget, self).for_each_trace(
            fn, selector, row, col, secondary_y
        )

    def add_trace(
        self, trace, row=None, col=None, secondary_y=None, exclude_empty_subplots=False
    ) -> "FigureWidget":
        """

        Add a trace to the figure

        Parameters
        ----------
        trace : BaseTraceType or dict
            Either:
              - An instances of a trace classe from the plotly.graph_objs
                package (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)
              - or a dicts where:

                  - The 'type' property specifies the trace type (e.g.
                    'scatter', 'bar', 'area', etc.). If the dict has no 'type'
                    property then 'scatter' is assumed.
                  - All remaining properties are passed to the constructor
                    of the specified trace type.

        row : 'all', int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`.
            If 'all', addresses all rows in the specified column(s).
        col : 'all', int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`.
            If 'all', addresses all columns in the specified row(s).
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.
              * The trace argument is a 2D cartesian trace
                (scatter, bar, etc.)
        exclude_empty_subplots: boolean
            If True, the trace will not be added to subplots that don't already
            have traces.
        Returns
        -------
        BaseFigure
            The Figure that add_trace was called on

        Examples
        --------

        >>> from plotly import subplots
        >>> import plotly.graph_objs as go

        Add two Scatter traces to a figure

        >>> fig = go.Figure()
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS
        Figure(...)


        Add two Scatter traces to vertically stacked subplots

        >>> fig = subplots.make_subplots(rows=2)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1) # doctest: +ELLIPSIS
        Figure(...)

        """
        return super(FigureWidget, self).add_trace(
            trace, row, col, secondary_y, exclude_empty_subplots
        )

    def add_traces(
        self,
        data,
        rows=None,
        cols=None,
        secondary_ys=None,
        exclude_empty_subplots=False,
    ) -> "FigureWidget":
        """

        Add traces to the figure

        Parameters
        ----------
        data : list[BaseTraceType or dict]
            A list of trace specifications to be added.
            Trace specifications may be either:

              - Instances of trace classes from the plotly.graph_objs
                package (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)
              - Dicts where:

                  - The 'type' property specifies the trace type (e.g.
                    'scatter', 'bar', 'area', etc.). If the dict has no 'type'
                    property then 'scatter' is assumed.
                  - All remaining properties are passed to the constructor
                    of the specified trace type.

        rows : None, list[int], or int (default None)
            List of subplot row indexes (starting from 1) for the traces to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
            If a single integer is passed, all traces will be added to row number

        cols : None or list[int] (default None)
            List of subplot column indexes (starting from 1) for the traces
            to be added. Only valid if figure was created using
            `plotly.tools.make_subplots`
            If a single integer is passed, all traces will be added to column number


        secondary_ys: None or list[boolean] (default None)
            List of secondary_y booleans for traces to be added. See the
            docstring for `add_trace` for more info.

        exclude_empty_subplots: boolean
            If True, the trace will not be added to subplots that don't already
            have traces.

        Returns
        -------
        BaseFigure
            The Figure that add_traces was called on

        Examples
        --------

        >>> from plotly import subplots
        >>> import plotly.graph_objs as go

        Add two Scatter traces to a figure

        >>> fig = go.Figure()
        >>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),
        ...                 go.Scatter(x=[1,2,3], y=[2,1,2])]) # doctest: +ELLIPSIS
        Figure(...)

        Add two Scatter traces to vertically stacked subplots

        >>> fig = subplots.make_subplots(rows=2)
        >>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),
        ...                 go.Scatter(x=[1,2,3], y=[2,1,2])],
        ...                 rows=[1, 2], cols=[1, 1]) # doctest: +ELLIPSIS
        Figure(...)

        """
        return super(FigureWidget, self).add_traces(
            data, rows, cols, secondary_ys, exclude_empty_subplots
        )

    def add_vline(
        self,
        x,
        row="all",
        col="all",
        exclude_empty_subplots=True,
        annotation=None,
        **kwargs,
    ) -> "FigureWidget":
        """

        Add a vertical line to a plot or subplot that extends infinitely in the
        y-dimension.

        Parameters
        ----------
        x: float or int
            A number representing the x coordinate of the vertical line.
        exclude_empty_subplots: Boolean
            If True (default) do not place the shape on subplots that have no data
            plotted on them.
        row: None, int or 'all'
            Subplot row for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        col: None, int or 'all'
            Subplot column for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        annotation: dict or plotly.graph_objects.layout.Annotation. If dict(),
            it is interpreted as describing an annotation. The annotation is
            placed relative to the shape based on annotation_position (see
            below) unless its x or y value has been specified for the annotation
            passed here. xref and yref are always the same as for the added
            shape and cannot be overridden.
        annotation_position: a string containing optionally ["top", "bottom"]
            and ["left", "right"] specifying where the text should be anchored
            to on the line. Example positions are "bottom left", "right top",
            "right", "bottom". If an annotation is added but annotation_position is
            not specified, this defaults to "top right".
        annotation_*: any parameters to go.layout.Annotation can be passed as
            keywords by prefixing them with "annotation_". For example, to specify the
            annotation text "example" you can pass annotation_text="example" as a
            keyword argument.
        **kwargs:
            Any named function parameters that can be passed to 'add_shape',
            except for x0, x1, y0, y1 or type.
        """
        return super(FigureWidget, self).add_vline(
            x, row, col, exclude_empty_subplots, annotation, **kwargs
        )

    def add_hline(
        self,
        y,
        row="all",
        col="all",
        exclude_empty_subplots=True,
        annotation=None,
        **kwargs,
    ) -> "FigureWidget":
        """

        Add a horizontal line to a plot or subplot that extends infinitely in the
        x-dimension.

        Parameters
        ----------
        y: float or int
            A number representing the y coordinate of the horizontal line.
        exclude_empty_subplots: Boolean
            If True (default) do not place the shape on subplots that have no data
            plotted on them.
        row: None, int or 'all'
            Subplot row for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        col: None, int or 'all'
            Subplot column for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        annotation: dict or plotly.graph_objects.layout.Annotation. If dict(),
            it is interpreted as describing an annotation. The annotation is
            placed relative to the shape based on annotation_position (see
            below) unless its x or y value has been specified for the annotation
            passed here. xref and yref are always the same as for the added
            shape and cannot be overridden.
        annotation_position: a string containing optionally ["top", "bottom"]
            and ["left", "right"] specifying where the text should be anchored
            to on the line. Example positions are "bottom left", "right top",
            "right", "bottom". If an annotation is added but annotation_position is
            not specified, this defaults to "top right".
        annotation_*: any parameters to go.layout.Annotation can be passed as
            keywords by prefixing them with "annotation_". For example, to specify the
            annotation text "example" you can pass annotation_text="example" as a
            keyword argument.
        **kwargs:
            Any named function parameters that can be passed to 'add_shape',
            except for x0, x1, y0, y1 or type.
        """
        return super(FigureWidget, self).add_hline(
            y, row, col, exclude_empty_subplots, annotation, **kwargs
        )

    def add_vrect(
        self,
        x0,
        x1,
        row="all",
        col="all",
        exclude_empty_subplots=True,
        annotation=None,
        **kwargs,
    ) -> "FigureWidget":
        """

        Add a rectangle to a plot or subplot that extends infinitely in the
        y-dimension.

        Parameters
        ----------
        x0: float or int
            A number representing the x coordinate of one side of the rectangle.
        x1: float or int
            A number representing the x coordinate of the other side of the rectangle.
        exclude_empty_subplots: Boolean
            If True (default) do not place the shape on subplots that have no data
            plotted on them.
        row: None, int or 'all'
            Subplot row for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        col: None, int or 'all'
            Subplot column for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        annotation: dict or plotly.graph_objects.layout.Annotation. If dict(),
            it is interpreted as describing an annotation. The annotation is
            placed relative to the shape based on annotation_position (see
            below) unless its x or y value has been specified for the annotation
            passed here. xref and yref are always the same as for the added
            shape and cannot be overridden.
        annotation_position: a string containing optionally ["inside", "outside"], ["top", "bottom"]
            and ["left", "right"] specifying where the text should be anchored
            to on the rectangle. Example positions are "outside top left", "inside
            bottom", "right", "inside left", "inside" ("outside" is not supported). If
            an annotation is added but annotation_position is not specified this
            defaults to "inside top right".
        annotation_*: any parameters to go.layout.Annotation can be passed as
            keywords by prefixing them with "annotation_". For example, to specify the
            annotation text "example" you can pass annotation_text="example" as a
            keyword argument.
        **kwargs:
            Any named function parameters that can be passed to 'add_shape',
            except for x0, x1, y0, y1 or type.
        """
        return super(FigureWidget, self).add_vrect(
            x0, x1, row, col, exclude_empty_subplots, annotation, **kwargs
        )

    def add_hrect(
        self,
        y0,
        y1,
        row="all",
        col="all",
        exclude_empty_subplots=True,
        annotation=None,
        **kwargs,
    ) -> "FigureWidget":
        """

        Add a rectangle to a plot or subplot that extends infinitely in the
        x-dimension.

        Parameters
        ----------
        y0: float or int
            A number representing the y coordinate of one side of the rectangle.
        y1: float or int
            A number representing the y coordinate of the other side of the rectangle.
        exclude_empty_subplots: Boolean
            If True (default) do not place the shape on subplots that have no data
            plotted on them.
        row: None, int or 'all'
            Subplot row for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        col: None, int or 'all'
            Subplot column for shape indexed starting at 1. If 'all', addresses all rows in
            the specified column(s). If both row and col are None, addresses the
            first subplot if subplots exist, or the only plot. By default is "all".
        annotation: dict or plotly.graph_objects.layout.Annotation. If dict(),
            it is interpreted as describing an annotation. The annotation is
            placed relative to the shape based on annotation_position (see
            below) unless its x or y value has been specified for the annotation
            passed here. xref and yref are always the same as for the added
            shape and cannot be overridden.
        annotation_position: a string containing optionally ["inside", "outside"], ["top", "bottom"]
            and ["left", "right"] specifying where the text should be anchored
            to on the rectangle. Example positions are "outside top left", "inside
            bottom", "right", "inside left", "inside" ("outside" is not supported). If
            an annotation is added but annotation_position is not specified this
            defaults to "inside top right".
        annotation_*: any parameters to go.layout.Annotation can be passed as
            keywords by prefixing them with "annotation_". For example, to specify the
            annotation text "example" you can pass annotation_text="example" as a
            keyword argument.
        **kwargs:
            Any named function parameters that can be passed to 'add_shape',
            except for x0, x1, y0, y1 or type.
        """
        return super(FigureWidget, self).add_hrect(
            y0, y1, row, col, exclude_empty_subplots, annotation, **kwargs
        )

    def set_subplots(
        self, rows=None, cols=None, **make_subplots_args
    ) -> "FigureWidget":
        """

        Add subplots to this figure. If the figure already contains subplots,
        then this throws an error. Accepts any keyword arguments that
        plotly.subplots.make_subplots accepts.

        """
        return super(FigureWidget, self).set_subplots(rows, cols, **make_subplots_args)

    def add_bar(
        self,
        alignmentgroup=None,
        base=None,
        basesrc=None,
        cliponaxis=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Bar

        new_trace = Bar(
            alignmentgroup=alignmentgroup,
            base=base,
            basesrc=basesrc,
            cliponaxis=cliponaxis,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_barpolar(
        self,
        base=None,
        basesrc=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetsrc=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        widthsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Barpolar

        new_trace = Barpolar(
            base=base,
            basesrc=basesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetsrc=offsetsrc,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_box(
        self,
        alignmentgroup=None,
        boxmean=None,
        boxpoints=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        lowerfence=None,
        lowerfencesrc=None,
        marker=None,
        mean=None,
        meansrc=None,
        median=None,
        mediansrc=None,
        meta=None,
        metasrc=None,
        name=None,
        notched=None,
        notchspan=None,
        notchspansrc=None,
        notchwidth=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        q1=None,
        q1src=None,
        q3=None,
        q3src=None,
        quartilemethod=None,
        sd=None,
        sdmultiple=None,
        sdsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showwhiskers=None,
        sizemode=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        upperfence=None,
        upperfencesrc=None,
        visible=None,
        whiskerwidth=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Box

        new_trace = Box(
            alignmentgroup=alignmentgroup,
            boxmean=boxmean,
            boxpoints=boxpoints,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            lowerfence=lowerfence,
            lowerfencesrc=lowerfencesrc,
            marker=marker,
            mean=mean,
            meansrc=meansrc,
            median=median,
            mediansrc=mediansrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            notched=notched,
            notchspan=notchspan,
            notchspansrc=notchspansrc,
            notchwidth=notchwidth,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            q1=q1,
            q1src=q1src,
            q3=q3,
            q3src=q3src,
            quartilemethod=quartilemethod,
            sd=sd,
            sdmultiple=sdmultiple,
            sdsrc=sdsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showwhiskers=showwhiskers,
            sizemode=sizemode,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            upperfence=upperfence,
            upperfencesrc=upperfencesrc,
            visible=visible,
            whiskerwidth=whiskerwidth,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_candlestick(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        whiskerwidth=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        yhoverformat=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Candlestick

        new_trace = Candlestick(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            whiskerwidth=whiskerwidth,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            yaxis=yaxis,
            yhoverformat=yhoverformat,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_carpet(
        self,
        a=None,
        a0=None,
        aaxis=None,
        asrc=None,
        b=None,
        b0=None,
        baxis=None,
        bsrc=None,
        carpet=None,
        cheaterslope=None,
        color=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        font=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Carpet

        new_trace = Carpet(
            a=a,
            a0=a0,
            aaxis=aaxis,
            asrc=asrc,
            b=b,
            b0=b0,
            baxis=baxis,
            bsrc=bsrc,
            carpet=carpet,
            cheaterslope=cheaterslope,
            color=color,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            font=font,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_choropleth(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geo=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Choropleth

        new_trace = Choropleth(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            geo=geo,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_choroplethmap(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Choroplethmap

        new_trace = Choroplethmap(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_choroplethmapbox(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        locations=None,
        locationssrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        reversescale=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Choroplethmapbox

        new_trace = Choroplethmapbox(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            locations=locations,
            locationssrc=locationssrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            reversescale=reversescale,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_cone(
        self,
        anchor=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        sizemode=None,
        sizeref=None,
        stream=None,
        text=None,
        textsrc=None,
        u=None,
        uhoverformat=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        vhoverformat=None,
        visible=None,
        vsrc=None,
        w=None,
        whoverformat=None,
        wsrc=None,
        x=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Cone

        new_trace = Cone(
            anchor=anchor,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            sizemode=sizemode,
            sizeref=sizeref,
            stream=stream,
            text=text,
            textsrc=textsrc,
            u=u,
            uhoverformat=uhoverformat,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            vhoverformat=vhoverformat,
            visible=visible,
            vsrc=vsrc,
            w=w,
            whoverformat=whoverformat,
            wsrc=wsrc,
            x=x,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_contour(
        self,
        autocolorscale=None,
        autocontour=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoverongaps=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textfont=None,
        textsrc=None,
        texttemplate=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zorder=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Contour

        new_trace = Contour(
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoverongaps=hoverongaps,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textfont=textfont,
            textsrc=textsrc,
            texttemplate=texttemplate,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zorder=zorder,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_contourcarpet(
        self,
        a=None,
        a0=None,
        asrc=None,
        atype=None,
        autocolorscale=None,
        autocontour=None,
        b=None,
        b0=None,
        bsrc=None,
        btype=None,
        carpet=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        da=None,
        db=None,
        fillcolor=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zorder=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Contourcarpet

        new_trace = Contourcarpet(
            a=a,
            a0=a0,
            asrc=asrc,
            atype=atype,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            b=b,
            b0=b0,
            bsrc=bsrc,
            btype=btype,
            carpet=carpet,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            da=da,
            db=db,
            fillcolor=fillcolor,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zorder=zorder,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_densitymap(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lon=None,
        lonsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        radius=None,
        radiussrc=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Densitymap

        new_trace = Densitymap(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lon=lon,
            lonsrc=lonsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            radius=radius,
            radiussrc=radiussrc,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_densitymapbox(
        self,
        autocolorscale=None,
        below=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lon=None,
        lonsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        radius=None,
        radiussrc=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        subplot=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        z=None,
        zauto=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Densitymapbox

        new_trace = Densitymapbox(
            autocolorscale=autocolorscale,
            below=below,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lon=lon,
            lonsrc=lonsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            radius=radius,
            radiussrc=radiussrc,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            subplot=subplot,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            z=z,
            zauto=zauto,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_funnel(
        self,
        alignmentgroup=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Funnel

        new_trace = Funnel(
            alignmentgroup=alignmentgroup,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_funnelarea(
        self,
        aspectratio=None,
        baseratio=None,
        customdata=None,
        customdatasrc=None,
        dlabel=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        scalegroup=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        title=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Funnelarea

        new_trace = Funnelarea(
            aspectratio=aspectratio,
            baseratio=baseratio,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dlabel=dlabel,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            scalegroup=scalegroup,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            title=title,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_heatmap(
        self,
        autocolorscale=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoverongaps=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textfont=None,
        textsrc=None,
        texttemplate=None,
        transpose=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xgap=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        xtype=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        ygap=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        ytype=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zorder=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Heatmap

        new_trace = Heatmap(
            autocolorscale=autocolorscale,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoverongaps=hoverongaps,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textfont=textfont,
            textsrc=textsrc,
            texttemplate=texttemplate,
            transpose=transpose,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xgap=xgap,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            xtype=xtype,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            ygap=ygap,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            ytype=ytype,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zorder=zorder,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram(
        self,
        alignmentgroup=None,
        autobinx=None,
        autobiny=None,
        bingroup=None,
        cliponaxis=None,
        constraintext=None,
        cumulative=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        xaxis=None,
        xbins=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybins=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Histogram

        new_trace = Histogram(
            alignmentgroup=alignmentgroup,
            autobinx=autobinx,
            autobiny=autobiny,
            bingroup=bingroup,
            cliponaxis=cliponaxis,
            constraintext=constraintext,
            cumulative=cumulative,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbins=xbins,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybins=ybins,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram2d(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        textfont=None,
        texttemplate=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xgap=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        ygap=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Histogram2d

        new_trace = Histogram2d(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            textfont=textfont,
            texttemplate=texttemplate,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xgap=xgap,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            ygap=ygap,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_histogram2dcontour(
        self,
        autobinx=None,
        autobiny=None,
        autocolorscale=None,
        autocontour=None,
        bingroup=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        histfunc=None,
        histnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        nbinsx=None,
        nbinsy=None,
        ncontours=None,
        opacity=None,
        reversescale=None,
        showlegend=None,
        showscale=None,
        stream=None,
        textfont=None,
        texttemplate=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xbingroup=None,
        xbins=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yaxis=None,
        ybingroup=None,
        ybins=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zauto=None,
        zhoverformat=None,
        zmax=None,
        zmid=None,
        zmin=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Histogram2dContour

        new_trace = Histogram2dContour(
            autobinx=autobinx,
            autobiny=autobiny,
            autocolorscale=autocolorscale,
            autocontour=autocontour,
            bingroup=bingroup,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            histfunc=histfunc,
            histnorm=histnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            nbinsx=nbinsx,
            nbinsy=nbinsy,
            ncontours=ncontours,
            opacity=opacity,
            reversescale=reversescale,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            textfont=textfont,
            texttemplate=texttemplate,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xbingroup=xbingroup,
            xbins=xbins,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yaxis=yaxis,
            ybingroup=ybingroup,
            ybins=ybins,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zauto=zauto,
            zhoverformat=zhoverformat,
            zmax=zmax,
            zmid=zmid,
            zmin=zmin,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_icicle(
        self,
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        labels=None,
        labelssrc=None,
        leaf=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        pathbar=None,
        root=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tiling=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Icicle

        new_trace = Icicle(
            branchvalues=branchvalues,
            count=count,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            labels=labels,
            labelssrc=labelssrc,
            leaf=leaf,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            pathbar=pathbar,
            root=root,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            tiling=tiling,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_image(
        self,
        colormodel=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        source=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x0=None,
        xaxis=None,
        y0=None,
        yaxis=None,
        z=None,
        zmax=None,
        zmin=None,
        zorder=None,
        zsmooth=None,
        zsrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Image

        new_trace = Image(
            colormodel=colormodel,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            source=source,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x0=x0,
            xaxis=xaxis,
            y0=y0,
            yaxis=yaxis,
            z=z,
            zmax=zmax,
            zmin=zmin,
            zorder=zorder,
            zsmooth=zsmooth,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_indicator(
        self,
        align=None,
        customdata=None,
        customdatasrc=None,
        delta=None,
        domain=None,
        gauge=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        number=None,
        stream=None,
        title=None,
        uid=None,
        uirevision=None,
        value=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Indicator

        new_trace = Indicator(
            align=align,
            customdata=customdata,
            customdatasrc=customdatasrc,
            delta=delta,
            domain=domain,
            gauge=gauge,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            number=number,
            stream=stream,
            title=title,
            uid=uid,
            uirevision=uirevision,
            value=value,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_isosurface(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuehoverformat=None,
        valuesrc=None,
        visible=None,
        x=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Isosurface

        new_trace = Isosurface(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuehoverformat=valuehoverformat,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_mesh3d(
        self,
        alphahull=None,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        color=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        delaunayaxis=None,
        facecolor=None,
        facecolorsrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        i=None,
        ids=None,
        idssrc=None,
        intensity=None,
        intensitymode=None,
        intensitysrc=None,
        isrc=None,
        j=None,
        jsrc=None,
        k=None,
        ksrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        vertexcolor=None,
        vertexcolorsrc=None,
        visible=None,
        x=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Mesh3d

        new_trace = Mesh3d(
            alphahull=alphahull,
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            color=color,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            delaunayaxis=delaunayaxis,
            facecolor=facecolor,
            facecolorsrc=facecolorsrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            i=i,
            ids=ids,
            idssrc=idssrc,
            intensity=intensity,
            intensitymode=intensitymode,
            intensitysrc=intensitysrc,
            isrc=isrc,
            j=j,
            jsrc=jsrc,
            k=k,
            ksrc=ksrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            vertexcolor=vertexcolor,
            vertexcolorsrc=vertexcolorsrc,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_ohlc(
        self,
        close=None,
        closesrc=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        high=None,
        highsrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        low=None,
        lowsrc=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        open=None,
        opensrc=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textsrc=None,
        tickwidth=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        yaxis=None,
        yhoverformat=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Ohlc

        new_trace = Ohlc(
            close=close,
            closesrc=closesrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            high=high,
            highsrc=highsrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            low=low,
            lowsrc=lowsrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            open=open,
            opensrc=opensrc,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textsrc=textsrc,
            tickwidth=tickwidth,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            yaxis=yaxis,
            yhoverformat=yhoverformat,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_parcats(
        self,
        arrangement=None,
        bundlecolors=None,
        counts=None,
        countssrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        hoverinfo=None,
        hoveron=None,
        hovertemplate=None,
        labelfont=None,
        legendgrouptitle=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        sortpaths=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Parcats

        new_trace = Parcats(
            arrangement=arrangement,
            bundlecolors=bundlecolors,
            counts=counts,
            countssrc=countssrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            hoverinfo=hoverinfo,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            labelfont=labelfont,
            legendgrouptitle=legendgrouptitle,
            legendwidth=legendwidth,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            sortpaths=sortpaths,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_parcoords(
        self,
        customdata=None,
        customdatasrc=None,
        dimensions=None,
        dimensiondefaults=None,
        domain=None,
        ids=None,
        idssrc=None,
        labelangle=None,
        labelfont=None,
        labelside=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        meta=None,
        metasrc=None,
        name=None,
        rangefont=None,
        stream=None,
        tickfont=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Parcoords

        new_trace = Parcoords(
            customdata=customdata,
            customdatasrc=customdatasrc,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            domain=domain,
            ids=ids,
            idssrc=idssrc,
            labelangle=labelangle,
            labelfont=labelfont,
            labelside=labelside,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            meta=meta,
            metasrc=metasrc,
            name=name,
            rangefont=rangefont,
            stream=stream,
            tickfont=tickfont,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_pie(
        self,
        automargin=None,
        customdata=None,
        customdatasrc=None,
        direction=None,
        dlabel=None,
        domain=None,
        hole=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        insidetextorientation=None,
        label0=None,
        labels=None,
        labelssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        pull=None,
        pullsrc=None,
        rotation=None,
        scalegroup=None,
        showlegend=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        title=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Pie

        new_trace = Pie(
            automargin=automargin,
            customdata=customdata,
            customdatasrc=customdatasrc,
            direction=direction,
            dlabel=dlabel,
            domain=domain,
            hole=hole,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            insidetextorientation=insidetextorientation,
            label0=label0,
            labels=labels,
            labelssrc=labelssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            pull=pull,
            pullsrc=pullsrc,
            rotation=rotation,
            scalegroup=scalegroup,
            showlegend=showlegend,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            title=title,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_sankey(
        self,
        arrangement=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        link=None,
        meta=None,
        metasrc=None,
        name=None,
        node=None,
        orientation=None,
        selectedpoints=None,
        stream=None,
        textfont=None,
        uid=None,
        uirevision=None,
        valueformat=None,
        valuesuffix=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Sankey

        new_trace = Sankey(
            arrangement=arrangement,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            link=link,
            meta=meta,
            metasrc=metasrc,
            name=name,
            node=node,
            orientation=orientation,
            selectedpoints=selectedpoints,
            stream=stream,
            textfont=textfont,
            uid=uid,
            uirevision=uirevision,
            valueformat=valueformat,
            valuesuffix=valuesuffix,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatter(
        self,
        alignmentgroup=None,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        fillgradient=None,
        fillpattern=None,
        groupnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stackgaps=None,
        stackgroup=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scatter

        new_trace = Scatter(
            alignmentgroup=alignmentgroup,
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            fillgradient=fillgradient,
            fillpattern=fillpattern,
            groupnorm=groupnorm,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stackgaps=stackgaps,
            stackgroup=stackgroup,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scatter3d(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        error_x=None,
        error_y=None,
        error_z=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        projection=None,
        scene=None,
        showlegend=None,
        stream=None,
        surfaceaxis=None,
        surfacecolor=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scatter3d

        new_trace = Scatter3d(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            error_x=error_x,
            error_y=error_y,
            error_z=error_z,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            projection=projection,
            scene=scene,
            showlegend=showlegend,
            stream=stream,
            surfaceaxis=surfaceaxis,
            surfacecolor=surfacecolor,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattercarpet(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        carpet=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxis=None,
        yaxis=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattercarpet

        new_trace = Scattercarpet(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            carpet=carpet,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxis=xaxis,
            yaxis=yaxis,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scattergeo(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        featureidkey=None,
        fill=None,
        fillcolor=None,
        geo=None,
        geojson=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        locationmode=None,
        locations=None,
        locationssrc=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattergeo

        new_trace = Scattergeo(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            featureidkey=featureidkey,
            fill=fill,
            fillcolor=fillcolor,
            geo=geo,
            geojson=geojson,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            locationmode=locationmode,
            locations=locations,
            locationssrc=locationssrc,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattergl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattergl

        new_trace = Scattergl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dx=dx,
            dy=dy,
            error_x=error_x,
            error_y=error_y,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_scattermap(
        self,
        below=None,
        cluster=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattermap

        new_trace = Scattermap(
            below=below,
            cluster=cluster,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattermapbox(
        self,
        below=None,
        cluster=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        lat=None,
        latsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        lon=None,
        lonsrc=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattermapbox

        new_trace = Scattermapbox(
            below=below,
            cluster=cluster,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            lat=lat,
            latsrc=latsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            lon=lon,
            lonsrc=lonsrc,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolar(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scatterpolar

        new_trace = Scatterpolar(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterpolargl(
        self,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dr=None,
        dtheta=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        r=None,
        r0=None,
        rsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        theta=None,
        theta0=None,
        thetasrc=None,
        thetaunit=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scatterpolargl

        new_trace = Scatterpolargl(
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            dr=dr,
            dtheta=dtheta,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            r=r,
            r0=r0,
            rsrc=rsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            theta=theta,
            theta0=theta0,
            thetasrc=thetasrc,
            thetaunit=thetaunit,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scattersmith(
        self,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        imag=None,
        imagsrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        real=None,
        realsrc=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scattersmith

        new_trace = Scattersmith(
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            imag=imag,
            imagsrc=imagsrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            real=real,
            realsrc=realsrc,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_scatterternary(
        self,
        a=None,
        asrc=None,
        b=None,
        bsrc=None,
        c=None,
        cliponaxis=None,
        connectgaps=None,
        csrc=None,
        customdata=None,
        customdatasrc=None,
        fill=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        subplot=None,
        sum=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Scatterternary

        new_trace = Scatterternary(
            a=a,
            asrc=asrc,
            b=b,
            bsrc=bsrc,
            c=c,
            cliponaxis=cliponaxis,
            connectgaps=connectgaps,
            csrc=csrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fill=fill,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            mode=mode,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            subplot=subplot,
            sum=sum,
            text=text,
            textfont=textfont,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_splom(
        self,
        customdata=None,
        customdatasrc=None,
        diagonal=None,
        dimensions=None,
        dimensiondefaults=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        marker=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        showlowerhalf=None,
        showupperhalf=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        xaxes=None,
        xhoverformat=None,
        yaxes=None,
        yhoverformat=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Splom

        new_trace = Splom(
            customdata=customdata,
            customdatasrc=customdatasrc,
            diagonal=diagonal,
            dimensions=dimensions,
            dimensiondefaults=dimensiondefaults,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            marker=marker,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            showlowerhalf=showlowerhalf,
            showupperhalf=showupperhalf,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            xaxes=xaxes,
            xhoverformat=xhoverformat,
            yaxes=yaxes,
            yhoverformat=yhoverformat,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_streamtube(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        customdata=None,
        customdatasrc=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        maxdisplayed=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        sizeref=None,
        starts=None,
        stream=None,
        text=None,
        u=None,
        uhoverformat=None,
        uid=None,
        uirevision=None,
        usrc=None,
        v=None,
        vhoverformat=None,
        visible=None,
        vsrc=None,
        w=None,
        whoverformat=None,
        wsrc=None,
        x=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Streamtube

        new_trace = Streamtube(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            maxdisplayed=maxdisplayed,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            sizeref=sizeref,
            starts=starts,
            stream=stream,
            text=text,
            u=u,
            uhoverformat=uhoverformat,
            uid=uid,
            uirevision=uirevision,
            usrc=usrc,
            v=v,
            vhoverformat=vhoverformat,
            visible=visible,
            vsrc=vsrc,
            w=w,
            whoverformat=whoverformat,
            wsrc=wsrc,
            x=x,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_sunburst(
        self,
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        insidetextorientation=None,
        labels=None,
        labelssrc=None,
        leaf=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        root=None,
        rotation=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Sunburst

        new_trace = Sunburst(
            branchvalues=branchvalues,
            count=count,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            insidetextorientation=insidetextorientation,
            labels=labels,
            labelssrc=labelssrc,
            leaf=leaf,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            root=root,
            rotation=rotation,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_surface(
        self,
        autocolorscale=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        connectgaps=None,
        contours=None,
        customdata=None,
        customdatasrc=None,
        hidesurface=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        opacityscale=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        stream=None,
        surfacecolor=None,
        surfacecolorsrc=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        visible=None,
        x=None,
        xcalendar=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        ycalendar=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zcalendar=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Surface

        new_trace = Surface(
            autocolorscale=autocolorscale,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            connectgaps=connectgaps,
            contours=contours,
            customdata=customdata,
            customdatasrc=customdatasrc,
            hidesurface=hidesurface,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            opacityscale=opacityscale,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            stream=stream,
            surfacecolor=surfacecolor,
            surfacecolorsrc=surfacecolorsrc,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            x=x,
            xcalendar=xcalendar,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            ycalendar=ycalendar,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zcalendar=zcalendar,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_table(
        self,
        cells=None,
        columnorder=None,
        columnordersrc=None,
        columnwidth=None,
        columnwidthsrc=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        header=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        meta=None,
        metasrc=None,
        name=None,
        stream=None,
        uid=None,
        uirevision=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Table

        new_trace = Table(
            cells=cells,
            columnorder=columnorder,
            columnordersrc=columnordersrc,
            columnwidth=columnwidth,
            columnwidthsrc=columnwidthsrc,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            header=header,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            ids=ids,
            idssrc=idssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            stream=stream,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_treemap(
        self,
        branchvalues=None,
        count=None,
        customdata=None,
        customdatasrc=None,
        domain=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        insidetextfont=None,
        labels=None,
        labelssrc=None,
        legend=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        level=None,
        marker=None,
        maxdepth=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        outsidetextfont=None,
        parents=None,
        parentssrc=None,
        pathbar=None,
        root=None,
        sort=None,
        stream=None,
        text=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        tiling=None,
        uid=None,
        uirevision=None,
        values=None,
        valuessrc=None,
        visible=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Treemap

        new_trace = Treemap(
            branchvalues=branchvalues,
            count=count,
            customdata=customdata,
            customdatasrc=customdatasrc,
            domain=domain,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            insidetextfont=insidetextfont,
            labels=labels,
            labelssrc=labelssrc,
            legend=legend,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            level=level,
            marker=marker,
            maxdepth=maxdepth,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            outsidetextfont=outsidetextfont,
            parents=parents,
            parentssrc=parentssrc,
            pathbar=pathbar,
            root=root,
            sort=sort,
            stream=stream,
            text=text,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            tiling=tiling,
            uid=uid,
            uirevision=uirevision,
            values=values,
            valuessrc=valuessrc,
            visible=visible,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_violin(
        self,
        alignmentgroup=None,
        bandwidth=None,
        box=None,
        customdata=None,
        customdatasrc=None,
        fillcolor=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        jitter=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meanline=None,
        meta=None,
        metasrc=None,
        name=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        pointpos=None,
        points=None,
        quartilemethod=None,
        scalegroup=None,
        scalemode=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        side=None,
        span=None,
        spanmode=None,
        stream=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        width=None,
        x=None,
        x0=None,
        xaxis=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yhoverformat=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Violin

        new_trace = Violin(
            alignmentgroup=alignmentgroup,
            bandwidth=bandwidth,
            box=box,
            customdata=customdata,
            customdatasrc=customdatasrc,
            fillcolor=fillcolor,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hoveron=hoveron,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            jitter=jitter,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            marker=marker,
            meanline=meanline,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offsetgroup=offsetgroup,
            opacity=opacity,
            orientation=orientation,
            pointpos=pointpos,
            points=points,
            quartilemethod=quartilemethod,
            scalegroup=scalegroup,
            scalemode=scalemode,
            selected=selected,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            side=side,
            span=span,
            spanmode=spanmode,
            stream=stream,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            unselected=unselected,
            visible=visible,
            width=width,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def add_volume(
        self,
        autocolorscale=None,
        caps=None,
        cauto=None,
        cmax=None,
        cmid=None,
        cmin=None,
        coloraxis=None,
        colorbar=None,
        colorscale=None,
        contour=None,
        customdata=None,
        customdatasrc=None,
        flatshading=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        isomax=None,
        isomin=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        lighting=None,
        lightposition=None,
        meta=None,
        metasrc=None,
        name=None,
        opacity=None,
        opacityscale=None,
        reversescale=None,
        scene=None,
        showlegend=None,
        showscale=None,
        slices=None,
        spaceframe=None,
        stream=None,
        surface=None,
        text=None,
        textsrc=None,
        uid=None,
        uirevision=None,
        value=None,
        valuehoverformat=None,
        valuesrc=None,
        visible=None,
        x=None,
        xhoverformat=None,
        xsrc=None,
        y=None,
        yhoverformat=None,
        ysrc=None,
        z=None,
        zhoverformat=None,
        zsrc=None,
        row=None,
        col=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Volume

        new_trace = Volume(
            autocolorscale=autocolorscale,
            caps=caps,
            cauto=cauto,
            cmax=cmax,
            cmid=cmid,
            cmin=cmin,
            coloraxis=coloraxis,
            colorbar=colorbar,
            colorscale=colorscale,
            contour=contour,
            customdata=customdata,
            customdatasrc=customdatasrc,
            flatshading=flatshading,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            isomax=isomax,
            isomin=isomin,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            lighting=lighting,
            lightposition=lightposition,
            meta=meta,
            metasrc=metasrc,
            name=name,
            opacity=opacity,
            opacityscale=opacityscale,
            reversescale=reversescale,
            scene=scene,
            showlegend=showlegend,
            showscale=showscale,
            slices=slices,
            spaceframe=spaceframe,
            stream=stream,
            surface=surface,
            text=text,
            textsrc=textsrc,
            uid=uid,
            uirevision=uirevision,
            value=value,
            valuehoverformat=valuehoverformat,
            valuesrc=valuesrc,
            visible=visible,
            x=x,
            xhoverformat=xhoverformat,
            xsrc=xsrc,
            y=y,
            yhoverformat=yhoverformat,
            ysrc=ysrc,
            z=z,
            zhoverformat=zhoverformat,
            zsrc=zsrc,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col)

    def add_waterfall(
        self,
        alignmentgroup=None,
        base=None,
        cliponaxis=None,
        connector=None,
        constraintext=None,
        customdata=None,
        customdatasrc=None,
        decreasing=None,
        dx=None,
        dy=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        increasing=None,
        insidetextanchor=None,
        insidetextfont=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        measure=None,
        measuresrc=None,
        meta=None,
        metasrc=None,
        name=None,
        offset=None,
        offsetgroup=None,
        offsetsrc=None,
        opacity=None,
        orientation=None,
        outsidetextfont=None,
        selectedpoints=None,
        showlegend=None,
        stream=None,
        text=None,
        textangle=None,
        textfont=None,
        textinfo=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatesrc=None,
        totals=None,
        uid=None,
        uirevision=None,
        visible=None,
        width=None,
        widthsrc=None,
        x=None,
        x0=None,
        xaxis=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import Waterfall

        new_trace = Waterfall(
            alignmentgroup=alignmentgroup,
            base=base,
            cliponaxis=cliponaxis,
            connector=connector,
            constraintext=constraintext,
            customdata=customdata,
            customdatasrc=customdatasrc,
            decreasing=decreasing,
            dx=dx,
            dy=dy,
            hoverinfo=hoverinfo,
            hoverinfosrc=hoverinfosrc,
            hoverlabel=hoverlabel,
            hovertemplate=hovertemplate,
            hovertemplatesrc=hovertemplatesrc,
            hovertext=hovertext,
            hovertextsrc=hovertextsrc,
            ids=ids,
            idssrc=idssrc,
            increasing=increasing,
            insidetextanchor=insidetextanchor,
            insidetextfont=insidetextfont,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            measure=measure,
            measuresrc=measuresrc,
            meta=meta,
            metasrc=metasrc,
            name=name,
            offset=offset,
            offsetgroup=offsetgroup,
            offsetsrc=offsetsrc,
            opacity=opacity,
            orientation=orientation,
            outsidetextfont=outsidetextfont,
            selectedpoints=selectedpoints,
            showlegend=showlegend,
            stream=stream,
            text=text,
            textangle=textangle,
            textfont=textfont,
            textinfo=textinfo,
            textposition=textposition,
            textpositionsrc=textpositionsrc,
            textsrc=textsrc,
            texttemplate=texttemplate,
            texttemplatesrc=texttemplatesrc,
            totals=totals,
            uid=uid,
            uirevision=uirevision,
            visible=visible,
            width=width,
            widthsrc=widthsrc,
            x=x,
            x0=x0,
            xaxis=xaxis,
            xhoverformat=xhoverformat,
            xperiod=xperiod,
            xperiod0=xperiod0,
            xperiodalignment=xperiodalignment,
            xsrc=xsrc,
            y=y,
            y0=y0,
            yaxis=yaxis,
            yhoverformat=yhoverformat,
            yperiod=yperiod,
            yperiod0=yperiod0,
            yperiodalignment=yperiodalignment,
            ysrc=ysrc,
            zorder=zorder,
            **kwargs,
        )
        return self.add_trace(new_trace, row=row, col=col, secondary_y=secondary_y)

    def select_coloraxes(self, selector=None, row=None, col=None):
        """
        Select coloraxis subplot objects from a particular subplot cell
        and/or coloraxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            coloraxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the coloraxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("coloraxis", selector, row, col)

    def for_each_coloraxis(
        self, fn, selector=None, row=None, col=None
    ) -> "FigureWidget":
        """
        Apply a function to all coloraxis objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single coloraxis object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            coloraxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_coloraxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all coloraxis objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            coloraxis objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            coloraxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all coloraxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            coloraxis and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of coloraxis objects to select.
            To select coloraxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all coloraxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            coloraxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_coloraxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_geos(self, selector=None, row=None, col=None):
        """
        Select geo subplot objects from a particular subplot cell
        and/or geo subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            geo and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the geo
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("geo", selector, row, col)

    def for_each_geo(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all geo objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single geo object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            geo and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_geos(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all geo objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            geo objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            geo objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all geo objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            geo and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of geo objects to select.
            To select geo objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all geo objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            geo object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_geos(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_legends(self, selector=None, row=None, col=None):
        """
        Select legend subplot objects from a particular subplot cell
        and/or legend subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            legend objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all legend objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            legend and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of legend objects to select.
            To select legend objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all legend objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the legend
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("legend", selector, row, col)

    def for_each_legend(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all legend objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single legend object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            legend objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all legend objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            legend and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of legend objects to select.
            To select legend objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all legend objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_legends(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_legends(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all legend objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            legend objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            legend objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all legend objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            legend and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of legend objects to select.
            To select legend objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all legend objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            legend object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_legends(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_maps(self, selector=None, row=None, col=None):
        """
        Select map subplot objects from a particular subplot cell
        and/or map subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            map objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all map objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            map and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of map objects to select.
            To select map objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all map objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the map
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("map", selector, row, col)

    def for_each_map(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all map objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single map object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            map objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all map objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            map and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of map objects to select.
            To select map objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all map objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_maps(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_maps(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all map objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            map objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            map objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all map objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            map and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of map objects to select.
            To select map objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all map objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            map object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_maps(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_mapboxes(self, selector=None, row=None, col=None):
        """
        Select mapbox subplot objects from a particular subplot cell
        and/or mapbox subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            mapbox and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the mapbox
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("mapbox", selector, row, col)

    def for_each_mapbox(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all mapbox objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single mapbox object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            mapbox and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_mapboxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all mapbox objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            mapbox objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            mapbox objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all mapbox objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            mapbox and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of mapbox objects to select.
            To select mapbox objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all mapbox objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            mapbox object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_mapboxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_polars(self, selector=None, row=None, col=None):
        """
        Select polar subplot objects from a particular subplot cell
        and/or polar subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            polar and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the polar
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("polar", selector, row, col)

    def for_each_polar(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all polar objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single polar object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            polar and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_polars(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all polar objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            polar objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            polar objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all polar objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            polar and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of polar objects to select.
            To select polar objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all polar objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            polar object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_polars(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_scenes(self, selector=None, row=None, col=None):
        """
        Select scene subplot objects from a particular subplot cell
        and/or scene subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            scene and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the scene
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("scene", selector, row, col)

    def for_each_scene(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all scene objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single scene object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            scene and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_scenes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all scene objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            scene objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            scene objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all scene objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            scene and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of scene objects to select.
            To select scene objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all scene objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            scene object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_scenes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_smiths(self, selector=None, row=None, col=None):
        """
        Select smith subplot objects from a particular subplot cell
        and/or smith subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            smith objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all smith objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            smith and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of smith objects to select.
            To select smith objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all smith objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the smith
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("smith", selector, row, col)

    def for_each_smith(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all smith objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single smith object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            smith objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all smith objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            smith and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of smith objects to select.
            To select smith objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all smith objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_smiths(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_smiths(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all smith objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            smith objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            smith objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all smith objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            smith and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of smith objects to select.
            To select smith objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all smith objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            smith object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_smiths(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_ternaries(self, selector=None, row=None, col=None):
        """
        Select ternary subplot objects from a particular subplot cell
        and/or ternary subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            ternary and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the ternary
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("ternary", selector, row, col)

    def for_each_ternary(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all ternary objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single ternary object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            ternary and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_ternaries(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all ternary objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            ternary objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            ternary objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all ternary objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            ternary and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of ternary objects to select.
            To select ternary objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all ternary objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            ternary object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_ternaries(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_xaxes(self, selector=None, row=None, col=None):
        """
        Select xaxis subplot objects from a particular subplot cell
        and/or xaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            xaxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        generator
            Generator that iterates through all of the xaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix("xaxis", selector, row, col)

    def for_each_xaxis(self, fn, selector=None, row=None, col=None) -> "FigureWidget":
        """
        Apply a function to all xaxis objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single xaxis object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            xaxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            fn(obj)

        return self

    def update_xaxes(
        self, patch=None, selector=None, overwrite=False, row=None, col=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all xaxis objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            xaxis objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            xaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all xaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            xaxis and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of xaxis objects to select.
            To select xaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all xaxis objects are selected.
        **kwargs
            Additional property updates to apply to each selected
            xaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_xaxes(selector=selector, row=row, col=col):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_yaxes(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select yaxis subplot objects from a particular subplot cell
        and/or yaxis subplot objects that satisfy custom selection
        criteria.

        Parameters
        ----------
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            yaxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition.

            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the yaxis
            objects that satisfy all of the specified selection criteria
        """

        return self._select_layout_subplots_by_prefix(
            "yaxis", selector, row, col, secondary_y=secondary_y
        )

    def for_each_yaxis(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ) -> "FigureWidget":
        """
        Apply a function to all yaxis objects that satisfy the
        specified selection criteria

        Parameters
        ----------
        fn:
            Function that inputs a single yaxis object.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            yaxis and those for which the function returned True will
            be in the selection.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition.

            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            fn(obj)

        return self

    def update_yaxes(
        self,
        patch=None,
        selector=None,
        overwrite=False,
        row=None,
        col=None,
        secondary_y=None,
        **kwargs,
    ) -> "FigureWidget":
        """
        Perform a property update operation on all yaxis objects
        that satisfy the specified selection criteria

        Parameters
        ----------
        patch: dict
            Dictionary of property updates to be applied to all
            yaxis objects that satisfy the selection criteria.
        selector: dict, function, or None (default None)
            Dict to use as selection criteria.
            yaxis objects will be selected if they contain
            properties corresponding to all of the dictionary's keys, with
            values that exactly match the supplied values. If None
            (the default), all yaxis objects are selected. If a
            function, it must be a function accepting a single argument and
            returning a boolean. The function will be called on each
            yaxis and those for which the function returned True will
            be in the selection.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        row, col: int or None (default None)
            Subplot row and column index of yaxis objects to select.
            To select yaxis objects by row and column, the Figure
            must have been created using plotly.subplots.make_subplots.
            If None (the default), all yaxis objects are selected.
        secondary_y: boolean or None (default None)
            * If True, only select yaxis objects associated with the secondary
              y-axis of the subplot.
            * If False, only select yaxis objects associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter yaxis objects based on
              a secondary y-axis condition.

            To select yaxis objects by secondary y-axis, the Figure must
            have been created using plotly.subplots.make_subplots. See
            the docstring for the specs argument to make_subplots for more
            info on creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected
            yaxis object. If a property is specified in
            both patch and in **kwargs then the one in **kwargs
            takes precedence.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self.select_yaxes(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            obj.update(patch, overwrite=overwrite, **kwargs)

        return self

    def select_annotations(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select annotations from a particular subplot cell and/or annotations
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str, or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each annotation and those for which the function returned True
            will be in the selection. If an int N, the Nth annotation matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotation that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the annotations that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "annotations", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_annotation(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all annotations that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single annotation object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each annotation and those for which the function returned True
            will be in the selection. If an int N, the Nth annotation matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotations that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="annotations",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_annotations(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all annotations that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all annotations that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all annotations are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each annotation and those for which the function returned True
            will be in the selection. If an int N, the Nth annotation matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of annotations to select.
            To select annotations by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            annotation that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all annotations are selected.
        secondary_y: boolean or None (default None)
            * If True, only select annotations associated with the secondary
              y-axis of the subplot.
            * If False, only select annotations associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter annotations based on secondary
              y-axis.

            To select annotations by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected annotation. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="annotations",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_annotation(
        self,
        arg=None,
        align=None,
        arrowcolor=None,
        arrowhead=None,
        arrowside=None,
        arrowsize=None,
        arrowwidth=None,
        ax=None,
        axref=None,
        ay=None,
        ayref=None,
        bgcolor=None,
        bordercolor=None,
        borderpad=None,
        borderwidth=None,
        captureevents=None,
        clicktoshow=None,
        font=None,
        height=None,
        hoverlabel=None,
        hovertext=None,
        name=None,
        opacity=None,
        showarrow=None,
        standoff=None,
        startarrowhead=None,
        startarrowsize=None,
        startstandoff=None,
        templateitemname=None,
        text=None,
        textangle=None,
        valign=None,
        visible=None,
        width=None,
        x=None,
        xanchor=None,
        xclick=None,
        xref=None,
        xshift=None,
        y=None,
        yanchor=None,
        yclick=None,
        yref=None,
        yshift=None,
        row=None,
        col=None,
        secondary_y=None,
        exclude_empty_subplots=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Annotation(
            arg,
            align=align,
            arrowcolor=arrowcolor,
            arrowhead=arrowhead,
            arrowside=arrowside,
            arrowsize=arrowsize,
            arrowwidth=arrowwidth,
            ax=ax,
            axref=axref,
            ay=ay,
            ayref=ayref,
            bgcolor=bgcolor,
            bordercolor=bordercolor,
            borderpad=borderpad,
            borderwidth=borderwidth,
            captureevents=captureevents,
            clicktoshow=clicktoshow,
            font=font,
            height=height,
            hoverlabel=hoverlabel,
            hovertext=hovertext,
            name=name,
            opacity=opacity,
            showarrow=showarrow,
            standoff=standoff,
            startarrowhead=startarrowhead,
            startarrowsize=startarrowsize,
            startstandoff=startstandoff,
            templateitemname=templateitemname,
            text=text,
            textangle=textangle,
            valign=valign,
            visible=visible,
            width=width,
            x=x,
            xanchor=xanchor,
            xclick=xclick,
            xref=xref,
            xshift=xshift,
            y=y,
            yanchor=yanchor,
            yclick=yclick,
            yref=yref,
            yshift=yshift,
            **kwargs,
        )
        return self._add_annotation_like(
            "annotation",
            "annotations",
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
            exclude_empty_subplots=exclude_empty_subplots,
        )

    def select_layout_images(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select images from a particular subplot cell and/or images
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str, or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each image and those for which the function returned True
            will be in the selection. If an int N, the Nth image matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            image that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the images that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "images", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_layout_image(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all images that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single image object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each image and those for which the function returned True
            will be in the selection. If an int N, the Nth image matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            images that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="images",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_layout_images(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all images that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all images that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all images are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each image and those for which the function returned True
            will be in the selection. If an int N, the Nth image matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of images to select.
            To select images by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            image that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all images are selected.
        secondary_y: boolean or None (default None)
            * If True, only select images associated with the secondary
              y-axis of the subplot.
            * If False, only select images associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter images based on secondary
              y-axis.

            To select images by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected image. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="images",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_layout_image(
        self,
        arg=None,
        layer=None,
        name=None,
        opacity=None,
        sizex=None,
        sizey=None,
        sizing=None,
        source=None,
        templateitemname=None,
        visible=None,
        x=None,
        xanchor=None,
        xref=None,
        y=None,
        yanchor=None,
        yref=None,
        row=None,
        col=None,
        secondary_y=None,
        exclude_empty_subplots=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Image(
            arg,
            layer=layer,
            name=name,
            opacity=opacity,
            sizex=sizex,
            sizey=sizey,
            sizing=sizing,
            source=source,
            templateitemname=templateitemname,
            visible=visible,
            x=x,
            xanchor=xanchor,
            xref=xref,
            y=y,
            yanchor=yanchor,
            yref=yref,
            **kwargs,
        )
        return self._add_annotation_like(
            "image",
            "images",
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
            exclude_empty_subplots=exclude_empty_subplots,
        )

    def select_selections(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select selections from a particular subplot cell and/or selections
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str, or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all selections are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each selection and those for which the function returned True
            will be in the selection. If an int N, the Nth selection matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of selections to select.
            To select selections by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            selection that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all selections are selected.
        secondary_y: boolean or None (default None)
            * If True, only select selections associated with the secondary
              y-axis of the subplot.
            * If False, only select selections associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter selections based on secondary
              y-axis.

            To select selections by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the selections that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "selections", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_selection(
        self, fn, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Apply a function to all selections that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single selection object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all selections are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each selection and those for which the function returned True
            will be in the selection. If an int N, the Nth selection matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of selections to select.
            To select selections by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            selections that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all selections are selected.
        secondary_y: boolean or None (default None)
            * If True, only select selections associated with the secondary
              y-axis of the subplot.
            * If False, only select selections associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter selections based on secondary
              y-axis.

            To select selections by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="selections",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_selections(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all selections that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all selections that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all selections are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each selection and those for which the function returned True
            will be in the selection. If an int N, the Nth selection matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of selections to select.
            To select selections by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            selection that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all selections are selected.
        secondary_y: boolean or None (default None)
            * If True, only select selections associated with the secondary
              y-axis of the subplot.
            * If False, only select selections associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter selections based on secondary
              y-axis.

            To select selections by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected selection. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="selections",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_selection(
        self,
        arg=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        templateitemname=None,
        type=None,
        x0=None,
        x1=None,
        xref=None,
        y0=None,
        y1=None,
        yref=None,
        row=None,
        col=None,
        secondary_y=None,
        exclude_empty_subplots=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Selection(
            arg,
            line=line,
            name=name,
            opacity=opacity,
            path=path,
            templateitemname=templateitemname,
            type=type,
            x0=x0,
            x1=x1,
            xref=xref,
            y0=y0,
            y1=y1,
            yref=yref,
            **kwargs,
        )
        return self._add_annotation_like(
            "selection",
            "selections",
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
            exclude_empty_subplots=exclude_empty_subplots,
        )

    def select_shapes(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select shapes from a particular subplot cell and/or shapes
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str, or None (default None)
            Dict to use as selection criteria.
            Annotations will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each shape and those for which the function returned True
            will be in the selection. If an int N, the Nth shape matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shape that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the shapes that satisfy
            all of the specified selection criteria
        """
        return self._select_annotations_like(
            "shapes", selector=selector, row=row, col=col, secondary_y=secondary_y
        )

    def for_each_shape(self, fn, selector=None, row=None, col=None, secondary_y=None):
        """
        Apply a function to all shapes that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single shape object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each shape and those for which the function returned True
            will be in the selection. If an int N, the Nth shape matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shapes that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="shapes",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            fn(obj)

        return self

    def update_shapes(
        self, patch=None, selector=None, row=None, col=None, secondary_y=None, **kwargs
    ) -> "FigureWidget":
        """
        Perform a property update operation on all shapes that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all shapes that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all shapes are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each shape and those for which the function returned True
            will be in the selection. If an int N, the Nth shape matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of shapes to select.
            To select shapes by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  To select only those
            shape that are in paper coordinates, set row and col to the
            string 'paper'.  If None (the default), all shapes are selected.
        secondary_y: boolean or None (default None)
            * If True, only select shapes associated with the secondary
              y-axis of the subplot.
            * If False, only select shapes associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter shapes based on secondary
              y-axis.

            To select shapes by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        **kwargs
            Additional property updates to apply to each selected shape. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the FigureWidget object that the method was called on
        """
        for obj in self._select_annotations_like(
            prop="shapes",
            selector=selector,
            row=row,
            col=col,
            secondary_y=secondary_y,
        ):
            obj.update(patch, **kwargs)

        return self

    def add_shape(
        self,
        arg=None,
        editable=None,
        fillcolor=None,
        fillrule=None,
        label=None,
        layer=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        name=None,
        opacity=None,
        path=None,
        showlegend=None,
        templateitemname=None,
        type=None,
        visible=None,
        x0=None,
        x0shift=None,
        x1=None,
        x1shift=None,
        xanchor=None,
        xref=None,
        xsizemode=None,
        y0=None,
        y0shift=None,
        y1=None,
        y1shift=None,
        yanchor=None,
        yref=None,
        ysizemode=None,
        row=None,
        col=None,
        secondary_y=None,
        exclude_empty_subplots=None,
        **kwargs,
    ) -> "FigureWidget":
        from plotly.graph_objs import layout as _layout

        new_obj = _layout.Shape(
            arg,
            editable=editable,
            fillcolor=fillcolor,
            fillrule=fillrule,
            label=label,
            layer=layer,
            legend=legend,
            legendgroup=legendgroup,
            legendgrouptitle=legendgrouptitle,
            legendrank=legendrank,
            legendwidth=legendwidth,
            line=line,
            name=name,
            opacity=opacity,
            path=path,
            showlegend=showlegend,
            templateitemname=templateitemname,
            type=type,
            visible=visible,
            x0=x0,
            x0shift=x0shift,
            x1=x1,
            x1shift=x1shift,
            xanchor=xanchor,
            xref=xref,
            xsizemode=xsizemode,
            y0=y0,
            y0shift=y0shift,
            y1=y1,
            y1shift=y1shift,
            yanchor=yanchor,
            yref=yref,
            ysizemode=ysizemode,
            **kwargs,
        )
        return self._add_annotation_like(
            "shape",
            "shapes",
            new_obj,
            row=row,
            col=col,
            secondary_y=secondary_y,
            exclude_empty_subplots=exclude_empty_subplots,
        )
