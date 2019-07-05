from features.helpers.api_posts import POSTS

@given(u'use endpoint posts')
def step_impl(context):
    context.api = POSTS()


@when(u'add item Post')
def step_impl(context):
    context.res = context.api.post("API Testing", "Example testing API with Python")

@then(u'I see inserted item')
def step_impl(context):
    assert context.res.status_code == 200