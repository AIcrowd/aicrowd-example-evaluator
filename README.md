# aicrowd-example-evaluator

This is a basic implementation of a simple aicrowd-evaluator.
Please have a look at [evaluator.py](evaluator.py) for a sample implementation.

# Steps
* Installation
```
git clone https://github.com/AIcrowd/aicrowd-example-evaluator
cd aicrowd-example-evaluator
pip install -r requirements.txt
```
* Update the [aicrowd.yaml](aicrowd.yaml) file with the following values
  - `challenge.name` : This is the name of your challenge.
  - `challenge.template` : This is the name of the template being used by us to create the evaluator. Do not change its value from `simple-evaluator`
  - `challenge.authors` : Information about the authors of the evaluator
  - `challenge.version` : Version number of your evaluator


* Implement the actual evaluator class in `evaluator.py`. Do not rename the file or the evaluator class `AIcrowdEvaluator`.
* Remember to add all the requirements to the `requirements.txt` file
* Add the ground_truth file(s) to the `data/` folder, and ensure to not commit the files into the repository, and instead provide them to the aicrowd admins separately.
* Add a sample submission to the `data/` folder. This is typically either your baseline submission or a random submission, and can be either force checked into the repository or provided to the admins separately.
* When we receieve an evaluator for a challenge, we will test it by running :
```
pip install -r requirements.txt
python evaluator.py
```
so in your code, please ensure you have a block similar to:

```python
if __name__ == "__main__":
    # Lets assume the the ground_truth is a CSV file
    # and is present at data/ground_truth.csv
    # and a sample submission is present at data/sample_submission.csv
    ground_truth_path = "data/ground_truth.csv"
    _client_payload = {}
    _client_payload["submission_file_path"] = "data/sample_submission.csv"
    _client_payload["aicrowd_submission_id"] = 1234
    _client_payload["aicrowd_participant_id"] = 1234
    
    # Instaiate a dummy context
    _context = {}

    # Instantiate an evaluator
    aicrowd_evaluator = AIcrowdEvaluator(ground_truth_path)
    
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    print(result)

```

# Implementation of ExampleEvaluator

You have implement an `AIcrowdEvaluator` class as described in the example below.

```python
import pandas as pd
import numpy as np

class AIcrowdEvaluator:
  def __init__(self, ground_truth_path, **kwargs):
    """
    This is the AIcrowd evaluator class which will be used for the evaluation.
    Please note that the class name should be `AIcrowdEvaluator`
    `ground_truth` : Holds the path for the ground truth which is used to score the submissions.
    """
    self.ground_truth_path = ground_truth_path

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
    
    """
    You can also add a private_score and private_score_secondary.
    The private scores will be relvealed only when the challenge gets over.

    To do so, simple add them to the "meta" field of the _result_object like:
    
    _result_object["meta"] = {
        "private_score" = np.random.random(),
        "private_score_secondary" = np.random.random()
    }
    """
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


    assert "score" in _result_object
    assert "score_secondary" in _result_object

    return _result_object

```

# Author
Sharada Mohanty <mohanty@aicrowd.com>   
