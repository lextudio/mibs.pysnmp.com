# SNMP MIB module (GDCMP7002-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCMP7002-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:18 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Dsx1_ObjectIdentity = ObjectIdentity
dsx1 = _Dsx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6)
)
_Mp7002System_ObjectIdentity = ObjectIdentity
mp7002System = _Mp7002System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6)
)
_Mp7002Version_ObjectIdentity = ObjectIdentity
mp7002Version = _Mp7002Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1)
)


class _Mp7002MIBversion_Type(DisplayString):
    """Custom type mp7002MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Mp7002MIBversion_Type.__name__ = "DisplayString"
_Mp7002MIBversion_Object = MibScalar
mp7002MIBversion = _Mp7002MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 1),
    _Mp7002MIBversion_Type()
)
mp7002MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002MIBversion.setStatus("mandatory")
_Mp7002VersionTable_Object = MibTable
mp7002VersionTable = _Mp7002VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    mp7002VersionTable.setStatus("mandatory")
_Mp7002VersionEntry_Object = MibTableRow
mp7002VersionEntry = _Mp7002VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2, 1)
)
mp7002VersionEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002VersionIndex"),
)
if mibBuilder.loadTexts:
    mp7002VersionEntry.setStatus("mandatory")
_Mp7002VersionIndex_Type = SCinstance
_Mp7002VersionIndex_Object = MibTableColumn
mp7002VersionIndex = _Mp7002VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2, 1, 1),
    _Mp7002VersionIndex_Type()
)
mp7002VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002VersionIndex.setStatus("mandatory")


class _Mp7002FirmwareRev_Type(DisplayString):
    """Custom type mp7002FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Mp7002FirmwareRev_Type.__name__ = "DisplayString"
_Mp7002FirmwareRev_Object = MibTableColumn
mp7002FirmwareRev = _Mp7002FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2, 1, 2),
    _Mp7002FirmwareRev_Type()
)
mp7002FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FirmwareRev.setStatus("mandatory")


class _Mp7002ModelNumber_Type(DisplayString):
    """Custom type mp7002ModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Mp7002ModelNumber_Type.__name__ = "DisplayString"
_Mp7002ModelNumber_Object = MibTableColumn
mp7002ModelNumber = _Mp7002ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2, 1, 3),
    _Mp7002ModelNumber_Type()
)
mp7002ModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002ModelNumber.setStatus("mandatory")


class _Mp7002E1x_Type(Integer32):
    """Custom type mp7002E1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notPresent", 2))
    )


_Mp7002E1x_Type.__name__ = "Integer32"
_Mp7002E1x_Object = MibTableColumn
mp7002E1x = _Mp7002E1x_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 1, 2, 1, 4),
    _Mp7002E1x_Type()
)
mp7002E1x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002E1x.setStatus("mandatory")
_Mp7002Maintenance_ObjectIdentity = ObjectIdentity
mp7002Maintenance = _Mp7002Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2)
)
_Mp7002MaintenanceTable_Object = MibTable
mp7002MaintenanceTable = _Mp7002MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mp7002MaintenanceTable.setStatus("mandatory")
_Mp7002MaintenanceEntry_Object = MibTableRow
mp7002MaintenanceEntry = _Mp7002MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1)
)
mp7002MaintenanceEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    mp7002MaintenanceEntry.setStatus("mandatory")
_Mp7002MaintenanceLineIndex_Type = SCinstance
_Mp7002MaintenanceLineIndex_Object = MibTableColumn
mp7002MaintenanceLineIndex = _Mp7002MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 1),
    _Mp7002MaintenanceLineIndex_Type()
)
mp7002MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002MaintenanceLineIndex.setStatus("mandatory")


class _Mp7002SoftReset_Type(Integer32):
    """Custom type mp7002SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Mp7002SoftReset_Type.__name__ = "Integer32"
_Mp7002SoftReset_Object = MibTableColumn
mp7002SoftReset = _Mp7002SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 2),
    _Mp7002SoftReset_Type()
)
mp7002SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002SoftReset.setStatus("mandatory")


class _Mp7002SysUpTime_Type(Integer32):
    """Custom type mp7002SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002SysUpTime_Type.__name__ = "Integer32"
_Mp7002SysUpTime_Object = MibTableColumn
mp7002SysUpTime = _Mp7002SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 3),
    _Mp7002SysUpTime_Type()
)
mp7002SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002SysUpTime.setStatus("mandatory")


class _Mp7002DefaultInit_Type(Integer32):
    """Custom type mp7002DefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 2),
          ("normal", 1))
    )


_Mp7002DefaultInit_Type.__name__ = "Integer32"
_Mp7002DefaultInit_Object = MibTableColumn
mp7002DefaultInit = _Mp7002DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 4),
    _Mp7002DefaultInit_Type()
)
mp7002DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002DefaultInit.setStatus("mandatory")


class _Mp7002ResetStats_Type(Integer32):
    """Custom type mp7002ResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Mp7002ResetStats_Type.__name__ = "Integer32"
_Mp7002ResetStats_Object = MibTableColumn
mp7002ResetStats = _Mp7002ResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 5),
    _Mp7002ResetStats_Type()
)
mp7002ResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002ResetStats.setStatus("mandatory")


class _Mp7002LedStatus_Type(OctetString):
    """Custom type mp7002LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Mp7002LedStatus_Type.__name__ = "OctetString"
_Mp7002LedStatus_Object = MibTableColumn
mp7002LedStatus = _Mp7002LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 6),
    _Mp7002LedStatus_Type()
)
mp7002LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002LedStatus.setStatus("mandatory")


class _Mp7002E1Circuit_Type(DisplayString):
    """Custom type mp7002E1Circuit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7002E1Circuit_Type.__name__ = "DisplayString"
_Mp7002E1Circuit_Object = MibTableColumn
mp7002E1Circuit = _Mp7002E1Circuit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 7),
    _Mp7002E1Circuit_Type()
)
mp7002E1Circuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002E1Circuit.setStatus("mandatory")


class _Mp7002E1XCircuit_Type(DisplayString):
    """Custom type mp7002E1XCircuit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7002E1XCircuit_Type.__name__ = "DisplayString"
_Mp7002E1XCircuit_Object = MibTableColumn
mp7002E1XCircuit = _Mp7002E1XCircuit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 8),
    _Mp7002E1XCircuit_Type()
)
mp7002E1XCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002E1XCircuit.setStatus("mandatory")


class _Mp7002TSBundle1Name_Type(DisplayString):
    """Custom type mp7002TSBundle1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7002TSBundle1Name_Type.__name__ = "DisplayString"
_Mp7002TSBundle1Name_Object = MibTableColumn
mp7002TSBundle1Name = _Mp7002TSBundle1Name_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 9),
    _Mp7002TSBundle1Name_Type()
)
mp7002TSBundle1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TSBundle1Name.setStatus("mandatory")


class _Mp7002TSBundle2Name_Type(DisplayString):
    """Custom type mp7002TSBundle2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Mp7002TSBundle2Name_Type.__name__ = "DisplayString"
_Mp7002TSBundle2Name_Object = MibTableColumn
mp7002TSBundle2Name = _Mp7002TSBundle2Name_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 10),
    _Mp7002TSBundle2Name_Type()
)
mp7002TSBundle2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TSBundle2Name.setStatus("mandatory")


class _Mp7002SetRealTime_Type(Integer32):
    """Custom type mp7002SetRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002SetRealTime_Type.__name__ = "Integer32"
_Mp7002SetRealTime_Object = MibTableColumn
mp7002SetRealTime = _Mp7002SetRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 11),
    _Mp7002SetRealTime_Type()
)
mp7002SetRealTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002SetRealTime.setStatus("mandatory")


class _Mp7002AlarmStatus_Type(OctetString):
    """Custom type mp7002AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Mp7002AlarmStatus_Type.__name__ = "OctetString"
_Mp7002AlarmStatus_Object = MibTableColumn
mp7002AlarmStatus = _Mp7002AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 12),
    _Mp7002AlarmStatus_Type()
)
mp7002AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002AlarmStatus.setStatus("mandatory")


class _Mp7002SystemTimingGenStatus_Type(Integer32):
    """Custom type mp7002SystemTimingGenStatus based on Integer32"""
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
        *(("clk4mhz", 3),
          ("clk8khz", 2),
          ("clk8khzand4mhz", 4),
          ("none", 1))
    )


_Mp7002SystemTimingGenStatus_Type.__name__ = "Integer32"
_Mp7002SystemTimingGenStatus_Object = MibTableColumn
mp7002SystemTimingGenStatus = _Mp7002SystemTimingGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 13),
    _Mp7002SystemTimingGenStatus_Type()
)
mp7002SystemTimingGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002SystemTimingGenStatus.setStatus("mandatory")


class _Mp7002FarEndResetStats_Type(Integer32):
    """Custom type mp7002FarEndResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Mp7002FarEndResetStats_Type.__name__ = "Integer32"
_Mp7002FarEndResetStats_Object = MibTableColumn
mp7002FarEndResetStats = _Mp7002FarEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 14),
    _Mp7002FarEndResetStats_Type()
)
mp7002FarEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002FarEndResetStats.setStatus("mandatory")


