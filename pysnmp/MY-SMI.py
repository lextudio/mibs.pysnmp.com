# SNMP MIB module (MY-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:14 2024
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

switchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97)
)
switchMib.setRevisions(
        ("2002-03-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_My_ObjectIdentity = ObjectIdentity
my = _My_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_MySwitchProducts_ObjectIdentity = ObjectIdentity
mySwitchProducts = _MySwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 1)
)
if mibBuilder.loadTexts:
    mySwitchProducts.setStatus("current")
_MyMgmt_ObjectIdentity = ObjectIdentity
myMgmt = _MyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2)
)
if mibBuilder.loadTexts:
    myMgmt.setStatus("current")
_MyAgentCapability_ObjectIdentity = ObjectIdentity
myAgentCapability = _MyAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 3)
)
if mibBuilder.loadTexts:
    myAgentCapability.setStatus("current")
_MyModules_ObjectIdentity = ObjectIdentity
myModules = _MyModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 4)
)
if mibBuilder.loadTexts:
    myModules.setStatus("current")
_MyExperiment_ObjectIdentity = ObjectIdentity
myExperiment = _MyExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 5)
)
if mibBuilder.loadTexts:
    myExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-SMI",
    **{"my": my,
       "products": products,
       "switchMib": switchMib,
       "mySwitchProducts": mySwitchProducts,
       "myMgmt": myMgmt,
       "myAgentCapability": myAgentCapability,
       "myModules": myModules,
       "myExperiment": myExperiment}
)
