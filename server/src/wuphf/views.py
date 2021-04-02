from django.shortcuts import render, redirect
from django.views import View
from wuphf.models import WuphfReceiver, Wuphf
from django.http import JsonResponse


class HomePage(View):
    """Home Page - Send a WUPHF"""
    template_name = 'home.html'

    def get_context(self):
        return {
            'recipients': WuphfReceiver.objects.all()
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context())

    def post(self, request, *args, **kwargs):
        """Receive the send_wuphf request"""
        receiver = WuphfReceiver.objects.get(id=request.POST['receiver'])
        message = str(request.POST.get('message'))[:99]
        sender = str(request.POST.get('sender'))[:19]
        self.send_wuphf(sender, message, receiver)
        return redirect('wuphf_sent')

    def send_wuphf(self, sender, message, receiver):
        """Code for handling the sending of a wuphf"""
        Wuphf.objects.create(sender=sender, message=message)
        receiver.call_home_phone(sender, message)
        receiver.call_cell_phone(sender, message)
        receiver.text_cell_phone(sender, message)


class WuphfSent(View):
    """Confirmation of sent page"""
    template_name = 'wuphf_sent.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class WuphfMessagesList(View):
    """Confirmation of sent page"""

    def get(self, request, *args, **kwargs):
        context = {
            'wuphfs': [x.id for x in Wuphf.objects.filter(seen=False)]
        }
        return JsonResponse(context)


class WuphfMessagesDetails(View):
    """Returns message dettails"""

    def get(self, request, *args, **kwargs):
        wuphf_id = request.GET.get('id')
        wuphf = Wuphf.objects.get(id=wuphf_id)
        wuphf.seen = True
        wuphf.save()
        context = {
            'message': wuphf.message,
            'sender': wuphf.sender,
        }
        return JsonResponse(context)
