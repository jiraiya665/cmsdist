### RPM cms cmssw CMSSW_1_6_X_2007-07-18-08_2007-07-16-09
## IMPORT configurations 
Provides: /bin/zsh
Requires: cmssw-tool-conf python glimpse

#-ap start 2007-07-17
# WARNING: the following statement is needed to build the nightlies
# but will make "standard" builds of tags like CMSSW_X-Y-Z-g483 
# impossible without creating a new queue in the TC. 
# If you want to reuse an existing tag for this type of builds,
# please comment out the following statement:

%define cvstag		%v

#-ap end 2007-07-17

%define toolconf        ${CMSSW_TOOL_CONF_ROOT}/configurations/tools-STANDALONE.conf
%define cvsprojuc       %(echo %n | sed -e "s|-debug||"| tr 'a-z' 'A-Z')
%define cvsprojlc       %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir          %cvsprojuc
%define cvsserver       %cvsprojlc
%define conflevel       _2
%define prebuildtarget  gindices
%define buildtarget     release-build
%define patchsrc perl -p -i -e 's!<select name=(MyODBC)>!!' config/requirements ;
%define useCmsTC        1

## IMPORT cms-scram-build
## IMPORT scramv1-build