class _Mp7002NearEndStatLastInitialized_Type(Integer32):
    """Custom type mp7002NearEndStatLastInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002NearEndStatLastInitialized_Type.__name__ = "Integer32"
_Mp7002NearEndStatLastInitialized_Object = MibTableColumn
mp7002NearEndStatLastInitialized = _Mp7002NearEndStatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 15),
    _Mp7002NearEndStatLastInitialized_Type()
)
mp7002NearEndStatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndStatLastInitialized.setStatus("mandatory")


class _Mp7002FarEndStatLastInitialized_Type(Integer32):
    """Custom type mp7002FarEndStatLastInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002FarEndStatLastInitialized_Type.__name__ = "Integer32"
_Mp7002FarEndStatLastInitialized_Object = MibTableColumn
mp7002FarEndStatLastInitialized = _Mp7002FarEndStatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 2, 1, 1, 16),
    _Mp7002FarEndStatLastInitialized_Type()
)
mp7002FarEndStatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndStatLastInitialized.setStatus("mandatory")
_Mp7002Configuration_ObjectIdentity = ObjectIdentity
mp7002Configuration = _Mp7002Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3)
)
_Mp7002ConfigTable_Object = MibTable
mp7002ConfigTable = _Mp7002ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1)
)
if mibBuilder.loadTexts:
    mp7002ConfigTable.setStatus("mandatory")
_Mp7002ConfigEntry_Object = MibTableRow
mp7002ConfigEntry = _Mp7002ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1)
)
mp7002ConfigEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002ConfigIndex"),
)
if mibBuilder.loadTexts:
    mp7002ConfigEntry.setStatus("mandatory")
_Mp7002ConfigIndex_Type = SCinstance
_Mp7002ConfigIndex_Object = MibTableColumn
mp7002ConfigIndex = _Mp7002ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 1),
    _Mp7002ConfigIndex_Type()
)
mp7002ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002ConfigIndex.setStatus("mandatory")


class _Mp7002InterfaceType_Type(Integer32):
    """Custom type mp7002InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diu", 1),
          ("niu", 2),
          ("notAssigned", 3))
    )


_Mp7002InterfaceType_Type.__name__ = "Integer32"
_Mp7002InterfaceType_Object = MibTableColumn
mp7002InterfaceType = _Mp7002InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 2),
    _Mp7002InterfaceType_Type()
)
mp7002InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002InterfaceType.setStatus("mandatory")


class _Mp7002RcvrRange_Type(Integer32):
    """Custom type mp7002RcvrRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_Mp7002RcvrRange_Type.__name__ = "Integer32"
_Mp7002RcvrRange_Object = MibTableColumn
mp7002RcvrRange = _Mp7002RcvrRange_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 3),
    _Mp7002RcvrRange_Type()
)
mp7002RcvrRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002RcvrRange.setStatus("mandatory")


class _Mp7002TransmitClockSource_Type(Integer32):
    """Custom type mp7002TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("recovered", 2),
          ("system", 1))
    )


_Mp7002TransmitClockSource_Type.__name__ = "Integer32"
_Mp7002TransmitClockSource_Object = MibTableColumn
mp7002TransmitClockSource = _Mp7002TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 4),
    _Mp7002TransmitClockSource_Type()
)
mp7002TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TransmitClockSource.setStatus("mandatory")


class _Mp7002FallbackClockSource_Type(Integer32):
    """Custom type mp7002FallbackClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("recovered", 2),
          ("system", 1))
    )


_Mp7002FallbackClockSource_Type.__name__ = "Integer32"
_Mp7002FallbackClockSource_Object = MibTableColumn
mp7002FallbackClockSource = _Mp7002FallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 5),
    _Mp7002FallbackClockSource_Type()
)
mp7002FallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002FallbackClockSource.setStatus("mandatory")


class _Mp7002FacilityDataLink_Type(Integer32):
    """Custom type mp7002FacilityDataLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("none", 1),
          ("notActive", 3))
    )


_Mp7002FacilityDataLink_Type.__name__ = "Integer32"
_Mp7002FacilityDataLink_Object = MibTableColumn
mp7002FacilityDataLink = _Mp7002FacilityDataLink_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 6),
    _Mp7002FacilityDataLink_Type()
)
mp7002FacilityDataLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002FacilityDataLink.setStatus("mandatory")


class _Mp7002NearEndValidIntervals_Type(Integer32):
    """Custom type mp7002NearEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mp7002NearEndValidIntervals_Type.__name__ = "Integer32"
_Mp7002NearEndValidIntervals_Object = MibTableColumn
mp7002NearEndValidIntervals = _Mp7002NearEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 7),
    _Mp7002NearEndValidIntervals_Type()
)
mp7002NearEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndValidIntervals.setStatus("mandatory")


class _Mp7002FarEndValidIntervals_Type(Integer32):
    """Custom type mp7002FarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mp7002FarEndValidIntervals_Type.__name__ = "Integer32"
_Mp7002FarEndValidIntervals_Object = MibTableColumn
mp7002FarEndValidIntervals = _Mp7002FarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 8),
    _Mp7002FarEndValidIntervals_Type()
)
mp7002FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndValidIntervals.setStatus("mandatory")


class _Mp7002NetworkConnection_Type(Integer32):
    """Custom type mp7002NetworkConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onLine", 1),
          ("standBy", 2))
    )


_Mp7002NetworkConnection_Type.__name__ = "Integer32"
_Mp7002NetworkConnection_Object = MibTableColumn
mp7002NetworkConnection = _Mp7002NetworkConnection_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 9),
    _Mp7002NetworkConnection_Type()
)
mp7002NetworkConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002NetworkConnection.setStatus("mandatory")


class _Mp7002Framing_Type(Integer32):
    """Custom type mp7002Framing based on Integer32"""
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
        *(("cCSwithCRC4", 4),
          ("cCSwithoutCRC4", 1),
          ("pCS0withCRC4", 5),
          ("pCS0withoutCRC4", 2),
          ("pCS1withCRC4", 6),
          ("pCS1withoutCRC4", 3))
    )


_Mp7002Framing_Type.__name__ = "Integer32"
_Mp7002Framing_Object = MibTableColumn
mp7002Framing = _Mp7002Framing_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 10),
    _Mp7002Framing_Type()
)
mp7002Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002Framing.setStatus("mandatory")


class _Mp7002LineCoding_Type(Integer32):
    """Custom type mp7002LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("hdb3", 2))
    )


_Mp7002LineCoding_Type.__name__ = "Integer32"
_Mp7002LineCoding_Object = MibTableColumn
mp7002LineCoding = _Mp7002LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 1, 1, 11),
    _Mp7002LineCoding_Type()
)
mp7002LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002LineCoding.setStatus("mandatory")
_Mp7002DCCConfigurationTable_Object = MibTable
mp7002DCCConfigurationTable = _Mp7002DCCConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 2)
)
if mibBuilder.loadTexts:
    mp7002DCCConfigurationTable.setStatus("mandatory")
_Mp7002DCCConfigurationEntry_Object = MibTableRow
mp7002DCCConfigurationEntry = _Mp7002DCCConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 2, 1)
)
mp7002DCCConfigurationEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002DCCConfigurationIndex"),
)
if mibBuilder.loadTexts:
    mp7002DCCConfigurationEntry.setStatus("mandatory")
_Mp7002DCCConfigurationIndex_Type = SCinstance
_Mp7002DCCConfigurationIndex_Object = MibTableColumn
mp7002DCCConfigurationIndex = _Mp7002DCCConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 2, 1, 1),
    _Mp7002DCCConfigurationIndex_Type()
)
mp7002DCCConfigurationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002DCCConfigurationIndex.setStatus("mandatory")


class _Mp7002TimeSlot_Type(Integer32):
    """Custom type mp7002TimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Mp7002TimeSlot_Type.__name__ = "Integer32"
_Mp7002TimeSlot_Object = MibTableColumn
mp7002TimeSlot = _Mp7002TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 2, 1, 2),
    _Mp7002TimeSlot_Type()
)
mp7002TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TimeSlot.setStatus("mandatory")


class _Mp7002Bandwidth_Type(Integer32):
    """Custom type mp7002Bandwidth based on Integer32"""
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
        *(("kbps56", 2),
          ("kbps64", 3),
          ("kbps8", 1),
          ("notAssigned", 4))
    )


_Mp7002Bandwidth_Type.__name__ = "Integer32"
_Mp7002Bandwidth_Object = MibTableColumn
mp7002Bandwidth = _Mp7002Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 3, 2, 1, 3),
    _Mp7002Bandwidth_Type()
)
mp7002Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002Bandwidth.setStatus("mandatory")
_Mp7002Diagnostics_ObjectIdentity = ObjectIdentity
mp7002Diagnostics = _Mp7002Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4)
)
_Mp7002DiagTable_Object = MibTable
mp7002DiagTable = _Mp7002DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1)
)
if mibBuilder.loadTexts:
    mp7002DiagTable.setStatus("mandatory")
_Mp7002DiagEntry_Object = MibTableRow
mp7002DiagEntry = _Mp7002DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1)
)
mp7002DiagEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002DiagIndex"),
)
if mibBuilder.loadTexts:
    mp7002DiagEntry.setStatus("mandatory")
