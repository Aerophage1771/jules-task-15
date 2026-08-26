import re
with open('index.html', 'r') as f:
    content = f.read()

match = re.search(r'<iframe srcdoc="(.*?)" title=', content, re.DOTALL)
if match:
    import html
    srcdoc = html.unescape(match.group(1))
    with open('mockup.html', 'w') as f:
        f.write(srcdoc)
    print("Extracted to mockup.html")
else:
    print("Not found")
