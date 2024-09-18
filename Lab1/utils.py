import pandas as pd
from datetime import datetime
from typing import Optional

def save_submission(submission: pd.DataFrame, output_path: str, additional_name: Optional[str]=None) -> None:

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if additional_name:
        file_name = f"sub_{additional_name}_{timestamp}.csv"
    else:
        file_name = f"sub_{timestamp}.csv"
    submission.to_csv(output_path + file_name, index=False)


def preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["Unnamed: 0", "Case_ID"])

    df = df.replace({"--": None, "not reported": None})
    df = df.fillna(-1)

    df["Age_at_diagnosis"] = df["Age_at_diagnosis"].apply(lambda x: int(x.split(" ")[0]) if isinstance(x, str) else x)
    return df
