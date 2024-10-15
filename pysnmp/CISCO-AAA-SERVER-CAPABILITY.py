# SNMP MIB module (CISCO-AAA-SERVER-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AAA-SERVER-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:23 2024
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

ciscoAAAServerCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 129)
)
ciscoAAAServerCapability.setRevisions(
        ("2008-07-21 00:00",
         "2006-02-21 00:00",
         "2003-11-14 00:00",
         "2000-01-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoAAAServerCapabilityV10R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 129, 1)
)
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityV10R00.setProductRelease("Cisco IOS 12.0(4)XJ")
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityV10R00.setStatus(
        "current"
    )

ciscoAAAServerCapabilityMDS13R1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 129, 2)
)
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityMDS13R1.setProductRelease("Cisco MDS 1.3(1)")
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityMDS13R1.setStatus(
        "current"
    )

ciscoAAAServerCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 129, 3)
)
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    ciscoAAAServerCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoAAAServerCapc4710aceVA1R70 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 129, 4)
)
if mibBuilder.loadTexts:
    ciscoAAAServerCapc4710aceVA1R70.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                         for ACE 4710 Application Control Engine 
                         Appliance.""")
if mibBuilder.loadTexts:
    ciscoAAAServerCapc4710aceVA1R70.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AAA-SERVER-CAPABILITY",
    **{"ciscoAAAServerCapability": ciscoAAAServerCapability,
       "ciscoAAAServerCapabilityV10R00": ciscoAAAServerCapabilityV10R00,
       "ciscoAAAServerCapabilityMDS13R1": ciscoAAAServerCapabilityMDS13R1,
       "ciscoAAAServerCapabilityACSWV03R000": ciscoAAAServerCapabilityACSWV03R000,
       "ciscoAAAServerCapc4710aceVA1R70": ciscoAAAServerCapc4710aceVA1R70}
)
