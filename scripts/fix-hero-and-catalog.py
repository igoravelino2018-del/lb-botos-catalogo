from pathlib import Path
p=Path('index.html')
s=p.read_text()
old='<div class="ref-media"><img src="https://raw.githubusercontent.com/igoravelino2018-del/lb-botos-catalogo/main/assets/hero-laysa-adv-pcx.jpg" alt="Laysa com Honda ADV 160 e Honda PCX 160"></div>'
new='<div class="ref-media"><img id="heroImageDesktop" class="hero-media-desktop" alt="LB Motos com Honda ADV e PCX"><img id="heroImageMobile" class="hero-media-mobile" alt="LB Motos com Honda ADV e PCX"></div>'
s=s.replace(old,new)
s=s.replace('<img id="heroImageDesktop" alt="" style="display:none"><img id="heroImageMobile" alt="" style="display:none">','')
css='''\n/* hero media + catalog recovery */\n.hero-media-desktop{display:block!important}.hero-media-mobile{display:none!important}\n#guideOverlay{display:none!important}\n@media(max-width:800px){.hero-media-desktop{display:none!important}.hero-media-mobile{display:block!important}.ref-media img{object-fit:cover!important;object-position:center 68%!important}}\n'''
s=s.replace('</style>',css+'\n</style>',1)
marker='<div id="catalogMount"><div class="loading">Carregando catálogo...</div></div>'
shim='''<div id="guideOverlay" aria-hidden="true"><button id="guideClose" type="button"></button><div id="guideTitle"></div><div id="guideLead"></div><div id="guidePoints"></div><div id="guideNote"></div><a id="guideCta" href="#"></a></div>\n'''
s=s.replace(marker,shim+marker)
p.write_text(s)
