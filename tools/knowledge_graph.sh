#!/usr/bin/env bash
# Development-only Graphify environment. Never included in the game runtime.
set -euo pipefail
PROJECT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
GRAPH_ENV=${MADOROMI_GRAPHIFY_ENV:-${MADOROMI_TOOLCHAINS:-/workspace/toolchains}/graphify-venv}
case ${1:-help} in
    setup)
        python3 -m venv --system-site-packages "$GRAPH_ENV"
        "$GRAPH_ENV/bin/python" -m pip install graphifyy==0.9.102
        ;;
    build|check|query|path|explain)
        [[ -x $GRAPH_ENV/bin/python ]] || { echo 'Run tools/knowledge_graph.sh setup first.' >&2; exit 1; }
        cd "$PROJECT"
        case $1 in
            build|check) exec "$GRAPH_ENV/bin/python" tools/knowledge_graph.py "$@" ;;
            *)
                "$GRAPH_ENV/bin/python" tools/knowledge_graph.py check
                verb=$1; shift
                exec "$GRAPH_ENV/bin/graphify" "$verb" "$@" --graph "$PROJECT/docs/graph/graph.json"
                ;;
        esac
        ;;
    *) echo 'Usage: tools/knowledge_graph.sh {setup|build|check|query "question"|path "A" "B"|explain "node"}' ;;
esac
