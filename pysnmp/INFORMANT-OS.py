# SNMP MIB module (INFORMANT-OS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-OS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:17 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(WtcsDisplayString,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "WtcsDisplayString",
    "informant")


# MODULE-IDENTITY

wmiOperatingSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22)
)
wmiOperatingSystem.setRevisions(
        ("2007-08-31 21:29",
         "2007-06-05 22:28",
         "2006-05-24 22:27",
         "2005-03-19 18:50",
         "2004-11-03 21:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WmiDesktop_ObjectIdentity = ObjectIdentity
wmiDesktop = _WmiDesktop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1)
)
if mibBuilder.loadTexts:
    wmiDesktop.setStatus("current")
_Win32DesktopTable_Object = MibTable
win32DesktopTable = _Win32DesktopTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1)
)
if mibBuilder.loadTexts:
    win32DesktopTable.setStatus("current")
_Win32DesktopEntry_Object = MibTableRow
win32DesktopEntry = _Win32DesktopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1)
)
win32DesktopEntry.setIndexNames(
    (0, "INFORMANT-OS", "osdtIndex"),
)
if mibBuilder.loadTexts:
    win32DesktopEntry.setStatus("current")


class _OsdtIndex_Type(Integer32):
    """Custom type osdtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsdtIndex_Type.__name__ = "Integer32"
_OsdtIndex_Object = MibTableColumn
osdtIndex = _OsdtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 1),
    _OsdtIndex_Type()
)
osdtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtIndex.setStatus("current")
_OsdtBorderWidth_Type = Gauge32
_OsdtBorderWidth_Object = MibTableColumn
osdtBorderWidth = _OsdtBorderWidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 2),
    _OsdtBorderWidth_Type()
)
osdtBorderWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtBorderWidth.setStatus("current")
_OsdtCaption_Type = WtcsDisplayString
_OsdtCaption_Object = MibTableColumn
osdtCaption = _OsdtCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 3),
    _OsdtCaption_Type()
)
osdtCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtCaption.setStatus("current")
_OsdtCoolSwitch_Type = TruthValue
_OsdtCoolSwitch_Object = MibTableColumn
osdtCoolSwitch = _OsdtCoolSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 4),
    _OsdtCoolSwitch_Type()
)
osdtCoolSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtCoolSwitch.setStatus("current")
_OsdtCursorBlinkRate_Type = Gauge32
_OsdtCursorBlinkRate_Object = MibTableColumn
osdtCursorBlinkRate = _OsdtCursorBlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 5),
    _OsdtCursorBlinkRate_Type()
)
osdtCursorBlinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtCursorBlinkRate.setStatus("current")
if mibBuilder.loadTexts:
    osdtCursorBlinkRate.setUnits("Milliseconds")
_OsdtDescription_Type = WtcsDisplayString
_OsdtDescription_Object = MibTableColumn
osdtDescription = _OsdtDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 6),
    _OsdtDescription_Type()
)
osdtDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtDescription.setStatus("current")
_OsdtDragFullWindows_Type = TruthValue
_OsdtDragFullWindows_Object = MibTableColumn
osdtDragFullWindows = _OsdtDragFullWindows_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 7),
    _OsdtDragFullWindows_Type()
)
osdtDragFullWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtDragFullWindows.setStatus("current")
_OsdtGridGranularity_Type = Gauge32
_OsdtGridGranularity_Object = MibTableColumn
osdtGridGranularity = _OsdtGridGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 8),
    _OsdtGridGranularity_Type()
)
osdtGridGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtGridGranularity.setStatus("current")
if mibBuilder.loadTexts:
    osdtGridGranularity.setUnits("8 Pixels")
_OsdtIconSpacing_Type = Gauge32
_OsdtIconSpacing_Object = MibTableColumn
osdtIconSpacing = _OsdtIconSpacing_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 9),
    _OsdtIconSpacing_Type()
)
osdtIconSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtIconSpacing.setStatus("current")
if mibBuilder.loadTexts:
    osdtIconSpacing.setUnits("Pixels")
_OsdtIconTitleFaceName_Type = WtcsDisplayString
_OsdtIconTitleFaceName_Object = MibTableColumn
osdtIconTitleFaceName = _OsdtIconTitleFaceName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 10),
    _OsdtIconTitleFaceName_Type()
)
osdtIconTitleFaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtIconTitleFaceName.setStatus("current")
_OsdtIconTitleSize_Type = Gauge32
_OsdtIconTitleSize_Object = MibTableColumn
osdtIconTitleSize = _OsdtIconTitleSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 11),
    _OsdtIconTitleSize_Type()
)
osdtIconTitleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtIconTitleSize.setStatus("current")
if mibBuilder.loadTexts:
    osdtIconTitleSize.setUnits("Point")
_OsdtIconTitleWrap_Type = TruthValue
_OsdtIconTitleWrap_Object = MibTableColumn
osdtIconTitleWrap = _OsdtIconTitleWrap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 12),
    _OsdtIconTitleWrap_Type()
)
osdtIconTitleWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtIconTitleWrap.setStatus("current")
_OsdtName_Type = WtcsDisplayString
_OsdtName_Object = MibTableColumn
osdtName = _OsdtName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 13),
    _OsdtName_Type()
)
osdtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtName.setStatus("current")
_OsdtPattern_Type = WtcsDisplayString
_OsdtPattern_Object = MibTableColumn
osdtPattern = _OsdtPattern_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 14),
    _OsdtPattern_Type()
)
osdtPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtPattern.setStatus("current")
_OsdtScreenSaverActive_Type = TruthValue
_OsdtScreenSaverActive_Object = MibTableColumn
osdtScreenSaverActive = _OsdtScreenSaverActive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 15),
    _OsdtScreenSaverActive_Type()
)
osdtScreenSaverActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtScreenSaverActive.setStatus("current")
_OsdtScreenSaverExecutable_Type = WtcsDisplayString
_OsdtScreenSaverExecutable_Object = MibTableColumn
osdtScreenSaverExecutable = _OsdtScreenSaverExecutable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 16),
    _OsdtScreenSaverExecutable_Type()
)
osdtScreenSaverExecutable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtScreenSaverExecutable.setStatus("current")
_OsdtScreenSaverSecure_Type = TruthValue
_OsdtScreenSaverSecure_Object = MibTableColumn
osdtScreenSaverSecure = _OsdtScreenSaverSecure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 17),
    _OsdtScreenSaverSecure_Type()
)
osdtScreenSaverSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtScreenSaverSecure.setStatus("current")
_OsdtScreenSaverTimeout_Type = Gauge32
_OsdtScreenSaverTimeout_Object = MibTableColumn
osdtScreenSaverTimeout = _OsdtScreenSaverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 18),
    _OsdtScreenSaverTimeout_Type()
)
osdtScreenSaverTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtScreenSaverTimeout.setStatus("current")
if mibBuilder.loadTexts:
    osdtScreenSaverTimeout.setUnits("Seconds")
_OsdtSettingID_Type = WtcsDisplayString
_OsdtSettingID_Object = MibTableColumn
osdtSettingID = _OsdtSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 19),
    _OsdtSettingID_Type()
)
osdtSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtSettingID.setStatus("current")
_OsdtWallpaper_Type = WtcsDisplayString
_OsdtWallpaper_Object = MibTableColumn
osdtWallpaper = _OsdtWallpaper_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 20),
    _OsdtWallpaper_Type()
)
osdtWallpaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtWallpaper.setStatus("current")
_OsdtWallpaperStretched_Type = TruthValue
_OsdtWallpaperStretched_Object = MibTableColumn
osdtWallpaperStretched = _OsdtWallpaperStretched_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 21),
    _OsdtWallpaperStretched_Type()
)
osdtWallpaperStretched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtWallpaperStretched.setStatus("current")
_OsdtWallpaperTiled_Type = TruthValue
_OsdtWallpaperTiled_Object = MibTableColumn
osdtWallpaperTiled = _OsdtWallpaperTiled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 1, 1, 22),
    _OsdtWallpaperTiled_Type()
)
osdtWallpaperTiled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdtWallpaperTiled.setStatus("current")
_Win32EnvironmentTable_Object = MibTable
win32EnvironmentTable = _Win32EnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2)
)
if mibBuilder.loadTexts:
    win32EnvironmentTable.setStatus("current")
_Win32EnvironmentEntry_Object = MibTableRow
win32EnvironmentEntry = _Win32EnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1)
)
win32EnvironmentEntry.setIndexNames(
    (0, "INFORMANT-OS", "osevIndex"),
)
if mibBuilder.loadTexts:
    win32EnvironmentEntry.setStatus("current")


class _OsevIndex_Type(Integer32):
    """Custom type osevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsevIndex_Type.__name__ = "Integer32"
_OsevIndex_Object = MibTableColumn
osevIndex = _OsevIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 1),
    _OsevIndex_Type()
)
osevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevIndex.setStatus("current")
_OsevCaption_Type = WtcsDisplayString
_OsevCaption_Object = MibTableColumn
osevCaption = _OsevCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 2),
    _OsevCaption_Type()
)
osevCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevCaption.setStatus("current")
_OsevDescription_Type = WtcsDisplayString
_OsevDescription_Object = MibTableColumn
osevDescription = _OsevDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 3),
    _OsevDescription_Type()
)
osevDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevDescription.setStatus("current")
_OsevInstallDate_Type = DateAndTime
_OsevInstallDate_Object = MibTableColumn
osevInstallDate = _OsevInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 4),
    _OsevInstallDate_Type()
)
osevInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevInstallDate.setStatus("current")
_OsevName_Type = WtcsDisplayString
_OsevName_Object = MibTableColumn
osevName = _OsevName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 5),
    _OsevName_Type()
)
osevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevName.setStatus("current")


class _OsevStatus_Type(Integer32):
    """Custom type osevStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsevStatus_Type.__name__ = "Integer32"
_OsevStatus_Object = MibTableColumn
osevStatus = _OsevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 6),
    _OsevStatus_Type()
)
osevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevStatus.setStatus("current")
_OsevSystemVariable_Type = TruthValue
_OsevSystemVariable_Object = MibTableColumn
osevSystemVariable = _OsevSystemVariable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 7),
    _OsevSystemVariable_Type()
)
osevSystemVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevSystemVariable.setStatus("current")


class _OsevUserName_Type(WtcsDisplayString):
    """Custom type osevUserName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 260),
    )


_OsevUserName_Type.__name__ = "WtcsDisplayString"
_OsevUserName_Object = MibTableColumn
osevUserName = _OsevUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 8),
    _OsevUserName_Type()
)
osevUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevUserName.setStatus("current")
_OsevVariableValue_Type = WtcsDisplayString
_OsevVariableValue_Object = MibTableColumn
osevVariableValue = _OsevVariableValue_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 2, 1, 9),
    _OsevVariableValue_Type()
)
osevVariableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osevVariableValue.setStatus("current")
_Win32TimeZoneTable_Object = MibTable
win32TimeZoneTable = _Win32TimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3)
)
if mibBuilder.loadTexts:
    win32TimeZoneTable.setStatus("current")
_Win32TimeZoneEntry_Object = MibTableRow
win32TimeZoneEntry = _Win32TimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1)
)
win32TimeZoneEntry.setIndexNames(
    (0, "INFORMANT-OS", "ostzIndex"),
)
if mibBuilder.loadTexts:
    win32TimeZoneEntry.setStatus("current")


class _OstzIndex_Type(Integer32):
    """Custom type ostzIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OstzIndex_Type.__name__ = "Integer32"
_OstzIndex_Object = MibTableColumn
ostzIndex = _OstzIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 1),
    _OstzIndex_Type()
)
ostzIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzIndex.setStatus("current")
_OstzBias_Type = Integer32
_OstzBias_Object = MibTableColumn
ostzBias = _OstzBias_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 2),
    _OstzBias_Type()
)
ostzBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzBias.setStatus("current")
if mibBuilder.loadTexts:
    ostzBias.setUnits("Minutes")
_OstzCaption_Type = WtcsDisplayString
_OstzCaption_Object = MibTableColumn
ostzCaption = _OstzCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 3),
    _OstzCaption_Type()
)
ostzCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzCaption.setStatus("current")
_OstzDaylightBias_Type = Integer32
_OstzDaylightBias_Object = MibTableColumn
ostzDaylightBias = _OstzDaylightBias_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 4),
    _OstzDaylightBias_Type()
)
ostzDaylightBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightBias.setStatus("current")
if mibBuilder.loadTexts:
    ostzDaylightBias.setUnits("Minutes")
_OstzDaylightDay_Type = Gauge32
_OstzDaylightDay_Object = MibTableColumn
ostzDaylightDay = _OstzDaylightDay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 5),
    _OstzDaylightDay_Type()
)
ostzDaylightDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightDay.setStatus("current")


class _OstzDaylightDayOfWeek_Type(Integer32):
    """Custom type ostzDaylightDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_OstzDaylightDayOfWeek_Type.__name__ = "Integer32"
_OstzDaylightDayOfWeek_Object = MibTableColumn
ostzDaylightDayOfWeek = _OstzDaylightDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 6),
    _OstzDaylightDayOfWeek_Type()
)
ostzDaylightDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightDayOfWeek.setStatus("current")
_OstzDaylightHour_Type = Gauge32
_OstzDaylightHour_Object = MibTableColumn
ostzDaylightHour = _OstzDaylightHour_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 7),
    _OstzDaylightHour_Type()
)
ostzDaylightHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightHour.setStatus("current")
_OstzDaylightMillisecond_Type = Gauge32
_OstzDaylightMillisecond_Object = MibTableColumn
ostzDaylightMillisecond = _OstzDaylightMillisecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 8),
    _OstzDaylightMillisecond_Type()
)
ostzDaylightMillisecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightMillisecond.setStatus("current")
_OstzDaylightMinute_Type = Gauge32
_OstzDaylightMinute_Object = MibTableColumn
ostzDaylightMinute = _OstzDaylightMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 9),
    _OstzDaylightMinute_Type()
)
ostzDaylightMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightMinute.setStatus("current")


class _OstzDaylightMonth_Type(Integer32):
    """Custom type ostzDaylightMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_OstzDaylightMonth_Type.__name__ = "Integer32"
_OstzDaylightMonth_Object = MibTableColumn
ostzDaylightMonth = _OstzDaylightMonth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 10),
    _OstzDaylightMonth_Type()
)
ostzDaylightMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightMonth.setStatus("current")


class _OstzDaylightName_Type(WtcsDisplayString):
    """Custom type ostzDaylightName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstzDaylightName_Type.__name__ = "WtcsDisplayString"
_OstzDaylightName_Object = MibTableColumn
ostzDaylightName = _OstzDaylightName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 11),
    _OstzDaylightName_Type()
)
ostzDaylightName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightName.setStatus("current")
_OstzDaylightSecond_Type = Gauge32
_OstzDaylightSecond_Object = MibTableColumn
ostzDaylightSecond = _OstzDaylightSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 12),
    _OstzDaylightSecond_Type()
)
ostzDaylightSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightSecond.setStatus("current")
_OstzDaylightYear_Type = Gauge32
_OstzDaylightYear_Object = MibTableColumn
ostzDaylightYear = _OstzDaylightYear_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 13),
    _OstzDaylightYear_Type()
)
ostzDaylightYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDaylightYear.setStatus("current")
_OstzDescription_Type = WtcsDisplayString
_OstzDescription_Object = MibTableColumn
ostzDescription = _OstzDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 14),
    _OstzDescription_Type()
)
ostzDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzDescription.setStatus("current")
_OstzSettingID_Type = WtcsDisplayString
_OstzSettingID_Object = MibTableColumn
ostzSettingID = _OstzSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 15),
    _OstzSettingID_Type()
)
ostzSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzSettingID.setStatus("current")
_OstzStandardBias_Type = Gauge32
_OstzStandardBias_Object = MibTableColumn
ostzStandardBias = _OstzStandardBias_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 16),
    _OstzStandardBias_Type()
)
ostzStandardBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardBias.setStatus("current")
if mibBuilder.loadTexts:
    ostzStandardBias.setUnits("Minutes")
_OstzStandardDay_Type = Gauge32
_OstzStandardDay_Object = MibTableColumn
ostzStandardDay = _OstzStandardDay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 17),
    _OstzStandardDay_Type()
)
ostzStandardDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardDay.setStatus("current")


class _OstzStandardDayOfWeek_Type(Integer32):
    """Custom type ostzStandardDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_OstzStandardDayOfWeek_Type.__name__ = "Integer32"
_OstzStandardDayOfWeek_Object = MibTableColumn
ostzStandardDayOfWeek = _OstzStandardDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 18),
    _OstzStandardDayOfWeek_Type()
)
ostzStandardDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardDayOfWeek.setStatus("current")
_OstzStandardHour_Type = Gauge32
_OstzStandardHour_Object = MibTableColumn
ostzStandardHour = _OstzStandardHour_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 19),
    _OstzStandardHour_Type()
)
ostzStandardHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardHour.setStatus("current")
_OstzStandardMillisecond_Type = Gauge32
_OstzStandardMillisecond_Object = MibTableColumn
ostzStandardMillisecond = _OstzStandardMillisecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 20),
    _OstzStandardMillisecond_Type()
)
ostzStandardMillisecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardMillisecond.setStatus("current")
_OstzStandardMinute_Type = Gauge32
_OstzStandardMinute_Object = MibTableColumn
ostzStandardMinute = _OstzStandardMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 21),
    _OstzStandardMinute_Type()
)
ostzStandardMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardMinute.setStatus("current")


class _OstzStandardMonth_Type(Integer32):
    """Custom type ostzStandardMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("april", 4),
          ("august", 8),
          ("december", 12),
          ("february", 2),
          ("january", 1),
          ("july", 7),
          ("june", 6),
          ("march", 3),
          ("may", 5),
          ("november", 11),
          ("october", 10),
          ("september", 9))
    )


_OstzStandardMonth_Type.__name__ = "Integer32"
_OstzStandardMonth_Object = MibTableColumn
ostzStandardMonth = _OstzStandardMonth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 22),
    _OstzStandardMonth_Type()
)
ostzStandardMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardMonth.setStatus("current")


class _OstzStandardName_Type(WtcsDisplayString):
    """Custom type ostzStandardName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstzStandardName_Type.__name__ = "WtcsDisplayString"
_OstzStandardName_Object = MibTableColumn
ostzStandardName = _OstzStandardName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 23),
    _OstzStandardName_Type()
)
ostzStandardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardName.setStatus("current")
_OstzStandardSecond_Type = Gauge32
_OstzStandardSecond_Object = MibTableColumn
ostzStandardSecond = _OstzStandardSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 24),
    _OstzStandardSecond_Type()
)
ostzStandardSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardSecond.setStatus("current")
_OstzStandardYear_Type = Gauge32
_OstzStandardYear_Object = MibTableColumn
ostzStandardYear = _OstzStandardYear_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 1, 3, 1, 25),
    _OstzStandardYear_Type()
)
ostzStandardYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostzStandardYear.setStatus("current")
_WmiDrivers_ObjectIdentity = ObjectIdentity
wmiDrivers = _WmiDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2)
)
if mibBuilder.loadTexts:
    wmiDrivers.setStatus("current")
_Win32DriverVXDTable_Object = MibTable
win32DriverVXDTable = _Win32DriverVXDTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1)
)
if mibBuilder.loadTexts:
    win32DriverVXDTable.setStatus("current")
_Win32DriverVXDEntry_Object = MibTableRow
win32DriverVXDEntry = _Win32DriverVXDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1)
)
win32DriverVXDEntry.setIndexNames(
    (0, "INFORMANT-OS", "osvxdIndex"),
)
if mibBuilder.loadTexts:
    win32DriverVXDEntry.setStatus("current")


class _OsvxdIndex_Type(Integer32):
    """Custom type osvxdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsvxdIndex_Type.__name__ = "Integer32"
_OsvxdIndex_Object = MibTableColumn
osvxdIndex = _OsvxdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 1),
    _OsvxdIndex_Type()
)
osvxdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdIndex.setStatus("current")
_OsvxdBuildNumber_Type = WtcsDisplayString
_OsvxdBuildNumber_Object = MibTableColumn
osvxdBuildNumber = _OsvxdBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 2),
    _OsvxdBuildNumber_Type()
)
osvxdBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdBuildNumber.setStatus("current")
_OsvxdCaption_Type = WtcsDisplayString
_OsvxdCaption_Object = MibTableColumn
osvxdCaption = _OsvxdCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 3),
    _OsvxdCaption_Type()
)
osvxdCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdCaption.setStatus("current")
_OsvxdCodeSet_Type = WtcsDisplayString
_OsvxdCodeSet_Object = MibTableColumn
osvxdCodeSet = _OsvxdCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 4),
    _OsvxdCodeSet_Type()
)
osvxdCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdCodeSet.setStatus("current")
_OsvxdControl_Type = WtcsDisplayString
_OsvxdControl_Object = MibTableColumn
osvxdControl = _OsvxdControl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 5),
    _OsvxdControl_Type()
)
osvxdControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdControl.setStatus("current")
_OsvxdDescription_Type = WtcsDisplayString
_OsvxdDescription_Object = MibTableColumn
osvxdDescription = _OsvxdDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 6),
    _OsvxdDescription_Type()
)
osvxdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdDescription.setStatus("current")
_OsvxdDeviceDescriptorBlock_Type = WtcsDisplayString
_OsvxdDeviceDescriptorBlock_Object = MibTableColumn
osvxdDeviceDescriptorBlock = _OsvxdDeviceDescriptorBlock_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 7),
    _OsvxdDeviceDescriptorBlock_Type()
)
osvxdDeviceDescriptorBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdDeviceDescriptorBlock.setStatus("current")
_OsvxdIdentificationCode_Type = WtcsDisplayString
_OsvxdIdentificationCode_Object = MibTableColumn
osvxdIdentificationCode = _OsvxdIdentificationCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 8),
    _OsvxdIdentificationCode_Type()
)
osvxdIdentificationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdIdentificationCode.setStatus("current")
_OsvxdInstallDate_Type = DateAndTime
_OsvxdInstallDate_Object = MibTableColumn
osvxdInstallDate = _OsvxdInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 9),
    _OsvxdInstallDate_Type()
)
osvxdInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdInstallDate.setStatus("current")
_OsvxdLanguageEdition_Type = WtcsDisplayString
_OsvxdLanguageEdition_Object = MibTableColumn
osvxdLanguageEdition = _OsvxdLanguageEdition_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 10),
    _OsvxdLanguageEdition_Type()
)
osvxdLanguageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdLanguageEdition.setStatus("current")
_OsvxdManufacturer_Type = WtcsDisplayString
_OsvxdManufacturer_Object = MibTableColumn
osvxdManufacturer = _OsvxdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 11),
    _OsvxdManufacturer_Type()
)
osvxdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdManufacturer.setStatus("current")
_OsvxdName_Type = WtcsDisplayString
_OsvxdName_Object = MibTableColumn
osvxdName = _OsvxdName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 12),
    _OsvxdName_Type()
)
osvxdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdName.setStatus("current")
_OsvxdOtherTargetOS_Type = WtcsDisplayString
_OsvxdOtherTargetOS_Object = MibTableColumn
osvxdOtherTargetOS = _OsvxdOtherTargetOS_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 13),
    _OsvxdOtherTargetOS_Type()
)
osvxdOtherTargetOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdOtherTargetOS.setStatus("current")
_OsvxdPMAPI_Type = WtcsDisplayString
_OsvxdPMAPI_Object = MibTableColumn
osvxdPMAPI = _OsvxdPMAPI_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 14),
    _OsvxdPMAPI_Type()
)
osvxdPMAPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdPMAPI.setStatus("current")
_OsvxdSerialNumber_Type = WtcsDisplayString
_OsvxdSerialNumber_Object = MibTableColumn
osvxdSerialNumber = _OsvxdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 15),
    _OsvxdSerialNumber_Type()
)
osvxdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdSerialNumber.setStatus("current")
_OsvxdServiceTableSize_Type = Gauge32
_OsvxdServiceTableSize_Object = MibTableColumn
osvxdServiceTableSize = _OsvxdServiceTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 16),
    _OsvxdServiceTableSize_Type()
)
osvxdServiceTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdServiceTableSize.setStatus("current")


class _OsvxdSoftwareElementID_Type(WtcsDisplayString):
    """Custom type osvxdSoftwareElementID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsvxdSoftwareElementID_Type.__name__ = "WtcsDisplayString"
_OsvxdSoftwareElementID_Object = MibTableColumn
osvxdSoftwareElementID = _OsvxdSoftwareElementID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 17),
    _OsvxdSoftwareElementID_Type()
)
osvxdSoftwareElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdSoftwareElementID.setStatus("current")


class _OsvxdSoftwareElementState_Type(Integer32):
    """Custom type osvxdSoftwareElementState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deployable", 1),
          ("executable", 3),
          ("installable", 2),
          ("running", 4))
    )


_OsvxdSoftwareElementState_Type.__name__ = "Integer32"
_OsvxdSoftwareElementState_Object = MibTableColumn
osvxdSoftwareElementState = _OsvxdSoftwareElementState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 18),
    _OsvxdSoftwareElementState_Type()
)
osvxdSoftwareElementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdSoftwareElementState.setStatus("current")


class _OsvxdStatus_Type(Integer32):
    """Custom type osvxdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsvxdStatus_Type.__name__ = "Integer32"
_OsvxdStatus_Object = MibTableColumn
osvxdStatus = _OsvxdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 19),
    _OsvxdStatus_Type()
)
osvxdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdStatus.setStatus("current")


class _OsvxdTargetOperatingSystem_Type(Integer32):
    """Custom type osvxdTargetOperatingSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61)
        )
    )
    namedValues = NamedValues(
        *(("aix", 9),
          ("aseries", 32),
          ("attunix", 3),
          ("beOS", 53),
          ("bs2000", 35),
          ("bsdunix", 41),
          ("dcOS", 23),
          ("decnt", 5),
          ("dedicated", 59),
          ("dgux", 4),
          ("digitalUnix", 6),
          ("epoc", 49),
          ("freeBSD", 42),
          ("gnuHurd", 44),
          ("hpMPE", 54),
          ("hpux", 8),
          ("inferno", 47),
          ("interactiveUNIX", 40),
          ("irix", 28),
          ("ixWorks", 50),
          ("javaVM", 13),
          ("linux", 36),
          ("lynx", 37),
          ("machKernel", 46),
          ("macos", 2),
          ("miNT", 52),
          ("msdos", 14),
          ("mvs", 10),
          ("ncr3000", 20),
          ("netBSD", 43),
          ("netWare", 21),
          ("nextStep", 55),
          ("openVMS", 7),
          ("os2", 12),
          ("os400", 11),
          ("os9", 45),
          ("osf", 22),
          ("other", 1),
          ("palmPilot", 56),
          ("qnx", 48),
          ("reliantUNIX", 24),
          ("rhapsody", 57),
          ("scoOpenServer", 26),
          ("scoUnixWare", 25),
          ("sequent", 27),
          ("solaris", 29),
          ("sunOS", 30),
          ("tandemNSK", 33),
          ("tandemNT", 34),
          ("tpf", 61),
          ("u6000", 31),
          ("unknown", 0),
          ("vmESA", 39),
          ("vse", 60),
          ("vxWorks", 51),
          ("win3x", 15),
          ("win95", 16),
          ("win98", 17),
          ("wince", 19),
          ("windows2000", 58),
          ("winnt", 18),
          ("xenix", 38))
    )


_OsvxdTargetOperatingSystem_Type.__name__ = "Integer32"
_OsvxdTargetOperatingSystem_Object = MibTableColumn
osvxdTargetOperatingSystem = _OsvxdTargetOperatingSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 20),
    _OsvxdTargetOperatingSystem_Type()
)
osvxdTargetOperatingSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdTargetOperatingSystem.setStatus("current")
_OsvxdV86API_Type = WtcsDisplayString
_OsvxdV86API_Object = MibTableColumn
osvxdV86API = _OsvxdV86API_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 21),
    _OsvxdV86API_Type()
)
osvxdV86API.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdV86API.setStatus("current")
_OsvxdVersion_Type = WtcsDisplayString
_OsvxdVersion_Object = MibTableColumn
osvxdVersion = _OsvxdVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 1, 1, 22),
    _OsvxdVersion_Type()
)
osvxdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvxdVersion.setStatus("current")
_Win32SystemDriverTable_Object = MibTable
win32SystemDriverTable = _Win32SystemDriverTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2)
)
if mibBuilder.loadTexts:
    win32SystemDriverTable.setStatus("current")
_Win32SystemDriverEntry_Object = MibTableRow
win32SystemDriverEntry = _Win32SystemDriverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1)
)
win32SystemDriverEntry.setIndexNames(
    (0, "INFORMANT-OS", "ossdIndex"),
)
if mibBuilder.loadTexts:
    win32SystemDriverEntry.setStatus("current")


class _OssdIndex_Type(Integer32):
    """Custom type ossdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OssdIndex_Type.__name__ = "Integer32"
_OssdIndex_Object = MibTableColumn
ossdIndex = _OssdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 1),
    _OssdIndex_Type()
)
ossdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdIndex.setStatus("current")
_OssdAcceptPause_Type = TruthValue
_OssdAcceptPause_Object = MibTableColumn
ossdAcceptPause = _OssdAcceptPause_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 2),
    _OssdAcceptPause_Type()
)
ossdAcceptPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdAcceptPause.setStatus("current")
_OssdAcceptStop_Type = TruthValue
_OssdAcceptStop_Object = MibTableColumn
ossdAcceptStop = _OssdAcceptStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 3),
    _OssdAcceptStop_Type()
)
ossdAcceptStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdAcceptStop.setStatus("current")
_OssdCaption_Type = WtcsDisplayString
_OssdCaption_Object = MibTableColumn
ossdCaption = _OssdCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 4),
    _OssdCaption_Type()
)
ossdCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdCaption.setStatus("current")


class _OssdCreationClassName_Type(WtcsDisplayString):
    """Custom type ossdCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OssdCreationClassName_Type.__name__ = "WtcsDisplayString"
_OssdCreationClassName_Object = MibTableColumn
ossdCreationClassName = _OssdCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 5),
    _OssdCreationClassName_Type()
)
ossdCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdCreationClassName.setStatus("current")
_OssdDescription_Type = WtcsDisplayString
_OssdDescription_Object = MibTableColumn
ossdDescription = _OssdDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 6),
    _OssdDescription_Type()
)
ossdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdDescription.setStatus("current")
_OssdDesktopInteract_Type = TruthValue
_OssdDesktopInteract_Object = MibTableColumn
ossdDesktopInteract = _OssdDesktopInteract_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 7),
    _OssdDesktopInteract_Type()
)
ossdDesktopInteract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdDesktopInteract.setStatus("current")
_OssdDisplayName_Type = WtcsDisplayString
_OssdDisplayName_Object = MibTableColumn
ossdDisplayName = _OssdDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 8),
    _OssdDisplayName_Type()
)
ossdDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdDisplayName.setStatus("current")
_OssdErrorControl_Type = WtcsDisplayString
_OssdErrorControl_Object = MibTableColumn
ossdErrorControl = _OssdErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 9),
    _OssdErrorControl_Type()
)
ossdErrorControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdErrorControl.setStatus("current")
_OssdExitCode_Type = Gauge32
_OssdExitCode_Object = MibTableColumn
ossdExitCode = _OssdExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 10),
    _OssdExitCode_Type()
)
ossdExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdExitCode.setStatus("current")
_OssdInstallDate_Type = DateAndTime
_OssdInstallDate_Object = MibTableColumn
ossdInstallDate = _OssdInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 11),
    _OssdInstallDate_Type()
)
ossdInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdInstallDate.setStatus("current")
_OssdName_Type = WtcsDisplayString
_OssdName_Object = MibTableColumn
ossdName = _OssdName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 12),
    _OssdName_Type()
)
ossdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdName.setStatus("current")
_OssdPathName_Type = WtcsDisplayString
_OssdPathName_Object = MibTableColumn
ossdPathName = _OssdPathName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 13),
    _OssdPathName_Type()
)
ossdPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdPathName.setStatus("current")
_OssdServiceSpecificExitCode_Type = Gauge32
_OssdServiceSpecificExitCode_Object = MibTableColumn
ossdServiceSpecificExitCode = _OssdServiceSpecificExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 14),
    _OssdServiceSpecificExitCode_Type()
)
ossdServiceSpecificExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdServiceSpecificExitCode.setStatus("current")


class _OssdServiceType_Type(Integer32):
    """Custom type ossdServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("adapter", 3),
          ("fileSystemDriver", 2),
          ("interactiveProcess", 7),
          ("kernalDriver", 1),
          ("ownProcess", 5),
          ("recognizerDriver", 4),
          ("shareProcess", 6))
    )


_OssdServiceType_Type.__name__ = "Integer32"
_OssdServiceType_Object = MibTableColumn
ossdServiceType = _OssdServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 15),
    _OssdServiceType_Type()
)
ossdServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdServiceType.setStatus("current")
_OssdStarted_Type = TruthValue
_OssdStarted_Object = MibTableColumn
ossdStarted = _OssdStarted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 16),
    _OssdStarted_Type()
)
ossdStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdStarted.setStatus("current")
_OssdStartMode_Type = WtcsDisplayString
_OssdStartMode_Object = MibTableColumn
ossdStartMode = _OssdStartMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 17),
    _OssdStartMode_Type()
)
ossdStartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdStartMode.setStatus("current")
_OssdStartName_Type = WtcsDisplayString
_OssdStartName_Object = MibTableColumn
ossdStartName = _OssdStartName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 18),
    _OssdStartName_Type()
)
ossdStartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdStartName.setStatus("current")


class _OssdState_Type(Integer32):
    """Custom type ossdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("continuePending", 5),
          ("pausePending", 6),
          ("paused", 7),
          ("running", 4),
          ("startPending", 2),
          ("stopPending", 3),
          ("stopped", 1),
          ("unknown", 8))
    )


_OssdState_Type.__name__ = "Integer32"
_OssdState_Object = MibTableColumn
ossdState = _OssdState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 19),
    _OssdState_Type()
)
ossdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdState.setStatus("current")


class _OssdStatus_Type(Integer32):
    """Custom type ossdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OssdStatus_Type.__name__ = "Integer32"
_OssdStatus_Object = MibTableColumn
ossdStatus = _OssdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 20),
    _OssdStatus_Type()
)
ossdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdStatus.setStatus("current")
_OssdSystemCreationClassName_Type = WtcsDisplayString
_OssdSystemCreationClassName_Object = MibTableColumn
ossdSystemCreationClassName = _OssdSystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 21),
    _OssdSystemCreationClassName_Type()
)
ossdSystemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdSystemCreationClassName.setStatus("current")
_OssdSystemName_Type = WtcsDisplayString
_OssdSystemName_Object = MibTableColumn
ossdSystemName = _OssdSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 22),
    _OssdSystemName_Type()
)
ossdSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdSystemName.setStatus("current")
_OssdTagId_Type = Gauge32
_OssdTagId_Object = MibTableColumn
ossdTagId = _OssdTagId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 2, 2, 1, 23),
    _OssdTagId_Type()
)
ossdTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossdTagId.setStatus("current")
_WmiFileSystem_ObjectIdentity = ObjectIdentity
wmiFileSystem = _WmiFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3)
)
if mibBuilder.loadTexts:
    wmiFileSystem.setStatus("current")
_Win32DiskPartitionTable_Object = MibTable
win32DiskPartitionTable = _Win32DiskPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1)
)
if mibBuilder.loadTexts:
    win32DiskPartitionTable.setStatus("current")
_Win32DiskPartitionEntry_Object = MibTableRow
win32DiskPartitionEntry = _Win32DiskPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1)
)
win32DiskPartitionEntry.setIndexNames(
    (0, "INFORMANT-OS", "osdpIndex"),
)
if mibBuilder.loadTexts:
    win32DiskPartitionEntry.setStatus("current")


class _OsdpIndex_Type(Integer32):
    """Custom type osdpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsdpIndex_Type.__name__ = "Integer32"
_OsdpIndex_Object = MibTableColumn
osdpIndex = _OsdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 1),
    _OsdpIndex_Type()
)
osdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpIndex.setStatus("current")


class _OsdpAccess_Type(Integer32):
    """Custom type osdpAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("readable", 1),
          ("readwriteSupported", 3),
          ("unknown", 0),
          ("writable", 2),
          ("writeOnce", 4))
    )


_OsdpAccess_Type.__name__ = "Integer32"
_OsdpAccess_Object = MibTableColumn
osdpAccess = _OsdpAccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 2),
    _OsdpAccess_Type()
)
osdpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpAccess.setStatus("current")


class _OsdpAvailability_Type(Integer32):
    """Custom type osdpAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notConfigured", 20),
          ("notInstalled", 11),
          ("notReady", 19),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("paused", 18),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("quiesced", 21),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OsdpAvailability_Type.__name__ = "Integer32"
_OsdpAvailability_Object = MibTableColumn
osdpAvailability = _OsdpAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 3),
    _OsdpAvailability_Type()
)
osdpAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpAvailability.setStatus("current")
_OsdpBlockSize_Type = Gauge32
_OsdpBlockSize_Object = MibTableColumn
osdpBlockSize = _OsdpBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 4),
    _OsdpBlockSize_Type()
)
osdpBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpBlockSize.setStatus("current")
_OsdpBootable_Type = TruthValue
_OsdpBootable_Object = MibTableColumn
osdpBootable = _OsdpBootable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 5),
    _OsdpBootable_Type()
)
osdpBootable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpBootable.setStatus("current")
_OsdpBootPartition_Type = TruthValue
_OsdpBootPartition_Object = MibTableColumn
osdpBootPartition = _OsdpBootPartition_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 6),
    _OsdpBootPartition_Type()
)
osdpBootPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpBootPartition.setStatus("current")
_OsdpCaption_Type = WtcsDisplayString
_OsdpCaption_Object = MibTableColumn
osdpCaption = _OsdpCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 7),
    _OsdpCaption_Type()
)
osdpCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpCaption.setStatus("current")


class _OsdpConfigManagerErrorCode_Type(Integer32):
    """Custom type osdpConfigManagerErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("bootConflicts", 6),
          ("cannotFilter", 7),
          ("cannotIdentify", 16),
          ("cannotLoad", 2),
          ("cannotLoadDrivers", 31),
          ("cannotStart", 10),
          ("cannotVerifyResources", 13),
          ("conflictIRQ", 30),
          ("deviceDisabled", 22),
          ("deviceFailed", 11),
          ("deviceProblem", 24),
          ("driverCorrupted", 4),
          ("driverLoaderMissing", 8),
          ("driversNotInstalled", 28),
          ("failedVXDloader", 19),
          ("invalidLogConfiguration", 27),
          ("lowResource", 3),
          ("missingResources", 29),
          ("needResource", 5),
          ("noFreeResources", 12),
          ("notConfigured", 1),
          ("reenumerationProblem", 15),
          ("registryCorrupted", 20),
          ("reinstallDrivers", 18),
          ("resourceIncorrect", 9),
          ("restartComputer", 14),
          ("settingUpDevice", 25),
          ("settingUpDevice2", 26),
          ("systemFailuer2", 23),
          ("systemFailure", 21),
          ("unknownResourceType", 17),
          ("workingProperly", 0))
    )


_OsdpConfigManagerErrorCode_Type.__name__ = "Integer32"
_OsdpConfigManagerErrorCode_Object = MibTableColumn
osdpConfigManagerErrorCode = _OsdpConfigManagerErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 8),
    _OsdpConfigManagerErrorCode_Type()
)
osdpConfigManagerErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpConfigManagerErrorCode.setStatus("current")
_OsdpConfigManagerUserConfig_Type = TruthValue
_OsdpConfigManagerUserConfig_Object = MibTableColumn
osdpConfigManagerUserConfig = _OsdpConfigManagerUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 9),
    _OsdpConfigManagerUserConfig_Type()
)
osdpConfigManagerUserConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpConfigManagerUserConfig.setStatus("current")
_OsdpCreationClassName_Type = WtcsDisplayString
_OsdpCreationClassName_Object = MibTableColumn
osdpCreationClassName = _OsdpCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 10),
    _OsdpCreationClassName_Type()
)
osdpCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpCreationClassName.setStatus("current")
_OsdpDescription_Type = WtcsDisplayString
_OsdpDescription_Object = MibTableColumn
osdpDescription = _OsdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 11),
    _OsdpDescription_Type()
)
osdpDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpDescription.setStatus("current")
_OsdpDeviceID_Type = WtcsDisplayString
_OsdpDeviceID_Object = MibTableColumn
osdpDeviceID = _OsdpDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 12),
    _OsdpDeviceID_Type()
)
osdpDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpDeviceID.setStatus("current")
_OsdpDiskIndex_Type = Gauge32
_OsdpDiskIndex_Object = MibTableColumn
osdpDiskIndex = _OsdpDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 13),
    _OsdpDiskIndex_Type()
)
osdpDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpDiskIndex.setStatus("current")
_OsdpErrorCleared_Type = TruthValue
_OsdpErrorCleared_Object = MibTableColumn
osdpErrorCleared = _OsdpErrorCleared_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 14),
    _OsdpErrorCleared_Type()
)
osdpErrorCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpErrorCleared.setStatus("current")
_OsdpErrorDescription_Type = WtcsDisplayString
_OsdpErrorDescription_Object = MibTableColumn
osdpErrorDescription = _OsdpErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 15),
    _OsdpErrorDescription_Type()
)
osdpErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpErrorDescription.setStatus("current")
_OsdpErrorMethodology_Type = WtcsDisplayString
_OsdpErrorMethodology_Object = MibTableColumn
osdpErrorMethodology = _OsdpErrorMethodology_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 16),
    _OsdpErrorMethodology_Type()
)
osdpErrorMethodology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpErrorMethodology.setStatus("current")
_OsdpHiddenSectors_Type = Gauge32
_OsdpHiddenSectors_Object = MibTableColumn
osdpHiddenSectors = _OsdpHiddenSectors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 17),
    _OsdpHiddenSectors_Type()
)
osdpHiddenSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpHiddenSectors.setStatus("current")
_OsdpPartitionIndex_Type = Gauge32
_OsdpPartitionIndex_Object = MibTableColumn
osdpPartitionIndex = _OsdpPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 18),
    _OsdpPartitionIndex_Type()
)
osdpPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPartitionIndex.setStatus("current")
_OsdpInstallDate_Type = DateAndTime
_OsdpInstallDate_Object = MibTableColumn
osdpInstallDate = _OsdpInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 19),
    _OsdpInstallDate_Type()
)
osdpInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpInstallDate.setStatus("current")
_OsdpLastErrorCode_Type = Gauge32
_OsdpLastErrorCode_Object = MibTableColumn
osdpLastErrorCode = _OsdpLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 20),
    _OsdpLastErrorCode_Type()
)
osdpLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpLastErrorCode.setStatus("current")
_OsdpName_Type = WtcsDisplayString
_OsdpName_Object = MibTableColumn
osdpName = _OsdpName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 21),
    _OsdpName_Type()
)
osdpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpName.setStatus("current")
_OsdpNumberOfBlocks_Type = Gauge32
_OsdpNumberOfBlocks_Object = MibTableColumn
osdpNumberOfBlocks = _OsdpNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 22),
    _OsdpNumberOfBlocks_Type()
)
osdpNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpNumberOfBlocks.setStatus("current")
_OsdpPNPDeviceID_Type = WtcsDisplayString
_OsdpPNPDeviceID_Object = MibTableColumn
osdpPNPDeviceID = _OsdpPNPDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 23),
    _OsdpPNPDeviceID_Type()
)
osdpPNPDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPNPDeviceID.setStatus("current")
_OsdpPowerManagementCapabilities_Type = WtcsDisplayString
_OsdpPowerManagementCapabilities_Object = MibTableColumn
osdpPowerManagementCapabilities = _OsdpPowerManagementCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 24),
    _OsdpPowerManagementCapabilities_Type()
)
osdpPowerManagementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPowerManagementCapabilities.setStatus("current")
_OsdpPowerManagementSupported_Type = TruthValue
_OsdpPowerManagementSupported_Object = MibTableColumn
osdpPowerManagementSupported = _OsdpPowerManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 25),
    _OsdpPowerManagementSupported_Type()
)
osdpPowerManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPowerManagementSupported.setStatus("current")
_OsdpPrimaryPartition_Type = TruthValue
_OsdpPrimaryPartition_Object = MibTableColumn
osdpPrimaryPartition = _OsdpPrimaryPartition_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 26),
    _OsdpPrimaryPartition_Type()
)
osdpPrimaryPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPrimaryPartition.setStatus("current")
_OsdpPurpose_Type = WtcsDisplayString
_OsdpPurpose_Object = MibTableColumn
osdpPurpose = _OsdpPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 27),
    _OsdpPurpose_Type()
)
osdpPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpPurpose.setStatus("current")
_OsdpRewritePartition_Type = TruthValue
_OsdpRewritePartition_Object = MibTableColumn
osdpRewritePartition = _OsdpRewritePartition_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 28),
    _OsdpRewritePartition_Type()
)
osdpRewritePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpRewritePartition.setStatus("current")
_OsdpSize_Type = WtcsDisplayString
_OsdpSize_Object = MibTableColumn
osdpSize = _OsdpSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 29),
    _OsdpSize_Type()
)
osdpSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpSize.setStatus("current")
if mibBuilder.loadTexts:
    osdpSize.setUnits("Bytes")
_OsdpStartingOffset_Type = Gauge32
_OsdpStartingOffset_Object = MibTableColumn
osdpStartingOffset = _OsdpStartingOffset_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 30),
    _OsdpStartingOffset_Type()
)
osdpStartingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpStartingOffset.setStatus("current")
if mibBuilder.loadTexts:
    osdpStartingOffset.setUnits("Bytes")


class _OsdpStatus_Type(Integer32):
    """Custom type osdpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsdpStatus_Type.__name__ = "Integer32"
_OsdpStatus_Object = MibTableColumn
osdpStatus = _OsdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 31),
    _OsdpStatus_Type()
)
osdpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpStatus.setStatus("current")


class _OsdpStatusInfo_Type(Integer32):
    """Custom type osdpStatusInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OsdpStatusInfo_Type.__name__ = "Integer32"
_OsdpStatusInfo_Object = MibTableColumn
osdpStatusInfo = _OsdpStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 32),
    _OsdpStatusInfo_Type()
)
osdpStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpStatusInfo.setStatus("current")
_OsdpSystemCreationClassName_Type = WtcsDisplayString
_OsdpSystemCreationClassName_Object = MibTableColumn
osdpSystemCreationClassName = _OsdpSystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 33),
    _OsdpSystemCreationClassName_Type()
)
osdpSystemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpSystemCreationClassName.setStatus("current")
_OsdpSystemName_Type = WtcsDisplayString
_OsdpSystemName_Object = MibTableColumn
osdpSystemName = _OsdpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 34),
    _OsdpSystemName_Type()
)
osdpSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpSystemName.setStatus("current")
_OsdpType_Type = WtcsDisplayString
_OsdpType_Object = MibTableColumn
osdpType = _OsdpType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 1, 1, 35),
    _OsdpType_Type()
)
osdpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdpType.setStatus("current")
_Win32LogicalDiskTable_Object = MibTable
win32LogicalDiskTable = _Win32LogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2)
)
if mibBuilder.loadTexts:
    win32LogicalDiskTable.setStatus("current")
_Win32LogicalDiskEntry_Object = MibTableRow
win32LogicalDiskEntry = _Win32LogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1)
)
win32LogicalDiskEntry.setIndexNames(
    (0, "INFORMANT-OS", "osldIndex"),
)
if mibBuilder.loadTexts:
    win32LogicalDiskEntry.setStatus("current")


class _OsldIndex_Type(Integer32):
    """Custom type osldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsldIndex_Type.__name__ = "Integer32"
_OsldIndex_Object = MibTableColumn
osldIndex = _OsldIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 1),
    _OsldIndex_Type()
)
osldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldIndex.setStatus("current")


class _OsldAccess_Type(Integer32):
    """Custom type osldAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("readWriteSupported", 3),
          ("readable", 1),
          ("unknown", 0),
          ("writable", 2),
          ("writeOnce", 4))
    )


_OsldAccess_Type.__name__ = "Integer32"
_OsldAccess_Object = MibTableColumn
osldAccess = _OsldAccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 2),
    _OsldAccess_Type()
)
osldAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldAccess.setStatus("current")


class _OsldAvailability_Type(Integer32):
    """Custom type osldAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notConfigured", 20),
          ("notInstalled", 11),
          ("notReady", 19),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("paused", 18),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("quiesced", 21),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OsldAvailability_Type.__name__ = "Integer32"
_OsldAvailability_Object = MibTableColumn
osldAvailability = _OsldAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 3),
    _OsldAvailability_Type()
)
osldAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldAvailability.setStatus("current")
_OsldBlockSize_Type = Gauge32
_OsldBlockSize_Object = MibTableColumn
osldBlockSize = _OsldBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 4),
    _OsldBlockSize_Type()
)
osldBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldBlockSize.setStatus("current")
_OsldCaption_Type = WtcsDisplayString
_OsldCaption_Object = MibTableColumn
osldCaption = _OsldCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 5),
    _OsldCaption_Type()
)
osldCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldCaption.setStatus("current")
_OsldCompressed_Type = TruthValue
_OsldCompressed_Object = MibTableColumn
osldCompressed = _OsldCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 6),
    _OsldCompressed_Type()
)
osldCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldCompressed.setStatus("current")


class _OsldConfigManagerErrorCode_Type(Integer32):
    """Custom type osldConfigManagerErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("bootConflicts", 6),
          ("cannotFilter", 7),
          ("cannotIdentify", 16),
          ("cannotLoad", 2),
          ("cannotLoadDrivers", 31),
          ("cannotStart", 10),
          ("cannotVerifyResources", 13),
          ("conflictIRQ", 30),
          ("deviceDisabled", 22),
          ("deviceFailed", 11),
          ("deviceProblem", 24),
          ("driverCorrupted", 4),
          ("driverLoaderMissing", 8),
          ("driversNotInstalled", 28),
          ("failedVXDloader", 19),
          ("invalidLogConfiguration", 27),
          ("lowResource", 3),
          ("missingResources", 29),
          ("needResource", 5),
          ("noFreeResources", 12),
          ("notConfigured", 1),
          ("reenumerationProblem", 15),
          ("registryCorrupted", 20),
          ("reinstallDrivers", 18),
          ("resourceIncorrect", 9),
          ("restartComputer", 14),
          ("settingUpDevice", 25),
          ("settingUpDevice2", 26),
          ("systemFailuer2", 23),
          ("systemFailure", 21),
          ("unknownResourceType", 17),
          ("workingProperly", 0))
    )


_OsldConfigManagerErrorCode_Type.__name__ = "Integer32"
_OsldConfigManagerErrorCode_Object = MibTableColumn
osldConfigManagerErrorCode = _OsldConfigManagerErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 7),
    _OsldConfigManagerErrorCode_Type()
)
osldConfigManagerErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldConfigManagerErrorCode.setStatus("current")
_OsldConfigManagerUserConfig_Type = TruthValue
_OsldConfigManagerUserConfig_Object = MibTableColumn
osldConfigManagerUserConfig = _OsldConfigManagerUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 8),
    _OsldConfigManagerUserConfig_Type()
)
osldConfigManagerUserConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldConfigManagerUserConfig.setStatus("current")
_OsldCreationClassName_Type = WtcsDisplayString
_OsldCreationClassName_Object = MibTableColumn
osldCreationClassName = _OsldCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 9),
    _OsldCreationClassName_Type()
)
osldCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldCreationClassName.setStatus("current")
_OsldDescription_Type = WtcsDisplayString
_OsldDescription_Object = MibTableColumn
osldDescription = _OsldDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 10),
    _OsldDescription_Type()
)
osldDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldDescription.setStatus("current")
_OsldDeviceID_Type = WtcsDisplayString
_OsldDeviceID_Object = MibTableColumn
osldDeviceID = _OsldDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 11),
    _OsldDeviceID_Type()
)
osldDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldDeviceID.setStatus("current")


class _OsldDriveType_Type(Integer32):
    """Custom type osldDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compactDisc", 5),
          ("localDisk", 3),
          ("networkDrive", 4),
          ("noRootDirectory", 1),
          ("ramDisk", 6),
          ("removableDisk", 2),
          ("unknown", 0))
    )


_OsldDriveType_Type.__name__ = "Integer32"
_OsldDriveType_Object = MibTableColumn
osldDriveType = _OsldDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 12),
    _OsldDriveType_Type()
)
osldDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldDriveType.setStatus("current")
_OsldErrorCleared_Type = TruthValue
_OsldErrorCleared_Object = MibTableColumn
osldErrorCleared = _OsldErrorCleared_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 13),
    _OsldErrorCleared_Type()
)
osldErrorCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldErrorCleared.setStatus("current")
_OsldErrorDescription_Type = WtcsDisplayString
_OsldErrorDescription_Object = MibTableColumn
osldErrorDescription = _OsldErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 14),
    _OsldErrorDescription_Type()
)
osldErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldErrorDescription.setStatus("current")
_OsldErrorMethodology_Type = WtcsDisplayString
_OsldErrorMethodology_Object = MibTableColumn
osldErrorMethodology = _OsldErrorMethodology_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 15),
    _OsldErrorMethodology_Type()
)
osldErrorMethodology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldErrorMethodology.setStatus("current")
_OsldFileSystem_Type = WtcsDisplayString
_OsldFileSystem_Object = MibTableColumn
osldFileSystem = _OsldFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 16),
    _OsldFileSystem_Type()
)
osldFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldFileSystem.setStatus("current")
_OsldFreeSpace_Type = Gauge32
_OsldFreeSpace_Object = MibTableColumn
osldFreeSpace = _OsldFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 17),
    _OsldFreeSpace_Type()
)
osldFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldFreeSpace.setStatus("current")
_OsldInstallDate_Type = DateAndTime
_OsldInstallDate_Object = MibTableColumn
osldInstallDate = _OsldInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 18),
    _OsldInstallDate_Type()
)
osldInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldInstallDate.setStatus("current")
_OsldLastErrorCode_Type = Gauge32
_OsldLastErrorCode_Object = MibTableColumn
osldLastErrorCode = _OsldLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 19),
    _OsldLastErrorCode_Type()
)
osldLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldLastErrorCode.setStatus("current")
_OsldMaximumComponentLength_Type = Gauge32
_OsldMaximumComponentLength_Object = MibTableColumn
osldMaximumComponentLength = _OsldMaximumComponentLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 20),
    _OsldMaximumComponentLength_Type()
)
osldMaximumComponentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldMaximumComponentLength.setStatus("current")


class _OsldMediaType_Type(Gauge32):
    """Custom type osldMediaType based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 22),
    )


_OsldMediaType_Type.__name__ = "Gauge32"
_OsldMediaType_Object = MibTableColumn
osldMediaType = _OsldMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 21),
    _OsldMediaType_Type()
)
osldMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldMediaType.setStatus("current")
_OsldName_Type = WtcsDisplayString
_OsldName_Object = MibTableColumn
osldName = _OsldName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 22),
    _OsldName_Type()
)
osldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldName.setStatus("current")
_OsldNumberOfBlocks_Type = Gauge32
_OsldNumberOfBlocks_Object = MibTableColumn
osldNumberOfBlocks = _OsldNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 23),
    _OsldNumberOfBlocks_Type()
)
osldNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldNumberOfBlocks.setStatus("current")
_OsldPNPDeviceID_Type = WtcsDisplayString
_OsldPNPDeviceID_Object = MibTableColumn
osldPNPDeviceID = _OsldPNPDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 24),
    _OsldPNPDeviceID_Type()
)
osldPNPDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldPNPDeviceID.setStatus("current")
_OsldPowerManagementCapabilities_Type = WtcsDisplayString
_OsldPowerManagementCapabilities_Object = MibTableColumn
osldPowerManagementCapabilities = _OsldPowerManagementCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 25),
    _OsldPowerManagementCapabilities_Type()
)
osldPowerManagementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldPowerManagementCapabilities.setStatus("current")
_OsldPowerManagementSupported_Type = TruthValue
_OsldPowerManagementSupported_Object = MibTableColumn
osldPowerManagementSupported = _OsldPowerManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 26),
    _OsldPowerManagementSupported_Type()
)
osldPowerManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldPowerManagementSupported.setStatus("current")
_OsldProviderName_Type = WtcsDisplayString
_OsldProviderName_Object = MibTableColumn
osldProviderName = _OsldProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 27),
    _OsldProviderName_Type()
)
osldProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldProviderName.setStatus("current")
_OsldPurpose_Type = WtcsDisplayString
_OsldPurpose_Object = MibTableColumn
osldPurpose = _OsldPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 28),
    _OsldPurpose_Type()
)
osldPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldPurpose.setStatus("current")
_OsldQuotasDisabled_Type = TruthValue
_OsldQuotasDisabled_Object = MibTableColumn
osldQuotasDisabled = _OsldQuotasDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 29),
    _OsldQuotasDisabled_Type()
)
osldQuotasDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldQuotasDisabled.setStatus("current")
_OsldQuotasIncomplete_Type = TruthValue
_OsldQuotasIncomplete_Object = MibTableColumn
osldQuotasIncomplete = _OsldQuotasIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 30),
    _OsldQuotasIncomplete_Type()
)
osldQuotasIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldQuotasIncomplete.setStatus("current")
_OsldQuotasRebuilding_Type = TruthValue
_OsldQuotasRebuilding_Object = MibTableColumn
osldQuotasRebuilding = _OsldQuotasRebuilding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 31),
    _OsldQuotasRebuilding_Type()
)
osldQuotasRebuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldQuotasRebuilding.setStatus("current")
_OsldSize_Type = Gauge32
_OsldSize_Object = MibTableColumn
osldSize = _OsldSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 32),
    _OsldSize_Type()
)
osldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldSize.setStatus("current")


class _OsldStatus_Type(Integer32):
    """Custom type osldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsldStatus_Type.__name__ = "Integer32"
_OsldStatus_Object = MibTableColumn
osldStatus = _OsldStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 33),
    _OsldStatus_Type()
)
osldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldStatus.setStatus("current")


class _OsldStatusInfo_Type(Integer32):
    """Custom type osldStatusInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OsldStatusInfo_Type.__name__ = "Integer32"
_OsldStatusInfo_Object = MibTableColumn
osldStatusInfo = _OsldStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 34),
    _OsldStatusInfo_Type()
)
osldStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldStatusInfo.setStatus("current")
_OsldSupportsDiskQuotas_Type = TruthValue
_OsldSupportsDiskQuotas_Object = MibTableColumn
osldSupportsDiskQuotas = _OsldSupportsDiskQuotas_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 35),
    _OsldSupportsDiskQuotas_Type()
)
osldSupportsDiskQuotas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldSupportsDiskQuotas.setStatus("current")
_OsldSupportsFileBasedCompression_Type = TruthValue
_OsldSupportsFileBasedCompression_Object = MibTableColumn
osldSupportsFileBasedCompression = _OsldSupportsFileBasedCompression_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 36),
    _OsldSupportsFileBasedCompression_Type()
)
osldSupportsFileBasedCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldSupportsFileBasedCompression.setStatus("current")
_OsldSystemCreationClassName_Type = WtcsDisplayString
_OsldSystemCreationClassName_Object = MibTableColumn
osldSystemCreationClassName = _OsldSystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 37),
    _OsldSystemCreationClassName_Type()
)
osldSystemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldSystemCreationClassName.setStatus("current")
_OsldSystemName_Type = WtcsDisplayString
_OsldSystemName_Object = MibTableColumn
osldSystemName = _OsldSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 38),
    _OsldSystemName_Type()
)
osldSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldSystemName.setStatus("current")
_OsldVolumeDirty_Type = TruthValue
_OsldVolumeDirty_Object = MibTableColumn
osldVolumeDirty = _OsldVolumeDirty_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 39),
    _OsldVolumeDirty_Type()
)
osldVolumeDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldVolumeDirty.setStatus("current")
_OsldVolumeName_Type = WtcsDisplayString
_OsldVolumeName_Object = MibTableColumn
osldVolumeName = _OsldVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 40),
    _OsldVolumeName_Type()
)
osldVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldVolumeName.setStatus("current")
_OsldVolumeSerialNumber_Type = WtcsDisplayString
_OsldVolumeSerialNumber_Object = MibTableColumn
osldVolumeSerialNumber = _OsldVolumeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 2, 1, 41),
    _OsldVolumeSerialNumber_Type()
)
osldVolumeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osldVolumeSerialNumber.setStatus("current")
_Win32MappedLogicalDiskTable_Object = MibTable
win32MappedLogicalDiskTable = _Win32MappedLogicalDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3)
)
if mibBuilder.loadTexts:
    win32MappedLogicalDiskTable.setStatus("current")
_Win32MappedLogicalDiskEntry_Object = MibTableRow
win32MappedLogicalDiskEntry = _Win32MappedLogicalDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1)
)
win32MappedLogicalDiskEntry.setIndexNames(
    (0, "INFORMANT-OS", "osmldIndex"),
)
if mibBuilder.loadTexts:
    win32MappedLogicalDiskEntry.setStatus("current")


class _OsmldIndex_Type(Integer32):
    """Custom type osmldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsmldIndex_Type.__name__ = "Integer32"
_OsmldIndex_Object = MibTableColumn
osmldIndex = _OsmldIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 1),
    _OsmldIndex_Type()
)
osmldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldIndex.setStatus("current")


class _OsmldAccess_Type(Integer32):
    """Custom type osmldAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("readWriteSupported", 3),
          ("readable", 1),
          ("unknown", 0),
          ("writeOnce", 4),
          ("writeable", 2))
    )


_OsmldAccess_Type.__name__ = "Integer32"
_OsmldAccess_Object = MibTableColumn
osmldAccess = _OsmldAccess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 2),
    _OsmldAccess_Type()
)
osmldAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldAccess.setStatus("current")


class _OsmldAvailability_Type(Integer32):
    """Custom type osmldAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 10),
          ("inTest", 5),
          ("installError", 12),
          ("notApplicable", 6),
          ("notInstalled", 11),
          ("offDuty", 9),
          ("offLine", 8),
          ("other", 1),
          ("powerCycle", 16),
          ("powerOff", 7),
          ("powerSaveLowPowerMode", 14),
          ("powerSaveStandby", 15),
          ("powerSaveUnknown", 13),
          ("powerSaveWarning", 17),
          ("runningFullPower", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OsmldAvailability_Type.__name__ = "Integer32"
_OsmldAvailability_Object = MibTableColumn
osmldAvailability = _OsmldAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 3),
    _OsmldAvailability_Type()
)
osmldAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldAvailability.setStatus("current")
_OsmldBlockSize_Type = Gauge32
_OsmldBlockSize_Object = MibTableColumn
osmldBlockSize = _OsmldBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 4),
    _OsmldBlockSize_Type()
)
osmldBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldBlockSize.setStatus("current")
if mibBuilder.loadTexts:
    osmldBlockSize.setUnits("Bytes")
_OsmldCaption_Type = WtcsDisplayString
_OsmldCaption_Object = MibTableColumn
osmldCaption = _OsmldCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 5),
    _OsmldCaption_Type()
)
osmldCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldCaption.setStatus("current")
_OsmldCompressed_Type = TruthValue
_OsmldCompressed_Object = MibTableColumn
osmldCompressed = _OsmldCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 6),
    _OsmldCompressed_Type()
)
osmldCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldCompressed.setStatus("current")


class _OsmldConfigManagerErrorCode_Type(Integer32):
    """Custom type osmldConfigManagerErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("bootConflicts", 6),
          ("cannotFilter", 7),
          ("cannotIdentify", 16),
          ("cannotLoad", 2),
          ("cannotLoadDrivers", 31),
          ("cannotStart", 10),
          ("cannotVerifyResources", 13),
          ("conflictIRQ", 30),
          ("deviceDisabled", 22),
          ("deviceFailed", 11),
          ("deviceProblem", 24),
          ("driverCorrupted", 4),
          ("driverLoaderMissing", 8),
          ("driversNotInstalled", 28),
          ("failedVXDloader", 19),
          ("invalidLogConfiguration", 27),
          ("lowResource", 3),
          ("missingResources", 29),
          ("needResource", 5),
          ("noFreeResources", 12),
          ("notConfigured", 1),
          ("reenumerationProblem", 15),
          ("registryCorrupted", 20),
          ("reinstallDrivers", 18),
          ("resourceIncorrect", 9),
          ("restartComputer", 14),
          ("settingUpDevice", 25),
          ("settingUpDevice2", 26),
          ("systemFailuer2", 23),
          ("systemFailure", 21),
          ("unknownResourceType", 17),
          ("workingProperly", 0))
    )


_OsmldConfigManagerErrorCode_Type.__name__ = "Integer32"
_OsmldConfigManagerErrorCode_Object = MibTableColumn
osmldConfigManagerErrorCode = _OsmldConfigManagerErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 7),
    _OsmldConfigManagerErrorCode_Type()
)
osmldConfigManagerErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldConfigManagerErrorCode.setStatus("current")
_OsmldConfigManagerUserConfig_Type = TruthValue
_OsmldConfigManagerUserConfig_Object = MibTableColumn
osmldConfigManagerUserConfig = _OsmldConfigManagerUserConfig_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 8),
    _OsmldConfigManagerUserConfig_Type()
)
osmldConfigManagerUserConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldConfigManagerUserConfig.setStatus("current")


class _OsmldCreationClassName_Type(WtcsDisplayString):
    """Custom type osmldCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsmldCreationClassName_Type.__name__ = "WtcsDisplayString"
_OsmldCreationClassName_Object = MibTableColumn
osmldCreationClassName = _OsmldCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 9),
    _OsmldCreationClassName_Type()
)
osmldCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldCreationClassName.setStatus("current")
_OsmldDescription_Type = WtcsDisplayString
_OsmldDescription_Object = MibTableColumn
osmldDescription = _OsmldDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 10),
    _OsmldDescription_Type()
)
osmldDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldDescription.setStatus("current")
_OsmldDeviceID_Type = WtcsDisplayString
_OsmldDeviceID_Object = MibTableColumn
osmldDeviceID = _OsmldDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 11),
    _OsmldDeviceID_Type()
)
osmldDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldDeviceID.setStatus("current")
_OsmldErrorCleared_Type = TruthValue
_OsmldErrorCleared_Object = MibTableColumn
osmldErrorCleared = _OsmldErrorCleared_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 12),
    _OsmldErrorCleared_Type()
)
osmldErrorCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldErrorCleared.setStatus("current")
_OsmldErrorDescription_Type = WtcsDisplayString
_OsmldErrorDescription_Object = MibTableColumn
osmldErrorDescription = _OsmldErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 13),
    _OsmldErrorDescription_Type()
)
osmldErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldErrorDescription.setStatus("current")
_OsmldErrorMethodology_Type = WtcsDisplayString
_OsmldErrorMethodology_Object = MibTableColumn
osmldErrorMethodology = _OsmldErrorMethodology_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 14),
    _OsmldErrorMethodology_Type()
)
osmldErrorMethodology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldErrorMethodology.setStatus("current")
_OsmldFileSystem_Type = WtcsDisplayString
_OsmldFileSystem_Object = MibTableColumn
osmldFileSystem = _OsmldFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 15),
    _OsmldFileSystem_Type()
)
osmldFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldFileSystem.setStatus("current")
_OsmldFreeSpace_Type = Gauge32
_OsmldFreeSpace_Object = MibTableColumn
osmldFreeSpace = _OsmldFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 16),
    _OsmldFreeSpace_Type()
)
osmldFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    osmldFreeSpace.setUnits("Bytes")
_OsmldInstallDate_Type = DateAndTime
_OsmldInstallDate_Object = MibTableColumn
osmldInstallDate = _OsmldInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 17),
    _OsmldInstallDate_Type()
)
osmldInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldInstallDate.setStatus("current")
_OsmldLastErrorCode_Type = Gauge32
_OsmldLastErrorCode_Object = MibTableColumn
osmldLastErrorCode = _OsmldLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 18),
    _OsmldLastErrorCode_Type()
)
osmldLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldLastErrorCode.setStatus("current")
_OsmldMaximumComponentLength_Type = Gauge32
_OsmldMaximumComponentLength_Object = MibTableColumn
osmldMaximumComponentLength = _OsmldMaximumComponentLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 19),
    _OsmldMaximumComponentLength_Type()
)
osmldMaximumComponentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldMaximumComponentLength.setStatus("current")
_OsmldName_Type = WtcsDisplayString
_OsmldName_Object = MibTableColumn
osmldName = _OsmldName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 20),
    _OsmldName_Type()
)
osmldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldName.setStatus("current")
_OsmldNumberOfBlocks_Type = Gauge32
_OsmldNumberOfBlocks_Object = MibTableColumn
osmldNumberOfBlocks = _OsmldNumberOfBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 21),
    _OsmldNumberOfBlocks_Type()
)
osmldNumberOfBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldNumberOfBlocks.setStatus("current")
_OsmldPNPDeviceID_Type = WtcsDisplayString
_OsmldPNPDeviceID_Object = MibTableColumn
osmldPNPDeviceID = _OsmldPNPDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 22),
    _OsmldPNPDeviceID_Type()
)
osmldPNPDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldPNPDeviceID.setStatus("current")


class _OsmldPowerManagementCapabilities_Type(Integer32):
    """Custom type osmldPowerManagementCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1),
          ("powerCyclingSupported", 6),
          ("powerSavingModesEnterAutomatic", 4),
          ("powerStateSettable", 5),
          ("timedPowerOnSupported", 7),
          ("unknown", 0))
    )


_OsmldPowerManagementCapabilities_Type.__name__ = "Integer32"
_OsmldPowerManagementCapabilities_Object = MibTableColumn
osmldPowerManagementCapabilities = _OsmldPowerManagementCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 23),
    _OsmldPowerManagementCapabilities_Type()
)
osmldPowerManagementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldPowerManagementCapabilities.setStatus("current")
_OsmldPowerManagementSupported_Type = TruthValue
_OsmldPowerManagementSupported_Object = MibTableColumn
osmldPowerManagementSupported = _OsmldPowerManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 24),
    _OsmldPowerManagementSupported_Type()
)
osmldPowerManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldPowerManagementSupported.setStatus("current")
_OsmldProviderName_Type = WtcsDisplayString
_OsmldProviderName_Object = MibTableColumn
osmldProviderName = _OsmldProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 25),
    _OsmldProviderName_Type()
)
osmldProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldProviderName.setStatus("current")
_OsmldPurpose_Type = WtcsDisplayString
_OsmldPurpose_Object = MibTableColumn
osmldPurpose = _OsmldPurpose_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 26),
    _OsmldPurpose_Type()
)
osmldPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldPurpose.setStatus("current")
_OsmldQuotasDisabled_Type = TruthValue
_OsmldQuotasDisabled_Object = MibTableColumn
osmldQuotasDisabled = _OsmldQuotasDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 27),
    _OsmldQuotasDisabled_Type()
)
osmldQuotasDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldQuotasDisabled.setStatus("current")
_OsmldQuotasIncomplete_Type = TruthValue
_OsmldQuotasIncomplete_Object = MibTableColumn
osmldQuotasIncomplete = _OsmldQuotasIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 28),
    _OsmldQuotasIncomplete_Type()
)
osmldQuotasIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldQuotasIncomplete.setStatus("current")
_OsmldQuotasRebuilding_Type = TruthValue
_OsmldQuotasRebuilding_Object = MibTableColumn
osmldQuotasRebuilding = _OsmldQuotasRebuilding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 29),
    _OsmldQuotasRebuilding_Type()
)
osmldQuotasRebuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldQuotasRebuilding.setStatus("current")
_OsmldSessionID_Type = WtcsDisplayString
_OsmldSessionID_Object = MibTableColumn
osmldSessionID = _OsmldSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 30),
    _OsmldSessionID_Type()
)
osmldSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSessionID.setStatus("current")
_OsmldSize_Type = Gauge32
_OsmldSize_Object = MibTableColumn
osmldSize = _OsmldSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 31),
    _OsmldSize_Type()
)
osmldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSize.setStatus("current")
if mibBuilder.loadTexts:
    osmldSize.setUnits("Bytes")


class _OsmldStatus_Type(Integer32):
    """Custom type osmldStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsmldStatus_Type.__name__ = "Integer32"
_OsmldStatus_Object = MibTableColumn
osmldStatus = _OsmldStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 32),
    _OsmldStatus_Type()
)
osmldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldStatus.setStatus("current")


class _OsmldStatusInfo_Type(Integer32):
    """Custom type osmldStatusInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3),
          ("notApplicable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OsmldStatusInfo_Type.__name__ = "Integer32"
_OsmldStatusInfo_Object = MibTableColumn
osmldStatusInfo = _OsmldStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 33),
    _OsmldStatusInfo_Type()
)
osmldStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldStatusInfo.setStatus("current")
_OsmldSupportsDiskQuotas_Type = TruthValue
_OsmldSupportsDiskQuotas_Object = MibTableColumn
osmldSupportsDiskQuotas = _OsmldSupportsDiskQuotas_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 34),
    _OsmldSupportsDiskQuotas_Type()
)
osmldSupportsDiskQuotas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSupportsDiskQuotas.setStatus("current")
_OsmldSupportFileBasedCompression_Type = TruthValue
_OsmldSupportFileBasedCompression_Object = MibTableColumn
osmldSupportFileBasedCompression = _OsmldSupportFileBasedCompression_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 35),
    _OsmldSupportFileBasedCompression_Type()
)
osmldSupportFileBasedCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSupportFileBasedCompression.setStatus("current")
_OsmldSystemCreationClassName_Type = WtcsDisplayString
_OsmldSystemCreationClassName_Object = MibTableColumn
osmldSystemCreationClassName = _OsmldSystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 36),
    _OsmldSystemCreationClassName_Type()
)
osmldSystemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSystemCreationClassName.setStatus("current")
_OsmldSystemName_Type = WtcsDisplayString
_OsmldSystemName_Object = MibTableColumn
osmldSystemName = _OsmldSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 37),
    _OsmldSystemName_Type()
)
osmldSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldSystemName.setStatus("current")
_OsmldVolumeName_Type = WtcsDisplayString
_OsmldVolumeName_Object = MibTableColumn
osmldVolumeName = _OsmldVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 38),
    _OsmldVolumeName_Type()
)
osmldVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldVolumeName.setStatus("current")
_OsmldVolumeSerialNumber_Type = WtcsDisplayString
_OsmldVolumeSerialNumber_Object = MibTableColumn
osmldVolumeSerialNumber = _OsmldVolumeSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 3, 1, 39),
    _OsmldVolumeSerialNumber_Type()
)
osmldVolumeSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osmldVolumeSerialNumber.setStatus("current")
_Win32QuotaSettingTable_Object = MibTable
win32QuotaSettingTable = _Win32QuotaSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4)
)
if mibBuilder.loadTexts:
    win32QuotaSettingTable.setStatus("current")
_Win32QuotaSettingEntry_Object = MibTableRow
win32QuotaSettingEntry = _Win32QuotaSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1)
)
win32QuotaSettingEntry.setIndexNames(
    (0, "INFORMANT-OS", "osqsIndex"),
)
if mibBuilder.loadTexts:
    win32QuotaSettingEntry.setStatus("current")


class _OsqsIndex_Type(Integer32):
    """Custom type osqsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsqsIndex_Type.__name__ = "Integer32"
_OsqsIndex_Object = MibTableColumn
osqsIndex = _OsqsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 1),
    _OsqsIndex_Type()
)
osqsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsIndex.setStatus("current")


class _OsqsCaption_Type(WtcsDisplayString):
    """Custom type osqsCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsqsCaption_Type.__name__ = "WtcsDisplayString"
_OsqsCaption_Object = MibTableColumn
osqsCaption = _OsqsCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 2),
    _OsqsCaption_Type()
)
osqsCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsCaption.setStatus("current")
_OsqsDefaultLimit_Type = WtcsDisplayString
_OsqsDefaultLimit_Object = MibTableColumn
osqsDefaultLimit = _OsqsDefaultLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 3),
    _OsqsDefaultLimit_Type()
)
osqsDefaultLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsDefaultLimit.setStatus("current")
if mibBuilder.loadTexts:
    osqsDefaultLimit.setUnits("Bytes")
_OsqsDefaultWarningLimit_Type = WtcsDisplayString
_OsqsDefaultWarningLimit_Object = MibTableColumn
osqsDefaultWarningLimit = _OsqsDefaultWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 4),
    _OsqsDefaultWarningLimit_Type()
)
osqsDefaultWarningLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsDefaultWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    osqsDefaultWarningLimit.setUnits("Bytes")
_OsqsDescription_Type = WtcsDisplayString
_OsqsDescription_Object = MibTableColumn
osqsDescription = _OsqsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 5),
    _OsqsDescription_Type()
)
osqsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsDescription.setStatus("current")
_OsqsExceededNotification_Type = TruthValue
_OsqsExceededNotification_Object = MibTableColumn
osqsExceededNotification = _OsqsExceededNotification_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 6),
    _OsqsExceededNotification_Type()
)
osqsExceededNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsExceededNotification.setStatus("current")


class _OsqsSettingID_Type(WtcsDisplayString):
    """Custom type osqsSettingID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsqsSettingID_Type.__name__ = "WtcsDisplayString"
_OsqsSettingID_Object = MibTableColumn
osqsSettingID = _OsqsSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 7),
    _OsqsSettingID_Type()
)
osqsSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsSettingID.setStatus("current")


class _OsqsState_Type(Integer32):
    """Custom type osqsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enforced", 2),
          ("tracked", 1))
    )


_OsqsState_Type.__name__ = "Integer32"
_OsqsState_Object = MibTableColumn
osqsState = _OsqsState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 8),
    _OsqsState_Type()
)
osqsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsState.setStatus("current")
_OsqsVolumePath_Type = WtcsDisplayString
_OsqsVolumePath_Object = MibTableColumn
osqsVolumePath = _OsqsVolumePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 9),
    _OsqsVolumePath_Type()
)
osqsVolumePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsVolumePath.setStatus("current")
_OsqsWarningExceededNotification_Type = TruthValue
_OsqsWarningExceededNotification_Object = MibTableColumn
osqsWarningExceededNotification = _OsqsWarningExceededNotification_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 4, 1, 10),
    _OsqsWarningExceededNotification_Type()
)
osqsWarningExceededNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqsWarningExceededNotification.setStatus("current")
_Win32VolumeTable_Object = MibTable
win32VolumeTable = _Win32VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5)
)
if mibBuilder.loadTexts:
    win32VolumeTable.setStatus("current")
_Win32VolumeEntry_Object = MibTableRow
win32VolumeEntry = _Win32VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1)
)
win32VolumeEntry.setIndexNames(
    (0, "INFORMANT-OS", "osvlIndex"),
)
if mibBuilder.loadTexts:
    win32VolumeEntry.setStatus("current")


class _OsvlIndex_Type(Integer32):
    """Custom type osvlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsvlIndex_Type.__name__ = "Integer32"
_OsvlIndex_Object = MibTableColumn
osvlIndex = _OsvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 1),
    _OsvlIndex_Type()
)
osvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlIndex.setStatus("current")
_OsvlAutomount_Type = TruthValue
_OsvlAutomount_Object = MibTableColumn
osvlAutomount = _OsvlAutomount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 2),
    _OsvlAutomount_Type()
)
osvlAutomount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlAutomount.setStatus("current")
_OsvlCapacity_Type = WtcsDisplayString
_OsvlCapacity_Object = MibTableColumn
osvlCapacity = _OsvlCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 3),
    _OsvlCapacity_Type()
)
osvlCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlCapacity.setStatus("current")
_OsvlCompressed_Type = TruthValue
_OsvlCompressed_Object = MibTableColumn
osvlCompressed = _OsvlCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 4),
    _OsvlCompressed_Type()
)
osvlCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlCompressed.setStatus("current")
_OsvlDeviceId_Type = WtcsDisplayString
_OsvlDeviceId_Object = MibTableColumn
osvlDeviceId = _OsvlDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 5),
    _OsvlDeviceId_Type()
)
osvlDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlDeviceId.setStatus("current")
_OsvlDirtyBitSet_Type = TruthValue
_OsvlDirtyBitSet_Object = MibTableColumn
osvlDirtyBitSet = _OsvlDirtyBitSet_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 6),
    _OsvlDirtyBitSet_Type()
)
osvlDirtyBitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlDirtyBitSet.setStatus("current")
_OsvlDriveLetter_Type = WtcsDisplayString
_OsvlDriveLetter_Object = MibTableColumn
osvlDriveLetter = _OsvlDriveLetter_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 7),
    _OsvlDriveLetter_Type()
)
osvlDriveLetter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlDriveLetter.setStatus("current")


class _OsvlDriveType_Type(Integer32):
    """Custom type osvlDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compactDisk", 5),
          ("localDisk", 3),
          ("networkDrive", 4),
          ("noRootDirectory", 1),
          ("ramDisk", 6),
          ("removableDisk", 2),
          ("unknown", 0))
    )


_OsvlDriveType_Type.__name__ = "Integer32"
_OsvlDriveType_Object = MibTableColumn
osvlDriveType = _OsvlDriveType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 8),
    _OsvlDriveType_Type()
)
osvlDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlDriveType.setStatus("current")
_OsvlFileSystem_Type = WtcsDisplayString
_OsvlFileSystem_Object = MibTableColumn
osvlFileSystem = _OsvlFileSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 9),
    _OsvlFileSystem_Type()
)
osvlFileSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlFileSystem.setStatus("current")
_OsvlFreeSpace_Type = WtcsDisplayString
_OsvlFreeSpace_Object = MibTableColumn
osvlFreeSpace = _OsvlFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 10),
    _OsvlFreeSpace_Type()
)
osvlFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlFreeSpace.setStatus("current")
_OsvlIndexingEnabled_Type = TruthValue
_OsvlIndexingEnabled_Object = MibTableColumn
osvlIndexingEnabled = _OsvlIndexingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 11),
    _OsvlIndexingEnabled_Type()
)
osvlIndexingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlIndexingEnabled.setStatus("current")
_OsvlLabel_Type = WtcsDisplayString
_OsvlLabel_Object = MibTableColumn
osvlLabel = _OsvlLabel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 12),
    _OsvlLabel_Type()
)
osvlLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlLabel.setStatus("current")
_OsvlMaximumFileNameLength_Type = Gauge32
_OsvlMaximumFileNameLength_Object = MibTableColumn
osvlMaximumFileNameLength = _OsvlMaximumFileNameLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 13),
    _OsvlMaximumFileNameLength_Type()
)
osvlMaximumFileNameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlMaximumFileNameLength.setStatus("current")
_OsvlQuotasEnabled_Type = TruthValue
_OsvlQuotasEnabled_Object = MibTableColumn
osvlQuotasEnabled = _OsvlQuotasEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 14),
    _OsvlQuotasEnabled_Type()
)
osvlQuotasEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlQuotasEnabled.setStatus("current")
_OsvlQuotasIncomplete_Type = TruthValue
_OsvlQuotasIncomplete_Object = MibTableColumn
osvlQuotasIncomplete = _OsvlQuotasIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 15),
    _OsvlQuotasIncomplete_Type()
)
osvlQuotasIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlQuotasIncomplete.setStatus("current")
_OsvlQuotasRebuilding_Type = TruthValue
_OsvlQuotasRebuilding_Object = MibTableColumn
osvlQuotasRebuilding = _OsvlQuotasRebuilding_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 16),
    _OsvlQuotasRebuilding_Type()
)
osvlQuotasRebuilding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlQuotasRebuilding.setStatus("current")
_OsvlSerialNumber_Type = Gauge32
_OsvlSerialNumber_Object = MibTableColumn
osvlSerialNumber = _OsvlSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 17),
    _OsvlSerialNumber_Type()
)
osvlSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlSerialNumber.setStatus("current")
_OsvlSupportsDiskQuotas_Type = TruthValue
_OsvlSupportsDiskQuotas_Object = MibTableColumn
osvlSupportsDiskQuotas = _OsvlSupportsDiskQuotas_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 18),
    _OsvlSupportsDiskQuotas_Type()
)
osvlSupportsDiskQuotas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlSupportsDiskQuotas.setStatus("current")
_OsvlSupportsFileBasedCompression_Type = TruthValue
_OsvlSupportsFileBasedCompression_Object = MibTableColumn
osvlSupportsFileBasedCompression = _OsvlSupportsFileBasedCompression_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 3, 5, 1, 19),
    _OsvlSupportsFileBasedCompression_Type()
)
osvlSupportsFileBasedCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osvlSupportsFileBasedCompression.setStatus("current")
_WmiJobObjects_ObjectIdentity = ObjectIdentity
wmiJobObjects = _WmiJobObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4)
)
if mibBuilder.loadTexts:
    wmiJobObjects.setStatus("current")
_Win32NamedJobObjectTable_Object = MibTable
win32NamedJobObjectTable = _Win32NamedJobObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1)
)
if mibBuilder.loadTexts:
    win32NamedJobObjectTable.setStatus("current")
_Win32NamedJobObjectEntry_Object = MibTableRow
win32NamedJobObjectEntry = _Win32NamedJobObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1)
)
win32NamedJobObjectEntry.setIndexNames(
    (0, "INFORMANT-OS", "osnjoIndex"),
)
if mibBuilder.loadTexts:
    win32NamedJobObjectEntry.setStatus("current")


class _OsnjoIndex_Type(Integer32):
    """Custom type osnjoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsnjoIndex_Type.__name__ = "Integer32"
_OsnjoIndex_Object = MibTableColumn
osnjoIndex = _OsnjoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1, 1),
    _OsnjoIndex_Type()
)
osnjoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnjoIndex.setStatus("current")


class _OsnjoBasicUIRestrictions_Type(Integer32):
    """Custom type osnjoBasicUIRestrictions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("desktop", 1),
          ("displaySettings", 2),
          ("exitWindows", 4),
          ("globalAtoms", 8),
          ("handles", 16),
          ("readClipboard", 32),
          ("systemParameters", 64),
          ("writeClipboard", 128))
    )


_OsnjoBasicUIRestrictions_Type.__name__ = "Integer32"
_OsnjoBasicUIRestrictions_Object = MibTableColumn
osnjoBasicUIRestrictions = _OsnjoBasicUIRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1, 2),
    _OsnjoBasicUIRestrictions_Type()
)
osnjoBasicUIRestrictions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnjoBasicUIRestrictions.setStatus("current")


class _OsnjoCaption_Type(WtcsDisplayString):
    """Custom type osnjoCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsnjoCaption_Type.__name__ = "WtcsDisplayString"
_OsnjoCaption_Object = MibTableColumn
osnjoCaption = _OsnjoCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1, 3),
    _OsnjoCaption_Type()
)
osnjoCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnjoCaption.setStatus("current")


class _OsnjoCollectionID_Type(WtcsDisplayString):
    """Custom type osnjoCollectionID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsnjoCollectionID_Type.__name__ = "WtcsDisplayString"
_OsnjoCollectionID_Object = MibTableColumn
osnjoCollectionID = _OsnjoCollectionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1, 4),
    _OsnjoCollectionID_Type()
)
osnjoCollectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnjoCollectionID.setStatus("current")
_OsnjoDescription_Type = WtcsDisplayString
_OsnjoDescription_Object = MibTableColumn
osnjoDescription = _OsnjoDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 1, 1, 5),
    _OsnjoDescription_Type()
)
osnjoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnjoDescription.setStatus("current")
_Win32NamedJobObjectActgInfoTable_Object = MibTable
win32NamedJobObjectActgInfoTable = _Win32NamedJobObjectActgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2)
)
if mibBuilder.loadTexts:
    win32NamedJobObjectActgInfoTable.setStatus("current")
_Win32NamedJobObjectActgInfoEntry_Object = MibTableRow
win32NamedJobObjectActgInfoEntry = _Win32NamedJobObjectActgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1)
)
win32NamedJobObjectActgInfoEntry.setIndexNames(
    (0, "INFORMANT-OS", "osjoaIndex"),
)
if mibBuilder.loadTexts:
    win32NamedJobObjectActgInfoEntry.setStatus("current")


class _OsjoaIndex_Type(Integer32):
    """Custom type osjoaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsjoaIndex_Type.__name__ = "Integer32"
_OsjoaIndex_Object = MibTableColumn
osjoaIndex = _OsjoaIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 1),
    _OsjoaIndex_Type()
)
osjoaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaIndex.setStatus("current")
_OsjoaActiveProcesses_Type = Gauge32
_OsjoaActiveProcesses_Object = MibTableColumn
osjoaActiveProcesses = _OsjoaActiveProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 2),
    _OsjoaActiveProcesses_Type()
)
osjoaActiveProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaActiveProcesses.setStatus("current")


class _OsjoaCaption_Type(WtcsDisplayString):
    """Custom type osjoaCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsjoaCaption_Type.__name__ = "WtcsDisplayString"
_OsjoaCaption_Object = MibTableColumn
osjoaCaption = _OsjoaCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 3),
    _OsjoaCaption_Type()
)
osjoaCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaCaption.setStatus("current")
_OsjoaDescription_Type = WtcsDisplayString
_OsjoaDescription_Object = MibTableColumn
osjoaDescription = _OsjoaDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 4),
    _OsjoaDescription_Type()
)
osjoaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaDescription.setStatus("current")


class _OsjoaName_Type(WtcsDisplayString):
    """Custom type osjoaName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsjoaName_Type.__name__ = "WtcsDisplayString"
_OsjoaName_Object = MibTableColumn
osjoaName = _OsjoaName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 5),
    _OsjoaName_Type()
)
osjoaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaName.setStatus("current")
_OsjoaOtherOperationCount_Type = Gauge32
_OsjoaOtherOperationCount_Object = MibTableColumn
osjoaOtherOperationCount = _OsjoaOtherOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 6),
    _OsjoaOtherOperationCount_Type()
)
osjoaOtherOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaOtherOperationCount.setStatus("current")
_OsjoaOtherTransferCount_Type = Gauge32
_OsjoaOtherTransferCount_Object = MibTableColumn
osjoaOtherTransferCount = _OsjoaOtherTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 7),
    _OsjoaOtherTransferCount_Type()
)
osjoaOtherTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaOtherTransferCount.setStatus("current")
_OsjoaPeakJobMemoryUsed_Type = Gauge32
_OsjoaPeakJobMemoryUsed_Object = MibTableColumn
osjoaPeakJobMemoryUsed = _OsjoaPeakJobMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 8),
    _OsjoaPeakJobMemoryUsed_Type()
)
osjoaPeakJobMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaPeakJobMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    osjoaPeakJobMemoryUsed.setUnits("KB")
_OsjoaPeakProcessMemoryUsed_Type = Gauge32
_OsjoaPeakProcessMemoryUsed_Object = MibTableColumn
osjoaPeakProcessMemoryUsed = _OsjoaPeakProcessMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 9),
    _OsjoaPeakProcessMemoryUsed_Type()
)
osjoaPeakProcessMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaPeakProcessMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    osjoaPeakProcessMemoryUsed.setUnits("KB")
_OsjoaReadOperationCount_Type = Gauge32
_OsjoaReadOperationCount_Object = MibTableColumn
osjoaReadOperationCount = _OsjoaReadOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 10),
    _OsjoaReadOperationCount_Type()
)
osjoaReadOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaReadOperationCount.setStatus("current")
_OsjoaReadTransferCount_Type = Gauge32
_OsjoaReadTransferCount_Object = MibTableColumn
osjoaReadTransferCount = _OsjoaReadTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 11),
    _OsjoaReadTransferCount_Type()
)
osjoaReadTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaReadTransferCount.setStatus("current")
_OsjoaThisPeriodTotalKernelTime_Type = WtcsDisplayString
_OsjoaThisPeriodTotalKernelTime_Object = MibTableColumn
osjoaThisPeriodTotalKernelTime = _OsjoaThisPeriodTotalKernelTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 12),
    _OsjoaThisPeriodTotalKernelTime_Type()
)
osjoaThisPeriodTotalKernelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaThisPeriodTotalKernelTime.setStatus("current")
if mibBuilder.loadTexts:
    osjoaThisPeriodTotalKernelTime.setUnits("100ns")
_OsjoaThisPeriodTotalUserTime_Type = WtcsDisplayString
_OsjoaThisPeriodTotalUserTime_Object = MibTableColumn
osjoaThisPeriodTotalUserTime = _OsjoaThisPeriodTotalUserTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 13),
    _OsjoaThisPeriodTotalUserTime_Type()
)
osjoaThisPeriodTotalUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaThisPeriodTotalUserTime.setStatus("current")
if mibBuilder.loadTexts:
    osjoaThisPeriodTotalUserTime.setUnits("100ns")
_OsjoaTotalKernelTime_Type = WtcsDisplayString
_OsjoaTotalKernelTime_Object = MibTableColumn
osjoaTotalKernelTime = _OsjoaTotalKernelTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 14),
    _OsjoaTotalKernelTime_Type()
)
osjoaTotalKernelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaTotalKernelTime.setStatus("current")
if mibBuilder.loadTexts:
    osjoaTotalKernelTime.setUnits("100ns")
_OsjoaTotalPageFaultCount_Type = Gauge32
_OsjoaTotalPageFaultCount_Object = MibTableColumn
osjoaTotalPageFaultCount = _OsjoaTotalPageFaultCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 15),
    _OsjoaTotalPageFaultCount_Type()
)
osjoaTotalPageFaultCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaTotalPageFaultCount.setStatus("current")
_OsjoaTotalProcesses_Type = Gauge32
_OsjoaTotalProcesses_Object = MibTableColumn
osjoaTotalProcesses = _OsjoaTotalProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 16),
    _OsjoaTotalProcesses_Type()
)
osjoaTotalProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaTotalProcesses.setStatus("current")
_OsjoaTotalTerminatedProcesses_Type = Gauge32
_OsjoaTotalTerminatedProcesses_Object = MibTableColumn
osjoaTotalTerminatedProcesses = _OsjoaTotalTerminatedProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 17),
    _OsjoaTotalTerminatedProcesses_Type()
)
osjoaTotalTerminatedProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaTotalTerminatedProcesses.setStatus("current")
_OsjoaTotalUserTime_Type = WtcsDisplayString
_OsjoaTotalUserTime_Object = MibTableColumn
osjoaTotalUserTime = _OsjoaTotalUserTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 18),
    _OsjoaTotalUserTime_Type()
)
osjoaTotalUserTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaTotalUserTime.setStatus("current")
if mibBuilder.loadTexts:
    osjoaTotalUserTime.setUnits("100ns")
_OsjoaWriteOperationCount_Type = Gauge32
_OsjoaWriteOperationCount_Object = MibTableColumn
osjoaWriteOperationCount = _OsjoaWriteOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 19),
    _OsjoaWriteOperationCount_Type()
)
osjoaWriteOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaWriteOperationCount.setStatus("current")
_OsjoaWriteTransferCount_Type = Gauge32
_OsjoaWriteTransferCount_Object = MibTableColumn
osjoaWriteTransferCount = _OsjoaWriteTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 2, 1, 20),
    _OsjoaWriteTransferCount_Type()
)
osjoaWriteTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjoaWriteTransferCount.setStatus("current")
_Win32NamedJobObjectLimitSetTable_Object = MibTable
win32NamedJobObjectLimitSetTable = _Win32NamedJobObjectLimitSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3)
)
if mibBuilder.loadTexts:
    win32NamedJobObjectLimitSetTable.setStatus("current")
_Win32NamedJobObjectLimitSetEntry_Object = MibTableRow
win32NamedJobObjectLimitSetEntry = _Win32NamedJobObjectLimitSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1)
)
win32NamedJobObjectLimitSetEntry.setIndexNames(
    (0, "INFORMANT-OS", "osjolIndex"),
)
if mibBuilder.loadTexts:
    win32NamedJobObjectLimitSetEntry.setStatus("current")


class _OsjolIndex_Type(Integer32):
    """Custom type osjolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsjolIndex_Type.__name__ = "Integer32"
_OsjolIndex_Object = MibTableColumn
osjolIndex = _OsjolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 1),
    _OsjolIndex_Type()
)
osjolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolIndex.setStatus("current")
_OsjolActiveProcessLimit_Type = Gauge32
_OsjolActiveProcessLimit_Object = MibTableColumn
osjolActiveProcessLimit = _OsjolActiveProcessLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 2),
    _OsjolActiveProcessLimit_Type()
)
osjolActiveProcessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolActiveProcessLimit.setStatus("current")
_OsjolAffinity_Type = Gauge32
_OsjolAffinity_Object = MibTableColumn
osjolAffinity = _OsjolAffinity_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 3),
    _OsjolAffinity_Type()
)
osjolAffinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolAffinity.setStatus("current")


class _OsjolCaption_Type(WtcsDisplayString):
    """Custom type osjolCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsjolCaption_Type.__name__ = "WtcsDisplayString"
_OsjolCaption_Object = MibTableColumn
osjolCaption = _OsjolCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 4),
    _OsjolCaption_Type()
)
osjolCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolCaption.setStatus("current")
_OsjolDescription_Type = WtcsDisplayString
_OsjolDescription_Object = MibTableColumn
osjolDescription = _OsjolDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 5),
    _OsjolDescription_Type()
)
osjolDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolDescription.setStatus("current")
_OsjolJobMemoryLimit_Type = Gauge32
_OsjolJobMemoryLimit_Object = MibTableColumn
osjolJobMemoryLimit = _OsjolJobMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 6),
    _OsjolJobMemoryLimit_Type()
)
osjolJobMemoryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolJobMemoryLimit.setStatus("current")


class _OsjolLimitFlags_Type(Integer32):
    """Custom type osjolLimitFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("activeProcessLimit", 8),
          ("limitAffinity", 16),
          ("limitBreakawayOK", 2048),
          ("limitDieOnUnhandledException", 1024),
          ("limitJobMemory", 512),
          ("limitJobTime", 4),
          ("limitPreserveJobTime", 64),
          ("limitPriorityClass", 32),
          ("limitProcessMemory", 256),
          ("limitProcessTime", 2),
          ("limitSchedulingClass", 128),
          ("limitWorkingSet", 1),
          ("silentBreakawayOK", 4096))
    )


_OsjolLimitFlags_Type.__name__ = "Integer32"
_OsjolLimitFlags_Object = MibTableColumn
osjolLimitFlags = _OsjolLimitFlags_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 7),
    _OsjolLimitFlags_Type()
)
osjolLimitFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolLimitFlags.setStatus("current")
_OsjolMaximumWorkingSetSize_Type = Gauge32
_OsjolMaximumWorkingSetSize_Object = MibTableColumn
osjolMaximumWorkingSetSize = _OsjolMaximumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 8),
    _OsjolMaximumWorkingSetSize_Type()
)
osjolMaximumWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolMaximumWorkingSetSize.setStatus("current")
_OsjolMinimumWorkingSetSize_Type = Gauge32
_OsjolMinimumWorkingSetSize_Object = MibTableColumn
osjolMinimumWorkingSetSize = _OsjolMinimumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 9),
    _OsjolMinimumWorkingSetSize_Type()
)
osjolMinimumWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolMinimumWorkingSetSize.setStatus("current")
_OsjolPerJobUserTimeLimit_Type = WtcsDisplayString
_OsjolPerJobUserTimeLimit_Object = MibTableColumn
osjolPerJobUserTimeLimit = _OsjolPerJobUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 10),
    _OsjolPerJobUserTimeLimit_Type()
)
osjolPerJobUserTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolPerJobUserTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    osjolPerJobUserTimeLimit.setUnits("100ns")
_OsjolPerProcessUserTimeLimit_Type = WtcsDisplayString
_OsjolPerProcessUserTimeLimit_Object = MibTableColumn
osjolPerProcessUserTimeLimit = _OsjolPerProcessUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 11),
    _OsjolPerProcessUserTimeLimit_Type()
)
osjolPerProcessUserTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolPerProcessUserTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    osjolPerProcessUserTimeLimit.setUnits("100ns")
_OsjolPriorityClass_Type = Gauge32
_OsjolPriorityClass_Object = MibTableColumn
osjolPriorityClass = _OsjolPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 12),
    _OsjolPriorityClass_Type()
)
osjolPriorityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolPriorityClass.setStatus("current")
_OsjolProcessMemoryLimit_Type = Gauge32
_OsjolProcessMemoryLimit_Object = MibTableColumn
osjolProcessMemoryLimit = _OsjolProcessMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 13),
    _OsjolProcessMemoryLimit_Type()
)
osjolProcessMemoryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolProcessMemoryLimit.setStatus("current")
_OsjolSchedulingClass_Type = Gauge32
_OsjolSchedulingClass_Object = MibTableColumn
osjolSchedulingClass = _OsjolSchedulingClass_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 14),
    _OsjolSchedulingClass_Type()
)
osjolSchedulingClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolSchedulingClass.setStatus("current")


class _OsjolSettingID_Type(WtcsDisplayString):
    """Custom type osjolSettingID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsjolSettingID_Type.__name__ = "WtcsDisplayString"
_OsjolSettingID_Object = MibTableColumn
osjolSettingID = _OsjolSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 4, 3, 1, 15),
    _OsjolSettingID_Type()
)
osjolSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osjolSettingID.setStatus("current")
_WmiPageFiles_ObjectIdentity = ObjectIdentity
wmiPageFiles = _WmiPageFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5)
)
if mibBuilder.loadTexts:
    wmiPageFiles.setStatus("current")
_Win32PageFileTable_Object = MibTable
win32PageFileTable = _Win32PageFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1)
)
if mibBuilder.loadTexts:
    win32PageFileTable.setStatus("current")
_Win32PageFileEntry_Object = MibTableRow
win32PageFileEntry = _Win32PageFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1)
)
win32PageFileEntry.setIndexNames(
    (0, "INFORMANT-OS", "ospfIndex"),
)
if mibBuilder.loadTexts:
    win32PageFileEntry.setStatus("current")


class _OspfIndex_Type(Integer32):
    """Custom type ospfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspfIndex_Type.__name__ = "Integer32"
_OspfIndex_Object = MibTableColumn
ospfIndex = _OspfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 1),
    _OspfIndex_Type()
)
ospfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIndex.setStatus("current")
_OspfAccessMask_Type = WtcsDisplayString
_OspfAccessMask_Object = MibTableColumn
ospfAccessMask = _OspfAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 2),
    _OspfAccessMask_Type()
)
ospfAccessMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAccessMask.setStatus("current")
_OspfArchive_Type = TruthValue
_OspfArchive_Object = MibTableColumn
ospfArchive = _OspfArchive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 3),
    _OspfArchive_Type()
)
ospfArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfArchive.setStatus("current")
_OspfCaption_Type = WtcsDisplayString
_OspfCaption_Object = MibTableColumn
ospfCaption = _OspfCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 4),
    _OspfCaption_Type()
)
ospfCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCaption.setStatus("current")
_OspfCompressed_Type = TruthValue
_OspfCompressed_Object = MibTableColumn
ospfCompressed = _OspfCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 5),
    _OspfCompressed_Type()
)
ospfCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompressed.setStatus("current")
_OspfCompressionMethod_Type = WtcsDisplayString
_OspfCompressionMethod_Object = MibTableColumn
ospfCompressionMethod = _OspfCompressionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 6),
    _OspfCompressionMethod_Type()
)
ospfCompressionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompressionMethod.setStatus("current")


class _OspfCreationClassName_Type(WtcsDisplayString):
    """Custom type ospfCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfCreationClassName_Type.__name__ = "WtcsDisplayString"
_OspfCreationClassName_Object = MibTableColumn
ospfCreationClassName = _OspfCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 7),
    _OspfCreationClassName_Type()
)
ospfCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCreationClassName.setStatus("current")
_OspfCreationDate_Type = DateAndTime
_OspfCreationDate_Object = MibTableColumn
ospfCreationDate = _OspfCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 8),
    _OspfCreationDate_Type()
)
ospfCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCreationDate.setStatus("current")
_OspfCSCreationClassName_Type = WtcsDisplayString
_OspfCSCreationClassName_Object = MibTableColumn
ospfCSCreationClassName = _OspfCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 9),
    _OspfCSCreationClassName_Type()
)
ospfCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCSCreationClassName.setStatus("current")
_OspfCSName_Type = WtcsDisplayString
_OspfCSName_Object = MibTableColumn
ospfCSName = _OspfCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 10),
    _OspfCSName_Type()
)
ospfCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCSName.setStatus("current")
_OspfDescription_Type = WtcsDisplayString
_OspfDescription_Object = MibTableColumn
ospfDescription = _OspfDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 11),
    _OspfDescription_Type()
)
ospfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDescription.setStatus("current")
_OspfDrive_Type = WtcsDisplayString
_OspfDrive_Object = MibTableColumn
ospfDrive = _OspfDrive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 12),
    _OspfDrive_Type()
)
ospfDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDrive.setStatus("current")
_OspfEightDotThreeFileName_Type = WtcsDisplayString
_OspfEightDotThreeFileName_Object = MibTableColumn
ospfEightDotThreeFileName = _OspfEightDotThreeFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 13),
    _OspfEightDotThreeFileName_Type()
)
ospfEightDotThreeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfEightDotThreeFileName.setStatus("current")
_OspfEncrypted_Type = TruthValue
_OspfEncrypted_Object = MibTableColumn
ospfEncrypted = _OspfEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 14),
    _OspfEncrypted_Type()
)
ospfEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfEncrypted.setStatus("current")
_OspfEncryptionMethod_Type = WtcsDisplayString
_OspfEncryptionMethod_Object = MibTableColumn
ospfEncryptionMethod = _OspfEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 15),
    _OspfEncryptionMethod_Type()
)
ospfEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfEncryptionMethod.setStatus("current")
_OspfExtension_Type = WtcsDisplayString
_OspfExtension_Object = MibTableColumn
ospfExtension = _OspfExtension_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 16),
    _OspfExtension_Type()
)
ospfExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExtension.setStatus("current")
_OspfFileName_Type = WtcsDisplayString
_OspfFileName_Object = MibTableColumn
ospfFileName = _OspfFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 17),
    _OspfFileName_Type()
)
ospfFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFileName.setStatus("current")
_OspfFileSize_Type = Gauge32
_OspfFileSize_Object = MibTableColumn
ospfFileSize = _OspfFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 18),
    _OspfFileSize_Type()
)
ospfFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFileSize.setStatus("current")
_OspfFileType_Type = WtcsDisplayString
_OspfFileType_Object = MibTableColumn
ospfFileType = _OspfFileType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 19),
    _OspfFileType_Type()
)
ospfFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFileType.setStatus("current")
_OspfFreeSpace_Type = Gauge32
_OspfFreeSpace_Object = MibTableColumn
ospfFreeSpace = _OspfFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 20),
    _OspfFreeSpace_Type()
)
ospfFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFreeSpace.setStatus("current")
if mibBuilder.loadTexts:
    ospfFreeSpace.setUnits("Megabytes")
_OspfFSCreationClassName_Type = WtcsDisplayString
_OspfFSCreationClassName_Object = MibTableColumn
ospfFSCreationClassName = _OspfFSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 21),
    _OspfFSCreationClassName_Type()
)
ospfFSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFSCreationClassName.setStatus("current")
_OspfFSName_Type = WtcsDisplayString
_OspfFSName_Object = MibTableColumn
ospfFSName = _OspfFSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 22),
    _OspfFSName_Type()
)
ospfFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfFSName.setStatus("current")
_OspfHidden_Type = TruthValue
_OspfHidden_Object = MibTableColumn
ospfHidden = _OspfHidden_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 23),
    _OspfHidden_Type()
)
ospfHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfHidden.setStatus("current")
_OspfInitialSize_Type = Gauge32
_OspfInitialSize_Object = MibTableColumn
ospfInitialSize = _OspfInitialSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 24),
    _OspfInitialSize_Type()
)
ospfInitialSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInitialSize.setStatus("current")
if mibBuilder.loadTexts:
    ospfInitialSize.setUnits("Megabytes")
_OspfInstallDate_Type = DateAndTime
_OspfInstallDate_Object = MibTableColumn
ospfInstallDate = _OspfInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 25),
    _OspfInstallDate_Type()
)
ospfInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInstallDate.setStatus("current")
_OspfInUseCount_Type = Gauge32
_OspfInUseCount_Object = MibTableColumn
ospfInUseCount = _OspfInUseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 26),
    _OspfInUseCount_Type()
)
ospfInUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInUseCount.setStatus("current")
_OspfLastAccessed_Type = DateAndTime
_OspfLastAccessed_Object = MibTableColumn
ospfLastAccessed = _OspfLastAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 27),
    _OspfLastAccessed_Type()
)
ospfLastAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLastAccessed.setStatus("current")
_OspfLastModified_Type = DateAndTime
_OspfLastModified_Object = MibTableColumn
ospfLastModified = _OspfLastModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 28),
    _OspfLastModified_Type()
)
ospfLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLastModified.setStatus("current")
_OspfManufacturer_Type = WtcsDisplayString
_OspfManufacturer_Object = MibTableColumn
ospfManufacturer = _OspfManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 29),
    _OspfManufacturer_Type()
)
ospfManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfManufacturer.setStatus("current")
_OspfMaximumSize_Type = Gauge32
_OspfMaximumSize_Object = MibTableColumn
ospfMaximumSize = _OspfMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 30),
    _OspfMaximumSize_Type()
)
ospfMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfMaximumSize.setStatus("current")
if mibBuilder.loadTexts:
    ospfMaximumSize.setUnits("Megabytes")
_OspfName_Type = WtcsDisplayString
_OspfName_Object = MibTableColumn
ospfName = _OspfName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 31),
    _OspfName_Type()
)
ospfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfName.setStatus("current")
_OspfPath_Type = WtcsDisplayString
_OspfPath_Object = MibTableColumn
ospfPath = _OspfPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 32),
    _OspfPath_Type()
)
ospfPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfPath.setStatus("current")
_OspfReadable_Type = TruthValue
_OspfReadable_Object = MibTableColumn
ospfReadable = _OspfReadable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 33),
    _OspfReadable_Type()
)
ospfReadable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfReadable.setStatus("current")


class _OspfStatus_Type(Integer32):
    """Custom type ospfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OspfStatus_Type.__name__ = "Integer32"
_OspfStatus_Object = MibTableColumn
ospfStatus = _OspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 34),
    _OspfStatus_Type()
)
ospfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfStatus.setStatus("current")
_OspfSystem_Type = TruthValue
_OspfSystem_Object = MibTableColumn
ospfSystem = _OspfSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 35),
    _OspfSystem_Type()
)
ospfSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfSystem.setStatus("current")
_OspfVersion_Type = WtcsDisplayString
_OspfVersion_Object = MibTableColumn
ospfVersion = _OspfVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 36),
    _OspfVersion_Type()
)
ospfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVersion.setStatus("current")
_OspfWriteable_Type = TruthValue
_OspfWriteable_Object = MibTableColumn
ospfWriteable = _OspfWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 1, 1, 37),
    _OspfWriteable_Type()
)
ospfWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfWriteable.setStatus("current")
_Win32PageFileSettingTable_Object = MibTable
win32PageFileSettingTable = _Win32PageFileSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2)
)
if mibBuilder.loadTexts:
    win32PageFileSettingTable.setStatus("current")
_Win32PageFileSettingEntry_Object = MibTableRow
win32PageFileSettingEntry = _Win32PageFileSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1)
)
win32PageFileSettingEntry.setIndexNames(
    (0, "INFORMANT-OS", "ospfsIndex"),
)
if mibBuilder.loadTexts:
    win32PageFileSettingEntry.setStatus("current")


class _OspfsIndex_Type(Integer32):
    """Custom type ospfsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspfsIndex_Type.__name__ = "Integer32"
_OspfsIndex_Object = MibTableColumn
ospfsIndex = _OspfsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 1),
    _OspfsIndex_Type()
)
ospfsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsIndex.setStatus("current")
_OspfsCaption_Type = WtcsDisplayString
_OspfsCaption_Object = MibTableColumn
ospfsCaption = _OspfsCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 2),
    _OspfsCaption_Type()
)
ospfsCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsCaption.setStatus("current")
_OspfsDescription_Type = WtcsDisplayString
_OspfsDescription_Object = MibTableColumn
ospfsDescription = _OspfsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 3),
    _OspfsDescription_Type()
)
ospfsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsDescription.setStatus("current")
_OspfsInitialSize_Type = Gauge32
_OspfsInitialSize_Object = MibTableColumn
ospfsInitialSize = _OspfsInitialSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 4),
    _OspfsInitialSize_Type()
)
ospfsInitialSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsInitialSize.setStatus("current")
if mibBuilder.loadTexts:
    ospfsInitialSize.setUnits("Megabytes")
_OspfsMaximumSize_Type = Gauge32
_OspfsMaximumSize_Object = MibTableColumn
ospfsMaximumSize = _OspfsMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 5),
    _OspfsMaximumSize_Type()
)
ospfsMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsMaximumSize.setStatus("current")
if mibBuilder.loadTexts:
    ospfsMaximumSize.setUnits("Megabytes")
_OspfsName_Type = WtcsDisplayString
_OspfsName_Object = MibTableColumn
ospfsName = _OspfsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 6),
    _OspfsName_Type()
)
ospfsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsName.setStatus("current")
_OspfsSettingID_Type = WtcsDisplayString
_OspfsSettingID_Object = MibTableColumn
ospfsSettingID = _OspfsSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 2, 1, 7),
    _OspfsSettingID_Type()
)
ospfsSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfsSettingID.setStatus("current")
_Win32PageFileUsageTable_Object = MibTable
win32PageFileUsageTable = _Win32PageFileUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3)
)
if mibBuilder.loadTexts:
    win32PageFileUsageTable.setStatus("current")
_Win32PageFileUsageEntry_Object = MibTableRow
win32PageFileUsageEntry = _Win32PageFileUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1)
)
win32PageFileUsageEntry.setIndexNames(
    (0, "INFORMANT-OS", "ospfuIndex"),
)
if mibBuilder.loadTexts:
    win32PageFileUsageEntry.setStatus("current")


class _OspfuIndex_Type(Integer32):
    """Custom type ospfuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspfuIndex_Type.__name__ = "Integer32"
_OspfuIndex_Object = MibTableColumn
ospfuIndex = _OspfuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 1),
    _OspfuIndex_Type()
)
ospfuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuIndex.setStatus("current")
_OspfuAllocatedBaseSize_Type = Gauge32
_OspfuAllocatedBaseSize_Object = MibTableColumn
ospfuAllocatedBaseSize = _OspfuAllocatedBaseSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 2),
    _OspfuAllocatedBaseSize_Type()
)
ospfuAllocatedBaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuAllocatedBaseSize.setStatus("current")
if mibBuilder.loadTexts:
    ospfuAllocatedBaseSize.setUnits("Megabytes")
_OspfuCaption_Type = WtcsDisplayString
_OspfuCaption_Object = MibTableColumn
ospfuCaption = _OspfuCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 3),
    _OspfuCaption_Type()
)
ospfuCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuCaption.setStatus("current")
_OspfuCurrentUsage_Type = Gauge32
_OspfuCurrentUsage_Object = MibTableColumn
ospfuCurrentUsage = _OspfuCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 4),
    _OspfuCurrentUsage_Type()
)
ospfuCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuCurrentUsage.setStatus("current")
if mibBuilder.loadTexts:
    ospfuCurrentUsage.setUnits("Megabytes")
_OspfuDescription_Type = WtcsDisplayString
_OspfuDescription_Object = MibTableColumn
ospfuDescription = _OspfuDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 5),
    _OspfuDescription_Type()
)
ospfuDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuDescription.setStatus("current")
_OspfuInstallDate_Type = DateAndTime
_OspfuInstallDate_Object = MibTableColumn
ospfuInstallDate = _OspfuInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 6),
    _OspfuInstallDate_Type()
)
ospfuInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuInstallDate.setStatus("current")
_OspfuName_Type = WtcsDisplayString
_OspfuName_Object = MibTableColumn
ospfuName = _OspfuName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 7),
    _OspfuName_Type()
)
ospfuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuName.setStatus("current")
_OspfuPeakUsage_Type = Gauge32
_OspfuPeakUsage_Object = MibTableColumn
ospfuPeakUsage = _OspfuPeakUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 8),
    _OspfuPeakUsage_Type()
)
ospfuPeakUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuPeakUsage.setStatus("current")
if mibBuilder.loadTexts:
    ospfuPeakUsage.setUnits("Megabytes")


class _OspfuStatus_Type(Integer32):
    """Custom type ospfuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OspfuStatus_Type.__name__ = "Integer32"
_OspfuStatus_Object = MibTableColumn
ospfuStatus = _OspfuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 9),
    _OspfuStatus_Type()
)
ospfuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuStatus.setStatus("current")
_OspfuTempPageFile_Type = TruthValue
_OspfuTempPageFile_Object = MibTableColumn
ospfuTempPageFile = _OspfuTempPageFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 5, 3, 1, 10),
    _OspfuTempPageFile_Type()
)
ospfuTempPageFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfuTempPageFile.setStatus("current")
_WmiMultimedia_ObjectIdentity = ObjectIdentity
wmiMultimedia = _WmiMultimedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6)
)
if mibBuilder.loadTexts:
    wmiMultimedia.setStatus("current")
_Win32CodecFileTable_Object = MibTable
win32CodecFileTable = _Win32CodecFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1)
)
if mibBuilder.loadTexts:
    win32CodecFileTable.setStatus("current")
_Win32CodecFileEntry_Object = MibTableRow
win32CodecFileEntry = _Win32CodecFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1)
)
win32CodecFileEntry.setIndexNames(
    (0, "INFORMANT-OS", "oscfIndex"),
)
if mibBuilder.loadTexts:
    win32CodecFileEntry.setStatus("current")


class _OscfIndex_Type(Integer32):
    """Custom type oscfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OscfIndex_Type.__name__ = "Integer32"
_OscfIndex_Object = MibTableColumn
oscfIndex = _OscfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 1),
    _OscfIndex_Type()
)
oscfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfIndex.setStatus("current")


class _OscfAccessMask_Type(Integer32):
    """Custom type oscfAccessMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("delete", 16),
          ("fileADDFILE", 1),
          ("fileADDSUBDIRECTORY", 2),
          ("fileDELETECHILD", 6),
          ("fileLISTDIRECTORY", 0),
          ("fileREADATTRIBUTES", 7),
          ("fileREADEA", 3),
          ("fileTRAVERSE", 5),
          ("fileWRITEATTRIBUTES", 8),
          ("fileWRITEEA", 4),
          ("readCONTROL", 17),
          ("synchronize", 20),
          ("writeDAC", 18),
          ("writeOWNER", 19))
    )


_OscfAccessMask_Type.__name__ = "Integer32"
_OscfAccessMask_Object = MibTableColumn
oscfAccessMask = _OscfAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 2),
    _OscfAccessMask_Type()
)
oscfAccessMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfAccessMask.setStatus("current")
_OscfArchive_Type = TruthValue
_OscfArchive_Object = MibTableColumn
oscfArchive = _OscfArchive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 3),
    _OscfArchive_Type()
)
oscfArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfArchive.setStatus("current")


class _OscfCaption_Type(WtcsDisplayString):
    """Custom type oscfCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OscfCaption_Type.__name__ = "WtcsDisplayString"
_OscfCaption_Object = MibTableColumn
oscfCaption = _OscfCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 4),
    _OscfCaption_Type()
)
oscfCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCaption.setStatus("current")
_OscfCompressed_Type = TruthValue
_OscfCompressed_Object = MibTableColumn
oscfCompressed = _OscfCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 5),
    _OscfCompressed_Type()
)
oscfCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCompressed.setStatus("current")
_OscfCompressionMethod_Type = WtcsDisplayString
_OscfCompressionMethod_Object = MibTableColumn
oscfCompressionMethod = _OscfCompressionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 6),
    _OscfCompressionMethod_Type()
)
oscfCompressionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCompressionMethod.setStatus("current")


class _OscfCreationClassName_Type(WtcsDisplayString):
    """Custom type oscfCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OscfCreationClassName_Type.__name__ = "WtcsDisplayString"
_OscfCreationClassName_Object = MibTableColumn
oscfCreationClassName = _OscfCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 7),
    _OscfCreationClassName_Type()
)
oscfCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCreationClassName.setStatus("current")
_OscfCreationDate_Type = DateAndTime
_OscfCreationDate_Object = MibTableColumn
oscfCreationDate = _OscfCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 8),
    _OscfCreationDate_Type()
)
oscfCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCreationDate.setStatus("current")
_OscfCSCreationClassName_Type = WtcsDisplayString
_OscfCSCreationClassName_Object = MibTableColumn
oscfCSCreationClassName = _OscfCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 9),
    _OscfCSCreationClassName_Type()
)
oscfCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCSCreationClassName.setStatus("current")
_OscfCSName_Type = WtcsDisplayString
_OscfCSName_Object = MibTableColumn
oscfCSName = _OscfCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 10),
    _OscfCSName_Type()
)
oscfCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfCSName.setStatus("current")
_OscfDescription_Type = WtcsDisplayString
_OscfDescription_Object = MibTableColumn
oscfDescription = _OscfDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 11),
    _OscfDescription_Type()
)
oscfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfDescription.setStatus("current")
_OscfDrive_Type = WtcsDisplayString
_OscfDrive_Object = MibTableColumn
oscfDrive = _OscfDrive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 12),
    _OscfDrive_Type()
)
oscfDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfDrive.setStatus("current")
_OscfEightDotThreeFileName_Type = WtcsDisplayString
_OscfEightDotThreeFileName_Object = MibTableColumn
oscfEightDotThreeFileName = _OscfEightDotThreeFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 13),
    _OscfEightDotThreeFileName_Type()
)
oscfEightDotThreeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfEightDotThreeFileName.setStatus("current")
_OscfEncrypted_Type = TruthValue
_OscfEncrypted_Object = MibTableColumn
oscfEncrypted = _OscfEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 14),
    _OscfEncrypted_Type()
)
oscfEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfEncrypted.setStatus("current")
_OscfEncryptionMethod_Type = WtcsDisplayString
_OscfEncryptionMethod_Object = MibTableColumn
oscfEncryptionMethod = _OscfEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 15),
    _OscfEncryptionMethod_Type()
)
oscfEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfEncryptionMethod.setStatus("current")
_OscfExtension_Type = WtcsDisplayString
_OscfExtension_Object = MibTableColumn
oscfExtension = _OscfExtension_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 16),
    _OscfExtension_Type()
)
oscfExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfExtension.setStatus("current")
_OscfFileName_Type = WtcsDisplayString
_OscfFileName_Object = MibTableColumn
oscfFileName = _OscfFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 17),
    _OscfFileName_Type()
)
oscfFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfFileName.setStatus("current")
_OscfFileSize_Type = Gauge32
_OscfFileSize_Object = MibTableColumn
oscfFileSize = _OscfFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 18),
    _OscfFileSize_Type()
)
oscfFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfFileSize.setStatus("current")
_OscfFileType_Type = WtcsDisplayString
_OscfFileType_Object = MibTableColumn
oscfFileType = _OscfFileType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 19),
    _OscfFileType_Type()
)
oscfFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfFileType.setStatus("current")
_OscfFSCreationClassName_Type = WtcsDisplayString
_OscfFSCreationClassName_Object = MibTableColumn
oscfFSCreationClassName = _OscfFSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 20),
    _OscfFSCreationClassName_Type()
)
oscfFSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfFSCreationClassName.setStatus("current")
_OscfFSName_Type = WtcsDisplayString
_OscfFSName_Object = MibTableColumn
oscfFSName = _OscfFSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 21),
    _OscfFSName_Type()
)
oscfFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfFSName.setStatus("current")


class _OscfGroup_Type(Integer32):
    """Custom type oscfGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("video", 2))
    )


_OscfGroup_Type.__name__ = "Integer32"
_OscfGroup_Object = MibTableColumn
oscfGroup = _OscfGroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 22),
    _OscfGroup_Type()
)
oscfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfGroup.setStatus("current")
_OscfHidden_Type = TruthValue
_OscfHidden_Object = MibTableColumn
oscfHidden = _OscfHidden_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 23),
    _OscfHidden_Type()
)
oscfHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfHidden.setStatus("current")
_OscfInstallDate_Type = DateAndTime
_OscfInstallDate_Object = MibTableColumn
oscfInstallDate = _OscfInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 24),
    _OscfInstallDate_Type()
)
oscfInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfInstallDate.setStatus("current")
_OscfInUseCount_Type = Gauge32
_OscfInUseCount_Object = MibTableColumn
oscfInUseCount = _OscfInUseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 25),
    _OscfInUseCount_Type()
)
oscfInUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfInUseCount.setStatus("current")
_OscfLastAccessed_Type = DateAndTime
_OscfLastAccessed_Object = MibTableColumn
oscfLastAccessed = _OscfLastAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 26),
    _OscfLastAccessed_Type()
)
oscfLastAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfLastAccessed.setStatus("current")
_OscfLastModified_Type = DateAndTime
_OscfLastModified_Object = MibTableColumn
oscfLastModified = _OscfLastModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 27),
    _OscfLastModified_Type()
)
oscfLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfLastModified.setStatus("current")
_OscfManufacturer_Type = WtcsDisplayString
_OscfManufacturer_Object = MibTableColumn
oscfManufacturer = _OscfManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 28),
    _OscfManufacturer_Type()
)
oscfManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfManufacturer.setStatus("current")
_OscfName_Type = WtcsDisplayString
_OscfName_Object = MibTableColumn
oscfName = _OscfName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 29),
    _OscfName_Type()
)
oscfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfName.setStatus("current")
_OscfPath_Type = WtcsDisplayString
_OscfPath_Object = MibTableColumn
oscfPath = _OscfPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 30),
    _OscfPath_Type()
)
oscfPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfPath.setStatus("current")
_OscfReadable_Type = TruthValue
_OscfReadable_Object = MibTableColumn
oscfReadable = _OscfReadable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 31),
    _OscfReadable_Type()
)
oscfReadable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfReadable.setStatus("current")


class _OscfStatus_Type(Integer32):
    """Custom type oscfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OscfStatus_Type.__name__ = "Integer32"
_OscfStatus_Object = MibTableColumn
oscfStatus = _OscfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 32),
    _OscfStatus_Type()
)
oscfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfStatus.setStatus("current")
_OscfSystem_Type = TruthValue
_OscfSystem_Object = MibTableColumn
oscfSystem = _OscfSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 33),
    _OscfSystem_Type()
)
oscfSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfSystem.setStatus("current")
_OscfVersion_Type = WtcsDisplayString
_OscfVersion_Object = MibTableColumn
oscfVersion = _OscfVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 34),
    _OscfVersion_Type()
)
oscfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfVersion.setStatus("current")
_OscfWriteable_Type = TruthValue
_OscfWriteable_Object = MibTableColumn
oscfWriteable = _OscfWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 6, 1, 1, 35),
    _OscfWriteable_Type()
)
oscfWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscfWriteable.setStatus("current")
_WmiNetworking_ObjectIdentity = ObjectIdentity
wmiNetworking = _WmiNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7)
)
if mibBuilder.loadTexts:
    wmiNetworking.setStatus("current")
_Win32IP4PersistedRouteTableTable_Object = MibTable
win32IP4PersistedRouteTableTable = _Win32IP4PersistedRouteTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1)
)
if mibBuilder.loadTexts:
    win32IP4PersistedRouteTableTable.setStatus("current")
_Win32IP4PersistedRouteTableEntry_Object = MibTableRow
win32IP4PersistedRouteTableEntry = _Win32IP4PersistedRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1)
)
win32IP4PersistedRouteTableEntry.setIndexNames(
    (0, "INFORMANT-OS", "osprtIndex"),
)
if mibBuilder.loadTexts:
    win32IP4PersistedRouteTableEntry.setStatus("current")


class _OsprtIndex_Type(Integer32):
    """Custom type osprtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsprtIndex_Type.__name__ = "Integer32"
_OsprtIndex_Object = MibTableColumn
osprtIndex = _OsprtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 1),
    _OsprtIndex_Type()
)
osprtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtIndex.setStatus("current")


class _OsprtCaption_Type(WtcsDisplayString):
    """Custom type osprtCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsprtCaption_Type.__name__ = "WtcsDisplayString"
_OsprtCaption_Object = MibTableColumn
osprtCaption = _OsprtCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 2),
    _OsprtCaption_Type()
)
osprtCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtCaption.setStatus("current")
_OsprtDescription_Type = WtcsDisplayString
_OsprtDescription_Object = MibTableColumn
osprtDescription = _OsprtDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 3),
    _OsprtDescription_Type()
)
osprtDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtDescription.setStatus("current")
_OsprtDestination_Type = WtcsDisplayString
_OsprtDestination_Object = MibTableColumn
osprtDestination = _OsprtDestination_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 4),
    _OsprtDestination_Type()
)
osprtDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtDestination.setStatus("current")
_OsprtInstallDate_Type = DateAndTime
_OsprtInstallDate_Object = MibTableColumn
osprtInstallDate = _OsprtInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 5),
    _OsprtInstallDate_Type()
)
osprtInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtInstallDate.setStatus("current")
_OsprtMask_Type = WtcsDisplayString
_OsprtMask_Object = MibTableColumn
osprtMask = _OsprtMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 6),
    _OsprtMask_Type()
)
osprtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtMask.setStatus("current")
_OsprtMetric1_Type = Integer32
_OsprtMetric1_Object = MibTableColumn
osprtMetric1 = _OsprtMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 7),
    _OsprtMetric1_Type()
)
osprtMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtMetric1.setStatus("current")
_OsprtName_Type = WtcsDisplayString
_OsprtName_Object = MibTableColumn
osprtName = _OsprtName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 8),
    _OsprtName_Type()
)
osprtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtName.setStatus("current")
_OsprtNextHop_Type = WtcsDisplayString
_OsprtNextHop_Object = MibTableColumn
osprtNextHop = _OsprtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 9),
    _OsprtNextHop_Type()
)
osprtNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtNextHop.setStatus("current")


class _OsprtStatus_Type(Integer32):
    """Custom type osprtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsprtStatus_Type.__name__ = "Integer32"
_OsprtStatus_Object = MibTableColumn
osprtStatus = _OsprtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 1, 1, 10),
    _OsprtStatus_Type()
)
osprtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osprtStatus.setStatus("current")
_Win32IP4RouteTableTable_Object = MibTable
win32IP4RouteTableTable = _Win32IP4RouteTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2)
)
if mibBuilder.loadTexts:
    win32IP4RouteTableTable.setStatus("current")
_Win32IP4RouteTableEntry_Object = MibTableRow
win32IP4RouteTableEntry = _Win32IP4RouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1)
)
win32IP4RouteTableEntry.setIndexNames(
    (0, "INFORMANT-OS", "osrtIndex"),
)
if mibBuilder.loadTexts:
    win32IP4RouteTableEntry.setStatus("current")


class _OsrtIndex_Type(Integer32):
    """Custom type osrtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsrtIndex_Type.__name__ = "Integer32"
_OsrtIndex_Object = MibTableColumn
osrtIndex = _OsrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 1),
    _OsrtIndex_Type()
)
osrtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtIndex.setStatus("current")
_OsrtAge_Type = Integer32
_OsrtAge_Object = MibTableColumn
osrtAge = _OsrtAge_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 2),
    _OsrtAge_Type()
)
osrtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtAge.setStatus("current")


class _OsrtCaption_Type(WtcsDisplayString):
    """Custom type osrtCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsrtCaption_Type.__name__ = "WtcsDisplayString"
_OsrtCaption_Object = MibTableColumn
osrtCaption = _OsrtCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 3),
    _OsrtCaption_Type()
)
osrtCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtCaption.setStatus("current")
_OsrtDescription_Type = WtcsDisplayString
_OsrtDescription_Object = MibTableColumn
osrtDescription = _OsrtDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 4),
    _OsrtDescription_Type()
)
osrtDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtDescription.setStatus("current")
_OsrtDestination_Type = WtcsDisplayString
_OsrtDestination_Object = MibTableColumn
osrtDestination = _OsrtDestination_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 5),
    _OsrtDestination_Type()
)
osrtDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtDestination.setStatus("current")
_OsrtInformation_Type = WtcsDisplayString
_OsrtInformation_Object = MibTableColumn
osrtInformation = _OsrtInformation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 6),
    _OsrtInformation_Type()
)
osrtInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtInformation.setStatus("current")
_OsrtInstallDate_Type = DateAndTime
_OsrtInstallDate_Object = MibTableColumn
osrtInstallDate = _OsrtInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 7),
    _OsrtInstallDate_Type()
)
osrtInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtInstallDate.setStatus("current")
_OsrtInterfaceIndex_Type = Integer32
_OsrtInterfaceIndex_Object = MibTableColumn
osrtInterfaceIndex = _OsrtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 8),
    _OsrtInterfaceIndex_Type()
)
osrtInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtInterfaceIndex.setStatus("current")
_OsrtMask_Type = WtcsDisplayString
_OsrtMask_Object = MibTableColumn
osrtMask = _OsrtMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 9),
    _OsrtMask_Type()
)
osrtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMask.setStatus("current")
_OsrtMetric1_Type = Integer32
_OsrtMetric1_Object = MibTableColumn
osrtMetric1 = _OsrtMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 10),
    _OsrtMetric1_Type()
)
osrtMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMetric1.setStatus("current")
_OsrtMetric2_Type = Integer32
_OsrtMetric2_Object = MibTableColumn
osrtMetric2 = _OsrtMetric2_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 11),
    _OsrtMetric2_Type()
)
osrtMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMetric2.setStatus("current")
_OsrtMetric3_Type = Integer32
_OsrtMetric3_Object = MibTableColumn
osrtMetric3 = _OsrtMetric3_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 12),
    _OsrtMetric3_Type()
)
osrtMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMetric3.setStatus("current")
_OsrtMetric4_Type = Integer32
_OsrtMetric4_Object = MibTableColumn
osrtMetric4 = _OsrtMetric4_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 13),
    _OsrtMetric4_Type()
)
osrtMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMetric4.setStatus("current")
_OsrtMetric5_Type = Integer32
_OsrtMetric5_Object = MibTableColumn
osrtMetric5 = _OsrtMetric5_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 14),
    _OsrtMetric5_Type()
)
osrtMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtMetric5.setStatus("current")
_OsrtName_Type = WtcsDisplayString
_OsrtName_Object = MibTableColumn
osrtName = _OsrtName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 15),
    _OsrtName_Type()
)
osrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtName.setStatus("current")
_OsrtNextHop_Type = WtcsDisplayString
_OsrtNextHop_Object = MibTableColumn
osrtNextHop = _OsrtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 16),
    _OsrtNextHop_Type()
)
osrtNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtNextHop.setStatus("current")


class _OsrtProtocol_Type(Integer32):
    """Custom type osrtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("esis", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("isis", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_OsrtProtocol_Type.__name__ = "Integer32"
_OsrtProtocol_Object = MibTableColumn
osrtProtocol = _OsrtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 17),
    _OsrtProtocol_Type()
)
osrtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtProtocol.setStatus("current")


class _OsrtStatus_Type(Integer32):
    """Custom type osrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsrtStatus_Type.__name__ = "Integer32"
_OsrtStatus_Object = MibTableColumn
osrtStatus = _OsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 18),
    _OsrtStatus_Type()
)
osrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtStatus.setStatus("current")


class _OsrtType_Type(Integer32):
    """Custom type osrtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_OsrtType_Type.__name__ = "Integer32"
_OsrtType_Object = MibTableColumn
osrtType = _OsrtType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 2, 1, 19),
    _OsrtType_Type()
)
osrtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrtType.setStatus("current")
_Win32NetworkClientTable_Object = MibTable
win32NetworkClientTable = _Win32NetworkClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3)
)
if mibBuilder.loadTexts:
    win32NetworkClientTable.setStatus("current")
_Win32NetworkClientEntry_Object = MibTableRow
win32NetworkClientEntry = _Win32NetworkClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1)
)
win32NetworkClientEntry.setIndexNames(
    (0, "INFORMANT-OS", "osnclIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkClientEntry.setStatus("current")


class _OsnclIndex_Type(Integer32):
    """Custom type osnclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsnclIndex_Type.__name__ = "Integer32"
_OsnclIndex_Object = MibTableColumn
osnclIndex = _OsnclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 1),
    _OsnclIndex_Type()
)
osnclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclIndex.setStatus("current")
_OsnclCaption_Type = WtcsDisplayString
_OsnclCaption_Object = MibTableColumn
osnclCaption = _OsnclCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 2),
    _OsnclCaption_Type()
)
osnclCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclCaption.setStatus("current")
_OsnclDescription_Type = WtcsDisplayString
_OsnclDescription_Object = MibTableColumn
osnclDescription = _OsnclDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 3),
    _OsnclDescription_Type()
)
osnclDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclDescription.setStatus("current")
_OsnclInstallDate_Type = DateAndTime
_OsnclInstallDate_Object = MibTableColumn
osnclInstallDate = _OsnclInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 4),
    _OsnclInstallDate_Type()
)
osnclInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclInstallDate.setStatus("current")
_OsnclManufacturer_Type = WtcsDisplayString
_OsnclManufacturer_Object = MibTableColumn
osnclManufacturer = _OsnclManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 5),
    _OsnclManufacturer_Type()
)
osnclManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclManufacturer.setStatus("current")
_OsnclName_Type = WtcsDisplayString
_OsnclName_Object = MibTableColumn
osnclName = _OsnclName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 6),
    _OsnclName_Type()
)
osnclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclName.setStatus("current")


class _OsnclStatus_Type(Integer32):
    """Custom type osnclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsnclStatus_Type.__name__ = "Integer32"
_OsnclStatus_Object = MibTableColumn
osnclStatus = _OsnclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 3, 1, 7),
    _OsnclStatus_Type()
)
osnclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnclStatus.setStatus("current")
_Win32NetworkConnectionTable_Object = MibTable
win32NetworkConnectionTable = _Win32NetworkConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4)
)
if mibBuilder.loadTexts:
    win32NetworkConnectionTable.setStatus("current")
_Win32NetworkConnectionEntry_Object = MibTableRow
win32NetworkConnectionEntry = _Win32NetworkConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1)
)
win32NetworkConnectionEntry.setIndexNames(
    (0, "INFORMANT-OS", "osncoIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkConnectionEntry.setStatus("current")


class _OsncoIndex_Type(Integer32):
    """Custom type osncoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsncoIndex_Type.__name__ = "Integer32"
_OsncoIndex_Object = MibTableColumn
osncoIndex = _OsncoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 1),
    _OsncoIndex_Type()
)
osncoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoIndex.setStatus("current")
_OsncoAccessMask_Type = WtcsDisplayString
_OsncoAccessMask_Object = MibTableColumn
osncoAccessMask = _OsncoAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 2),
    _OsncoAccessMask_Type()
)
osncoAccessMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoAccessMask.setStatus("current")
_OsncoCaption_Type = WtcsDisplayString
_OsncoCaption_Object = MibTableColumn
osncoCaption = _OsncoCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 3),
    _OsncoCaption_Type()
)
osncoCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoCaption.setStatus("current")
_OsncoComment_Type = WtcsDisplayString
_OsncoComment_Object = MibTableColumn
osncoComment = _OsncoComment_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 4),
    _OsncoComment_Type()
)
osncoComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoComment.setStatus("current")


class _OsncoConnectionState_Type(Integer32):
    """Custom type osncoConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("connecting", 5),
          ("disconnected", 4),
          ("error", 2),
          ("paused", 3),
          ("reconnecting", 6))
    )


_OsncoConnectionState_Type.__name__ = "Integer32"
_OsncoConnectionState_Object = MibTableColumn
osncoConnectionState = _OsncoConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 5),
    _OsncoConnectionState_Type()
)
osncoConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoConnectionState.setStatus("current")


class _OsncoConnectionType_Type(Integer32):
    """Custom type osncoConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("currentConnection", 1),
          ("persistentConnection", 2))
    )


_OsncoConnectionType_Type.__name__ = "Integer32"
_OsncoConnectionType_Object = MibTableColumn
osncoConnectionType = _OsncoConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 6),
    _OsncoConnectionType_Type()
)
osncoConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoConnectionType.setStatus("current")
_OsncoDescription_Type = WtcsDisplayString
_OsncoDescription_Object = MibTableColumn
osncoDescription = _OsncoDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 7),
    _OsncoDescription_Type()
)
osncoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoDescription.setStatus("current")


class _OsncoDisplayType_Type(Integer32):
    """Custom type osncoDisplayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("domain", 1),
          ("generic", 2),
          ("server", 3),
          ("share", 4))
    )


_OsncoDisplayType_Type.__name__ = "Integer32"
_OsncoDisplayType_Object = MibTableColumn
osncoDisplayType = _OsncoDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 8),
    _OsncoDisplayType_Type()
)
osncoDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoDisplayType.setStatus("current")
_OsncoInstallDate_Type = DateAndTime
_OsncoInstallDate_Object = MibTableColumn
osncoInstallDate = _OsncoInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 9),
    _OsncoInstallDate_Type()
)
osncoInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoInstallDate.setStatus("current")
_OsncoLocalName_Type = WtcsDisplayString
_OsncoLocalName_Object = MibTableColumn
osncoLocalName = _OsncoLocalName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 10),
    _OsncoLocalName_Type()
)
osncoLocalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoLocalName.setStatus("current")
_OsncoName_Type = WtcsDisplayString
_OsncoName_Object = MibTableColumn
osncoName = _OsncoName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 11),
    _OsncoName_Type()
)
osncoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoName.setStatus("current")
_OsncoPersistent_Type = TruthValue
_OsncoPersistent_Object = MibTableColumn
osncoPersistent = _OsncoPersistent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 12),
    _OsncoPersistent_Type()
)
osncoPersistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoPersistent.setStatus("current")
_OsncoProviderName_Type = WtcsDisplayString
_OsncoProviderName_Object = MibTableColumn
osncoProviderName = _OsncoProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 13),
    _OsncoProviderName_Type()
)
osncoProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoProviderName.setStatus("current")
_OsncoRemoteName_Type = WtcsDisplayString
_OsncoRemoteName_Object = MibTableColumn
osncoRemoteName = _OsncoRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 14),
    _OsncoRemoteName_Type()
)
osncoRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoRemoteName.setStatus("current")
_OsncoRemotePath_Type = WtcsDisplayString
_OsncoRemotePath_Object = MibTableColumn
osncoRemotePath = _OsncoRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 15),
    _OsncoRemotePath_Type()
)
osncoRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoRemotePath.setStatus("current")


class _OsncoResourceType_Type(Integer32):
    """Custom type osncoResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("disk", 1),
          ("print", 2))
    )


_OsncoResourceType_Type.__name__ = "Integer32"
_OsncoResourceType_Object = MibTableColumn
osncoResourceType = _OsncoResourceType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 16),
    _OsncoResourceType_Type()
)
osncoResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoResourceType.setStatus("current")


class _OsncoStatus_Type(Integer32):
    """Custom type osncoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsncoStatus_Type.__name__ = "Integer32"
_OsncoStatus_Object = MibTableColumn
osncoStatus = _OsncoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 17),
    _OsncoStatus_Type()
)
osncoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoStatus.setStatus("current")
_OsncoUserName_Type = WtcsDisplayString
_OsncoUserName_Object = MibTableColumn
osncoUserName = _OsncoUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 4, 1, 18),
    _OsncoUserName_Type()
)
osncoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osncoUserName.setStatus("current")
_Win32NetworkProtocolTable_Object = MibTable
win32NetworkProtocolTable = _Win32NetworkProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5)
)
if mibBuilder.loadTexts:
    win32NetworkProtocolTable.setStatus("current")
_Win32NetworkProtocolEntry_Object = MibTableRow
win32NetworkProtocolEntry = _Win32NetworkProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1)
)
win32NetworkProtocolEntry.setIndexNames(
    (0, "INFORMANT-OS", "osnpIndex"),
)
if mibBuilder.loadTexts:
    win32NetworkProtocolEntry.setStatus("current")


class _OsnpIndex_Type(Integer32):
    """Custom type osnpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsnpIndex_Type.__name__ = "Integer32"
_OsnpIndex_Object = MibTableColumn
osnpIndex = _OsnpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 1),
    _OsnpIndex_Type()
)
osnpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpIndex.setStatus("current")
_OsnpCaption_Type = WtcsDisplayString
_OsnpCaption_Object = MibTableColumn
osnpCaption = _OsnpCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 2),
    _OsnpCaption_Type()
)
osnpCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpCaption.setStatus("current")
_OsnpConnectionlessService_Type = TruthValue
_OsnpConnectionlessService_Object = MibTableColumn
osnpConnectionlessService = _OsnpConnectionlessService_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 3),
    _OsnpConnectionlessService_Type()
)
osnpConnectionlessService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpConnectionlessService.setStatus("current")
_OsnpDescription_Type = WtcsDisplayString
_OsnpDescription_Object = MibTableColumn
osnpDescription = _OsnpDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 4),
    _OsnpDescription_Type()
)
osnpDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpDescription.setStatus("current")
_OsnpGuaranteesDelivery_Type = TruthValue
_OsnpGuaranteesDelivery_Object = MibTableColumn
osnpGuaranteesDelivery = _OsnpGuaranteesDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 5),
    _OsnpGuaranteesDelivery_Type()
)
osnpGuaranteesDelivery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpGuaranteesDelivery.setStatus("current")
_OsnpGuaranteesSequencing_Type = TruthValue
_OsnpGuaranteesSequencing_Object = MibTableColumn
osnpGuaranteesSequencing = _OsnpGuaranteesSequencing_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 6),
    _OsnpGuaranteesSequencing_Type()
)
osnpGuaranteesSequencing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpGuaranteesSequencing.setStatus("current")
_OsnpInstallDate_Type = DateAndTime
_OsnpInstallDate_Object = MibTableColumn
osnpInstallDate = _OsnpInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 7),
    _OsnpInstallDate_Type()
)
osnpInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpInstallDate.setStatus("current")
_OsnpMaximumAddressSize_Type = Gauge32
_OsnpMaximumAddressSize_Object = MibTableColumn
osnpMaximumAddressSize = _OsnpMaximumAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 8),
    _OsnpMaximumAddressSize_Type()
)
osnpMaximumAddressSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpMaximumAddressSize.setStatus("current")
if mibBuilder.loadTexts:
    osnpMaximumAddressSize.setUnits("Characters")
_OsnpMaximumMessageSize_Type = Gauge32
_OsnpMaximumMessageSize_Object = MibTableColumn
osnpMaximumMessageSize = _OsnpMaximumMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 9),
    _OsnpMaximumMessageSize_Type()
)
osnpMaximumMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpMaximumMessageSize.setStatus("current")
if mibBuilder.loadTexts:
    osnpMaximumMessageSize.setUnits("Characters")
_OsnpMessageOriented_Type = TruthValue
_OsnpMessageOriented_Object = MibTableColumn
osnpMessageOriented = _OsnpMessageOriented_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 10),
    _OsnpMessageOriented_Type()
)
osnpMessageOriented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpMessageOriented.setStatus("current")
_OsnpMinimumAddressSize_Type = Gauge32
_OsnpMinimumAddressSize_Object = MibTableColumn
osnpMinimumAddressSize = _OsnpMinimumAddressSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 11),
    _OsnpMinimumAddressSize_Type()
)
osnpMinimumAddressSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpMinimumAddressSize.setStatus("current")
if mibBuilder.loadTexts:
    osnpMinimumAddressSize.setUnits("Characters")
_OsnpName_Type = WtcsDisplayString
_OsnpName_Object = MibTableColumn
osnpName = _OsnpName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 12),
    _OsnpName_Type()
)
osnpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpName.setStatus("current")
_OsnpPseudoStreamOriented_Type = TruthValue
_OsnpPseudoStreamOriented_Object = MibTableColumn
osnpPseudoStreamOriented = _OsnpPseudoStreamOriented_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 13),
    _OsnpPseudoStreamOriented_Type()
)
osnpPseudoStreamOriented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpPseudoStreamOriented.setStatus("current")


class _OsnpStatus_Type(Integer32):
    """Custom type osnpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsnpStatus_Type.__name__ = "Integer32"
_OsnpStatus_Object = MibTableColumn
osnpStatus = _OsnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 14),
    _OsnpStatus_Type()
)
osnpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpStatus.setStatus("current")
_OsnpSupportsBroadcasting_Type = TruthValue
_OsnpSupportsBroadcasting_Object = MibTableColumn
osnpSupportsBroadcasting = _OsnpSupportsBroadcasting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 15),
    _OsnpSupportsBroadcasting_Type()
)
osnpSupportsBroadcasting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsBroadcasting.setStatus("current")
_OsnpSupportsConnectData_Type = TruthValue
_OsnpSupportsConnectData_Object = MibTableColumn
osnpSupportsConnectData = _OsnpSupportsConnectData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 16),
    _OsnpSupportsConnectData_Type()
)
osnpSupportsConnectData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsConnectData.setStatus("current")
_OsnpSupportsDisconnectData_Type = TruthValue
_OsnpSupportsDisconnectData_Object = MibTableColumn
osnpSupportsDisconnectData = _OsnpSupportsDisconnectData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 17),
    _OsnpSupportsDisconnectData_Type()
)
osnpSupportsDisconnectData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsDisconnectData.setStatus("current")
_OsnpSupportsEncryption_Type = TruthValue
_OsnpSupportsEncryption_Object = MibTableColumn
osnpSupportsEncryption = _OsnpSupportsEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 18),
    _OsnpSupportsEncryption_Type()
)
osnpSupportsEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsEncryption.setStatus("current")
_OsnpSupportsExpeditedData_Type = TruthValue
_OsnpSupportsExpeditedData_Object = MibTableColumn
osnpSupportsExpeditedData = _OsnpSupportsExpeditedData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 19),
    _OsnpSupportsExpeditedData_Type()
)
osnpSupportsExpeditedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsExpeditedData.setStatus("current")
_OsnpSupportsFragmentation_Type = TruthValue
_OsnpSupportsFragmentation_Object = MibTableColumn
osnpSupportsFragmentation = _OsnpSupportsFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 20),
    _OsnpSupportsFragmentation_Type()
)
osnpSupportsFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsFragmentation.setStatus("current")
_OsnpSupportsGracefulClosing_Type = TruthValue
_OsnpSupportsGracefulClosing_Object = MibTableColumn
osnpSupportsGracefulClosing = _OsnpSupportsGracefulClosing_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 21),
    _OsnpSupportsGracefulClosing_Type()
)
osnpSupportsGracefulClosing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsGracefulClosing.setStatus("current")
_OsnpSupportsGuaranteedBandwidth_Type = TruthValue
_OsnpSupportsGuaranteedBandwidth_Object = MibTableColumn
osnpSupportsGuaranteedBandwidth = _OsnpSupportsGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 22),
    _OsnpSupportsGuaranteedBandwidth_Type()
)
osnpSupportsGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsGuaranteedBandwidth.setStatus("current")
_OsnpSupportsMulticasting_Type = TruthValue
_OsnpSupportsMulticasting_Object = MibTableColumn
osnpSupportsMulticasting = _OsnpSupportsMulticasting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 23),
    _OsnpSupportsMulticasting_Type()
)
osnpSupportsMulticasting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsMulticasting.setStatus("current")
_OsnpSupportsQualityofService_Type = TruthValue
_OsnpSupportsQualityofService_Object = MibTableColumn
osnpSupportsQualityofService = _OsnpSupportsQualityofService_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 5, 1, 24),
    _OsnpSupportsQualityofService_Type()
)
osnpSupportsQualityofService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osnpSupportsQualityofService.setStatus("current")
_Win32NTDomainTable_Object = MibTable
win32NTDomainTable = _Win32NTDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6)
)
if mibBuilder.loadTexts:
    win32NTDomainTable.setStatus("current")
_Win32NTDomainEntry_Object = MibTableRow
win32NTDomainEntry = _Win32NTDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1)
)
win32NTDomainEntry.setIndexNames(
    (0, "INFORMANT-OS", "osdoIndex"),
)
if mibBuilder.loadTexts:
    win32NTDomainEntry.setStatus("current")


class _OsdoIndex_Type(Integer32):
    """Custom type osdoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsdoIndex_Type.__name__ = "Integer32"
_OsdoIndex_Object = MibTableColumn
osdoIndex = _OsdoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 1),
    _OsdoIndex_Type()
)
osdoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoIndex.setStatus("current")


class _OsdoCaption_Type(WtcsDisplayString):
    """Custom type osdoCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsdoCaption_Type.__name__ = "WtcsDisplayString"
_OsdoCaption_Object = MibTableColumn
osdoCaption = _OsdoCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 2),
    _OsdoCaption_Type()
)
osdoCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoCaption.setStatus("current")
_OsdoClientSiteName_Type = WtcsDisplayString
_OsdoClientSiteName_Object = MibTableColumn
osdoClientSiteName = _OsdoClientSiteName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 3),
    _OsdoClientSiteName_Type()
)
osdoClientSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoClientSiteName.setStatus("current")
_OsdoCreationClassName_Type = WtcsDisplayString
_OsdoCreationClassName_Object = MibTableColumn
osdoCreationClassName = _OsdoCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 4),
    _OsdoCreationClassName_Type()
)
osdoCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoCreationClassName.setStatus("current")
_OsdoDcSiteName_Type = WtcsDisplayString
_OsdoDcSiteName_Object = MibTableColumn
osdoDcSiteName = _OsdoDcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 5),
    _OsdoDcSiteName_Type()
)
osdoDcSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDcSiteName.setStatus("current")
_OsdoDescription_Type = WtcsDisplayString
_OsdoDescription_Object = MibTableColumn
osdoDescription = _OsdoDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 6),
    _OsdoDescription_Type()
)
osdoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDescription.setStatus("current")
_OsdoDNSForestName_Type = WtcsDisplayString
_OsdoDNSForestName_Object = MibTableColumn
osdoDNSForestName = _OsdoDNSForestName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 7),
    _OsdoDNSForestName_Type()
)
osdoDNSForestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDNSForestName.setStatus("current")
_OsdoDomainControllerAddress_Type = WtcsDisplayString
_OsdoDomainControllerAddress_Object = MibTableColumn
osdoDomainControllerAddress = _OsdoDomainControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 8),
    _OsdoDomainControllerAddress_Type()
)
osdoDomainControllerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDomainControllerAddress.setStatus("current")


class _OsdoDomainControllerAddressType_Type(Integer32):
    """Custom type osdoDomainControllerAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnsINETADDRESS", 1),
          ("dnsNETBIOSADDRESS", 2))
    )


_OsdoDomainControllerAddressType_Type.__name__ = "Integer32"
_OsdoDomainControllerAddressType_Object = MibTableColumn
osdoDomainControllerAddressType = _OsdoDomainControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 9),
    _OsdoDomainControllerAddressType_Type()
)
osdoDomainControllerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDomainControllerAddressType.setStatus("current")
_OsdoDomainControllerName_Type = WtcsDisplayString
_OsdoDomainControllerName_Object = MibTableColumn
osdoDomainControllerName = _OsdoDomainControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 10),
    _OsdoDomainControllerName_Type()
)
osdoDomainControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDomainControllerName.setStatus("current")
_OsdoDomainGUID_Type = WtcsDisplayString
_OsdoDomainGUID_Object = MibTableColumn
osdoDomainGUID = _OsdoDomainGUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 11),
    _OsdoDomainGUID_Type()
)
osdoDomainGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDomainGUID.setStatus("current")
_OsdoDomainName_Type = WtcsDisplayString
_OsdoDomainName_Object = MibTableColumn
osdoDomainName = _OsdoDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 12),
    _OsdoDomainName_Type()
)
osdoDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDomainName.setStatus("current")
_OsdoDSDirectoryServiceFlag_Type = TruthValue
_OsdoDSDirectoryServiceFlag_Object = MibTableColumn
osdoDSDirectoryServiceFlag = _OsdoDSDirectoryServiceFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 13),
    _OsdoDSDirectoryServiceFlag_Type()
)
osdoDSDirectoryServiceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSDirectoryServiceFlag.setStatus("current")
_OsdoDSDnsControllerFlag_Type = TruthValue
_OsdoDSDnsControllerFlag_Object = MibTableColumn
osdoDSDnsControllerFlag = _OsdoDSDnsControllerFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 14),
    _OsdoDSDnsControllerFlag_Type()
)
osdoDSDnsControllerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSDnsControllerFlag.setStatus("current")
_OsdoDSDnsDomainFlag_Type = TruthValue
_OsdoDSDnsDomainFlag_Object = MibTableColumn
osdoDSDnsDomainFlag = _OsdoDSDnsDomainFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 15),
    _OsdoDSDnsDomainFlag_Type()
)
osdoDSDnsDomainFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSDnsDomainFlag.setStatus("current")
_OsdoDSDnsForestFlag_Type = TruthValue
_OsdoDSDnsForestFlag_Object = MibTableColumn
osdoDSDnsForestFlag = _OsdoDSDnsForestFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 16),
    _OsdoDSDnsForestFlag_Type()
)
osdoDSDnsForestFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSDnsForestFlag.setStatus("current")
_OsdoDSGlobalCatalogFlag_Type = TruthValue
_OsdoDSGlobalCatalogFlag_Object = MibTableColumn
osdoDSGlobalCatalogFlag = _OsdoDSGlobalCatalogFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 17),
    _OsdoDSGlobalCatalogFlag_Type()
)
osdoDSGlobalCatalogFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSGlobalCatalogFlag.setStatus("current")
_OsdoDSKerberosDistCenterFlag_Type = TruthValue
_OsdoDSKerberosDistCenterFlag_Object = MibTableColumn
osdoDSKerberosDistCenterFlag = _OsdoDSKerberosDistCenterFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 18),
    _OsdoDSKerberosDistCenterFlag_Type()
)
osdoDSKerberosDistCenterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSKerberosDistCenterFlag.setStatus("current")
_OsdoDSPriDomainControllerFlag_Type = TruthValue
_OsdoDSPriDomainControllerFlag_Object = MibTableColumn
osdoDSPriDomainControllerFlag = _OsdoDSPriDomainControllerFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 19),
    _OsdoDSPriDomainControllerFlag_Type()
)
osdoDSPriDomainControllerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSPriDomainControllerFlag.setStatus("current")
_OsdoDSTimeServiceFlag_Type = TruthValue
_OsdoDSTimeServiceFlag_Object = MibTableColumn
osdoDSTimeServiceFlag = _OsdoDSTimeServiceFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 20),
    _OsdoDSTimeServiceFlag_Type()
)
osdoDSTimeServiceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSTimeServiceFlag.setStatus("current")
_OsdoDSWritableFlag_Type = TruthValue
_OsdoDSWritableFlag_Object = MibTableColumn
osdoDSWritableFlag = _OsdoDSWritableFlag_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 21),
    _OsdoDSWritableFlag_Type()
)
osdoDSWritableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoDSWritableFlag.setStatus("current")
_OsdoInstallDate_Type = DateAndTime
_OsdoInstallDate_Object = MibTableColumn
osdoInstallDate = _OsdoInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 22),
    _OsdoInstallDate_Type()
)
osdoInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoInstallDate.setStatus("current")
_OsdoName_Type = WtcsDisplayString
_OsdoName_Object = MibTableColumn
osdoName = _OsdoName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 23),
    _OsdoName_Type()
)
osdoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoName.setStatus("current")
_OsdoNameFormat_Type = WtcsDisplayString
_OsdoNameFormat_Object = MibTableColumn
osdoNameFormat = _OsdoNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 24),
    _OsdoNameFormat_Type()
)
osdoNameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoNameFormat.setStatus("current")
_OsdoPrimaryOwnerContact_Type = WtcsDisplayString
_OsdoPrimaryOwnerContact_Object = MibTableColumn
osdoPrimaryOwnerContact = _OsdoPrimaryOwnerContact_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 25),
    _OsdoPrimaryOwnerContact_Type()
)
osdoPrimaryOwnerContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoPrimaryOwnerContact.setStatus("current")


class _OsdoPrimaryOwnerName_Type(WtcsDisplayString):
    """Custom type osdoPrimaryOwnerName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsdoPrimaryOwnerName_Type.__name__ = "WtcsDisplayString"
_OsdoPrimaryOwnerName_Object = MibTableColumn
osdoPrimaryOwnerName = _OsdoPrimaryOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 26),
    _OsdoPrimaryOwnerName_Type()
)
osdoPrimaryOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoPrimaryOwnerName.setStatus("current")
_OsdoRoles_Type = WtcsDisplayString
_OsdoRoles_Object = MibTableColumn
osdoRoles = _OsdoRoles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 27),
    _OsdoRoles_Type()
)
osdoRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoRoles.setStatus("current")


class _OsdoStatus_Type(Integer32):
    """Custom type osdoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsdoStatus_Type.__name__ = "Integer32"
_OsdoStatus_Object = MibTableColumn
osdoStatus = _OsdoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 7, 6, 1, 28),
    _OsdoStatus_Type()
)
osdoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdoStatus.setStatus("current")
_WmiOperatingSystemSettings_ObjectIdentity = ObjectIdentity
wmiOperatingSystemSettings = _WmiOperatingSystemSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8)
)
if mibBuilder.loadTexts:
    wmiOperatingSystemSettings.setStatus("current")
_Win32BootConfigurationTable_Object = MibTable
win32BootConfigurationTable = _Win32BootConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1)
)
if mibBuilder.loadTexts:
    win32BootConfigurationTable.setStatus("current")
_Win32BootConfigurationEntry_Object = MibTableRow
win32BootConfigurationEntry = _Win32BootConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1)
)
win32BootConfigurationEntry.setIndexNames(
    (0, "INFORMANT-OS", "osbcIndex"),
)
if mibBuilder.loadTexts:
    win32BootConfigurationEntry.setStatus("current")


class _OsbcIndex_Type(Integer32):
    """Custom type osbcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsbcIndex_Type.__name__ = "Integer32"
_OsbcIndex_Object = MibTableColumn
osbcIndex = _OsbcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 1),
    _OsbcIndex_Type()
)
osbcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcIndex.setStatus("current")
_OsbcBootDirectory_Type = WtcsDisplayString
_OsbcBootDirectory_Object = MibTableColumn
osbcBootDirectory = _OsbcBootDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 2),
    _OsbcBootDirectory_Type()
)
osbcBootDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcBootDirectory.setStatus("current")


class _OsbcCaption_Type(WtcsDisplayString):
    """Custom type osbcCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsbcCaption_Type.__name__ = "WtcsDisplayString"
_OsbcCaption_Object = MibTableColumn
osbcCaption = _OsbcCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 3),
    _OsbcCaption_Type()
)
osbcCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcCaption.setStatus("current")
_OsbcConfigurationPath_Type = WtcsDisplayString
_OsbcConfigurationPath_Object = MibTableColumn
osbcConfigurationPath = _OsbcConfigurationPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 4),
    _OsbcConfigurationPath_Type()
)
osbcConfigurationPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcConfigurationPath.setStatus("current")
_OsbcDescription_Type = WtcsDisplayString
_OsbcDescription_Object = MibTableColumn
osbcDescription = _OsbcDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 5),
    _OsbcDescription_Type()
)
osbcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcDescription.setStatus("current")
_OsbcLastDrive_Type = WtcsDisplayString
_OsbcLastDrive_Object = MibTableColumn
osbcLastDrive = _OsbcLastDrive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 6),
    _OsbcLastDrive_Type()
)
osbcLastDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcLastDrive.setStatus("current")


class _OsbcName_Type(WtcsDisplayString):
    """Custom type osbcName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsbcName_Type.__name__ = "WtcsDisplayString"
_OsbcName_Object = MibTableColumn
osbcName = _OsbcName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 7),
    _OsbcName_Type()
)
osbcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcName.setStatus("current")
_OsbcScratchDirectory_Type = WtcsDisplayString
_OsbcScratchDirectory_Object = MibTableColumn
osbcScratchDirectory = _OsbcScratchDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 8),
    _OsbcScratchDirectory_Type()
)
osbcScratchDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcScratchDirectory.setStatus("current")


class _OsbcSettingID_Type(WtcsDisplayString):
    """Custom type osbcSettingID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsbcSettingID_Type.__name__ = "WtcsDisplayString"
_OsbcSettingID_Object = MibTableColumn
osbcSettingID = _OsbcSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 9),
    _OsbcSettingID_Type()
)
osbcSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcSettingID.setStatus("current")
_OsbcTempDirectory_Type = WtcsDisplayString
_OsbcTempDirectory_Object = MibTableColumn
osbcTempDirectory = _OsbcTempDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 1, 1, 10),
    _OsbcTempDirectory_Type()
)
osbcTempDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osbcTempDirectory.setStatus("current")
_Win32ComputerSystemTable_Object = MibTable
win32ComputerSystemTable = _Win32ComputerSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2)
)
if mibBuilder.loadTexts:
    win32ComputerSystemTable.setStatus("current")
_Win32ComputerSystemEntry_Object = MibTableRow
win32ComputerSystemEntry = _Win32ComputerSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1)
)
win32ComputerSystemEntry.setIndexNames(
    (0, "INFORMANT-OS", "oscsIndex"),
)
if mibBuilder.loadTexts:
    win32ComputerSystemEntry.setStatus("current")


class _OscsIndex_Type(Integer32):
    """Custom type oscsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OscsIndex_Type.__name__ = "Integer32"
_OscsIndex_Object = MibTableColumn
oscsIndex = _OscsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 1),
    _OscsIndex_Type()
)
oscsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsIndex.setStatus("current")


class _OscsAdminPasswordStatus_Type(Integer32):
    """Custom type oscsAdminPasswordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("notImplemented", 3),
          ("unknown", 4))
    )


_OscsAdminPasswordStatus_Type.__name__ = "Integer32"
_OscsAdminPasswordStatus_Object = MibTableColumn
oscsAdminPasswordStatus = _OscsAdminPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 2),
    _OscsAdminPasswordStatus_Type()
)
oscsAdminPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsAdminPasswordStatus.setStatus("current")
_OscsAutomaticResetBootOption_Type = TruthValue
_OscsAutomaticResetBootOption_Object = MibTableColumn
oscsAutomaticResetBootOption = _OscsAutomaticResetBootOption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 3),
    _OscsAutomaticResetBootOption_Type()
)
oscsAutomaticResetBootOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsAutomaticResetBootOption.setStatus("current")
_OscsAutomaticResetCapability_Type = TruthValue
_OscsAutomaticResetCapability_Object = MibTableColumn
oscsAutomaticResetCapability = _OscsAutomaticResetCapability_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 4),
    _OscsAutomaticResetCapability_Type()
)
oscsAutomaticResetCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsAutomaticResetCapability.setStatus("current")


class _OscsBootOptionOnLimit_Type(Integer32):
    """Custom type oscsBootOptionOnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doNotReboot", 4),
          ("operatingSystem", 2),
          ("reserved", 1),
          ("systemUtilities", 3))
    )


_OscsBootOptionOnLimit_Type.__name__ = "Integer32"
_OscsBootOptionOnLimit_Object = MibTableColumn
oscsBootOptionOnLimit = _OscsBootOptionOnLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 5),
    _OscsBootOptionOnLimit_Type()
)
oscsBootOptionOnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsBootOptionOnLimit.setStatus("current")


class _OscsBootOptionOnWatchDog_Type(Integer32):
    """Custom type oscsBootOptionOnWatchDog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doNotReboot", 4),
          ("operatingSystem", 2),
          ("reserved", 1),
          ("systemUtilities", 3))
    )


_OscsBootOptionOnWatchDog_Type.__name__ = "Integer32"
_OscsBootOptionOnWatchDog_Object = MibTableColumn
oscsBootOptionOnWatchDog = _OscsBootOptionOnWatchDog_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 6),
    _OscsBootOptionOnWatchDog_Type()
)
oscsBootOptionOnWatchDog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsBootOptionOnWatchDog.setStatus("current")
_OscsBootROMSupported_Type = TruthValue
_OscsBootROMSupported_Object = MibTableColumn
oscsBootROMSupported = _OscsBootROMSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 7),
    _OscsBootROMSupported_Type()
)
oscsBootROMSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsBootROMSupported.setStatus("current")


class _OscsBootupState_Type(Integer32):
    """Custom type oscsBootupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failsafeBoot", 2),
          ("failsafeWithNetworkBoot", 3),
          ("normalBoot", 1))
    )


_OscsBootupState_Type.__name__ = "Integer32"
_OscsBootupState_Object = MibTableColumn
oscsBootupState = _OscsBootupState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 8),
    _OscsBootupState_Type()
)
oscsBootupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsBootupState.setStatus("current")
_OscsCaption_Type = WtcsDisplayString
_OscsCaption_Object = MibTableColumn
oscsCaption = _OscsCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 9),
    _OscsCaption_Type()
)
oscsCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsCaption.setStatus("current")


class _OscsChassisBootupState_Type(Integer32):
    """Custom type oscsChassisBootupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("nonrecoverable", 6),
          ("other", 1),
          ("safes", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OscsChassisBootupState_Type.__name__ = "Integer32"
_OscsChassisBootupState_Object = MibTableColumn
oscsChassisBootupState = _OscsChassisBootupState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 10),
    _OscsChassisBootupState_Type()
)
oscsChassisBootupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsChassisBootupState.setStatus("current")
_OscsCreationClassName_Type = WtcsDisplayString
_OscsCreationClassName_Object = MibTableColumn
oscsCreationClassName = _OscsCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 11),
    _OscsCreationClassName_Type()
)
oscsCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsCreationClassName.setStatus("current")
_OscsCurrentTimeZone_Type = Integer32
_OscsCurrentTimeZone_Object = MibTableColumn
oscsCurrentTimeZone = _OscsCurrentTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 12),
    _OscsCurrentTimeZone_Type()
)
oscsCurrentTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsCurrentTimeZone.setStatus("current")
if mibBuilder.loadTexts:
    oscsCurrentTimeZone.setUnits("Minutes")
_OscsDaylightInEffect_Type = TruthValue
_OscsDaylightInEffect_Object = MibTableColumn
oscsDaylightInEffect = _OscsDaylightInEffect_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 13),
    _OscsDaylightInEffect_Type()
)
oscsDaylightInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsDaylightInEffect.setStatus("current")
_OscsDescription_Type = WtcsDisplayString
_OscsDescription_Object = MibTableColumn
oscsDescription = _OscsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 14),
    _OscsDescription_Type()
)
oscsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsDescription.setStatus("current")
_OscsDNSHostName_Type = WtcsDisplayString
_OscsDNSHostName_Object = MibTableColumn
oscsDNSHostName = _OscsDNSHostName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 15),
    _OscsDNSHostName_Type()
)
oscsDNSHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsDNSHostName.setStatus("current")
_OscsDomain_Type = WtcsDisplayString
_OscsDomain_Object = MibTableColumn
oscsDomain = _OscsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 16),
    _OscsDomain_Type()
)
oscsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsDomain.setStatus("current")


class _OscsDomainRole_Type(Integer32):
    """Custom type oscsDomainRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("backupDomainController", 4),
          ("memberServer", 3),
          ("memberWorkstation", 1),
          ("primaryDomainController", 5),
          ("standaloneServer", 2),
          ("standaloneWorkstation", 0))
    )


_OscsDomainRole_Type.__name__ = "Integer32"
_OscsDomainRole_Object = MibTableColumn
oscsDomainRole = _OscsDomainRole_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 17),
    _OscsDomainRole_Type()
)
oscsDomainRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsDomainRole.setStatus("current")
_OscsEnableDaylightSavingsTime_Type = TruthValue
_OscsEnableDaylightSavingsTime_Object = MibTableColumn
oscsEnableDaylightSavingsTime = _OscsEnableDaylightSavingsTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 18),
    _OscsEnableDaylightSavingsTime_Type()
)
oscsEnableDaylightSavingsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsEnableDaylightSavingsTime.setStatus("current")


class _OscsFrontPanelResetStatus_Type(Integer32):
    """Custom type oscsFrontPanelResetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notImplemented", 2),
          ("unknown", 3))
    )


_OscsFrontPanelResetStatus_Type.__name__ = "Integer32"
_OscsFrontPanelResetStatus_Object = MibTableColumn
oscsFrontPanelResetStatus = _OscsFrontPanelResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 19),
    _OscsFrontPanelResetStatus_Type()
)
oscsFrontPanelResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsFrontPanelResetStatus.setStatus("current")
_OscsInfraredSupported_Type = TruthValue
_OscsInfraredSupported_Object = MibTableColumn
oscsInfraredSupported = _OscsInfraredSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 20),
    _OscsInfraredSupported_Type()
)
oscsInfraredSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsInfraredSupported.setStatus("current")
_OscsInitialLoadInfo_Type = WtcsDisplayString
_OscsInitialLoadInfo_Object = MibTableColumn
oscsInitialLoadInfo = _OscsInitialLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 21),
    _OscsInitialLoadInfo_Type()
)
oscsInitialLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsInitialLoadInfo.setStatus("current")
_OscsInstallDate_Type = DateAndTime
_OscsInstallDate_Object = MibTableColumn
oscsInstallDate = _OscsInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 22),
    _OscsInstallDate_Type()
)
oscsInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsInstallDate.setStatus("current")


class _OscsKeyboardPasswordStatus_Type(Integer32):
    """Custom type oscsKeyboardPasswordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notImplemented", 2),
          ("unknown", 3))
    )


_OscsKeyboardPasswordStatus_Type.__name__ = "Integer32"
_OscsKeyboardPasswordStatus_Object = MibTableColumn
oscsKeyboardPasswordStatus = _OscsKeyboardPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 23),
    _OscsKeyboardPasswordStatus_Type()
)
oscsKeyboardPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsKeyboardPasswordStatus.setStatus("current")
_OscsLastLoadInfo_Type = WtcsDisplayString
_OscsLastLoadInfo_Object = MibTableColumn
oscsLastLoadInfo = _OscsLastLoadInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 24),
    _OscsLastLoadInfo_Type()
)
oscsLastLoadInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsLastLoadInfo.setStatus("current")
_OscsManufacturer_Type = WtcsDisplayString
_OscsManufacturer_Object = MibTableColumn
oscsManufacturer = _OscsManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 25),
    _OscsManufacturer_Type()
)
oscsManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsManufacturer.setStatus("current")
_OscsModel_Type = WtcsDisplayString
_OscsModel_Object = MibTableColumn
oscsModel = _OscsModel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 26),
    _OscsModel_Type()
)
oscsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsModel.setStatus("current")
_OscsName_Type = WtcsDisplayString
_OscsName_Object = MibTableColumn
oscsName = _OscsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 27),
    _OscsName_Type()
)
oscsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsName.setStatus("current")


class _OscsNameFormat_Type(Integer32):
    """Custom type oscsNameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dcc", 10),
          ("dial", 3),
          ("e164", 12),
          ("hid", 4),
          ("hwa", 6),
          ("icd", 11),
          ("ip", 2),
          ("ipx", 9),
          ("isdn", 8),
          ("nwa", 5),
          ("osi", 14),
          ("other", 15),
          ("sna", 13),
          ("x25", 7))
    )


_OscsNameFormat_Type.__name__ = "Integer32"
_OscsNameFormat_Object = MibTableColumn
oscsNameFormat = _OscsNameFormat_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 28),
    _OscsNameFormat_Type()
)
oscsNameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsNameFormat.setStatus("current")
_OscsNetworkServerModeEnabled_Type = TruthValue
_OscsNetworkServerModeEnabled_Object = MibTableColumn
oscsNetworkServerModeEnabled = _OscsNetworkServerModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 29),
    _OscsNetworkServerModeEnabled_Type()
)
oscsNetworkServerModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsNetworkServerModeEnabled.setStatus("current")
_OscsNumberOfProcessors_Type = Gauge32
_OscsNumberOfProcessors_Object = MibTableColumn
oscsNumberOfProcessors = _OscsNumberOfProcessors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 30),
    _OscsNumberOfProcessors_Type()
)
oscsNumberOfProcessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsNumberOfProcessors.setStatus("current")
_OscsOEMLogoBitmap_Type = WtcsDisplayString
_OscsOEMLogoBitmap_Object = MibTableColumn
oscsOEMLogoBitmap = _OscsOEMLogoBitmap_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 31),
    _OscsOEMLogoBitmap_Type()
)
oscsOEMLogoBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsOEMLogoBitmap.setStatus("current")
_OscsOEMStringArray_Type = WtcsDisplayString
_OscsOEMStringArray_Object = MibTableColumn
oscsOEMStringArray = _OscsOEMStringArray_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 32),
    _OscsOEMStringArray_Type()
)
oscsOEMStringArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsOEMStringArray.setStatus("current")
_OscsPartOfDomain_Type = TruthValue
_OscsPartOfDomain_Object = MibTableColumn
oscsPartOfDomain = _OscsPartOfDomain_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 33),
    _OscsPartOfDomain_Type()
)
oscsPartOfDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPartOfDomain.setStatus("current")
_OscsPauseAfterReset_Type = Integer32
_OscsPauseAfterReset_Object = MibTableColumn
oscsPauseAfterReset = _OscsPauseAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 34),
    _OscsPauseAfterReset_Type()
)
oscsPauseAfterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPauseAfterReset.setStatus("current")
if mibBuilder.loadTexts:
    oscsPauseAfterReset.setUnits("Milliseconds")
_OscsPowerManagementCapabilities_Type = WtcsDisplayString
_OscsPowerManagementCapabilities_Object = MibTableColumn
oscsPowerManagementCapabilities = _OscsPowerManagementCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 35),
    _OscsPowerManagementCapabilities_Type()
)
oscsPowerManagementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPowerManagementCapabilities.setStatus("current")
_OscsPowerManagementSupported_Type = TruthValue
_OscsPowerManagementSupported_Object = MibTableColumn
oscsPowerManagementSupported = _OscsPowerManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 36),
    _OscsPowerManagementSupported_Type()
)
oscsPowerManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPowerManagementSupported.setStatus("current")


class _OscsPowerOnPasswordStatus_Type(Integer32):
    """Custom type oscsPowerOnPasswordStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("notImplemented", 2),
          ("unknown", 3))
    )


_OscsPowerOnPasswordStatus_Type.__name__ = "Integer32"
_OscsPowerOnPasswordStatus_Object = MibTableColumn
oscsPowerOnPasswordStatus = _OscsPowerOnPasswordStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 37),
    _OscsPowerOnPasswordStatus_Type()
)
oscsPowerOnPasswordStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPowerOnPasswordStatus.setStatus("current")


class _OscsPowerState_Type(Integer32):
    """Custom type oscsPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fullPower", 1),
          ("powerCycle", 5),
          ("powerOff", 6),
          ("powerSaveLowPowerMode", 2),
          ("powerSaveStandby", 3),
          ("powerSaveUnknown", 4),
          ("powerSaveWarning", 7),
          ("unknown", 0))
    )


_OscsPowerState_Type.__name__ = "Integer32"
_OscsPowerState_Object = MibTableColumn
oscsPowerState = _OscsPowerState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 38),
    _OscsPowerState_Type()
)
oscsPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPowerState.setStatus("current")


class _OscsPowerSupplyState_Type(Integer32):
    """Custom type oscsPowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("nonrecoverable", 6),
          ("other", 1),
          ("safe", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OscsPowerSupplyState_Type.__name__ = "Integer32"
_OscsPowerSupplyState_Object = MibTableColumn
oscsPowerSupplyState = _OscsPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 39),
    _OscsPowerSupplyState_Type()
)
oscsPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPowerSupplyState.setStatus("current")
_OscsPrimaryOwnerContact_Type = WtcsDisplayString
_OscsPrimaryOwnerContact_Object = MibTableColumn
oscsPrimaryOwnerContact = _OscsPrimaryOwnerContact_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 40),
    _OscsPrimaryOwnerContact_Type()
)
oscsPrimaryOwnerContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPrimaryOwnerContact.setStatus("current")
_OscsPrimaryOwnerName_Type = WtcsDisplayString
_OscsPrimaryOwnerName_Object = MibTableColumn
oscsPrimaryOwnerName = _OscsPrimaryOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 41),
    _OscsPrimaryOwnerName_Type()
)
oscsPrimaryOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPrimaryOwnerName.setStatus("current")


class _OscsResetCapability_Type(Integer32):
    """Custom type oscsResetCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 4),
          ("nonrecoverable", 5),
          ("other", 1),
          ("unknown", 2))
    )


_OscsResetCapability_Type.__name__ = "Integer32"
_OscsResetCapability_Object = MibTableColumn
oscsResetCapability = _OscsResetCapability_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 42),
    _OscsResetCapability_Type()
)
oscsResetCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsResetCapability.setStatus("current")
_OscsResetCount_Type = Integer32
_OscsResetCount_Object = MibTableColumn
oscsResetCount = _OscsResetCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 43),
    _OscsResetCount_Type()
)
oscsResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsResetCount.setStatus("current")
_OscsResetLimit_Type = Integer32
_OscsResetLimit_Object = MibTableColumn
oscsResetLimit = _OscsResetLimit_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 44),
    _OscsResetLimit_Type()
)
oscsResetLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsResetLimit.setStatus("current")
_OscsRoles_Type = WtcsDisplayString
_OscsRoles_Object = MibTableColumn
oscsRoles = _OscsRoles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 45),
    _OscsRoles_Type()
)
oscsRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsRoles.setStatus("current")


class _OscsStatus_Type(Integer32):
    """Custom type oscsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OscsStatus_Type.__name__ = "Integer32"
_OscsStatus_Object = MibTableColumn
oscsStatus = _OscsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 46),
    _OscsStatus_Type()
)
oscsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsStatus.setStatus("current")
_OscsSupportContactDescription_Type = WtcsDisplayString
_OscsSupportContactDescription_Object = MibTableColumn
oscsSupportContactDescription = _OscsSupportContactDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 47),
    _OscsSupportContactDescription_Type()
)
oscsSupportContactDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsSupportContactDescription.setStatus("current")


class _OscsSystemStartupDelay_Type(Integer32):
    """Custom type oscsSystemStartupDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OscsSystemStartupDelay_Type.__name__ = "Integer32"
_OscsSystemStartupDelay_Object = MibTableColumn
oscsSystemStartupDelay = _OscsSystemStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 48),
    _OscsSystemStartupDelay_Type()
)
oscsSystemStartupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsSystemStartupDelay.setStatus("current")
if mibBuilder.loadTexts:
    oscsSystemStartupDelay.setUnits("Seconds")
_OscsSystemStartupOptions_Type = WtcsDisplayString
_OscsSystemStartupOptions_Object = MibTableColumn
oscsSystemStartupOptions = _OscsSystemStartupOptions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 49),
    _OscsSystemStartupOptions_Type()
)
oscsSystemStartupOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsSystemStartupOptions.setStatus("current")


class _OscsSystemStartupSetting_Type(Integer32):
    """Custom type oscsSystemStartupSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OscsSystemStartupSetting_Type.__name__ = "Integer32"
_OscsSystemStartupSetting_Object = MibTableColumn
oscsSystemStartupSetting = _OscsSystemStartupSetting_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 50),
    _OscsSystemStartupSetting_Type()
)
oscsSystemStartupSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsSystemStartupSetting.setStatus("current")


class _OscsSystemType_Type(Integer32):
    """Custom type oscsSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("alphaBasedPC", 3),
          ("mipsBasedPC", 2),
          ("n64bitAlphaPC", 8),
          ("n64bitIntelPC", 7),
          ("powerPC", 4),
          ("shxPC", 5),
          ("strongARMPC", 6),
          ("unknown", 9),
          ("x86BasedPC", 1),
          ("x86Nec98PC", 10))
    )


_OscsSystemType_Type.__name__ = "Integer32"
_OscsSystemType_Object = MibTableColumn
oscsSystemType = _OscsSystemType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 51),
    _OscsSystemType_Type()
)
oscsSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsSystemType.setStatus("current")


class _OscsThermalState_Type(Integer32):
    """Custom type oscsThermalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("nonrecoverable", 6),
          ("other", 1),
          ("safe", 3),
          ("unknown", 2),
          ("warning", 4))
    )


_OscsThermalState_Type.__name__ = "Integer32"
_OscsThermalState_Object = MibTableColumn
oscsThermalState = _OscsThermalState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 52),
    _OscsThermalState_Type()
)
oscsThermalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsThermalState.setStatus("current")
_OscsTotalPhysicalMemory_Type = Gauge32
_OscsTotalPhysicalMemory_Object = MibTableColumn
oscsTotalPhysicalMemory = _OscsTotalPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 53),
    _OscsTotalPhysicalMemory_Type()
)
oscsTotalPhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsTotalPhysicalMemory.setStatus("current")
if mibBuilder.loadTexts:
    oscsTotalPhysicalMemory.setUnits("Bytes")
_OscsUserName_Type = WtcsDisplayString
_OscsUserName_Object = MibTableColumn
oscsUserName = _OscsUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 54),
    _OscsUserName_Type()
)
oscsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsUserName.setStatus("current")


class _OscsWakeUpType_Type(Integer32):
    """Custom type oscsWakeUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("acPowerRestored", 8),
          ("apmTimer", 3),
          ("lanRemote", 5),
          ("modemRing", 4),
          ("other", 1),
          ("pciPME", 7),
          ("powerSwitch", 6),
          ("reserved", 0),
          ("unknown", 2))
    )


_OscsWakeUpType_Type.__name__ = "Integer32"
_OscsWakeUpType_Object = MibTableColumn
oscsWakeUpType = _OscsWakeUpType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 55),
    _OscsWakeUpType_Type()
)
oscsWakeUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsWakeUpType.setStatus("current")
_OscsWorkgroup_Type = WtcsDisplayString
_OscsWorkgroup_Object = MibTableColumn
oscsWorkgroup = _OscsWorkgroup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 56),
    _OscsWorkgroup_Type()
)
oscsWorkgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsWorkgroup.setStatus("current")
_OscsAutomaticManagedPagefile_Type = TruthValue
_OscsAutomaticManagedPagefile_Object = MibTableColumn
oscsAutomaticManagedPagefile = _OscsAutomaticManagedPagefile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 57),
    _OscsAutomaticManagedPagefile_Type()
)
oscsAutomaticManagedPagefile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsAutomaticManagedPagefile.setStatus("current")
_OscsNumberOfLogicalProcessors_Type = Integer32
_OscsNumberOfLogicalProcessors_Object = MibTableColumn
oscsNumberOfLogicalProcessors = _OscsNumberOfLogicalProcessors_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 58),
    _OscsNumberOfLogicalProcessors_Type()
)
oscsNumberOfLogicalProcessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsNumberOfLogicalProcessors.setStatus("current")


class _OscsPCSystemType_Type(Integer32):
    """Custom type oscsPCSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("appliancePC", 6),
          ("desktop", 1),
          ("enterpriseServer", 4),
          ("maximum", 8),
          ("mobile", 2),
          ("performanceServer", 7),
          ("sohoServer", 5),
          ("unspecified", 0),
          ("workstation", 3))
    )


_OscsPCSystemType_Type.__name__ = "Integer32"
_OscsPCSystemType_Object = MibTableColumn
oscsPCSystemType = _OscsPCSystemType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 2, 1, 59),
    _OscsPCSystemType_Type()
)
oscsPCSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscsPCSystemType.setStatus("current")
_Win32ComputerSystemProductTable_Object = MibTable
win32ComputerSystemProductTable = _Win32ComputerSystemProductTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3)
)
if mibBuilder.loadTexts:
    win32ComputerSystemProductTable.setStatus("current")
_Win32ComputerSystemProductEntry_Object = MibTableRow
win32ComputerSystemProductEntry = _Win32ComputerSystemProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1)
)
win32ComputerSystemProductEntry.setIndexNames(
    (0, "INFORMANT-OS", "oscspIndex"),
)
if mibBuilder.loadTexts:
    win32ComputerSystemProductEntry.setStatus("current")


class _OscspIndex_Type(Integer32):
    """Custom type oscspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OscspIndex_Type.__name__ = "Integer32"
_OscspIndex_Object = MibTableColumn
oscspIndex = _OscspIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 1),
    _OscspIndex_Type()
)
oscspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspIndex.setStatus("current")


class _OscspCaption_Type(WtcsDisplayString):
    """Custom type oscspCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OscspCaption_Type.__name__ = "WtcsDisplayString"
_OscspCaption_Object = MibTableColumn
oscspCaption = _OscspCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 2),
    _OscspCaption_Type()
)
oscspCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspCaption.setStatus("current")
_OscspDescription_Type = WtcsDisplayString
_OscspDescription_Object = MibTableColumn
oscspDescription = _OscspDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 3),
    _OscspDescription_Type()
)
oscspDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspDescription.setStatus("current")


class _OscspIdentifyingNumber_Type(WtcsDisplayString):
    """Custom type oscspIdentifyingNumber based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OscspIdentifyingNumber_Type.__name__ = "WtcsDisplayString"
_OscspIdentifyingNumber_Object = MibTableColumn
oscspIdentifyingNumber = _OscspIdentifyingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 4),
    _OscspIdentifyingNumber_Type()
)
oscspIdentifyingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspIdentifyingNumber.setStatus("current")


class _OscspName_Type(WtcsDisplayString):
    """Custom type oscspName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OscspName_Type.__name__ = "WtcsDisplayString"
_OscspName_Object = MibTableColumn
oscspName = _OscspName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 5),
    _OscspName_Type()
)
oscspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspName.setStatus("current")


class _OscspSKUNumber_Type(WtcsDisplayString):
    """Custom type oscspSKUNumber based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OscspSKUNumber_Type.__name__ = "WtcsDisplayString"
_OscspSKUNumber_Object = MibTableColumn
oscspSKUNumber = _OscspSKUNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 6),
    _OscspSKUNumber_Type()
)
oscspSKUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspSKUNumber.setStatus("current")
_OscspUUID_Type = WtcsDisplayString
_OscspUUID_Object = MibTableColumn
oscspUUID = _OscspUUID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 7),
    _OscspUUID_Type()
)
oscspUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspUUID.setStatus("current")


class _OscspVendor_Type(WtcsDisplayString):
    """Custom type oscspVendor based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OscspVendor_Type.__name__ = "WtcsDisplayString"
_OscspVendor_Object = MibTableColumn
oscspVendor = _OscspVendor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 8),
    _OscspVendor_Type()
)
oscspVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspVendor.setStatus("current")


class _OscspVersion_Type(WtcsDisplayString):
    """Custom type oscspVersion based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OscspVersion_Type.__name__ = "WtcsDisplayString"
_OscspVersion_Object = MibTableColumn
oscspVersion = _OscspVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 3, 1, 9),
    _OscspVersion_Type()
)
oscspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscspVersion.setStatus("current")
_Win32LoadOrderGroupTable_Object = MibTable
win32LoadOrderGroupTable = _Win32LoadOrderGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4)
)
if mibBuilder.loadTexts:
    win32LoadOrderGroupTable.setStatus("current")
_Win32LoadOrderGroupEntry_Object = MibTableRow
win32LoadOrderGroupEntry = _Win32LoadOrderGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1)
)
win32LoadOrderGroupEntry.setIndexNames(
    (0, "INFORMANT-OS", "oslogIndex"),
)
if mibBuilder.loadTexts:
    win32LoadOrderGroupEntry.setStatus("current")


class _OslogIndex_Type(Integer32):
    """Custom type oslogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OslogIndex_Type.__name__ = "Integer32"
_OslogIndex_Object = MibTableColumn
oslogIndex = _OslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 1),
    _OslogIndex_Type()
)
oslogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogIndex.setStatus("current")
_OslogCaption_Type = WtcsDisplayString
_OslogCaption_Object = MibTableColumn
oslogCaption = _OslogCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 2),
    _OslogCaption_Type()
)
oslogCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogCaption.setStatus("current")
_OslogDescription_Type = WtcsDisplayString
_OslogDescription_Object = MibTableColumn
oslogDescription = _OslogDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 3),
    _OslogDescription_Type()
)
oslogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogDescription.setStatus("current")
_OslogDriverEnabled_Type = TruthValue
_OslogDriverEnabled_Object = MibTableColumn
oslogDriverEnabled = _OslogDriverEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 4),
    _OslogDriverEnabled_Type()
)
oslogDriverEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogDriverEnabled.setStatus("current")
_OslogGroupOrder_Type = Gauge32
_OslogGroupOrder_Object = MibTableColumn
oslogGroupOrder = _OslogGroupOrder_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 5),
    _OslogGroupOrder_Type()
)
oslogGroupOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogGroupOrder.setStatus("current")
_OslogInstallDate_Type = DateAndTime
_OslogInstallDate_Object = MibTableColumn
oslogInstallDate = _OslogInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 6),
    _OslogInstallDate_Type()
)
oslogInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogInstallDate.setStatus("current")
_OslogName_Type = WtcsDisplayString
_OslogName_Object = MibTableColumn
oslogName = _OslogName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 7),
    _OslogName_Type()
)
oslogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogName.setStatus("current")


class _OslogStatus_Type(Integer32):
    """Custom type oslogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OslogStatus_Type.__name__ = "Integer32"
_OslogStatus_Object = MibTableColumn
oslogStatus = _OslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 4, 1, 8),
    _OslogStatus_Type()
)
oslogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oslogStatus.setStatus("current")
_Win32OperatingSystemTable_Object = MibTable
win32OperatingSystemTable = _Win32OperatingSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5)
)
if mibBuilder.loadTexts:
    win32OperatingSystemTable.setStatus("current")
_Win32OperatingSystemEntry_Object = MibTableRow
win32OperatingSystemEntry = _Win32OperatingSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1)
)
win32OperatingSystemEntry.setIndexNames(
    (0, "INFORMANT-OS", "ososIndex"),
)
if mibBuilder.loadTexts:
    win32OperatingSystemEntry.setStatus("current")


class _OsosIndex_Type(Integer32):
    """Custom type ososIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsosIndex_Type.__name__ = "Integer32"
_OsosIndex_Object = MibTableColumn
ososIndex = _OsosIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 1),
    _OsosIndex_Type()
)
ososIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososIndex.setStatus("current")
_OsosBootDevice_Type = WtcsDisplayString
_OsosBootDevice_Object = MibTableColumn
ososBootDevice = _OsosBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 2),
    _OsosBootDevice_Type()
)
ososBootDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososBootDevice.setStatus("current")
_OsosBuildNumber_Type = WtcsDisplayString
_OsosBuildNumber_Object = MibTableColumn
ososBuildNumber = _OsosBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 3),
    _OsosBuildNumber_Type()
)
ososBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososBuildNumber.setStatus("current")
_OsosBuildType_Type = WtcsDisplayString
_OsosBuildType_Object = MibTableColumn
ososBuildType = _OsosBuildType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 4),
    _OsosBuildType_Type()
)
ososBuildType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososBuildType.setStatus("current")
_OsosCaption_Type = WtcsDisplayString
_OsosCaption_Object = MibTableColumn
ososCaption = _OsosCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 5),
    _OsosCaption_Type()
)
ososCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCaption.setStatus("current")


class _OsosCodeSet_Type(WtcsDisplayString):
    """Custom type ososCodeSet based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OsosCodeSet_Type.__name__ = "WtcsDisplayString"
_OsosCodeSet_Object = MibTableColumn
ososCodeSet = _OsosCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 6),
    _OsosCodeSet_Type()
)
ososCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCodeSet.setStatus("current")
_OsosCountryCode_Type = WtcsDisplayString
_OsosCountryCode_Object = MibTableColumn
ososCountryCode = _OsosCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 7),
    _OsosCountryCode_Type()
)
ososCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCountryCode.setStatus("current")


class _OsosCreationClassName_Type(WtcsDisplayString):
    """Custom type ososCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsosCreationClassName_Type.__name__ = "WtcsDisplayString"
_OsosCreationClassName_Object = MibTableColumn
ososCreationClassName = _OsosCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 8),
    _OsosCreationClassName_Type()
)
ososCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCreationClassName.setStatus("current")
_OsosCSCreationClassName_Type = WtcsDisplayString
_OsosCSCreationClassName_Object = MibTableColumn
ososCSCreationClassName = _OsosCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 9),
    _OsosCSCreationClassName_Type()
)
ososCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCSCreationClassName.setStatus("current")
_OsosCSDVersion_Type = WtcsDisplayString
_OsosCSDVersion_Object = MibTableColumn
ososCSDVersion = _OsosCSDVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 10),
    _OsosCSDVersion_Type()
)
ososCSDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCSDVersion.setStatus("current")
_OsosCSName_Type = WtcsDisplayString
_OsosCSName_Object = MibTableColumn
ososCSName = _OsosCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 11),
    _OsosCSName_Type()
)
ososCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCSName.setStatus("current")
_OsosCurrentTimeZone_Type = Integer32
_OsosCurrentTimeZone_Object = MibTableColumn
ososCurrentTimeZone = _OsosCurrentTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 12),
    _OsosCurrentTimeZone_Type()
)
ososCurrentTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososCurrentTimeZone.setStatus("current")
_OsosDataExecPrevention32BitAppl_Type = TruthValue
_OsosDataExecPrevention32BitAppl_Object = MibTableColumn
ososDataExecPrevention32BitAppl = _OsosDataExecPrevention32BitAppl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 13),
    _OsosDataExecPrevention32BitAppl_Type()
)
ososDataExecPrevention32BitAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDataExecPrevention32BitAppl.setStatus("current")
_OsosDataExecPreventionAvailable_Type = TruthValue
_OsosDataExecPreventionAvailable_Object = MibTableColumn
ososDataExecPreventionAvailable = _OsosDataExecPreventionAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 14),
    _OsosDataExecPreventionAvailable_Type()
)
ososDataExecPreventionAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDataExecPreventionAvailable.setStatus("current")
_OsosDataExecPreventionDrivers_Type = TruthValue
_OsosDataExecPreventionDrivers_Object = MibTableColumn
ososDataExecPreventionDrivers = _OsosDataExecPreventionDrivers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 15),
    _OsosDataExecPreventionDrivers_Type()
)
ososDataExecPreventionDrivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDataExecPreventionDrivers.setStatus("current")
_OsosDebug_Type = TruthValue
_OsosDebug_Object = MibTableColumn
ososDebug = _OsosDebug_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 16),
    _OsosDebug_Type()
)
ososDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDebug.setStatus("current")
_OsosDescription_Type = WtcsDisplayString
_OsosDescription_Object = MibTableColumn
ososDescription = _OsosDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 17),
    _OsosDescription_Type()
)
ososDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDescription.setStatus("current")
_OsosDistributed_Type = TruthValue
_OsosDistributed_Object = MibTableColumn
ososDistributed = _OsosDistributed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 18),
    _OsosDistributed_Type()
)
ososDistributed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososDistributed.setStatus("current")
_OsosEncryptionLevel_Type = Gauge32
_OsosEncryptionLevel_Object = MibTableColumn
ososEncryptionLevel = _OsosEncryptionLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 19),
    _OsosEncryptionLevel_Type()
)
ososEncryptionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososEncryptionLevel.setStatus("current")


class _OsosForegroundApplicationBoost_Type(Integer32):
    """Custom type ososForegroundApplicationBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maximum", 2),
          ("minimum", 1),
          ("none", 0))
    )


_OsosForegroundApplicationBoost_Type.__name__ = "Integer32"
_OsosForegroundApplicationBoost_Object = MibTableColumn
ososForegroundApplicationBoost = _OsosForegroundApplicationBoost_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 20),
    _OsosForegroundApplicationBoost_Type()
)
ososForegroundApplicationBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososForegroundApplicationBoost.setStatus("current")
_OsosFreePhysicalMemory_Type = Gauge32
_OsosFreePhysicalMemory_Object = MibTableColumn
ososFreePhysicalMemory = _OsosFreePhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 21),
    _OsosFreePhysicalMemory_Type()
)
ososFreePhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososFreePhysicalMemory.setStatus("current")
_OsosFreeSpaceInPagingFiles_Type = Gauge32
_OsosFreeSpaceInPagingFiles_Object = MibTableColumn
ososFreeSpaceInPagingFiles = _OsosFreeSpaceInPagingFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 22),
    _OsosFreeSpaceInPagingFiles_Type()
)
ososFreeSpaceInPagingFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososFreeSpaceInPagingFiles.setStatus("current")
_OsosFreeVirtualMemory_Type = Gauge32
_OsosFreeVirtualMemory_Object = MibTableColumn
ososFreeVirtualMemory = _OsosFreeVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 23),
    _OsosFreeVirtualMemory_Type()
)
ososFreeVirtualMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososFreeVirtualMemory.setStatus("current")
_OsosInstallDate_Type = DateAndTime
_OsosInstallDate_Object = MibTableColumn
ososInstallDate = _OsosInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 24),
    _OsosInstallDate_Type()
)
ososInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososInstallDate.setStatus("current")


class _OsosLargeSystemCache_Type(Integer32):
    """Custom type ososLargeSystemCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("optimizeMemoryForApplications", 0),
          ("optimizeMemoryForSystemPerform", 1))
    )


_OsosLargeSystemCache_Type.__name__ = "Integer32"
_OsosLargeSystemCache_Object = MibTableColumn
ososLargeSystemCache = _OsosLargeSystemCache_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 25),
    _OsosLargeSystemCache_Type()
)
ososLargeSystemCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososLargeSystemCache.setStatus("current")
_OsosLastBootUpTime_Type = DateAndTime
_OsosLastBootUpTime_Object = MibTableColumn
ososLastBootUpTime = _OsosLastBootUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 26),
    _OsosLastBootUpTime_Type()
)
ososLastBootUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososLastBootUpTime.setStatus("current")
_OsosLocalDateTime_Type = DateAndTime
_OsosLocalDateTime_Object = MibTableColumn
ososLocalDateTime = _OsosLocalDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 27),
    _OsosLocalDateTime_Type()
)
ososLocalDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososLocalDateTime.setStatus("current")
_OsosLocale_Type = WtcsDisplayString
_OsosLocale_Object = MibTableColumn
ososLocale = _OsosLocale_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 28),
    _OsosLocale_Type()
)
ososLocale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososLocale.setStatus("current")
_OsosManufacturer_Type = WtcsDisplayString
_OsosManufacturer_Object = MibTableColumn
ososManufacturer = _OsosManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 29),
    _OsosManufacturer_Type()
)
ososManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososManufacturer.setStatus("current")
_OsosMaxNumberOfProcesses_Type = Gauge32
_OsosMaxNumberOfProcesses_Object = MibTableColumn
ososMaxNumberOfProcesses = _OsosMaxNumberOfProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 30),
    _OsosMaxNumberOfProcesses_Type()
)
ososMaxNumberOfProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososMaxNumberOfProcesses.setStatus("current")
_OsosMaxProcessMemorySize_Type = Gauge32
_OsosMaxProcessMemorySize_Object = MibTableColumn
ososMaxProcessMemorySize = _OsosMaxProcessMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 31),
    _OsosMaxProcessMemorySize_Type()
)
ososMaxProcessMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososMaxProcessMemorySize.setStatus("current")
_OsosName_Type = WtcsDisplayString
_OsosName_Object = MibTableColumn
ososName = _OsosName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 32),
    _OsosName_Type()
)
ososName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososName.setStatus("current")
_OsosNumberOfLicensedUsers_Type = Gauge32
_OsosNumberOfLicensedUsers_Object = MibTableColumn
ososNumberOfLicensedUsers = _OsosNumberOfLicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 33),
    _OsosNumberOfLicensedUsers_Type()
)
ososNumberOfLicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososNumberOfLicensedUsers.setStatus("current")
_OsosNumberOfProcesses_Type = Gauge32
_OsosNumberOfProcesses_Object = MibTableColumn
ososNumberOfProcesses = _OsosNumberOfProcesses_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 34),
    _OsosNumberOfProcesses_Type()
)
ososNumberOfProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososNumberOfProcesses.setStatus("current")
_OsosNumberOfUsers_Type = Gauge32
_OsosNumberOfUsers_Object = MibTableColumn
ososNumberOfUsers = _OsosNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 35),
    _OsosNumberOfUsers_Type()
)
ososNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososNumberOfUsers.setStatus("current")
_OsosOrganization_Type = WtcsDisplayString
_OsosOrganization_Object = MibTableColumn
ososOrganization = _OsosOrganization_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 36),
    _OsosOrganization_Type()
)
ososOrganization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososOrganization.setStatus("current")


class _OsosOSLanguage_Type(Integer32):
    """Custom type ososOSLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              9,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1065,
              1066,
              1069,
              1070,
              1071,
              1072,
              1073,
              1074,
              1076,
              1077,
              1078,
              1080,
              1081,
              1082,
              1084,
              1085,
              1086,
              2049,
              2052,
              2055,
              2057,
              2058,
              2060,
              2064,
              2067,
              2068,
              2070,
              2072,
              2073,
              2074,
              2077,
              3073,
              3076,
              3079,
              3081,
              3082,
              3084,
              3098,
              4097,
              4100,
              4103,
              4105,
              4106,
              4108,
              5121,
              5127,
              5129,
              5130,
              5132,
              6145,
              6153,
              6154,
              7169,
              7177,
              7178,
              8193,
              8201,
              8202,
              9217,
              9226,
              10241,
              10249,
              10250,
              11265,
              11273,
              11274,
              12289,
              12298,
              13313,
              13322,
              14337,
              14346,
              15361,
              15370,
              16385,
              16394,
              17418,
              18442,
              19466,
              20490)
        )
    )
    namedValues = NamedValues(
        *(("afrikaans", 1078),
          ("albanian", 1052),
          ("arabic", 1),
          ("arabicAlgeria", 5121),
          ("arabicBahrain", 15361),
          ("arabicEgypt", 3073),
          ("arabicIraq", 2049),
          ("arabicJordan", 11265),
          ("arabicKuwait", 13313),
          ("arabicLebanon", 12289),
          ("arabicLibya", 4097),
          ("arabicMorocco", 6145),
          ("arabicOman", 8193),
          ("arabicQatar", 16385),
          ("arabicSaudiArabia", 1025),
          ("arabicSyria", 10241),
          ("arabicTunisia", 7169),
          ("arabicUAE", 14337),
          ("arabicYemen", 9217),
          ("basque", 1069),
          ("belarusian", 1059),
          ("bulgarian", 1026),
          ("catalan", 1027),
          ("chinese", 4),
          ("chineseHongKongSAR", 3076),
          ("chinesePRC", 2052),
          ("chineseSingapore", 4100),
          ("chineseTaiwan", 1028),
          ("croatian", 1050),
          ("czech", 1029),
          ("danish", 1030),
          ("dutchBelgium", 2067),
          ("dutchNetherlands", 1043),
          ("english", 9),
          ("englishAustralia", 3081),
          ("englishBelize", 10249),
          ("englishCanada", 4105),
          ("englishIreland", 6153),
          ("englishJamaica", 8201),
          ("englishNewZealand", 5129),
          ("englishSouthAfrica", 7177),
          ("englishTrinidad", 11273),
          ("englishUnitedKingdom", 2057),
          ("englishUnitedStates", 1033),
          ("estonian", 1061),
          ("faeroese", 1080),
          ("farsi", 1065),
          ("finnish", 1035),
          ("frenchBelgium", 2060),
          ("frenchCanada", 3084),
          ("frenchFrance", 1036),
          ("frenchLuxembourg", 5132),
          ("frenchSwitzerland", 4108),
          ("gaelic", 1084),
          ("germanAustria", 3079),
          ("germanGermany", 1031),
          ("germanLiechtenstein", 5127),
          ("germanLuxembourg", 4103),
          ("germanSwitzerland", 2055),
          ("greek", 1032),
          ("hebrew", 1037),
          ("hindi", 1081),
          ("hungarian", 1038),
          ("icelandic", 1039),
          ("indonesian", 1057),
          ("italianItaly", 1040),
          ("italianSwitzerland", 2064),
          ("japanese", 1041),
          ("korean", 1042),
          ("latvian", 1062),
          ("lithuanian", 1063),
          ("macedonianFYROM", 1071),
          ("malayMalaysia", 1086),
          ("maltese", 1082),
          ("norwegianBokmal", 1044),
          ("norwegianNynorsk", 2068),
          ("polish", 1045),
          ("portugueseBrazil", 1046),
          ("portuguesePortugal", 2070),
          ("rhaetoRomanic", 1047),
          ("romanian", 1048),
          ("romanianMoldova", 2072),
          ("russian", 1049),
          ("russianMoldova", 2073),
          ("serbian", 1070),
          ("serbianCyrillic", 3098),
          ("serbianLatin", 2074),
          ("slovak", 1051),
          ("slovenian", 1060),
          ("spanishArgentina", 11274),
          ("spanishBolivia", 16394),
          ("spanishChile", 13322),
          ("spanishColombia", 9226),
          ("spanishCostaRica", 5130),
          ("spanishDominicanRepublic", 7178),
          ("spanishEcuador", 12298),
          ("spanishElSalvador", 17418),
          ("spanishGuatemala", 4106),
          ("spanishHonduras", 18442),
          ("spanishInternationalSort", 3082),
          ("spanishMexico", 2058),
          ("spanishNicaragua", 19466),
          ("spanishPanama", 6154),
          ("spanishParaguay", 15370),
          ("spanishPeru", 10250),
          ("spanishPuertoRico", 20490),
          ("spanishTraditionalSort", 1034),
          ("spanishUruguay", 14346),
          ("spanishVenezuela", 8202),
          ("sutu", 1072),
          ("swedish", 1053),
          ("swedishFinland", 2077),
          ("thai", 1054),
          ("tsonga", 1073),
          ("tswana", 1074),
          ("turkish", 1055),
          ("ukrainian", 1058),
          ("urdu", 1056),
          ("vietnamese", 1066),
          ("xhosa", 1076),
          ("yiddish", 1085),
          ("zulu", 1077))
    )


_OsosOSLanguage_Type.__name__ = "Integer32"
_OsosOSLanguage_Object = MibTableColumn
ososOSLanguage = _OsosOSLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 37),
    _OsosOSLanguage_Type()
)
ososOSLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososOSLanguage.setStatus("current")
_OsosOSProductSuite_Type = Gauge32
_OsosOSProductSuite_Object = MibTableColumn
ososOSProductSuite = _OsosOSProductSuite_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 38),
    _OsosOSProductSuite_Type()
)
ososOSProductSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososOSProductSuite.setStatus("current")


class _OsosOSType_Type(Integer32):
    """Custom type ososOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("aix", 9),
          ("aseries", 32),
          ("attunix", 3),
          ("beOS", 53),
          ("bs2000", 35),
          ("bsdunix", 41),
          ("dcOS", 23),
          ("decnt", 5),
          ("dgux", 4),
          ("digitalUnix", 6),
          ("epoc", 49),
          ("freeBSD", 42),
          ("gnuHurd", 44),
          ("hpMPE", 54),
          ("hpux", 8),
          ("inferno", 47),
          ("interactiveUNIX", 40),
          ("irix", 28),
          ("ixWorks", 50),
          ("javaVM", 13),
          ("linux", 36),
          ("lynx", 37),
          ("machKernel", 46),
          ("macros", 2),
          ("miNT", 52),
          ("msdos", 14),
          ("mvs", 10),
          ("ncr3000", 20),
          ("netBSD", 43),
          ("netWare", 21),
          ("nextStep", 55),
          ("openVMS", 7),
          ("os2", 12),
          ("os400", 11),
          ("os9", 45),
          ("osf", 22),
          ("other", 1),
          ("palmPilot", 56),
          ("qnx", 48),
          ("reliantUNIX", 24),
          ("rhapsody", 57),
          ("scoOpenServer", 26),
          ("scoUnixWare", 25),
          ("sequent", 27),
          ("solaris", 29),
          ("sunOS", 30),
          ("tandemNSK", 33),
          ("tandemNT", 34),
          ("u6000", 31),
          ("unknown", 0),
          ("vmESA", 39),
          ("vxWorks", 51),
          ("win3x", 15),
          ("win95", 16),
          ("win98", 17),
          ("wince", 19),
          ("winnt", 18),
          ("xenix", 38))
    )


_OsosOSType_Type.__name__ = "Integer32"
_OsosOSType_Object = MibTableColumn
ososOSType = _OsosOSType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 39),
    _OsosOSType_Type()
)
ososOSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososOSType.setStatus("current")
_OsosOtherTypeDescription_Type = WtcsDisplayString
_OsosOtherTypeDescription_Object = MibTableColumn
ososOtherTypeDescription = _OsosOtherTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 40),
    _OsosOtherTypeDescription_Type()
)
ososOtherTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososOtherTypeDescription.setStatus("current")
_OsosPAEEnabled_Type = TruthValue
_OsosPAEEnabled_Object = MibTableColumn
ososPAEEnabled = _OsosPAEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 41),
    _OsosPAEEnabled_Type()
)
ososPAEEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososPAEEnabled.setStatus("current")
_OsosPlusProductID_Type = WtcsDisplayString
_OsosPlusProductID_Object = MibTableColumn
ososPlusProductID = _OsosPlusProductID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 42),
    _OsosPlusProductID_Type()
)
ososPlusProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososPlusProductID.setStatus("current")
_OsosPlusVersionNumber_Type = WtcsDisplayString
_OsosPlusVersionNumber_Object = MibTableColumn
ososPlusVersionNumber = _OsosPlusVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 43),
    _OsosPlusVersionNumber_Type()
)
ososPlusVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososPlusVersionNumber.setStatus("current")
_OsosPrimary_Type = TruthValue
_OsosPrimary_Object = MibTableColumn
ososPrimary = _OsosPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 44),
    _OsosPrimary_Type()
)
ososPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososPrimary.setStatus("current")


class _OsosProductType_Type(Integer32):
    """Custom type ososProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domainController", 2),
          ("server", 3),
          ("workStation", 1))
    )


_OsosProductType_Type.__name__ = "Integer32"
_OsosProductType_Object = MibTableColumn
ososProductType = _OsosProductType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 45),
    _OsosProductType_Type()
)
ososProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososProductType.setStatus("current")


class _OsosQuantumLength_Type(Integer32):
    """Custom type ososQuantumLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneTick", 2),
          ("twoTicks", 3),
          ("unknown", 1))
    )


_OsosQuantumLength_Type.__name__ = "Integer32"
_OsosQuantumLength_Object = MibTableColumn
ososQuantumLength = _OsosQuantumLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 46),
    _OsosQuantumLength_Type()
)
ososQuantumLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososQuantumLength.setStatus("current")


class _OsosQuantumType_Type(Integer32):
    """Custom type ososQuantumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("unknown", 1),
          ("variable", 3))
    )


_OsosQuantumType_Type.__name__ = "Integer32"
_OsosQuantumType_Object = MibTableColumn
ososQuantumType = _OsosQuantumType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 47),
    _OsosQuantumType_Type()
)
ososQuantumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososQuantumType.setStatus("current")
_OsosRegisteredUser_Type = WtcsDisplayString
_OsosRegisteredUser_Object = MibTableColumn
ososRegisteredUser = _OsosRegisteredUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 48),
    _OsosRegisteredUser_Type()
)
ososRegisteredUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososRegisteredUser.setStatus("current")
_OsosSerialNumber_Type = WtcsDisplayString
_OsosSerialNumber_Object = MibTableColumn
ososSerialNumber = _OsosSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 49),
    _OsosSerialNumber_Type()
)
ososSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSerialNumber.setStatus("current")


class _OsosServicePackMajorVersion_Type(Integer32):
    """Custom type ososServicePackMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsosServicePackMajorVersion_Type.__name__ = "Integer32"
_OsosServicePackMajorVersion_Object = MibTableColumn
ososServicePackMajorVersion = _OsosServicePackMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 50),
    _OsosServicePackMajorVersion_Type()
)
ososServicePackMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososServicePackMajorVersion.setStatus("current")


class _OsosServicePackMinorVersion_Type(Integer32):
    """Custom type ososServicePackMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsosServicePackMinorVersion_Type.__name__ = "Integer32"
_OsosServicePackMinorVersion_Object = MibTableColumn
ososServicePackMinorVersion = _OsosServicePackMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 51),
    _OsosServicePackMinorVersion_Type()
)
ososServicePackMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososServicePackMinorVersion.setStatus("current")
_OsosSizeStoredInPagingFiles_Type = Gauge32
_OsosSizeStoredInPagingFiles_Object = MibTableColumn
ososSizeStoredInPagingFiles = _OsosSizeStoredInPagingFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 52),
    _OsosSizeStoredInPagingFiles_Type()
)
ososSizeStoredInPagingFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSizeStoredInPagingFiles.setStatus("current")


class _OsosStatus_Type(Integer32):
    """Custom type ososStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsosStatus_Type.__name__ = "Integer32"
_OsosStatus_Object = MibTableColumn
ososStatus = _OsosStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 53),
    _OsosStatus_Type()
)
ososStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososStatus.setStatus("current")
_OsosSuiteMask_Type = Gauge32
_OsosSuiteMask_Object = MibTableColumn
ososSuiteMask = _OsosSuiteMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 54),
    _OsosSuiteMask_Type()
)
ososSuiteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSuiteMask.setStatus("current")
_OsosSystemDevice_Type = WtcsDisplayString
_OsosSystemDevice_Object = MibTableColumn
ososSystemDevice = _OsosSystemDevice_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 55),
    _OsosSystemDevice_Type()
)
ososSystemDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSystemDevice.setStatus("current")
_OsosSystemDirectory_Type = WtcsDisplayString
_OsosSystemDirectory_Object = MibTableColumn
ososSystemDirectory = _OsosSystemDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 56),
    _OsosSystemDirectory_Type()
)
ososSystemDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSystemDirectory.setStatus("current")
_OsosSystemDrive_Type = WtcsDisplayString
_OsosSystemDrive_Object = MibTableColumn
ososSystemDrive = _OsosSystemDrive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 57),
    _OsosSystemDrive_Type()
)
ososSystemDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososSystemDrive.setStatus("current")
_OsosTotalSwapSpaceSize_Type = Gauge32
_OsosTotalSwapSpaceSize_Object = MibTableColumn
ososTotalSwapSpaceSize = _OsosTotalSwapSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 58),
    _OsosTotalSwapSpaceSize_Type()
)
ososTotalSwapSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososTotalSwapSpaceSize.setStatus("current")
_OsosTotalVirtualMemorySize_Type = Gauge32
_OsosTotalVirtualMemorySize_Object = MibTableColumn
ososTotalVirtualMemorySize = _OsosTotalVirtualMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 59),
    _OsosTotalVirtualMemorySize_Type()
)
ososTotalVirtualMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososTotalVirtualMemorySize.setStatus("current")
_OsosTotalVisibleMemorySize_Type = Gauge32
_OsosTotalVisibleMemorySize_Object = MibTableColumn
ososTotalVisibleMemorySize = _OsosTotalVisibleMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 60),
    _OsosTotalVisibleMemorySize_Type()
)
ososTotalVisibleMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososTotalVisibleMemorySize.setStatus("current")
_OsosVersion_Type = WtcsDisplayString
_OsosVersion_Object = MibTableColumn
ososVersion = _OsosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 61),
    _OsosVersion_Type()
)
ososVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososVersion.setStatus("current")
_OsosWindowsDirectory_Type = WtcsDisplayString
_OsosWindowsDirectory_Object = MibTableColumn
ososWindowsDirectory = _OsosWindowsDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 5, 1, 62),
    _OsosWindowsDirectory_Type()
)
ososWindowsDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ososWindowsDirectory.setStatus("current")
_Win32OSRecoveryConfigTable_Object = MibTable
win32OSRecoveryConfigTable = _Win32OSRecoveryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6)
)
if mibBuilder.loadTexts:
    win32OSRecoveryConfigTable.setStatus("current")
_Win32OSRecoveryConfigEntry_Object = MibTableRow
win32OSRecoveryConfigEntry = _Win32OSRecoveryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1)
)
win32OSRecoveryConfigEntry.setIndexNames(
    (0, "INFORMANT-OS", "osrcIndex"),
)
if mibBuilder.loadTexts:
    win32OSRecoveryConfigEntry.setStatus("current")


class _OsrcIndex_Type(Integer32):
    """Custom type osrcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsrcIndex_Type.__name__ = "Integer32"
_OsrcIndex_Object = MibTableColumn
osrcIndex = _OsrcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 1),
    _OsrcIndex_Type()
)
osrcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcIndex.setStatus("current")
_OsrcAutoReboot_Type = TruthValue
_OsrcAutoReboot_Object = MibTableColumn
osrcAutoReboot = _OsrcAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 2),
    _OsrcAutoReboot_Type()
)
osrcAutoReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcAutoReboot.setStatus("current")
_OsrcCaption_Type = WtcsDisplayString
_OsrcCaption_Object = MibTableColumn
osrcCaption = _OsrcCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 3),
    _OsrcCaption_Type()
)
osrcCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcCaption.setStatus("current")
_OsrcDebugFilePath_Type = WtcsDisplayString
_OsrcDebugFilePath_Object = MibTableColumn
osrcDebugFilePath = _OsrcDebugFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 4),
    _OsrcDebugFilePath_Type()
)
osrcDebugFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcDebugFilePath.setStatus("current")


class _OsrcDebugInfoType_Type(Integer32):
    """Custom type osrcDebugInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completeMemoryDump", 1),
          ("kernelMemoryDump", 2),
          ("none", 0),
          ("smallMemoryDump", 3))
    )


_OsrcDebugInfoType_Type.__name__ = "Integer32"
_OsrcDebugInfoType_Object = MibTableColumn
osrcDebugInfoType = _OsrcDebugInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 5),
    _OsrcDebugInfoType_Type()
)
osrcDebugInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcDebugInfoType.setStatus("current")
_OsrcDescription_Type = WtcsDisplayString
_OsrcDescription_Object = MibTableColumn
osrcDescription = _OsrcDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 6),
    _OsrcDescription_Type()
)
osrcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcDescription.setStatus("current")
_OsrcExpandedDebugFilePath_Type = WtcsDisplayString
_OsrcExpandedDebugFilePath_Object = MibTableColumn
osrcExpandedDebugFilePath = _OsrcExpandedDebugFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 7),
    _OsrcExpandedDebugFilePath_Type()
)
osrcExpandedDebugFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcExpandedDebugFilePath.setStatus("current")
_OsrcExpandedMiniDumpDirectory_Type = WtcsDisplayString
_OsrcExpandedMiniDumpDirectory_Object = MibTableColumn
osrcExpandedMiniDumpDirectory = _OsrcExpandedMiniDumpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 8),
    _OsrcExpandedMiniDumpDirectory_Type()
)
osrcExpandedMiniDumpDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcExpandedMiniDumpDirectory.setStatus("current")
_OsrcKernelDumpOnly_Type = TruthValue
_OsrcKernelDumpOnly_Object = MibTableColumn
osrcKernelDumpOnly = _OsrcKernelDumpOnly_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 9),
    _OsrcKernelDumpOnly_Type()
)
osrcKernelDumpOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcKernelDumpOnly.setStatus("current")
_OsrcMiniDumpDirectory_Type = WtcsDisplayString
_OsrcMiniDumpDirectory_Object = MibTableColumn
osrcMiniDumpDirectory = _OsrcMiniDumpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 10),
    _OsrcMiniDumpDirectory_Type()
)
osrcMiniDumpDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcMiniDumpDirectory.setStatus("current")


class _OsrcName_Type(WtcsDisplayString):
    """Custom type osrcName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsrcName_Type.__name__ = "WtcsDisplayString"
_OsrcName_Object = MibTableColumn
osrcName = _OsrcName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 11),
    _OsrcName_Type()
)
osrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcName.setStatus("current")
_OsrcOverwriteExistingDebugFile_Type = TruthValue
_OsrcOverwriteExistingDebugFile_Object = MibTableColumn
osrcOverwriteExistingDebugFile = _OsrcOverwriteExistingDebugFile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 12),
    _OsrcOverwriteExistingDebugFile_Type()
)
osrcOverwriteExistingDebugFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcOverwriteExistingDebugFile.setStatus("current")
_OsrcSendAdminAlert_Type = TruthValue
_OsrcSendAdminAlert_Object = MibTableColumn
osrcSendAdminAlert = _OsrcSendAdminAlert_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 13),
    _OsrcSendAdminAlert_Type()
)
osrcSendAdminAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcSendAdminAlert.setStatus("current")
_OsrcSettingID_Type = WtcsDisplayString
_OsrcSettingID_Object = MibTableColumn
osrcSettingID = _OsrcSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 14),
    _OsrcSettingID_Type()
)
osrcSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcSettingID.setStatus("current")
_OsrcWriteDebugInfo_Type = TruthValue
_OsrcWriteDebugInfo_Object = MibTableColumn
osrcWriteDebugInfo = _OsrcWriteDebugInfo_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 15),
    _OsrcWriteDebugInfo_Type()
)
osrcWriteDebugInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcWriteDebugInfo.setStatus("current")
_OsrcWriteToSystemLog_Type = TruthValue
_OsrcWriteToSystemLog_Object = MibTableColumn
osrcWriteToSystemLog = _OsrcWriteToSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 6, 1, 16),
    _OsrcWriteToSystemLog_Type()
)
osrcWriteToSystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osrcWriteToSystemLog.setStatus("current")
_Win32QuickFixEngineeringTable_Object = MibTable
win32QuickFixEngineeringTable = _Win32QuickFixEngineeringTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7)
)
if mibBuilder.loadTexts:
    win32QuickFixEngineeringTable.setStatus("current")
_Win32QuickFixEngineeringEntry_Object = MibTableRow
win32QuickFixEngineeringEntry = _Win32QuickFixEngineeringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1)
)
win32QuickFixEngineeringEntry.setIndexNames(
    (0, "INFORMANT-OS", "osqfeIndex"),
)
if mibBuilder.loadTexts:
    win32QuickFixEngineeringEntry.setStatus("current")


class _OsqfeIndex_Type(Integer32):
    """Custom type osqfeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsqfeIndex_Type.__name__ = "Integer32"
_OsqfeIndex_Object = MibTableColumn
osqfeIndex = _OsqfeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 1),
    _OsqfeIndex_Type()
)
osqfeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeIndex.setStatus("current")
_OsqfeCaption_Type = WtcsDisplayString
_OsqfeCaption_Object = MibTableColumn
osqfeCaption = _OsqfeCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 2),
    _OsqfeCaption_Type()
)
osqfeCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeCaption.setStatus("current")


class _OsqfeCSName_Type(WtcsDisplayString):
    """Custom type osqfeCSName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OsqfeCSName_Type.__name__ = "WtcsDisplayString"
_OsqfeCSName_Object = MibTableColumn
osqfeCSName = _OsqfeCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 3),
    _OsqfeCSName_Type()
)
osqfeCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeCSName.setStatus("current")
_OsqfeDescription_Type = WtcsDisplayString
_OsqfeDescription_Object = MibTableColumn
osqfeDescription = _OsqfeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 4),
    _OsqfeDescription_Type()
)
osqfeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeDescription.setStatus("current")
_OsqfeFixComments_Type = WtcsDisplayString
_OsqfeFixComments_Object = MibTableColumn
osqfeFixComments = _OsqfeFixComments_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 5),
    _OsqfeFixComments_Type()
)
osqfeFixComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeFixComments.setStatus("current")


class _OsqfeHotFixID_Type(WtcsDisplayString):
    """Custom type osqfeHotFixID based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 260),
    )


_OsqfeHotFixID_Type.__name__ = "WtcsDisplayString"
_OsqfeHotFixID_Object = MibTableColumn
osqfeHotFixID = _OsqfeHotFixID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 6),
    _OsqfeHotFixID_Type()
)
osqfeHotFixID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeHotFixID.setStatus("current")
_OsqfeInstallDate_Type = DateAndTime
_OsqfeInstallDate_Object = MibTableColumn
osqfeInstallDate = _OsqfeInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 7),
    _OsqfeInstallDate_Type()
)
osqfeInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeInstallDate.setStatus("current")
_OsqfeInstalledBy_Type = WtcsDisplayString
_OsqfeInstalledBy_Object = MibTableColumn
osqfeInstalledBy = _OsqfeInstalledBy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 8),
    _OsqfeInstalledBy_Type()
)
osqfeInstalledBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeInstalledBy.setStatus("current")
_OsqfeInstalledOn_Type = WtcsDisplayString
_OsqfeInstalledOn_Object = MibTableColumn
osqfeInstalledOn = _OsqfeInstalledOn_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 9),
    _OsqfeInstalledOn_Type()
)
osqfeInstalledOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeInstalledOn.setStatus("current")
_OsqfeName_Type = WtcsDisplayString
_OsqfeName_Object = MibTableColumn
osqfeName = _OsqfeName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 10),
    _OsqfeName_Type()
)
osqfeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeName.setStatus("current")


class _OsqfeServicePackInEffect_Type(WtcsDisplayString):
    """Custom type osqfeServicePackInEffect based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 260),
    )


_OsqfeServicePackInEffect_Type.__name__ = "WtcsDisplayString"
_OsqfeServicePackInEffect_Object = MibTableColumn
osqfeServicePackInEffect = _OsqfeServicePackInEffect_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 11),
    _OsqfeServicePackInEffect_Type()
)
osqfeServicePackInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeServicePackInEffect.setStatus("current")


class _OsqfeStatus_Type(Integer32):
    """Custom type osqfeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsqfeStatus_Type.__name__ = "Integer32"
_OsqfeStatus_Object = MibTableColumn
osqfeStatus = _OsqfeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 7, 1, 12),
    _OsqfeStatus_Type()
)
osqfeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osqfeStatus.setStatus("current")
_Win32StartupCommandTable_Object = MibTable
win32StartupCommandTable = _Win32StartupCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8)
)
if mibBuilder.loadTexts:
    win32StartupCommandTable.setStatus("current")
_Win32StartupCommandEntry_Object = MibTableRow
win32StartupCommandEntry = _Win32StartupCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1)
)
win32StartupCommandEntry.setIndexNames(
    (0, "INFORMANT-OS", "osscIndex"),
)
if mibBuilder.loadTexts:
    win32StartupCommandEntry.setStatus("current")


class _OsscIndex_Type(Integer32):
    """Custom type osscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsscIndex_Type.__name__ = "Integer32"
_OsscIndex_Object = MibTableColumn
osscIndex = _OsscIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 1),
    _OsscIndex_Type()
)
osscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscIndex.setStatus("current")
_OsscCaption_Type = WtcsDisplayString
_OsscCaption_Object = MibTableColumn
osscCaption = _OsscCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 2),
    _OsscCaption_Type()
)
osscCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscCaption.setStatus("current")
_OsscCommand_Type = WtcsDisplayString
_OsscCommand_Object = MibTableColumn
osscCommand = _OsscCommand_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 3),
    _OsscCommand_Type()
)
osscCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscCommand.setStatus("current")
_OsscDescription_Type = WtcsDisplayString
_OsscDescription_Object = MibTableColumn
osscDescription = _OsscDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 4),
    _OsscDescription_Type()
)
osscDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscDescription.setStatus("current")
_OsscLocation_Type = WtcsDisplayString
_OsscLocation_Object = MibTableColumn
osscLocation = _OsscLocation_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 5),
    _OsscLocation_Type()
)
osscLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscLocation.setStatus("current")
_OsscName_Type = WtcsDisplayString
_OsscName_Object = MibTableColumn
osscName = _OsscName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 6),
    _OsscName_Type()
)
osscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscName.setStatus("current")
_OsscSettingID_Type = WtcsDisplayString
_OsscSettingID_Object = MibTableColumn
osscSettingID = _OsscSettingID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 7),
    _OsscSettingID_Type()
)
osscSettingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscSettingID.setStatus("current")
_OsscUser_Type = WtcsDisplayString
_OsscUser_Object = MibTableColumn
osscUser = _OsscUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 8, 1, 8),
    _OsscUser_Type()
)
osscUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscUser.setStatus("current")


class _Win32Shutdown_Type(Integer32):
    """Custom type win32Shutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("forceShutdown", 5),
          ("forcedLogOff", 4),
          ("forcedPowerOff", 12),
          ("forcedReboot", 6),
          ("logOff", 0),
          ("powerOff", 8),
          ("reboot", 2),
          ("shutdown", 1))
    )


_Win32Shutdown_Type.__name__ = "Integer32"
_Win32Shutdown_Object = MibScalar
win32Shutdown = _Win32Shutdown_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 9),
    _Win32Shutdown_Type()
)
win32Shutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32Shutdown.setStatus("current")
_Win32WinSATTable_Object = MibTable
win32WinSATTable = _Win32WinSATTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10)
)
if mibBuilder.loadTexts:
    win32WinSATTable.setStatus("current")
_Win32WinSATEntry_Object = MibTableRow
win32WinSATEntry = _Win32WinSATEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1)
)
win32WinSATEntry.setIndexNames(
    (0, "INFORMANT-OS", "ossatIndex"),
)
if mibBuilder.loadTexts:
    win32WinSATEntry.setStatus("current")


class _OssatIndex_Type(Integer32):
    """Custom type ossatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OssatIndex_Type.__name__ = "Integer32"
_OssatIndex_Object = MibTableColumn
ossatIndex = _OssatIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 1),
    _OssatIndex_Type()
)
ossatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatIndex.setStatus("current")
_OssatCPUScore_Type = Integer32
_OssatCPUScore_Object = MibTableColumn
ossatCPUScore = _OssatCPUScore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 2),
    _OssatCPUScore_Type()
)
ossatCPUScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatCPUScore.setStatus("current")
_OssatD3DScore_Type = Integer32
_OssatD3DScore_Object = MibTableColumn
ossatD3DScore = _OssatD3DScore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 3),
    _OssatD3DScore_Type()
)
ossatD3DScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatD3DScore.setStatus("current")
_OssatDiskScore_Type = Integer32
_OssatDiskScore_Object = MibTableColumn
ossatDiskScore = _OssatDiskScore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 4),
    _OssatDiskScore_Type()
)
ossatDiskScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatDiskScore.setStatus("current")
_OssatGraphicsScore_Type = Integer32
_OssatGraphicsScore_Object = MibTableColumn
ossatGraphicsScore = _OssatGraphicsScore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 5),
    _OssatGraphicsScore_Type()
)
ossatGraphicsScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatGraphicsScore.setStatus("current")
_OssatMemoryScore_Type = Integer32
_OssatMemoryScore_Object = MibTableColumn
ossatMemoryScore = _OssatMemoryScore_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 6),
    _OssatMemoryScore_Type()
)
ossatMemoryScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatMemoryScore.setStatus("current")
_OssatTimeTaken_Type = WtcsDisplayString
_OssatTimeTaken_Object = MibTableColumn
ossatTimeTaken = _OssatTimeTaken_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 7),
    _OssatTimeTaken_Type()
)
ossatTimeTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatTimeTaken.setStatus("current")


class _OssatAssessmentState_Type(Integer32):
    """Custom type ossatAssessmentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("incoherentWithHardware", 2),
          ("invalid", 4),
          ("noAssessmentAvailable", 3),
          ("stateUknown", 0),
          ("valid", 1))
    )


_OssatAssessmentState_Type.__name__ = "Integer32"
_OssatAssessmentState_Object = MibTableColumn
ossatAssessmentState = _OssatAssessmentState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 8),
    _OssatAssessmentState_Type()
)
ossatAssessmentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatAssessmentState.setStatus("current")
_OssatSPRLevel_Type = Integer32
_OssatSPRLevel_Object = MibTableColumn
ossatSPRLevel = _OssatSPRLevel_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 8, 10, 1, 9),
    _OssatSPRLevel_Type()
)
ossatSPRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossatSPRLevel.setStatus("current")
_WmiProcesses_ObjectIdentity = ObjectIdentity
wmiProcesses = _WmiProcesses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9)
)
if mibBuilder.loadTexts:
    wmiProcesses.setStatus("current")
_Win32ProcessTable_Object = MibTable
win32ProcessTable = _Win32ProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1)
)
if mibBuilder.loadTexts:
    win32ProcessTable.setStatus("current")
_Win32ProcessEntry_Object = MibTableRow
win32ProcessEntry = _Win32ProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1)
)
win32ProcessEntry.setIndexNames(
    (0, "INFORMANT-OS", "ospsIndex"),
)
if mibBuilder.loadTexts:
    win32ProcessEntry.setStatus("current")


class _OspsIndex_Type(Integer32):
    """Custom type ospsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OspsIndex_Type.__name__ = "Integer32"
_OspsIndex_Object = MibTableColumn
ospsIndex = _OspsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 1),
    _OspsIndex_Type()
)
ospsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsIndex.setStatus("current")
_OspsCaption_Type = WtcsDisplayString
_OspsCaption_Object = MibTableColumn
ospsCaption = _OspsCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 2),
    _OspsCaption_Type()
)
ospsCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCaption.setStatus("current")
_OspsCommandLine_Type = WtcsDisplayString
_OspsCommandLine_Object = MibTableColumn
ospsCommandLine = _OspsCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 3),
    _OspsCommandLine_Type()
)
ospsCommandLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCommandLine.setStatus("current")


class _OspsCreationClassName_Type(WtcsDisplayString):
    """Custom type ospsCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspsCreationClassName_Type.__name__ = "WtcsDisplayString"
_OspsCreationClassName_Object = MibTableColumn
ospsCreationClassName = _OspsCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 4),
    _OspsCreationClassName_Type()
)
ospsCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCreationClassName.setStatus("current")
_OspsCreationDate_Type = DateAndTime
_OspsCreationDate_Object = MibTableColumn
ospsCreationDate = _OspsCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 5),
    _OspsCreationDate_Type()
)
ospsCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCreationDate.setStatus("current")
_OspsCSCreationClassName_Type = WtcsDisplayString
_OspsCSCreationClassName_Object = MibTableColumn
ospsCSCreationClassName = _OspsCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 6),
    _OspsCSCreationClassName_Type()
)
ospsCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCSCreationClassName.setStatus("current")
_OspsCSName_Type = WtcsDisplayString
_OspsCSName_Object = MibTableColumn
ospsCSName = _OspsCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 7),
    _OspsCSName_Type()
)
ospsCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsCSName.setStatus("current")
_OspsDescription_Type = WtcsDisplayString
_OspsDescription_Object = MibTableColumn
ospsDescription = _OspsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 8),
    _OspsDescription_Type()
)
ospsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsDescription.setStatus("current")
_OspsExecutablePath_Type = WtcsDisplayString
_OspsExecutablePath_Object = MibTableColumn
ospsExecutablePath = _OspsExecutablePath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 9),
    _OspsExecutablePath_Type()
)
ospsExecutablePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsExecutablePath.setStatus("current")


class _OspsExecutionState_Type(Integer32):
    """Custom type ospsExecutionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspsExecutionState_Type.__name__ = "Integer32"
_OspsExecutionState_Object = MibTableColumn
ospsExecutionState = _OspsExecutionState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 10),
    _OspsExecutionState_Type()
)
ospsExecutionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsExecutionState.setStatus("current")
_OspsHandle_Type = WtcsDisplayString
_OspsHandle_Object = MibTableColumn
ospsHandle = _OspsHandle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 11),
    _OspsHandle_Type()
)
ospsHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsHandle.setStatus("current")
_OspsHandleCount_Type = Gauge32
_OspsHandleCount_Object = MibTableColumn
ospsHandleCount = _OspsHandleCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 12),
    _OspsHandleCount_Type()
)
ospsHandleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsHandleCount.setStatus("current")
_OspsInstallDate_Type = DateAndTime
_OspsInstallDate_Object = MibTableColumn
ospsInstallDate = _OspsInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 13),
    _OspsInstallDate_Type()
)
ospsInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsInstallDate.setStatus("current")
_OspsKernelModeTime_Type = Counter64
_OspsKernelModeTime_Object = MibTableColumn
ospsKernelModeTime = _OspsKernelModeTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 14),
    _OspsKernelModeTime_Type()
)
ospsKernelModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsKernelModeTime.setStatus("current")
if mibBuilder.loadTexts:
    ospsKernelModeTime.setUnits("100ns")
_OspsMaximumWorkingSetSize_Type = Gauge32
_OspsMaximumWorkingSetSize_Object = MibTableColumn
ospsMaximumWorkingSetSize = _OspsMaximumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 15),
    _OspsMaximumWorkingSetSize_Type()
)
ospsMaximumWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsMaximumWorkingSetSize.setStatus("current")
if mibBuilder.loadTexts:
    ospsMaximumWorkingSetSize.setUnits("Kilobytes")
_OspsMinimumWorkingSetSize_Type = Gauge32
_OspsMinimumWorkingSetSize_Object = MibTableColumn
ospsMinimumWorkingSetSize = _OspsMinimumWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 16),
    _OspsMinimumWorkingSetSize_Type()
)
ospsMinimumWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsMinimumWorkingSetSize.setStatus("current")
if mibBuilder.loadTexts:
    ospsMinimumWorkingSetSize.setUnits("Kilobytes")
_OspsName_Type = WtcsDisplayString
_OspsName_Object = MibTableColumn
ospsName = _OspsName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 17),
    _OspsName_Type()
)
ospsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsName.setStatus("current")
_OspsOSCreationClassName_Type = WtcsDisplayString
_OspsOSCreationClassName_Object = MibTableColumn
ospsOSCreationClassName = _OspsOSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 18),
    _OspsOSCreationClassName_Type()
)
ospsOSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsOSCreationClassName.setStatus("current")
_OspsOSName_Type = WtcsDisplayString
_OspsOSName_Object = MibTableColumn
ospsOSName = _OspsOSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 19),
    _OspsOSName_Type()
)
ospsOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsOSName.setStatus("current")
_OspsOtherOperationCount_Type = Counter64
_OspsOtherOperationCount_Object = MibTableColumn
ospsOtherOperationCount = _OspsOtherOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 20),
    _OspsOtherOperationCount_Type()
)
ospsOtherOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsOtherOperationCount.setStatus("current")
_OspsOtherTransferCount_Type = Counter64
_OspsOtherTransferCount_Object = MibTableColumn
ospsOtherTransferCount = _OspsOtherTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 21),
    _OspsOtherTransferCount_Type()
)
ospsOtherTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsOtherTransferCount.setStatus("current")
if mibBuilder.loadTexts:
    ospsOtherTransferCount.setUnits("Bytes")
_OspsPageFaults_Type = Gauge32
_OspsPageFaults_Object = MibTableColumn
ospsPageFaults = _OspsPageFaults_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 22),
    _OspsPageFaults_Type()
)
ospsPageFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPageFaults.setStatus("current")
_OspsPageFileUsage_Type = Gauge32
_OspsPageFileUsage_Object = MibTableColumn
ospsPageFileUsage = _OspsPageFileUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 23),
    _OspsPageFileUsage_Type()
)
ospsPageFileUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPageFileUsage.setStatus("current")
if mibBuilder.loadTexts:
    ospsPageFileUsage.setUnits("Kilobytes")
_OspsParentProcessId_Type = Gauge32
_OspsParentProcessId_Object = MibTableColumn
ospsParentProcessId = _OspsParentProcessId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 24),
    _OspsParentProcessId_Type()
)
ospsParentProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsParentProcessId.setStatus("current")
_OspsPeakPageFileUsage_Type = Gauge32
_OspsPeakPageFileUsage_Object = MibTableColumn
ospsPeakPageFileUsage = _OspsPeakPageFileUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 25),
    _OspsPeakPageFileUsage_Type()
)
ospsPeakPageFileUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPeakPageFileUsage.setStatus("current")
if mibBuilder.loadTexts:
    ospsPeakPageFileUsage.setUnits("Kilobytes")
_OspsPeakVirtualSize_Type = Gauge32
_OspsPeakVirtualSize_Object = MibTableColumn
ospsPeakVirtualSize = _OspsPeakVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 26),
    _OspsPeakVirtualSize_Type()
)
ospsPeakVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPeakVirtualSize.setStatus("current")
if mibBuilder.loadTexts:
    ospsPeakVirtualSize.setUnits("Bytes")
_OspsPeakWorkingSetSize_Type = Gauge32
_OspsPeakWorkingSetSize_Object = MibTableColumn
ospsPeakWorkingSetSize = _OspsPeakWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 27),
    _OspsPeakWorkingSetSize_Type()
)
ospsPeakWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPeakWorkingSetSize.setStatus("current")
if mibBuilder.loadTexts:
    ospsPeakWorkingSetSize.setUnits("Kilobytes")
_OspsPriority_Type = Gauge32
_OspsPriority_Object = MibTableColumn
ospsPriority = _OspsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 28),
    _OspsPriority_Type()
)
ospsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPriority.setStatus("current")
_OspsPrivatePageCount_Type = Gauge32
_OspsPrivatePageCount_Object = MibTableColumn
ospsPrivatePageCount = _OspsPrivatePageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 29),
    _OspsPrivatePageCount_Type()
)
ospsPrivatePageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsPrivatePageCount.setStatus("current")
_OspsProcessId_Type = Gauge32
_OspsProcessId_Object = MibTableColumn
ospsProcessId = _OspsProcessId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 30),
    _OspsProcessId_Type()
)
ospsProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsProcessId.setStatus("current")
_OspsQuotaNonPagedPoolUsage_Type = Gauge32
_OspsQuotaNonPagedPoolUsage_Object = MibTableColumn
ospsQuotaNonPagedPoolUsage = _OspsQuotaNonPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 31),
    _OspsQuotaNonPagedPoolUsage_Type()
)
ospsQuotaNonPagedPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsQuotaNonPagedPoolUsage.setStatus("current")
_OspsQuotaPagedPoolUsage_Type = Gauge32
_OspsQuotaPagedPoolUsage_Object = MibTableColumn
ospsQuotaPagedPoolUsage = _OspsQuotaPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 32),
    _OspsQuotaPagedPoolUsage_Type()
)
ospsQuotaPagedPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsQuotaPagedPoolUsage.setStatus("current")
_OspsQuotaPeakNonPagedPoolUsage_Type = Gauge32
_OspsQuotaPeakNonPagedPoolUsage_Object = MibTableColumn
ospsQuotaPeakNonPagedPoolUsage = _OspsQuotaPeakNonPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 33),
    _OspsQuotaPeakNonPagedPoolUsage_Type()
)
ospsQuotaPeakNonPagedPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsQuotaPeakNonPagedPoolUsage.setStatus("current")
_OspsQuotaPeakPagedPoolUsage_Type = Gauge32
_OspsQuotaPeakPagedPoolUsage_Object = MibTableColumn
ospsQuotaPeakPagedPoolUsage = _OspsQuotaPeakPagedPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 34),
    _OspsQuotaPeakPagedPoolUsage_Type()
)
ospsQuotaPeakPagedPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsQuotaPeakPagedPoolUsage.setStatus("current")
_OspsReadOperationCount_Type = Counter64
_OspsReadOperationCount_Object = MibTableColumn
ospsReadOperationCount = _OspsReadOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 35),
    _OspsReadOperationCount_Type()
)
ospsReadOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsReadOperationCount.setStatus("current")
_OspsReadTransferCount_Type = Counter64
_OspsReadTransferCount_Object = MibTableColumn
ospsReadTransferCount = _OspsReadTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 36),
    _OspsReadTransferCount_Type()
)
ospsReadTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsReadTransferCount.setStatus("current")
if mibBuilder.loadTexts:
    ospsReadTransferCount.setUnits("Bytes")
_OspsSessionId_Type = Gauge32
_OspsSessionId_Object = MibTableColumn
ospsSessionId = _OspsSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 37),
    _OspsSessionId_Type()
)
ospsSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsSessionId.setStatus("current")
_OspsStatus_Type = WtcsDisplayString
_OspsStatus_Object = MibTableColumn
ospsStatus = _OspsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 38),
    _OspsStatus_Type()
)
ospsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsStatus.setStatus("current")
_OspsTerminationDate_Type = DateAndTime
_OspsTerminationDate_Object = MibTableColumn
ospsTerminationDate = _OspsTerminationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 39),
    _OspsTerminationDate_Type()
)
ospsTerminationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsTerminationDate.setStatus("current")
_OspsThreadCount_Type = Gauge32
_OspsThreadCount_Object = MibTableColumn
ospsThreadCount = _OspsThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 40),
    _OspsThreadCount_Type()
)
ospsThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsThreadCount.setStatus("current")
_OspsUserModeTime_Type = Counter64
_OspsUserModeTime_Object = MibTableColumn
ospsUserModeTime = _OspsUserModeTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 41),
    _OspsUserModeTime_Type()
)
ospsUserModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsUserModeTime.setStatus("current")
if mibBuilder.loadTexts:
    ospsUserModeTime.setUnits("100ns")
_OspsVirtualSize_Type = Gauge32
_OspsVirtualSize_Object = MibTableColumn
ospsVirtualSize = _OspsVirtualSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 42),
    _OspsVirtualSize_Type()
)
ospsVirtualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsVirtualSize.setStatus("current")
if mibBuilder.loadTexts:
    ospsVirtualSize.setUnits("Bytes")
_OspsWindowsVersion_Type = WtcsDisplayString
_OspsWindowsVersion_Object = MibTableColumn
ospsWindowsVersion = _OspsWindowsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 43),
    _OspsWindowsVersion_Type()
)
ospsWindowsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsWindowsVersion.setStatus("current")
_OspsWorkingSetSize_Type = Gauge32
_OspsWorkingSetSize_Object = MibTableColumn
ospsWorkingSetSize = _OspsWorkingSetSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 44),
    _OspsWorkingSetSize_Type()
)
ospsWorkingSetSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsWorkingSetSize.setStatus("current")
_OspsWriteOperationCount_Type = Counter64
_OspsWriteOperationCount_Object = MibTableColumn
ospsWriteOperationCount = _OspsWriteOperationCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 45),
    _OspsWriteOperationCount_Type()
)
ospsWriteOperationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsWriteOperationCount.setStatus("current")
_OspsWriteTransferCount_Type = Counter64
_OspsWriteTransferCount_Object = MibTableColumn
ospsWriteTransferCount = _OspsWriteTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 1, 1, 46),
    _OspsWriteTransferCount_Type()
)
ospsWriteTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospsWriteTransferCount.setStatus("current")
if mibBuilder.loadTexts:
    ospsWriteTransferCount.setUnits("Bytes")
_Win32ThreadTable_Object = MibTable
win32ThreadTable = _Win32ThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2)
)
if mibBuilder.loadTexts:
    win32ThreadTable.setStatus("current")
_Win32ThreadEntry_Object = MibTableRow
win32ThreadEntry = _Win32ThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1)
)
win32ThreadEntry.setIndexNames(
    (0, "INFORMANT-OS", "ostdIndex"),
)
if mibBuilder.loadTexts:
    win32ThreadEntry.setStatus("current")


class _OstdIndex_Type(Integer32):
    """Custom type ostdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OstdIndex_Type.__name__ = "Integer32"
_OstdIndex_Object = MibTableColumn
ostdIndex = _OstdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 1),
    _OstdIndex_Type()
)
ostdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdIndex.setStatus("current")


class _OstdCaption_Type(WtcsDisplayString):
    """Custom type ostdCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OstdCaption_Type.__name__ = "WtcsDisplayString"
_OstdCaption_Object = MibTableColumn
ostdCaption = _OstdCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 2),
    _OstdCaption_Type()
)
ostdCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdCaption.setStatus("current")


class _OstdCreationClassName_Type(WtcsDisplayString):
    """Custom type ostdCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdCreationClassName_Type.__name__ = "WtcsDisplayString"
_OstdCreationClassName_Object = MibTableColumn
ostdCreationClassName = _OstdCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 3),
    _OstdCreationClassName_Type()
)
ostdCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdCreationClassName.setStatus("current")


class _OstdCSCreationClassName_Type(WtcsDisplayString):
    """Custom type ostdCSCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdCSCreationClassName_Type.__name__ = "WtcsDisplayString"
_OstdCSCreationClassName_Object = MibTableColumn
ostdCSCreationClassName = _OstdCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 4),
    _OstdCSCreationClassName_Type()
)
ostdCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdCSCreationClassName.setStatus("current")


class _OstdCSName_Type(WtcsDisplayString):
    """Custom type ostdCSName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdCSName_Type.__name__ = "WtcsDisplayString"
_OstdCSName_Object = MibTableColumn
ostdCSName = _OstdCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 5),
    _OstdCSName_Type()
)
ostdCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdCSName.setStatus("current")
_OstdDescription_Type = WtcsDisplayString
_OstdDescription_Object = MibTableColumn
ostdDescription = _OstdDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 6),
    _OstdDescription_Type()
)
ostdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdDescription.setStatus("current")
_OstdElapsedTime_Type = Counter64
_OstdElapsedTime_Object = MibTableColumn
ostdElapsedTime = _OstdElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 7),
    _OstdElapsedTime_Type()
)
ostdElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    ostdElapsedTime.setUnits("Milliseconds")


class _OstdExecutionState_Type(Integer32):
    """Custom type ostdExecutionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 4),
          ("other", 1),
          ("ready", 2),
          ("running", 3),
          ("suspendedBlocked", 5),
          ("suspendedReady", 6),
          ("unknown", 0))
    )


_OstdExecutionState_Type.__name__ = "Integer32"
_OstdExecutionState_Object = MibTableColumn
ostdExecutionState = _OstdExecutionState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 8),
    _OstdExecutionState_Type()
)
ostdExecutionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdExecutionState.setStatus("current")


class _OstdHandle_Type(WtcsDisplayString):
    """Custom type ostdHandle based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdHandle_Type.__name__ = "WtcsDisplayString"
_OstdHandle_Object = MibTableColumn
ostdHandle = _OstdHandle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 9),
    _OstdHandle_Type()
)
ostdHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdHandle.setStatus("current")
_OstdInstallDate_Type = DateAndTime
_OstdInstallDate_Object = MibTableColumn
ostdInstallDate = _OstdInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 10),
    _OstdInstallDate_Type()
)
ostdInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdInstallDate.setStatus("current")
_OstdKernelModeTime_Type = Counter64
_OstdKernelModeTime_Object = MibTableColumn
ostdKernelModeTime = _OstdKernelModeTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 11),
    _OstdKernelModeTime_Type()
)
ostdKernelModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdKernelModeTime.setStatus("current")
if mibBuilder.loadTexts:
    ostdKernelModeTime.setUnits("100ns")
_OstdName_Type = WtcsDisplayString
_OstdName_Object = MibTableColumn
ostdName = _OstdName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 12),
    _OstdName_Type()
)
ostdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdName.setStatus("current")
_OstdOSCreationClassName_Type = WtcsDisplayString
_OstdOSCreationClassName_Object = MibTableColumn
ostdOSCreationClassName = _OstdOSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 13),
    _OstdOSCreationClassName_Type()
)
ostdOSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdOSCreationClassName.setStatus("current")


class _OstdOSName_Type(WtcsDisplayString):
    """Custom type ostdOSName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdOSName_Type.__name__ = "WtcsDisplayString"
_OstdOSName_Object = MibTableColumn
ostdOSName = _OstdOSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 14),
    _OstdOSName_Type()
)
ostdOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdOSName.setStatus("current")
_OstdPriority_Type = Gauge32
_OstdPriority_Object = MibTableColumn
ostdPriority = _OstdPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 15),
    _OstdPriority_Type()
)
ostdPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdPriority.setStatus("current")
_OstdPriorityBase_Type = Gauge32
_OstdPriorityBase_Object = MibTableColumn
ostdPriorityBase = _OstdPriorityBase_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 16),
    _OstdPriorityBase_Type()
)
ostdPriorityBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdPriorityBase.setStatus("current")


class _OstdProcessCreationClassName_Type(WtcsDisplayString):
    """Custom type ostdProcessCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdProcessCreationClassName_Type.__name__ = "WtcsDisplayString"
_OstdProcessCreationClassName_Object = MibTableColumn
ostdProcessCreationClassName = _OstdProcessCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 17),
    _OstdProcessCreationClassName_Type()
)
ostdProcessCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdProcessCreationClassName.setStatus("current")


class _OstdProcessHandle_Type(WtcsDisplayString):
    """Custom type ostdProcessHandle based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OstdProcessHandle_Type.__name__ = "WtcsDisplayString"
_OstdProcessHandle_Object = MibTableColumn
ostdProcessHandle = _OstdProcessHandle_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 18),
    _OstdProcessHandle_Type()
)
ostdProcessHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdProcessHandle.setStatus("current")
_OstdStartAddress_Type = Gauge32
_OstdStartAddress_Object = MibTableColumn
ostdStartAddress = _OstdStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 19),
    _OstdStartAddress_Type()
)
ostdStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdStartAddress.setStatus("current")


class _OstdStatus_Type(Integer32):
    """Custom type ostdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OstdStatus_Type.__name__ = "Integer32"
_OstdStatus_Object = MibTableColumn
ostdStatus = _OstdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 20),
    _OstdStatus_Type()
)
ostdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdStatus.setStatus("current")


class _OstdThreadState_Type(Integer32):
    """Custom type ostdThreadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("initialized", 0),
          ("ready", 1),
          ("running", 2),
          ("standby", 3),
          ("terminated", 4),
          ("transition", 6),
          ("unknown", 7),
          ("waiting", 5))
    )


_OstdThreadState_Type.__name__ = "Integer32"
_OstdThreadState_Object = MibTableColumn
ostdThreadState = _OstdThreadState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 21),
    _OstdThreadState_Type()
)
ostdThreadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdThreadState.setStatus("current")


class _OstdThreadWaitReason_Type(Integer32):
    """Custom type ostdThreadWaitReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("eventPairHigh", 14),
          ("eventPairLow", 15),
          ("executionDelay", 4),
          ("executionDelay2", 11),
          ("executive", 0),
          ("executive2", 7),
          ("freePage", 1),
          ("freePage2", 5),
          ("freePage3", 8),
          ("freePage4", 12),
          ("lpcreceive", 16),
          ("lpcreply", 17),
          ("pageIn", 2),
          ("pageIn2", 6),
          ("pageIn3", 9),
          ("pageIn4", 13),
          ("pageOut", 19),
          ("poolAllocation", 3),
          ("poolAllocation2", 10),
          ("unknown", 20),
          ("virtualMemory", 18))
    )


_OstdThreadWaitReason_Type.__name__ = "Integer32"
_OstdThreadWaitReason_Object = MibTableColumn
ostdThreadWaitReason = _OstdThreadWaitReason_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 22),
    _OstdThreadWaitReason_Type()
)
ostdThreadWaitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdThreadWaitReason.setStatus("current")
_OstdUserModeTime_Type = Counter64
_OstdUserModeTime_Object = MibTableColumn
ostdUserModeTime = _OstdUserModeTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 2, 1, 23),
    _OstdUserModeTime_Type()
)
ostdUserModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostdUserModeTime.setStatus("current")
if mibBuilder.loadTexts:
    ostdUserModeTime.setUnits("100ns")


class _Win32CreateProcess_Type(WtcsDisplayString):
    """Custom type win32CreateProcess based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Win32CreateProcess_Type.__name__ = "WtcsDisplayString"
_Win32CreateProcess_Object = MibScalar
win32CreateProcess = _Win32CreateProcess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 9, 3),
    _Win32CreateProcess_Type()
)
win32CreateProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    win32CreateProcess.setStatus("current")
_WmiSchedulerJobs_ObjectIdentity = ObjectIdentity
wmiSchedulerJobs = _WmiSchedulerJobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10)
)
if mibBuilder.loadTexts:
    wmiSchedulerJobs.setStatus("current")
_Win32CurrentTimeTable_Object = MibTable
win32CurrentTimeTable = _Win32CurrentTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1)
)
if mibBuilder.loadTexts:
    win32CurrentTimeTable.setStatus("current")
_Win32CurrentTimeEntry_Object = MibTableRow
win32CurrentTimeEntry = _Win32CurrentTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1)
)
win32CurrentTimeEntry.setIndexNames(
    (0, "INFORMANT-OS", "osctIndex"),
)
if mibBuilder.loadTexts:
    win32CurrentTimeEntry.setStatus("current")


class _OsctIndex_Type(Integer32):
    """Custom type osctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsctIndex_Type.__name__ = "Integer32"
_OsctIndex_Object = MibTableColumn
osctIndex = _OsctIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 1),
    _OsctIndex_Type()
)
osctIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctIndex.setStatus("current")
_OsctDay_Type = Gauge32
_OsctDay_Object = MibTableColumn
osctDay = _OsctDay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 2),
    _OsctDay_Type()
)
osctDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctDay.setStatus("current")
_OsctDayOfWeek_Type = Gauge32
_OsctDayOfWeek_Object = MibTableColumn
osctDayOfWeek = _OsctDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 3),
    _OsctDayOfWeek_Type()
)
osctDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctDayOfWeek.setStatus("current")
_OsctHour_Type = Gauge32
_OsctHour_Object = MibTableColumn
osctHour = _OsctHour_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 4),
    _OsctHour_Type()
)
osctHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctHour.setStatus("current")
_OsctMilliseconds_Type = Gauge32
_OsctMilliseconds_Object = MibTableColumn
osctMilliseconds = _OsctMilliseconds_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 5),
    _OsctMilliseconds_Type()
)
osctMilliseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctMilliseconds.setStatus("current")
_OsctMinute_Type = Gauge32
_OsctMinute_Object = MibTableColumn
osctMinute = _OsctMinute_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 6),
    _OsctMinute_Type()
)
osctMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctMinute.setStatus("current")
_OsctMonth_Type = Gauge32
_OsctMonth_Object = MibTableColumn
osctMonth = _OsctMonth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 7),
    _OsctMonth_Type()
)
osctMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctMonth.setStatus("current")
_OsctQuarter_Type = Gauge32
_OsctQuarter_Object = MibTableColumn
osctQuarter = _OsctQuarter_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 8),
    _OsctQuarter_Type()
)
osctQuarter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctQuarter.setStatus("current")
_OsctSecond_Type = Gauge32
_OsctSecond_Object = MibTableColumn
osctSecond = _OsctSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 9),
    _OsctSecond_Type()
)
osctSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctSecond.setStatus("current")
_OsctWeekInMonth_Type = Gauge32
_OsctWeekInMonth_Object = MibTableColumn
osctWeekInMonth = _OsctWeekInMonth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 10),
    _OsctWeekInMonth_Type()
)
osctWeekInMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctWeekInMonth.setStatus("current")
_OsctYear_Type = Gauge32
_OsctYear_Object = MibTableColumn
osctYear = _OsctYear_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 1, 1, 11),
    _OsctYear_Type()
)
osctYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctYear.setStatus("current")
_Win32ScheduledJobTable_Object = MibTable
win32ScheduledJobTable = _Win32ScheduledJobTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2)
)
if mibBuilder.loadTexts:
    win32ScheduledJobTable.setStatus("current")
_Win32ScheduledJobEntry_Object = MibTableRow
win32ScheduledJobEntry = _Win32ScheduledJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1)
)
win32ScheduledJobEntry.setIndexNames(
    (0, "INFORMANT-OS", "ossjIndex"),
)
if mibBuilder.loadTexts:
    win32ScheduledJobEntry.setStatus("current")


class _OssjIndex_Type(Integer32):
    """Custom type ossjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OssjIndex_Type.__name__ = "Integer32"
_OssjIndex_Object = MibTableColumn
ossjIndex = _OssjIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 1),
    _OssjIndex_Type()
)
ossjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjIndex.setStatus("current")
_OssjCaption_Type = WtcsDisplayString
_OssjCaption_Object = MibTableColumn
ossjCaption = _OssjCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 2),
    _OssjCaption_Type()
)
ossjCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjCaption.setStatus("current")
_OssjCommand_Type = WtcsDisplayString
_OssjCommand_Object = MibTableColumn
ossjCommand = _OssjCommand_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 3),
    _OssjCommand_Type()
)
ossjCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjCommand.setStatus("current")
_OssjDaysOfMonth_Type = Gauge32
_OssjDaysOfMonth_Object = MibTableColumn
ossjDaysOfMonth = _OssjDaysOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 4),
    _OssjDaysOfMonth_Type()
)
ossjDaysOfMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjDaysOfMonth.setStatus("current")
_OssjDaysOfWeek_Type = Gauge32
_OssjDaysOfWeek_Object = MibTableColumn
ossjDaysOfWeek = _OssjDaysOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 5),
    _OssjDaysOfWeek_Type()
)
ossjDaysOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjDaysOfWeek.setStatus("current")
_OssjDescription_Type = WtcsDisplayString
_OssjDescription_Object = MibTableColumn
ossjDescription = _OssjDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 6),
    _OssjDescription_Type()
)
ossjDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjDescription.setStatus("current")
_OssjElapsedTime_Type = DateAndTime
_OssjElapsedTime_Object = MibTableColumn
ossjElapsedTime = _OssjElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 7),
    _OssjElapsedTime_Type()
)
ossjElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjElapsedTime.setStatus("current")
_OssjInstallDate_Type = DateAndTime
_OssjInstallDate_Object = MibTableColumn
ossjInstallDate = _OssjInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 8),
    _OssjInstallDate_Type()
)
ossjInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjInstallDate.setStatus("current")
_OssjInteractWithDesktop_Type = TruthValue
_OssjInteractWithDesktop_Object = MibTableColumn
ossjInteractWithDesktop = _OssjInteractWithDesktop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 9),
    _OssjInteractWithDesktop_Type()
)
ossjInteractWithDesktop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjInteractWithDesktop.setStatus("current")
_OssjJobId_Type = Gauge32
_OssjJobId_Object = MibTableColumn
ossjJobId = _OssjJobId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 10),
    _OssjJobId_Type()
)
ossjJobId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjJobId.setStatus("current")


class _OssjJobStatus_Type(Integer32):
    """Custom type ossjJobStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_OssjJobStatus_Type.__name__ = "Integer32"
_OssjJobStatus_Object = MibTableColumn
ossjJobStatus = _OssjJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 11),
    _OssjJobStatus_Type()
)
ossjJobStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjJobStatus.setStatus("current")
_OssjName_Type = WtcsDisplayString
_OssjName_Object = MibTableColumn
ossjName = _OssjName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 12),
    _OssjName_Type()
)
ossjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjName.setStatus("current")
_OssjNotify_Type = WtcsDisplayString
_OssjNotify_Object = MibTableColumn
ossjNotify = _OssjNotify_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 13),
    _OssjNotify_Type()
)
ossjNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjNotify.setStatus("current")
_OssjOwner_Type = WtcsDisplayString
_OssjOwner_Object = MibTableColumn
ossjOwner = _OssjOwner_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 14),
    _OssjOwner_Type()
)
ossjOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjOwner.setStatus("current")
_OssjPriority_Type = Gauge32
_OssjPriority_Object = MibTableColumn
ossjPriority = _OssjPriority_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 15),
    _OssjPriority_Type()
)
ossjPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjPriority.setStatus("current")
_OssjRunRepeatedly_Type = TruthValue
_OssjRunRepeatedly_Object = MibTableColumn
ossjRunRepeatedly = _OssjRunRepeatedly_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 16),
    _OssjRunRepeatedly_Type()
)
ossjRunRepeatedly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjRunRepeatedly.setStatus("current")
_OssjStartTime_Type = DateAndTime
_OssjStartTime_Object = MibTableColumn
ossjStartTime = _OssjStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 17),
    _OssjStartTime_Type()
)
ossjStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjStartTime.setStatus("current")


class _OssjStatus_Type(Integer32):
    """Custom type ossjStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OssjStatus_Type.__name__ = "Integer32"
_OssjStatus_Object = MibTableColumn
ossjStatus = _OssjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 18),
    _OssjStatus_Type()
)
ossjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjStatus.setStatus("current")
_OssjTimeSubmitted_Type = DateAndTime
_OssjTimeSubmitted_Object = MibTableColumn
ossjTimeSubmitted = _OssjTimeSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 19),
    _OssjTimeSubmitted_Type()
)
ossjTimeSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjTimeSubmitted.setStatus("current")
_OssjUntilTime_Type = DateAndTime
_OssjUntilTime_Object = MibTableColumn
ossjUntilTime = _OssjUntilTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 10, 2, 1, 20),
    _OssjUntilTime_Type()
)
ossjUntilTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossjUntilTime.setStatus("current")
_WmiServices_ObjectIdentity = ObjectIdentity
wmiServices = _WmiServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11)
)
if mibBuilder.loadTexts:
    wmiServices.setStatus("current")
_Win32ServiceTable_Object = MibTable
win32ServiceTable = _Win32ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1)
)
if mibBuilder.loadTexts:
    win32ServiceTable.setStatus("current")
_Win32ServiceEntry_Object = MibTableRow
win32ServiceEntry = _Win32ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1)
)
win32ServiceEntry.setIndexNames(
    (0, "INFORMANT-OS", "ossvcIndex"),
)
if mibBuilder.loadTexts:
    win32ServiceEntry.setStatus("current")


class _OssvcIndex_Type(Integer32):
    """Custom type ossvcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OssvcIndex_Type.__name__ = "Integer32"
_OssvcIndex_Object = MibTableColumn
ossvcIndex = _OssvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 1),
    _OssvcIndex_Type()
)
ossvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcIndex.setStatus("current")
_OssvcAcceptPause_Type = TruthValue
_OssvcAcceptPause_Object = MibTableColumn
ossvcAcceptPause = _OssvcAcceptPause_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 2),
    _OssvcAcceptPause_Type()
)
ossvcAcceptPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcAcceptPause.setStatus("current")
_OssvcAcceptStop_Type = TruthValue
_OssvcAcceptStop_Object = MibTableColumn
ossvcAcceptStop = _OssvcAcceptStop_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 3),
    _OssvcAcceptStop_Type()
)
ossvcAcceptStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcAcceptStop.setStatus("current")
_OssvcCaption_Type = WtcsDisplayString
_OssvcCaption_Object = MibTableColumn
ossvcCaption = _OssvcCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 4),
    _OssvcCaption_Type()
)
ossvcCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcCaption.setStatus("current")
_OssvcCheckPoint_Type = Gauge32
_OssvcCheckPoint_Object = MibTableColumn
ossvcCheckPoint = _OssvcCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 5),
    _OssvcCheckPoint_Type()
)
ossvcCheckPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcCheckPoint.setStatus("current")


class _OssvcCreationClassName_Type(WtcsDisplayString):
    """Custom type ossvcCreationClassName based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OssvcCreationClassName_Type.__name__ = "WtcsDisplayString"
_OssvcCreationClassName_Object = MibTableColumn
ossvcCreationClassName = _OssvcCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 6),
    _OssvcCreationClassName_Type()
)
ossvcCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcCreationClassName.setStatus("current")
_OssvcDescription_Type = WtcsDisplayString
_OssvcDescription_Object = MibTableColumn
ossvcDescription = _OssvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 7),
    _OssvcDescription_Type()
)
ossvcDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcDescription.setStatus("current")
_OssvcDesktopInteract_Type = TruthValue
_OssvcDesktopInteract_Object = MibTableColumn
ossvcDesktopInteract = _OssvcDesktopInteract_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 8),
    _OssvcDesktopInteract_Type()
)
ossvcDesktopInteract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcDesktopInteract.setStatus("current")
_OssvcDisplayName_Type = WtcsDisplayString
_OssvcDisplayName_Object = MibTableColumn
ossvcDisplayName = _OssvcDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 9),
    _OssvcDisplayName_Type()
)
ossvcDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcDisplayName.setStatus("current")
_OssvcErrorControl_Type = WtcsDisplayString
_OssvcErrorControl_Object = MibTableColumn
ossvcErrorControl = _OssvcErrorControl_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 10),
    _OssvcErrorControl_Type()
)
ossvcErrorControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcErrorControl.setStatus("current")
_OssvcExitCode_Type = Gauge32
_OssvcExitCode_Object = MibTableColumn
ossvcExitCode = _OssvcExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 11),
    _OssvcExitCode_Type()
)
ossvcExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcExitCode.setStatus("current")
_OssvcInstallDate_Type = DateAndTime
_OssvcInstallDate_Object = MibTableColumn
ossvcInstallDate = _OssvcInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 12),
    _OssvcInstallDate_Type()
)
ossvcInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcInstallDate.setStatus("current")
_OssvcName_Type = WtcsDisplayString
_OssvcName_Object = MibTableColumn
ossvcName = _OssvcName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 13),
    _OssvcName_Type()
)
ossvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcName.setStatus("current")
_OssvcPathName_Type = WtcsDisplayString
_OssvcPathName_Object = MibTableColumn
ossvcPathName = _OssvcPathName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 14),
    _OssvcPathName_Type()
)
ossvcPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcPathName.setStatus("current")
_OssvcProcessId_Type = Gauge32
_OssvcProcessId_Object = MibTableColumn
ossvcProcessId = _OssvcProcessId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 15),
    _OssvcProcessId_Type()
)
ossvcProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcProcessId.setStatus("current")
_OssvcServiceSpecificExitCode_Type = Gauge32
_OssvcServiceSpecificExitCode_Object = MibTableColumn
ossvcServiceSpecificExitCode = _OssvcServiceSpecificExitCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 16),
    _OssvcServiceSpecificExitCode_Type()
)
ossvcServiceSpecificExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcServiceSpecificExitCode.setStatus("current")


class _OssvcServiceType_Type(Integer32):
    """Custom type ossvcServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("adapter", 3),
          ("fileSystemDriver", 2),
          ("interactiveProcess", 7),
          ("kernelDriver", 1),
          ("ownProcess", 5),
          ("recognizerDriver", 4),
          ("shareProcess", 6))
    )


_OssvcServiceType_Type.__name__ = "Integer32"
_OssvcServiceType_Object = MibTableColumn
ossvcServiceType = _OssvcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 17),
    _OssvcServiceType_Type()
)
ossvcServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcServiceType.setStatus("current")
_OssvcStarted_Type = TruthValue
_OssvcStarted_Object = MibTableColumn
ossvcStarted = _OssvcStarted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 18),
    _OssvcStarted_Type()
)
ossvcStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcStarted.setStatus("current")
_OssvcStartMode_Type = WtcsDisplayString
_OssvcStartMode_Object = MibTableColumn
ossvcStartMode = _OssvcStartMode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 19),
    _OssvcStartMode_Type()
)
ossvcStartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcStartMode.setStatus("current")
_OssvcStartName_Type = WtcsDisplayString
_OssvcStartName_Object = MibTableColumn
ossvcStartName = _OssvcStartName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 20),
    _OssvcStartName_Type()
)
ossvcStartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcStartName.setStatus("current")


class _OssvcState_Type(Integer32):
    """Custom type ossvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("continuePending", 5),
          ("pausePending", 6),
          ("paused", 7),
          ("running", 4),
          ("startPending", 2),
          ("stopPending", 3),
          ("stopped", 1),
          ("unknown", 8))
    )


_OssvcState_Type.__name__ = "Integer32"
_OssvcState_Object = MibTableColumn
ossvcState = _OssvcState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 21),
    _OssvcState_Type()
)
ossvcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossvcState.setStatus("current")


class _OssvcStatus_Type(Integer32):
    """Custom type ossvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OssvcStatus_Type.__name__ = "Integer32"
_OssvcStatus_Object = MibTableColumn
ossvcStatus = _OssvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 22),
    _OssvcStatus_Type()
)
ossvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcStatus.setStatus("current")
_OssvcSystemCreationClassName_Type = WtcsDisplayString
_OssvcSystemCreationClassName_Object = MibTableColumn
ossvcSystemCreationClassName = _OssvcSystemCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 23),
    _OssvcSystemCreationClassName_Type()
)
ossvcSystemCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcSystemCreationClassName.setStatus("current")
_OssvcSystemName_Type = WtcsDisplayString
_OssvcSystemName_Object = MibTableColumn
ossvcSystemName = _OssvcSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 24),
    _OssvcSystemName_Type()
)
ossvcSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcSystemName.setStatus("current")
_OssvcTagId_Type = Gauge32
_OssvcTagId_Object = MibTableColumn
ossvcTagId = _OssvcTagId_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 25),
    _OssvcTagId_Type()
)
ossvcTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcTagId.setStatus("current")
_OssvcWaitHint_Type = Gauge32
_OssvcWaitHint_Object = MibTableColumn
ossvcWaitHint = _OssvcWaitHint_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 11, 1, 1, 26),
    _OssvcWaitHint_Type()
)
ossvcWaitHint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossvcWaitHint.setStatus("current")
_WmiShares_ObjectIdentity = ObjectIdentity
wmiShares = _WmiShares_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12)
)
if mibBuilder.loadTexts:
    wmiShares.setStatus("current")
_Win32DFSNodeTable_Object = MibTable
win32DFSNodeTable = _Win32DFSNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1)
)
if mibBuilder.loadTexts:
    win32DFSNodeTable.setStatus("current")
_Win32DFSNodeEntry_Object = MibTableRow
win32DFSNodeEntry = _Win32DFSNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1)
)
win32DFSNodeEntry.setIndexNames(
    (0, "INFORMANT-OS", "osdfsnIndex"),
)
if mibBuilder.loadTexts:
    win32DFSNodeEntry.setStatus("current")


class _OsdfsnIndex_Type(Integer32):
    """Custom type osdfsnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsdfsnIndex_Type.__name__ = "Integer32"
_OsdfsnIndex_Object = MibTableColumn
osdfsnIndex = _OsdfsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 1),
    _OsdfsnIndex_Type()
)
osdfsnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnIndex.setStatus("current")


class _OsdfsnCaption_Type(WtcsDisplayString):
    """Custom type osdfsnCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsdfsnCaption_Type.__name__ = "WtcsDisplayString"
_OsdfsnCaption_Object = MibTableColumn
osdfsnCaption = _OsdfsnCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 2),
    _OsdfsnCaption_Type()
)
osdfsnCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnCaption.setStatus("current")
_OsdfsnDescription_Type = WtcsDisplayString
_OsdfsnDescription_Object = MibTableColumn
osdfsnDescription = _OsdfsnDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 3),
    _OsdfsnDescription_Type()
)
osdfsnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnDescription.setStatus("current")
_OsdfsnInstallDate_Type = DateAndTime
_OsdfsnInstallDate_Object = MibTableColumn
osdfsnInstallDate = _OsdfsnInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 4),
    _OsdfsnInstallDate_Type()
)
osdfsnInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnInstallDate.setStatus("current")
_OsdfsnName_Type = WtcsDisplayString
_OsdfsnName_Object = MibTableColumn
osdfsnName = _OsdfsnName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 5),
    _OsdfsnName_Type()
)
osdfsnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnName.setStatus("current")
_OsdfsnRoot_Type = TruthValue
_OsdfsnRoot_Object = MibTableColumn
osdfsnRoot = _OsdfsnRoot_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 6),
    _OsdfsnRoot_Type()
)
osdfsnRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnRoot.setStatus("current")


class _OsdfsnState_Type(Integer32):
    """Custom type osdfsnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inconsistent", 1),
          ("offline", 3),
          ("ok", 0),
          ("online", 2))
    )


_OsdfsnState_Type.__name__ = "Integer32"
_OsdfsnState_Object = MibTableColumn
osdfsnState = _OsdfsnState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 7),
    _OsdfsnState_Type()
)
osdfsnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnState.setStatus("current")


class _OsdfsnStatus_Type(Integer32):
    """Custom type osdfsnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsdfsnStatus_Type.__name__ = "Integer32"
_OsdfsnStatus_Object = MibTableColumn
osdfsnStatus = _OsdfsnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 8),
    _OsdfsnStatus_Type()
)
osdfsnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnStatus.setStatus("current")
_OsdfsnTimeout_Type = Gauge32
_OsdfsnTimeout_Object = MibTableColumn
osdfsnTimeout = _OsdfsnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 1, 1, 9),
    _OsdfsnTimeout_Type()
)
osdfsnTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfsnTimeout.setStatus("current")
if mibBuilder.loadTexts:
    osdfsnTimeout.setUnits("Seconds")
_Win32DFSTargetTable_Object = MibTable
win32DFSTargetTable = _Win32DFSTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2)
)
if mibBuilder.loadTexts:
    win32DFSTargetTable.setStatus("current")
_Win32DFSTargetEntry_Object = MibTableRow
win32DFSTargetEntry = _Win32DFSTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1)
)
win32DFSTargetEntry.setIndexNames(
    (0, "INFORMANT-OS", "osdfstIndex"),
)
if mibBuilder.loadTexts:
    win32DFSTargetEntry.setStatus("current")


class _OsdfstIndex_Type(Integer32):
    """Custom type osdfstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsdfstIndex_Type.__name__ = "Integer32"
_OsdfstIndex_Object = MibTableColumn
osdfstIndex = _OsdfstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 1),
    _OsdfstIndex_Type()
)
osdfstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstIndex.setStatus("current")


class _OsdfstCaption_Type(WtcsDisplayString):
    """Custom type osdfstCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsdfstCaption_Type.__name__ = "WtcsDisplayString"
_OsdfstCaption_Object = MibTableColumn
osdfstCaption = _OsdfstCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 2),
    _OsdfstCaption_Type()
)
osdfstCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstCaption.setStatus("current")
_OsdfstDescription_Type = WtcsDisplayString
_OsdfstDescription_Object = MibTableColumn
osdfstDescription = _OsdfstDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 3),
    _OsdfstDescription_Type()
)
osdfstDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstDescription.setStatus("current")
_OsdfstInstallDate_Type = DateAndTime
_OsdfstInstallDate_Object = MibTableColumn
osdfstInstallDate = _OsdfstInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 4),
    _OsdfstInstallDate_Type()
)
osdfstInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstInstallDate.setStatus("current")
_OsdfstLinkName_Type = WtcsDisplayString
_OsdfstLinkName_Object = MibTableColumn
osdfstLinkName = _OsdfstLinkName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 5),
    _OsdfstLinkName_Type()
)
osdfstLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstLinkName.setStatus("current")
_OsdfstName_Type = WtcsDisplayString
_OsdfstName_Object = MibTableColumn
osdfstName = _OsdfstName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 6),
    _OsdfstName_Type()
)
osdfstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstName.setStatus("current")
_OsdfstServerName_Type = WtcsDisplayString
_OsdfstServerName_Object = MibTableColumn
osdfstServerName = _OsdfstServerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 7),
    _OsdfstServerName_Type()
)
osdfstServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstServerName.setStatus("current")
_OsdfstShareName_Type = WtcsDisplayString
_OsdfstShareName_Object = MibTableColumn
osdfstShareName = _OsdfstShareName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 8),
    _OsdfstShareName_Type()
)
osdfstShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstShareName.setStatus("current")


class _OsdfstState_Type(Integer32):
    """Custom type osdfstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("offline", 0),
          ("online", 2))
    )


_OsdfstState_Type.__name__ = "Integer32"
_OsdfstState_Object = MibTableColumn
osdfstState = _OsdfstState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 9),
    _OsdfstState_Type()
)
osdfstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstState.setStatus("current")


class _OsdfstStatus_Type(Integer32):
    """Custom type osdfstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 4))
    )


_OsdfstStatus_Type.__name__ = "Integer32"
_OsdfstStatus_Object = MibTableColumn
osdfstStatus = _OsdfstStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 2, 1, 10),
    _OsdfstStatus_Type()
)
osdfstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osdfstStatus.setStatus("current")
_Win32ServerConnectionTable_Object = MibTable
win32ServerConnectionTable = _Win32ServerConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3)
)
if mibBuilder.loadTexts:
    win32ServerConnectionTable.setStatus("current")
_Win32ServerConnectionEntry_Object = MibTableRow
win32ServerConnectionEntry = _Win32ServerConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1)
)
win32ServerConnectionEntry.setIndexNames(
    (0, "INFORMANT-OS", "osscnIndex"),
)
if mibBuilder.loadTexts:
    win32ServerConnectionEntry.setStatus("current")


class _OsscnIndex_Type(Integer32):
    """Custom type osscnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsscnIndex_Type.__name__ = "Integer32"
_OsscnIndex_Object = MibTableColumn
osscnIndex = _OsscnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 1),
    _OsscnIndex_Type()
)
osscnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnIndex.setStatus("current")
_OsscnActiveTime_Type = Gauge32
_OsscnActiveTime_Object = MibTableColumn
osscnActiveTime = _OsscnActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 2),
    _OsscnActiveTime_Type()
)
osscnActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    osscnActiveTime.setUnits("Seconds")


class _OsscnCaption_Type(WtcsDisplayString):
    """Custom type osscnCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsscnCaption_Type.__name__ = "WtcsDisplayString"
_OsscnCaption_Object = MibTableColumn
osscnCaption = _OsscnCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 3),
    _OsscnCaption_Type()
)
osscnCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnCaption.setStatus("current")
_OsscnComputerName_Type = WtcsDisplayString
_OsscnComputerName_Object = MibTableColumn
osscnComputerName = _OsscnComputerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 4),
    _OsscnComputerName_Type()
)
osscnComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnComputerName.setStatus("current")
_OsscnConnectionID_Type = Gauge32
_OsscnConnectionID_Object = MibTableColumn
osscnConnectionID = _OsscnConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 5),
    _OsscnConnectionID_Type()
)
osscnConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnConnectionID.setStatus("current")
_OsscnDescription_Type = WtcsDisplayString
_OsscnDescription_Object = MibTableColumn
osscnDescription = _OsscnDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 6),
    _OsscnDescription_Type()
)
osscnDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnDescription.setStatus("current")
_OsscnInstallDate_Type = DateAndTime
_OsscnInstallDate_Object = MibTableColumn
osscnInstallDate = _OsscnInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 7),
    _OsscnInstallDate_Type()
)
osscnInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnInstallDate.setStatus("current")
_OsscnName_Type = WtcsDisplayString
_OsscnName_Object = MibTableColumn
osscnName = _OsscnName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 8),
    _OsscnName_Type()
)
osscnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnName.setStatus("current")
_OsscnNumberOfFiles_Type = Gauge32
_OsscnNumberOfFiles_Object = MibTableColumn
osscnNumberOfFiles = _OsscnNumberOfFiles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 9),
    _OsscnNumberOfFiles_Type()
)
osscnNumberOfFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnNumberOfFiles.setStatus("current")
_OsscnNumberOfUsers_Type = Gauge32
_OsscnNumberOfUsers_Object = MibTableColumn
osscnNumberOfUsers = _OsscnNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 10),
    _OsscnNumberOfUsers_Type()
)
osscnNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnNumberOfUsers.setStatus("current")
_OsscnShareName_Type = WtcsDisplayString
_OsscnShareName_Object = MibTableColumn
osscnShareName = _OsscnShareName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 11),
    _OsscnShareName_Type()
)
osscnShareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnShareName.setStatus("current")


class _OsscnStatus_Type(Integer32):
    """Custom type osscnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsscnStatus_Type.__name__ = "Integer32"
_OsscnStatus_Object = MibTableColumn
osscnStatus = _OsscnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 12),
    _OsscnStatus_Type()
)
osscnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnStatus.setStatus("current")
_OsscnUserName_Type = WtcsDisplayString
_OsscnUserName_Object = MibTableColumn
osscnUserName = _OsscnUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 3, 1, 13),
    _OsscnUserName_Type()
)
osscnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscnUserName.setStatus("current")
_Win32ServerSessionTable_Object = MibTable
win32ServerSessionTable = _Win32ServerSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4)
)
if mibBuilder.loadTexts:
    win32ServerSessionTable.setStatus("current")
_Win32ServerSessionEntry_Object = MibTableRow
win32ServerSessionEntry = _Win32ServerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1)
)
win32ServerSessionEntry.setIndexNames(
    (0, "INFORMANT-OS", "osssIndex"),
)
if mibBuilder.loadTexts:
    win32ServerSessionEntry.setStatus("current")


class _OsssIndex_Type(Integer32):
    """Custom type osssIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsssIndex_Type.__name__ = "Integer32"
_OsssIndex_Object = MibTableColumn
osssIndex = _OsssIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 1),
    _OsssIndex_Type()
)
osssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssIndex.setStatus("current")
_OsssActiveTime_Type = Gauge32
_OsssActiveTime_Object = MibTableColumn
osssActiveTime = _OsssActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 2),
    _OsssActiveTime_Type()
)
osssActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssActiveTime.setStatus("current")
if mibBuilder.loadTexts:
    osssActiveTime.setUnits("Seconds")


class _OsssCaption_Type(WtcsDisplayString):
    """Custom type osssCaption based on WtcsDisplayString"""
    subtypeSpec = WtcsDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OsssCaption_Type.__name__ = "WtcsDisplayString"
_OsssCaption_Object = MibTableColumn
osssCaption = _OsssCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 3),
    _OsssCaption_Type()
)
osssCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssCaption.setStatus("current")
_OsssClientType_Type = WtcsDisplayString
_OsssClientType_Object = MibTableColumn
osssClientType = _OsssClientType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 4),
    _OsssClientType_Type()
)
osssClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssClientType.setStatus("current")
_OsssComputerName_Type = WtcsDisplayString
_OsssComputerName_Object = MibTableColumn
osssComputerName = _OsssComputerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 5),
    _OsssComputerName_Type()
)
osssComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssComputerName.setStatus("current")
_OsssDescription_Type = WtcsDisplayString
_OsssDescription_Object = MibTableColumn
osssDescription = _OsssDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 6),
    _OsssDescription_Type()
)
osssDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssDescription.setStatus("current")
_OsssIdleTime_Type = Gauge32
_OsssIdleTime_Object = MibTableColumn
osssIdleTime = _OsssIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 7),
    _OsssIdleTime_Type()
)
osssIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    osssIdleTime.setUnits("Seconds")
_OsssInstallDate_Type = DateAndTime
_OsssInstallDate_Object = MibTableColumn
osssInstallDate = _OsssInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 8),
    _OsssInstallDate_Type()
)
osssInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssInstallDate.setStatus("current")
_OsssName_Type = WtcsDisplayString
_OsssName_Object = MibTableColumn
osssName = _OsssName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 9),
    _OsssName_Type()
)
osssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssName.setStatus("current")
_OsssResourcesOpened_Type = Gauge32
_OsssResourcesOpened_Object = MibTableColumn
osssResourcesOpened = _OsssResourcesOpened_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 10),
    _OsssResourcesOpened_Type()
)
osssResourcesOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssResourcesOpened.setStatus("current")


class _OsssSessionType_Type(Integer32):
    """Custom type osssSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guest", 0),
          ("noEncryption", 1),
          ("other", 2))
    )


_OsssSessionType_Type.__name__ = "Integer32"
_OsssSessionType_Object = MibTableColumn
osssSessionType = _OsssSessionType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 11),
    _OsssSessionType_Type()
)
osssSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssSessionType.setStatus("current")


class _OsssStatus_Type(Integer32):
    """Custom type osssStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsssStatus_Type.__name__ = "Integer32"
_OsssStatus_Object = MibTableColumn
osssStatus = _OsssStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 12),
    _OsssStatus_Type()
)
osssStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssStatus.setStatus("current")
_OsssTransportName_Type = WtcsDisplayString
_OsssTransportName_Object = MibTableColumn
osssTransportName = _OsssTransportName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 13),
    _OsssTransportName_Type()
)
osssTransportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssTransportName.setStatus("current")
_OsssUserName_Type = WtcsDisplayString
_OsssUserName_Object = MibTableColumn
osssUserName = _OsssUserName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 4, 1, 14),
    _OsssUserName_Type()
)
osssUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osssUserName.setStatus("current")
_Win32ShareTable_Object = MibTable
win32ShareTable = _Win32ShareTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5)
)
if mibBuilder.loadTexts:
    win32ShareTable.setStatus("current")
_Win32ShareEntry_Object = MibTableRow
win32ShareEntry = _Win32ShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1)
)
win32ShareEntry.setIndexNames(
    (0, "INFORMANT-OS", "osshIndex"),
)
if mibBuilder.loadTexts:
    win32ShareEntry.setStatus("current")


class _OsshIndex_Type(Integer32):
    """Custom type osshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsshIndex_Type.__name__ = "Integer32"
_OsshIndex_Object = MibTableColumn
osshIndex = _OsshIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 1),
    _OsshIndex_Type()
)
osshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshIndex.setStatus("current")
_OsshAccessMask_Type = Gauge32
_OsshAccessMask_Object = MibTableColumn
osshAccessMask = _OsshAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 2),
    _OsshAccessMask_Type()
)
osshAccessMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshAccessMask.setStatus("current")
_OsshAllowMaximum_Type = TruthValue
_OsshAllowMaximum_Object = MibTableColumn
osshAllowMaximum = _OsshAllowMaximum_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 3),
    _OsshAllowMaximum_Type()
)
osshAllowMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshAllowMaximum.setStatus("current")
_OsshCaption_Type = WtcsDisplayString
_OsshCaption_Object = MibTableColumn
osshCaption = _OsshCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 4),
    _OsshCaption_Type()
)
osshCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshCaption.setStatus("current")
_OsshDescription_Type = WtcsDisplayString
_OsshDescription_Object = MibTableColumn
osshDescription = _OsshDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 5),
    _OsshDescription_Type()
)
osshDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshDescription.setStatus("current")
_OsshInstallDate_Type = DateAndTime
_OsshInstallDate_Object = MibTableColumn
osshInstallDate = _OsshInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 6),
    _OsshInstallDate_Type()
)
osshInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshInstallDate.setStatus("current")
_OsshMaximumAllowed_Type = Gauge32
_OsshMaximumAllowed_Object = MibTableColumn
osshMaximumAllowed = _OsshMaximumAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 7),
    _OsshMaximumAllowed_Type()
)
osshMaximumAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshMaximumAllowed.setStatus("current")
_OsshName_Type = WtcsDisplayString
_OsshName_Object = MibTableColumn
osshName = _OsshName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 8),
    _OsshName_Type()
)
osshName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshName.setStatus("current")
_OsshPath_Type = WtcsDisplayString
_OsshPath_Object = MibTableColumn
osshPath = _OsshPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 9),
    _OsshPath_Type()
)
osshPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshPath.setStatus("current")


class _OsshStatus_Type(Integer32):
    """Custom type osshStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OsshStatus_Type.__name__ = "Integer32"
_OsshStatus_Object = MibTableColumn
osshStatus = _OsshStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 10),
    _OsshStatus_Type()
)
osshStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshStatus.setStatus("current")
_OsshType_Type = Gauge32
_OsshType_Object = MibTableColumn
osshType = _OsshType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 12, 5, 1, 11),
    _OsshType_Type()
)
osshType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osshType.setStatus("current")
_WmiStorage_ObjectIdentity = ObjectIdentity
wmiStorage = _WmiStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13)
)
if mibBuilder.loadTexts:
    wmiStorage.setStatus("current")
_Win32ShadowContextTable_Object = MibTable
win32ShadowContextTable = _Win32ShadowContextTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1)
)
if mibBuilder.loadTexts:
    win32ShadowContextTable.setStatus("current")
_Win32ShadowContextEntry_Object = MibTableRow
win32ShadowContextEntry = _Win32ShadowContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1)
)
win32ShadowContextEntry.setIndexNames(
    (0, "INFORMANT-OS", "osscxIndex"),
)
if mibBuilder.loadTexts:
    win32ShadowContextEntry.setStatus("current")


class _OsscxIndex_Type(Integer32):
    """Custom type osscxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsscxIndex_Type.__name__ = "Integer32"
_OsscxIndex_Object = MibTableColumn
osscxIndex = _OsscxIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 1),
    _OsscxIndex_Type()
)
osscxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxIndex.setStatus("current")
_OsscxClientAccessible_Type = TruthValue
_OsscxClientAccessible_Object = MibTableColumn
osscxClientAccessible = _OsscxClientAccessible_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 2),
    _OsscxClientAccessible_Type()
)
osscxClientAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxClientAccessible.setStatus("current")
_OsscxDifferential_Type = TruthValue
_OsscxDifferential_Object = MibTableColumn
osscxDifferential = _OsscxDifferential_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 3),
    _OsscxDifferential_Type()
)
osscxDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxDifferential.setStatus("current")
_OsscxExposedLocally_Type = TruthValue
_OsscxExposedLocally_Object = MibTableColumn
osscxExposedLocally = _OsscxExposedLocally_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 4),
    _OsscxExposedLocally_Type()
)
osscxExposedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxExposedLocally.setStatus("current")
_OsscxExposedRemotely_Type = TruthValue
_OsscxExposedRemotely_Object = MibTableColumn
osscxExposedRemotely = _OsscxExposedRemotely_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 5),
    _OsscxExposedRemotely_Type()
)
osscxExposedRemotely.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxExposedRemotely.setStatus("current")
_OsscxHardwareAssisted_Type = TruthValue
_OsscxHardwareAssisted_Object = MibTableColumn
osscxHardwareAssisted = _OsscxHardwareAssisted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 6),
    _OsscxHardwareAssisted_Type()
)
osscxHardwareAssisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxHardwareAssisted.setStatus("current")
_OsscxImported_Type = TruthValue
_OsscxImported_Object = MibTableColumn
osscxImported = _OsscxImported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 7),
    _OsscxImported_Type()
)
osscxImported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxImported.setStatus("current")
_OsscxName_Type = WtcsDisplayString
_OsscxName_Object = MibTableColumn
osscxName = _OsscxName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 8),
    _OsscxName_Type()
)
osscxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxName.setStatus("current")
_OsscxNoAutoRelease_Type = TruthValue
_OsscxNoAutoRelease_Object = MibTableColumn
osscxNoAutoRelease = _OsscxNoAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 9),
    _OsscxNoAutoRelease_Type()
)
osscxNoAutoRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxNoAutoRelease.setStatus("current")
_OsscxNotSurfaced_Type = TruthValue
_OsscxNotSurfaced_Object = MibTableColumn
osscxNotSurfaced = _OsscxNotSurfaced_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 10),
    _OsscxNotSurfaced_Type()
)
osscxNotSurfaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxNotSurfaced.setStatus("current")
_OsscxNoWriters_Type = TruthValue
_OsscxNoWriters_Object = MibTableColumn
osscxNoWriters = _OsscxNoWriters_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 11),
    _OsscxNoWriters_Type()
)
osscxNoWriters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxNoWriters.setStatus("current")
_OsscxPersistent_Type = TruthValue
_OsscxPersistent_Object = MibTableColumn
osscxPersistent = _OsscxPersistent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 12),
    _OsscxPersistent_Type()
)
osscxPersistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxPersistent.setStatus("current")
_OsscxPlex_Type = TruthValue
_OsscxPlex_Object = MibTableColumn
osscxPlex = _OsscxPlex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 13),
    _OsscxPlex_Type()
)
osscxPlex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxPlex.setStatus("current")
_OsscxTransportable_Type = TruthValue
_OsscxTransportable_Object = MibTableColumn
osscxTransportable = _OsscxTransportable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 1, 1, 14),
    _OsscxTransportable_Type()
)
osscxTransportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscxTransportable.setStatus("current")
_Win32ShadowCopyTable_Object = MibTable
win32ShadowCopyTable = _Win32ShadowCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2)
)
if mibBuilder.loadTexts:
    win32ShadowCopyTable.setStatus("current")
_Win32ShadowCopyEntry_Object = MibTableRow
win32ShadowCopyEntry = _Win32ShadowCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1)
)
win32ShadowCopyEntry.setIndexNames(
    (0, "INFORMANT-OS", "osscpIndex"),
)
if mibBuilder.loadTexts:
    win32ShadowCopyEntry.setStatus("current")


class _OsscpIndex_Type(Integer32):
    """Custom type osscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsscpIndex_Type.__name__ = "Integer32"
_OsscpIndex_Object = MibTableColumn
osscpIndex = _OsscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 1),
    _OsscpIndex_Type()
)
osscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpIndex.setStatus("current")
_OsscpClientAccessible_Type = TruthValue
_OsscpClientAccessible_Object = MibTableColumn
osscpClientAccessible = _OsscpClientAccessible_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 2),
    _OsscpClientAccessible_Type()
)
osscpClientAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpClientAccessible.setStatus("current")
_OsscpCount_Type = Gauge32
_OsscpCount_Object = MibTableColumn
osscpCount = _OsscpCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 3),
    _OsscpCount_Type()
)
osscpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpCount.setStatus("current")
_OsscpDeviceObject_Type = WtcsDisplayString
_OsscpDeviceObject_Object = MibTableColumn
osscpDeviceObject = _OsscpDeviceObject_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 4),
    _OsscpDeviceObject_Type()
)
osscpDeviceObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpDeviceObject.setStatus("current")
_OsscpDifferential_Type = TruthValue
_OsscpDifferential_Object = MibTableColumn
osscpDifferential = _OsscpDifferential_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 5),
    _OsscpDifferential_Type()
)
osscpDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpDifferential.setStatus("current")
_OsscpExposedLocally_Type = TruthValue
_OsscpExposedLocally_Object = MibTableColumn
osscpExposedLocally = _OsscpExposedLocally_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 6),
    _OsscpExposedLocally_Type()
)
osscpExposedLocally.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpExposedLocally.setStatus("current")
_OsscpExposedName_Type = WtcsDisplayString
_OsscpExposedName_Object = MibTableColumn
osscpExposedName = _OsscpExposedName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 7),
    _OsscpExposedName_Type()
)
osscpExposedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpExposedName.setStatus("current")
_OsscpExposedRemotely_Type = TruthValue
_OsscpExposedRemotely_Object = MibTableColumn
osscpExposedRemotely = _OsscpExposedRemotely_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 8),
    _OsscpExposedRemotely_Type()
)
osscpExposedRemotely.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpExposedRemotely.setStatus("current")
_OsscpHardwareAssisted_Type = TruthValue
_OsscpHardwareAssisted_Object = MibTableColumn
osscpHardwareAssisted = _OsscpHardwareAssisted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 9),
    _OsscpHardwareAssisted_Type()
)
osscpHardwareAssisted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpHardwareAssisted.setStatus("current")
_OsscpID_Type = WtcsDisplayString
_OsscpID_Object = MibTableColumn
osscpID = _OsscpID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 10),
    _OsscpID_Type()
)
osscpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpID.setStatus("current")
_OsscpImported_Type = TruthValue
_OsscpImported_Object = MibTableColumn
osscpImported = _OsscpImported_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 11),
    _OsscpImported_Type()
)
osscpImported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpImported.setStatus("current")
_OsscpNoAutoRelease_Type = TruthValue
_OsscpNoAutoRelease_Object = MibTableColumn
osscpNoAutoRelease = _OsscpNoAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 12),
    _OsscpNoAutoRelease_Type()
)
osscpNoAutoRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpNoAutoRelease.setStatus("current")
_OsscpNotSurfaced_Type = TruthValue
_OsscpNotSurfaced_Object = MibTableColumn
osscpNotSurfaced = _OsscpNotSurfaced_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 13),
    _OsscpNotSurfaced_Type()
)
osscpNotSurfaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpNotSurfaced.setStatus("current")
_OsscpNoWriters_Type = TruthValue
_OsscpNoWriters_Object = MibTableColumn
osscpNoWriters = _OsscpNoWriters_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 14),
    _OsscpNoWriters_Type()
)
osscpNoWriters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpNoWriters.setStatus("current")
_OsscpOriginatingMachine_Type = WtcsDisplayString
_OsscpOriginatingMachine_Object = MibTableColumn
osscpOriginatingMachine = _OsscpOriginatingMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 15),
    _OsscpOriginatingMachine_Type()
)
osscpOriginatingMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpOriginatingMachine.setStatus("current")
_OsscpPersistent_Type = TruthValue
_OsscpPersistent_Object = MibTableColumn
osscpPersistent = _OsscpPersistent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 16),
    _OsscpPersistent_Type()
)
osscpPersistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpPersistent.setStatus("current")
_OsscpPlex_Type = TruthValue
_OsscpPlex_Object = MibTableColumn
osscpPlex = _OsscpPlex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 17),
    _OsscpPlex_Type()
)
osscpPlex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpPlex.setStatus("current")
_OsscpProviderID_Type = WtcsDisplayString
_OsscpProviderID_Object = MibTableColumn
osscpProviderID = _OsscpProviderID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 18),
    _OsscpProviderID_Type()
)
osscpProviderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpProviderID.setStatus("current")
_OsscpServiceMachine_Type = WtcsDisplayString
_OsscpServiceMachine_Object = MibTableColumn
osscpServiceMachine = _OsscpServiceMachine_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 19),
    _OsscpServiceMachine_Type()
)
osscpServiceMachine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpServiceMachine.setStatus("current")
_OsscpSetID_Type = WtcsDisplayString
_OsscpSetID_Object = MibTableColumn
osscpSetID = _OsscpSetID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 20),
    _OsscpSetID_Type()
)
osscpSetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpSetID.setStatus("current")


class _OsscpState_Type(Integer32):
    """Custom type osscpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 10),
          ("committed", 7),
          ("count", 12),
          ("created", 9),
          ("deleted", 11),
          ("precommitted", 5),
          ("prepared", 3),
          ("preparing", 1),
          ("processingCommit", 6),
          ("processingPostcommit", 8),
          ("processingPrecommit", 4),
          ("processingPrepare", 2),
          ("unknown", 0))
    )


_OsscpState_Type.__name__ = "Integer32"
_OsscpState_Object = MibTableColumn
osscpState = _OsscpState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 21),
    _OsscpState_Type()
)
osscpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpState.setStatus("current")
_OsscpTransportable_Type = TruthValue
_OsscpTransportable_Object = MibTableColumn
osscpTransportable = _OsscpTransportable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 22),
    _OsscpTransportable_Type()
)
osscpTransportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpTransportable.setStatus("current")
_OsscpVolumeName_Type = WtcsDisplayString
_OsscpVolumeName_Object = MibTableColumn
osscpVolumeName = _OsscpVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 2, 1, 23),
    _OsscpVolumeName_Type()
)
osscpVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osscpVolumeName.setStatus("current")
_Win32ShadowProviderTable_Object = MibTable
win32ShadowProviderTable = _Win32ShadowProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3)
)
if mibBuilder.loadTexts:
    win32ShadowProviderTable.setStatus("current")
_Win32ShadowProviderEntry_Object = MibTableRow
win32ShadowProviderEntry = _Win32ShadowProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1)
)
win32ShadowProviderEntry.setIndexNames(
    (0, "INFORMANT-OS", "osspIndex"),
)
if mibBuilder.loadTexts:
    win32ShadowProviderEntry.setStatus("current")


class _OsspIndex_Type(Integer32):
    """Custom type osspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsspIndex_Type.__name__ = "Integer32"
_OsspIndex_Object = MibTableColumn
osspIndex = _OsspIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 1),
    _OsspIndex_Type()
)
osspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspIndex.setStatus("current")
_OsspCLSID_Type = WtcsDisplayString
_OsspCLSID_Object = MibTableColumn
osspCLSID = _OsspCLSID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 2),
    _OsspCLSID_Type()
)
osspCLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspCLSID.setStatus("current")
_OsspID_Type = WtcsDisplayString
_OsspID_Object = MibTableColumn
osspID = _OsspID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 3),
    _OsspID_Type()
)
osspID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspID.setStatus("current")
_OsspName_Type = WtcsDisplayString
_OsspName_Object = MibTableColumn
osspName = _OsspName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 4),
    _OsspName_Type()
)
osspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspName.setStatus("current")


class _OsspType_Type(Integer32):
    """Custom type osspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 3),
          ("software", 2),
          ("system", 1),
          ("unknown", 0))
    )


_OsspType_Type.__name__ = "Integer32"
_OsspType_Object = MibTableColumn
osspType = _OsspType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 5),
    _OsspType_Type()
)
osspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspType.setStatus("current")
_OsspVersion_Type = WtcsDisplayString
_OsspVersion_Object = MibTableColumn
osspVersion = _OsspVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 6),
    _OsspVersion_Type()
)
osspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspVersion.setStatus("current")
_OsspVersionID_Type = WtcsDisplayString
_OsspVersionID_Object = MibTableColumn
osspVersionID = _OsspVersionID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 13, 3, 1, 7),
    _OsspVersionID_Type()
)
osspVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osspVersionID.setStatus("current")
_WmiEventLog_ObjectIdentity = ObjectIdentity
wmiEventLog = _WmiEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14)
)
if mibBuilder.loadTexts:
    wmiEventLog.setStatus("current")
_Win32NTEventlogFileTable_Object = MibTable
win32NTEventlogFileTable = _Win32NTEventlogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1)
)
if mibBuilder.loadTexts:
    win32NTEventlogFileTable.setStatus("current")
_Win32NTEventlogFileEntry_Object = MibTableRow
win32NTEventlogFileEntry = _Win32NTEventlogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1)
)
win32NTEventlogFileEntry.setIndexNames(
    (0, "INFORMANT-OS", "oselfIndex"),
)
if mibBuilder.loadTexts:
    win32NTEventlogFileEntry.setStatus("current")


class _OselfIndex_Type(Integer32):
    """Custom type oselfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OselfIndex_Type.__name__ = "Integer32"
_OselfIndex_Object = MibTableColumn
oselfIndex = _OselfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 1),
    _OselfIndex_Type()
)
oselfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfIndex.setStatus("current")
_OselfAccessMask_Type = WtcsDisplayString
_OselfAccessMask_Object = MibTableColumn
oselfAccessMask = _OselfAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 2),
    _OselfAccessMask_Type()
)
oselfAccessMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfAccessMask.setStatus("current")
_OselfArchive_Type = TruthValue
_OselfArchive_Object = MibTableColumn
oselfArchive = _OselfArchive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 3),
    _OselfArchive_Type()
)
oselfArchive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfArchive.setStatus("current")
_OselfCaption_Type = WtcsDisplayString
_OselfCaption_Object = MibTableColumn
oselfCaption = _OselfCaption_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 4),
    _OselfCaption_Type()
)
oselfCaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCaption.setStatus("current")
_OselfCompressed_Type = TruthValue
_OselfCompressed_Object = MibTableColumn
oselfCompressed = _OselfCompressed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 5),
    _OselfCompressed_Type()
)
oselfCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCompressed.setStatus("current")
_OselfCompressionMethod_Type = WtcsDisplayString
_OselfCompressionMethod_Object = MibTableColumn
oselfCompressionMethod = _OselfCompressionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 6),
    _OselfCompressionMethod_Type()
)
oselfCompressionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCompressionMethod.setStatus("current")
_OselfCreationClassName_Type = WtcsDisplayString
_OselfCreationClassName_Object = MibTableColumn
oselfCreationClassName = _OselfCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 7),
    _OselfCreationClassName_Type()
)
oselfCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCreationClassName.setStatus("current")
_OselfCreationDate_Type = DateAndTime
_OselfCreationDate_Object = MibTableColumn
oselfCreationDate = _OselfCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 8),
    _OselfCreationDate_Type()
)
oselfCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCreationDate.setStatus("current")
_OselfCSCreationClassName_Type = WtcsDisplayString
_OselfCSCreationClassName_Object = MibTableColumn
oselfCSCreationClassName = _OselfCSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 9),
    _OselfCSCreationClassName_Type()
)
oselfCSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCSCreationClassName.setStatus("current")
_OselfCSName_Type = WtcsDisplayString
_OselfCSName_Object = MibTableColumn
oselfCSName = _OselfCSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 10),
    _OselfCSName_Type()
)
oselfCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfCSName.setStatus("current")
_OselfDescription_Type = WtcsDisplayString
_OselfDescription_Object = MibTableColumn
oselfDescription = _OselfDescription_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 11),
    _OselfDescription_Type()
)
oselfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfDescription.setStatus("current")
_OselfDrive_Type = WtcsDisplayString
_OselfDrive_Object = MibTableColumn
oselfDrive = _OselfDrive_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 12),
    _OselfDrive_Type()
)
oselfDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfDrive.setStatus("current")
_OselfEightDotThreeFileName_Type = WtcsDisplayString
_OselfEightDotThreeFileName_Object = MibTableColumn
oselfEightDotThreeFileName = _OselfEightDotThreeFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 13),
    _OselfEightDotThreeFileName_Type()
)
oselfEightDotThreeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfEightDotThreeFileName.setStatus("current")
_OselfEncrypted_Type = TruthValue
_OselfEncrypted_Object = MibTableColumn
oselfEncrypted = _OselfEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 14),
    _OselfEncrypted_Type()
)
oselfEncrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfEncrypted.setStatus("current")
_OselfEncryptionMethod_Type = WtcsDisplayString
_OselfEncryptionMethod_Object = MibTableColumn
oselfEncryptionMethod = _OselfEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 15),
    _OselfEncryptionMethod_Type()
)
oselfEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfEncryptionMethod.setStatus("current")
_OselfExtension_Type = WtcsDisplayString
_OselfExtension_Object = MibTableColumn
oselfExtension = _OselfExtension_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 16),
    _OselfExtension_Type()
)
oselfExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfExtension.setStatus("current")
_OselfFileName_Type = WtcsDisplayString
_OselfFileName_Object = MibTableColumn
oselfFileName = _OselfFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 17),
    _OselfFileName_Type()
)
oselfFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfFileName.setStatus("current")
_OselfFileSize_Type = Gauge32
_OselfFileSize_Object = MibTableColumn
oselfFileSize = _OselfFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 18),
    _OselfFileSize_Type()
)
oselfFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfFileSize.setStatus("current")
_OselfFileType_Type = WtcsDisplayString
_OselfFileType_Object = MibTableColumn
oselfFileType = _OselfFileType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 19),
    _OselfFileType_Type()
)
oselfFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfFileType.setStatus("current")
_OselfFSCreationClassName_Type = WtcsDisplayString
_OselfFSCreationClassName_Object = MibTableColumn
oselfFSCreationClassName = _OselfFSCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 20),
    _OselfFSCreationClassName_Type()
)
oselfFSCreationClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfFSCreationClassName.setStatus("current")
_OselfFSName_Type = WtcsDisplayString
_OselfFSName_Object = MibTableColumn
oselfFSName = _OselfFSName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 21),
    _OselfFSName_Type()
)
oselfFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfFSName.setStatus("current")
_OselfHidden_Type = TruthValue
_OselfHidden_Object = MibTableColumn
oselfHidden = _OselfHidden_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 22),
    _OselfHidden_Type()
)
oselfHidden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfHidden.setStatus("current")
_OselfInstallDate_Type = DateAndTime
_OselfInstallDate_Object = MibTableColumn
oselfInstallDate = _OselfInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 23),
    _OselfInstallDate_Type()
)
oselfInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfInstallDate.setStatus("current")
_OselfInUseCount_Type = Gauge32
_OselfInUseCount_Object = MibTableColumn
oselfInUseCount = _OselfInUseCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 24),
    _OselfInUseCount_Type()
)
oselfInUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfInUseCount.setStatus("current")
_OselfLastAccessed_Type = DateAndTime
_OselfLastAccessed_Object = MibTableColumn
oselfLastAccessed = _OselfLastAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 25),
    _OselfLastAccessed_Type()
)
oselfLastAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfLastAccessed.setStatus("current")
_OselfLastModified_Type = DateAndTime
_OselfLastModified_Object = MibTableColumn
oselfLastModified = _OselfLastModified_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 26),
    _OselfLastModified_Type()
)
oselfLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfLastModified.setStatus("current")
_OselfLogFileName_Type = WtcsDisplayString
_OselfLogFileName_Object = MibTableColumn
oselfLogFileName = _OselfLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 27),
    _OselfLogFileName_Type()
)
oselfLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfLogFileName.setStatus("current")
_OselfManufacturer_Type = WtcsDisplayString
_OselfManufacturer_Object = MibTableColumn
oselfManufacturer = _OselfManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 28),
    _OselfManufacturer_Type()
)
oselfManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfManufacturer.setStatus("current")
_OselfMaxFileSize_Type = Gauge32
_OselfMaxFileSize_Object = MibTableColumn
oselfMaxFileSize = _OselfMaxFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 29),
    _OselfMaxFileSize_Type()
)
oselfMaxFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfMaxFileSize.setStatus("current")
_OselfName_Type = WtcsDisplayString
_OselfName_Object = MibTableColumn
oselfName = _OselfName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 30),
    _OselfName_Type()
)
oselfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfName.setStatus("current")
_OselfNumberOfRecords_Type = Gauge32
_OselfNumberOfRecords_Object = MibTableColumn
oselfNumberOfRecords = _OselfNumberOfRecords_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 31),
    _OselfNumberOfRecords_Type()
)
oselfNumberOfRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfNumberOfRecords.setStatus("current")
_OselfOverwriteOutDated_Type = Gauge32
_OselfOverwriteOutDated_Object = MibTableColumn
oselfOverwriteOutDated = _OselfOverwriteOutDated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 32),
    _OselfOverwriteOutDated_Type()
)
oselfOverwriteOutDated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfOverwriteOutDated.setStatus("current")
if mibBuilder.loadTexts:
    oselfOverwriteOutDated.setUnits("Days")
_OselfOverWritePolicy_Type = WtcsDisplayString
_OselfOverWritePolicy_Object = MibTableColumn
oselfOverWritePolicy = _OselfOverWritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 33),
    _OselfOverWritePolicy_Type()
)
oselfOverWritePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfOverWritePolicy.setStatus("current")
_OselfPath_Type = WtcsDisplayString
_OselfPath_Object = MibTableColumn
oselfPath = _OselfPath_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 34),
    _OselfPath_Type()
)
oselfPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfPath.setStatus("current")
_OselfReadable_Type = TruthValue
_OselfReadable_Object = MibTableColumn
oselfReadable = _OselfReadable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 35),
    _OselfReadable_Type()
)
oselfReadable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfReadable.setStatus("current")
_OselfSources_Type = WtcsDisplayString
_OselfSources_Object = MibTableColumn
oselfSources = _OselfSources_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 36),
    _OselfSources_Type()
)
oselfSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfSources.setStatus("current")


class _OselfStatus_Type(Integer32):
    """Custom type oselfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("error", 2),
          ("lostComm", 12),
          ("noContact", 11),
          ("nonRecover", 10),
          ("ok", 1),
          ("predFail", 5),
          ("service", 8),
          ("starting", 6),
          ("stopping", 7),
          ("stressed", 9),
          ("unknown", 4))
    )


_OselfStatus_Type.__name__ = "Integer32"
_OselfStatus_Object = MibTableColumn
oselfStatus = _OselfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 37),
    _OselfStatus_Type()
)
oselfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfStatus.setStatus("current")
_OselfSystem_Type = TruthValue
_OselfSystem_Object = MibTableColumn
oselfSystem = _OselfSystem_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 38),
    _OselfSystem_Type()
)
oselfSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfSystem.setStatus("current")
_OselfVersion_Type = WtcsDisplayString
_OselfVersion_Object = MibTableColumn
oselfVersion = _OselfVersion_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 39),
    _OselfVersion_Type()
)
oselfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfVersion.setStatus("current")
_OselfWriteable_Type = TruthValue
_OselfWriteable_Object = MibTableColumn
oselfWriteable = _OselfWriteable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 1, 1, 40),
    _OselfWriteable_Type()
)
oselfWriteable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselfWriteable.setStatus("current")
_Win32NTLogEventTable_Object = MibTable
win32NTLogEventTable = _Win32NTLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2)
)
if mibBuilder.loadTexts:
    win32NTLogEventTable.setStatus("current")
_Win32NTLogEventEntry_Object = MibTableRow
win32NTLogEventEntry = _Win32NTLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1)
)
win32NTLogEventEntry.setIndexNames(
    (0, "INFORMANT-OS", "oselIndex"),
)
if mibBuilder.loadTexts:
    win32NTLogEventEntry.setStatus("current")


class _OselIndex_Type(Integer32):
    """Custom type oselIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OselIndex_Type.__name__ = "Integer32"
_OselIndex_Object = MibTableColumn
oselIndex = _OselIndex_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 1),
    _OselIndex_Type()
)
oselIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselIndex.setStatus("current")
_OselCategory_Type = Gauge32
_OselCategory_Object = MibTableColumn
oselCategory = _OselCategory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 2),
    _OselCategory_Type()
)
oselCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselCategory.setStatus("current")
_OselCategoryString_Type = WtcsDisplayString
_OselCategoryString_Object = MibTableColumn
oselCategoryString = _OselCategoryString_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 3),
    _OselCategoryString_Type()
)
oselCategoryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselCategoryString.setStatus("current")
_OselComputerName_Type = WtcsDisplayString
_OselComputerName_Object = MibTableColumn
oselComputerName = _OselComputerName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 4),
    _OselComputerName_Type()
)
oselComputerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselComputerName.setStatus("current")
_OselData_Type = WtcsDisplayString
_OselData_Object = MibTableColumn
oselData = _OselData_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 5),
    _OselData_Type()
)
oselData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselData.setStatus("current")
_OselEventCode_Type = Gauge32
_OselEventCode_Object = MibTableColumn
oselEventCode = _OselEventCode_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 6),
    _OselEventCode_Type()
)
oselEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselEventCode.setStatus("current")
_OselEventIdentifier_Type = Gauge32
_OselEventIdentifier_Object = MibTableColumn
oselEventIdentifier = _OselEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 7),
    _OselEventIdentifier_Type()
)
oselEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselEventIdentifier.setStatus("current")


class _OselEventType_Type(Integer32):
    """Custom type oselEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("information", 3),
          ("securityAuditFailure", 5),
          ("securityAuditSuccess", 4),
          ("warning", 2))
    )


_OselEventType_Type.__name__ = "Integer32"
_OselEventType_Object = MibTableColumn
oselEventType = _OselEventType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 8),
    _OselEventType_Type()
)
oselEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselEventType.setStatus("current")
_OselInsertionStrings_Type = WtcsDisplayString
_OselInsertionStrings_Object = MibTableColumn
oselInsertionStrings = _OselInsertionStrings_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 9),
    _OselInsertionStrings_Type()
)
oselInsertionStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselInsertionStrings.setStatus("current")
_OselLogfile_Type = WtcsDisplayString
_OselLogfile_Object = MibTableColumn
oselLogfile = _OselLogfile_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 10),
    _OselLogfile_Type()
)
oselLogfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselLogfile.setStatus("current")
_OselMessage_Type = WtcsDisplayString
_OselMessage_Object = MibTableColumn
oselMessage = _OselMessage_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 11),
    _OselMessage_Type()
)
oselMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselMessage.setStatus("current")
_OselRecordNumber_Type = Gauge32
_OselRecordNumber_Object = MibTableColumn
oselRecordNumber = _OselRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 12),
    _OselRecordNumber_Type()
)
oselRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselRecordNumber.setStatus("current")
_OselSourceName_Type = WtcsDisplayString
_OselSourceName_Object = MibTableColumn
oselSourceName = _OselSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 13),
    _OselSourceName_Type()
)
oselSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselSourceName.setStatus("current")
_OselTimeGenerated_Type = DateAndTime
_OselTimeGenerated_Object = MibTableColumn
oselTimeGenerated = _OselTimeGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 14),
    _OselTimeGenerated_Type()
)
oselTimeGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselTimeGenerated.setStatus("current")
_OselTimeWritten_Type = DateAndTime
_OselTimeWritten_Object = MibTableColumn
oselTimeWritten = _OselTimeWritten_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 15),
    _OselTimeWritten_Type()
)
oselTimeWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselTimeWritten.setStatus("current")
_OselType_Type = WtcsDisplayString
_OselType_Object = MibTableColumn
oselType = _OselType_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 16),
    _OselType_Type()
)
oselType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselType.setStatus("current")
_OselUser_Type = WtcsDisplayString
_OselUser_Object = MibTableColumn
oselUser = _OselUser_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 22, 14, 2, 1, 17),
    _OselUser_Type()
)
oselUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oselUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-OS",
    **{"wmiOperatingSystem": wmiOperatingSystem,
       "wmiDesktop": wmiDesktop,
       "win32DesktopTable": win32DesktopTable,
       "win32DesktopEntry": win32DesktopEntry,
       "osdtIndex": osdtIndex,
       "osdtBorderWidth": osdtBorderWidth,
       "osdtCaption": osdtCaption,
       "osdtCoolSwitch": osdtCoolSwitch,
       "osdtCursorBlinkRate": osdtCursorBlinkRate,
       "osdtDescription": osdtDescription,
       "osdtDragFullWindows": osdtDragFullWindows,
       "osdtGridGranularity": osdtGridGranularity,
       "osdtIconSpacing": osdtIconSpacing,
       "osdtIconTitleFaceName": osdtIconTitleFaceName,
       "osdtIconTitleSize": osdtIconTitleSize,
       "osdtIconTitleWrap": osdtIconTitleWrap,
       "osdtName": osdtName,
       "osdtPattern": osdtPattern,
       "osdtScreenSaverActive": osdtScreenSaverActive,
       "osdtScreenSaverExecutable": osdtScreenSaverExecutable,
       "osdtScreenSaverSecure": osdtScreenSaverSecure,
       "osdtScreenSaverTimeout": osdtScreenSaverTimeout,
       "osdtSettingID": osdtSettingID,
       "osdtWallpaper": osdtWallpaper,
       "osdtWallpaperStretched": osdtWallpaperStretched,
       "osdtWallpaperTiled": osdtWallpaperTiled,
       "win32EnvironmentTable": win32EnvironmentTable,
       "win32EnvironmentEntry": win32EnvironmentEntry,
       "osevIndex": osevIndex,
       "osevCaption": osevCaption,
       "osevDescription": osevDescription,
       "osevInstallDate": osevInstallDate,
       "osevName": osevName,
       "osevStatus": osevStatus,
       "osevSystemVariable": osevSystemVariable,
       "osevUserName": osevUserName,
       "osevVariableValue": osevVariableValue,
       "win32TimeZoneTable": win32TimeZoneTable,
       "win32TimeZoneEntry": win32TimeZoneEntry,
       "ostzIndex": ostzIndex,
       "ostzBias": ostzBias,
       "ostzCaption": ostzCaption,
       "ostzDaylightBias": ostzDaylightBias,
       "ostzDaylightDay": ostzDaylightDay,
       "ostzDaylightDayOfWeek": ostzDaylightDayOfWeek,
       "ostzDaylightHour": ostzDaylightHour,
       "ostzDaylightMillisecond": ostzDaylightMillisecond,
       "ostzDaylightMinute": ostzDaylightMinute,
       "ostzDaylightMonth": ostzDaylightMonth,
       "ostzDaylightName": ostzDaylightName,
       "ostzDaylightSecond": ostzDaylightSecond,
       "ostzDaylightYear": ostzDaylightYear,
       "ostzDescription": ostzDescription,
       "ostzSettingID": ostzSettingID,
       "ostzStandardBias": ostzStandardBias,
       "ostzStandardDay": ostzStandardDay,
       "ostzStandardDayOfWeek": ostzStandardDayOfWeek,
       "ostzStandardHour": ostzStandardHour,
       "ostzStandardMillisecond": ostzStandardMillisecond,
       "ostzStandardMinute": ostzStandardMinute,
       "ostzStandardMonth": ostzStandardMonth,
       "ostzStandardName": ostzStandardName,
       "ostzStandardSecond": ostzStandardSecond,
       "ostzStandardYear": ostzStandardYear,
       "wmiDrivers": wmiDrivers,
       "win32DriverVXDTable": win32DriverVXDTable,
       "win32DriverVXDEntry": win32DriverVXDEntry,
       "osvxdIndex": osvxdIndex,
       "osvxdBuildNumber": osvxdBuildNumber,
       "osvxdCaption": osvxdCaption,
       "osvxdCodeSet": osvxdCodeSet,
       "osvxdControl": osvxdControl,
       "osvxdDescription": osvxdDescription,
       "osvxdDeviceDescriptorBlock": osvxdDeviceDescriptorBlock,
       "osvxdIdentificationCode": osvxdIdentificationCode,
       "osvxdInstallDate": osvxdInstallDate,
       "osvxdLanguageEdition": osvxdLanguageEdition,
       "osvxdManufacturer": osvxdManufacturer,
       "osvxdName": osvxdName,
       "osvxdOtherTargetOS": osvxdOtherTargetOS,
       "osvxdPMAPI": osvxdPMAPI,
       "osvxdSerialNumber": osvxdSerialNumber,
       "osvxdServiceTableSize": osvxdServiceTableSize,
       "osvxdSoftwareElementID": osvxdSoftwareElementID,
       "osvxdSoftwareElementState": osvxdSoftwareElementState,
       "osvxdStatus": osvxdStatus,
       "osvxdTargetOperatingSystem": osvxdTargetOperatingSystem,
       "osvxdV86API": osvxdV86API,
       "osvxdVersion": osvxdVersion,
       "win32SystemDriverTable": win32SystemDriverTable,
       "win32SystemDriverEntry": win32SystemDriverEntry,
       "ossdIndex": ossdIndex,
       "ossdAcceptPause": ossdAcceptPause,
       "ossdAcceptStop": ossdAcceptStop,
       "ossdCaption": ossdCaption,
       "ossdCreationClassName": ossdCreationClassName,
       "ossdDescription": ossdDescription,
       "ossdDesktopInteract": ossdDesktopInteract,
       "ossdDisplayName": ossdDisplayName,
       "ossdErrorControl": ossdErrorControl,
       "ossdExitCode": ossdExitCode,
       "ossdInstallDate": ossdInstallDate,
       "ossdName": ossdName,
       "ossdPathName": ossdPathName,
       "ossdServiceSpecificExitCode": ossdServiceSpecificExitCode,
       "ossdServiceType": ossdServiceType,
       "ossdStarted": ossdStarted,
       "ossdStartMode": ossdStartMode,
       "ossdStartName": ossdStartName,
       "ossdState": ossdState,
       "ossdStatus": ossdStatus,
       "ossdSystemCreationClassName": ossdSystemCreationClassName,
       "ossdSystemName": ossdSystemName,
       "ossdTagId": ossdTagId,
       "wmiFileSystem": wmiFileSystem,
       "win32DiskPartitionTable": win32DiskPartitionTable,
       "win32DiskPartitionEntry": win32DiskPartitionEntry,
       "osdpIndex": osdpIndex,
       "osdpAccess": osdpAccess,
       "osdpAvailability": osdpAvailability,
       "osdpBlockSize": osdpBlockSize,
       "osdpBootable": osdpBootable,
       "osdpBootPartition": osdpBootPartition,
       "osdpCaption": osdpCaption,
       "osdpConfigManagerErrorCode": osdpConfigManagerErrorCode,
       "osdpConfigManagerUserConfig": osdpConfigManagerUserConfig,
       "osdpCreationClassName": osdpCreationClassName,
       "osdpDescription": osdpDescription,
       "osdpDeviceID": osdpDeviceID,
       "osdpDiskIndex": osdpDiskIndex,
       "osdpErrorCleared": osdpErrorCleared,
       "osdpErrorDescription": osdpErrorDescription,
       "osdpErrorMethodology": osdpErrorMethodology,
       "osdpHiddenSectors": osdpHiddenSectors,
       "osdpPartitionIndex": osdpPartitionIndex,
       "osdpInstallDate": osdpInstallDate,
       "osdpLastErrorCode": osdpLastErrorCode,
       "osdpName": osdpName,
       "osdpNumberOfBlocks": osdpNumberOfBlocks,
       "osdpPNPDeviceID": osdpPNPDeviceID,
       "osdpPowerManagementCapabilities": osdpPowerManagementCapabilities,
       "osdpPowerManagementSupported": osdpPowerManagementSupported,
       "osdpPrimaryPartition": osdpPrimaryPartition,
       "osdpPurpose": osdpPurpose,
       "osdpRewritePartition": osdpRewritePartition,
       "osdpSize": osdpSize,
       "osdpStartingOffset": osdpStartingOffset,
       "osdpStatus": osdpStatus,
       "osdpStatusInfo": osdpStatusInfo,
       "osdpSystemCreationClassName": osdpSystemCreationClassName,
       "osdpSystemName": osdpSystemName,
       "osdpType": osdpType,
       "win32LogicalDiskTable": win32LogicalDiskTable,
       "win32LogicalDiskEntry": win32LogicalDiskEntry,
       "osldIndex": osldIndex,
       "osldAccess": osldAccess,
       "osldAvailability": osldAvailability,
       "osldBlockSize": osldBlockSize,
       "osldCaption": osldCaption,
       "osldCompressed": osldCompressed,
       "osldConfigManagerErrorCode": osldConfigManagerErrorCode,
       "osldConfigManagerUserConfig": osldConfigManagerUserConfig,
       "osldCreationClassName": osldCreationClassName,
       "osldDescription": osldDescription,
       "osldDeviceID": osldDeviceID,
       "osldDriveType": osldDriveType,
       "osldErrorCleared": osldErrorCleared,
       "osldErrorDescription": osldErrorDescription,
       "osldErrorMethodology": osldErrorMethodology,
       "osldFileSystem": osldFileSystem,
       "osldFreeSpace": osldFreeSpace,
       "osldInstallDate": osldInstallDate,
       "osldLastErrorCode": osldLastErrorCode,
       "osldMaximumComponentLength": osldMaximumComponentLength,
       "osldMediaType": osldMediaType,
       "osldName": osldName,
       "osldNumberOfBlocks": osldNumberOfBlocks,
       "osldPNPDeviceID": osldPNPDeviceID,
       "osldPowerManagementCapabilities": osldPowerManagementCapabilities,
       "osldPowerManagementSupported": osldPowerManagementSupported,
       "osldProviderName": osldProviderName,
       "osldPurpose": osldPurpose,
       "osldQuotasDisabled": osldQuotasDisabled,
       "osldQuotasIncomplete": osldQuotasIncomplete,
       "osldQuotasRebuilding": osldQuotasRebuilding,
       "osldSize": osldSize,
       "osldStatus": osldStatus,
       "osldStatusInfo": osldStatusInfo,
       "osldSupportsDiskQuotas": osldSupportsDiskQuotas,
       "osldSupportsFileBasedCompression": osldSupportsFileBasedCompression,
       "osldSystemCreationClassName": osldSystemCreationClassName,
       "osldSystemName": osldSystemName,
       "osldVolumeDirty": osldVolumeDirty,
       "osldVolumeName": osldVolumeName,
       "osldVolumeSerialNumber": osldVolumeSerialNumber,
       "win32MappedLogicalDiskTable": win32MappedLogicalDiskTable,
       "win32MappedLogicalDiskEntry": win32MappedLogicalDiskEntry,
       "osmldIndex": osmldIndex,
       "osmldAccess": osmldAccess,
       "osmldAvailability": osmldAvailability,
       "osmldBlockSize": osmldBlockSize,
       "osmldCaption": osmldCaption,
       "osmldCompressed": osmldCompressed,
       "osmldConfigManagerErrorCode": osmldConfigManagerErrorCode,
       "osmldConfigManagerUserConfig": osmldConfigManagerUserConfig,
       "osmldCreationClassName": osmldCreationClassName,
       "osmldDescription": osmldDescription,
       "osmldDeviceID": osmldDeviceID,
       "osmldErrorCleared": osmldErrorCleared,
       "osmldErrorDescription": osmldErrorDescription,
       "osmldErrorMethodology": osmldErrorMethodology,
       "osmldFileSystem": osmldFileSystem,
       "osmldFreeSpace": osmldFreeSpace,
       "osmldInstallDate": osmldInstallDate,
       "osmldLastErrorCode": osmldLastErrorCode,
       "osmldMaximumComponentLength": osmldMaximumComponentLength,
       "osmldName": osmldName,
       "osmldNumberOfBlocks": osmldNumberOfBlocks,
       "osmldPNPDeviceID": osmldPNPDeviceID,
       "osmldPowerManagementCapabilities": osmldPowerManagementCapabilities,
       "osmldPowerManagementSupported": osmldPowerManagementSupported,
       "osmldProviderName": osmldProviderName,
       "osmldPurpose": osmldPurpose,
       "osmldQuotasDisabled": osmldQuotasDisabled,
       "osmldQuotasIncomplete": osmldQuotasIncomplete,
       "osmldQuotasRebuilding": osmldQuotasRebuilding,
       "osmldSessionID": osmldSessionID,
       "osmldSize": osmldSize,
       "osmldStatus": osmldStatus,
       "osmldStatusInfo": osmldStatusInfo,
       "osmldSupportsDiskQuotas": osmldSupportsDiskQuotas,
       "osmldSupportFileBasedCompression": osmldSupportFileBasedCompression,
       "osmldSystemCreationClassName": osmldSystemCreationClassName,
       "osmldSystemName": osmldSystemName,
       "osmldVolumeName": osmldVolumeName,
       "osmldVolumeSerialNumber": osmldVolumeSerialNumber,
       "win32QuotaSettingTable": win32QuotaSettingTable,
       "win32QuotaSettingEntry": win32QuotaSettingEntry,
       "osqsIndex": osqsIndex,
       "osqsCaption": osqsCaption,
       "osqsDefaultLimit": osqsDefaultLimit,
       "osqsDefaultWarningLimit": osqsDefaultWarningLimit,
       "osqsDescription": osqsDescription,
       "osqsExceededNotification": osqsExceededNotification,
       "osqsSettingID": osqsSettingID,
       "osqsState": osqsState,
       "osqsVolumePath": osqsVolumePath,
       "osqsWarningExceededNotification": osqsWarningExceededNotification,
       "win32VolumeTable": win32VolumeTable,
       "win32VolumeEntry": win32VolumeEntry,
       "osvlIndex": osvlIndex,
       "osvlAutomount": osvlAutomount,
       "osvlCapacity": osvlCapacity,
       "osvlCompressed": osvlCompressed,
       "osvlDeviceId": osvlDeviceId,
       "osvlDirtyBitSet": osvlDirtyBitSet,
       "osvlDriveLetter": osvlDriveLetter,
       "osvlDriveType": osvlDriveType,
       "osvlFileSystem": osvlFileSystem,
       "osvlFreeSpace": osvlFreeSpace,
       "osvlIndexingEnabled": osvlIndexingEnabled,
       "osvlLabel": osvlLabel,
       "osvlMaximumFileNameLength": osvlMaximumFileNameLength,
       "osvlQuotasEnabled": osvlQuotasEnabled,
       "osvlQuotasIncomplete": osvlQuotasIncomplete,
       "osvlQuotasRebuilding": osvlQuotasRebuilding,
       "osvlSerialNumber": osvlSerialNumber,
       "osvlSupportsDiskQuotas": osvlSupportsDiskQuotas,
       "osvlSupportsFileBasedCompression": osvlSupportsFileBasedCompression,
       "wmiJobObjects": wmiJobObjects,
       "win32NamedJobObjectTable": win32NamedJobObjectTable,
       "win32NamedJobObjectEntry": win32NamedJobObjectEntry,
       "osnjoIndex": osnjoIndex,
       "osnjoBasicUIRestrictions": osnjoBasicUIRestrictions,
       "osnjoCaption": osnjoCaption,
       "osnjoCollectionID": osnjoCollectionID,
       "osnjoDescription": osnjoDescription,
       "win32NamedJobObjectActgInfoTable": win32NamedJobObjectActgInfoTable,
       "win32NamedJobObjectActgInfoEntry": win32NamedJobObjectActgInfoEntry,
       "osjoaIndex": osjoaIndex,
       "osjoaActiveProcesses": osjoaActiveProcesses,
       "osjoaCaption": osjoaCaption,
       "osjoaDescription": osjoaDescription,
       "osjoaName": osjoaName,
       "osjoaOtherOperationCount": osjoaOtherOperationCount,
       "osjoaOtherTransferCount": osjoaOtherTransferCount,
       "osjoaPeakJobMemoryUsed": osjoaPeakJobMemoryUsed,
       "osjoaPeakProcessMemoryUsed": osjoaPeakProcessMemoryUsed,
       "osjoaReadOperationCount": osjoaReadOperationCount,
       "osjoaReadTransferCount": osjoaReadTransferCount,
       "osjoaThisPeriodTotalKernelTime": osjoaThisPeriodTotalKernelTime,
       "osjoaThisPeriodTotalUserTime": osjoaThisPeriodTotalUserTime,
       "osjoaTotalKernelTime": osjoaTotalKernelTime,
       "osjoaTotalPageFaultCount": osjoaTotalPageFaultCount,
       "osjoaTotalProcesses": osjoaTotalProcesses,
       "osjoaTotalTerminatedProcesses": osjoaTotalTerminatedProcesses,
       "osjoaTotalUserTime": osjoaTotalUserTime,
       "osjoaWriteOperationCount": osjoaWriteOperationCount,
       "osjoaWriteTransferCount": osjoaWriteTransferCount,
       "win32NamedJobObjectLimitSetTable": win32NamedJobObjectLimitSetTable,
       "win32NamedJobObjectLimitSetEntry": win32NamedJobObjectLimitSetEntry,
       "osjolIndex": osjolIndex,
       "osjolActiveProcessLimit": osjolActiveProcessLimit,
       "osjolAffinity": osjolAffinity,
       "osjolCaption": osjolCaption,
       "osjolDescription": osjolDescription,
       "osjolJobMemoryLimit": osjolJobMemoryLimit,
       "osjolLimitFlags": osjolLimitFlags,
       "osjolMaximumWorkingSetSize": osjolMaximumWorkingSetSize,
       "osjolMinimumWorkingSetSize": osjolMinimumWorkingSetSize,
       "osjolPerJobUserTimeLimit": osjolPerJobUserTimeLimit,
       "osjolPerProcessUserTimeLimit": osjolPerProcessUserTimeLimit,
       "osjolPriorityClass": osjolPriorityClass,
       "osjolProcessMemoryLimit": osjolProcessMemoryLimit,
       "osjolSchedulingClass": osjolSchedulingClass,
       "osjolSettingID": osjolSettingID,
       "wmiPageFiles": wmiPageFiles,
       "win32PageFileTable": win32PageFileTable,
       "win32PageFileEntry": win32PageFileEntry,
       "ospfIndex": ospfIndex,
       "ospfAccessMask": ospfAccessMask,
       "ospfArchive": ospfArchive,
       "ospfCaption": ospfCaption,
       "ospfCompressed": ospfCompressed,
       "ospfCompressionMethod": ospfCompressionMethod,
       "ospfCreationClassName": ospfCreationClassName,
       "ospfCreationDate": ospfCreationDate,
       "ospfCSCreationClassName": ospfCSCreationClassName,
       "ospfCSName": ospfCSName,
       "ospfDescription": ospfDescription,
       "ospfDrive": ospfDrive,
       "ospfEightDotThreeFileName": ospfEightDotThreeFileName,
       "ospfEncrypted": ospfEncrypted,
       "ospfEncryptionMethod": ospfEncryptionMethod,
       "ospfExtension": ospfExtension,
       "ospfFileName": ospfFileName,
       "ospfFileSize": ospfFileSize,
       "ospfFileType": ospfFileType,
       "ospfFreeSpace": ospfFreeSpace,
       "ospfFSCreationClassName": ospfFSCreationClassName,
       "ospfFSName": ospfFSName,
       "ospfHidden": ospfHidden,
       "ospfInitialSize": ospfInitialSize,
       "ospfInstallDate": ospfInstallDate,
       "ospfInUseCount": ospfInUseCount,
       "ospfLastAccessed": ospfLastAccessed,
       "ospfLastModified": ospfLastModified,
       "ospfManufacturer": ospfManufacturer,
       "ospfMaximumSize": ospfMaximumSize,
       "ospfName": ospfName,
       "ospfPath": ospfPath,
       "ospfReadable": ospfReadable,
       "ospfStatus": ospfStatus,
       "ospfSystem": ospfSystem,
       "ospfVersion": ospfVersion,
       "ospfWriteable": ospfWriteable,
       "win32PageFileSettingTable": win32PageFileSettingTable,
       "win32PageFileSettingEntry": win32PageFileSettingEntry,
       "ospfsIndex": ospfsIndex,
       "ospfsCaption": ospfsCaption,
       "ospfsDescription": ospfsDescription,
       "ospfsInitialSize": ospfsInitialSize,
       "ospfsMaximumSize": ospfsMaximumSize,
       "ospfsName": ospfsName,
       "ospfsSettingID": ospfsSettingID,
       "win32PageFileUsageTable": win32PageFileUsageTable,
       "win32PageFileUsageEntry": win32PageFileUsageEntry,
       "ospfuIndex": ospfuIndex,
       "ospfuAllocatedBaseSize": ospfuAllocatedBaseSize,
       "ospfuCaption": ospfuCaption,
       "ospfuCurrentUsage": ospfuCurrentUsage,
       "ospfuDescription": ospfuDescription,
       "ospfuInstallDate": ospfuInstallDate,
       "ospfuName": ospfuName,
       "ospfuPeakUsage": ospfuPeakUsage,
       "ospfuStatus": ospfuStatus,
       "ospfuTempPageFile": ospfuTempPageFile,
       "wmiMultimedia": wmiMultimedia,
       "win32CodecFileTable": win32CodecFileTable,
       "win32CodecFileEntry": win32CodecFileEntry,
       "oscfIndex": oscfIndex,
       "oscfAccessMask": oscfAccessMask,
       "oscfArchive": oscfArchive,
       "oscfCaption": oscfCaption,
       "oscfCompressed": oscfCompressed,
       "oscfCompressionMethod": oscfCompressionMethod,
       "oscfCreationClassName": oscfCreationClassName,
       "oscfCreationDate": oscfCreationDate,
       "oscfCSCreationClassName": oscfCSCreationClassName,
       "oscfCSName": oscfCSName,
       "oscfDescription": oscfDescription,
       "oscfDrive": oscfDrive,
       "oscfEightDotThreeFileName": oscfEightDotThreeFileName,
       "oscfEncrypted": oscfEncrypted,
       "oscfEncryptionMethod": oscfEncryptionMethod,
       "oscfExtension": oscfExtension,
       "oscfFileName": oscfFileName,
       "oscfFileSize": oscfFileSize,
       "oscfFileType": oscfFileType,
       "oscfFSCreationClassName": oscfFSCreationClassName,
       "oscfFSName": oscfFSName,
       "oscfGroup": oscfGroup,
       "oscfHidden": oscfHidden,
       "oscfInstallDate": oscfInstallDate,
       "oscfInUseCount": oscfInUseCount,
       "oscfLastAccessed": oscfLastAccessed,
       "oscfLastModified": oscfLastModified,
       "oscfManufacturer": oscfManufacturer,
       "oscfName": oscfName,
       "oscfPath": oscfPath,
       "oscfReadable": oscfReadable,
       "oscfStatus": oscfStatus,
       "oscfSystem": oscfSystem,
       "oscfVersion": oscfVersion,
       "oscfWriteable": oscfWriteable,
       "wmiNetworking": wmiNetworking,
       "win32IP4PersistedRouteTableTable": win32IP4PersistedRouteTableTable,
       "win32IP4PersistedRouteTableEntry": win32IP4PersistedRouteTableEntry,
       "osprtIndex": osprtIndex,
       "osprtCaption": osprtCaption,
       "osprtDescription": osprtDescription,
       "osprtDestination": osprtDestination,
       "osprtInstallDate": osprtInstallDate,
       "osprtMask": osprtMask,
       "osprtMetric1": osprtMetric1,
       "osprtName": osprtName,
       "osprtNextHop": osprtNextHop,
       "osprtStatus": osprtStatus,
       "win32IP4RouteTableTable": win32IP4RouteTableTable,
       "win32IP4RouteTableEntry": win32IP4RouteTableEntry,
       "osrtIndex": osrtIndex,
       "osrtAge": osrtAge,
       "osrtCaption": osrtCaption,
       "osrtDescription": osrtDescription,
       "osrtDestination": osrtDestination,
       "osrtInformation": osrtInformation,
       "osrtInstallDate": osrtInstallDate,
       "osrtInterfaceIndex": osrtInterfaceIndex,
       "osrtMask": osrtMask,
       "osrtMetric1": osrtMetric1,
       "osrtMetric2": osrtMetric2,
       "osrtMetric3": osrtMetric3,
       "osrtMetric4": osrtMetric4,
       "osrtMetric5": osrtMetric5,
       "osrtName": osrtName,
       "osrtNextHop": osrtNextHop,
       "osrtProtocol": osrtProtocol,
       "osrtStatus": osrtStatus,
       "osrtType": osrtType,
       "win32NetworkClientTable": win32NetworkClientTable,
       "win32NetworkClientEntry": win32NetworkClientEntry,
       "osnclIndex": osnclIndex,
       "osnclCaption": osnclCaption,
       "osnclDescription": osnclDescription,
       "osnclInstallDate": osnclInstallDate,
       "osnclManufacturer": osnclManufacturer,
       "osnclName": osnclName,
       "osnclStatus": osnclStatus,
       "win32NetworkConnectionTable": win32NetworkConnectionTable,
       "win32NetworkConnectionEntry": win32NetworkConnectionEntry,
       "osncoIndex": osncoIndex,
       "osncoAccessMask": osncoAccessMask,
       "osncoCaption": osncoCaption,
       "osncoComment": osncoComment,
       "osncoConnectionState": osncoConnectionState,
       "osncoConnectionType": osncoConnectionType,
       "osncoDescription": osncoDescription,
       "osncoDisplayType": osncoDisplayType,
       "osncoInstallDate": osncoInstallDate,
       "osncoLocalName": osncoLocalName,
       "osncoName": osncoName,
       "osncoPersistent": osncoPersistent,
       "osncoProviderName": osncoProviderName,
       "osncoRemoteName": osncoRemoteName,
       "osncoRemotePath": osncoRemotePath,
       "osncoResourceType": osncoResourceType,
       "osncoStatus": osncoStatus,
       "osncoUserName": osncoUserName,
       "win32NetworkProtocolTable": win32NetworkProtocolTable,
       "win32NetworkProtocolEntry": win32NetworkProtocolEntry,
       "osnpIndex": osnpIndex,
       "osnpCaption": osnpCaption,
       "osnpConnectionlessService": osnpConnectionlessService,
       "osnpDescription": osnpDescription,
       "osnpGuaranteesDelivery": osnpGuaranteesDelivery,
       "osnpGuaranteesSequencing": osnpGuaranteesSequencing,
       "osnpInstallDate": osnpInstallDate,
       "osnpMaximumAddressSize": osnpMaximumAddressSize,
       "osnpMaximumMessageSize": osnpMaximumMessageSize,
       "osnpMessageOriented": osnpMessageOriented,
       "osnpMinimumAddressSize": osnpMinimumAddressSize,
       "osnpName": osnpName,
       "osnpPseudoStreamOriented": osnpPseudoStreamOriented,
       "osnpStatus": osnpStatus,
       "osnpSupportsBroadcasting": osnpSupportsBroadcasting,
       "osnpSupportsConnectData": osnpSupportsConnectData,
       "osnpSupportsDisconnectData": osnpSupportsDisconnectData,
       "osnpSupportsEncryption": osnpSupportsEncryption,
       "osnpSupportsExpeditedData": osnpSupportsExpeditedData,
       "osnpSupportsFragmentation": osnpSupportsFragmentation,
       "osnpSupportsGracefulClosing": osnpSupportsGracefulClosing,
       "osnpSupportsGuaranteedBandwidth": osnpSupportsGuaranteedBandwidth,
       "osnpSupportsMulticasting": osnpSupportsMulticasting,
       "osnpSupportsQualityofService": osnpSupportsQualityofService,
       "win32NTDomainTable": win32NTDomainTable,
       "win32NTDomainEntry": win32NTDomainEntry,
       "osdoIndex": osdoIndex,
       "osdoCaption": osdoCaption,
       "osdoClientSiteName": osdoClientSiteName,
       "osdoCreationClassName": osdoCreationClassName,
       "osdoDcSiteName": osdoDcSiteName,
       "osdoDescription": osdoDescription,
       "osdoDNSForestName": osdoDNSForestName,
       "osdoDomainControllerAddress": osdoDomainControllerAddress,
       "osdoDomainControllerAddressType": osdoDomainControllerAddressType,
       "osdoDomainControllerName": osdoDomainControllerName,
       "osdoDomainGUID": osdoDomainGUID,
       "osdoDomainName": osdoDomainName,
       "osdoDSDirectoryServiceFlag": osdoDSDirectoryServiceFlag,
       "osdoDSDnsControllerFlag": osdoDSDnsControllerFlag,
       "osdoDSDnsDomainFlag": osdoDSDnsDomainFlag,
       "osdoDSDnsForestFlag": osdoDSDnsForestFlag,
       "osdoDSGlobalCatalogFlag": osdoDSGlobalCatalogFlag,
       "osdoDSKerberosDistCenterFlag": osdoDSKerberosDistCenterFlag,
       "osdoDSPriDomainControllerFlag": osdoDSPriDomainControllerFlag,
       "osdoDSTimeServiceFlag": osdoDSTimeServiceFlag,
       "osdoDSWritableFlag": osdoDSWritableFlag,
       "osdoInstallDate": osdoInstallDate,
       "osdoName": osdoName,
       "osdoNameFormat": osdoNameFormat,
       "osdoPrimaryOwnerContact": osdoPrimaryOwnerContact,
       "osdoPrimaryOwnerName": osdoPrimaryOwnerName,
       "osdoRoles": osdoRoles,
       "osdoStatus": osdoStatus,
       "wmiOperatingSystemSettings": wmiOperatingSystemSettings,
       "win32BootConfigurationTable": win32BootConfigurationTable,
       "win32BootConfigurationEntry": win32BootConfigurationEntry,
       "osbcIndex": osbcIndex,
       "osbcBootDirectory": osbcBootDirectory,
       "osbcCaption": osbcCaption,
       "osbcConfigurationPath": osbcConfigurationPath,
       "osbcDescription": osbcDescription,
       "osbcLastDrive": osbcLastDrive,
       "osbcName": osbcName,
       "osbcScratchDirectory": osbcScratchDirectory,
       "osbcSettingID": osbcSettingID,
       "osbcTempDirectory": osbcTempDirectory,
       "win32ComputerSystemTable": win32ComputerSystemTable,
       "win32ComputerSystemEntry": win32ComputerSystemEntry,
       "oscsIndex": oscsIndex,
       "oscsAdminPasswordStatus": oscsAdminPasswordStatus,
       "oscsAutomaticResetBootOption": oscsAutomaticResetBootOption,
       "oscsAutomaticResetCapability": oscsAutomaticResetCapability,
       "oscsBootOptionOnLimit": oscsBootOptionOnLimit,
       "oscsBootOptionOnWatchDog": oscsBootOptionOnWatchDog,
       "oscsBootROMSupported": oscsBootROMSupported,
       "oscsBootupState": oscsBootupState,
       "oscsCaption": oscsCaption,
       "oscsChassisBootupState": oscsChassisBootupState,
       "oscsCreationClassName": oscsCreationClassName,
       "oscsCurrentTimeZone": oscsCurrentTimeZone,
       "oscsDaylightInEffect": oscsDaylightInEffect,
       "oscsDescription": oscsDescription,
       "oscsDNSHostName": oscsDNSHostName,
       "oscsDomain": oscsDomain,
       "oscsDomainRole": oscsDomainRole,
       "oscsEnableDaylightSavingsTime": oscsEnableDaylightSavingsTime,
       "oscsFrontPanelResetStatus": oscsFrontPanelResetStatus,
       "oscsInfraredSupported": oscsInfraredSupported,
       "oscsInitialLoadInfo": oscsInitialLoadInfo,
       "oscsInstallDate": oscsInstallDate,
       "oscsKeyboardPasswordStatus": oscsKeyboardPasswordStatus,
       "oscsLastLoadInfo": oscsLastLoadInfo,
       "oscsManufacturer": oscsManufacturer,
       "oscsModel": oscsModel,
       "oscsName": oscsName,
       "oscsNameFormat": oscsNameFormat,
       "oscsNetworkServerModeEnabled": oscsNetworkServerModeEnabled,
       "oscsNumberOfProcessors": oscsNumberOfProcessors,
       "oscsOEMLogoBitmap": oscsOEMLogoBitmap,
       "oscsOEMStringArray": oscsOEMStringArray,
       "oscsPartOfDomain": oscsPartOfDomain,
       "oscsPauseAfterReset": oscsPauseAfterReset,
       "oscsPowerManagementCapabilities": oscsPowerManagementCapabilities,
       "oscsPowerManagementSupported": oscsPowerManagementSupported,
       "oscsPowerOnPasswordStatus": oscsPowerOnPasswordStatus,
       "oscsPowerState": oscsPowerState,
       "oscsPowerSupplyState": oscsPowerSupplyState,
       "oscsPrimaryOwnerContact": oscsPrimaryOwnerContact,
       "oscsPrimaryOwnerName": oscsPrimaryOwnerName,
       "oscsResetCapability": oscsResetCapability,
       "oscsResetCount": oscsResetCount,
       "oscsResetLimit": oscsResetLimit,
       "oscsRoles": oscsRoles,
       "oscsStatus": oscsStatus,
       "oscsSupportContactDescription": oscsSupportContactDescription,
       "oscsSystemStartupDelay": oscsSystemStartupDelay,
       "oscsSystemStartupOptions": oscsSystemStartupOptions,
       "oscsSystemStartupSetting": oscsSystemStartupSetting,
       "oscsSystemType": oscsSystemType,
       "oscsThermalState": oscsThermalState,
       "oscsTotalPhysicalMemory": oscsTotalPhysicalMemory,
       "oscsUserName": oscsUserName,
       "oscsWakeUpType": oscsWakeUpType,
       "oscsWorkgroup": oscsWorkgroup,
       "oscsAutomaticManagedPagefile": oscsAutomaticManagedPagefile,
       "oscsNumberOfLogicalProcessors": oscsNumberOfLogicalProcessors,
       "oscsPCSystemType": oscsPCSystemType,
       "win32ComputerSystemProductTable": win32ComputerSystemProductTable,
       "win32ComputerSystemProductEntry": win32ComputerSystemProductEntry,
       "oscspIndex": oscspIndex,
       "oscspCaption": oscspCaption,
       "oscspDescription": oscspDescription,
       "oscspIdentifyingNumber": oscspIdentifyingNumber,
       "oscspName": oscspName,
       "oscspSKUNumber": oscspSKUNumber,
       "oscspUUID": oscspUUID,
       "oscspVendor": oscspVendor,
       "oscspVersion": oscspVersion,
       "win32LoadOrderGroupTable": win32LoadOrderGroupTable,
       "win32LoadOrderGroupEntry": win32LoadOrderGroupEntry,
       "oslogIndex": oslogIndex,
       "oslogCaption": oslogCaption,
       "oslogDescription": oslogDescription,
       "oslogDriverEnabled": oslogDriverEnabled,
       "oslogGroupOrder": oslogGroupOrder,
       "oslogInstallDate": oslogInstallDate,
       "oslogName": oslogName,
       "oslogStatus": oslogStatus,
       "win32OperatingSystemTable": win32OperatingSystemTable,
       "win32OperatingSystemEntry": win32OperatingSystemEntry,
       "ososIndex": ososIndex,
       "ososBootDevice": ososBootDevice,
       "ososBuildNumber": ososBuildNumber,
       "ososBuildType": ososBuildType,
       "ososCaption": ososCaption,
       "ososCodeSet": ososCodeSet,
       "ososCountryCode": ososCountryCode,
       "ososCreationClassName": ososCreationClassName,
       "ososCSCreationClassName": ososCSCreationClassName,
       "ososCSDVersion": ososCSDVersion,
       "ososCSName": ososCSName,
       "ososCurrentTimeZone": ososCurrentTimeZone,
       "ososDataExecPrevention32BitAppl": ososDataExecPrevention32BitAppl,
       "ososDataExecPreventionAvailable": ososDataExecPreventionAvailable,
       "ososDataExecPreventionDrivers": ososDataExecPreventionDrivers,
       "ososDebug": ososDebug,
       "ososDescription": ososDescription,
       "ososDistributed": ososDistributed,
       "ososEncryptionLevel": ososEncryptionLevel,
       "ososForegroundApplicationBoost": ososForegroundApplicationBoost,
       "ososFreePhysicalMemory": ososFreePhysicalMemory,
       "ososFreeSpaceInPagingFiles": ososFreeSpaceInPagingFiles,
       "ososFreeVirtualMemory": ososFreeVirtualMemory,
       "ososInstallDate": ososInstallDate,
       "ososLargeSystemCache": ososLargeSystemCache,
       "ososLastBootUpTime": ososLastBootUpTime,
       "ososLocalDateTime": ososLocalDateTime,
       "ososLocale": ososLocale,
       "ososManufacturer": ososManufacturer,
       "ososMaxNumberOfProcesses": ososMaxNumberOfProcesses,
       "ososMaxProcessMemorySize": ososMaxProcessMemorySize,
       "ososName": ososName,
       "ososNumberOfLicensedUsers": ososNumberOfLicensedUsers,
       "ososNumberOfProcesses": ososNumberOfProcesses,
       "ososNumberOfUsers": ososNumberOfUsers,
       "ososOrganization": ososOrganization,
       "ososOSLanguage": ososOSLanguage,
       "ososOSProductSuite": ososOSProductSuite,
       "ososOSType": ososOSType,
       "ososOtherTypeDescription": ososOtherTypeDescription,
       "ososPAEEnabled": ososPAEEnabled,
       "ososPlusProductID": ososPlusProductID,
       "ososPlusVersionNumber": ososPlusVersionNumber,
       "ososPrimary": ososPrimary,
       "ososProductType": ososProductType,
       "ososQuantumLength": ososQuantumLength,
       "ososQuantumType": ososQuantumType,
       "ososRegisteredUser": ososRegisteredUser,
       "ososSerialNumber": ososSerialNumber,
       "ososServicePackMajorVersion": ososServicePackMajorVersion,
       "ososServicePackMinorVersion": ososServicePackMinorVersion,
       "ososSizeStoredInPagingFiles": ososSizeStoredInPagingFiles,
       "ososStatus": ososStatus,
       "ososSuiteMask": ososSuiteMask,
       "ososSystemDevice": ososSystemDevice,
       "ososSystemDirectory": ososSystemDirectory,
       "ososSystemDrive": ososSystemDrive,
       "ososTotalSwapSpaceSize": ososTotalSwapSpaceSize,
       "ososTotalVirtualMemorySize": ososTotalVirtualMemorySize,
       "ososTotalVisibleMemorySize": ososTotalVisibleMemorySize,
       "ososVersion": ososVersion,
       "ososWindowsDirectory": ososWindowsDirectory,
       "win32OSRecoveryConfigTable": win32OSRecoveryConfigTable,
       "win32OSRecoveryConfigEntry": win32OSRecoveryConfigEntry,
       "osrcIndex": osrcIndex,
       "osrcAutoReboot": osrcAutoReboot,
       "osrcCaption": osrcCaption,
       "osrcDebugFilePath": osrcDebugFilePath,
       "osrcDebugInfoType": osrcDebugInfoType,
       "osrcDescription": osrcDescription,
       "osrcExpandedDebugFilePath": osrcExpandedDebugFilePath,
       "osrcExpandedMiniDumpDirectory": osrcExpandedMiniDumpDirectory,
       "osrcKernelDumpOnly": osrcKernelDumpOnly,
       "osrcMiniDumpDirectory": osrcMiniDumpDirectory,
       "osrcName": osrcName,
       "osrcOverwriteExistingDebugFile": osrcOverwriteExistingDebugFile,
       "osrcSendAdminAlert": osrcSendAdminAlert,
       "osrcSettingID": osrcSettingID,
       "osrcWriteDebugInfo": osrcWriteDebugInfo,
       "osrcWriteToSystemLog": osrcWriteToSystemLog,
       "win32QuickFixEngineeringTable": win32QuickFixEngineeringTable,
       "win32QuickFixEngineeringEntry": win32QuickFixEngineeringEntry,
       "osqfeIndex": osqfeIndex,
       "osqfeCaption": osqfeCaption,
       "osqfeCSName": osqfeCSName,
       "osqfeDescription": osqfeDescription,
       "osqfeFixComments": osqfeFixComments,
       "osqfeHotFixID": osqfeHotFixID,
       "osqfeInstallDate": osqfeInstallDate,
       "osqfeInstalledBy": osqfeInstalledBy,
       "osqfeInstalledOn": osqfeInstalledOn,
       "osqfeName": osqfeName,
       "osqfeServicePackInEffect": osqfeServicePackInEffect,
       "osqfeStatus": osqfeStatus,
       "win32StartupCommandTable": win32StartupCommandTable,
       "win32StartupCommandEntry": win32StartupCommandEntry,
       "osscIndex": osscIndex,
       "osscCaption": osscCaption,
       "osscCommand": osscCommand,
       "osscDescription": osscDescription,
       "osscLocation": osscLocation,
       "osscName": osscName,
       "osscSettingID": osscSettingID,
       "osscUser": osscUser,
       "win32Shutdown": win32Shutdown,
       "win32WinSATTable": win32WinSATTable,
       "win32WinSATEntry": win32WinSATEntry,
       "ossatIndex": ossatIndex,
       "ossatCPUScore": ossatCPUScore,
       "ossatD3DScore": ossatD3DScore,
       "ossatDiskScore": ossatDiskScore,
       "ossatGraphicsScore": ossatGraphicsScore,
       "ossatMemoryScore": ossatMemoryScore,
       "ossatTimeTaken": ossatTimeTaken,
       "ossatAssessmentState": ossatAssessmentState,
       "ossatSPRLevel": ossatSPRLevel,
       "wmiProcesses": wmiProcesses,
       "win32ProcessTable": win32ProcessTable,
       "win32ProcessEntry": win32ProcessEntry,
       "ospsIndex": ospsIndex,
       "ospsCaption": ospsCaption,
       "ospsCommandLine": ospsCommandLine,
       "ospsCreationClassName": ospsCreationClassName,
       "ospsCreationDate": ospsCreationDate,
       "ospsCSCreationClassName": ospsCSCreationClassName,
       "ospsCSName": ospsCSName,
       "ospsDescription": ospsDescription,
       "ospsExecutablePath": ospsExecutablePath,
       "ospsExecutionState": ospsExecutionState,
       "ospsHandle": ospsHandle,
       "ospsHandleCount": ospsHandleCount,
       "ospsInstallDate": ospsInstallDate,
       "ospsKernelModeTime": ospsKernelModeTime,
       "ospsMaximumWorkingSetSize": ospsMaximumWorkingSetSize,
       "ospsMinimumWorkingSetSize": ospsMinimumWorkingSetSize,
       "ospsName": ospsName,
       "ospsOSCreationClassName": ospsOSCreationClassName,
       "ospsOSName": ospsOSName,
       "ospsOtherOperationCount": ospsOtherOperationCount,
       "ospsOtherTransferCount": ospsOtherTransferCount,
       "ospsPageFaults": ospsPageFaults,
       "ospsPageFileUsage": ospsPageFileUsage,
       "ospsParentProcessId": ospsParentProcessId,
       "ospsPeakPageFileUsage": ospsPeakPageFileUsage,
       "ospsPeakVirtualSize": ospsPeakVirtualSize,
       "ospsPeakWorkingSetSize": ospsPeakWorkingSetSize,
       "ospsPriority": ospsPriority,
       "ospsPrivatePageCount": ospsPrivatePageCount,
       "ospsProcessId": ospsProcessId,
       "ospsQuotaNonPagedPoolUsage": ospsQuotaNonPagedPoolUsage,
       "ospsQuotaPagedPoolUsage": ospsQuotaPagedPoolUsage,
       "ospsQuotaPeakNonPagedPoolUsage": ospsQuotaPeakNonPagedPoolUsage,
       "ospsQuotaPeakPagedPoolUsage": ospsQuotaPeakPagedPoolUsage,
       "ospsReadOperationCount": ospsReadOperationCount,
       "ospsReadTransferCount": ospsReadTransferCount,
       "ospsSessionId": ospsSessionId,
       "ospsStatus": ospsStatus,
       "ospsTerminationDate": ospsTerminationDate,
       "ospsThreadCount": ospsThreadCount,
       "ospsUserModeTime": ospsUserModeTime,
       "ospsVirtualSize": ospsVirtualSize,
       "ospsWindowsVersion": ospsWindowsVersion,
       "ospsWorkingSetSize": ospsWorkingSetSize,
       "ospsWriteOperationCount": ospsWriteOperationCount,
       "ospsWriteTransferCount": ospsWriteTransferCount,
       "win32ThreadTable": win32ThreadTable,
       "win32ThreadEntry": win32ThreadEntry,
       "ostdIndex": ostdIndex,
       "ostdCaption": ostdCaption,
       "ostdCreationClassName": ostdCreationClassName,
       "ostdCSCreationClassName": ostdCSCreationClassName,
       "ostdCSName": ostdCSName,
       "ostdDescription": ostdDescription,
       "ostdElapsedTime": ostdElapsedTime,
       "ostdExecutionState": ostdExecutionState,
       "ostdHandle": ostdHandle,
       "ostdInstallDate": ostdInstallDate,
       "ostdKernelModeTime": ostdKernelModeTime,
       "ostdName": ostdName,
       "ostdOSCreationClassName": ostdOSCreationClassName,
       "ostdOSName": ostdOSName,
       "ostdPriority": ostdPriority,
       "ostdPriorityBase": ostdPriorityBase,
       "ostdProcessCreationClassName": ostdProcessCreationClassName,
       "ostdProcessHandle": ostdProcessHandle,
       "ostdStartAddress": ostdStartAddress,
       "ostdStatus": ostdStatus,
       "ostdThreadState": ostdThreadState,
       "ostdThreadWaitReason": ostdThreadWaitReason,
       "ostdUserModeTime": ostdUserModeTime,
       "win32CreateProcess": win32CreateProcess,
       "wmiSchedulerJobs": wmiSchedulerJobs,
       "win32CurrentTimeTable": win32CurrentTimeTable,
       "win32CurrentTimeEntry": win32CurrentTimeEntry,
       "osctIndex": osctIndex,
       "osctDay": osctDay,
       "osctDayOfWeek": osctDayOfWeek,
       "osctHour": osctHour,
       "osctMilliseconds": osctMilliseconds,
       "osctMinute": osctMinute,
       "osctMonth": osctMonth,
       "osctQuarter": osctQuarter,
       "osctSecond": osctSecond,
       "osctWeekInMonth": osctWeekInMonth,
       "osctYear": osctYear,
       "win32ScheduledJobTable": win32ScheduledJobTable,
       "win32ScheduledJobEntry": win32ScheduledJobEntry,
       "ossjIndex": ossjIndex,
       "ossjCaption": ossjCaption,
       "ossjCommand": ossjCommand,
       "ossjDaysOfMonth": ossjDaysOfMonth,
       "ossjDaysOfWeek": ossjDaysOfWeek,
       "ossjDescription": ossjDescription,
       "ossjElapsedTime": ossjElapsedTime,
       "ossjInstallDate": ossjInstallDate,
       "ossjInteractWithDesktop": ossjInteractWithDesktop,
       "ossjJobId": ossjJobId,
       "ossjJobStatus": ossjJobStatus,
       "ossjName": ossjName,
       "ossjNotify": ossjNotify,
       "ossjOwner": ossjOwner,
       "ossjPriority": ossjPriority,
       "ossjRunRepeatedly": ossjRunRepeatedly,
       "ossjStartTime": ossjStartTime,
       "ossjStatus": ossjStatus,
       "ossjTimeSubmitted": ossjTimeSubmitted,
       "ossjUntilTime": ossjUntilTime,
       "wmiServices": wmiServices,
       "win32ServiceTable": win32ServiceTable,
       "win32ServiceEntry": win32ServiceEntry,
       "ossvcIndex": ossvcIndex,
       "ossvcAcceptPause": ossvcAcceptPause,
       "ossvcAcceptStop": ossvcAcceptStop,
       "ossvcCaption": ossvcCaption,
       "ossvcCheckPoint": ossvcCheckPoint,
       "ossvcCreationClassName": ossvcCreationClassName,
       "ossvcDescription": ossvcDescription,
       "ossvcDesktopInteract": ossvcDesktopInteract,
       "ossvcDisplayName": ossvcDisplayName,
       "ossvcErrorControl": ossvcErrorControl,
       "ossvcExitCode": ossvcExitCode,
       "ossvcInstallDate": ossvcInstallDate,
       "ossvcName": ossvcName,
       "ossvcPathName": ossvcPathName,
       "ossvcProcessId": ossvcProcessId,
       "ossvcServiceSpecificExitCode": ossvcServiceSpecificExitCode,
       "ossvcServiceType": ossvcServiceType,
       "ossvcStarted": ossvcStarted,
       "ossvcStartMode": ossvcStartMode,
       "ossvcStartName": ossvcStartName,
       "ossvcState": ossvcState,
       "ossvcStatus": ossvcStatus,
       "ossvcSystemCreationClassName": ossvcSystemCreationClassName,
       "ossvcSystemName": ossvcSystemName,
       "ossvcTagId": ossvcTagId,
       "ossvcWaitHint": ossvcWaitHint,
       "wmiShares": wmiShares,
       "win32DFSNodeTable": win32DFSNodeTable,
       "win32DFSNodeEntry": win32DFSNodeEntry,
       "osdfsnIndex": osdfsnIndex,
       "osdfsnCaption": osdfsnCaption,
       "osdfsnDescription": osdfsnDescription,
       "osdfsnInstallDate": osdfsnInstallDate,
       "osdfsnName": osdfsnName,
       "osdfsnRoot": osdfsnRoot,
       "osdfsnState": osdfsnState,
       "osdfsnStatus": osdfsnStatus,
       "osdfsnTimeout": osdfsnTimeout,
       "win32DFSTargetTable": win32DFSTargetTable,
       "win32DFSTargetEntry": win32DFSTargetEntry,
       "osdfstIndex": osdfstIndex,
       "osdfstCaption": osdfstCaption,
       "osdfstDescription": osdfstDescription,
       "osdfstInstallDate": osdfstInstallDate,
       "osdfstLinkName": osdfstLinkName,
       "osdfstName": osdfstName,
       "osdfstServerName": osdfstServerName,
       "osdfstShareName": osdfstShareName,
       "osdfstState": osdfstState,
       "osdfstStatus": osdfstStatus,
       "win32ServerConnectionTable": win32ServerConnectionTable,
       "win32ServerConnectionEntry": win32ServerConnectionEntry,
       "osscnIndex": osscnIndex,
       "osscnActiveTime": osscnActiveTime,
       "osscnCaption": osscnCaption,
       "osscnComputerName": osscnComputerName,
       "osscnConnectionID": osscnConnectionID,
       "osscnDescription": osscnDescription,
       "osscnInstallDate": osscnInstallDate,
       "osscnName": osscnName,
       "osscnNumberOfFiles": osscnNumberOfFiles,
       "osscnNumberOfUsers": osscnNumberOfUsers,
       "osscnShareName": osscnShareName,
       "osscnStatus": osscnStatus,
       "osscnUserName": osscnUserName,
       "win32ServerSessionTable": win32ServerSessionTable,
       "win32ServerSessionEntry": win32ServerSessionEntry,
       "osssIndex": osssIndex,
       "osssActiveTime": osssActiveTime,
       "osssCaption": osssCaption,
       "osssClientType": osssClientType,
       "osssComputerName": osssComputerName,
       "osssDescription": osssDescription,
       "osssIdleTime": osssIdleTime,
       "osssInstallDate": osssInstallDate,
       "osssName": osssName,
       "osssResourcesOpened": osssResourcesOpened,
       "osssSessionType": osssSessionType,
       "osssStatus": osssStatus,
       "osssTransportName": osssTransportName,
       "osssUserName": osssUserName,
       "win32ShareTable": win32ShareTable,
       "win32ShareEntry": win32ShareEntry,
       "osshIndex": osshIndex,
       "osshAccessMask": osshAccessMask,
       "osshAllowMaximum": osshAllowMaximum,
       "osshCaption": osshCaption,
       "osshDescription": osshDescription,
       "osshInstallDate": osshInstallDate,
       "osshMaximumAllowed": osshMaximumAllowed,
       "osshName": osshName,
       "osshPath": osshPath,
       "osshStatus": osshStatus,
       "osshType": osshType,
       "wmiStorage": wmiStorage,
       "win32ShadowContextTable": win32ShadowContextTable,
       "win32ShadowContextEntry": win32ShadowContextEntry,
       "osscxIndex": osscxIndex,
       "osscxClientAccessible": osscxClientAccessible,
       "osscxDifferential": osscxDifferential,
       "osscxExposedLocally": osscxExposedLocally,
       "osscxExposedRemotely": osscxExposedRemotely,
       "osscxHardwareAssisted": osscxHardwareAssisted,
       "osscxImported": osscxImported,
       "osscxName": osscxName,
       "osscxNoAutoRelease": osscxNoAutoRelease,
       "osscxNotSurfaced": osscxNotSurfaced,
       "osscxNoWriters": osscxNoWriters,
       "osscxPersistent": osscxPersistent,
       "osscxPlex": osscxPlex,
       "osscxTransportable": osscxTransportable,
       "win32ShadowCopyTable": win32ShadowCopyTable,
       "win32ShadowCopyEntry": win32ShadowCopyEntry,
       "osscpIndex": osscpIndex,
       "osscpClientAccessible": osscpClientAccessible,
       "osscpCount": osscpCount,
       "osscpDeviceObject": osscpDeviceObject,
       "osscpDifferential": osscpDifferential,
       "osscpExposedLocally": osscpExposedLocally,
       "osscpExposedName": osscpExposedName,
       "osscpExposedRemotely": osscpExposedRemotely,
       "osscpHardwareAssisted": osscpHardwareAssisted,
       "osscpID": osscpID,
       "osscpImported": osscpImported,
       "osscpNoAutoRelease": osscpNoAutoRelease,
       "osscpNotSurfaced": osscpNotSurfaced,
       "osscpNoWriters": osscpNoWriters,
       "osscpOriginatingMachine": osscpOriginatingMachine,
       "osscpPersistent": osscpPersistent,
       "osscpPlex": osscpPlex,
       "osscpProviderID": osscpProviderID,
       "osscpServiceMachine": osscpServiceMachine,
       "osscpSetID": osscpSetID,
       "osscpState": osscpState,
       "osscpTransportable": osscpTransportable,
       "osscpVolumeName": osscpVolumeName,
       "win32ShadowProviderTable": win32ShadowProviderTable,
       "win32ShadowProviderEntry": win32ShadowProviderEntry,
       "osspIndex": osspIndex,
       "osspCLSID": osspCLSID,
       "osspID": osspID,
       "osspName": osspName,
       "osspType": osspType,
       "osspVersion": osspVersion,
       "osspVersionID": osspVersionID,
       "wmiEventLog": wmiEventLog,
       "win32NTEventlogFileTable": win32NTEventlogFileTable,
       "win32NTEventlogFileEntry": win32NTEventlogFileEntry,
       "oselfIndex": oselfIndex,
       "oselfAccessMask": oselfAccessMask,
       "oselfArchive": oselfArchive,
       "oselfCaption": oselfCaption,
       "oselfCompressed": oselfCompressed,
       "oselfCompressionMethod": oselfCompressionMethod,
       "oselfCreationClassName": oselfCreationClassName,
       "oselfCreationDate": oselfCreationDate,
       "oselfCSCreationClassName": oselfCSCreationClassName,
       "oselfCSName": oselfCSName,
       "oselfDescription": oselfDescription,
       "oselfDrive": oselfDrive,
       "oselfEightDotThreeFileName": oselfEightDotThreeFileName,
       "oselfEncrypted": oselfEncrypted,
       "oselfEncryptionMethod": oselfEncryptionMethod,
       "oselfExtension": oselfExtension,
       "oselfFileName": oselfFileName,
       "oselfFileSize": oselfFileSize,
       "oselfFileType": oselfFileType,
       "oselfFSCreationClassName": oselfFSCreationClassName,
       "oselfFSName": oselfFSName,
       "oselfHidden": oselfHidden,
       "oselfInstallDate": oselfInstallDate,
       "oselfInUseCount": oselfInUseCount,
       "oselfLastAccessed": oselfLastAccessed,
       "oselfLastModified": oselfLastModified,
       "oselfLogFileName": oselfLogFileName,
       "oselfManufacturer": oselfManufacturer,
       "oselfMaxFileSize": oselfMaxFileSize,
       "oselfName": oselfName,
       "oselfNumberOfRecords": oselfNumberOfRecords,
       "oselfOverwriteOutDated": oselfOverwriteOutDated,
       "oselfOverWritePolicy": oselfOverWritePolicy,
       "oselfPath": oselfPath,
       "oselfReadable": oselfReadable,
       "oselfSources": oselfSources,
       "oselfStatus": oselfStatus,
       "oselfSystem": oselfSystem,
       "oselfVersion": oselfVersion,
       "oselfWriteable": oselfWriteable,
       "win32NTLogEventTable": win32NTLogEventTable,
       "win32NTLogEventEntry": win32NTLogEventEntry,
       "oselIndex": oselIndex,
       "oselCategory": oselCategory,
       "oselCategoryString": oselCategoryString,
       "oselComputerName": oselComputerName,
       "oselData": oselData,
       "oselEventCode": oselEventCode,
       "oselEventIdentifier": oselEventIdentifier,
       "oselEventType": oselEventType,
       "oselInsertionStrings": oselInsertionStrings,
       "oselLogfile": oselLogfile,
       "oselMessage": oselMessage,
       "oselRecordNumber": oselRecordNumber,
       "oselSourceName": oselSourceName,
       "oselTimeGenerated": oselTimeGenerated,
       "oselTimeWritten": oselTimeWritten,
       "oselType": oselType,
       "oselUser": oselUser}
)
