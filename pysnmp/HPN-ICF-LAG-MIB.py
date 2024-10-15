# SNMP MIB module (HPN-ICF-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:44 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfLAG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLAGMibObjects_ObjectIdentity = ObjectIdentity
hpnicfLAGMibObjects = _HpnicfLAGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1)
)
_HpnicfAggLinkTable_Object = MibTable
hpnicfAggLinkTable = _HpnicfAggLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfAggLinkTable.setStatus("current")
_HpnicfAggLinkEntry_Object = MibTableRow
hpnicfAggLinkEntry = _HpnicfAggLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1)
)
hpnicfAggLinkEntry.setIndexNames(
    (0, "HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"),
)
if mibBuilder.loadTexts:
    hpnicfAggLinkEntry.setStatus("current")
_HpnicfAggLinkNumber_Type = Integer32
_HpnicfAggLinkNumber_Object = MibTableColumn
hpnicfAggLinkNumber = _HpnicfAggLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 1),
    _HpnicfAggLinkNumber_Type()
)
hpnicfAggLinkNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAggLinkNumber.setStatus("current")


class _HpnicfAggLinkName_Type(DisplayString):
    """Custom type hpnicfAggLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnicfAggLinkName_Type.__name__ = "DisplayString"
_HpnicfAggLinkName_Object = MibTableColumn
hpnicfAggLinkName = _HpnicfAggLinkName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 2),
    _HpnicfAggLinkName_Type()
)
hpnicfAggLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAggLinkName.setStatus("current")


class _HpnicfAggLinkMode_Type(Integer32):
    """Custom type hpnicfAggLinkMode based on Integer32"""
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


_HpnicfAggLinkMode_Type.__name__ = "Integer32"
_HpnicfAggLinkMode_Object = MibTableColumn
hpnicfAggLinkMode = _HpnicfAggLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 3),
    _HpnicfAggLinkMode_Type()
)
hpnicfAggLinkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAggLinkMode.setStatus("current")
_HpnicfAggLinkPortList_Type = PortList
_HpnicfAggLinkPortList_Object = MibTableColumn
hpnicfAggLinkPortList = _HpnicfAggLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 4),
    _HpnicfAggLinkPortList_Type()
)
hpnicfAggLinkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAggLinkPortList.setStatus("current")
_HpnicfAggLinkState_Type = RowStatus
_HpnicfAggLinkState_Object = MibTableColumn
hpnicfAggLinkState = _HpnicfAggLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 5),
    _HpnicfAggLinkState_Type()
)
hpnicfAggLinkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAggLinkState.setStatus("current")
_HpnicfAggPortListSelectedPorts_Type = PortList
_HpnicfAggPortListSelectedPorts_Object = MibTableColumn
hpnicfAggPortListSelectedPorts = _HpnicfAggPortListSelectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 6),
    _HpnicfAggPortListSelectedPorts_Type()
)
hpnicfAggPortListSelectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAggPortListSelectedPorts.setStatus("current")
_HpnicfAggPortListSamePartnerPorts_Type = PortList
_HpnicfAggPortListSamePartnerPorts_Object = MibTableColumn
hpnicfAggPortListSamePartnerPorts = _HpnicfAggPortListSamePartnerPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 1, 1, 7),
    _HpnicfAggPortListSamePartnerPorts_Type()
)
hpnicfAggPortListSamePartnerPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAggPortListSamePartnerPorts.setStatus("current")
_HpnicfAggPortTable_Object = MibTable
hpnicfAggPortTable = _HpnicfAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfAggPortTable.setStatus("current")
_HpnicfAggPortEntry_Object = MibTableRow
hpnicfAggPortEntry = _HpnicfAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1)
)
hpnicfAggPortEntry.setIndexNames(
    (0, "HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfAggPortEntry.setStatus("current")
_HpnicfAggPortIndex_Type = Gauge32
_HpnicfAggPortIndex_Object = MibTableColumn
hpnicfAggPortIndex = _HpnicfAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 1),
    _HpnicfAggPortIndex_Type()
)
hpnicfAggPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfAggPortIndex.setStatus("current")


class _HpnicfAggPortNotAttachedReason_Type(Integer32):
    """Custom type hpnicfAggPortNotAttachedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnicfAggPortNotAttachedReason_Type.__name__ = "Integer32"
_HpnicfAggPortNotAttachedReason_Object = MibTableColumn
hpnicfAggPortNotAttachedReason = _HpnicfAggPortNotAttachedReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 2),
    _HpnicfAggPortNotAttachedReason_Type()
)
hpnicfAggPortNotAttachedReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAggPortNotAttachedReason.setStatus("current")
_HpnicfAggPortLacpState_Type = TruthValue
_HpnicfAggPortLacpState_Object = MibTableColumn
hpnicfAggPortLacpState = _HpnicfAggPortLacpState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 3),
    _HpnicfAggPortLacpState_Type()
)
hpnicfAggPortLacpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAggPortLacpState.setStatus("current")


