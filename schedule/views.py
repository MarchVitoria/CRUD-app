from django.shortcuts import render, redirect
from schedule.models import Schedule
from django.contrib import messages

  

def create(request):
    teacher = request.POST.get('teacher')
    subject = request.POST.get('subject')
    class_date = request.POST.get('class_date')
    class_time = request.POST.get('class_time')
    student = request.POST.get('student')
    
    if not all([teacher, subject, class_date, class_time, student]):
        messages.error(request, 'Por favor, preencha todos os campos.')

    elif Schedule.objects.filter(teacher=teacher, class_date=class_date, class_time=class_time).exists():
        messages.error(request, f'Já existe um agendamento para esta data e horário com o/a professor/a {teacher}.')

    elif Schedule.objects.filter(student=student, class_date=class_date, class_time=class_time).exists():
        messages.error(request, f'Já existe um agendamento para esta data e horário para o/a aluno/a {student}.')
    
    else:
        try:
            new_schedule = Schedule.objects.create(
                teacher=teacher,
                subject=subject,
                class_date=class_date,
                class_time=class_time,
                student=student
            )
            messages.success(request, 'Agendamento realizado com sucesso.')

        except Exception as e:
            messages.error(request, f'Erro ao realizar agendamento: {e}')

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