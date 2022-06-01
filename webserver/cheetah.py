from flask import Flask
from dotenv import load_dotenv
from routes import *
import os


class CheetahWebServer(Flask):

    def __init__(self) -> None:
        super().__init__(__name__)


def main() -> None:
    load_dotenv()
    CheetahWebServer().run(port=os.getenv('CHEETAH_PORT'))


if __name__ == '__main__':
    main()
