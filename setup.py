from setuptools import find_packages,setup
from typing import List

#002. CREAMOS LAS CONDICIONES PARA LLAMAR LOS PAQUETES DESDE REQUIREMENT
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """
    esta función va a retornar la lista de paquetes dentro de requirements
    """
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
           # ESTO OMITIRÁ EL "-e ." dentro de requirement.txt
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



# 001. CREAMOS EL SETUP
setup(
name="MLPROJECT2023",
version="0.0.1",
author="Kokke",
author_email="jorge.amaya.s@gmail.com",
packages=find_packages(),
# install_requires=["pandas","numpy","seaborn"]
install_requires=get_requirements("requirements.txt")




)