# SNMP MIB module (PDN-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:29 2024
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

(pdn_dns,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-dns")

(DNSServerType,
 DomainName) = mibBuilder.importSymbols(
    "PDN-TC",
    "DNSServerType",
    "DomainName")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDNSMIBObjects_ObjectIdentity = ObjectIdentity
pdnDNSMIBObjects = _PdnDNSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1)
)
_DevDNSDefaultDomainName_Type = DomainName
_DevDNSDefaultDomainName_Object = MibScalar
devDNSDefaultDomainName = _DevDNSDefaultDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 1),
    _DevDNSDefaultDomainName_Type()
)
devDNSDefaultDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDNSDefaultDomainName.setStatus("mandatory")
_DevDNSRetryTimeout_Type = Integer32
_DevDNSRetryTimeout_Object = MibScalar
devDNSRetryTimeout = _DevDNSRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 2),
    _DevDNSRetryTimeout_Type()
)
devDNSRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDNSRetryTimeout.setStatus("mandatory")
_DevDNSMaxRetries_Type = Integer32
_DevDNSMaxRetries_Object = MibScalar
devDNSMaxRetries = _DevDNSMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 3),
    _DevDNSMaxRetries_Type()
)
devDNSMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDNSMaxRetries.setStatus("mandatory")
_DevDNSServerTable_Object = MibTable
devDNSServerTable = _DevDNSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4)
)
if mibBuilder.loadTexts:
    devDNSServerTable.setStatus("mandatory")
_DevDNSServerEntry_Object = MibTableRow
devDNSServerEntry = _DevDNSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1)
)
devDNSServerEntry.setIndexNames(
    (0, "PDN-DNS-MIB", "devDNSServerIP"),
)
if mibBuilder.loadTexts:
    devDNSServerEntry.setStatus("mandatory")
_DevDNSServerIP_Type = IpAddress
_DevDNSServerIP_Object = MibTableColumn
devDNSServerIP = _DevDNSServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 1),
    _DevDNSServerIP_Type()
)
devDNSServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDNSServerIP.setStatus("mandatory")
_DevDNSServerType_Type = DNSServerType
_DevDNSServerType_Object = MibTableColumn
devDNSServerType = _DevDNSServerType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 2),
    _DevDNSServerType_Type()
)
devDNSServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDNSServerType.setStatus("mandatory")
_DevDNSRowStatus_Type = RowStatus
_DevDNSRowStatus_Object = MibTableColumn
devDNSRowStatus = _DevDNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 4, 1, 3),
    _DevDNSRowStatus_Type()
)
devDNSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDNSRowStatus.setStatus("mandatory")
_DevHostMappingTable_Object = MibTable
devHostMappingTable = _DevHostMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5)
)
if mibBuilder.loadTexts:
    devHostMappingTable.setStatus("mandatory")
_DevHostMappingEntry_Object = MibTableRow
devHostMappingEntry = _DevHostMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1)
)
devHostMappingEntry.setIndexNames(
    (0, "PDN-DNS-MIB", "devHostMappingIpAddress"),
)
if mibBuilder.loadTexts:
    devHostMappingEntry.setStatus("mandatory")
_DevHostMappingIpAddress_Type = IpAddress
_DevHostMappingIpAddress_Object = MibTableColumn
devHostMappingIpAddress = _DevHostMappingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 1),
    _DevHostMappingIpAddress_Type()
)
devHostMappingIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devHostMappingIpAddress.setStatus("mandatory")


class _DevHostMappingHostName_Type(DisplayString):
    """Custom type devHostMappingHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DevHostMappingHostName_Type.__name__ = "DisplayString"
_DevHostMappingHostName_Object = MibTableColumn
devHostMappingHostName = _DevHostMappingHostName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 2),
    _DevHostMappingHostName_Type()
)
devHostMappingHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devHostMappingHostName.setStatus("mandatory")
_DevHostMappingRowStatus_Type = RowStatus
_DevHostMappingRowStatus_Object = MibTableColumn
devHostMappingRowStatus = _DevHostMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 1, 5, 1, 3),
    _DevHostMappingRowStatus_Type()
)
devHostMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devHostMappingRowStatus.setStatus("mandatory")
_PdnDNSMIBTraps_ObjectIdentity = ObjectIdentity
pdnDNSMIBTraps = _PdnDNSMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 17, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DNS-MIB",
    **{"pdnDNSMIBObjects": pdnDNSMIBObjects,
       "devDNSDefaultDomainName": devDNSDefaultDomainName,
       "devDNSRetryTimeout": devDNSRetryTimeout,
       "devDNSMaxRetries": devDNSMaxRetries,
       "devDNSServerTable": devDNSServerTable,
       "devDNSServerEntry": devDNSServerEntry,
       "devDNSServerIP": devDNSServerIP,
       "devDNSServerType": devDNSServerType,
       "devDNSRowStatus": devDNSRowStatus,
       "devHostMappingTable": devHostMappingTable,
       "devHostMappingEntry": devHostMappingEntry,
       "devHostMappingIpAddress": devHostMappingIpAddress,
       "devHostMappingHostName": devHostMappingHostName,
       "devHostMappingRowStatus": devHostMappingRowStatus,
       "pdnDNSMIBTraps": pdnDNSMIBTraps}
)
