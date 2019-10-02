from features.modules.posts import Posts


@step(u'use endpoint posts')
def step_impl(context):
    context.api = Posts(context.config.userdata['url'])


@step(u'I want to read the posts')
def step_impl(context):
    context.res = context.api.get()


@step(u'I get all items registered posts')
def step_impl(context):
    assert context.res.status_code == 200
