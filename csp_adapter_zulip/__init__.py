"""CSP adapter for Zulip, built on chatom."""

__version__ = "0.1.0"

from chatom.zulip import (
    ZULIP_CAPABILITIES,
    MockZulipBackend,
    ZulipBackend,
    ZulipChannel,
    ZulipConfig,
    ZulipMessage,
    ZulipPresence,
    ZulipPresenceStatus,
    ZulipUser,
    mention_channel,
    mention_user,
)

from .adapter import ZulipAdapter

__all__ = (
    "ZULIP_CAPABILITIES",
    "MockZulipBackend",
    "ZulipAdapter",
    "ZulipBackend",
    "ZulipChannel",
    "ZulipConfig",
    "ZulipMessage",
    "ZulipPresence",
    "ZulipPresenceStatus",
    "ZulipUser",
    "mention_channel",
    "mention_user",
)
