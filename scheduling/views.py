from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Slot, Schedule
from .forms import ScheduleForm

def list_slots(request):
    slots = Slot.objects.all()
    return render(request, 'scheduling/slot_list.html', {'slots': slots})

@login_required
def sign_up_for_slot(request, slot_id):
    slot = Slot.objects.get(id=slot_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.nurse = request.user
            schedule.slot = slot
            schedule.save()
            messages.success(request, 'You have successfully signed up for this slot.')
            return redirect('slots_list')
    else:
        form = ScheduleForm()
    return render(request, 'scheduling/sign_up.html', {'form': form, 'slot': slot})
