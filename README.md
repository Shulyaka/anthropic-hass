# anthropic-hass
![CI](https://github.com/Shulyaka/anthropic-hass/actions/workflows/anthropic-hass.yml/badge.svg?branch=master)

Home Assistant custom component for Anthropic Claude conversation agent

Legal notice: This integration uses the official API. Please note that Anthropic API is intended for B2B and not for individual use, [more info here](https://support.anthropic.com/en/articles/8987200-can-i-use-the-claude-api-for-individual-use). Therefore this integration is intended for commercial uses.

The Anthropic integration adds a conversation agent powered by [Anthropic](https://www.anthropic.com), such as Claude 3.5 Sonnet, in Home Assistant.

Controlling Home Assistant is done by providing the AI access to the Assist API of Home Assistant. You can control what devices and entities it can access from the Exposed Entities page. The AI can provide you information about your devices and control them.

This integration does not integrate with [sentence triggers](https://www.home-assistant.io/docs/automation/trigger/#sentence-trigger).

This integration requires an API key to use, [which you can generate here.](https://console.anthropic.com/settings/keys). This is a paid service, we advise you to monitor your costs in the [Anthropic portal](https://console.anthropic.com/settings/cost) closely.

{% include integrations/config_flow.md %}

## Generate an API Key

The Anthropic API key is used to authenticate requests to the Anthropic API. To generate an API key, take the following steps:

- Log in to the [Anthropic portal](https://console.anthropic.com) or sign up for an account.
- Enable billing with a valid credit card on the [plans page](https://console.anthropic.com/settings/plans).
- Visit the [API Keys page](https://console.anthropic.com/settings/keys) to retrieve the API key you'll use to configure the integration.

## Configuration
Instructions:
  description: Instructions for the AI on how it should respond to your requests. It is written using [Home Assistant Templating](https://www.home-assistant.io/docs/configuration/templating/).

Control Home Assistant:
  description: If the model is allowed to interact with Home Assistant. It can only control or provide information about entities that are [exposed](https://www.home-assistant.io/voice_control/voice_remote_expose_devices/) to it.

Recommended settings:
  description: If enabled, the recommended model and settings are chosen.

If you choose not to use the recommended settings, you can configure the following options:

Model:
  description: The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/about-claude/models#model-names) for additional details and options.

Maximum Tokens to Return in Response:
  description: The maximum number of tokens to generate before stopping. Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate. Different models have different maximum values for this parameter. See [models](https://docs.anthropic.com/en/docs/models-overview) for details.

Temperature:
  description: Amount of randomness injected into the response. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks. Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

