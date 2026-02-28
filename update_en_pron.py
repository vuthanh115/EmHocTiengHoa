import json
import re

html_file = r"c:\Users\vophi\Downloads\Github\Math_L4_2\EmHocTiengHoa\index.html"

pinyin_to_en = {
    "bàba": "bah-bah", "māma": "mah-mah", "gēge": "guh-guh", "dìdi": "dee-dee",
    "āyí": "ah-yee", "bóbo": "bwo-bwo", "nǐ hǎo": "nee how", "nín hǎo": "neen how",
    "mèimei": "may-may", "māo": "maow", "gǒu": "go", "wǒ": "waw", "hǎo": "how",
    "píngguǒ": "peeng-gwo", "pútao": "poo-taow", "lí": "lee",
    "dàngāo": "dahn-gow", "bǐnggān": "beeng-gahn", "táng": "tahng", "kāfēi": "kah-fay",
    "chá": "chah", "niúnǎi": "nyo-nye", "zhè": "juh", "shì": "shrr",
    "miànbāo": "myen-bow", "niúròu": "nyo-ro", "miàntiáo": "myen-tyaow", "zhōu": "joe",
    "lǎoshī": "laow-shrr", "gōngrén": "gong-run", "yéye": "yeh-yeh", "nǎinai": "nye-nye",
    "wǎn": "wahn", "kuàizi": "kwye-zih", "cài": "tsye", "fàn": "fahn", "nà": "nah",
    "huā": "hwah", "yèzi": "yeh-zih", "cǎo": "tsow", "shù": "shoo", "sēnlín": "sun-leen",
    "zhuōzi": "jwo-zih", "yǐzi": "yee-zih", "chuáng": "chwahng", "shūbāo": "shoo-bow", "sǎn": "sahn",
    "fēijī": "fay-jee", "qìchē": "chee-chuh", "lúnchuán": "lwun-chwahn", "zìxíngchē": "zih-sheeng-chuh", "yǒu": "yo",
    "jīqìrén": "jee-chee-run", "píqiú": "pee-chyo", "wáwa": "wah-wah", "xióngmāo": "shyong-maow", "huǒjiàn": "hwo-jyen",
    "Zhōngguó": "jong-gwo", "guóqí": "gwo-chee", "Běijīng": "bay-jeeng", "Tiān'ānmén": "tyen-ahn-mun", "Chángchéng": "chahng-chung",
    "yǔ": "yoo", "xuě": "shweh", "wù": "woo", "fēng": "fung", "xià": "shyah",
    "tàiyáng": "tye-yahng", "yuèliang": "yweh-lyahng", "yún": "ywin", "xīngxing": "sheeng-sheeng", "cǎihóng": "tsye-hong",
    "ěrduo": "ur-dwo", "bízi": "bee-zih", "yǎnjing": "yen-jeeng", "zuǐ": "zway", "shǒu": "show", "jiǎo": "jyaow",
    "shǒutào": "show-taow", "shǒujuàn": "show-jwen", "xié": "shyeh", "kùzi": "koo-zih", "qúnzi": "chwin-zih", "shàngyī": "shahng-yee",
    "shū": "shoo", "huàr": "hwar", "bǐ": "bee", "de": "duh", "yīfu": "yee-foo", "kàn": "kahn",
    "qǐchuáng": "chee-chwahng", "chànggē": "chahng-guh", "tiàowǔ": "tyaow-woo", "wán yóuxì": "wahn yo-shee", "shuìjiào": "shway-jyaow", "xué Hànyǔ": "shweh hahn-yoo",
    
    # Examples
    "Bàba hǎo!": "bah-bah how!", "Māma hǎo!": "mah-mah how!", "Āyí hǎo!": "ah-yee how!", "Bóbo hǎo!": "bwo-bwo how!",
    "Mèimei hǎo!": "may-may how!", "Nǐ hǎo!": "nee how!", "Wǒ yào pútao.": "waw yaow poo-taow.", "Dìdi yào píngguǒ.": "dee-dee yaow peeng-gwo.",
    "Gēge yào kāfēi.": "guh-guh yaow kah-fay.", "Wǒ yào dàngāo.": "waw yaow dahn-gow.", "Zhè shì chá.": "juh shrr chah.", "Zhè shì niúnǎi.": "juh shrr nyo-nye.",
    "Zhè shì niúròu.": "juh shrr nyo-ro.", "Wǒ yào miànbāo.": "waw yaow myen-bow.", "Zhè shì lǎoshī.": "juh shrr laow-shrr.", "Lǎoshī hǎo!": "laow-shrr how!",
    "Zhè shì shénme?": "juh shrr shun-muh?", "Zhè shì wǎn.": "juh shrr wahn.", "Zhè shì huā.": "juh shrr hwah.", "Nà shì yèzi.": "nah shrr yeh-zih.",
    "Wǒ yǒu zhuōzi, yǐzi.": "waw yo jwo-zih, yee-zih.", "Zhè shì shūbāo.": "juh shrr shoo-bow.", "Nǐ yǒu fēijī ma?": "nee yo fay-jee mah?", "Wǒ yǒu fēijī.": "waw yo fay-jee.",
    "Wǒ yǒu jīqìrén.": "waw yo jee-chee-run.", "Wǒ méi yǒu huǒjiàn.": "waw may yo hwo-jyen.", "Zhè shì guóqí ma?": "juh shrr gwo-chee mah?", "Zhè shì Zhōngguó guóqí.": "juh shrr jong-gwo gwo-chee.",
    "Xià yǔ le!": "shyah yoo luh!", "Xià xuě le!": "shyah shweh luh!", "Nà shì tàiyáng ma?": "nah shrr tye-yahng mah?", "Nà bú shì tàiyáng, nà shì yuèliang.": "nah boo shrr tye-yahng, nah shrr yweh-lyahng.",
    "Zhè shì ěrduo ma?": "juh shrr ur-dwo mah?", "Zhè shì yǎnjing.": "juh shrr yen-jeeng.", "Zhè shì wǒ de yīfu.": "juh shrr waw duh yee-foo.", "Nà shì dìdi de kùzi.": "nah shrr dee-dee duh koo-zih.",
    "Wǒ kàn shū.": "waw kahn shoo.", "Dìdi huà huàr.": "dee-dee hwah hwar.", "Wǒmen chànggē.": "waw-mun chahng-guh.", "Wǒmen tiàowǔ.": "waw-mun tyaow-woo."
}

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'const DATA = (\[.*?\]);', content, re.DOTALL)
if match:
    data_str = match.group(1)
    
    try:
        data = json.loads(data_str)
        
        for lesson in data:
            if 'vocab' in lesson:
                for word in lesson['vocab']:
                    pinyin = word['pinyin']
                    if 'ipa' in word:
                        del word['ipa']
                    if pinyin in pinyin_to_en:
                        word['en_pron'] = pinyin_to_en[pinyin]
                    else:
                        print(f"Missing en_pron for vocab: {pinyin}")
                        word['en_pron'] = pinyin
                        
            if 'examples' in lesson:
                for ex in lesson['examples']:
                    pinyin = ex['pinyin']
                    if 'ipa' in ex:
                        del ex['ipa']
                    if pinyin in pinyin_to_en:
                        ex['en_pron'] = pinyin_to_en[pinyin]
                    else:
                        print(f"Missing en_pron for example: {pinyin}")
                        ex['en_pron'] = pinyin

        new_data_str = json.dumps(data, ensure_ascii=False, indent=12)
        new_content = content.replace(data_str, new_data_str)
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print("Updated index.html with EN phonetic successfully.")
        
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")
        
else:
    print("Could not find DATA pattern.")
