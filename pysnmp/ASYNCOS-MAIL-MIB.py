# SNMP MIB module (ASYNCOS-MAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASYNCOS-MAIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:56 2024
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

(asyncOSMail,) = mibBuilder.importSymbols(
    "IRONPORT-SMI",
    "asyncOSMail")

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


# MODULE-IDENTITY

asyncOSMailObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1)
)
asyncOSMailObjects.setRevisions(
        ("2011-03-07 00:00",
         "2010-07-01 00:00",
         "2009-04-07 00:00",
         "2009-01-15 00:00",
         "2005-03-07 00:00",
         "2005-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PerCentMemoryUtilization_Type(Integer32):
    """Custom type perCentMemoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PerCentMemoryUtilization_Type.__name__ = "Integer32"
_PerCentMemoryUtilization_Object = MibScalar
perCentMemoryUtilization = _PerCentMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 1),
    _PerCentMemoryUtilization_Type()
)
perCentMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perCentMemoryUtilization.setStatus("current")


class _PerCentCPUUtilization_Type(Integer32):
    """Custom type perCentCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PerCentCPUUtilization_Type.__name__ = "Integer32"
_PerCentCPUUtilization_Object = MibScalar
perCentCPUUtilization = _PerCentCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 2),
    _PerCentCPUUtilization_Type()
)
perCentCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perCentCPUUtilization.setStatus("current")


class _PerCentDiskIOUtilization_Type(Integer32):
    """Custom type perCentDiskIOUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PerCentDiskIOUtilization_Type.__name__ = "Integer32"
_PerCentDiskIOUtilization_Object = MibScalar
perCentDiskIOUtilization = _PerCentDiskIOUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 3),
    _PerCentDiskIOUtilization_Type()
)
perCentDiskIOUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perCentDiskIOUtilization.setStatus("current")


class _PerCentQueueUtilization_Type(Integer32):
    """Custom type perCentQueueUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PerCentQueueUtilization_Type.__name__ = "Integer32"
_PerCentQueueUtilization_Object = MibScalar
perCentQueueUtilization = _PerCentQueueUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 4),
    _PerCentQueueUtilization_Type()
)
perCentQueueUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perCentQueueUtilization.setStatus("current")


class _QueueAvailabilityStatus_Type(Integer32):
    """Custom type queueAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("queueFull", 3),
          ("queueSpaceAvailable", 1),
          ("queueSpaceShortage", 2))
    )


_QueueAvailabilityStatus_Type.__name__ = "Integer32"
_QueueAvailabilityStatus_Object = MibScalar
queueAvailabilityStatus = _QueueAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 5),
    _QueueAvailabilityStatus_Type()
)
queueAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueAvailabilityStatus.setStatus("current")


class _ResourceConservationReason_Type(Integer32):
    """Custom type resourceConservationReason based on Integer32"""
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
        *(("memoryShortage", 2),
          ("noResourceConservation", 1),
          ("queueFull", 4),
          ("queueSpaceShortage", 3))
    )


_ResourceConservationReason_Type.__name__ = "Integer32"
_ResourceConservationReason_Object = MibScalar
resourceConservationReason = _ResourceConservationReason_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 6),
    _ResourceConservationReason_Type()
)
resourceConservationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resourceConservationReason.setStatus("current")


class _MemoryAvailabilityStatus_Type(Integer32):
    """Custom type memoryAvailabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("memoryAvailable", 1),
          ("memoryFull", 3),
          ("memoryShortage", 2))
    )


_MemoryAvailabilityStatus_Type.__name__ = "Integer32"
_MemoryAvailabilityStatus_Object = MibScalar
memoryAvailabilityStatus = _MemoryAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 7),
    _MemoryAvailabilityStatus_Type()
)
memoryAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAvailabilityStatus.setStatus("current")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("current")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("current")


class _PowerSupplyIndex_Type(Integer32):
    """Custom type powerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PowerSupplyIndex_Type.__name__ = "Integer32"
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("current")


class _PowerSupplyStatus_Type(Integer32):
    """Custom type powerSupplyStatus based on Integer32"""
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
        *(("powerSupplyFaulty", 4),
          ("powerSupplyHealthy", 2),
          ("powerSupplyNoAC", 3),
          ("powerSupplyNotInstalled", 1))
    )


_PowerSupplyStatus_Type.__name__ = "Integer32"
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 2),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")


class _PowerSupplyRedundancy_Type(Integer32):
    """Custom type powerSupplyRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyRedundancyLost", 2),
          ("powerSupplyRedundancyOK", 1))
    )


