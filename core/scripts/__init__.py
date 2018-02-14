# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.scripts.rmq_pre_setup import queue_declare, declare_vhost, declare_exchange
# ----------- END: In-App Imports ---------- #

__all__ = [
    # All public symbols go here.
]

__import__('pkg_resources').declare_namespace(__name__)


def presets():
    """."""

    declare_vhost()
    declare_exchange()
    queue_declare()
