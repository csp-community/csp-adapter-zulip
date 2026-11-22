"""Tests for csp-adapter-zulip."""

import csp_adapter_zulip
from csp_adapter_zulip import ZulipAdapter, ZulipBackend, ZulipConfig


def test_exports():
    for name in csp_adapter_zulip.__all__:
        assert getattr(csp_adapter_zulip, name) is not None
    assert isinstance(csp_adapter_zulip.__version__, str)


def test_adapter_wraps_backend():
    adapter = ZulipAdapter(ZulipConfig(site="https://example.zulipchat.com", email="bot@example.com", api_key="key"))
    assert type(adapter.backend) is ZulipBackend
    assert adapter.backend.config.site == "https://example.zulipchat.com"
