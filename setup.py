import setuptools

setuptools.setup(
    name="cifar10_models",
    version="1.0.0",
    python_requires=">3.6",
    author="Huy Phan",
    author_email="",
    description="pytorch implementation of various models on cifar10",
    packages=setuptools.find_packages(),
    install_requires=["torch", "torchvision", "tqdm"],
    tests_require=[],
    classifiers=["Programming Language :: Python",],
)
