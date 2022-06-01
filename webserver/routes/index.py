from typing import Text


def index_setup(app) -> None:
    @app.route('/')
    def index() -> Text:
        pass
