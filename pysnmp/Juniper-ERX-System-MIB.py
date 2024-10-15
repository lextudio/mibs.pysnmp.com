# SNMP MIB module (Juniper-ERX-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ERX-System-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:11 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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


# MODULE-IDENTITY

juniERXSysMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17)
)
juniERXSysMIB.setRevisions(
        ("2003-11-24 21:01",
         "2003-11-24 14:26",
         "2003-11-18 22:06",
         "2002-10-14 17:40",
         "2002-04-12 20:57",
         "2001-05-21 19:27",
         "2001-05-15 18:27",
         "2000-04-25 18:44",
         "2000-01-20 00:00",
         "1999-02-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniTimingSelector(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )



class JuniTimingSourceType(Integer32, TextualConvention):
    status = "deprecated"
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



class JuniTimingSourceLineType(Integer32, TextualConvention):
    status = "deprecated"
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



class JuniSysCardType(Integer32, TextualConvention):
    status = "deprecated"
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
              38)
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
          ("ge2", 38),
          ("geFe", 24),
          ("hssi", 23),
          ("hybrid", 35),
          ("oc12Atm", 12),
          ("oc12Pos", 11),
          ("oc12Server", 22),
          ("oc3", 3),
          ("oc3Atm", 14),
          ("oc3AtmGe", 36),
          ("oc3AtmPos", 37),
          ("oc3Pos", 13),
          ("oc3oc12Atm", 18),
          ("oc3oc12Pos", 17),
          ("oc48", 33),
          ("srp", 1),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("ue3f12", 28),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Atm4", 34),
          ("ut3Frame", 5),
          ("ut3f12", 27),
          ("v35", 26),
          ("vts", 32))
    )



# MIB Managed Objects in the order of their OIDs

_JuniERXSysTrap_ObjectIdentity = ObjectIdentity
juniERXSysTrap = _JuniERXSysTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0)
)
_JuniERXSysObjects_ObjectIdentity = ObjectIdentity
juniERXSysObjects = _JuniERXSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1)
)
_JuniERXSysGeneral_ObjectIdentity = ObjectIdentity
juniERXSysGeneral = _JuniERXSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1)
)


class _JuniERXSysChassisRev_Type(Integer32):
    """Custom type juniERXSysChassisRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysChassisRev_Type.__name__ = "Integer32"
_JuniERXSysChassisRev_Object = MibScalar
juniERXSysChassisRev = _JuniERXSysChassisRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 1),
    _JuniERXSysChassisRev_Type()
)
juniERXSysChassisRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysChassisRev.setStatus("deprecated")
_JuniERXSysSwVersion_Type = DisplayString
_JuniERXSysSwVersion_Object = MibScalar
juniERXSysSwVersion = _JuniERXSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 2),
    _JuniERXSysSwVersion_Type()
)
juniERXSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSwVersion.setStatus("deprecated")
_JuniERXSysSwBuildDate_Type = DisplayString
_JuniERXSysSwBuildDate_Object = MibScalar
juniERXSysSwBuildDate = _JuniERXSysSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 3),
    _JuniERXSysSwBuildDate_Type()
)
juniERXSysSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSwBuildDate.setStatus("deprecated")


class _JuniERXSysRevertControl_Type(Integer32):
    """Custom type juniERXSysRevertControl based on Integer32"""
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


_JuniERXSysRevertControl_Type.__name__ = "Integer32"
_JuniERXSysRevertControl_Object = MibScalar
juniERXSysRevertControl = _JuniERXSysRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 4),
    _JuniERXSysRevertControl_Type()
)
juniERXSysRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysRevertControl.setStatus("deprecated")


class _JuniERXSysRevertTimeOfDay_Type(Integer32):
    """Custom type juniERXSysRevertTimeOfDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_JuniERXSysRevertTimeOfDay_Type.__name__ = "Integer32"
_JuniERXSysRevertTimeOfDay_Object = MibScalar
juniERXSysRevertTimeOfDay = _JuniERXSysRevertTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 5),
    _JuniERXSysRevertTimeOfDay_Type()
)
juniERXSysRevertTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysRevertTimeOfDay.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysRevertTimeOfDay.setUnits("seconds")


class _JuniERXSysBootConfigControl_Type(Integer32):
    """Custom type juniERXSysBootConfigControl based on Integer32"""
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


_JuniERXSysBootConfigControl_Type.__name__ = "Integer32"
_JuniERXSysBootConfigControl_Object = MibScalar
juniERXSysBootConfigControl = _JuniERXSysBootConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 6),
    _JuniERXSysBootConfigControl_Type()
)
juniERXSysBootConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootConfigControl.setStatus("deprecated")


class _JuniERXSysBootBackupConfigControl_Type(Integer32):
    """Custom type juniERXSysBootBackupConfigControl based on Integer32"""
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


_JuniERXSysBootBackupConfigControl_Type.__name__ = "Integer32"
_JuniERXSysBootBackupConfigControl_Object = MibScalar
juniERXSysBootBackupConfigControl = _JuniERXSysBootBackupConfigControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 7),
    _JuniERXSysBootBackupConfigControl_Type()
)
juniERXSysBootBackupConfigControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootBackupConfigControl.setStatus("deprecated")


class _JuniERXSysBootForceBackupControl_Type(Integer32):
    """Custom type juniERXSysBootForceBackupControl based on Integer32"""
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


_JuniERXSysBootForceBackupControl_Type.__name__ = "Integer32"
_JuniERXSysBootForceBackupControl_Object = MibScalar
juniERXSysBootForceBackupControl = _JuniERXSysBootForceBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 8),
    _JuniERXSysBootForceBackupControl_Type()
)
juniERXSysBootForceBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootForceBackupControl.setStatus("deprecated")


class _JuniERXSysBootAutoRevertControl_Type(Integer32):
    """Custom type juniERXSysBootAutoRevertControl based on Integer32"""
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


_JuniERXSysBootAutoRevertControl_Type.__name__ = "Integer32"
_JuniERXSysBootAutoRevertControl_Object = MibScalar
juniERXSysBootAutoRevertControl = _JuniERXSysBootAutoRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 9),
    _JuniERXSysBootAutoRevertControl_Type()
)
juniERXSysBootAutoRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootAutoRevertControl.setStatus("deprecated")


class _JuniERXSysBootAutoRevertCountTolerance_Type(Unsigned32):
    """Custom type juniERXSysBootAutoRevertCountTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniERXSysBootAutoRevertCountTolerance_Type.__name__ = "Unsigned32"
_JuniERXSysBootAutoRevertCountTolerance_Object = MibScalar
juniERXSysBootAutoRevertCountTolerance = _JuniERXSysBootAutoRevertCountTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 10),
    _JuniERXSysBootAutoRevertCountTolerance_Type()
)
juniERXSysBootAutoRevertCountTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootAutoRevertCountTolerance.setStatus("deprecated")


class _JuniERXSysBootAutoRevertTimeTolerance_Type(Unsigned32):
    """Custom type juniERXSysBootAutoRevertTimeTolerance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniERXSysBootAutoRevertTimeTolerance_Type.__name__ = "Unsigned32"
_JuniERXSysBootAutoRevertTimeTolerance_Object = MibScalar
juniERXSysBootAutoRevertTimeTolerance = _JuniERXSysBootAutoRevertTimeTolerance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 11),
    _JuniERXSysBootAutoRevertTimeTolerance_Type()
)
juniERXSysBootAutoRevertTimeTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootAutoRevertTimeTolerance.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysBootAutoRevertTimeTolerance.setUnits("seconds")


class _JuniERXSysBootReleaseFile_Type(DisplayString):
    """Custom type juniERXSysBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysBootReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysBootReleaseFile_Object = MibScalar
juniERXSysBootReleaseFile = _JuniERXSysBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 12),
    _JuniERXSysBootReleaseFile_Type()
)
juniERXSysBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootReleaseFile.setStatus("deprecated")


class _JuniERXSysBootConfigFile_Type(DisplayString):
    """Custom type juniERXSysBootConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysBootConfigFile_Type.__name__ = "DisplayString"
