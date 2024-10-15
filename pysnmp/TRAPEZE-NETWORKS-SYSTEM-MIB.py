# SNMP MIB module (TRAPEZE-NETWORKS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:38 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8)
)
trpzSystemMib.setRevisions(
        ("2007-08-14 00:12",
         "2007-05-04 00:10",
         "2007-03-14 00:07",
         "2006-11-09 00:04",
         "2006-06-06 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzSysCpuLoad(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TrpzSysMemoryAmount(Unsigned32, TextualConvention):
    status = "current"


class TrpzSysPowerSupplyStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("ac-failed", 3),
          ("ac-ok-dc-ok", 5),
          ("dc-failed", 4),
          ("other", 1),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzSysObjects_ObjectIdentity = ObjectIdentity
trpzSysObjects = _TrpzSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1)
)
_TrpzSysDataObjects_ObjectIdentity = ObjectIdentity
trpzSysDataObjects = _TrpzSysDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1)
)
_TrpzSysCpuMemoryUsedBytes_Type = Unsigned32
_TrpzSysCpuMemoryUsedBytes_Object = MibScalar
trpzSysCpuMemoryUsedBytes = _TrpzSysCpuMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 1),
    _TrpzSysCpuMemoryUsedBytes_Type()
)
trpzSysCpuMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryUsedBytes.setStatus("obsolete")
_TrpzSysCpuMemoryTotalBytes_Type = Unsigned32
_TrpzSysCpuMemoryTotalBytes_Object = MibScalar
trpzSysCpuMemoryTotalBytes = _TrpzSysCpuMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 2),
    _TrpzSysCpuMemoryTotalBytes_Type()
)
trpzSysCpuMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryTotalBytes.setStatus("obsolete")
_TrpzSysFlashMemoryUsedBytes_Type = Unsigned32
_TrpzSysFlashMemoryUsedBytes_Object = MibScalar
trpzSysFlashMemoryUsedBytes = _TrpzSysFlashMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 3),
    _TrpzSysFlashMemoryUsedBytes_Type()
)
trpzSysFlashMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysFlashMemoryUsedBytes.setStatus("current")
_TrpzSysFlashMemoryTotalBytes_Type = Unsigned32
_TrpzSysFlashMemoryTotalBytes_Object = MibScalar
trpzSysFlashMemoryTotalBytes = _TrpzSysFlashMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 4),
    _TrpzSysFlashMemoryTotalBytes_Type()
)
trpzSysFlashMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysFlashMemoryTotalBytes.setStatus("current")
_TrpzSysCpuAverageLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuAverageLoad_Object = MibScalar
trpzSysCpuAverageLoad = _TrpzSysCpuAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 5),
    _TrpzSysCpuAverageLoad_Type()
)
trpzSysCpuAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuAverageLoad.setStatus("current")
_TrpzSysCpuMemorySize_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemorySize_Object = MibScalar
trpzSysCpuMemorySize = _TrpzSysCpuMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 6),
    _TrpzSysCpuMemorySize_Type()
)
trpzSysCpuMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemorySize.setStatus("current")
_TrpzSysCpuLoadDetail_ObjectIdentity = ObjectIdentity
trpzSysCpuLoadDetail = _TrpzSysCpuLoadDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11)
)
_TrpzSysCpuInstantLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuInstantLoad_Object = MibScalar
trpzSysCpuInstantLoad = _TrpzSysCpuInstantLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 1),
    _TrpzSysCpuInstantLoad_Type()
)
trpzSysCpuInstantLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuInstantLoad.setStatus("current")
_TrpzSysCpuLastMinuteLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuLastMinuteLoad_Object = MibScalar
trpzSysCpuLastMinuteLoad = _TrpzSysCpuLastMinuteLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 2),
    _TrpzSysCpuLastMinuteLoad_Type()
)
trpzSysCpuLastMinuteLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuLastMinuteLoad.setStatus("current")
_TrpzSysCpuLast5MinutesLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuLast5MinutesLoad_Object = MibScalar
trpzSysCpuLast5MinutesLoad = _TrpzSysCpuLast5MinutesLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 3),
    _TrpzSysCpuLast5MinutesLoad_Type()
)
trpzSysCpuLast5MinutesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuLast5MinutesLoad.setStatus("current")
_TrpzSysCpuLastHourLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuLastHourLoad_Object = MibScalar
trpzSysCpuLastHourLoad = _TrpzSysCpuLastHourLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 4),
    _TrpzSysCpuLastHourLoad_Type()
)
trpzSysCpuLastHourLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuLastHourLoad.setStatus("current")
_TrpzSysCpuLastDayLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuLastDayLoad_Object = MibScalar
trpzSysCpuLastDayLoad = _TrpzSysCpuLastDayLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 5),
    _TrpzSysCpuLastDayLoad_Type()
)
trpzSysCpuLastDayLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuLastDayLoad.setStatus("current")
_TrpzSysCpuLast3DaysLoad_Type = TrpzSysCpuLoad
_TrpzSysCpuLast3DaysLoad_Object = MibScalar
trpzSysCpuLast3DaysLoad = _TrpzSysCpuLast3DaysLoad_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 11, 6),
    _TrpzSysCpuLast3DaysLoad_Type()
)
trpzSysCpuLast3DaysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuLast3DaysLoad.setStatus("current")
_TrpzSysCpuMemoryUsageDetail_ObjectIdentity = ObjectIdentity
trpzSysCpuMemoryUsageDetail = _TrpzSysCpuMemoryUsageDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12)
)
_TrpzSysCpuMemoryInstantUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryInstantUsage_Object = MibScalar
trpzSysCpuMemoryInstantUsage = _TrpzSysCpuMemoryInstantUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 1),
    _TrpzSysCpuMemoryInstantUsage_Type()
)
trpzSysCpuMemoryInstantUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryInstantUsage.setStatus("current")
_TrpzSysCpuMemoryLastMinuteUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastMinuteUsage_Object = MibScalar
trpzSysCpuMemoryLastMinuteUsage = _TrpzSysCpuMemoryLastMinuteUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 2),
    _TrpzSysCpuMemoryLastMinuteUsage_Type()
)
trpzSysCpuMemoryLastMinuteUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryLastMinuteUsage.setStatus("current")
_TrpzSysCpuMemoryLast5MinutesUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryLast5MinutesUsage_Object = MibScalar
trpzSysCpuMemoryLast5MinutesUsage = _TrpzSysCpuMemoryLast5MinutesUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 3),
    _TrpzSysCpuMemoryLast5MinutesUsage_Type()
)
trpzSysCpuMemoryLast5MinutesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryLast5MinutesUsage.setStatus("current")
_TrpzSysCpuMemoryLastHourUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastHourUsage_Object = MibScalar
trpzSysCpuMemoryLastHourUsage = _TrpzSysCpuMemoryLastHourUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 4),
    _TrpzSysCpuMemoryLastHourUsage_Type()
)
trpzSysCpuMemoryLastHourUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryLastHourUsage.setStatus("current")
_TrpzSysCpuMemoryLastDayUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryLastDayUsage_Object = MibScalar
trpzSysCpuMemoryLastDayUsage = _TrpzSysCpuMemoryLastDayUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 5),
    _TrpzSysCpuMemoryLastDayUsage_Type()
)
trpzSysCpuMemoryLastDayUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryLastDayUsage.setStatus("current")
_TrpzSysCpuMemoryLast3DaysUsage_Type = TrpzSysMemoryAmount
_TrpzSysCpuMemoryLast3DaysUsage_Object = MibScalar
trpzSysCpuMemoryLast3DaysUsage = _TrpzSysCpuMemoryLast3DaysUsage_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 12, 6),
    _TrpzSysCpuMemoryLast3DaysUsage_Type()
)
trpzSysCpuMemoryLast3DaysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysCpuMemoryLast3DaysUsage.setStatus("current")
_TrpzSysChassisComponents_ObjectIdentity = ObjectIdentity
trpzSysChassisComponents = _TrpzSysChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13)
)
_TrpzSysChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
trpzSysChasCompPowerSupplies = _TrpzSysChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1)
)
_TrpzSysNumPowerSuppliesSupported_Type = Unsigned32
_TrpzSysNumPowerSuppliesSupported_Object = MibScalar
trpzSysNumPowerSuppliesSupported = _TrpzSysNumPowerSuppliesSupported_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 1),
    _TrpzSysNumPowerSuppliesSupported_Type()
)
trpzSysNumPowerSuppliesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysNumPowerSuppliesSupported.setStatus("current")
_TrpzSysPowerSupplyTable_Object = MibTable
trpzSysPowerSupplyTable = _TrpzSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    trpzSysPowerSupplyTable.setStatus("current")
_TrpzSysPowerSupplyEntry_Object = MibTableRow
trpzSysPowerSupplyEntry = _TrpzSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 2, 1)
)
trpzSysPowerSupplyEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-SYSTEM-MIB", "trpzSysPowerSupplyDeviceOID"),
)
if mibBuilder.loadTexts:
    trpzSysPowerSupplyEntry.setStatus("current")
