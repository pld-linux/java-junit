Summary:	Java regression test package
Name:		junit
Version:	3.8.1
Release:	0.1
License:	IBM Public License
Group:		Development
URL:		http://www.junit.org/
Source0:	http://dl.sourceforge.net/junit/%{name}%{version}.zip
# Source0-md5:	5110326e4b7f7497dfa60ede4b626751
BuildRequires:	jakarta-ant
Buildarch:	noarch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JUnit is a regression testing framework written by Erich Gamma and
Kent Beck. It is used by the developer who implements unit tests in
Java. JUnit is Open Source Software, released under the IBM Public
License and hosted on SourceForge.

%package manual
Summary:	Manual for %{name}
Group:		Development

%description manual
Documentation for %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%package demo
Summary:	Demos for %{name}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep

%setup -q -n %{name}%{version}
# extract sources
jar xvf src.jar

%build
ant dist

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install %{name}%{version}/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr %{name}%{version}/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
# demo
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr %{name}%{version}/%{name}/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc README.html
%{_javadir}/*
%dir %{_datadir}/%{name}

%files manual
%defattr(644,root,root,755)
%doc %{name}%{version}/doc/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}

%files demo
%defattr(644,root,root,755)
%{_datadir}/%{name}/*
