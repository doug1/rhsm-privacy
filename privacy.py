#! /usr/bin/python

import re

from subscription_manager.base_plugin import SubManPlugin

requires_api_version = "1.0"

class FactsPrivacyPlugin(SubManPlugin):
    def post_facts_collection_hook(self, conduit):
        p = re.compile('(asset_tag|interface|mac_addr|part_num|serial)')
        redact = [key for key in conduit.facts if p.search(key)]
        for key in redact: del conduit.facts[key]

