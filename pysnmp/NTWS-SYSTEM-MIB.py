# SNMP MIB module (NTWS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:00 2024
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

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8)
)
ntwsSystemMib.setRevisions(
        ("2007-08-31 00:13",
         "2007-08-14 00:12",
         "2007-05-04 00:10",
         "2007-03-14 00:07",
         "2006-11-09 00:04",
         "2006-06-06 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsSysCpuLoad(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class NtwsSysMemoryAmount(Unsigned32, TextualConvention):
    status = "current"


class NtwsSysPowerSupplyStatus(Integer32, TextualConvention):
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

_NtwsSysObjects_ObjectIdentity = ObjectIdentity
ntwsSysObjects = _NtwsSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1)
)
_NtwsSysDataObjects_ObjectIdentity = ObjectIdentity
ntwsSysDataObjects = _NtwsSysDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1)
)
_NtwsSysCpuMemoryUsedBytes_Type = Unsigned32
_NtwsSysCpuMemoryUsedBytes_Object = MibScalar
ntwsSysCpuMemoryUsedBytes = _NtwsSysCpuMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 1),
    _NtwsSysCpuMemoryUsedBytes_Type()
)
ntwsSysCpuMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryUsedBytes.setStatus("obsolete")
_NtwsSysCpuMemoryTotalBytes_Type = Unsigned32
_NtwsSysCpuMemoryTotalBytes_Object = MibScalar
ntwsSysCpuMemoryTotalBytes = _NtwsSysCpuMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 2),
    _NtwsSysCpuMemoryTotalBytes_Type()
)
ntwsSysCpuMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryTotalBytes.setStatus("obsolete")
_NtwsSysFlashMemoryUsedBytes_Type = Unsigned32
_NtwsSysFlashMemoryUsedBytes_Object = MibScalar
ntwsSysFlashMemoryUsedBytes = _NtwsSysFlashMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 3),
    _NtwsSysFlashMemoryUsedBytes_Type()
)
ntwsSysFlashMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysFlashMemoryUsedBytes.setStatus("current")
_NtwsSysFlashMemoryTotalBytes_Type = Unsigned32
_NtwsSysFlashMemoryTotalBytes_Object = MibScalar
ntwsSysFlashMemoryTotalBytes = _NtwsSysFlashMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 4),
    _NtwsSysFlashMemoryTotalBytes_Type()
)
ntwsSysFlashMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysFlashMemoryTotalBytes.setStatus("current")
_NtwsSysCpuAverageLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuAverageLoad_Object = MibScalar
ntwsSysCpuAverageLoad = _NtwsSysCpuAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 5),
    _NtwsSysCpuAverageLoad_Type()
)
ntwsSysCpuAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuAverageLoad.setStatus("current")
_NtwsSysCpuMemorySize_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemorySize_Object = MibScalar
ntwsSysCpuMemorySize = _NtwsSysCpuMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 6),
    _NtwsSysCpuMemorySize_Type()
)
ntwsSysCpuMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemorySize.setStatus("current")
_NtwsSysCpuLoadDetail_ObjectIdentity = ObjectIdentity
ntwsSysCpuLoadDetail = _NtwsSysCpuLoadDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11)
)
_NtwsSysCpuInstantLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuInstantLoad_Object = MibScalar
ntwsSysCpuInstantLoad = _NtwsSysCpuInstantLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 1),
    _NtwsSysCpuInstantLoad_Type()
)
ntwsSysCpuInstantLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuInstantLoad.setStatus("current")
_NtwsSysCpuLastMinuteLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuLastMinuteLoad_Object = MibScalar
ntwsSysCpuLastMinuteLoad = _NtwsSysCpuLastMinuteLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 2),
    _NtwsSysCpuLastMinuteLoad_Type()
)
ntwsSysCpuLastMinuteLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuLastMinuteLoad.setStatus("current")
_NtwsSysCpuLast5MinutesLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuLast5MinutesLoad_Object = MibScalar
ntwsSysCpuLast5MinutesLoad = _NtwsSysCpuLast5MinutesLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 3),
    _NtwsSysCpuLast5MinutesLoad_Type()
)
ntwsSysCpuLast5MinutesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuLast5MinutesLoad.setStatus("current")
_NtwsSysCpuLastHourLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuLastHourLoad_Object = MibScalar
ntwsSysCpuLastHourLoad = _NtwsSysCpuLastHourLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 4),
    _NtwsSysCpuLastHourLoad_Type()
)
ntwsSysCpuLastHourLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuLastHourLoad.setStatus("current")
_NtwsSysCpuLastDayLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuLastDayLoad_Object = MibScalar
ntwsSysCpuLastDayLoad = _NtwsSysCpuLastDayLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 5),
    _NtwsSysCpuLastDayLoad_Type()
)
ntwsSysCpuLastDayLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuLastDayLoad.setStatus("current")
_NtwsSysCpuLast3DaysLoad_Type = NtwsSysCpuLoad
_NtwsSysCpuLast3DaysLoad_Object = MibScalar
ntwsSysCpuLast3DaysLoad = _NtwsSysCpuLast3DaysLoad_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 11, 6),
    _NtwsSysCpuLast3DaysLoad_Type()
)
ntwsSysCpuLast3DaysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuLast3DaysLoad.setStatus("current")
_NtwsSysCpuMemoryUsageDetail_ObjectIdentity = ObjectIdentity
ntwsSysCpuMemoryUsageDetail = _NtwsSysCpuMemoryUsageDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12)
)
_NtwsSysCpuMemoryInstantUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryInstantUsage_Object = MibScalar
ntwsSysCpuMemoryInstantUsage = _NtwsSysCpuMemoryInstantUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 1),
    _NtwsSysCpuMemoryInstantUsage_Type()
)
ntwsSysCpuMemoryInstantUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryInstantUsage.setStatus("current")
_NtwsSysCpuMemoryLastMinuteUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastMinuteUsage_Object = MibScalar
ntwsSysCpuMemoryLastMinuteUsage = _NtwsSysCpuMemoryLastMinuteUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 2),
    _NtwsSysCpuMemoryLastMinuteUsage_Type()
)
ntwsSysCpuMemoryLastMinuteUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryLastMinuteUsage.setStatus("current")
_NtwsSysCpuMemoryLast5MinutesUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryLast5MinutesUsage_Object = MibScalar
ntwsSysCpuMemoryLast5MinutesUsage = _NtwsSysCpuMemoryLast5MinutesUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 3),
    _NtwsSysCpuMemoryLast5MinutesUsage_Type()
)
ntwsSysCpuMemoryLast5MinutesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryLast5MinutesUsage.setStatus("current")
_NtwsSysCpuMemoryLastHourUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastHourUsage_Object = MibScalar
ntwsSysCpuMemoryLastHourUsage = _NtwsSysCpuMemoryLastHourUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 4),
    _NtwsSysCpuMemoryLastHourUsage_Type()
)
ntwsSysCpuMemoryLastHourUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryLastHourUsage.setStatus("current")
_NtwsSysCpuMemoryLastDayUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryLastDayUsage_Object = MibScalar
ntwsSysCpuMemoryLastDayUsage = _NtwsSysCpuMemoryLastDayUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 5),
    _NtwsSysCpuMemoryLastDayUsage_Type()
)
ntwsSysCpuMemoryLastDayUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryLastDayUsage.setStatus("current")
_NtwsSysCpuMemoryLast3DaysUsage_Type = NtwsSysMemoryAmount
_NtwsSysCpuMemoryLast3DaysUsage_Object = MibScalar
ntwsSysCpuMemoryLast3DaysUsage = _NtwsSysCpuMemoryLast3DaysUsage_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 12, 6),
    _NtwsSysCpuMemoryLast3DaysUsage_Type()
)
ntwsSysCpuMemoryLast3DaysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysCpuMemoryLast3DaysUsage.setStatus("current")
_NtwsSysChassisComponents_ObjectIdentity = ObjectIdentity
ntwsSysChassisComponents = _NtwsSysChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13)
)
_NtwsSysChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
ntwsSysChasCompPowerSupplies = _NtwsSysChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1)
)
_NtwsSysNumPowerSuppliesSupported_Type = Unsigned32
_NtwsSysNumPowerSuppliesSupported_Object = MibScalar
ntwsSysNumPowerSuppliesSupported = _NtwsSysNumPowerSuppliesSupported_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 1),
    _NtwsSysNumPowerSuppliesSupported_Type()
)
ntwsSysNumPowerSuppliesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysNumPowerSuppliesSupported.setStatus("current")
_NtwsSysPowerSupplyTable_Object = MibTable
ntwsSysPowerSupplyTable = _NtwsSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsSysPowerSupplyTable.setStatus("current")
_NtwsSysPowerSupplyEntry_Object = MibTableRow
ntwsSysPowerSupplyEntry = _NtwsSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 2, 1)
)
ntwsSysPowerSupplyEntry.setIndexNames(
    (0, "NTWS-SYSTEM-MIB", "ntwsSysPowerSupplyDeviceOID"),
)
if mibBuilder.loadTexts:
    ntwsSysPowerSupplyEntry.setStatus("current")
