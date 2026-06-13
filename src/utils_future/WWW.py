import requests

from utils_future.console.Log import Log

log = Log("WWW")


class WWW:

    def __init__(
        self,
        url: str,
    ):
        self.url = url

    def __str__(self) -> str:
        return f"🌐{self.url}"

    def get_response(self):
        response = requests.get(
            self.url,
            timeout=30,
        )
        response.raise_for_status()
        return response

    def download_binary(self, file_path) -> str:
        response = self.get_response()
        with open(file_path, "wb") as fd:
            fd.write(response.content)
        return file_path
