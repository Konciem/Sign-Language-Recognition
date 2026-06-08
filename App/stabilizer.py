from collections import deque
from collections import Counter


class GestureStabilizer:
    def __init__(self, window_size=15):
        self.history = deque(maxlen=window_size)

    def get_stable_prediction(self, current_prediction):
        self.history.append(current_prediction)

        most_common = Counter(self.history).most_common(1)
        return most_common[0][0]