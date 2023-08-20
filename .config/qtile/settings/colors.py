import json
import pathlib

from .path import qtile_path

font_size = 16
font_family = 'HurmitNerdFontMono'


def load_colorscheme() -> dict:
    theme = 'gruvbox'

    theme_file = pathlib.Path(qtile_path) / f'settings/colorscheme/{theme}.json'
    if not theme_file.exists():
        raise Exception(f'"{theme_file}" does not exist')

    with open(theme_file, 'r', encoding='utf-8') as file:
        return json.load(file)


color = load_colorscheme()
