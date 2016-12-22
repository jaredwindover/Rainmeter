class Option:
    def __init__(self, name=None, default=None):
        if name == None:
            raise ValueError('Must specify a name')
        self.name = name
        self.default = default

    def __str__(self):
        return self.name + "=" + self.ValueString()

class StringOption(Option):
    def __init__(self, name=None, default=None, val=None):
        Option.__init__(self, name)
        self.val = s

    def valueString(self):
        return self.val
