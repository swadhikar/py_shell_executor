from dataclasses import dataclass


@dataclass
class Command:
    cmd: str
    result_equal: str = None
    result_contain: str = None
    result_not_contain: str = None
    result_not_equal: str = None
    fail_msg: str = None
    pass_msg: str = None
    redirect_result: str = None
    pass_return_code: int = 0
