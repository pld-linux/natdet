Summary:	NATDet - easy to use NAT detecion program
Summary(pl):	NATDet - �atwy w obs�udze program do wykrywania NAT-u w sieci
Name:		natdet
Version:	1.0.5
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications/Networking
Source0:	http://elceef.itsec.pl/natdet/%{name}-%{version}.tgz
# Source0-md5:	e1a9eb839b429b70f661fe87f1b13ed8
Patch0:		%{name}-PLD.patch
URL:		http://elceef.itsec.pl/natdet/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NATDet is quite small but very useful (especially for network
administrators) tool. By using it, you're able to detect guys who
share internet connection illegaly, without your authorization.

%description -l pl
NATDet jest ca�kiem ma�ym, ale bardzo u�ytecznym (zw�aszcza dla
administrator�w sieci) narz�dziem. U�ywaj�c go mo�na wykry�
u�ytkownik�w, kt�rzy nielegalnie udost�pniaj� po��czenie internetowe.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%configure
%{__make} all natstat \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir},%{_datadir}/%{name}}

install natdet $RPM_BUILD_ROOT%{_bindir}
install natstat/natstat $RPM_BUILD_ROOT%{_bindir}
install signatures $RPM_BUILD_ROOT%{_datadir}/%{name}
install doc/natdet.1 $RPM_BUILD_ROOT%{_mandir}/man1
install natstat/README doc/README-natstat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CREDITS doc/README* doc/Platforms doc/CHANGES doc/FAQ doc/debug-mode
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/natdet.1*
