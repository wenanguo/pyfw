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
<title>接口定义</title>
<jsp:include page="../../resources/page/inc.jsp"></jsp:include>
<script type="text/javascript" src="jsp/app/js/commonAppSiDefineManager.js"></script>
<script type="text/javascript">
			
var tool_btns = 
{
'0' : ['-',
{id:"btn_add",text:"新增",iconCls:"book_add",disabled:false,handler:function(){doAdd();}},'-',
{id:"btn_edit",text:"修改",iconCls:"book_edit",disabled:false,handler:function(){doEdit();}},'-',
{id:"btn_del",text:"删除",iconCls:"book_delete",disabled:false,handler:function(){doDel();}},'-'
],
'1' : ['-',
{id:"btn_inparam_add",text:"新增",iconCls:"book_add",disabled:false,handler:function(){doInParamAdd();}},'-',
{id:"btn_inparam_edit",text:"修改",iconCls:"book_edit",disabled:false,handler:function(){doInParamEdit();}},'-',
{id:"btn_inparam_del",text:"删除",iconCls:"book_delete",disabled:false,handler:function(){doInParamDel();}},'-'
],
'2' : ['-',
{id:"btn_outparam_add",text:"新增",iconCls:"book_add",disabled:false,handler:function(){doOutParamAdd();}},'-',
{id:"btn_outparam_edit",text:"修改",iconCls:"book_edit",disabled:false,handler:function(){doOutParamEdit();}},'-',
{id:"btn_outparam_del",text:"删除",iconCls:"book_delete",disabled:false,handler:function(){doOutParamDel();}},'-'
]

};
		</script>

</head>
<body class="easyui-layout" data-options="fit:true">

  	<input id='basePath' style="display:none;" value="<%=basePath%>" />
    	
	    
	   <div data-options="region:'west',split:true" title="模块" style="width:200px;">
	   <ul class="easyui-tree" style="padding:10px;fit:true;border:0px" id="commonSysClassTree" ></ul>
	   </div>
	   
    	<div data-options="region:'center',border:false">
    	
	    	<div class="easyui-layout" data-options="fit:true,border:false">
	    	
		    	<div data-options="region:'north',border:false" style="height:400px">
		    		<table id="dataGrid"></table>
			    	<div id="add" title="新增" style="width:600px;height:585px;"></div>
		    	</div>
		    	
		    	<div data-options="region:'center',border:false">
		
					<div class="easyui-tabs" data-options="border:false,fit:true">
						<div title="请求参数定义" >
							<table id="inParamGrid"></table>
						</div>
						<div title="返回参数定义" >
							<table id="outParamGrid"></table>
						</div>
					</div>
				</div>
	    	
	    	</div>
    	
	    </div>
	    
	    
	    
	

</body>
</html>