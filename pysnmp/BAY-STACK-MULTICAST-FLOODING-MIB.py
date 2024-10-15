# SNMP MIB module (BAY-STACK-MULTICAST-FLOODING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-MULTICAST-FLOODING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:12 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackMulticastFloodingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 6)
)
bayStackMulticastFloodingMib.setRevisions(
        ("2009-06-25 00:00",
         "2008-06-25 00:00",
         "2008-06-19 00:00",
         "2006-08-07 00:00",
         "2004-05-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsmfNotifications_ObjectIdentity = ObjectIdentity
bsmfNotifications = _BsmfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 0)
)
_BsmfObjects_ObjectIdentity = ObjectIdentity
bsmfObjects = _BsmfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 1)
)
_BsmfMulticastFloodingEnabled_Type = TruthValue
_BsmfMulticastFloodingEnabled_Object = MibScalar
bsmfMulticastFloodingEnabled = _BsmfMulticastFloodingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 1, 1),
    _BsmfMulticastFloodingEnabled_Type()
)
bsmfMulticastFloodingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmfMulticastFloodingEnabled.setStatus("current")
_BsmfAllowedAddressTable_Object = MibTable
bsmfAllowedAddressTable = _BsmfAllowedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 2)
)
if mibBuilder.loadTexts:
    bsmfAllowedAddressTable.setStatus("current")
_BsmfAllowedAddressEntry_Object = MibTableRow
bsmfAllowedAddressEntry = _BsmfAllowedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 2, 1)
)
bsmfAllowedAddressEntry.setIndexNames(
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfAllowedAddressMacAddr"),
)
if mibBuilder.loadTexts:
    bsmfAllowedAddressEntry.setStatus("current")
_BsmfAllowedAddressMacAddr_Type = MacAddress
_BsmfAllowedAddressMacAddr_Object = MibTableColumn
bsmfAllowedAddressMacAddr = _BsmfAllowedAddressMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 2, 1, 1),
    _BsmfAllowedAddressMacAddr_Type()
)
bsmfAllowedAddressMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfAllowedAddressMacAddr.setStatus("current")
_BsmfAllowedAddressRowStatus_Type = RowStatus
_BsmfAllowedAddressRowStatus_Object = MibTableColumn
bsmfAllowedAddressRowStatus = _BsmfAllowedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 2, 1, 2),
    _BsmfAllowedAddressRowStatus_Type()
)
bsmfAllowedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsmfAllowedAddressRowStatus.setStatus("current")
_BsmfAllowedInetAddressTable_Object = MibTable
bsmfAllowedInetAddressTable = _BsmfAllowedInetAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 3)
)
if mibBuilder.loadTexts:
    bsmfAllowedInetAddressTable.setStatus("current")
_BsmfAllowedInetAddressEntry_Object = MibTableRow
bsmfAllowedInetAddressEntry = _BsmfAllowedInetAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 3, 1)
)
bsmfAllowedInetAddressEntry.setIndexNames(
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfAllowedInetAddressType"),
    (1, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfAllowedInetAddress"),
)
if mibBuilder.loadTexts:
    bsmfAllowedInetAddressEntry.setStatus("current")
_BsmfAllowedInetAddressType_Type = InetAddressType
_BsmfAllowedInetAddressType_Object = MibTableColumn
bsmfAllowedInetAddressType = _BsmfAllowedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 3, 1, 1),
    _BsmfAllowedInetAddressType_Type()
)
bsmfAllowedInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfAllowedInetAddressType.setStatus("current")


