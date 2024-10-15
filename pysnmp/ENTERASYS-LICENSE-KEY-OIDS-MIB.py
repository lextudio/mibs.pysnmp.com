# SNMP MIB module (ENTERASYS-LICENSE-KEY-OIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-LICENSE-KEY-OIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:03 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(etsysOidOtherLicenseKeyId,) = mibBuilder.importSymbols(
    "ENTERASYS-OIDS-MIB",
    "etsysOidOtherLicenseKeyId")

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

etsysLicenseKeyOidsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 56)
)
etsysLicenseKeyOidsMIB.setRevisions(
        ("2009-08-05 20:14",
         "2008-02-26 13:51",
         "2008-01-18 15:56",
         "2007-06-11 14:24",
         "2006-11-13 15:29",
         "2006-09-05 17:37",
         "2006-08-15 19:56",
         "2005-12-13 21:12",
         "2004-11-03 17:01",
         "2004-08-24 13:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysLicKeyIdNSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNSeries = _EtsysLicKeyIdNSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1)
)
_EtsysLicKeyIdNL3AdvancedFeature_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNL3AdvancedFeature = _EtsysLicKeyIdNL3AdvancedFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNL3AdvancedFeature.setStatus("current")
_EtsysLicKeyIdNGoldRedundancy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNGoldRedundancy = _EtsysLicKeyIdNGoldRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNGoldRedundancy.setStatus("current")
_EtsysLicKeyIdNPlatinumHighCapacity_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNPlatinumHighCapacity = _EtsysLicKeyIdNPlatinumHighCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNPlatinumHighCapacity.setStatus("current")
_EtsysLicKeyIdNPlatinumPortCapacity_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNPlatinumPortCapacity = _EtsysLicKeyIdNPlatinumPortCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNPlatinumPortCapacity.setStatus("current")
_EtsysLicKeyIdNGoldPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNGoldPolicy = _EtsysLicKeyIdNGoldPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNGoldPolicy.setStatus("current")
_EtsysLicKeyIdNL3DiamondFeature_ObjectIdentity = ObjectIdentity
etsysLicKeyIdNL3DiamondFeature = _EtsysLicKeyIdNL3DiamondFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdNL3DiamondFeature.setStatus("current")
_EtsysLicKeyIdCSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdCSeries = _EtsysLicKeyIdCSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2)
)
_EtsysLicKeyIdCAdvancedRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdCAdvancedRouting = _EtsysLicKeyIdCAdvancedRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdCAdvancedRouting.setStatus("current")
_EtsysLicKeyIdC3IpV6Routing_ObjectIdentity = ObjectIdentity
etsysLicKeyIdC3IpV6Routing = _EtsysLicKeyIdC3IpV6Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdC3IpV6Routing.setStatus("current")
_EtsysLicKeyIdBSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBSeries = _EtsysLicKeyIdBSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3)
)
_EtsysLicKeyIdBPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBPolicy = _EtsysLicKeyIdBPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdBPolicy.setStatus("current")
_EtsysLicKeyIdBRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdBRouting = _EtsysLicKeyIdBRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdBRouting.setStatus("current")
_EtsysLicKeyIdDSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdDSeries = _EtsysLicKeyIdDSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 4)
)
_EtsysLicKeyIdDPolicy_ObjectIdentity = ObjectIdentity
etsysLicKeyIdDPolicy = _EtsysLicKeyIdDPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdDPolicy.setStatus("current")
_EtsysLicKeyIdGSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdGSeries = _EtsysLicKeyIdGSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 5)
)
_EtsysLicKeyIdGRouting_ObjectIdentity = ObjectIdentity
etsysLicKeyIdGRouting = _EtsysLicKeyIdGRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdGRouting.setStatus("current")
_EtsysLicKeyIdSSeries_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSSeries = _EtsysLicKeyIdSSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6)
)
_EtsysLicKeyIdSxEOSxPPC_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxPPC = _EtsysLicKeyIdSxEOSxPPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxPPC.setStatus("current")
_EtsysLicKeyIdSxEOSxL3xACCESS_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxL3xACCESS = _EtsysLicKeyIdSxEOSxL3xACCESS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxL3xACCESS.setStatus("current")
_EtsysLicKeyIdSxEOSxL3xCORE_ObjectIdentity = ObjectIdentity
etsysLicKeyIdSxEOSxL3xCORE = _EtsysLicKeyIdSxEOSxL3xCORE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 2, 3, 2, 6, 3)
)
if mibBuilder.loadTexts:
    etsysLicKeyIdSxEOSxL3xCORE.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-LICENSE-KEY-OIDS-MIB",
    **{"etsysLicenseKeyOidsMIB": etsysLicenseKeyOidsMIB,
       "etsysLicKeyIdNSeries": etsysLicKeyIdNSeries,
       "etsysLicKeyIdNL3AdvancedFeature": etsysLicKeyIdNL3AdvancedFeature,
       "etsysLicKeyIdNGoldRedundancy": etsysLicKeyIdNGoldRedundancy,
       "etsysLicKeyIdNPlatinumHighCapacity": etsysLicKeyIdNPlatinumHighCapacity,
       "etsysLicKeyIdNPlatinumPortCapacity": etsysLicKeyIdNPlatinumPortCapacity,
       "etsysLicKeyIdNGoldPolicy": etsysLicKeyIdNGoldPolicy,
       "etsysLicKeyIdNL3DiamondFeature": etsysLicKeyIdNL3DiamondFeature,
       "etsysLicKeyIdCSeries": etsysLicKeyIdCSeries,
       "etsysLicKeyIdCAdvancedRouting": etsysLicKeyIdCAdvancedRouting,
       "etsysLicKeyIdC3IpV6Routing": etsysLicKeyIdC3IpV6Routing,
       "etsysLicKeyIdBSeries": etsysLicKeyIdBSeries,
       "etsysLicKeyIdBPolicy": etsysLicKeyIdBPolicy,
       "etsysLicKeyIdBRouting": etsysLicKeyIdBRouting,
       "etsysLicKeyIdDSeries": etsysLicKeyIdDSeries,
       "etsysLicKeyIdDPolicy": etsysLicKeyIdDPolicy,
       "etsysLicKeyIdGSeries": etsysLicKeyIdGSeries,
       "etsysLicKeyIdGRouting": etsysLicKeyIdGRouting,
       "etsysLicKeyIdSSeries": etsysLicKeyIdSSeries,
       "etsysLicKeyIdSxEOSxPPC": etsysLicKeyIdSxEOSxPPC,
       "etsysLicKeyIdSxEOSxL3xACCESS": etsysLicKeyIdSxEOSxL3xACCESS,
       "etsysLicKeyIdSxEOSxL3xCORE": etsysLicKeyIdSxEOSxL3xCORE}
)
