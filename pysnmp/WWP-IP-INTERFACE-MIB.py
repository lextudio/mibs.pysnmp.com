# SNMP MIB module (WWP-IP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-IP-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:42 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpIpInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17)
)
wwpIpInterfaceMIB.setRevisions(
        ("2003-05-02 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpIpInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBObjects = _WwpIpInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1)
)
_WwpIpInterface_ObjectIdentity = ObjectIdentity
wwpIpInterface = _WwpIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1)
)
_WwpIpInterfaceTable_Object = MibTable
wwpIpInterfaceTable = _WwpIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpIpInterfaceTable.setStatus("current")
_WwpIpInterfaceEntry_Object = MibTableRow
wwpIpInterfaceEntry = _WwpIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1)
)
wwpIpInterfaceEntry.setIndexNames(
    (0, "WWP-IP-INTERFACE-MIB", "wwpIpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wwpIpInterfaceEntry.setStatus("current")


class _WwpIpInterfaceIndex_Type(Integer32):
    """Custom type wwpIpInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpIpInterfaceIndex_Type.__name__ = "Integer32"
_WwpIpInterfaceIndex_Object = MibTableColumn
wwpIpInterfaceIndex = _WwpIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1, 1),
    _WwpIpInterfaceIndex_Type()
)
wwpIpInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIpInterfaceIndex.setStatus("current")


class _WwpIpInterfaceName_Type(DisplayString):
    """Custom type wwpIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpIpInterfaceName_Type.__name__ = "DisplayString"
_WwpIpInterfaceName_Object = MibTableColumn
wwpIpInterfaceName = _WwpIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1, 2),
    _WwpIpInterfaceName_Type()
)
wwpIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIpInterfaceName.setStatus("current")
_WwpIpInterfaceIpAddr_Type = IpAddress
_WwpIpInterfaceIpAddr_Object = MibTableColumn
wwpIpInterfaceIpAddr = _WwpIpInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1, 3),
    _WwpIpInterfaceIpAddr_Type()
)
wwpIpInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceIpAddr.setStatus("current")
_WwpIpInterfaceSubnet_Type = IpAddress
_WwpIpInterfaceSubnet_Object = MibTableColumn
wwpIpInterfaceSubnet = _WwpIpInterfaceSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1, 4),
    _WwpIpInterfaceSubnet_Type()
)
wwpIpInterfaceSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceSubnet.setStatus("current")


class _WwpIpInterfaceIfIndexXref_Type(Integer32):
    """Custom type wwpIpInterfaceIfIndexXref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpIpInterfaceIfIndexXref_Type.__name__ = "Integer32"
_WwpIpInterfaceIfIndexXref_Object = MibTableColumn
wwpIpInterfaceIfIndexXref = _WwpIpInterfaceIfIndexXref_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 1, 1, 5),
    _WwpIpInterfaceIfIndexXref_Type()
)
wwpIpInterfaceIfIndexXref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIpInterfaceIfIndexXref.setStatus("current")
_WwpIpExtInterfaceTable_Object = MibTable
wwpIpExtInterfaceTable = _WwpIpExtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpIpExtInterfaceTable.setStatus("current")
_WwpIpExtInterfaceEntry_Object = MibTableRow
wwpIpExtInterfaceEntry = _WwpIpExtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpIpExtInterfaceEntry.setStatus("current")
_WwpIpInterfaceEnable_Type = TruthValue
_WwpIpInterfaceEnable_Object = MibTableColumn
wwpIpInterfaceEnable = _WwpIpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 2, 1, 1),
    _WwpIpInterfaceEnable_Type()
)
wwpIpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceEnable.setStatus("current")
_WwpIpInterfaceVlanId_Type = VlanId
_WwpIpInterfaceVlanId_Object = MibTableColumn
wwpIpInterfaceVlanId = _WwpIpInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 2, 1, 2),
    _WwpIpInterfaceVlanId_Type()
)
wwpIpInterfaceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceVlanId.setStatus("current")


class _WwpIpInterfaceMgmtPktPriority_Type(Integer32):
    """Custom type wwpIpInterfaceMgmtPktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpIpInterfaceMgmtPktPriority_Type.__name__ = "Integer32"
