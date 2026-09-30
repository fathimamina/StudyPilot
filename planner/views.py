from django.shortcuts import render

from .models import Module, Topic, Task
from .parser import parse_module


def module_input(request):

    if request.method == 'POST':

        module_name = request.POST.get('module_name')
        raw_text = request.POST.get('raw_text')

        parsed_data = parse_module(raw_text)
        print(parsed_data)

        module = Module.objects.create(
            name=module_name,
            raw_text=raw_text
        )

        for topic_data in parsed_data:

            topic = Topic.objects.create(
                module=module,
                title=topic_data["title"]
            )

            for task_title in topic_data["tasks"]:

                Task.objects.create(
                    topic=topic,
                    title=task_title,
                    task_type="theory"
                )

    modules = Module.objects.all()

    return render(
        request,
        'planner/module_input.html',
        {'modules': modules}
    )