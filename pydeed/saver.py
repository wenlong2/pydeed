class JobSaver:
    def save_to_html(self, jobs, filename, exclude_keywords=[]):

        with open(filename, "w", encoding="utf-8") as f:
            f.write("""
<html><head><style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
}
tbody tr:nth-child(odd) {
  background-color: #fff;
}

tbody tr:nth-child(even) {
  background-color: #eee;
}
a {
text-decoration:none
}
</style><title>Job Listings</title></head><body>
            """)
            f.write("<h1>Filtered Job Posts</h1><h2>Excluding posts with keywords (case-insensitive): ")
            f.write(', '.join(exclude_keywords)+' </h2>')
            f.write("<table><tr><th>Title</th><th>Location</th><th>Salary</th><th>Days Posted</th></tr>")

            for job in jobs:
                f.write("<tr>")
                f.write(f"<td><a href='{job['link']}'>{job['title']}</a></td>")
                f.write(f"<td>{job['location']}</td>")
                f.write(f"<td>{job['salary']}</td>")
                f.write(f"<td>{job['days_posted']}</td>")
                f.write("</tr>")
            
            f.write("</table></body></html>")
        print(f"Job listings saved to {filename}")
