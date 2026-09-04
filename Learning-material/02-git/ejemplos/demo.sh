#!/usr/bin/env bash
# Reproduce la demo del libro de Git paso a paso.
# Corré: bash demo.sh   (crea un repo de juguete en ./proyecto)
set -e
rm -rf proyecto && mkdir proyecto && cd proyecto
git init
echo "print('hola')" > app.py
git add app.py
git commit -m "primer commit"
echo "print('hola mundo')" > app.py
echo "# Proyecto" > README.md
git add -A && git commit -m "mejorar saludo y agregar README"
git switch -c feature/login
echo "def login(): ..." >> app.py
git add -A && git commit -m "agregar login"
git switch main
git merge feature/login          # fast-forward
git log --oneline --graph --all
echo "--- listo. Mirá tambien ejemplos/salidas/ para la salida capturada ---"
