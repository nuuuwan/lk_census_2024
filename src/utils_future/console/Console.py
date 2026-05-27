from utils_base.console.constants import (COLOR_BACKGROUND, COLOR_FOREGROUND,
                                          COLOR_FORMAT)


class Console:
    @staticmethod
    def format(*args, **kwargs) -> str:
        foreground = kwargs.get("foreground", "")
        background = kwargs.get("background", "")
        format = kwargs.get("format", "")
        text = " ".join(args)
        return "".join(
            [foreground, background, format, text, COLOR_FORMAT.RESET]
        )

    @staticmethod
    def print(*args, **kwargs):
        print(Console.format(*args, **kwargs))

    @staticmethod
    def h1(*args) -> str:
        return Console.format(
            *args,
            foreground=COLOR_FOREGROUND.WHITE,
            background=COLOR_BACKGROUND.GREEN,
            format=COLOR_FORMAT.UNDERLINE,
        )

    @staticmethod
    def h2(*args) -> str:
        return Console.format(
            *args,
            foreground=COLOR_FOREGROUND.GREEN,
        )

    @staticmethod
    def normal(*args) -> str:
        return Console.format(*args, foreground=COLOR_FOREGROUND.WHITE)

    @staticmethod
    def note(*args) -> str:
        return Console.format(
            *args,
            foreground=COLOR_FOREGROUND.YELLOW,
            format=COLOR_FORMAT.ITALIC,
        )

    @staticmethod
    def md5_line(line) -> str:  # noqa: CFQ004
        if not line:
            return ""
        if line.startswith("# "):
            return Console.h1(line[2:])
        if line.startswith("## "):
            return Console.h2(line[3:])
        if line.startswith("*") and line.endswith("*"):
            return Console.note(line[1:-1])
        return Console.normal(line)

    @staticmethod
    def md5(*args) -> str:
        return "\n".join(Console.md5_line(arg) for arg in args)

    @staticmethod
    def print_lines(*args):
        for arg in args:
            print(arg)
