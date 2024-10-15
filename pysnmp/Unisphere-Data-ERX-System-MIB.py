# SNMP MIB module (Unisphere-Data-ERX-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ERX-System-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:38 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdERXSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17)
)
usdERXSysMIB.setRevisions(
        ("2002-10-14 17:40",
         "2002-04-12 20:57",
         "2001-05-21 19:27",
         "2001-05-15 18:27",
         "2000-04-25 18:44",
         "2000-01-20 00:00",
         "1999-02-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdTimingSelector(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class UsdTimingSourceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingInterfaceIfIndex", 1),
          ("timingInternal", 2),
          ("timingLine", 3))
    )



class UsdTimingSourceLineType(Integer32, TextualConvention):
    status = "current"
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
        *(("timingSourceLineE1PortA", 1),
          ("timingSourceLineE1PortB", 2),
          ("timingSourceLineT1PortA", 3),
          ("timingSourceLineT1PortB", 4),
          ("timingSourceLineUndefined", 0))
    )



class UsdSysCardType(Integer32, TextualConvention):
    status = "current"
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
        *(("ce1", 8),
          ("coc12", 21),
          ("coc12F3", 29),
          ("coc3", 20),
          ("coc3F3", 30),
          ("coc3oc12", 19),
          ("cocxF3", 31),
          ("ct1", 9),
          ("ct3", 2),
          ("ct3P12", 25),
          ("dpfe", 10),
          ("fe8", 16),
          ("ge", 15),
          ("geFe", 24),
          ("hssi", 23),
          ("oc12Atm", 12),
          ("oc12Pos", 11),
          ("oc12Server", 22),
          ("oc3", 3),
          ("oc3Atm", 14),
          ("oc3Pos", 13),
          ("oc3oc12Atm", 18),
          ("oc3oc12Pos", 17),
          ("srp", 1),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("ue3f12", 28),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Frame", 5),
          ("ut3f12", 27),
          ("v35", 26))
    )



# MIB Managed Objects in the order of their OIDs

_UsdERXSysTrap_ObjectIdentity = ObjectIdentity
usdERXSysTrap = _UsdERXSysTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0)
)
_UsdERXSysObjects_ObjectIdentity = ObjectIdentity
usdERXSysObjects = _UsdERXSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1)
)
_UsdERXSysGeneral_ObjectIdentity = ObjectIdentity
usdERXSysGeneral = _UsdERXSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1)
)


class _UsdERXSysChassisRev_Type(Integer32):
    """Custom type usdERXSysChassisRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysChassisRev_Type.__name__ = "Integer32"
_UsdERXSysChassisRev_Object = MibScalar
usdERXSysChassisRev = _UsdERXSysChassisRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 1),
    _UsdERXSysChassisRev_Type()
)
usdERXSysChassisRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysChassisRev.setStatus("current")
_UsdERXSysSwVersion_Type = DisplayString
_UsdERXSysSwVersion_Object = MibScalar
usdERXSysSwVersion = _UsdERXSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 2),
    _UsdERXSysSwVersion_Type()
)
usdERXSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSwVersion.setStatus("current")
_UsdERXSysSwBuildDate_Type = DisplayString
_UsdERXSysSwBuildDate_Object = MibScalar
usdERXSysSwBuildDate = _UsdERXSysSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 3),
    _UsdERXSysSwBuildDate_Type()
)
usdERXSysSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSwBuildDate.setStatus("current")


class _UsdERXSysRevertControl_Type(Integer32):
    """Custom type usdERXSysRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("off", 0),
          ("timeOfDay", 2))
    )


_UsdERXSysRevertControl_Type.__name__ = "Integer32"
_UsdERXSysRevertControl_Object = MibScalar
usdERXSysRevertControl = _UsdERXSysRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 4),
    _UsdERXSysRevertControl_Type()
)
usdERXSysRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysRevertControl.setStatus("current")


class _UsdERXSysRevertTimeOfDay_Type(Integer32):
    """Custom type usdERXSysRevertTimeOfDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_UsdERXSysRevertTimeOfDay_Type.__name__ = "Integer32"
_UsdERXSysRevertTimeOfDay_Object = MibScalar
usdERXSysRevertTimeOfDay = _UsdERXSysRevertTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 5),
    _UsdERXSysRevertTimeOfDay_Type()
)
usdERXSysRevertTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysRevertTimeOfDay.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysRevertTimeOfDay.setUnits("seconds")


class _UsdERXSysBootConfigControl_Type(Integer32):
    """Custom type usdERXSysBootConfigControl based on Integer32"""
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
        *(("factoryDefaults", 2),
          ("file", 0),
          ("fileOnce", 1),
          ("runningConfiguration", 3))
    )


_UsdERXSysBootConfigControl_Type.__name__ = "Integer32"
_UsdERXSysBootConfigControl_Object = MibScalar
usdERXSysBootConfigControl = _UsdERXSysBootConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 6),
    _UsdERXSysBootConfigControl_Type()
)
usdERXSysBootConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootConfigControl.setStatus("current")


class _UsdERXSysBootBackupConfigControl_Type(Integer32):
    """Custom type usdERXSysBootBackupConfigControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefaults", 1),
          ("file", 0),
          ("none", 2))
    )


_UsdERXSysBootBackupConfigControl_Type.__name__ = "Integer32"
_UsdERXSysBootBackupConfigControl_Object = MibScalar
usdERXSysBootBackupConfigControl = _UsdERXSysBootBackupConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 7),
    _UsdERXSysBootBackupConfigControl_Type()
)
usdERXSysBootBackupConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootBackupConfigControl.setStatus("current")


class _UsdERXSysBootForceBackupControl_Type(Integer32):
    """Custom type usdERXSysBootForceBackupControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_UsdERXSysBootForceBackupControl_Type.__name__ = "Integer32"
_UsdERXSysBootForceBackupControl_Object = MibScalar
usdERXSysBootForceBackupControl = _UsdERXSysBootForceBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 8),
    _UsdERXSysBootForceBackupControl_Type()
)
usdERXSysBootForceBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootForceBackupControl.setStatus("current")


class _UsdERXSysBootAutoRevertControl_Type(Integer32):
    """Custom type usdERXSysBootAutoRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("never", 1),
          ("set", 2))
    )


_UsdERXSysBootAutoRevertControl_Type.__name__ = "Integer32"
_UsdERXSysBootAutoRevertControl_Object = MibScalar
usdERXSysBootAutoRevertControl = _UsdERXSysBootAutoRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 9),
    _UsdERXSysBootAutoRevertControl_Type()
)
usdERXSysBootAutoRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootAutoRevertControl.setStatus("current")


class _UsdERXSysBootAutoRevertCountTolerance_Type(Unsigned32):
    """Custom type usdERXSysBootAutoRevertCountTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_UsdERXSysBootAutoRevertCountTolerance_Type.__name__ = "Unsigned32"
_UsdERXSysBootAutoRevertCountTolerance_Object = MibScalar
usdERXSysBootAutoRevertCountTolerance = _UsdERXSysBootAutoRevertCountTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 10),
    _UsdERXSysBootAutoRevertCountTolerance_Type()
)
usdERXSysBootAutoRevertCountTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootAutoRevertCountTolerance.setStatus("current")


class _UsdERXSysBootAutoRevertTimeTolerance_Type(Unsigned32):
    """Custom type usdERXSysBootAutoRevertTimeTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_UsdERXSysBootAutoRevertTimeTolerance_Type.__name__ = "Unsigned32"
_UsdERXSysBootAutoRevertTimeTolerance_Object = MibScalar
usdERXSysBootAutoRevertTimeTolerance = _UsdERXSysBootAutoRevertTimeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 11),
    _UsdERXSysBootAutoRevertTimeTolerance_Type()
)
usdERXSysBootAutoRevertTimeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootAutoRevertTimeTolerance.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysBootAutoRevertTimeTolerance.setUnits("seconds")


