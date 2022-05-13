$num = Read-Host -Prompt "Dime un número"
if($num -gt 10){
    $num = Read-Host -Prompt "Dime un número que sea menor a 10"
}

for($i = 0; $i -le 10; $i++){ #$i+=1
    Write-Host $i "x" $num "=" ($i*$num)
}