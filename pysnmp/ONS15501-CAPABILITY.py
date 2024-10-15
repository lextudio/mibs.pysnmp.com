# SNMP MIB module (ONS15501-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONS15501-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:12 2024
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

(synchronous,) = mibBuilder.importSymbols(
    "ONS15501-MIB",
    "synchronous")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

ons15501MIBCapabilities = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 15, 11)
)
ons15501MIBCapabilities.setRevisions(
        ("2002-10-15 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SynEmbLxCapability_ObjectIdentity = ObjectIdentity
synEmbLxCapability = _SynEmbLxCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1869, 15)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ons15501CapOld = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1869, 15, 11, 1)
)
if mibBuilder.loadTexts:
    ons15501CapOld.setProductRelease("Release 3.0 of ONS15501 software.")
if mibBuilder.loadTexts:
    ons15501CapOld.setStatus(
        "current"
    )

ons15501CapDC = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1869, 15, 11, 2)
)
if mibBuilder.loadTexts:
    ons15501CapDC.setProductRelease("DC series of ONS15501, Release 4.0")
if mibBuilder.loadTexts:
    ons15501CapDC.setStatus(
        "current"
    )

ons15501CapAC = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1869, 15, 11, 3)
)
if mibBuilder.loadTexts:
    ons15501CapAC.setProductRelease("AC series of ONS15501, Release 4.0")
if mibBuilder.loadTexts:
    ons15501CapAC.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONS15501-CAPABILITY",
    **{"synEmbLxCapability": synEmbLxCapability,
       "ons15501MIBCapabilities": ons15501MIBCapabilities,
       "ons15501CapOld": ons15501CapOld,
       "ons15501CapDC": ons15501CapDC,
       "ons15501CapAC": ons15501CapAC}
)
