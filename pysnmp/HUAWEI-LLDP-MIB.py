# SNMP MIB module (HUAWEI-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:34 2024
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

(lldpLocSysCapEnabled,
 lldpLocSysCapSupported,
 lldpPortConfigPortNum) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "lldpLocSysCapEnabled",
    "lldpLocSysCapSupported",
    "lldpPortConfigPortNum")

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

hwLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwLldpObjects_ObjectIdentity = ObjectIdentity
hwLldpObjects = _HwLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1)
)
_HwLldpConfiguration_ObjectIdentity = ObjectIdentity
hwLldpConfiguration = _HwLldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1)
)


class _HwLldpEnable_Type(EnabledStatus):
    """Custom type hwLldpEnable based on EnabledStatus"""
    defaultValue = 2


_HwLldpEnable_Object = MibScalar
hwLldpEnable = _HwLldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 1),
    _HwLldpEnable_Type()
)
hwLldpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLldpEnable.setStatus("current")
_HwLldpLocManIPAddr_Type = IpAddress
_HwLldpLocManIPAddr_Object = MibScalar
hwLldpLocManIPAddr = _HwLldpLocManIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 2),
    _HwLldpLocManIPAddr_Type()
)
hwLldpLocManIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLldpLocManIPAddr.setStatus("current")
_HwLldpCounterReset_Type = EnabledStatus
_HwLldpCounterReset_Object = MibScalar
hwLldpCounterReset = _HwLldpCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 3),
    _HwLldpCounterReset_Type()
)
hwLldpCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLldpCounterReset.setStatus("current")


class _HwLldpNotificationEnable_Type(EnabledStatus):
    """Custom type hwLldpNotificationEnable based on EnabledStatus"""
    defaultValue = 2


