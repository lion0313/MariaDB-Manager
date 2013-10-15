%define _topdir	 	%(echo $PWD)/
%define name		skysql-mgr-galera
%define release		##RELEASE_TAG##
%define version 	##VERSION_TAG##
%define buildroot 	%{_topdir}/%{name}-%{version}-%{release}root
%define install_path	/usr/local/skysql/

BuildRoot:		%{buildroot}
BuildArch:              noarch
Summary: 		SkySQL Cloud Data Suite
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-%{release}.tar.gz
Prefix: 		/
Group: 			Development/Tools
Requires:		MariaDBManager sqlite admin_php skysql_monitor tomcat7 = 7.0.39-1 gawk grep
#BuildRequires:		

%description
Metapackage to install SkySQL рackages for MariaDB+Galera

%prep

%setup -q

%build

%post
mkdir -p /usr/local/skysql/SQLite/AdminConsole
chown -R apache:apache %{install_path}SQLite

chkconfig --add tomcat7
/etc/init.d/tomcat7 restart

sed -i 's/# chkconfig: -/# chkconfig: 2345/' /etc/init.d/httpd
chkconfig --add httpd
/etc/init.d/httpd restart

%install

mkdir -p $RPM_BUILD_ROOT%{install_path}
mkdir $RPM_BUILD_ROOT%{install_path}config
mkdir $RPM_BUILD_ROOT%{install_path}skysql_aws/

cp manager.json $RPM_BUILD_ROOT%{install_path}config/
cp skysql.config $RPM_BUILD_ROOT%{install_path}skysql_aws/

mkdir -p $RPM_BUILD_ROOT/etc/init.d/
cp tomcat7 $RPM_BUILD_ROOT/etc/init.d/

%clean


%files
%defattr(-,root,root)
%{install_path}config/manager.json
%{install_path}skysql_aws/skysql.config
/etc/init.d/tomcat7


%changelog
