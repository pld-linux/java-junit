Summary:	JUnit - regression testing framework
Summary(pl):	JUnit - ¶rodowisko do testów regresji
Name:		junit
Version:	3.7
Release:	1
License:	IBM Public License
Group:		Development/Languages/Java
Source0:	%{name}%{version}.zip
URL:		http://www.junit.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JUnit - regression testing framework.

%description -l pl
JUnit - ¶rodowisko do testów regresji.

%package doc
Summary:	JUnit documentation
Summary(pl):	Dokumentacja do JUnit
Group:		Development/Languages/Java

%description doc
JUnit documentation.

%description doc -l pl
Dokumentacja do JUnit.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install junit.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc javadoc junit
