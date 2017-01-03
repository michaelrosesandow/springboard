from xml.etree import ElementTree as ET
document_tree = ET.parse('./data/mondial_database_less.xml')

for element in document_tree.iterfind('country'):
    print(element.text)

