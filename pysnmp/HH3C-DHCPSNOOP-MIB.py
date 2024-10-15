# SNMP MIB module (HH3C-DHCPSNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCPSNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:44 2024
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

(hh3cdot1qVlanIndex,) = mibBuilder.importSymbols(
    "HH3C-LswVLAN-MIB",
    "hh3cdot1qVlanIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDhcpSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDhcpSnoopMibObject_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoopMibObject = _Hh3cDhcpSnoopMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1)
)


class _Hh3cDhcpSnoopEnable_Type(Integer32):
    """Custom type hh3cDhcpSnoopEnable based on Integer32"""
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


_Hh3cDhcpSnoopEnable_Type.__name__ = "Integer32"
_Hh3cDhcpSnoopEnable_Object = MibScalar
hh3cDhcpSnoopEnable = _Hh3cDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 1),
    _Hh3cDhcpSnoopEnable_Type()
)
hh3cDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopEnable.setStatus("current")
_Hh3cDhcpSnoopTable_Object = MibTable
hh3cDhcpSnoopTable = _Hh3cDhcpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopTable.setStatus("current")
_Hh3cDhcpSnoopEntry_Object = MibTableRow
hh3cDhcpSnoopEntry = _Hh3cDhcpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1)
)
hh3cDhcpSnoopEntry.setIndexNames(
    (0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddressType"),
    (0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddress"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopEntry.setStatus("current")


class _Hh3cDhcpSnoopClientIpAddressType_Type(InetAddressType):
    """Custom type hh3cDhcpSnoopClientIpAddressType based on InetAddressType"""


_Hh3cDhcpSnoopClientIpAddressType_Object = MibTableColumn
hh3cDhcpSnoopClientIpAddressType = _Hh3cDhcpSnoopClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 1),
    _Hh3cDhcpSnoopClientIpAddressType_Type()
)
hh3cDhcpSnoopClientIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopClientIpAddressType.setStatus("current")
_Hh3cDhcpSnoopClientIpAddress_Type = InetAddress
_Hh3cDhcpSnoopClientIpAddress_Object = MibTableColumn
hh3cDhcpSnoopClientIpAddress = _Hh3cDhcpSnoopClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 2),
    _Hh3cDhcpSnoopClientIpAddress_Type()
)
hh3cDhcpSnoopClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopClientIpAddress.setStatus("current")
_Hh3cDhcpSnoopClientMacAddress_Type = MacAddress
_Hh3cDhcpSnoopClientMacAddress_Object = MibTableColumn
hh3cDhcpSnoopClientMacAddress = _Hh3cDhcpSnoopClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 3),
    _Hh3cDhcpSnoopClientMacAddress_Type()
)
hh3cDhcpSnoopClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopClientMacAddress.setStatus("current")


class _Hh3cDhcpSnoopClientProperty_Type(Integer32):
    """Custom type hh3cDhcpSnoopClientProperty based on Integer32"""
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


_Hh3cDhcpSnoopClientProperty_Type.__name__ = "Integer32"
_Hh3cDhcpSnoopClientProperty_Object = MibTableColumn
hh3cDhcpSnoopClientProperty = _Hh3cDhcpSnoopClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 4),
    _Hh3cDhcpSnoopClientProperty_Type()
)
hh3cDhcpSnoopClientProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopClientProperty.setStatus("current")
_Hh3cDhcpSnoopClientUnitNum_Type = Integer32
_Hh3cDhcpSnoopClientUnitNum_Object = MibTableColumn
hh3cDhcpSnoopClientUnitNum = _Hh3cDhcpSnoopClientUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 5),
    _Hh3cDhcpSnoopClientUnitNum_Type()
)
hh3cDhcpSnoopClientUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopClientUnitNum.setStatus("current")
_Hh3cDhcpSnoopTrustTable_Object = MibTable
hh3cDhcpSnoopTrustTable = _Hh3cDhcpSnoopTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopTrustTable.setStatus("current")
_Hh3cDhcpSnoopTrustEntry_Object = MibTableRow
hh3cDhcpSnoopTrustEntry = _Hh3cDhcpSnoopTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1)
)
hh3cDhcpSnoopTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopTrustEntry.setStatus("current")


class _Hh3cDhcpSnoopTrustStatus_Type(Integer32):
    """Custom type hh3cDhcpSnoopTrustStatus based on Integer32"""
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


