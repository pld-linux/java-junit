Summary: 	JUnit
Name:		junit
Version:	3.7
Release:	1
License:	IBM Public License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	%{name}%{version}.zip
URL:		http://www.junit.org
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JUnit

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	JUnit documentation

%description doc
JUnit documentation

%prep
%setup -q -n %{name}%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp junit.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf README.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc javadoc junit
