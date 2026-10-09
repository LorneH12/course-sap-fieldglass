"""Rebuild the branded release; run from any directory with Python 3."""
from pathlib import Path
import json,zipfile,html
r=Path(__file__).resolve().parent
c=json.loads((r/'branded-course.json').read_text())
(r/'course-data.js').write_text('window.COURSE='+json.dumps(c,ensure_ascii=False)+';')
files=['hero-editorial.jpg','index.html','course-data.js','experience.js','experience.css','widgets.js','companion.txt','companion.vtt','js/tracking.js']
manifest='<?xml version="1.0"?><manifest identifier="'+c['id']+'-branded" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2" xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"><metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata><organizations default="org"><organization identifier="org"><title>'+html.escape(c['title'])+'</title><item identifier="item" identifierref="sco"><title>'+html.escape(c['title'])+'</title></item></organization></organizations><resources><resource identifier="sco" type="webcontent" adlcp:scormtype="sco" href="index.html">'+''.join('<file href="'+n+'"/>' for n in files)+'</resource></resources></manifest>'
with zipfile.ZipFile(r/'release-scorm12.zip','w',zipfile.ZIP_DEFLATED) as z:
 for n in files:z.write(r/n,n)
 z.writestr('imsmanifest.xml',manifest)
print('Branded SCORM 1.2 candidate rebuilt; external video requires internet.')
