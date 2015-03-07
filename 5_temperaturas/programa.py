from bottle import route, default_app, template
from lxml import etree
@route('/')
def index():
    doc=etree.parse(sevilla.xml")
    muni=doc.findall("municipio")
    return template("index.tpl", mun=muni)
@route('/<cod>/<name>')
def temp(cod,name):
	doc=etree.parse("http://www.aemet.es/xml/municipios/localidad_"+cod+".xml")
	p=doc.find("prediccion/dia")
	max=p.find("temperatura").find("maxima").text
	min=p.find("temperatura").find("minima").text
	return template("temp.tpl",name=name,max=max,min=min)

run(host='0.0.0.0', port=8080)