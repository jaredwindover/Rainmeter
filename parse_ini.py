import sys
import re
from functools import wraps

class Matchable:
    @classmethod
    def match(cls, *args, **kwargs):
        line = args[0]
        match_obj = cls.regex.match(line)
        if match_obj:
            return cls(match_obj)
        return None

def class_log(str_func, class_name):
    @wraps(str_func)
    def wrapper(*args, **kwargs):
        return class_name.upper() + ' ' + str_func(*args, **kwargs)
    return wrapper

def str_log(cls):
    if '__str__' in vars(cls):
        str_func = cls.__str__
        setattr(cls, '__str__', class_log(str_func, cls.__name__))
    return cls

@str_log
class BlankLine(Matchable):
    regex = re.compile('^\s*$')

    def __init__(self, match):
        pass

    def __str__(self):
        return "\n"

@str_log
class Comment(Matchable):
    regex = re.compile('^\s*;\s*(.*)$')

    def __init__(self, match):
        self.text = match.group(1)

    def __str__(self):
        return "; " + self.text + "\n"

@str_log
class Section(Matchable):
    regex = re.compile('^\[(.*)\]$')

    def __init__(self, match):
        self.name = match.group(1)


    def __str__(self):
        return "[" + self.name + "]\n"

@str_log
class RainmeterSection(Section):
    regex = re.compile('^\[(Rainmeter)\]$')

@str_log
class MetadataSection(Section):
    regex = re.compile('^\[(Metadata)\]$')

@str_log
class VariablesSection(Section):
    regex = re.compile('^\[(Variables)\]$')

@str_log
class Other(Matchable):
    regex = re.compile('^.*$')

    def __init__(self, match):
        self.text = match.group(0)

    def __str__(self):
        return self.text + "\n"

matchers = [
    BlankLine,
    Comment,
    RainmeterSection,
    MetadataSection,
    VariablesSection,
    Section,
    Other]

def main():
    f = open(sys.argv[1])
    contents = []
    for line in f:
        for matcher in matchers:
            obj = matcher.match(line)
            if obj:
                contents.append(obj)
                break

    for content in contents:
        print(content, end="")

if __name__=='__main__':
    main()
