import pandas as pd
import numpy as np

class ExampleEvaluator:
  def __init__(self, answer_file_path, round=1):
    """
    `round` : Holds the round for which the evaluation is being done. 
    can be 1, 2...upto the number of rounds the challenge has.
    Different rounds will mostly have different ground truth files.
    """
    self.answer_file_path = answer_file_path
    self.round = round

  def _evaluate(self, client_payload, _context={}):
    """
    `client_payload` will be a dict with (atleast) the following keys :
      - submission_file_path : local file path of the submitted file
      - aicrowd_submission_id : A unique id representing the submission
      - aicrowd_participant_id : A unique id for participant/team submitting (if enabled)
    """
    submission_file_path = client_payload["submission_file_path"]
    aicrowd_submission_id = client_payload["aicrowd_submission_id"]
    aicrowd_participant_uid = client_payload["aicrowd_participant_id"]
    
    submission = pd.read_csv(submission_file_path)
    # Or your preferred way to read your submission

    """
    Do something with your submitted file to come up
    with a score and a secondary score.

    If you want to report back an error to the user,
    then you can simply do :
      `raise Exception("YOUR-CUSTOM-ERROR")`

     You are encouraged to add as many validations as possible
     to provide meaningful feedback to your users
    """
    _result_object = {
        "score": np.random.random(),
        "score_secondary" : np.random.random()
    }
    
    media_dir = '/tmp/'

    """
    To add media to the result object such that it shows on the challenge leaderboard:
    - Save the file at '/tmp/<filename>'
    - Add the path of the media to the result object:
        For images, add file path to _result_object["media_image_path"]
        For videos, add file path to _result_object["media_video_path"] and
                    add file path to _result_object["media_video_thumb_path"] (for small video going on the leaderboard)
    
    For example, 
    _result_object["media_image_path"] = '/tmp/submission-image.png'
    _result_object["media_video_path"] = '/tmp/submission-video.mp4'
    _result_object["media_video_thumb_path"] = '/tmp/submission-video-small.mp4'
    """
    return _result_object

if __name__ == "__main__":
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.csv
    answer_file_path = "data/ground_truth.csv"
    _client_payload = {}
    _client_payload["submission_file_path"] = "data/sample_submission.csv"
    _client_payload["aicrowd_submission_id"] = 1123
    _client_payload["aicrowd_participant_id"] = 1234
    
    # Instaiate a dummy context
    _context = {}
    # Instantiate an evaluator
    aicrowd_evaluator = ExampleEvaluator(answer_file_path)
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    print(result)
