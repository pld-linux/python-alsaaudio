%define 	module	alsaaudio
%define		_name	pyalsaaudio
Summary:	Wrappers for accessing the ALSA API from Python
Summary(pl.UTF-8):	Interfejs dający dostęp do ALSA API z poziomu Pythona
Name:		python-%{module}
Version:	0.4
Release:	0.1
License:	PSF
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyalsaaudio/%{_name}-%{version}.tar.gz
# Source0-md5:	b312c28efba7db0494836a79f0a49898
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
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{py_sitedir}/alsaaudio.so
%if "%{pld_release}" != "ac"
%{py_sitedir}/%{_name}-*.egg-info
%endif
