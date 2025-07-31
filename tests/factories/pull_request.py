import factory

from prai.models.github import PullRequestGet
from prai.models.github.pull_request__get import (
    SimpleUser,
    Label,
    Milestone,
    TeamSimple,
    LicenseSimple,
    Permissions,
    Repository,
    Repository1,
    Head,
    Base,
    Link,
    FieldLinks,
    AutoMerge,
    CodeSearchIndexStatus,
)


class SimpleUserFactory(factory.Factory):
    """Factory for SimpleUser model."""

    class Meta:
        model = SimpleUser

    name = factory.Faker("name")
    email = factory.Faker("email")
    login = factory.Faker("user_name")
    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDQ6VXNlcjE=")
    avatar_url = factory.Faker("url")
    gravatar_id = factory.Faker("md5")
    url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}")
    html_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.login}")
    followers_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/followers")
    following_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/users/{obj.login}/following{{/other_user}}"
    )
    gists_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/gists{{/gist_id}}")
    starred_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/users/{obj.login}/starred{{/owner}}{{/repo}}"
    )
    subscriptions_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/subscriptions")
    organizations_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/orgs")
    repos_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/repos")
    events_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/events{{/privacy}}")
    received_events_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/users/{obj.login}/received_events")
    type = "User"
    site_admin = False
    starred_at = None
    user_view_type = "public"


class LabelFactory(factory.Factory):
    """Factory for Label model."""

    class Meta:
        model = Label

    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDU6TGFiZWwxMDg5NDA5Ng==")
    url = factory.Faker("url")
    name = factory.Faker("word")
    description = factory.Faker("sentence")
    color = factory.Faker("color")
    default = False


class MilestoneFactory(factory.Factory):
    """Factory for Milestone model."""

    class Meta:
        model = Milestone

    url = factory.Faker("url")
    html_url = factory.Faker("url")
    labels_url = factory.Faker("url")
    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDk6TWlsZXN0b25lMTAwMjYwNA==")
    number = factory.Faker("random_int", min=1, max=999)
    state = "open"
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("sentence")
    creator = factory.SubFactory(SimpleUserFactory)
    open_issues = factory.Faker("random_int", min=0, max=20)
    closed_issues = factory.Faker("random_int", min=0, max=20)
    created_at = factory.Faker("date_time_between", start_date="-2y", end_date="-1y")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    closed_at = None
    due_on = factory.Faker("date_time_between", start_date="now", end_date="+1y")


class TeamSimpleFactory(factory.Factory):
    """Factory for TeamSimple model."""

    class Meta:
        model = TeamSimple

    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDQ6VGVhbTE=")
    url = factory.Faker("url")
    members_url = factory.Faker("url")
    name = factory.Faker("company")
    description = factory.Faker("sentence")
    permission = "pull"
    privacy = "closed"
    notification_setting = "notifications_enabled"
    html_url = factory.Faker("url")
    repositories_url = factory.Faker("url")
    slug = factory.Faker("slug")
    ldap_dn = None


class LicenseSimpleFactory(factory.Factory):
    """Factory for LicenseSimple model."""

    class Meta:
        model = LicenseSimple

    key = "mit"
    name = "MIT License"
    url = "https://api.github.com/licenses/mit"
    spdx_id = "MIT"
    node_id = factory.Faker("lexify", text="MDc6TGljZW5zZW1pdA==")
    html_url = "https://opensource.org/licenses/MIT"


class PermissionsFactory(factory.Factory):
    """Factory for Permissions model."""

    class Meta:
        model = Permissions

    admin = False
    pull = True
    triage = True
    push = False
    maintain = False


class CodeSearchIndexStatusFactory(factory.Factory):
    """Factory for CodeSearchIndexStatus model."""

    class Meta:
        model = CodeSearchIndexStatus

    lexical_search_ok = True
    lexical_commit_sha = factory.Faker("sha1")


