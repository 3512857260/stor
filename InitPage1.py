

class InitPage:

    login_success_date = [
        {"username": "jason", "pwd": "1234567", "expect": "Student Login"},
        {"username": "admin", "pwd": "root", "expect": "Student Login12345"},
        {"username": "acer", "pwd": "123456", "expect": "Student Login"}
    ]


    login_error_data = [
        #  id:msg_uname
        {"username": "jason1", "pwd": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "admin", "pwd": "root1", "expect": "账户名错误或密码错误!别瞎弄!"},
        {"username": "acer", "pwd": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"}
    ]


























# class Init:
#
#     login_success_dats = [
#         {"username": "acer", "pwd": "123456", "expect": "Student Login"}
#     ]
#
#
#     login_error_datt = [
#         #  id:msg_uname
#         {"username": "acer", "pwd": "123456789", "expect": "账户名错误或密码错误!别瞎弄!"}
#     ]








