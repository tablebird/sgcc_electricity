from notify import UrlPushNotify

def test_push_notify() -> None:
    url_notify = UrlPushNotify()
    assert url_notify is not None
    assert url_notify("test_user", 5.0) is True