_Mp7002DiagIndex_Type = SCinstance
_Mp7002DiagIndex_Object = MibTableColumn
mp7002DiagIndex = _Mp7002DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 1),
    _Mp7002DiagIndex_Type()
)
mp7002DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002DiagIndex.setStatus("mandatory")


class _Mp7002TestPattern_Type(Integer32):
    """Custom type mp7002TestPattern based on Integer32"""
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
        *(("noCode", 1),
          ("pat1in4", 4),
          ("pat2047", 3),
          ("pat511", 2))
    )


_Mp7002TestPattern_Type.__name__ = "Integer32"
_Mp7002TestPattern_Object = MibTableColumn
mp7002TestPattern = _Mp7002TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 2),
    _Mp7002TestPattern_Type()
)
mp7002TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TestPattern.setStatus("obsolete")


class _Mp7002DiagConfig_Type(Integer32):
    """Custom type mp7002DiagConfig based on Integer32"""
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
        *(("lineLoopback", 2),
          ("localTest", 4),
          ("noLoop", 1),
          ("patGenOn", 6),
          ("payloadLoopback", 3),
          ("unitTest", 5))
    )


_Mp7002DiagConfig_Type.__name__ = "Integer32"
_Mp7002DiagConfig_Object = MibTableColumn
mp7002DiagConfig = _Mp7002DiagConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 3),
    _Mp7002DiagConfig_Type()
)
mp7002DiagConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002DiagConfig.setStatus("mandatory")


class _Mp7002TestLimit_Type(Integer32):
    """Custom type mp7002TestLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLimit", 3),
          ("testTime10Mins", 1),
          ("testTime20Mins", 2))
    )


_Mp7002TestLimit_Type.__name__ = "Integer32"
_Mp7002TestLimit_Object = MibTableColumn
mp7002TestLimit = _Mp7002TestLimit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 4),
    _Mp7002TestLimit_Type()
)
mp7002TestLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TestLimit.setStatus("mandatory")


class _Mp7002TestExecutionStatus_Type(Integer32):
    """Custom type mp7002TestExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notInTest", 1),
          ("testCompleted", 4),
          ("testCompletedNotInTest", 5),
          ("testInProgress", 2))
    )


_Mp7002TestExecutionStatus_Type.__name__ = "Integer32"
_Mp7002TestExecutionStatus_Object = MibTableColumn
mp7002TestExecutionStatus = _Mp7002TestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 5),
    _Mp7002TestExecutionStatus_Type()
)
mp7002TestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002TestExecutionStatus.setStatus("mandatory")


class _Mp7002TestExceptions_Type(Integer32):
    """Custom type mp7002TestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Mp7002TestExceptions_Type.__name__ = "Integer32"
_Mp7002TestExceptions_Object = MibTableColumn
mp7002TestExceptions = _Mp7002TestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 6),
    _Mp7002TestExceptions_Type()
)
mp7002TestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002TestExceptions.setStatus("mandatory")


class _Mp7002TestResults_Type(Integer32):
    """Custom type mp7002TestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_Mp7002TestResults_Type.__name__ = "Integer32"
_Mp7002TestResults_Object = MibTableColumn
mp7002TestResults = _Mp7002TestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 7),
    _Mp7002TestResults_Type()
)
mp7002TestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002TestResults.setStatus("obsolete")


class _Mp7002ResetTestResults_Type(Integer32):
    """Custom type mp7002ResetTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Mp7002ResetTestResults_Type.__name__ = "Integer32"
_Mp7002ResetTestResults_Object = MibTableColumn
mp7002ResetTestResults = _Mp7002ResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 4, 1, 1, 8),
    _Mp7002ResetTestResults_Type()
)
mp7002ResetTestResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002ResetTestResults.setStatus("obsolete")
_Mp7002Performance_ObjectIdentity = ObjectIdentity
mp7002Performance = _Mp7002Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5)
)
_Mp7002NearEndCurrent15MinTable_Object = MibTable
mp7002NearEndCurrent15MinTable = _Mp7002NearEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 1)
)
if mibBuilder.loadTexts:
    mp7002NearEndCurrent15MinTable.setStatus("mandatory")
_Mp7002NearEndCurrent15MinEntry_Object = MibTableRow
mp7002NearEndCurrent15MinEntry = _Mp7002NearEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 1, 1)
)
mp7002NearEndCurrent15MinEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002NearEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    mp7002NearEndCurrent15MinEntry.setStatus("mandatory")
_Mp7002NearEndCurrent15MinIndex_Type = SCinstance
_Mp7002NearEndCurrent15MinIndex_Object = MibTableColumn
mp7002NearEndCurrent15MinIndex = _Mp7002NearEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 1, 1, 1),
    _Mp7002NearEndCurrent15MinIndex_Type()
)
mp7002NearEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndCurrent15MinIndex.setStatus("mandatory")


class _Mp7002NearEndCurrent15MinStat_Type(OctetString):
    """Custom type mp7002NearEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Mp7002NearEndCurrent15MinStat_Type.__name__ = "OctetString"
_Mp7002NearEndCurrent15MinStat_Object = MibTableColumn
mp7002NearEndCurrent15MinStat = _Mp7002NearEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 1, 1, 2),
    _Mp7002NearEndCurrent15MinStat_Type()
)
mp7002NearEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndCurrent15MinStat.setStatus("mandatory")
_Mp7002NearEndIntervalTable_Object = MibTable
mp7002NearEndIntervalTable = _Mp7002NearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 2)
)
if mibBuilder.loadTexts:
    mp7002NearEndIntervalTable.setStatus("mandatory")
_Mp7002NearEndIntervalEntry_Object = MibTableRow
mp7002NearEndIntervalEntry = _Mp7002NearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 2, 1)
)
mp7002NearEndIntervalEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002NearEndIntervalIndex"),
    (0, "GDCMP7002-MIB", "mp7002NearEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    mp7002NearEndIntervalEntry.setStatus("mandatory")
_Mp7002NearEndIntervalIndex_Type = SCinstance
_Mp7002NearEndIntervalIndex_Object = MibTableColumn
mp7002NearEndIntervalIndex = _Mp7002NearEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 2, 1, 1),
    _Mp7002NearEndIntervalIndex_Type()
)
mp7002NearEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndIntervalIndex.setStatus("mandatory")


class _Mp7002NearEndIntervalNumber_Type(Integer32):
    """Custom type mp7002NearEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mp7002NearEndIntervalNumber_Type.__name__ = "Integer32"
_Mp7002NearEndIntervalNumber_Object = MibTableColumn
mp7002NearEndIntervalNumber = _Mp7002NearEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 2, 1, 2),
    _Mp7002NearEndIntervalNumber_Type()
)
mp7002NearEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndIntervalNumber.setStatus("mandatory")


class _Mp7002NearEndIntervalStat_Type(OctetString):
    """Custom type mp7002NearEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Mp7002NearEndIntervalStat_Type.__name__ = "OctetString"
_Mp7002NearEndIntervalStat_Object = MibTableColumn
mp7002NearEndIntervalStat = _Mp7002NearEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 2, 1, 3),
    _Mp7002NearEndIntervalStat_Type()
)
mp7002NearEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndIntervalStat.setStatus("mandatory")
_Mp7002NearEndCurrent24HrTable_Object = MibTable
mp7002NearEndCurrent24HrTable = _Mp7002NearEndCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 3)
)
if mibBuilder.loadTexts:
    mp7002NearEndCurrent24HrTable.setStatus("mandatory")
_Mp7002NearEndCurrent24HrEntry_Object = MibTableRow
mp7002NearEndCurrent24HrEntry = _Mp7002NearEndCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 3, 1)
)
mp7002NearEndCurrent24HrEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002NearEndCurrent24HrIndex"),
)
if mibBuilder.loadTexts:
    mp7002NearEndCurrent24HrEntry.setStatus("mandatory")
_Mp7002NearEndCurrent24HrIndex_Type = SCinstance
_Mp7002NearEndCurrent24HrIndex_Object = MibTableColumn
mp7002NearEndCurrent24HrIndex = _Mp7002NearEndCurrent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 3, 1, 1),
    _Mp7002NearEndCurrent24HrIndex_Type()
)
mp7002NearEndCurrent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndCurrent24HrIndex.setStatus("mandatory")


