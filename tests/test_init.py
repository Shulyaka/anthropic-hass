"""Tests for the Anthropic integration."""

from unittest.mock import AsyncMock, patch

import pytest
from anthropic import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
)
from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component
from httpx import URL, Request, Response
from pytest_homeassistant_custom_component.common import MockConfigEntry


def test_test(hass):
    """Workaround for https://github.com/MatthewFlamm/pytest-homeassistant-custom-component/discussions/160."""


@pytest.mark.parametrize(
    ("side_effect", "error"),
    [
        (APIConnectionError(request=None), "Connection error"),
        (APITimeoutError(request=None), "Request timed out"),
        (
            BadRequestError(
                message="Your credit balance is too low to access the Claude API. "
                "Please go to Plans & Billing to upgrade or purchase credits.",
                response=Response(
                    status_code=400,
                    request=Request(method="POST", url=URL()),
                ),
                body={"type": "error", "error": {"type": "invalid_request_error"}},
            ),
            "anthropic integration not ready yet: "
            "Your credit balance is too low to access the Claude API",
        ),
        (
            AuthenticationError(
                message="invalid x-api-key",
                response=Response(
                    status_code=401,
                    request=Request(method="POST", url=URL()),
                ),
                body={"type": "error", "error": {"type": "authentication_error"}},
            ),
            "Invalid API key",
        ),
    ],
)
async def test_init_error(
    hass: HomeAssistant,
    mock_config_entry: MockConfigEntry,
    caplog: pytest.LogCaptureFixture,
    side_effect,
    error,
) -> None:
    """Test initialization errors."""
    with patch(
        "anthropic.resources.messages.AsyncMessages.create",
        new_callable=AsyncMock,
        side_effect=side_effect,
    ):
        assert await async_setup_component(hass, "anthropic", {})
        await hass.async_block_till_done()
        assert error in caplog.text
