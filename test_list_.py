import list_


def test_create():
    l = list_.List()
    assert l.state() == "[]"


def test_insert():
    l = list_.List()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.state() == "[3,2,1]"


def test_delete():
    l = list_.List()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.delete() == 3
    assert l.state() == "[2,1]"