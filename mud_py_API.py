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


def getSensors_All():
    return Sensor.objects.all()
    
def getSensorTypes():
    return SensorDataType.objects.all()
    
