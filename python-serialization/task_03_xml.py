#!/usr/bin/python3
"""Moduel to learn how to serialize/deserialize from/to xml file"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ", level=0)
    tree.write(filename)


def deserialize_from_xml(filename):
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
