from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

class Session(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Session {self.id} - {self.player.name}"

class Result(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='results')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=200, blank=True)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Result {self.id} - {self.session}"