_PowerSupplyRedundancy_Type.__name__ = "Integer32"
_PowerSupplyRedundancy_Object = MibTableColumn
powerSupplyRedundancy = _PowerSupplyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 3),
    _PowerSupplyRedundancy_Type()
)
powerSupplyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRedundancy.setStatus("current")
_PowerSupplyName_Type = DisplayString
_PowerSupplyName_Object = MibTableColumn
powerSupplyName = _PowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 8, 1, 4),
    _PowerSupplyName_Type()
)
powerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyName.setStatus("current")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("current")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1)
)
temperatureEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("current")


class _TemperatureIndex_Type(Integer32):
    """Custom type temperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TemperatureIndex_Type.__name__ = "Integer32"
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")
_DegreesCelsius_Type = Integer32
_DegreesCelsius_Object = MibTableColumn
degreesCelsius = _DegreesCelsius_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 2),
    _DegreesCelsius_Type()
)
degreesCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    degreesCelsius.setStatus("current")
_TemperatureName_Type = DisplayString
_TemperatureName_Object = MibTableColumn
temperatureName = _TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 9, 1, 3),
    _TemperatureName_Type()
)
temperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureName.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1)
)
fanEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")
_FanRPMs_Type = Gauge32
_FanRPMs_Object = MibTableColumn
fanRPMs = _FanRPMs_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 2),
    _FanRPMs_Type()
)
fanRPMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRPMs.setStatus("current")
_FanName_Type = DisplayString
_FanName_Object = MibTableColumn
fanName = _FanName_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 10, 1, 3),
    _FanName_Type()
)
fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanName.setStatus("current")
_WorkQueueMessages_Type = Gauge32
_WorkQueueMessages_Object = MibScalar
workQueueMessages = _WorkQueueMessages_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 11),
    _WorkQueueMessages_Type()
)
workQueueMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    workQueueMessages.setStatus("current")
_KeyExpirationTable_Object = MibTable
keyExpirationTable = _KeyExpirationTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    keyExpirationTable.setStatus("current")
_KeyExpirationEntry_Object = MibTableRow
keyExpirationEntry = _KeyExpirationEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1)
)
keyExpirationEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "keyExpirationIndex"),
)
if mibBuilder.loadTexts:
    keyExpirationEntry.setStatus("current")


class _KeyExpirationIndex_Type(Integer32):
    """Custom type keyExpirationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_KeyExpirationIndex_Type.__name__ = "Integer32"
_KeyExpirationIndex_Object = MibTableColumn
keyExpirationIndex = _KeyExpirationIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 1),
    _KeyExpirationIndex_Type()
)
keyExpirationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyExpirationIndex.setStatus("current")
_KeyDescription_Type = DisplayString
_KeyDescription_Object = MibTableColumn
keyDescription = _KeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 2),
    _KeyDescription_Type()
)
keyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyDescription.setStatus("current")
_KeyIsPerpetual_Type = TruthValue
_KeyIsPerpetual_Object = MibTableColumn
keyIsPerpetual = _KeyIsPerpetual_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 3),
    _KeyIsPerpetual_Type()
)
keyIsPerpetual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyIsPerpetual.setStatus("current")
_KeySecondsUntilExpire_Type = Gauge32
_KeySecondsUntilExpire_Object = MibTableColumn
keySecondsUntilExpire = _KeySecondsUntilExpire_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 12, 1, 4),
    _KeySecondsUntilExpire_Type()
)
keySecondsUntilExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keySecondsUntilExpire.setStatus("current")
_UpdateTable_Object = MibTable
updateTable = _UpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    updateTable.setStatus("current")
_UpdateEntry_Object = MibTableRow
updateEntry = _UpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1)
)
updateEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "updateIndex"),
)
if mibBuilder.loadTexts:
    updateEntry.setStatus("current")


