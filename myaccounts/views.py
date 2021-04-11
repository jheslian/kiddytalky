from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DeleteView, DetailView
from main.models import Parent, User
from .forms import EditParentInfo
from django.contrib.sessions.models import Session
from django.core.cache import cache
from accounts.forms import ParentRegistrationForm

#a = session_data('.eJxVjDsOgzAQRO_iOrL8wZilTJ8zWLt4HUgigwxUUe4eI1Ek3WjmzXuLgPs2hn3lEqYoemHF5bcjHJ6cjyE-MN9nOcx5KxPJA5HnusrbHPl1Pdk_wYjrWN_YsNJtZ1LrEpNHTQQQa4KElMAQWGd9YyOqZNAb1mDA06Cp6ZyzqkqnGBYsnDfR288XLhg8nA:1lVF0v:5e8QVAy1o8IFjfWcjwgYKcSquY9oqFWwMo5FlPCYGxg')
#print("FFDGD",a.get_decoded())


def my_account_view(request):
    return render(request, 'myAccount.html')


class MyAccountView(DetailView):

    # session = Session.objects.get(pk='bq5cinqbmqgru14xay54yy67q12fpipw')
    # print('BBBBBBBBB', session.get_decoded())

    template_name = 'myAccount.html'

    def get_object(self):
        """current_pk = self.session.pk
        session = Session.objects.get(pk=current_pk)
        print("EEeeEEEEEEEEEEEEEEEEEEEE",session)
        data = session.get_decoded()
        print("gniiiiiiiii: ", data.get('parent_id_session'))"""
        id_ = self.kwargs.get("id")
        return get_object_or_404(Parent, id=id_)



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
        return get_object_or_404(Parent, user_id=id_)

    """def get_success_url(self):
        return redirect('index')"""
