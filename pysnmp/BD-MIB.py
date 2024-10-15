# SNMP MIB module (BD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:31 2024
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

(bcsiModules,
 fcSwitch) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules",
    "fcSwitch")

(SwPortIndex,) = mibBuilder.importSymbols(
    "Brocade-TC",
    "SwPortIndex")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(swVfId,) = mibBuilder.importSymbols(
    "SW-MIB",
    "swVfId")


# MODULE-IDENTITY

bd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congestion", 1),
          ("latency", 2))
    )



# MIB Managed Objects in the order of their OIDs

_BdTraps_ObjectIdentity = ObjectIdentity
bdTraps = _BdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0)
)
if mibBuilder.loadTexts:
    bdTraps.setStatus("current")
_BdConfig_ObjectIdentity = ObjectIdentity
bdConfig = _BdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1)
)
if mibBuilder.loadTexts:
    bdConfig.setStatus("current")
_BdStatus_Type = TruthValue
_BdStatus_Object = MibScalar
bdStatus = _BdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 1),
    _BdStatus_Type()
)
bdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdStatus.setStatus("current")


class _BdLThreshold_Type(DisplayString):
    """Custom type bdLThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdLThreshold_Type.__name__ = "DisplayString"
_BdLThreshold_Object = MibScalar
bdLThreshold = _BdLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 2),
    _BdLThreshold_Type()
)
bdLThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdLThreshold.setStatus("current")


class _BdCThreshold_Type(DisplayString):
    """Custom type bdCThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdCThreshold_Type.__name__ = "DisplayString"
_BdCThreshold_Object = MibScalar
bdCThreshold = _BdCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 3),
    _BdCThreshold_Type()
)
bdCThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdCThreshold.setStatus("current")


class _BdQTime_Type(Integer32):
    """Custom type bdQTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_BdQTime_Type.__name__ = "Integer32"
_BdQTime_Object = MibScalar
bdQTime = _BdQTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 4),
    _BdQTime_Type()
)
bdQTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdQTime.setStatus("current")
if mibBuilder.loadTexts:
    bdQTime.setUnits("seconds")


class _BdWinAvgTime_Type(Integer32):
    """Custom type bdWinAvgTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BdWinAvgTime_Type.__name__ = "Integer32"
_BdWinAvgTime_Object = MibScalar
bdWinAvgTime = _BdWinAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 5),
    _BdWinAvgTime_Type()
)
bdWinAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdWinAvgTime.setStatus("current")
if mibBuilder.loadTexts:
    bdWinAvgTime.setUnits("seconds")


class _BdThreshold_Type(DisplayString):
    """Custom type bdThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdThreshold_Type.__name__ = "DisplayString"
_BdThreshold_Object = MibScalar
bdThreshold = _BdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 6),
    _BdThreshold_Type()
)
bdThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bdThreshold.setStatus("current")
_NBdType_Type = BdType
_NBdType_Object = MibScalar
nBdType = _NBdType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 1, 7),
    _NBdType_Type()
)
nBdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nBdType.setStatus("current")
_BdStats_ObjectIdentity = ObjectIdentity
bdStats = _BdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2)
)
if mibBuilder.loadTexts:
    bdStats.setStatus("current")
_BdNumOfEntries_Type = Integer32
_BdNumOfEntries_Object = MibScalar
bdNumOfEntries = _BdNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 1),
    _BdNumOfEntries_Type()
)
bdNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdNumOfEntries.setStatus("current")
_BdStatsTable_Object = MibTable
bdStatsTable = _BdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2)
)
if mibBuilder.loadTexts:
    bdStatsTable.setStatus("current")
_BdStatsEntry_Object = MibTableRow
bdStatsEntry = _BdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1)
)
bdStatsEntry.setIndexNames(
    (0, "BD-MIB", "userPortNumber"),
    (0, "BD-MIB", "bdType"),
    (0, "BD-MIB", "bdSampleTime"),
)
if mibBuilder.loadTexts:
    bdStatsEntry.setStatus("current")
_UserPortNumber_Type = SwPortIndex
_UserPortNumber_Object = MibTableColumn
userPortNumber = _UserPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 1),
    _UserPortNumber_Type()
)
userPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPortNumber.setStatus("current")
_BdSampleTime_Type = Unsigned32
_BdSampleTime_Object = MibTableColumn
bdSampleTime = _BdSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 2),
    _BdSampleTime_Type()
)
bdSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdSampleTime.setStatus("current")
if mibBuilder.loadTexts:
    bdSampleTime.setUnits("seconds")
_BdType_Type = BdType
_BdType_Object = MibTableColumn
bdType = _BdType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 3),
    _BdType_Type()
)
bdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdType.setStatus("current")


class _BdStatsValue10SecsSample_Type(DisplayString):
    """Custom type bdStatsValue10SecsSample based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdStatsValue10SecsSample_Type.__name__ = "DisplayString"
