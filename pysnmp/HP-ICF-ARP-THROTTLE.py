# SNMP MIB module (HP-ICF-ARP-THROTTLE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-ARP-THROTTLE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:04 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfArpThrottle = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119)
)
hpicfArpThrottle.setRevisions(
        ("2015-05-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfArpThrottleNotifications_ObjectIdentity = ObjectIdentity
hpicfArpThrottleNotifications = _HpicfArpThrottleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 0)
)
_HpicfArpThrottleObjects_ObjectIdentity = ObjectIdentity
hpicfArpThrottleObjects = _HpicfArpThrottleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1)
)
_HpicfArpThrottleClientOverThreshold_Type = MacAddress
_HpicfArpThrottleClientOverThreshold_Object = MibScalar
hpicfArpThrottleClientOverThreshold = _HpicfArpThrottleClientOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 1),
    _HpicfArpThrottleClientOverThreshold_Type()
)
hpicfArpThrottleClientOverThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpThrottleClientOverThreshold.setStatus("current")
_HpicfArpThrottleConfig_ObjectIdentity = ObjectIdentity
hpicfArpThrottleConfig = _HpicfArpThrottleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2)
)
_HpicfArpThrottleEnable_Type = TruthValue
_HpicfArpThrottleEnable_Object = MibScalar
hpicfArpThrottleEnable = _HpicfArpThrottleEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 1),
    _HpicfArpThrottleEnable_Type()
)
hpicfArpThrottleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpThrottleEnable.setStatus("current")


class _HpicfArpThrottleRemediationMode_Type(Integer32):
    """Custom type hpicfArpThrottleRemediationMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("monitor", 0))
    )


_HpicfArpThrottleRemediationMode_Type.__name__ = "Integer32"
_HpicfArpThrottleRemediationMode_Object = MibScalar
hpicfArpThrottleRemediationMode = _HpicfArpThrottleRemediationMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 2),
    _HpicfArpThrottleRemediationMode_Type()
)
hpicfArpThrottleRemediationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpThrottleRemediationMode.setStatus("current")


class _HpicfArpThrottleThreshold_Type(Integer32):
    """Custom type hpicfArpThrottleThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpicfArpThrottleThreshold_Type.__name__ = "Integer32"
_HpicfArpThrottleThreshold_Object = MibScalar
hpicfArpThrottleThreshold = _HpicfArpThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 3),
    _HpicfArpThrottleThreshold_Type()
)
hpicfArpThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpThrottleThreshold.setStatus("current")


