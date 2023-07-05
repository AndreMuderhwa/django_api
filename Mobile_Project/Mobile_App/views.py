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
@permission_classes([IsAuthenticated])
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

@api_view(['POST'])
def createUser(request):
    ser=UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response("Utilisateur ajouté")
    return Response(ser.errors)