import os
import sys
from django.core.wsgi import get_wsgi_application
from django.utils import timezone

proj_path = "./mud_py"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mud_py.mud_py.mud_py.settings')
sys.path.append(proj_path)
os.chdir(proj_path)

application = get_wsgi_application()

from sensor.models import Sensor
from sensor.models import SensorData
from sensor.models import SensorDataUnit
from sensor.models import SensorDataType
from controlnode.models import ControlNode
from controlnode.models import ControlNodeData
from controlnode.models import ControlNodeDataType
from controlnode.models import ControlNodeUnit


def getControlNodes_All():
    return ControlNode.objects.all()
    
def getControlNodeDataType():
    return ControlNodeDataType.objects.all()
    
def getControlNodeDataType_Unit(nodeType):
       return ControlNodeDataType.objects.only('unit').get(typeName=nodeType).unit.abbreviatedName

def getControlNode_Date_TimeRange(controlNodeID,  startDateTime,  endDateTime,  nodeType):    
    return ControlNodeData.objects.filter(timestamp__range=[startDateTime, endDateTime],  node__nodeid = controlNodeID,  datatype__typeName = nodeType).order_by('timestamp')

def getSensors_All():
    return Sensor.objects.all()
    
def getSensorTypes():
    return SensorDataType.objects.all()

def getSensorDataType_Unit(sensorType):
       return SensorDataType.objects.only('unit').get(typeName=sensorType).unit.abbreviatedName
    
def getSensorData_Date_TimeRange(sensorID,  startDateTime,  endDateTime,  sensorType):    
    return SensorData.objects.filter(timestamp__range=[startDateTime, endDateTime],  sensor__sensorID = sensorID,  datatype__typeName = sensorType).order_by('timestamp')
