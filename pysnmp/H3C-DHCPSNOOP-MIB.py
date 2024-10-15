# SNMP MIB module (H3C-DHCPSNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-DHCPSNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:04 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(hwdot1qVlanIndex,) = mibBuilder.importSymbols(
    "HUAWEI-LswVLAN-MIB",
    "hwdot1qVlanIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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


# MODULE-IDENTITY

h3cDhcpSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDhcpSnoopMibObject_ObjectIdentity = ObjectIdentity
h3cDhcpSnoopMibObject = _H3cDhcpSnoopMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1)
)


class _H3cDhcpSnoopEnable_Type(Integer32):
    """Custom type h3cDhcpSnoopEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_H3cDhcpSnoopEnable_Type.__name__ = "Integer32"
_H3cDhcpSnoopEnable_Object = MibScalar
h3cDhcpSnoopEnable = _H3cDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 1),
    _H3cDhcpSnoopEnable_Type()
)
h3cDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDhcpSnoopEnable.setStatus("current")
_H3cDhcpSnoopTable_Object = MibTable
h3cDhcpSnoopTable = _H3cDhcpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopTable.setStatus("current")
_H3cDhcpSnoopEntry_Object = MibTableRow
h3cDhcpSnoopEntry = _H3cDhcpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1)
)
h3cDhcpSnoopEntry.setIndexNames(
    (0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddressType"),
    (0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopClientIpAddress"),
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopEntry.setStatus("current")


class _H3cDhcpSnoopClientIpAddressType_Type(InetAddressType):
    """Custom type h3cDhcpSnoopClientIpAddressType based on InetAddressType"""


_H3cDhcpSnoopClientIpAddressType_Object = MibTableColumn
h3cDhcpSnoopClientIpAddressType = _H3cDhcpSnoopClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 1),
    _H3cDhcpSnoopClientIpAddressType_Type()
)
h3cDhcpSnoopClientIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDhcpSnoopClientIpAddressType.setStatus("current")
_H3cDhcpSnoopClientIpAddress_Type = InetAddress
_H3cDhcpSnoopClientIpAddress_Object = MibTableColumn
h3cDhcpSnoopClientIpAddress = _H3cDhcpSnoopClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 2),
    _H3cDhcpSnoopClientIpAddress_Type()
)
h3cDhcpSnoopClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDhcpSnoopClientIpAddress.setStatus("current")
_H3cDhcpSnoopClientMacAddress_Type = MacAddress
_H3cDhcpSnoopClientMacAddress_Object = MibTableColumn
h3cDhcpSnoopClientMacAddress = _H3cDhcpSnoopClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 3),
    _H3cDhcpSnoopClientMacAddress_Type()
)
h3cDhcpSnoopClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDhcpSnoopClientMacAddress.setStatus("current")


class _H3cDhcpSnoopClientProperty_Type(Integer32):
    """Custom type h3cDhcpSnoopClientProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_H3cDhcpSnoopClientProperty_Type.__name__ = "Integer32"
_H3cDhcpSnoopClientProperty_Object = MibTableColumn
h3cDhcpSnoopClientProperty = _H3cDhcpSnoopClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 4),
    _H3cDhcpSnoopClientProperty_Type()
)
h3cDhcpSnoopClientProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDhcpSnoopClientProperty.setStatus("current")
_H3cDhcpSnoopClientUnitNum_Type = Integer32
_H3cDhcpSnoopClientUnitNum_Object = MibTableColumn
h3cDhcpSnoopClientUnitNum = _H3cDhcpSnoopClientUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 2, 1, 5),
    _H3cDhcpSnoopClientUnitNum_Type()
)
h3cDhcpSnoopClientUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDhcpSnoopClientUnitNum.setStatus("current")
_H3cDhcpSnoopTrustTable_Object = MibTable
h3cDhcpSnoopTrustTable = _H3cDhcpSnoopTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopTrustTable.setStatus("current")
_H3cDhcpSnoopTrustEntry_Object = MibTableRow
h3cDhcpSnoopTrustEntry = _H3cDhcpSnoopTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1)
)
h3cDhcpSnoopTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopTrustEntry.setStatus("current")


class _H3cDhcpSnoopTrustStatus_Type(Integer32):
    """Custom type h3cDhcpSnoopTrustStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 0))
    )


_H3cDhcpSnoopTrustStatus_Type.__name__ = "Integer32"
_H3cDhcpSnoopTrustStatus_Object = MibTableColumn
h3cDhcpSnoopTrustStatus = _H3cDhcpSnoopTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 3, 1, 1),
    _H3cDhcpSnoopTrustStatus_Type()
)
h3cDhcpSnoopTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDhcpSnoopTrustStatus.setStatus("current")
_H3cDhcpSnoopVlanTable_Object = MibTable
h3cDhcpSnoopVlanTable = _H3cDhcpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopVlanTable.setStatus("current")
_H3cDhcpSnoopVlanEntry_Object = MibTableRow
h3cDhcpSnoopVlanEntry = _H3cDhcpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1)
)
h3cDhcpSnoopVlanEntry.setIndexNames(
    (0, "H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopVlanEntry.setStatus("current")


class _H3cDhcpSnoopVlanIndex_Type(Integer32):
    """Custom type h3cDhcpSnoopVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cDhcpSnoopVlanIndex_Type.__name__ = "Integer32"
