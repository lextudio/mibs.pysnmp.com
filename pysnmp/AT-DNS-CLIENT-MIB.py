# SNMP MIB module (AT-DNS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-DNS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:02 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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

atDNSClient = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1)
)
atDNSClient.setRevisions(
        ("2010-06-14 04:45",
         "2008-09-18 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtDns_ObjectIdentity = ObjectIdentity
atDns = _AtDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501)
)
if mibBuilder.loadTexts:
    atDns.setStatus("current")


class _AtDNSServerIndexNext_Type(Integer32):
    """Custom type atDNSServerIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtDNSServerIndexNext_Type.__name__ = "Integer32"
_AtDNSServerIndexNext_Object = MibScalar
atDNSServerIndexNext = _AtDNSServerIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 1),
    _AtDNSServerIndexNext_Type()
)
atDNSServerIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDNSServerIndexNext.setStatus("current")
_AtDNSServerTable_Object = MibTable
atDNSServerTable = _AtDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2)
)
if mibBuilder.loadTexts:
    atDNSServerTable.setStatus("current")
_AtDNSServerEntry_Object = MibTableRow
atDNSServerEntry = _AtDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1)
)
atDNSServerEntry.setIndexNames(
    (0, "AT-DNS-CLIENT-MIB", "atDNSServerIndex"),
)
if mibBuilder.loadTexts:
    atDNSServerEntry.setStatus("current")


class _AtDNSServerIndex_Type(Integer32):
    """Custom type atDNSServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtDNSServerIndex_Type.__name__ = "Integer32"
_AtDNSServerIndex_Object = MibTableColumn
atDNSServerIndex = _AtDNSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 1),
    _AtDNSServerIndex_Type()
)
atDNSServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atDNSServerIndex.setStatus("current")


class _AtDNSServerAddrType_Type(InetAddressType):
    """Custom type atDNSServerAddrType based on InetAddressType"""


_AtDNSServerAddrType_Object = MibTableColumn
atDNSServerAddrType = _AtDNSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 2),
    _AtDNSServerAddrType_Type()
)
atDNSServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDNSServerAddrType.setStatus("current")


class _AtDNSServerAddr_Type(IpAddress):
    """Custom type atDNSServerAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AtDNSServerAddr_Object = MibTableColumn
atDNSServerAddr = _AtDNSServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 3),
    _AtDNSServerAddr_Type()
)
atDNSServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDNSServerAddr.setStatus("current")


class _AtDNSServerStatus_Type(RowStatus):
    """Custom type atDNSServerStatus based on RowStatus"""
    defaultValue = 1


_AtDNSServerStatus_Object = MibTableColumn
atDNSServerStatus = _AtDNSServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 501, 1, 2, 1, 4),
    _AtDNSServerStatus_Type()
)
atDNSServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atDNSServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-DNS-CLIENT-MIB",
    **{"atDns": atDns,
       "atDNSClient": atDNSClient,
       "atDNSServerIndexNext": atDNSServerIndexNext,
       "atDNSServerTable": atDNSServerTable,
       "atDNSServerEntry": atDNSServerEntry,
       "atDNSServerIndex": atDNSServerIndex,
       "atDNSServerAddrType": atDNSServerAddrType,
       "atDNSServerAddr": atDNSServerAddr,
       "atDNSServerStatus": atDNSServerStatus}
)
