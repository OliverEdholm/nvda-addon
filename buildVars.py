# Image describer
# Config for building .nvda-addon file
# 
# Copyright (c) Oliver Edholm, 2019
# Sponsored by Klarna Bank AB
# 
# This software is licensed under the GNU General Public License 2.0. See COPYING.txt for details.
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "ImageDescriber",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Image describer"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""An extension for describing images by utilizing ML methods. Press NVDA+Control+I to get a description of an object."""),
	# version
	"addon_version" : "1.0",
	# Author(s)
	"addon_author" : u"Oliver Edholm <oliver.edholm@gmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion" : "2013.1",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion" : "2019.1"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon/globalPlugins/imageDescriber/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