class _Mp7002NearEndCurrent24HrStat_Type(OctetString):
    """Custom type mp7002NearEndCurrent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Mp7002NearEndCurrent24HrStat_Type.__name__ = "OctetString"
_Mp7002NearEndCurrent24HrStat_Object = MibTableColumn
mp7002NearEndCurrent24HrStat = _Mp7002NearEndCurrent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 3, 1, 2),
    _Mp7002NearEndCurrent24HrStat_Type()
)
mp7002NearEndCurrent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndCurrent24HrStat.setStatus("mandatory")
_Mp7002NearEndRecent24HrTable_Object = MibTable
mp7002NearEndRecent24HrTable = _Mp7002NearEndRecent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 4)
)
if mibBuilder.loadTexts:
    mp7002NearEndRecent24HrTable.setStatus("mandatory")
_Mp7002NearEndRecent24HrEntry_Object = MibTableRow
mp7002NearEndRecent24HrEntry = _Mp7002NearEndRecent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 4, 1)
)
mp7002NearEndRecent24HrEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002NearEndRecent24HrIndex"),
)
if mibBuilder.loadTexts:
    mp7002NearEndRecent24HrEntry.setStatus("mandatory")
_Mp7002NearEndRecent24HrIndex_Type = SCinstance
_Mp7002NearEndRecent24HrIndex_Object = MibTableColumn
mp7002NearEndRecent24HrIndex = _Mp7002NearEndRecent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 4, 1, 1),
    _Mp7002NearEndRecent24HrIndex_Type()
)
mp7002NearEndRecent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndRecent24HrIndex.setStatus("mandatory")


class _Mp7002NearEndRecent24HrStat_Type(OctetString):
    """Custom type mp7002NearEndRecent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Mp7002NearEndRecent24HrStat_Type.__name__ = "OctetString"
_Mp7002NearEndRecent24HrStat_Object = MibTableColumn
mp7002NearEndRecent24HrStat = _Mp7002NearEndRecent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 4, 1, 2),
    _Mp7002NearEndRecent24HrStat_Type()
)
mp7002NearEndRecent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndRecent24HrStat.setStatus("mandatory")
_Mp7002FarEndCurrent15MinTable_Object = MibTable
mp7002FarEndCurrent15MinTable = _Mp7002FarEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 5)
)
if mibBuilder.loadTexts:
    mp7002FarEndCurrent15MinTable.setStatus("mandatory")
_Mp7002FarEndCurrent15MinEntry_Object = MibTableRow
mp7002FarEndCurrent15MinEntry = _Mp7002FarEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 5, 1)
)
mp7002FarEndCurrent15MinEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002FarEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    mp7002FarEndCurrent15MinEntry.setStatus("mandatory")
_Mp7002FarEndCurrent15MinIndex_Type = SCinstance
_Mp7002FarEndCurrent15MinIndex_Object = MibTableColumn
mp7002FarEndCurrent15MinIndex = _Mp7002FarEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 5, 1, 1),
    _Mp7002FarEndCurrent15MinIndex_Type()
)
mp7002FarEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndCurrent15MinIndex.setStatus("mandatory")


class _Mp7002FarEndCurrent15MinStat_Type(OctetString):
    """Custom type mp7002FarEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Mp7002FarEndCurrent15MinStat_Type.__name__ = "OctetString"
_Mp7002FarEndCurrent15MinStat_Object = MibTableColumn
mp7002FarEndCurrent15MinStat = _Mp7002FarEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 5, 1, 2),
    _Mp7002FarEndCurrent15MinStat_Type()
)
mp7002FarEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndCurrent15MinStat.setStatus("mandatory")
_Mp7002FarEndIntervalTable_Object = MibTable
mp7002FarEndIntervalTable = _Mp7002FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 6)
)
if mibBuilder.loadTexts:
    mp7002FarEndIntervalTable.setStatus("mandatory")
_Mp7002FarEndIntervalEntry_Object = MibTableRow
mp7002FarEndIntervalEntry = _Mp7002FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 6, 1)
)
mp7002FarEndIntervalEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002FarEndIntervalIndex"),
    (0, "GDCMP7002-MIB", "mp7002FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    mp7002FarEndIntervalEntry.setStatus("mandatory")
_Mp7002FarEndIntervalIndex_Type = SCinstance
_Mp7002FarEndIntervalIndex_Object = MibTableColumn
mp7002FarEndIntervalIndex = _Mp7002FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 6, 1, 1),
    _Mp7002FarEndIntervalIndex_Type()
)
mp7002FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndIntervalIndex.setStatus("mandatory")


class _Mp7002FarEndIntervalNumber_Type(Integer32):
    """Custom type mp7002FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Mp7002FarEndIntervalNumber_Type.__name__ = "Integer32"
_Mp7002FarEndIntervalNumber_Object = MibTableColumn
mp7002FarEndIntervalNumber = _Mp7002FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 6, 1, 2),
    _Mp7002FarEndIntervalNumber_Type()
)
mp7002FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndIntervalNumber.setStatus("mandatory")


class _Mp7002FarEndIntervalStat_Type(OctetString):
    """Custom type mp7002FarEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Mp7002FarEndIntervalStat_Type.__name__ = "OctetString"
_Mp7002FarEndIntervalStat_Object = MibTableColumn
mp7002FarEndIntervalStat = _Mp7002FarEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 6, 1, 3),
    _Mp7002FarEndIntervalStat_Type()
)
mp7002FarEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndIntervalStat.setStatus("mandatory")
_Mp7002CurrentFarEnd24HrTable_Object = MibTable
mp7002CurrentFarEnd24HrTable = _Mp7002CurrentFarEnd24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 7)
)
if mibBuilder.loadTexts:
    mp7002CurrentFarEnd24HrTable.setStatus("mandatory")
_Mp7002CurrentFarEnd24HrEntry_Object = MibTableRow
mp7002CurrentFarEnd24HrEntry = _Mp7002CurrentFarEnd24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 7, 1)
)
mp7002CurrentFarEnd24HrEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002CurrentFarEnd24HrIndex"),
)
if mibBuilder.loadTexts:
    mp7002CurrentFarEnd24HrEntry.setStatus("mandatory")
_Mp7002CurrentFarEnd24HrIndex_Type = SCinstance
_Mp7002CurrentFarEnd24HrIndex_Object = MibTableColumn
mp7002CurrentFarEnd24HrIndex = _Mp7002CurrentFarEnd24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 7, 1, 1),
    _Mp7002CurrentFarEnd24HrIndex_Type()
)
mp7002CurrentFarEnd24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002CurrentFarEnd24HrIndex.setStatus("mandatory")


class _Mp7002CurrentFarEnd24HrStat_Type(OctetString):
    """Custom type mp7002CurrentFarEnd24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Mp7002CurrentFarEnd24HrStat_Type.__name__ = "OctetString"
_Mp7002CurrentFarEnd24HrStat_Object = MibTableColumn
mp7002CurrentFarEnd24HrStat = _Mp7002CurrentFarEnd24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 7, 1, 2),
    _Mp7002CurrentFarEnd24HrStat_Type()
)
mp7002CurrentFarEnd24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002CurrentFarEnd24HrStat.setStatus("mandatory")
_Mp7002RecentFarEnd24HrTable_Object = MibTable
mp7002RecentFarEnd24HrTable = _Mp7002RecentFarEnd24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 8)
)
if mibBuilder.loadTexts:
    mp7002RecentFarEnd24HrTable.setStatus("mandatory")
_Mp7002RecentFarEnd24HrEntry_Object = MibTableRow
mp7002RecentFarEnd24HrEntry = _Mp7002RecentFarEnd24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 8, 1)
)
mp7002RecentFarEnd24HrEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002RecentFarEnd24HrIndex"),
)
if mibBuilder.loadTexts:
    mp7002RecentFarEnd24HrEntry.setStatus("mandatory")
_Mp7002RecentFarEnd24HrIndex_Type = SCinstance
_Mp7002RecentFarEnd24HrIndex_Object = MibTableColumn
mp7002RecentFarEnd24HrIndex = _Mp7002RecentFarEnd24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 8, 1, 1),
    _Mp7002RecentFarEnd24HrIndex_Type()
)
mp7002RecentFarEnd24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002RecentFarEnd24HrIndex.setStatus("mandatory")


class _Mp7002RecentFarEnd24HrStat_Type(OctetString):
    """Custom type mp7002RecentFarEnd24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Mp7002RecentFarEnd24HrStat_Type.__name__ = "OctetString"
_Mp7002RecentFarEnd24HrStat_Object = MibTableColumn
mp7002RecentFarEnd24HrStat = _Mp7002RecentFarEnd24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 8, 1, 2),
    _Mp7002RecentFarEnd24HrStat_Type()
)
mp7002RecentFarEnd24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002RecentFarEnd24HrStat.setStatus("mandatory")
_Mp7002UnavailableTimeRegTable_Object = MibTable
mp7002UnavailableTimeRegTable = _Mp7002UnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9)
)
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegTable.setStatus("mandatory")
_Mp7002UnavailableTimeRegEntry_Object = MibTableRow
mp7002UnavailableTimeRegEntry = _Mp7002UnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9, 1)
)
mp7002UnavailableTimeRegEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002UnavailableTimeRegIndex"),
    (0, "GDCMP7002-MIB", "mp7002UnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegEntry.setStatus("mandatory")
_Mp7002UnavailableTimeRegIndex_Type = SCinstance
_Mp7002UnavailableTimeRegIndex_Object = MibTableColumn
mp7002UnavailableTimeRegIndex = _Mp7002UnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9, 1, 1),
    _Mp7002UnavailableTimeRegIndex_Type()
)
mp7002UnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegIndex.setStatus("mandatory")


class _Mp7002UnavailableTimeRegNumber_Type(Integer32):
    """Custom type mp7002UnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Mp7002UnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Mp7002UnavailableTimeRegNumber_Object = MibTableColumn
mp7002UnavailableTimeRegNumber = _Mp7002UnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9, 1, 2),
    _Mp7002UnavailableTimeRegNumber_Type()
)
mp7002UnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegNumber.setStatus("mandatory")


