# SNMP MIB module (H3C-IPV6-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-IPV6-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:45 2024
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


# MODULE-IDENTITY

h3cIpv6AddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71)
)
h3cIpv6AddrMIB.setRevisions(
        ("2006-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIpv6AddressObjects_ObjectIdentity = ObjectIdentity
h3cIpv6AddressObjects = _H3cIpv6AddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1)
)
_H3cIpv6AddressConfig_ObjectIdentity = ObjectIdentity
h3cIpv6AddressConfig = _H3cIpv6AddressConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1)
)
_H3cIpv6AddrSetTable_Object = MibTable
h3cIpv6AddrSetTable = _H3cIpv6AddrSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIpv6AddrSetTable.setStatus("current")
_H3cIpv6AddrSetEntry_Object = MibTableRow
h3cIpv6AddrSetEntry = _H3cIpv6AddrSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1)
)
h3cIpv6AddrSetEntry.setIndexNames(
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrSetIfIndex"),
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrSetAddrType"),
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrSetAddr"),
)
if mibBuilder.loadTexts:
    h3cIpv6AddrSetEntry.setStatus("current")


class _H3cIpv6AddrSetIfIndex_Type(Integer32):
    """Custom type h3cIpv6AddrSetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpv6AddrSetIfIndex_Type.__name__ = "Integer32"
_H3cIpv6AddrSetIfIndex_Object = MibTableColumn
h3cIpv6AddrSetIfIndex = _H3cIpv6AddrSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 1),
    _H3cIpv6AddrSetIfIndex_Type()
)
h3cIpv6AddrSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetIfIndex.setStatus("current")
_H3cIpv6AddrSetAddrType_Type = InetAddressType
_H3cIpv6AddrSetAddrType_Object = MibTableColumn
h3cIpv6AddrSetAddrType = _H3cIpv6AddrSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 2),
    _H3cIpv6AddrSetAddrType_Type()
)
h3cIpv6AddrSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetAddrType.setStatus("current")
_H3cIpv6AddrSetAddr_Type = InetAddress
_H3cIpv6AddrSetAddr_Object = MibTableColumn
h3cIpv6AddrSetAddr = _H3cIpv6AddrSetAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 3),
    _H3cIpv6AddrSetAddr_Type()
)
h3cIpv6AddrSetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetAddr.setStatus("current")


class _H3cIpv6AddrSetPfxLength_Type(Integer32):
    """Custom type h3cIpv6AddrSetPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_H3cIpv6AddrSetPfxLength_Type.__name__ = "Integer32"
_H3cIpv6AddrSetPfxLength_Object = MibTableColumn
h3cIpv6AddrSetPfxLength = _H3cIpv6AddrSetPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 4),
    _H3cIpv6AddrSetPfxLength_Type()
)
h3cIpv6AddrSetPfxLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetPfxLength.setStatus("current")


class _H3cIpv6AddrSetSourceType_Type(Integer32):
    """Custom type h3cIpv6AddrSetSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assignedEUI64Ip", 2),
          ("assignedIp", 1),
          ("assignedLinklocalIp", 3))
    )


_H3cIpv6AddrSetSourceType_Type.__name__ = "Integer32"
_H3cIpv6AddrSetSourceType_Object = MibTableColumn
h3cIpv6AddrSetSourceType = _H3cIpv6AddrSetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 5),
    _H3cIpv6AddrSetSourceType_Type()
)
h3cIpv6AddrSetSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetSourceType.setStatus("current")
_H3cIpv6AddrSetRowStatus_Type = RowStatus
_H3cIpv6AddrSetRowStatus_Object = MibTableColumn
h3cIpv6AddrSetRowStatus = _H3cIpv6AddrSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 1, 1, 6),
    _H3cIpv6AddrSetRowStatus_Type()
)
h3cIpv6AddrSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv6AddrSetRowStatus.setStatus("current")
_H3cIpv6AddrReadTable_Object = MibTable
h3cIpv6AddrReadTable = _H3cIpv6AddrReadTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIpv6AddrReadTable.setStatus("current")
_H3cIpv6AddrReadEntry_Object = MibTableRow
h3cIpv6AddrReadEntry = _H3cIpv6AddrReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1)
)
h3cIpv6AddrReadEntry.setIndexNames(
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrReadIfIndex"),
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrReadAddrType"),
    (0, "H3C-IPV6-ADDRESS-MIB", "h3cIpv6AddrReadAddr"),
)
if mibBuilder.loadTexts:
    h3cIpv6AddrReadEntry.setStatus("current")


class _H3cIpv6AddrReadIfIndex_Type(Integer32):
    """Custom type h3cIpv6AddrReadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpv6AddrReadIfIndex_Type.__name__ = "Integer32"
