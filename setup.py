from setuptools import setup

package_name = 'ros2_cam_openCV'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bjorn',
    maintainer_email='bjoern.ellensohn@gmail.com',
    description='Using OpenCV to publish UVC camera stream (should be fast?)',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_node = ros2_cam_openCV.cam_node:main'
        ],
    },
)
