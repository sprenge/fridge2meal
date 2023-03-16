# pip3 install PyMuPDF
import re
import os
import time
import fitz
from bs4 import BeautifulSoup

base = "C:\\tmp\\"
fn1 = os.path.join(base+'IEZG2__thema_2022.pdf')
fn2 = os.path.join(base+'IEZG2_index_ingrediënten_2022.pdf')
fn3 = os.path.join(base+'IEZG2_index_recepten_2022.pdf')

ingredient_translation_table = {
    'Bessen, zwarte': 'Zwarte bessen',
    'Kool, rode': 'Rode kool',
    'Wijn, rode': 'Rode wijn',
    'Rijst, wilde': 'Wilde rijst',
    'Aardappel, zoet': 'Zoete aardappel',
    'Bessen, blauwe': 'Blauwe bessen',
    'Ham, gedroogd': 'Gedroogde ham',
    'Tomaat, gedroogd': 'Gedroogde tomaat',
    'Biet, rode': 'Rode biet',
    'Peper, rode': 'Rode peper',
    'Besjes, rood': 'Rode besjes',
    'Wijn, witte': 'Witte wijn',
    'Bonen, zwarte': 'Zwarte bonen',
    'Kool, witte': 'Witte kool',
    'Bonen, witte': 'Witte bonen',
}


# recipes pointing to book and page number book
recipe_list = []
with fitz.open(fn1) as doc:
    recipe_list = []
    for page in doc:
        html = page.get_text("html")
        parsed_html = BeautifulSoup(html, 'html.parser')

        ps = parsed_html.find_all('p')
        plist = []
        for p in ps:
            plist.append(p)
        i = 0
        for p in plist:
            s = p['style']
            if "left:62.4pt" in s:
                receipt = p.span.string
                if receipt != "Recept":
                    rec = {
                        "recipe": p.span.string.strip(),
                        "book": plist[i+1].span.string,
                        "page": plist[i+2].span.string
                    }
                    # print(rec)
                    recipe_list.append(rec)
            i += 1

recipe_ing = {}  # index is recipe + book , data = list of ingredients
for r in recipe_list:
    try:
        i = int(r['page'])
        akey = r['book']+'_' + r['page']
        if akey not in recipe_ing:
            recipe_ing[akey] = {"recipe": r['recipe'], "ingredient_list": []}
    except:
        print("no valid page for", r)

plist = []

with fitz.open(fn2) as doc:
    nbr_match = 0
    page_nbr = 1
    for page in doc:
        html = page.get_text("html")
        parsed_html = BeautifulSoup(html, 'html.parser')
        # print(parsed_html)
        ps = parsed_html.find_all('p')
        for p in ps:
            plist.append(p)
            # print(p)
i = 0
scope_ingredient = ""
ingredient_list = []

for p in plist:
    s = p['style']
    t = p.span.string
    if "left:79." in s:
        scope_ingredient = t
    if "left:167.2" in s or "left:167.3" in s:
        try:
            r = t.strip().lower().capitalize()
            r = re.sub(' +', ' ', r)
            if r != "Recept":
                rec = {
                    "ingredient": scope_ingredient,
                    "recipe": r,
                    "book": plist[i+1].span.string,
                    "page": plist[i+2].span.string
                }
                try:
                    a = int(rec['page'])
                    ingredient_list.append(rec)
                except:
                    # print("exception for", r)
                    rec['book'] = "to_be_completed"
                    rec['page'] = "to be completed"
                ingredient_list.append(rec)
        except Exception as e:
            print(len(plist), i)
            print("exc", e)
        nbr_match += 1
    i += 1

recipe_ing = {}  # index is recipe + book , data = list of ingredients
ingredients = set()
for ing in ingredient_list:
    akey = ing['book']+'_' + ing['page']
    if akey not in recipe_ing:
        recipe_ing[akey] = {"recipe": ing['recipe'], "ingredient_list": set()}
    recipe_ing[akey]['ingredient_list'].add(ing['ingredient'])
    ingredients.add(ing['ingredient'])
    # print(ing)
print(len(recipe_ing))
for e in recipe_ing:
    pass
    if 'PP_' in e:
        pass
        # print(e, recipe_ing[e])

for i in ingredients:
    if ',' in i:
        pass
        print(i)
    else:
        if ' ' in i:
            pass
            print(i)
# print(ingredients)
print(len(ingredients))
