# SNMP MIB module (HH3C-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:45 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cLAG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLAGMibObjects_ObjectIdentity = ObjectIdentity
hh3cLAGMibObjects = _Hh3cLAGMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1)
)
_Hh3cAggLinkTable_Object = MibTable
hh3cAggLinkTable = _Hh3cAggLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cAggLinkTable.setStatus("current")
_Hh3cAggLinkEntry_Object = MibTableRow
hh3cAggLinkEntry = _Hh3cAggLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1)
)
hh3cAggLinkEntry.setIndexNames(
    (0, "HH3C-LAG-MIB", "hh3cAggLinkNumber"),
)
if mibBuilder.loadTexts:
    hh3cAggLinkEntry.setStatus("current")
_Hh3cAggLinkNumber_Type = Integer32
_Hh3cAggLinkNumber_Object = MibTableColumn
hh3cAggLinkNumber = _Hh3cAggLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 1),
    _Hh3cAggLinkNumber_Type()
)
hh3cAggLinkNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAggLinkNumber.setStatus("current")


class _Hh3cAggLinkName_Type(DisplayString):
    """Custom type hh3cAggLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAggLinkName_Type.__name__ = "DisplayString"
_Hh3cAggLinkName_Object = MibTableColumn
hh3cAggLinkName = _Hh3cAggLinkName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 2),
    _Hh3cAggLinkName_Type()
)
hh3cAggLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAggLinkName.setStatus("current")


class _Hh3cAggLinkMode_Type(Integer32):
    """Custom type hh3cAggLinkMode based on Integer32"""
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


_Hh3cAggLinkMode_Type.__name__ = "Integer32"
_Hh3cAggLinkMode_Object = MibTableColumn
hh3cAggLinkMode = _Hh3cAggLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 3),
    _Hh3cAggLinkMode_Type()
)
hh3cAggLinkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAggLinkMode.setStatus("current")
_Hh3cAggLinkPortList_Type = PortList
_Hh3cAggLinkPortList_Object = MibTableColumn
hh3cAggLinkPortList = _Hh3cAggLinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 4),
    _Hh3cAggLinkPortList_Type()
)
hh3cAggLinkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAggLinkPortList.setStatus("current")
_Hh3cAggLinkState_Type = RowStatus
_Hh3cAggLinkState_Object = MibTableColumn
hh3cAggLinkState = _Hh3cAggLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 5),
    _Hh3cAggLinkState_Type()
)
hh3cAggLinkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAggLinkState.setStatus("current")
_Hh3cAggPortListSelectedPorts_Type = PortList
_Hh3cAggPortListSelectedPorts_Object = MibTableColumn
hh3cAggPortListSelectedPorts = _Hh3cAggPortListSelectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 6),
    _Hh3cAggPortListSelectedPorts_Type()
)
hh3cAggPortListSelectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAggPortListSelectedPorts.setStatus("current")
_Hh3cAggPortListSamePartnerPorts_Type = PortList
_Hh3cAggPortListSamePartnerPorts_Object = MibTableColumn
hh3cAggPortListSamePartnerPorts = _Hh3cAggPortListSamePartnerPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 1, 1, 7),
    _Hh3cAggPortListSamePartnerPorts_Type()
)
hh3cAggPortListSamePartnerPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAggPortListSamePartnerPorts.setStatus("current")
_Hh3cAggPortTable_Object = MibTable
hh3cAggPortTable = _Hh3cAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cAggPortTable.setStatus("current")
_Hh3cAggPortEntry_Object = MibTableRow
hh3cAggPortEntry = _Hh3cAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2, 1)
)
hh3cAggPortEntry.setIndexNames(
    (0, "HH3C-LAG-MIB", "hh3cAggPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cAggPortEntry.setStatus("current")
_Hh3cAggPortIndex_Type = Gauge32
_Hh3cAggPortIndex_Object = MibTableColumn
hh3cAggPortIndex = _Hh3cAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2, 1, 1),
    _Hh3cAggPortIndex_Type()
)
hh3cAggPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAggPortIndex.setStatus("current")


class _Hh3cAggPortNotAttachedReason_Type(Integer32):
    """Custom type hh3cAggPortNotAttachedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cAggPortNotAttachedReason_Type.__name__ = "Integer32"
