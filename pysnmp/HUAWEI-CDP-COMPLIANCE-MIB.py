# SNMP MIB module (HUAWEI-CDP-COMPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-CDP-COMPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:19 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(TimeFilter,
 ZeroBasedCounter32) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter",
    "ZeroBasedCounter32")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwCdpComplianceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwCdpComplianceObjects_ObjectIdentity = ObjectIdentity
hwCdpComplianceObjects = _HwCdpComplianceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1)
)
_HwCdpComplianceConfiguration_ObjectIdentity = ObjectIdentity
hwCdpComplianceConfiguration = _HwCdpComplianceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1)
)


class _HwCdpComplianceEnable_Type(EnabledStatus):
    """Custom type hwCdpComplianceEnable based on EnabledStatus"""


_HwCdpComplianceEnable_Object = MibScalar
hwCdpComplianceEnable = _HwCdpComplianceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 1),
    _HwCdpComplianceEnable_Type()
)
hwCdpComplianceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpComplianceEnable.setStatus("current")


class _HwCdpComplianceNotificationInterval_Type(Integer32):
    """Custom type hwCdpComplianceNotificationInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwCdpComplianceNotificationInterval_Type.__name__ = "Integer32"
_HwCdpComplianceNotificationInterval_Object = MibScalar
hwCdpComplianceNotificationInterval = _HwCdpComplianceNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 2),
    _HwCdpComplianceNotificationInterval_Type()
)
hwCdpComplianceNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpComplianceNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwCdpComplianceNotificationInterval.setUnits("seconds")
_HwCdpCompliancePortConfigTable_Object = MibTable
hwCdpCompliancePortConfigTable = _HwCdpCompliancePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigTable.setStatus("current")
_HwCdpCompliancePortConfigEntry_Object = MibTableRow
hwCdpCompliancePortConfigEntry = _HwCdpCompliancePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1)
)
hwCdpCompliancePortConfigEntry.setIndexNames(
    (0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigEntry.setStatus("current")
_HwCdpCompliancePortConfigIfIndex_Type = InterfaceIndex
_HwCdpCompliancePortConfigIfIndex_Object = MibTableColumn
hwCdpCompliancePortConfigIfIndex = _HwCdpCompliancePortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 1),
    _HwCdpCompliancePortConfigIfIndex_Type()
)
hwCdpCompliancePortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigIfIndex.setStatus("current")


class _HwCdpCompliancePortConfigAdminStatus_Type(Integer32):
    """Custom type hwCdpCompliancePortConfigAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("rxOnly", 2))
    )


_HwCdpCompliancePortConfigAdminStatus_Type.__name__ = "Integer32"
_HwCdpCompliancePortConfigAdminStatus_Object = MibTableColumn
hwCdpCompliancePortConfigAdminStatus = _HwCdpCompliancePortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 2),
    _HwCdpCompliancePortConfigAdminStatus_Type()
)
hwCdpCompliancePortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigAdminStatus.setStatus("current")