_NtwsSysPowerSupplyDeviceOID_Type = ObjectIdentifier
_NtwsSysPowerSupplyDeviceOID_Object = MibTableColumn
ntwsSysPowerSupplyDeviceOID = _NtwsSysPowerSupplyDeviceOID_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 2, 1, 1),
    _NtwsSysPowerSupplyDeviceOID_Type()
)
ntwsSysPowerSupplyDeviceOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsSysPowerSupplyDeviceOID.setStatus("current")
_NtwsSysPowerSupplyStatus_Type = NtwsSysPowerSupplyStatus
_NtwsSysPowerSupplyStatus_Object = MibTableColumn
ntwsSysPowerSupplyStatus = _NtwsSysPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 2, 1, 2),
    _NtwsSysPowerSupplyStatus_Type()
)
ntwsSysPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysPowerSupplyStatus.setStatus("current")


class _NtwsSysPowerSupplyDescr_Type(DisplayString):
    """Custom type ntwsSysPowerSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtwsSysPowerSupplyDescr_Type.__name__ = "DisplayString"
_NtwsSysPowerSupplyDescr_Object = MibTableColumn
ntwsSysPowerSupplyDescr = _NtwsSysPowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 8, 1, 1, 13, 1, 2, 1, 3),
    _NtwsSysPowerSupplyDescr_Type()
)
ntwsSysPowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsSysPowerSupplyDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-SYSTEM-MIB",
    **{"NtwsSysCpuLoad": NtwsSysCpuLoad,
       "NtwsSysMemoryAmount": NtwsSysMemoryAmount,
       "NtwsSysPowerSupplyStatus": NtwsSysPowerSupplyStatus,
       "ntwsSystemMib": ntwsSystemMib,
       "ntwsSysObjects": ntwsSysObjects,
       "ntwsSysDataObjects": ntwsSysDataObjects,
       "ntwsSysCpuMemoryUsedBytes": ntwsSysCpuMemoryUsedBytes,
       "ntwsSysCpuMemoryTotalBytes": ntwsSysCpuMemoryTotalBytes,
       "ntwsSysFlashMemoryUsedBytes": ntwsSysFlashMemoryUsedBytes,
       "ntwsSysFlashMemoryTotalBytes": ntwsSysFlashMemoryTotalBytes,
       "ntwsSysCpuAverageLoad": ntwsSysCpuAverageLoad,
       "ntwsSysCpuMemorySize": ntwsSysCpuMemorySize,
       "ntwsSysCpuLoadDetail": ntwsSysCpuLoadDetail,
       "ntwsSysCpuInstantLoad": ntwsSysCpuInstantLoad,
       "ntwsSysCpuLastMinuteLoad": ntwsSysCpuLastMinuteLoad,
       "ntwsSysCpuLast5MinutesLoad": ntwsSysCpuLast5MinutesLoad,
       "ntwsSysCpuLastHourLoad": ntwsSysCpuLastHourLoad,
       "ntwsSysCpuLastDayLoad": ntwsSysCpuLastDayLoad,
       "ntwsSysCpuLast3DaysLoad": ntwsSysCpuLast3DaysLoad,
       "ntwsSysCpuMemoryUsageDetail": ntwsSysCpuMemoryUsageDetail,
       "ntwsSysCpuMemoryInstantUsage": ntwsSysCpuMemoryInstantUsage,
       "ntwsSysCpuMemoryLastMinuteUsage": ntwsSysCpuMemoryLastMinuteUsage,
       "ntwsSysCpuMemoryLast5MinutesUsage": ntwsSysCpuMemoryLast5MinutesUsage,
       "ntwsSysCpuMemoryLastHourUsage": ntwsSysCpuMemoryLastHourUsage,
       "ntwsSysCpuMemoryLastDayUsage": ntwsSysCpuMemoryLastDayUsage,
       "ntwsSysCpuMemoryLast3DaysUsage": ntwsSysCpuMemoryLast3DaysUsage,
       "ntwsSysChassisComponents": ntwsSysChassisComponents,
       "ntwsSysChasCompPowerSupplies": ntwsSysChasCompPowerSupplies,
       "ntwsSysNumPowerSuppliesSupported": ntwsSysNumPowerSuppliesSupported,
       "ntwsSysPowerSupplyTable": ntwsSysPowerSupplyTable,
       "ntwsSysPowerSupplyEntry": ntwsSysPowerSupplyEntry,
       "ntwsSysPowerSupplyDeviceOID": ntwsSysPowerSupplyDeviceOID,
       "ntwsSysPowerSupplyStatus": ntwsSysPowerSupplyStatus,
       "ntwsSysPowerSupplyDescr": ntwsSysPowerSupplyDescr}
)