class _HpicfArpThrottleBlacklistAgingTime_Type(Integer32):
    """Custom type hpicfArpThrottleBlacklistAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_HpicfArpThrottleBlacklistAgingTime_Type.__name__ = "Integer32"
_HpicfArpThrottleBlacklistAgingTime_Object = MibScalar
hpicfArpThrottleBlacklistAgingTime = _HpicfArpThrottleBlacklistAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 4),
    _HpicfArpThrottleBlacklistAgingTime_Type()
)
hpicfArpThrottleBlacklistAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpThrottleBlacklistAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfArpThrottleBlacklistAgingTime.setUnits("seconds")
_HpicfArpThrottleExcludedMacTable_Object = MibTable
hpicfArpThrottleExcludedMacTable = _HpicfArpThrottleExcludedMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfArpThrottleExcludedMacTable.setStatus("current")
_HpicfArpThrottleExcludedMacEntry_Object = MibTableRow
hpicfArpThrottleExcludedMacEntry = _HpicfArpThrottleExcludedMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 5, 1)
)
hpicfArpThrottleExcludedMacEntry.setIndexNames(
    (0, "HP-ICF-ARP-THROTTLE", "hpicfArpThrottleExcludedMac"),
)
if mibBuilder.loadTexts:
    hpicfArpThrottleExcludedMacEntry.setStatus("current")
_HpicfArpThrottleExcludedMac_Type = MacAddress
_HpicfArpThrottleExcludedMac_Object = MibTableColumn
hpicfArpThrottleExcludedMac = _HpicfArpThrottleExcludedMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 5, 1, 1),
    _HpicfArpThrottleExcludedMac_Type()
)
hpicfArpThrottleExcludedMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfArpThrottleExcludedMac.setStatus("current")
_HpicfArpThrottleExcludedMacStatus_Type = RowStatus
_HpicfArpThrottleExcludedMacStatus_Object = MibTableColumn
hpicfArpThrottleExcludedMacStatus = _HpicfArpThrottleExcludedMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 2, 5, 1, 2),
    _HpicfArpThrottleExcludedMacStatus_Type()
)
hpicfArpThrottleExcludedMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfArpThrottleExcludedMacStatus.setStatus("current")
_HpicfArpThrottleStats_ObjectIdentity = ObjectIdentity
hpicfArpThrottleStats = _HpicfArpThrottleStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 3)
)
_HpicfArpThrottleStatsNumClientsInBlacklist_Type = Counter32
_HpicfArpThrottleStatsNumClientsInBlacklist_Object = MibScalar
hpicfArpThrottleStatsNumClientsInBlacklist = _HpicfArpThrottleStatsNumClientsInBlacklist_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 3, 1),
    _HpicfArpThrottleStatsNumClientsInBlacklist_Type()
)
hpicfArpThrottleStatsNumClientsInBlacklist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpThrottleStatsNumClientsInBlacklist.setStatus("current")
_HpicfArpThrottleStatsNumClientsBeingTracked_Type = Counter32
_HpicfArpThrottleStatsNumClientsBeingTracked_Object = MibScalar
hpicfArpThrottleStatsNumClientsBeingTracked = _HpicfArpThrottleStatsNumClientsBeingTracked_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 1, 3, 2),
    _HpicfArpThrottleStatsNumClientsBeingTracked_Type()
)
hpicfArpThrottleStatsNumClientsBeingTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpThrottleStatsNumClientsBeingTracked.setStatus("current")
_HpicfArpThrottleConformance_ObjectIdentity = ObjectIdentity
hpicfArpThrottleConformance = _HpicfArpThrottleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2)
)
_HpicfArpThrottleGroups_ObjectIdentity = ObjectIdentity
hpicfArpThrottleGroups = _HpicfArpThrottleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2, 1)
)
_HpicfArpThrottleCompliances_ObjectIdentity = ObjectIdentity
hpicfArpThrottleCompliances = _HpicfArpThrottleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2, 2)
)

# Managed Objects groups

hpicfArpThrottleBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2, 1, 1)
)
hpicfArpThrottleBaseGroup.setObjects(
      *(("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleEnable"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleRemediationMode"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleThreshold"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleBlacklistAgingTime"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleExcludedMacStatus"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleStatsNumClientsInBlacklist"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleStatsNumClientsBeingTracked"),
        ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleClientOverThreshold"))
)
if mibBuilder.loadTexts:
    hpicfArpThrottleBaseGroup.setStatus("current")


# Notification objects

hpicfArpThrottleExceedThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 0, 1)
)
hpicfArpThrottleExceedThresholdTrap.setObjects(
    ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleClientOverThreshold")
)
if mibBuilder.loadTexts:
    hpicfArpThrottleExceedThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfArpThrottleNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2, 1, 2)
)
hpicfArpThrottleNotificationGroup.setObjects(
    ("HP-ICF-ARP-THROTTLE", "hpicfArpThrottleExceedThresholdTrap")
)
if mibBuilder.loadTexts:
    hpicfArpThrottleNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfArpThrottleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfArpThrottleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-ARP-THROTTLE",
    **{"hpicfArpThrottle": hpicfArpThrottle,
       "hpicfArpThrottleNotifications": hpicfArpThrottleNotifications,
       "hpicfArpThrottleExceedThresholdTrap": hpicfArpThrottleExceedThresholdTrap,
       "hpicfArpThrottleObjects": hpicfArpThrottleObjects,
       "hpicfArpThrottleClientOverThreshold": hpicfArpThrottleClientOverThreshold,
       "hpicfArpThrottleConfig": hpicfArpThrottleConfig,
       "hpicfArpThrottleEnable": hpicfArpThrottleEnable,
       "hpicfArpThrottleRemediationMode": hpicfArpThrottleRemediationMode,
       "hpicfArpThrottleThreshold": hpicfArpThrottleThreshold,
       "hpicfArpThrottleBlacklistAgingTime": hpicfArpThrottleBlacklistAgingTime,
       "hpicfArpThrottleExcludedMacTable": hpicfArpThrottleExcludedMacTable,
       "hpicfArpThrottleExcludedMacEntry": hpicfArpThrottleExcludedMacEntry,
       "hpicfArpThrottleExcludedMac": hpicfArpThrottleExcludedMac,
       "hpicfArpThrottleExcludedMacStatus": hpicfArpThrottleExcludedMacStatus,
       "hpicfArpThrottleStats": hpicfArpThrottleStats,
       "hpicfArpThrottleStatsNumClientsInBlacklist": hpicfArpThrottleStatsNumClientsInBlacklist,
       "hpicfArpThrottleStatsNumClientsBeingTracked": hpicfArpThrottleStatsNumClientsBeingTracked,
       "hpicfArpThrottleConformance": hpicfArpThrottleConformance,
       "hpicfArpThrottleGroups": hpicfArpThrottleGroups,
       "hpicfArpThrottleBaseGroup": hpicfArpThrottleBaseGroup,
       "hpicfArpThrottleNotificationGroup": hpicfArpThrottleNotificationGroup,
       "hpicfArpThrottleCompliances": hpicfArpThrottleCompliances,
       "hpicfArpThrottleCompliance": hpicfArpThrottleCompliance}
)
