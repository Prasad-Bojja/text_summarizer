from django.shortcuts import render
from transformers import pipeline

summarize = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(request):
    output_text = ""  # Initialize output_text outside of the if statement
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        output_text = summarize(input_text, max_length=130, min_length=30, do_sample=False)
    return render(request, 'summarize_text.html', {'output_text': output_text})
