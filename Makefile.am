SUBDIRS = data gnomenews po

bin_SCRIPTS = gnome-news

EXTRA_DIST = \
	gnome-news.in \
	$(NULL)

CLEANFILES = \
	$(bin_SCRIPTS) \
	$(NULL)

MAINTAINERCLEANFILES = \
	$(GITIGNORE_MAINTAINERCLEANFILES_TOPLEVEL) \
	$(GITIGNORE_MAINTAINERCLEANFILES_MAKEFILE_IN) \
	$(GITIGNORE_MAINTAINERCLEANFILES_M4_LIBTOOL)

DISTCHECK_CONFIGURE_FLAGS = \
	--enable-appstream-util \
	$(NULL)

GITIGNOREFILES = \
	**/*.swp \
	m4/ \
	autom4te.cache/ \
	aclocal.m4 \
	ChangeLog \
	INSTALL \
	install-sh \
	missing \
	py-compile \
	gnomenews/__pycache__ \
	$(NULL)

gnome-news: gnome-news.in Makefile
	$(AM_V_GEN)sed						\
		-e s!\@srcdir\@!$(abs_top_srcdir)!	\
		-e s!\@prefix\@!$(prefix)!		\
		-e s!\@datadir\@!$(datadir)!		\
		-e s!\@pkgdatadir\@!$(pkgdatadir)!	\
		-e s!\@libexecdir\@!$(libexecdir)!	\
		-e s!\@libdir\@!$(libdir)!		\
		-e s!\@pkglibdir\@!$(pkglibdir)!	\
		-e s!\@localedir\@!$(localedir)!	\
		-e s!\@pythondir\@!$(pythondir)!	\
		-e s!\@pyexecdir\@!$(pyexecdir)!	\
		-e s!\@PACKAGE\@!$(PACKAGE)!		\
		-e s!\@version\@!$(VERSION)!		\
		< $< > $@
	chmod a+x $@

all-local: gnome-news

-include $(top_srcdir)/git.mk
