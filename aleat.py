#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class holaApp(webapp.webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        return("200 ok", ("<html><body>Hola." +
                          "<a href=" +
                          str(random.randint(0, 10000000)) +
                          ">Dame Otra!!" +
                          "</p>" +
                          "</body></html>" +
                          "\r\n"))

if __name__ == "__main__":
    serv = holaApp("localhost", 1234)
