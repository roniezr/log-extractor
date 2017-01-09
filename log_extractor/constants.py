"""

"""
JOB_ARTIFACT = 'artifact'
JOB_ARTIFACT_ZIP = '{0}/*zip*/archive.zip'.format(JOB_ARTIFACT)

ARCHIVE_EXTENSIONS = ['.gz', '.zip', '.xz', '.tar', '.bz2']

TEAMS = ['sla', 'virt', 'networking', 'storage', 'system']

FIELD_TEST_NAME = 'Test Name'
FIELD_SETUP = 'SETUP <'
FIELD_TEARDOWN = 'PACKAGE TEARDOWN'

LOG_ART_RUNNER = 'art_test_runner.log'
LOG_ENGINE = 'engine.log'

TS_FORMAT = '%Y-%m-%d %H:%M:%S,%f'
TS_START = 'start_timestamp'
TS_END = 'end_timestamp'

HOST_LOGS = ["vdsm.log", "supervdsm.log"]
DEFAULT_LOGS = HOST_LOGS + [LOG_ENGINE]
