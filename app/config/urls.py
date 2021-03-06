"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from todo import views as views_todo
from service_tastemeasure import views as views_tastemeasure


router = routers.DefaultRouter()
router.register(r'todos', views_todo.TodoView, 'todo')
router.register(r'balances', views_tastemeasure.BalanceGameView, 'balance')
router.register(r'nicknames', views_tastemeasure.NicknamesView, 'nickname')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

""" Take this comment out to enable DebugToolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
"""
