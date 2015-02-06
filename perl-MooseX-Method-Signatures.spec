%define upstream_name    MooseX-Method-Signatures
%define upstream_version 0.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Method declarations with type constraints and no source filter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B::Hooks::EndOfScope)
BuildRequires:	perl(Context::Preserve)
BuildRequires:	perl(Devel::Declare)   >= 0.5.11
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose::Util::TypeConstraints)
BuildRequires:	perl(MooseX::LazyRequire)
BuildRequires:	perl(MooseX::Meta::Signature::Combined)
BuildRequires:	perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires:	perl(Parse::Method::Signatures)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)       >= 0.880.0
BuildRequires:	perl(aliased)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch
Requires:	perl(aliased)

%description
Provides a proper method keyword, like "sub" but specificly for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/MooseX


%changelog
* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2011.0
+ Revision: 575400
- update to 0.36

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.350.0-1mdv2011.0
+ Revision: 558816
- new version

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 552418
- update to 0.34

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2010.1
+ Revision: 502084
- update to 0.30

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.1
+ Revision: 461332
- update to 0.29

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 447606
- update to 0.27

* Wed Sep 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 434687
- update to new version 0.26

* Tue Sep 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.0
+ Revision: 423158
- update to 0.24

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 421832
- update to 0.23

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 420270
- update to 0.21

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 418126
- update to 0.20

* Mon Aug 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.190.0-1mdv2010.0
+ Revision: 417171
- update buildrequires:
- adding missing buildrequires:
- update to 0.19

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 405946
- rebuild using %%perl_convert_version

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2010.0
+ Revision: 372187
- update to new version 0.16

* Sun Mar 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-2mdv2009.1
+ Revision: 352913
+ rebuild (emptylog)

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.1
+ Revision: 348829
- update to new version 0.12

* Sun Mar 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.1
+ Revision: 346267
- update to new version 0.10

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 344534
- update to new version 0.09

* Sun Feb 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 343990
- new version

* Thu Dec 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.1
+ Revision: 310093
- import perl-MooseX-Method-Signatures


* Thu Dec 04 2008 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist

