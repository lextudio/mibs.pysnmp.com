# SNMP MIB module (CISCO-VOICE-DIAL-CONTROL-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-DIAL-CONTROL-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:21 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoVoiceDialControlCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 83)
)
ciscoVoiceDialControlCapability.setRevisions(
        ("2009-03-31 00:00",
         "2006-11-16 00:00",
         "2005-07-25 00:00",
         "1999-07-12 00:00",
         "1998-01-09 00:00",
         "1997-06-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoVoiceDialControlCapabilityV11R03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 1)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV11R03.setProductRelease("Cisco IOS 11.3")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV11R03.setStatus(
        "obsolete"
    )

ciscoVoiceDialControlCapabilityV11R03Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 2)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV11R03Rev1.setProductRelease("Cisco IOS 11.3")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV11R03Rev1.setStatus(
        "current"
    )

ciscoVoiceDialControlCapabilityV12R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 3)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV12R00.setProductRelease("Cisco IOS 12.0(5)")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV12R00.setStatus(
        "obsolete"
    )

ciscoVoiceDialControlCapabilityV12R00Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 4)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV12R00Rev1.setProductRelease("Cisco IOS 12.0(5)")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV12R00Rev1.setStatus(
        "current"
    )

ciscoVoiceDialControlCapabilityV124R03T5400 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 5)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV124R03T5400.setProductRelease("Cisco IOS 12.4(3)T on AS5400")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapabilityV124R03T5400.setStatus(
        "current"
    )

ciscoVoiceDialControlCapV12R04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 6)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapV12R04.setProductRelease("Cisco IOS 12.4 for all platforms except IAD2420")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapV12R04.setStatus(
        "current"
    )

ciscoVoiceDialControlCapV12R04Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 83, 7)
)
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapV12R04Rev1.setProductRelease("Cisco IOS 12.4T")
if mibBuilder.loadTexts:
    ciscoVoiceDialControlCapV12R04Rev1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-DIAL-CONTROL-CAPABILITY",
    **{"ciscoVoiceDialControlCapability": ciscoVoiceDialControlCapability,
       "ciscoVoiceDialControlCapabilityV11R03": ciscoVoiceDialControlCapabilityV11R03,
       "ciscoVoiceDialControlCapabilityV11R03Rev1": ciscoVoiceDialControlCapabilityV11R03Rev1,
       "ciscoVoiceDialControlCapabilityV12R00": ciscoVoiceDialControlCapabilityV12R00,
       "ciscoVoiceDialControlCapabilityV12R00Rev1": ciscoVoiceDialControlCapabilityV12R00Rev1,
       "ciscoVoiceDialControlCapabilityV124R03T5400": ciscoVoiceDialControlCapabilityV124R03T5400,
       "ciscoVoiceDialControlCapV12R04": ciscoVoiceDialControlCapV12R04,
       "ciscoVoiceDialControlCapV12R04Rev1": ciscoVoiceDialControlCapV12R04Rev1}
)
