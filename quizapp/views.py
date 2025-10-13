from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Question, Session, Result
from .forms import PlayerForm, QuestionForm
from django.contrib import messages

def index(request):
    players = Player.objects.order_by('-created_at')[:5]
    sessions = Session.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {'players': players, 'sessions': sessions})

# Players CRUD
def players_list(request):
    players = Player.objects.order_by('-created_at')
    return render(request, 'players_list.html', {'players': players})

def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Игрок создан')
            return redirect('players_list')
    else:
        form = PlayerForm()
    return render(request, 'player_form.html', {'form': form})

def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Игрок обновлён')
            return redirect('players_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'player_form.html', {'form': form, 'player': player})

def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        messages.success(request, 'Игрок удалён')
        return redirect('players_list')
    return render(request, 'player_confirm_delete.html', {'player': player})

# Questions CRUD
def questions_list(request):
    questions = Question.objects.order_by('-created_at')
    return render(request, 'questions_list.html', {'questions': questions})

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вопрос добавлен')
            return redirect('questions_list')
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})

def question_edit(request, pk):
    q = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=q)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вопрос обновлён')
            return redirect('questions_list')
    else:
        form = QuestionForm(instance=q)
    return render(request, 'question_form.html', {'form': form, 'question': q})

def question_delete(request, pk):
    q = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        q.delete()
        messages.success(request, 'Вопрос удалён')
        return redirect('questions_list')
    return render(request, 'question_confirm_delete.html', {'question': q})

# Sessions
def sessions_list(request):
    sessions = Session.objects.order_by('-created_at')
    return render(request, 'sessions_list.html', {'sessions': sessions})

def session_create(request):
    players = Player.objects.order_by('name')
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        if not player_id:
            messages.error(request, 'Выберите игрока')
        else:
            s = Session.objects.create(player_id=player_id)
            messages.success(request, 'Сессия создана')
            return redirect('play_session', pk=s.id)
    return render(request, 'session_form.html', {'players': players})

def session_view(request, pk):
    s = get_object_or_404(Session, pk=pk)
    return render(request, 'session_view.html', {'session': s})

def play_session(request, pk):
    s = get_object_or_404(Session, pk=pk)
    questions = list(Question.objects.all())
    if request.method == 'POST':
        qid = int(request.POST['question_id'])
        given = request.POST.get('given_answer', '').strip()
        q = get_object_or_404(Question, pk=qid)
        correct = (given.lower() == q.answer.lower())
        Result.objects.create(session=s, question=q, given_answer=given, correct=correct)
        if correct:
            s.score += 1
            s.save()
        messages.info(request, 'Ответ сохранён — ' + ('правильно' if correct else 'неправильно'))
        return redirect('play_session', pk=s.id)
    results = s.results.all()
    answered_qids = {r.question_id for r in results}
    remaining = [q for q in questions if q.id not in answered_qids]
    return render(request, 'play_session.html', {'session': s, 'remaining': remaining, 'results': results})

def results_list(request):
    sessions = Session.objects.order_by('-created_at')
    return render(request, 'results_list.html', {'sessions': sessions})
