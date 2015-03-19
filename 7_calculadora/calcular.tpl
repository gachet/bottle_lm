% include('header.tpl')
<%
	if ope=="Sumar":
		result=int(numero1)+int(numero2)
		signo="+"
	end
	if ope=="Restar":
		result=int(numero1)-int(numero2)
		signo="-"
	end
	if ope=="Multiplicar":
		result=int(numero1)*int(numero2)
		signo="*"
	end
	if ope=="Dividir":
		result=float(numero1)/float(numero2)
		signo="/"
	end	
%>
	<h3>{{numero1}} {{signo}} {{numero2}}</h3>
	<h2>Resultado:{{result}}</h2>
% include('footer.tpl')