# SNMP MIB module (A3COM-HUAWEI-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:16 2024
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

(huaweiDatacomm,
 huaweiMgmt) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiDatacomm",
    "huaweiMgmt")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwLAG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLAGMibObjects_ObjectIdentity = ObjectIdentity
hwLAGMibObjects = _HwLAGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1)
)
_HwAggLinkTable_Object = MibTable
hwAggLinkTable = _HwAggLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1)
)
if mibBuilder.loadTexts:
    hwAggLinkTable.setStatus("current")
_HwAggLinkEntry_Object = MibTableRow
hwAggLinkEntry = _HwAggLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1)
)
hwAggLinkEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LAG-MIB", "hwAggLinkNumber"),
)
if mibBuilder.loadTexts:
    hwAggLinkEntry.setStatus("current")
_HwAggLinkNumber_Type = Integer32
_HwAggLinkNumber_Object = MibTableColumn
hwAggLinkNumber = _HwAggLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 1),
    _HwAggLinkNumber_Type()
)
hwAggLinkNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAggLinkNumber.setStatus("current")


class _HwAggLinkName_Type(DisplayString):
    """Custom type hwAggLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwAggLinkName_Type.__name__ = "DisplayString"
_HwAggLinkName_Object = MibTableColumn
hwAggLinkName = _HwAggLinkName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 2),
    _HwAggLinkName_Type()
)
hwAggLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAggLinkName.setStatus("current")


class _HwAggLinkMode_Type(Integer32):
    """Custom type hwAggLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("manual", 1),
          ("static", 2))
    )


_HwAggLinkMode_Type.__name__ = "Integer32"
_HwAggLinkMode_Object = MibTableColumn
hwAggLinkMode = _HwAggLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 3),
    _HwAggLinkMode_Type()
)
hwAggLinkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAggLinkMode.setStatus("current")
_HwAggLinkPortList_Type = PortList
_HwAggLinkPortList_Object = MibTableColumn
hwAggLinkPortList = _HwAggLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 4),
    _HwAggLinkPortList_Type()
)
hwAggLinkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAggLinkPortList.setStatus("current")
_HwAggLinkState_Type = RowStatus
_HwAggLinkState_Object = MibTableColumn
hwAggLinkState = _HwAggLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 5),
    _HwAggLinkState_Type()
)
hwAggLinkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAggLinkState.setStatus("current")
_HwAggPortListSelectedPorts_Type = PortList
_HwAggPortListSelectedPorts_Object = MibTableColumn
hwAggPortListSelectedPorts = _HwAggPortListSelectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 6),
    _HwAggPortListSelectedPorts_Type()
)
hwAggPortListSelectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAggPortListSelectedPorts.setStatus("current")
_HwAggPortListSamePartnerPorts_Type = PortList
_HwAggPortListSamePartnerPorts_Object = MibTableColumn
hwAggPortListSamePartnerPorts = _HwAggPortListSamePartnerPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 1, 1, 7),
    _HwAggPortListSamePartnerPorts_Type()
)
hwAggPortListSamePartnerPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAggPortListSamePartnerPorts.setStatus("current")
_HwAggPortTable_Object = MibTable
hwAggPortTable = _HwAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2)
)
if mibBuilder.loadTexts:
    hwAggPortTable.setStatus("current")
_HwAggPortEntry_Object = MibTableRow
hwAggPortEntry = _HwAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2, 1)
)
hwAggPortEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LAG-MIB", "hwAggPortIndex"),
)
if mibBuilder.loadTexts:
    hwAggPortEntry.setStatus("current")
_HwAggPortIndex_Type = Gauge32
_HwAggPortIndex_Object = MibTableColumn
hwAggPortIndex = _HwAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2, 1, 1),
    _HwAggPortIndex_Type()
)
hwAggPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAggPortIndex.setStatus("current")


class _HwAggPortNotAttachedReason_Type(Integer32):
    """Custom type hwAggPortNotAttachedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwAggPortNotAttachedReason_Type.__name__ = "Integer32"
_HwAggPortNotAttachedReason_Object = MibTableColumn
hwAggPortNotAttachedReason = _HwAggPortNotAttachedReason_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2, 1, 2),
    _HwAggPortNotAttachedReason_Type()
)
hwAggPortNotAttachedReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAggPortNotAttachedReason.setStatus("current")
_HwAggPortLacpState_Type = TruthValue
_HwAggPortLacpState_Object = MibTableColumn
hwAggPortLacpState = _HwAggPortLacpState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2, 1, 3),
    _HwAggPortLacpState_Type()
)
hwAggPortLacpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAggPortLacpState.setStatus("current")


class _HwAggPortNotAttachedString_Type(DisplayString):
    """Custom type hwAggPortNotAttachedString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwAggPortNotAttachedString_Type.__name__ = "DisplayString"
_HwAggPortNotAttachedString_Object = MibTableColumn
hwAggPortNotAttachedString = _HwAggPortNotAttachedString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 2, 1, 4),
    _HwAggPortNotAttachedString_Type()
)
hwAggPortNotAttachedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAggPortNotAttachedString.setStatus("current")


class _HwAggResourceAllocationValue_Type(PortList):
    """Custom type hwAggResourceAllocationValue based on PortList"""
    defaultValue = OctetString("0")


