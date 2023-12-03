from django.shortcuts import render
from .models import Package, Notification

def Homeview(request):
    packages = Package.objects.all()
    notifications = Notification.objects.filter(user=request.user, read=False)
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
    return render(request, 'package_detail.html', context)

def MarkNotificationAsRead(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()
    return redirect('home')