class _UsdERXSysBootReleaseFile_Type(DisplayString):
    """Custom type usdERXSysBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysBootReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysBootReleaseFile_Object = MibScalar
usdERXSysBootReleaseFile = _UsdERXSysBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 12),
    _UsdERXSysBootReleaseFile_Type()
)
usdERXSysBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootReleaseFile.setStatus("current")


class _UsdERXSysBootConfigFile_Type(DisplayString):
    """Custom type usdERXSysBootConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysBootConfigFile_Type.__name__ = "DisplayString"
_UsdERXSysBootConfigFile_Object = MibScalar
usdERXSysBootConfigFile = _UsdERXSysBootConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 13),
    _UsdERXSysBootConfigFile_Type()
)
usdERXSysBootConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootConfigFile.setStatus("current")


class _UsdERXSysBootBackupReleaseFile_Type(DisplayString):
    """Custom type usdERXSysBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysBootBackupReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysBootBackupReleaseFile_Object = MibScalar
usdERXSysBootBackupReleaseFile = _UsdERXSysBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 14),
    _UsdERXSysBootBackupReleaseFile_Type()
)
usdERXSysBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootBackupReleaseFile.setStatus("current")


class _UsdERXSysBootBackupConfigFile_Type(DisplayString):
    """Custom type usdERXSysBootBackupConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysBootBackupConfigFile_Type.__name__ = "DisplayString"
_UsdERXSysBootBackupConfigFile_Object = MibScalar
usdERXSysBootBackupConfigFile = _UsdERXSysBootBackupConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 15),
    _UsdERXSysBootBackupConfigFile_Type()
)
usdERXSysBootBackupConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysBootBackupConfigFile.setStatus("current")
_UsdERXSysAdminTimingSource_Type = UsdTimingSelector
_UsdERXSysAdminTimingSource_Object = MibScalar
usdERXSysAdminTimingSource = _UsdERXSysAdminTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 16),
    _UsdERXSysAdminTimingSource_Type()
)
usdERXSysAdminTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysAdminTimingSource.setStatus("current")
_UsdERXSysOperTimingSource_Type = UsdTimingSelector
_UsdERXSysOperTimingSource_Object = MibScalar
usdERXSysOperTimingSource = _UsdERXSysOperTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 17),
    _UsdERXSysOperTimingSource_Type()
)
usdERXSysOperTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysOperTimingSource.setStatus("current")


class _UsdERXSysTimingDisableAutoUpgrade_Type(TruthValue):
    """Custom type usdERXSysTimingDisableAutoUpgrade based on TruthValue"""


_UsdERXSysTimingDisableAutoUpgrade_Object = MibScalar
usdERXSysTimingDisableAutoUpgrade = _UsdERXSysTimingDisableAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 18),
    _UsdERXSysTimingDisableAutoUpgrade_Type()
)
usdERXSysTimingDisableAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysTimingDisableAutoUpgrade.setStatus("current")
_UsdERXSysTimingSelectorTable_Object = MibTable
usdERXSysTimingSelectorTable = _UsdERXSysTimingSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19)
)
if mibBuilder.loadTexts:
    usdERXSysTimingSelectorTable.setStatus("current")
_UsdERXSysTimingSelectorEntry_Object = MibTableRow
usdERXSysTimingSelectorEntry = _UsdERXSysTimingSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1)
)
usdERXSysTimingSelectorEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysTimingSelectorIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysTimingSelectorEntry.setStatus("current")
_UsdERXSysTimingSelectorIndex_Type = UsdTimingSelector
_UsdERXSysTimingSelectorIndex_Object = MibTableColumn
usdERXSysTimingSelectorIndex = _UsdERXSysTimingSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 1),
    _UsdERXSysTimingSelectorIndex_Type()
)
usdERXSysTimingSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysTimingSelectorIndex.setStatus("current")
_UsdERXSysTimingSourceType_Type = UsdTimingSourceType
_UsdERXSysTimingSourceType_Object = MibTableColumn
usdERXSysTimingSourceType = _UsdERXSysTimingSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 2),
    _UsdERXSysTimingSourceType_Type()
)
usdERXSysTimingSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysTimingSourceType.setStatus("current")
_UsdERXSysTimingSourceIfIndex_Type = InterfaceIndexOrZero
_UsdERXSysTimingSourceIfIndex_Object = MibTableColumn
usdERXSysTimingSourceIfIndex = _UsdERXSysTimingSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 3),
    _UsdERXSysTimingSourceIfIndex_Type()
)
usdERXSysTimingSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysTimingSourceIfIndex.setStatus("current")


class _UsdERXSysTimingSourceLine_Type(UsdTimingSourceLineType):
    """Custom type usdERXSysTimingSourceLine based on UsdTimingSourceLineType"""


_UsdERXSysTimingSourceLine_Object = MibTableColumn
usdERXSysTimingSourceLine = _UsdERXSysTimingSourceLine_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 4),
    _UsdERXSysTimingSourceLine_Type()
)
usdERXSysTimingSourceLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysTimingSourceLine.setStatus("current")


class _UsdERXSysTimingStatus_Type(Integer32):
    """Custom type usdERXSysTimingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timingStatusError", 2),
          ("timingStatusOk", 1),
          ("timingStatusUnknown", 3))
    )


_UsdERXSysTimingStatus_Type.__name__ = "Integer32"
_UsdERXSysTimingStatus_Object = MibTableColumn
usdERXSysTimingStatus = _UsdERXSysTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 5),
    _UsdERXSysTimingStatus_Type()
)
usdERXSysTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTimingStatus.setStatus("current")


class _UsdERXSysMemUtilPct_Type(Integer32):
    """Custom type usdERXSysMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_UsdERXSysMemUtilPct_Type.__name__ = "Integer32"
_UsdERXSysMemUtilPct_Object = MibScalar
usdERXSysMemUtilPct = _UsdERXSysMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 20),
    _UsdERXSysMemUtilPct_Type()
)
usdERXSysMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysMemUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysMemUtilPct.setUnits("percent")
_UsdERXSysMemCapacity_Type = Integer32
_UsdERXSysMemCapacity_Object = MibScalar
usdERXSysMemCapacity = _UsdERXSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 21),
    _UsdERXSysMemCapacity_Type()
)
usdERXSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysMemCapacity.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysMemCapacity.setUnits("bytes")


class _UsdERXSysHighMemUtilThreshold_Type(Integer32):
    """Custom type usdERXSysHighMemUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_UsdERXSysHighMemUtilThreshold_Type.__name__ = "Integer32"
_UsdERXSysHighMemUtilThreshold_Object = MibScalar
usdERXSysHighMemUtilThreshold = _UsdERXSysHighMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 22),
    _UsdERXSysHighMemUtilThreshold_Type()
)
usdERXSysHighMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysHighMemUtilThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysHighMemUtilThreshold.setUnits("percent")


class _UsdERXSysAbatedMemUtilThreshold_Type(Integer32):
    """Custom type usdERXSysAbatedMemUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_UsdERXSysAbatedMemUtilThreshold_Type.__name__ = "Integer32"
_UsdERXSysAbatedMemUtilThreshold_Object = MibScalar
usdERXSysAbatedMemUtilThreshold = _UsdERXSysAbatedMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 23),
    _UsdERXSysAbatedMemUtilThreshold_Type()
)
usdERXSysAbatedMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysAbatedMemUtilThreshold.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysAbatedMemUtilThreshold.setUnits("percent")


class _UsdERXSysMemUtilTrapEnable_Type(TruthValue):
    """Custom type usdERXSysMemUtilTrapEnable based on TruthValue"""


