from ghp_import import ghp_import
ghp_import(
    srcdir='jupyterbooks/_build/html',
    push=True,
    nojekyll=True,
    force=True,
    no_history=True
    )
