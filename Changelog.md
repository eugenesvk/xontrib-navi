# Changelog
All notable changes to this project will be documented in this file

[unreleased]: https://github.com/eugenesvk/xontrib-navi/compare/0.0.4...HEAD
## [Unreleased]
<!-- - __Added__ -->
  <!-- + :sparkles:  -->
  <!-- new features -->
<!-- - __Changed__ -->
  <!-- +   -->
  <!-- changes in existing functionality -->
<!-- - __Fixed__ -->
  <!-- + :beetle:  -->
  <!-- bug fixes -->
<!-- - __Deprecated__ -->
  <!-- + :poop:  -->
  <!-- soon-to-be removed features -->
<!-- - __Removed__ -->
  <!-- + :wastebasket:  -->
  <!-- now removed features -->
<!-- - __Security__ -->
  <!-- + :lock:  -->
  <!-- vulnerabilities -->

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
