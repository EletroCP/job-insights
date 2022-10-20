from src import jobs


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    file_content = jobs.read(path)
    data = []
    for row in file_content:
        if row['job_type'] not in data:
            data.append(row['job_type'])
    return data


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    if job_type == '':
        return []
    filter_job = []
    for job in jobs:
        if job_type in job['job_type']:
            filter_job.append(job)
    return filter_job


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    file_content = jobs.read(path)
    data = []
    for row in file_content:
        if row['industry'] not in data and row['industry'] != '':
            data.append(row['industry'])
    return data


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    if industry == '':
        return []
    filter_industry = []
    for job in jobs:
        if industry in job['industry']:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    file_content = jobs.read(path)
    data = [
        int(info["max_salary"])
        for info in file_content
        if info["max_salary"].isnumeric()
    ]
    return max(data)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    file_content = jobs.read(path)
    data = [
        int(info["min_salary"])
        for info in file_content
        if info["min_salary"].isnumeric()
    ]
    return min(data)


def chec_job(job):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
    ):
        return False
    return True


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (
        not chec_job(job)
        or int(job["min_salary"] > job["max_salary"])
        or not isinstance(salary, int)
    ):
        raise ValueError()
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def check_job_range(job, salary):
    try:
        if matches_salary_range(job, salary):
            return job

    except ValueError:
        return None


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return [
        check_job_range(job, salary)
        for job in jobs
        if check_job_range(job, salary) is not None
    ]
