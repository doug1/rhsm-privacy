#!/bin/sh

install -m 644 privacy.FactsPrivacyPlugin.conf /etc/rhsm/pluginconf.d/privacy.FactsPrivacyPlugin.conf
install -m 644 privacy.py /usr/share/rhsm-plugins/privacy.py

