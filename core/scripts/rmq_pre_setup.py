# -*- coding: utf-8 -*-

"""

    Module :mod:``

    This Module is created to...

    LICENSE: The End User license agreement is located at the entry level.

"""

# ----------- START: Native Imports ---------- #
import shlex
import subprocess
# ----------- END: Native Imports ---------- #

# ----------- START: Third Party Imports ---------- #
# ----------- END: Third Party Imports ---------- #

# ----------- START: In-App Imports ---------- #
from core.utils.environ import (
    get_build_path,
    get_rabbitmq_details,
    get_queue_details
)
# ----------- END: In-App Imports ---------- #


def run_command(command):
    _out = list()
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
            _out.append(output.strip())
    rc = process.poll()
    return True if not rc else False, _out


def queue_declare():
    """."""
    queue_details = get_queue_details()
    mq_details = get_rabbitmq_details()

    executable = '{}/bin/rabbitmqadmin'.format(get_build_path())

    for _, (queue_name, durable) in queue_details.items():
        #
        # Cleanup the existing queues.
        status, output = run_command(
            '{} delete queue name={} --vhost={} -u {} -p {}'.format(
                executable,
                queue_name,
                mq_details['vhost'],
                mq_details['username'],
                mq_details['password']
            )
        )

        #
        # Create queues.
        status, output = run_command(
            '{} declare queue name={} --vhost={} durable={} -u {} -p {}'.format(
                executable,
                queue_name,
                mq_details['vhost'],
                'true' if durable == 'durable_true' else 'false',
                mq_details['username'],
                mq_details['password']
            )
        )


def declare_exchange():

    mq_details = get_rabbitmq_details()

    executable = '{}/bin/rabbitmqadmin'.format(get_build_path())

    status, output = run_command(
        '{} declare exchange name={} --vhost={} type=direct -u {} -p {}'.format(
            executable,
            mq_details['exchange'],
            mq_details['vhost'],
            mq_details['username'],
            mq_details['password']
        )
    )


def declare_vhost():
    """."""
    mq_details = get_rabbitmq_details()

    executable = '{}/bin/rabbitmqadmin'.format(get_build_path())

    print 'Deleting Virtual host: ', mq_details['vhost'],
    status, output = run_command(
        '{} delete vhost name={} -u {} -p {}'.format(
            executable,
            mq_details['vhost'],
            mq_details['username'],
            mq_details['password']
        )
    )

    print 'Creating Virtual host: ', mq_details['vhost'],
    status, output = run_command(
        '{} declare vhost name={} -u {} -p {}'.format(
            executable,
            mq_details['vhost'],
            mq_details['username'],
            mq_details['password']
        )
    )

    print 'Setting Permission for user {} on Virtual host {}'.format(mq_details['username'], mq_details['vhost'])
    status, output = run_command(
        '{} declare permission vhost={} user={} configure=.* write=.* read=.* -u {} -p {}'.format(
            executable,
            mq_details['vhost'],
            mq_details['username'],
            mq_details['username'],
            mq_details['password']
        )
    )
