import os 
import subprocess

header = "const {$,top,self,alert,window,screen,parent,length,jQuery,jquery,frames,origin,history,toolbar,menubar,document,external,location,navigator,statusbar,Handlebars,scrollbars,performance,personalbar,locationbar,localstorage,frameElement,customElements} = require('./setup_env.js'); \n"

def filter_bc(bytecode):
	filtered_bytecode = []
	for code in bytecode:
		if "@" in code:
			code = code.split(":")
			code = code[1].split()
			for c in code:
				if len(c) > 2:
					filtered_bytecode.append(c)
					break
	return [x.lower() for x in filtered_bytecode]

def js_to_bc(jsCode):
	linesCode = jsCode.splitlines()
	linesCode.insert(0,header)
	with open("temp.js",'w+', encoding = "ISO-8859-1") as writeFile:
		writeFile.writelines(linesCode)

	cmd = ['node','--print-bytecode','temp.js']
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	try:
		outs, errs = proc.communicate(timeout=15)
		if errs:
			print(errs.decode('ascii'))

	except subprocess.TimeoutExpired:
		proc.kill()
		outs, errs = proc.communicate()
		print ("Timeout")
	
	bytecode = outs.decode('ascii').splitlines()
	os.remove("temp.js")
	return filter_bc(bytecode)