_HwAggResourceAllocationValue_Object = MibScalar
hwAggResourceAllocationValue = _HwAggResourceAllocationValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 1, 3),
    _HwAggResourceAllocationValue_Type()
)
hwAggResourceAllocationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAggResourceAllocationValue.setStatus("current")
_HwLAGMibNotifications_ObjectIdentity = ObjectIdentity
hwLAGMibNotifications = _HwLAGMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 2)
)
_HwLAGMibConformance_ObjectIdentity = ObjectIdentity
hwLAGMibConformance = _HwLAGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3)
)
_HwLAGMibCompliances_ObjectIdentity = ObjectIdentity
hwLAGMibCompliances = _HwLAGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3, 1)
)
_HwLAGMibGroup_ObjectIdentity = ObjectIdentity
hwLAGMibGroup = _HwLAGMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3, 2)
)

# Managed Objects groups

hwLAGMibObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3, 2, 1)
)
hwLAGMibObjectGroup.setObjects(
      *(("A3COM-HUAWEI-LAG-MIB", "hwAggLinkName"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggLinkMode"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggLinkPortList"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggLinkState"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortListSelectedPorts"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortListSamePartnerPorts"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortNotAttachedReason"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortLacpState"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortNotAttachedString"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggResourceAllocationValue"))
)
if mibBuilder.loadTexts:
    hwLAGMibObjectGroup.setStatus("current")


# Notification objects

hwAggSpeedChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 2, 1)
)
hwAggSpeedChangedNotification.setObjects(
    ("A3COM-HUAWEI-LAG-MIB", "hwAggLinkNumber")
)
if mibBuilder.loadTexts:
    hwAggSpeedChangedNotification.setStatus(
        "current"
    )

hwAggPortInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 2, 2)
)
hwAggPortInactiveNotification.setObjects(
    ("A3COM-HUAWEI-LAG-MIB", "hwAggLinkNumber")
)
if mibBuilder.loadTexts:
    hwAggPortInactiveNotification.setStatus(
        "current"
    )

hwAggPortInactiveNotification2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 2, 3)
)
hwAggPortInactiveNotification2.setObjects(
      *(("A3COM-HUAWEI-LAG-MIB", "hwAggLinkNumber"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortIndex"))
)
if mibBuilder.loadTexts:
    hwAggPortInactiveNotification2.setStatus(
        "current"
    )

hwAggPortActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 2, 4)
)
hwAggPortActiveNotification.setObjects(
      *(("A3COM-HUAWEI-LAG-MIB", "hwAggLinkNumber"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortIndex"))
)
if mibBuilder.loadTexts:
    hwAggPortActiveNotification.setStatus(
        "current"
    )


# Notifications groups

hwLAGMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3, 2, 2)
)
hwLAGMibNotificationGroup.setObjects(
      *(("A3COM-HUAWEI-LAG-MIB", "hwAggSpeedChangedNotification"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortInactiveNotification"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortInactiveNotification2"),
        ("A3COM-HUAWEI-LAG-MIB", "hwAggPortActiveNotification"))
)
if mibBuilder.loadTexts:
    hwLAGMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLAGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwLAGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LAG-MIB",
    **{"hwLAG": hwLAG,
       "hwLAGMibObjects": hwLAGMibObjects,
       "hwAggLinkTable": hwAggLinkTable,
       "hwAggLinkEntry": hwAggLinkEntry,
       "hwAggLinkNumber": hwAggLinkNumber,
       "hwAggLinkName": hwAggLinkName,
       "hwAggLinkMode": hwAggLinkMode,
       "hwAggLinkPortList": hwAggLinkPortList,
       "hwAggLinkState": hwAggLinkState,
       "hwAggPortListSelectedPorts": hwAggPortListSelectedPorts,
       "hwAggPortListSamePartnerPorts": hwAggPortListSamePartnerPorts,
       "hwAggPortTable": hwAggPortTable,
       "hwAggPortEntry": hwAggPortEntry,
       "hwAggPortIndex": hwAggPortIndex,
       "hwAggPortNotAttachedReason": hwAggPortNotAttachedReason,
       "hwAggPortLacpState": hwAggPortLacpState,
       "hwAggPortNotAttachedString": hwAggPortNotAttachedString,
       "hwAggResourceAllocationValue": hwAggResourceAllocationValue,
       "hwLAGMibNotifications": hwLAGMibNotifications,
       "hwAggSpeedChangedNotification": hwAggSpeedChangedNotification,
       "hwAggPortInactiveNotification": hwAggPortInactiveNotification,
       "hwAggPortInactiveNotification2": hwAggPortInactiveNotification2,
       "hwAggPortActiveNotification": hwAggPortActiveNotification,
       "hwLAGMibConformance": hwLAGMibConformance,
       "hwLAGMibCompliances": hwLAGMibCompliances,
       "hwLAGMibCompliance": hwLAGMibCompliance,
       "hwLAGMibGroup": hwLAGMibGroup,
       "hwLAGMibObjectGroup": hwLAGMibObjectGroup,
       "hwLAGMibNotificationGroup": hwLAGMibNotificationGroup}
)
