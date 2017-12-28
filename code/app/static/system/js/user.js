

$(function(){
	
	
	/**
	 * 初始化菜单树
	 */
	$('#commonSysClassTree').tree({
		url:'commonSysClass/tree.htm',
		method:'get',
		animate:true,
		onClick: function(node){
			
			//判断是否叶子节点
			if($(this).tree('isLeaf',node.target))
			{
				siType=node.id;
				//刷新grid
				reloadgrid(siType);
				
				//启用接口管理按钮
				disableToolbar(false);
			}
		}
	});
	
	
	
	
	/**
	 * 设置datagrid
	 */
	$('#dataGrid').datagrid({
		fit : true,
		url : "/api/v1.0/userslist/1",
		border : false,
		rownumbers : true,
		singleSelect:true,
		fitColumns : true,
		pagination : true, // 允许分页
		pageSize : 20, // 重写每页显示的记录条数，默认为10
		pageList : [10,20,50,100], // 设置每页记录条数的列表
		nowrap : true,
		toolbar : tool_btns[0],
	    columns:[[
	    	{field:'id',checkbox:true},
			{
				field:'username',
				title:'用户名称',
				width:40
			},
			{
				field:'operateDt',
				title:'操作时间',
				width:90,
				formatter:function(value,rowData,rowIndex){
					return value?new Date(value).format('yyyy-MM-dd'):'<span style="color:#0A8B0A">- -</span>';
				},
				hidden:true
				
			}
		]],
		onClickRow : function(rowIndex, rowData) {
			
			commonAppSiDefineId=rowData.id;
			reloadInParamGrid(commonAppSiDefineId);
			reloadOutParamGrid(commonAppSiDefineId);
			
			
			//启用参数按钮
			disableParamToolbar(false);

		

		},
		onDblClickRow:function(rowIndex, rowData){
			doEdit();
			
		},
		pagination:true,
		loadMsg:'正在加载...'
	});
	

	
	//初始化载入
	//reloadgrid();
	
	

	
});







/**
 * 通过条件刷新grid
 */
function reloadgrid(siType) {
	
	var urlStr='system//userlist';

	
	$('#dataGrid').datagrid({
		url : urlStr
	});

	
}

/**
 * 通过条件刷新inParamGrid
 */
function reloadParamGrid(params) {
	
	$('#'+params.gridName+'').datagrid({
		url : 'commonAppSiData/list.htm?paramType='+params.paramType+'&commonAppSiDefineId='
				+ params.commonAppSiDefineId
	});
	
}

/**
 * 根据接口定义编号刷新入参数据
 * @param commonAppSiDefineId
 */
function reloadInParamGrid(commonAppSiDefineId) {
	
	//重新载入出参
	var params = {
			gridName:'inParamGrid',
			commonAppSiDefineId : commonAppSiDefineId,
			paramType:1
			};
			
	reloadParamGrid(params);
	
}

/**
 * 根据接口定义编号刷新出参数据
 * @param commonAppSiDefineId
 */
function reloadOutParamGrid(commonAppSiDefineId) {
	
	//重新载入出参
	var params = {
			gridName:'outParamGrid',
			commonAppSiDefineId : commonAppSiDefineId,
			paramType:2
			};
			
	reloadParamGrid(params);
	
}



/**
 * 查询方法
 */
function doSearch(){
	$('#chartletList').datagrid('load',{  
		nickName:$.trim($('#filterParam1').val()),
		phone:$('#filterParam2').val(),
		state:$('#filterParam3').val()
	});
}

/**
 * 清空过滤条件
 */
function doClear(){
	$('#filterParam1').val('');
	$('#filterParam2').val('');
	$('#filterParam3').val('');
}
/**
 * 新增方法
 */
function doAdd(){
	$('#add').show().dialog({
		modal:true,
		title:'新增接口定义',
		href:'jsp/app/commonAppSiDefineManager-add.jsp',
		cache:false,
		toolbar:[{
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				
				//设置当前选中节点
				//$("#webNewsTypeId").val(moduleId);
				
				$('#addForm').form('submit',{
					url:'commonAppSiDefine/create.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
						var obj = eval('('+ data +')');
						
						$('#add').dialog('close');
						showRMsg(obj.msg);
						
						//刷新grid
						reloadgrid(siType);
								
					}
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
			}
		}],
		onLoad:function(){
			$('#addForm').form('reset');

			
			var param={
					siType:siType
			};
			$('#addForm').form('load', param);
			
			
		}
	});
}

/**
 * 新增参数方法
 */
function doInParamAdd(){
	$('#add').show().dialog({
		modal:true,
		title:'新增参数定义',
		href:'jsp/app/commonAppSiDataManager-add.jsp',
		cache:false,
		toolbar:[{
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				
				$('#addForm').form('submit',{
					url:'commonAppSiData/create.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
						var obj = eval('('+ data +')');
						
						$('#add').dialog('close');
						showRMsg(obj.msg);
						
						//刷新grid
						reloadInParamGrid(commonAppSiDefineId);
								
					}
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
			}
		}],
		onLoad:function(){
			
			
			$('#addForm').form('clear');
			
			var param={
					paramType:1,
					commonAppSiDefineId:commonAppSiDefineId
			};
			$('#addForm').form('load', param);
			
			
		}
	
	});
}


/**
 * 新增返回参数方法
 */
