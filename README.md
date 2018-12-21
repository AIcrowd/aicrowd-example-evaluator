# aicrowd-example-evaluator

This is a basic implementation of a simple aicrowd-evaluator.
Please have a look at [example_evaluator.py](example_evaluator.py) for a sample implementation.

# Steps
* Installation
```
git clone https://github.com/AIcrowd/aicrowd-example-evaluator
cd aicrowd-example-evaluator
pip install -r requirements.txt
```
* Update the [aicrowd.json](aicrowd.json) file with the following values
  - `evaluator_name` : This is the name of your evaluator. Please use [snake casing](https://en.wikipedia.org/wiki/Snake_case) when naming the evaluator. The name also has to match the actual file containing the evaluator class. In this example, [example_evaluator.py](example_evaluator.py)
  - `evaluator_class` : This is the class name of your evaluator implemented inside [example_evaluator.py](example_evaluator.py). The class name has to follow Upper [Camel Casing](https://en.wikipedia.org/wiki/Camel_case). In this case, `ExampleEvaluator`
  - `challenge_client_name` : A value provided by the admins when your challenge is launched
  - `challenge_grader_id` : A value provided by the admins when your challenge is launched
  - `evaluation_pipeline_version` : A value ideally provided by the admins. For now, you can safely use the value `1.0`
  - `authors` : Information about the authors of the evaluator
  - `version` : version number of your evaluator

* Update the `__init__.py` file with the relevant import file. Ideally it should follow the pattern `from .[evaluator_name] import [evaluator_class]`. In this example `from .example_evaluator import ExampleEvaluator`

* Implement the actual evaluator class in `example_evaluator.py`. Do rename the file based on the value you chose for the `evaluator_name` field in `aicrowd.json`.
* Remember to add all the requirements to the `requirements.txt` file
* Add the ground_truth file(s) to the `data/` folder, and ensure to not commit the files into the repository, and instead provide them to the aicrowd admins separately.
* Add a sample submission to the `data/` folder. This is typically either your baseline submission or a random submission, and can be either force checked into the repository or provided to the admins separately.
* When we receieve an evaluator for a challenge, we will test it by running :
```
pip install -r requirements.txt
python [evaluator_name].py
```
so in your code, please ensure you have a block similar to :
```python
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

```

# Implmentation of ExampleEvaluator

You have implement an `ExampleEvaluator` class as described in the example below.

```python
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
    if you want to report back an error to the user,
    then you can simply do :
      `raise Exception("YOUR-CUSTOM-ERROR")`
     You are encouraged to add as many validations as possible
     to provide meaningful feedback to your users
    """
    _result_object = {
        "score": np.random.random(),
        "score_secondary" : np.random.random()
    }
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
    aicrowd_evaluator = ExampleEvaluator(answer_file_path, round=1)
    # Evaluate
    result = aicrowd_evaluator._evaluate(_client_payload, _context)
    print(result)
```

# Author
Sharada Mohanty <mohanty@aicrowd.com>   
