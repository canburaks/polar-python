# WebhookSubscriptionRevokedPayload

Sent when a subscription is revoked, the user looses access immediately.
Happens when the subscription is canceled, or payment is past due.

**Discord & Slack support:** Full


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      | Example                                          |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `type`                                           | *Literal["subscription.revoked"]*                | :heavy_check_mark:                               | N/A                                              | subscription.revoked                             |
| `data`                                           | [models.Subscription](../models/subscription.md) | :heavy_check_mark:                               | N/A                                              |                                                  |