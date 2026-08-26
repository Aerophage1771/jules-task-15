from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "section" and next((val for name, val in attrs if name == 'class' and 'stage' in val), None):
            id_attr = next((val for name, val in attrs if name == 'id'), None)
            class_attr = next((val for name, val in attrs if name == 'class'), None)
            data_stage = next((val for name, val in attrs if name == 'data-stage'), None)
            print(f"section: id={id_attr}, class={class_attr}, data-stage={data_stage}")

parser = MyHTMLParser()
with open('mockup.html', 'r') as f:
    parser.feed(f.read())
