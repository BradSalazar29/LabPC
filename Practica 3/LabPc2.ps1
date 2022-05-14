#Brad Dai Salazar Leal
do{
    $opc = Read-Host -Prompt "[1] Ver Perfil Red Actual [2] Cambiar Perfil Red Actual [3] salir "
    switch($opc){
          1 {
            Ver-PerfilRedActual

        } 2 {
            Cambiar-PerfilRedActual

        } 3 {
            Write-Host 'Estas saliendo'
        }
    }
}while ($opc -ne 3)
function Ver-PerfilRedActual{  
    $perfilRed = Get-NetConnectionProfile  
    Write-Host "Nombre de red:" $perfilRed.Name  
    Write-Host "Perfil de red:" $perfilRed.NetworkCategory  
}  

function Cambiar-PerfilRedActual{  
    $perfilRed = Get-NetConnectionProfile  
    if($perfilRed.NetworkCategory -eq "Public"){  
        Write-Host "El perfil actual es público"  
        $opc = Read-Host -Prompt "Quieres cambiar a privado? [Y] Si [N] No"  
        if($opc -eq "Y"){  
            Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Private  
            Write-Host "Perfil cambiado"  
        }  
    } else{  
        Write-Host "El perfil actual es privado"  
        $opc = Read-Host -Prompt "Quieres cambiar a público? [Y] Si [N] No"  
        if($opc -eq "Y"){  
            Set-NetConnectionProfile -Name $perfilRed.Name -NetworkCategory Public 
            Write-Host "Perfil cambiado"  
        }  
    }  
    Ver-PerfilRedActual  
}
