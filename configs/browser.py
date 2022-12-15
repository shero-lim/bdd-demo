from urllib.parse import urlparse
from configs.config import config

DEFAULT_CHROME_ARGS = [
    "--enable-automation",
    "--disable-background-timer-throttling",
    "--disable-renderer-backgrounding",
    "--disable-backgrounding-occluded-windows",
    "--disable-ipc-flooding-protection",
    "--allow-http-screen-capture",
    "--no-user-gesture-required",
    "--autoplay-policy=no-user-gesture-required",
    "--ignore-autoplay-restrictions",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--ignore-certificate-errors",
    "--allow-running-insecure-content",
    "--disable-web-security",
    "--disable-browser-side-navigation",
    "--ignore-certificate-errors",
]

DEFAULT_CHROME_PREFS = {
    "profile.managed_default_content_settings.notifications": 1,
    "intl.accept_languages": "en",
    "prompt_for_download": False,
    "enable_do_not_track": True,
}

browserConfigurations = {
    "chrome": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
        },
        "goog:loggingPrefs": {
            "driver": "INFO",
            "browser": "INFO"
        },
    },
    "chrome#stable": {
        "browserName": "chrome",
        "browserVersion": "stable",
        "goog:chromeOptions": {
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
        },
        "goog:loggingPrefs": {
            "driver": "INFO",
            "browser": "INFO"
        },
    },
    "chrome#mobile": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
            "mobileEmulation": {"deviceName": "Nexus 5"}
        },
    },
    "chrome#debug": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": ["--verbose", "--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
                     *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
                "directory_upgrade": True,
            },
        },
    },
    "chrome#headless": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": ["--headless", "--verbose", "--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
                     "--lang=en", *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
                "directory_upgrade": True,
            },
        },
    },
    "chrome#real-device": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": [*DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
        },
    },
    "chrome#user-data-dir": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
                     "--user-data-dir=" + config["userDataDirOfChrome"], *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
        },
        "goog:loggingPrefs": {
            'driver': 'INFO',
            'browser': 'INFO'
        },
    },
    "electron": {
        "browserName": "chrome",
        "goog:chromeOptions": {
            "binary": config["electronBinary"],
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
        },
        "goog:loggingPrefs": {
            'driver': 'INFO',
            'browser': 'INFO'
        },
    },
    "electron#federation": {
        "browserName": "chrome",
        "browserVersion": "electron",
        "goog:chromeOptions": {
            "binary": "",
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
        },
        "goog:loggingPrefs": {
            "driver": "INFO",
            "browser": "INFO"
        },
        "sf:envs": {
            "LAST_ENV_URL": config["siteUrl"],
        }
    },
    "electron#webinar": {
        "browserName": "chrome",
        "browserVersion": "electron",
        "goog:chromeOptions": {
            "binary": config["electronBinary"],
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream", *DEFAULT_CHROME_ARGS],
        },
        "goog:loggingPrefs": {
            'driver': 'INFO',
            'browser': 'INFO'
        },
    },
    "electron#user-data-dir": {
        "browserName": "chrome",
        "browserVersion": 'electron',
        "goog:chromeOptions": {
            "binary": config["electronBinary"],
            "args": ["--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
                     "--user-data-dir=" + config["userDataDirOfElectron"], *DEFAULT_CHROME_ARGS]},
        "goog:loggingPrefs": {
            "driver": "INFO",
            "browser": "INFO"
        },
    },
    "firefox": {
        "browserName": "firefox",
        "acceptInsecureCerts": True,
        "moz:firefoxOptions": {
            "prefs": {
                "media.navigator.streams.fake": True,
                "permissions.default.microphone": 1,
                "permissions.default.camera": 1,
                "accept_untrusted_certs": True,
            },
        }
    },
    "safari": {
        "browserName": "safari",
        "acceptInsecureCerts": True,
    },
    "msedge": {
        "browserName": "MicrosoftEdge",
        "ms:edgeOptions": {
            "args": ["--start-maximized", "--use-fake-ui-for-media-stream", "--use-fake-device-for-media-stream",
                     *DEFAULT_CHROME_ARGS],
            "prefs": {
                **DEFAULT_CHROME_PREFS,
            },
        },

    },
}

print(browserConfigurations)
