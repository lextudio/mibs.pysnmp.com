# SNMP MIB module (TPLINK-IPV6ADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-IPV6ADDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:13 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkIpv6AddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50)
)
tplinkIpv6AddrMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkIpv6AddrMIBObjects_ObjectIdentity = ObjectIdentity
tplinkIpv6AddrMIBObjects = _TplinkIpv6AddrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1)
)
_Ipv6ParaConfigAddrTable_Object = MibTable
ipv6ParaConfigAddrTable = _Ipv6ParaConfigAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrTable.setStatus("current")
_Ipv6ParaConfigAddrEntry_Object = MibTableRow
ipv6ParaConfigAddrEntry = _Ipv6ParaConfigAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1)
)
ipv6ParaConfigAddrEntry.setIndexNames(
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigIfIndex"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigAddrType"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigSourceType"),
    (0, "TPLINK-IPV6ADDR-MIB", "ipv6ParaConfigAddress"),
)
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrEntry.setStatus("current")
_Ipv6ParaConfigIfIndex_Type = Integer32
_Ipv6ParaConfigIfIndex_Object = MibTableColumn
ipv6ParaConfigIfIndex = _Ipv6ParaConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 2),
    _Ipv6ParaConfigIfIndex_Type()
)
ipv6ParaConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigIfIndex.setStatus("current")
_Ipv6ParaConfigAddrType_Type = InetAddressType
_Ipv6ParaConfigAddrType_Object = MibTableColumn
ipv6ParaConfigAddrType = _Ipv6ParaConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 3),
    _Ipv6ParaConfigAddrType_Type()
)
ipv6ParaConfigAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigAddrType.setStatus("current")
_Ipv6ParaConfigAddress_Type = InetAddress
_Ipv6ParaConfigAddress_Object = MibTableColumn
ipv6ParaConfigAddress = _Ipv6ParaConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 4),
    _Ipv6ParaConfigAddress_Type()
)
ipv6ParaConfigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigAddress.setStatus("current")


class _Ipv6ParaConfigPrefixLength_Type(Integer32):
    """Custom type ipv6ParaConfigPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Ipv6ParaConfigPrefixLength_Type.__name__ = "Integer32"
_Ipv6ParaConfigPrefixLength_Object = MibTableColumn
ipv6ParaConfigPrefixLength = _Ipv6ParaConfigPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 5),
    _Ipv6ParaConfigPrefixLength_Type()
)
ipv6ParaConfigPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6ParaConfigPrefixLength.setStatus("current")


class _Ipv6ParaConfigSourceType_Type(Integer32):
    """Custom type ipv6ParaConfigSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("assignedEUI64Ip", 2),
          ("assignedIp", 1),
          ("assignedLinklocalIp", 3),
          ("autoIp", 4),
          ("dhcpv6", 5),
          ("negotiate", 6))
    )


_Ipv6ParaConfigSourceType_Type.__name__ = "Integer32"
_Ipv6ParaConfigSourceType_Object = MibTableColumn
ipv6ParaConfigSourceType = _Ipv6ParaConfigSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 6),
    _Ipv6ParaConfigSourceType_Type()
)
ipv6ParaConfigSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6ParaConfigSourceType.setStatus("current")
_Ipv6ParaConfigRowStatus_Type = RowStatus
_Ipv6ParaConfigRowStatus_Object = MibTableColumn
ipv6ParaConfigRowStatus = _Ipv6ParaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 1, 1, 1, 7),
    _Ipv6ParaConfigRowStatus_Type()
)
ipv6ParaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipv6ParaConfigRowStatus.setStatus("current")
_TplinkIpv6AddrNotifications_ObjectIdentity = ObjectIdentity
tplinkIpv6AddrNotifications = _TplinkIpv6AddrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 50, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-IPV6ADDR-MIB",
    **{"tplinkIpv6AddrMIB": tplinkIpv6AddrMIB,
       "tplinkIpv6AddrMIBObjects": tplinkIpv6AddrMIBObjects,
       "ipv6ParaConfigAddrTable": ipv6ParaConfigAddrTable,
       "ipv6ParaConfigAddrEntry": ipv6ParaConfigAddrEntry,
       "ipv6ParaConfigIfIndex": ipv6ParaConfigIfIndex,
       "ipv6ParaConfigAddrType": ipv6ParaConfigAddrType,
       "ipv6ParaConfigAddress": ipv6ParaConfigAddress,
       "ipv6ParaConfigPrefixLength": ipv6ParaConfigPrefixLength,
       "ipv6ParaConfigSourceType": ipv6ParaConfigSourceType,
       "ipv6ParaConfigRowStatus": ipv6ParaConfigRowStatus,
       "tplinkIpv6AddrNotifications": tplinkIpv6AddrNotifications}
)