class RepositoryFactory(factory.Factory):
    """Factory for Repository model."""

    class Meta:
        model = Repository

    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDEwOlJlcG9zaXRvcnkxMjk2MjY5")
    name = factory.Faker("word")
    full_name = factory.LazyAttribute(lambda obj: f"{obj.owner.login}/{obj.name}")
    license = factory.SubFactory(LicenseSimpleFactory)
    forks = factory.Faker("random_int", min=0, max=100)
    permissions = factory.SubFactory(PermissionsFactory)
    owner = factory.SubFactory(SimpleUserFactory)
    private = False
    html_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.full_name}")
    description = factory.Faker("sentence")
    fork = False
    url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}")
    archive_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/{{archive_format}}{{/ref}}"
    )
    assignees_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/assignees{{/user}}"
    )
    blobs_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/blobs{{/sha}}")
    branches_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/branches{{/branch}}"
    )
    collaborators_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/collaborators{{/collaborator}}"
    )
    comments_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/comments{{/number}}"
    )
    commits_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/commits{{/sha}}")
    compare_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/compare/{{base}}...{{head}}"
    )
    contents_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/contents/{{+path}}")
    contributors_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/contributors")
    deployments_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/deployments")
    downloads_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/downloads")
    events_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/events")
    forks_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/forks")
    git_commits_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/commits{{/sha}}"
    )
    git_refs_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/refs{{/sha}}")
    git_tags_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/tags{{/sha}}")
    git_url = factory.LazyAttribute(lambda obj: f"git:github.com/{obj.full_name}.git")
    issue_comment_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues/comments{{/number}}"
    )
    issue_events_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues/events{{/number}}"
    )
    issues_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues{{/number}}")
    keys_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/keys{{/key_id}}")
    labels_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/labels{{/name}}")
    languages_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/languages")
    merges_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/merges")
    milestones_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/milestones{{/number}}"
    )
    notifications_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/notifications{{?since,all,participating}}"
    )
    pulls_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/pulls{{/number}}")
    releases_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/releases{{/id}}")
    ssh_url = factory.LazyAttribute(lambda obj: f"git@github.com:{obj.full_name}.git")
    stargazers_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/stargazers")
    statuses_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/statuses/{{sha}}")
    subscribers_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/subscribers")
    subscription_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/subscription")
    tags_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/tags")
    teams_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/teams")
    trees_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/trees{{/sha}}")
    clone_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.full_name}.git")
    mirror_url = None
    hooks_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/hooks")
    svn_url = factory.LazyAttribute(lambda obj: f"https://svn.github.com/{obj.full_name}")
    homepage = factory.Faker("url")
    language = "Python"
    forks_count = factory.Faker("random_int", min=0, max=100)
    stargazers_count = factory.Faker("random_int", min=0, max=1000)
    watchers_count = factory.Faker("random_int", min=0, max=1000)
    size = factory.Faker("random_int", min=100, max=50000)
    default_branch = "main"
    open_issues_count = factory.Faker("random_int", min=0, max=50)
    is_template = False
    topics = []
    has_issues = True
    has_projects = True
    has_wiki = True
    has_pages = False
    has_downloads = True
    has_discussions = False
    archived = False
    disabled = False
    visibility = "public"
    pushed_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    created_at = factory.Faker("date_time_between", start_date="-5y", end_date="-1y")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    allow_rebase_merge = True
    temp_clone_token = None
    allow_squash_merge = True
    allow_auto_merge = False
    delete_branch_on_merge = False
    allow_update_branch = False
    use_squash_pr_title_as_default = False
    squash_merge_commit_title = None
    squash_merge_commit_message = None
    merge_commit_title = None
    merge_commit_message = None
    allow_merge_commit = True
    allow_forking = True
    web_commit_signoff_required = False
    open_issues = factory.Faker("random_int", min=0, max=50)
    watchers = factory.Faker("random_int", min=0, max=1000)
    master_branch = None
    starred_at = None
    anonymous_access_enabled = None
    code_search_index_status = factory.SubFactory(CodeSearchIndexStatusFactory)


