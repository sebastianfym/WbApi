from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .services import create_campaign, check_and_update_bet
from .services_config import headers, url_for_update_bet, url_for_create_campaign


class WildberriesViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['POST'], url_path='create_campaign')
    def create_campaign(self, request):
        url = url_for_create_campaign
        try:
            query_params = {
                "type": 8,  # автоматическая кампания
                "name": request.data["product_name"],  # Название кампании
                "subjectId": request.data["item_id"],  # ID предмета, для которого создается кампания.
                "sum": request.data["deposit_amount"],  # Сумма пополнения
                "btype": request.data["btype"],  # 0 - balance, 1 - net, 3 - bonus
                "on_pause": request.data["on_pause"]  # False - будет сразу запущена, True - запуск кампании будет доступен через 3 минуты после создания кампании.
            }
            result = create_campaign(url, query_params, headers)
            print(result)
            return Response(result, 200)
        except KeyError as error:
            return Response({"Ошибка:": f"Вы пропустили обязательное значение {error}"}, 400)

    @action(detail=False, methods=['POST'], url_path='update_bet')
    def check_and_update_bet(self, request):
        url = url_for_update_bet
        try:
            query_params = {
                "advertId": request.data["advertisement_id"],  # Идентификатор кампании, где меняется ставка
                "type": 9,  # 9 (поиск + каталог). Для type указывается значение 9 (всегда).
                "cpm": request.data["cpm"],  # Новое значение ставки
                "param": request.data["item_id"],  # id объекта в кампании (subjectId)
                "instrument": 6  # Для instrument указывается значение 4 или 6 в зависимости от того, в каталоге или поиске необходимо изменить ставку.
            }  # Если в кампании Поиск + Каталог доступен только Поиск, то установить ставку в Каталог (instrument = 4) не получится. В ответ Вы получите статус-код 422

            step = request.data["step"]
            result = check_and_update_bet(url, query_params, headers, step)
            return Response(result, 200)
        except KeyError as error:
            return Response({"Ошибка:": f"Вы пропустили обязательное значение {error}"}, 400)



