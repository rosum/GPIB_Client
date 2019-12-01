import setuptools


setuptools.setup(
     name='gpib_client',
     version='1.0',
     scripts=['gpib_client'] ,
     author="Jan Rosum",
     author_email="jrosum1996@gmail.com",
     description="A Python Client for the GPIB RESTful Service",
     long_description="A Python Client for the GPIB RESTful Service",
     long_description_content_type="text",
     url="https://gitlab.janrosum.com/root/gpib_client",
     packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )