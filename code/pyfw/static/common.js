/*Show Notification*/
function Notify(message, position, timeout, theme, icon, closable) {
    toastr.options.positionClass = 'toast-' + position;
    toastr.options.extendedTimeOut = 0; //1000;
    toastr.options.timeOut = timeout;
    toastr.options.closeButton = closable;
    toastr.options.iconClass = icon + ' toast-' + theme;
    toastr[theme](message);
}


// /**
//  * 将表单序列化为对象
//  * @returns {{}}
//  */
// $.fn.serializeObject = function() {
//         var o = {};
//         var a = this.serializeArray();
//         $.each(a, function() {
//             if (o[this.name]) {
//                 if (!o[this.name].push) {
//                     o[this.name] = [ o[this.name] ];
//                 }
//                 o[this.name].push(this.value || '');
//             } else {
//                 o[this.name] = this.value || '';
//             }
//         });
//         return o;
// }



/**
 * 将form里面的内容序列化成json
 * 相同的checkbox用分号拼接起来
 * @param {dom} 指定的选择器
 * @param {obj} 需要拼接在后面的json对象
 * @method serializeJson
 * */
$.fn.serializeJson=function(otherString){
  var serializeObj={},
    array=this.serializeArray();
  $(array).each(function(){
    if(serializeObj[this.name]){
      serializeObj[this.name]+=';'+this.value;
    }else{
      serializeObj[this.name]=this.value;
    }
  });

  if(otherString!=undefined){
    var otherArray = otherString.split(';');
    $(otherArray).each(function(){
      var otherSplitArray = this.split(':');
      serializeObj[otherSplitArray[0]]=otherSplitArray[1];
    });
  }
  return serializeObj;
};

/**
 * 将josn对象赋值给form
 * @param {dom} 指定的选择器
 * @param {obj} 需要给form赋值的json对象
 * @method serializeJson
 * */
$.fn.setForm = function(jsonValue){
  var obj = this;
  $.each(jsonValue,function(name,ival){
    var $oinput = obj.find("input[name="+name+"]");
    if($oinput.attr("type")=="checkbox"){
      if(ival !== null){
        var checkboxObj = $("[name="+name+"]");
        var checkArray = ival.split(";");
        for(var i=0;i<checkboxObj.length;i++){
          for(var j=0;j<checkArray.length;j++){
            if(checkboxObj[i].value == checkArray[j]){
              checkboxObj[i].click();
            }
          }
        }
      }
    }
    else if($oinput.attr("type")=="radio"){
      $oinput.each(function(){
        var radioObj = $("[name="+name+"]");
        for(var i=0;i<radioObj.length;i++){
          if(radioObj[i].value == ival){
            radioObj[i].click();
          }
        }
      });
    }
    else if($oinput.attr("type")=="textarea"){
      obj.find("[name="+name+"]").html(ival);
    }
    else{
      obj.find("[name="+name+"]").val(ival);
    }
  })
}


/**
 * 过滤jquery serialize方法获取表单空值问题
 * @param serStr
 */
function serializeNotNull(serStr){
    return serStr.split("&").filter(function(str){return !str.endsWith("=")}).join("&");
}