import os


class Preview:
    def __init__(self, lang: str):
        self.lang = lang

    def __call__(self):
        os.system("cls" if os.name == "nt" else "clear")
        if self.lang == "en":
            Preview.preview_en()
        elif self.lang == "ru":
            Preview.preview_ru()
        else:
            Preview.preview_ua()

    def preview_en():
        print(
            """
     _      ___            _    _____         ____ _     ___
    | |__  / _ \ _ __ ___ | |__|___ / _ __   / ___| |   |_ _|
    | '_ \| | | | '_ ` _ \| '_ \ |_ \| '__| | |   | |    | |
    | |_) | |_| | | | | | | |_) |__) | |    | |___| |___ | |
    |_.__/ \___/|_| |_| |_|_.__/____/|_|     \____|_____|___|
        """
        )
        print()
        print("\033[35m[*]\033[0m {}".format("Made by Moonquit (github.com)"))
        print("\033[31m[*]\033[0m {}".format('Press "CTRL + C" or "CTRL + Z" to exit'))
        print(
            f"""
        _________________________________________________
        |_________________________________________________|

                [\033[34m{1}\033[0m] {'quick start'}
                [\033[34m{2}\033[0m] {'custom start'}
                [\033[34m{3}\033[0m] {'change language'}
                [\033[34m{99}\033[0m] {'exit'}
        _________________________________________________
        |_________________________________________________|               
            """
        )

    def preview_ru():
        print(
            """
     _      ___            _    _____         ____ _     ___
    | |__  / _ \ _ __ ___ | |__|___ / _ __   / ___| |   |_ _|
    | '_ \| | | | '_ ` _ \| '_ \ |_ \| '__| | |   | |    | |
    | |_) | |_| | | | | | | |_) |__) | |    | |___| |___ | |
    |_.__/ \___/|_| |_| |_|_.__/____/|_|     \____|_____|___|
        """
        )
        print()
        print("\033[35m[*]\033[0m {}".format("Cоздатель: Moonquit (github.com)"))
        print(
            "\033[31m[*]\033[0m {}".format(
                'Нажмините "CTRL + C" или "CTRL + Z" для выхода'
            )
        )
        print(
            f"""
        _________________________________________________
        |_________________________________________________|

                [\033[34m{1}\033[0m] {'быстрый запуск'}
                [\033[34m{2}\033[0m] {'кастомный запуск'}
                [\033[34m{3}\033[0m] {'сменить язык'}
                [\033[34m{99}\033[0m] {'выход'}
        _________________________________________________
        |_________________________________________________|               
            """
        )

    def preview_ua():
        print(
            """
     _      ___            _    _____         ____ _     ___
    | |__  / _ \ _ __ ___ | |__|___ / _ __   / ___| |   |_ _|
    | '_ \| | | | '_ ` _ \| '_ \ |_ \| '__| | |   | |    | |
    | |_) | |_| | | | | | | |_) |__) | |    | |___| |___ | |
    |_.__/ \___/|_| |_| |_|_.__/____/|_|     \____|_____|___|
        """
        )
        print()
        print("\033[35m[*]\033[0m {}".format("Творець: Moonquit (github.com)"))
        print(
            "\033[31m[*]\033[0m {}".format(
                'Нажмініте "CTRL + C" або "CTRL + Z" для виходу'
            )
        )
        print(
            f"""
        _________________________________________________
        |_________________________________________________|

                [\033[34m{1}\033[0m] {'швидкий запуск'}
                [\033[34m{2}\033[0m] {'кастомний запуск'}
                [\033[34m{3}\033[0m] {'змінити мову'}
                [\033[34m{99}\033[0m] {'вихід'}
        _________________________________________________
        |_________________________________________________|               
            """
        )