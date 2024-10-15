# SNMP MIB module (OG-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OG-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:47 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

opengear = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049)
)
opengear.setRevisions(
        ("2013-11-15 00:00",
         "2013-08-11 00:00",
         "2010-03-22 11:27",
         "2005-02-24 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgProducts_ObjectIdentity = ObjectIdentity
ogProducts = _OgProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 1)
)
if mibBuilder.loadTexts:
    ogProducts.setStatus("current")
_OgLegacyMgmt_ObjectIdentity = ObjectIdentity
ogLegacyMgmt = _OgLegacyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 2)
)
if mibBuilder.loadTexts:
    ogLegacyMgmt.setStatus("current")
_OgExperimental_ObjectIdentity = ObjectIdentity
ogExperimental = _OgExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 3)
)
if mibBuilder.loadTexts:
    ogExperimental.setStatus("current")
_OgInternal_ObjectIdentity = ObjectIdentity
ogInternal = _OgInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 4)
)
if mibBuilder.loadTexts:
    ogInternal.setStatus("current")
_OgReserved1_ObjectIdentity = ObjectIdentity
ogReserved1 = _OgReserved1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 5)
)
if mibBuilder.loadTexts:
    ogReserved1.setStatus("current")
_OgReserved2_ObjectIdentity = ObjectIdentity
ogReserved2 = _OgReserved2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 6)
)
if mibBuilder.loadTexts:
    ogReserved2.setStatus("current")
_OtherEnterprises_ObjectIdentity = ObjectIdentity
otherEnterprises = _OtherEnterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 7)
)
if mibBuilder.loadTexts:
    otherEnterprises.setStatus("current")
_OgAgentCapability_ObjectIdentity = ObjectIdentity
ogAgentCapability = _OgAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 8)
)
if mibBuilder.loadTexts:
    ogAgentCapability.setStatus("current")
_OgConfig_ObjectIdentity = ObjectIdentity
ogConfig = _OgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 9)
)
if mibBuilder.loadTexts:
    ogConfig.setStatus("current")
_OgMgmt_ObjectIdentity = ObjectIdentity
ogMgmt = _OgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10)
)
if mibBuilder.loadTexts:
    ogMgmt.setStatus("current")
_OgModules_ObjectIdentity = ObjectIdentity
ogModules = _OgModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 11)
)
if mibBuilder.loadTexts:
    ogModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-SMI-MIB",
    **{"opengear": opengear,
       "ogProducts": ogProducts,
       "ogLegacyMgmt": ogLegacyMgmt,
       "ogExperimental": ogExperimental,
       "ogInternal": ogInternal,
       "ogReserved1": ogReserved1,
       "ogReserved2": ogReserved2,
       "otherEnterprises": otherEnterprises,
       "ogAgentCapability": ogAgentCapability,
       "ogConfig": ogConfig,
       "ogMgmt": ogMgmt,
       "ogModules": ogModules}
)
