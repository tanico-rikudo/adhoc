import os
from enum import Enum
from  .exception import InvalidEnvError

class Env(Enum):
    DEV = 1
    UAT = 2
    PROD = 3
    
class Util: 

    @classmethod
    def get_env_string(cls):
        hostname = os.uname()[1]
        if hostname in ["tkfrksvd1"]:
            return Env.DEV
        elif hostname in ["tkfrksvt1"]:
            return Env.UAT
        elif hostname in ["tkfrksvp1"]:
            return Env.PROD
        else:
            return None
            # InvalidEnvError("Invalid environment")
