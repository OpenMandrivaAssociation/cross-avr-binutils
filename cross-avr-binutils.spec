%define target avr

Name:           cross-%{target}-binutils
Version:        2.24
Release:        1
Summary:        Cross Compiling GNU binutils targeted at %{target}
Group:          Development/Other
License:        GPLv2+
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org:21/pub/gnu/binutils/binutils-%{version}.tar.bz2
BuildRequires:  gawk texinfo

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c
sed -i -e 's/@colophon/@@colophon/' \
       -e 's/doc@cygnus.com/doc@@cygnus.com/' binutils-%{version}/bfd/doc/bfd.texinfo


%build
mkdir -p build
pushd build
CFLAGS="%{optflags}" ../binutils-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-werror --disable-nls
make %{?_smp_mflags}
popd build


%install
pushd build
make install DESTDIR=%{buildroot}
popd build
# these are for win targets only
rm %{buildroot}%{_mandir}/man1/%{target}-{dlltool,nlmconv,windres}.1
# we don't want these as we are a cross version
rm -r %{buildroot}%{_infodir}
rm    %{buildroot}%{_libdir}/libiberty.a


%files
%defattr(-,root,root,-)
%doc binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1*
