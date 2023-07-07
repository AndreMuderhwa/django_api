from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Mobile_App.models import *
from Mobile_App.serializer import *
from . forms import *
# Create your views here.


@login_required
def index(request):
    partis=PartiPolitique.objects.all()
    form=PartiPolitiqueForm()
    if request.method=="POST":
        f=PartiPolitiqueForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
    context={"formulaire":form,
             "data":partis
             }
    return render(request,"index.html",context)


def login_view(request):
    if request.method=="POST":
        nomUser=request.POST.get("username")
        pwd=request.POST.get("password")
        user=authenticate(username=nomUser,password=pwd)
        if user is None:
            context={"erreur":"Mot de passe ou nom d'utilisateur incorrect."}
            return render(request,"login.html",context)
        login(request,user)
        return redirect("index")
    return render(request,"login.html",{})

@login_required
def logoutview(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login")
    return render(request,"logout.html",{})









@api_view(['GET'])
def getFondateur(request):
    q=Fondateur.objects.all()
    ser=FondateurSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateFondateur(request,pk):
    obj=Fondateur.objects.get(id_fondateur=pk)
    ser=FondateurSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Fondateur modifié")
    return Response(ser.errors)


@api_view(['GET'])
def deleteFondateur(request,pk):
    obj=get_object_or_404(Fondateur,id_fondateur=pk)
    obj.delete()
    return Response("Fondateur supprime")


@api_view(['POST'])
def createFondateur(request):
    ser=FondateurSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Fondateur ajouté")
    return Response(ser.errors)
    


@api_view(['GET'])
def getPartie(request):
    q=PartiPolitique.objects.all()
    ser=PartiPolitiqueSerializer(q,many=True)
    return Response(ser.data)



@api_view(['POST'])
def createPartiP(request):
    ser=PartiPolitiqueSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Parti politique ajouté")
    return Response(ser.errors)


@api_view(['GET'])
def viewPartiFondateur(request):
    obj=PartiPolitique.objects.filter(statut_membre=1)
    ser=ViewPartiFondateurSerializer(obj, many=True)
    return Response(ser.data)
######################USER
@api_view(['POST'])
def createUser(request):
    ser=UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Utilisateur ajouté")
    return Response(ser.errors)
#####################MEMBRE
@api_view(['POST'])
def createMembre(request):
    ser=MembreSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Membre ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getMembre(request):
    q=Membre.objects.all()
    ser=MembreSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateMembre(request,pk):
    obj=Membre.objects.get(id_membre=pk)
    ser=MembreSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Membre modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deleteMembre(request,pk):
    obj=get_object_or_404(Membre,id_membre=pk)
    obj.delete()
    return Response("Membre supprime")

###########################POST
@api_view(['POST'])
def createPost(request):
    ser=PostSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Post ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getPost(request):
    q=Post.objects.all()
    ser=PostSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updatePost(request,pk):
    obj=Post.objects.get(id_post=pk)
    ser=PostSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Post modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deletePost(request,pk):
    obj=get_object_or_404(Post,id_post=pk)
    obj.delete()
    return Response("Post supprime")
##################VIDEO

@api_view(['POST'])
def createVideo(request):
    ser=VideoSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Video ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getVideo(request):
    q=Video.objects.all()
    ser=VideoSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateVideo(request,pk):
    obj=Video.objects.get(id_video=pk)
    ser=VideoSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Video modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deleteVideo(request,pk):
    obj=get_object_or_404(Video,id_video=pk)
    obj.delete()
    return Response("Video supprime")

################STORY
@api_view(['POST'])
def createStory(request):
    ser=StorySerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Story ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getStory(request):
    q=Story.objects.all()
    ser=StorySerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateStory(request,pk):
    obj=Story.objects.get(id_story=pk)
    ser=StorySerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Story modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deleteStory(request,pk):
    obj=get_object_or_404(Story,id_story=pk)
    obj.delete()
    return Response("Story supprime")

#################IMAGES
@api_view(['POST'])
def createImages(request):
    ser=ImageSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Images ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getImages(request):
    q=Images.objects.all()
    ser=ImageSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateImages(request,pk):
    obj=Images.objects.get(id_image=pk)
    ser=ImageSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Images modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deleteImages(request,pk):
    obj=get_object_or_404(Images,id_image=pk)
    obj.delete()
    return Response("Images supprime")
#######################COMMENTAIRE
@api_view(['POST'])
def createCommentaire(request):
    ser=ImageSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Images ajouté")
    return Response(ser.errors)

@api_view(['GET'])
def getCommentaire(request):
    q=Images.objects.all()
    ser=ImageSerializer(q,many=True)
    return Response(ser.data)

@api_view(['PUT'])
def updateCommentaire(request,pk):
    obj=Commentaire.objects.get(id_commentaire=pk)
    ser=CommentaireSerializer(instance=obj, data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Commentaire modifié")
    return Response(ser.errors)

@api_view(['GET'])
def deleteCommentaire(request,pk):
    obj=get_object_or_404(Commentaire,id_commentaire=pk)
    obj.delete()
    return Response("Commentaire supprime")
