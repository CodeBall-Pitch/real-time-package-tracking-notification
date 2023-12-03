from django.shortcuts import render,redirect
from .models import Package, Notification

def Homeview(request):
    packages = Package.objects.all()
    notifications = Notification.objects.filter(user=request.user, read=True)
    
    context = {
        'packages': packages,
        'notifications': notifications,
    }
    return render(request, 'home.html', context)

def PackageDetailView(request, tracking_number):
    package = Package.objects.get(tracking_number=tracking_number)
    context = {
        'package': package,
    }
    return render(request, 'detail.html', context)

def MarkNotificationAsUnread(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = False
    notification.save()
    return redirect('home')