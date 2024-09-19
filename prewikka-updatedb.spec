# TODO: apache (and other webservers?) configuration for prewikka WSGI
Summary:	Tools to update Prewikka database
Summary(pl.UTF-8):	Narzędzia do uaktualniania bazy danych Prewikki
Name:		prewikka-updatedb
Version:	5.2.0
Release:	1
License:	GPL v2+
Group:		Applications/Networking
#Source0Download: https://www.prelude-siem.org/projects/prelude/files
Source0:	https://www.prelude-siem.org/attachments/download/1399/%{name}-%{version}.tar.gz
# Source0-md5:	24f43f2ee9d77406c692e4c4742a00c7
URL:		https://www.prelude-siem.org/
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# need the same python version as prewika, < 5.2 used python2 in PLD
Requires:	prewikka >= 5.2
# pkg_resources
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools to update Prewikka database.

%description -l pl.UTF-8
Narzędzia do uaktualniania bazy danych Prewikki.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/prewikkaupdatedb
%{py3_sitescriptdir}/prewikka_updatedb-%{version}-py*.egg-info
