
%define		zope_subname	LocalFS
Summary:	This product allows you to store Zope objects as human-readable files
Summary(pl.UTF-8):   Dodatek umożliwiający praktyczniejsze przetrzymywanie obiektów Zope
Name:		Zope-%{zope_subname}
Version:	1.6
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://www.easyleading.org/Downloads/%{zope_subname}-%{version}-andreas.tar.gz
# Source0-md5:	0196bdc5df0797cd33f5297b5a52c2f8
URL:		http://www.easyleading.org/Members/Eddy/LocalFS-1.6-andreas/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This product allows you to store Zope objects as human-readable files
in the local file system.

%description -l pl.UTF-8
Dodatek dla Zope umożliwiający przetrzymywanie obiektów Zope w
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
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README TODO
%{_datadir}/%{name}
