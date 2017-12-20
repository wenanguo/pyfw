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

    <title>新增内容</title>
</head>
<body>

	<div class="easyui-layout" data-options="fit:true">
		<div class="contactFieldset" data-options="region:'center',border:false">
			<form id="addForm" method="post">
				<table class="table" width="100%" border='0' cellspacing='0' cellpadding='1'>
					<tr>
						<td style="text-align:left;font-size:12px;">接口编码:<span style="color:red">*</span></td>
						<td>
							<input id="siService" name="siService" class="easyui-validatebox" style="width:240px;" validType="length[0,25]" required="required" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">接口名称:<span style="color:red">*</span></td>
						<td>
							<input id="siName" name="siName" class="easyui-validatebox" style="width:240px;"  validType="length[0,50]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">服务类名:<span style="color:red">*</span></td>
						<td>
							<input id="siServiceName" name="siServiceName" class="easyui-validatebox" style="width:240px;"  validType="length[0,50]" />
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">服务方法名:<span style="color:red">*</span></td>
						<td>
							<input id="siServiceMethod" name="siServiceMethod" class="easyui-validatebox" style="width:240px;"  validType="length[0,30]" />
						</td>
					</tr>
					
					<tr>
						<td style="text-align:left;font-size:12px;">模拟接口:<span style="color:red">*</span></td>
						<td>
							<input type="radio" name="siDemo" value="2" checked="checked"/>是
							<input type="radio" name="siDemo" value="1" />否
						</td>
					</tr>
					
					<tr>
						<td style="text-align:left;font-size:12px;">开启日志:<span style="color:red">*</span></td>
						<td>
							<input type="radio" name="siLogging" value="2" checked="checked"/>是
							<input type="radio" name="siLogging" value="1" />否
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">授权访问:<span style="color:red">*</span></td>
						<td>
							<input type="radio" name="siAuthAccess" value="2" checked="checked"/>是
							<input type="radio" name="siAuthAccess" value="1" />否
						</td>
					</tr>
					<tr>
						<td style="text-align:left;font-size:12px;">多行显示:<span style="color:red">*</span></td>
						<td>
							<input type="radio" name="siMultiResult" value="2" checked="checked"/>是
							<input type="radio" name="siMultiResult" value="1" />否
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
					 <input type="hidden" id="siType" name="siType" value="1">
					 <input type="hidden" id="id" name="id" value=""> 
			</form>
		</div>
	</div>
</body>