_HwLldpNotificationEnable_Object = MibScalar
hwLldpNotificationEnable = _HwLldpNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 4),
    _HwLldpNotificationEnable_Type()
)
hwLldpNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLldpNotificationEnable.setStatus("current")
_HwLldpPortConfigTable_Object = MibTable
hwLldpPortConfigTable = _HwLldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwLldpPortConfigTable.setStatus("current")
_HwLldpPortConfigEntry_Object = MibTableRow
hwLldpPortConfigEntry = _HwLldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1)
)
hwLldpPortConfigEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    hwLldpPortConfigEntry.setStatus("current")
_HwLldpPortConfigIfIndex_Type = InterfaceIndex
_HwLldpPortConfigIfIndex_Object = MibTableColumn
hwLldpPortConfigIfIndex = _HwLldpPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 11),
    _HwLldpPortConfigIfIndex_Type()
)
hwLldpPortConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLldpPortConfigIfIndex.setStatus("current")
_HwLldpPortConfigCounterReset_Type = EnabledStatus
_HwLldpPortConfigCounterReset_Object = MibTableColumn
hwLldpPortConfigCounterReset = _HwLldpPortConfigCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 1, 5, 1, 12),
    _HwLldpPortConfigCounterReset_Type()
)
hwLldpPortConfigCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLldpPortConfigCounterReset.setStatus("current")
_HwLldpRemoteSystemData_ObjectIdentity = ObjectIdentity
hwLldpRemoteSystemData = _HwLldpRemoteSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2)
)
_HwLldpRemProtoTypeTable_Object = MibTable
hwLldpRemProtoTypeTable = _HwLldpRemProtoTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwLldpRemProtoTypeTable.setStatus("current")
_HwLldpRemProtoTypeEntry_Object = MibTableRow
hwLldpRemProtoTypeEntry = _HwLldpRemProtoTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1)
)
hwLldpRemProtoTypeEntry.setIndexNames(
    (0, "LLDP-MIB", "lldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    hwLldpRemProtoTypeEntry.setStatus("current")


class _HwLldpRemProtoType_Type(Integer32):
    """Custom type hwLldpRemProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cdp", 2),
          ("lldp", 1),
          ("unknown", 255))
    )


_HwLldpRemProtoType_Type.__name__ = "Integer32"
_HwLldpRemProtoType_Object = MibTableColumn
hwLldpRemProtoType = _HwLldpRemProtoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 1, 2, 1, 1, 1),
    _HwLldpRemProtoType_Type()
)
hwLldpRemProtoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLldpRemProtoType.setStatus("current")
_HwLldpTraps_ObjectIdentity = ObjectIdentity
hwLldpTraps = _HwLldpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2)
)
_HwLldpConformance_ObjectIdentity = ObjectIdentity
hwLldpConformance = _HwLldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3)
)
_HwLldpCompliances_ObjectIdentity = ObjectIdentity
hwLldpCompliances = _HwLldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1)
)
_HwLldpGroups_ObjectIdentity = ObjectIdentity
hwLldpGroups = _HwLldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2)
)

# Managed Objects groups

hwLldpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 1)
)
hwLldpConfigGroup.setObjects(
      *(("HUAWEI-LLDP-MIB", "hwLldpEnable"),
        ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr"),
        ("HUAWEI-LLDP-MIB", "hwLldpNotificationEnable"))
)
if mibBuilder.loadTexts:
    hwLldpConfigGroup.setStatus("current")

hwLldpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 2)
)
hwLldpStatsGroup.setObjects(
      *(("HUAWEI-LLDP-MIB", "hwLldpCounterReset"),
        ("HUAWEI-LLDP-MIB", "hwLldpPortConfigCounterReset"))
)
if mibBuilder.loadTexts:
    hwLldpStatsGroup.setStatus("current")

hwLldpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 3)
)
hwLldpPortGroup.setObjects(
      *(("HUAWEI-LLDP-MIB", "hwLldpPortConfigIfIndex"),
        ("HUAWEI-LLDP-MIB", "hwLldpRemProtoType"))
)
if mibBuilder.loadTexts:
    hwLldpPortGroup.setStatus("current")


# Notification objects

hwLldpEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 1)
)
if mibBuilder.loadTexts:
    hwLldpEnabled.setStatus(
        "current"
    )

hwLldpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 2)
)
if mibBuilder.loadTexts:
    hwLldpDisabled.setStatus(
        "current"
    )

hwLldpLocSysCapSupportedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 3)
)
hwLldpLocSysCapSupportedChange.setObjects(
    ("LLDP-MIB", "lldpLocSysCapSupported")
)
if mibBuilder.loadTexts:
    hwLldpLocSysCapSupportedChange.setStatus(
        "current"
    )

hwLldpLocSysCapEnabledChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 4)
)
hwLldpLocSysCapEnabledChange.setObjects(
    ("LLDP-MIB", "lldpLocSysCapEnabled")
)
if mibBuilder.loadTexts:
    hwLldpLocSysCapEnabledChange.setStatus(
        "current"
    )

hwLldpLocManIPAddrChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 2, 5)
)
hwLldpLocManIPAddrChange.setObjects(
    ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddr")
)
if mibBuilder.loadTexts:
    hwLldpLocManIPAddrChange.setStatus(
        "current"
    )


# Notifications groups

hwLldpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 2, 4)
)
hwLldpTrapGroup.setObjects(
      *(("HUAWEI-LLDP-MIB", "hwLldpEnabled"),
        ("HUAWEI-LLDP-MIB", "hwLldpDisabled"),
        ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapSupportedChange"),
        ("HUAWEI-LLDP-MIB", "hwLldpLocSysCapEnabledChange"),
        ("HUAWEI-LLDP-MIB", "hwLldpLocManIPAddrChange"))
)
if mibBuilder.loadTexts:
    hwLldpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 134, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LLDP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwLldpMIB": hwLldpMIB,
       "hwLldpObjects": hwLldpObjects,
       "hwLldpConfiguration": hwLldpConfiguration,
       "hwLldpEnable": hwLldpEnable,
       "hwLldpLocManIPAddr": hwLldpLocManIPAddr,
       "hwLldpCounterReset": hwLldpCounterReset,
       "hwLldpNotificationEnable": hwLldpNotificationEnable,
       "hwLldpPortConfigTable": hwLldpPortConfigTable,
       "hwLldpPortConfigEntry": hwLldpPortConfigEntry,
       "hwLldpPortConfigIfIndex": hwLldpPortConfigIfIndex,
       "hwLldpPortConfigCounterReset": hwLldpPortConfigCounterReset,
       "hwLldpRemoteSystemData": hwLldpRemoteSystemData,
       "hwLldpRemProtoTypeTable": hwLldpRemProtoTypeTable,
       "hwLldpRemProtoTypeEntry": hwLldpRemProtoTypeEntry,
       "hwLldpRemProtoType": hwLldpRemProtoType,
       "hwLldpTraps": hwLldpTraps,
       "hwLldpEnabled": hwLldpEnabled,
       "hwLldpDisabled": hwLldpDisabled,
       "hwLldpLocSysCapSupportedChange": hwLldpLocSysCapSupportedChange,
       "hwLldpLocSysCapEnabledChange": hwLldpLocSysCapEnabledChange,
       "hwLldpLocManIPAddrChange": hwLldpLocManIPAddrChange,
       "hwLldpConformance": hwLldpConformance,
       "hwLldpCompliances": hwLldpCompliances,
       "lldpCompliance": lldpCompliance,
       "hwLldpGroups": hwLldpGroups,
       "hwLldpConfigGroup": hwLldpConfigGroup,
       "hwLldpStatsGroup": hwLldpStatsGroup,
       "hwLldpPortGroup": hwLldpPortGroup,
       "hwLldpTrapGroup": hwLldpTrapGroup}
)
