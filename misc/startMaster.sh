#!/bin/sh

echo blenders em n0:

chmod 777 scriptMaster.py scriptSlave.py scriptCliente.py pendulo.blend

myblender="blender -b -noaudio"

$myblender -P scriptMaster.py &
sleep 5
$myblender -P scriptSlave.py &
sleep 5
blender pendulo.blend -b -noaudio -o /tmp/ -F AVIJPEG -x 1 -P scriptCliente.py  &
sleep 5
ps -aux | grep $USER | grep blender | grep -v grep | grep -v ssh &

echo blenders em n1:
ssh -n n1 "$myblender -P scriptSlave.py &:sleep 10: ps -aux | grep $USER | grep blender | grep -v grep | grep -v ssh"

echo blenders em n10:
ssh -n n10 "$myblender -P scriptSlave.py &:sleep 10: ps -aux | grep $USER | grep blender | grep -v grep | grep -v ssh"

echo blenders em n11:
ssh -n n11 "$myblender -P scriptSlave.py &:sleep10: ps -aux | grep $USER | grep blender | grep -v grep | grep -v ssh"

