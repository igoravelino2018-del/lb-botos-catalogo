from pathlib import Path
p=Path('index.html')
s=p.read_text()
# direct, stable hero sources
s=s.replace('<img id="heroImageDesktop" class="hero-media-desktop" alt="LB Motos com Honda ADV e PCX">','<img id="heroImageDesktop" class="hero-media-desktop" src="/assets/hero-desktop-v2.webp?v=20" alt="LB Motos com Honda ADV e PCX">')
s=s.replace('<img id="heroImageMobile" class="hero-media-mobile" alt="LB Motos com Honda ADV e PCX">','<img id="heroImageMobile" class="hero-media-mobile" src="/assets/hero-mobile-v2.webp?v=20" alt="LB Motos com Honda ADV e PCX">')
# point CTAs to the embedded full catalog
s=s.replace('href="#catalogMount">Escolher minha Honda ›</a>','href="#catalogFrame">Escolher minha Honda ›</a>')
s=s.replace('class="featured-more" href="#catalogMount"','class="featured-more" href="#catalogFrame"')
# robust full catalog iframe replaces fragile async mount
start=s.find('<div id="catalogMount">')
script=s.find('<script>',start)
end_script=s.find('</script>',script)+9
if start!=-1 and script!=-1 and end_script>8:
    replacement='''<section id="catalogFrame" class="catalog-frame-wrap" aria-label="Catálogo completo"><iframe src="/catalog-core.html?v=4" title="Catálogo completo LB Motos" loading="eager"></iframe></section>'''
    s=s[:start]+replacement+s[end_script:]
css='''\n/* stable homepage v1 */\n.catalog-frame-wrap{width:100%;background:#f7f7f7;overflow:hidden}.catalog-frame-wrap iframe{display:block;width:100%;height:7200px;border:0;background:#fff}\n@media(max-width:800px){.catalog-frame-wrap iframe{height:9800px}.ref-media{min-height:360px!important}.ref-media img{width:100%!important;height:100%!important;object-fit:cover!important}}\n'''
s=s.replace('</style>',css+'</style>',1)
p.write_text(s)