class _HwCdpCompliancePortConfigHoldTime_Type(Integer32):
    """Custom type hwCdpCompliancePortConfigHoldTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 254),
    )


_HwCdpCompliancePortConfigHoldTime_Type.__name__ = "Integer32"
_HwCdpCompliancePortConfigHoldTime_Object = MibTableColumn
hwCdpCompliancePortConfigHoldTime = _HwCdpCompliancePortConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 3),
    _HwCdpCompliancePortConfigHoldTime_Type()
)
hwCdpCompliancePortConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigHoldTime.setUnits("seconds")


class _HwCdpCompliancePortConfigNotificationEnable_Type(TruthValue):
    """Custom type hwCdpCompliancePortConfigNotificationEnable based on TruthValue"""


_HwCdpCompliancePortConfigNotificationEnable_Object = MibTableColumn
hwCdpCompliancePortConfigNotificationEnable = _HwCdpCompliancePortConfigNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 4),
    _HwCdpCompliancePortConfigNotificationEnable_Type()
)
hwCdpCompliancePortConfigNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpCompliancePortConfigNotificationEnable.setStatus("current")
_HwCdpCompliancePortStatsReset_Type = EnabledStatus
_HwCdpCompliancePortStatsReset_Object = MibTableColumn
hwCdpCompliancePortStatsReset = _HwCdpCompliancePortStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 1, 3, 1, 5),
    _HwCdpCompliancePortStatsReset_Type()
)
hwCdpCompliancePortStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCdpCompliancePortStatsReset.setStatus("current")
_HwCdpComplianceStatistics_ObjectIdentity = ObjectIdentity
hwCdpComplianceStatistics = _HwCdpComplianceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2)
)
_HwCdpComplianceStatsRemTablesLastChangeTime_Type = TimeStamp
_HwCdpComplianceStatsRemTablesLastChangeTime_Object = MibScalar
hwCdpComplianceStatsRemTablesLastChangeTime = _HwCdpComplianceStatsRemTablesLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 1),
    _HwCdpComplianceStatsRemTablesLastChangeTime_Type()
)
hwCdpComplianceStatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRemTablesLastChangeTime.setStatus("current")
_HwCdpComplianceStatsRemTablesAgeouts_Type = ZeroBasedCounter32
_HwCdpComplianceStatsRemTablesAgeouts_Object = MibScalar
hwCdpComplianceStatsRemTablesAgeouts = _HwCdpComplianceStatsRemTablesAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 2),
    _HwCdpComplianceStatsRemTablesAgeouts_Type()
)
hwCdpComplianceStatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRemTablesAgeouts.setStatus("current")
_HwCdpComplianceStatsRxPortTable_Object = MibTable
hwCdpComplianceStatsRxPortTable = _HwCdpComplianceStatsRxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRxPortTable.setStatus("current")
_HwCdpComplianceStatsRxPortEntry_Object = MibTableRow
hwCdpComplianceStatsRxPortEntry = _HwCdpComplianceStatsRxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1)
)
hwCdpComplianceStatsRxPortEntry.setIndexNames(
    (0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRxPortEntry.setStatus("current")
_HwCdpComplianceStatsRxPortIfIndex_Type = InterfaceIndex
_HwCdpComplianceStatsRxPortIfIndex_Object = MibTableColumn
hwCdpComplianceStatsRxPortIfIndex = _HwCdpComplianceStatsRxPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 1),
    _HwCdpComplianceStatsRxPortIfIndex_Type()
)
hwCdpComplianceStatsRxPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRxPortIfIndex.setStatus("current")
_HwCdpComplianceStatsRxPortFramesTotal_Type = Counter32
_HwCdpComplianceStatsRxPortFramesTotal_Object = MibTableColumn
hwCdpComplianceStatsRxPortFramesTotal = _HwCdpComplianceStatsRxPortFramesTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 2),
    _HwCdpComplianceStatsRxPortFramesTotal_Type()
)
hwCdpComplianceStatsRxPortFramesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRxPortFramesTotal.setStatus("current")
_HwCdpComplianceStatsRxPortAgeoutsTotal_Type = Counter32
_HwCdpComplianceStatsRxPortAgeoutsTotal_Object = MibTableColumn
hwCdpComplianceStatsRxPortAgeoutsTotal = _HwCdpComplianceStatsRxPortAgeoutsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 2, 3, 1, 3),
    _HwCdpComplianceStatsRxPortAgeoutsTotal_Type()
)
hwCdpComplianceStatsRxPortAgeoutsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceStatsRxPortAgeoutsTotal.setStatus("current")
_HwCdpComplianceRemoteSystemsData_ObjectIdentity = ObjectIdentity
hwCdpComplianceRemoteSystemsData = _HwCdpComplianceRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3)
)
_HwCdpComplianceRemoteTable_Object = MibTable
hwCdpComplianceRemoteTable = _HwCdpComplianceRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwCdpComplianceRemoteTable.setStatus("current")
_HwCdpComplianceRemoteEntry_Object = MibTableRow
hwCdpComplianceRemoteEntry = _HwCdpComplianceRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1)
)
hwCdpComplianceRemoteEntry.setIndexNames(
    (0, "HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemLocalPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwCdpComplianceRemoteEntry.setStatus("current")
_HwCdpComplianceRemLocalPortIfIndex_Type = InterfaceIndex
_HwCdpComplianceRemLocalPortIfIndex_Object = MibTableColumn
hwCdpComplianceRemLocalPortIfIndex = _HwCdpComplianceRemLocalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 1),
    _HwCdpComplianceRemLocalPortIfIndex_Type()
)
hwCdpComplianceRemLocalPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCdpComplianceRemLocalPortIfIndex.setStatus("current")
_HwCdpComplianceRemTimeMark_Type = TimeFilter
_HwCdpComplianceRemTimeMark_Object = MibTableColumn
hwCdpComplianceRemTimeMark = _HwCdpComplianceRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 2),
    _HwCdpComplianceRemTimeMark_Type()
)
hwCdpComplianceRemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceRemTimeMark.setStatus("current")


class _HwCdpComplianceRemoteInfo_Type(OctetString):
    """Custom type hwCdpComplianceRemoteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1600),
    )


