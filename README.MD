# Business Requirement

## Make an automation pipeline for my analytics team report that should answer question like:

1. Which programming languages are trending?
2. Which repositories are getting the most stars?
3. Which owners created the most popular repositories?
4. How many repositories were created each day?
5. Which repositories crossed 1000 stars?

## Data Required:

| Fields | Why it's needed |
| :--- | :--- |
| **languages** | To know name of programming languages |
| **language % in each repo** | To check language trend |
| **repository** | To know name of repository |
| **stars_count** | To keep track for stars on each repo |
| **owner_name** | To know name of repo owners |
| **created_at** | To know when a repo is created (Date, Time) |


## Possible GitHub Endpoint:

1. GET /search/repositories
    GET /search/repositories needs:

    q required
    Optional headers:
    Accept: application/vnd.github+json
    Optional query parameters:

    sort
    stars
    forks
    help-wanted-issues
    updated
    order
    desc
    asc
    per_page
    max 100
    page

# Final Output:
Every morning 9:00 AM a new report should be triggered to Team members via mail.