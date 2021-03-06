#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ImageFile class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ImageFile(BlockModel):
    """
    This class contains methods related the ImageFile class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Realiza a aquisição de uma imagem a " + \
            "partir de algum dispositivo, " + \
            "seja este uma mídia ou um dispositivo de " + \
            "aquisição de imagens (câmera, scanner)."
        self.label = "Image File"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Image Source"

        self.properties = [{"label": "File Name",
                            "name": "filename",
                            "type": MOSAICODE_OPEN_FILE,
                            "value":"/usr/share/mosaicode/images/lenna.png"
                            }
                           ]

        # ----------------------------C/OpenCv code-------------------------
        self.codes["declaration"] = 'IplImage * $port[output_image]$ = NULL;\n'
        self.codes["declaration"] += '$port[output_image]$ = cvLoadImage("$prop[filename]$",-1);\n'
	self.codes["execution"] = "\n"
        self.codes["cleanup"] = "cvReleaseImage(&$port[output_image]$);\n"


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
