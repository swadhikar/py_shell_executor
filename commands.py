import subprocess
from typing import Tuple, Any
from exceptions import (
    CommandException,
    FailIfResultContains,
    FailIfResultEquals,
    FailIfResultNotEquals,
    FailIfResultNotContains
)
from models import Command
from logger import log


def _execute(command: str, timeout: int = 5) -> Tuple[Any, int]:
    log('info', f'Executing command: {command}')
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result, error = proc.communicate(timeout=timeout)

    return_code = proc.returncode

    if return_code != 0:
        error = error.decode("utf - 8")
        log('error', f'Command "{command}" failed: {error}')
        raise CommandException(f'Command "{command}" failed. Exit code={return_code}, result={result}')

    result = result.decode('utf-8').strip()
    log('info', f'Result returned: {result}')
    return result, proc.returncode


def _validate_result(cmd: str, cmd_obj: Command, result: str) -> None:
    """Raises exception if conditions fail"""
    if_not_equal = cmd_obj.fail_if_result_not_equals
    if if_not_equal and if_not_equal.lower() != result.lower():
        log('error', cmd_obj.fail_msg)
        raise FailIfResultNotEquals(f'Command output "{result}" matches {if_not_equal}"')

    if_contains = cmd_obj.fail_if_result_contains
    if if_contains and if_contains.lower() in result.lower():
        log('error', cmd_obj.fail_msg)
        raise FailIfResultContains(f'Command output "{result}" contains {if_contains}"')

    if_not_contains = cmd_obj.fail_if_result_not_contains
    if if_not_contains and if_not_contains.lower() in result.lower():
        log('error', cmd_obj.fail_msg)
        raise FailIfResultNotContains(f'Command output "{result}" does not contain {if_not_contains}"')

    if_equal = cmd_obj.fail_if_result_equals
    if if_equal and result == if_equal:
        log('error', cmd_obj.fail_msg)
        raise FailIfResultEquals(f'Command output "{result}" does not match "{if_equal}"')

    log('info', cmd_obj.success_msg)


def run(cmd_obj: Command, cmd_config: dict) -> Tuple[str, int]:
    # Fetch command and verify if it ran successfully
    cmd = cmd_obj.cmd
    result, return_code = _execute(cmd)

    # Verify if commands fulfill conditions
    _validate_result(cmd, cmd_obj, result)

    # Recursive function
    if cmd_obj.send_result_execute:
        new_cmd_obj = Command(**cmd_config[cmd_obj.send_result_execute])  # needs config
        new_cmd_obj.cmd = new_cmd_obj.cmd.replace('<COMMAND OUTPUT>', result)
        return run(new_cmd_obj, cmd_config=cmd_config)

    return result, return_code
