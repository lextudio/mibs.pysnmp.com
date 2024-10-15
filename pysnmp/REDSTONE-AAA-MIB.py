# SNMP MIB module (REDSTONE-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:31 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsName,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsName")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rsAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20)
)
rsAaaMIB.setRevisions(
        ("1999-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsAaaDomainName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



# MIB Managed Objects in the order of their OIDs

_RsAaaObjects_ObjectIdentity = ObjectIdentity
rsAaaObjects = _RsAaaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1)
)
_RsAaaAssignment_ObjectIdentity = ObjectIdentity
rsAaaAssignment = _RsAaaAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1)
)
_RsAaaAssignGeneral_ObjectIdentity = ObjectIdentity
rsAaaAssignGeneral = _RsAaaAssignGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 1)
)


class _RsAaaAssignBrasLicense_Type(DisplayString):
    """Custom type rsAaaAssignBrasLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RsAaaAssignBrasLicense_Type.__name__ = "DisplayString"
_RsAaaAssignBrasLicense_Object = MibScalar
rsAaaAssignBrasLicense = _RsAaaAssignBrasLicense_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 1, 1),
    _RsAaaAssignBrasLicense_Type()
)
rsAaaAssignBrasLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAssignBrasLicense.setStatus("current")
_RsAaaAssignBrasLicensedUsers_Type = Integer32
_RsAaaAssignBrasLicensedUsers_Object = MibScalar
rsAaaAssignBrasLicensedUsers = _RsAaaAssignBrasLicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 1, 2),
    _RsAaaAssignBrasLicensedUsers_Type()
)
rsAaaAssignBrasLicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAaaAssignBrasLicensedUsers.setStatus("current")
_RsAaaAssignDomain_ObjectIdentity = ObjectIdentity
rsAaaAssignDomain = _RsAaaAssignDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2)
)
_RsAaaAssignDomainTable_Object = MibTable
rsAaaAssignDomainTable = _RsAaaAssignDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsAaaAssignDomainTable.setStatus("current")
_RsAaaAssignDomainEntry_Object = MibTableRow
rsAaaAssignDomainEntry = _RsAaaAssignDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1, 1)
)
rsAaaAssignDomainEntry.setIndexNames(
    (1, "REDSTONE-AAA-MIB", "rsAaaAssignDomainName"),
)
if mibBuilder.loadTexts:
    rsAaaAssignDomainEntry.setStatus("current")
_RsAaaAssignDomainName_Type = RsAaaDomainName
_RsAaaAssignDomainName_Object = MibTableColumn
rsAaaAssignDomainName = _RsAaaAssignDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1, 1, 1),
    _RsAaaAssignDomainName_Type()
)
rsAaaAssignDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAaaAssignDomainName.setStatus("current")
_RsAaaAssignDomainRowStatus_Type = RowStatus
_RsAaaAssignDomainRowStatus_Object = MibTableColumn
rsAaaAssignDomainRowStatus = _RsAaaAssignDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1, 1, 2),
    _RsAaaAssignDomainRowStatus_Type()
)
rsAaaAssignDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAaaAssignDomainRowStatus.setStatus("current")
_RsAaaAssignDomainRouterName_Type = RsName
_RsAaaAssignDomainRouterName_Object = MibTableColumn
rsAaaAssignDomainRouterName = _RsAaaAssignDomainRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1, 1, 3),
    _RsAaaAssignDomainRouterName_Type()
)
rsAaaAssignDomainRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAaaAssignDomainRouterName.setStatus("current")


class _RsAaaAssignDomainLoopback_Type(Integer32):
    """Custom type rsAaaAssignDomainLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32000),
    )


_RsAaaAssignDomainLoopback_Type.__name__ = "Integer32"
_RsAaaAssignDomainLoopback_Object = MibTableColumn
rsAaaAssignDomainLoopback = _RsAaaAssignDomainLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 1, 2, 1, 1, 4),
    _RsAaaAssignDomainLoopback_Type()
)
rsAaaAssignDomainLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAaaAssignDomainLoopback.setStatus("current")
_RsAaaAuthentication_ObjectIdentity = ObjectIdentity
rsAaaAuthentication = _RsAaaAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 2)
)
_RsAaaAuthGeneral_ObjectIdentity = ObjectIdentity
rsAaaAuthGeneral = _RsAaaAuthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 2, 1)
)
_RsAaaAccounting_ObjectIdentity = ObjectIdentity
rsAaaAccounting = _RsAaaAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 3)
)
_RsAaaAcctGeneral_ObjectIdentity = ObjectIdentity
rsAaaAcctGeneral = _RsAaaAcctGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 3, 1)
)


