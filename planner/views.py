from django.shortcuts import render
from .models import Module

# Create your views here.
def module_input(request):

    if request.method == 'POST':
        module_name = request.POST.get('module_name')
        raw_text = request.POST.get('raw_text')

        Module.objects.create(
            name=module_name,
            raw_text=raw_text
        )
    modules = Module.objects.all()
    return render(request, 'planner/module_input.html', {'modules':modules})