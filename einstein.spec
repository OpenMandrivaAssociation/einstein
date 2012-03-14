# Spec is based on ALT Linux work

Name:		einstein
Version:	2.0
Release:	%mkrel 1
Summary:	Remake of old DOS game Sherlock which was inspired by Albert Einstein's puzzle
License:	GPL
Group:		Games/Puzzles
URL:		http://games.flowix.com/en/index.html
Source:		http://www.babichev.info/files/einstein/%{name}-%{version}-src.tar.gz
Source1:	%{name}-1.0-html-pages.tgz
Source2:	%{name}-wrapper
Source3:	icon.bmp
Source4:	einstein.desktop
Source5:	einstein.png
Patch1:		einstein-math_h.patch
Patch2:		einstein-Makefile.patch
Patch3:		einstein-formatter_cpp.patch
Patch4:		einstein-2.0-deb-icon_change.patch
Patch5:		einstein-2.0-deb-font_change.patch
Patch6:		einstein-2.0-deb-random_init.patch
Patch7:		einstein-2.0-alt-rules_clarification.patch
Patch8:		einstein-2.0-alt-fix_mkres_link.patch
Patch9:		einstein-2.0-alt-translation_fix.patch
Patch10:	einstein-2.0-gcc43.patch
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	freetype-devel
BuildRequires:	zlib-devel
BuildRequires:	makedepend

%description
Einstein puzzle is cross-platform open source remake of old DOS game Sherlock
which was inspired by Albert Einstein's puzzle. Einstein said that only those
with an intelligence quotient of 97 percentile and higher should be able to
solve it.

The game goal is to open all cards in square of 6x6 cards.
Every row of square contains cards of one type only. For example, first row
contains arabic digits, second - letters, third - rome digits, fouths - dices,
fifth - geometric figures, sixs - mathematic symbols.

%prep
%setup
%setup -q -T -D -a 1

%patch1
%patch2
%patch3 -p2
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%__install %{SOURCE3} res/
%__mv %{name} doc
%__cp /usr/share/fonts/TTF/dejavu/DejaVuSans.ttf res/

%build
%make depend
%make -C mkres
pushd res
../mkres/mkres --source resources.descr --output ../einstein.res
popd
%make PREFIX=/usr

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_datadir}/%{name}/res
%makeinstall_std PREFIX=%{buildroot}%{_prefix}
%__mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
%__install %{SOURCE2} %{buildroot}%{_bindir}/%{name}
%__chmod 755 %{buildroot}%{_bindir}/%{name}
%__install -Dm 0644 %{SOURCE4} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -Dm 0644 %{SOURCE5} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf %{buildroot}

%files
%doc doc/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

