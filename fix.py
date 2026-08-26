import re
with open('index.html', 'r') as f:
    text = f.read()

# Replace the inner course id
text = text.replace('<section id="course" class="portal-section">', '<section id="course-library" class="portal-section">')
text = text.replace('<a href="#course">Course</a>', '<a href="#course-library">Course</a>')

with open('index.html', 'w') as f:
    f.write(text)
