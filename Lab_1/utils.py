import pandas as pd
from datetime import datetime

def save_submission(submission: pd.DataFrame, output_path: str) -> None:

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    submission.to_csv(output_path + f"sub_{timestamp}.csv", index=False)
