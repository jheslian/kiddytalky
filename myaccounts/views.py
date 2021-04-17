from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DeleteView, DetailView
from main.models import Parent, User, Child
from .forms import EditParentInfo
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth import logout


def my_account_view(request):
    return render(request, 'myAccount.html')


class MyAccountView(DetailView):
    template_name = 'myAccount.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, user_id=id_)


class UpdateParentView(UpdateView):
    form_class = EditParentInfo
    template_name = 'parent/editprofile_parent.html'

    """def get_success_url(self):
        id_ = self.kwargs.get("id")
        return redirect(f"/myaccount/")"""

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")

        print("USERRRRRR IDDDD", id_)
        return get_object_or_404(Parent, user_id=id_)


class DeleteParentView(DeleteView):
    template_name = 'parent/delete.html'
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        parent = Parent.objects.get(user_id=id_)

        childs = Child.objects.filter(parent_id=parent.id)
        for kid in childs:
            user = User.objects.get(id=kid.user_id)
            User.objects.filter(id=user.id).delete() #suppression de l'enfant ayant l'id parent à supprimer

        return get_object_or_404(User, id=id_)


class ParentPasswordChangeView(PasswordChangeView):
    template_name = 'parent/change_pass_parent.html'
    success_url = reverse_lazy('main:myaccounts:parent-password-succes')

    def form_valid(self, form):
        form.save()
        logout(self.request)
        self.request.session.flush()
        return super().form_valid(form)




class ParentPasswordDoneView(PasswordResetDoneView):
    template_name = 'parent/change_pass_succes.html'

