from django.shortcuts import render_to_response


class MobileCheckerMiddleware(object):
    def process_response(self, request, response):
        if request.META and 'HTTP_USER_AGENT' in request.META \
                and 'iPhone' in request.META['HTTP_USER_AGENT']:
            return render_to_response('pages/mobile_app_download.html')

        return response
