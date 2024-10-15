# SNMP MIB module (RBTWS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:39 2024
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

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8)
)
rbtwsSystemMib.setRevisions(
        ("2007-08-14 00:12",
         "2007-05-04 00:10",
         "2007-03-14 00:07",
         "2006-11-09 00:04",
         "2006-06-06 00:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsSysCpuLoad(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class RbtwsSysMemoryAmount(Unsigned32, TextualConvention):
    status = "current"


class RbtwsSysPowerSupplyStatus(Integer32, TextualConvention):
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

_RbtwsSysObjects_ObjectIdentity = ObjectIdentity
rbtwsSysObjects = _RbtwsSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1)
)
_RbtwsSysDataObjects_ObjectIdentity = ObjectIdentity
rbtwsSysDataObjects = _RbtwsSysDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1)
)
_RbtwsSysCpuMemoryUsedBytes_Type = Unsigned32
_RbtwsSysCpuMemoryUsedBytes_Object = MibScalar
rbtwsSysCpuMemoryUsedBytes = _RbtwsSysCpuMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 1),
    _RbtwsSysCpuMemoryUsedBytes_Type()
)
rbtwsSysCpuMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryUsedBytes.setStatus("obsolete")
_RbtwsSysCpuMemoryTotalBytes_Type = Unsigned32
_RbtwsSysCpuMemoryTotalBytes_Object = MibScalar
rbtwsSysCpuMemoryTotalBytes = _RbtwsSysCpuMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 2),
    _RbtwsSysCpuMemoryTotalBytes_Type()
)
rbtwsSysCpuMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryTotalBytes.setStatus("obsolete")
_RbtwsSysFlashMemoryUsedBytes_Type = Unsigned32
_RbtwsSysFlashMemoryUsedBytes_Object = MibScalar
rbtwsSysFlashMemoryUsedBytes = _RbtwsSysFlashMemoryUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 3),
    _RbtwsSysFlashMemoryUsedBytes_Type()
)
rbtwsSysFlashMemoryUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysFlashMemoryUsedBytes.setStatus("current")
_RbtwsSysFlashMemoryTotalBytes_Type = Unsigned32
_RbtwsSysFlashMemoryTotalBytes_Object = MibScalar
rbtwsSysFlashMemoryTotalBytes = _RbtwsSysFlashMemoryTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 4),
    _RbtwsSysFlashMemoryTotalBytes_Type()
)
rbtwsSysFlashMemoryTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysFlashMemoryTotalBytes.setStatus("current")
_RbtwsSysCpuAverageLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuAverageLoad_Object = MibScalar
rbtwsSysCpuAverageLoad = _RbtwsSysCpuAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 5),
    _RbtwsSysCpuAverageLoad_Type()
)
rbtwsSysCpuAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuAverageLoad.setStatus("current")
_RbtwsSysCpuMemorySize_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemorySize_Object = MibScalar
rbtwsSysCpuMemorySize = _RbtwsSysCpuMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 6),
    _RbtwsSysCpuMemorySize_Type()
)
rbtwsSysCpuMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemorySize.setStatus("current")
_RbtwsSysCpuLoadDetail_ObjectIdentity = ObjectIdentity
rbtwsSysCpuLoadDetail = _RbtwsSysCpuLoadDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11)
)
_RbtwsSysCpuInstantLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuInstantLoad_Object = MibScalar
rbtwsSysCpuInstantLoad = _RbtwsSysCpuInstantLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 1),
    _RbtwsSysCpuInstantLoad_Type()
)
rbtwsSysCpuInstantLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuInstantLoad.setStatus("current")
_RbtwsSysCpuLastMinuteLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuLastMinuteLoad_Object = MibScalar
rbtwsSysCpuLastMinuteLoad = _RbtwsSysCpuLastMinuteLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 2),
    _RbtwsSysCpuLastMinuteLoad_Type()
)
rbtwsSysCpuLastMinuteLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuLastMinuteLoad.setStatus("current")
_RbtwsSysCpuLast5MinutesLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuLast5MinutesLoad_Object = MibScalar
rbtwsSysCpuLast5MinutesLoad = _RbtwsSysCpuLast5MinutesLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 3),
    _RbtwsSysCpuLast5MinutesLoad_Type()
)
rbtwsSysCpuLast5MinutesLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuLast5MinutesLoad.setStatus("current")
_RbtwsSysCpuLastHourLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuLastHourLoad_Object = MibScalar
rbtwsSysCpuLastHourLoad = _RbtwsSysCpuLastHourLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 4),
    _RbtwsSysCpuLastHourLoad_Type()
)
rbtwsSysCpuLastHourLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuLastHourLoad.setStatus("current")
_RbtwsSysCpuLastDayLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuLastDayLoad_Object = MibScalar
rbtwsSysCpuLastDayLoad = _RbtwsSysCpuLastDayLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 5),
    _RbtwsSysCpuLastDayLoad_Type()
)
rbtwsSysCpuLastDayLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuLastDayLoad.setStatus("current")
_RbtwsSysCpuLast3DaysLoad_Type = RbtwsSysCpuLoad
_RbtwsSysCpuLast3DaysLoad_Object = MibScalar
rbtwsSysCpuLast3DaysLoad = _RbtwsSysCpuLast3DaysLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 11, 6),
    _RbtwsSysCpuLast3DaysLoad_Type()
)
rbtwsSysCpuLast3DaysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuLast3DaysLoad.setStatus("current")
_RbtwsSysCpuMemoryUsageDetail_ObjectIdentity = ObjectIdentity
rbtwsSysCpuMemoryUsageDetail = _RbtwsSysCpuMemoryUsageDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12)
)
_RbtwsSysCpuMemoryInstantUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryInstantUsage_Object = MibScalar
rbtwsSysCpuMemoryInstantUsage = _RbtwsSysCpuMemoryInstantUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 1),
    _RbtwsSysCpuMemoryInstantUsage_Type()
)
rbtwsSysCpuMemoryInstantUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryInstantUsage.setStatus("current")
_RbtwsSysCpuMemoryLastMinuteUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastMinuteUsage_Object = MibScalar
rbtwsSysCpuMemoryLastMinuteUsage = _RbtwsSysCpuMemoryLastMinuteUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 2),
    _RbtwsSysCpuMemoryLastMinuteUsage_Type()
)
rbtwsSysCpuMemoryLastMinuteUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryLastMinuteUsage.setStatus("current")
_RbtwsSysCpuMemoryLast5MinutesUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLast5MinutesUsage_Object = MibScalar
rbtwsSysCpuMemoryLast5MinutesUsage = _RbtwsSysCpuMemoryLast5MinutesUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 3),
    _RbtwsSysCpuMemoryLast5MinutesUsage_Type()
)
rbtwsSysCpuMemoryLast5MinutesUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryLast5MinutesUsage.setStatus("current")
_RbtwsSysCpuMemoryLastHourUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastHourUsage_Object = MibScalar
rbtwsSysCpuMemoryLastHourUsage = _RbtwsSysCpuMemoryLastHourUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 4),
    _RbtwsSysCpuMemoryLastHourUsage_Type()
)
rbtwsSysCpuMemoryLastHourUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryLastHourUsage.setStatus("current")
_RbtwsSysCpuMemoryLastDayUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLastDayUsage_Object = MibScalar
rbtwsSysCpuMemoryLastDayUsage = _RbtwsSysCpuMemoryLastDayUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 5),
    _RbtwsSysCpuMemoryLastDayUsage_Type()
)
rbtwsSysCpuMemoryLastDayUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryLastDayUsage.setStatus("current")
_RbtwsSysCpuMemoryLast3DaysUsage_Type = RbtwsSysMemoryAmount
_RbtwsSysCpuMemoryLast3DaysUsage_Object = MibScalar
rbtwsSysCpuMemoryLast3DaysUsage = _RbtwsSysCpuMemoryLast3DaysUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 12, 6),
    _RbtwsSysCpuMemoryLast3DaysUsage_Type()
)
rbtwsSysCpuMemoryLast3DaysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysCpuMemoryLast3DaysUsage.setStatus("current")
_RbtwsSysChassisComponents_ObjectIdentity = ObjectIdentity
rbtwsSysChassisComponents = _RbtwsSysChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13)
)
_RbtwsSysChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
rbtwsSysChasCompPowerSupplies = _RbtwsSysChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1)
)
_RbtwsSysNumPowerSuppliesSupported_Type = Unsigned32
_RbtwsSysNumPowerSuppliesSupported_Object = MibScalar
rbtwsSysNumPowerSuppliesSupported = _RbtwsSysNumPowerSuppliesSupported_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 1),
    _RbtwsSysNumPowerSuppliesSupported_Type()
)
rbtwsSysNumPowerSuppliesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysNumPowerSuppliesSupported.setStatus("current")
_RbtwsSysPowerSupplyTable_Object = MibTable
rbtwsSysPowerSupplyTable = _RbtwsSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    rbtwsSysPowerSupplyTable.setStatus("current")
_RbtwsSysPowerSupplyEntry_Object = MibTableRow
rbtwsSysPowerSupplyEntry = _RbtwsSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 2, 1)
)
rbtwsSysPowerSupplyEntry.setIndexNames(
    (0, "RBTWS-SYSTEM-MIB", "rbtwsSysPowerSupplyDeviceOID"),
)
if mibBuilder.loadTexts:
    rbtwsSysPowerSupplyEntry.setStatus("current")