class Repository1Factory(factory.Factory):
    """Factory for Repository1 model (base repository)."""

    class Meta:
        model = Repository1

    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDEwOlJlcG9zaXRvcnkxMjk2MjY5")
    name = factory.Faker("word")
    full_name = factory.LazyAttribute(lambda obj: f"{obj.owner.login}/{obj.name}")
    license = factory.SubFactory(LicenseSimpleFactory)
    forks = factory.Faker("random_int", min=0, max=100)
    permissions = factory.SubFactory(PermissionsFactory)
    owner = factory.SubFactory(SimpleUserFactory)
    private = False
    html_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.full_name}")
    description = factory.Faker("sentence")
    fork = False
    url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}")
    archive_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/{{archive_format}}{{/ref}}"
    )
    assignees_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/assignees{{/user}}"
    )
    blobs_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/blobs{{/sha}}")
    branches_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/branches{{/branch}}"
    )
    collaborators_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/collaborators{{/collaborator}}"
    )
    comments_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/comments{{/number}}"
    )
    commits_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/commits{{/sha}}")
    compare_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/compare/{{base}}...{{head}}"
    )
    contents_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/contents/{{+path}}")
    contributors_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/contributors")
    deployments_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/deployments")
    downloads_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/downloads")
    events_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/events")
    forks_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/forks")
    git_commits_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/commits{{/sha}}"
    )
    git_refs_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/refs{{/sha}}")
    git_tags_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/tags{{/sha}}")
    git_url = factory.LazyAttribute(lambda obj: f"git:github.com/{obj.full_name}.git")
    issue_comment_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues/comments{{/number}}"
    )
    issue_events_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues/events{{/number}}"
    )
    issues_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/issues{{/number}}")
    keys_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/keys{{/key_id}}")
    labels_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/labels{{/name}}")
    languages_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/languages")
    merges_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/merges")
    milestones_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/milestones{{/number}}"
    )
    notifications_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.full_name}/notifications{{?since,all,participating}}"
    )
    pulls_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/pulls{{/number}}")
    releases_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/releases{{/id}}")
    ssh_url = factory.LazyAttribute(lambda obj: f"git@github.com:{obj.full_name}.git")
    stargazers_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/stargazers")
    statuses_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/statuses/{{sha}}")
    subscribers_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/subscribers")
    subscription_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/subscription")
    tags_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/tags")
    teams_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/teams")
    trees_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/git/trees{{/sha}}")
    clone_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.full_name}.git")
    mirror_url = None
    hooks_url = factory.LazyAttribute(lambda obj: f"https://api.github.com/repos/{obj.full_name}/hooks")
    svn_url = factory.LazyAttribute(lambda obj: f"https://svn.github.com/{obj.full_name}")
    homepage = factory.Faker("url")
    language = "Python"
    forks_count = factory.Faker("random_int", min=0, max=100)
    stargazers_count = factory.Faker("random_int", min=0, max=1000)
    watchers_count = factory.Faker("random_int", min=0, max=1000)
    size = factory.Faker("random_int", min=100, max=50000)
    default_branch = "main"
    open_issues_count = factory.Faker("random_int", min=0, max=50)
    is_template = False
    topics = []
    has_issues = True
    has_projects = True
    has_wiki = True
    has_pages = False
    has_downloads = True
    has_discussions = False
    archived = False
    disabled = False
    visibility = "public"
    pushed_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    created_at = factory.Faker("date_time_between", start_date="-5y", end_date="-1y")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    allow_rebase_merge = True
    temp_clone_token = None
    allow_squash_merge = True
    allow_auto_merge = False
    delete_branch_on_merge = False
    allow_update_branch = False
    use_squash_pr_title_as_default = False
    squash_merge_commit_title = None
    squash_merge_commit_message = None
    merge_commit_title = None
    merge_commit_message = None
    allow_merge_commit = True
    allow_forking = True
    web_commit_signoff_required = False
    forks = factory.Faker("random_int", min=0, max=100)
    open_issues = factory.Faker("random_int", min=0, max=50)
    watchers = factory.Faker("random_int", min=0, max=1000)
    master_branch = None
    starred_at = None
    anonymous_access_enabled = None
    code_search_index_status = factory.SubFactory(CodeSearchIndexStatusFactory)


class HeadFactory(factory.Factory):
    """Factory for Head model."""

    class Meta:
        model = Head

    label = factory.LazyAttribute(lambda obj: f"{obj.user.login}:{obj.ref}")
    ref = factory.Faker("word")
    repo = factory.SubFactory(RepositoryFactory)
    sha = factory.Faker("sha1")
    user = factory.SubFactory(SimpleUserFactory)


