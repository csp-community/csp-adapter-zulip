"""Reply to any Zulip message that says hello."""

import os

import csp
from csp import ts

from csp_adapter_zulip import ZulipAdapter, ZulipConfig, ZulipMessage


@csp.node
def reply_to_hello(msg: ts[ZulipMessage]) -> ts[ZulipMessage]:
    if "hello" in msg.content.lower():
        return ZulipMessage(channel=msg.channel, content=f"hello, {msg.author_name}")


def graph(adapter: ZulipAdapter):
    messages = csp.unroll(adapter.subscribe())
    csp.print("messages", messages)
    adapter.publish(reply_to_hello(messages))


if __name__ == "__main__":
    config = ZulipConfig(
        site=os.environ["ZULIP_SITE"],
        email=os.environ["ZULIP_EMAIL"],
        api_key=os.environ["ZULIP_API_KEY"],
    )
    csp.run(graph, ZulipAdapter(config), realtime=True)
