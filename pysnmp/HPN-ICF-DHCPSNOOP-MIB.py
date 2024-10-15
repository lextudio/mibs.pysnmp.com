# SNMP MIB module (HPN-ICF-DHCPSNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCPSNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:44 2024
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

(hpnicfdot1qVlanIndex,) = mibBuilder.importSymbols(
    "HPN-ICF-LswVLAN-MIB",
    "hpnicfdot1qVlanIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfDhcpSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDhcpSnoopMibObject_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoopMibObject = _HpnicfDhcpSnoopMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1)
)


class _HpnicfDhcpSnoopEnable_Type(Integer32):
    """Custom type hpnicfDhcpSnoopEnable based on Integer32"""
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


_HpnicfDhcpSnoopEnable_Type.__name__ = "Integer32"
_HpnicfDhcpSnoopEnable_Object = MibScalar
hpnicfDhcpSnoopEnable = _HpnicfDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 1),
    _HpnicfDhcpSnoopEnable_Type()
)
hpnicfDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopEnable.setStatus("current")
_HpnicfDhcpSnoopTable_Object = MibTable
hpnicfDhcpSnoopTable = _HpnicfDhcpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopTable.setStatus("current")
_HpnicfDhcpSnoopEntry_Object = MibTableRow
hpnicfDhcpSnoopEntry = _HpnicfDhcpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1)
)
hpnicfDhcpSnoopEntry.setIndexNames(
    (0, "HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopClientIpAddressType"),
    (0, "HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopClientIpAddress"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopEntry.setStatus("current")


class _HpnicfDhcpSnoopClientIpAddressType_Type(InetAddressType):
    """Custom type hpnicfDhcpSnoopClientIpAddressType based on InetAddressType"""


_HpnicfDhcpSnoopClientIpAddressType_Object = MibTableColumn
hpnicfDhcpSnoopClientIpAddressType = _HpnicfDhcpSnoopClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1, 1),
    _HpnicfDhcpSnoopClientIpAddressType_Type()
)
hpnicfDhcpSnoopClientIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopClientIpAddressType.setStatus("current")
_HpnicfDhcpSnoopClientIpAddress_Type = InetAddress
_HpnicfDhcpSnoopClientIpAddress_Object = MibTableColumn
hpnicfDhcpSnoopClientIpAddress = _HpnicfDhcpSnoopClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1, 2),
    _HpnicfDhcpSnoopClientIpAddress_Type()
)
hpnicfDhcpSnoopClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopClientIpAddress.setStatus("current")
_HpnicfDhcpSnoopClientMacAddress_Type = MacAddress
_HpnicfDhcpSnoopClientMacAddress_Object = MibTableColumn
hpnicfDhcpSnoopClientMacAddress = _HpnicfDhcpSnoopClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1, 3),
    _HpnicfDhcpSnoopClientMacAddress_Type()
)
hpnicfDhcpSnoopClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopClientMacAddress.setStatus("current")


class _HpnicfDhcpSnoopClientProperty_Type(Integer32):
    """Custom type hpnicfDhcpSnoopClientProperty based on Integer32"""
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


_HpnicfDhcpSnoopClientProperty_Type.__name__ = "Integer32"
_HpnicfDhcpSnoopClientProperty_Object = MibTableColumn
hpnicfDhcpSnoopClientProperty = _HpnicfDhcpSnoopClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1, 4),
    _HpnicfDhcpSnoopClientProperty_Type()
)
hpnicfDhcpSnoopClientProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopClientProperty.setStatus("current")
_HpnicfDhcpSnoopClientUnitNum_Type = Integer32
_HpnicfDhcpSnoopClientUnitNum_Object = MibTableColumn
hpnicfDhcpSnoopClientUnitNum = _HpnicfDhcpSnoopClientUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 2, 1, 5),
    _HpnicfDhcpSnoopClientUnitNum_Type()
)
hpnicfDhcpSnoopClientUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopClientUnitNum.setStatus("current")
_HpnicfDhcpSnoopTrustTable_Object = MibTable
hpnicfDhcpSnoopTrustTable = _HpnicfDhcpSnoopTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopTrustTable.setStatus("current")
_HpnicfDhcpSnoopTrustEntry_Object = MibTableRow
hpnicfDhcpSnoopTrustEntry = _HpnicfDhcpSnoopTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 3, 1)
)
hpnicfDhcpSnoopTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopTrustEntry.setStatus("current")


