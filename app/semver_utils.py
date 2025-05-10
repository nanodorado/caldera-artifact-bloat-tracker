import semver

def sort_versions_semver(releases):
    # Sort a list of releases by semantic versioning
    return sorted(releases, key=lambda x: semver.VersionInfo.parse(x["tag"]))