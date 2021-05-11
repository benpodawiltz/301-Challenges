## Author Ben Podawiltz
## Date: 5.10.21
## Revision:
## Purpose: Add a new user to active directory


###################################################

# Variables

$NewUser = Read-Host "Please Enter New User Name [First Last]"
$LogOnName = Read-Host "Please Enter LogOn Name"
$Password = Read-Host "Please Enter Password" -AsSecureString
$Email = Read-Host "Please Enter Email Address"
$Department = Read-Host "Please Enter Department"
$Title = Read-Host "Please Enter Job Title"
$Company = Read-Host "Please Enter Company Name"
$City = Read-Host "Please Enter City"
$State = Read-Host "Please Enter a State"

#####################################################

$Principal = $LogOnName + $Domain
$Domain = "@corp.globexpower.com"

#####################################################

# Function

New-ADUser -Name $NewUser -SamAccountName $LogOnName -UserPrincipalName $Principal -EmailAddress $Email -Title $Title -Company $Company -Department $Department -City $City -State $State
-AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) -Enabled $True -ChangePasswordAtLogon $true



#####################################################

# Sources: https://docs.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps



#End	
 
