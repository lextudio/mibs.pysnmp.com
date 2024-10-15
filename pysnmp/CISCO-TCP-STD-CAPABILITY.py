# SNMP MIB module (CISCO-TCP-STD-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TCP-STD-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:35 2024
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

ciscoTcpStdCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 481)
)
ciscoTcpStdCapability.setRevisions(
        ("2008-08-11 00:00",
         "2008-02-08 00:00",
         "2006-11-08 00:00",
         "2006-10-25 00:00",
         "2006-05-26 00:00",
         "2006-02-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoTcpStdCapIOSXRV3R2CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 1)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapIOSXRV3R2CRS1.setProductRelease("Cisco IOS XR 3.2.0 for CRS-1")
if mibBuilder.loadTexts:
    ciscoTcpStdCapIOSXRV3R2CRS1.setStatus(
        "current"
    )

ciscoTcpStdCapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 2)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapACSWV03R000.setProductRelease("""\
ACSW (Application Control Software) 3.0

                    for Application Control Engine(ACE)

                    Service Module.""")
if mibBuilder.loadTexts:
    ciscoTcpStdCapACSWV03R000.setStatus(
        "current"
    )

ciscoTcpStdCapCTSV100 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 3)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapCTSV100.setProductRelease("Cisco TelePresence System (CTS) 1.0.0.")
if mibBuilder.loadTexts:
    ciscoTcpStdCapCTSV100.setStatus(
        "current"
    )

ciscoTcpStdCapCTMV1000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 4)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapCTMV1000.setProductRelease("Cisco TelePresence Manager (CTM) 1.0.0.0.")
if mibBuilder.loadTexts:
    ciscoTcpStdCapCTMV1000.setStatus(
        "current"
    )

ciscoTcpStdCapIOSXRV3R4CRS1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 5)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapIOSXRV3R4CRS1.setProductRelease("Cisco IOS XR 3.4 for CRS-1")
if mibBuilder.loadTexts:
    ciscoTcpStdCapIOSXRV3R4CRS1.setStatus(
        "current"
    )

ciscoTcpStdCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 481, 6)
)
if mibBuilder.loadTexts:
    ciscoTcpStdCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance.""")
if mibBuilder.loadTexts:
    ciscoTcpStdCapc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TCP-STD-CAPABILITY",
    **{"ciscoTcpStdCapability": ciscoTcpStdCapability,
       "ciscoTcpStdCapIOSXRV3R2CRS1": ciscoTcpStdCapIOSXRV3R2CRS1,
       "ciscoTcpStdCapACSWV03R000": ciscoTcpStdCapACSWV03R000,
       "ciscoTcpStdCapCTSV100": ciscoTcpStdCapCTSV100,
       "ciscoTcpStdCapCTMV1000": ciscoTcpStdCapCTMV1000,
       "ciscoTcpStdCapIOSXRV3R4CRS1": ciscoTcpStdCapIOSXRV3R4CRS1,
       "ciscoTcpStdCapc4710aceVA1R700": ciscoTcpStdCapc4710aceVA1R700}
)