_UsdERXSysMemUtilTrapEnable_Object = MibScalar
usdERXSysMemUtilTrapEnable = _UsdERXSysMemUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 24),
    _UsdERXSysMemUtilTrapEnable_Type()
)
usdERXSysMemUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysMemUtilTrapEnable.setStatus("current")
_UsdERXSysFabric_ObjectIdentity = ObjectIdentity
usdERXSysFabric = _UsdERXSysFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2)
)
_UsdERXSysFabricSpeed_Type = Integer32
_UsdERXSysFabricSpeed_Object = MibScalar
usdERXSysFabricSpeed = _UsdERXSysFabricSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2, 1),
    _UsdERXSysFabricSpeed_Type()
)
usdERXSysFabricSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysFabricSpeed.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysFabricSpeed.setUnits("gigabits per second")


class _UsdERXSysFabricRev_Type(Integer32):
    """Custom type usdERXSysFabricRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysFabricRev_Type.__name__ = "Integer32"
_UsdERXSysFabricRev_Object = MibScalar
usdERXSysFabricRev = _UsdERXSysFabricRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2, 2),
    _UsdERXSysFabricRev_Type()
)
usdERXSysFabricRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysFabricRev.setStatus("current")
_UsdERXSysNvs_ObjectIdentity = ObjectIdentity
usdERXSysNvs = _UsdERXSysNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3)
)


class _UsdERXSysNvsStatus_Type(Integer32):
    """Custom type usdERXSysNvsStatus based on Integer32"""
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
        *(("nearCapacity", 3),
          ("nearConfigCapacity", 5),
          ("notPresent", 0),
          ("ok", 4),
          ("volumeError", 2),
          ("writeProtected", 1))
    )


_UsdERXSysNvsStatus_Type.__name__ = "Integer32"
_UsdERXSysNvsStatus_Object = MibScalar
usdERXSysNvsStatus = _UsdERXSysNvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 1),
    _UsdERXSysNvsStatus_Type()
)
usdERXSysNvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysNvsStatus.setStatus("current")
_UsdERXSysNvsCapacity_Type = Integer32
_UsdERXSysNvsCapacity_Object = MibScalar
usdERXSysNvsCapacity = _UsdERXSysNvsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 2),
    _UsdERXSysNvsCapacity_Type()
)
usdERXSysNvsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysNvsCapacity.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysNvsCapacity.setUnits("megabytes")


class _UsdERXSysNvsUtilPct_Type(Integer32):
    """Custom type usdERXSysNvsUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_UsdERXSysNvsUtilPct_Type.__name__ = "Integer32"
_UsdERXSysNvsUtilPct_Object = MibScalar
usdERXSysNvsUtilPct = _UsdERXSysNvsUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 3),
    _UsdERXSysNvsUtilPct_Type()
)
usdERXSysNvsUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysNvsUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysNvsUtilPct.setUnits("percent")
_UsdERXSysSlot_ObjectIdentity = ObjectIdentity
usdERXSysSlot = _UsdERXSysSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4)
)
_UsdERXSysSlotCount_Type = Integer32
_UsdERXSysSlotCount_Object = MibScalar
usdERXSysSlotCount = _UsdERXSysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 1),
    _UsdERXSysSlotCount_Type()
)
usdERXSysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotCount.setStatus("current")
_UsdERXSysSlotTable_Object = MibTable
usdERXSysSlotTable = _UsdERXSysSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdERXSysSlotTable.setStatus("current")
_UsdERXSysSlotEntry_Object = MibTableRow
usdERXSysSlotEntry = _UsdERXSysSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1)
)
usdERXSysSlotEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysSlotEntry.setStatus("current")


class _UsdERXSysSlotIndex_Type(Integer32):
    """Custom type usdERXSysSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysSlotIndex_Type.__name__ = "Integer32"
_UsdERXSysSlotIndex_Object = MibTableColumn
usdERXSysSlotIndex = _UsdERXSysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 1),
    _UsdERXSysSlotIndex_Type()
)
usdERXSysSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysSlotIndex.setStatus("current")


class _UsdERXSysSlotDescr_Type(DisplayString):
    """Custom type usdERXSysSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdERXSysSlotDescr_Type.__name__ = "DisplayString"
_UsdERXSysSlotDescr_Object = MibTableColumn
usdERXSysSlotDescr = _UsdERXSysSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 2),
    _UsdERXSysSlotDescr_Type()
)
usdERXSysSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotDescr.setStatus("current")
_UsdERXSysSlotCurrentCardType_Type = UsdSysCardType
_UsdERXSysSlotCurrentCardType_Object = MibTableColumn
usdERXSysSlotCurrentCardType = _UsdERXSysSlotCurrentCardType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 3),
    _UsdERXSysSlotCurrentCardType_Type()
)
usdERXSysSlotCurrentCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotCurrentCardType.setStatus("current")


class _UsdERXSysSlotRev_Type(Integer32):
    """Custom type usdERXSysSlotRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysSlotRev_Type.__name__ = "Integer32"
_UsdERXSysSlotRev_Object = MibTableColumn
usdERXSysSlotRev = _UsdERXSysSlotRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 4),
    _UsdERXSysSlotRev_Type()
)
usdERXSysSlotRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotRev.setStatus("current")
_UsdERXSysSlotAdminStatus_Type = UsdEnable
_UsdERXSysSlotAdminStatus_Object = MibTableColumn
usdERXSysSlotAdminStatus = _UsdERXSysSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 5),
    _UsdERXSysSlotAdminStatus_Type()
)
usdERXSysSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotAdminStatus.setStatus("current")


class _UsdERXSysSlotOperStatus_Type(Integer32):
    """Custom type usdERXSysSlotOperStatus based on Integer32"""
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
        *(("booting", 4),
          ("disabled", 2),
          ("empty", 1),
          ("failed", 3),
          ("inactive", 8),
          ("initializing", 5),
          ("online", 6),
          ("standby", 7),
          ("unknown", 0))
    )


_UsdERXSysSlotOperStatus_Type.__name__ = "Integer32"
_UsdERXSysSlotOperStatus_Object = MibTableColumn
usdERXSysSlotOperStatus = _UsdERXSysSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 6),
    _UsdERXSysSlotOperStatus_Type()
)
usdERXSysSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotOperStatus.setStatus("current")


class _UsdERXSysSlotDisableReason_Type(Integer32):
    """Custom type usdERXSysSlotDisableReason based on Integer32"""
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
        *(("admin", 3),
          ("assessing", 2),
          ("cardMismatch", 4),
          ("fabricLimit", 5),
          ("imageError", 6),
          ("none", 0),
          ("unknown", 1))
    )


_UsdERXSysSlotDisableReason_Type.__name__ = "Integer32"
_UsdERXSysSlotDisableReason_Object = MibTableColumn
usdERXSysSlotDisableReason = _UsdERXSysSlotDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 7),
    _UsdERXSysSlotDisableReason_Type()
)
usdERXSysSlotDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotDisableReason.setStatus("current")
_UsdERXSysSlotExpectedCardType_Type = UsdSysCardType
_UsdERXSysSlotExpectedCardType_Object = MibTableColumn
usdERXSysSlotExpectedCardType = _UsdERXSysSlotExpectedCardType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 8),
    _UsdERXSysSlotExpectedCardType_Type()
)
usdERXSysSlotExpectedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotExpectedCardType.setStatus("current")


class _UsdERXSysSlotControl_Type(Integer32):
    """Custom type usdERXSysSlotControl based on Integer32"""
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
        *(("flush", 1),
          ("forceFailover", 3),
          ("noBoot", 4),
          ("noBootBackup", 5),
          ("noOperation", 0),
          ("reset", 2))
    )


_UsdERXSysSlotControl_Type.__name__ = "Integer32"
_UsdERXSysSlotControl_Object = MibTableColumn
usdERXSysSlotControl = _UsdERXSysSlotControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 9),
    _UsdERXSysSlotControl_Type()
)
usdERXSysSlotControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotControl.setStatus("current")


class _UsdERXSysSlotCpuUtilPct_Type(Integer32):
    """Custom type usdERXSysSlotCpuUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_UsdERXSysSlotCpuUtilPct_Type.__name__ = "Integer32"
