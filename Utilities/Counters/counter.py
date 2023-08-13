from threading import Lock


class Counter:

    def __init__(self) -> None:
        self._value = 0
        self._lock = Lock()

    def getter(self) -> int:
        with self._lock:
            return self._value

    def setter(self) -> None:
        with self._lock:
            self._value += 1

    def __repr__(self) -> str:
        return self._value
