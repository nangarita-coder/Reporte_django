from ..models import Foro

def get_foros():
    foros = Foro.objects.all()
    return foros

def get_foro(var_pk):
    foro = Foro.objects.get(pk=var_pk)
    return foro

def update_foro(var_pk, new_var):
    foro = get_foro(var_pk)
    foro.name = new_var["name"]
    foro.save()
    return foro

def create_foro(var):
    foro = Foro(name=var["name"])
    foro.save()
    return foro