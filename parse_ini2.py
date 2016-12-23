import sys
import configparser

def configStringDictionary(d):
    res = ""
    return ''.join(["{}={}\n".format(k,v) for k,v in d.items()])

def configStringSection(name, d):
    return '[{}]\n'.format(name) + configStringDictionary(d) + "\n"

def configStringSectionDict(d):
    return ''.join([configStringSection(n,d2) for n,d2 in d.items()])

class RainmeterSkin:
    def __init__(self, cfg):
        self.measures = {}
        self.meters = {}
        self.styles = {}
        for section, options in cfg.items():
            if section == 'Rainmeter':
                self.rainmeter = options
                continue
            if section == 'Metadata':
                self.metadata = options
                continue
            if section == 'Variables':
                self.variables = options
                continue
            if 'meter' in options:
                self.meters[section] = options
                continue
            if 'measure' in options:
                self.measures[section] = options
                continue
            self.styles[section] = options

    def __str__(self):
        return (
            configStringSection('Metadata', self.metadata) +
            configStringSection('Rainmeter', self.rainmeter) +
            configStringSection('Variables', self.variables) +
            configStringSectionDict(self.styles) +
            configStringSectionDict(self.measures) +
            configStringSectionDict(self.meters)
        )

def main():
    cp = configparser.RawConfigParser()
    cp.read(sys.argv[1])
    skin_ini = {x:{y:cp.get(x,y) for y in cp.options(x)} for x in cp.sections()}
    print(RainmeterSkin(skin_ini))


if __name__=='__main__':
    main()