_H3cIpv6AddrReadIfIndex_Object = MibTableColumn
h3cIpv6AddrReadIfIndex = _H3cIpv6AddrReadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 1),
    _H3cIpv6AddrReadIfIndex_Type()
)
h3cIpv6AddrReadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadIfIndex.setStatus("current")
_H3cIpv6AddrReadAddrType_Type = InetAddressType
_H3cIpv6AddrReadAddrType_Object = MibTableColumn
h3cIpv6AddrReadAddrType = _H3cIpv6AddrReadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 2),
    _H3cIpv6AddrReadAddrType_Type()
)
h3cIpv6AddrReadAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadAddrType.setStatus("current")
_H3cIpv6AddrReadAddr_Type = InetAddress
_H3cIpv6AddrReadAddr_Object = MibTableColumn
h3cIpv6AddrReadAddr = _H3cIpv6AddrReadAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 3),
    _H3cIpv6AddrReadAddr_Type()
)
h3cIpv6AddrReadAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadAddr.setStatus("current")


class _H3cIpv6AddrReadPfxLength_Type(Integer32):
    """Custom type h3cIpv6AddrReadPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_H3cIpv6AddrReadPfxLength_Type.__name__ = "Integer32"
_H3cIpv6AddrReadPfxLength_Object = MibTableColumn
h3cIpv6AddrReadPfxLength = _H3cIpv6AddrReadPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 4),
    _H3cIpv6AddrReadPfxLength_Type()
)
h3cIpv6AddrReadPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadPfxLength.setStatus("current")


class _H3cIpv6AddrReadSourceType_Type(Integer32):
    """Custom type h3cIpv6AddrReadSourceType based on Integer32"""
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
        *(("assignedAutoIp", 3),
          ("assignedEUI64Ip", 2),
          ("assignedIp", 1),
          ("autoIp", 4),
          ("cluster", 7),
          ("dhcpv6", 5),
          ("negotiate", 6))
    )


_H3cIpv6AddrReadSourceType_Type.__name__ = "Integer32"
_H3cIpv6AddrReadSourceType_Object = MibTableColumn
h3cIpv6AddrReadSourceType = _H3cIpv6AddrReadSourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 5),
    _H3cIpv6AddrReadSourceType_Type()
)
h3cIpv6AddrReadSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadSourceType.setStatus("current")


class _H3cIpv6AddrReadCatalog_Type(Integer32):
    """Custom type h3cIpv6AddrReadCatalog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("global", 5),
          ("linklocal", 2),
          ("nodelocal", 1),
          ("orglocal", 4),
          ("sitelocal", 3))
    )


_H3cIpv6AddrReadCatalog_Type.__name__ = "Integer32"
_H3cIpv6AddrReadCatalog_Object = MibTableColumn
h3cIpv6AddrReadCatalog = _H3cIpv6AddrReadCatalog_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 71, 1, 1, 2, 1, 6),
    _H3cIpv6AddrReadCatalog_Type()
)
h3cIpv6AddrReadCatalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpv6AddrReadCatalog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-IPV6-ADDRESS-MIB",
    **{"h3cIpv6AddrMIB": h3cIpv6AddrMIB,
       "h3cIpv6AddressObjects": h3cIpv6AddressObjects,
       "h3cIpv6AddressConfig": h3cIpv6AddressConfig,
       "h3cIpv6AddrSetTable": h3cIpv6AddrSetTable,
       "h3cIpv6AddrSetEntry": h3cIpv6AddrSetEntry,
       "h3cIpv6AddrSetIfIndex": h3cIpv6AddrSetIfIndex,
       "h3cIpv6AddrSetAddrType": h3cIpv6AddrSetAddrType,
       "h3cIpv6AddrSetAddr": h3cIpv6AddrSetAddr,
       "h3cIpv6AddrSetPfxLength": h3cIpv6AddrSetPfxLength,
       "h3cIpv6AddrSetSourceType": h3cIpv6AddrSetSourceType,
       "h3cIpv6AddrSetRowStatus": h3cIpv6AddrSetRowStatus,
       "h3cIpv6AddrReadTable": h3cIpv6AddrReadTable,
       "h3cIpv6AddrReadEntry": h3cIpv6AddrReadEntry,
       "h3cIpv6AddrReadIfIndex": h3cIpv6AddrReadIfIndex,
       "h3cIpv6AddrReadAddrType": h3cIpv6AddrReadAddrType,
       "h3cIpv6AddrReadAddr": h3cIpv6AddrReadAddr,
       "h3cIpv6AddrReadPfxLength": h3cIpv6AddrReadPfxLength,
       "h3cIpv6AddrReadSourceType": h3cIpv6AddrReadSourceType,
       "h3cIpv6AddrReadCatalog": h3cIpv6AddrReadCatalog}
)
