#!/usr/bin/python3
"""Moduel to learn how to serialize/deserialize from/to xml file"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to a simple indented XML file."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    indent_xml(root)
    tree = ET.ElementTree(root)
    tree.write(filename)


def indent_xml(elem, level=0):
    """Add indentation and line breaks for readability."""
    i = "\n" + "    " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for element in root:
        text = element.text.strip() if element.text else ""
        if text.isdigit():
            value = int(text)
        else:
            try:
                value = float(text)
            except ValueError:
                value = text
        result[element.tag] = value

    return result
