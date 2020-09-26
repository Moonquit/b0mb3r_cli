import os


PREVIEW = """
 _      ___            _    _____         ____ _     ___
| |__  / _ \ _ __ ___ | |__|___ / _ __   / ___| |   |_ _|
| '_ \| | | | '_ ` _ \| '_ \ |_ \| '__| | |   | |    | |
| |_) | |_| | | | | | | |_) |__) | |    | |___| |___ | |
|_.__/ \___/|_| |_| |_|_.__/____/|_|     \____|_____|___|
"""

AUTHOR = "\033[35m[*]\033[0m {} Moonquit (github.com)"
HOW_STOP = '\033[31m[*]\033[0m {} "CTRL + C" or "CTRL + Z" {}'


class Preview:
    def __init__(self, lang: str):
        self.lang = lang

    def __call__(self):
        os.system("cls" if os.name == "nt" else "clear")

        author = AUTHOR.format("Made by")
        how_stop = HOW_STOP.format("Press", "to exit")
        quick_start = "quick start"
        custom_start = "custom start"
        change_lang = "change language"
        exit_ = "exit"

        if self.lang == "en":
            pass
        elif self.lang == "ru":
            author = AUTHOR.format("Создатель:")
            how_stop = HOW_STOP.format("Нажмите", "для выхода")
            quick_start = "быстрый запуск"
            custom_start = "кастомный запуск"
            change_lang = "сменить язык"
            exit_ = "выход"
        elif self.lang == "ua":
            author = AUTHOR.format("Творець:")
            how_stop = HOW_STOP.format("Нажмініте", "для виходу")
            quick_start = "швидкий запуск"
            custom_start = "кастомний запуск"
            change_lang = "змінити мову"
            exit_ = "вихід"
        else:
            raise ValueError("Unknown language passed! (languages: en, ru, ua)")

        self._run(
            preview=PREVIEW,
            author=author,
            how_stop=how_stop,
            quick_start=quick_start,
            custom_start=custom_start,
            change_lang=change_lang,
            exit_=exit_,
        )

    def _run(
        self,
        preview: str,
        author: str,
        how_stop: str,
        quick_start: str,
        custom_start: str,
        change_lang: str,
        exit_: str,
    ):
        print(preview)
        print()
        print(author)
        print(how_stop)
        print(
            f"""
         _________________________________________________
        |_________________________________________________|

                [\033[34m{1}\033[0m] {quick_start}
                [\033[34m{2}\033[0m] {custom_start}
                [\033[34m{3}\033[0m] {change_lang}
                [\033[34m{99}\033[0m] {exit_}
         _________________________________________________
        |_________________________________________________|               
            """
        )