_TrpzSysPowerSupplyDeviceOID_Type = ObjectIdentifier
_TrpzSysPowerSupplyDeviceOID_Object = MibTableColumn
trpzSysPowerSupplyDeviceOID = _TrpzSysPowerSupplyDeviceOID_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 2, 1, 1),
    _TrpzSysPowerSupplyDeviceOID_Type()
)
trpzSysPowerSupplyDeviceOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzSysPowerSupplyDeviceOID.setStatus("current")
_TrpzSysPowerSupplyStatus_Type = TrpzSysPowerSupplyStatus
_TrpzSysPowerSupplyStatus_Object = MibTableColumn
trpzSysPowerSupplyStatus = _TrpzSysPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 2, 1, 2),
    _TrpzSysPowerSupplyStatus_Type()
)
trpzSysPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysPowerSupplyStatus.setStatus("current")


class _TrpzSysPowerSupplyDescr_Type(DisplayString):
    """Custom type trpzSysPowerSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrpzSysPowerSupplyDescr_Type.__name__ = "DisplayString"
_TrpzSysPowerSupplyDescr_Object = MibTableColumn
trpzSysPowerSupplyDescr = _TrpzSysPowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 8, 1, 1, 13, 1, 2, 1, 3),
    _TrpzSysPowerSupplyDescr_Type()
)
trpzSysPowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzSysPowerSupplyDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-SYSTEM-MIB",
    **{"TrpzSysCpuLoad": TrpzSysCpuLoad,
       "TrpzSysMemoryAmount": TrpzSysMemoryAmount,
       "TrpzSysPowerSupplyStatus": TrpzSysPowerSupplyStatus,
       "trpzSystemMib": trpzSystemMib,
       "trpzSysObjects": trpzSysObjects,
       "trpzSysDataObjects": trpzSysDataObjects,
       "trpzSysCpuMemoryUsedBytes": trpzSysCpuMemoryUsedBytes,
       "trpzSysCpuMemoryTotalBytes": trpzSysCpuMemoryTotalBytes,
       "trpzSysFlashMemoryUsedBytes": trpzSysFlashMemoryUsedBytes,
       "trpzSysFlashMemoryTotalBytes": trpzSysFlashMemoryTotalBytes,
       "trpzSysCpuAverageLoad": trpzSysCpuAverageLoad,
       "trpzSysCpuMemorySize": trpzSysCpuMemorySize,
       "trpzSysCpuLoadDetail": trpzSysCpuLoadDetail,
       "trpzSysCpuInstantLoad": trpzSysCpuInstantLoad,
       "trpzSysCpuLastMinuteLoad": trpzSysCpuLastMinuteLoad,
       "trpzSysCpuLast5MinutesLoad": trpzSysCpuLast5MinutesLoad,
       "trpzSysCpuLastHourLoad": trpzSysCpuLastHourLoad,
       "trpzSysCpuLastDayLoad": trpzSysCpuLastDayLoad,
       "trpzSysCpuLast3DaysLoad": trpzSysCpuLast3DaysLoad,
       "trpzSysCpuMemoryUsageDetail": trpzSysCpuMemoryUsageDetail,
       "trpzSysCpuMemoryInstantUsage": trpzSysCpuMemoryInstantUsage,
       "trpzSysCpuMemoryLastMinuteUsage": trpzSysCpuMemoryLastMinuteUsage,
       "trpzSysCpuMemoryLast5MinutesUsage": trpzSysCpuMemoryLast5MinutesUsage,
       "trpzSysCpuMemoryLastHourUsage": trpzSysCpuMemoryLastHourUsage,
       "trpzSysCpuMemoryLastDayUsage": trpzSysCpuMemoryLastDayUsage,
       "trpzSysCpuMemoryLast3DaysUsage": trpzSysCpuMemoryLast3DaysUsage,
       "trpzSysChassisComponents": trpzSysChassisComponents,
       "trpzSysChasCompPowerSupplies": trpzSysChasCompPowerSupplies,
       "trpzSysNumPowerSuppliesSupported": trpzSysNumPowerSuppliesSupported,
       "trpzSysPowerSupplyTable": trpzSysPowerSupplyTable,
       "trpzSysPowerSupplyEntry": trpzSysPowerSupplyEntry,
       "trpzSysPowerSupplyDeviceOID": trpzSysPowerSupplyDeviceOID,
       "trpzSysPowerSupplyStatus": trpzSysPowerSupplyStatus,
       "trpzSysPowerSupplyDescr": trpzSysPowerSupplyDescr}
)
