%define upstream_name    MooseX-Method-Signatures
%define upstream_version 0.36

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Method declarations with type constraints and no source filter
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(Context::Preserve)
BuildRequires: perl(Devel::Declare)   >= 0.5.11
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::LazyRequire)
BuildRequires: perl(MooseX::Meta::Signature::Combined)
BuildRequires: perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires: perl(Parse::Method::Signatures)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)       >= 0.880.0
BuildRequires: perl-aliased
BuildRequires: perl-namespace-autoclean
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires:   perl-aliased

%description
Provides a proper method keyword, like "sub" but specificly for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/MooseX
