import requests
import re
from app.semver_utils import sort_versions_semver

# GitHub REST API endpoint template
GITHUB_API = "https://api.github.com/repos/{owner}/{repo}/releases"

# Regex pattern to match tarball assets for Airflow
TARBALL_PATTERN = re.compile(r"apache[-_]airflow-(\d+\.\d+\.\d+)\.tar\.gz")

def get_release_deltas(owner, repo, start_tag, end_tag):
    url = GITHUB_API.format(owner=owner, repo=repo)
    releases = requests.get(url).json()

    tarballs = []

    # Iterate over all GitHub releases and extract tarball assets
    for release in releases:
        tag = release["tag_name"].lstrip("v")

        # Only process the first matching tarball per release
        for asset in release.get("assets", []):
            name = asset["name"]
            match = TARBALL_PATTERN.match(name)
            if match:
                tarballs.append({
                    "tag": tag,
                    "size": asset["size"]
                })
                break  # Exit after the first matching .tar.gz

    # Sort releases using semantic versioning
    sorted_releases = sort_versions_semver(tarballs)

    # Compute deltas between releases within the selected version range
    delta_list = []
    recording = False
    for i in range(1, len(sorted_releases)):
        prev = sorted_releases[i - 1]
        curr = sorted_releases[i]

        if curr["tag"] == start_tag.lstrip("v"):
            recording = True

        if recording:
            delta = curr["size"] / prev["size"]
            delta_list.append({
                "previous_tag": prev["tag"],
                "tag": curr["tag"],
                "delta": delta
            })

        if curr["tag"] == end_tag.lstrip("v"):
            break

    return delta_list