_JuniERXSysBootConfigFile_Object = MibScalar
juniERXSysBootConfigFile = _JuniERXSysBootConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 13),
    _JuniERXSysBootConfigFile_Type()
)
juniERXSysBootConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootConfigFile.setStatus("deprecated")


class _JuniERXSysBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniERXSysBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysBootBackupReleaseFile_Object = MibScalar
juniERXSysBootBackupReleaseFile = _JuniERXSysBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 14),
    _JuniERXSysBootBackupReleaseFile_Type()
)
juniERXSysBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootBackupReleaseFile.setStatus("deprecated")


class _JuniERXSysBootBackupConfigFile_Type(DisplayString):
    """Custom type juniERXSysBootBackupConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysBootBackupConfigFile_Type.__name__ = "DisplayString"
_JuniERXSysBootBackupConfigFile_Object = MibScalar
juniERXSysBootBackupConfigFile = _JuniERXSysBootBackupConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 15),
    _JuniERXSysBootBackupConfigFile_Type()
)
juniERXSysBootBackupConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysBootBackupConfigFile.setStatus("deprecated")
_JuniERXSysAdminTimingSource_Type = JuniTimingSelector
_JuniERXSysAdminTimingSource_Object = MibScalar
juniERXSysAdminTimingSource = _JuniERXSysAdminTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 16),
    _JuniERXSysAdminTimingSource_Type()
)
juniERXSysAdminTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysAdminTimingSource.setStatus("deprecated")
_JuniERXSysOperTimingSource_Type = JuniTimingSelector
_JuniERXSysOperTimingSource_Object = MibScalar
juniERXSysOperTimingSource = _JuniERXSysOperTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 17),
    _JuniERXSysOperTimingSource_Type()
)
juniERXSysOperTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysOperTimingSource.setStatus("deprecated")


class _JuniERXSysTimingDisableAutoUpgrade_Type(TruthValue):
    """Custom type juniERXSysTimingDisableAutoUpgrade based on TruthValue"""


_JuniERXSysTimingDisableAutoUpgrade_Object = MibScalar
juniERXSysTimingDisableAutoUpgrade = _JuniERXSysTimingDisableAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 18),
    _JuniERXSysTimingDisableAutoUpgrade_Type()
)
juniERXSysTimingDisableAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysTimingDisableAutoUpgrade.setStatus("deprecated")
_JuniERXSysTimingSelectorTable_Object = MibTable
juniERXSysTimingSelectorTable = _JuniERXSysTimingSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19)
)
if mibBuilder.loadTexts:
    juniERXSysTimingSelectorTable.setStatus("deprecated")
_JuniERXSysTimingSelectorEntry_Object = MibTableRow
juniERXSysTimingSelectorEntry = _JuniERXSysTimingSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1)
)
juniERXSysTimingSelectorEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysTimingSelectorIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysTimingSelectorEntry.setStatus("deprecated")
_JuniERXSysTimingSelectorIndex_Type = JuniTimingSelector
_JuniERXSysTimingSelectorIndex_Object = MibTableColumn
juniERXSysTimingSelectorIndex = _JuniERXSysTimingSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 1),
    _JuniERXSysTimingSelectorIndex_Type()
)
juniERXSysTimingSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysTimingSelectorIndex.setStatus("deprecated")
_JuniERXSysTimingSourceType_Type = JuniTimingSourceType
_JuniERXSysTimingSourceType_Object = MibTableColumn
juniERXSysTimingSourceType = _JuniERXSysTimingSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 2),
    _JuniERXSysTimingSourceType_Type()
)
juniERXSysTimingSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysTimingSourceType.setStatus("deprecated")
_JuniERXSysTimingSourceIfIndex_Type = InterfaceIndexOrZero
_JuniERXSysTimingSourceIfIndex_Object = MibTableColumn
juniERXSysTimingSourceIfIndex = _JuniERXSysTimingSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 3),
    _JuniERXSysTimingSourceIfIndex_Type()
)
juniERXSysTimingSourceIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysTimingSourceIfIndex.setStatus("deprecated")


class _JuniERXSysTimingSourceLine_Type(JuniTimingSourceLineType):
    """Custom type juniERXSysTimingSourceLine based on JuniTimingSourceLineType"""


_JuniERXSysTimingSourceLine_Object = MibTableColumn
juniERXSysTimingSourceLine = _JuniERXSysTimingSourceLine_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 4),
    _JuniERXSysTimingSourceLine_Type()
)
juniERXSysTimingSourceLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysTimingSourceLine.setStatus("deprecated")


class _JuniERXSysTimingStatus_Type(Integer32):
    """Custom type juniERXSysTimingStatus based on Integer32"""
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


_JuniERXSysTimingStatus_Type.__name__ = "Integer32"
_JuniERXSysTimingStatus_Object = MibTableColumn
juniERXSysTimingStatus = _JuniERXSysTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 19, 1, 5),
    _JuniERXSysTimingStatus_Type()
)
juniERXSysTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTimingStatus.setStatus("deprecated")


class _JuniERXSysMemUtilPct_Type(Integer32):
    """Custom type juniERXSysMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniERXSysMemUtilPct_Type.__name__ = "Integer32"
_JuniERXSysMemUtilPct_Object = MibScalar
juniERXSysMemUtilPct = _JuniERXSysMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 20),
    _JuniERXSysMemUtilPct_Type()
)
juniERXSysMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysMemUtilPct.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysMemUtilPct.setUnits("percent")
_JuniERXSysMemCapacity_Type = Integer32
_JuniERXSysMemCapacity_Object = MibScalar
juniERXSysMemCapacity = _JuniERXSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 21),
    _JuniERXSysMemCapacity_Type()
)
juniERXSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysMemCapacity.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysMemCapacity.setUnits("bytes")


class _JuniERXSysHighMemUtilThreshold_Type(Integer32):
    """Custom type juniERXSysHighMemUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniERXSysHighMemUtilThreshold_Type.__name__ = "Integer32"
_JuniERXSysHighMemUtilThreshold_Object = MibScalar
juniERXSysHighMemUtilThreshold = _JuniERXSysHighMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 22),
    _JuniERXSysHighMemUtilThreshold_Type()
)
juniERXSysHighMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysHighMemUtilThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysHighMemUtilThreshold.setUnits("percent")


class _JuniERXSysAbatedMemUtilThreshold_Type(Integer32):
    """Custom type juniERXSysAbatedMemUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_JuniERXSysAbatedMemUtilThreshold_Type.__name__ = "Integer32"
_JuniERXSysAbatedMemUtilThreshold_Object = MibScalar
juniERXSysAbatedMemUtilThreshold = _JuniERXSysAbatedMemUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 23),
    _JuniERXSysAbatedMemUtilThreshold_Type()
)
juniERXSysAbatedMemUtilThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysAbatedMemUtilThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysAbatedMemUtilThreshold.setUnits("percent")


class _JuniERXSysMemUtilTrapEnable_Type(TruthValue):
    """Custom type juniERXSysMemUtilTrapEnable based on TruthValue"""


_JuniERXSysMemUtilTrapEnable_Object = MibScalar
juniERXSysMemUtilTrapEnable = _JuniERXSysMemUtilTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 24),
    _JuniERXSysMemUtilTrapEnable_Type()
)
juniERXSysMemUtilTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysMemUtilTrapEnable.setStatus("deprecated")


class _JuniERXSysGeneralTrapEnable_Type(TruthValue):
    """Custom type juniERXSysGeneralTrapEnable based on TruthValue"""


_JuniERXSysGeneralTrapEnable_Object = MibScalar
juniERXSysGeneralTrapEnable = _JuniERXSysGeneralTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 1, 25),
    _JuniERXSysGeneralTrapEnable_Type()
)
juniERXSysGeneralTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysGeneralTrapEnable.setStatus("deprecated")
_JuniERXSysFabric_ObjectIdentity = ObjectIdentity
juniERXSysFabric = _JuniERXSysFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2)
)
_JuniERXSysFabricSpeed_Type = Integer32
_JuniERXSysFabricSpeed_Object = MibScalar
juniERXSysFabricSpeed = _JuniERXSysFabricSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2, 1),
    _JuniERXSysFabricSpeed_Type()
)
juniERXSysFabricSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysFabricSpeed.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysFabricSpeed.setUnits("gigabits per second")


