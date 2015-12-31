#!/usr/bin/python

import sys,os,time,logger

source_file = sys.argv[1]
formated_source_file = source_file.split('/')[-1]

backup_dir = '/home/antenna/lesson/backup/'
backup_to_file = '''%s%s_%s.tgz''' %(backup_dir,formated_source_file,time.strftime("%Y%m%d%H%M%S",time.localtime()))
def run_backup(runtime='now',exclude_file_name='None'):
	if len(sys.argv) == 4:
		print '--------exclude file mode--------'
		if sys.argv[2] == '-X':
			exclude_file_name = sys.argv[3]
		#	backup_cmd = "tar -cvzfX %s %s %s " %(backup_to_file,exclude_file_name,source_file)
			backup_cmd = "tar -cvzf %s  %s " %(backup_to_file,source_file)

	else:
		print '--------Normal mode:--------'
		# tar -cvzf %s  %s  |wc -l
		backup_cmd = "tar -N '2015/11/26' -cvzf %s  %s  |wc -l" %(backup_to_file,source_file) 
	run_command = os.system(backup_cmd)
	if run_command == 0:
		logger.record_log('Full Backup','Success','N/A','test')
	else:
		logger.record_log('Full Backup','Failure','N/A','test')



run_backup()
