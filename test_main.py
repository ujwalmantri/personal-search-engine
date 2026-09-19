from main import main

def test_main_runs_successfully(tmp_path, monkeypatch, capsys):
    (tmp_path / "sample.txt").write_text("Hello, World!")
    inputs = iter([str(tmp_path), "hello"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()

    captured = capsys.readouterr()

    assert "Discovered and processed 1 documents" in captured.out
    assert "Found 1 matching document" in captured.out