function doOutParamAdd(){
	$('#add').show().dialog({
		modal:true,
		title:'新增返回参数定义',
		href:'jsp/app/commonAppSiDataManager-add.jsp',
		cache:false,
		toolbar:[{
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				
				$('#addForm').form('submit',{
					url:'commonAppSiData/create.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
						var obj = eval('('+ data +')');
						
						$('#add').dialog('close');
						showRMsg(obj.msg);
						
						//刷新grid
						reloadOutParamGrid(commonAppSiDefineId);
								
					}
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
			}
		}],
		onLoad:function(){
			
			
			$('#addForm').form('clear');
			
			var param={
					paramType:2,
					commonAppSiDefineId:commonAppSiDefineId
			};
			$('#addForm').form('load', param);
			
			
		}
	});
}


/**
 * 修改方法
 */
function doEdit(){
	
	//获得选择行
	var rows = $('#dataGrid').datagrid('getSelections');

	if (rows.length != 1) {
		$.messager.alert('提示', '请选择一条数据再进行修改', 'error');
		return false;
	}
	
	
	
	$('#add').show().dialog({
		modal:true,
		title:'修改接口定义',
		href:'jsp/app/commonAppSiDefineManager-add.jsp',
		cache:false,
		toolbar:[{  
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				$('#addForm').form('submit',{
					url:'commonAppSiDefine/update.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
						var obj = eval('('+ data +')');
						$('#add').dialog('close');
						
						showRMsg(obj.msg);


						//刷新grid
						reloadgrid(siType);
						
					}  
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
				
			}
		}],
		onLoad:function(){
			$('#addForm').form('load', rows[0]);

		}
	});
}

/**
 * 修改入参方法
 */
function doInParamEdit(){
	
	//获得选择行
	var rows = $('#inParamGrid').datagrid('getSelections');

	if (rows.length != 1) {
		$.messager.alert('提示', '请选择一条数据再进行修改', 'error');
		return false;
	}
	
	$('#add').show().dialog({
		modal:true,
		title:'修改入参定义',
		href:'jsp/app/commonAppSiDataManager-add.jsp',
		cache:false,
		toolbar:[{  
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				$('#addForm').form('submit',{
					url:'commonAppSiData/update.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
					
						//关闭窗口
						$('#add').dialog('close');
						
						//提示消息
						showRMsg($.parseJSON(data).msg);

						//从新载入数据
						reloadInParamGrid(commonAppSiDefineId);
						
					}  
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
				
			}
		}],
		onLoad:function(){
			$('#addForm').form('load', rows[0]);

		}
	});
}


/**
 * 修改返回参数方法
 */
function doOutParamEdit(){
	
	//获得选择行
	var rows = $('#outParamGrid').datagrid('getSelections');

	if (rows.length != 1) {
		$.messager.alert('提示', '请选择一条数据再进行修改', 'error');
		return false;
	}
	
	$('#add').show().dialog({
		modal:true,
		title:'修改入参定义',
		href:'jsp/app/commonAppSiDataManager-add.jsp',
		cache:false,
		toolbar:[{  
			text:'提交',  
			iconCls:'tick',  
			handler:function(){
				$('#addForm').form('submit',{
					url:'commonAppSiData/update.htm',
					onSubmit: function(){
						var isValid = $('#addForm').form('validate');
						if (!isValid){
							return false;	
						}
						
					},
					success:function(data){
					
						//关闭窗口
						$('#add').dialog('close');
						
						//提示消息
						showRMsg($.parseJSON(data).msg);

						//从新载入数据
						reloadOutParamGrid(commonAppSiDefineId);
						
					}  
				});
			}
		},'-',{
			text:'关闭',
			iconCls:'cancel',  
			handler:function(){
				$('#add').dialog('close');
				
			}
		}],
		onLoad:function(){
			$('#addForm').form('load', rows[0]);

		}
	});
}



/**
 * 删除方法
 */
function doDel() {
	var data = $('#dataGrid').datagrid('getChecked');
	if (!data.length == 1) {
		$.messager.alert('提示', '请选择一条数据再进行删除', 'error');
		return;
	}

	
	$.messager.confirm('提示', '确认删除吗？', function(r) {
					if (r) {
						
						$.ajax({
									url : 'commonAppSiDefine/delete.htm',
									data : {
										id : data[0].id
									},
									dataType : 'json',
									success : function(data) {
										//刷新grid
										reloadgrid(siType);
										
										showRMsg(data.msg);
										
									}
								});
					}
				});
}


/**
 * 删除方法
 */
function doInParamDel() {
	var data = $('#inParamGrid').datagrid('getChecked');
	if (!data.length == 1) {
		$.messager.alert('提示', '请选择一条数据再进行删除', 'error');
		return;
	}

	
	$.messager.confirm('提示', '确认删除吗？', function(r) {
					if (r) {
						
						$.ajax({
									url : 'commonAppSiData/delete.htm',
									data : {
										id : data[0].id
									},
									dataType : 'json',
									success : function(data) {
										
										reloadInParamGrid(commonAppSiDefineId);
										
										showRMsg(data.msg);
										
									}
								});
					}
				});
}


/**
 * 删除方法
 */
function doOutParamDel() {
	var data = $('#outParamGrid').datagrid('getChecked');
	if (!data.length == 1) {
		$.messager.alert('提示', '请选择一条数据再进行删除', 'error');
		return;
	}

	
	$.messager.confirm('提示', '确认删除吗？', function(r) {
					if (r) {
						
						$.ajax({
									url : 'commonAppSiData/delete.htm',
									data : {
										id : data[0].id
									},
									dataType : 'json',
									success : function(data) {
										
										reloadOutParamGrid(commonAppSiDefineId);
										
										showRMsg(data.msg);
										
									}
								});
					}
				});
}


 /**
  * 按回车触发查询事件
  */
function setTrack(event){
	var e = event?event:window.event;
	if(e.keyCode == 13){
		doSearch();
	}
}


