from django.conf import settings
from django.http import JsonResponse
from django.views import View

from .send_message_telegram import send_message


JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


class BaseView(View):
    """
    Базовый класс всех представлений. Обрабатывает
    исключений и отправляет админам в телеграм
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            send_message(settings.DEV_TG_ID, e.__str__())
            return self._response({'errorMessage': e}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS
        )