_UsdERXSysSlotCpuUtilPct_Object = MibTableColumn
usdERXSysSlotCpuUtilPct = _UsdERXSysSlotCpuUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 10),
    _UsdERXSysSlotCpuUtilPct_Type()
)
usdERXSysSlotCpuUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotCpuUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysSlotCpuUtilPct.setUnits("percent")


class _UsdERXSysSlotMemUtilPct_Type(Integer32):
    """Custom type usdERXSysSlotMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_UsdERXSysSlotMemUtilPct_Type.__name__ = "Integer32"
_UsdERXSysSlotMemUtilPct_Object = MibTableColumn
usdERXSysSlotMemUtilPct = _UsdERXSysSlotMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 11),
    _UsdERXSysSlotMemUtilPct_Type()
)
usdERXSysSlotMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotMemUtilPct.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysSlotMemUtilPct.setUnits("percent")
_UsdERXSysSlotIoaPresent_Type = TruthValue
_UsdERXSysSlotIoaPresent_Object = MibTableColumn
usdERXSysSlotIoaPresent = _UsdERXSysSlotIoaPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 12),
    _UsdERXSysSlotIoaPresent_Type()
)
usdERXSysSlotIoaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotIoaPresent.setStatus("current")
_UsdERXSysSlotPortCount_Type = Integer32
_UsdERXSysSlotPortCount_Object = MibTableColumn
usdERXSysSlotPortCount = _UsdERXSysSlotPortCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 13),
    _UsdERXSysSlotPortCount_Type()
)
usdERXSysSlotPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotPortCount.setStatus("current")
_UsdERXSysSlotLastChange_Type = TimeTicks
_UsdERXSysSlotLastChange_Object = MibTableColumn
usdERXSysSlotLastChange = _UsdERXSysSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 14),
    _UsdERXSysSlotLastChange_Type()
)
usdERXSysSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotLastChange.setStatus("current")
_UsdERXSysSlotRedundancyLockout_Type = UsdEnable
_UsdERXSysSlotRedundancyLockout_Object = MibTableColumn
usdERXSysSlotRedundancyLockout = _UsdERXSysSlotRedundancyLockout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 15),
    _UsdERXSysSlotRedundancyLockout_Type()
)
usdERXSysSlotRedundancyLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotRedundancyLockout.setStatus("current")
_UsdERXSysSlotRedundancyGroupId_Type = Unsigned32
_UsdERXSysSlotRedundancyGroupId_Object = MibTableColumn
usdERXSysSlotRedundancyGroupId = _UsdERXSysSlotRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 16),
    _UsdERXSysSlotRedundancyGroupId_Type()
)
usdERXSysSlotRedundancyGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotRedundancyGroupId.setStatus("current")
_UsdERXSysSlotSpareServer_Type = TruthValue
_UsdERXSysSlotSpareServer_Object = MibTableColumn
usdERXSysSlotSpareServer = _UsdERXSysSlotSpareServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 17),
    _UsdERXSysSlotSpareServer_Type()
)
usdERXSysSlotSpareServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotSpareServer.setStatus("current")
_UsdERXSysSlotAssociatedSlot_Type = Integer32
_UsdERXSysSlotAssociatedSlot_Object = MibTableColumn
usdERXSysSlotAssociatedSlot = _UsdERXSysSlotAssociatedSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 18),
    _UsdERXSysSlotAssociatedSlot_Type()
)
usdERXSysSlotAssociatedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotAssociatedSlot.setStatus("current")


class _UsdERXSysSlotRevertControl_Type(Integer32):
    """Custom type usdERXSysSlotRevertControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 1),
          ("off", 0),
          ("timeAndDate", 2))
    )


_UsdERXSysSlotRevertControl_Type.__name__ = "Integer32"
_UsdERXSysSlotRevertControl_Object = MibTableColumn
usdERXSysSlotRevertControl = _UsdERXSysSlotRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 19),
    _UsdERXSysSlotRevertControl_Type()
)
usdERXSysSlotRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotRevertControl.setStatus("current")
_UsdERXSysSlotRedundancyRevertTime_Type = DateAndTime
_UsdERXSysSlotRedundancyRevertTime_Object = MibTableColumn
usdERXSysSlotRedundancyRevertTime = _UsdERXSysSlotRedundancyRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 20),
    _UsdERXSysSlotRedundancyRevertTime_Type()
)
usdERXSysSlotRedundancyRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotRedundancyRevertTime.setStatus("current")


class _UsdERXSysSlotBootReleaseFile_Type(DisplayString):
    """Custom type usdERXSysSlotBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysSlotBootReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysSlotBootReleaseFile_Object = MibTableColumn
usdERXSysSlotBootReleaseFile = _UsdERXSysSlotBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 21),
    _UsdERXSysSlotBootReleaseFile_Type()
)
usdERXSysSlotBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotBootReleaseFile.setStatus("current")


class _UsdERXSysSlotBootBackupReleaseFile_Type(DisplayString):
    """Custom type usdERXSysSlotBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysSlotBootBackupReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysSlotBootBackupReleaseFile_Object = MibTableColumn
usdERXSysSlotBootBackupReleaseFile = _UsdERXSysSlotBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 22),
    _UsdERXSysSlotBootBackupReleaseFile_Type()
)
usdERXSysSlotBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSlotBootBackupReleaseFile.setStatus("current")


class _UsdERXSysSlotSerialNumber_Type(DisplayString):
    """Custom type usdERXSysSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdERXSysSlotSerialNumber_Type.__name__ = "DisplayString"
_UsdERXSysSlotSerialNumber_Object = MibTableColumn
usdERXSysSlotSerialNumber = _UsdERXSysSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 23),
    _UsdERXSysSlotSerialNumber_Type()
)
usdERXSysSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotSerialNumber.setStatus("current")


class _UsdERXSysSlotAssemblyPartNumber_Type(DisplayString):
    """Custom type usdERXSysSlotAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdERXSysSlotAssemblyPartNumber_Type.__name__ = "DisplayString"
_UsdERXSysSlotAssemblyPartNumber_Object = MibTableColumn
usdERXSysSlotAssemblyPartNumber = _UsdERXSysSlotAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 24),
    _UsdERXSysSlotAssemblyPartNumber_Type()
)
usdERXSysSlotAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotAssemblyPartNumber.setStatus("current")


class _UsdERXSysSlotAssemblyRev_Type(DisplayString):
    """Custom type usdERXSysSlotAssemblyRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_UsdERXSysSlotAssemblyRev_Type.__name__ = "DisplayString"
_UsdERXSysSlotAssemblyRev_Object = MibTableColumn
usdERXSysSlotAssemblyRev = _UsdERXSysSlotAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 25),
    _UsdERXSysSlotAssemblyRev_Type()
)
usdERXSysSlotAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotAssemblyRev.setStatus("current")


class _UsdERXSysSlotIoaSerialNumber_Type(DisplayString):
    """Custom type usdERXSysSlotIoaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdERXSysSlotIoaSerialNumber_Type.__name__ = "DisplayString"
_UsdERXSysSlotIoaSerialNumber_Object = MibTableColumn
usdERXSysSlotIoaSerialNumber = _UsdERXSysSlotIoaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 26),
    _UsdERXSysSlotIoaSerialNumber_Type()
)
usdERXSysSlotIoaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotIoaSerialNumber.setStatus("current")


class _UsdERXSysSlotIoaAssemblyPartNumber_Type(DisplayString):
    """Custom type usdERXSysSlotIoaAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_UsdERXSysSlotIoaAssemblyPartNumber_Type.__name__ = "DisplayString"
_UsdERXSysSlotIoaAssemblyPartNumber_Object = MibTableColumn
usdERXSysSlotIoaAssemblyPartNumber = _UsdERXSysSlotIoaAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 27),
    _UsdERXSysSlotIoaAssemblyPartNumber_Type()
)
usdERXSysSlotIoaAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotIoaAssemblyPartNumber.setStatus("current")


class _UsdERXSysSlotIoaAssemblyRev_Type(DisplayString):
    """Custom type usdERXSysSlotIoaAssemblyRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_UsdERXSysSlotIoaAssemblyRev_Type.__name__ = "DisplayString"
