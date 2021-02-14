from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import CustomUserCreationForm
from .models import YouTube, Files, Pelcon
from django.contrib import messages
from django.db.models import Sum






def home(request):
	like = ['1', '0', '0']
	satisfied = ["Django", "Machine Learning", "Robotics", "None"]
	total_viewer = YouTube.objects.aggregate(Sum("v_watched"))
	print(total_viewer)
	total_viewer = total_viewer.get("v_watched__sum")
	print(total_viewer)


	context = {"like":like, "satisfied":satisfied, "total_viewer":total_viewer}
	return render(request, 'comment/mo.html', context)


def youtube(request):
	if request.method == "POST":
		full_names = request.POST['full_names']
		comment = request.POST['comment']
		v_watched = request.POST['v_watched']
		satisfied = request.POST['satisfied']
		viewer_like = request.POST['viewer_like']
		print("satisfied ? :", satisfied)
		print("Viewer Like : ", viewer_like)

		a = YouTube(full_names=full_names, comment=comment, v_watched=v_watched, satisfied=satisfied, viewer_like=viewer_like)
		a.save()
		messages.success(request, 'Feedback was Submitted successfully!')
		return redirect('home')
	else:
		messages.error(request, 'Failed To Submit Feedback, retry')
		return redirect('home')



def motech(request):
	names = ["Pelcon", "Crow", "Alpine", "Eagle" ]
	context = {"names":names}
	return render(request, 'comment/motech.html', context)



class FileView(generic.ListView):
    model = Files
    template_name = 'comment/file.html'
    context_object_name = 'files'
    paginate_by = 6

    def get_queryset(self):
    	return Files.objects.order_by('-id')



def uploadForm(request):
	return render(request, 'comment/upload.html')


def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'Files Submitted successfully!')
        return redirect('files')
    else:
    	messages.error(request, 'Files was not Submitted successfully!')
    	return redirect('form')



class PelconView(generic.ListView):
	model = Pelcon
	template_name = 'comment/pelcon.html'
	context_object_name = 'files'
	paginate_by = 4


	def get_queryset(self):
		return Pelcon.objects.order_by('-id')


def myUpload(request):
	return render(request, 'comment/myUpload.html')



def pelconUpload(request):
	if request.method == 'POST':
		name = request.POST['name']
		owner = request.POST['owner']
		pdf = request.FILES['pdf']
		cover = request.FILES['cover']

		a = Pelcon(name=name, owner=owner, pdf=pdf, cover=cover)
		a.save()
		messages.success(request, 'Files was Submitted successfully')
		return redirect('pelcon')
	else:
		messages.error(request, 'Files was not Submitted successfully')
		return redirect('myupload')


