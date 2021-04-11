from django.shortcuts import get_object_or_404, reverse, redirect
from django.views.generic import UpdateView, DetailView, DeleteView, CreateView, ListView
from .forms import EditChildInfo, ChildRegistrationForm
from main.models import Child, User, Parent
from crum import get_current_user




class ChildListView(ListView):
    template_name = 'mykids.html'

    #e = get_current_user()
    #print("HOME CRUMMMMMM", e.id)

    def get_queryset(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        queryset = Child.objects.all().filter(parent_id=id_)
        return queryset

    """    def get(self, request, *args):
        request.GET.get('id')

        print("TTTTTTT", request.GET.get('id') )
        print("TTTTAAAATTT", self.request.session['id_parent'])

        return super(ChildListView, self).get(request, *args)"""



class MyChildView(DetailView):
    template_name = 'childview.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, id=id_)


class UpdateChildView(UpdateView):
    form_class = EditChildInfo
    template_name = 'editprofile_enfant.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, id=id_)

    def get_success_url(self):
        return reverse('main:mykids:kids')


class DeleteChildView(DeleteView):
    model = Child
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Child, user_id=id_)

    def get_success_url(self):
        return redirect('main:mykids:kids')


class ChildRegisterView(CreateView):
    model = User
    form_class = ChildRegistrationForm
    template_name = 'child/child_register.html'

    def form_valid(self, form):

        form.save()
        return redirect('main:mykids:childregister')
        """print('id user: ', id_)
        parent = Parent.objects.get(user_id=id_)
        print('Objet user: ', parent)
        print("id du parent: ", parent.id)"""
        # Child.parent_id = parent.id
        #  child = Child.objects.create(parent_id=parent.id)
        # child = Child.parent_id
        # print("child object",child)
        # child.save()

    """ def get_context_data(self):
        context = super().get_context_data()
        id_ = self.request.session['id_parent']
        parent = Parent.objects.get(user_id=id_)
        child = self.request.child
        context["parent_id"] = parent.objects.all()
        return context"""
