# SNMP MIB module (WWP-DNS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-DNS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:37 2024
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpDnsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49)
)
wwpDnsClientMIB.setRevisions(
        ("2003-03-19 10:12",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpDnsClientMIBObjects_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBObjects = _WwpDnsClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1)
)
_WwpDnsClient_ObjectIdentity = ObjectIdentity
wwpDnsClient = _WwpDnsClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1)
)


class _WwpDnsResolverEnable_Type(TruthValue):
    """Custom type wwpDnsResolverEnable based on TruthValue"""


_WwpDnsResolverEnable_Object = MibScalar
wwpDnsResolverEnable = _WwpDnsResolverEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 1),
    _WwpDnsResolverEnable_Type()
)
wwpDnsResolverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDnsResolverEnable.setStatus("current")


class _WwpDnsDomainAdminName_Type(DisplayString):
    """Custom type wwpDnsDomainAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpDnsDomainAdminName_Type.__name__ = "DisplayString"
_WwpDnsDomainAdminName_Object = MibScalar
wwpDnsDomainAdminName = _WwpDnsDomainAdminName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 2),
    _WwpDnsDomainAdminName_Type()
)
wwpDnsDomainAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpDnsDomainAdminName.setStatus("current")


class _WwpDnsDomainOperName_Type(DisplayString):
    """Custom type wwpDnsDomainOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpDnsDomainOperName_Type.__name__ = "DisplayString"
_WwpDnsDomainOperName_Object = MibScalar
wwpDnsDomainOperName = _WwpDnsDomainOperName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 3),
    _WwpDnsDomainOperName_Type()
)
wwpDnsDomainOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDnsDomainOperName.setStatus("current")
_WwpDnsNameAdminServerTable_Object = MibTable
wwpDnsNameAdminServerTable = _WwpDnsNameAdminServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpDnsNameAdminServerTable.setStatus("current")
_WwpDnsNameAdminServerEntry_Object = MibTableRow
wwpDnsNameAdminServerEntry = _WwpDnsNameAdminServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 4, 1)
)
wwpDnsNameAdminServerEntry.setIndexNames(
    (0, "WWP-DNS-CLIENT-MIB", "wwpDnsAdminServerId"),
)
if mibBuilder.loadTexts:
    wwpDnsNameAdminServerEntry.setStatus("current")


class _WwpDnsAdminServerId_Type(Integer32):
    """Custom type wwpDnsAdminServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpDnsAdminServerId_Type.__name__ = "Integer32"
_WwpDnsAdminServerId_Object = MibTableColumn
wwpDnsAdminServerId = _WwpDnsAdminServerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 4, 1, 1),
    _WwpDnsAdminServerId_Type()
)
wwpDnsAdminServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDnsAdminServerId.setStatus("current")
_WwpDnsAdminServerAddr_Type = IpAddress
_WwpDnsAdminServerAddr_Object = MibTableColumn
wwpDnsAdminServerAddr = _WwpDnsAdminServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 4, 1, 2),
    _WwpDnsAdminServerAddr_Type()
)
wwpDnsAdminServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpDnsAdminServerAddr.setStatus("current")
_WwpDnsAdminServerStatus_Type = RowStatus
_WwpDnsAdminServerStatus_Object = MibTableColumn
wwpDnsAdminServerStatus = _WwpDnsAdminServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 4, 1, 3),
    _WwpDnsAdminServerStatus_Type()
)
wwpDnsAdminServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpDnsAdminServerStatus.setStatus("current")
_WwpDnsNameOperServerTable_Object = MibTable
wwpDnsNameOperServerTable = _WwpDnsNameOperServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpDnsNameOperServerTable.setStatus("current")
_WwpDnsNameOperServerEntry_Object = MibTableRow
wwpDnsNameOperServerEntry = _WwpDnsNameOperServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 5, 1)
)
wwpDnsNameOperServerEntry.setIndexNames(
    (0, "WWP-DNS-CLIENT-MIB", "wwpDnsOperServerId"),
)
if mibBuilder.loadTexts:
    wwpDnsNameOperServerEntry.setStatus("current")


class _WwpDnsOperServerId_Type(Integer32):
    """Custom type wwpDnsOperServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpDnsOperServerId_Type.__name__ = "Integer32"
_WwpDnsOperServerId_Object = MibTableColumn
wwpDnsOperServerId = _WwpDnsOperServerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 5, 1, 1),
    _WwpDnsOperServerId_Type()
)
wwpDnsOperServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDnsOperServerId.setStatus("current")
_WwpDnsOperServerAddr_Type = IpAddress
_WwpDnsOperServerAddr_Object = MibTableColumn
wwpDnsOperServerAddr = _WwpDnsOperServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 1, 1, 5, 1, 2),
    _WwpDnsOperServerAddr_Type()
)
wwpDnsOperServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpDnsOperServerAddr.setStatus("current")
_WwpDnsClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBNotificationPrefix = _WwpDnsClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 2)
)
_WwpDnsClientMIBNotifications_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBNotifications = _WwpDnsClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 2, 0)
)
_WwpDnsClientMIBConformance_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBConformance = _WwpDnsClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 3)
)
_WwpDnsClientMIBCompliances_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBCompliances = _WwpDnsClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 3, 1)
)
_WwpDnsClientMIBGroups_ObjectIdentity = ObjectIdentity
wwpDnsClientMIBGroups = _WwpDnsClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 49, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-DNS-CLIENT-MIB",
    **{"wwpDnsClientMIB": wwpDnsClientMIB,
       "wwpDnsClientMIBObjects": wwpDnsClientMIBObjects,
       "wwpDnsClient": wwpDnsClient,
       "wwpDnsResolverEnable": wwpDnsResolverEnable,
       "wwpDnsDomainAdminName": wwpDnsDomainAdminName,
       "wwpDnsDomainOperName": wwpDnsDomainOperName,
       "wwpDnsNameAdminServerTable": wwpDnsNameAdminServerTable,
       "wwpDnsNameAdminServerEntry": wwpDnsNameAdminServerEntry,
       "wwpDnsAdminServerId": wwpDnsAdminServerId,
       "wwpDnsAdminServerAddr": wwpDnsAdminServerAddr,
       "wwpDnsAdminServerStatus": wwpDnsAdminServerStatus,
       "wwpDnsNameOperServerTable": wwpDnsNameOperServerTable,
       "wwpDnsNameOperServerEntry": wwpDnsNameOperServerEntry,
       "wwpDnsOperServerId": wwpDnsOperServerId,
       "wwpDnsOperServerAddr": wwpDnsOperServerAddr,
       "wwpDnsClientMIBNotificationPrefix": wwpDnsClientMIBNotificationPrefix,
       "wwpDnsClientMIBNotifications": wwpDnsClientMIBNotifications,
       "wwpDnsClientMIBConformance": wwpDnsClientMIBConformance,
       "wwpDnsClientMIBCompliances": wwpDnsClientMIBCompliances,
       "wwpDnsClientMIBGroups": wwpDnsClientMIBGroups}
)