_UsdERXSysSlotIoaAssemblyRev_Object = MibTableColumn
usdERXSysSlotIoaAssemblyRev = _UsdERXSysSlotIoaAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 28),
    _UsdERXSysSlotIoaAssemblyRev_Type()
)
usdERXSysSlotIoaAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSlotIoaAssemblyRev.setStatus("current")
_UsdERXSysPort_ObjectIdentity = ObjectIdentity
usdERXSysPort = _UsdERXSysPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5)
)
_UsdERXSysPortTable_Object = MibTable
usdERXSysPortTable = _UsdERXSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdERXSysPortTable.setStatus("current")
_UsdERXSysPortEntry_Object = MibTableRow
usdERXSysPortEntry = _UsdERXSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1)
)
usdERXSysPortEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIndex"),
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysPortIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysPortEntry.setStatus("current")


class _UsdERXSysPortIndex_Type(Integer32):
    """Custom type usdERXSysPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysPortIndex_Type.__name__ = "Integer32"
_UsdERXSysPortIndex_Object = MibTableColumn
usdERXSysPortIndex = _UsdERXSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 1),
    _UsdERXSysPortIndex_Type()
)
usdERXSysPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysPortIndex.setStatus("current")


class _UsdERXSysPortDescr_Type(DisplayString):
    """Custom type usdERXSysPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdERXSysPortDescr_Type.__name__ = "DisplayString"
_UsdERXSysPortDescr_Object = MibTableColumn
usdERXSysPortDescr = _UsdERXSysPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 2),
    _UsdERXSysPortDescr_Type()
)
usdERXSysPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysPortDescr.setStatus("current")


class _UsdERXSysPortType_Type(Integer32):
    """Custom type usdERXSysPortType based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("ce1", 8),
          ("coc12", 15),
          ("coc3", 14),
          ("ct1", 9),
          ("ct3", 2),
          ("eth", 1),
          ("hssi", 17),
          ("oc12Server", 16),
          ("oc12cAtm", 11),
          ("oc12cPos", 10),
          ("oc3c", 3),
          ("oc3cAtm", 13),
          ("oc3cPos", 12),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Frame", 5),
          ("v35", 18))
    )


_UsdERXSysPortType_Type.__name__ = "Integer32"
_UsdERXSysPortType_Object = MibTableColumn
usdERXSysPortType = _UsdERXSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 3),
    _UsdERXSysPortType_Type()
)
usdERXSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysPortType.setStatus("current")
_UsdERXSysPortIfIndex_Type = InterfaceIndexOrZero
_UsdERXSysPortIfIndex_Object = MibTableColumn
usdERXSysPortIfIndex = _UsdERXSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 4),
    _UsdERXSysPortIfIndex_Type()
)
usdERXSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysPortIfIndex.setStatus("current")
_UsdERXSysPower_ObjectIdentity = ObjectIdentity
usdERXSysPower = _UsdERXSysPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6)
)
_UsdERXSysPowerTable_Object = MibTable
usdERXSysPowerTable = _UsdERXSysPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1)
)
if mibBuilder.loadTexts:
    usdERXSysPowerTable.setStatus("current")
_UsdERXSysPowerEntry_Object = MibTableRow
usdERXSysPowerEntry = _UsdERXSysPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1)
)
usdERXSysPowerEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysPowerIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysPowerEntry.setStatus("current")


class _UsdERXSysPowerIndex_Type(Integer32):
    """Custom type usdERXSysPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysPowerIndex_Type.__name__ = "Integer32"
_UsdERXSysPowerIndex_Object = MibTableColumn
usdERXSysPowerIndex = _UsdERXSysPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 1),
    _UsdERXSysPowerIndex_Type()
)
usdERXSysPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysPowerIndex.setStatus("current")


class _UsdERXSysPowerDescr_Type(DisplayString):
    """Custom type usdERXSysPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdERXSysPowerDescr_Type.__name__ = "DisplayString"
_UsdERXSysPowerDescr_Object = MibTableColumn
usdERXSysPowerDescr = _UsdERXSysPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 2),
    _UsdERXSysPowerDescr_Type()
)
usdERXSysPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysPowerDescr.setStatus("current")


class _UsdERXSysPowerStatus_Type(Integer32):
    """Custom type usdERXSysPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_UsdERXSysPowerStatus_Type.__name__ = "Integer32"
_UsdERXSysPowerStatus_Object = MibTableColumn
usdERXSysPowerStatus = _UsdERXSysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 3),
    _UsdERXSysPowerStatus_Type()
)
usdERXSysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysPowerStatus.setStatus("current")
_UsdERXSysTemperature_ObjectIdentity = ObjectIdentity
usdERXSysTemperature = _UsdERXSysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7)
)


class _UsdERXSysTempFanStatus_Type(Integer32):
    """Custom type usdERXSysTempFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1),
          ("warning", 2))
    )


_UsdERXSysTempFanStatus_Type.__name__ = "Integer32"
_UsdERXSysTempFanStatus_Object = MibScalar
usdERXSysTempFanStatus = _UsdERXSysTempFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 1),
    _UsdERXSysTempFanStatus_Type()
)
usdERXSysTempFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempFanStatus.setStatus("current")
_UsdERXSysTempTable_Object = MibTable
usdERXSysTempTable = _UsdERXSysTempTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2)
)
if mibBuilder.loadTexts:
    usdERXSysTempTable.setStatus("current")
_UsdERXSysTempEntry_Object = MibTableRow
usdERXSysTempEntry = _UsdERXSysTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1)
)
usdERXSysTempEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIndex"),
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysTempIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysTempEntry.setStatus("current")


class _UsdERXSysTempIndex_Type(Integer32):
    """Custom type usdERXSysTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysTempIndex_Type.__name__ = "Integer32"
_UsdERXSysTempIndex_Object = MibTableColumn
usdERXSysTempIndex = _UsdERXSysTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 1),
    _UsdERXSysTempIndex_Type()
)
usdERXSysTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysTempIndex.setStatus("current")


class _UsdERXSysTempDescr_Type(DisplayString):
    """Custom type usdERXSysTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UsdERXSysTempDescr_Type.__name__ = "DisplayString"
_UsdERXSysTempDescr_Object = MibTableColumn
usdERXSysTempDescr = _UsdERXSysTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 2),
    _UsdERXSysTempDescr_Type()
)
usdERXSysTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempDescr.setStatus("current")


class _UsdERXSysTempStatus_Type(Integer32):
    """Custom type usdERXSysTempStatus based on Integer32"""
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
        *(("failed", 1),
          ("nominal", 3),
          ("tooHigh", 4),
          ("tooHighWarning", 6),
          ("tooLow", 2),
          ("tooLowWarning", 5),
          ("unknown", 0))
    )


_UsdERXSysTempStatus_Type.__name__ = "Integer32"
_UsdERXSysTempStatus_Object = MibTableColumn
usdERXSysTempStatus = _UsdERXSysTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 3),
    _UsdERXSysTempStatus_Type()
)
usdERXSysTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempStatus.setStatus("current")
_UsdERXSysTempValue_Type = Integer32
_UsdERXSysTempValue_Object = MibTableColumn
usdERXSysTempValue = _UsdERXSysTempValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 4),
    _UsdERXSysTempValue_Type()
)
usdERXSysTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempValue.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysTempValue.setUnits("degrees Celsius")


class _UsdERXSysTempProtectionStatus_Type(Integer32):
    """Custom type usdERXSysTempProtectionStatus based on Integer32"""
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
        *(("activatedHoldOffExpired", 3),
          ("activatedTempTooHigh", 4),
          ("inHoldOff", 2),
          ("monitoring", 1))
    )


_UsdERXSysTempProtectionStatus_Type.__name__ = "Integer32"
_UsdERXSysTempProtectionStatus_Object = MibScalar
usdERXSysTempProtectionStatus = _UsdERXSysTempProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 3),
    _UsdERXSysTempProtectionStatus_Type()
)
usdERXSysTempProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempProtectionStatus.setStatus("current")


class _UsdERXSysTempProtectionHoldOffTime_Type(Integer32):
    """Custom type usdERXSysTempProtectionHoldOffTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_UsdERXSysTempProtectionHoldOffTime_Type.__name__ = "Integer32"
