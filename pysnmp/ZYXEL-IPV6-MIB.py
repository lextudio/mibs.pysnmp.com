# SNMP MIB module (ZYXEL-IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:05 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIpv6Setup_ObjectIdentity = ObjectIdentity
zyxelIpv6Setup = _ZyxelIpv6Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1)
)
_ZyIpv6HopLimit_Type = Integer32
_ZyIpv6HopLimit_Object = MibScalar
zyIpv6HopLimit = _ZyIpv6HopLimit_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 1),
    _ZyIpv6HopLimit_Type()
)
zyIpv6HopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6HopLimit.setStatus("current")
_ZyIpv6IcmpRateLimitErrorInterval_Type = Integer32
_ZyIpv6IcmpRateLimitErrorInterval_Object = MibScalar
zyIpv6IcmpRateLimitErrorInterval = _ZyIpv6IcmpRateLimitErrorInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 2),
    _ZyIpv6IcmpRateLimitErrorInterval_Type()
)
zyIpv6IcmpRateLimitErrorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6IcmpRateLimitErrorInterval.setStatus("current")
_ZyIpv6IcmpRateLimitBucketSize_Type = Integer32
_ZyIpv6IcmpRateLimitBucketSize_Object = MibScalar
zyIpv6IcmpRateLimitBucketSize = _ZyIpv6IcmpRateLimitBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 3),
    _ZyIpv6IcmpRateLimitBucketSize_Type()
)
zyIpv6IcmpRateLimitBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6IcmpRateLimitBucketSize.setStatus("current")
_ZyIpv6MaxNumberOfGlobalAddrresses_Type = Integer32
_ZyIpv6MaxNumberOfGlobalAddrresses_Object = MibScalar
zyIpv6MaxNumberOfGlobalAddrresses = _ZyIpv6MaxNumberOfGlobalAddrresses_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 4),
    _ZyIpv6MaxNumberOfGlobalAddrresses_Type()
)
zyIpv6MaxNumberOfGlobalAddrresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6MaxNumberOfGlobalAddrresses.setStatus("current")
_ZyxelIpv6Table_Object = MibTable
zyxelIpv6Table = _ZyxelIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelIpv6Table.setStatus("current")
_ZyxelIpv6Entry_Object = MibTableRow
zyxelIpv6Entry = _ZyxelIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1)
)
zyxelIpv6Entry.setIndexNames(
    (0, "ZYXEL-IPV6-MIB", "zyIpv6IfIndex"),
)
if mibBuilder.loadTexts:
    zyxelIpv6Entry.setStatus("current")
_ZyIpv6IfIndex_Type = Integer32
_ZyIpv6IfIndex_Object = MibTableColumn
zyIpv6IfIndex = _ZyIpv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 1),
    _ZyIpv6IfIndex_Type()
)
zyIpv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6IfIndex.setStatus("current")
_ZyIpv6State_Type = EnabledStatus
_ZyIpv6State_Object = MibTableColumn
zyIpv6State = _ZyIpv6State_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 2),
    _ZyIpv6State_Type()
)
zyIpv6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6State.setStatus("current")


class _ZyIpv6AddressAutoConfigState_Type(EnabledStatus):
    """Custom type zyIpv6AddressAutoConfigState based on EnabledStatus"""
    subtypeSpec = EnabledStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 2),
          ("stateless", 1))
    )