_WwpIpInterfaceMgmtPktPriority_Object = MibTableColumn
wwpIpInterfaceMgmtPktPriority = _WwpIpInterfaceMgmtPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 2, 1, 3),
    _WwpIpInterfaceMgmtPktPriority_Type()
)
wwpIpInterfaceMgmtPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceMgmtPktPriority.setStatus("current")


class _WwpIpInterfaceAddrNotifEnabled_Type(TruthValue):
    """Custom type wwpIpInterfaceAddrNotifEnabled based on TruthValue"""


_WwpIpInterfaceAddrNotifEnabled_Object = MibScalar
wwpIpInterfaceAddrNotifEnabled = _WwpIpInterfaceAddrNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 1, 1, 3),
    _WwpIpInterfaceAddrNotifEnabled_Type()
)
wwpIpInterfaceAddrNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIpInterfaceAddrNotifEnabled.setStatus("current")
_WwpIpInterfaceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBNotificationPrefix = _WwpIpInterfaceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 2)
)
_WwpIpInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBNotifications = _WwpIpInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 2, 0)
)
_WwpIpInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBConformance = _WwpIpInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 3)
)
_WwpIpInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBCompliances = _WwpIpInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 3, 1)
)
_WwpIpInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
wwpIpInterfaceMIBGroups = _WwpIpInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 3, 2)
)
wwpIpInterfaceEntry.registerAugmentions(
    ("WWP-IP-INTERFACE-MIB",
     "wwpIpExtInterfaceEntry")
)
wwpIpExtInterfaceEntry.setIndexNames(*wwpIpInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects

wwpIpInterfaceAddrChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 17, 2, 0, 1)
)
wwpIpInterfaceAddrChgNotification.setObjects(
      *(("WWP-IP-INTERFACE-MIB", "wwpIpInterfaceName"),
        ("WWP-IP-INTERFACE-MIB", "wwpIpInterfaceIpAddr"),
        ("WWP-IP-INTERFACE-MIB", "wwpIpInterfaceSubnet"))
)
if mibBuilder.loadTexts:
    wwpIpInterfaceAddrChgNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-IP-INTERFACE-MIB",
    **{"VlanId": VlanId,
       "wwpIpInterfaceMIB": wwpIpInterfaceMIB,
       "wwpIpInterfaceMIBObjects": wwpIpInterfaceMIBObjects,
       "wwpIpInterface": wwpIpInterface,
       "wwpIpInterfaceTable": wwpIpInterfaceTable,
       "wwpIpInterfaceEntry": wwpIpInterfaceEntry,
       "wwpIpInterfaceIndex": wwpIpInterfaceIndex,
       "wwpIpInterfaceName": wwpIpInterfaceName,
       "wwpIpInterfaceIpAddr": wwpIpInterfaceIpAddr,
       "wwpIpInterfaceSubnet": wwpIpInterfaceSubnet,
       "wwpIpInterfaceIfIndexXref": wwpIpInterfaceIfIndexXref,
       "wwpIpExtInterfaceTable": wwpIpExtInterfaceTable,
       "wwpIpExtInterfaceEntry": wwpIpExtInterfaceEntry,
       "wwpIpInterfaceEnable": wwpIpInterfaceEnable,
       "wwpIpInterfaceVlanId": wwpIpInterfaceVlanId,
       "wwpIpInterfaceMgmtPktPriority": wwpIpInterfaceMgmtPktPriority,
       "wwpIpInterfaceAddrNotifEnabled": wwpIpInterfaceAddrNotifEnabled,
       "wwpIpInterfaceMIBNotificationPrefix": wwpIpInterfaceMIBNotificationPrefix,
       "wwpIpInterfaceMIBNotifications": wwpIpInterfaceMIBNotifications,
       "wwpIpInterfaceAddrChgNotification": wwpIpInterfaceAddrChgNotification,
       "wwpIpInterfaceMIBConformance": wwpIpInterfaceMIBConformance,
       "wwpIpInterfaceMIBCompliances": wwpIpInterfaceMIBCompliances,
       "wwpIpInterfaceMIBGroups": wwpIpInterfaceMIBGroups}
)
