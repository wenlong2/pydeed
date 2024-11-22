class JobFilter:
    def __init__(self, exclude_keywords):
        self.exclude_keywords = exclude_keywords

    def filter(self, job_posts):
        filtered_jobs = []
        for job in job_posts:
            if not any(keyword.lower() in job["text"].lower() for keyword in self.exclude_keywords):
                filtered_jobs.append(job)
        return filtered_jobs