_H3cDhcpSnoopVlanIndex_Object = MibTableColumn
h3cDhcpSnoopVlanIndex = _H3cDhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 1),
    _H3cDhcpSnoopVlanIndex_Type()
)
h3cDhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDhcpSnoopVlanIndex.setStatus("current")


class _H3cDhcpSnoopVlanEnable_Type(TruthValue):
    """Custom type h3cDhcpSnoopVlanEnable based on TruthValue"""


_H3cDhcpSnoopVlanEnable_Object = MibTableColumn
h3cDhcpSnoopVlanEnable = _H3cDhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 1, 4, 1, 2),
    _H3cDhcpSnoopVlanEnable_Type()
)
h3cDhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDhcpSnoopVlanEnable.setStatus("current")
_H3cDhcpSnoopTraps_ObjectIdentity = ObjectIdentity
h3cDhcpSnoopTraps = _H3cDhcpSnoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2)
)
_H3cDhcpSnoopTrapsPrefix_ObjectIdentity = ObjectIdentity
h3cDhcpSnoopTrapsPrefix = _H3cDhcpSnoopTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0)
)
_H3cDhcpSnoopTrapsObject_ObjectIdentity = ObjectIdentity
h3cDhcpSnoopTrapsObject = _H3cDhcpSnoopTrapsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1)
)
_H3cDhcpSnoopSpoofServerMac_Type = MacAddress
_H3cDhcpSnoopSpoofServerMac_Object = MibScalar
h3cDhcpSnoopSpoofServerMac = _H3cDhcpSnoopSpoofServerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 1),
    _H3cDhcpSnoopSpoofServerMac_Type()
)
h3cDhcpSnoopSpoofServerMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDhcpSnoopSpoofServerMac.setStatus("current")
_H3cDhcpSnoopSpoofServerIP_Type = IpAddress
_H3cDhcpSnoopSpoofServerIP_Object = MibScalar
h3cDhcpSnoopSpoofServerIP = _H3cDhcpSnoopSpoofServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 1, 2),
    _H3cDhcpSnoopSpoofServerIP_Type()
)
h3cDhcpSnoopSpoofServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDhcpSnoopSpoofServerIP.setStatus("current")

# Managed Objects groups


# Notification objects

h3cDhcpSnoopSpoofServerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 36, 2, 0, 1)
)
h3cDhcpSnoopSpoofServerDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"),
        ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerMac"),
        ("H3C-DHCPSNOOP-MIB", "h3cDhcpSnoopSpoofServerIP"))
)
if mibBuilder.loadTexts:
    h3cDhcpSnoopSpoofServerDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DHCPSNOOP-MIB",
    **{"h3cDhcpSnoop": h3cDhcpSnoop,
       "h3cDhcpSnoopMibObject": h3cDhcpSnoopMibObject,
       "h3cDhcpSnoopEnable": h3cDhcpSnoopEnable,
       "h3cDhcpSnoopTable": h3cDhcpSnoopTable,
       "h3cDhcpSnoopEntry": h3cDhcpSnoopEntry,
       "h3cDhcpSnoopClientIpAddressType": h3cDhcpSnoopClientIpAddressType,
       "h3cDhcpSnoopClientIpAddress": h3cDhcpSnoopClientIpAddress,
       "h3cDhcpSnoopClientMacAddress": h3cDhcpSnoopClientMacAddress,
       "h3cDhcpSnoopClientProperty": h3cDhcpSnoopClientProperty,
       "h3cDhcpSnoopClientUnitNum": h3cDhcpSnoopClientUnitNum,
       "h3cDhcpSnoopTrustTable": h3cDhcpSnoopTrustTable,
       "h3cDhcpSnoopTrustEntry": h3cDhcpSnoopTrustEntry,
       "h3cDhcpSnoopTrustStatus": h3cDhcpSnoopTrustStatus,
       "h3cDhcpSnoopVlanTable": h3cDhcpSnoopVlanTable,
       "h3cDhcpSnoopVlanEntry": h3cDhcpSnoopVlanEntry,
       "h3cDhcpSnoopVlanIndex": h3cDhcpSnoopVlanIndex,
       "h3cDhcpSnoopVlanEnable": h3cDhcpSnoopVlanEnable,
       "h3cDhcpSnoopTraps": h3cDhcpSnoopTraps,
       "h3cDhcpSnoopTrapsPrefix": h3cDhcpSnoopTrapsPrefix,
       "h3cDhcpSnoopSpoofServerDetected": h3cDhcpSnoopSpoofServerDetected,
       "h3cDhcpSnoopTrapsObject": h3cDhcpSnoopTrapsObject,
       "h3cDhcpSnoopSpoofServerMac": h3cDhcpSnoopSpoofServerMac,
       "h3cDhcpSnoopSpoofServerIP": h3cDhcpSnoopSpoofServerIP}
)
