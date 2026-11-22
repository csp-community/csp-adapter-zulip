"""Zulip CSP adapter using chatom's Zulip backend."""

from chatom.csp import BackendAdapter
from chatom.zulip import ZulipBackend, ZulipConfig

__all__ = ("ZulipAdapter",)


# chatom declares BackendAdapter conditionally: a placeholder function when csp is
# missing, the real class otherwise. csp is a hard dependency here, so it is always
# the class at runtime, but ty sees the union of both branches.
class ZulipAdapter(BackendAdapter):  # ty: ignore[invalid-base]
    """CSP adapter for Zulip, wrapping chatom's ZulipBackend.

    ``subscribe()`` returns a time series of incoming messages and ``publish()``
    sends them.
    """

    def __init__(self, config: ZulipConfig):
        super().__init__(ZulipBackend(config=config))