class _RsAaaAcctInterval_Type(Integer32):
    """Custom type rsAaaAcctInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 64800),
    )


_RsAaaAcctInterval_Type.__name__ = "Integer32"
_RsAaaAcctInterval_Object = MibScalar
rsAaaAcctInterval = _RsAaaAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 3, 1, 1),
    _RsAaaAcctInterval_Type()
)
rsAaaAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsAaaAcctInterval.setUnits("seconds")
_RsAaaAcctDupServerRouterName_Type = RsName
_RsAaaAcctDupServerRouterName_Object = MibScalar
rsAaaAcctDupServerRouterName = _RsAaaAcctDupServerRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 3, 1, 2),
    _RsAaaAcctDupServerRouterName_Type()
)
rsAaaAcctDupServerRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAcctDupServerRouterName.setStatus("current")
_RsAaaAddress_ObjectIdentity = ObjectIdentity
rsAaaAddress = _RsAaaAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4)
)
_RsAaaAddrGeneral_ObjectIdentity = ObjectIdentity
rsAaaAddrGeneral = _RsAaaAddrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 1)
)


class _RsAaaAddrPoolDefault_Type(Integer32):
    """Custom type rsAaaAddrPoolDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 0))
    )


_RsAaaAddrPoolDefault_Type.__name__ = "Integer32"
_RsAaaAddrPoolDefault_Object = MibScalar
rsAaaAddrPoolDefault = _RsAaaAddrPoolDefault_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 1, 1),
    _RsAaaAddrPoolDefault_Type()
)
rsAaaAddrPoolDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAddrPoolDefault.setStatus("current")
_RsAaaAddrNameServer_ObjectIdentity = ObjectIdentity
rsAaaAddrNameServer = _RsAaaAddrNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2)
)
_RsAaaAddrDns_ObjectIdentity = ObjectIdentity
rsAaaAddrDns = _RsAaaAddrDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 1)
)
_RsAaaAddrDnsPrimary_Type = IpAddress
_RsAaaAddrDnsPrimary_Object = MibScalar
rsAaaAddrDnsPrimary = _RsAaaAddrDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 1, 1),
    _RsAaaAddrDnsPrimary_Type()
)
rsAaaAddrDnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAddrDnsPrimary.setStatus("current")
_RsAaaAddrDnsSecondary_Type = IpAddress
_RsAaaAddrDnsSecondary_Object = MibScalar
rsAaaAddrDnsSecondary = _RsAaaAddrDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 1, 2),
    _RsAaaAddrDnsSecondary_Type()
)
rsAaaAddrDnsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAddrDnsSecondary.setStatus("current")
_RsAaaAddrWins_ObjectIdentity = ObjectIdentity
rsAaaAddrWins = _RsAaaAddrWins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 2)
)
_RsAaaAddrWinsPrimary_Type = IpAddress
_RsAaaAddrWinsPrimary_Object = MibScalar
rsAaaAddrWinsPrimary = _RsAaaAddrWinsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 2, 1),
    _RsAaaAddrWinsPrimary_Type()
)
rsAaaAddrWinsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAddrWinsPrimary.setStatus("current")
_RsAaaAddrWinsSecondary_Type = IpAddress
_RsAaaAddrWinsSecondary_Object = MibScalar
rsAaaAddrWinsSecondary = _RsAaaAddrWinsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 1, 4, 2, 2, 2),
    _RsAaaAddrWinsSecondary_Type()
)
rsAaaAddrWinsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAaaAddrWinsSecondary.setStatus("current")
_RsAaaMIBConformance_ObjectIdentity = ObjectIdentity
rsAaaMIBConformance = _RsAaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 4)
)
_RsAaaMIBCompliances_ObjectIdentity = ObjectIdentity
rsAaaMIBCompliances = _RsAaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 4, 1)
)
_RsAaaMIBGroups_ObjectIdentity = ObjectIdentity
rsAaaMIBGroups = _RsAaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 4, 2)
)

