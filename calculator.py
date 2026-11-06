from utils import parse_date, days_between, add_days, is_valid_date

class DayCalculator:
    def calculate_difference(self, start_text, end_text):
        if not is_valid_date(start_text):
            raise ValueError("Неверная дата начала")
        if not is_valid_date(end_text):
            raise ValueError("Неверная дата окончания")
        start = parse_date(start_text)
        end = parse_date(end_text)
        return days_between(start, end)

    def calculate_target_date(self, start_text, days_text):
        if not is_valid_date(start_text):
            raise ValueError("Неверная дата начала")
        try:
            days = int(days_text.strip())
        except ValueError:
            raise ValueError("Количество дней должно быть целым числом")
        start = parse_date(start_text)
        return add_days(start, days)

    def calculate_weekday(self, date_text):
        if not is_valid_date(date_text):
            raise ValueError("Неверная дата")
        d = parse_date(date_text)
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг",
                    "Пятница", "Суббота", "Воскресенье"]
        return weekdays[d.weekday()]

    def is_leap_year(self, year_text):
        try:
            year = int(year_text.strip())
        except ValueError:
            raise ValueError("Год должен быть целым числом")
        if year < 1 or year > 9999:
            raise ValueError("Год вне допустимого диапазона")
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)