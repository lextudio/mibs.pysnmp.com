# SNMP MIB module (CISCO-CAS-IF-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CAS-IF-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:53 2024
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

(ciscoAgentCapability,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoAgentCapability")

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

ciscoCasIfCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 122)
)
ciscoCasIfCapability.setRevisions(
        ("2009-12-04 00:00",
         "2004-08-10 00:00",
         "2003-12-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoCasIfCapabilityV5R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 122, 1)
)
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV5R000.setProductRelease("MGX8850 Release 5.0")
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV5R000.setStatus(
        "current"
    )

ciscoCasIfCapabilityV5R015 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 122, 2)
)
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV5R015.setProductRelease("MGX8850 Release 5.0.15")
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV5R015.setStatus(
        "current"
    )

ciscoCasIfCapabilityV12R04TPC3xxx = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 122, 3)
)
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV12R04TPC3xxx.setProductRelease("""\
CISCO IOS 12.4T for Integrate Service
                     Router (ISR) c2xxx and c3xxx platforms.""")
if mibBuilder.loadTexts:
    ciscoCasIfCapabilityV12R04TPC3xxx.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CAS-IF-CAPABILITY",
    **{"ciscoCasIfCapability": ciscoCasIfCapability,
       "ciscoCasIfCapabilityV5R000": ciscoCasIfCapabilityV5R000,
       "ciscoCasIfCapabilityV5R015": ciscoCasIfCapabilityV5R015,
       "ciscoCasIfCapabilityV12R04TPC3xxx": ciscoCasIfCapabilityV12R04TPC3xxx}
)
