# SNMP MIB module (CISCO-SNMPv2-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNMPv2-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:39 2024
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

ciscoSnmpV2Capability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 113)
)
ciscoSnmpV2Capability.setRevisions(
        ("2007-11-12 00:00",
         "2006-05-30 00:00",
         "2006-04-24 00:00",
         "2004-03-18 00:00",
         "2002-02-07 00:00",
         "2002-01-31 00:00",
         "1994-08-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSnmpV2CapabilityV10R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 1)
)
if mibBuilder.loadTexts:
    ciscoSnmpV2CapabilityV10R02.setProductRelease("Cisco IOS 10.2")
if mibBuilder.loadTexts:
    ciscoSnmpV2CapabilityV10R02.setStatus(
        "current"
    )

ciscoRpmsSnmpV2CapabilityV20 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 2)
)
if mibBuilder.loadTexts:
    ciscoRpmsSnmpV2CapabilityV20.setProductRelease("Cisco Resource Policy Management Server (RPMS) 2.0")
if mibBuilder.loadTexts:
    ciscoRpmsSnmpV2CapabilityV20.setStatus(
        "current"
    )

ciscoMgxSnmpV2CapabilityV20 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 3)
)
if mibBuilder.loadTexts:
    ciscoMgxSnmpV2CapabilityV20.setProductRelease("MGX8850 Release 2.0.00")
if mibBuilder.loadTexts:
    ciscoMgxSnmpV2CapabilityV20.setStatus(
        "current"
    )

ciscoBpxSesSnmpV2CapabilityV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 4)
)
if mibBuilder.loadTexts:
    ciscoBpxSesSnmpV2CapabilityV10.setProductRelease("Cisco BPX SES Release 1.0.00")
if mibBuilder.loadTexts:
    ciscoBpxSesSnmpV2CapabilityV10.setStatus(
        "current"
    )

ciscoSnmpV2CapCatOSV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 5)
)
if mibBuilder.loadTexts:
    ciscoSnmpV2CapCatOSV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) for Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoSnmpV2CapCatOSV08R0301.setStatus(
        "current"
    )

ciscoSnmpV2CapCatOSV08R0601 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 6)
)
if mibBuilder.loadTexts:
    ciscoSnmpV2CapCatOSV08R0601.setProductRelease("""\
Cisco CatOS 8.6(1) for Catalyst 6000/6500
                          and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoSnmpV2CapCatOSV08R0601.setStatus(
        "current"
    )

ciscoSnmpV2CapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 7)
)
if mibBuilder.loadTexts:
    ciscoSnmpV2CapACSWV03R000.setProductRelease("""\
ACSW (Application Control Software) 3.0
                          for Application Control Engine (ACE) 
                          Service Module.""")
if mibBuilder.loadTexts:
    ciscoSnmpV2CapACSWV03R000.setStatus(
        "current"
    )

ciscoSnmpV2Capc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 113, 8)
)
if mibBuilder.loadTexts:
    ciscoSnmpV2Capc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance.""")
if mibBuilder.loadTexts:
    ciscoSnmpV2Capc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMPv2-CAPABILITY",
    **{"ciscoSnmpV2Capability": ciscoSnmpV2Capability,
       "ciscoSnmpV2CapabilityV10R02": ciscoSnmpV2CapabilityV10R02,
       "ciscoRpmsSnmpV2CapabilityV20": ciscoRpmsSnmpV2CapabilityV20,
       "ciscoMgxSnmpV2CapabilityV20": ciscoMgxSnmpV2CapabilityV20,
       "ciscoBpxSesSnmpV2CapabilityV10": ciscoBpxSesSnmpV2CapabilityV10,
       "ciscoSnmpV2CapCatOSV08R0301": ciscoSnmpV2CapCatOSV08R0301,
       "ciscoSnmpV2CapCatOSV08R0601": ciscoSnmpV2CapCatOSV08R0601,
       "ciscoSnmpV2CapACSWV03R000": ciscoSnmpV2CapACSWV03R000,
       "ciscoSnmpV2Capc4710aceVA1R700": ciscoSnmpV2Capc4710aceVA1R700}
)
