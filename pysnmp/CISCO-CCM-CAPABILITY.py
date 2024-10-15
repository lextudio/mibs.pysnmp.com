# SNMP MIB module (CISCO-CCM-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CCM-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:06 2024
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

ciscoCCMCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 211)
)
ciscoCCMCapability.setRevisions(
        ("2011-06-14 00:00",
         "2009-12-15 00:00",
         "2008-08-21 00:00",
         "2008-02-20 00:00",
         "2005-11-21 00:00",
         "2003-10-03 00:00",
         "2002-03-21 00:00",
         "2001-07-02 00:00",
         "2001-06-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoCCMCapabilityV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 1)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R00.setProductRelease("Cisco Call Manager 3.0")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R00.setStatus(
        "current"
    )

ciscoCCMCapabilityV3R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 2)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R01.setProductRelease("Cisco Call Manager 3.1")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R01.setStatus(
        "current"
    )

ciscoCCMCapabilityV3R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 3)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R03.setProductRelease("Cisco Call Manager 3.3")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R03.setStatus(
        "obsolete"
    )

ciscoCCMCapabilityV3R03Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 4)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R03Rev1.setProductRelease("Cisco Call Manager 3.3")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV3R03Rev1.setStatus(
        "current"
    )

ciscoCCMCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 5)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV4R00.setProductRelease("Cisco Call Manager 4.0")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV4R00.setStatus(
        "current"
    )

ciscoCCMCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 6)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV5R00.setProductRelease("Cisco Call Manager 5.0")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV5R00.setStatus(
        "current"
    )

ciscoCCMCapabilityV7R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 7)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV7R00.setProductRelease("Cisco Unified Communications Manager 7.0")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV7R00.setStatus(
        "current"
    )

ciscoCCMCapabilityV7R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 8)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV7R01.setProductRelease("Cisco Unified Communications Manager 7.1")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV7R01.setStatus(
        "current"
    )

ciscoCCMCapabilityV8R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 9)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV8R00.setProductRelease("Cisco Unified Communications Manager 8.0")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV8R00.setStatus(
        "current"
    )

ciscoCCMCapabilityV8R05 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 211, 10)
)
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV8R05.setProductRelease("Cisco Unified Communications Manager 8.5")
if mibBuilder.loadTexts:
    ciscoCCMCapabilityV8R05.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CCM-CAPABILITY",
    **{"ciscoCCMCapability": ciscoCCMCapability,
       "ciscoCCMCapabilityV3R00": ciscoCCMCapabilityV3R00,
       "ciscoCCMCapabilityV3R01": ciscoCCMCapabilityV3R01,
       "ciscoCCMCapabilityV3R03": ciscoCCMCapabilityV3R03,
       "ciscoCCMCapabilityV3R03Rev1": ciscoCCMCapabilityV3R03Rev1,
       "ciscoCCMCapabilityV4R00": ciscoCCMCapabilityV4R00,
       "ciscoCCMCapabilityV5R00": ciscoCCMCapabilityV5R00,
       "ciscoCCMCapabilityV7R00": ciscoCCMCapabilityV7R00,
       "ciscoCCMCapabilityV7R01": ciscoCCMCapabilityV7R01,
       "ciscoCCMCapabilityV8R00": ciscoCCMCapabilityV8R00,
       "ciscoCCMCapabilityV8R05": ciscoCCMCapabilityV8R05}
)
