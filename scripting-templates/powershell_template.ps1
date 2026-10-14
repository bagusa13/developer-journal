<#
.SYNOPSIS
    Production PowerShell Automation Script Template.

.DESCRIPTION
    Standardized PowerShell boilerplate designed for systems administration,
    incident triage, and automation tasks. Follows PowerShell Core / 5.1 best practices.

.PARAMETER TargetPath
    The path to the file or folder to process.

.PARAMETER OutputPath
    Optional path to write report or exported data.

.PARAMETER Force
    Overwrites destination files without prompting.

.EXAMPLE
    .\powershell_template.ps1 -TargetPath "C:\Logs" -OutputPath "C:\Reports\summary.json" -Verbose

.NOTES
    Author     : Mohammad Bagus Satrio (https://github.com/bagusa13)
    Repository : developer-journal
#>

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true, Position = 0, ValueFromPipeline = $true, HelpMessage = "Path to the target file or directory")]
    [ValidateScript({ Test-Path $_ })]
    [string]$TargetPath,

    [Parameter(Mandatory = $false)]
    [string]$OutputPath,

    [Parameter(Mandatory = $false)]
    [switch]$Force
)

# Enforce strict error handling
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Write-Log {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Message,

        [Parameter(Mandatory = $false)]
        [ValidateSet('INFO', 'SUCCESS', 'WARNING', 'ERROR')]
        [string]$Level = 'INFO'
    )

    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $colors = @{
        'INFO'    = 'Cyan'
        'SUCCESS' = 'Green'
        'WARNING' = 'Yellow'
        'ERROR'   = 'Red'
    }

    Write-Host "[$timestamp] [$Level] $Message" -ForegroundColor $colors[$Level]
}

function Main {
    Write-Log -Message "Starting automation routine..." -Level INFO
    Write-Verbose "Target Path resolved to: $(Resolve-Path $TargetPath)"

    try {
        $targetItem = Get-Item -Path $TargetPath

        if ($targetItem.PSIsContainer) {
            Write-Log -Message "Target is a directory containing $($targetItem.GetFileSystemInfos().Count) items." -Level INFO
        } else {
            Write-Log -Message "Target is a single file: $($targetItem.Name) ($($targetItem.Length) bytes)." -Level INFO
        }

        # Example action guarded by -WhatIf / SupportsShouldProcess
        if ($OutputPath) {
            if ($PSCmdlet.ShouldProcess($OutputPath, "Export audit report")) {
                $report = [PSCustomObject]@{
                    ExecutionTime = (Get-Date).ToString("o")
                    TargetName    = $targetItem.Name
                    FullPath      = $targetItem.FullName
                    Size          = if ($targetItem.PSIsContainer) { 0 } else { $targetItem.Length }
                    AuditedBy     = $env:USERNAME
                }

                $report | ConvertTo-Json -Depth 3 | Set-Content -Path $OutputPath -Encoding UTF8 -Force:$Force
                Write-Log -Message "Report successfully exported to: $OutputPath" -Level SUCCESS
            }
        }

        Write-Log -Message "Execution completed without errors." -Level SUCCESS
        exit 0

    } catch [System.Management.Automation.ItemNotFoundException] {
        Write-Log -Message "Item not found: $_" -Level ERROR
        exit 1
    } catch {
        Write-Log -Message "Fatal unexpected exception: $($_.Exception.Message)" -Level ERROR
        Write-Verbose $_.ScriptStackTrace
        exit 1
    }
}

Main
