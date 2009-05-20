%bcond_without  javadoc         # don't build javadoc

%if "%{pld_release}" == "ti"
%bcond_without java_sun        # build with gcj
%else
%bcond_with    java_sun        # build with java-sun
%endif

%include	/usr/lib/rpm/macros.java

%define		srcname		junit
Summary:	JUnit - regression testing framework
Summary(pl.UTF-8):	JUnit - środowisko do testów regresji
Name:		java-junit
Version:	4.4
Release:	2
License:	IBM Common Public License v1.0
Group:		Libraries/Java
Source0:	http://dl.sourceforge.net/junit/%{srcname}-%{version}-src.jar
# Source0-md5:	4126a0974473f7cb7df7fd5cd109505d
URL:		http://www.junit.org/
%{!?with_java_sun:BuildRequires:        java-gcj-compat-devel}
BuildRequires:	java-hamcrest
%{?with_java_sun:BuildRequires:	java-sun >= 1.5}
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-hamcrest
Requires:	jdk >= 1.5
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
export CLASSPATH=$(build-classpath hamcrest-core)

%javac $(find -name '*.java')
%jar -cvf %{srcname}-%{version}.jar $(find -type f '!' -name '*.java')
%{?with_javadoc:%javadoc -d javadoc $(find -name '*.java')}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit-%{version}.jar
ln -sf junit-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/junit.jar

# javadoc
%if %{with_javadoc}
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

%if %{with_javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%endif