_Hh3cAggPortNotAttachedReason_Object = MibTableColumn
hh3cAggPortNotAttachedReason = _Hh3cAggPortNotAttachedReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2, 1, 2),
    _Hh3cAggPortNotAttachedReason_Type()
)
hh3cAggPortNotAttachedReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAggPortNotAttachedReason.setStatus("current")
_Hh3cAggPortLacpState_Type = TruthValue
_Hh3cAggPortLacpState_Object = MibTableColumn
hh3cAggPortLacpState = _Hh3cAggPortLacpState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2, 1, 3),
    _Hh3cAggPortLacpState_Type()
)
hh3cAggPortLacpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAggPortLacpState.setStatus("current")


class _Hh3cAggPortNotAttachedString_Type(DisplayString):
    """Custom type hh3cAggPortNotAttachedString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAggPortNotAttachedString_Type.__name__ = "DisplayString"
_Hh3cAggPortNotAttachedString_Object = MibTableColumn
hh3cAggPortNotAttachedString = _Hh3cAggPortNotAttachedString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 2, 1, 4),
    _Hh3cAggPortNotAttachedString_Type()
)
hh3cAggPortNotAttachedString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAggPortNotAttachedString.setStatus("current")


class _Hh3cAggResourceAllocationValue_Type(PortList):
    """Custom type hh3cAggResourceAllocationValue based on PortList"""
    defaultValue = OctetString("0")


_Hh3cAggResourceAllocationValue_Object = MibScalar
hh3cAggResourceAllocationValue = _Hh3cAggResourceAllocationValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 1, 3),
    _Hh3cAggResourceAllocationValue_Type()
)
hh3cAggResourceAllocationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAggResourceAllocationValue.setStatus("current")
_Hh3cLAGMibNotifications_ObjectIdentity = ObjectIdentity
hh3cLAGMibNotifications = _Hh3cLAGMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 2)
)
_Hh3cLAGMibConformance_ObjectIdentity = ObjectIdentity
hh3cLAGMibConformance = _Hh3cLAGMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3)
)
_Hh3cLAGMibCompliances_ObjectIdentity = ObjectIdentity
hh3cLAGMibCompliances = _Hh3cLAGMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3, 1)
)
_Hh3cLAGMibGroup_ObjectIdentity = ObjectIdentity
hh3cLAGMibGroup = _Hh3cLAGMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3, 2)
)

# Managed Objects groups

hh3cLAGMibObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3, 2, 1)
)
hh3cLAGMibObjectGroup.setObjects(
      *(("HH3C-LAG-MIB", "hh3cAggLinkName"),
        ("HH3C-LAG-MIB", "hh3cAggLinkMode"),
        ("HH3C-LAG-MIB", "hh3cAggLinkPortList"),
        ("HH3C-LAG-MIB", "hh3cAggLinkState"),
        ("HH3C-LAG-MIB", "hh3cAggPortListSelectedPorts"),
        ("HH3C-LAG-MIB", "hh3cAggPortListSamePartnerPorts"),
        ("HH3C-LAG-MIB", "hh3cAggPortNotAttachedReason"),
        ("HH3C-LAG-MIB", "hh3cAggPortLacpState"),
        ("HH3C-LAG-MIB", "hh3cAggPortNotAttachedString"),
        ("HH3C-LAG-MIB", "hh3cAggResourceAllocationValue"))
)
if mibBuilder.loadTexts:
    hh3cLAGMibObjectGroup.setStatus("current")


# Notification objects

hh3cAggSpeedChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 2, 1)
)
hh3cAggSpeedChangedNotification.setObjects(
    ("HH3C-LAG-MIB", "hh3cAggLinkNumber")
)
if mibBuilder.loadTexts:
    hh3cAggSpeedChangedNotification.setStatus(
        "current"
    )

hh3cAggPortInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 2, 2)
)
hh3cAggPortInactiveNotification.setObjects(
    ("HH3C-LAG-MIB", "hh3cAggLinkNumber")
)
if mibBuilder.loadTexts:
    hh3cAggPortInactiveNotification.setStatus(
        "current"
    )

hh3cAggPortInactiveNotification2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 2, 3)
)
hh3cAggPortInactiveNotification2.setObjects(
      *(("HH3C-LAG-MIB", "hh3cAggLinkNumber"),
        ("HH3C-LAG-MIB", "hh3cAggPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cAggPortInactiveNotification2.setStatus(
        "current"
    )

hh3cAggPortActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 2, 4)
)
hh3cAggPortActiveNotification.setObjects(
      *(("HH3C-LAG-MIB", "hh3cAggLinkNumber"),
        ("HH3C-LAG-MIB", "hh3cAggPortIndex"))
)
if mibBuilder.loadTexts:
    hh3cAggPortActiveNotification.setStatus(
        "current"
    )


# Notifications groups

hh3cLAGMibNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3, 2, 2)
)
hh3cLAGMibNotificationGroup.setObjects(
      *(("HH3C-LAG-MIB", "hh3cAggSpeedChangedNotification"),
        ("HH3C-LAG-MIB", "hh3cAggPortInactiveNotification"),
        ("HH3C-LAG-MIB", "hh3cAggPortInactiveNotification2"),
        ("HH3C-LAG-MIB", "hh3cAggPortActiveNotification"))
)
if mibBuilder.loadTexts:
    hh3cLAGMibNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cLAGMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 8, 25, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLAGMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LAG-MIB",
    **{"hh3cLAG": hh3cLAG,
       "hh3cLAGMibObjects": hh3cLAGMibObjects,
       "hh3cAggLinkTable": hh3cAggLinkTable,
       "hh3cAggLinkEntry": hh3cAggLinkEntry,
       "hh3cAggLinkNumber": hh3cAggLinkNumber,
       "hh3cAggLinkName": hh3cAggLinkName,
       "hh3cAggLinkMode": hh3cAggLinkMode,
       "hh3cAggLinkPortList": hh3cAggLinkPortList,
       "hh3cAggLinkState": hh3cAggLinkState,
       "hh3cAggPortListSelectedPorts": hh3cAggPortListSelectedPorts,
       "hh3cAggPortListSamePartnerPorts": hh3cAggPortListSamePartnerPorts,
       "hh3cAggPortTable": hh3cAggPortTable,
       "hh3cAggPortEntry": hh3cAggPortEntry,
       "hh3cAggPortIndex": hh3cAggPortIndex,
       "hh3cAggPortNotAttachedReason": hh3cAggPortNotAttachedReason,
       "hh3cAggPortLacpState": hh3cAggPortLacpState,
       "hh3cAggPortNotAttachedString": hh3cAggPortNotAttachedString,
       "hh3cAggResourceAllocationValue": hh3cAggResourceAllocationValue,
       "hh3cLAGMibNotifications": hh3cLAGMibNotifications,
       "hh3cAggSpeedChangedNotification": hh3cAggSpeedChangedNotification,
       "hh3cAggPortInactiveNotification": hh3cAggPortInactiveNotification,
       "hh3cAggPortInactiveNotification2": hh3cAggPortInactiveNotification2,
       "hh3cAggPortActiveNotification": hh3cAggPortActiveNotification,
       "hh3cLAGMibConformance": hh3cLAGMibConformance,
       "hh3cLAGMibCompliances": hh3cLAGMibCompliances,
       "hh3cLAGMibCompliance": hh3cLAGMibCompliance,
       "hh3cLAGMibGroup": hh3cLAGMibGroup,
       "hh3cLAGMibObjectGroup": hh3cLAGMibObjectGroup,
       "hh3cLAGMibNotificationGroup": hh3cLAGMibNotificationGroup}
)
