%include	/usr/lib/rpm/macros.python
%define		zope_subname	LocalFS
Summary:	This product allows you to store Zope objects as human-readable files
Summary(pl):	Dodatek umo¿liwiaj±cy praktyczniejsze przetrzymywanie obiektów Zope
Name:		Zope-%{zope_subname}
Version:	1.1.0
Release:	1
License:	Distributable
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/localfs/%{zope_subname}-1-1-0.tgz
# Source0-md5:	738c05ad9e4cb59518269bc21fa79a1d
URL:		http://www.my-zope.org/Members/kedai/LocalFS-1-1-0.tgz/file_view/
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
%setup -q -c %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af lib/python/Products/LocalFS/{Extensions,dtml,help,www,*.py,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%doc lib/python/Products/LocalFS/{CHANGES,LICENSE,README,TODO}
%{_datadir}/%{name}