class _BsmfAllowedInetAddress_Type(InetAddress):
    """Custom type bsmfAllowedInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_BsmfAllowedInetAddress_Type.__name__ = "InetAddress"
_BsmfAllowedInetAddress_Object = MibTableColumn
bsmfAllowedInetAddress = _BsmfAllowedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 3, 1, 2),
    _BsmfAllowedInetAddress_Type()
)
bsmfAllowedInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfAllowedInetAddress.setStatus("current")
_BsmfAllowedInetAddressRowStatus_Type = RowStatus
_BsmfAllowedInetAddressRowStatus_Object = MibTableColumn
bsmfAllowedInetAddressRowStatus = _BsmfAllowedInetAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 3, 1, 3),
    _BsmfAllowedInetAddressRowStatus_Type()
)
bsmfAllowedInetAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsmfAllowedInetAddressRowStatus.setStatus("current")
_BsmfVlanTable_Object = MibTable
bsmfVlanTable = _BsmfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 4)
)
if mibBuilder.loadTexts:
    bsmfVlanTable.setStatus("current")
_BsmfVlanEntry_Object = MibTableRow
bsmfVlanEntry = _BsmfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 4, 1)
)
bsmfVlanEntry.setIndexNames(
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanId"),
)
if mibBuilder.loadTexts:
    bsmfVlanEntry.setStatus("current")
_BsmfVlanId_Type = VlanId
_BsmfVlanId_Object = MibTableColumn
bsmfVlanId = _BsmfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 4, 1, 1),
    _BsmfVlanId_Type()
)
bsmfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanId.setStatus("current")
_BsmfVlanMulticastFloodingEnabled_Type = TruthValue
_BsmfVlanMulticastFloodingEnabled_Object = MibTableColumn
bsmfVlanMulticastFloodingEnabled = _BsmfVlanMulticastFloodingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 4, 1, 2),
    _BsmfVlanMulticastFloodingEnabled_Type()
)
bsmfVlanMulticastFloodingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsmfVlanMulticastFloodingEnabled.setStatus("current")
_BsmfVlanAllowedAddressTable_Object = MibTable
bsmfVlanAllowedAddressTable = _BsmfVlanAllowedAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 5)
)
if mibBuilder.loadTexts:
    bsmfVlanAllowedAddressTable.setStatus("current")
_BsmfVlanAllowedAddressEntry_Object = MibTableRow
bsmfVlanAllowedAddressEntry = _BsmfVlanAllowedAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 5, 1)
)
bsmfVlanAllowedAddressEntry.setIndexNames(
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanAllowedAddressVlanId"),
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanAllowedAddressMacAddr"),
)
if mibBuilder.loadTexts:
    bsmfVlanAllowedAddressEntry.setStatus("current")
_BsmfVlanAllowedAddressVlanId_Type = VlanId
_BsmfVlanAllowedAddressVlanId_Object = MibTableColumn
bsmfVlanAllowedAddressVlanId = _BsmfVlanAllowedAddressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 5, 1, 1),
    _BsmfVlanAllowedAddressVlanId_Type()
)
bsmfVlanAllowedAddressVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanAllowedAddressVlanId.setStatus("current")
_BsmfVlanAllowedAddressMacAddr_Type = MacAddress
_BsmfVlanAllowedAddressMacAddr_Object = MibTableColumn
bsmfVlanAllowedAddressMacAddr = _BsmfVlanAllowedAddressMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 5, 1, 2),
    _BsmfVlanAllowedAddressMacAddr_Type()
)
bsmfVlanAllowedAddressMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanAllowedAddressMacAddr.setStatus("current")
_BsmfVlanAllowedAddressRowStatus_Type = RowStatus
_BsmfVlanAllowedAddressRowStatus_Object = MibTableColumn
bsmfVlanAllowedAddressRowStatus = _BsmfVlanAllowedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 5, 1, 3),
    _BsmfVlanAllowedAddressRowStatus_Type()
)
bsmfVlanAllowedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsmfVlanAllowedAddressRowStatus.setStatus("current")
_BsmfVlanAllowedInetAddressTable_Object = MibTable
bsmfVlanAllowedInetAddressTable = _BsmfVlanAllowedInetAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6)
)
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddressTable.setStatus("current")
_BsmfVlanAllowedInetAddressEntry_Object = MibTableRow
bsmfVlanAllowedInetAddressEntry = _BsmfVlanAllowedInetAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6, 1)
)
bsmfVlanAllowedInetAddressEntry.setIndexNames(
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanAllowedInetAddressVlanId"),
    (0, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanAllowedInetAddressType"),
    (1, "BAY-STACK-MULTICAST-FLOODING-MIB", "bsmfVlanAllowedInetAddress"),
)
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddressEntry.setStatus("current")
_BsmfVlanAllowedInetAddressVlanId_Type = VlanId
_BsmfVlanAllowedInetAddressVlanId_Object = MibTableColumn
bsmfVlanAllowedInetAddressVlanId = _BsmfVlanAllowedInetAddressVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6, 1, 1),
    _BsmfVlanAllowedInetAddressVlanId_Type()
)
bsmfVlanAllowedInetAddressVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddressVlanId.setStatus("current")
_BsmfVlanAllowedInetAddressType_Type = InetAddressType
_BsmfVlanAllowedInetAddressType_Object = MibTableColumn
bsmfVlanAllowedInetAddressType = _BsmfVlanAllowedInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6, 1, 2),
    _BsmfVlanAllowedInetAddressType_Type()
)
bsmfVlanAllowedInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddressType.setStatus("current")


class _BsmfVlanAllowedInetAddress_Type(InetAddress):
    """Custom type bsmfVlanAllowedInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_BsmfVlanAllowedInetAddress_Type.__name__ = "InetAddress"
