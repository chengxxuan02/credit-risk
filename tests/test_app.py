from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def test_app_starts():
    app = AppTest.from_file(APP_PATH, default_timeout=30).run()

    assert not app.exception
    assert app.title[0].value == "Credit Risk Prediction App"


def test_default_prediction():
    app = AppTest.from_file(APP_PATH, default_timeout=30).run()
    assert not app.exception

    app.button[0].click().run()

    assert not app.exception
    assert len(app.success) == 1
    assert "**GOOD**" in app.success[0].value
