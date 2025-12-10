
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other

# Spack Project Developers. See the top-level COPYRIGHT file for details.

#

# SPDX-License-Identifier: (Apache-2.0 OR MIT)



from spack.package import *



class SpackExercise(CMakePackage):

    """Spack Exercise for Simulation Software Engineering."""



    homepage = "https://simulation-software-engineering.github.io/homepage/"

    url      = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.1.0.tar.gz"



    maintainers = ["adr1ja"]



    version("0.3.0", sha256="4b5d909f29ae06fb128d84bc13346e927517fc5e219736c57d76f3f01b3699c2")

    version("0.2.0", sha256="2d3a39f60d0092d6e382d6229971930bc68fc6d494052a6a683e3519d08e5e8a")

    version("0.1.0", sha256="772370783a388b394f1146c9867087e5b2257904fc494c8b671a9f0742111d4e")



    depends_on("boost@1.65.1:", when="@0.2.0:")

    depends_on("yaml-cpp@0.7.0:", when="@0.3.0:")