_RbtwsSysPowerSupplyDeviceOID_Type = ObjectIdentifier
_RbtwsSysPowerSupplyDeviceOID_Object = MibTableColumn
rbtwsSysPowerSupplyDeviceOID = _RbtwsSysPowerSupplyDeviceOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 2, 1, 1),
    _RbtwsSysPowerSupplyDeviceOID_Type()
)
rbtwsSysPowerSupplyDeviceOID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsSysPowerSupplyDeviceOID.setStatus("current")
_RbtwsSysPowerSupplyStatus_Type = RbtwsSysPowerSupplyStatus
_RbtwsSysPowerSupplyStatus_Object = MibTableColumn
rbtwsSysPowerSupplyStatus = _RbtwsSysPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 2, 1, 2),
    _RbtwsSysPowerSupplyStatus_Type()
)
rbtwsSysPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysPowerSupplyStatus.setStatus("current")


class _RbtwsSysPowerSupplyDescr_Type(DisplayString):
    """Custom type rbtwsSysPowerSupplyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbtwsSysPowerSupplyDescr_Type.__name__ = "DisplayString"
_RbtwsSysPowerSupplyDescr_Object = MibTableColumn
rbtwsSysPowerSupplyDescr = _RbtwsSysPowerSupplyDescr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 8, 1, 1, 13, 1, 2, 1, 3),
    _RbtwsSysPowerSupplyDescr_Type()
)
rbtwsSysPowerSupplyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsSysPowerSupplyDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-SYSTEM-MIB",
    **{"RbtwsSysCpuLoad": RbtwsSysCpuLoad,
       "RbtwsSysMemoryAmount": RbtwsSysMemoryAmount,
       "RbtwsSysPowerSupplyStatus": RbtwsSysPowerSupplyStatus,
       "rbtwsSystemMib": rbtwsSystemMib,
       "rbtwsSysObjects": rbtwsSysObjects,
       "rbtwsSysDataObjects": rbtwsSysDataObjects,
       "rbtwsSysCpuMemoryUsedBytes": rbtwsSysCpuMemoryUsedBytes,
       "rbtwsSysCpuMemoryTotalBytes": rbtwsSysCpuMemoryTotalBytes,
       "rbtwsSysFlashMemoryUsedBytes": rbtwsSysFlashMemoryUsedBytes,
       "rbtwsSysFlashMemoryTotalBytes": rbtwsSysFlashMemoryTotalBytes,
       "rbtwsSysCpuAverageLoad": rbtwsSysCpuAverageLoad,
       "rbtwsSysCpuMemorySize": rbtwsSysCpuMemorySize,
       "rbtwsSysCpuLoadDetail": rbtwsSysCpuLoadDetail,
       "rbtwsSysCpuInstantLoad": rbtwsSysCpuInstantLoad,
       "rbtwsSysCpuLastMinuteLoad": rbtwsSysCpuLastMinuteLoad,
       "rbtwsSysCpuLast5MinutesLoad": rbtwsSysCpuLast5MinutesLoad,
       "rbtwsSysCpuLastHourLoad": rbtwsSysCpuLastHourLoad,
       "rbtwsSysCpuLastDayLoad": rbtwsSysCpuLastDayLoad,
       "rbtwsSysCpuLast3DaysLoad": rbtwsSysCpuLast3DaysLoad,
       "rbtwsSysCpuMemoryUsageDetail": rbtwsSysCpuMemoryUsageDetail,
       "rbtwsSysCpuMemoryInstantUsage": rbtwsSysCpuMemoryInstantUsage,
       "rbtwsSysCpuMemoryLastMinuteUsage": rbtwsSysCpuMemoryLastMinuteUsage,
       "rbtwsSysCpuMemoryLast5MinutesUsage": rbtwsSysCpuMemoryLast5MinutesUsage,
       "rbtwsSysCpuMemoryLastHourUsage": rbtwsSysCpuMemoryLastHourUsage,
       "rbtwsSysCpuMemoryLastDayUsage": rbtwsSysCpuMemoryLastDayUsage,
       "rbtwsSysCpuMemoryLast3DaysUsage": rbtwsSysCpuMemoryLast3DaysUsage,
       "rbtwsSysChassisComponents": rbtwsSysChassisComponents,
       "rbtwsSysChasCompPowerSupplies": rbtwsSysChasCompPowerSupplies,
       "rbtwsSysNumPowerSuppliesSupported": rbtwsSysNumPowerSuppliesSupported,
       "rbtwsSysPowerSupplyTable": rbtwsSysPowerSupplyTable,
       "rbtwsSysPowerSupplyEntry": rbtwsSysPowerSupplyEntry,
       "rbtwsSysPowerSupplyDeviceOID": rbtwsSysPowerSupplyDeviceOID,
       "rbtwsSysPowerSupplyStatus": rbtwsSysPowerSupplyStatus,
       "rbtwsSysPowerSupplyDescr": rbtwsSysPowerSupplyDescr}
)
