# SNMP MIB module (CISCO-C8500-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-C8500-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:29 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoC8500RedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105)
)
ciscoC8500RedundancyMIB.setRevisions(
        ("2003-05-04 00:00",
         "1998-06-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RedundancyStatus(Integer32, TextualConvention):
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
        *(("fault", 3),
          ("notPresent", 1),
          ("ok", 2))
    )



class RedundancyMode(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 1),
          ("notPresent", 4),
          ("standby", 2),
          ("unused", 3))
    )



class RedundancySlotIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoC8500RedundancyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoC8500RedundancyMIBObjects = _CiscoC8500RedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1)
)
_CcrCpu_ObjectIdentity = ObjectIdentity
ccrCpu = _CcrCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1)
)
_CcrCpuTable_Object = MibTable
ccrCpuTable = _CcrCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccrCpuTable.setStatus("current")
_CcrCpuEntry_Object = MibTableRow
ccrCpuEntry = _CcrCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1)
)
ccrCpuEntry.setIndexNames(
    (0, "CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSlotIndex"),
)
if mibBuilder.loadTexts:
    ccrCpuEntry.setStatus("current")
_CcrCpuSlotIndex_Type = RedundancySlotIndex
_CcrCpuSlotIndex_Object = MibTableColumn
ccrCpuSlotIndex = _CcrCpuSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 1),
    _CcrCpuSlotIndex_Type()
)
ccrCpuSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrCpuSlotIndex.setStatus("current")
_CcrCpuMode_Type = RedundancyMode
_CcrCpuMode_Object = MibTableColumn
ccrCpuMode = _CcrCpuMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 2),
    _CcrCpuMode_Type()
)
ccrCpuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrCpuMode.setStatus("current")
_CcrCpuStatus_Type = RedundancyStatus
_CcrCpuStatus_Object = MibTableColumn
ccrCpuStatus = _CcrCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 1, 1, 3),
    _CcrCpuStatus_Type()
)
ccrCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrCpuStatus.setStatus("current")


class _CcrSyncConfigOnSet_Type(Bits):
    """Custom type ccrSyncConfigOnSet based on Bits"""
    namedValues = NamedValues(
        *(("runningConfig", 0),
          ("startupConfig", 1))
    )

_CcrSyncConfigOnSet_Type.__name__ = "Bits"
_CcrSyncConfigOnSet_Object = MibScalar
ccrSyncConfigOnSet = _CcrSyncConfigOnSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 2),
    _CcrSyncConfigOnSet_Type()
)
ccrSyncConfigOnSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrSyncConfigOnSet.setStatus("current")


class _CcrCpuStandbyEnableMode_Type(TruthValue):
    """Custom type ccrCpuStandbyEnableMode based on TruthValue"""


_CcrCpuStandbyEnableMode_Object = MibScalar
ccrCpuStandbyEnableMode = _CcrCpuStandbyEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 3),
    _CcrCpuStandbyEnableMode_Type()
)
ccrCpuStandbyEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrCpuStandbyEnableMode.setStatus("current")


class _CcrCpuSwitchoverTime_Type(Integer32):
    """Custom type ccrCpuSwitchoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcrCpuSwitchoverTime_Type.__name__ = "Integer32"
_CcrCpuSwitchoverTime_Object = MibScalar
ccrCpuSwitchoverTime = _CcrCpuSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 4),
    _CcrCpuSwitchoverTime_Type()
)
ccrCpuSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrCpuSwitchoverTime.setStatus("current")
if mibBuilder.loadTexts:
    ccrCpuSwitchoverTime.setUnits("seconds")


class _CcrForceCounterSync_Type(Integer32):
    """Custom type ccrForceCounterSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcesync", 1),
          ("noop", 2))
    )


_CcrForceCounterSync_Type.__name__ = "Integer32"
_CcrForceCounterSync_Object = MibScalar
ccrForceCounterSync = _CcrForceCounterSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 5),
    _CcrForceCounterSync_Type()
)
ccrForceCounterSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrForceCounterSync.setStatus("current")


class _CcrIfCounterSyncFreq_Type(Integer32):
    """Custom type ccrIfCounterSyncFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CcrIfCounterSyncFreq_Type.__name__ = "Integer32"
_CcrIfCounterSyncFreq_Object = MibScalar
ccrIfCounterSyncFreq = _CcrIfCounterSyncFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 6),
    _CcrIfCounterSyncFreq_Type()
)
ccrIfCounterSyncFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrIfCounterSyncFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccrIfCounterSyncFreq.setUnits("minutes")


class _CcrVcCounterSyncFreq_Type(Integer32):
    """Custom type ccrVcCounterSyncFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CcrVcCounterSyncFreq_Type.__name__ = "Integer32"