class _Mp7002UnavailableTimeRegStart_Type(Integer32):
    """Custom type mp7002UnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002UnavailableTimeRegStart_Type.__name__ = "Integer32"
_Mp7002UnavailableTimeRegStart_Object = MibTableColumn
mp7002UnavailableTimeRegStart = _Mp7002UnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9, 1, 3),
    _Mp7002UnavailableTimeRegStart_Type()
)
mp7002UnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegStart.setStatus("mandatory")


class _Mp7002UnavailableTimeRegStop_Type(Integer32):
    """Custom type mp7002UnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002UnavailableTimeRegStop_Type.__name__ = "Integer32"
_Mp7002UnavailableTimeRegStop_Object = MibTableColumn
mp7002UnavailableTimeRegStop = _Mp7002UnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 9, 1, 4),
    _Mp7002UnavailableTimeRegStop_Type()
)
mp7002UnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002UnavailableTimeRegStop.setStatus("mandatory")
_Mp7002FarEndUnavailableTimeRegTable_Object = MibTable
mp7002FarEndUnavailableTimeRegTable = _Mp7002FarEndUnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10)
)
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegTable.setStatus("mandatory")
_Mp7002FarEndUnavailableTimeRegEntry_Object = MibTableRow
mp7002FarEndUnavailableTimeRegEntry = _Mp7002FarEndUnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10, 1)
)
mp7002FarEndUnavailableTimeRegEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002FarEndUnavailableTimeRegIndex"),
    (0, "GDCMP7002-MIB", "mp7002FarEndUnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegEntry.setStatus("mandatory")
_Mp7002FarEndUnavailableTimeRegIndex_Type = SCinstance
_Mp7002FarEndUnavailableTimeRegIndex_Object = MibTableColumn
mp7002FarEndUnavailableTimeRegIndex = _Mp7002FarEndUnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10, 1, 1),
    _Mp7002FarEndUnavailableTimeRegIndex_Type()
)
mp7002FarEndUnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegIndex.setStatus("mandatory")


class _Mp7002FarEndUnavailableTimeRegNumber_Type(Integer32):
    """Custom type mp7002FarEndUnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Mp7002FarEndUnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Mp7002FarEndUnavailableTimeRegNumber_Object = MibTableColumn
mp7002FarEndUnavailableTimeRegNumber = _Mp7002FarEndUnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10, 1, 2),
    _Mp7002FarEndUnavailableTimeRegNumber_Type()
)
mp7002FarEndUnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegNumber.setStatus("mandatory")


class _Mp7002FarEndUnavailableTimeRegStart_Type(Integer32):
    """Custom type mp7002FarEndUnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002FarEndUnavailableTimeRegStart_Type.__name__ = "Integer32"
_Mp7002FarEndUnavailableTimeRegStart_Object = MibTableColumn
mp7002FarEndUnavailableTimeRegStart = _Mp7002FarEndUnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10, 1, 3),
    _Mp7002FarEndUnavailableTimeRegStart_Type()
)
mp7002FarEndUnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegStart.setStatus("mandatory")


class _Mp7002FarEndUnavailableTimeRegStop_Type(Integer32):
    """Custom type mp7002FarEndUnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Mp7002FarEndUnavailableTimeRegStop_Type.__name__ = "Integer32"
_Mp7002FarEndUnavailableTimeRegStop_Object = MibTableColumn
mp7002FarEndUnavailableTimeRegStop = _Mp7002FarEndUnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 5, 10, 1, 4),
    _Mp7002FarEndUnavailableTimeRegStop_Type()
)
mp7002FarEndUnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndUnavailableTimeRegStop.setStatus("mandatory")
_Mp7002SysConfig_ObjectIdentity = ObjectIdentity
mp7002SysConfig = _Mp7002SysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7)
)
_Mp7002SysTimingTable_Object = MibTable
mp7002SysTimingTable = _Mp7002SysTimingTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 1)
)
if mibBuilder.loadTexts:
    mp7002SysTimingTable.setStatus("mandatory")
_Mp7002SysTimingEntry_Object = MibTableRow
mp7002SysTimingEntry = _Mp7002SysTimingEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 1, 1)
)
mp7002SysTimingEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002SysTimingIndex"),
)
if mibBuilder.loadTexts:
    mp7002SysTimingEntry.setStatus("mandatory")
_Mp7002SysTimingIndex_Type = SCinstance
_Mp7002SysTimingIndex_Object = MibTableColumn
mp7002SysTimingIndex = _Mp7002SysTimingIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 1, 1, 1),
    _Mp7002SysTimingIndex_Type()
)
mp7002SysTimingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002SysTimingIndex.setStatus("mandatory")


class _Mp7002SysTimingGen_Type(Integer32):
    """Custom type mp7002SysTimingGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_Mp7002SysTimingGen_Type.__name__ = "Integer32"
_Mp7002SysTimingGen_Object = MibTableColumn
mp7002SysTimingGen = _Mp7002SysTimingGen_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 1, 1, 2),
    _Mp7002SysTimingGen_Type()
)
mp7002SysTimingGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002SysTimingGen.setStatus("mandatory")
_Mp7002HighwayAssignTable_Object = MibTable
mp7002HighwayAssignTable = _Mp7002HighwayAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2)
)
if mibBuilder.loadTexts:
    mp7002HighwayAssignTable.setStatus("mandatory")
_Mp7002HighwayAssignEntry_Object = MibTableRow
mp7002HighwayAssignEntry = _Mp7002HighwayAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1)
)
mp7002HighwayAssignEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002HighwayAssignIndex"),
    (0, "GDCMP7002-MIB", "mp7002TimeSlotBundle"),
)
if mibBuilder.loadTexts:
    mp7002HighwayAssignEntry.setStatus("mandatory")
_Mp7002HighwayAssignIndex_Type = SCinstance
_Mp7002HighwayAssignIndex_Object = MibTableColumn
mp7002HighwayAssignIndex = _Mp7002HighwayAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 1),
    _Mp7002HighwayAssignIndex_Type()
)
mp7002HighwayAssignIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002HighwayAssignIndex.setStatus("mandatory")


class _Mp7002TimeSlotBundle_Type(Integer32):
    """Custom type mp7002TimeSlotBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bundle1", 1),
          ("bundle2", 2))
    )


_Mp7002TimeSlotBundle_Type.__name__ = "Integer32"
_Mp7002TimeSlotBundle_Object = MibTableColumn
mp7002TimeSlotBundle = _Mp7002TimeSlotBundle_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 2),
    _Mp7002TimeSlotBundle_Type()
)
mp7002TimeSlotBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002TimeSlotBundle.setStatus("mandatory")


class _Mp7002StartTimeSlot_Type(Integer32):
    """Custom type mp7002StartTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Mp7002StartTimeSlot_Type.__name__ = "Integer32"
_Mp7002StartTimeSlot_Object = MibTableColumn
mp7002StartTimeSlot = _Mp7002StartTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 3),
    _Mp7002StartTimeSlot_Type()
)
mp7002StartTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002StartTimeSlot.setStatus("mandatory")


class _Mp7002NumberOfTimeSlots_Type(Integer32):
    """Custom type mp7002NumberOfTimeSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Mp7002NumberOfTimeSlots_Type.__name__ = "Integer32"
_Mp7002NumberOfTimeSlots_Object = MibTableColumn
mp7002NumberOfTimeSlots = _Mp7002NumberOfTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 4),
    _Mp7002NumberOfTimeSlots_Type()
)
mp7002NumberOfTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002NumberOfTimeSlots.setStatus("mandatory")


class _Mp7002BundleDestination_Type(Integer32):
    """Custom type mp7002BundleDestination based on Integer32"""
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
        *(("highway1", 2),
          ("highway2", 3),
          ("highway3", 4),
          ("highway4", 5),
          ("notAssigned", 1))
    )


_Mp7002BundleDestination_Type.__name__ = "Integer32"
_Mp7002BundleDestination_Object = MibTableColumn
mp7002BundleDestination = _Mp7002BundleDestination_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 5),
    _Mp7002BundleDestination_Type()
)
mp7002BundleDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002BundleDestination.setStatus("mandatory")


class _Mp7002ExecuteAssign_Type(Integer32):
    """Custom type mp7002ExecuteAssign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("normal", 1))
    )


