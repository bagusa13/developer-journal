#!/usr/bin/env bash
# ==============================================================================
# Script Name   : bash_script_template.sh
# Description   : Production-grade Bash automation boilerplate with strict mode,
#                 signal traps, clean argument parsing, and structured logging.
# Author        : Mohammad Bagus Satrio (https://github.com/bagusa13)
# Repository    : developer-journal
# ==============================================================================

# Unofficial Bash Strict Mode
set -euo pipefail
IFS=$'\n\t'

# ANSI Color Codes for Terminal Output
readonly COLOR_RESET="\033[0m"
readonly COLOR_RED="\033[1;31m"
readonly COLOR_GREEN="\033[1;32m"
readonly COLOR_YELLOW="\033[1;33m"
readonly COLOR_BLUE="\033[1;34m"

# Default Variables
VERBOSE=false
DRY_RUN=false
TARGET_FILE=""
OUTPUT_DIR=""

# --- Logging Functions ---
log_info() {
    printf "${COLOR_BLUE}[INFO]${COLOR_RESET}  $(date '+%Y-%m-%d %H:%M:%S') - %s\n" "$*"
}

log_success() {
    printf "${COLOR_GREEN}[OK]${COLOR_RESET}    $(date '+%Y-%m-%d %H:%M:%S') - %s\n" "$*"
}

log_warn() {
    printf "${COLOR_YELLOW}[WARN]${COLOR_RESET}  $(date '+%Y-%m-%d %H:%M:%S') - %s\n" "$*" >&2
}

log_error() {
    printf "${COLOR_RED}[ERROR]${COLOR_RESET} $(date '+%Y-%m-%d %H:%M:%S') - %s\n" "$*" >&2
}

# --- Signal Cleanup Handler ---
cleanup() {
    local exit_code=$?
    if [[ $exit_code -ne 0 ]]; then
        log_error "Script failed with exit status code: ${exit_code}"
    fi
    # Perform temporary file removals or state cleanup here if necessary
}
trap cleanup EXIT
trap 'log_warn "Interrupted by user (SIGINT/SIGTERM)"; exit 130' INT TERM

# --- Usage Banner ---
usage() {
    cat <<EOF
Usage: $(basename "$0") -f <file> [-o <output_dir>] [-d] [-v] [-h]

Options:
  -f <file>         Target input file (Required)
  -o <output_dir>   Destination directory for generated artifacts
  -d                Dry-run mode (Simulate without applying changes)
  -v                Verbose mode (Show detailed output)
  -h                Show this help message and exit

Example:
  $(basename "$0") -f /etc/hosts -o /tmp/backup -v
EOF
    exit 2
}

# --- Argument Parsing ---
while getopts ":f:o:dvh" opt; do
    case "${opt}" in
        f) TARGET_FILE="${OPTARG}" ;;
        o) OUTPUT_DIR="${OPTARG}" ;;
        d) DRY_RUN=true ;;
        v) VERBOSE=true ;;
        h) usage ;;
        \?)
            log_error "Invalid option: -${OPTARG}"
            usage
            ;;
        :)
            log_error "Option -${OPTARG} requires an argument."
            usage
            ;;
    esac
done
shift $((OPTIND -1))

# --- Validation ---
if [[ -z "${TARGET_FILE}" ]]; then
    log_error "Missing required option: -f <file>"
    usage
fi

if [[ ! -e "${TARGET_FILE}" ]]; then
    log_error "Target file does not exist: ${TARGET_FILE}"
    exit 1
fi

# --- Main Logic ---
log_info "Starting automation routine..."
log_info "Target File : ${TARGET_FILE}"

if [[ "${DRY_RUN}" == true ]]; then
    log_warn "[DRY-RUN] Simulation mode active. No persistent modifications will be made."
fi

if [[ "${VERBOSE}" == true ]]; then
    log_info "Verbose debugging enabled."
    ls -lh "${TARGET_FILE}"
fi

# Example task execution
if [[ -n "${OUTPUT_DIR}" ]]; then
    if [[ "${DRY_RUN}" == false ]]; then
        mkdir -p "${OUTPUT_DIR}"
        log_success "Created output directory: ${OUTPUT_DIR}"
    else
        log_info "[DRY-RUN] Would create directory: ${OUTPUT_DIR}"
    fi
fi

log_success "Script finished without errors."
exit 0