_BdStatsValue10SecsSample_Object = MibTableColumn
bdStatsValue10SecsSample = _BdStatsValue10SecsSample_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 4),
    _BdStatsValue10SecsSample_Type()
)
bdStatsValue10SecsSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdStatsValue10SecsSample.setStatus("current")


class _BdStatsValue60SecsSample_Type(DisplayString):
    """Custom type bdStatsValue60SecsSample based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdStatsValue60SecsSample_Type.__name__ = "DisplayString"
_BdStatsValue60SecsSample_Object = MibTableColumn
bdStatsValue60SecsSample = _BdStatsValue60SecsSample_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 5),
    _BdStatsValue60SecsSample_Type()
)
bdStatsValue60SecsSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdStatsValue60SecsSample.setStatus("current")


class _BdStatsValue300SecsSample_Type(DisplayString):
    """Custom type bdStatsValue300SecsSample based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_BdStatsValue300SecsSample_Type.__name__ = "DisplayString"
_BdStatsValue300SecsSample_Object = MibTableColumn
bdStatsValue300SecsSample = _BdStatsValue300SecsSample_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 2, 1, 6),
    _BdStatsValue300SecsSample_Type()
)
bdStatsValue300SecsSample.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdStatsValue300SecsSample.setStatus("current")


class _BdAggrStats_Type(DisplayString):
    """Custom type bdAggrStats based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_BdAggrStats_Type.__name__ = "DisplayString"
_BdAggrStats_Object = MibScalar
bdAggrStats = _BdAggrStats_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 3),
    _BdAggrStats_Type()
)
bdAggrStats.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bdAggrStats.setStatus("current")


class _BdAbsoluteValue_Type(Integer32):
    """Custom type bdAbsoluteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_BdAbsoluteValue_Type.__name__ = "Integer32"
_BdAbsoluteValue_Object = MibScalar
bdAbsoluteValue = _BdAbsoluteValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 4),
    _BdAbsoluteValue_Type()
)
bdAbsoluteValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bdAbsoluteValue.setStatus("current")
_BdAvgFrameSize_Type = Unsigned32
_BdAvgFrameSize_Object = MibScalar
bdAvgFrameSize = _BdAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 2, 5),
    _BdAvgFrameSize_Type()
)
bdAvgFrameSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bdAvgFrameSize.setStatus("current")

# Managed Objects groups


# Notification objects

bdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0, 1)
)
bdTrap.setObjects(
      *(("BD-MIB", "userPortNumber"),
        ("BD-MIB", "bdWinAvgTime"),
        ("BD-MIB", "nBdType"),
        ("BD-MIB", "bdThreshold"),
        ("BD-MIB", "bdAggrStats"),
        ("BD-MIB", "bdAbsoluteValue"),
        ("SW-MIB", "swVfId"),
        ("BD-MIB", "bdAvgFrameSize"))
)
if mibBuilder.loadTexts:
    bdTrap.setStatus(
        "current"
    )

bdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 51, 0, 2)
)
bdClearTrap.setObjects(
      *(("BD-MIB", "userPortNumber"),
        ("BD-MIB", "bdWinAvgTime"),
        ("BD-MIB", "nBdType"),
        ("BD-MIB", "bdThreshold"),
        ("BD-MIB", "bdAggrStats"),
        ("BD-MIB", "bdAbsoluteValue"),
        ("SW-MIB", "swVfId"),
        ("BD-MIB", "bdAvgFrameSize"))
)
if mibBuilder.loadTexts:
    bdClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BD-MIB",
    **{"BdType": BdType,
       "bd": bd,
       "bdTraps": bdTraps,
       "bdTrap": bdTrap,
       "bdClearTrap": bdClearTrap,
       "bdConfig": bdConfig,
       "bdStatus": bdStatus,
       "bdLThreshold": bdLThreshold,
       "bdCThreshold": bdCThreshold,
       "bdQTime": bdQTime,
       "bdWinAvgTime": bdWinAvgTime,
       "bdThreshold": bdThreshold,
       "nBdType": nBdType,
       "bdStats": bdStats,
       "bdNumOfEntries": bdNumOfEntries,
       "bdStatsTable": bdStatsTable,
       "bdStatsEntry": bdStatsEntry,
       "userPortNumber": userPortNumber,
       "bdSampleTime": bdSampleTime,
       "bdType": bdType,
       "bdStatsValue10SecsSample": bdStatsValue10SecsSample,
       "bdStatsValue60SecsSample": bdStatsValue60SecsSample,
       "bdStatsValue300SecsSample": bdStatsValue300SecsSample,
       "bdAggrStats": bdAggrStats,
       "bdAbsoluteValue": bdAbsoluteValue,
       "bdAvgFrameSize": bdAvgFrameSize}
)
