# SNMP MIB module (FDRY-DNS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-DNS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:39 2024
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


# MODULE-IDENTITY

fdryDns2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34)
)
fdryDns2MIB.setRevisions(
        ("2010-06-02 00:00",
         "2009-01-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryDns2DomainName_ObjectIdentity = ObjectIdentity
fdryDns2DomainName = _FdryDns2DomainName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1)
)
_FdryDns2DomainNameTable_Object = MibTable
fdryDns2DomainNameTable = _FdryDns2DomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1)
)
if mibBuilder.loadTexts:
    fdryDns2DomainNameTable.setStatus("current")
_FdryDns2DomainNameEntry_Object = MibTableRow
fdryDns2DomainNameEntry = _FdryDns2DomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1, 1)
)
fdryDns2DomainNameEntry.setIndexNames(
    (0, "FDRY-DNS2-MIB", "fdryDns2DomainNameIndex"),
)
if mibBuilder.loadTexts:
    fdryDns2DomainNameEntry.setStatus("current")
_FdryDns2DomainNameIndex_Type = Unsigned32
_FdryDns2DomainNameIndex_Object = MibTableColumn
fdryDns2DomainNameIndex = _FdryDns2DomainNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1, 1, 1),
    _FdryDns2DomainNameIndex_Type()
)
fdryDns2DomainNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDns2DomainNameIndex.setStatus("current")


class _FdryDns2DomainNameAddrType_Type(InetAddressType):
    """Custom type fdryDns2DomainNameAddrType based on InetAddressType"""


_FdryDns2DomainNameAddrType_Object = MibTableColumn
fdryDns2DomainNameAddrType = _FdryDns2DomainNameAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1, 1, 2),
    _FdryDns2DomainNameAddrType_Type()
)
fdryDns2DomainNameAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDns2DomainNameAddrType.setStatus("current")


class _FdryDns2DomainNameName_Type(DisplayString):
    """Custom type fdryDns2DomainNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FdryDns2DomainNameName_Type.__name__ = "DisplayString"
_FdryDns2DomainNameName_Object = MibTableColumn
fdryDns2DomainNameName = _FdryDns2DomainNameName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1, 1, 3),
    _FdryDns2DomainNameName_Type()
)
fdryDns2DomainNameName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDns2DomainNameName.setStatus("current")
_FdryDns2DomainNameRowStatus_Type = RowStatus
_FdryDns2DomainNameRowStatus_Object = MibTableColumn
fdryDns2DomainNameRowStatus = _FdryDns2DomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 1, 1, 1, 4),
    _FdryDns2DomainNameRowStatus_Type()
)
fdryDns2DomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDns2DomainNameRowStatus.setStatus("current")
_FdryDnsServer_ObjectIdentity = ObjectIdentity
fdryDnsServer = _FdryDnsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2)
)
_FdryDnsServerTable_Object = MibTable
fdryDnsServerTable = _FdryDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1)
)
if mibBuilder.loadTexts:
    fdryDnsServerTable.setStatus("current")
_FdryDnsServerEntry_Object = MibTableRow
fdryDnsServerEntry = _FdryDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1, 1)
)
fdryDnsServerEntry.setIndexNames(
    (0, "FDRY-DNS2-MIB", "fdryDnsServerAddrType"),
    (0, "FDRY-DNS2-MIB", "fdryDnsServerIndex"),
)
if mibBuilder.loadTexts:
    fdryDnsServerEntry.setStatus("current")


class _FdryDnsServerAddrType_Type(InetAddressType):
    """Custom type fdryDnsServerAddrType based on InetAddressType"""


_FdryDnsServerAddrType_Object = MibTableColumn
fdryDnsServerAddrType = _FdryDnsServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1, 1, 1),
    _FdryDnsServerAddrType_Type()
)
fdryDnsServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDnsServerAddrType.setStatus("current")
_FdryDnsServerIndex_Type = Unsigned32
_FdryDnsServerIndex_Object = MibTableColumn
fdryDnsServerIndex = _FdryDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1, 1, 2),
    _FdryDnsServerIndex_Type()
)
fdryDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDnsServerIndex.setStatus("current")
_FdryDnsServerAddr_Type = InetAddress
_FdryDnsServerAddr_Object = MibTableColumn
fdryDnsServerAddr = _FdryDnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1, 1, 3),
    _FdryDnsServerAddr_Type()
)
fdryDnsServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDnsServerAddr.setStatus("current")
_FdryDnsServerRowStatus_Type = RowStatus
_FdryDnsServerRowStatus_Object = MibTableColumn
fdryDnsServerRowStatus = _FdryDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 34, 2, 1, 1, 4),
    _FdryDnsServerRowStatus_Type()
)
fdryDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDnsServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-DNS2-MIB",
    **{"fdryDns2MIB": fdryDns2MIB,
       "fdryDns2DomainName": fdryDns2DomainName,
       "fdryDns2DomainNameTable": fdryDns2DomainNameTable,
       "fdryDns2DomainNameEntry": fdryDns2DomainNameEntry,
       "fdryDns2DomainNameIndex": fdryDns2DomainNameIndex,
       "fdryDns2DomainNameAddrType": fdryDns2DomainNameAddrType,
       "fdryDns2DomainNameName": fdryDns2DomainNameName,
       "fdryDns2DomainNameRowStatus": fdryDns2DomainNameRowStatus,
       "fdryDnsServer": fdryDnsServer,
       "fdryDnsServerTable": fdryDnsServerTable,
       "fdryDnsServerEntry": fdryDnsServerEntry,
       "fdryDnsServerAddrType": fdryDnsServerAddrType,
       "fdryDnsServerIndex": fdryDnsServerIndex,
       "fdryDnsServerAddr": fdryDnsServerAddr,
       "fdryDnsServerRowStatus": fdryDnsServerRowStatus}
)
