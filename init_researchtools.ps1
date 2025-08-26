# Add this script to your powershell startup script to make the scripts and
# tools in this package accessible from any directory on your system.

# Get input arguments
param(
	[string]$ProjectPath,
	[bool]$Verbose
)

# Create a PS function to call plot_json_xy.py
$PlotJSONXyScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\plot_json_xy.py"
function plot_json_xy {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$args
	)
	
	python $PlotJSONXyScriptPath @args
}

# Create a PS function to call plot_json_xy.py
$UnivPathScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\univpath"
function univpath {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$args
	)
	
	python $UnivPathScriptPath @args
}

# Success message if requested
if ($Verbose){
	Write-Output "Added ResearchTools at path:" $ProjectPath
}