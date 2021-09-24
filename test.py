from bs4.element import PreformattedString
from translatepy.utils.sanitize import remove_spaces
from translatepy import Translate
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool

pool = ThreadPool(100)

t = Translate()

with open("html.html") as input:
    page = BeautifulSoup(input.read(), "html.parser")

#nodes = [tag.text for tag in page.find_all(text=True, recursive=True, attrs=lambda class_name: "notranslate" not in str(class_name).split()) if not isinstance(tag, (PreformattedString)) and remove_spaces(tag) != ""]
nodes = [tag for tag in page.find_all(text=True, recursive=True) if not isinstance(tag, (PreformattedString)) and remove_spaces(tag) != ""]
pool.map(lambda node: node.replace_with(t.translate(str(node), "Japanese").result), nodes)
with open("out.html", "w") as out:
    out.write(str(page))