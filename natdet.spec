Summary:	NATDet - easy to use NAT detecion program
Summary(pl):	NATDet - ³atwy w obs³udze program do wykrywania NAT-u w sieci
Name:		natdet
Version:	1.0.0
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Networking
Source0:	http://r3b00t.itsec.pl/natdet/%{name}-%{version}.tgz
# Source0-md5:	a472486fea0182e192b22717b0da4b4c
Patch0:		%{name}-bpfh.patch
URL:		http://r3b00t.itsec.pl/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NATDet is quite small but very useful (especially for network
administrators) tool. By using it, you're able to detect guys who
share internet connection illegaly, without your authorization.

%description -l pl
NATDet jest ca³kiem ma³ym ale bardzo u¿ytecznym (zw³aszcza dla
administratorów sieci) narzêdziem. U¿ywaj±c go mo¿na wykryæ
u¿ytkowników, którzy nielegalnie udostepniaj± pol±czenie internetowe.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install natdet $RPM_BUILD_ROOT%{_bindir}
install natdet.fp $RPM_BUILD_ROOT%{_sysconfdir}
install doc/natdet.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/CREDITS doc/README* doc/PLATFORMS
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/natdet.fp
%{_mandir}/man1/natdet.1*
