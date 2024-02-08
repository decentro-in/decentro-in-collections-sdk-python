# coding: utf-8

"""
    decentro-in-collections

    Collections

    The version of the OpenAPI document: 1.0.0
    Contact: admin@decentro.tech
    Created by: https://decentro.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import decentro_in_collections_client
from decentro_in_collections_client.paths.v2_payments_upi_link import post
from decentro_in_collections_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2PaymentsUpiLink(ApiTestMixin, unittest.TestCase):
    """
    V2PaymentsUpiLink unit test stubs
        Generate payment link
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
