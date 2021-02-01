from requests import get
from json import loads
from safeIO import JSONFile

results = []
results.extend([ua["ua"] for ua in loads(get("https://raw.githubusercontent.com/N0taN3rd/userAgentLists/master/json/chrome.json").text)])
results.extend([ua["ua"] for ua in loads(get("https://raw.githubusercontent.com/N0taN3rd/userAgentLists/master/json/firefox.json").text)])
results.extend([ua["ua"] for ua in loads(get("https://raw.githubusercontent.com/N0taN3rd/userAgentLists/master/json/internet-explorer.json").text)])
results.extend([ua["ua"] for ua in loads(get("https://raw.githubusercontent.com/N0taN3rd/userAgentLists/master/json/opera.json").text)])
results.extend([ua["ua"] for ua in loads(get("https://raw.githubusercontent.com/N0taN3rd/userAgentLists/master/json/safari.json").text)])

JSONFile("userAgents.json").write(results)