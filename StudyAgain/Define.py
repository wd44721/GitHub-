"""
def 函数名(形参):
    表达式...
    :return 默认None
"""
# 函数类型
# 普通参数 | 默认参数 | 关键字参数 | 收集参数 | 组合参数
"""
（普通参数）
def 函数名(形参1，形参2):
    表达式...
    
调用：函数名(实参1，实参2)  》如果少了任何一个，程序就会报错
"""
"""
（默认参数） 默认参数就是定义函数时，形参给定一个值。
def 函数名(形参1，形参2=xxx):
    表达式...
    
调用：     函数名(实参1)    》默认是把xxx当做了实参2
        | 函数名(实参1，实参2) 
        | 函数名(实参1，形参2=实参2)
        | 函数名(形参1=实参1，形参2=实参2) 两个顺序可随意调整
"""
"""
(关键字参数) 在调用函数时，传入实参时带参数名，用这样的方式传入的实参叫做关键字参数
用法1：和默认参数里的形参2的用法是一样的
def 函数名(形参1，形参2=xxx，形参3=xxx):
    表达式...
用法2：提前新建一个变量元组或者列表
def 函数名(形参1，*args):
    表达式...
用法3：提前新建一个变量字典
def 函数名(形参1，**args):
    表达式...

"""
def func(p1,p2,p3=0,p4=0):
    print(p1,p2,p3,p4)
func(1,2,3,4)
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person("wang",1,2,1,city="长沙",job="python")
def person(name, age, *, city, job, **args):
    print(name, age,  city, job, args)

person("wang",1,city="长沙",job="python",love="rong")
"""
（收集参数） *args—args是一个空元组，**kwargs—kwargs是一个字典
def 函数名(*args):
    表达式

调用：函数名(p1,p2,p3,p4)

def 函数名(**kwargs):
    表达式
"""
def func(*args):
    # print(args)
    pass
f1 = [1,2,3,4]
func(1,2,3,4)
func(*f1)   # 解包

def func(**kwargs):
    # print(kwargs)
    pass
f2 = {"p1":1,"p2":2}
func(p1=1,p2=2)
func(**f2)  # 解包

"""
（组合参数）顺序 —> 必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def func(name,age,*args,city,job,**kwargs):     ->city和job是命名关键字参数
    print(name,age,args,city,job,kwargs)
def func(name,age,*args,city=None,job=None,**kwargs):     ->也可以给city和job制定默认值
    print(name,age,args,city,job,kwargs)
        
"""
def func(name,age,*args,city=None,job=None,**kwargs):
    print(name,age,args,city,job,kwargs)
func("wang",27)
func("wang",27,"hobit","love",city="长沙",job="python",love="rong")