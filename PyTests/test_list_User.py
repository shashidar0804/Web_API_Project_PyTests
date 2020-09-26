import pytest
import requests
import json

from conftest import supply_token


@pytest.mark.parametrize("userid,firstname,lastname,phone",
                         [("FINPP", "Finn", "pp", "358418232323"), (("FINPX", "Fin", "pq", "358418232343"))])
def test_valid_user_with_token(supply_url, userid, firstname, lastname, phone):
    url = supply_url + "/users/" + str(userid)
    payload = {}
    token = supply_token()
    headers = {
        'Content-Type': 'application/json',
        'Token': token
    }
    resp = requests.request("GET", url, headers=headers, data=payload)
    j = json.loads(resp.text)
    assert resp.status_code == 200, resp.text
    assert j['payload']['firstname'] == firstname, resp.text
    assert j['payload']['lastname'] == lastname, resp.text
    assert j['payload']['phone'] == phone


def test_token_authentication(supply_url):
    url = supply_url + "/users/sha"
    resp = requests.get(url)
    assert resp.status_code == 401, resp.text


def test_users_list(supply_url):
    url = supply_url + "/users"
    resp = requests.get(url)
    assert resp.status_code == 200, resp.text


@pytest.mark.parametrize("userid",["FINPP"])
def test_put_user(supply_url, userid):
    url = supply_url + "/users/" + str(userid)

    payload = payload = "{\n        \"firstname\": \"Finn\",\n        \"lastname\": \"pp\",\n        \"phone\": " \
                        "\"358418232323\"\n} "
    token = supply_token()
    headers = {
        'Content-Type': 'application/json',
        'Token': token
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 200, response.text
