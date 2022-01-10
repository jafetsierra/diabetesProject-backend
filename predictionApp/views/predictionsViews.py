from django.conf                       import settings
from rest_framework                    import generics, status, views
from rest_framework.response           import Response
from rest_framework.permissions        import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from predictionApp.models.prediction                import Prediction
from predictionApp.serializers.predictionSerializer import PredictionSerializer
from predictionApp.models.user                      import User
from predictionApp.XGB                              import make_prediction

class PredictionCreateView(generics.CreateAPIView):
    queryset           = Prediction.objects.all()
    serializer_class   = PredictionSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        print(request,'\n',kwargs)
        
        if valid_data['user_id'] != kwargs['fk']:#request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        #XGB prediction on data
        print('\n'*2,request.data,'\n'*2,type(request.data['prediction_data']['bmi']))
        request.data['prediction_data']['user_id'] = kwargs['fk']
        rta = make_prediction(request.data['prediction_data'])
        
        serializer = PredictionSerializer(data=rta)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(rta, status=status.HTTP_201_CREATED)

        
class ListPredictionsViews(generics.ListAPIView):
    serializer_class   = PredictionSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Prediction.objects.filter(user_id=self.kwargs['user'])
        return queryset