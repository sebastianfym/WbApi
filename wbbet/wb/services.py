import requests


def create_campaign(url: str, query_params: dict, headers: dict) -> dict:  # Использовать, если у нас еще нет кампании
    response = requests.post(url, data=query_params, headers=headers)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        return {"error": "Некорректный id предмета"}
    elif response.status_code == 401:
        return {"error": "Ошибка авторизации"}
    elif response.status_code == 422:
        return {"error": "Ошибка получения размещения в рекомендациях на главной"}


def check_and_update_bet(url: str, query_params: dict, headers: dict,
                         step: int) -> dict:  # Использовать в случае, если кампания есть и нужно обновить ставку
    while True:
        response = requests.post(url, data=query_params, headers=headers)

        if response.status_code == 200:
            return {'Success': 'Продвижение прошло успешно.'}
        elif response.status_code == 401:
            return {"error": "Ошибка авторизации"}
        elif response.status_code == 422:
            query_params["cpm"] += step
