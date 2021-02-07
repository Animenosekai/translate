from safeIO import JSONFile
from os.path import abspath, dirname

data = JSONFile(dirname(abspath(__file__)) + "/userAgents.json").read()
USER_AGENTS = data