class _JuniERXSysFabricRev_Type(Integer32):
    """Custom type juniERXSysFabricRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysFabricRev_Type.__name__ = "Integer32"
_JuniERXSysFabricRev_Object = MibScalar
juniERXSysFabricRev = _JuniERXSysFabricRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 2, 2),
    _JuniERXSysFabricRev_Type()
)
juniERXSysFabricRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysFabricRev.setStatus("deprecated")
_JuniERXSysNvs_ObjectIdentity = ObjectIdentity
juniERXSysNvs = _JuniERXSysNvs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3)
)


class _JuniERXSysNvsStatus_Type(Integer32):
    """Custom type juniERXSysNvsStatus based on Integer32"""
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


_JuniERXSysNvsStatus_Type.__name__ = "Integer32"
_JuniERXSysNvsStatus_Object = MibScalar
juniERXSysNvsStatus = _JuniERXSysNvsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 1),
    _JuniERXSysNvsStatus_Type()
)
juniERXSysNvsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysNvsStatus.setStatus("deprecated")
_JuniERXSysNvsCapacity_Type = Integer32
_JuniERXSysNvsCapacity_Object = MibScalar
juniERXSysNvsCapacity = _JuniERXSysNvsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 2),
    _JuniERXSysNvsCapacity_Type()
)
juniERXSysNvsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysNvsCapacity.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysNvsCapacity.setUnits("megabytes")


class _JuniERXSysNvsUtilPct_Type(Integer32):
    """Custom type juniERXSysNvsUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniERXSysNvsUtilPct_Type.__name__ = "Integer32"
_JuniERXSysNvsUtilPct_Object = MibScalar
juniERXSysNvsUtilPct = _JuniERXSysNvsUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 3, 3),
    _JuniERXSysNvsUtilPct_Type()
)
juniERXSysNvsUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysNvsUtilPct.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysNvsUtilPct.setUnits("percent")
_JuniERXSysSlot_ObjectIdentity = ObjectIdentity
juniERXSysSlot = _JuniERXSysSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4)
)
_JuniERXSysSlotCount_Type = Integer32
_JuniERXSysSlotCount_Object = MibScalar
juniERXSysSlotCount = _JuniERXSysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 1),
    _JuniERXSysSlotCount_Type()
)
juniERXSysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotCount.setStatus("deprecated")
_JuniERXSysSlotTable_Object = MibTable
juniERXSysSlotTable = _JuniERXSysSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniERXSysSlotTable.setStatus("deprecated")
_JuniERXSysSlotEntry_Object = MibTableRow
juniERXSysSlotEntry = _JuniERXSysSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1)
)
juniERXSysSlotEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysSlotIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysSlotEntry.setStatus("deprecated")


class _JuniERXSysSlotIndex_Type(Integer32):
    """Custom type juniERXSysSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysSlotIndex_Type.__name__ = "Integer32"
_JuniERXSysSlotIndex_Object = MibTableColumn
juniERXSysSlotIndex = _JuniERXSysSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 1),
    _JuniERXSysSlotIndex_Type()
)
juniERXSysSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysSlotIndex.setStatus("deprecated")


class _JuniERXSysSlotDescr_Type(DisplayString):
    """Custom type juniERXSysSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniERXSysSlotDescr_Type.__name__ = "DisplayString"
_JuniERXSysSlotDescr_Object = MibTableColumn
juniERXSysSlotDescr = _JuniERXSysSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 2),
    _JuniERXSysSlotDescr_Type()
)
juniERXSysSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotDescr.setStatus("deprecated")
_JuniERXSysSlotCurrentCardType_Type = JuniSysCardType
_JuniERXSysSlotCurrentCardType_Object = MibTableColumn
juniERXSysSlotCurrentCardType = _JuniERXSysSlotCurrentCardType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 3),
    _JuniERXSysSlotCurrentCardType_Type()
)
juniERXSysSlotCurrentCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotCurrentCardType.setStatus("deprecated")


class _JuniERXSysSlotRev_Type(Integer32):
    """Custom type juniERXSysSlotRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysSlotRev_Type.__name__ = "Integer32"
_JuniERXSysSlotRev_Object = MibTableColumn
juniERXSysSlotRev = _JuniERXSysSlotRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 4),
    _JuniERXSysSlotRev_Type()
)
juniERXSysSlotRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotRev.setStatus("deprecated")
_JuniERXSysSlotAdminStatus_Type = JuniEnable
_JuniERXSysSlotAdminStatus_Object = MibTableColumn
juniERXSysSlotAdminStatus = _JuniERXSysSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 5),
    _JuniERXSysSlotAdminStatus_Type()
)
juniERXSysSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotAdminStatus.setStatus("deprecated")


class _JuniERXSysSlotOperStatus_Type(Integer32):
    """Custom type juniERXSysSlotOperStatus based on Integer32"""
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


_JuniERXSysSlotOperStatus_Type.__name__ = "Integer32"
_JuniERXSysSlotOperStatus_Object = MibTableColumn
juniERXSysSlotOperStatus = _JuniERXSysSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 6),
    _JuniERXSysSlotOperStatus_Type()
)
juniERXSysSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotOperStatus.setStatus("deprecated")


class _JuniERXSysSlotDisableReason_Type(Integer32):
    """Custom type juniERXSysSlotDisableReason based on Integer32"""
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


_JuniERXSysSlotDisableReason_Type.__name__ = "Integer32"
_JuniERXSysSlotDisableReason_Object = MibTableColumn
juniERXSysSlotDisableReason = _JuniERXSysSlotDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 7),
    _JuniERXSysSlotDisableReason_Type()
)
juniERXSysSlotDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotDisableReason.setStatus("deprecated")
_JuniERXSysSlotExpectedCardType_Type = JuniSysCardType
_JuniERXSysSlotExpectedCardType_Object = MibTableColumn
juniERXSysSlotExpectedCardType = _JuniERXSysSlotExpectedCardType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 8),
    _JuniERXSysSlotExpectedCardType_Type()
)
juniERXSysSlotExpectedCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotExpectedCardType.setStatus("deprecated")


class _JuniERXSysSlotControl_Type(Integer32):
    """Custom type juniERXSysSlotControl based on Integer32"""
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


_JuniERXSysSlotControl_Type.__name__ = "Integer32"
_JuniERXSysSlotControl_Object = MibTableColumn
juniERXSysSlotControl = _JuniERXSysSlotControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 9),
    _JuniERXSysSlotControl_Type()
)
juniERXSysSlotControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotControl.setStatus("deprecated")


class _JuniERXSysSlotCpuUtilPct_Type(Integer32):
    """Custom type juniERXSysSlotCpuUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniERXSysSlotCpuUtilPct_Type.__name__ = "Integer32"
_JuniERXSysSlotCpuUtilPct_Object = MibTableColumn
juniERXSysSlotCpuUtilPct = _JuniERXSysSlotCpuUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 10),
    _JuniERXSysSlotCpuUtilPct_Type()
)
juniERXSysSlotCpuUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotCpuUtilPct.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysSlotCpuUtilPct.setUnits("percent")