# Managed Objects groups

rsAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 4, 2, 1)
)
rsAaaGroup.setObjects(
      *(("REDSTONE-AAA-MIB", "rsAaaAssignBrasLicense"),
        ("REDSTONE-AAA-MIB", "rsAaaAssignBrasLicensedUsers"),
        ("REDSTONE-AAA-MIB", "rsAaaAssignDomainName"),
        ("REDSTONE-AAA-MIB", "rsAaaAssignDomainRowStatus"),
        ("REDSTONE-AAA-MIB", "rsAaaAssignDomainRouterName"),
        ("REDSTONE-AAA-MIB", "rsAaaAssignDomainLoopback"),
        ("REDSTONE-AAA-MIB", "rsAaaAcctInterval"),
        ("REDSTONE-AAA-MIB", "rsAaaAcctDupServerRouterName"),
        ("REDSTONE-AAA-MIB", "rsAaaAddrPoolDefault"),
        ("REDSTONE-AAA-MIB", "rsAaaAddrDnsPrimary"),
        ("REDSTONE-AAA-MIB", "rsAaaAddrDnsSecondary"),
        ("REDSTONE-AAA-MIB", "rsAaaAddrWinsPrimary"),
        ("REDSTONE-AAA-MIB", "rsAaaAddrWinsSecondary"))
)
if mibBuilder.loadTexts:
    rsAaaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsAaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 20, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsAaaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-AAA-MIB",
    **{"RsAaaDomainName": RsAaaDomainName,
       "rsAaaMIB": rsAaaMIB,
       "rsAaaObjects": rsAaaObjects,
       "rsAaaAssignment": rsAaaAssignment,
       "rsAaaAssignGeneral": rsAaaAssignGeneral,
       "rsAaaAssignBrasLicense": rsAaaAssignBrasLicense,
       "rsAaaAssignBrasLicensedUsers": rsAaaAssignBrasLicensedUsers,
       "rsAaaAssignDomain": rsAaaAssignDomain,
       "rsAaaAssignDomainTable": rsAaaAssignDomainTable,
       "rsAaaAssignDomainEntry": rsAaaAssignDomainEntry,
       "rsAaaAssignDomainName": rsAaaAssignDomainName,
       "rsAaaAssignDomainRowStatus": rsAaaAssignDomainRowStatus,
       "rsAaaAssignDomainRouterName": rsAaaAssignDomainRouterName,
       "rsAaaAssignDomainLoopback": rsAaaAssignDomainLoopback,
       "rsAaaAuthentication": rsAaaAuthentication,
       "rsAaaAuthGeneral": rsAaaAuthGeneral,
       "rsAaaAccounting": rsAaaAccounting,
       "rsAaaAcctGeneral": rsAaaAcctGeneral,
       "rsAaaAcctInterval": rsAaaAcctInterval,
       "rsAaaAcctDupServerRouterName": rsAaaAcctDupServerRouterName,
       "rsAaaAddress": rsAaaAddress,
       "rsAaaAddrGeneral": rsAaaAddrGeneral,
       "rsAaaAddrPoolDefault": rsAaaAddrPoolDefault,
       "rsAaaAddrNameServer": rsAaaAddrNameServer,
       "rsAaaAddrDns": rsAaaAddrDns,
       "rsAaaAddrDnsPrimary": rsAaaAddrDnsPrimary,
       "rsAaaAddrDnsSecondary": rsAaaAddrDnsSecondary,
       "rsAaaAddrWins": rsAaaAddrWins,
       "rsAaaAddrWinsPrimary": rsAaaAddrWinsPrimary,
       "rsAaaAddrWinsSecondary": rsAaaAddrWinsSecondary,
       "rsAaaMIBConformance": rsAaaMIBConformance,
       "rsAaaMIBCompliances": rsAaaMIBCompliances,
       "rsAaaCompliance": rsAaaCompliance,
       "rsAaaMIBGroups": rsAaaMIBGroups,
       "rsAaaGroup": rsAaaGroup}
)
