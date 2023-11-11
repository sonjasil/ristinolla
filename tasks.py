from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/pelin_alku.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task
def cov_report(ctx):
    ctx.run("coverage html", pty=True)