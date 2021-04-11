from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DeleteView, DetailView
from main.models import Parent, User
from .forms import EditParentInfo


def my_account_view(request):
    return render(request, 'myAccount.html')


class MyAccountView(DetailView):
    template_name = 'myAccount.html'

    def get_object(self):
        """current_pk = self.session.pk
        session = Session.objects.get(pk=current_pk)
        print("EEeeEEEEEEEEEEEEEEEEEEEE",session)
        data = session.get_decoded()
        print("gniiiiiiiii: ", data.get('parent_id_session'))"""
        #print("00000000000",self.request.session['id_parent'])
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, user_id=id_)



class UpdateParentView(UpdateView):
    form_class = EditParentInfo
    template_name = 'parent/editprofile_parent.html'


    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, user_id=id_)



class DeleteParentView(DeleteView):

    template_name = 'parent/delete.html'
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)

    """def get_success_url(self):
        return redirect('index')"""
