# SNMP MIB module (CISCO-SLB-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SLB-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:19 2024
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

ciscoSlbCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 181)
)
ciscoSlbCapability.setRevisions(
        ("2008-07-24 00:00",
         "2008-02-07 00:00",
         "2006-12-09 00:00",
         "2006-03-21 00:00",
         "2001-03-09 00:00",
         "2000-10-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSlbCapabilityV12R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 1)
)
if mibBuilder.loadTexts:
    ciscoSlbCapabilityV12R01.setProductRelease("Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01")
if mibBuilder.loadTexts:
    ciscoSlbCapabilityV12R01.setStatus(
        "obsolete"
    )

ciscoIfCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 2)
)
if mibBuilder.loadTexts:
    ciscoIfCapabilityACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    ciscoIfCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 3)
)
if mibBuilder.loadTexts:
    ciscoSlbExtCapabilityACSWV300RA12.setProductRelease("""\
ACSW (Application Control Software)
                version 3.0(0)A1(2).""")
if mibBuilder.loadTexts:
    ciscoSlbExtCapabilityACSWV300RA12.setStatus(
        "current"
    )

ciscoSlbCapabilityNewV12R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 4)
)
if mibBuilder.loadTexts:
    ciscoSlbCapabilityNewV12R01.setProductRelease("Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01")
if mibBuilder.loadTexts:
    ciscoSlbCapabilityNewV12R01.setStatus(
        "current"
    )

ciscoSlbCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 5)
)
if mibBuilder.loadTexts:
    ciscoSlbCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    appliance.""")
if mibBuilder.loadTexts:
    ciscoSlbCapc4710aceVA1R700.setStatus(
        "current"
    )

ciscoSlbCapc4710aceVA3R100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 181, 6)
)
if mibBuilder.loadTexts:
    ciscoSlbCapc4710aceVA3R100.setProductRelease("""\
ACSW (Application Control Software) A3(1) for
                     ACE 4710 Application Control Engine Appliance.""")
if mibBuilder.loadTexts:
    ciscoSlbCapc4710aceVA3R100.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SLB-CAPABILITY",
    **{"ciscoSlbCapability": ciscoSlbCapability,
       "ciscoSlbCapabilityV12R01": ciscoSlbCapabilityV12R01,
       "ciscoIfCapabilityACSWV03R000": ciscoIfCapabilityACSWV03R000,
       "ciscoSlbExtCapabilityACSWV300RA12": ciscoSlbExtCapabilityACSWV300RA12,
       "ciscoSlbCapabilityNewV12R01": ciscoSlbCapabilityNewV12R01,
       "ciscoSlbCapc4710aceVA1R700": ciscoSlbCapc4710aceVA1R700,
       "ciscoSlbCapc4710aceVA3R100": ciscoSlbCapc4710aceVA3R100}
)
