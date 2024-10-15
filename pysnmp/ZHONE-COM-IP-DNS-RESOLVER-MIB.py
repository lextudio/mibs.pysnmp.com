# SNMP MIB module (ZHONE-COM-IP-DNS-RESOLVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-IP-DNS-RESOLVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:13 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(rdEntry,
 rdIndex) = mibBuilder.importSymbols(
    "ZHONE-COM-IP-RD-MIB",
    "rdEntry",
    "rdIndex")

(zhoneIp,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp",
    "zhoneModules")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comIpDnsResolver = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 62)
)
comIpDnsResolver.setRevisions(
        ("1900-09-11 16:08",
         "1900-09-29 09:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnsResolver_ObjectIdentity = ObjectIdentity
dnsResolver = _DnsResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12)
)
if mibBuilder.loadTexts:
    dnsResolver.setStatus("current")
_ZhDnsResConfigImplementIdent_Type = ZhoneAdminString
_ZhDnsResConfigImplementIdent_Object = MibScalar
zhDnsResConfigImplementIdent = _ZhDnsResConfigImplementIdent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 1),
    _ZhDnsResConfigImplementIdent_Type()
)
zhDnsResConfigImplementIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhDnsResConfigImplementIdent.setStatus("current")
_ZhDnsResConfigTable_Object = MibTable
zhDnsResConfigTable = _ZhDnsResConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2)
)
if mibBuilder.loadTexts:
    zhDnsResConfigTable.setStatus("current")
_ZhDnsResConfigEntry_Object = MibTableRow
zhDnsResConfigEntry = _ZhDnsResConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    zhDnsResConfigEntry.setStatus("current")


class _ZhDnsResConfigQueryOrder_Type(Integer32):
    """Custom type zhDnsResConfigQueryOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dnsFirst", 2),
          ("dnsOnly", 3),
          ("hostsFirst", 1))
    )


_ZhDnsResConfigQueryOrder_Type.__name__ = "Integer32"
_ZhDnsResConfigQueryOrder_Object = MibTableColumn
zhDnsResConfigQueryOrder = _ZhDnsResConfigQueryOrder_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 1),
    _ZhDnsResConfigQueryOrder_Type()
)
zhDnsResConfigQueryOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhDnsResConfigQueryOrder.setStatus("current")
_ZhDnsResConfigDomainName_Type = SnmpAdminString
_ZhDnsResConfigDomainName_Object = MibTableColumn
zhDnsResConfigDomainName = _ZhDnsResConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 2),
    _ZhDnsResConfigDomainName_Type()
)
zhDnsResConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhDnsResConfigDomainName.setStatus("current")


class _ZhDnsResConfigFirstNameServer_Type(IpAddress):
    """Custom type zhDnsResConfigFirstNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_ZhDnsResConfigFirstNameServer_Object = MibTableColumn
zhDnsResConfigFirstNameServer = _ZhDnsResConfigFirstNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 3),
    _ZhDnsResConfigFirstNameServer_Type()
)
zhDnsResConfigFirstNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhDnsResConfigFirstNameServer.setStatus("current")


class _ZhDnsResConfigSecondNameServer_Type(IpAddress):
    """Custom type zhDnsResConfigSecondNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_ZhDnsResConfigSecondNameServer_Object = MibTableColumn
zhDnsResConfigSecondNameServer = _ZhDnsResConfigSecondNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 4),
    _ZhDnsResConfigSecondNameServer_Type()
)
zhDnsResConfigSecondNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhDnsResConfigSecondNameServer.setStatus("current")


class _ZhDnsResConfigThirdNameServer_Type(IpAddress):
    """Custom type zhDnsResConfigThirdNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_ZhDnsResConfigThirdNameServer_Object = MibTableColumn
zhDnsResConfigThirdNameServer = _ZhDnsResConfigThirdNameServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 2, 1, 5),
    _ZhDnsResConfigThirdNameServer_Type()
)
zhDnsResConfigThirdNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhDnsResConfigThirdNameServer.setStatus("current")
_ZhDnsResHostsTable_Object = MibTable
zhDnsResHostsTable = _ZhDnsResHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3)
)
if mibBuilder.loadTexts:
    zhDnsResHostsTable.setStatus("current")
_ZhDnsResHostsEntry_Object = MibTableRow
zhDnsResHostsEntry = _ZhDnsResHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1)
)
zhDnsResHostsEntry.setIndexNames(
    (0, "ZHONE-COM-IP-RD-MIB", "rdIndex"),
    (0, "ZHONE-COM-IP-DNS-RESOLVER-MIB", "zhDnsResHostsIpAddress"),
)
if mibBuilder.loadTexts:
    zhDnsResHostsEntry.setStatus("current")
