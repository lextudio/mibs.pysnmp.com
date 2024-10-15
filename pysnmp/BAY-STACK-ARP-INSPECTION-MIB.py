# SNMP MIB module (BAY-STACK-ARP-INSPECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-ARP-INSPECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:50 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackArpInspectionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 18)
)
bayStackArpInspectionMib.setRevisions(
        ("2013-10-11 00:00",
         "2013-07-05 00:00",
         "2008-10-30 00:00",
         "2006-06-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsArpInspectionNotifications_ObjectIdentity = ObjectIdentity
bsArpInspectionNotifications = _BsArpInspectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 0)
)
_BsArpInspectionObjects_ObjectIdentity = ObjectIdentity
bsArpInspectionObjects = _BsArpInspectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1)
)
_BsArpInspectionVlanTable_Object = MibTable
bsArpInspectionVlanTable = _BsArpInspectionVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1)
)
if mibBuilder.loadTexts:
    bsArpInspectionVlanTable.setStatus("current")
_BsArpInspectionVlanEntry_Object = MibTableRow
bsArpInspectionVlanEntry = _BsArpInspectionVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1)
)
bsArpInspectionVlanEntry.setIndexNames(
    (0, "BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionVlanId"),
)
if mibBuilder.loadTexts:
    bsArpInspectionVlanEntry.setStatus("current")
_BsArpInspectionVlanId_Type = VlanIndex
_BsArpInspectionVlanId_Object = MibTableColumn
bsArpInspectionVlanId = _BsArpInspectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1, 1),
    _BsArpInspectionVlanId_Type()
)
bsArpInspectionVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsArpInspectionVlanId.setStatus("current")
_BsArpInspectionVlanEnabled_Type = TruthValue
_BsArpInspectionVlanEnabled_Object = MibTableColumn
bsArpInspectionVlanEnabled = _BsArpInspectionVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 1, 1, 2),
    _BsArpInspectionVlanEnabled_Type()
)
bsArpInspectionVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsArpInspectionVlanEnabled.setStatus("current")
_BsArpInspectionIfTable_Object = MibTable
bsArpInspectionIfTable = _BsArpInspectionIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2)
)
if mibBuilder.loadTexts:
    bsArpInspectionIfTable.setStatus("current")
_BsArpInspectionIfEntry_Object = MibTableRow
bsArpInspectionIfEntry = _BsArpInspectionIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1)
)
bsArpInspectionIfEntry.setIndexNames(
    (0, "BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionIfIndex"),
)
if mibBuilder.loadTexts:
    bsArpInspectionIfEntry.setStatus("current")
_BsArpInspectionIfIndex_Type = InterfaceIndex
_BsArpInspectionIfIndex_Object = MibTableColumn
bsArpInspectionIfIndex = _BsArpInspectionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1, 1),
    _BsArpInspectionIfIndex_Type()
)
bsArpInspectionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsArpInspectionIfIndex.setStatus("current")
_BsArpInspectionIfTrusted_Type = TruthValue
_BsArpInspectionIfTrusted_Object = MibTableColumn
bsArpInspectionIfTrusted = _BsArpInspectionIfTrusted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 2, 1, 2),
    _BsArpInspectionIfTrusted_Type()
)
bsArpInspectionIfTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsArpInspectionIfTrusted.setStatus("current")
_BsArpInspectionNotificationObjects_ObjectIdentity = ObjectIdentity
bsArpInspectionNotificationObjects = _BsArpInspectionNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 3)
)
_BsArpInspectionNotificationSourceMACAddr_Type = MacAddress
_BsArpInspectionNotificationSourceMACAddr_Object = MibScalar
bsArpInspectionNotificationSourceMACAddr = _BsArpInspectionNotificationSourceMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 1, 3, 1),
    _BsArpInspectionNotificationSourceMACAddr_Type()
)
bsArpInspectionNotificationSourceMACAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsArpInspectionNotificationSourceMACAddr.setStatus("current")

# Managed Objects groups


# Notification objects

bsaiArpPacketDroppedOnUntrustedPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 18, 0, 1)
)
bsaiArpPacketDroppedOnUntrustedPort.setObjects(
      *(("BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionIfTrusted"),
        ("BAY-STACK-ARP-INSPECTION-MIB", "bsArpInspectionNotificationSourceMACAddr"))
)
if mibBuilder.loadTexts:
    bsaiArpPacketDroppedOnUntrustedPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-ARP-INSPECTION-MIB",
    **{"bayStackArpInspectionMib": bayStackArpInspectionMib,
       "bsArpInspectionNotifications": bsArpInspectionNotifications,
       "bsaiArpPacketDroppedOnUntrustedPort": bsaiArpPacketDroppedOnUntrustedPort,
       "bsArpInspectionObjects": bsArpInspectionObjects,
       "bsArpInspectionVlanTable": bsArpInspectionVlanTable,
       "bsArpInspectionVlanEntry": bsArpInspectionVlanEntry,
       "bsArpInspectionVlanId": bsArpInspectionVlanId,
       "bsArpInspectionVlanEnabled": bsArpInspectionVlanEnabled,
       "bsArpInspectionIfTable": bsArpInspectionIfTable,
       "bsArpInspectionIfEntry": bsArpInspectionIfEntry,
       "bsArpInspectionIfIndex": bsArpInspectionIfIndex,
       "bsArpInspectionIfTrusted": bsArpInspectionIfTrusted,
       "bsArpInspectionNotificationObjects": bsArpInspectionNotificationObjects,
       "bsArpInspectionNotificationSourceMACAddr": bsArpInspectionNotificationSourceMACAddr}
)
