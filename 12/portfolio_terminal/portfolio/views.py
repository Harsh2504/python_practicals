from django.shortcuts import render
from .forms import ContactForm

def portfolio_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form submission (e.g., send email or store in database)
            success_message = "I will reach you out soon!"
            form = ContactForm()  # Reset form after submission
            return render(request, 'portfolio/portfolio.html', {
                'form': form,
                'success_message': success_message,
            })
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/portfolio.html', {'form': form})
