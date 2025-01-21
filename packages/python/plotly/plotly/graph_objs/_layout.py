from plotly.basedatatypes import BaseLayoutType as _BaseLayoutType
import copy as _copy


class Layout(_BaseLayoutType):

    _subplotid_prop_names = [
        "coloraxis",
        "geo",
        "legend",
        "map",
        "mapbox",
        "polar",
        "scene",
        "smith",
        "ternary",
        "xaxis",
        "yaxis",
    ]

    import re

    _subplotid_prop_re = re.compile("^(" + "|".join(_subplotid_prop_names) + r")(\d+)$")

    @property
    def _subplotid_validators(self):
        from plotly.validators.layout import (
            ColoraxisValidator,
            GeoValidator,
            LegendValidator,
            MapValidator,
            MapboxValidator,
            PolarValidator,
            SceneValidator,
            SmithValidator,
            TernaryValidator,
            XaxisValidator,
            YaxisValidator,
        )

        return {
            "coloraxis": ColoraxisValidator,
            "geo": GeoValidator,
            "legend": LegendValidator,
            "map": MapValidator,
            "mapbox": MapboxValidator,
            "polar": PolarValidator,
            "scene": SceneValidator,
            "smith": SmithValidator,
            "ternary": TernaryValidator,
            "xaxis": XaxisValidator,
            "yaxis": YaxisValidator,
        }

    def _subplot_re_match(self, prop):
        return self._subplotid_prop_re.match(prop)

    _parent_path_str = ""
    _path_str = "layout"
    _valid_props = {
        "activeselection",
        "activeshape",
        "annotationdefaults",
        "annotations",
        "autosize",
        "autotypenumbers",
        "barcornerradius",
        "bargap",
        "bargroupgap",
        "barmode",
        "barnorm",
        "boxgap",
        "boxgroupgap",
        "boxmode",
        "calendar",
        "clickmode",
        "coloraxis",
        "colorscale",
        "colorway",
        "computed",
        "datarevision",
        "dragmode",
        "editrevision",
        "extendfunnelareacolors",
        "extendiciclecolors",
        "extendpiecolors",
        "extendsunburstcolors",
        "extendtreemapcolors",
        "font",
        "funnelareacolorway",
        "funnelgap",
        "funnelgroupgap",
        "funnelmode",
        "geo",
        "grid",
        "height",
        "hiddenlabels",
        "hiddenlabelssrc",
        "hidesources",
        "hoverdistance",
        "hoverlabel",
        "hovermode",
        "hoversubplots",
        "iciclecolorway",
        "imagedefaults",
        "images",
        "legend",
        "map",
        "mapbox",
        "margin",
        "meta",
        "metasrc",
        "minreducedheight",
        "minreducedwidth",
        "modebar",
        "newselection",
        "newshape",
        "paper_bgcolor",
        "piecolorway",
        "plot_bgcolor",
        "polar",
        "scattergap",
        "scattermode",
        "scene",
        "selectdirection",
        "selectiondefaults",
        "selectionrevision",
        "selections",
        "separators",
        "shapedefaults",
        "shapes",
        "showlegend",
        "sliderdefaults",
        "sliders",
        "smith",
        "spikedistance",
        "sunburstcolorway",
        "template",
        "ternary",
        "title",
        "transition",
        "treemapcolorway",
        "uirevision",
        "uniformtext",
        "updatemenudefaults",
        "updatemenus",
        "violingap",
        "violingroupgap",
        "violinmode",
        "waterfallgap",
        "waterfallgroupgap",
        "waterfallmode",
        "width",
        "xaxis",
        "yaxis",
    }

    @property
    def activeselection(self):
        return self["activeselection"]

    @activeselection.setter
    def activeselection(self, val):
        self["activeselection"] = val

    @property
    def activeshape(self):
        return self["activeshape"]

    @activeshape.setter
    def activeshape(self, val):
        self["activeshape"] = val

    @property
    def annotations(self):
        return self["annotations"]

    @annotations.setter
    def annotations(self, val):
        self["annotations"] = val

    @property
    def annotationdefaults(self):
        return self["annotationdefaults"]

    @annotationdefaults.setter
    def annotationdefaults(self, val):
        self["annotationdefaults"] = val

    @property
    def autosize(self):
        return self["autosize"]

    @autosize.setter
    def autosize(self, val):
        self["autosize"] = val

    @property
    def autotypenumbers(self):
        return self["autotypenumbers"]

    @autotypenumbers.setter
    def autotypenumbers(self, val):
        self["autotypenumbers"] = val

    @property
    def barcornerradius(self):
        return self["barcornerradius"]

    @barcornerradius.setter
    def barcornerradius(self, val):
        self["barcornerradius"] = val

    @property
    def bargap(self):
        return self["bargap"]

    @bargap.setter
    def bargap(self, val):
        self["bargap"] = val

    @property
    def bargroupgap(self):
        return self["bargroupgap"]

    @bargroupgap.setter
    def bargroupgap(self, val):
        self["bargroupgap"] = val

    @property
    def barmode(self):
        return self["barmode"]

    @barmode.setter
    def barmode(self, val):
        self["barmode"] = val

    @property
    def barnorm(self):
        return self["barnorm"]

    @barnorm.setter
    def barnorm(self, val):
        self["barnorm"] = val

    @property
    def boxgap(self):
        return self["boxgap"]

    @boxgap.setter
    def boxgap(self, val):
        self["boxgap"] = val

    @property
    def boxgroupgap(self):
        return self["boxgroupgap"]

    @boxgroupgap.setter
    def boxgroupgap(self, val):
        self["boxgroupgap"] = val

    @property
    def boxmode(self):
        return self["boxmode"]

    @boxmode.setter
    def boxmode(self, val):
        self["boxmode"] = val

    @property
    def calendar(self):
        return self["calendar"]

    @calendar.setter
    def calendar(self, val):
        self["calendar"] = val

    @property
    def clickmode(self):
        return self["clickmode"]

    @clickmode.setter
    def clickmode(self, val):
        self["clickmode"] = val

    @property
    def coloraxis(self):
        return self["coloraxis"]

    @coloraxis.setter
    def coloraxis(self, val):
        self["coloraxis"] = val

    @property
    def colorscale(self):
        return self["colorscale"]

    @colorscale.setter
    def colorscale(self, val):
        self["colorscale"] = val

    @property
    def colorway(self):
        return self["colorway"]

    @colorway.setter
    def colorway(self, val):
        self["colorway"] = val

    @property
    def computed(self):
        return self["computed"]

    @computed.setter
    def computed(self, val):
        self["computed"] = val

    @property
    def datarevision(self):
        return self["datarevision"]

    @datarevision.setter
    def datarevision(self, val):
        self["datarevision"] = val

    @property
    def dragmode(self):
        return self["dragmode"]

    @dragmode.setter
    def dragmode(self, val):
        self["dragmode"] = val

    @property
    def editrevision(self):
        return self["editrevision"]

    @editrevision.setter
    def editrevision(self, val):
        self["editrevision"] = val

    @property
    def extendfunnelareacolors(self):
        return self["extendfunnelareacolors"]

    @extendfunnelareacolors.setter
    def extendfunnelareacolors(self, val):
        self["extendfunnelareacolors"] = val

    @property
    def extendiciclecolors(self):
        return self["extendiciclecolors"]

    @extendiciclecolors.setter
    def extendiciclecolors(self, val):
        self["extendiciclecolors"] = val

    @property
    def extendpiecolors(self):
        return self["extendpiecolors"]

    @extendpiecolors.setter
    def extendpiecolors(self, val):
        self["extendpiecolors"] = val

    @property
    def extendsunburstcolors(self):
        return self["extendsunburstcolors"]

    @extendsunburstcolors.setter
    def extendsunburstcolors(self, val):
        self["extendsunburstcolors"] = val

    @property
    def extendtreemapcolors(self):
        return self["extendtreemapcolors"]

    @extendtreemapcolors.setter
    def extendtreemapcolors(self, val):
        self["extendtreemapcolors"] = val

    @property
    def font(self):
        return self["font"]

    @font.setter
    def font(self, val):
        self["font"] = val

    @property
    def funnelareacolorway(self):
        return self["funnelareacolorway"]

    @funnelareacolorway.setter
    def funnelareacolorway(self, val):
        self["funnelareacolorway"] = val

    @property
    def funnelgap(self):
        return self["funnelgap"]

    @funnelgap.setter
    def funnelgap(self, val):
        self["funnelgap"] = val

    @property
    def funnelgroupgap(self):
        return self["funnelgroupgap"]

    @funnelgroupgap.setter
    def funnelgroupgap(self, val):
        self["funnelgroupgap"] = val

    @property
    def funnelmode(self):
        return self["funnelmode"]

    @funnelmode.setter
    def funnelmode(self, val):
        self["funnelmode"] = val

    @property
    def geo(self):
        return self["geo"]

    @geo.setter
    def geo(self, val):
        self["geo"] = val

    @property
    def grid(self):
        return self["grid"]

    @grid.setter
    def grid(self, val):
        self["grid"] = val

    @property
    def height(self):
        return self["height"]

    @height.setter
    def height(self, val):
        self["height"] = val

    @property
    def hiddenlabels(self):
        return self["hiddenlabels"]

    @hiddenlabels.setter
    def hiddenlabels(self, val):
        self["hiddenlabels"] = val

    @property
    def hiddenlabelssrc(self):
        return self["hiddenlabelssrc"]

    @hiddenlabelssrc.setter
    def hiddenlabelssrc(self, val):
        self["hiddenlabelssrc"] = val

    @property
    def hidesources(self):
        return self["hidesources"]

    @hidesources.setter
    def hidesources(self, val):
        self["hidesources"] = val

    @property
    def hoverdistance(self):
        return self["hoverdistance"]

    @hoverdistance.setter
    def hoverdistance(self, val):
        self["hoverdistance"] = val

    @property
    def hoverlabel(self):
        return self["hoverlabel"]

    @hoverlabel.setter
    def hoverlabel(self, val):
        self["hoverlabel"] = val

    @property
    def hovermode(self):
        return self["hovermode"]

    @hovermode.setter
    def hovermode(self, val):
        self["hovermode"] = val

    @property
    def hoversubplots(self):
        return self["hoversubplots"]

    @hoversubplots.setter
    def hoversubplots(self, val):
        self["hoversubplots"] = val

    @property
    def iciclecolorway(self):
        return self["iciclecolorway"]

    @iciclecolorway.setter
    def iciclecolorway(self, val):
        self["iciclecolorway"] = val

    @property
    def images(self):
        return self["images"]

    @images.setter
    def images(self, val):
        self["images"] = val

    @property
    def imagedefaults(self):
        return self["imagedefaults"]

    @imagedefaults.setter
    def imagedefaults(self, val):
        self["imagedefaults"] = val

    @property
    def legend(self):
        return self["legend"]

    @legend.setter
    def legend(self, val):
        self["legend"] = val

    @property
    def map(self):
        return self["map"]

    @map.setter
    def map(self, val):
        self["map"] = val

    @property
    def mapbox(self):
        return self["mapbox"]

    @mapbox.setter
    def mapbox(self, val):
        self["mapbox"] = val

    @property
    def margin(self):
        return self["margin"]

    @margin.setter
    def margin(self, val):
        self["margin"] = val

    @property
    def meta(self):
        return self["meta"]

    @meta.setter
    def meta(self, val):
        self["meta"] = val

    @property
    def metasrc(self):
        return self["metasrc"]

    @metasrc.setter
    def metasrc(self, val):
        self["metasrc"] = val

    @property
    def minreducedheight(self):
        return self["minreducedheight"]

    @minreducedheight.setter
    def minreducedheight(self, val):
        self["minreducedheight"] = val

    @property
    def minreducedwidth(self):
        return self["minreducedwidth"]

    @minreducedwidth.setter
    def minreducedwidth(self, val):
        self["minreducedwidth"] = val

    @property
    def modebar(self):
        return self["modebar"]

    @modebar.setter
    def modebar(self, val):
        self["modebar"] = val

    @property
    def newselection(self):
        return self["newselection"]

    @newselection.setter
    def newselection(self, val):
        self["newselection"] = val

    @property
    def newshape(self):
        return self["newshape"]

    @newshape.setter
    def newshape(self, val):
        self["newshape"] = val

    @property
    def paper_bgcolor(self):
        return self["paper_bgcolor"]

    @paper_bgcolor.setter
    def paper_bgcolor(self, val):
        self["paper_bgcolor"] = val

    @property
    def piecolorway(self):
        return self["piecolorway"]

    @piecolorway.setter
    def piecolorway(self, val):
        self["piecolorway"] = val

    @property
    def plot_bgcolor(self):
        return self["plot_bgcolor"]

    @plot_bgcolor.setter
    def plot_bgcolor(self, val):
        self["plot_bgcolor"] = val

    @property
    def polar(self):
        return self["polar"]

    @polar.setter
    def polar(self, val):
        self["polar"] = val

    @property
    def scattergap(self):
        return self["scattergap"]

    @scattergap.setter
    def scattergap(self, val):
        self["scattergap"] = val

    @property
    def scattermode(self):
        return self["scattermode"]

    @scattermode.setter
    def scattermode(self, val):
        self["scattermode"] = val

    @property
    def scene(self):
        return self["scene"]

    @scene.setter
    def scene(self, val):
        self["scene"] = val

    @property
    def selectdirection(self):
        return self["selectdirection"]

    @selectdirection.setter
    def selectdirection(self, val):
        self["selectdirection"] = val

    @property
    def selectionrevision(self):
        return self["selectionrevision"]

    @selectionrevision.setter
    def selectionrevision(self, val):
        self["selectionrevision"] = val

    @property
    def selections(self):
        return self["selections"]

    @selections.setter
    def selections(self, val):
        self["selections"] = val

    @property
    def selectiondefaults(self):
        return self["selectiondefaults"]

    @selectiondefaults.setter
    def selectiondefaults(self, val):
        self["selectiondefaults"] = val

    @property
    def separators(self):
        return self["separators"]

    @separators.setter
    def separators(self, val):
        self["separators"] = val

    @property
    def shapes(self):
        return self["shapes"]

    @shapes.setter
    def shapes(self, val):
        self["shapes"] = val

    @property
    def shapedefaults(self):
        return self["shapedefaults"]

    @shapedefaults.setter
    def shapedefaults(self, val):
        self["shapedefaults"] = val

    @property
    def showlegend(self):
        return self["showlegend"]

    @showlegend.setter
    def showlegend(self, val):
        self["showlegend"] = val

    @property
    def sliders(self):
        return self["sliders"]

    @sliders.setter
    def sliders(self, val):
        self["sliders"] = val

    @property
    def sliderdefaults(self):
        return self["sliderdefaults"]

    @sliderdefaults.setter
    def sliderdefaults(self, val):
        self["sliderdefaults"] = val

    @property
    def smith(self):
        return self["smith"]

    @smith.setter
    def smith(self, val):
        self["smith"] = val

    @property
    def spikedistance(self):
        return self["spikedistance"]

    @spikedistance.setter
    def spikedistance(self, val):
        self["spikedistance"] = val

    @property
    def sunburstcolorway(self):
        return self["sunburstcolorway"]

    @sunburstcolorway.setter
    def sunburstcolorway(self, val):
        self["sunburstcolorway"] = val

    @property
    def template(self):
        return self["template"]

    @template.setter
    def template(self, val):
        self["template"] = val

    @property
    def ternary(self):
        return self["ternary"]

    @ternary.setter
    def ternary(self, val):
        self["ternary"] = val

    @property
    def title(self):
        return self["title"]

    @title.setter
    def title(self, val):
        self["title"] = val

    @property
    def transition(self):
        return self["transition"]

    @transition.setter
    def transition(self, val):
        self["transition"] = val

    @property
    def treemapcolorway(self):
        return self["treemapcolorway"]

    @treemapcolorway.setter
    def treemapcolorway(self, val):
        self["treemapcolorway"] = val

    @property
    def uirevision(self):
        return self["uirevision"]

    @uirevision.setter
    def uirevision(self, val):
        self["uirevision"] = val

    @property
    def uniformtext(self):
        return self["uniformtext"]

    @uniformtext.setter
    def uniformtext(self, val):
        self["uniformtext"] = val

    @property
    def updatemenus(self):
        return self["updatemenus"]

    @updatemenus.setter
    def updatemenus(self, val):
        self["updatemenus"] = val

    @property
    def updatemenudefaults(self):
        return self["updatemenudefaults"]

    @updatemenudefaults.setter
    def updatemenudefaults(self, val):
        self["updatemenudefaults"] = val

    @property
    def violingap(self):
        return self["violingap"]

    @violingap.setter
    def violingap(self, val):
        self["violingap"] = val

    @property
    def violingroupgap(self):
        return self["violingroupgap"]

    @violingroupgap.setter
    def violingroupgap(self, val):
        self["violingroupgap"] = val

    @property
    def violinmode(self):
        return self["violinmode"]

    @violinmode.setter
    def violinmode(self, val):
        self["violinmode"] = val

    @property
    def waterfallgap(self):
        return self["waterfallgap"]

    @waterfallgap.setter
    def waterfallgap(self, val):
        self["waterfallgap"] = val

    @property
    def waterfallgroupgap(self):
        return self["waterfallgroupgap"]

    @waterfallgroupgap.setter
    def waterfallgroupgap(self, val):
        self["waterfallgroupgap"] = val

    @property
    def waterfallmode(self):
        return self["waterfallmode"]

    @waterfallmode.setter
    def waterfallmode(self, val):
        self["waterfallmode"] = val

    @property
    def width(self):
        return self["width"]

    @width.setter
    def width(self, val):
        self["width"] = val

    @property
    def xaxis(self):
        return self["xaxis"]

    @xaxis.setter
    def xaxis(self, val):
        self["xaxis"] = val

    @property
    def yaxis(self):
        return self["yaxis"]

    @yaxis.setter
    def yaxis(self, val):
        self["yaxis"] = val

    @property
    def _prop_descriptions(self):
        return """\
        """

    def __init__(
        self,
        arg=None,
        activeselection=None,
        activeshape=None,
        annotations=None,
        annotationdefaults=None,
        autosize=None,
        autotypenumbers=None,
        barcornerradius=None,
        bargap=None,
        bargroupgap=None,
        barmode=None,
        barnorm=None,
        boxgap=None,
        boxgroupgap=None,
        boxmode=None,
        calendar=None,
        clickmode=None,
        coloraxis=None,
        colorscale=None,
        colorway=None,
        computed=None,
        datarevision=None,
        dragmode=None,
        editrevision=None,
        extendfunnelareacolors=None,
        extendiciclecolors=None,
        extendpiecolors=None,
        extendsunburstcolors=None,
        extendtreemapcolors=None,
        font=None,
        funnelareacolorway=None,
        funnelgap=None,
        funnelgroupgap=None,
        funnelmode=None,
        geo=None,
        grid=None,
        height=None,
        hiddenlabels=None,
        hiddenlabelssrc=None,
        hidesources=None,
        hoverdistance=None,
        hoverlabel=None,
        hovermode=None,
        hoversubplots=None,
        iciclecolorway=None,
        images=None,
        imagedefaults=None,
        legend=None,
        map=None,
        mapbox=None,
        margin=None,
        meta=None,
        metasrc=None,
        minreducedheight=None,
        minreducedwidth=None,
        modebar=None,
        newselection=None,
        newshape=None,
        paper_bgcolor=None,
        piecolorway=None,
        plot_bgcolor=None,
        polar=None,
        scattergap=None,
        scattermode=None,
        scene=None,
        selectdirection=None,
        selectionrevision=None,
        selections=None,
        selectiondefaults=None,
        separators=None,
        shapes=None,
        shapedefaults=None,
        showlegend=None,
        sliders=None,
        sliderdefaults=None,
        smith=None,
        spikedistance=None,
        sunburstcolorway=None,
        template=None,
        ternary=None,
        title=None,
        transition=None,
        treemapcolorway=None,
        uirevision=None,
        uniformtext=None,
        updatemenus=None,
        updatemenudefaults=None,
        violingap=None,
        violingroupgap=None,
        violinmode=None,
        waterfallgap=None,
        waterfallgroupgap=None,
        waterfallmode=None,
        width=None,
        xaxis=None,
        yaxis=None,
        **kwargs,
    ):
        super(Layout, self).__init__("layout")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        self._valid_props = {
            "activeselection",
            "activeshape",
            "annotationdefaults",
            "annotations",
            "autosize",
            "autotypenumbers",
            "barcornerradius",
            "bargap",
            "bargroupgap",
            "barmode",
            "barnorm",
            "boxgap",
            "boxgroupgap",
            "boxmode",
            "calendar",
            "clickmode",
            "coloraxis",
            "colorscale",
            "colorway",
            "computed",
            "datarevision",
            "dragmode",
            "editrevision",
            "extendfunnelareacolors",
            "extendiciclecolors",
            "extendpiecolors",
            "extendsunburstcolors",
            "extendtreemapcolors",
            "font",
            "funnelareacolorway",
            "funnelgap",
            "funnelgroupgap",
            "funnelmode",
            "geo",
            "grid",
            "height",
            "hiddenlabels",
            "hiddenlabelssrc",
            "hidesources",
            "hoverdistance",
            "hoverlabel",
            "hovermode",
            "hoversubplots",
            "iciclecolorway",
            "imagedefaults",
            "images",
            "legend",
            "map",
            "mapbox",
            "margin",
            "meta",
            "metasrc",
            "minreducedheight",
            "minreducedwidth",
            "modebar",
            "newselection",
            "newshape",
            "paper_bgcolor",
            "piecolorway",
            "plot_bgcolor",
            "polar",
            "scattergap",
            "scattermode",
            "scene",
            "selectdirection",
            "selectiondefaults",
            "selectionrevision",
            "selections",
            "separators",
            "shapedefaults",
            "shapes",
            "showlegend",
            "sliderdefaults",
            "sliders",
            "smith",
            "spikedistance",
            "sunburstcolorway",
            "template",
            "ternary",
            "title",
            "transition",
            "treemapcolorway",
            "uirevision",
            "uniformtext",
            "updatemenudefaults",
            "updatemenus",
            "violingap",
            "violingroupgap",
            "violinmode",
            "waterfallgap",
            "waterfallgroupgap",
            "waterfallmode",
            "width",
            "xaxis",
            "yaxis",
        }

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.Layout
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Layout`"""
            )

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        _v = arg.pop("activeselection", None)
        _v = activeselection if activeselection is not None else _v
        if _v is not None:
            self["activeselection"] = _v
        _v = arg.pop("activeshape", None)
        _v = activeshape if activeshape is not None else _v
        if _v is not None:
            self["activeshape"] = _v
        _v = arg.pop("annotations", None)
        _v = annotations if annotations is not None else _v
        if _v is not None:
            self["annotations"] = _v
        _v = arg.pop("annotationdefaults", None)
        _v = annotationdefaults if annotationdefaults is not None else _v
        if _v is not None:
            self["annotationdefaults"] = _v
        _v = arg.pop("autosize", None)
        _v = autosize if autosize is not None else _v
        if _v is not None:
            self["autosize"] = _v
        _v = arg.pop("autotypenumbers", None)
        _v = autotypenumbers if autotypenumbers is not None else _v
        if _v is not None:
            self["autotypenumbers"] = _v
        _v = arg.pop("barcornerradius", None)
        _v = barcornerradius if barcornerradius is not None else _v
        if _v is not None:
            self["barcornerradius"] = _v
        _v = arg.pop("bargap", None)
        _v = bargap if bargap is not None else _v
        if _v is not None:
            self["bargap"] = _v
        _v = arg.pop("bargroupgap", None)
        _v = bargroupgap if bargroupgap is not None else _v
        if _v is not None:
            self["bargroupgap"] = _v
        _v = arg.pop("barmode", None)
        _v = barmode if barmode is not None else _v
        if _v is not None:
            self["barmode"] = _v
        _v = arg.pop("barnorm", None)
        _v = barnorm if barnorm is not None else _v
        if _v is not None:
            self["barnorm"] = _v
        _v = arg.pop("boxgap", None)
        _v = boxgap if boxgap is not None else _v
        if _v is not None:
            self["boxgap"] = _v
        _v = arg.pop("boxgroupgap", None)
        _v = boxgroupgap if boxgroupgap is not None else _v
        if _v is not None:
            self["boxgroupgap"] = _v
        _v = arg.pop("boxmode", None)
        _v = boxmode if boxmode is not None else _v
        if _v is not None:
            self["boxmode"] = _v
        _v = arg.pop("calendar", None)
        _v = calendar if calendar is not None else _v
        if _v is not None:
            self["calendar"] = _v
        _v = arg.pop("clickmode", None)
        _v = clickmode if clickmode is not None else _v
        if _v is not None:
            self["clickmode"] = _v
        _v = arg.pop("coloraxis", None)
        _v = coloraxis if coloraxis is not None else _v
        if _v is not None:
            self["coloraxis"] = _v
        _v = arg.pop("colorscale", None)
        _v = colorscale if colorscale is not None else _v
        if _v is not None:
            self["colorscale"] = _v
        _v = arg.pop("colorway", None)
        _v = colorway if colorway is not None else _v
        if _v is not None:
            self["colorway"] = _v
        _v = arg.pop("computed", None)
        _v = computed if computed is not None else _v
        if _v is not None:
            self["computed"] = _v
        _v = arg.pop("datarevision", None)
        _v = datarevision if datarevision is not None else _v
        if _v is not None:
            self["datarevision"] = _v
        _v = arg.pop("dragmode", None)
        _v = dragmode if dragmode is not None else _v
        if _v is not None:
            self["dragmode"] = _v
        _v = arg.pop("editrevision", None)
        _v = editrevision if editrevision is not None else _v
        if _v is not None:
            self["editrevision"] = _v
        _v = arg.pop("extendfunnelareacolors", None)
        _v = extendfunnelareacolors if extendfunnelareacolors is not None else _v
        if _v is not None:
            self["extendfunnelareacolors"] = _v
        _v = arg.pop("extendiciclecolors", None)
        _v = extendiciclecolors if extendiciclecolors is not None else _v
        if _v is not None:
            self["extendiciclecolors"] = _v
        _v = arg.pop("extendpiecolors", None)
        _v = extendpiecolors if extendpiecolors is not None else _v
        if _v is not None:
            self["extendpiecolors"] = _v
        _v = arg.pop("extendsunburstcolors", None)
        _v = extendsunburstcolors if extendsunburstcolors is not None else _v
        if _v is not None:
            self["extendsunburstcolors"] = _v
        _v = arg.pop("extendtreemapcolors", None)
        _v = extendtreemapcolors if extendtreemapcolors is not None else _v
        if _v is not None:
            self["extendtreemapcolors"] = _v
        _v = arg.pop("font", None)
        _v = font if font is not None else _v
        if _v is not None:
            self["font"] = _v
        _v = arg.pop("funnelareacolorway", None)
        _v = funnelareacolorway if funnelareacolorway is not None else _v
        if _v is not None:
            self["funnelareacolorway"] = _v
        _v = arg.pop("funnelgap", None)
        _v = funnelgap if funnelgap is not None else _v
        if _v is not None:
            self["funnelgap"] = _v
        _v = arg.pop("funnelgroupgap", None)
        _v = funnelgroupgap if funnelgroupgap is not None else _v
        if _v is not None:
            self["funnelgroupgap"] = _v
        _v = arg.pop("funnelmode", None)
        _v = funnelmode if funnelmode is not None else _v
        if _v is not None:
            self["funnelmode"] = _v
        _v = arg.pop("geo", None)
        _v = geo if geo is not None else _v
        if _v is not None:
            self["geo"] = _v
        _v = arg.pop("grid", None)
        _v = grid if grid is not None else _v
        if _v is not None:
            self["grid"] = _v
        _v = arg.pop("height", None)
        _v = height if height is not None else _v
        if _v is not None:
            self["height"] = _v
        _v = arg.pop("hiddenlabels", None)
        _v = hiddenlabels if hiddenlabels is not None else _v
        if _v is not None:
            self["hiddenlabels"] = _v
        _v = arg.pop("hiddenlabelssrc", None)
        _v = hiddenlabelssrc if hiddenlabelssrc is not None else _v
        if _v is not None:
            self["hiddenlabelssrc"] = _v
        _v = arg.pop("hidesources", None)
        _v = hidesources if hidesources is not None else _v
        if _v is not None:
            self["hidesources"] = _v
        _v = arg.pop("hoverdistance", None)
        _v = hoverdistance if hoverdistance is not None else _v
        if _v is not None:
            self["hoverdistance"] = _v
        _v = arg.pop("hoverlabel", None)
        _v = hoverlabel if hoverlabel is not None else _v
        if _v is not None:
            self["hoverlabel"] = _v
        _v = arg.pop("hovermode", None)
        _v = hovermode if hovermode is not None else _v
        if _v is not None:
            self["hovermode"] = _v
        _v = arg.pop("hoversubplots", None)
        _v = hoversubplots if hoversubplots is not None else _v
        if _v is not None:
            self["hoversubplots"] = _v
        _v = arg.pop("iciclecolorway", None)
        _v = iciclecolorway if iciclecolorway is not None else _v
        if _v is not None:
            self["iciclecolorway"] = _v
        _v = arg.pop("images", None)
        _v = images if images is not None else _v
        if _v is not None:
            self["images"] = _v
        _v = arg.pop("imagedefaults", None)
        _v = imagedefaults if imagedefaults is not None else _v
        if _v is not None:
            self["imagedefaults"] = _v
        _v = arg.pop("legend", None)
        _v = legend if legend is not None else _v
        if _v is not None:
            self["legend"] = _v
        _v = arg.pop("map", None)
        _v = map if map is not None else _v
        if _v is not None:
            self["map"] = _v
        _v = arg.pop("mapbox", None)
        _v = mapbox if mapbox is not None else _v
        if _v is not None:
            self["mapbox"] = _v
        _v = arg.pop("margin", None)
        _v = margin if margin is not None else _v
        if _v is not None:
            self["margin"] = _v
        _v = arg.pop("meta", None)
        _v = meta if meta is not None else _v
        if _v is not None:
            self["meta"] = _v
        _v = arg.pop("metasrc", None)
        _v = metasrc if metasrc is not None else _v
        if _v is not None:
            self["metasrc"] = _v
        _v = arg.pop("minreducedheight", None)
        _v = minreducedheight if minreducedheight is not None else _v
        if _v is not None:
            self["minreducedheight"] = _v
        _v = arg.pop("minreducedwidth", None)
        _v = minreducedwidth if minreducedwidth is not None else _v
        if _v is not None:
            self["minreducedwidth"] = _v
        _v = arg.pop("modebar", None)
        _v = modebar if modebar is not None else _v
        if _v is not None:
            self["modebar"] = _v
        _v = arg.pop("newselection", None)
        _v = newselection if newselection is not None else _v
        if _v is not None:
            self["newselection"] = _v
        _v = arg.pop("newshape", None)
        _v = newshape if newshape is not None else _v
        if _v is not None:
            self["newshape"] = _v
        _v = arg.pop("paper_bgcolor", None)
        _v = paper_bgcolor if paper_bgcolor is not None else _v
        if _v is not None:
            self["paper_bgcolor"] = _v
        _v = arg.pop("piecolorway", None)
        _v = piecolorway if piecolorway is not None else _v
        if _v is not None:
            self["piecolorway"] = _v
        _v = arg.pop("plot_bgcolor", None)
        _v = plot_bgcolor if plot_bgcolor is not None else _v
        if _v is not None:
            self["plot_bgcolor"] = _v
        _v = arg.pop("polar", None)
        _v = polar if polar is not None else _v
        if _v is not None:
            self["polar"] = _v
        _v = arg.pop("scattergap", None)
        _v = scattergap if scattergap is not None else _v
        if _v is not None:
            self["scattergap"] = _v
        _v = arg.pop("scattermode", None)
        _v = scattermode if scattermode is not None else _v
        if _v is not None:
            self["scattermode"] = _v
        _v = arg.pop("scene", None)
        _v = scene if scene is not None else _v
        if _v is not None:
            self["scene"] = _v
        _v = arg.pop("selectdirection", None)
        _v = selectdirection if selectdirection is not None else _v
        if _v is not None:
            self["selectdirection"] = _v
        _v = arg.pop("selectionrevision", None)
        _v = selectionrevision if selectionrevision is not None else _v
        if _v is not None:
            self["selectionrevision"] = _v
        _v = arg.pop("selections", None)
        _v = selections if selections is not None else _v
        if _v is not None:
            self["selections"] = _v
        _v = arg.pop("selectiondefaults", None)
        _v = selectiondefaults if selectiondefaults is not None else _v
        if _v is not None:
            self["selectiondefaults"] = _v
        _v = arg.pop("separators", None)
        _v = separators if separators is not None else _v
        if _v is not None:
            self["separators"] = _v
        _v = arg.pop("shapes", None)
        _v = shapes if shapes is not None else _v
        if _v is not None:
            self["shapes"] = _v
        _v = arg.pop("shapedefaults", None)
        _v = shapedefaults if shapedefaults is not None else _v
        if _v is not None:
            self["shapedefaults"] = _v
        _v = arg.pop("showlegend", None)
        _v = showlegend if showlegend is not None else _v
        if _v is not None:
            self["showlegend"] = _v
        _v = arg.pop("sliders", None)
        _v = sliders if sliders is not None else _v
        if _v is not None:
            self["sliders"] = _v
        _v = arg.pop("sliderdefaults", None)
        _v = sliderdefaults if sliderdefaults is not None else _v
        if _v is not None:
            self["sliderdefaults"] = _v
        _v = arg.pop("smith", None)
        _v = smith if smith is not None else _v
        if _v is not None:
            self["smith"] = _v
        _v = arg.pop("spikedistance", None)
        _v = spikedistance if spikedistance is not None else _v
        if _v is not None:
            self["spikedistance"] = _v
        _v = arg.pop("sunburstcolorway", None)
        _v = sunburstcolorway if sunburstcolorway is not None else _v
        if _v is not None:
            self["sunburstcolorway"] = _v
        _v = arg.pop("template", None)
        _v = template if template is not None else _v
        if _v is not None:
            self["template"] = _v
        _v = arg.pop("ternary", None)
        _v = ternary if ternary is not None else _v
        if _v is not None:
            self["ternary"] = _v
        _v = arg.pop("title", None)
        _v = title if title is not None else _v
        if _v is not None:
            self["title"] = _v
        _v = arg.pop("transition", None)
        _v = transition if transition is not None else _v
        if _v is not None:
            self["transition"] = _v
        _v = arg.pop("treemapcolorway", None)
        _v = treemapcolorway if treemapcolorway is not None else _v
        if _v is not None:
            self["treemapcolorway"] = _v
        _v = arg.pop("uirevision", None)
        _v = uirevision if uirevision is not None else _v
        if _v is not None:
            self["uirevision"] = _v
        _v = arg.pop("uniformtext", None)
        _v = uniformtext if uniformtext is not None else _v
        if _v is not None:
            self["uniformtext"] = _v
        _v = arg.pop("updatemenus", None)
        _v = updatemenus if updatemenus is not None else _v
        if _v is not None:
            self["updatemenus"] = _v
        _v = arg.pop("updatemenudefaults", None)
        _v = updatemenudefaults if updatemenudefaults is not None else _v
        if _v is not None:
            self["updatemenudefaults"] = _v
        _v = arg.pop("violingap", None)
        _v = violingap if violingap is not None else _v
        if _v is not None:
            self["violingap"] = _v
        _v = arg.pop("violingroupgap", None)
        _v = violingroupgap if violingroupgap is not None else _v
        if _v is not None:
            self["violingroupgap"] = _v
        _v = arg.pop("violinmode", None)
        _v = violinmode if violinmode is not None else _v
        if _v is not None:
            self["violinmode"] = _v
        _v = arg.pop("waterfallgap", None)
        _v = waterfallgap if waterfallgap is not None else _v
        if _v is not None:
            self["waterfallgap"] = _v
        _v = arg.pop("waterfallgroupgap", None)
        _v = waterfallgroupgap if waterfallgroupgap is not None else _v
        if _v is not None:
            self["waterfallgroupgap"] = _v
        _v = arg.pop("waterfallmode", None)
        _v = waterfallmode if waterfallmode is not None else _v
        if _v is not None:
            self["waterfallmode"] = _v
        _v = arg.pop("width", None)
        _v = width if width is not None else _v
        if _v is not None:
            self["width"] = _v
        _v = arg.pop("xaxis", None)
        _v = xaxis if xaxis is not None else _v
        if _v is not None:
            self["xaxis"] = _v
        _v = arg.pop("yaxis", None)
        _v = yaxis if yaxis is not None else _v
        if _v is not None:
            self["yaxis"] = _v
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
