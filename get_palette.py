import re
with open('inputs/Theme-02-Metropolitan-Riviera.html', 'r') as f:
    text = f.read()

match = re.search(r'<h3><span class="accent">/</span>GermaineTutoring.com Production Translation</h3>(.*?)<h3><span class="accent">/</span>Strategies</h3>', text, re.DOTALL)
if match:
    block = match.group(1)
    for chip in re.finditer(r'<div class="hx">([^<]+)</div>', block):
        print(chip.group(1))
