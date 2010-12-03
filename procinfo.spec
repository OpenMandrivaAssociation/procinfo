Summary: 	A tool for gathering and displaying system information
Name: 		procinfo
Version:	18
Release:	%mkrel 12
License: 	GPL
Group: 		Monitoring
URL:		http://freshmeat.net/projects/procinfo
Source: 	ftp://ftp.cistron.nl/pub/people/svm/procinfo-%{version}.tar.bz2
Patch0:		procinfo-14-misc.patch
Patch3:		procinfo-17-mandir.patch
Patch5:		procinfo-17-uptime.patch
Patch6:		procinfo-17-lsdev.patch
Patch7:		procinfo-18-acct.patch
Patch8:		procinfo-18-mharris-use-sysconf.patch
Patch9:		procinfo-18-maxdev.patch
Patch10:	procinfo-18-ranges.patch
Patch11:	procinfo-18-cpu-steal.patch
Patch12:	procinfo-18-intr.patch
BuildRequires: 	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The procinfo command gets system data from the /proc directory (the kernel
filesystem), formats it and displays it on standard output. You can use
procinfo to acquire information about your system from the kernel as it is
running.

Install procinfo if you'd like to use it to gather and display system data.

%prep

%setup -q
%patch0 -p1 -b .misc
%patch3 -p1 -b .mandir
%patch5 -p1 -b .uptime
%patch6 -p1 -b .lsdev
%patch7 -p1 -b .acct
%patch8 -p1 -b .mharris-use-sysconf
%patch9 -p1 -b .maxdev
%patch10 -p1 -b .ranges
%patch11 -p1 -b .steal
%patch12 -p1 -b .intr

%build
%make RPM_OPT_FLAGS="%{optflags} -I/usr/include/ncurses" LDFLAGS="%{ldflags}" LDLIBS="-lncurses"

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
%{_bindir}/procinfo
%{_bindir}/lsdev
%{_bindir}/socklist
%{_mandir}/man8/procinfo.8*
%{_mandir}/man8/lsdev.8*
%{_mandir}/man8/socklist.8*
