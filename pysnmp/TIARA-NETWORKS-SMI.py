# SNMP MIB module (TIARA-NETWORKS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:54 2024
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

tiaraNetworks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174)
)
tiaraNetworks.setRevisions(
        ("1993-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TiaraProducts_ObjectIdentity = ObjectIdentity
tiaraProducts = _TiaraProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1)
)
if mibBuilder.loadTexts:
    tiaraProducts.setStatus("current")
_TiaraMgmt_ObjectIdentity = ObjectIdentity
tiaraMgmt = _TiaraMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2)
)
if mibBuilder.loadTexts:
    tiaraMgmt.setStatus("current")
_TiaraInterfaces_ObjectIdentity = ObjectIdentity
tiaraInterfaces = _TiaraInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7)
)
if mibBuilder.loadTexts:
    tiaraInterfaces.setStatus("current")
_TiaraModules_ObjectIdentity = ObjectIdentity
tiaraModules = _TiaraModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 3)
)
if mibBuilder.loadTexts:
    tiaraModules.setStatus("current")
_TiaraExperiment_ObjectIdentity = ObjectIdentity
tiaraExperiment = _TiaraExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 4)
)
if mibBuilder.loadTexts:
    tiaraExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-SMI",
    **{"tiaraNetworks": tiaraNetworks,
       "tiaraProducts": tiaraProducts,
       "tiaraMgmt": tiaraMgmt,
       "tiaraInterfaces": tiaraInterfaces,
       "tiaraModules": tiaraModules,
       "tiaraExperiment": tiaraExperiment}
)
