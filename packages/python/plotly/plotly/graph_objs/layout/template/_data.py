from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Data(_BaseLayoutHierarchyType):

    _parent_path_str = "layout.template"
    _path_str = "layout.template.data"
    _valid_props = {
        "bar",
        "barpolar",
        "box",
        "candlestick",
        "carpet",
        "choropleth",
        "choroplethmap",
        "choroplethmapbox",
        "cone",
        "contour",
        "contourcarpet",
        "densitymap",
        "densitymapbox",
        "funnel",
        "funnelarea",
        "heatmap",
        "histogram",
        "histogram2d",
        "histogram2dcontour",
        "icicle",
        "image",
        "indicator",
        "isosurface",
        "mesh3d",
        "ohlc",
        "parcats",
        "parcoords",
        "pie",
        "sankey",
        "scatter",
        "scatter3d",
        "scattercarpet",
        "scattergeo",
        "scattergl",
        "scattermap",
        "scattermapbox",
        "scatterpolar",
        "scatterpolargl",
        "scattersmith",
        "scatterternary",
        "splom",
        "streamtube",
        "sunburst",
        "surface",
        "table",
        "treemap",
        "violin",
        "volume",
        "waterfall",
    }

    @property
    def barpolar(self):
        return self["barpolar"]

    @barpolar.setter
    def barpolar(self, val):
        self["barpolar"] = val

    @property
    def bar(self):
        return self["bar"]

    @bar.setter
    def bar(self, val):
        self["bar"] = val

    @property
    def box(self):
        return self["box"]

    @box.setter
    def box(self, val):
        self["box"] = val

    @property
    def candlestick(self):
        return self["candlestick"]

    @candlestick.setter
    def candlestick(self, val):
        self["candlestick"] = val

    @property
    def carpet(self):
        return self["carpet"]

    @carpet.setter
    def carpet(self, val):
        self["carpet"] = val

    @property
    def choroplethmapbox(self):
        return self["choroplethmapbox"]

    @choroplethmapbox.setter
    def choroplethmapbox(self, val):
        self["choroplethmapbox"] = val

    @property
    def choroplethmap(self):
        return self["choroplethmap"]

    @choroplethmap.setter
    def choroplethmap(self, val):
        self["choroplethmap"] = val

    @property
    def choropleth(self):
        return self["choropleth"]

    @choropleth.setter
    def choropleth(self, val):
        self["choropleth"] = val

    @property
    def cone(self):
        return self["cone"]

    @cone.setter
    def cone(self, val):
        self["cone"] = val

    @property
    def contourcarpet(self):
        return self["contourcarpet"]

    @contourcarpet.setter
    def contourcarpet(self, val):
        self["contourcarpet"] = val

    @property
    def contour(self):
        return self["contour"]

    @contour.setter
    def contour(self, val):
        self["contour"] = val

    @property
    def densitymapbox(self):
        return self["densitymapbox"]

    @densitymapbox.setter
    def densitymapbox(self, val):
        self["densitymapbox"] = val

    @property
    def densitymap(self):
        return self["densitymap"]

    @densitymap.setter
    def densitymap(self, val):
        self["densitymap"] = val

    @property
    def funnelarea(self):
        return self["funnelarea"]

    @funnelarea.setter
    def funnelarea(self, val):
        self["funnelarea"] = val

    @property
    def funnel(self):
        return self["funnel"]

    @funnel.setter
    def funnel(self, val):
        self["funnel"] = val

    @property
    def heatmap(self):
        return self["heatmap"]

    @heatmap.setter
    def heatmap(self, val):
        self["heatmap"] = val

    @property
    def histogram2dcontour(self):
        return self["histogram2dcontour"]

    @histogram2dcontour.setter
    def histogram2dcontour(self, val):
        self["histogram2dcontour"] = val

    @property
    def histogram2d(self):
        return self["histogram2d"]

    @histogram2d.setter
    def histogram2d(self, val):
        self["histogram2d"] = val

    @property
    def histogram(self):
        return self["histogram"]

    @histogram.setter
    def histogram(self, val):
        self["histogram"] = val

    @property
    def icicle(self):
        return self["icicle"]

    @icicle.setter
    def icicle(self, val):
        self["icicle"] = val

    @property
    def image(self):
        return self["image"]

    @image.setter
    def image(self, val):
        self["image"] = val

    @property
    def indicator(self):
        return self["indicator"]

    @indicator.setter
    def indicator(self, val):
        self["indicator"] = val

    @property
    def isosurface(self):
        return self["isosurface"]

    @isosurface.setter
    def isosurface(self, val):
        self["isosurface"] = val

    @property
    def mesh3d(self):
        return self["mesh3d"]

    @mesh3d.setter
    def mesh3d(self, val):
        self["mesh3d"] = val

    @property
    def ohlc(self):
        return self["ohlc"]

    @ohlc.setter
    def ohlc(self, val):
        self["ohlc"] = val

    @property
    def parcats(self):
        return self["parcats"]

    @parcats.setter
    def parcats(self, val):
        self["parcats"] = val

    @property
    def parcoords(self):
        return self["parcoords"]

    @parcoords.setter
    def parcoords(self, val):
        self["parcoords"] = val

    @property
    def pie(self):
        return self["pie"]

    @pie.setter
    def pie(self, val):
        self["pie"] = val

    @property
    def sankey(self):
        return self["sankey"]

    @sankey.setter
    def sankey(self, val):
        self["sankey"] = val

    @property
    def scatter3d(self):
        return self["scatter3d"]

    @scatter3d.setter
    def scatter3d(self, val):
        self["scatter3d"] = val

    @property
    def scattercarpet(self):
        return self["scattercarpet"]

    @scattercarpet.setter
    def scattercarpet(self, val):
        self["scattercarpet"] = val

    @property
    def scattergeo(self):
        return self["scattergeo"]

    @scattergeo.setter
    def scattergeo(self, val):
        self["scattergeo"] = val

    @property
    def scattergl(self):
        return self["scattergl"]

    @scattergl.setter
    def scattergl(self, val):
        self["scattergl"] = val

    @property
    def scattermapbox(self):
        return self["scattermapbox"]

    @scattermapbox.setter
    def scattermapbox(self, val):
        self["scattermapbox"] = val

    @property
    def scattermap(self):
        return self["scattermap"]

    @scattermap.setter
    def scattermap(self, val):
        self["scattermap"] = val

    @property
    def scatterpolargl(self):
        return self["scatterpolargl"]

    @scatterpolargl.setter
    def scatterpolargl(self, val):
        self["scatterpolargl"] = val

    @property
    def scatterpolar(self):
        return self["scatterpolar"]

    @scatterpolar.setter
    def scatterpolar(self, val):
        self["scatterpolar"] = val

    @property
    def scatter(self):
        return self["scatter"]

    @scatter.setter
    def scatter(self, val):
        self["scatter"] = val

    @property
    def scattersmith(self):
        return self["scattersmith"]

    @scattersmith.setter
    def scattersmith(self, val):
        self["scattersmith"] = val

    @property
    def scatterternary(self):
        return self["scatterternary"]

    @scatterternary.setter
    def scatterternary(self, val):
        self["scatterternary"] = val

    @property
    def splom(self):
        return self["splom"]

    @splom.setter
    def splom(self, val):
        self["splom"] = val

    @property
    def streamtube(self):
        return self["streamtube"]

    @streamtube.setter
    def streamtube(self, val):
        self["streamtube"] = val

    @property
    def sunburst(self):
        return self["sunburst"]

    @sunburst.setter
    def sunburst(self, val):
        self["sunburst"] = val

    @property
    def surface(self):
        return self["surface"]

    @surface.setter
    def surface(self, val):
        self["surface"] = val

    @property
    def table(self):
        return self["table"]

    @table.setter
    def table(self, val):
        self["table"] = val

    @property
    def treemap(self):
        return self["treemap"]

    @treemap.setter
    def treemap(self, val):
        self["treemap"] = val

    @property
    def violin(self):
        return self["violin"]

    @violin.setter
    def violin(self, val):
        self["violin"] = val

    @property
    def volume(self):
        return self["volume"]

    @volume.setter
    def volume(self, val):
        self["volume"] = val

    @property
    def waterfall(self):
        return self["waterfall"]

    @waterfall.setter
    def waterfall(self, val):
        self["waterfall"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        barpolar=None,
        bar=None,
        box=None,
        candlestick=None,
        carpet=None,
        choroplethmapbox=None,
        choroplethmap=None,
        choropleth=None,
        cone=None,
        contourcarpet=None,
        contour=None,
        densitymapbox=None,
        densitymap=None,
        funnelarea=None,
        funnel=None,
        heatmap=None,
        histogram2dcontour=None,
        histogram2d=None,
        histogram=None,
        icicle=None,
        image=None,
        indicator=None,
        isosurface=None,
        mesh3d=None,
        ohlc=None,
        parcats=None,
        parcoords=None,
        pie=None,
        sankey=None,
        scatter3d=None,
        scattercarpet=None,
        scattergeo=None,
        scattergl=None,
        scattermapbox=None,
        scattermap=None,
        scatterpolargl=None,
        scatterpolar=None,
        scatter=None,
        scattersmith=None,
        scatterternary=None,
        splom=None,
        streamtube=None,
        sunburst=None,
        surface=None,
        table=None,
        treemap=None,
        violin=None,
        volume=None,
        waterfall=None,
        **kwargs,
    ):
        super(Data, self).__init__("data")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.template.Data
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.template.Data`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("barpolar", None)
        _v = barpolar if barpolar is not None else _v
        if _v is not None:
            self["barpolar"] = _v
        _v = arg.pop("bar", None)
        _v = bar if bar is not None else _v
        if _v is not None:
            self["bar"] = _v
        _v = arg.pop("box", None)
        _v = box if box is not None else _v
        if _v is not None:
            self["box"] = _v
        _v = arg.pop("candlestick", None)
        _v = candlestick if candlestick is not None else _v
        if _v is not None:
            self["candlestick"] = _v
        _v = arg.pop("carpet", None)
        _v = carpet if carpet is not None else _v
        if _v is not None:
            self["carpet"] = _v
        _v = arg.pop("choroplethmapbox", None)
        _v = choroplethmapbox if choroplethmapbox is not None else _v
        if _v is not None:
            self["choroplethmapbox"] = _v
        _v = arg.pop("choroplethmap", None)
        _v = choroplethmap if choroplethmap is not None else _v
        if _v is not None:
            self["choroplethmap"] = _v
        _v = arg.pop("choropleth", None)
        _v = choropleth if choropleth is not None else _v
        if _v is not None:
            self["choropleth"] = _v
        _v = arg.pop("cone", None)
        _v = cone if cone is not None else _v
        if _v is not None:
            self["cone"] = _v
        _v = arg.pop("contourcarpet", None)
        _v = contourcarpet if contourcarpet is not None else _v
        if _v is not None:
            self["contourcarpet"] = _v
        _v = arg.pop("contour", None)
        _v = contour if contour is not None else _v
        if _v is not None:
            self["contour"] = _v
        _v = arg.pop("densitymapbox", None)
        _v = densitymapbox if densitymapbox is not None else _v
        if _v is not None:
            self["densitymapbox"] = _v
        _v = arg.pop("densitymap", None)
        _v = densitymap if densitymap is not None else _v
        if _v is not None:
            self["densitymap"] = _v
        _v = arg.pop("funnelarea", None)
        _v = funnelarea if funnelarea is not None else _v
        if _v is not None:
            self["funnelarea"] = _v
        _v = arg.pop("funnel", None)
        _v = funnel if funnel is not None else _v
        if _v is not None:
            self["funnel"] = _v
        _v = arg.pop("heatmap", None)
        _v = heatmap if heatmap is not None else _v
        if _v is not None:
            self["heatmap"] = _v
        _v = arg.pop("histogram2dcontour", None)
        _v = histogram2dcontour if histogram2dcontour is not None else _v
        if _v is not None:
            self["histogram2dcontour"] = _v
        _v = arg.pop("histogram2d", None)
        _v = histogram2d if histogram2d is not None else _v
        if _v is not None:
            self["histogram2d"] = _v
        _v = arg.pop("histogram", None)
        _v = histogram if histogram is not None else _v
        if _v is not None:
            self["histogram"] = _v
        _v = arg.pop("icicle", None)
        _v = icicle if icicle is not None else _v
        if _v is not None:
            self["icicle"] = _v
        _v = arg.pop("image", None)
        _v = image if image is not None else _v
        if _v is not None:
            self["image"] = _v
        _v = arg.pop("indicator", None)
        _v = indicator if indicator is not None else _v
        if _v is not None:
            self["indicator"] = _v
        _v = arg.pop("isosurface", None)
        _v = isosurface if isosurface is not None else _v
        if _v is not None:
            self["isosurface"] = _v
        _v = arg.pop("mesh3d", None)
        _v = mesh3d if mesh3d is not None else _v
        if _v is not None:
            self["mesh3d"] = _v
        _v = arg.pop("ohlc", None)
        _v = ohlc if ohlc is not None else _v
        if _v is not None:
            self["ohlc"] = _v
        _v = arg.pop("parcats", None)
        _v = parcats if parcats is not None else _v
        if _v is not None:
            self["parcats"] = _v
        _v = arg.pop("parcoords", None)
        _v = parcoords if parcoords is not None else _v
        if _v is not None:
            self["parcoords"] = _v
        _v = arg.pop("pie", None)
        _v = pie if pie is not None else _v
        if _v is not None:
            self["pie"] = _v
        _v = arg.pop("sankey", None)
        _v = sankey if sankey is not None else _v
        if _v is not None:
            self["sankey"] = _v
        _v = arg.pop("scatter3d", None)
        _v = scatter3d if scatter3d is not None else _v
        if _v is not None:
            self["scatter3d"] = _v
        _v = arg.pop("scattercarpet", None)
        _v = scattercarpet if scattercarpet is not None else _v
        if _v is not None:
            self["scattercarpet"] = _v
        _v = arg.pop("scattergeo", None)
        _v = scattergeo if scattergeo is not None else _v
        if _v is not None:
            self["scattergeo"] = _v
        _v = arg.pop("scattergl", None)
        _v = scattergl if scattergl is not None else _v
        if _v is not None:
            self["scattergl"] = _v
        _v = arg.pop("scattermapbox", None)
        _v = scattermapbox if scattermapbox is not None else _v
        if _v is not None:
            self["scattermapbox"] = _v
        _v = arg.pop("scattermap", None)
        _v = scattermap if scattermap is not None else _v
        if _v is not None:
            self["scattermap"] = _v
        _v = arg.pop("scatterpolargl", None)
        _v = scatterpolargl if scatterpolargl is not None else _v
        if _v is not None:
            self["scatterpolargl"] = _v
        _v = arg.pop("scatterpolar", None)
        _v = scatterpolar if scatterpolar is not None else _v
        if _v is not None:
            self["scatterpolar"] = _v
        _v = arg.pop("scatter", None)
        _v = scatter if scatter is not None else _v
        if _v is not None:
            self["scatter"] = _v
        _v = arg.pop("scattersmith", None)
        _v = scattersmith if scattersmith is not None else _v
        if _v is not None:
            self["scattersmith"] = _v
        _v = arg.pop("scatterternary", None)
        _v = scatterternary if scatterternary is not None else _v
        if _v is not None:
            self["scatterternary"] = _v
        _v = arg.pop("splom", None)
        _v = splom if splom is not None else _v
        if _v is not None:
            self["splom"] = _v
        _v = arg.pop("streamtube", None)
        _v = streamtube if streamtube is not None else _v
        if _v is not None:
            self["streamtube"] = _v
        _v = arg.pop("sunburst", None)
        _v = sunburst if sunburst is not None else _v
        if _v is not None:
            self["sunburst"] = _v
        _v = arg.pop("surface", None)
        _v = surface if surface is not None else _v
        if _v is not None:
            self["surface"] = _v
        _v = arg.pop("table", None)
        _v = table if table is not None else _v
        if _v is not None:
            self["table"] = _v
        _v = arg.pop("treemap", None)
        _v = treemap if treemap is not None else _v
        if _v is not None:
            self["treemap"] = _v
        _v = arg.pop("violin", None)
        _v = violin if violin is not None else _v
        if _v is not None:
            self["violin"] = _v
        _v = arg.pop("volume", None)
        _v = volume if volume is not None else _v
        if _v is not None:
            self["volume"] = _v
        _v = arg.pop("waterfall", None)
        _v = waterfall if waterfall is not None else _v
        if _v is not None:
            self["waterfall"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
