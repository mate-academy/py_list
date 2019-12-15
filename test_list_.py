import list_


def test_create():
    l = list_.List()
    assert l.get_list() == "[]"


def test_insert():
    l = list_.List()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.get_list() == "[3,2,1]"


def test_delete():
    l = list_.List()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    assert l.delete() == 3
    assert l.get_list() == "[2,1]"