class BaseFactory(factory.Factory):
    """Factory for Base model."""

    class Meta:
        model = Base

    label = factory.LazyAttribute(lambda obj: f"{obj.user.login}:{obj.ref}")
    ref = "main"
    repo = factory.SubFactory(Repository1Factory)
    sha = factory.Faker("sha1")
    user = factory.SubFactory(SimpleUserFactory)


class LinkFactory(factory.Factory):
    """Factory for Link model."""

    class Meta:
        model = Link

    href = factory.Faker("url")


class FieldLinksFactory(factory.Factory):
    """Factory for FieldLinks model."""

    class Meta:
        model = FieldLinks

    comments = factory.SubFactory(LinkFactory)
    commits = factory.SubFactory(LinkFactory)
    statuses = factory.SubFactory(LinkFactory)
    html = factory.SubFactory(LinkFactory)
    issue = factory.SubFactory(LinkFactory)
    review_comments = factory.SubFactory(LinkFactory)
    review_comment = factory.SubFactory(LinkFactory)
    self = factory.SubFactory(LinkFactory)


class AutoMergeFactory(factory.Factory):
    """Factory for AutoMerge model."""

    class Meta:
        model = AutoMerge

    enabled_by = factory.SubFactory(SimpleUserFactory)
    merge_method = "merge"
    commit_title = factory.Faker("sentence")
    commit_message = factory.Faker("text", max_nb_chars=200)


class PullRequestGetFactory(factory.Factory):
    """Factory for PullRequestGet model."""

    class Meta:
        model = PullRequestGet

    url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/pulls/{obj.number}"
    )
    id = factory.Faker("random_int", min=1, max=999999)
    node_id = factory.Faker("lexify", text="MDExOlB1bGxSZXF1ZXN0MQ==")
    html_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.base.repo.full_name}/pull/{obj.number}")
    diff_url = factory.LazyAttribute(lambda obj: f"https://github.com/{obj.base.repo.full_name}/pull/{obj.number}.diff")
    patch_url = factory.LazyAttribute(
        lambda obj: f"https://github.com/{obj.base.repo.full_name}/pull/{obj.number}.patch"
    )
    issue_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/issues/{obj.number}"
    )
    commits_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/pulls/{obj.number}/commits"
    )
    review_comments_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/pulls/{obj.number}/comments"
    )
    review_comment_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/pulls/comments{{/number}}"
    )
    comments_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/issues/{obj.number}/comments"
    )
    statuses_url = factory.LazyAttribute(
        lambda obj: f"https://api.github.com/repos/{obj.base.repo.full_name}/statuses/{obj.head.sha}"
    )
    number = factory.Faker("random_int", min=1, max=9999)
    state = "open"
    locked = False
    title = factory.Faker("sentence", nb_words=4)
    user = factory.SubFactory(SimpleUserFactory)
    body = factory.Faker("text", max_nb_chars=500)
    labels = []
    milestone = None
    active_lock_reason = None
    created_at = factory.Faker("date_time_between", start_date="-1y", end_date="-1w")
    updated_at = factory.Faker("date_time_between", start_date="-1w", end_date="now")
    closed_at = None
    merged_at = None
    merge_commit_sha = None
    assignee = None
    assignees = []
    requested_reviewers = []
    requested_teams = []
    head = factory.SubFactory(HeadFactory)
    base = factory.SubFactory(BaseFactory)
    _links = factory.SubFactory(FieldLinksFactory)
    author_association = "OWNER"
    auto_merge = None
    draft = False
    merged = False
    mergeable = True
    rebaseable = True
    mergeable_state = "clean"
    merged_by = None
    comments = factory.Faker("random_int", min=0, max=20)
    review_comments = factory.Faker("random_int", min=0, max=10)
    maintainer_can_modify = True
    commits = factory.Faker("random_int", min=1, max=50)
    additions = factory.Faker("random_int", min=0, max=1000)
    deletions = factory.Faker("random_int", min=0, max=500)
    changed_files = factory.Faker("random_int", min=1, max=20)
