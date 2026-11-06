import tkinter as tk
from tkinter import ttk, messagebox
from calculator import DayCalculator
from utils import format_date

class DayCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.calc = DayCalculator()
        self.root.title("Калькулятор дней")
        self.root.geometry("460x420")
        self.root.resizable(False, False)
        self.build()

    def build(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.tab_diff = ttk.Frame(notebook)
        self.tab_add = ttk.Frame(notebook)
        self.tab_info = ttk.Frame(notebook)
        notebook.add(self.tab_diff, text="Разница дат")
        notebook.add(self.tab_add, text="Прибавить дни")
        notebook.add(self.tab_info, text="Инфо о дате")
        self.build_diff_tab()
        self.build_add_tab()
        self.build_info_tab()

    def build_diff_tab(self):
        frame = self.tab_diff
        ttk.Label(frame, text="Дата начала (ДД.ММ.ГГГГ):").pack(anchor="w", padx=15, pady=(15, 2))
        self.diff_start = ttk.Entry(frame, width=30)
        self.diff_start.pack(padx=15)
        ttk.Label(frame, text="Дата окончания (ДД.ММ.ГГГГ):").pack(anchor="w", padx=15, pady=(10, 2))
        self.diff_end = ttk.Entry(frame, width=30)
        self.diff_end.pack(padx=15)
        ttk.Button(frame, text="Вычислить", command=self.on_diff).pack(pady=15)
        self.diff_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.diff_result.pack(padx=15, pady=5)

    def build_add_tab(self):
        frame = self.tab_add
        ttk.Label(frame, text="Начальная дата (ДД.ММ.ГГГГ):").pack(anchor="w", padx=15, pady=(15, 2))
        self.add_start = ttk.Entry(frame, width=30)
        self.add_start.pack(padx=15)
        ttk.Label(frame, text="Количество дней:").pack(anchor="w", padx=15, pady=(10, 2))
        self.add_days = ttk.Entry(frame, width=30)
        self.add_days.pack(padx=15)
        ttk.Button(frame, text="Вычислить", command=self.on_add).pack(pady=15)
        self.add_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.add_result.pack(padx=15, pady=5)

    def build_info_tab(self):
        frame = self.tab_info
        ttk.Label(frame, text="Дата (ДД.ММ.ГГГГ):").pack(anchor="w", padx=15, pady=(15, 2))
        self.info_date = ttk.Entry(frame, width=30)
        self.info_date.pack(padx=15)
        ttk.Button(frame, text="Узнать день недели", command=self.on_weekday).pack(pady=15)
        self.info_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.info_result.pack(padx=15, pady=5)
        ttk.Separator(frame, orient="horizontal").pack(fill="x", padx=15, pady=10)
        ttk.Label(frame, text="Проверить год на високосность:").pack(anchor="w", padx=15, pady=(5, 2))
        self.year_entry = ttk.Entry(frame, width=30)
        self.year_entry.pack(padx=15)
        ttk.Button(frame, text="Проверить", command=self.on_leap).pack(pady=10)
        self.leap_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.leap_result.pack(padx=15, pady=5)

    def on_diff(self):
        try:
            result = self.calc.calculate_difference(self.diff_start.get(), self.diff_end.get())
            self.diff_result.config(text=f"Разница: {result} дней")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            self.diff_result.config(text="")

    def on_add(self):
        try:
            result = self.calc.calculate_target_date(self.add_start.get(), self.add_days.get())
            self.add_result.config(text=f"Результат: {format_date(result)}")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            self.add_result.config(text="")

    def on_weekday(self):
        try:
            result = self.calc.calculate_weekday(self.info_date.get())
            self.info_result.config(text=f"День недели: {result}")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            self.info_result.config(text="")

    def on_leap(self):
        try:
            result = self.calc.is_leap_year(self.year_entry.get())
            text = "Високосный" if result else "Не високосный"
            self.leap_result.config(text=text)
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            self.leap_result.config(text="")