class _HpnicfAggPortNotAttachedString_Type(DisplayString):
    """Custom type hpnicfAggPortNotAttachedString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfAggPortNotAttachedString_Type.__name__ = "DisplayString"
_HpnicfAggPortNotAttachedString_Object = MibTableColumn
hpnicfAggPortNotAttachedString = _HpnicfAggPortNotAttachedString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 2, 1, 4),
    _HpnicfAggPortNotAttachedString_Type()
)
hpnicfAggPortNotAttachedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfAggPortNotAttachedString.setStatus("current")


class _HpnicfAggResourceAllocationValue_Type(PortList):
    """Custom type hpnicfAggResourceAllocationValue based on PortList"""
    defaultValue = OctetString("0")


_HpnicfAggResourceAllocationValue_Object = MibScalar
hpnicfAggResourceAllocationValue = _HpnicfAggResourceAllocationValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 1, 3),
    _HpnicfAggResourceAllocationValue_Type()
)
hpnicfAggResourceAllocationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAggResourceAllocationValue.setStatus("current")
_HpnicfLAGMibNotifications_ObjectIdentity = ObjectIdentity
hpnicfLAGMibNotifications = _HpnicfLAGMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2)
)
_HpnicfLAGMibConformance_ObjectIdentity = ObjectIdentity
hpnicfLAGMibConformance = _HpnicfLAGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3)
)
_HpnicfLAGMibCompliances_ObjectIdentity = ObjectIdentity
hpnicfLAGMibCompliances = _HpnicfLAGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 1)
)
_HpnicfLAGMibGroup_ObjectIdentity = ObjectIdentity
hpnicfLAGMibGroup = _HpnicfLAGMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2)
)

# Managed Objects groups

hpnicfLAGMibObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2, 1)
)
hpnicfLAGMibObjectGroup.setObjects(
      *(("HPN-ICF-LAG-MIB", "hpnicfAggLinkName"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggLinkMode"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggLinkPortList"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggLinkState"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortListSelectedPorts"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortListSamePartnerPorts"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortNotAttachedReason"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortLacpState"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortNotAttachedString"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggResourceAllocationValue"))
)
if mibBuilder.loadTexts:
    hpnicfLAGMibObjectGroup.setStatus("current")


# Notification objects

hpnicfAggSpeedChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 1)
)
hpnicfAggSpeedChangedNotification.setObjects(
    ("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber")
)
if mibBuilder.loadTexts:
    hpnicfAggSpeedChangedNotification.setStatus(
        "current"
    )

hpnicfAggPortInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 2)
)
hpnicfAggPortInactiveNotification.setObjects(
    ("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber")
)
if mibBuilder.loadTexts:
    hpnicfAggPortInactiveNotification.setStatus(
        "current"
    )

hpnicfAggPortInactiveNotification2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 3)
)
hpnicfAggPortInactiveNotification2.setObjects(
      *(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfAggPortInactiveNotification2.setStatus(
        "current"
    )

hpnicfAggPortActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 2, 4)
)
hpnicfAggPortActiveNotification.setObjects(
      *(("HPN-ICF-LAG-MIB", "hpnicfAggLinkNumber"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortIndex"))
)
if mibBuilder.loadTexts:
    hpnicfAggPortActiveNotification.setStatus(
        "current"
    )


# Notifications groups

hpnicfLAGMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 2, 2)
)
hpnicfLAGMibNotificationGroup.setObjects(
      *(("HPN-ICF-LAG-MIB", "hpnicfAggSpeedChangedNotification"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortInactiveNotification"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortInactiveNotification2"),
        ("HPN-ICF-LAG-MIB", "hpnicfAggPortActiveNotification"))
)
if mibBuilder.loadTexts:
    hpnicfLAGMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfLAGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfLAGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LAG-MIB",
    **{"hpnicfLAG": hpnicfLAG,
       "hpnicfLAGMibObjects": hpnicfLAGMibObjects,
       "hpnicfAggLinkTable": hpnicfAggLinkTable,
       "hpnicfAggLinkEntry": hpnicfAggLinkEntry,
       "hpnicfAggLinkNumber": hpnicfAggLinkNumber,
       "hpnicfAggLinkName": hpnicfAggLinkName,
       "hpnicfAggLinkMode": hpnicfAggLinkMode,
       "hpnicfAggLinkPortList": hpnicfAggLinkPortList,
       "hpnicfAggLinkState": hpnicfAggLinkState,
       "hpnicfAggPortListSelectedPorts": hpnicfAggPortListSelectedPorts,
       "hpnicfAggPortListSamePartnerPorts": hpnicfAggPortListSamePartnerPorts,
       "hpnicfAggPortTable": hpnicfAggPortTable,
       "hpnicfAggPortEntry": hpnicfAggPortEntry,
       "hpnicfAggPortIndex": hpnicfAggPortIndex,
       "hpnicfAggPortNotAttachedReason": hpnicfAggPortNotAttachedReason,
       "hpnicfAggPortLacpState": hpnicfAggPortLacpState,
       "hpnicfAggPortNotAttachedString": hpnicfAggPortNotAttachedString,
       "hpnicfAggResourceAllocationValue": hpnicfAggResourceAllocationValue,
       "hpnicfLAGMibNotifications": hpnicfLAGMibNotifications,
       "hpnicfAggSpeedChangedNotification": hpnicfAggSpeedChangedNotification,
       "hpnicfAggPortInactiveNotification": hpnicfAggPortInactiveNotification,
       "hpnicfAggPortInactiveNotification2": hpnicfAggPortInactiveNotification2,
       "hpnicfAggPortActiveNotification": hpnicfAggPortActiveNotification,
       "hpnicfLAGMibConformance": hpnicfLAGMibConformance,
       "hpnicfLAGMibCompliances": hpnicfLAGMibCompliances,
       "hpnicfLAGMibCompliance": hpnicfLAGMibCompliance,
       "hpnicfLAGMibGroup": hpnicfLAGMibGroup,
       "hpnicfLAGMibObjectGroup": hpnicfLAGMibObjectGroup,
       "hpnicfLAGMibNotificationGroup": hpnicfLAGMibNotificationGroup}
)