_Hh3cDhcpSnoopTrustStatus_Type.__name__ = "Integer32"
_Hh3cDhcpSnoopTrustStatus_Object = MibTableColumn
hh3cDhcpSnoopTrustStatus = _Hh3cDhcpSnoopTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1, 1),
    _Hh3cDhcpSnoopTrustStatus_Type()
)
hh3cDhcpSnoopTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopTrustStatus.setStatus("current")
_Hh3cDhcpSnoopVlanTable_Object = MibTable
hh3cDhcpSnoopVlanTable = _Hh3cDhcpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopVlanTable.setStatus("current")
_Hh3cDhcpSnoopVlanEntry_Object = MibTableRow
hh3cDhcpSnoopVlanEntry = _Hh3cDhcpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1)
)
hh3cDhcpSnoopVlanEntry.setIndexNames(
    (0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopVlanEntry.setStatus("current")


class _Hh3cDhcpSnoopVlanIndex_Type(Integer32):
    """Custom type hh3cDhcpSnoopVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDhcpSnoopVlanIndex_Type.__name__ = "Integer32"
_Hh3cDhcpSnoopVlanIndex_Object = MibTableColumn
hh3cDhcpSnoopVlanIndex = _Hh3cDhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 1),
    _Hh3cDhcpSnoopVlanIndex_Type()
)
hh3cDhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopVlanIndex.setStatus("current")


class _Hh3cDhcpSnoopVlanEnable_Type(TruthValue):
    """Custom type hh3cDhcpSnoopVlanEnable based on TruthValue"""


_Hh3cDhcpSnoopVlanEnable_Object = MibTableColumn
hh3cDhcpSnoopVlanEnable = _Hh3cDhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 2),
    _Hh3cDhcpSnoopVlanEnable_Type()
)
hh3cDhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopVlanEnable.setStatus("current")
_Hh3cDhcpSnoopTraps_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoopTraps = _Hh3cDhcpSnoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2)
)
_Hh3cDhcpSnoopTrapsPrefix_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoopTrapsPrefix = _Hh3cDhcpSnoopTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0)
)
_Hh3cDhcpSnoopTrapsObject_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoopTrapsObject = _Hh3cDhcpSnoopTrapsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1)
)
_Hh3cDhcpSnoopSpoofServerMac_Type = MacAddress
_Hh3cDhcpSnoopSpoofServerMac_Object = MibScalar
hh3cDhcpSnoopSpoofServerMac = _Hh3cDhcpSnoopSpoofServerMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 1),
    _Hh3cDhcpSnoopSpoofServerMac_Type()
)
hh3cDhcpSnoopSpoofServerMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopSpoofServerMac.setStatus("current")
_Hh3cDhcpSnoopSpoofServerIP_Type = IpAddress
_Hh3cDhcpSnoopSpoofServerIP_Object = MibScalar
hh3cDhcpSnoopSpoofServerIP = _Hh3cDhcpSnoopSpoofServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 2),
    _Hh3cDhcpSnoopSpoofServerIP_Type()
)
hh3cDhcpSnoopSpoofServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDhcpSnoopSpoofServerIP.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDhcpSnoopSpoofServerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0, 1)
)
hh3cDhcpSnoopSpoofServerDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"),
        ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerMac"),
        ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerIP"))
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoopSpoofServerDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCPSNOOP-MIB",
    **{"hh3cDhcpSnoop": hh3cDhcpSnoop,
       "hh3cDhcpSnoopMibObject": hh3cDhcpSnoopMibObject,
       "hh3cDhcpSnoopEnable": hh3cDhcpSnoopEnable,
       "hh3cDhcpSnoopTable": hh3cDhcpSnoopTable,
       "hh3cDhcpSnoopEntry": hh3cDhcpSnoopEntry,
       "hh3cDhcpSnoopClientIpAddressType": hh3cDhcpSnoopClientIpAddressType,
       "hh3cDhcpSnoopClientIpAddress": hh3cDhcpSnoopClientIpAddress,
       "hh3cDhcpSnoopClientMacAddress": hh3cDhcpSnoopClientMacAddress,
       "hh3cDhcpSnoopClientProperty": hh3cDhcpSnoopClientProperty,
       "hh3cDhcpSnoopClientUnitNum": hh3cDhcpSnoopClientUnitNum,
       "hh3cDhcpSnoopTrustTable": hh3cDhcpSnoopTrustTable,
       "hh3cDhcpSnoopTrustEntry": hh3cDhcpSnoopTrustEntry,
       "hh3cDhcpSnoopTrustStatus": hh3cDhcpSnoopTrustStatus,
       "hh3cDhcpSnoopVlanTable": hh3cDhcpSnoopVlanTable,
       "hh3cDhcpSnoopVlanEntry": hh3cDhcpSnoopVlanEntry,
       "hh3cDhcpSnoopVlanIndex": hh3cDhcpSnoopVlanIndex,
       "hh3cDhcpSnoopVlanEnable": hh3cDhcpSnoopVlanEnable,
       "hh3cDhcpSnoopTraps": hh3cDhcpSnoopTraps,
       "hh3cDhcpSnoopTrapsPrefix": hh3cDhcpSnoopTrapsPrefix,
       "hh3cDhcpSnoopSpoofServerDetected": hh3cDhcpSnoopSpoofServerDetected,
       "hh3cDhcpSnoopTrapsObject": hh3cDhcpSnoopTrapsObject,
       "hh3cDhcpSnoopSpoofServerMac": hh3cDhcpSnoopSpoofServerMac,
       "hh3cDhcpSnoopSpoofServerIP": hh3cDhcpSnoopSpoofServerIP}
)
