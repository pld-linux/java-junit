%include	/usr/lib/rpm/macros.java
Summary:	JUnit - regression testing framework
Summary(pl.UTF-8):	JUnit - środowisko do testów regresji
Name:		junit
Version:	4.4
Release:	1
License:	IBM Common Public License v1.0
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/junit/%{name}-%{version}-src.jar
# Source0-md5:	4126a0974473f7cb7df7fd5cd109505d
URL:		http://www.junit.org/
BuildRequires:	hamcrest
BuildRequires:	jdk >= 1.5
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	hamcrest
Requires:	jdk >= 1.5
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
%jar -cvf %{name}-%{version}.jar $(find -type f '!' -name '*.java')
%javadoc -d javadoc $(find -name '*.java')

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
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
