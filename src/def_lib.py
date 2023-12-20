import xml.etree.ElementTree as ET

menu_tree = 'src/menu/tree.xml'

def get_item(command) :
    print(command)
    xml_root = ET.parse(menu_tree).getroot()
    n_item = ''
    for element in xml_root.iter():
        #if element.attrib['command'] == '/' + command :
        if element.attrib['command'] == command :
            n_item = element.attrib['item']
    return n_item

def print_menu_lvl(item) :
    xml_root = ET.parse(menu_tree).getroot()
    output_text = ''
    for element in xml_root.iter():
        if element.attrib['item'] == item :
            output_text += element.text.strip()
            output_text += ':\n'
            for ch_element in element.iter():
                #print(f"Тег: {ch_element.tag}, Атрибуты: {ch_element.attrib}")
                if ch_element.attrib['par_item'] == item :
                    output_text += '/'
                    output_text += ch_element.text.strip()
                    output_text += '\n'

    return output_text
