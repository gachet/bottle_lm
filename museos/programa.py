from bottle import route, default_app, template, run, static_file, error
from lxml import etree
@route('/')
def index():
    doc=etree.parse("museos.xml")
    museos=doc.xpath("//SchemaData")
    return template("index.tpl",museos=museos)

run(host='0.0.0.0', port=8080)