class _UpdateIndex_Type(Integer32):
    """Custom type updateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_UpdateIndex_Type.__name__ = "Integer32"
_UpdateIndex_Object = MibTableColumn
updateIndex = _UpdateIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 1),
    _UpdateIndex_Type()
)
updateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateIndex.setStatus("current")
_UpdateServiceName_Type = DisplayString
_UpdateServiceName_Object = MibTableColumn
updateServiceName = _UpdateServiceName_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 2),
    _UpdateServiceName_Type()
)
updateServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateServiceName.setStatus("current")
_Updates_Type = Counter32
_Updates_Object = MibTableColumn
updates = _Updates_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 3),
    _Updates_Type()
)
updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updates.setStatus("current")
_UpdateFailures_Type = Counter32
_UpdateFailures_Object = MibTableColumn
updateFailures = _UpdateFailures_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 13, 1, 4),
    _UpdateFailures_Type()
)
updateFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    updateFailures.setStatus("current")
_OldestMessageAge_Type = Gauge32
_OldestMessageAge_Object = MibScalar
oldestMessageAge = _OldestMessageAge_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 14),
    _OldestMessageAge_Type()
)
oldestMessageAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oldestMessageAge.setStatus("current")
_OutstandingDNSRequests_Type = Gauge32
_OutstandingDNSRequests_Object = MibScalar
outstandingDNSRequests = _OutstandingDNSRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 15),
    _OutstandingDNSRequests_Type()
)
outstandingDNSRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outstandingDNSRequests.setStatus("current")
_PendingDNSRequests_Type = Gauge32
_PendingDNSRequests_Object = MibScalar
pendingDNSRequests = _PendingDNSRequests_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 16),
    _PendingDNSRequests_Type()
)
pendingDNSRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pendingDNSRequests.setStatus("current")
_RaidEvents_Type = Counter32
_RaidEvents_Object = MibScalar
raidEvents = _RaidEvents_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 17),
    _RaidEvents_Type()
)
raidEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidEvents.setStatus("current")
_RaidTable_Object = MibTable
raidTable = _RaidTable_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    raidTable.setStatus("current")
_RaidEntry_Object = MibTableRow
raidEntry = _RaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1)
)
raidEntry.setIndexNames(
    (0, "ASYNCOS-MAIL-MIB", "raidIndex"),
)
if mibBuilder.loadTexts:
    raidEntry.setStatus("current")


class _RaidIndex_Type(Integer32):
    """Custom type raidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RaidIndex_Type.__name__ = "Integer32"
_RaidIndex_Object = MibTableColumn
raidIndex = _RaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 1),
    _RaidIndex_Type()
)
raidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidIndex.setStatus("current")


