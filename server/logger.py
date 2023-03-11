import time
import datetime


def time_formatted(format="%Y-%m-%d %H:%M:%S") -> str:
    return time.strftime(format, time.localtime())


def info(msg: str) -> None:
    print(f"[{time_formatted()}][INFO] msg")
