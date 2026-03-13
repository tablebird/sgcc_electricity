
from db import MysqlDB

def test_mysql() -> None:
    db = MysqlDB()
    assert db.connect_user_db("test_user") is True
    assert db.insert_data({"date": "2023-10-02", "usage": 123.45}) is True
    assert db.insert_expand_data({"name": "test_key", "value": "test_value"}) is True
    # Clean up environment variables

    