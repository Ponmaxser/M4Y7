from django.core.exceptions import PermissionDenied

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()

        if task.owner != request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)