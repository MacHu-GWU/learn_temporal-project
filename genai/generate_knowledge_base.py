# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

from docpack.github_fetcher import GitHubPipeline

dir_repo = Path.home().joinpath("Documents", "GitHub", "temporal-documentation")
dir_here = Path(__file__).absolute().parent
dir_tmp = dir_here / "tmp"
shutil.rmtree(dir_tmp, ignore_errors=True)
dir_tmp.mkdir()

gh_pipeline = GitHubPipeline(
    domain="github.com",
    account="temporalio",
    repo="documentation",
    branch="main",
    dir_repo=dir_repo,
    include=[
        "README.rst",
        "docs/cli/**/*.md",
        "docs/cli/**/*.mdx",
        "docs/develop/python/**/*.md",
        "docs/develop/python/**/*.mdx",
        "docs/encyclopedia/**/*.md",
        "docs/encyclopedia/**/*.mdx",
        "docs/evaluate/**/*.md",
        "docs/evaluate/**/*.mdx",
        "docs/references/**/*.md",
        "docs/references/**/*.mdx",
        "docs/troubleshooting/**/*.md",
        "docs/troubleshooting/**/*.mdx",
        "docs/*.md",
        "docs/*.mdx",
    ],
    exclude=[
        "docs/encyclopedia/nexus*.mdx",
    ],
    dir_out=dir_tmp,
)
gh_pipeline.fetch()
path_knowledge_base = dir_here / "learn_temporal_knowledge_base.xml"
lines = list()
for path in dir_tmp.glob("*.xml"):
    lines.append(path.read_text())
path_knowledge_base.write_text("\n".join(lines))
