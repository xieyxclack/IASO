<?php
return array(
	//'配置项'=>'配置值'
	'URL_PATHINFO_DEPR' => '/',
	// URL不区分大小写
	'URL_CASE_INSENSITIVE' => true,
	'DB_TYPE'=>'mysql',
	'DB_HOST'=>'127.0.0.1',
	'DB_NAME'=>'temp',
	'DB_USER'=>'root',
	'DB_PWD'=>'root',
	'DB_PORT'=>3306,
	'DB_PREFIX'=>'',
	'DB_DEBUG' =>  TRUE, // 数据库调试模式 开启后可以记录SQL日志
	'URL_HTML_SUFFIX'=>'',
	'URL_MODEL'=>1,
	'SHOW_PAGE_TRACE' => true,
	'PUBLISH_DAY' => 0 ,
	'PUBLISH_TIME' => 9 ,
	'IS_SUNDAY_AVAILABLE' => 0 ,
	'SESSION_EXPIRE'=>604800,
	'SESSION_TYPE'=>'Db',
	'SESSION_TABLE'=>'think_session'
);