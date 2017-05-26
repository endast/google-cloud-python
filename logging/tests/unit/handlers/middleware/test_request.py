# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest


class TestRequestMiddleware(unittest.TestCase):

    def _get_target_class(self):
        from google.cloud.logging.handlers.middleware.request import RequestMiddleware

        return RequestMiddleware

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_get_request(self):
        from django.conf import settings
        from django.test.utils import setup_test_environment
        from django.test import RequestFactory

        settings.configure()
        setup_test_environment()

        self.middleware = self._make_one()
        self.request = RequestFactory().get('/')
        self.middleware.process_request(self.request)
        self.assertEqual(self.middleware.get_request(), self.request)
