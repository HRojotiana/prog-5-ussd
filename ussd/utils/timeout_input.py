import signal


class TimeoutException(Exception):
    pass


def _handle_timeout(signum, frame):
    raise TimeoutException


def demander_choix_avec_timeout(message: str, timeout: int = 5) -> str | None:
    signal.signal(signal.SIGALRM, _handle_timeout)
    signal.alarm(timeout)

    try:
        return input(message + " ")
    except TimeoutException:
        return None
    finally:
        signal.alarm(0)
