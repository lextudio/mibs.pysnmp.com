# SNMP MIB module (CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:38 2024
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

ciscoTelepresenceExchangeSystemCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 615)
)
ciscoTelepresenceExchangeSystemCapability.setRevisions(
        ("2013-04-11 00:00",
         "2012-08-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoTelepresenceCapabilityCTXV120 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 615, 1)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceCapabilityCTXV120.setProductRelease("""\
OS=TELEPRESENCE EXCHANGE SYSTEM
                     OSVERSION=1.2.0
                     PLATFORM=TelePresence (TP)
                     INTERFACE=None""")
if mibBuilder.loadTexts:
    ciscoTelepresenceCapabilityCTXV120.setStatus(
        "current"
    )

ciscoTelepresenceCapabilityCTXV130 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 615, 2)
)
if mibBuilder.loadTexts:
    ciscoTelepresenceCapabilityCTXV130.setProductRelease("""\
OS=TELEPRESENCE EXCHANGE SYSTEM
                     OSVERSION=1.3.0
                     PLATFORM=TelePresence (TP)
                     INTERFACE=None""")
if mibBuilder.loadTexts:
    ciscoTelepresenceCapabilityCTXV130.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY",
    **{"ciscoTelepresenceExchangeSystemCapability": ciscoTelepresenceExchangeSystemCapability,
       "ciscoTelepresenceCapabilityCTXV120": ciscoTelepresenceCapabilityCTXV120,
       "ciscoTelepresenceCapabilityCTXV130": ciscoTelepresenceCapabilityCTXV130}
)
