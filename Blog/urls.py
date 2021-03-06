"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.feeds import AllPostsRssFeed
"""
我们这里导入了一个 include 函数，然后利用这个函数把 blog 应用下的 urls.py 文件包含了进来。
此外 include 前还有一个 ''，这是一个空字符串。这里也可以写其它字符串，django 会把这个字符串
和后面 include 的 urls.py 文件中的 URL 拼接。比如说如果我们这里把 '' 改成 'app/'，
而我们在 app/urls.py 中写的 URL 是 ''，即一个空字符串。
那么 django 最终匹配的就是 app/ 加上一个空字符串，即 app/。
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('comments.urls')),
    path('all/rss/', AllPostsRssFeed(), name='rss'),
]
