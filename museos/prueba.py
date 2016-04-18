from lxml import etree
doc=etree.parse("museos.xml")

museos=doc.xpath("//SchemaData")
for museo in museos:
	for info in museo:
		
		if info.attrib["name"]=="NOMBRE":
			print info.text
		if info.attrib["name"]=="DIRECCION":
			print info.text
		if info.attrib["name"]=="TELEFONO":
			print info.text
			print "==========================="