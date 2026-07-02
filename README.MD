# GitHub ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline built in Python that fetches trending GitHub repository data, transforms it into an analytics-friendly format, and generates business reports.

---

# Project Overview

The analytics team requires daily reports to understand GitHub repository trends.

This pipeline automatically:

- Fetches repository data from the GitHub REST API
- Stores the raw JSON response
- Transforms nested JSON into a flat tabular format
- Generates business reports
- Maintains execution logs

---

# Business Requirement

Generate reports that answer the following questions:

1. Which programming languages are trending?
2. Which repositories are getting the most stars?
3. Which owners created the most popular repositories?
4. How many repositories were created each day?
5. Which repositories crossed 1000 stars?

---

# GitHub API

**Endpoint**

```
GET /search/repositories
```

Current query parameters:

```python
PARAMS = {
    "q": "is:public",
    "sort": "stars",
    "order": "desc",
    "page": 1,
    "per_page": 100
}
```

---

# Project Structure

```
github-etl/
│
├── config/
│   └── config.py
│
├── extract/
│   └── github_extract.py
│
├── transform/
│   └── github_transform.py
│
├── report/
│   └── github_report.py
│
├── utils/
│   ├── logger.py
│   ├── save_json.py
│   └── save_csv.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── logs/
│
├── main.py
│
└── README.md
```

---

# ETL Workflow

```
GitHub API
      │
      ▼
Extract
      │
      ▼
Raw JSON
(data/raw)
      │
      ▼
Transform
(json_normalize)
      │
      ▼
Processed CSV
(data/processed)
      │
      ▼
Generate Reports
      │
      ▼
reports/
      │
      ▼
Execution Logs
(logs/)
```

---

# Generated Reports

The pipeline generates the following reports:

- Trending Programming Languages
- Top Starred Repositories
- Top Repository Owners
- Repositories Created Each Day
- Repositories With More Than 1000 Stars

---

# Output

## Raw Data

```
data/raw/
```

Stores the original GitHub API response in JSON format.

Example:

```
github_2026-07-02.json
```

---

## Processed Data

```
data/processed/
```

Stores the flattened repository dataset in CSV format.

Example:

```
github_2026-07-02.csv
```

---

## Reports

```
reports/
```

Example:

```
github_trending_languages_2026-07-02.csv

github_top_repositories_2026-07-02.csv

github_top_owners_2026-07-02.csv

github_repositories_created_each_day_2026-07-02.csv

github_repositories_above_1000_stars_2026-07-02.csv
```

---

## Logs

```
logs/
```

Example:

```
github_2026-07-02.log
```

Sample:

```
Pipeline started.
Data fetched successfully.
Raw JSON saved.
Processed CSV saved.
Reports generated successfully.
Pipeline completed.
```

---

# Technologies Used

- Python 3
- Requests
- Pandas
- Pathlib
- Datetime
- GitHub REST API

---

# How to Run

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd github-etl
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python main.py
```

---

# Future Improvements

- Schedule pipeline execution using Cron or Airflow
- Load processed data into PostgreSQL
- Send reports automatically via email
- Dockerize the application
- Add unit tests
- CI/CD using GitHub Actions

---

# Author

**Deepesh Sabran**

Built to demonstrate ETL pipeline development using Python, Pandas, and the GitHub REST API.