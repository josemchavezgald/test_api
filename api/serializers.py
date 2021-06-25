from rest_framework import serializers
from .models import Mesa,Tablero,Patas,Tornillo



class TableroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tablero
		fields = [
			'largo','ancho','espesor'
		]
class PatasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patas
		fields = [
			'largo','ancho','espesor','cantidad'
		]

class TornilloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tornillo
		fields = [
			'largo','diametro','cantidad'
		]

class FlatMesaSerializer(serializers.ModelSerializer):

	tablero = TableroSerializer(read_only=True)
	patas = PatasSerializer(read_only=True)
	tornillos = TornilloSerializer(read_only=True)

	class Meta:
		model=Mesa
		fields=['tablero','patas','tornillos','created_at']

class MesaSerializer(serializers.ModelSerializer):

	tablero = TableroSerializer()
	patas = PatasSerializer()
	tornillos = TornilloSerializer()

	created_at = serializers.SerializerMethodField(read_only=True)

	def get_created_at(self,obj):
		data = obj.created_at
		data_result = {
			'anio': data.year,
			'mes': data.month,
			'dia': data.day
		}

		return data_result

	class Meta:
		model = Mesa
		fields = [
			'tablero','patas','tornillos','created_at'
		]

	