_CcrVcCounterSyncFreq_Object = MibScalar
ccrVcCounterSyncFreq = _CcrVcCounterSyncFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 7),
    _CcrVcCounterSyncFreq_Type()
)
ccrVcCounterSyncFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrVcCounterSyncFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccrVcCounterSyncFreq.setUnits("minutes")
_CcrSigCounterSyncEnable_Type = TruthValue
_CcrSigCounterSyncEnable_Object = MibScalar
ccrSigCounterSyncEnable = _CcrSigCounterSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 1, 8),
    _CcrSigCounterSyncEnable_Type()
)
ccrSigCounterSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrSigCounterSyncEnable.setStatus("current")
_CcrSwitch_ObjectIdentity = ObjectIdentity
ccrSwitch = _CcrSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2)
)
_CcrSwitchTable_Object = MibTable
ccrSwitchTable = _CcrSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccrSwitchTable.setStatus("current")
_CcrSwitchEntry_Object = MibTableRow
ccrSwitchEntry = _CcrSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1)
)
ccrSwitchEntry.setIndexNames(
    (0, "CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchSlotIndex"),
)
if mibBuilder.loadTexts:
    ccrSwitchEntry.setStatus("current")
_CcrSwitchSlotIndex_Type = RedundancySlotIndex
_CcrSwitchSlotIndex_Object = MibTableColumn
ccrSwitchSlotIndex = _CcrSwitchSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 1),
    _CcrSwitchSlotIndex_Type()
)
ccrSwitchSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrSwitchSlotIndex.setStatus("current")
_CcrSwitchMode_Type = RedundancyMode
_CcrSwitchMode_Object = MibTableColumn
ccrSwitchMode = _CcrSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 2),
    _CcrSwitchMode_Type()
)
ccrSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrSwitchMode.setStatus("current")
_CcrSwitchStatus_Type = RedundancyStatus
_CcrSwitchStatus_Object = MibTableColumn
ccrSwitchStatus = _CcrSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 1, 1, 3),
    _CcrSwitchStatus_Type()
)
ccrSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrSwitchStatus.setStatus("current")
_CcrSwitchLastSwitchoverTime_Type = TimeStamp
_CcrSwitchLastSwitchoverTime_Object = MibScalar
ccrSwitchLastSwitchoverTime = _CcrSwitchLastSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 2),
    _CcrSwitchLastSwitchoverTime_Type()
)
ccrSwitchLastSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrSwitchLastSwitchoverTime.setStatus("current")


class _CcrSwitchLastSwitchoverReason_Type(Integer32):
    """Custom type ccrSwitchLastSwitchoverReason based on Integer32"""
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
        *(("cardFailed", 4),
          ("cardInserted", 7),
          ("cardRecovered", 5),
          ("cardRemoved", 6),
          ("none", 1),
          ("notKnown", 2),
          ("userInitiated", 3))
    )


_CcrSwitchLastSwitchoverReason_Type.__name__ = "Integer32"
_CcrSwitchLastSwitchoverReason_Object = MibScalar
ccrSwitchLastSwitchoverReason = _CcrSwitchLastSwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 3),
    _CcrSwitchLastSwitchoverReason_Type()
)
ccrSwitchLastSwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrSwitchLastSwitchoverReason.setStatus("current")


class _CcrSwitchBw_Type(Integer32):
    """Custom type ccrSwitchBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenGbps", 1),
          ("twentyGbps", 2))
    )


_CcrSwitchBw_Type.__name__ = "Integer32"
_CcrSwitchBw_Object = MibScalar
ccrSwitchBw = _CcrSwitchBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 4),
    _CcrSwitchBw_Type()
)
ccrSwitchBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrSwitchBw.setStatus("current")


class _CcrDesiredSwitchBw_Type(Integer32):
    """Custom type ccrDesiredSwitchBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenGbps", 1),
          ("twentyGbps", 2))
    )


_CcrDesiredSwitchBw_Type.__name__ = "Integer32"
_CcrDesiredSwitchBw_Object = MibScalar
ccrDesiredSwitchBw = _CcrDesiredSwitchBw_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 1, 2, 5),
    _CcrDesiredSwitchBw_Type()
)
ccrDesiredSwitchBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrDesiredSwitchBw.setStatus("current")
_CiscoC8500RedundancyMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoC8500RedundancyMIBNotificationPrefix = _CiscoC8500RedundancyMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 2)
)
_CcrMIBNotifications_ObjectIdentity = ObjectIdentity
ccrMIBNotifications = _CcrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0)
)
_CiscoC8500RedundancyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoC8500RedundancyMIBConformance = _CiscoC8500RedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3)
)
_CiscoC8500RedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoC8500RedundancyMIBCompliances = _CiscoC8500RedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1)
)
_CiscoC8500RedundancyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoC8500RedundancyMIBGroups = _CiscoC8500RedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2)
)

# Managed Objects groups

ccrCpuMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 1)
)
ccrCpuMibGroup.setObjects(
      *(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"))
)
if mibBuilder.loadTexts:
    ccrCpuMibGroup.setStatus("obsolete")

ccrSwitchMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 2)
)
ccrSwitchMibGroup.setObjects(
      *(("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverTime"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchLastSwitchoverReason"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchBw"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrDesiredSwitchBw"))
)
if mibBuilder.loadTexts:
    ccrSwitchMibGroup.setStatus("current")

ccrCpuMibGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 4)
)
ccrCpuMibGroup1.setObjects(
      *(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuMode"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSyncConfigOnSet"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStandbyEnableMode"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuSwitchoverTime"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrForceCounterSync"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrIfCounterSyncFreq"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrVcCounterSyncFreq"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSigCounterSyncEnable"))
)
if mibBuilder.loadTexts:
    ccrCpuMibGroup1.setStatus("current")


# Notification objects

ccrCpuStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 1)
)
ccrCpuStatusChange.setObjects(
    ("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatus")
)
if mibBuilder.loadTexts:
    ccrCpuStatusChange.setStatus(
        "current"
    )

ccrSwitchStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 2)
)
ccrSwitchStatusChange.setObjects(
    ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatus")
)
if mibBuilder.loadTexts:
    ccrSwitchStatusChange.setStatus(
        "current"
    )

ccrSwitchModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 2, 0, 3)
)
ccrSwitchModeChange.setObjects(
    ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchMode")
)
if mibBuilder.loadTexts:
    ccrSwitchModeChange.setStatus(
        "current"
    )


# Notifications groups

ccrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 2, 3)
)
ccrNotificationsGroup.setObjects(
      *(("CISCO-C8500-REDUNDANCY-MIB", "ccrCpuStatusChange"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchStatusChange"),
        ("CISCO-C8500-REDUNDANCY-MIB", "ccrSwitchModeChange"))
)
if mibBuilder.loadTexts:
    ccrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoC8500RedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoC8500RedundancyMIBCompliance.setStatus(
        "obsolete"
    )

ciscoC8500RedundancyMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 105, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoC8500RedundancyMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-C8500-REDUNDANCY-MIB",
    **{"RedundancyStatus": RedundancyStatus,
       "RedundancyMode": RedundancyMode,
       "RedundancySlotIndex": RedundancySlotIndex,
       "ciscoC8500RedundancyMIB": ciscoC8500RedundancyMIB,
       "ciscoC8500RedundancyMIBObjects": ciscoC8500RedundancyMIBObjects,
       "ccrCpu": ccrCpu,
       "ccrCpuTable": ccrCpuTable,
       "ccrCpuEntry": ccrCpuEntry,
       "ccrCpuSlotIndex": ccrCpuSlotIndex,
       "ccrCpuMode": ccrCpuMode,
       "ccrCpuStatus": ccrCpuStatus,
       "ccrSyncConfigOnSet": ccrSyncConfigOnSet,
       "ccrCpuStandbyEnableMode": ccrCpuStandbyEnableMode,
       "ccrCpuSwitchoverTime": ccrCpuSwitchoverTime,
       "ccrForceCounterSync": ccrForceCounterSync,
       "ccrIfCounterSyncFreq": ccrIfCounterSyncFreq,
       "ccrVcCounterSyncFreq": ccrVcCounterSyncFreq,
       "ccrSigCounterSyncEnable": ccrSigCounterSyncEnable,
       "ccrSwitch": ccrSwitch,
       "ccrSwitchTable": ccrSwitchTable,
       "ccrSwitchEntry": ccrSwitchEntry,
       "ccrSwitchSlotIndex": ccrSwitchSlotIndex,
       "ccrSwitchMode": ccrSwitchMode,
       "ccrSwitchStatus": ccrSwitchStatus,
       "ccrSwitchLastSwitchoverTime": ccrSwitchLastSwitchoverTime,
       "ccrSwitchLastSwitchoverReason": ccrSwitchLastSwitchoverReason,
       "ccrSwitchBw": ccrSwitchBw,
       "ccrDesiredSwitchBw": ccrDesiredSwitchBw,
       "ciscoC8500RedundancyMIBNotificationPrefix": ciscoC8500RedundancyMIBNotificationPrefix,
       "ccrMIBNotifications": ccrMIBNotifications,
       "ccrCpuStatusChange": ccrCpuStatusChange,
       "ccrSwitchStatusChange": ccrSwitchStatusChange,
       "ccrSwitchModeChange": ccrSwitchModeChange,
       "ciscoC8500RedundancyMIBConformance": ciscoC8500RedundancyMIBConformance,
       "ciscoC8500RedundancyMIBCompliances": ciscoC8500RedundancyMIBCompliances,
       "ciscoC8500RedundancyMIBCompliance": ciscoC8500RedundancyMIBCompliance,
       "ciscoC8500RedundancyMIBComplianceRev1": ciscoC8500RedundancyMIBComplianceRev1,
       "ciscoC8500RedundancyMIBGroups": ciscoC8500RedundancyMIBGroups,
       "ccrCpuMibGroup": ccrCpuMibGroup,
       "ccrSwitchMibGroup": ccrSwitchMibGroup,
       "ccrNotificationsGroup": ccrNotificationsGroup,
       "ccrCpuMibGroup1": ccrCpuMibGroup1}
)
