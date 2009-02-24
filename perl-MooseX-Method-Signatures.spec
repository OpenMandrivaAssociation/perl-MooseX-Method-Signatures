%define module   MooseX-Method-Signatures
%define version    0.09
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Method declarations with type constraints and no source filter
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/MooseX/%{module}-%{version}.tar.gz
BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(Devel::Declare)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Meta::Signature::Combined)
BuildRequires: perl(Parse::Method::Signatures)
BuildRequires: perl(Test::Exception)
BuildRequires: perl-aliased
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Provides a proper method keyword, like "sub" but specificly for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -q -n %{module}-%{version} 

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