class _JuniERXSysSlotMemUtilPct_Type(Integer32):
    """Custom type juniERXSysSlotMemUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_JuniERXSysSlotMemUtilPct_Type.__name__ = "Integer32"
_JuniERXSysSlotMemUtilPct_Object = MibTableColumn
juniERXSysSlotMemUtilPct = _JuniERXSysSlotMemUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 11),
    _JuniERXSysSlotMemUtilPct_Type()
)
juniERXSysSlotMemUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotMemUtilPct.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysSlotMemUtilPct.setUnits("percent")
_JuniERXSysSlotIoaPresent_Type = TruthValue
_JuniERXSysSlotIoaPresent_Object = MibTableColumn
juniERXSysSlotIoaPresent = _JuniERXSysSlotIoaPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 12),
    _JuniERXSysSlotIoaPresent_Type()
)
juniERXSysSlotIoaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotIoaPresent.setStatus("deprecated")
_JuniERXSysSlotPortCount_Type = Integer32
_JuniERXSysSlotPortCount_Object = MibTableColumn
juniERXSysSlotPortCount = _JuniERXSysSlotPortCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 13),
    _JuniERXSysSlotPortCount_Type()
)
juniERXSysSlotPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotPortCount.setStatus("deprecated")
_JuniERXSysSlotLastChange_Type = TimeTicks
_JuniERXSysSlotLastChange_Object = MibTableColumn
juniERXSysSlotLastChange = _JuniERXSysSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 14),
    _JuniERXSysSlotLastChange_Type()
)
juniERXSysSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotLastChange.setStatus("deprecated")
_JuniERXSysSlotRedundancyLockout_Type = JuniEnable
_JuniERXSysSlotRedundancyLockout_Object = MibTableColumn
juniERXSysSlotRedundancyLockout = _JuniERXSysSlotRedundancyLockout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 15),
    _JuniERXSysSlotRedundancyLockout_Type()
)
juniERXSysSlotRedundancyLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotRedundancyLockout.setStatus("deprecated")
_JuniERXSysSlotRedundancyGroupId_Type = Unsigned32
_JuniERXSysSlotRedundancyGroupId_Object = MibTableColumn
juniERXSysSlotRedundancyGroupId = _JuniERXSysSlotRedundancyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 16),
    _JuniERXSysSlotRedundancyGroupId_Type()
)
juniERXSysSlotRedundancyGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotRedundancyGroupId.setStatus("deprecated")
_JuniERXSysSlotSpareServer_Type = TruthValue
_JuniERXSysSlotSpareServer_Object = MibTableColumn
juniERXSysSlotSpareServer = _JuniERXSysSlotSpareServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 17),
    _JuniERXSysSlotSpareServer_Type()
)
juniERXSysSlotSpareServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotSpareServer.setStatus("deprecated")
_JuniERXSysSlotAssociatedSlot_Type = Integer32
_JuniERXSysSlotAssociatedSlot_Object = MibTableColumn
juniERXSysSlotAssociatedSlot = _JuniERXSysSlotAssociatedSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 18),
    _JuniERXSysSlotAssociatedSlot_Type()
)
juniERXSysSlotAssociatedSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotAssociatedSlot.setStatus("deprecated")


class _JuniERXSysSlotRevertControl_Type(Integer32):
    """Custom type juniERXSysSlotRevertControl based on Integer32"""
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


_JuniERXSysSlotRevertControl_Type.__name__ = "Integer32"
_JuniERXSysSlotRevertControl_Object = MibTableColumn
juniERXSysSlotRevertControl = _JuniERXSysSlotRevertControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 19),
    _JuniERXSysSlotRevertControl_Type()
)
juniERXSysSlotRevertControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotRevertControl.setStatus("deprecated")
_JuniERXSysSlotRedundancyRevertTime_Type = DateAndTime
_JuniERXSysSlotRedundancyRevertTime_Object = MibTableColumn
juniERXSysSlotRedundancyRevertTime = _JuniERXSysSlotRedundancyRevertTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 20),
    _JuniERXSysSlotRedundancyRevertTime_Type()
)
juniERXSysSlotRedundancyRevertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotRedundancyRevertTime.setStatus("deprecated")


class _JuniERXSysSlotBootReleaseFile_Type(DisplayString):
    """Custom type juniERXSysSlotBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysSlotBootReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysSlotBootReleaseFile_Object = MibTableColumn
juniERXSysSlotBootReleaseFile = _JuniERXSysSlotBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 21),
    _JuniERXSysSlotBootReleaseFile_Type()
)
juniERXSysSlotBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotBootReleaseFile.setStatus("deprecated")


class _JuniERXSysSlotBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniERXSysSlotBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysSlotBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysSlotBootBackupReleaseFile_Object = MibTableColumn
juniERXSysSlotBootBackupReleaseFile = _JuniERXSysSlotBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 22),
    _JuniERXSysSlotBootBackupReleaseFile_Type()
)
juniERXSysSlotBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSlotBootBackupReleaseFile.setStatus("deprecated")


class _JuniERXSysSlotSerialNumber_Type(DisplayString):
    """Custom type juniERXSysSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniERXSysSlotSerialNumber_Type.__name__ = "DisplayString"
_JuniERXSysSlotSerialNumber_Object = MibTableColumn
juniERXSysSlotSerialNumber = _JuniERXSysSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 23),
    _JuniERXSysSlotSerialNumber_Type()
)
juniERXSysSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotSerialNumber.setStatus("deprecated")


class _JuniERXSysSlotAssemblyPartNumber_Type(DisplayString):
    """Custom type juniERXSysSlotAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniERXSysSlotAssemblyPartNumber_Type.__name__ = "DisplayString"
_JuniERXSysSlotAssemblyPartNumber_Object = MibTableColumn
juniERXSysSlotAssemblyPartNumber = _JuniERXSysSlotAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 24),
    _JuniERXSysSlotAssemblyPartNumber_Type()
)
juniERXSysSlotAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotAssemblyPartNumber.setStatus("deprecated")


class _JuniERXSysSlotAssemblyRev_Type(DisplayString):
    """Custom type juniERXSysSlotAssemblyRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_JuniERXSysSlotAssemblyRev_Type.__name__ = "DisplayString"
_JuniERXSysSlotAssemblyRev_Object = MibTableColumn
juniERXSysSlotAssemblyRev = _JuniERXSysSlotAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 25),
    _JuniERXSysSlotAssemblyRev_Type()
)
juniERXSysSlotAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotAssemblyRev.setStatus("deprecated")


class _JuniERXSysSlotIoaSerialNumber_Type(DisplayString):
    """Custom type juniERXSysSlotIoaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniERXSysSlotIoaSerialNumber_Type.__name__ = "DisplayString"
_JuniERXSysSlotIoaSerialNumber_Object = MibTableColumn
juniERXSysSlotIoaSerialNumber = _JuniERXSysSlotIoaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 26),
    _JuniERXSysSlotIoaSerialNumber_Type()
)
juniERXSysSlotIoaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotIoaSerialNumber.setStatus("deprecated")


class _JuniERXSysSlotIoaAssemblyPartNumber_Type(DisplayString):
    """Custom type juniERXSysSlotIoaAssemblyPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_JuniERXSysSlotIoaAssemblyPartNumber_Type.__name__ = "DisplayString"
_JuniERXSysSlotIoaAssemblyPartNumber_Object = MibTableColumn
juniERXSysSlotIoaAssemblyPartNumber = _JuniERXSysSlotIoaAssemblyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 27),
    _JuniERXSysSlotIoaAssemblyPartNumber_Type()
)
juniERXSysSlotIoaAssemblyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotIoaAssemblyPartNumber.setStatus("deprecated")


class _JuniERXSysSlotIoaAssemblyRev_Type(DisplayString):
    """Custom type juniERXSysSlotIoaAssemblyRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_JuniERXSysSlotIoaAssemblyRev_Type.__name__ = "DisplayString"
_JuniERXSysSlotIoaAssemblyRev_Object = MibTableColumn
juniERXSysSlotIoaAssemblyRev = _JuniERXSysSlotIoaAssemblyRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 4, 2, 1, 28),
    _JuniERXSysSlotIoaAssemblyRev_Type()
)
juniERXSysSlotIoaAssemblyRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSlotIoaAssemblyRev.setStatus("deprecated")
_JuniERXSysPort_ObjectIdentity = ObjectIdentity
juniERXSysPort = _JuniERXSysPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5)
)
_JuniERXSysPortTable_Object = MibTable
juniERXSysPortTable = _JuniERXSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniERXSysPortTable.setStatus("deprecated")
_JuniERXSysPortEntry_Object = MibTableRow
juniERXSysPortEntry = _JuniERXSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1)
)
juniERXSysPortEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysSlotIndex"),
    (0, "Juniper-ERX-System-MIB", "juniERXSysPortIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysPortEntry.setStatus("deprecated")


class _JuniERXSysPortIndex_Type(Integer32):
    """Custom type juniERXSysPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysPortIndex_Type.__name__ = "Integer32"
_JuniERXSysPortIndex_Object = MibTableColumn
juniERXSysPortIndex = _JuniERXSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 1),
    _JuniERXSysPortIndex_Type()
)
juniERXSysPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysPortIndex.setStatus("deprecated")


class _JuniERXSysPortDescr_Type(DisplayString):
    """Custom type juniERXSysPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniERXSysPortDescr_Type.__name__ = "DisplayString"
_JuniERXSysPortDescr_Object = MibTableColumn
juniERXSysPortDescr = _JuniERXSysPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 2),
    _JuniERXSysPortDescr_Type()
)
juniERXSysPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysPortDescr.setStatus("deprecated")


