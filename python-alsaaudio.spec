%define 	module	alsaaudio
%define		_name	pyalsaaudio
Summary:	Wrappers for accessing the ALSA API from Python
Summary(pl.UTF-8):	Interfejs dający dostęp do ALSA API z poziomu Pythona
Name:		python-%{module}
Version:	0.7
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pyalsaaudio/%{_name}-%{version}.tar.gz
# Source0-md5:	2c573e5352d425cf4c09b3ee1d36ba68
URL:		http://sourceforge.net/projects/pyalsaaudio/
BuildRequires:	alsa-lib-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains wrappers for accessing the ALSA API from Python.
It is fairly complete for PCM devices and Mixer access.

%description -l pl.UTF-8
Pakiet zawiera interfejs umożliwiający dostęp do ALSA API z poziomu
Pythona. Jest w zasadzie już kompletny jeśli chodzi o dostęp do
urządzeń PCM i Miksera.

%prep
%setup -q -n %{_name}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{py_sitedir}/alsaaudio.so
%if "%{pld_release}" != "ac"
%{py_sitedir}/%{_name}-*.egg-info
%endif
