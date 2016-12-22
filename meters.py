import image

class Padding:
    def __init__(self, left, right, top, bottom):
        self.Left = left
        self.Right = right
        self.Top = top
        self.Bottom = bottom

class Color:
    def __init__(self, red, green, blue, alpha=None):
        self.Red = red
        self.Green = green
        self.Blue = blue
        self.Alpha = alpha

class Bevel:
    NoBevel = 0
    Raised = 1
    Sunken = 2

class ToolTipIcon:
    ToolTipInfo = "Info"
    ToolTipWarning = "Warning"
    ToolTipError = "Error"
    ToolTipQuestion = "Question"
    ToolTipShield = "Shield"

class ToolTipType:
    Normal = 0
    Balloon = 1

class Meter():
    def __init__(self, cfg):
        self.Meter = None
        self.MeterStyle = []
        self.X = 0
        self.Y = 0
        self.W = None
        self.H = None
        self.Padding = None
        self.Hidden = False
        self.UpdateDivider = 1
        self.OnUpdateAction = None
        self.SolidColor1 = Color(0,0,0,0)
        self.GradientAngle = None
        self.BevelType = Bevel.NoBevel
        self.AntiAlias = False
        self.DynamicVariables = False
        self.TransformationMatrix = [1,0,0,1,0,0]
        self.Group = []
        self.ToolTipText = None
        self.ToolTipTitle = None
        self.ToolTipIcon = None
        self.ToolTipType = ToolTipType.Normal
        self.ToolTipWidth = 1000
        self.ToolTipHidden = False

class _ImageMeter(Meter, image.ImageOptions):
    def __init__(self, cfg):
        Meter.__init__(self, cfg)
        image.ImageOptions.__init__(self, cfg)

class Orientation:
    Horizontal = "Horizontal"
    Vertical = "Vertical"

class BarMeter(_ImageMeter):
    def __init__(self, cfg):
        _ImageMeter.__init__(self, cfg)
        self.Meter = "Bar"
        self.MeasureName = None
        self.BarColor = Color(0,128,0)
        self.BarImage = None
        self.BarBorder = None
        self.BarOrientation = Orientation.Vertical
        self.Flip = False

class Alignment:
    Left = "Left"
    Center = "Center"
    Right = "Right"

class BitmapMeter(_ImageMeter):
    def __init__(self, cfg):
        _ImageMeter.__init__(self, cfg)
        self.Meter = "Bitmap"
        self.MeasureName = None
        self.BitmapImage = None
        self.BitmapFrames = 1
        self.BitmapTransitionFrames = None
        self.BitmapZeroFrame = 0
        self.BitmapExtend = False
        self.BitmapDigits = 0
        self.BitmapAlign = None
        self.BitmapSeparation = 0

class ButtonMeter(_ImageMeter):
    def __init__(self, cfg):
        _ImageMeter.__init__(self, cfg)
        self.Meter = "Button"
        self.ButtonImage = None
        self.ButtonCommand = None

class HistogramMeter(Meter):
    def __init__(self, cfg):
        Meter.__init__(self, cfg)
        self.Meter = "Histogram"
        self.MeasureName = None
        self.MeasureName2 = None
        self.Autoscale = False
        self.GraphStart = Alignment.Right
        self.GraphOrientation = Orientation.Vertical
        self.Flip = False
        self.PrimaryColor = Color(0,0x80,0)
        self.SecondaryColor = Color(0xff,0,0)
        self.BothColor = Color(0xff,0xff,0)
        self.PrimaryImage = None
        self.PrimaryImagePath = None
        self.PrimaryImageCrop = None
        self.PrimaryImageTint = None
        self.PrimaryImageAlpha = None
        self.PrimaryImageFlip = None
        self.PrimaryImageRotate = None
        self.PrimaryColorMatrix = None
        self.SecondaryImage = None
        self.SecondaryImagePath = None
        self.SecondaryImageCrop = None
        self.SecondaryImageTint = None
        self.SecondaryImageAlpha = None
        self.SecondaryImageFlip = None
        self.SecondaryImageRotate = None
        self.SecondaryColorMatrix = None
        self.BothImage = None
        self.BothImagePath = None
        self.BothImageCrop = None
        self.BothImageTint = None
        self.BothImageAlpha = None
        self.BothImageFlip = None
        self.BothImageRotate = None
        self.BothColorMatrix = None

