import json
import csv
import xml.etree.ElementTree as ET
from model.product import Product


def print_products(products):
    sorted_products = sorted(products, key=lambda p: p.unit_price, reverse=True)

    print("---- JSON Format ----")
    json_output = json.dumps([p.to_dict() for p in sorted_products], indent=4)
    print(json_output)

    # print("\n---- XML Format ----")
    # root = ET.Element("products")
    # for p in sorted_products:
    #     p_elem = ET.SubElement(root, "product")
    #     for k, v in p.to_dict().items():
    #         child = ET.SubElement(p_elem, k)
    #         child.text = str(v)
    # tree = ET.ElementTree(root)
    # ET.dump(tree)

    print("\n---- XML Format ----")
    root = ET.Element("products")
    for p in sorted_products:
        p_elem = ET.SubElement(root, "product")
        for k, v in p.to_dict().items():
            child = ET.SubElement(p_elem, k)
            child.text = str(v)

    # Pretty print using minidom
    from xml.dom import minidom
    xml_str = ET.tostring(root, encoding='utf-8')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="   ")  # 3-space indent like the PDF
    print(pretty_xml)

    print("\n---- CSV Format ----")
    csv_headers = ["productId", "name", "dateSupplied", "quantityInStock", "unitPrice"]
    writer = csv.DictWriter(
        open("output.csv", "w", newline=''), fieldnames=csv_headers)
    writer.writeheader()
    for p in sorted_products:
        writer.writerow(p.to_dict())

    # Print CSV to console as well
    print(",".join(csv_headers))
    for p in sorted_products:
        row = p.to_dict()
        print(",".join(str(row[h]) for h in csv_headers))


if __name__ == "__main__":
    products = [
        Product(3128874119, "Banana", "2023-01-24", 124, 0.55),
        Product(2927458265, "Apple", "2022-12-09", 18, 1.09),
        Product(9189927460, "Carrot", "2023-03-31", 89, 2.99)
    ]

    print_products(products)
