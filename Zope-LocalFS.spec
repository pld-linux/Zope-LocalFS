
%define		zope_subname	LocalFS
Summary:	This product allows you to store Zope objects as human-readable files
Summary(pl):	Dodatek umo¿liwiaj±cy praktyczniejsze przetrzymywanie obiektów Zope
Name:		Zope-%{zope_subname}
Version:	1.3
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://www.easyleading.org/Downloads/%{zope_subname}-%{version}-andreas.tar.gz
# Source0-md5:	0fe97ac8a24e1e706df8d5d4d9543858
URL:		http://www.easyleading.org/Members/Eddy/LocalFS_1_3/
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This product allows you to store Zope objects as human-readable files
in the local file system.

%description -l pl
Dodatek dla Zope umo¿liwiaj±cy przetrzymywanie obiektów Zope w
lokalnym systemie plików.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,www,*.py,version.txt,refresh.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README TODO
%{_datadir}/%{name}
