#!/usr/bin/python3
"""Moduel to learn how to serialize/deserialize from/to xml file"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for element in root:
        text = element.text

        if text.isdigit():
            value = int(text)
        else:
            try:
                value = float(text)
            except ValueError:
                value = text

        result[element.tag] = value

    return result
