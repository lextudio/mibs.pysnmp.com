# SNMP MIB module (CISCO-SYSLOG-EXT-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSLOG-EXT-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:23 2024
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

ciscoSyslogExtCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 454)
)
ciscoSyslogExtCapability.setRevisions(
        ("2008-06-30 00:00",
         "2006-04-18 00:00",
         "2005-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSyslogExtCapabilityMDS3R0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 454, 1)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityMDS3R0.setProductRelease("Cisco MDS 3.0(1)")
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityMDS3R0.setStatus(
        "current"
    )

ciscoSyslogExtCapabilityACSWV03R0000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 454, 2)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityACSWV03R0000.setProductRelease("""\
ACSW (Application Control Software) 3.0
                for Application Control Engine(ACE) module.""")
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityACSWV03R0000.setStatus(
        "obsolete"
    )

ciscoSyslogExtCapACSWV03R0000Rev1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 454, 3)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtCapACSWV03R0000Rev1.setProductRelease("""\
ACSW (Application Control Software) 3.0
                    for Application Control Engine(ACE) module.""")
if mibBuilder.loadTexts:
    ciscoSyslogExtCapACSWV03R0000Rev1.setStatus(
        "current"
    )

ciscoSyslogExtCapabilityc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 454, 4)
)
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance.""")
if mibBuilder.loadTexts:
    ciscoSyslogExtCapabilityc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSLOG-EXT-CAPABILITY",
    **{"ciscoSyslogExtCapability": ciscoSyslogExtCapability,
       "ciscoSyslogExtCapabilityMDS3R0": ciscoSyslogExtCapabilityMDS3R0,
       "ciscoSyslogExtCapabilityACSWV03R0000": ciscoSyslogExtCapabilityACSWV03R0000,
       "ciscoSyslogExtCapACSWV03R0000Rev1": ciscoSyslogExtCapACSWV03R0000Rev1,
       "ciscoSyslogExtCapabilityc4710aceVA1R700": ciscoSyslogExtCapabilityc4710aceVA1R700}
)