_Mp7002ExecuteAssign_Type.__name__ = "Integer32"
_Mp7002ExecuteAssign_Object = MibTableColumn
mp7002ExecuteAssign = _Mp7002ExecuteAssign_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 6, 7, 2, 1, 6),
    _Mp7002ExecuteAssign_Type()
)
mp7002ExecuteAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002ExecuteAssign.setStatus("mandatory")
_Mp7002Alarms_ObjectIdentity = ObjectIdentity
mp7002Alarms = _Mp7002Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9)
)
_Mp7002AlarmData_ObjectIdentity = ObjectIdentity
mp7002AlarmData = _Mp7002AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1)
)
_Mp7002NoResponseAlm_ObjectIdentity = ObjectIdentity
mp7002NoResponseAlm = _Mp7002NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 1)
)
_Mp7002DiagRxErrAlm_ObjectIdentity = ObjectIdentity
mp7002DiagRxErrAlm = _Mp7002DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 2)
)
_Mp7002PowerUpAlm_ObjectIdentity = ObjectIdentity
mp7002PowerUpAlm = _Mp7002PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 3)
)
_Mp7002NvRamCorrupt_ObjectIdentity = ObjectIdentity
mp7002NvRamCorrupt = _Mp7002NvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 4)
)
_Mp7002UnitFailure_ObjectIdentity = ObjectIdentity
mp7002UnitFailure = _Mp7002UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 5)
)
_Mp7002TimingLoss_ObjectIdentity = ObjectIdentity
mp7002TimingLoss = _Mp7002TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 6)
)
_Mp7002LCV_ObjectIdentity = ObjectIdentity
mp7002LCV = _Mp7002LCV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 7)
)
_Mp7002LossOfSignal_ObjectIdentity = ObjectIdentity
mp7002LossOfSignal = _Mp7002LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 8)
)
_Mp7002LossOfFrame_ObjectIdentity = ObjectIdentity
mp7002LossOfFrame = _Mp7002LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 9)
)
_Mp7002AlarmIndSignal_ObjectIdentity = ObjectIdentity
mp7002AlarmIndSignal = _Mp7002AlarmIndSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 10)
)
_Mp7002NEES_ObjectIdentity = ObjectIdentity
mp7002NEES = _Mp7002NEES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 11)
)
_Mp7002NEBBE_ObjectIdentity = ObjectIdentity
mp7002NEBBE = _Mp7002NEBBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 12)
)
_Mp7002NESES_ObjectIdentity = ObjectIdentity
mp7002NESES = _Mp7002NESES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 13)
)
_Mp7002NEUAS_ObjectIdentity = ObjectIdentity
mp7002NEUAS = _Mp7002NEUAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 14)
)
_Mp7002FEES_ObjectIdentity = ObjectIdentity
mp7002FEES = _Mp7002FEES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 15)
)
_Mp7002FEBBE_ObjectIdentity = ObjectIdentity
mp7002FEBBE = _Mp7002FEBBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 16)
)
_Mp7002FESES_ObjectIdentity = ObjectIdentity
mp7002FESES = _Mp7002FESES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 17)
)
_Mp7002FEUAS_ObjectIdentity = ObjectIdentity
mp7002FEUAS = _Mp7002FEUAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 18)
)
_Mp7002RAI_ObjectIdentity = ObjectIdentity
mp7002RAI = _Mp7002RAI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 1, 19)
)
_Mp7002NearEndAlarmConfigTable_Object = MibTable
mp7002NearEndAlarmConfigTable = _Mp7002NearEndAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2)
)
if mibBuilder.loadTexts:
    mp7002NearEndAlarmConfigTable.setStatus("mandatory")
_Mp7002NearEndAlarmConfigEntry_Object = MibTableRow
mp7002NearEndAlarmConfigEntry = _Mp7002NearEndAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2, 1)
)
mp7002NearEndAlarmConfigEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002NearEndAlarmConfigIndex"),
    (0, "GDCMP7002-MIB", "mp7002NearEndAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    mp7002NearEndAlarmConfigEntry.setStatus("mandatory")
_Mp7002NearEndAlarmConfigIndex_Type = SCinstance
_Mp7002NearEndAlarmConfigIndex_Object = MibTableColumn
mp7002NearEndAlarmConfigIndex = _Mp7002NearEndAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2, 1, 1),
    _Mp7002NearEndAlarmConfigIndex_Type()
)
mp7002NearEndAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndAlarmConfigIndex.setStatus("mandatory")
_Mp7002NearEndAlarmConfigIdentifier_Type = ObjectIdentifier
_Mp7002NearEndAlarmConfigIdentifier_Object = MibTableColumn
mp7002NearEndAlarmConfigIdentifier = _Mp7002NearEndAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2, 1, 2),
    _Mp7002NearEndAlarmConfigIdentifier_Type()
)
mp7002NearEndAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002NearEndAlarmConfigIdentifier.setStatus("mandatory")


class _Mp7002NearEndAlarmCountWindow_Type(Integer32):
    """Custom type mp7002NearEndAlarmCountWindow based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("infinite", 9),
          ("last10sec", 3),
          ("last15min", 6),
          ("last1hr", 7),
          ("last1min", 5),
          ("last1sec", 2),
          ("last24hr", 8),
          ("last30sec", 4))
    )


_Mp7002NearEndAlarmCountWindow_Type.__name__ = "Integer32"
_Mp7002NearEndAlarmCountWindow_Object = MibTableColumn
mp7002NearEndAlarmCountWindow = _Mp7002NearEndAlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2, 1, 3),
    _Mp7002NearEndAlarmCountWindow_Type()
)
mp7002NearEndAlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002NearEndAlarmCountWindow.setStatus("mandatory")


class _Mp7002NearEndAlarmCountThreshold_Type(Integer32):
    """Custom type mp7002NearEndAlarmCountThreshold based on Integer32"""
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
        *(("thresGT1", 1),
          ("thresGT10", 3),
          ("thresGT100", 4),
          ("thresGT1000", 5),
          ("thresGT10000", 6),
          ("thresGT3", 2))
    )


_Mp7002NearEndAlarmCountThreshold_Type.__name__ = "Integer32"
_Mp7002NearEndAlarmCountThreshold_Object = MibTableColumn
mp7002NearEndAlarmCountThreshold = _Mp7002NearEndAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 2, 1, 4),
    _Mp7002NearEndAlarmCountThreshold_Type()
)
mp7002NearEndAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002NearEndAlarmCountThreshold.setStatus("mandatory")
_Mp7002FarEndAlarmConfigTable_Object = MibTable
mp7002FarEndAlarmConfigTable = _Mp7002FarEndAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3)
)
if mibBuilder.loadTexts:
    mp7002FarEndAlarmConfigTable.setStatus("mandatory")
_Mp7002FarEndAlarmConfigEntry_Object = MibTableRow
mp7002FarEndAlarmConfigEntry = _Mp7002FarEndAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3, 1)
)
mp7002FarEndAlarmConfigEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002FarEndAlarmConfigIndex"),
    (0, "GDCMP7002-MIB", "mp7002FarEndAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    mp7002FarEndAlarmConfigEntry.setStatus("mandatory")
_Mp7002FarEndAlarmConfigIndex_Type = SCinstance
_Mp7002FarEndAlarmConfigIndex_Object = MibTableColumn
mp7002FarEndAlarmConfigIndex = _Mp7002FarEndAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3, 1, 1),
    _Mp7002FarEndAlarmConfigIndex_Type()
)
mp7002FarEndAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndAlarmConfigIndex.setStatus("mandatory")
_Mp7002FarEndAlarmConfigIdentifier_Type = ObjectIdentifier
_Mp7002FarEndAlarmConfigIdentifier_Object = MibTableColumn
mp7002FarEndAlarmConfigIdentifier = _Mp7002FarEndAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3, 1, 2),
    _Mp7002FarEndAlarmConfigIdentifier_Type()
)
mp7002FarEndAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002FarEndAlarmConfigIdentifier.setStatus("mandatory")


class _Mp7002FarEndAlarmCountWindow_Type(Integer32):
    """Custom type mp7002FarEndAlarmCountWindow based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("infinite", 9),
          ("last10sec", 3),
          ("last15min", 6),
          ("last1hr", 7),
          ("last1min", 5),
          ("last1sec", 2),
          ("last24hr", 8),
          ("last30sec", 4))
    )


_Mp7002FarEndAlarmCountWindow_Type.__name__ = "Integer32"
_Mp7002FarEndAlarmCountWindow_Object = MibTableColumn
mp7002FarEndAlarmCountWindow = _Mp7002FarEndAlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3, 1, 3),
    _Mp7002FarEndAlarmCountWindow_Type()
)
mp7002FarEndAlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002FarEndAlarmCountWindow.setStatus("mandatory")


class _Mp7002FarEndAlarmCountThreshold_Type(Integer32):
    """Custom type mp7002FarEndAlarmCountThreshold based on Integer32"""
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
        *(("thresGT1", 1),
          ("thresGT10", 3),
          ("thresGT100", 4),
          ("thresGT1000", 5),
          ("thresGT10000", 6),
          ("thresGT3", 2))
    )


_Mp7002FarEndAlarmCountThreshold_Type.__name__ = "Integer32"
_Mp7002FarEndAlarmCountThreshold_Object = MibTableColumn
mp7002FarEndAlarmCountThreshold = _Mp7002FarEndAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 3, 1, 4),
    _Mp7002FarEndAlarmCountThreshold_Type()
)
mp7002FarEndAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002FarEndAlarmCountThreshold.setStatus("mandatory")
_Mp7002LocalAlarmConfigTable_Object = MibTable
mp7002LocalAlarmConfigTable = _Mp7002LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4)
)
if mibBuilder.loadTexts:
    mp7002LocalAlarmConfigTable.setStatus("mandatory")