_UsdERXSysTempProtectionHoldOffTime_Object = MibScalar
usdERXSysTempProtectionHoldOffTime = _UsdERXSysTempProtectionHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 4),
    _UsdERXSysTempProtectionHoldOffTime_Type()
)
usdERXSysTempProtectionHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempProtectionHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysTempProtectionHoldOffTime.setUnits("seconds")


class _UsdERXSysTempProtectionHoldOffTimeRemaining_Type(Integer32):
    """Custom type usdERXSysTempProtectionHoldOffTimeRemaining based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_UsdERXSysTempProtectionHoldOffTimeRemaining_Type.__name__ = "Integer32"
_UsdERXSysTempProtectionHoldOffTimeRemaining_Object = MibScalar
usdERXSysTempProtectionHoldOffTimeRemaining = _UsdERXSysTempProtectionHoldOffTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 5),
    _UsdERXSysTempProtectionHoldOffTimeRemaining_Type()
)
usdERXSysTempProtectionHoldOffTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysTempProtectionHoldOffTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    usdERXSysTempProtectionHoldOffTimeRemaining.setUnits("seconds")
_UsdERXSysSubsystem_ObjectIdentity = ObjectIdentity
usdERXSysSubsystem = _UsdERXSysSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8)
)
_UsdERXSysSubsystemTable_Object = MibTable
usdERXSysSubsystemTable = _UsdERXSysSubsystemTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1)
)
if mibBuilder.loadTexts:
    usdERXSysSubsystemTable.setStatus("current")
_UsdERXSysSubsystemEntry_Object = MibTableRow
usdERXSysSubsystemEntry = _UsdERXSysSubsystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1)
)
usdERXSysSubsystemEntry.setIndexNames(
    (0, "Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemIndex"),
)
if mibBuilder.loadTexts:
    usdERXSysSubsystemEntry.setStatus("current")


class _UsdERXSysSubsystemIndex_Type(Integer32):
    """Custom type usdERXSysSubsystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdERXSysSubsystemIndex_Type.__name__ = "Integer32"
_UsdERXSysSubsystemIndex_Object = MibTableColumn
usdERXSysSubsystemIndex = _UsdERXSysSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 1),
    _UsdERXSysSubsystemIndex_Type()
)
usdERXSysSubsystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdERXSysSubsystemIndex.setStatus("current")


class _UsdERXSysSubsystemName_Type(DisplayString):
    """Custom type usdERXSysSubsystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysSubsystemName_Type.__name__ = "DisplayString"
_UsdERXSysSubsystemName_Object = MibTableColumn
usdERXSysSubsystemName = _UsdERXSysSubsystemName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 2),
    _UsdERXSysSubsystemName_Type()
)
usdERXSysSubsystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdERXSysSubsystemName.setStatus("current")


class _UsdERXSysSubsystemControl_Type(Integer32):
    """Custom type usdERXSysSubsystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noBoot", 1),
          ("noBootBackup", 2),
          ("noOperation", 0))
    )


_UsdERXSysSubsystemControl_Type.__name__ = "Integer32"
_UsdERXSysSubsystemControl_Object = MibTableColumn
usdERXSysSubsystemControl = _UsdERXSysSubsystemControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 3),
    _UsdERXSysSubsystemControl_Type()
)
usdERXSysSubsystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSubsystemControl.setStatus("current")


class _UsdERXSysSubsystemBootReleaseFile_Type(DisplayString):
    """Custom type usdERXSysSubsystemBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysSubsystemBootReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysSubsystemBootReleaseFile_Object = MibTableColumn
usdERXSysSubsystemBootReleaseFile = _UsdERXSysSubsystemBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 4),
    _UsdERXSysSubsystemBootReleaseFile_Type()
)
usdERXSysSubsystemBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSubsystemBootReleaseFile.setStatus("current")


class _UsdERXSysSubsystemBootBackupReleaseFile_Type(DisplayString):
    """Custom type usdERXSysSubsystemBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_UsdERXSysSubsystemBootBackupReleaseFile_Type.__name__ = "DisplayString"
_UsdERXSysSubsystemBootBackupReleaseFile_Object = MibTableColumn
usdERXSysSubsystemBootBackupReleaseFile = _UsdERXSysSubsystemBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 5),
    _UsdERXSysSubsystemBootBackupReleaseFile_Type()
)
usdERXSysSubsystemBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdERXSysSubsystemBootBackupReleaseFile.setStatus("current")
_UsdERXSysConformance_ObjectIdentity = ObjectIdentity
usdERXSysConformance = _UsdERXSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2)
)
_UsdERXSysCompliances_ObjectIdentity = ObjectIdentity
usdERXSysCompliances = _UsdERXSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1)
)
_UsdERXSysGroups_ObjectIdentity = ObjectIdentity
usdERXSysGroups = _UsdERXSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2)
)

# Managed Objects groups

usdERXSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 1)
)
usdERXSysGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysChassisRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwVersion"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwBuildDate"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertTimeOfDay"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootForceBackupControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertCountTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertTimeTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysFabricSpeed"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysFabricRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsCapacity"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCount"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCurrentCardType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAdminStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDisableReason"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotExpectedCardType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCpuUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotMemUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIoaPresent"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotPortCount"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotLastChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyLockout"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyGroupId"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotSpareServer"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAssociatedSlot"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyRevertTime"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotBootBackupReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPortDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPortType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPortIfIndex"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempValue"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemName"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemBootBackupReleaseFile"))
)
if mibBuilder.loadTexts:
    usdERXSysGroup.setStatus("obsolete")

usdERXSysGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 3)
)
usdERXSysGeneralGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysChassisRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwVersion"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwBuildDate"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertTimeOfDay"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootForceBackupControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertCountTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertTimeTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigFile"))
)
if mibBuilder.loadTexts:
    usdERXSysGeneralGroup.setStatus("obsolete")

usdERXSysFabricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 4)
)
usdERXSysFabricGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysFabricSpeed"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysFabricRev"))
)
if mibBuilder.loadTexts:
    usdERXSysFabricGroup.setStatus("current")

usdERXSysNvsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 5)
)
usdERXSysNvsGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsCapacity"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysNvsUtilPct"))
)
if mibBuilder.loadTexts:
    usdERXSysNvsGroup.setStatus("current")

usdERXSysSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 6)
)
usdERXSysSlotGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCount"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCurrentCardType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAdminStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDisableReason"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotExpectedCardType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCpuUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotMemUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIoaPresent"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotPortCount"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotLastChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyLockout"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyGroupId"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotSpareServer"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAssociatedSlot"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotRedundancyRevertTime"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotBootBackupReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotSerialNumber"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAssemblyPartNumber"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAssemblyRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIoaSerialNumber"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIoaAssemblyPartNumber"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotIoaAssemblyRev"))
)
if mibBuilder.loadTexts:
    usdERXSysSlotGroup.setStatus("current")

usdERXSysPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 7)
)
usdERXSysPortGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysPortDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPortType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPortIfIndex"))
)
if mibBuilder.loadTexts:
    usdERXSysPortGroup.setStatus("current")

usdERXSysPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 8)
)
usdERXSysPowerGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatus"))
)
if mibBuilder.loadTexts:
    usdERXSysPowerGroup.setStatus("current")

usdERXSysTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 9)
)
usdERXSysTemperatureGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempValue"))
)
if mibBuilder.loadTexts:
    usdERXSysTemperatureGroup.setStatus("obsolete")

usdERXSysSubsystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 10)
)
usdERXSysSubsystemGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemName"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSubsystemBootBackupReleaseFile"))
)
if mibBuilder.loadTexts:
    usdERXSysSubsystemGroup.setStatus("current")

usdERXSysTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 11)
)
usdERXSysTimingGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysAdminTimingSource"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysOperTimingSource"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTimingDisableAutoUpgrade"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTimingSourceType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTimingSourceIfIndex"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTimingSourceLine"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTimingStatus"))
)
if mibBuilder.loadTexts:
    usdERXSysTimingGroup.setStatus("current")

usdERXSysGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 12)
)
usdERXSysGeneralGroup2.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysChassisRev"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwVersion"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSwBuildDate"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysRevertTimeOfDay"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootForceBackupControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertControl"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertCountTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootAutoRevertTimeTolerance"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootConfigFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupReleaseFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysBootBackupConfigFile"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysMemUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysMemCapacity"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysHighMemUtilThreshold"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysAbatedMemUtilThreshold"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysMemUtilTrapEnable"))
)
if mibBuilder.loadTexts:
    usdERXSysGeneralGroup2.setStatus("current")

usdERXSysTemperatureGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 14)
)
usdERXSysTemperatureGroup2.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempDescr"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempValue"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionHoldOffTime"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    usdERXSysTemperatureGroup2.setStatus("current")


# Notification objects

usdERXSysSlotOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 1)
)
usdERXSysSlotOperStatusChange.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotCurrentCardType"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAdminStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDisableReason"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotSpareServer"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotAssociatedSlot"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotDescr"))
)
if mibBuilder.loadTexts:
    usdERXSysSlotOperStatusChange.setStatus(
        "current"
    )

usdERXSysPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 2)
)
usdERXSysPowerStatusChange.setObjects(
    ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatus")
)
if mibBuilder.loadTexts:
    usdERXSysPowerStatusChange.setStatus(
        "current"
    )

usdERXSysTempFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 3)
)
usdERXSysTempFanStatusChange.setObjects(
    ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatus")
)
if mibBuilder.loadTexts:
    usdERXSysTempFanStatusChange.setStatus(
        "current"
    )

usdERXSysTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 4)
)
usdERXSysTempStatusChange.setObjects(
    ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatus")
)
if mibBuilder.loadTexts:
    usdERXSysTempStatusChange.setStatus(
        "current"
    )

usdERXSysHighMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 5)
)
usdERXSysHighMemUtil.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysMemCapacity"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysMemUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysAbatedMemUtilThreshold"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysHighMemUtilThreshold"))
)
if mibBuilder.loadTexts:
    usdERXSysHighMemUtil.setStatus(
        "current"
    )

usdERXSysAbatedMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 6)
)
usdERXSysAbatedMemUtil.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysMemCapacity"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysMemUtilPct"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysAbatedMemUtilThreshold"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysHighMemUtilThreshold"))
)
if mibBuilder.loadTexts:
    usdERXSysAbatedMemUtil.setStatus(
        "current"
    )

usdERXSysTempProtectionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 7)
)
usdERXSysTempProtectionStatusChange.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionStatus"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    usdERXSysTempProtectionStatusChange.setStatus(
        "current"
    )


# Notifications groups

usdERXSysNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 2)
)
usdERXSysNotifyGroup.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatusChange"))
)
if mibBuilder.loadTexts:
    usdERXSysNotifyGroup.setStatus(
        "obsolete"
    )

usdERXSysNotifyGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 13)
)
usdERXSysNotifyGroup2.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysHighMemUtil"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysAbatedMemUtil"))
)
if mibBuilder.loadTexts:
    usdERXSysNotifyGroup2.setStatus(
        "obsolete"
    )

usdERXSysNotifyGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 15)
)
usdERXSysNotifyGroup3.setObjects(
      *(("Unisphere-Data-ERX-System-MIB", "usdERXSysSlotOperStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysPowerStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempFanStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempStatusChange"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysHighMemUtil"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysAbatedMemUtil"),
        ("Unisphere-Data-ERX-System-MIB", "usdERXSysTempProtectionStatusChange"))
)
if mibBuilder.loadTexts:
    usdERXSysNotifyGroup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

usdERXSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdERXSysCompliance.setStatus(
        "obsolete"
    )

usdERXSysCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdERXSysCompliance1.setStatus(
        "obsolete"
    )

usdERXSysCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdERXSysCompliance2.setStatus(
        "obsolete"
    )

usdERXSysCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdERXSysCompliance3.setStatus(
        "obsolete"
    )

usdERXSysCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdERXSysCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ERX-System-MIB",
    **{"UsdTimingSelector": UsdTimingSelector,
       "UsdTimingSourceType": UsdTimingSourceType,
       "UsdTimingSourceLineType": UsdTimingSourceLineType,
       "UsdSysCardType": UsdSysCardType,
       "usdERXSysMIB": usdERXSysMIB,
       "usdERXSysTrap": usdERXSysTrap,
       "usdERXSysSlotOperStatusChange": usdERXSysSlotOperStatusChange,
       "usdERXSysPowerStatusChange": usdERXSysPowerStatusChange,
       "usdERXSysTempFanStatusChange": usdERXSysTempFanStatusChange,
       "usdERXSysTempStatusChange": usdERXSysTempStatusChange,
       "usdERXSysHighMemUtil": usdERXSysHighMemUtil,
       "usdERXSysAbatedMemUtil": usdERXSysAbatedMemUtil,
       "usdERXSysTempProtectionStatusChange": usdERXSysTempProtectionStatusChange,
       "usdERXSysObjects": usdERXSysObjects,
       "usdERXSysGeneral": usdERXSysGeneral,
       "usdERXSysChassisRev": usdERXSysChassisRev,
       "usdERXSysSwVersion": usdERXSysSwVersion,
       "usdERXSysSwBuildDate": usdERXSysSwBuildDate,
       "usdERXSysRevertControl": usdERXSysRevertControl,
       "usdERXSysRevertTimeOfDay": usdERXSysRevertTimeOfDay,
       "usdERXSysBootConfigControl": usdERXSysBootConfigControl,
       "usdERXSysBootBackupConfigControl": usdERXSysBootBackupConfigControl,
       "usdERXSysBootForceBackupControl": usdERXSysBootForceBackupControl,
       "usdERXSysBootAutoRevertControl": usdERXSysBootAutoRevertControl,
       "usdERXSysBootAutoRevertCountTolerance": usdERXSysBootAutoRevertCountTolerance,
       "usdERXSysBootAutoRevertTimeTolerance": usdERXSysBootAutoRevertTimeTolerance,
       "usdERXSysBootReleaseFile": usdERXSysBootReleaseFile,
       "usdERXSysBootConfigFile": usdERXSysBootConfigFile,
       "usdERXSysBootBackupReleaseFile": usdERXSysBootBackupReleaseFile,
       "usdERXSysBootBackupConfigFile": usdERXSysBootBackupConfigFile,
       "usdERXSysAdminTimingSource": usdERXSysAdminTimingSource,
       "usdERXSysOperTimingSource": usdERXSysOperTimingSource,
       "usdERXSysTimingDisableAutoUpgrade": usdERXSysTimingDisableAutoUpgrade,
       "usdERXSysTimingSelectorTable": usdERXSysTimingSelectorTable,
       "usdERXSysTimingSelectorEntry": usdERXSysTimingSelectorEntry,
       "usdERXSysTimingSelectorIndex": usdERXSysTimingSelectorIndex,
       "usdERXSysTimingSourceType": usdERXSysTimingSourceType,
       "usdERXSysTimingSourceIfIndex": usdERXSysTimingSourceIfIndex,
       "usdERXSysTimingSourceLine": usdERXSysTimingSourceLine,
       "usdERXSysTimingStatus": usdERXSysTimingStatus,
       "usdERXSysMemUtilPct": usdERXSysMemUtilPct,
       "usdERXSysMemCapacity": usdERXSysMemCapacity,
       "usdERXSysHighMemUtilThreshold": usdERXSysHighMemUtilThreshold,
       "usdERXSysAbatedMemUtilThreshold": usdERXSysAbatedMemUtilThreshold,
       "usdERXSysMemUtilTrapEnable": usdERXSysMemUtilTrapEnable,
       "usdERXSysFabric": usdERXSysFabric,
       "usdERXSysFabricSpeed": usdERXSysFabricSpeed,
       "usdERXSysFabricRev": usdERXSysFabricRev,
       "usdERXSysNvs": usdERXSysNvs,
       "usdERXSysNvsStatus": usdERXSysNvsStatus,
       "usdERXSysNvsCapacity": usdERXSysNvsCapacity,
       "usdERXSysNvsUtilPct": usdERXSysNvsUtilPct,
       "usdERXSysSlot": usdERXSysSlot,
       "usdERXSysSlotCount": usdERXSysSlotCount,
       "usdERXSysSlotTable": usdERXSysSlotTable,
       "usdERXSysSlotEntry": usdERXSysSlotEntry,
       "usdERXSysSlotIndex": usdERXSysSlotIndex,
       "usdERXSysSlotDescr": usdERXSysSlotDescr,
       "usdERXSysSlotCurrentCardType": usdERXSysSlotCurrentCardType,
       "usdERXSysSlotRev": usdERXSysSlotRev,
       "usdERXSysSlotAdminStatus": usdERXSysSlotAdminStatus,
       "usdERXSysSlotOperStatus": usdERXSysSlotOperStatus,
       "usdERXSysSlotDisableReason": usdERXSysSlotDisableReason,
       "usdERXSysSlotExpectedCardType": usdERXSysSlotExpectedCardType,
       "usdERXSysSlotControl": usdERXSysSlotControl,
       "usdERXSysSlotCpuUtilPct": usdERXSysSlotCpuUtilPct,
       "usdERXSysSlotMemUtilPct": usdERXSysSlotMemUtilPct,
       "usdERXSysSlotIoaPresent": usdERXSysSlotIoaPresent,
       "usdERXSysSlotPortCount": usdERXSysSlotPortCount,
       "usdERXSysSlotLastChange": usdERXSysSlotLastChange,
       "usdERXSysSlotRedundancyLockout": usdERXSysSlotRedundancyLockout,
       "usdERXSysSlotRedundancyGroupId": usdERXSysSlotRedundancyGroupId,
       "usdERXSysSlotSpareServer": usdERXSysSlotSpareServer,
       "usdERXSysSlotAssociatedSlot": usdERXSysSlotAssociatedSlot,
       "usdERXSysSlotRevertControl": usdERXSysSlotRevertControl,
       "usdERXSysSlotRedundancyRevertTime": usdERXSysSlotRedundancyRevertTime,
       "usdERXSysSlotBootReleaseFile": usdERXSysSlotBootReleaseFile,
       "usdERXSysSlotBootBackupReleaseFile": usdERXSysSlotBootBackupReleaseFile,
       "usdERXSysSlotSerialNumber": usdERXSysSlotSerialNumber,
       "usdERXSysSlotAssemblyPartNumber": usdERXSysSlotAssemblyPartNumber,
       "usdERXSysSlotAssemblyRev": usdERXSysSlotAssemblyRev,
       "usdERXSysSlotIoaSerialNumber": usdERXSysSlotIoaSerialNumber,
       "usdERXSysSlotIoaAssemblyPartNumber": usdERXSysSlotIoaAssemblyPartNumber,
       "usdERXSysSlotIoaAssemblyRev": usdERXSysSlotIoaAssemblyRev,
       "usdERXSysPort": usdERXSysPort,
       "usdERXSysPortTable": usdERXSysPortTable,
       "usdERXSysPortEntry": usdERXSysPortEntry,
       "usdERXSysPortIndex": usdERXSysPortIndex,
       "usdERXSysPortDescr": usdERXSysPortDescr,
       "usdERXSysPortType": usdERXSysPortType,
       "usdERXSysPortIfIndex": usdERXSysPortIfIndex,
       "usdERXSysPower": usdERXSysPower,
       "usdERXSysPowerTable": usdERXSysPowerTable,
       "usdERXSysPowerEntry": usdERXSysPowerEntry,
       "usdERXSysPowerIndex": usdERXSysPowerIndex,
       "usdERXSysPowerDescr": usdERXSysPowerDescr,
       "usdERXSysPowerStatus": usdERXSysPowerStatus,
       "usdERXSysTemperature": usdERXSysTemperature,
       "usdERXSysTempFanStatus": usdERXSysTempFanStatus,
       "usdERXSysTempTable": usdERXSysTempTable,
       "usdERXSysTempEntry": usdERXSysTempEntry,
       "usdERXSysTempIndex": usdERXSysTempIndex,
       "usdERXSysTempDescr": usdERXSysTempDescr,
       "usdERXSysTempStatus": usdERXSysTempStatus,
       "usdERXSysTempValue": usdERXSysTempValue,
       "usdERXSysTempProtectionStatus": usdERXSysTempProtectionStatus,
       "usdERXSysTempProtectionHoldOffTime": usdERXSysTempProtectionHoldOffTime,
       "usdERXSysTempProtectionHoldOffTimeRemaining": usdERXSysTempProtectionHoldOffTimeRemaining,
       "usdERXSysSubsystem": usdERXSysSubsystem,
       "usdERXSysSubsystemTable": usdERXSysSubsystemTable,
       "usdERXSysSubsystemEntry": usdERXSysSubsystemEntry,
       "usdERXSysSubsystemIndex": usdERXSysSubsystemIndex,
       "usdERXSysSubsystemName": usdERXSysSubsystemName,
       "usdERXSysSubsystemControl": usdERXSysSubsystemControl,
       "usdERXSysSubsystemBootReleaseFile": usdERXSysSubsystemBootReleaseFile,
       "usdERXSysSubsystemBootBackupReleaseFile": usdERXSysSubsystemBootBackupReleaseFile,
       "usdERXSysConformance": usdERXSysConformance,
       "usdERXSysCompliances": usdERXSysCompliances,
       "usdERXSysCompliance": usdERXSysCompliance,
       "usdERXSysCompliance1": usdERXSysCompliance1,
       "usdERXSysCompliance2": usdERXSysCompliance2,
       "usdERXSysCompliance3": usdERXSysCompliance3,
       "usdERXSysCompliance4": usdERXSysCompliance4,
       "usdERXSysGroups": usdERXSysGroups,
       "usdERXSysGroup": usdERXSysGroup,
       "usdERXSysNotifyGroup": usdERXSysNotifyGroup,
       "usdERXSysGeneralGroup": usdERXSysGeneralGroup,
       "usdERXSysFabricGroup": usdERXSysFabricGroup,
       "usdERXSysNvsGroup": usdERXSysNvsGroup,
       "usdERXSysSlotGroup": usdERXSysSlotGroup,
       "usdERXSysPortGroup": usdERXSysPortGroup,
       "usdERXSysPowerGroup": usdERXSysPowerGroup,
       "usdERXSysTemperatureGroup": usdERXSysTemperatureGroup,
       "usdERXSysSubsystemGroup": usdERXSysSubsystemGroup,
       "usdERXSysTimingGroup": usdERXSysTimingGroup,
       "usdERXSysGeneralGroup2": usdERXSysGeneralGroup2,
       "usdERXSysNotifyGroup2": usdERXSysNotifyGroup2,
       "usdERXSysTemperatureGroup2": usdERXSysTemperatureGroup2,
       "usdERXSysNotifyGroup3": usdERXSysNotifyGroup3}
)