_ZyIpv6AddressAutoConfigState_Type.__name__ = "EnabledStatus"
_ZyIpv6AddressAutoConfigState_Object = MibTableColumn
zyIpv6AddressAutoConfigState = _ZyIpv6AddressAutoConfigState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 3),
    _ZyIpv6AddressAutoConfigState_Type()
)
zyIpv6AddressAutoConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6AddressAutoConfigState.setStatus("current")
_ZyIpv6LinkLocalIpAddrressType_Type = InetAddressType
_ZyIpv6LinkLocalIpAddrressType_Object = MibTableColumn
zyIpv6LinkLocalIpAddrressType = _ZyIpv6LinkLocalIpAddrressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 4),
    _ZyIpv6LinkLocalIpAddrressType_Type()
)
zyIpv6LinkLocalIpAddrressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6LinkLocalIpAddrressType.setStatus("current")
_ZyIpv6LinkLocalIpAddrress_Type = InetAddress
_ZyIpv6LinkLocalIpAddrress_Object = MibTableColumn
zyIpv6LinkLocalIpAddrress = _ZyIpv6LinkLocalIpAddrress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 5),
    _ZyIpv6LinkLocalIpAddrress_Type()
)
zyIpv6LinkLocalIpAddrress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6LinkLocalIpAddrress.setStatus("current")
_ZyIpv6DefaultGatewayType_Type = InetAddressType
_ZyIpv6DefaultGatewayType_Object = MibTableColumn
zyIpv6DefaultGatewayType = _ZyIpv6DefaultGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 6),
    _ZyIpv6DefaultGatewayType_Type()
)
zyIpv6DefaultGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6DefaultGatewayType.setStatus("current")
_ZyIpv6DefaultGateway_Type = InetAddress
_ZyIpv6DefaultGateway_Object = MibTableColumn
zyIpv6DefaultGateway = _ZyIpv6DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 5, 1, 7),
    _ZyIpv6DefaultGateway_Type()
)
zyIpv6DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIpv6DefaultGateway.setStatus("current")
_ZyxelIpv6GlobalAddressTable_Object = MibTable
zyxelIpv6GlobalAddressTable = _ZyxelIpv6GlobalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelIpv6GlobalAddressTable.setStatus("current")
_ZyxelIpv6GlobalAddressEntry_Object = MibTableRow
zyxelIpv6GlobalAddressEntry = _ZyxelIpv6GlobalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1)
)
zyxelIpv6GlobalAddressEntry.setIndexNames(
    (0, "ZYXEL-IPV6-MIB", "zyIpv6GlobalAddressIfIndex"),
    (0, "ZYXEL-IPV6-MIB", "zyIpv6GlobalAddressIpAddressType"),
    (0, "ZYXEL-IPV6-MIB", "zyIpv6GlobalAddressIpAddress"),
    (0, "ZYXEL-IPV6-MIB", "zyIpv6GlobalAddressPrefixLength"),
    (0, "ZYXEL-IPV6-MIB", "zyIpv6GlobalAddressEUI64State"),
)
if mibBuilder.loadTexts:
    zyxelIpv6GlobalAddressEntry.setStatus("current")
_ZyIpv6GlobalAddressIfIndex_Type = Integer32
_ZyIpv6GlobalAddressIfIndex_Object = MibTableColumn
zyIpv6GlobalAddressIfIndex = _ZyIpv6GlobalAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 1),
    _ZyIpv6GlobalAddressIfIndex_Type()
)
zyIpv6GlobalAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressIfIndex.setStatus("current")
_ZyIpv6GlobalAddressIpAddressType_Type = InetAddressType
_ZyIpv6GlobalAddressIpAddressType_Object = MibTableColumn
zyIpv6GlobalAddressIpAddressType = _ZyIpv6GlobalAddressIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 2),
    _ZyIpv6GlobalAddressIpAddressType_Type()
)
zyIpv6GlobalAddressIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressIpAddressType.setStatus("current")
_ZyIpv6GlobalAddressIpAddress_Type = InetAddress
_ZyIpv6GlobalAddressIpAddress_Object = MibTableColumn
zyIpv6GlobalAddressIpAddress = _ZyIpv6GlobalAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 3),
    _ZyIpv6GlobalAddressIpAddress_Type()
)
zyIpv6GlobalAddressIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressIpAddress.setStatus("current")
_ZyIpv6GlobalAddressPrefixLength_Type = Integer32
_ZyIpv6GlobalAddressPrefixLength_Object = MibTableColumn
zyIpv6GlobalAddressPrefixLength = _ZyIpv6GlobalAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 4),
    _ZyIpv6GlobalAddressPrefixLength_Type()
)
zyIpv6GlobalAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressPrefixLength.setStatus("current")
_ZyIpv6GlobalAddressEUI64State_Type = EnabledStatus
_ZyIpv6GlobalAddressEUI64State_Object = MibTableColumn
zyIpv6GlobalAddressEUI64State = _ZyIpv6GlobalAddressEUI64State_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 5),
    _ZyIpv6GlobalAddressEUI64State_Type()
)
zyIpv6GlobalAddressEUI64State.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressEUI64State.setStatus("current")


