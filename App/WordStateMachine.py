import time

class WordStateMachine:
    def __init__(self, cooldown_time=1.5):
        self.current_word = ""
        self.last_char = ""
        self.last_update_time = time.time()
        self.cooldown_time = cooldown_time

    def process(self, char):
        if not char or char == "---":
            return

        current_time = time.time()

        if char.lower() == 'space':
            if current_time - self.last_update_time > self.cooldown_time:
                self.current_word += " "
                self.last_update_time = current_time
                self.last_char = char
            return

        if char.lower() == 'nothing':
            self.last_char = char
            return

        if char != self.last_char or (current_time - self.last_update_time > self.cooldown_time):
            self.current_word += char
            self.last_char = char
            self.last_update_time = current_time

    def get_current_word(self):
        return self.current_word

    def reset(self):
        self.current_word = ""
        self.last_char = ""