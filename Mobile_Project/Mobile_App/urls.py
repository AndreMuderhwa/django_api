from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("allFondateur",views.getFondateur),
    path("create_fondateur",views.createFondateur),
    path("update_fondateur/<str:pk>",views.updateFondateur),
    path("delete_fondateur/<str:pk>",views.deleteFondateur),
    path("allParti",views.getPartie),
    path("create_parti",views.createPartiP),
    path("view_parti_fondateur",views.viewPartiFondateur),


    path("create_user",views.createUser,name="create_user"),


    path("login",views.login_view, name="login"),
    path("logout",views.logoutview, name="logout")


]