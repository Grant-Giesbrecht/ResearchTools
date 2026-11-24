# Add this script to your powershell startup script to make the scripts and
# tools in this package accessible from any directory on your system.
#
# Example:
#   . "C:\Users\USERNAME\Documents\GitHub\ResearchTools\init_researchtools.ps1" -ProjectPath "C:\Users\USERNAME\Documents\GitHub\ResearchTools\" -Verbose



# Get input arguments
[CmdletBinding()]
param(
	[Parameter(Mandatory=$true)]
	[string]$ProjectPath
)

# Create a PS function to call plot_json_xy.py
$PlotJSONXyScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\plot_json_xy.py"
function plot_json_xy {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$scriptargs
	)
	
	python $PlotJSONXyScriptPath @scriptargs
}

# Create a PS function to call plot_json_xy.py
$UnivPathScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\univpath"
function univpath {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$scriptargs
	)
	
	python $UnivPathScriptPath @scriptargs
}

# Create a PS function to call plot_json_xy.py
$ViewJsonScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\view_json.py"
function viewjson {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$scriptargs
	)
	
	python $ViewJsonScriptPath @scriptargs
}

# Create a PS function to call s2p_to_Z.py
$S2pZScriptPath = Join-Path -Path $ProjectPath -ChildPath "scripts\s2p_to_Z.py"
function s2pz {
	param(
		[Parameter(ValueFromRemainingArguments=$true)]
		[string[]]$scriptargs
	)

	python $S2pZScriptPath @scriptargs
}

# Success message if requested
Write-Verbose "Added ResearchTools at path: $ProjectPath"