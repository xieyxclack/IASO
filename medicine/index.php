<?php
// +----------------------------------------------------------------------
// | ThinkPHP [ WE CAN DO IT JUST THINK ]
// +----------------------------------------------------------------------
// | Copyright (c) 2006-2014 http://thinkphp.cn All rights reserved.
// +----------------------------------------------------------------------
// | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
// +----------------------------------------------------------------------
// | Author: liu21st <liu21st@gmail.com>
// +----------------------------------------------------------------------

// 应用入口文件

// 检测PHP环境
if(version_compare(PHP_VERSION,'5.3.0','<'))  die('require PHP > 5.3.0 !');

// 开启调试模式 建议开发阶段开启 部署阶段注释或者设为false
define('APP_DEBUG',true);

//zlz：所有路径常量均以'/'结尾
// 定义应用目录
define('APP_PATH','./Application/');
//定义安全文件
define('DIR_SECURE_FILENAME', 'index.html');
//定义缓存目录zlz：运行时目录
define('RUNTIME_PATH' , dirname(__FILE__).'/Runtime/' );
define('COMMON_CONFIG_PATH' , dirname(__FILE__).'/Application/Common/Conf/' );
// 引入ThinkPHP入口文件
require './ThinkPHP/ThinkPHP.php';

// 亲^_^ 后面不需要任何代码了 就是如此简单