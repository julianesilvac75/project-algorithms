from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "testmessage"

    assert encrypt_message(message, -1) == "egassemtset"
    assert encrypt_message(message, 3) == "set_egassemt"
    assert encrypt_message(message, 4) == "egassem_tset"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, "key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1234, 10)
