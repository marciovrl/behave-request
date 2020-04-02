from features.helpers.api import API
from features.helpers.data import (
    create_post,
    create_token
)


@step('use endpoint "{endpoint}"')
def step_impl(context, endpoint):
    url = context.config.userdata['url'] + endpoint
    context.api = API(url)


@step('I want to read the posts')
def step_impl(context):
    context.res = context.api.get()


@step('I get the code "{code}"')
def step_impl(context, code):
    assert str(context.res.status_code) == code


@step('add item Post')
def step_impl(context):
    context.post = create_post()

    context.res = context.api.post(context.post)
