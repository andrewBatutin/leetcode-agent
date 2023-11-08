from src.ai_assistant.sandbox import run_loop


def test_simple_assistant():
    res = run_loop()
    assert res is not None
