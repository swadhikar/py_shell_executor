import subprocess
from typing import Tuple, Any
from shell.exceptions import (
    CommandException,
    ResultDoesNotContainException,
    ResultNotEqualException,
    ResultEqualException,
    ResultContainException
)
from shell.models import Command
from shell.logger import log


def _execute(command: str, timeout: int = 5) -> Tuple[str, int]:
    log('info', f'Executing command: {command}')
    proc = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result, error = proc.communicate(timeout=timeout)

    return_code = proc.returncode

    if return_code != 0:
        error = error.decode("utf - 8")
        log('error', f'Command "{command}" failed: {error}')
        # Need to customize exception cases
        raise CommandException(f'Command "{command}" failed. Exit code={return_code}, result={result}')

    result = result.decode('utf-8').strip()
    log('info', f'Result returned: {result}')
    return result, proc.returncode


def _validate_result(cmd_obj: Command, result: str) -> None:
    """Raises exception if conditions fail"""
    if_not_equal = cmd_obj.result_not_equal
    if if_not_equal and if_not_equal.lower() != result.lower():
        log('error', cmd_obj.fail_msg)
        raise ResultEqualException(f'Command output "{result}" matches {if_not_equal}"')

    if_contains = cmd_obj.result_contain
    if if_contains and if_contains.lower() in result.lower():
        log('error', cmd_obj.fail_msg)
        raise ResultDoesNotContainException(f'Command output "{result}" contains {if_contains}"')

    if_not_contains = cmd_obj.result_not_contain
    if if_not_contains and if_not_contains.lower() not in result.lower():
        log('error', cmd_obj.fail_msg)
        raise ResultContainException(f'Command output "{result}" contains {if_not_contains}"')

    if_equal = cmd_obj.result_equal
    if if_equal and result == if_equal:
        log('error', cmd_obj.fail_msg)
        raise ResultNotEqualException(f'Command output "{result}" does not match "{if_equal}"')

    log('info', cmd_obj.pass_msg)


def run(cmd_obj: Command, cmd_config: dict) -> Tuple[str, int]:
    # Fetch command and verify if it ran successfully
    cmd = cmd_obj.cmd
    result, return_code = _execute(cmd)

    # Verify if commands fulfill conditions
    _validate_result(cmd_obj, result)

    # Recursive function
    if cmd_obj.redirect_result:
        new_cmd_obj = Command(**cmd_config[cmd_obj.redirect_result])  # needs config
        new_cmd_obj.cmd = new_cmd_obj.cmd.replace('<COMMAND OUTPUT>', result)
        return run(new_cmd_obj, cmd_config=cmd_config)

    return result, return_code