_ZhDnsResHostsIpAddress_Type = IpAddress
_ZhDnsResHostsIpAddress_Object = MibTableColumn
zhDnsResHostsIpAddress = _ZhDnsResHostsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 1),
    _ZhDnsResHostsIpAddress_Type()
)
zhDnsResHostsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhDnsResHostsIpAddress.setStatus("current")
_ZhDnsResHostsName_Type = SnmpAdminString
_ZhDnsResHostsName_Object = MibTableColumn
zhDnsResHostsName = _ZhDnsResHostsName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 2),
    _ZhDnsResHostsName_Type()
)
zhDnsResHostsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsName.setStatus("current")
_ZhDnsResHostsAlias1_Type = SnmpAdminString
_ZhDnsResHostsAlias1_Object = MibTableColumn
zhDnsResHostsAlias1 = _ZhDnsResHostsAlias1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 3),
    _ZhDnsResHostsAlias1_Type()
)
zhDnsResHostsAlias1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsAlias1.setStatus("current")
_ZhDnsResHostsAlias2_Type = SnmpAdminString
_ZhDnsResHostsAlias2_Object = MibTableColumn
zhDnsResHostsAlias2 = _ZhDnsResHostsAlias2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 4),
    _ZhDnsResHostsAlias2_Type()
)
zhDnsResHostsAlias2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsAlias2.setStatus("current")
_ZhDnsResHostsAlias3_Type = SnmpAdminString
_ZhDnsResHostsAlias3_Object = MibTableColumn
zhDnsResHostsAlias3 = _ZhDnsResHostsAlias3_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 5),
    _ZhDnsResHostsAlias3_Type()
)
zhDnsResHostsAlias3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsAlias3.setStatus("current")
_ZhDnsResHostsAlias4_Type = SnmpAdminString
_ZhDnsResHostsAlias4_Object = MibTableColumn
zhDnsResHostsAlias4 = _ZhDnsResHostsAlias4_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 6),
    _ZhDnsResHostsAlias4_Type()
)
zhDnsResHostsAlias4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsAlias4.setStatus("current")


class _ZhDnsResHostsRowStatus_Type(ZhoneRowStatus):
    """Custom type zhDnsResHostsRowStatus based on ZhoneRowStatus"""


_ZhDnsResHostsRowStatus_Object = MibTableColumn
zhDnsResHostsRowStatus = _ZhDnsResHostsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 12, 3, 1, 7),
    _ZhDnsResHostsRowStatus_Type()
)
zhDnsResHostsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zhDnsResHostsRowStatus.setStatus("current")
rdEntry.registerAugmentions(
    ("ZHONE-COM-IP-DNS-RESOLVER-MIB",
     "zhDnsResConfigEntry")
)
zhDnsResConfigEntry.setIndexNames(*rdEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-IP-DNS-RESOLVER-MIB",
    **{"dnsResolver": dnsResolver,
       "zhDnsResConfigImplementIdent": zhDnsResConfigImplementIdent,
       "zhDnsResConfigTable": zhDnsResConfigTable,
       "zhDnsResConfigEntry": zhDnsResConfigEntry,
       "zhDnsResConfigQueryOrder": zhDnsResConfigQueryOrder,
       "zhDnsResConfigDomainName": zhDnsResConfigDomainName,
       "zhDnsResConfigFirstNameServer": zhDnsResConfigFirstNameServer,
       "zhDnsResConfigSecondNameServer": zhDnsResConfigSecondNameServer,
       "zhDnsResConfigThirdNameServer": zhDnsResConfigThirdNameServer,
       "zhDnsResHostsTable": zhDnsResHostsTable,
       "zhDnsResHostsEntry": zhDnsResHostsEntry,
       "zhDnsResHostsIpAddress": zhDnsResHostsIpAddress,
       "zhDnsResHostsName": zhDnsResHostsName,
       "zhDnsResHostsAlias1": zhDnsResHostsAlias1,
       "zhDnsResHostsAlias2": zhDnsResHostsAlias2,
       "zhDnsResHostsAlias3": zhDnsResHostsAlias3,
       "zhDnsResHostsAlias4": zhDnsResHostsAlias4,
       "zhDnsResHostsRowStatus": zhDnsResHostsRowStatus,
       "comIpDnsResolver": comIpDnsResolver}
)
