import json

import os

import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_files(host):
    pg_version = 11
    pg_conf_filename = "/etc/postgresql/{version}/postgresql.conf".format(
        version=pg_version
    )
    pg_hba_filename = "/etc/postgresql/{version}/pg_hba.conf".format(
        version=pg_version
    )

    if (host.system_info.distribution in ['centos']):
        pg_conf_filename = "/var/lib/pgsql/{version}/data/postgresql.conf".format(
            version=pg_version
        )
        pg_hba_filename = "/var/lib/pgsql/{version}/data/pg_hba.conf".format(
            version=pg_version
        )

    pg_hba = host.file(pg_hba_filename)
    assert pg_hba.contains("local")
    assert pg_hba.user == "postgres"
    assert pg_hba.group == "postgres"
    assert pg_hba.mode == 0o644
