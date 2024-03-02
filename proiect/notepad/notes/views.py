from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserLoginForm, NoteForm, NoteEditForm
from users.forms import RegisterForm
from .models import Notes
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer
from .models import Notes
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect

def home_view(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def notes(request):
    notes = Notes.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes.html', {'notes': notes})

# ...

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes_page', pk=note.id)
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})

def notes_page(request, pk):
    note = Notes.objects.get(id=pk)
    return render(request,'notes_page.html', {'note': note})




@login_required
def edit_note(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')
    else:
        form = NoteEditForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})

@login_required
def delete_note(request, pk):
        note = Notes.objects.get(id=pk)
        if request.method == 'POST':
            note.delete()
            return redirect('notes')
        return render(request, 'delete_note.html', {'note': note})

# API Views

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_notes(request):
            notes = Notes.objects.filter(user=request.user).order_by('-created_at')
            serializer = NoteSerializer(notes, many=True)
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_note(request):
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_edit_note(request, pk):
    try:
        note = Notes.objects.get(id=pk, user=request.user)
    except Notes.DoesNotExist:
        return Response({'error': 'Note not found.'}, status=404)

    serializer = NoteSerializer(instance=note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_note(request, pk):
            try:
                note = Notes.objects.get(id=pk, user=request.user)
            except Notes.DoesNotExist:
                return Response({'error': 'Note not found.'}, status=404)

            note.delete()
            return Response(status=204)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_notes_details(request, pk):
                try:
                    note = Notes.objects.get(id=pk, user=request.user)
                except Notes.DoesNotExist:
                    return Response({'error': 'Note not found.'}, status=404)

                serializer = NoteSerializer(note)
                return Response(serializer.data)


@csrf_protect
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
    

