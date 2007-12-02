%define		_java_source	1.4
%define		_java_target	1.4
%include	/usr/lib/rpm/macros.java
Summary:	JUnit - regression testing framework
Summary(pl.UTF-8):	JUnit - środowisko do testów regresji
Name:		junit
Version:	3.8.2
Release:	2
License:	IBM Common Public License v1.0
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/junit/%{name}%{version}.zip
# Source0-md5:	9b8963ba2147a64bd5f1574b6fd289cb
URL:		http://www.junit.org/
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jdk >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JUnit - regression testing framework.

%description -l pl.UTF-8
JUnit - środowisko do testów regresji.

%package doc
Summary:	JUnit documentation
Summary(pl.UTF-8):	Dokumentacja do JUnit
Group:		Development/Languages/Java

%description doc
JUnit documentation.

%description doc -l pl.UTF-8
Dokumentacja do JUnit.

%package javadoc
Summary:	Javadoc documentation for JUnit
Summary(pl.UTF-8):	Dokumentacja javadoc dla JUnit
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
JUnit API documentation.

%prep
%setup -q -n %{name}%{version}
install -d build
unzip -q src.jar -d build

%build
cd build
%javac -target %{_java_target} -source %{_java_source} $(find -name '*.java')
%jar -cvf %{name}-%{version}.jar $(find -type f '!' -name '*.java')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install build/junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit-%{version}.jar
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
