from django.shortcuts import render, get_object_or_404
from django.views.generic import UpdateView, DeleteView
from main.models import Parent, User
from .forms import EditParentInfo


def my_account_view(request):
    return render(request, 'myAccount.html')


class UpdateParentView(UpdateView):
    form_class = EditParentInfo
    template_name = 'parent/edit_profile.html'
    queryset = Parent.objects.all()


    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
