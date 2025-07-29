import factory

from prai.models.github.user import Plan, PrivateUser, PublicUser, User


class PlanFactory(factory.Factory):
    class Meta:
        model = Plan

    collaborators = factory.Faker("random_int", min=0, max=100)
    name = factory.Faker("word")
    space = factory.Faker("random_int", min=1000, max=1000000)
    private_repos = factory.Faker("random_int", min=0, max=50)


class PrivateUserFactory(factory.Factory):
    class Meta:
        model = PrivateUser

    login = factory.Faker("user_name")
    id = factory.Faker("random_int", min=1, max=999999)
    user_view_type = None
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
    name = factory.Faker("name")
    company = factory.Faker("company")
    blog = factory.Faker("url")
    location = factory.Faker("city")
    email = factory.Faker("email")
    notification_email = factory.Faker("email")
    hireable = factory.Faker("boolean")
    bio = factory.Faker("text", max_nb_chars=200)
    twitter_username = factory.Faker("user_name")
    public_repos = factory.Faker("random_int", min=0, max=100)
    public_gists = factory.Faker("random_int", min=0, max=50)
    followers = factory.Faker("random_int", min=0, max=1000)
    following = factory.Faker("random_int", min=0, max=500)
    created_at = factory.Faker("date_time_between", start_date="-10y", end_date="now")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    private_gists = factory.Faker("random_int", min=0, max=100)
    total_private_repos = factory.Faker("random_int", min=0, max=200)
    owned_private_repos = factory.Faker("random_int", min=0, max=150)
    disk_usage = factory.Faker("random_int", min=1000, max=50000)
    collaborators = factory.Faker("random_int", min=0, max=20)
    two_factor_authentication = factory.Faker("boolean")
    plan = factory.SubFactory(PlanFactory)
    business_plus = factory.Faker("boolean")
    ldap_dn = None


class PublicUserFactory(factory.Factory):
    class Meta:
        model = PublicUser

    login = factory.Faker("user_name")
    id = factory.Faker("random_int", min=1, max=999999)
    user_view_type = None
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
    name = factory.Faker("name")
    company = factory.Faker("company")
    blog = factory.Faker("url")
    location = factory.Faker("city")
    email = factory.Faker("email")
    notification_email = factory.Faker("email")
    hireable = factory.Faker("boolean")
    bio = factory.Faker("text", max_nb_chars=200)
    twitter_username = factory.Faker("user_name")
    public_repos = factory.Faker("random_int", min=0, max=100)
    public_gists = factory.Faker("random_int", min=0, max=50)
    followers = factory.Faker("random_int", min=0, max=1000)
    following = factory.Faker("random_int", min=0, max=500)
    created_at = factory.Faker("date_time_between", start_date="-10y", end_date="now")
    updated_at = factory.Faker("date_time_between", start_date="-1y", end_date="now")
    plan = factory.SubFactory(PlanFactory)
    private_gists = factory.Faker("random_int", min=0, max=10)
    total_private_repos = factory.Faker("random_int", min=0, max=5)
    owned_private_repos = factory.Faker("random_int", min=0, max=3)
    disk_usage = factory.Faker("random_int", min=100, max=5000)
    collaborators = factory.Faker("random_int", min=0, max=5)


class UserFactory(factory.Factory):
    class Meta:
        model = User

    root = factory.SubFactory(PrivateUserFactory)

    @classmethod
    def create_private(cls, **kwargs):
        return cls(root=PrivateUserFactory(**kwargs))

    @classmethod
    def create_public(cls, **kwargs):
        return cls(root=PublicUserFactory(**kwargs))
