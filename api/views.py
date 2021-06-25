from django.shortcuts import render
from rest_framework import viewsets,filters,status
from rest_framework.response import Response
from .models import Mesa,Tornillo,Tablero,Patas
from .serializers import MesaSerializer,TableroSerializer, TornilloSerializer, PatasSerializer,FlatMesaSerializer
from django.db.models import Sum
from .variables import get_meses, get_mes


class MesaView(viewsets.ModelViewSet):
	serializer_class = MesaSerializer
	queryset = Mesa.objects.all().order_by('created_at') 

	def create(self,request):
		data = request.data

		print(data)
		data_tablero = data['tablero']
		data_patas = data['patas']
		data_tornillos = data['tornillos']

		tablero = Tablero.objects.create(**data_tablero)
		patas = Patas.objects.create(**data_patas)
		tornillos = Tornillo.objects.create(**data_tornillos)

		mesa = Mesa.objects.create(tablero=tablero,patas=patas,tornillos=tornillos)

		return Response(status=status.HTTP_201_CREATED)
		
class DataRelevanteView(viewsets.ModelViewSet):

	serializer_class = FlatMesaSerializer
	queryset = Mesa.objects.all().order_by('created_at')

	def get_cantidad_tornillos(self):

		cantidad =Tornillo.objects.all().aggregate(total=Sum('cantidad'))['total'] 
		if cantidad == None:
			cantidad = 0

		return cantidad

	def get_cantidad_patas(self):

		cantidad = Patas.objects.all().aggregate(total=Sum('cantidad'))['total'] 
		if cantidad == None:
			cantidad = 0

		return cantidad

	def get_cantidad_mesas(self):

		cantidad =len(Mesa.objects.all())

		return cantidad

	def get_mesas_por_mes(self,meses):

		#Inicialice algunos valores para poder mostrar gráfico en frontend.
		data_mes_mesas = {
			1:10,
			2:2,
			3:20,
			4:8,
			5:5,
			6:0,
			7:0,
			8:0,
			9:0,
			10:0,
			11:0,
			12:0
		}

		mesas = Mesa.objects.all()

		for mesa in mesas:
			mes = mesa.created_at.month
			data_mes_mesas[mes] += 1

		data_result = []

		for i in range(1,13):
			data = {
				'mes': meses[i],
				'cantidad':data_mes_mesas[i]
			}

			data_result.append(data)

		return data_result

	def get_cantidad_mesas_mes(self,mes_actual):
		
		contador = 0
		
		mesas = Mesa.objects.all()

		for mesa in mesas:

			mes = mesa.created_at.month

			if(mes == mes_actual):
				contador+=1

		return contador


	def list(self,request,*args,**kwargs):
		response = super().list(request,*args,**kwargs)

		mes_actual = get_mes()

		meses = get_meses()

		response.data = {
			'cantidad_tornillos': self.get_cantidad_tornillos(),
			'cantidad_patas': self.get_cantidad_patas(),
			'cantidad_mesas': self.get_cantidad_mesas(),
			'mesas_por_mes': self.get_mesas_por_mes(meses),
			'cantidad_mesas_mes':{
				'mes': meses[mes_actual],
				'cantidad': self.get_cantidad_mesas_mes(mes_actual)
			}
		}

		return response

