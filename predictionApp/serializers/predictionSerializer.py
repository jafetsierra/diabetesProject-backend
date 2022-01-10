from rest_framework                     import serializers
from predictionApp.models.prediction    import Prediction
from predictionApp.models.user          import User

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = [
            'user',
            'age',
            'pregnancies',
            'glucose',
            'bloodpreassure',
            'insulin',
            'bmi',
            'tskinthickness',
            'dpedigreefunc',
            'rta',
        ]        
        
    def to_representation(self,obj):
        prediction = Prediction.objects.get(id=obj.id)
        user       = User.objects.get(id=prediction.user_id)
        return {
            'id'                : prediction.id,
            'age'               : prediction.age,
            'pregnancies'       : prediction.pregnancies,
            'glucose'           : prediction.glucose,
            'bloodpreassure'    : prediction.bloodpreassure,
            'insulin'           : prediction.insulin, 
            'bmi'               : prediction.bmi,
            'tskinthickness'    : prediction.tskinthickness,
            'dpedigreefunc'     : prediction.dpedigreefunc,
            'rta'               : prediction.rta,
            'user': {
                'id'         : user.id,
                'name'       : user.name
            }
        }