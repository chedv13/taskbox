from django.shortcuts import render_to_response


class CheckIphoneRequest(object):
    def process_response(self, request, response):
        if 'iPhone' in request.META['HTTP_USER_AGENT']:
            return render_to_response('pages/mobile_app_download.html')

        return response
