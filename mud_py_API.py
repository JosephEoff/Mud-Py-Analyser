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
from sensor.models import SensorDataType

from controlnode.models import ControlNode
from controlnode.models import ControlNodeData
from controlnode.models import ControlNodeDataType

from zone.models import Zone

def getZones():
    return Zone.objects.all()

def getControlNodes_All():
    return ControlNode.objects.all()
    
def getControlNodeDataType():
    return ControlNodeDataType.objects.all()
    
def getControlNodeDataType_Unit(nodeTypeID):
       return ControlNodeDataType.objects.only('unit').get(id=nodeTypeID).unit.abbreviatedName

def getControlNode_Date_TimeRange(controlNodeID,  startDateTime,  endDateTime,  nodeTypeID):    
    return ControlNodeData.objects.filter(timestamp__range=[startDateTime, endDateTime],  node__id = controlNodeID,  datatype__id = nodeTypeID).order_by('timestamp')

def getSensors_All():
    return Sensor.objects.all()
    
def getSensorTypes():
    return SensorDataType.objects.all()

def getSensorDataType_Unit(sensorTypeID):
       return SensorDataType.objects.only('unit').get(id=sensorTypeID).unit.abbreviatedName
    
def getSensorData_Date_TimeRange(sensorID,  startDateTime,  endDateTime,  sensorTypeID):    
    return SensorData.objects.filter(timestamp__range=[startDateTime, endDateTime],  sensor_id = sensorID,  datatype_id = sensorTypeID).order_by('timestamp')

def getZoneSensorData_Date_TimeRange(zoneID,  startDateTime,  endDateTime,  sensorTypeID):
        return SensorData.objects.filter(timestamp__range=[startDateTime, endDateTime],  zone__id = zoneID,  datatype_id = sensorTypeID).order_by('timestamp')
