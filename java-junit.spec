Summary:	JUnit - regression testing framework
Summary(pl):	JUnit - ¶rodowisko do testów regresji
Name:		junit
Version:	3.8.2
Release:	1
License:	IBM Common Public License v1.0
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/junit/%{name}%{version}.zip
# Source0-md5:	9b8963ba2147a64bd5f1574b6fd289cb
URL:		http://www.junit.org/
BuildRequires:	unzip
Requires:	jdk >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

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
install junit.jar $RPM_BUILD_ROOT%{_javalibdir}/junit-%{version}.jar
ln -sf junit-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/junit.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html cpl-v10.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc javadoc junit
