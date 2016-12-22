class Substitution:
    def __init__(self, pattern, replacement):
        self.pattern = pattern
        self.replacement = replacement

class Measure:
    def __str__(self):


    def __init__(self, cfg):
        self.Measure = None
        self.UpdateDivider = 1
        self.OnUpdateAction = None
        self.OnChangeAction = None
        self.InvertMeasure = False
        self.MaxValue = 1.0
        self.MinValue = 0.0
        self.AverageSize = 1
        self.DynamicVariables = False
        self.Disabled = False
        self.Paused = False
        self.Group = []
        self.IfAboveValue = None
        self.IfAboveAction = None
        self.IfBelowValue = None
        self.IfBelowAction = None
        self.IfEqualValue = None
        self.IfEqualAction = None
        self.IfConditions = []
        self.IfTrueActions = []
        self.IfFalseActions = []
        self.IfConditionMode = False
        self.IfMatches = []
        self.IfMatchActions = []
        self.IfNotMatchActions = []
        self.IfMatchMode = False
        self.Substitute = []
        self.RegExpSubstitute = False

class ConstantFormula():
    def __init__(self, value):
        self.value = value

class CalcMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Calc"
        self.Formula = ConstantFormula(0)
        self.UpdateRandom = False
        self.UniqueRandom = False
        self.LowBound = 0.0
        self.HighBound = 100.0

class CPUMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "CPU"
        self.Processor = 0

class FreeDiskSpaceMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "FreeDiskSpace"
        self.Drive = "C:"
        self.Total = False
        self.Label = False
        self.Type = False
        self.IgnoreRemovable = True
        self.DiskQuota = True

class LoopMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Loop"
        self.StartValue = 1
        self.EndValue = 100
        self.Increment = 1
        self.LoopCount = 0

class MemoryMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = None
        self.Total = False

class PhysicalMemoryMeasure(MemoryMeasure):
    def __init__(self, cfg):
        MemoryMeasure.__init__(self, cfg)
        self.Measure = "PhysicalMemory"

class SwapMemoryMeasure(MemoryMeasure):
    def __init__(self, cfg):
        MemoryMeasure.__init__(self, cfg)
        self.Measure = "SwapMemory"

class VirtualMemoryMeasure(MemoryMeasure):
    def __init__(self, cfg):
        MemoryMeasure.__init__(self, cfg)
        self.Measure = "Memory"

class NetMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Interface = 0
        self.Cumulative = 0

class NetInMeasure(NetMeasure):
    def __init__(self, cfg):
        NetMeasure.__init__(self, cfg)
        self.Measure = "NetIn"

class NetOutMeasure(NetMeasure):
    def __init__(self, cfg):
        NetMeasure.__init__(self, cfg)
        self.Measure = "NetOut"

class NetTotalMeasure(NetMeasure):
    def __init__(self, cfg):
        NetMeasure.__init__(self, cfg)
        self.Measure = "NetTotal"

class PluginMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Plugin"
        self.Plugin = None

class RegistryMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Registry"
        self.RegHKey = None
        self.RegKey = None
        self.RegValue = None

class ScriptMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Script"
        self.ScriptFile = None
        self.Options = {}

class StringMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "String"
        self.String = None

class TimeZone():
    local = "local"

class TimeMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Time"
        self.Format = "%H:%M:%S"
        self.TimeStamp = None
        self.TimeStampFormat = None
        self.TimeStampLocale = None
        self.FormatLocale = None
        self.TimeZone = TimeZone.local
        self.DaylightSavingTime = True

class UptimeMeasure(Measure):
    def __init__(self, cfg):
        Measure.__init__(self, cfg)
        self.Measure = "Uptime"
        self.Format = "%4!i!d %3!i!:%2!02i!"
        self.AddDaysToHours = True
        self.SecondsValue = None

def ParseMeasure(cfg):
    t = cfg['measure']
    return {
        "Calc": CalcMeasure,
        "CPU": CPUMeasure,
        "FreeDiskSpace": FreeDiskSpaceMeasure,
        "Loop": LoopMeasure,
        "PhysicalMemory": PhysicalMemoryMeasure,
        "SwapMemory": SwapMemoryMeasure,
        "Memory": VirtualMemoryMeasure,
        "NetIn": NetInMeasure,
        "NetOut": NetOutMeasure,
        "NetTotal": NetTotalMeasure,
        "Plugin": PluginMeasure,
        "Registry": RegistryMeasure,
        "Script": ScriptMeasure,
        "String": StringMeasure,
        "Time": TimeMeasure,
        "Uptime": UptimeMeasure
    }[t](cfg)
