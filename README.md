
Env variables:

SHELLY_PLUG_IP
SHELLY_PLUG_INTERVAL  - polling status of shelly plug status in seconds
NEW_RELIC_LICENSE_KEY


Shelly S Plug returns the following:

{
  "wifi_sta": {...},
  "cloud": {...},
  "mqtt": {...},
  "time": "13:15",
  "relays": [
    {
      "ison": true,
      "has_timer": false,
      "timer_started": 0,
      "timer_duration": 0,
      "timer_remaining": 0,
      "overpower": false,
      "source": "http"
    }
  ],
  "meters": [
    {
      "power": 42.37,
      "overpower": 0,
      "is_valid": true,
      "timestamp": 169926,
      "counters": [0, 0, 0],
      "total": 12345
    }
  ]
}

