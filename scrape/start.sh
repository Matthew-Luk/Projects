#!/bin/bash
pids=( )

trap terminate SIGINT
terminate() {
  (( ${#pids[@]} )) && kill "${pids[@]}"
}

#the rest of your code goes here
commands=(
	"python server/server.py"
	"npm start --prefix client/"
)

for  i in ${!commands[@]}; do
  ${commands[$i]} & pids+=( "$!" )
done

for pid in "${pids[@]}"; do
  wait "$pid" || (( retval |= $? ))
done
exit "$retval"