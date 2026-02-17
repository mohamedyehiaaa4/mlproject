import sys
try:
    from src.logger import logger
except ModuleNotFoundError:
    from logger import logger


def error_message_details(error, error_detail=sys):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"Error message: [{str(error)}]"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"error message: [{str(error)}]"
    )


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        self.error_message = error_message_details(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logger.exception("Divide by zero error")
        raise CustomException(e, sys) from e
