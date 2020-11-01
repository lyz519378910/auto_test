# 判断   id 是否存在 列表中
def find_person(self, id_param, lst_param):
    for item in lst_param:
        if item.phone == id_param:
            return item
    else:
        return None

# 判断   登录  id 与 name 是否在列表中
def find_login(self, id_param, name_param, lst_param):
    for person in lst_param:
        if person.id == id_param and person.name == name_param:
            return person
    else:
        return None


# 登录、注册（增加）一条龙
def add_stu(self, lst):                                           # lst列表
    stu_id = input('please enter your stu id:')
    stu_person = self.find_person(stu_id, lst)                    # 判断id 是否存在 列表中
    if stu_person is None:
        print('请注册!')
        stu_name = input('please enter stu name:')
        stu = Student(stu_id, stu_name)
        lst.append(stu)
        print('注册成功!')
        print(stu_person.s_id, stu_person.s_name)
    else:
        stu_name = input('please enter stu name:')
        stu_person = self.find_login(stu_id, stu_name, lst)       # 判断登录  id 与 name 是否在列表中
        if stu_person is not None:
            print('登陆成功!')
            # 跳转
        else:
            print('密码错误!')


#删除
def delete(self, lst_param):
    id = input('请输入电话:')
    phone = self.find_person(id, lst_param)  # 判断id 是否存在 列表中
    if phone is None:
        print('请注册!')
        self.add_card(lst_param)
    else:
        lst_param.remove(phone)
        print('删除成功!')


#修改
def recharge(self, lst_param):
    id = input('请输入电话:')
    phone = self.find_person(id, lst_param)  # 判断id 是否存在 列表中
    if phone is None:
        print('请注册!')
        self.add_card(lst_param)
    else:
        phone.money = charge
        print('修改成功!')


#查找
def search(self, lst_param):
    id = input('请输入电话:')
    phone = self.find_person(id, lst_param)  # 判断id 是否存在 列表中
    if phone is None:
        print('请注册!')
        name = input('请输入姓名:')
        person = Card(name,id,0)
        lst_param.append(person)
        print('注册成功!')
        print(id,name)
    else:
        print(phone.name,phone.phone,phone.money)

#类属性（实例化的对象都可以调用类属性，s1可以调用，s2也可以调用）
class Manage:

    card_lst = [Card('lyz','185','0')]     ##类属性（实例化的对象都可以调用类属性，s1可以调用，s2也可以调用 且 公共显示所有内容）
    tec_club = {'id': []}                  #一对多，比如说：'阿根廷国家队':['梅西','迪马利亚','阿奎罗']


    def __init__(self):
        self.stu_club = []                 #方法属性，只能实例化对象调用，s1可以调用，s2也可以调用 但是 只显示自身内容