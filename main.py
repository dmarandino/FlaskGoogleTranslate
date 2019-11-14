from flask import Flask, render_template, flash, redirect, url_for
from flask_googletrans import translator
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
ts = translator(app)
Bootstrap(app)
app.config['SECRET_KEY'] = 'Random String'

textin = 'test 123'
keys = 'fr'
all_languages = {'af': 'afrikaans',
                 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic',
                 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque',
                 'be': 'belarusian',
                 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian',
                 'ca': 'catalan',
                 'ceb': 'cebuano', 'ny': 'chichewa',
                 'zh-cn': 'chinese (simplified)',
                 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
                 'hr': 'croatian',
                 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
                 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino',
                 'fi': 'finnish',
                 'fr': 'french', 'fy': 'frisian',
                 'gl': 'galician', 'ka': 'georgian',
                 'de': 'german', 'el': 'greek',
                 'gu': 'gujarati', 'ht': 'haitian creole',
                 'ha': 'hausa', 'haw': 'hawaiian',
                 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
                 'hu': 'hungarian',
                 'is': 'icelandic',
                 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish',
                 'it': 'italian',
                 'ja': 'japanese',
                 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh',
                 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)',
                 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
                 'lt': 'lithuanian',
                 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy',
                 'ms': 'malay', 'ml': 'malayalam',
                 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
                 'mn': 'mongolian',
                 'my': 'myanmar (burmese)',
                 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto',
                 'fa': 'persian', 'pl': 'polish',
                 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
                 'ru': 'russian', 'sm': 'samoan',
                 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
                 'sn': 'shona', 'sd': 'sindhi',
                 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian',
                 'so': 'somali', 'es': 'spanish',
                 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish',
                 'tg': 'tajik', 'ta': 'tamil',
                 'te': 'telugu', 'th': 'thai', 'tr': 'turkish',
                 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek',
                 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
                 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu',
                 'fil': 'Filipino', 'he': 'Hebrew'}
trans_lang = 'en'


class TranslationForm(FlaskForm):
    inputText = StringField('Text to translate', validators=[DataRequired()])
    language = StringField('Language to translate to', validators=[DataRequired()])
    submit = SubmitField('Translate')


def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = TranslationForm()
    if form.validate_on_submit():
        global textin
        global trans_lang
        global keys

        textin = form.inputText.data
        trans_lang = form.language.data.lower()

        keys = getKeysByValue(all_languages, trans_lang)
        return redirect(url_for('main'))
    return render_template('home.html', form=form)


@app.route("/translate", methods=['GET', 'POST'])
def main():
    print(all_languages.get('german', 'none'))
    return render_template('index.html', text=textin, src='en', dest=keys)


@app.route("/supported", methods=['GET', 'POST'])
def supported():
    return render_template('supported.html', all_languages=all_languages)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
