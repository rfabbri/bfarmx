# Blender Render Farm Experiments

This is a collection of unfinished scripts for setting up a Blender render farm
on a typical hybrid cluster. Use at your own risk. 

## Status

At present our script experiments are mostly based on blender's netrender
being spawned to several nodes using Python and no UI. You can reuse parts of
this, eg, to get blender to render remotely for you even on a single node.

For those who need to access a system through PBS, 
we wrote simple PBS scripts to spawn the Blender instances and setup netrender.
These have fragments of shell script so that they can also be used as a basis
for any other way of bootstrapping the blender farm.

A definitive solution is still under investigation.

## Contents

### Generally useful scripts for the main functionality

    core/Client.py           # For use in the render farm
    core/Master.py           # For use in the render farm
    core/Slave.py            # For use in the render farm

    misc/bljob               # starts a single CLI blender job, 
                             # useful for using blender with nohup etc

    These scripts start the netrender extension

### Early experiments with PBS to setup the entire farm

    pbs/farm.pbs             # Starts a Master and a Client on a control node,
                             # and Slaves on all others

    pbs/*                    # Remaining scripts to bring up blender on each node

    These are shell script fragments (warning: experimental).

### Rudimentary scripts to perform basic tasks
    misc/ls-blenders         # lists all blenders running on nodes, for debugging
    misc/startMaster.sh      # crude way of bringing up blender farm 
                             # on all nodes through shell / ssh

## Tutorial/Examples

A community-written tutorial using these experiments is available at

http://wiki.nosdigitais.teia.org.br/Blender_Farm

A (possibly out-of-sync) copy of that tutorial is available at

    Blender_Farm.wiki

In mediawiki format.

### Updating the tutorial

1) download source from the wiki over Blender_farm.wiki and run a git diff
2) carefully see if there were changes on the wiki or on the Git. If on the
wiki, just patch up those changes. If on the Git, just move original git file
back to the wiki (overwrite it)

## Authors

These early experiments were put together in parts by:

Douglas Pio, Hilton Guaraldi and Ricardo Fabbri

Polytechnic Institute at UERJ - Rio de Janeiro State University

http://pt.wikipedia.org/wiki/IPRJ

www.iprj.uerj.br

## License

GPL - see COPYING for details. We may provide a different license upon request.

Copyright (C) 2013-2015 Douglas Pio, Hilton Guaraldi and Ricardo Fabbri
