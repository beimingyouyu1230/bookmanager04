from django.urls import path

from book.views import index,book,login,weibo


urlpatterns = [
    path('index/',index),
    # path('1/100/',index)
    path('<cat_id>/<book_id>/',book),
    path('login',login),
    path('weibo',weibo)

]