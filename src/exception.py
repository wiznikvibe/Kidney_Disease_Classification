import sys 
from src.logger import logging

def error_message_details(error, error_details: sys):
    _, _, exec_tb = error_details.exc_info()
    filename = exec_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script {filename}, line_number: {exec_tb.tb_lineno}, Error Message: {str(error)}"
    return error_message

class CustomException(Exception):

    def __init__(self, error_message, error_details:sys):

        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message
