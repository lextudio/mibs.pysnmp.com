# SNMP MIB module (NT-ENTERPRISE-DATA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NT-ENTERPRISE-DATA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:58 2024
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

(nortel,) = mibBuilder.importSymbols(
    "NORTEL-MIB",
    "nortel")

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


# MODULE-IDENTITY

ntEnterpriseData = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73)
)
ntEnterpriseData.setRevisions(
        ("2008-10-13 00:00",
         "2008-02-25 00:00",
         "2007-06-01 00:00",
         "2007-03-15 00:00",
         "2006-02-07 00:00",
         "2006-02-01 00:00",
         "2006-01-25 00:00",
         "2006-01-18 00:00",
         "2005-11-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtEnterpriseDataMibs_ObjectIdentity = ObjectIdentity
ntEnterpriseDataMibs = _NtEnterpriseDataMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1)
)
_NtEnterpriseDataTasmanMibs_ObjectIdentity = ObjectIdentity
ntEnterpriseDataTasmanMibs = _NtEnterpriseDataTasmanMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1)
)
_NtEnterpriseDataTasmanMgmt_ObjectIdentity = ObjectIdentity
ntEnterpriseDataTasmanMgmt = _NtEnterpriseDataTasmanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1)
)
_NtEnterpriseDataTasmanInterfaces_ObjectIdentity = ObjectIdentity
ntEnterpriseDataTasmanInterfaces = _NtEnterpriseDataTasmanInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2)
)
_NtEnterpriseDataTasmanModules_ObjectIdentity = ObjectIdentity
ntEnterpriseDataTasmanModules = _NtEnterpriseDataTasmanModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3)
)
_NtEnterpriseDataNewburyMibs_ObjectIdentity = ObjectIdentity
ntEnterpriseDataNewburyMibs = _NtEnterpriseDataNewburyMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 2)
)
_NtEnterpriseDataRegistration_ObjectIdentity = ObjectIdentity
ntEnterpriseDataRegistration = _NtEnterpriseDataRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2)
)
_NtEnterpriseSwitches_ObjectIdentity = ObjectIdentity
ntEnterpriseSwitches = _NtEnterpriseSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 1)
)
_NtEthernetSwitch_ObjectIdentity = ObjectIdentity
ntEthernetSwitch = _NtEthernetSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 1, 1)
)
_NtEthernetRoutingSwitch_ObjectIdentity = ObjectIdentity
ntEthernetRoutingSwitch = _NtEthernetRoutingSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 1, 2)
)
_NtEnterpriseRouters_ObjectIdentity = ObjectIdentity
ntEnterpriseRouters = _NtEnterpriseRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2)
)
_NtSecureRouter6200Series_ObjectIdentity = ObjectIdentity
ntSecureRouter6200Series = _NtSecureRouter6200Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 1)
)
_NtSecureRouter6230_ObjectIdentity = ObjectIdentity
ntSecureRouter6230 = _NtSecureRouter6230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 1, 1)
)
_NtSecureRouter6280_ObjectIdentity = ObjectIdentity
ntSecureRouter6280 = _NtSecureRouter6280_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 1, 2)
)
_NtSecureRouter3000Series_ObjectIdentity = ObjectIdentity
ntSecureRouter3000Series = _NtSecureRouter3000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 2)
)
_NtSecureRouter3120_ObjectIdentity = ObjectIdentity
ntSecureRouter3120 = _NtSecureRouter3120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 2, 1)
)
_NtSecureRouter1000Series_ObjectIdentity = ObjectIdentity
ntSecureRouter1000Series = _NtSecureRouter1000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3)
)
_NtSecureRouter1001_ObjectIdentity = ObjectIdentity
ntSecureRouter1001 = _NtSecureRouter1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 1)
)
_NtSecureRouter1002_ObjectIdentity = ObjectIdentity
ntSecureRouter1002 = _NtSecureRouter1002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 2)
)
_NtSecureRouter1004_ObjectIdentity = ObjectIdentity
ntSecureRouter1004 = _NtSecureRouter1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 3)
)
_NtSecureRouter1002E_ObjectIdentity = ObjectIdentity
ntSecureRouter1002E = _NtSecureRouter1002E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 4)
)
_NtSecureRouter1004E_ObjectIdentity = ObjectIdentity
ntSecureRouter1004E = _NtSecureRouter1004E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 5)
)
_NtSecureRouter1001S_ObjectIdentity = ObjectIdentity
ntSecureRouter1001S = _NtSecureRouter1001S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 3, 6)
)
_NtSecureRouterNESeries_ObjectIdentity = ObjectIdentity
ntSecureRouterNESeries = _NtSecureRouterNESeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 4)
)
_NtSecureRouterNE05_ObjectIdentity = ObjectIdentity
ntSecureRouterNE05 = _NtSecureRouterNE05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 4, 1)
)
_NtSecureRouterNE08_ObjectIdentity = ObjectIdentity
ntSecureRouterNE08 = _NtSecureRouterNE08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 4, 2)
)
_NtSecureRouterNE16_ObjectIdentity = ObjectIdentity
ntSecureRouterNE16 = _NtSecureRouterNE16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 4, 3)
)
_NtSecureRouterNE20_ObjectIdentity = ObjectIdentity
ntSecureRouterNE20 = _NtSecureRouterNE20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 4, 4)
)
_NtSecureRouter4000Series_ObjectIdentity = ObjectIdentity
ntSecureRouter4000Series = _NtSecureRouter4000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 5)
)
_NtSecureRouter4134_ObjectIdentity = ObjectIdentity
ntSecureRouter4134 = _NtSecureRouter4134_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 5, 1)
)
_NtSecureRouter2000Series_ObjectIdentity = ObjectIdentity
ntSecureRouter2000Series = _NtSecureRouter2000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 6)
)
_NtSecureRouter2330_ObjectIdentity = ObjectIdentity
ntSecureRouter2330 = _NtSecureRouter2330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 2, 6, 1)
)
_NtEnterpriseServiceGateways_ObjectIdentity = ObjectIdentity
ntEnterpriseServiceGateways = _NtEnterpriseServiceGateways_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 3)
)
_EnterpriseGateway_ObjectIdentity = ObjectIdentity
enterpriseGateway = _EnterpriseGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 4)
)
_AdvancedGateway2000Series_ObjectIdentity = ObjectIdentity
advancedGateway2000Series = _AdvancedGateway2000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 4, 1)
)
_AdvancedGateway2330_ObjectIdentity = ObjectIdentity
advancedGateway2330 = _AdvancedGateway2330_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 2, 4, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    **{"ntEnterpriseData": ntEnterpriseData,
       "ntEnterpriseDataMibs": ntEnterpriseDataMibs,
       "ntEnterpriseDataTasmanMibs": ntEnterpriseDataTasmanMibs,
       "ntEnterpriseDataTasmanMgmt": ntEnterpriseDataTasmanMgmt,
       "ntEnterpriseDataTasmanInterfaces": ntEnterpriseDataTasmanInterfaces,
       "ntEnterpriseDataTasmanModules": ntEnterpriseDataTasmanModules,
       "ntEnterpriseDataNewburyMibs": ntEnterpriseDataNewburyMibs,
       "ntEnterpriseDataRegistration": ntEnterpriseDataRegistration,
       "ntEnterpriseSwitches": ntEnterpriseSwitches,
       "ntEthernetSwitch": ntEthernetSwitch,
       "ntEthernetRoutingSwitch": ntEthernetRoutingSwitch,
       "ntEnterpriseRouters": ntEnterpriseRouters,
       "ntSecureRouter6200Series": ntSecureRouter6200Series,
       "ntSecureRouter6230": ntSecureRouter6230,
       "ntSecureRouter6280": ntSecureRouter6280,
       "ntSecureRouter3000Series": ntSecureRouter3000Series,
       "ntSecureRouter3120": ntSecureRouter3120,
       "ntSecureRouter1000Series": ntSecureRouter1000Series,
       "ntSecureRouter1001": ntSecureRouter1001,
       "ntSecureRouter1002": ntSecureRouter1002,
       "ntSecureRouter1004": ntSecureRouter1004,
       "ntSecureRouter1002E": ntSecureRouter1002E,
       "ntSecureRouter1004E": ntSecureRouter1004E,
       "ntSecureRouter1001S": ntSecureRouter1001S,
       "ntSecureRouterNESeries": ntSecureRouterNESeries,
       "ntSecureRouterNE05": ntSecureRouterNE05,
       "ntSecureRouterNE08": ntSecureRouterNE08,
       "ntSecureRouterNE16": ntSecureRouterNE16,
       "ntSecureRouterNE20": ntSecureRouterNE20,
       "ntSecureRouter4000Series": ntSecureRouter4000Series,
       "ntSecureRouter4134": ntSecureRouter4134,
       "ntSecureRouter2000Series": ntSecureRouter2000Series,
       "ntSecureRouter2330": ntSecureRouter2330,
       "ntEnterpriseServiceGateways": ntEnterpriseServiceGateways,
       "enterpriseGateway": enterpriseGateway,
       "advancedGateway2000Series": advancedGateway2000Series,
       "advancedGateway2330": advancedGateway2330}
)