class _ZyIpv6GlobalAddressStatus_Type(Integer32):
    """Custom type zyIpv6GlobalAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deprecated", 2),
          ("duplicate", 7),
          ("inaccessible", 4),
          ("invalid", 3),
          ("preferred", 1),
          ("tentative", 6),
          ("unknown", 5))
    )


_ZyIpv6GlobalAddressStatus_Type.__name__ = "Integer32"
_ZyIpv6GlobalAddressStatus_Object = MibTableColumn
zyIpv6GlobalAddressStatus = _ZyIpv6GlobalAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 6),
    _ZyIpv6GlobalAddressStatus_Type()
)
zyIpv6GlobalAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressStatus.setStatus("current")
_ZyIpv6GlobalAddressRowStatus_Type = RowStatus
_ZyIpv6GlobalAddressRowStatus_Object = MibTableColumn
zyIpv6GlobalAddressRowStatus = _ZyIpv6GlobalAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 34, 1, 6, 1, 7),
    _ZyIpv6GlobalAddressRowStatus_Type()
)
zyIpv6GlobalAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIpv6GlobalAddressRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPV6-MIB",
    **{"zyxelIpv6": zyxelIpv6,
       "zyxelIpv6Setup": zyxelIpv6Setup,
       "zyIpv6HopLimit": zyIpv6HopLimit,
       "zyIpv6IcmpRateLimitErrorInterval": zyIpv6IcmpRateLimitErrorInterval,
       "zyIpv6IcmpRateLimitBucketSize": zyIpv6IcmpRateLimitBucketSize,
       "zyIpv6MaxNumberOfGlobalAddrresses": zyIpv6MaxNumberOfGlobalAddrresses,
       "zyxelIpv6Table": zyxelIpv6Table,
       "zyxelIpv6Entry": zyxelIpv6Entry,
       "zyIpv6IfIndex": zyIpv6IfIndex,
       "zyIpv6State": zyIpv6State,
       "zyIpv6AddressAutoConfigState": zyIpv6AddressAutoConfigState,
       "zyIpv6LinkLocalIpAddrressType": zyIpv6LinkLocalIpAddrressType,
       "zyIpv6LinkLocalIpAddrress": zyIpv6LinkLocalIpAddrress,
       "zyIpv6DefaultGatewayType": zyIpv6DefaultGatewayType,
       "zyIpv6DefaultGateway": zyIpv6DefaultGateway,
       "zyxelIpv6GlobalAddressTable": zyxelIpv6GlobalAddressTable,
       "zyxelIpv6GlobalAddressEntry": zyxelIpv6GlobalAddressEntry,
       "zyIpv6GlobalAddressIfIndex": zyIpv6GlobalAddressIfIndex,
       "zyIpv6GlobalAddressIpAddressType": zyIpv6GlobalAddressIpAddressType,
       "zyIpv6GlobalAddressIpAddress": zyIpv6GlobalAddressIpAddress,
       "zyIpv6GlobalAddressPrefixLength": zyIpv6GlobalAddressPrefixLength,
       "zyIpv6GlobalAddressEUI64State": zyIpv6GlobalAddressEUI64State,
       "zyIpv6GlobalAddressStatus": zyIpv6GlobalAddressStatus,
       "zyIpv6GlobalAddressRowStatus": zyIpv6GlobalAddressRowStatus}
)
