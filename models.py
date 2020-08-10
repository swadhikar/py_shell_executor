from dataclasses import dataclass


@dataclass
class Command:
    cmd: str
    fail_if_result_equals: str = None
    fail_if_result_contains: str = None
    fail_if_result_not_equals: str = None
    fail_msg: str = None
    success_msg: str = None
    send_result_execute: str = None
    success_return_code: int = 0
