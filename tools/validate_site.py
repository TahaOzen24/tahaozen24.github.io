"""Check public links, canonical URLs, contact details and the tracking-free contract."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json,re,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
PUBLIC=ROOT/'public'
CONFIG=json.loads((ROOT/'site.json').read_text(encoding='utf-8'))

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.ids=set();self.links=[];self.headings=0;self.lang='';self.canonical='';self.scripts=0;self.forms=0;self.style_links=[];self.bad_images=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids,'Duplicate HTML id: '+a['id']
            self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang','')
        if tag=='h1':self.headings+=1
        if tag=='script':self.scripts+=1
        if tag=='form':self.forms+=1
        if tag=='a':self.links.append(a.get('href',''))
        if tag=='link':
            if a.get('rel')=='canonical':self.canonical=a.get('href','')
            if a.get('rel') in ('stylesheet','icon'):self.style_links.append(a.get('href',''))
        if tag=='img' and 'alt' not in a:self.bad_images+=1

def resolve(path):
    relative=unquote(path).lstrip('/')
    target=PUBLIC/relative
    if target.is_dir():target=target/'index.html'
    assert target.resolve().is_relative_to(PUBLIC.resolve()),'Path escapes public root'
    return target

def main():
    parsed={}
    for path in PUBLIC.rglob('*.html'):
        text=path.read_text(encoding='utf-8');page=Page();page.feed(text);parsed[path]=page
        assert page.lang in ('tr','en'),path
        assert page.headings==1 and 'content' in page.ids,path
        assert page.scripts==0 and page.forms==0 and page.bad_images==0,path
        assert CONFIG['email'] in text and 'mailto:'+CONFIG['email'] in text,path
        assert not re.search(r'Lorem ipsum|TODO|TBD|example\.com|your@email|\[your',text,re.I),path
        relative=path.relative_to(PUBLIC).as_posix();route='/'+relative.removesuffix('index.html')
        assert page.canonical==CONFIG['origin']+route,(path,page.canonical,route)
        for asset in page.style_links:
            assert not urlsplit(asset).scheme and resolve(asset).is_file(),(path,asset)
    total=0
    for path,page in parsed.items():
        for href in page.links:
            assert href,'Empty link in '+str(path)
            u=urlsplit(href)
            if u.scheme:
                assert u.scheme in ('https','mailto'),href
                continue
            target=resolve(u.path) if u.path else path
            assert target.is_file(),(path,href)
            if u.fragment:assert target in parsed and unquote(u.fragment) in parsed[target].ids,(path,href)
            total+=1
    tr=parsed[PUBLIC/'block-mirage/privacy/index.html'];en=parsed[PUBLIC/'block-mirage/privacy/en/index.html']
    assert tr.ids==en.ids,'Translated policies must keep the same sections'
    ad=(PUBLIC/'app-ads.txt').read_bytes()
    assert ad==f"google.com, {CONFIG['publisher']}, DIRECT, f08c47fec0942fa0\n".encode(),ad
    assert 'Allow: /' in (PUBLIC/'robots.txt').read_text()
    sitemap=ET.parse(PUBLIC/'sitemap.xml')
    urls=[n.text for n in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert len(urls)==8 and len(set(urls))==8
    for url in urls:
        assert url.startswith(CONFIG['origin']+'/') and resolve(urlsplit(url).path).is_file(),url
    assert not any(p.is_symlink() for p in PUBLIC.rglob('*'))
    print(f'SITE CHECKS PASS: {len(parsed)} HTML pages, {total} internal links, 8 sitemap URLs, matching TR/EN sections, root app-ads.txt and no active third-party scripts/forms')

if __name__=='__main__':main()
