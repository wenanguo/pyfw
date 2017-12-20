<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<!DOCTYPE html>
<html>
<head>
<base href="<%=basePath%>">
<title>黔聚软件</title>
<jsp:include page="../../resources/page/inc.jsp"></jsp:include>
<script type="text/javascript" src="jsp/news/js/newsManager.js"></script>

    <title>新增参数</title>
</head>
<body>

	<div class="easyui-layout" data-options="fit:true">
		<div class="contactFieldset" data-options="region:'center',border:false">
			<form id="addForm" method="post">
				<table class="table" width="100%" border='0' cellspacing='0' cellpadding='1'>
					<tr>
						<td style="text-align:left;font-size:12px;">参数名称:<span style="color:red">*</span></td>
						<td>
							<input id="dataName" name="dataName" class="easyui-validatebox" style="width:240px;" validType="length[0,25]" required="required" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">参数标题:<span style="color:red">*</span></td>
						<td>
							<input id="dataTitle" name="dataTitle" class="easyui-validatebox" style="width:240px;"  validType="length[0,25]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">数据类型:<span style="color:red">*</span></td>
						<td>
							<input id="dataType" name="dataType" class="easyui-validatebox" style="width:240px;"  validType="length[0,25]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">表达式:<span style="color:red">*</span></td>
						<td>
							<input id="dataPattern" name="dataPattern" class="easyui-validatebox" style="width:240px;"  validType="length[0,25]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">默认值:<span style="color:red">*</span></td>
						<td>
							<input id="dataDefaultVal" name="dataDefaultVal" class="easyui-validatebox" style="width:240px;"  validType="length[0,25]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">状态:<span style="color:red">*</span></td>
						<td>
							<input type="radio" name="status" value="100" checked="checked"/>启用
							<input type="radio" name="status" value="104" />停用
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">备注:<span style="color:red">*</span></td>
						<td>
							<textarea  id="memo" name="memo" style="width:240px; height:100px" type="text">
							
						    </textarea> 
						   
						</td>
					</tr>
					</table>
					
					 <input type="hidden" id="commonAppSiDefineId" name="commonAppSiDefineId" value="1">
					 <input type="hidden" id="paramType" name="paramType" value="1">
					 <input type="hidden" id="id" name="id" value=""> 
			</form>
		</div>
	</div>
</body>