_Mp7002LocalAlarmConfigEntry_Object = MibTableRow
mp7002LocalAlarmConfigEntry = _Mp7002LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1)
)
mp7002LocalAlarmConfigEntry.setIndexNames(
    (0, "GDCMP7002-MIB", "mp7002LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    mp7002LocalAlarmConfigEntry.setStatus("mandatory")
_Mp7002LocalAlarmConfigIndex_Type = SCinstance
_Mp7002LocalAlarmConfigIndex_Object = MibTableColumn
mp7002LocalAlarmConfigIndex = _Mp7002LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 1),
    _Mp7002LocalAlarmConfigIndex_Type()
)
mp7002LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp7002LocalAlarmConfigIndex.setStatus("mandatory")


class _Mp7002UASNE_Type(Integer32):
    """Custom type mp7002UASNE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002UASNE_Type.__name__ = "Integer32"
_Mp7002UASNE_Object = MibTableColumn
mp7002UASNE = _Mp7002UASNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 2),
    _Mp7002UASNE_Type()
)
mp7002UASNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002UASNE.setStatus("mandatory")


class _Mp7002SESNE_Type(Integer32):
    """Custom type mp7002SESNE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002SESNE_Type.__name__ = "Integer32"
_Mp7002SESNE_Object = MibTableColumn
mp7002SESNE = _Mp7002SESNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 3),
    _Mp7002SESNE_Type()
)
mp7002SESNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002SESNE.setStatus("mandatory")


class _Mp7002BBENE_Type(Integer32):
    """Custom type mp7002BBENE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002BBENE_Type.__name__ = "Integer32"
_Mp7002BBENE_Object = MibTableColumn
mp7002BBENE = _Mp7002BBENE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 4),
    _Mp7002BBENE_Type()
)
mp7002BBENE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002BBENE.setStatus("mandatory")


class _Mp7002ESNE_Type(Integer32):
    """Custom type mp7002ESNE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002ESNE_Type.__name__ = "Integer32"
_Mp7002ESNE_Object = MibTableColumn
mp7002ESNE = _Mp7002ESNE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 5),
    _Mp7002ESNE_Type()
)
mp7002ESNE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002ESNE.setStatus("mandatory")


class _Mp7002UASFE_Type(Integer32):
    """Custom type mp7002UASFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002UASFE_Type.__name__ = "Integer32"
_Mp7002UASFE_Object = MibTableColumn
mp7002UASFE = _Mp7002UASFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 6),
    _Mp7002UASFE_Type()
)
mp7002UASFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002UASFE.setStatus("mandatory")


class _Mp7002SESFE_Type(Integer32):
    """Custom type mp7002SESFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002SESFE_Type.__name__ = "Integer32"
_Mp7002SESFE_Object = MibTableColumn
mp7002SESFE = _Mp7002SESFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 7),
    _Mp7002SESFE_Type()
)
mp7002SESFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002SESFE.setStatus("mandatory")


class _Mp7002BBEFE_Type(Integer32):
    """Custom type mp7002BBEFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002BBEFE_Type.__name__ = "Integer32"
_Mp7002BBEFE_Object = MibTableColumn
mp7002BBEFE = _Mp7002BBEFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 8),
    _Mp7002BBEFE_Type()
)
mp7002BBEFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002BBEFE.setStatus("mandatory")


class _Mp7002ESFE_Type(Integer32):
    """Custom type mp7002ESFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002ESFE_Type.__name__ = "Integer32"
_Mp7002ESFE_Object = MibTableColumn
mp7002ESFE = _Mp7002ESFE_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 9),
    _Mp7002ESFE_Type()
)
mp7002ESFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002ESFE.setStatus("mandatory")


class _Mp7002LOS_Type(Integer32):
    """Custom type mp7002LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002LOS_Type.__name__ = "Integer32"
_Mp7002LOS_Object = MibTableColumn
mp7002LOS = _Mp7002LOS_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 10),
    _Mp7002LOS_Type()
)
mp7002LOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002LOS.setStatus("mandatory")


class _Mp7002LOF_Type(Integer32):
    """Custom type mp7002LOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002LOF_Type.__name__ = "Integer32"
_Mp7002LOF_Object = MibTableColumn
mp7002LOF = _Mp7002LOF_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 11),
    _Mp7002LOF_Type()
)
mp7002LOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002LOF.setStatus("mandatory")


class _Mp7002AIS_Type(Integer32):
    """Custom type mp7002AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002AIS_Type.__name__ = "Integer32"
_Mp7002AIS_Object = MibTableColumn
mp7002AIS = _Mp7002AIS_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 12),
    _Mp7002AIS_Type()
)
mp7002AIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002AIS.setStatus("mandatory")


class _Mp7002TmgLoss_Type(Integer32):
    """Custom type mp7002TmgLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002TmgLoss_Type.__name__ = "Integer32"
_Mp7002TmgLoss_Object = MibTableColumn
mp7002TmgLoss = _Mp7002TmgLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 13),
    _Mp7002TmgLoss_Type()
)
mp7002TmgLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002TmgLoss.setStatus("mandatory")


class _Mp7002LCVs_Type(Integer32):
    """Custom type mp7002LCVs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002LCVs_Type.__name__ = "Integer32"
_Mp7002LCVs_Object = MibTableColumn
mp7002LCVs = _Mp7002LCVs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 14),
    _Mp7002LCVs_Type()
)
mp7002LCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002LCVs.setStatus("mandatory")


class _Mp7002NtwkRAI_Type(Integer32):
    """Custom type mp7002NtwkRAI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Mp7002NtwkRAI_Type.__name__ = "Integer32"
