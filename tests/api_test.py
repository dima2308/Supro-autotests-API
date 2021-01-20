import pytest
import json
import allure

from utils import *
from config import  run_id
from testrail_methods import add_result_for_case


@pytest.mark.positive
@allure.epic('API методы')
@allure.story('Успешные запросы')
class TestSuccessRequests:

    @allure.title('Получение версии протокола и ПО')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/757414')
    def test_get_version(self, client):
        case_id = 757414
        res = client.get_version()
        res_data = json.loads(res.text)

        api_version = res_data['data']['API']['version']
        app_version = res_data['data']['Application']['version']
        results_info = [api_version, app_version]

        assert all(results_info) and res.status_code == 200, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Получение списка активных баннеров')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/757415')
    def test_get_active_banners(self, client):
        case_id = 757415
        res = client.get_active_banners()
        res_data = json.loads(res.text)

        type_data = type(res_data['data'])
        params = get_banners_list(res_data['data'])

        assert type_data == list and all(params), add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Получение списка независимых предложений')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756194')
    def test_get_independent_offers(self, client):
        case_id = 756194
        req_data = {
            'terminal_id': 1,
            'user_id': 1
        }

        res = client.get_independent_offers(req_data)
        res_data = json.loads(res.text)
        type_data = type(res_data['data'])

        assert type_data == list and res.status_code == 200, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Получение списка зависимых предложений')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756192')
    @pytest.mark.parametrize('games_id', [
        pytest.param(['71032', '71035'], marks=pytest.mark.xfail),
        ['7103', '71035']],
        ids=["No offers", "Offers"])
    def test_get_dependent_offers(self, client, games_id):
        case_id = 756192
        data = {
            'terminal_id': 1,
            'user_id': 1,
            'basket': games_id
        }

        res = client.get_dependent_offers(data)
        res_data = json.loads(res.text)

        test_results = []

        for i, val in enumerate(res_data):
            test_results.append(res_data['data'][games_id[i]] != [])

        assert any(test_results) and res.status_code == 200, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Регистрация продажи билета')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/801518')
    def test_register_sale(self, client):
        case_id = 801518
        data = {
            'terminal_id': 1000000000,
            'user_id': 10000000,
            'data': 'Jl+rsdjEMGg='
        }

        res = client.register_sale(data)
        res_data = json.loads(res.text)

        assert res.status_code == 200 and res_data["result"] == "OK", add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Получение списка персональных предложений')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/890421')
    def test_get_personal_offers(self, client):
        case_id = 890421
        data = {
            'terminal_id': 1000000000,
            'user_id': 10000000,
            'phone': 79999999998
        }

        res = client.get_personal_offers(data)
        res_data = json.loads(res.text)

        assert res.status_code == 200 and res_data["result"] == "OK", add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)


@allure.epic('API методы')
@allure.story('Неуспешные запросы')
@pytest.mark.negative
class TestUnsuccessRequests:

    @allure.title('Запрос на получение зависимых предложений с пустой корзиной')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756193')
    def test_get_dependent_offers_with_empty_basket(self, client):
        case_id = 756193
        data = {
            'terminal_id': 1,
            'user_id': 1,
            'basket': []
        }

        res = client.get_dependent_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Запрос на получение зависимых предложений с пустым пользователем')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/757412')
    def test_get_dependent_offers_without_user(self, client):
        case_id = 757412
        data = {
            'terminal_id': 1,
            'basket': [2]
        }

        res = client.get_dependent_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Запрос на получение независимых предложений с невалидным параметром')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/756195')
    def test_get_independent_offers_with_invalid_param(self, client):
        case_id = 756195
        data = {
            'terminal_id': -1,
            'user_id': 1
        }

        res = client.get_independent_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Запрос на получение независимых предложений с пустым параметром')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/757413')
    def test_get_independent_offers_with_empty_param(self, client):
        case_id = 757413
        data = {
            "terminal_id": -1,
            "user_id": ''
        }

        res = client.get_independent_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Запрос на получение персональных предложений с некорректным номером телефона')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/892903')
    def test_get_personal_offers_with_invalid_phone(self, client):
        case_id = 892903
        data = {
            'terminal_id': 1000000000,
            'user_id': 10000000,
            'phone': 799999999981
        }

        res = client.get_personal_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)

    @allure.title('Запрос на получение персональных предложений с пустым параметром')
    @allure.testcase('https://qa-tr.it.orglot.office/testrail/index.php?/cases/view/892904')
    def test_get_personal_offers_with_empty_param(self, client):
        case_id = 892904
        data = {
            'terminal_id': 1000000000,
            'user_id': 10000000,
            'phone': 799999999981
        }

        res = client.get_personal_offers(data)

        assert res.status_code == 400, add_result_for_case(run_id, case_id, 5)
        add_result_for_case(run_id, case_id, 1)
