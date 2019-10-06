from users.users import Users

def test_build_salt():
    a_user = Users("bill", "bill@bill.com", "abcdefg")
    assert a_user.build_salt() == "dJlmr8mgKMr9o7Ond5rohljvHNQpEZ"