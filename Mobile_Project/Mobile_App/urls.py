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



    ##################MEMBRE
     path("allMembre",views.getMembre),
    path("create_membre",views.createMembre),
    path("update_membre/<str:pk>",views.updateMembre),
    path("delete_membre/<str:pk>",views.deleteMembre),
    ####################POST
     path("allPost",views.getPost),
    path("create_post",views.createPost),
    path("update_post/<str:pk>",views.updatePost),
    path("delete_post/<str:pk>",views.deletePost),

    ###########################STORY
     path("allStory",views.getStory),
    path("create_story",views.createStory),
    path("update_story/<str:pk>",views.updateStory),
    path("delete_story/<str:pk>",views.deleteStory),
    ##############VIDEO
    path("allVideo",views.getVideo),
    path("create_video",views.createVideo),
    path("update_video/<str:pk>",views.updateVideo),
    path("delete_video/<str:pk>",views.deleteVideo),

    #############IMAGES
      path("allImage",views.getImages),
    path("create_image",views.createImages),
    path("update_image/<str:pk>",views.updateImages),
    path("delete_image/<str:pk>",views.deleteImages),
    ######COMMENTAIRE
    path("allCommentaire",views.getCommentaire),
    path("create_commentaire",views.createCommentaire),
    path("update_commentaire/<str:pk>",views.updateCommentaire),
    path("delete_commentaire/<str:pk>",views.deleteCommentaire),


    path("create_user",views.createUser,name="create_user"),


    path("login",views.login_view, name="login"),
    path("logout",views.logoutview, name="logout")


]