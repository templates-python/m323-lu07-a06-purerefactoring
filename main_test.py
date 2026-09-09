"""Pytest-Fälle des Templates."""

import main


def test(capsys):
    """The total is printed for the corrected quantity."""
    main.calculate()
    captured = capsys.readouterr()
    assert captured.out == 'Total: 73.75\n'