class _HpnicfDhcpSnoopTrustStatus_Type(Integer32):
    """Custom type hpnicfDhcpSnoopTrustStatus based on Integer32"""
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


_HpnicfDhcpSnoopTrustStatus_Type.__name__ = "Integer32"
_HpnicfDhcpSnoopTrustStatus_Object = MibTableColumn
hpnicfDhcpSnoopTrustStatus = _HpnicfDhcpSnoopTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 3, 1, 1),
    _HpnicfDhcpSnoopTrustStatus_Type()
)
hpnicfDhcpSnoopTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopTrustStatus.setStatus("current")
_HpnicfDhcpSnoopVlanTable_Object = MibTable
hpnicfDhcpSnoopVlanTable = _HpnicfDhcpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopVlanTable.setStatus("current")
_HpnicfDhcpSnoopVlanEntry_Object = MibTableRow
hpnicfDhcpSnoopVlanEntry = _HpnicfDhcpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 4, 1)
)
hpnicfDhcpSnoopVlanEntry.setIndexNames(
    (0, "HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopVlanEntry.setStatus("current")


class _HpnicfDhcpSnoopVlanIndex_Type(Integer32):
    """Custom type hpnicfDhcpSnoopVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfDhcpSnoopVlanIndex_Type.__name__ = "Integer32"
_HpnicfDhcpSnoopVlanIndex_Object = MibTableColumn
hpnicfDhcpSnoopVlanIndex = _HpnicfDhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 4, 1, 1),
    _HpnicfDhcpSnoopVlanIndex_Type()
)
hpnicfDhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopVlanIndex.setStatus("current")


class _HpnicfDhcpSnoopVlanEnable_Type(TruthValue):
    """Custom type hpnicfDhcpSnoopVlanEnable based on TruthValue"""


_HpnicfDhcpSnoopVlanEnable_Object = MibTableColumn
hpnicfDhcpSnoopVlanEnable = _HpnicfDhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 1, 4, 1, 2),
    _HpnicfDhcpSnoopVlanEnable_Type()
)
hpnicfDhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopVlanEnable.setStatus("current")
_HpnicfDhcpSnoopTraps_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoopTraps = _HpnicfDhcpSnoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2)
)
_HpnicfDhcpSnoopTrapsPrefix_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoopTrapsPrefix = _HpnicfDhcpSnoopTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 0)
)
_HpnicfDhcpSnoopTrapsObject_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoopTrapsObject = _HpnicfDhcpSnoopTrapsObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 1)
)
_HpnicfDhcpSnoopSpoofServerMac_Type = MacAddress
_HpnicfDhcpSnoopSpoofServerMac_Object = MibScalar
hpnicfDhcpSnoopSpoofServerMac = _HpnicfDhcpSnoopSpoofServerMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 1, 1),
    _HpnicfDhcpSnoopSpoofServerMac_Type()
)
hpnicfDhcpSnoopSpoofServerMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopSpoofServerMac.setStatus("current")
_HpnicfDhcpSnoopSpoofServerIP_Type = IpAddress
_HpnicfDhcpSnoopSpoofServerIP_Object = MibScalar
hpnicfDhcpSnoopSpoofServerIP = _HpnicfDhcpSnoopSpoofServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 1, 2),
    _HpnicfDhcpSnoopSpoofServerIP_Type()
)
hpnicfDhcpSnoopSpoofServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopSpoofServerIP.setStatus("current")
_HpnicfDhcpSnoopBindingIP_Type = IpAddress
_HpnicfDhcpSnoopBindingIP_Object = MibScalar
hpnicfDhcpSnoopBindingIP = _HpnicfDhcpSnoopBindingIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 1, 3),
    _HpnicfDhcpSnoopBindingIP_Type()
)
hpnicfDhcpSnoopBindingIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopBindingIP.setStatus("current")
_HpnicfDhcpSnoopBindingMac_Type = MacAddress
_HpnicfDhcpSnoopBindingMac_Object = MibScalar
hpnicfDhcpSnoopBindingMac = _HpnicfDhcpSnoopBindingMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 1, 4),
    _HpnicfDhcpSnoopBindingMac_Type()
)
hpnicfDhcpSnoopBindingMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopBindingMac.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfDhcpSnoopSpoofServerDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 0, 1)
)
hpnicfDhcpSnoopSpoofServerDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"),
        ("HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopSpoofServerMac"),
        ("HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopSpoofServerIP"))
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopSpoofServerDetected.setStatus(
        "current"
    )

hpnicfDhcpSnoopNewBinding = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 36, 2, 0, 2)
)
hpnicfDhcpSnoopNewBinding.setObjects(
      *(("HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopBindingIP"),
        ("HPN-ICF-DHCPSNOOP-MIB", "hpnicfDhcpSnoopBindingMac"))
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoopNewBinding.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCPSNOOP-MIB",
    **{"hpnicfDhcpSnoop": hpnicfDhcpSnoop,
       "hpnicfDhcpSnoopMibObject": hpnicfDhcpSnoopMibObject,
       "hpnicfDhcpSnoopEnable": hpnicfDhcpSnoopEnable,
       "hpnicfDhcpSnoopTable": hpnicfDhcpSnoopTable,
       "hpnicfDhcpSnoopEntry": hpnicfDhcpSnoopEntry,
       "hpnicfDhcpSnoopClientIpAddressType": hpnicfDhcpSnoopClientIpAddressType,
       "hpnicfDhcpSnoopClientIpAddress": hpnicfDhcpSnoopClientIpAddress,
       "hpnicfDhcpSnoopClientMacAddress": hpnicfDhcpSnoopClientMacAddress,
       "hpnicfDhcpSnoopClientProperty": hpnicfDhcpSnoopClientProperty,
       "hpnicfDhcpSnoopClientUnitNum": hpnicfDhcpSnoopClientUnitNum,
       "hpnicfDhcpSnoopTrustTable": hpnicfDhcpSnoopTrustTable,
       "hpnicfDhcpSnoopTrustEntry": hpnicfDhcpSnoopTrustEntry,
       "hpnicfDhcpSnoopTrustStatus": hpnicfDhcpSnoopTrustStatus,
       "hpnicfDhcpSnoopVlanTable": hpnicfDhcpSnoopVlanTable,
       "hpnicfDhcpSnoopVlanEntry": hpnicfDhcpSnoopVlanEntry,
       "hpnicfDhcpSnoopVlanIndex": hpnicfDhcpSnoopVlanIndex,
       "hpnicfDhcpSnoopVlanEnable": hpnicfDhcpSnoopVlanEnable,
       "hpnicfDhcpSnoopTraps": hpnicfDhcpSnoopTraps,
       "hpnicfDhcpSnoopTrapsPrefix": hpnicfDhcpSnoopTrapsPrefix,
       "hpnicfDhcpSnoopSpoofServerDetected": hpnicfDhcpSnoopSpoofServerDetected,
       "hpnicfDhcpSnoopNewBinding": hpnicfDhcpSnoopNewBinding,
       "hpnicfDhcpSnoopTrapsObject": hpnicfDhcpSnoopTrapsObject,
       "hpnicfDhcpSnoopSpoofServerMac": hpnicfDhcpSnoopSpoofServerMac,
       "hpnicfDhcpSnoopSpoofServerIP": hpnicfDhcpSnoopSpoofServerIP,
       "hpnicfDhcpSnoopBindingIP": hpnicfDhcpSnoopBindingIP,
       "hpnicfDhcpSnoopBindingMac": hpnicfDhcpSnoopBindingMac}
)
