from django.shortcuts import render, redirect
from schedule.models import Schedule


def create(request):
    teacher = request.POST.get('teacher')
    subject = request.POST.get('subject')
    class_date = request.POST.get('class_date')
    class_time = request.POST.get('class_time')
    student = request.POST.get('student')

    try:
        print("ANTES")  
        new = Schedule.objects.create(teacher=teacher, subject=subject, class_date=class_date, class_time=class_time, student=student)
        print("DEPOIS", new.name)  
        
        if new is not None:
            print("Agendamento realizado com sucesso.")
        else:
            print("Confira os dados e tente novamente.")
    except:
        print("Erro ao realizar agendamento.")
    
    schedules = Schedule.objects.all()
    return render(request, 'read.html', {'schedules': schedules})

def read(request):
    schedules = Schedule.objects.all()
    return render(request, 'read.html', {'schedules': schedules})

def detail(request, id):
    schedule = Schedule.objects.get(id=id)
    return render(request, 'update.html', {'schedule': schedule}) 
def update(request, id):
    try:
        schedule = Schedule.objects.get(id=id)
    except:
        print("Agendamento não localizado.")

    schedule.teacher = request.POST.get('teacher')
    schedule.subject = request.POST.get('subject')
    schedule.class_date = request.POST.get('class_date')
    schedule.class_time = request.POST.get('class_time')
    schedule.student = request.POST.get('student')

    schedule.save()
    return redirect(read)

def delete(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    return redirect(read)