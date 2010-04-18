
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		srcname		junit
%include	/usr/lib/rpm/macros.java
Summary:	JUnit - regression testing framework
Summary(pl.UTF-8):	JUnit - środowisko do testów regresji
Name:		java-junit
Version:	4.8
Release:	1
License:	IBM Common Public License v1.0
Group:		Libraries/Java
Source0:	http://downloads.sourceforge.net/junit/%{srcname}-%{version}-src.jar
# Source0-md5:	5e1f1c4551bcd8399a1c3aeae123f575
URL:		http://www.junit.org/
BuildRequires:	java-hamcrest
BuildRequires:	java-qdox
BuildRequires:	java-sun
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-hamcrest
Requires:	java-qdox
Provides:	junit
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

%prep
%setup -qc
install -d javadoc
rm -f junit/runner/Version.java.template

%build
required_jars="hamcrest-core qdox"
CLASSPATH=$(build-classpath $required_jars)

%javac -cp $CLASSPATH -target 1.5 -source 1.5 $(find -name '*.java')
%jar -cvf %{srcname}-%{version}.jar $(find -type f '!' -name '*.java')

%{?with_javadoc:%javadoc -classpath $CLASSPATH -d javadoc $(find -name '*.java')}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit-%{version}.jar
ln -sf junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
