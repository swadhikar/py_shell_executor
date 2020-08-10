import subprocess


def print_message(message_type, message):
    if message:
        print(f'{message_type.upper()}: {message}')


# command = 'ls | wc -l'
def execute(command):
    print_message('info', f'Executing command: {command}')
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result, error = proc.communicate(timeout=5)

    if not error:
        result = result.decode('utf-8').strip()
        print_message('info', f'Result returned: {result}')
        return result

    error = error.decode("utf - 8")
    print(f'Command "{command}" failed: {error}')
    return None


# config = {
#     "ls -ltr | wc -l": {
#         "expected_result": "5",
#         "fail_condition": "ls -ltr"
#     }
# }
#
# for command in config:
#     expected_result = config[command]['expected_result']
#     result = execute(command)
#
#     if expected_result == result:
#         print(f'Command "{command}" returned "{result}" and matches expected condition "{expected_result}"')
#         exit(0)
#
#     print(f'Command "{command}" returned "{result}" which DOES NOT MATCH with'
#           f'expected result: "{expected_result}". Trying alternate command...')
#     fail_command = config[command]['fail_condition']
#     execute(fail_command)

config = {
    "cmd_1": {
        "cmd": "ps -ef | grep ssh-agent | grep -v '/usr/bin/ps' | awk 'NR==1{ print $2 }'",
        "fail_condition": "",
        "fail_msg": "ERROR: SSH agent is not running in this machine!",
        "success_msg": "INFO: SSH agent is started and running in this machine!",
        "send_result_execute": "cmd_3"
    },
    "cmd_3": {
        "cmd": "ps -ef | grep <COMMAND OUTPUT>",
        "fail_condition": "",
        "fail_msg": "ERROR: Unable to find SSH agent running in this PC!",
        "success_msg": "INFO: SSH agent is started and running in this machine!",
    }
}

for command in config:
    result = execute(config[command]['cmd'])

    if config[command]['fail_condition'] == result:
        failure_msg = config[command].get('fail_msg', '')
        print(f'{failure_msg}')
        exit(1)

    success_msg = config[command].get('success_msg', '')
    print(f'{success_msg}')

    if config[command].get('send_result_execute'):
        new_cmd_name = config[command].get('send_result_execute')
        new_cmd = f"{config[new_cmd_name]['cmd']}".replace('<COMMAND OUTPUT>', result)
        result = execute(new_cmd)

        if config[new_cmd_name]['fail_condition'] == result:
            failure_msg = config[command].get('fail_msg', '')
            print(f'{failure_msg}')
            exit(1)

        success_msg = config[new_cmd_name].get('success_msg', '')
        print(f'{success_msg}')

    exit(0)
