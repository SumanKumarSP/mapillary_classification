# Author: Raphael Delhome
# Organization: Oslandia
# Date: september 2017

# Mapillary data set reading

import json
import logging
import os
import sys

import utils

##################
# Transform the image into input data
# Input data: np.array of shape [2448, 3264, 3]
# 18000, 2000 and 5000 images respectively for training, validation and
# testing set
##################
# Transform the labelled image into output data
# Output data: an array of 66 0-1 values, 1 if the i-th Mapillary object is
# on the image, 0 otherwise
# np.array of shape [18000, 66] for training set, and [2000, 66] for
# validation set

utils.logger.info("Read config file...")
# read in config file
with open('data/config.json') as config_file:
    config = json.load(config_file)
labels = config['labels']

utils.logger.info("Mapillary image size inventory...")
utils.mapillary_image_sizes = size_inventory()
utils.mapillary_image_sizes.to_csv("data/mapillary_image_sizes.csv")
utils.mapillary_image_size_plot(mapillary_image_sizes,
                          "../images/mapillary_image_sizes.png")

utils.logger.info("Mapillary data preparation...")
utils.mapillary_data_preparation("training", len(labels))
utils.mapillary_data_preparation("validation", len(labels))
utils.mapillary_data_preparation("testing", len(labels))

utils.logger.info("Mapillary output checking...")
utils.mapillary_output_checking("training", len(labels))
utils.mapillary_output_checking("validation", len(labels))
