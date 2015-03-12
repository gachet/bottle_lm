<!DOCTYPE html>
<html lang="es">
<head>
<title>Tabla</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Tabla de multiplicar del {{numero}}</h1>
    </header>
    <ul>
    % for n in xrange(1,11):
    % resultado = n * int(numero)
      <li> {{n}} * {{numero}} = {{resultado}}</li>
    % end
    </ul>    
</body>
</html>