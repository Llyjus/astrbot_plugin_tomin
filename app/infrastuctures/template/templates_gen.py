import base64

from pathlib import Path
from jinja2 import Template
from app.schemas import  *


'''
title:str
intro:str

'''




template_path = Path(__file__).resolve().parent / 'templates'

def template_generator(temp:str, content:dict) -> str:
    '''
    combine base html and css with template html and css, 
    then render the final html with content
    '''

    
    def loader(name: str) -> str:
        return (template_path / name).read_text(encoding="utf-8")
    
    # load base html and css
    base_html = loader("base.html")
    base_css  = loader("base.css")
    base = base_html.replace("/* style_base */", base_css)
        
    static_link = Path(__file__).resolve().parents[1] / "images"

    def uri(p: Path, mime="image/jpeg") -> str:
        return "data:%s;base64,%s" % (
            mime,
            base64.b64encode(p.read_bytes()).decode("ascii")
        )


    # hardcode replace background image with base64
    def background_hardcode_replace(html:str, content:dict):

        from pathlib import Path
        '''
        background1_url:str
        background2_url:str
        background3_url:str
        avatar_url:str
        '''


        


        user_avatar_link = content.get('avatar_path', )
        bg1 = uri(static_link / "backgrounds/background1.jpg")
        bg2 = uri(static_link / "backgrounds/background2.jpg")
        bg3 = uri(static_link / "backgrounds/background3.jpg")
        avtr = uri(static_link / "logo/logo.jpg") if not user_avatar_link else uri(Path(user_avatar_link))  

        html = html.replace("background1_url", bg1)
        html = html.replace("background2_url", bg2)
        html = html.replace("background3_url", bg3)
        html = html.replace("avatar_url", avtr)
        return html








    # templates renderer
    def cards_temp(html:str, content:dict):




        '''
cards:cards list
    (for card in cards: attributes(str) list)
        '''




        card_html = loader("cards.html")
        card_css = loader('cards.css')
        # assert character's picture for each card
        for card in content['cards']:
            character:str = card['picture_key'][0]
            rarity:str = card['picture_key'][1]
            pic_path = static_link / "characters" / character / f"{rarity}.png"
            if pic_path.exists():
                path = uri(pic_path)
            else:
                path = ""
            card['picture'] = path
        
        # base_href = f'<base href="{base_link}">'

        html = html.replace("<!-- content -->", card_html)
        html = html.replace('/* style_custom */', card_css)
        # html = html.replace('<!-- base -->', base_href)


        card_tpl = Template(html)
        return card_tpl.render(**content)




    temp_dict = {
        'cards':cards_temp

    }


    # call renderer
    if temp not in temp_dict:
        raise Invalid_input(f'未知的模板类型：{temp}')

    html = background_hardcode_replace(base, content)
    html = temp_dict[temp](html, content)

    return html

