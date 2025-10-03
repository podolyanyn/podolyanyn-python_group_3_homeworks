class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_index = 0  #

    def first_channel(self):
        self.current_index = 0
        return self.channels[self.current_index]

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.channels[self.current_index]

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
            return self.channels[self.current_index]
        else:
            return "Канал не існує"

    def next_channel(self):
        if self.current_index + 1 >= len(self.channels):
            self.current_index = 0  # якщо останній — на перший
        else:
            self.current_index += 1
        return self.channels[self.current_index]

    def previous_channel(self):
        if self.current_index == 0:
            self.current_index = len(self.channels) - 1  # якщо перший — на останній
        else:
            self.current_index -= 1
        return self.channels[self.current_index]

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, query):
        if isinstance(query, int):
            if 1 <= query <= len(self.channels):
                return "Так"
        elif isinstance(query, str):
            if query in self.channels:
                return "Так"
        return "Ні"

КАНАЛИ = ["BBC", "Discovery", "TV1000"]
controller = TVController(КАНАЛИ)

print(controller.first_channel())      # ➜ BBC
print(controller.last_channel())       # ➜ TV1000
print(controller.turn_channel(2))      # ➜ Discovery
print(controller.next_channel())       # ➜ TV1000
print(controller.next_channel())       # ➜ BBC
print(controller.previous_channel())   # ➜ TV1000
print(controller.current_channel())    # ➜ TV1000
print(controller.exists(4))            # ➜ Ні
print(controller.exists("BBC"))        # ➜ Так
print(controller.exists("CNN"))        # ➜ Ні