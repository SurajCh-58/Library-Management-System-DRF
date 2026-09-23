# Library-Management-System-DRF

This is a simple DRF CRUD project that I built to revise URL routing, serializers, serializer validation, and how to reuse the same validation logic for multiple model attributes by passing arguments such as `queryset`, `field_name`, etc.

I also learned how `requires_context=True` works in `apps/common/utils.py`. It is used when the validator needs access to the serializer field and its parent serializer, which allows the validator to get information such as the model field name.

The project is divided into three separate apps:

* `books`
* `members`
* `borrowing`

## Current limitation

There is currently one limitation in the member API. Any user can send a `GET` request and see all registered members instead of only seeing their own profile.

This is because I have not implemented authentication and authorization yet. I plan to fix this later when authentication is added.

For example, after authentication is implemented, I can use `get_queryset()` in the view to return only the currently logged-in user's profile:

```python
def get_queryset(self):
    return Member.objects.filter(user=self.request.user)
```

Here, `self.request.user` represents the currently logged-in user, so the user will only be able to access their own profile.

## Django Admin

I also learned the basics of Django Admin customization in this project, including:

* `list_display`
* `list_filter`
* Admin actions
* Creating custom admin actions to update member status
