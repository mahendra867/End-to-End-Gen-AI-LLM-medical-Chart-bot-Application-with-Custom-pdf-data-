from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'Mahendra',
    author_email= 'mahendramahesh2001@gmail.com',
    packages= find_packages(), # this find_packages looks for the __init__.py file in every folder and in whichever the folder the find_packages found this __init__.py constructer file then the find_packages consider those  folders as package , since we add this __init__.py file in the src folder, so why it is important to take src folder as package because if we conisder some folder along its respected files as package which those folder files can be able to import in anywhere in the projct workspace lets say if i would like to import the some code component from src-> helper.py code to app.py since we convert the src as package by using this setup.py  with the help of find_package parameter we can able to import the code component of src-> helper.py file code component in this way (from src.helper.py import particular_class) in the app.py file, so without converting folder as package if we want to import something file component in any where of the project workspace it will throw error module not found to prevent this error and make avialble of each file component to anywhere of the workspace we need to convert that folder as package
    install_requires = []

)