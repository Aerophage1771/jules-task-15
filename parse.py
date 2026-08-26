import re
with open('inputs/Theme-02-Metropolitan-Riviera.html', 'r') as f:
    text = f.read()

# Extract fonts for Bentinck and Onest, or at least Didone and Gross
# Actually let's just grep for `@font-face`
for m in re.finditer(r'@font-face\s*{([^}]+)}', text):
    content = m.group(1)
    if 'family' in content:
        name = re.search(r'font-family:\s*([^;]+)', content)
        if name:
            print(name.group(1).strip())
