import pandas as pd

data=[
  {
    "id": 1,
    "name": "Alice",
    "grades": [
      {"subject": "Math", "marks": {"mid": 80, "final": 90}},
      {"subject": "Science", "marks": {"mid": 85, "final": 95}}
    ]
  }
]

df=pd.json_normalize(data, record_path=['grades'], meta=['id', 'name'], record_prefix='grade_')
print(df)