from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ex_upload/index.html')

from .forms import UploadFileForm
from django.shortcuts import reverse, redirect

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES) # 모델 폼이니까 바로 모델에 저장시킬 수 있음
        if form.is_valid():
            form.save()
            return redirect(reverse('ex_upload:index'))
    else:
        form = UploadFileForm()
        
    return render(request, 'ex_upload/upload_form.html', {'form':form})