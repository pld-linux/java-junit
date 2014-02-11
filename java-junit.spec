#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		srcname		junit
%include	/usr/lib/rpm/macros.java
Summary:	JUnit - regression testing framework
Summary(pl.UTF-8):	JUnit - środowisko do testów regresji
Name:		java-junit
Version:	4.11
Release:	1
License:	IBM Common Public License v1.0
Group:		Libraries/Java
Source0:	https://github.com/junit-team/junit/archive/r%{version}.tar.gz
# Source0-md5:	bf62095e510f50baf0962af329438647
URL:		http://www.junit.org/
BuildRequires:	java-hamcrest11
BuildRequires:	java-qdox
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-hamcrest11
Requires:	java-qdox
Obsoletes:	junit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JUnit - regression testing framework.

%description -l pl.UTF-8
JUnit - środowisko do testów regresji.

%package javadoc
Summary:	Javadoc documentation for JUnit
Summary(pl.UTF-8):	Dokumentacja javadoc dla pakietu JUnit
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	junit-doc
Obsoletes:	junit-javadoc

%description javadoc
JUnit API documentation.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu JUnit.

%package source
Summary:	Source code of JUnit
Summary(pl.UTF-8):	Kod źródłowy JUnita
Group:		Documentation
Requires:	jpackage-utils >= 1.7.5-2

%description source
Source code of JUnit.

%description source -l pl.UTF-8
Kod źródłowy JUnita.

%prep
%setup -q -n junit-r%{version}
install -d javadoc
rm -f junit/runner/Version.java.template

%build
required_jars="hamcrest11-core qdox"
CLASSPATH=$(build-classpath $required_jars)

%ant dist \
	-Dversion-status=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install junit%{version}/junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit-%{version}.jar
ln -sf junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -pr junit%{version}/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

# source
install -d $RPM_BUILD_ROOT%{_javasrcdir}
install junit%{version}/junit-%{version}-src.jar $RPM_BUILD_ROOT%{_javasrcdir}/%{srcname}.src.jar

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/junit-%{version}.jar
%{_javadir}/junit.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif

%files source
%defattr(644,root,root,755)
%{_javasrcdir}/%{srcname}.src.jar
