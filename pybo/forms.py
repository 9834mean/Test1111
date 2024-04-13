from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):			
    class Meta:
        model = Question
        fields = ['subject', 'content']
        widgets = {
            # <input type="text" name="subject" maxlength="200" required id="id_subject" class="form-control">
            'subject': forms.TextInput(attrs={'class': 'form-control'}), 
            # <textarea name="content" cols="40" rows="10" required id="id_content" class="form-control">
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목', 
            'content': '내용',
        }