class _JuniERXSysPortType_Type(Integer32):
    """Custom type juniERXSysPortType based on Integer32"""
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
              19)
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
          ("oc12cAtm", 11),
          ("oc12cPos", 10),
          ("oc3c", 3),
          ("oc3cAtm", 13),
          ("oc3cPos", 12),
          ("oc48cPos", 19),
          ("server", 16),
          ("ue3Atm", 6),
          ("ue3Frame", 7),
          ("unknown", 0),
          ("ut3Atm", 4),
          ("ut3Frame", 5),
          ("v35", 18))
    )


_JuniERXSysPortType_Type.__name__ = "Integer32"
_JuniERXSysPortType_Object = MibTableColumn
juniERXSysPortType = _JuniERXSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 3),
    _JuniERXSysPortType_Type()
)
juniERXSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysPortType.setStatus("deprecated")
_JuniERXSysPortIfIndex_Type = InterfaceIndexOrZero
_JuniERXSysPortIfIndex_Object = MibTableColumn
juniERXSysPortIfIndex = _JuniERXSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 5, 1, 1, 4),
    _JuniERXSysPortIfIndex_Type()
)
juniERXSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysPortIfIndex.setStatus("deprecated")
_JuniERXSysPower_ObjectIdentity = ObjectIdentity
juniERXSysPower = _JuniERXSysPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6)
)
_JuniERXSysPowerTable_Object = MibTable
juniERXSysPowerTable = _JuniERXSysPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniERXSysPowerTable.setStatus("deprecated")
_JuniERXSysPowerEntry_Object = MibTableRow
juniERXSysPowerEntry = _JuniERXSysPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1)
)
juniERXSysPowerEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysPowerIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysPowerEntry.setStatus("deprecated")


class _JuniERXSysPowerIndex_Type(Integer32):
    """Custom type juniERXSysPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysPowerIndex_Type.__name__ = "Integer32"
_JuniERXSysPowerIndex_Object = MibTableColumn
juniERXSysPowerIndex = _JuniERXSysPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 1),
    _JuniERXSysPowerIndex_Type()
)
juniERXSysPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysPowerIndex.setStatus("deprecated")


class _JuniERXSysPowerDescr_Type(DisplayString):
    """Custom type juniERXSysPowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniERXSysPowerDescr_Type.__name__ = "DisplayString"
_JuniERXSysPowerDescr_Object = MibTableColumn
juniERXSysPowerDescr = _JuniERXSysPowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 2),
    _JuniERXSysPowerDescr_Type()
)
juniERXSysPowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysPowerDescr.setStatus("deprecated")


class _JuniERXSysPowerStatus_Type(Integer32):
    """Custom type juniERXSysPowerStatus based on Integer32"""
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


_JuniERXSysPowerStatus_Type.__name__ = "Integer32"
_JuniERXSysPowerStatus_Object = MibTableColumn
juniERXSysPowerStatus = _JuniERXSysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 6, 1, 1, 3),
    _JuniERXSysPowerStatus_Type()
)
juniERXSysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysPowerStatus.setStatus("deprecated")
_JuniERXSysTemperature_ObjectIdentity = ObjectIdentity
juniERXSysTemperature = _JuniERXSysTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7)
)


class _JuniERXSysTempFanStatus_Type(Integer32):
    """Custom type juniERXSysTempFanStatus based on Integer32"""
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


_JuniERXSysTempFanStatus_Type.__name__ = "Integer32"
_JuniERXSysTempFanStatus_Object = MibScalar
juniERXSysTempFanStatus = _JuniERXSysTempFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 1),
    _JuniERXSysTempFanStatus_Type()
)
juniERXSysTempFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempFanStatus.setStatus("deprecated")
_JuniERXSysTempTable_Object = MibTable
juniERXSysTempTable = _JuniERXSysTempTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniERXSysTempTable.setStatus("deprecated")
_JuniERXSysTempEntry_Object = MibTableRow
juniERXSysTempEntry = _JuniERXSysTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1)
)
juniERXSysTempEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysSlotIndex"),
    (0, "Juniper-ERX-System-MIB", "juniERXSysTempIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysTempEntry.setStatus("deprecated")


class _JuniERXSysTempIndex_Type(Integer32):
    """Custom type juniERXSysTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysTempIndex_Type.__name__ = "Integer32"
_JuniERXSysTempIndex_Object = MibTableColumn
juniERXSysTempIndex = _JuniERXSysTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 1),
    _JuniERXSysTempIndex_Type()
)
juniERXSysTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysTempIndex.setStatus("deprecated")


class _JuniERXSysTempDescr_Type(DisplayString):
    """Custom type juniERXSysTempDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JuniERXSysTempDescr_Type.__name__ = "DisplayString"
_JuniERXSysTempDescr_Object = MibTableColumn
juniERXSysTempDescr = _JuniERXSysTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 2),
    _JuniERXSysTempDescr_Type()
)
juniERXSysTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempDescr.setStatus("deprecated")


class _JuniERXSysTempStatus_Type(Integer32):
    """Custom type juniERXSysTempStatus based on Integer32"""
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


_JuniERXSysTempStatus_Type.__name__ = "Integer32"
_JuniERXSysTempStatus_Object = MibTableColumn
juniERXSysTempStatus = _JuniERXSysTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 3),
    _JuniERXSysTempStatus_Type()
)
juniERXSysTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempStatus.setStatus("deprecated")
_JuniERXSysTempValue_Type = Integer32
_JuniERXSysTempValue_Object = MibTableColumn
juniERXSysTempValue = _JuniERXSysTempValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 2, 1, 4),
    _JuniERXSysTempValue_Type()
)
juniERXSysTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempValue.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysTempValue.setUnits("degrees Celsius")


class _JuniERXSysTempProtectionStatus_Type(Integer32):
    """Custom type juniERXSysTempProtectionStatus based on Integer32"""
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


_JuniERXSysTempProtectionStatus_Type.__name__ = "Integer32"
_JuniERXSysTempProtectionStatus_Object = MibScalar
juniERXSysTempProtectionStatus = _JuniERXSysTempProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 3),
    _JuniERXSysTempProtectionStatus_Type()
)
juniERXSysTempProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempProtectionStatus.setStatus("deprecated")


class _JuniERXSysTempProtectionHoldOffTime_Type(Integer32):
    """Custom type juniERXSysTempProtectionHoldOffTime based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_JuniERXSysTempProtectionHoldOffTime_Type.__name__ = "Integer32"
_JuniERXSysTempProtectionHoldOffTime_Object = MibScalar
juniERXSysTempProtectionHoldOffTime = _JuniERXSysTempProtectionHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 4),
    _JuniERXSysTempProtectionHoldOffTime_Type()
)
juniERXSysTempProtectionHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempProtectionHoldOffTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysTempProtectionHoldOffTime.setUnits("seconds")


class _JuniERXSysTempProtectionHoldOffTimeRemaining_Type(Integer32):
    """Custom type juniERXSysTempProtectionHoldOffTimeRemaining based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_JuniERXSysTempProtectionHoldOffTimeRemaining_Type.__name__ = "Integer32"
