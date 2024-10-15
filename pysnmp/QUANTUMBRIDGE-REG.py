# SNMP MIB module (QUANTUMBRIDGE-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QUANTUMBRIDGE-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:37 2024
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

quantumBridgeRegistrations = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QuantumBridge_ObjectIdentity = ObjectIdentity
quantumBridge = _QuantumBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323)
)
if mibBuilder.loadTexts:
    quantumBridge.setStatus("current")
_QbMibs_ObjectIdentity = ObjectIdentity
qbMibs = _QbMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2)
)
if mibBuilder.loadTexts:
    qbMibs.setStatus("current")
_QbProducts_ObjectIdentity = ObjectIdentity
qbProducts = _QbProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 3)
)
if mibBuilder.loadTexts:
    qbProducts.setStatus("current")
_Qb5000SystemID_ObjectIdentity = ObjectIdentity
qb5000SystemID = _Qb5000SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 3, 1)
)
_Qb3000SystemID_ObjectIdentity = ObjectIdentity
qb3000SystemID = _Qb3000SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 3, 2)
)
_Qb8000SystemID_ObjectIdentity = ObjectIdentity
qb8000SystemID = _Qb8000SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 3, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QUANTUMBRIDGE-REG",
    **{"quantumBridge": quantumBridge,
       "quantumBridgeRegistrations": quantumBridgeRegistrations,
       "qbMibs": qbMibs,
       "qbProducts": qbProducts,
       "qb5000SystemID": qb5000SystemID,
       "qb3000SystemID": qb3000SystemID,
       "qb8000SystemID": qb8000SystemID}
)
