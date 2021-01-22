from django.shortcuts import render
from django.http import HttpResponse
from .models import Camera_manage, Equipment_manage, Booking
from .forms import BookingForm
import datetime
from django.contrib.auth.decorators import login_required

@login_required

# Create your views here.
def index(request):
    camera_data = Camera_manage.objects.all()
    equipment_data = Equipment_manage.objects.all()

    params = {
        'camera': camera_data,
        'equipment': equipment_data,
    }

    return render(request, 'yoyaku_system/index.html', params)



def yoyaku(request):
    camera_data = Camera_manage.objects.all()
    equipment_data = Equipment_manage.objects.all()
    start_day = datetime.datetime.now()
    
    params = {
            'camera_data': camera_data,
            'equipment_data': equipment_data,
            'camera': '',
            'equipment': '',
            'camera_quantity': '',
            'form': BookingForm(),
            'start_day': start_day,
        }

    return render(request, 'yoyaku_system/yoyaku.html', params)

def confirm(request):

    camera_data = Camera_manage.objects.all()
    equipment_data = Equipment_manage.objects.all()


    camera_post = request.POST['camera_name']
    equipment_post = request.POST['equipment_name']

    start_day = request.POST.get("rental_start", None)
    start_day = datetime.datetime.strptime(start_day, '%Y-%m-%dT%H:%M') #文字列型をdateオブジェクトに変換
    end_day = start_day + datetime.timedelta(days=30)
    
    camera = Camera_manage.objects.get(camera_number=camera_post)
    equipment = Equipment_manage.objects.get(equipment_number=equipment_post)

    """
    conf(request, camera, equipment)
    if (camera.camera_quantity < 0 or equipment.equipment_quantity < 0):
    return render(request, 'yoyaku_system/not_booking.html')
    """

    params = {
        'camera_data': camera_data,
        'equipment_data': equipment_data,
        'camera': camera,
        'equipment': equipment,
        'camera_quantity': camera.camera_quantity,
        'form': BookingForm(request.POST),
        'start_day': start_day.strftime('%Y/%m/%d'),
        'end_day':end_day.strftime('%Y/%m/%d'),
    }

    booking_info(start_day,end_day)

    return render(request, 'yoyaku_system/confirm.html', params)


def conf(camera, equipment):
        #残り個数
    c_residue = camera.camera_quantity - 1
    e_residue = equipment.equipment_quantity - 1

    camera.camera_quantity = c_residue
    equipment.equipment_quantity = e_residue
    
    camera.save()
    equipment.save()

def booking_info(start_day, end_day):
    #ユーザー情報からメールアドレスを引っ張ってきてデータベースに保存したい
    booking = Booking(lending_day=start_day,return_day=end_day,returned=False)
    booking.save()