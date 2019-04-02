from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from posts_api.handlers import get_error_response
from apps.users.serializers import UserLoginSerializer


class LoginJSONRenderer(JSONRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = dict()

        if data.get('token', None):
            response_data['data'] = {'token': data['token']}
            valid_data = VerifyJSONWebTokenSerializer().validate(
                response_data['data'])
            user_to_dict = UserLoginSerializer(
                valid_data['user'],
            ).instance.__dict__
            del user_to_dict['_state'], \
                user_to_dict['password'], \
                user_to_dict['is_superuser']
            response_data['data']['user'] = user_to_dict

        elif data.get('is_reserved', None) is not None:
            response_data['data'] = data
        else:
            response_data = get_error_response(data)
        renderer_context = renderer_context or {}
        response = super().render(
            response_data, accepted_media_type, renderer_context)
        return response


class UserJSONRenderer(JSONRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status = True \
            if renderer_context['response'].status_code in range(200, 300) \
            else False
        if status:
            response_data = {
                'data':
                    {'user': None}
            }
            if data:
                response_data['data']['user'] = data
            if renderer_context['response'].status_code == 201:
                from rest_framework_jwt.settings import api_settings
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                token = jwt_encode_handler(data),
                response_data['data']['token'] = token[0]
            elif renderer_context['response'].status_code == 204:
                response_data = None
        else:
            response_data = get_error_response(data)
        renderer_context = renderer_context or {}
        response = super().render(
            response_data, accepted_media_type, renderer_context)
        return response
