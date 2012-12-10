%define target avr

Name:           cross-%{target}-binutils
Version:        2.22
Release:        %mkrel 1
Summary:        Cross Compiling GNU binutils targeted at %{target}
Group:          Development/Other
License:        GPLv2+
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.bz2
BuildRequires:  gawk texinfo

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.


%prep
%setup -q -c


%build
mkdir -p build
pushd build
CFLAGS="%optflags" ../binutils-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-werror --disable-nls
make %{?_smp_mflags}
popd build


%install
rm -rf %{buildroot}
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


%changelog
* Mon Mar 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.22-1mdv2012.0
+ Revision: 785574
- update to 2.22

* Tue Oct 04 2011 Andrey Smirnov <asmirnov@mandriva.org> 2.21.1-1
+ Revision: 702720
- imported package cross-avr-binutils

* Tue Oct 12 2010 Funda Wang <fwang@mandriva.org> 2.20.51.0.11-1mnb2
+ Revision: 585033
- sync with main native binutils

* Mon Dec 28 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.20.51.0.4-1mnb2
+ Revision: 483151
- Update/sync with binutils 2.20.51.0.4-1mnb2
- Enable cross build for avr target, first release based on
  binutils-2.19.51.0.2-1mnb2
- binutils.spec: rename to cross-avr-binutils.spec
- Branch cross-avr-binutils, from current binutils.

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - don't ship with PIC libiberty for mips..
    - add missing 'OPTION_FIX_GS2F_KERNEL' enum type in binutils-2.19.51.0.2-mips-ls2f_fetch_fix.patch

* Wed Feb 11 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.19.51.0.2-1mnb2
+ Revision: 339335
- apply mips patches from 2008.1 Gdium tree
- enable 64 bit support for mipsel
- new release: 2.19.51.0.2
- spec cosmetics
- remove locale files when doing cross build
- fix string literal errors when building binutils for mips

* Wed Dec 24 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.19.50.0.1-1mnb2
+ Revision: 318384
- fix buildrequires
- sync with 2.19.50.0.1-8.fc11
- new release
- sync with binutils-2.18.50.0.9-1.fc10

* Mon Aug 18 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.18.50.0.8-1mnb2
+ Revision: 273254
- new release
- sync with binutils-2.18.50.0.8-2.fc10

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.18.50.0.6-1mnb2
+ Revision: 211109
- Updated to version 2.18.50.0.6
- Changed license tag (GPL -> GPLv3+, following policy).
- Sync patches with Fedora.

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.18.50.0.3-1mnb1
+ Revision: 170649
- replace %%mkrel with %%manbo_mkrel for Manbo Core 1

* Thu Jan 31 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.18.50.0.3-1mdv2008.1
+ Revision: 160824
- New release: 2.18.50.3
- sync patches with Fedora
- regenerate P21 (linux32)
- don't hardcode vendor name & os in target
- add translations
- cosmetics
- add missing ia64 patch from fedora
- sync with fedora 2.17.50.0.12-4
- move checks to %%check
- s/mandrake/mandriva/

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill file require on info-install

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Pixel <pixel@mandriva.com>
    - fix group (#28151)

* Sun May 06 2007 Christiaan Welvaart <spturtle@mandriva.org> 2.17.50.0.9-2mdv2008.0
+ Revision: 23749
- match all sparc flavors when checking target_cpu
- fix check to build alternate binaries for spu

