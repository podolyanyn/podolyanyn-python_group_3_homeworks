class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers.copy()

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            if worker.boss != self:
                worker.boss = self
            if worker not in self._workers:
                self._workers.append(worker)
        else:
            raise TypeError("Можна додавати тільки об'єкти Worker")

    def __repr__(self):
        return f"Boss({self.name}, компанія: {self.company})"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("boss повинен бути об'єктом Boss")
        self._boss = new_boss
        if self not in new_boss.workers:
            new_boss.add_worker(self)

    def __repr__(self):
        return f"Worker({self.name}, компанія: {self.company})"


bosses = []
workers = []

n_bosses = int(input("Скільки босів ви хочете створити? "))
for i in range(n_bosses):
    bid = int(input(f"ID боса #{i+1}: "))
    name = input(f"Ім'я боса #{i+1}: ")
    company = input(f"Компанія боса #{i+1}: ")
    bosses.append(Boss(bid, name, company))

n_workers = int(input("Скільки працівників ви хочете створити? "))
for i in range(n_workers):
    wid = int(input(f"ID працівника #{i+1}: "))
    name = input(f"Ім'я працівника #{i+1}: ")
    company = input(f"Компанія працівника #{i+1}: ")

    print("Оберіть боса для цього працівника:")
    for idx, boss in enumerate(bosses, 1):
        print(f"{idx}. {boss.name} ({boss.company})")

    boss_choice = int(input("Введіть номер боса: ")) - 1
    chosen_boss = bosses[boss_choice]

    workers.append(Worker(wid, name, company, chosen_boss))

print("\n--- Список босів і їх працівників ---")
for boss in bosses:
    print(f"{boss.name} ({boss.company}): {boss.workers}")