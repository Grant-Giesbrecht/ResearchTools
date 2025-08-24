# Add this script to your powershell startup script to make the scripts and
# tools in this package accessible from any directory on your system.

# Get input arguments
param(
	[string]$ProjectPath,
	[bool]$Verbose
)

# Create a PS function to call plot_json_xy.py
function plot_json_xy {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$args
	)
	$ScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\plot_json_xy.py"
	python $ScriptPath @args
}

# Success message if requested
if ($Verbose){
	Write-Output "Added ResearchTools at path:"+$ProjectPath
}