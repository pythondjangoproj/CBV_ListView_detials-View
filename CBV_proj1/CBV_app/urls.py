# from django.contrib import admin
from django.urls import path
from . import views
app_name= 'CBV_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',views.Hello_view.as_view()),
    # path('second/',views.Hello_template_view.as_view()),
    path('',views.Booklist_view.as_view()),
    path('<pk>/',views.BookDetails_view.as_view()),
]
