from safeIO import JSONFile

data = JSONFile("models/userAgents.json").read()
USER_AGENTS = data