# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium.webdriver.support.event_firing_webdriver import \
    EventFiringWebDriver

from utils import factory


@pytest.fixture
def driver(request):
    """Return a factory function creating WebDriver instances.
    """
    driver_type = request.config.getoption('driver')
    if driver_type is None:
        raise pytest.UsageError('--driver must be specified')

    driver_fixture = '{0}_driver'.format(driver_type.lower())
    driver_factory = request.getfuncargvalue(driver_fixture)

    event_listener = request.config.getoption('event_listener')
    if event_listener:
        # Import the specified event listener and wrap the driver instance
        mod_name, class_name = event_listener.rsplit('.', 1)
        mod = __import__(mod_name, fromlist=[class_name])
        event_listener = getattr(mod, class_name)

    @factory
    def _get_instance():
        web_driver = driver_factory.get_instance()
        if not isinstance(web_driver, EventFiringWebDriver):
            web_driver = EventFiringWebDriver(web_driver, event_listener())

        request.node._driver = web_driver
        request.addfinalizer(web_driver.quit)
        return web_driver
    return _get_instance
