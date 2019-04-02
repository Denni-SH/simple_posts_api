from rest_framework.renderers import JSONRenderer

from posts_api.handlers import get_error_response


class PostJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status = True \
            if renderer_context['response'].status_code in range(200, 300) \
            else False
        if status:
            response_data = None
            if renderer_context['response'].status_code != 204:
                response_data = {
                    'data':
                        {'post': data}
                }
        else:
            response_data = get_error_response(data)
        renderer_context = renderer_context or {}
        response = super().render(
            response_data, accepted_media_type, renderer_context)
        return response
