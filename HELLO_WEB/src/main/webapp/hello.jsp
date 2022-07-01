<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
	String p = request.getParameter("p");
	String a = "good morning";
	
	int pp = Integer.parseInt(p);
	
// 	String result = "";
// 	for(int i = 1; i < 10; i++){
// 		result += pp + " * " + i + "= " + (pp*i) + "<br/>";
// 	}

%>
<%=p %>단!!!!!!!!
<br/>
<%for(int i = 1; i < 10; i++){ %>
	<%=pp %> * <%=i %> = <%=(pp*i) %><br>
<%} %>

<%-- <% out.println(p + "단<br/>"); %> --%>
<%--<%
	for(int i = 1; i < 10; i++){
		out.println(pp + " * " + i + "= " + (pp*i) + "<br/>");
	}
--%>

<%-- <% out.println(result); %> --%>
</body>
</html>