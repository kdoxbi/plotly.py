from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Geo(_BaseLayoutHierarchyType):

    _parent_path_str = "layout"
    _path_str = "layout.geo"
    _valid_props = {
        "bgcolor",
        "center",
        "coastlinecolor",
        "coastlinewidth",
        "countrycolor",
        "countrywidth",
        "domain",
        "fitbounds",
        "framecolor",
        "framewidth",
        "lakecolor",
        "landcolor",
        "lataxis",
        "lonaxis",
        "oceancolor",
        "projection",
        "resolution",
        "rivercolor",
        "riverwidth",
        "scope",
        "showcoastlines",
        "showcountries",
        "showframe",
        "showlakes",
        "showland",
        "showocean",
        "showrivers",
        "showsubunits",
        "subunitcolor",
        "subunitwidth",
        "uirevision",
        "visible",
    }

    @property
    def bgcolor(self):
        return self["bgcolor"]

    @bgcolor.setter
    def bgcolor(self, val):
        self["bgcolor"] = val

    @property
    def center(self):
        return self["center"]

    @center.setter
    def center(self, val):
        self["center"] = val

    @property
    def coastlinecolor(self):
        return self["coastlinecolor"]

    @coastlinecolor.setter
    def coastlinecolor(self, val):
        self["coastlinecolor"] = val

    @property
    def coastlinewidth(self):
        return self["coastlinewidth"]

    @coastlinewidth.setter
    def coastlinewidth(self, val):
        self["coastlinewidth"] = val

    @property
    def countrycolor(self):
        return self["countrycolor"]

    @countrycolor.setter
    def countrycolor(self, val):
        self["countrycolor"] = val

    @property
    def countrywidth(self):
        return self["countrywidth"]

    @countrywidth.setter
    def countrywidth(self, val):
        self["countrywidth"] = val

    @property
    def domain(self):
        return self["domain"]

    @domain.setter
    def domain(self, val):
        self["domain"] = val

    @property
    def fitbounds(self):
        return self["fitbounds"]

    @fitbounds.setter
    def fitbounds(self, val):
        self["fitbounds"] = val

    @property
    def framecolor(self):
        return self["framecolor"]

    @framecolor.setter
    def framecolor(self, val):
        self["framecolor"] = val

    @property
    def framewidth(self):
        return self["framewidth"]

    @framewidth.setter
    def framewidth(self, val):
        self["framewidth"] = val

    @property
    def lakecolor(self):
        return self["lakecolor"]

    @lakecolor.setter
    def lakecolor(self, val):
        self["lakecolor"] = val

    @property
    def landcolor(self):
        return self["landcolor"]

    @landcolor.setter
    def landcolor(self, val):
        self["landcolor"] = val

    @property
    def lataxis(self):
        return self["lataxis"]

    @lataxis.setter
    def lataxis(self, val):
        self["lataxis"] = val

    @property
    def lonaxis(self):
        return self["lonaxis"]

    @lonaxis.setter
    def lonaxis(self, val):
        self["lonaxis"] = val

    @property
    def oceancolor(self):
        return self["oceancolor"]

    @oceancolor.setter
    def oceancolor(self, val):
        self["oceancolor"] = val

    @property
    def projection(self):
        return self["projection"]

    @projection.setter
    def projection(self, val):
        self["projection"] = val

    @property
    def resolution(self):
        return self["resolution"]

    @resolution.setter
    def resolution(self, val):
        self["resolution"] = val

    @property
    def rivercolor(self):
        return self["rivercolor"]

    @rivercolor.setter
    def rivercolor(self, val):
        self["rivercolor"] = val

    @property
    def riverwidth(self):
        return self["riverwidth"]

    @riverwidth.setter
    def riverwidth(self, val):
        self["riverwidth"] = val

    @property
    def scope(self):
        return self["scope"]

    @scope.setter
    def scope(self, val):
        self["scope"] = val

    @property
    def showcoastlines(self):
        return self["showcoastlines"]

    @showcoastlines.setter
    def showcoastlines(self, val):
        self["showcoastlines"] = val

    @property
    def showcountries(self):
        return self["showcountries"]

    @showcountries.setter
    def showcountries(self, val):
        self["showcountries"] = val

    @property
    def showframe(self):
        return self["showframe"]

    @showframe.setter
    def showframe(self, val):
        self["showframe"] = val

    @property
    def showlakes(self):
        return self["showlakes"]

    @showlakes.setter
    def showlakes(self, val):
        self["showlakes"] = val

    @property
    def showland(self):
        return self["showland"]

    @showland.setter
    def showland(self, val):
        self["showland"] = val

    @property
    def showocean(self):
        return self["showocean"]

    @showocean.setter
    def showocean(self, val):
        self["showocean"] = val

    @property
    def showrivers(self):
        return self["showrivers"]

    @showrivers.setter
    def showrivers(self, val):
        self["showrivers"] = val

    @property
    def showsubunits(self):
        return self["showsubunits"]

    @showsubunits.setter
    def showsubunits(self, val):
        self["showsubunits"] = val

    @property
    def subunitcolor(self):
        return self["subunitcolor"]

    @subunitcolor.setter
    def subunitcolor(self, val):
        self["subunitcolor"] = val

    @property
    def subunitwidth(self):
        return self["subunitwidth"]

    @subunitwidth.setter
    def subunitwidth(self, val):
        self["subunitwidth"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def visible(self):
        return self["visible"]

    @visible.setter
    def visible(self, val):
        self["visible"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        bgcolor=None,
        center=None,
        coastlinecolor=None,
        coastlinewidth=None,
        countrycolor=None,
        countrywidth=None,
        domain=None,
        fitbounds=None,
        framecolor=None,
        framewidth=None,
        lakecolor=None,
        landcolor=None,
        lataxis=None,
        lonaxis=None,
        oceancolor=None,
        projection=None,
        resolution=None,
        rivercolor=None,
        riverwidth=None,
        scope=None,
        showcoastlines=None,
        showcountries=None,
        showframe=None,
        showlakes=None,
        showland=None,
        showocean=None,
        showrivers=None,
        showsubunits=None,
        subunitcolor=None,
        subunitwidth=None,
        uirevision=None,
        visible=None,
        **kwargs,
    ):
        super(Geo, self).__init__("geo")

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
The first argument to the plotly.graph_objs.layout.Geo
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Geo`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("bgcolor", None)
        _v = bgcolor if bgcolor is not None else _v
        if _v is not None:
            self["bgcolor"] = _v
        _v = arg.pop("center", None)
        _v = center if center is not None else _v
        if _v is not None:
            self["center"] = _v
        _v = arg.pop("coastlinecolor", None)
        _v = coastlinecolor if coastlinecolor is not None else _v
        if _v is not None:
            self["coastlinecolor"] = _v
        _v = arg.pop("coastlinewidth", None)
        _v = coastlinewidth if coastlinewidth is not None else _v
        if _v is not None:
            self["coastlinewidth"] = _v
        _v = arg.pop("countrycolor", None)
        _v = countrycolor if countrycolor is not None else _v
        if _v is not None:
            self["countrycolor"] = _v
        _v = arg.pop("countrywidth", None)
        _v = countrywidth if countrywidth is not None else _v
        if _v is not None:
            self["countrywidth"] = _v
        _v = arg.pop("domain", None)
        _v = domain if domain is not None else _v
        if _v is not None:
            self["domain"] = _v
        _v = arg.pop("fitbounds", None)
        _v = fitbounds if fitbounds is not None else _v
        if _v is not None:
            self["fitbounds"] = _v
        _v = arg.pop("framecolor", None)
        _v = framecolor if framecolor is not None else _v
        if _v is not None:
            self["framecolor"] = _v
        _v = arg.pop("framewidth", None)
        _v = framewidth if framewidth is not None else _v
        if _v is not None:
            self["framewidth"] = _v
        _v = arg.pop("lakecolor", None)
        _v = lakecolor if lakecolor is not None else _v
        if _v is not None:
            self["lakecolor"] = _v
        _v = arg.pop("landcolor", None)
        _v = landcolor if landcolor is not None else _v
        if _v is not None:
            self["landcolor"] = _v
        _v = arg.pop("lataxis", None)
        _v = lataxis if lataxis is not None else _v
        if _v is not None:
            self["lataxis"] = _v
        _v = arg.pop("lonaxis", None)
        _v = lonaxis if lonaxis is not None else _v
        if _v is not None:
            self["lonaxis"] = _v
        _v = arg.pop("oceancolor", None)
        _v = oceancolor if oceancolor is not None else _v
        if _v is not None:
            self["oceancolor"] = _v
        _v = arg.pop("projection", None)
        _v = projection if projection is not None else _v
        if _v is not None:
            self["projection"] = _v
        _v = arg.pop("resolution", None)
        _v = resolution if resolution is not None else _v
        if _v is not None:
            self["resolution"] = _v
        _v = arg.pop("rivercolor", None)
        _v = rivercolor if rivercolor is not None else _v
        if _v is not None:
            self["rivercolor"] = _v
        _v = arg.pop("riverwidth", None)
        _v = riverwidth if riverwidth is not None else _v
        if _v is not None:
            self["riverwidth"] = _v
        _v = arg.pop("scope", None)
        _v = scope if scope is not None else _v
        if _v is not None:
            self["scope"] = _v
        _v = arg.pop("showcoastlines", None)
        _v = showcoastlines if showcoastlines is not None else _v
        if _v is not None:
            self["showcoastlines"] = _v
        _v = arg.pop("showcountries", None)
        _v = showcountries if showcountries is not None else _v
        if _v is not None:
            self["showcountries"] = _v
        _v = arg.pop("showframe", None)
        _v = showframe if showframe is not None else _v
        if _v is not None:
            self["showframe"] = _v
        _v = arg.pop("showlakes", None)
        _v = showlakes if showlakes is not None else _v
        if _v is not None:
            self["showlakes"] = _v
        _v = arg.pop("showland", None)
        _v = showland if showland is not None else _v
        if _v is not None:
            self["showland"] = _v
        _v = arg.pop("showocean", None)
        _v = showocean if showocean is not None else _v
        if _v is not None:
            self["showocean"] = _v
        _v = arg.pop("showrivers", None)
        _v = showrivers if showrivers is not None else _v
        if _v is not None:
            self["showrivers"] = _v
        _v = arg.pop("showsubunits", None)
        _v = showsubunits if showsubunits is not None else _v
        if _v is not None:
            self["showsubunits"] = _v
        _v = arg.pop("subunitcolor", None)
        _v = subunitcolor if subunitcolor is not None else _v
        if _v is not None:
            self["subunitcolor"] = _v
        _v = arg.pop("subunitwidth", None)
        _v = subunitwidth if subunitwidth is not None else _v
        if _v is not None:
            self["subunitwidth"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("visible", None)
        _v = visible if visible is not None else _v
        if _v is not None:
            self["visible"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
