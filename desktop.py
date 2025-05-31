"""Интерфейс решения квадратного уравнения на Tkinter"""
import tkinter as tk
from logic import kv_ur


class Frame1(tk.Frame):
    """Первый фрейм"""
    def __init__(self):
        super().__init__()

        self.lab_abc = tk.Label(
            self, width=43, text='Введите значения a, b и с:',
            bg='white', height=1
            )

        self.ent_a = tk.Entry(self, width=50, bg='gray')

        self.ent_b = tk.Entry(self, width=50, bg='gray')

        self.ent_c = tk.Entry(self, width=50, bg='gray')

        self.lab_abc.pack()

        self.ent_a.pack()

        self.ent_b.pack()

        self.ent_c.pack()


class Frame2(Frame1):
    """Второй фрейм"""
    def __init__(self):
        super().__init__()

        self.lab_message = tk.Label(self, width=80, bg='gray')

        self.lab_1 = tk.Label(self, width=80, bg='gray')

        self.lab_2 = tk.Label(self, width=80, bg='gray')

        self.lab_3 = tk.Label(self, width=80, bg='gray')

        self.lab_text_1 = tk.Label(self, width=80, bg='white')

        self.lab_text_2 = tk.Label(self, width=80, bg='white')

        self.lab_text_3 = tk.Label(self, width=80, bg='white')

        self.but = tk.Button(
            self, width=80,
            text='Вычислить', bg='black', fg='white', command=self.vichisl
            )

        self.but.bind(self, '<Button-1>', self.vichisl)

        self.but.pack()

        self.lab_message.pack()

        self.lab_text_1.pack()

        self.lab_1.pack()

        self.lab_text_2.pack()

        self.lab_2.pack()

        self.lab_3.pack()

    def vichisl(self):
        """Функция для вычислений"""
        self.lab_1['text'] = ''
        self.lab_2['text'] = ''
        self.lab_3['text'] = ''
        self.lab_text_1['text'] = ''
        self.lab_text_2['text'] = ''
        self.lab_text_3['text'] = ''
        a = int(self.ent_a.get())
        b = int(self.ent_b.get())
        c = int(self.ent_c.get())
        otvet = kv_ur(a, b, c)
        self.lab_message['text'] = otvet[0]
        if len(otvet) == 4:
            self.lab_text_1['text'] = "Дискриминант:"
            self.lab_1['text'] = otvet[1]
            self.lab_text_2['text'] = "Корни:"
            self.lab_2['text'] = f'x1={otvet[2]}'
            self.lab_3['text'] = f'x2={otvet[3]}'
        elif len(otvet) == 3:
            self.lab_text_1['text'] = "Дискриминант:"
            self.lab_1['text'] = otvet[1]
            self.lab_text_2['text'] = "Корни:"
            self.lab_2['text'] = otvet[2]
        elif len(otvet) == 2:
            self.lab_text_1['text'] = "Корни:"
            self.lab_1['text'] = otvet[1]


class Kvurtkint(tk.Tk, Frame2):
    """Класс для создания окна программы"""

    def __init__(self):
        super().__init__()

        self.title("Решение квадратного уравнения")

        Frame2().pack()


if __name__ == "__main__":
    app = Kvurtkint()
    app.mainloop()
