import boto3
import os
import subprocess
import logging
from helpers import  update_route_field
logging.basicConfig(level=logging.INFO)

def blurVideo(file_name):
    logging.info(f'blurring started for file -> {file_name}')
    dim_file_name = f'dim_{file_name}'
    dimenstion_command = ['ffmpeg', '-i', f'inputs/{file_name}', '-s', '608x1088', f'inputs/{dim_file_name}']
    command = ['deface', f'inputs/{dim_file_name}', '-o', f'blurred/{file_name}']
    try:
        logging.info('Changing dimenstion...')
        result_dim = subprocess.run(dimenstion_command, check=True, capture_output=True, text=True)
        logging.info("Command Output result_dim:", result_dim.stdout)
        logging.info("Command Error Output result_dim:", result_dim.stderr)
        logging.info('blurring...')
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info("Command Output:", result.stdout)
        logging.info("Command Error Output:", result.stderr)
        return True
    except Exception as e:
        logging.info('Error in blur proecss')
        logging.info(e)
        try:     
            update_route_field(route_id, 'processStatus', 'BLUR_ERROR')
        except Exception as e:
            logging.info('Error while updating the Database about the error')
            logging.info(e)
        return False
    finally:
        os.remove(f'inputs/{file_name}')
        os.remove(f'inputs/{dim_file_name}')


# if __name__ == "__main__":
#     blurVideo('dubai_small_vid.mp4')
#     logging.info('done')
