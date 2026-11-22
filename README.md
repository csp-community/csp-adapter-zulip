# csp zulip adapter

A [csp](https://github.com/point72/csp) adapter for [Zulip](https://zulip.com)

[![Build Status](https://github.com/csp-community/csp-adapter-zulip/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/csp-community/csp-adapter-zulip/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/csp-community/csp-adapter-zulip/branch/main/graph/badge.svg)](https://codecov.io/gh/csp-community/csp-adapter-zulip)
[![License](https://img.shields.io/github/license/csp-community/csp-adapter-zulip)](https://github.com/csp-community/csp-adapter-zulip)
[![PyPI](https://img.shields.io/pypi/v/csp-adapter-zulip.svg)](https://pypi.python.org/pypi/csp-adapter-zulip)

## Overview

The Zulip adapter reads and writes Zulip messages in [csp](https://github.com/point72/csp) graphs. It wraps the Zulip backend from [chatom](https://github.com/1kbgz/chatom), which uses the [`zulip`](https://pypi.org/project/zulip/) API client.

## Chat Framework

[`csp-bot`](https://github.com/Point72/csp-bot) is a framework for writing cross-platform, command oriented chat bots.

## Installation

Install with `pip`:

```bash
pip install csp csp-adapter-zulip
```

## License

This software is licensed under the Apache 2.0 license. See the [LICENSE](https://github.com/csp-community/csp-adapter-zulip/blob/main/LICENSE) file for details.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
