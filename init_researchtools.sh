#!/usr/bin/env bash
# Source this file from ~/.bashrc or ~/.bash_profile
# Example:
#   source /path/to/research_tools.sh /abs/path/to/project true

PROJECT_PATH="$1"
VERBOSE="$2"

if [[ -z "$PROJECT_PATH" ]]; then
    echo "Error: PROJECT_PATH not provided" >&2
    return 1
fi

# Resolve absolute path (optional but safer)
PROJECT_PATH="$(cd "$PROJECT_PATH" && pwd)"

PLOT_JSON_XY_SCRIPT="$PROJECT_PATH/scripts/plot_json_xy.py"
UNIVPATH_SCRIPT="$PROJECT_PATH/scripts/univpath"
VIEW_JSON_SCRIPT="$PROJECT_PATH/scripts/view_json.py"

plot_json_xy() {
    python "$PLOT_JSON_XY_SCRIPT" "$@"
}

univpath() {
    python "$UNIVPATH_SCRIPT" "$@"
}

viewjson() {
    python "$VIEW_JSON_SCRIPT" "$@"
}

if [[ "$VERBOSE" == "true" || "$VERBOSE" == "1" ]]; then
    echo "Added ResearchTools at path: $PROJECT_PATH"
fi
