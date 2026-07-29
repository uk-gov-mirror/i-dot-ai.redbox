import logging
import os

from playwright.sync_api import Page
from yarl import URL

from .pages import LandingPage

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)


BASE_URL = URL(os.environ.get("BASE_URL", " "))


def test_user_journey(page: Page):
    """End to end user journey test.

    Simulates a single user journey through the application, running against the full suite of microservices.

    Uses the Page Object Model - see https://pinboard.in/u:brunns/t:page-object for some resources explaining this.
    Please add to the page objects in `pages.py` where necessary - don't put page specific logic at this level.

    We should not be asserting anything about AI generated content in this test, aside from asserting that there
    is some."""

    logger.debug("Starting the E2E test on url %s", BASE_URL)

    # Landing page
    landing_page = LandingPage(page, BASE_URL)

    # Sign in
    chats_page = landing_page.sign_in()

    chats_page.write_message = "Hello world"
    chats_page = chats_page.send()


def test_support_pages(page: Page):
    # Landing page
    landing_page = LandingPage(page, BASE_URL)

    # Privacy page
    landing_page.navigate_to_privacy_page()

    # Accessibility page
    landing_page.navigate_to_accessibility_page()

    # Support page
    landing_page.navigate_to_support_page()
