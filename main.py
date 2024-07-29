"""Менеджер задач
Задача: Создай класс Task, который позволяет управлять задачами (делами).
У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
(выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
выполненных задач и вывода списка текущих (не выполненных) задач.
"""


class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline,
                           'description': description, 'status': "не выполнено"})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Выполнено"
                print(f"Задача {description} выполнена")

    def show_tasks(self):
        print("текущие задачи")
        for task in self.tasks:
            if task ['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")


t = Task()
t.add_task("08.08.2024", "Прочитать книгу")
t.add_task("08.08.2024", "Пробежать марафон")
t.add_task("08.08.2024", "Починить машину")

t.show_tasks()

t.complete_tasks("Прочитать книгу")
t.show_tasks()