_BsmfVlanAllowedInetAddress_Object = MibTableColumn
bsmfVlanAllowedInetAddress = _BsmfVlanAllowedInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6, 1, 3),
    _BsmfVlanAllowedInetAddress_Type()
)
bsmfVlanAllowedInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddress.setStatus("current")
_BsmfVlanAllowedInetAddressRowStatus_Type = RowStatus
_BsmfVlanAllowedInetAddressRowStatus_Object = MibTableColumn
bsmfVlanAllowedInetAddressRowStatus = _BsmfVlanAllowedInetAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 6, 6, 1, 4),
    _BsmfVlanAllowedInetAddressRowStatus_Type()
)
bsmfVlanAllowedInetAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsmfVlanAllowedInetAddressRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-MULTICAST-FLOODING-MIB",
    **{"bayStackMulticastFloodingMib": bayStackMulticastFloodingMib,
       "bsmfNotifications": bsmfNotifications,
       "bsmfObjects": bsmfObjects,
       "bsmfMulticastFloodingEnabled": bsmfMulticastFloodingEnabled,
       "bsmfAllowedAddressTable": bsmfAllowedAddressTable,
       "bsmfAllowedAddressEntry": bsmfAllowedAddressEntry,
       "bsmfAllowedAddressMacAddr": bsmfAllowedAddressMacAddr,
       "bsmfAllowedAddressRowStatus": bsmfAllowedAddressRowStatus,
       "bsmfAllowedInetAddressTable": bsmfAllowedInetAddressTable,
       "bsmfAllowedInetAddressEntry": bsmfAllowedInetAddressEntry,
       "bsmfAllowedInetAddressType": bsmfAllowedInetAddressType,
       "bsmfAllowedInetAddress": bsmfAllowedInetAddress,
       "bsmfAllowedInetAddressRowStatus": bsmfAllowedInetAddressRowStatus,
       "bsmfVlanTable": bsmfVlanTable,
       "bsmfVlanEntry": bsmfVlanEntry,
       "bsmfVlanId": bsmfVlanId,
       "bsmfVlanMulticastFloodingEnabled": bsmfVlanMulticastFloodingEnabled,
       "bsmfVlanAllowedAddressTable": bsmfVlanAllowedAddressTable,
       "bsmfVlanAllowedAddressEntry": bsmfVlanAllowedAddressEntry,
       "bsmfVlanAllowedAddressVlanId": bsmfVlanAllowedAddressVlanId,
       "bsmfVlanAllowedAddressMacAddr": bsmfVlanAllowedAddressMacAddr,
       "bsmfVlanAllowedAddressRowStatus": bsmfVlanAllowedAddressRowStatus,
       "bsmfVlanAllowedInetAddressTable": bsmfVlanAllowedInetAddressTable,
       "bsmfVlanAllowedInetAddressEntry": bsmfVlanAllowedInetAddressEntry,
       "bsmfVlanAllowedInetAddressVlanId": bsmfVlanAllowedInetAddressVlanId,
       "bsmfVlanAllowedInetAddressType": bsmfVlanAllowedInetAddressType,
       "bsmfVlanAllowedInetAddress": bsmfVlanAllowedInetAddress,
       "bsmfVlanAllowedInetAddressRowStatus": bsmfVlanAllowedInetAddressRowStatus}
)
