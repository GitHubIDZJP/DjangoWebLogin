from django.shortcuts import render
#
from  django.http import  HttpResponse
from  . import  models # .表示从当前的路径获取(倒库)
#
# def login(request):
#     return HttpResponse('<h1>大哈巴<h1>')
def register(request):
    return render(request, 'jiaP/index.html')
    # return HttpResponse(request,'')
    # return render(request, 'jiaP/register.html')
def hello(request):
    # return HttpResponse('sdsd') #加载文字
    #判断请求方法---post
    if  request.method == 'POST':
        # 接收表单数据可以直接request.POST.get
        # 返回用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')

        '''
        HttpResponse('恭喜登录成功')类似print()
        '''
        # 判断
        #长度不能少于8个字符且密码不能为空,传8个空格也不行
        # if username and len(password)>=3:
        #     return HttpResponse('恭喜登录成功')
        # else:
        #     return HttpResponse('密码不能为空，长度需要大于等于3个字符')
        password=password.strip()#清除空格
        if password and len(password)>=8:
            #验证用户密码是否正确，根据用户名搜索系统中的用户
            #把User对象拿过来，先倒库
            #object 不会自动提示，要自己写，
            #filter 如果没有获取到，也不会抛出异常
            '''
            username=username
            前面这个变量username等于models.py下的username = models.CharField(max_length=128,unique=True)的这个username,
            后面这个username则是username = request.POST.get('username')的username
            '''
            #返回搜获结果，如果搜索到则为空，没搜索到则不为空
            res = models.User.objects.filter(username=username)
            #通过下标获-记录-对应用户对象，判断密码是否和我传进啦的一模一样，如果密码正确，进入index.html
            #判断用户存在且密码正常
            '''
            res and res[0].passwors 是否存在
            password 是否正确
            '''
            if res and res[0].password == password:
                return render(request, 'jiaP/index.html', {'username': username})
            else:
        # 密码不正确
                return HttpResponse('密码不正确!!!')



            # return HttpResponse('恭喜登录成功')
        else:


            return HttpResponse('密码不能为空，长度需要大于等于8个字符')
        # if username and password:
        #     return HttpResponse('恭喜登录成功')




    return render(request,'jiaP/JSD.html') #加载HTML

'''
要把用户名存到数据库


1.回到http://127.0.0.1:8000/hello/测试
   账号: sougouid
   密码：qazwsxed
'''


