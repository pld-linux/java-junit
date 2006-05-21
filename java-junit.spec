Summary:	JUnit - regression testing framework
Summary(pl):	JUnit - ¶rodowisko do testów regresji
Name:		junit
Version:	4.1
Release:	1
License:	IBM Common Public License v1.0
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/junit/%{name}%{version}.zip
# Source0-md5:	e66d3e77c70b3297f2c6a12990fc3120
URL:		http://www.junit.org/
BuildRequires:	unzip
Requires:	jdk >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package javadoc
Summary:	Javadoc documentation for JUnit
Summary(pl):	Dokumentacja javadoc dla JUnit
Group:		Development/Languages/Java

%description javadoc
JUnit API documentation.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit-%{version}.jar
ln -sf junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.html cpl-v10.html
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/* junit/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
