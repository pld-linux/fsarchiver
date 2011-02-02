Summary:	Safe and flexible file-system backup/deployment tool
Name:		fsarchiver
Version:	0.6.12
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/fsarchiver/%{name}-%{version}.tar.gz
# Source0-md5:	dc54cefcf9c2bc331063d82a7ad54133
URL:		http://www.fsarchiver.org/
BuildRequires:	attr-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	libblkid-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libuuid-devel
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSArchiver is a system tool that allows you to save the contents of a
file-system to a compressed archive file. The file-system can be
restored on a partition which has a different size and it can be
restored on a different file-system. Unlike tar/dar, FSArchiver also
creates the file-system when it extracts the data to partitions.
Everything is checksummed in the archive in order to protect the data.
If the archive is corrupt, you just lose the current file, not the
whole archive.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
