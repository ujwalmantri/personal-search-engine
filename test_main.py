from main import main

def test_main_runs_successfully(tmp_path, monkeypatch, capsys):
    (tmp_path / "sample.txt").write_text("Hello, World!")

    monkeypatch.setattr("builtins.input", lambda _: str(tmp_path))

    main()

    captured = capsys.readouterr()

    assert "Discovered and processed 1 documents" in captured.out
    assert "hello" in captured.out