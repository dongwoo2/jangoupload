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

from .models import UploadFile

def file_list(request):
    list = UploadFile.objects.all().order_by('-pk')
    return render(
                request,
                'ex_upload/file_list.html',
                {'list':list}
    )
    
import os
from django.conf import settings
    
def delete_file(request, id):
    file = UploadFile.objects.get(pk=id)
    
    #실제 업로드된 파일도 삭제
    media_root = settings.MEDIA_ROOT
    remove_file = media_root + "/" + str(file.file)
    
    if os.path.isfile(remove_file): # 리무브파일이 실제 파일이라면 삭제하겠다. 존재하지 않는다면 삭제하지 않고 넘어감
        os.remove(remove_file) # 실제 파일 삭제
    
    file.delete() # DB에서 삭제
    
    return redirect(reverse('ex_upload:list'))