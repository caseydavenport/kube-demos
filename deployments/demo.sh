#!/bin/bash

. $(dirname ${BASH_SOURCE})/../util.sh

desc "Create a service that fronts any version of this demo"
run "cat $(relative svc.yaml)"
run "kubectl --namespace=demos create -f $(relative svc.yaml)"

desc "Deploy v1 of our app"
run "cat $(relative deployment.yaml)"
run "kubectl --namespace=demos create -f $(relative deployment.yaml) --validate=false"

tmux new -d -s my-session \
    "$(dirname ${BASH_SOURCE})/split1_lhs.sh" \; \
    split-window -h -d "sleep 15; $(dirname $BASH_SOURCE)/split1_rhs.sh" \; \
    attach \;
