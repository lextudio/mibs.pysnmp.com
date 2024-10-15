# SNMP MIB module (CISCO-IP-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:34 2024
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

ciscoIpCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 445)
)
ciscoIpCapability.setRevisions(
        ("2010-09-30 00:00",
         "2008-08-11 00:00",
         "2007-11-05 00:00",
         "2006-11-03 00:00",
         "2006-05-27 00:00",
         "2006-02-17 00:00",
         "2005-07-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cIpCapV320CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 1)
)
if mibBuilder.loadTexts:
    cIpCapV320CRS1.setProductRelease("Cisco IOS XR 3.2.0 for CRS-1")
if mibBuilder.loadTexts:
    cIpCapV320CRS1.setStatus(
        "current"
    )

cIpCapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 2)
)
if mibBuilder.loadTexts:
    cIpCapACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    cIpCapACSWV03R000.setStatus(
        "current"
    )

cIpCapCTSV100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 3)
)
if mibBuilder.loadTexts:
    cIpCapCTSV100.setProductRelease("Cisco TelePresence System (CTS) 1.0.0")
if mibBuilder.loadTexts:
    cIpCapCTSV100.setStatus(
        "current"
    )

cIpCapCTMV1000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 4)
)
if mibBuilder.loadTexts:
    cIpCapCTMV1000.setProductRelease("Cisco TelePresence Manager (CTM) 1.0.0.0")
if mibBuilder.loadTexts:
    cIpCapCTMV1000.setStatus(
        "current"
    )

cIpCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 5)
)
if mibBuilder.loadTexts:
    cIpCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance""")
if mibBuilder.loadTexts:
    cIpCapc4710aceVA1R700.setStatus(
        "current"
    )

ciscoIpCapabilityV12R2SE = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 445, 6)
)
if mibBuilder.loadTexts:
    ciscoIpCapabilityV12R2SE.setProductRelease("Cisco IOS 12.2SE Catalyst 2k/3k Series.")
if mibBuilder.loadTexts:
    ciscoIpCapabilityV12R2SE.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-CAPABILITY",
    **{"ciscoIpCapability": ciscoIpCapability,
       "cIpCapV320CRS1": cIpCapV320CRS1,
       "cIpCapACSWV03R000": cIpCapACSWV03R000,
       "cIpCapCTSV100": cIpCapCTSV100,
       "cIpCapCTMV1000": cIpCapCTMV1000,
       "cIpCapc4710aceVA1R700": cIpCapc4710aceVA1R700,
       "ciscoIpCapabilityV12R2SE": ciscoIpCapabilityV12R2SE}
)
