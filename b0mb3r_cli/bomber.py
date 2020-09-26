import re
import time
import subprocess

import requests


class Bomber:
    """
    Main class

    :param lang: Language - en, ru, ua (optional parameter)
    :type lang: str

    """

    def __init__(self, lang: str = "en"):
        if lang.lower() in ["en", "ru", "ua"]:
            self.lang = lang
        else:
            raise ValueError("Unknown language passed! (languages: en, ua, ru)")

    def log_ok(text: str):
        print("\033[32m[*]\033[0m {}".format(str(text)))

    def log_error(text: str):
        print(f"\033[31m[error]\033[0m -> {str(text)}".format(str(text)))

    def log(text="", symbol="*"):
        print(f"\033[34m[{symbol}]\033[0m {text}")

    @staticmethod
    def start(phone: str = "", port: int = 8080, cycles: int = 100, lang: str = "en"):
        """
        bomber launch

        :param phone: Mobile phone
        :type phone: int or str

        :param port: Port for launch local server (optional parameter)
        :type port: int or str

        :param cycles: Number of cycles (repetitions) (optional parameter)
        :type cycles: int or str

        """
        phone = re.sub(r"[^0-9]+", r"", str(phone))
        cycles = re.sub(r"[^0-9]+", r"", str(cycles))
        port = re.sub(r"[^0-9]+", r"", str(port))

        if lang not in ["en", "ru", "ua"]:
            raise ValueError("Unknown language passed! (languages: en, ua, ru)")

        if phone == "" or len(phone) > 12:
            raise ValueError(
                "Incorrect number passed! (examples: +79995554433 or 79995554433)"
            )

        if cycles == "":
            raise ValueError("Incorrect number of cycles passed! (int)")

        if lang == "en":
            Bomber.log_ok("b0mb3r starting...")
        elif lang == "ru" or lang == "ua":
            Bomber.log_ok("Запуск b0mb3r...")

        # start process with bomber
        proc = subprocess.Popen(["b0mb3r", "--only-api", "--port", f"{port}"])

        time.sleep(10)
        base_url = f"http://127.0.0.1:{port}"

        try:
            attack_start = requests.post(
                url=f"{base_url}/attack/start/",
                json={"number_of_cycles": cycles, "phone": phone},
            )

            """
            I decided to remove this piece of code (it's something of a log),
            because I could not disable logs in b0mb3r :)


            if attack_start["success"]:
                attack_id = attack_start["id"]
                url_check_status = f"{base_url}/attack/{attack_id}/status/"
                
                print()
                if lang == "en":
                    log_ok(f"Successful start -> timeout: {timeout}sec, number of cycles: {cycles}")
                elif lang == "ru":
                    log_ok(f"Успешный запуск -> таймаут: {timeout}сек, количество циклов: {cycles}")
                elif lang == "ua":
                    log_ok(f"Успішний запуск -> таймаут: {timeout}сек, кількість цилків: {cycles}")


                bomber_work = True
                count_done = 0

                while bomber_work:
                    try:
                        check_status = requests.get(url_check_status).json()
                    except requests.exceptions.RequestException as err:
                        log_error(f"[status check]: {err}")

                    count_total = int(check_status['end_at'])
                    resp_count_done = int(check_status['currently_at'])

                    if resp_count_done > count_done:
                        log_ok(f"Progress: {resp_count_done}/{count_total}")
                    count_done = resp_count_done

                    if count_done == count_total:
                        count_status =f"{count_done}/{count_total}"

                        if lang == "en":
                            log_ok(f"Spam finished! -> {count_status}")
                        elif lang == "ua":
                            log_ok(f"Спам завершено! -> {count_status}")
                        elif lang == "ru":
                            log_ok(f"Спам завершен! -> {count_status}")

                        bomber_work = False

                    time.sleep(timeout)

            else:
                log_error("[attack start]: Unknown error")
            

        if lang == "en":
            log_ok(f"Spam finished!")
        elif lang == "ua":
            log_ok(f"Спам завершено!")
        elif lang == "ru":
            log_ok(f"Спам завершен!")

        exit("b0mb3r CLI completed!")

            """

        except requests.exceptions.RequestException as err:
            Bomber.log_error(f"[start spam]: {err}")

    def custom_start(self):
        if self.lang == "en":
            Bomber.log("Enter a phone number: (examples: +79995554433 or 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Incorecct number. Try again:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Select port: (by default: 8080)")
            port = re.sub(r"[^0-9]+", r"", input("> "))
            while port == "" or len(port) > 4:
                Bomber.log_error("[port]: Incorrect port! Try again:")
                port = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Enter the number of cycles: (by default: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error("[cycles]: Incorrect number of cycles! Try again:")
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        elif self.lang == "ru":
            Bomber.log("Введите номер: (примеры: +79995554433 или 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Неверный номер! Попробуйте ещё раз:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Выберите порт: (по умолчанию: 8080)")
            port = re.sub(r"[^0-9]+", r"", input("> "))
            while port == "" or len(port) > 4:
                Bomber.log_error("[port]: Неверный порт! Попробуйте ещё раз:")
                port = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Введите количество повторов: (по умолчанию: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error(
                    "[cycles]: Неверное количество повторов! Попробуйте ещё раз:"
                )
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        elif self.lang == "ua":
            Bomber.log("Введіть номер: (приклади: +79995554433 або 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Неправильний номер! Спробуйте ще раз:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Виберіть порт: (за замовчуванням: 8080)")
            port = re.sub(r"[^0-9]+", r"", input("> "))
            while port == "" or len(port) > 4:
                Bomber.log_error("[port]: Невірний порт! Спробуйте ще раз:")
                port = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Введіть кількість повторів: (за замовчуванням: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error(
                    "[cycles]: Неправильне кількість повторів! Спробуйте ще раз:"
                )
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        self.start(phone=phone, port=port, cycles=cycles, lang=self.lang)

    def quick_start(self):
        if self.lang == "en":
            Bomber.log("Enter a phone number: (examples: +79995554433 or 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Incorecct number. Try again:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Enter the number of cycles: (by default: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error("[cycles]: Incorrect number of cycles! Try again:")
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        elif self.lang == "ru":
            Bomber.log("Введите номер: (примеры: +79995554433 или 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Неверный номер! Попробуйте ещё раз:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Введите количество повторов: (по умолчанию: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error(
                    "[cycles]: Неверное количество повторов! Попробуйте ещё раз:"
                )
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        elif self.lang == "ua":
            Bomber.log("Введіть номер: (приклади: +79995554433 або 79995554433)")
            phone = re.sub(r"[^0-9]+", r"", input("> "))
            while phone == "" or len(phone) > 12:
                Bomber.log_error("[number]: Неправильний номер! Спробуйте ще раз:")
                phone = re.sub(r"[^0-9]+", r"", input("> "))

            Bomber.log("Введіть кількість повторів: (за замовчуванням: 100)")
            cycles = re.sub(r"[^0-9]+", r"", input("> "))
            while cycles == "":
                Bomber.log_error(
                    "[cycles]: Неправильне кількість повторів! Спробуйте ще раз:"
                )
                cycles = re.sub(r"[^0-9]+", r"", input("> "))

        self.start(phone=phone, cycles=cycles, lang=self.lang)
