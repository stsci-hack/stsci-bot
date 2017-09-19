from changebot.github_api import IssueHandler, RepoHandler

repo = RepoHandler('astropy/astropy', 'master', None)

issue = IssueHandler('astropy/astropy', '6573', None)
print(issue.labels)


