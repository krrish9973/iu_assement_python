from database import session
from iu_assement_python.src.models.training_data import TrainingData
from iu_assement_python.src.models.ideal_function import IdealFunction
from iu_assement_python.src.models.test_data import TestData

class AddTrainingDataToDB:
    def add_data(self,data):
        for index, row in data.iterrows():
            session.add(TrainingData(x=row['x'], y1=row['y1'], y2=row['y2'], y3=row['y3'], y4=row['y4']))
        session.commit()
        session.close()

class AddIdealFunctionsToDB:
    def add_data(self,data):
        for index, row in data.iterrows():
            session.add(IdealFunction(
                x=row['x'],
                y1=row['y1'], y2=row['y2'], y3=row['y3'], y4=row['y4'], y5=row['y5'], y6=row['y6'],
                y7=row['y7'], y8=row['y8'], y9=row['y9'], y10=row['y10'], y11=row['y11'],
                y12=row['y12'], y13=row['y13'], y14=row['y14'], y15=row['y15'], y16=row['y16'],
                y17=row['y17'], y18=row['y18'], y19=row['y19'], y20=row['y20'], y21=row['y21'],
                y22=row['y22'], y23=row['y23'], y24=row['y24'], y25=row['y25'], y26=row['y26'],
                y27=row['y27'], y28=row['y28'], y29=row['y29'], y30=row['y30'], y31=row['y31'],
                y32=row['y32'], y33=row['y33'], y34=row['y34'], y35=row['y35'], y36=row['y36'],
                y37=row['y37'], y38=row['y38'], y39=row['y39'], y40=row['y40'], y41=row['y41'],
                y42=row['y42'], y43=row['y43'], y44=row['y44'], y45=row['y45'], y46=row['y46'],
                y47=row['y47'], y48=row['y48'], y49=row['y49'], y50=row['y50']
            ))
            session.commit()
            session.close()

class AddMappedTestDataToDB:
    def add_data(self,data):
        for row in data:
            session.add(TestData(x=row['x'], y=row['y'], ideal_function_id=row['ideal_function_id'],
                                 deviation=row['deviation']))
        session.commit()
        session.close()