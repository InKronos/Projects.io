import os
from sys import path
from django.db import models
from django.http.response import JsonResponse
#from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Projects, RatingProject
from users.models import Users
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from django.db.models import Avg
from .serializers import *


class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset =  Projects.objects.all()
   

    serializer_class = ProjectAuthorizeSerializer
    def retrieve(self, request, pk=None):
        item = Projects.objects.get(pk = pk)
        return Response({"Project": ProjectAuthorizeSerializer(item).data, "Meneger": Users.objects.filter(pk = item.idOwner.pk).first().name})

    def byTitle(self, request, title = "", *args, **kwargs):
      queryset =  Projects.objects.filter(title__contains=str(title))
      return Response(ProjectAuthorizeSerializer(queryset, many = True).data)

   # @action(detail=True,methods=['DELETE'])
    def destroy(self, request,pk=None, **kwargs):
      Projects.objects.filter(pk=pk,idOwner_id =int(request.user.id)).delete()
      return Response()

    def create(self, request, **kwargs):
      data = request.data
      
      datapath = str(request.user.id)+"/"+data.get("title")+"/"+"data"
      presentationpath = str(request.user.id)+"/"+data.get("title")+"/"+"presentation"
      os.makedirs("./FileBase/"+datapath)
      os.makedirs("./FileBase/"+presentationpath)
      p =Projects( idOwner_id = request.user.id,title=data.get("title"),description=data.get("description"),folder=datapath,presentation =presentationpath)
      p.save()
      return Response()

    def update(self, request, pk=None, *args, **kwargs):
        p = Projects.objects.filter(pk=pk).first()
        data = request.data
        if(p.idOwner_id ==int(request.user.id)):
          p.title = data.get("title",p.title)
          p.description = data.get("description",p.description)
          newstage =data.get("stage",p.stage)
          if newstage =="BS":
            p.stage =  Projects.ProjectStages.BRAINSTORM
          elif newstage =="EB":
            p.stage =  Projects.ProjectStages.EARLYBIRD
          elif newstage =="PG":
            p.stage =  Projects.ProjectStages.PlayGround
          p.save()
        return Response(ProjectAuthorizeSerializer(p).data)

          

    def partial_update(self, request, pk=None, *args, **kwargs):
         return Response({"detail": "Niedozwolona metoda \"PATCH\"."})
          
    @action(detail=True,methods=['POST'])
    def mark(self, request,pk=None, **kwargs):
        if request.method == 'POST':
          data = request.data
        
        
        
          RatingProject.objects.update_or_create(idProject_id = int(pk),
                                      idUser_id =int(request.user.id),
                                      defaults = {'mark':  data.get("mark",None)} )


          
        mark =RatingProject.objects.filter(idProject_id = pk).aggregate(avg_mark = Avg('mark'))
        Projects.objects.filter(pk = pk).update(averageRate = mark['avg_mark'])
        return Response()

    def list(self, request, *args, **kwargs):

      sorting = request.GET.get('sort',"")
      title_contain =  request.GET.get('titlecontain',"")
      desc_contain = request.GET.get('descecontain',"")
      up =  request.GET.get('up',"")
      down =  request.GET.get('down',0)
      queryset = Projects.objects.all()
      if not title_contain == "":
        queryset = queryset.filter(title__icontains=str(title_contain))
      
      if (not desc_contain ==""):
          queryset = queryset.filter(decription__icontains=str(desc_contain))

      if (not sorting == ""):
        queryset = queryset.order_by(sorting)

      if not up == "" and down =="": 
        queryset = queryset[int(down):int(up)]

      projects = [ {"Project": ProjectUnAuthorizeSerializer(item).data, "Meneger":Users.objects.filter(pk = item.idOwner.pk).first().name} for item in queryset ]
      return Response(projects)
        
    def get_queryset(self):
        return  Projects.objects.all()

   #def perform_create(self, serializer):
    #    return serializer.save(owner=self.request.user)



#class ProjectViewSet(viewsets.ModelViewSet):
 #   permission_classes = [permissions.AllowAny]
 #   queryset =  Projects.objects.get(pk = id)

 #   serializer_class = ProjectSerializer