class Margins:
    def __init__(self, left, top, right, bottom):
        self.Left = left
        self.Top = top
        self.Right = right
        self.Bottom = bottom

class ImageMeter(_ImageMeter):
    def __init__(self, cfg):
        _ImageMeter.__init__(self, cfg)
        self.Meter = "Image"
        self.MeasureNames = []
        self.ImageName = "%1.png"
        self.PreserverAspectRation = False
        self.ScaleMargins = None
        self.Tile = False
        self.MaskImageName = None
        self.MaskImagePath = None
        self.MaskImageFlip = None
        self.MaskImageRotate = 0.0

class LineMeter(Meter):
    def __init__(self, cfg):
        Meter.__init__(self, cfg)
        self.Meter = "Line"
        self.LineCount = 1
        self.MeasureNames = []
        self.LineColors = []
        self.LineWidth = 1
        self.Scales = []
        self.AutoScale = False
        self.HorizontalLines = False
        self.HorizontalLineColor = Color(0,0,0,0xff)
        self.GraphStart = Alignment.Right
        self.GraphOrientation = Orientation.Vertical
        self.Flip = False

class RotatorMeter(_ImageMeter):
    def __init__(self, cfg):
        _ImageMeter.__init__(self, cfg)
        self.Meter = "Rotator"
        self.ImageName = None
        self.MeasureName = None
        self.OffsetX = 0.0
        self.OffsetY = 0.0
        self.StartAngle = 0.0
        self.RotationAngle = "(2 * pi)"
        self.ValueRemainder = 0

class RoundlineMeter(Meter):
    def __init__(self, cfg):
        Meter.__init__(self, cfg)
        self.Meter = "Roundline"
        self.MeasureName = None
        self.StartAngle = None
        self.RotationAngle = None
        self.LineStart = None
        self.LineLength = None
        self.LineWidth = 1
        self.LineColor = Color(0xff, 0xff, 0xff, 0xff)
        self.Solid = False
        self.ControlAngle = True
        self.ControlStart = 0
        self.StartShift = 0
        self.ControlLength = 0
        self.LengthShift = 0
        self.ValueRemainder = None

class StringAlignment:
    Left = "Left"
    Right = "Right"
    Center = "Center"
    LeftTop = "LeftTop"
    RightTop = "RightTop"
    CenterTop = "CenterTop"
    LeftCenter = "LeftCenter"
    RightCenter = "RightCenter"
    CenterCenter = "CenterCenter"
    LeftBottom = "LeftBottom"
    RightBottom = "RightBottom"
    CenterBottom = "CenterBottom"

class StringStyle:
    Normal = "Normal"
    Bold = "Bold"
    Italic = "Italic"
    BoldItalic = "BoldItalic"

class StringCase:
    Upper = "Upper"
    Lower = "Lower"
    Proper = "Proper"

class StringEffect:
    Shadow = "Shadow"
    Border = "Border"

class ClipString:
    Disabled = 0
    Enabled = 1
    Auto = 2

class AutoScale:
    Disabled = "0"
    Pow2 = "1"
    Pow2Bound = "1k"
    Kilo = "2"
    KiloBound = "2k"

class StringMeter(Meter):
    def __init__(self, cfg):
        Meter.__init__(self, cfg)
        self.Meter = "String"
        self.MeasureNames = []
        self.Text = "%1"
        self.Prefix = None
        self.Postfix = None
        self.FontFace = "Arial"
        self.FontSize = 10
        self.FontColor = Color(0,0,0,0xff)
        self.StringAlign = StringAlignment.Left
        self.StringStyle = StringStyle.Normal
        self.StringCase = None
        self.StringEffect = None
        self.FontEffectColor = Color(0,0,0,0xff)
        self.ClipString = ClipString.Disabled
        self.ClipStringW = None
        self.ClipStringH = None
        self.Angle = 0.0
        self.Percentual = False
        self.NumOfDecimals = 0
        self.Scale = 1
        self.AutoScale = AutoScale.Disabled
        self.InlineSettings = []
        self.InlinePatterns = []

def ParseMeter(cfg):
    t = cfg['meter']
    return     {
        "Bar":BarMeter,
        "Bitmap":BitmapMeter,
        "Button":ButtonMeter,
        "Histogram":HistogramMeter,
        "Image":ImageMeter,
        "Line":LineMeter,
        "Rotator":RotatorMeter,
        "Roundline":RoundlineMeter,
        "String":StringMeter
    }[t](cfg)
