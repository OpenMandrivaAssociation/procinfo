Summary: 	A tool for gathering and displaying system information
Name: 		procinfo
Version:	18
Release:	%mkrel 9
License: 	GPL
Group: 		Monitoring
URL:		http://freshmeat.net/projects/procinfo
Source: 	ftp://ftp.cistron.nl/pub/people/svm/procinfo-%{version}.tar.bz2
Patch0: 	procinfo-14-misc.patch
BuildRequires: 	libtermcap-devel
Buildroot: 	%{_tmppath}/%{name}-root

%description
The procinfo command gets system data from the /proc directory (the kernel
filesystem), formats it and displays it on standard output. You can use
procinfo to acquire information about your system from the kernel as it is
running.

Install procinfo if you'd like to use it to gather and display system data.

%prep

%setup -q
%patch0 -p1 -b .misc

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man8}
perl -p -i -e 's/-o 0 -g 0//g' Makefile
perl -p -i -e 's!/man/!/share/man/!g' Makefile
perl -p -i -e 's!$(prefix)/man!'%{buildroot}'%{_mandir}!g' Makefile
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%{_bindir}/*
%{_mandir}/man8/*


