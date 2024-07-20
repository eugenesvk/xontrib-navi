# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/xontrib-navi/compare/0.0.5...HEAD
## [Unreleased]
<!-- - ✨ __Added__ -->
  <!-- + new features -->
<!-- - Δ __Changed__ -->
  <!-- + changes in existing functionality -->
<!-- - 🐞 __Fixed__ -->
  <!-- + bug fixes -->
<!-- - 💩 __Deprecated__ -->
  <!-- + soon-to-be removed features -->
<!-- - 🗑️ __Removed__ -->
  <!-- + now removed features -->
<!-- - 🔒 __Security__ -->
  <!-- + vulnerabilities -->

[0.0.5]: https://github.com/eugenesvk/xontrib-navi/releases/tag/0.0.5
## [0.0.5]
  - __Changed__
    + drop trying to find a binary in a nonexistent cache, which is now very costly, especially with larger `$PATH`s

[0.0.4]: https://github.com/eugenesvk/xontrib-navi/releases/tag/0.0.4
## [0.0.4]
  - __Fixed__
    + 🐞 work with changed paths in xonsh v18

[0.0.3]: https://github.com/eugenesvk/xontrib-navi/releases/tag/0.0.3
## [0.0.3]
  - __Added__
    + :sparkles: feed navi a single command at the cursor location instead of the whole multi-command line
  - __Fixed__
    + :beetle: compare navi's best match to a space-stripped user command
