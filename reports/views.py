from django.shortcuts import render, redirect, get_object_or_404
from .models import Report
from postagens.models import Postagens
from .forms import ReportForm

def reportar_postagem(request, postagem_id):
    error_message = None
    post = get_object_or_404(Postagens, id=postagem_id)
    if not request.user.is_authenticated:
        error_message = 'Você precisa estar logado para acessar esta página.'
        return redirect('login')
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        motivo = request.POST.get('motivo')
        if form.is_valid():
            if motivo:
                report = Report.objects.create(
                    motivo=motivo,
                    postagem=post,
                )
                report.save()
                return redirect('home')
            else:
                error_message = 'Motivo não pode ser vazio.'
                return render(request, 'reports/report.html', {'error_message': error_message, 'post': post, 'form': form})
    else:
        form = ReportForm()
    
    return render(request, 'reports/report.html', {'error_message': error_message, 'post':post})