#!/usr/bin/env python


client = {
	'remote_client1':{
		'host' : '192.168.0.113',
	      'passwd' : 'alex3434',
		
	     'fileSet' : [
		'/usr/local/triaquae/log',	
		'/var/log/'],

	    'exclude'  : ['*.xml','test.log'],
	    
	    'bakup_policy': 'backup_for_client1',
	} ,
	'remote_client2':{
                'host' : '10.0.0.124',
              'passwd' : 'alex3dd',

	} 

}

Storage = {
	'local_01' : ['/dev/backup/'],
	'local_02' : ['/nfs/localback/'],

	'netdrive_01':{
		'host': '172.9.9.22',
		'pass': 'sfaf;f!',
	'remote_drive': '/dev/netBackup/',
	}


}
Back_policy = {
	'backup_for_client1': {
		'scheduler' : 'daily_incremental',
		'storage'   : 'local_01',
	}
	

}

Scheduler = {
	'daily_incremental' : {
		'run_time': {'hour':01,'minute': 23},
		'run_day': [1,2,3,4,5,6],
		'run_by_month':[],
		},

	'full_backup'	: {
		'run_time': {'hour':03,'minute':01},
                'run_day': [7]
		},	
}

	

