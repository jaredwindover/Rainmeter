import sys
import configparser
import pprint
import measures
import meters
import image

class RainmeterSkin:
    def __init__(self, cfg):
        self.measures = {}
        self.meters = {}
        self.styles = {}
        for section, options in cfg.items():
            if section == 'Rainmeter':
                self.rainmeter = SkinRainmeter(options)
                continue
            if section == 'Metadata':
                self.metadata = Metadata(options)
                continue
            if section == 'Variables':
                self.variables = Variables(options)
                continue
            if 'meter' in options:
                self.meters[section] = meters.ParseMeter(options)
                continue
            if 'measure' in options:
                self.measures[section] = measures.ParseMeasure(options)
                continue
            self.styles[section] = options

    def __str__(self):
        return (
            str(self.metadata) + "\n" +
            str(self.rainmeter) + "\n" +
            str(self.variables) + "\n" +
            str(self.styles) + "\n" +
            str(self.measures) + "\n" +
            str(self.meters) + "\n"
        )

class Origin:
    top_left = 1
    top_right = 2
    bottom_left = 3
    bottom_right = 4
    center = 5

class SkinRainmeter(image.ImageOptions):
    def __init__(self, cfg):
        self.Update = 1000
        self.DefaultUpdateDivider = 1
        self.AccurateText = 0
        self.DynamicWindowSize = 0
        self.SkinWidth = None
        self.SkinHeight = None
        self.DragMargins = (0,0,0,0)
        self.OnRefreshAction = None
        self.OnUpdateAction = None
        self.OnCloseAction = None
        self.OnFocusAction = None
        self.OnUnfocusAction = None
        self.OnWakeAction = None
        self.TransitionUpdate = 100
        self.ToolTipHidden = 0
        self.Group = []
        self.Background = None
        self.BackgroundMode = 1
        self.BackgroundMargins = (0,0,0,0)
        self.SolidColor = (0,0,0,0)
        self.SolidColor2 = (0,0,0,0)
        self.GradientAngle = None
        self.BevelType = 0
        self.ContextTitles = []
        self.ContextActions = []
        self.Blur = 0
        self.BlurRegions = []
        image.ImageOptions.__init__(self, cfg)

#class Metadata:
#    def __init__(self, cfg):
#        self.Name = None
#        self.Author = None
#        self.Information = None
#        self.Version = None
#        self.License = None

class Metadata:
    def __init__(self, cfg):
        self.options = {}

class Variables:
    def __init__(self, cfg):
        pass

def main():
    cp = configparser.RawConfigParser()
    cp.read(sys.argv[1])
    skin_ini = {x:{y:cp.get(x,y) for y in cp.options(x)} for x in cp.sections()}
    print(RainmeterSkin(skin_ini))

if __name__=='__main__':
    main()
