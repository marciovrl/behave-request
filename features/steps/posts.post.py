from features.modules.posts import Posts
from features.helpers.data import FakePosts


@step(u'add item Post')
def step_impl(context):
    context.posts = FakePosts()
    context.res = context.api.post(
        context.posts.titlle, context.posts.body)


@step(u'I see inserted item')
def step_impl(context):
    assert context.res.status_code == 201
