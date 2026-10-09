from pathlib import Path
import json,zipfile,html
r=Path(__file__).resolve().parents[1]
cpath=r/'assets/course.json'
if cpath.exists():
 c=json.loads(cpath.read_text());(r/'js/content.js').write_text('window.COURSE='+json.dumps(c,ensure_ascii=False)+';');(r/'css/brand.css').write_text(':root{--primary:'+c['brand']['primary']+';--ink:'+c['brand']['ink']+'}')
name=r.name
files=[p for base in ['index.html','css','js','assets'] for p in ([r/base] if (r/base).is_file() else (r/base).rglob('*')) if p.is_file()]
manifest='<?xml version="1.0" encoding="UTF-8"?><manifest identifier="'+name+'" version="1.0" xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2" xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"><metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata><organizations default="org"><organization identifier="org"><title>'+name+'</title><item identifier="item" identifierref="sco"><title>'+name+'</title></item></organization></organizations><resources><resource identifier="sco" type="webcontent" adlcp:scormtype="sco" href="index.html">'+''.join('<file href="'+html.escape(str(p.relative_to(r)),quote=True)+'"/>' for p in files)+'</resource></resources></manifest>'
(r/'imsmanifest.xml').write_text(manifest);(r/'dist').mkdir(exist_ok=True)
with zipfile.ZipFile(r/'dist'/ (name+'-scorm12.zip'),'w',zipfile.ZIP_DEFLATED) as z:
 for p in files+[r/'imsmanifest.xml']:z.write(p,str(p.relative_to(r)))
print(name+' packaged')