_HwCdpComplianceRemoteInfo_Type.__name__ = "OctetString"
_HwCdpComplianceRemoteInfo_Object = MibTableColumn
hwCdpComplianceRemoteInfo = _HwCdpComplianceRemoteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 1, 3, 1, 1, 3),
    _HwCdpComplianceRemoteInfo_Type()
)
hwCdpComplianceRemoteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCdpComplianceRemoteInfo.setStatus("current")
_HwCdpComplianceNotifications_ObjectIdentity = ObjectIdentity
hwCdpComplianceNotifications = _HwCdpComplianceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2)
)
_HwCdpComplianceNotificationPrefix_ObjectIdentity = ObjectIdentity
hwCdpComplianceNotificationPrefix = _HwCdpComplianceNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2, 1)
)
_HwCdpComplianceConformance_ObjectIdentity = ObjectIdentity
hwCdpComplianceConformance = _HwCdpComplianceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3)
)
_HwCdpComplianceCompliances_ObjectIdentity = ObjectIdentity
hwCdpComplianceCompliances = _HwCdpComplianceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 1)
)
_HwCdpComplianceGroups_ObjectIdentity = ObjectIdentity
hwCdpComplianceGroups = _HwCdpComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2)
)

# Managed Objects groups

hwCdpComplianceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 1)
)
hwCdpComplianceConfigGroup.setObjects(
      *(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceEnable"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceNotificationInterval"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigAdminStatus"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigHoldTime"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortConfigNotificationEnable"))
)
if mibBuilder.loadTexts:
    hwCdpComplianceConfigGroup.setStatus("current")

hwCdpComplianceStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 2)
)
hwCdpComplianceStatsGroup.setObjects(
      *(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortFramesTotal"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpCompliancePortStatsReset"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesLastChangeTime"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesAgeouts"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRxPortAgeoutsTotal"))
)
if mibBuilder.loadTexts:
    hwCdpComplianceStatsGroup.setStatus("current")

hwCdpComplianceRemSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 3)
)
hwCdpComplianceRemSysGroup.setObjects(
      *(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemoteInfo"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemTimeMark"))
)
if mibBuilder.loadTexts:
    hwCdpComplianceRemSysGroup.setStatus("current")


# Notification objects

hwCdpComplianceRemTablesChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 2, 1, 1)
)
hwCdpComplianceRemTablesChange.setObjects(
      *(("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesLastChangeTime"),
        ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceStatsRemTablesAgeouts"))
)
if mibBuilder.loadTexts:
    hwCdpComplianceRemTablesChange.setStatus(
        "current"
    )


# Notifications groups

hwCdpComplianceTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 2, 4)
)
hwCdpComplianceTrapGroup.setObjects(
    ("HUAWEI-CDP-COMPLIANCE-MIB", "hwCdpComplianceRemTablesChange")
)
if mibBuilder.loadTexts:
    hwCdpComplianceTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwCdpComplianceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 198, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwCdpComplianceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-CDP-COMPLIANCE-MIB",
    **{"hwCdpComplianceMIB": hwCdpComplianceMIB,
       "hwCdpComplianceObjects": hwCdpComplianceObjects,
       "hwCdpComplianceConfiguration": hwCdpComplianceConfiguration,
       "hwCdpComplianceEnable": hwCdpComplianceEnable,
       "hwCdpComplianceNotificationInterval": hwCdpComplianceNotificationInterval,
       "hwCdpCompliancePortConfigTable": hwCdpCompliancePortConfigTable,
       "hwCdpCompliancePortConfigEntry": hwCdpCompliancePortConfigEntry,
       "hwCdpCompliancePortConfigIfIndex": hwCdpCompliancePortConfigIfIndex,
       "hwCdpCompliancePortConfigAdminStatus": hwCdpCompliancePortConfigAdminStatus,
       "hwCdpCompliancePortConfigHoldTime": hwCdpCompliancePortConfigHoldTime,
       "hwCdpCompliancePortConfigNotificationEnable": hwCdpCompliancePortConfigNotificationEnable,
       "hwCdpCompliancePortStatsReset": hwCdpCompliancePortStatsReset,
       "hwCdpComplianceStatistics": hwCdpComplianceStatistics,
       "hwCdpComplianceStatsRemTablesLastChangeTime": hwCdpComplianceStatsRemTablesLastChangeTime,
       "hwCdpComplianceStatsRemTablesAgeouts": hwCdpComplianceStatsRemTablesAgeouts,
       "hwCdpComplianceStatsRxPortTable": hwCdpComplianceStatsRxPortTable,
       "hwCdpComplianceStatsRxPortEntry": hwCdpComplianceStatsRxPortEntry,
       "hwCdpComplianceStatsRxPortIfIndex": hwCdpComplianceStatsRxPortIfIndex,
       "hwCdpComplianceStatsRxPortFramesTotal": hwCdpComplianceStatsRxPortFramesTotal,
       "hwCdpComplianceStatsRxPortAgeoutsTotal": hwCdpComplianceStatsRxPortAgeoutsTotal,
       "hwCdpComplianceRemoteSystemsData": hwCdpComplianceRemoteSystemsData,
       "hwCdpComplianceRemoteTable": hwCdpComplianceRemoteTable,
       "hwCdpComplianceRemoteEntry": hwCdpComplianceRemoteEntry,
       "hwCdpComplianceRemLocalPortIfIndex": hwCdpComplianceRemLocalPortIfIndex,
       "hwCdpComplianceRemTimeMark": hwCdpComplianceRemTimeMark,
       "hwCdpComplianceRemoteInfo": hwCdpComplianceRemoteInfo,
       "hwCdpComplianceNotifications": hwCdpComplianceNotifications,
       "hwCdpComplianceNotificationPrefix": hwCdpComplianceNotificationPrefix,
       "hwCdpComplianceRemTablesChange": hwCdpComplianceRemTablesChange,
       "hwCdpComplianceConformance": hwCdpComplianceConformance,
       "hwCdpComplianceCompliances": hwCdpComplianceCompliances,
       "hwCdpComplianceCompliance": hwCdpComplianceCompliance,
       "hwCdpComplianceGroups": hwCdpComplianceGroups,
       "hwCdpComplianceConfigGroup": hwCdpComplianceConfigGroup,
       "hwCdpComplianceStatsGroup": hwCdpComplianceStatsGroup,
       "hwCdpComplianceRemSysGroup": hwCdpComplianceRemSysGroup,
       "hwCdpComplianceTrapGroup": hwCdpComplianceTrapGroup}
)
