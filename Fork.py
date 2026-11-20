import threading


class Fork:
    def __init__(self, id: int):
        self.id = id
        self._is_clean = True
        self.lock = threading.Lock()

    @property
    def is_clean(self) -> bool:
        return self._is_clean

    @is_clean.setter
    def is_clean(self, state:bool):
        self._is_clean = state

    def clean(self):
        self.is_clean = True

    def __str__(self):
        return f"Fork NO.{self.id} ({self.is_clean})"