_Mp7002NtwkRAI_Object = MibTableColumn
mp7002NtwkRAI = _Mp7002NtwkRAI_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 9, 4, 1, 15),
    _Mp7002NtwkRAI_Type()
)
mp7002NtwkRAI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mp7002NtwkRAI.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCMP7002-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "mp7002System": mp7002System,
       "mp7002Version": mp7002Version,
       "mp7002MIBversion": mp7002MIBversion,
       "mp7002VersionTable": mp7002VersionTable,
       "mp7002VersionEntry": mp7002VersionEntry,
       "mp7002VersionIndex": mp7002VersionIndex,
       "mp7002FirmwareRev": mp7002FirmwareRev,
       "mp7002ModelNumber": mp7002ModelNumber,
       "mp7002E1x": mp7002E1x,
       "mp7002Maintenance": mp7002Maintenance,
       "mp7002MaintenanceTable": mp7002MaintenanceTable,
       "mp7002MaintenanceEntry": mp7002MaintenanceEntry,
       "mp7002MaintenanceLineIndex": mp7002MaintenanceLineIndex,
       "mp7002SoftReset": mp7002SoftReset,
       "mp7002SysUpTime": mp7002SysUpTime,
       "mp7002DefaultInit": mp7002DefaultInit,
       "mp7002ResetStats": mp7002ResetStats,
       "mp7002LedStatus": mp7002LedStatus,
       "mp7002E1Circuit": mp7002E1Circuit,
       "mp7002E1XCircuit": mp7002E1XCircuit,
       "mp7002TSBundle1Name": mp7002TSBundle1Name,
       "mp7002TSBundle2Name": mp7002TSBundle2Name,
       "mp7002SetRealTime": mp7002SetRealTime,
       "mp7002AlarmStatus": mp7002AlarmStatus,
       "mp7002SystemTimingGenStatus": mp7002SystemTimingGenStatus,
       "mp7002FarEndResetStats": mp7002FarEndResetStats,
       "mp7002NearEndStatLastInitialized": mp7002NearEndStatLastInitialized,
       "mp7002FarEndStatLastInitialized": mp7002FarEndStatLastInitialized,
       "mp7002Configuration": mp7002Configuration,
       "mp7002ConfigTable": mp7002ConfigTable,
       "mp7002ConfigEntry": mp7002ConfigEntry,
       "mp7002ConfigIndex": mp7002ConfigIndex,
       "mp7002InterfaceType": mp7002InterfaceType,
       "mp7002RcvrRange": mp7002RcvrRange,
       "mp7002TransmitClockSource": mp7002TransmitClockSource,
       "mp7002FallbackClockSource": mp7002FallbackClockSource,
       "mp7002FacilityDataLink": mp7002FacilityDataLink,
       "mp7002NearEndValidIntervals": mp7002NearEndValidIntervals,
       "mp7002FarEndValidIntervals": mp7002FarEndValidIntervals,
       "mp7002NetworkConnection": mp7002NetworkConnection,
       "mp7002Framing": mp7002Framing,
       "mp7002LineCoding": mp7002LineCoding,
       "mp7002DCCConfigurationTable": mp7002DCCConfigurationTable,
       "mp7002DCCConfigurationEntry": mp7002DCCConfigurationEntry,
       "mp7002DCCConfigurationIndex": mp7002DCCConfigurationIndex,
       "mp7002TimeSlot": mp7002TimeSlot,
       "mp7002Bandwidth": mp7002Bandwidth,
       "mp7002Diagnostics": mp7002Diagnostics,
       "mp7002DiagTable": mp7002DiagTable,
       "mp7002DiagEntry": mp7002DiagEntry,
       "mp7002DiagIndex": mp7002DiagIndex,
       "mp7002TestPattern": mp7002TestPattern,
       "mp7002DiagConfig": mp7002DiagConfig,
       "mp7002TestLimit": mp7002TestLimit,
       "mp7002TestExecutionStatus": mp7002TestExecutionStatus,
       "mp7002TestExceptions": mp7002TestExceptions,
       "mp7002TestResults": mp7002TestResults,
       "mp7002ResetTestResults": mp7002ResetTestResults,
       "mp7002Performance": mp7002Performance,
       "mp7002NearEndCurrent15MinTable": mp7002NearEndCurrent15MinTable,
       "mp7002NearEndCurrent15MinEntry": mp7002NearEndCurrent15MinEntry,
       "mp7002NearEndCurrent15MinIndex": mp7002NearEndCurrent15MinIndex,
       "mp7002NearEndCurrent15MinStat": mp7002NearEndCurrent15MinStat,
       "mp7002NearEndIntervalTable": mp7002NearEndIntervalTable,
       "mp7002NearEndIntervalEntry": mp7002NearEndIntervalEntry,
       "mp7002NearEndIntervalIndex": mp7002NearEndIntervalIndex,
       "mp7002NearEndIntervalNumber": mp7002NearEndIntervalNumber,
       "mp7002NearEndIntervalStat": mp7002NearEndIntervalStat,
       "mp7002NearEndCurrent24HrTable": mp7002NearEndCurrent24HrTable,
       "mp7002NearEndCurrent24HrEntry": mp7002NearEndCurrent24HrEntry,
       "mp7002NearEndCurrent24HrIndex": mp7002NearEndCurrent24HrIndex,
       "mp7002NearEndCurrent24HrStat": mp7002NearEndCurrent24HrStat,
       "mp7002NearEndRecent24HrTable": mp7002NearEndRecent24HrTable,
       "mp7002NearEndRecent24HrEntry": mp7002NearEndRecent24HrEntry,
       "mp7002NearEndRecent24HrIndex": mp7002NearEndRecent24HrIndex,
       "mp7002NearEndRecent24HrStat": mp7002NearEndRecent24HrStat,
       "mp7002FarEndCurrent15MinTable": mp7002FarEndCurrent15MinTable,
       "mp7002FarEndCurrent15MinEntry": mp7002FarEndCurrent15MinEntry,
       "mp7002FarEndCurrent15MinIndex": mp7002FarEndCurrent15MinIndex,
       "mp7002FarEndCurrent15MinStat": mp7002FarEndCurrent15MinStat,
       "mp7002FarEndIntervalTable": mp7002FarEndIntervalTable,
       "mp7002FarEndIntervalEntry": mp7002FarEndIntervalEntry,
       "mp7002FarEndIntervalIndex": mp7002FarEndIntervalIndex,
       "mp7002FarEndIntervalNumber": mp7002FarEndIntervalNumber,
       "mp7002FarEndIntervalStat": mp7002FarEndIntervalStat,
       "mp7002CurrentFarEnd24HrTable": mp7002CurrentFarEnd24HrTable,
       "mp7002CurrentFarEnd24HrEntry": mp7002CurrentFarEnd24HrEntry,
       "mp7002CurrentFarEnd24HrIndex": mp7002CurrentFarEnd24HrIndex,
       "mp7002CurrentFarEnd24HrStat": mp7002CurrentFarEnd24HrStat,
       "mp7002RecentFarEnd24HrTable": mp7002RecentFarEnd24HrTable,
       "mp7002RecentFarEnd24HrEntry": mp7002RecentFarEnd24HrEntry,
       "mp7002RecentFarEnd24HrIndex": mp7002RecentFarEnd24HrIndex,
       "mp7002RecentFarEnd24HrStat": mp7002RecentFarEnd24HrStat,
       "mp7002UnavailableTimeRegTable": mp7002UnavailableTimeRegTable,
       "mp7002UnavailableTimeRegEntry": mp7002UnavailableTimeRegEntry,
       "mp7002UnavailableTimeRegIndex": mp7002UnavailableTimeRegIndex,
       "mp7002UnavailableTimeRegNumber": mp7002UnavailableTimeRegNumber,
       "mp7002UnavailableTimeRegStart": mp7002UnavailableTimeRegStart,
       "mp7002UnavailableTimeRegStop": mp7002UnavailableTimeRegStop,
       "mp7002FarEndUnavailableTimeRegTable": mp7002FarEndUnavailableTimeRegTable,
       "mp7002FarEndUnavailableTimeRegEntry": mp7002FarEndUnavailableTimeRegEntry,
       "mp7002FarEndUnavailableTimeRegIndex": mp7002FarEndUnavailableTimeRegIndex,
       "mp7002FarEndUnavailableTimeRegNumber": mp7002FarEndUnavailableTimeRegNumber,
       "mp7002FarEndUnavailableTimeRegStart": mp7002FarEndUnavailableTimeRegStart,
       "mp7002FarEndUnavailableTimeRegStop": mp7002FarEndUnavailableTimeRegStop,
       "mp7002SysConfig": mp7002SysConfig,
       "mp7002SysTimingTable": mp7002SysTimingTable,
       "mp7002SysTimingEntry": mp7002SysTimingEntry,
       "mp7002SysTimingIndex": mp7002SysTimingIndex,
       "mp7002SysTimingGen": mp7002SysTimingGen,
       "mp7002HighwayAssignTable": mp7002HighwayAssignTable,
       "mp7002HighwayAssignEntry": mp7002HighwayAssignEntry,
       "mp7002HighwayAssignIndex": mp7002HighwayAssignIndex,
       "mp7002TimeSlotBundle": mp7002TimeSlotBundle,
       "mp7002StartTimeSlot": mp7002StartTimeSlot,
       "mp7002NumberOfTimeSlots": mp7002NumberOfTimeSlots,
       "mp7002BundleDestination": mp7002BundleDestination,
       "mp7002ExecuteAssign": mp7002ExecuteAssign,
       "mp7002Alarms": mp7002Alarms,
       "mp7002AlarmData": mp7002AlarmData,
       "mp7002NoResponseAlm": mp7002NoResponseAlm,
       "mp7002DiagRxErrAlm": mp7002DiagRxErrAlm,
       "mp7002PowerUpAlm": mp7002PowerUpAlm,
       "mp7002NvRamCorrupt": mp7002NvRamCorrupt,
       "mp7002UnitFailure": mp7002UnitFailure,
       "mp7002TimingLoss": mp7002TimingLoss,
       "mp7002LCV": mp7002LCV,
       "mp7002LossOfSignal": mp7002LossOfSignal,
       "mp7002LossOfFrame": mp7002LossOfFrame,
       "mp7002AlarmIndSignal": mp7002AlarmIndSignal,
       "mp7002NEES": mp7002NEES,
       "mp7002NEBBE": mp7002NEBBE,
       "mp7002NESES": mp7002NESES,
       "mp7002NEUAS": mp7002NEUAS,
       "mp7002FEES": mp7002FEES,
       "mp7002FEBBE": mp7002FEBBE,
       "mp7002FESES": mp7002FESES,
       "mp7002FEUAS": mp7002FEUAS,
       "mp7002RAI": mp7002RAI,
       "mp7002NearEndAlarmConfigTable": mp7002NearEndAlarmConfigTable,
       "mp7002NearEndAlarmConfigEntry": mp7002NearEndAlarmConfigEntry,
       "mp7002NearEndAlarmConfigIndex": mp7002NearEndAlarmConfigIndex,
       "mp7002NearEndAlarmConfigIdentifier": mp7002NearEndAlarmConfigIdentifier,
       "mp7002NearEndAlarmCountWindow": mp7002NearEndAlarmCountWindow,
       "mp7002NearEndAlarmCountThreshold": mp7002NearEndAlarmCountThreshold,
       "mp7002FarEndAlarmConfigTable": mp7002FarEndAlarmConfigTable,
       "mp7002FarEndAlarmConfigEntry": mp7002FarEndAlarmConfigEntry,
       "mp7002FarEndAlarmConfigIndex": mp7002FarEndAlarmConfigIndex,
       "mp7002FarEndAlarmConfigIdentifier": mp7002FarEndAlarmConfigIdentifier,
       "mp7002FarEndAlarmCountWindow": mp7002FarEndAlarmCountWindow,
       "mp7002FarEndAlarmCountThreshold": mp7002FarEndAlarmCountThreshold,
       "mp7002LocalAlarmConfigTable": mp7002LocalAlarmConfigTable,
       "mp7002LocalAlarmConfigEntry": mp7002LocalAlarmConfigEntry,
       "mp7002LocalAlarmConfigIndex": mp7002LocalAlarmConfigIndex,
       "mp7002UASNE": mp7002UASNE,
       "mp7002SESNE": mp7002SESNE,
       "mp7002BBENE": mp7002BBENE,
       "mp7002ESNE": mp7002ESNE,
       "mp7002UASFE": mp7002UASFE,
       "mp7002SESFE": mp7002SESFE,
       "mp7002BBEFE": mp7002BBEFE,
       "mp7002ESFE": mp7002ESFE,
       "mp7002LOS": mp7002LOS,
       "mp7002LOF": mp7002LOF,
       "mp7002AIS": mp7002AIS,
       "mp7002TmgLoss": mp7002TmgLoss,
       "mp7002LCVs": mp7002LCVs,
       "mp7002NtwkRAI": mp7002NtwkRAI}
)
