#!/usr/bin/env python3

from requests import post, put, get, delete
from requests.auth import HTTPBasicAuth
import json

class gpib_client:

    def __init__(self, adress, host, port, user, pw):
        self.user = user
        self.pw = pw
        self.adress = adress

        self.basic_url = host + ":" + str(port) + "/instrument/adress/" + str(adress)

        if user is None:
            post(self.basic_url + "/register")
        else:
            post(self.basic_url + "/register", auth=HTTPBasicAuth(user, pw))

    def read(self):

        if self.user is None:
            r = get(self.basic_url)
        else:
            r = get(self.basic_url, auth=HTTPBasicAuth(self.user, self.pw))

        value = json.loads(r.content)

        data = value['data']
        time = float(value['time'])

        return data, time

    def write(self, query):

        query_url = self.basic_url + "?q=" + query

        if self.user is None:
            r = put(query_url)
        else:
            r = put(query_url, auth=HTTPBasicAuth(self.user, self.pw))

        value = json.loads(r.content)

        time = float(value['time'])

        return time

    def write_read(self, query):

        query_url = self.basic_url + "?q=" + query

        if self.user is None:
            r = post(query_url)
        else:
            r = post(query_url, auth=HTTPBasicAuth(self.user, self.pw))

        value = json.loads(r.content)

        time = float(value['time'])
        data = value['data']

        return data, time

    def write_read_bulk(self, query, count):

        query_url = self.basic_url + "/count/" + str(count) + "?q=" + query

        if self.user is None:
            r = post(query_url)
        else:
            r = post(query_url, auth=HTTPBasicAuth(self.user, self.pw))

        values = json.loads(r.content)

        epoch_time = float(values[0]['time'])
        datas = []
        times = []

        for value in values:
            times.append(float(value['time']) - epoch_time)
            datas.append(value['data'])

        return datas, times, epoch_time

    def rst(self):

        self.write('*RST')

    def identify(self):

        data, time = self.write_read('*IDN?')
        return data

    def purge(self):

        if self.user is None:
            r = delete(self.basic_url + "/register")
        else:
            r = delete(self.basic_url + "/register", auth=HTTPBasicAuth(self.user, self.pw))