_JuniERXSysTempProtectionHoldOffTimeRemaining_Object = MibScalar
juniERXSysTempProtectionHoldOffTimeRemaining = _JuniERXSysTempProtectionHoldOffTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 7, 5),
    _JuniERXSysTempProtectionHoldOffTimeRemaining_Type()
)
juniERXSysTempProtectionHoldOffTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysTempProtectionHoldOffTimeRemaining.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniERXSysTempProtectionHoldOffTimeRemaining.setUnits("seconds")
_JuniERXSysSubsystem_ObjectIdentity = ObjectIdentity
juniERXSysSubsystem = _JuniERXSysSubsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8)
)
_JuniERXSysSubsystemTable_Object = MibTable
juniERXSysSubsystemTable = _JuniERXSysSubsystemTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1)
)
if mibBuilder.loadTexts:
    juniERXSysSubsystemTable.setStatus("deprecated")
_JuniERXSysSubsystemEntry_Object = MibTableRow
juniERXSysSubsystemEntry = _JuniERXSysSubsystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1)
)
juniERXSysSubsystemEntry.setIndexNames(
    (0, "Juniper-ERX-System-MIB", "juniERXSysSubsystemIndex"),
)
if mibBuilder.loadTexts:
    juniERXSysSubsystemEntry.setStatus("deprecated")


class _JuniERXSysSubsystemIndex_Type(Integer32):
    """Custom type juniERXSysSubsystemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniERXSysSubsystemIndex_Type.__name__ = "Integer32"
_JuniERXSysSubsystemIndex_Object = MibTableColumn
juniERXSysSubsystemIndex = _JuniERXSysSubsystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 1),
    _JuniERXSysSubsystemIndex_Type()
)
juniERXSysSubsystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniERXSysSubsystemIndex.setStatus("deprecated")


class _JuniERXSysSubsystemName_Type(DisplayString):
    """Custom type juniERXSysSubsystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysSubsystemName_Type.__name__ = "DisplayString"
_JuniERXSysSubsystemName_Object = MibTableColumn
juniERXSysSubsystemName = _JuniERXSysSubsystemName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 2),
    _JuniERXSysSubsystemName_Type()
)
juniERXSysSubsystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniERXSysSubsystemName.setStatus("deprecated")


class _JuniERXSysSubsystemControl_Type(Integer32):
    """Custom type juniERXSysSubsystemControl based on Integer32"""
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


_JuniERXSysSubsystemControl_Type.__name__ = "Integer32"
_JuniERXSysSubsystemControl_Object = MibTableColumn
juniERXSysSubsystemControl = _JuniERXSysSubsystemControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 3),
    _JuniERXSysSubsystemControl_Type()
)
juniERXSysSubsystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSubsystemControl.setStatus("deprecated")


class _JuniERXSysSubsystemBootReleaseFile_Type(DisplayString):
    """Custom type juniERXSysSubsystemBootReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysSubsystemBootReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysSubsystemBootReleaseFile_Object = MibTableColumn
juniERXSysSubsystemBootReleaseFile = _JuniERXSysSubsystemBootReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 4),
    _JuniERXSysSubsystemBootReleaseFile_Type()
)
juniERXSysSubsystemBootReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSubsystemBootReleaseFile.setStatus("deprecated")


class _JuniERXSysSubsystemBootBackupReleaseFile_Type(DisplayString):
    """Custom type juniERXSysSubsystemBootBackupReleaseFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JuniERXSysSubsystemBootBackupReleaseFile_Type.__name__ = "DisplayString"
_JuniERXSysSubsystemBootBackupReleaseFile_Object = MibTableColumn
juniERXSysSubsystemBootBackupReleaseFile = _JuniERXSysSubsystemBootBackupReleaseFile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 1, 8, 1, 1, 5),
    _JuniERXSysSubsystemBootBackupReleaseFile_Type()
)
juniERXSysSubsystemBootBackupReleaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniERXSysSubsystemBootBackupReleaseFile.setStatus("deprecated")
_JuniERXSysConformance_ObjectIdentity = ObjectIdentity
juniERXSysConformance = _JuniERXSysConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2)
)
_JuniERXSysCompliances_ObjectIdentity = ObjectIdentity
juniERXSysCompliances = _JuniERXSysCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1)
)
_JuniERXSysGroups_ObjectIdentity = ObjectIdentity
juniERXSysGroups = _JuniERXSysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2)
)

# Managed Objects groups

juniERXSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 1)
)
juniERXSysGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysChassisRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwVersion"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwBuildDate"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertTimeOfDay"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootForceBackupControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertCountTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertTimeTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysFabricSpeed"),
        ("Juniper-ERX-System-MIB", "juniERXSysFabricRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysNvsStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysNvsCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysNvsUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotCount"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotCurrentCardType"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAdminStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDisableReason"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotExpectedCardType"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotCpuUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotIoaPresent"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotPortCount"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotLastChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyLockout"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyGroupId"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotSpareServer"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAssociatedSlot"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyRevertTime"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysPortDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysPortType"),
        ("Juniper-ERX-System-MIB", "juniERXSysPortIfIndex"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempFanStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempValue"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemName"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemBootBackupReleaseFile"))
)
if mibBuilder.loadTexts:
    juniERXSysGroup.setStatus("obsolete")

juniERXSysGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 3)
)
juniERXSysGeneralGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysChassisRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwVersion"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwBuildDate"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertTimeOfDay"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootForceBackupControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertCountTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertTimeTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigFile"))
)
if mibBuilder.loadTexts:
    juniERXSysGeneralGroup.setStatus("obsolete")

juniERXSysFabricGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 4)
)
juniERXSysFabricGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysFabricSpeed"),
        ("Juniper-ERX-System-MIB", "juniERXSysFabricRev"))
)
if mibBuilder.loadTexts:
    juniERXSysFabricGroup.setStatus("deprecated")

juniERXSysNvsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 5)
)
juniERXSysNvsGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysNvsStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysNvsCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysNvsUtilPct"))
)
if mibBuilder.loadTexts:
    juniERXSysNvsGroup.setStatus("deprecated")

juniERXSysSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 6)
)
juniERXSysSlotGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSlotCount"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotCurrentCardType"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAdminStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDisableReason"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotExpectedCardType"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotCpuUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotIoaPresent"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotPortCount"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotLastChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyLockout"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyGroupId"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotSpareServer"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAssociatedSlot"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotRedundancyRevertTime"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotSerialNumber"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAssemblyPartNumber"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAssemblyRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotIoaSerialNumber"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotIoaAssemblyPartNumber"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotIoaAssemblyRev"))
)
if mibBuilder.loadTexts:
    juniERXSysSlotGroup.setStatus("deprecated")

juniERXSysPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 7)
)
juniERXSysPortGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysPortDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysPortType"),
        ("Juniper-ERX-System-MIB", "juniERXSysPortIfIndex"))
)
if mibBuilder.loadTexts:
    juniERXSysPortGroup.setStatus("deprecated")

juniERXSysPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 8)
)
juniERXSysPowerGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysPowerDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerStatus"))
)
if mibBuilder.loadTexts:
    juniERXSysPowerGroup.setStatus("deprecated")

juniERXSysTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 9)
)
juniERXSysTemperatureGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysTempFanStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempValue"))
)
if mibBuilder.loadTexts:
    juniERXSysTemperatureGroup.setStatus("obsolete")

juniERXSysSubsystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 10)
)
juniERXSysSubsystemGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSubsystemName"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysSubsystemBootBackupReleaseFile"))
)
if mibBuilder.loadTexts:
    juniERXSysSubsystemGroup.setStatus("deprecated")

juniERXSysTimingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 11)
)
juniERXSysTimingGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysAdminTimingSource"),
        ("Juniper-ERX-System-MIB", "juniERXSysOperTimingSource"),
        ("Juniper-ERX-System-MIB", "juniERXSysTimingDisableAutoUpgrade"),
        ("Juniper-ERX-System-MIB", "juniERXSysTimingSourceType"),
        ("Juniper-ERX-System-MIB", "juniERXSysTimingSourceIfIndex"),
        ("Juniper-ERX-System-MIB", "juniERXSysTimingSourceLine"),
        ("Juniper-ERX-System-MIB", "juniERXSysTimingStatus"))
)
if mibBuilder.loadTexts:
    juniERXSysTimingGroup.setStatus("deprecated")

juniERXSysGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 12)
)
juniERXSysGeneralGroup2.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysChassisRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwVersion"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwBuildDate"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertTimeOfDay"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootForceBackupControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertCountTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertTimeTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilTrapEnable"))
)
if mibBuilder.loadTexts:
    juniERXSysGeneralGroup2.setStatus("obsolete")

juniERXSysTemperatureGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 14)
)
juniERXSysTemperatureGroup2.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysTempFanStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempDescr"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempValue"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempProtectionStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempProtectionHoldOffTime"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    juniERXSysTemperatureGroup2.setStatus("deprecated")

juniERXSysGeneralGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 16)
)
juniERXSysGeneralGroup3.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysChassisRev"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwVersion"),
        ("Juniper-ERX-System-MIB", "juniERXSysSwBuildDate"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysRevertTimeOfDay"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootForceBackupControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertControl"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertCountTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootAutoRevertTimeTolerance"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupReleaseFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysBootBackupConfigFile"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilTrapEnable"),
        ("Juniper-ERX-System-MIB", "juniERXSysGeneralTrapEnable"))
)
if mibBuilder.loadTexts:
    juniERXSysGeneralGroup3.setStatus("deprecated")


# Notification objects

juniERXSysSlotOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 1)
)
juniERXSysSlotOperStatusChange.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSlotCurrentCardType"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAdminStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDisableReason"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotSpareServer"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotAssociatedSlot"),
        ("Juniper-ERX-System-MIB", "juniERXSysSlotDescr"))
)
if mibBuilder.loadTexts:
    juniERXSysSlotOperStatusChange.setStatus(
        "deprecated"
    )

juniERXSysPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 2)
)
juniERXSysPowerStatusChange.setObjects(
    ("Juniper-ERX-System-MIB", "juniERXSysPowerStatus")
)
if mibBuilder.loadTexts:
    juniERXSysPowerStatusChange.setStatus(
        "deprecated"
    )

juniERXSysTempFanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 3)
)
juniERXSysTempFanStatusChange.setObjects(
    ("Juniper-ERX-System-MIB", "juniERXSysTempFanStatus")
)
if mibBuilder.loadTexts:
    juniERXSysTempFanStatusChange.setStatus(
        "deprecated"
    )

juniERXSysTempStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 4)
)
juniERXSysTempStatusChange.setObjects(
    ("Juniper-ERX-System-MIB", "juniERXSysTempStatus")
)
if mibBuilder.loadTexts:
    juniERXSysTempStatusChange.setStatus(
        "deprecated"
    )

juniERXSysHighMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 5)
)
juniERXSysHighMemUtil.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysMemCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtilThreshold"))
)
if mibBuilder.loadTexts:
    juniERXSysHighMemUtil.setStatus(
        "deprecated"
    )

juniERXSysAbatedMemUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 6)
)
juniERXSysAbatedMemUtil.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysMemCapacity"),
        ("Juniper-ERX-System-MIB", "juniERXSysMemUtilPct"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtilThreshold"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtilThreshold"))
)
if mibBuilder.loadTexts:
    juniERXSysAbatedMemUtil.setStatus(
        "deprecated"
    )

juniERXSysTempProtectionStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 0, 7)
)
juniERXSysTempProtectionStatusChange.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysTempProtectionStatus"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempProtectionHoldOffTimeRemaining"))
)
if mibBuilder.loadTexts:
    juniERXSysTempProtectionStatusChange.setStatus(
        "deprecated"
    )


# Notifications groups

juniERXSysNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 2)
)
juniERXSysNotifyGroup.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempFanStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatusChange"))
)
if mibBuilder.loadTexts:
    juniERXSysNotifyGroup.setStatus(
        "obsolete"
    )

juniERXSysNotifyGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 13)
)
juniERXSysNotifyGroup2.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempFanStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtil"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtil"))
)
if mibBuilder.loadTexts:
    juniERXSysNotifyGroup2.setStatus(
        "obsolete"
    )

juniERXSysNotifyGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 2, 15)
)
juniERXSysNotifyGroup3.setObjects(
      *(("Juniper-ERX-System-MIB", "juniERXSysSlotOperStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysPowerStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempFanStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempStatusChange"),
        ("Juniper-ERX-System-MIB", "juniERXSysHighMemUtil"),
        ("Juniper-ERX-System-MIB", "juniERXSysAbatedMemUtil"),
        ("Juniper-ERX-System-MIB", "juniERXSysTempProtectionStatusChange"))
)
if mibBuilder.loadTexts:
    juniERXSysNotifyGroup3.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

juniERXSysCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance.setStatus(
        "obsolete"
    )

juniERXSysCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance1.setStatus(
        "obsolete"
    )

juniERXSysCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance2.setStatus(
        "obsolete"
    )

juniERXSysCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance3.setStatus(
        "obsolete"
    )

juniERXSysCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance4.setStatus(
        "obsolete"
    )

juniERXSysCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 17, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniERXSysCompliance5.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ERX-System-MIB",
    **{"JuniTimingSelector": JuniTimingSelector,
       "JuniTimingSourceType": JuniTimingSourceType,
       "JuniTimingSourceLineType": JuniTimingSourceLineType,
       "JuniSysCardType": JuniSysCardType,
       "juniERXSysMIB": juniERXSysMIB,
       "juniERXSysTrap": juniERXSysTrap,
       "juniERXSysSlotOperStatusChange": juniERXSysSlotOperStatusChange,
       "juniERXSysPowerStatusChange": juniERXSysPowerStatusChange,
       "juniERXSysTempFanStatusChange": juniERXSysTempFanStatusChange,
       "juniERXSysTempStatusChange": juniERXSysTempStatusChange,
       "juniERXSysHighMemUtil": juniERXSysHighMemUtil,
       "juniERXSysAbatedMemUtil": juniERXSysAbatedMemUtil,
       "juniERXSysTempProtectionStatusChange": juniERXSysTempProtectionStatusChange,
       "juniERXSysObjects": juniERXSysObjects,
       "juniERXSysGeneral": juniERXSysGeneral,
       "juniERXSysChassisRev": juniERXSysChassisRev,
       "juniERXSysSwVersion": juniERXSysSwVersion,
       "juniERXSysSwBuildDate": juniERXSysSwBuildDate,
       "juniERXSysRevertControl": juniERXSysRevertControl,
       "juniERXSysRevertTimeOfDay": juniERXSysRevertTimeOfDay,
       "juniERXSysBootConfigControl": juniERXSysBootConfigControl,
       "juniERXSysBootBackupConfigControl": juniERXSysBootBackupConfigControl,
       "juniERXSysBootForceBackupControl": juniERXSysBootForceBackupControl,
       "juniERXSysBootAutoRevertControl": juniERXSysBootAutoRevertControl,
       "juniERXSysBootAutoRevertCountTolerance": juniERXSysBootAutoRevertCountTolerance,
       "juniERXSysBootAutoRevertTimeTolerance": juniERXSysBootAutoRevertTimeTolerance,
       "juniERXSysBootReleaseFile": juniERXSysBootReleaseFile,
       "juniERXSysBootConfigFile": juniERXSysBootConfigFile,
       "juniERXSysBootBackupReleaseFile": juniERXSysBootBackupReleaseFile,
       "juniERXSysBootBackupConfigFile": juniERXSysBootBackupConfigFile,
       "juniERXSysAdminTimingSource": juniERXSysAdminTimingSource,
       "juniERXSysOperTimingSource": juniERXSysOperTimingSource,
       "juniERXSysTimingDisableAutoUpgrade": juniERXSysTimingDisableAutoUpgrade,
       "juniERXSysTimingSelectorTable": juniERXSysTimingSelectorTable,
       "juniERXSysTimingSelectorEntry": juniERXSysTimingSelectorEntry,
       "juniERXSysTimingSelectorIndex": juniERXSysTimingSelectorIndex,
       "juniERXSysTimingSourceType": juniERXSysTimingSourceType,
       "juniERXSysTimingSourceIfIndex": juniERXSysTimingSourceIfIndex,
       "juniERXSysTimingSourceLine": juniERXSysTimingSourceLine,
       "juniERXSysTimingStatus": juniERXSysTimingStatus,
       "juniERXSysMemUtilPct": juniERXSysMemUtilPct,
       "juniERXSysMemCapacity": juniERXSysMemCapacity,
       "juniERXSysHighMemUtilThreshold": juniERXSysHighMemUtilThreshold,
       "juniERXSysAbatedMemUtilThreshold": juniERXSysAbatedMemUtilThreshold,
       "juniERXSysMemUtilTrapEnable": juniERXSysMemUtilTrapEnable,
       "juniERXSysGeneralTrapEnable": juniERXSysGeneralTrapEnable,
       "juniERXSysFabric": juniERXSysFabric,
       "juniERXSysFabricSpeed": juniERXSysFabricSpeed,
       "juniERXSysFabricRev": juniERXSysFabricRev,
       "juniERXSysNvs": juniERXSysNvs,
       "juniERXSysNvsStatus": juniERXSysNvsStatus,
       "juniERXSysNvsCapacity": juniERXSysNvsCapacity,
       "juniERXSysNvsUtilPct": juniERXSysNvsUtilPct,
       "juniERXSysSlot": juniERXSysSlot,
       "juniERXSysSlotCount": juniERXSysSlotCount,
       "juniERXSysSlotTable": juniERXSysSlotTable,
       "juniERXSysSlotEntry": juniERXSysSlotEntry,
       "juniERXSysSlotIndex": juniERXSysSlotIndex,
       "juniERXSysSlotDescr": juniERXSysSlotDescr,
       "juniERXSysSlotCurrentCardType": juniERXSysSlotCurrentCardType,
       "juniERXSysSlotRev": juniERXSysSlotRev,
       "juniERXSysSlotAdminStatus": juniERXSysSlotAdminStatus,
       "juniERXSysSlotOperStatus": juniERXSysSlotOperStatus,
       "juniERXSysSlotDisableReason": juniERXSysSlotDisableReason,
       "juniERXSysSlotExpectedCardType": juniERXSysSlotExpectedCardType,
       "juniERXSysSlotControl": juniERXSysSlotControl,
       "juniERXSysSlotCpuUtilPct": juniERXSysSlotCpuUtilPct,
       "juniERXSysSlotMemUtilPct": juniERXSysSlotMemUtilPct,
       "juniERXSysSlotIoaPresent": juniERXSysSlotIoaPresent,
       "juniERXSysSlotPortCount": juniERXSysSlotPortCount,
       "juniERXSysSlotLastChange": juniERXSysSlotLastChange,
       "juniERXSysSlotRedundancyLockout": juniERXSysSlotRedundancyLockout,
       "juniERXSysSlotRedundancyGroupId": juniERXSysSlotRedundancyGroupId,
       "juniERXSysSlotSpareServer": juniERXSysSlotSpareServer,
       "juniERXSysSlotAssociatedSlot": juniERXSysSlotAssociatedSlot,
       "juniERXSysSlotRevertControl": juniERXSysSlotRevertControl,
       "juniERXSysSlotRedundancyRevertTime": juniERXSysSlotRedundancyRevertTime,
       "juniERXSysSlotBootReleaseFile": juniERXSysSlotBootReleaseFile,
       "juniERXSysSlotBootBackupReleaseFile": juniERXSysSlotBootBackupReleaseFile,
       "juniERXSysSlotSerialNumber": juniERXSysSlotSerialNumber,
       "juniERXSysSlotAssemblyPartNumber": juniERXSysSlotAssemblyPartNumber,
       "juniERXSysSlotAssemblyRev": juniERXSysSlotAssemblyRev,
       "juniERXSysSlotIoaSerialNumber": juniERXSysSlotIoaSerialNumber,
       "juniERXSysSlotIoaAssemblyPartNumber": juniERXSysSlotIoaAssemblyPartNumber,
       "juniERXSysSlotIoaAssemblyRev": juniERXSysSlotIoaAssemblyRev,
       "juniERXSysPort": juniERXSysPort,
       "juniERXSysPortTable": juniERXSysPortTable,
       "juniERXSysPortEntry": juniERXSysPortEntry,
       "juniERXSysPortIndex": juniERXSysPortIndex,
       "juniERXSysPortDescr": juniERXSysPortDescr,
       "juniERXSysPortType": juniERXSysPortType,
       "juniERXSysPortIfIndex": juniERXSysPortIfIndex,
       "juniERXSysPower": juniERXSysPower,
       "juniERXSysPowerTable": juniERXSysPowerTable,
       "juniERXSysPowerEntry": juniERXSysPowerEntry,
       "juniERXSysPowerIndex": juniERXSysPowerIndex,
       "juniERXSysPowerDescr": juniERXSysPowerDescr,
       "juniERXSysPowerStatus": juniERXSysPowerStatus,
       "juniERXSysTemperature": juniERXSysTemperature,
       "juniERXSysTempFanStatus": juniERXSysTempFanStatus,
       "juniERXSysTempTable": juniERXSysTempTable,
       "juniERXSysTempEntry": juniERXSysTempEntry,
       "juniERXSysTempIndex": juniERXSysTempIndex,
       "juniERXSysTempDescr": juniERXSysTempDescr,
       "juniERXSysTempStatus": juniERXSysTempStatus,
       "juniERXSysTempValue": juniERXSysTempValue,
       "juniERXSysTempProtectionStatus": juniERXSysTempProtectionStatus,
       "juniERXSysTempProtectionHoldOffTime": juniERXSysTempProtectionHoldOffTime,
       "juniERXSysTempProtectionHoldOffTimeRemaining": juniERXSysTempProtectionHoldOffTimeRemaining,
       "juniERXSysSubsystem": juniERXSysSubsystem,
       "juniERXSysSubsystemTable": juniERXSysSubsystemTable,
       "juniERXSysSubsystemEntry": juniERXSysSubsystemEntry,
       "juniERXSysSubsystemIndex": juniERXSysSubsystemIndex,
       "juniERXSysSubsystemName": juniERXSysSubsystemName,
       "juniERXSysSubsystemControl": juniERXSysSubsystemControl,
       "juniERXSysSubsystemBootReleaseFile": juniERXSysSubsystemBootReleaseFile,
       "juniERXSysSubsystemBootBackupReleaseFile": juniERXSysSubsystemBootBackupReleaseFile,
       "juniERXSysConformance": juniERXSysConformance,
       "juniERXSysCompliances": juniERXSysCompliances,
       "juniERXSysCompliance": juniERXSysCompliance,
       "juniERXSysCompliance1": juniERXSysCompliance1,
       "juniERXSysCompliance2": juniERXSysCompliance2,
       "juniERXSysCompliance3": juniERXSysCompliance3,
       "juniERXSysCompliance4": juniERXSysCompliance4,
       "juniERXSysCompliance5": juniERXSysCompliance5,
       "juniERXSysGroups": juniERXSysGroups,
       "juniERXSysGroup": juniERXSysGroup,
       "juniERXSysNotifyGroup": juniERXSysNotifyGroup,
       "juniERXSysGeneralGroup": juniERXSysGeneralGroup,
       "juniERXSysFabricGroup": juniERXSysFabricGroup,
       "juniERXSysNvsGroup": juniERXSysNvsGroup,
       "juniERXSysSlotGroup": juniERXSysSlotGroup,
       "juniERXSysPortGroup": juniERXSysPortGroup,
       "juniERXSysPowerGroup": juniERXSysPowerGroup,
       "juniERXSysTemperatureGroup": juniERXSysTemperatureGroup,
       "juniERXSysSubsystemGroup": juniERXSysSubsystemGroup,
       "juniERXSysTimingGroup": juniERXSysTimingGroup,
       "juniERXSysGeneralGroup2": juniERXSysGeneralGroup2,
       "juniERXSysNotifyGroup2": juniERXSysNotifyGroup2,
       "juniERXSysTemperatureGroup2": juniERXSysTemperatureGroup2,
       "juniERXSysNotifyGroup3": juniERXSysNotifyGroup3,
       "juniERXSysGeneralGroup3": juniERXSysGeneralGroup3}
)