class _RaidStatus_Type(Integer32):
    """Custom type raidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("driveFailure", 2),
          ("driveHealthy", 1),
          ("driveRebuild", 3))
    )


_RaidStatus_Type.__name__ = "Integer32"
_RaidStatus_Object = MibTableColumn
raidStatus = _RaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 2),
    _RaidStatus_Type()
)
raidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidStatus.setStatus("current")
_RaidID_Type = DisplayString
_RaidID_Object = MibTableColumn
raidID = _RaidID_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 3),
    _RaidID_Type()
)
raidID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidID.setStatus("current")
_RaidLastError_Type = DisplayString
_RaidLastError_Object = MibTableColumn
raidLastError = _RaidLastError_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 18, 1, 4),
    _RaidLastError_Type()
)
raidLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidLastError.setStatus("current")
_OpenFilesOrSockets_Type = Gauge32
_OpenFilesOrSockets_Object = MibScalar
openFilesOrSockets = _OpenFilesOrSockets_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 19),
    _OpenFilesOrSockets_Type()
)
openFilesOrSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    openFilesOrSockets.setStatus("current")
_MailTransferThreads_Type = Gauge32
_MailTransferThreads_Object = MibScalar
mailTransferThreads = _MailTransferThreads_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 20),
    _MailTransferThreads_Type()
)
mailTransferThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailTransferThreads.setStatus("current")
_ConnectionURL_Type = DisplayString
_ConnectionURL_Object = MibScalar
connectionURL = _ConnectionURL_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 21),
    _ConnectionURL_Type()
)
connectionURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    connectionURL.setStatus("current")
_HsmErrorReason_Type = DisplayString
_HsmErrorReason_Object = MibScalar
hsmErrorReason = _HsmErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 1, 22),
    _HsmErrorReason_Type()
)
hsmErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsmErrorReason.setStatus("current")
_AsyncOSMailNotifications_ObjectIdentity = ObjectIdentity
asyncOSMailNotifications = _AsyncOSMailNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2)
)

# Managed Objects groups


# Notification objects

resourceConservationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 1)
)
resourceConservationMode.setObjects(
    ("ASYNCOS-MAIL-MIB", "resourceConservationReason")
)
if mibBuilder.loadTexts:
    resourceConservationMode.setStatus(
        "current"
    )

powerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 2)
)
powerSupplyStatusChange.setObjects(
    ("ASYNCOS-MAIL-MIB", "powerSupplyStatus")
)
if mibBuilder.loadTexts:
    powerSupplyStatusChange.setStatus(
        "current"
    )

highTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 3)
)
highTemperature.setObjects(
    ("ASYNCOS-MAIL-MIB", "temperatureName")
)
if mibBuilder.loadTexts:
    highTemperature.setStatus(
        "current"
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 4)
)
fanFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "fanName")
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        "current"
    )

keyExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 5)
)
keyExpiration.setObjects(
    ("ASYNCOS-MAIL-MIB", "keyDescription")
)
if mibBuilder.loadTexts:
    keyExpiration.setStatus(
        "current"
    )

updateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 6)
)
updateFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "updateServiceName")
)
if mibBuilder.loadTexts:
    updateFailure.setStatus(
        "current"
    )

raidStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 7)
)
raidStatusChange.setObjects(
    ("ASYNCOS-MAIL-MIB", "raidID")
)
if mibBuilder.loadTexts:
    raidStatusChange.setStatus(
        "current"
    )

connectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 8)
)
connectivityFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "connectionURL")
)
if mibBuilder.loadTexts:
    connectivityFailure.setStatus(
        "current"
    )

memoryUtilizationExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 9)
)
memoryUtilizationExceeded.setObjects(
    ("ASYNCOS-MAIL-MIB", "perCentMemoryUtilization")
)
if mibBuilder.loadTexts:
    memoryUtilizationExceeded.setStatus(
        "current"
    )

cpuUtilizationExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 10)
)
cpuUtilizationExceeded.setObjects(
    ("ASYNCOS-MAIL-MIB", "perCentCPUUtilization")
)
if mibBuilder.loadTexts:
    cpuUtilizationExceeded.setStatus(
        "current"
    )

hsmInitializationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 11)
)
hsmInitializationFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "hsmErrorReason")
)
if mibBuilder.loadTexts:
    hsmInitializationFailure.setStatus(
        "current"
    )

hsmResetLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15497, 1, 1, 2, 12)
)
hsmResetLoginFailure.setObjects(
    ("ASYNCOS-MAIL-MIB", "hsmErrorReason")
)
if mibBuilder.loadTexts:
    hsmResetLoginFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASYNCOS-MAIL-MIB",
    **{"asyncOSMailObjects": asyncOSMailObjects,
       "perCentMemoryUtilization": perCentMemoryUtilization,
       "perCentCPUUtilization": perCentCPUUtilization,
       "perCentDiskIOUtilization": perCentDiskIOUtilization,
       "perCentQueueUtilization": perCentQueueUtilization,
       "queueAvailabilityStatus": queueAvailabilityStatus,
       "resourceConservationReason": resourceConservationReason,
       "memoryAvailabilityStatus": memoryAvailabilityStatus,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyStatus": powerSupplyStatus,
       "powerSupplyRedundancy": powerSupplyRedundancy,
       "powerSupplyName": powerSupplyName,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureIndex": temperatureIndex,
       "degreesCelsius": degreesCelsius,
       "temperatureName": temperatureName,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanRPMs": fanRPMs,
       "fanName": fanName,
       "workQueueMessages": workQueueMessages,
       "keyExpirationTable": keyExpirationTable,
       "keyExpirationEntry": keyExpirationEntry,
       "keyExpirationIndex": keyExpirationIndex,
       "keyDescription": keyDescription,
       "keyIsPerpetual": keyIsPerpetual,
       "keySecondsUntilExpire": keySecondsUntilExpire,
       "updateTable": updateTable,
       "updateEntry": updateEntry,
       "updateIndex": updateIndex,
       "updateServiceName": updateServiceName,
       "updates": updates,
       "updateFailures": updateFailures,
       "oldestMessageAge": oldestMessageAge,
       "outstandingDNSRequests": outstandingDNSRequests,
       "pendingDNSRequests": pendingDNSRequests,
       "raidEvents": raidEvents,
       "raidTable": raidTable,
       "raidEntry": raidEntry,
       "raidIndex": raidIndex,
       "raidStatus": raidStatus,
       "raidID": raidID,
       "raidLastError": raidLastError,
       "openFilesOrSockets": openFilesOrSockets,
       "mailTransferThreads": mailTransferThreads,
       "connectionURL": connectionURL,
       "hsmErrorReason": hsmErrorReason,
       "asyncOSMailNotifications": asyncOSMailNotifications,
       "resourceConservationMode": resourceConservationMode,
       "powerSupplyStatusChange": powerSupplyStatusChange,
       "highTemperature": highTemperature,
       "fanFailure": fanFailure,
       "keyExpiration": keyExpiration,
       "updateFailure": updateFailure,
       "raidStatusChange": raidStatusChange,
       "connectivityFailure": connectivityFailure,
       "memoryUtilizationExceeded": memoryUtilizationExceeded,
       "cpuUtilizationExceeded": cpuUtilizationExceeded,
       "hsmInitializationFailure": hsmInitializationFailure,
       "hsmResetLoginFailure": hsmResetLoginFailure}
)
