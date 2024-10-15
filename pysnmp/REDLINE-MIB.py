# SNMP MIB module (REDLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDLINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:27 2024
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

redline = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10728)
)
redline.setRevisions(
        ("2005-06-08 17:50",
         "2001-11-08 00:00",
         "2001-08-12 00:00",
         "2002-03-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedlineProducts_ObjectIdentity = ObjectIdentity
redlineProducts = _RedlineProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 1)
)
if mibBuilder.loadTexts:
    redlineProducts.setStatus("current")
_RedlineMgmt_ObjectIdentity = ObjectIdentity
redlineMgmt = _RedlineMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2)
)
if mibBuilder.loadTexts:
    redlineMgmt.setStatus("current")
_RedlineSystem_ObjectIdentity = ObjectIdentity
redlineSystem = _RedlineSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 1)
)
_RedlineTransmission_ObjectIdentity = ObjectIdentity
redlineTransmission = _RedlineTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 2, 10)
)
_RedlineExperiment_ObjectIdentity = ObjectIdentity
redlineExperiment = _RedlineExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 3)
)
if mibBuilder.loadTexts:
    redlineExperiment.setStatus("current")
_RedlineAdmin_ObjectIdentity = ObjectIdentity
redlineAdmin = _RedlineAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 4)
)
if mibBuilder.loadTexts:
    redlineAdmin.setStatus("current")
_RedlineModules_ObjectIdentity = ObjectIdentity
redlineModules = _RedlineModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 5)
)
if mibBuilder.loadTexts:
    redlineModules.setStatus("current")
_RedlinePartners_ObjectIdentity = ObjectIdentity
redlinePartners = _RedlinePartners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 6)
)
if mibBuilder.loadTexts:
    redlinePartners.setStatus("current")
_RedlineOtherEnterpises_ObjectIdentity = ObjectIdentity
redlineOtherEnterpises = _RedlineOtherEnterpises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 7)
)
if mibBuilder.loadTexts:
    redlineOtherEnterpises.setStatus("current")
_RedlineAgentCapability_ObjectIdentity = ObjectIdentity
redlineAgentCapability = _RedlineAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10728, 8)
)
if mibBuilder.loadTexts:
    redlineAgentCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDLINE-MIB",
    **{"redline": redline,
       "redlineProducts": redlineProducts,
       "redlineMgmt": redlineMgmt,
       "redlineSystem": redlineSystem,
       "redlineTransmission": redlineTransmission,
       "redlineExperiment": redlineExperiment,
       "redlineAdmin": redlineAdmin,
       "redlineModules": redlineModules,
       "redlinePartners": redlinePartners,
       "redlineOtherEnterpises": redlineOtherEnterpises,
       "redlineAgentCapability": redlineAgentCapability}
)
