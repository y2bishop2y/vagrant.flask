# 
# Standalone maniftest - for dev Vagrant Box.
# 
import 'lib/*.pp'

include fabric 
include git 
# include postgresql
include python
include vagrant
