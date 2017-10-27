import pytest
import mikobase


def test_ssh():
    connection = mikobase.ssh("localhost", 12345, "root", "root")
    assert 'root' in connection.sendCommand("pwd")
    connection.sendCommand("echo 'test' > test.txt")
    assert 'test.txt' in connection.sendCommand("ls")
    assert 'test' in connection.sendCommand("cat test.txt")

