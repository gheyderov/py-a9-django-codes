from django.utils.deprecation import MiddlewareMixin
from account.models import BlockedIps


class GetUserIpsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if request.user.is_authenticated:
            request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
                request.user.save()


class BlockUserMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        user = BlockedIps.objects.filter(ip = ip_address)
        if user:
            raise PermissionError