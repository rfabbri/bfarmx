# Blender Render Farm Experiments

This is a collection of unfinished scripts for setting up a Blender render farm
on a typical hybrid cluster. Use at your own risk. 

## Status

At present our script experiments are mostly based on blender's netrender
being spawned to several nodes using Python and no UI. You can reuse parts of
this, eg, to get blender to render remotely for you even on a single node.

For those who need to access a system through PBS, 
we wrote simple PBS scripts to spawn the Blender instances and setup netrender.

A definitive solution is still under investigation.

## Contents

### Generally useful scripts for the main functionality

    core/Client.py
    core/Master.py

### Early experiments with PBS to setup the entire farm

    pbs/*
    pbs/separated
    pbs/single


## Authors

These early experiments were put together in parts by:

Douglas Pio, Hilton Guaraldi and Ricardo Fabbri

Polytechnic Institute at UERJ - Rio de Janeiro State University

http://pt.wikipedia.org/wiki/IPRJ

www.iprj.uerj.br

## License

GPL - see COPYING for details. We may provide a different license upon request.

Copyright (C) 2013-2015 Douglas Pio, Hilton Guaraldi and Ricardo Fabbri
