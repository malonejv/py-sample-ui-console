
param
(
    [ArgumentCompleter({
        param($commandName, $parameterName, $wordToComplete, $commandAst, $fakeBoundParameters)

        # check to see whether the user already specified a parent directory...
        if ($fakeBoundParameters.ContainsKey('ParentPath'))
        {
          # if so, take that user input...
          $PackageFolder = $fakeBoundParameters['PackageFolder']
        }
        else
        {
          # ...else fall back to a default path, i.e. the windows folder
          $PackageFolder = "..\LocalPackages\"
        }

        # list all whl files
        Get-ChildItem $PackageFolder -Filter *.whl -ErrorAction Ignore | 
        Sort-Object -Property Name |
        Where-Object { $_.Name -like "$wordToComplete*" } | 
        Foreach-Object { 
          # create completionresult items:
          $pkgName = $_.BaseName
          $fileName = $_.Name
          $fullpath = $_.FullName
          [System.Management.Automation.CompletionResult]::new($pkgName, $fullpath, "ParameterValue", "$fileName`r`n")
        }
    })]  
    [string]
    # Specifies the package name
    $Package,
    [string] $PackageFolder = "..\LocalPackages\",
    [switch]$Verbose
)

if($Verbose) {
  $VerbosePreference = "Continue" 
}


$PackagePath=$PackageFolder

Write-Verbose "Validating $PackagePath exists..." 
Write-Verbose ""    
if((Test-Path $PackagePath)){

    .\venv\Scripts\deactivate.bat venv
    .\venv\Scripts\activate

    Write-Verbose "Installing package $Package..." 
    Write-Verbose ""    
    Write-Verbose "$PackagePath$Package.whl"  
    python -m pip install $PackagePath$Package.whl
}

<#
    .SYNOPSIS
    Installs a local package.

    .DESCRIPTION
        Installs a local python package passed as parameter with pip from ..\LocalPackages.

    .PARAMETER Package
    Specifies the package name.

    .EXAMPLE
    PS> install -Package "package-name"

#>