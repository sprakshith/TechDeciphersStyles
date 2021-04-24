import seaborn as sns
import urllib.request as req
from IPython.core.display import HTML


current_theme = 'gray_area'


def load_css(theme=None):
    response_main = req.urlopen(
        'https://raw.githubusercontent.com/sprakshith/TechDeciphersStyles/main/static/main.css')

    if theme == 'cyan_sisters':
        global current_theme
        current_theme = 'cyan_sisters'

        response_theme = req.urlopen(
            'https://raw.githubusercontent.com/sprakshith/TechDeciphersStyles/main/static/cyan_sisters.css')

        return HTML('<style>' + response_main.read().decode('utf-8') +
                    response_theme.read().decode('utf-8') + '</style>')
    elif theme == 'dark_matter':
        global current_theme
        current_theme = 'dark_matter'

        response_theme = req.urlopen(
            'https://raw.githubusercontent.com/sprakshith/TechDeciphersStyles/main/static/dark_matter.css')

        return HTML('<style>' + response_main.read().decode('utf-8') +
                    response_theme.read().decode('utf-8') + '</style>')
    elif theme == 'genus_lavandula':
        global current_theme
        current_theme = 'genus_lavandula'

        response_theme = req.urlopen(
            'https://raw.githubusercontent.com/sprakshith/TechDeciphersStyles/main/static/genus_lavandula.css')

        return HTML('<style>' + response_main.read().decode('utf-8') +
                    response_theme.read().decode('utf-8') + '</style>')
    else:
        global current_theme
        current_theme = 'gray_area'

        response_theme = req.urlopen(
            'https://raw.githubusercontent.com/sprakshith/TechDeciphersStyles/main/static/gray_area.css')

        return HTML('<style>' + response_main.read().decode('utf-8') +
                    response_theme.read().decode('utf-8') + '</style>')


def get_color_palette(theme=None):
    if theme == 'cyan_sisters':
        return sns.color_palette(['#39ace7', '#0784b5'])
    elif theme == 'dark_matter':
        return sns.color_palette(['#757575', '#212121'])
    elif theme == 'genus_lavandula':
        return sns.color_palette(['#a176c6', '#8653af'])
    else:
        return sns.color_palette(['#78909C', '#37474F'])


def get_background_color():
    if current_theme == 'cyan_sisters':
        return '#cadeef'
    elif current_theme == 'dark_matter':
        return '#e0e0e0'
    elif current_theme == 'genus_lavandula':
        return '#e9d5eb'
    else:
        return '#CFD8DC'
