# SNMP MIB module (CADANT-CMTS-DNSCLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-DNSCLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:26 2024
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

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadDnsClientMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8)
)
cadDnsClientMib.setRevisions(
        ("2003-07-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadDnsClientObjects_ObjectIdentity = ObjectIdentity
cadDnsClientObjects = _CadDnsClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1)
)


class _CadDnsClientEnable_Type(TruthValue):
    """Custom type cadDnsClientEnable based on TruthValue"""


_CadDnsClientEnable_Object = MibScalar
cadDnsClientEnable = _CadDnsClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1, 1),
    _CadDnsClientEnable_Type()
)
cadDnsClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDnsClientEnable.setStatus("current")
_CadDnsClientDefaultDomain_Type = DisplayString
_CadDnsClientDefaultDomain_Object = MibScalar
cadDnsClientDefaultDomain = _CadDnsClientDefaultDomain_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 1, 2),
    _CadDnsClientDefaultDomain_Type()
)
cadDnsClientDefaultDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadDnsClientDefaultDomain.setStatus("current")
_CadDnsClientServerTable_Object = MibTable
cadDnsClientServerTable = _CadDnsClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2)
)
if mibBuilder.loadTexts:
    cadDnsClientServerTable.setStatus("current")
_CadDnsClientServerEntry_Object = MibTableRow
cadDnsClientServerEntry = _CadDnsClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1)
)
cadDnsClientServerEntry.setIndexNames(
    (0, "CADANT-CMTS-DNSCLIENT-MIB", "cadDnsClientServerIpAddr"),
)
if mibBuilder.loadTexts:
    cadDnsClientServerEntry.setStatus("current")
_CadDnsClientServerIpAddr_Type = IpAddress
_CadDnsClientServerIpAddr_Object = MibTableColumn
cadDnsClientServerIpAddr = _CadDnsClientServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 1),
    _CadDnsClientServerIpAddr_Type()
)
cadDnsClientServerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDnsClientServerIpAddr.setStatus("current")


class _CadDnsClientServerPrefId_Type(Integer32):
    """Custom type cadDnsClientServerPrefId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CadDnsClientServerPrefId_Type.__name__ = "Integer32"
_CadDnsClientServerPrefId_Object = MibTableColumn
cadDnsClientServerPrefId = _CadDnsClientServerPrefId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 2),
    _CadDnsClientServerPrefId_Type()
)
cadDnsClientServerPrefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadDnsClientServerPrefId.setStatus("current")
_CadDnsClientServerRowStatus_Type = RowStatus
_CadDnsClientServerRowStatus_Object = MibTableColumn
cadDnsClientServerRowStatus = _CadDnsClientServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 2, 1, 3),
    _CadDnsClientServerRowStatus_Type()
)
cadDnsClientServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDnsClientServerRowStatus.setStatus("current")
_CadDnsClientDomainNameTable_Object = MibTable
cadDnsClientDomainNameTable = _CadDnsClientDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3)
)
if mibBuilder.loadTexts:
    cadDnsClientDomainNameTable.setStatus("current")
_CadDnsClientDomainNameEntry_Object = MibTableRow
cadDnsClientDomainNameEntry = _CadDnsClientDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1)
)
cadDnsClientDomainNameEntry.setIndexNames(
    (0, "CADANT-CMTS-DNSCLIENT-MIB", "cadDnsClientDomainName"),
)
if mibBuilder.loadTexts:
    cadDnsClientDomainNameEntry.setStatus("current")
_CadDnsClientDomainName_Type = DisplayString
_CadDnsClientDomainName_Object = MibTableColumn
cadDnsClientDomainName = _CadDnsClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1, 1),
    _CadDnsClientDomainName_Type()
)
cadDnsClientDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadDnsClientDomainName.setStatus("current")
_CadDnsClientDomainNameRowStatus_Type = RowStatus
_CadDnsClientDomainNameRowStatus_Object = MibTableColumn
cadDnsClientDomainNameRowStatus = _CadDnsClientDomainNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 8, 3, 1, 2),
    _CadDnsClientDomainNameRowStatus_Type()
)
cadDnsClientDomainNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadDnsClientDomainNameRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-DNSCLIENT-MIB",
    **{"cadDnsClientMib": cadDnsClientMib,
       "cadDnsClientObjects": cadDnsClientObjects,
       "cadDnsClientEnable": cadDnsClientEnable,
       "cadDnsClientDefaultDomain": cadDnsClientDefaultDomain,
       "cadDnsClientServerTable": cadDnsClientServerTable,
       "cadDnsClientServerEntry": cadDnsClientServerEntry,
       "cadDnsClientServerIpAddr": cadDnsClientServerIpAddr,
       "cadDnsClientServerPrefId": cadDnsClientServerPrefId,
       "cadDnsClientServerRowStatus": cadDnsClientServerRowStatus,
       "cadDnsClientDomainNameTable": cadDnsClientDomainNameTable,
       "cadDnsClientDomainNameEntry": cadDnsClientDomainNameEntry,
       "cadDnsClientDomainName": cadDnsClientDomainName,
       "cadDnsClientDomainNameRowStatus": cadDnsClientDomainNameRowStatus}
)
