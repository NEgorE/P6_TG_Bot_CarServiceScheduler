import xml.etree.ElementTree as ET

from src.text_lib import menu as m

menu_tree = 'src/menu/tree.xml'

def get_item(command) :
    print(command)
    xml_root = ET.parse(menu_tree).getroot()
    n_item = ''
    for element in xml_root.iter():
        if element.attrib['command'] == command :
            #if command
            n_item = element.attrib['item']
            break
    return n_item

def print_menu_lvl(item, lang_code) :
    text_values = m.menu_text[lang_code]
    xml_root = ET.parse(menu_tree).getroot()
    output_text = ''
    for element in xml_root.iter():
        if element.attrib['item'] == item :
            #output_text += element.text.strip()
            output_text += text_values[item].strip()
            output_text += ' :\n'
            for ch_element in element.iter():
                if ch_element.attrib['par_item'] == item :
                    output_text += '/'
                    output_text += text_values[ch_element.attrib['item']].strip()
                    output_text += '\n'

    return output_text
