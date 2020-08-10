import unittest

from exceptions import *
from models import Command
from logger import log
import commands

cmd_1 = {
    "cmd": "ps -ef | grep ssh-agent | grep -v '/usr/bin/ps' | awk 'NR==1{ print $2 }'",
    "fail_if_result_equals": "",
    "fail_msg": "SSH agent is not running in this machine!",
    "success_msg": "SSH agent is started and running in this machine!",
}

cmd_2 = {
    "cmd": "cmdswadhi -ltr",
    "fail_if_result_equals": ""
}

cmd_3 = {
    "cmd": "ps -ef | grep ssh-agent | grep -v '/usr/bin/ps' | awk 'NR==1{ print $2 }'",
    "fail_if_result_equals": "",
    "send_result_execute": "cmd_4"
}

cmd_4 = {
    "cmd": "ps -ef | grep <COMMAND OUTPUT>",
    "fail_if_result_equals": "",
    "fail_msg": "Unable to find SSH agent running in this PC!",
    "success_msg": "SSH agent is started and running in this machine!",
    "send_result_execute": "cmd_5"
}

cmd_5 = {
    "cmd": "echo <COMMAND OUTPUT>  | wc -l",
    "fail_if_result_not_equals": "1",
    "success_msg": "Found exactly one ssh-agent process successfully!",
    "fail_msg": "Failed to find at least one ssh-agent process in this PC",
}

cmd_6 = {
    "cmd": "ps -ef | grep ssh-agent | grep -v '/usr/bin/ps' | awk 'NR==1{ print $2 }'",
    "fail_if_result_equals": "",
    "send_result_execute": "cmd_7",
    "success_msg": "Found exactly one ssh-agent process successfully!"
}

cmd_7 = {
    "cmd": "ps -ef | grep <COMMAND OUTPUT>",
    "fail_if_result_equals": "",
    "fail_msg": "Unable to find SSH agent running in this PC!",
    "send_result_execute": "cmd_8",
    "success_msg": "Successfully grepped",
}

cmd_8 = {
    "cmd": "echo <COMMAND OUTPUT>  | wc -l",
    "fail_if_result_not_equals": "2",
    "success_msg": "Found exactly one ssh-agent process successfully!",
    "fail_msg": "Only one ssh-agent process detected as expected",
}

cmd_config = {
    'cmd_1': cmd_1,
    'cmd_2': cmd_2,
    'cmd_3': cmd_3,
    'cmd_4': cmd_4,
    'cmd_5': cmd_5,
    'cmd_6': cmd_6,
    'cmd_7': cmd_7,
    'cmd_8': cmd_8
}


class TestShellExecutor(unittest.TestCase):
    def test_commands(self):
        command_1 = Command(**cmd_1)
        commands.run(command_1, cmd_config=cmd_config)

    def test_commands_exception(self):
        command_2 = Command(**cmd_2)
        try:
            commands.run(command_2, cmd_config=cmd_config)
        except CommandException as e:
            log('error', e)
        else:
            raise Exception('CommandException not raised')

    def test_commands_recursive(self):
        command_3 = Command(**cmd_3)
        commands.run(command_3, cmd_config=cmd_config)

    def test_commands_recursive_exception(self):
        command_6 = Command(**cmd_6)
        try:
            commands.run(command_6, cmd_config=cmd_config)
        except FailIfResultNotEquals:
            pass
        else:
            raise Exception('FailIfResultNotEquals is not raised!')


if __name__ == '__main__':
    unittest.main()
