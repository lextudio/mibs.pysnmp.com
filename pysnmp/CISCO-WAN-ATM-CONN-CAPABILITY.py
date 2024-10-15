# SNMP MIB module (CISCO-WAN-ATM-CONN-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-CONN-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:45 2024
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

ciscoWanAtmConnCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 380)
)
ciscoWanAtmConnCapability.setRevisions(
        ("2004-02-07 00:00",
         "2002-03-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cwAtmConnCapabilityAxsmV2R0160 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 1)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmV2R0160.setProductRelease("MGX8850 Release 2.1.60.")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmV2R0160.setStatus(
        "current"
    )

cwAtmConnCapabilityAxsmeV2R0160 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 2)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmeV2R0160.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmeV2R0160.setStatus(
        "current"
    )

cwAtmConnCapabilityRpmprV2R0160 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 3)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmprV2R0160.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmprV2R0160.setStatus(
        "current"
    )

cwAtmConnCapabilityBpxsesV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 4)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityBpxsesV3R00.setProductRelease("BPX SES Release 3.0.00")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityBpxsesV3R00.setStatus(
        "current"
    )

cwAtmConnCapabilityAxsmV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 5)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmV3R00.setProductRelease("MGX8850 Release 3.0.00.")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmV3R00.setStatus(
        "current"
    )

cwAtmConnCapabilityAxsmeV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 6)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmeV3R00.setProductRelease("MGX8850 Release 3.0.00.")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityAxsmeV3R00.setStatus(
        "current"
    )

cwAtmConnCapabilityPxm1eV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 7)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityPxm1eV3R00.setProductRelease("MGX8850 Release 3.0.00.")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityPxm1eV3R00.setStatus(
        "current"
    )

cwAtmConnCapabilityRpmprV3R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 8)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmprV3R00.setProductRelease("MGX8850 Release 3.0.00")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmprV3R00.setStatus(
        "current"
    )

cwAtmConnCapabilityRpmxfV12R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 9)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmxfV12R02.setProductRelease("""\
IOS Release 12.2
                          in MGX8850 Release 3.0.00""")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityRpmxfV12R02.setStatus(
        "current"
    )

cwAtmConnCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 380, 10)
)
if mibBuilder.loadTexts:
    cwAtmConnCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.00.")
if mibBuilder.loadTexts:
    cwAtmConnCapabilityV5R00.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-CONN-CAPABILITY",
    **{"ciscoWanAtmConnCapability": ciscoWanAtmConnCapability,
       "cwAtmConnCapabilityAxsmV2R0160": cwAtmConnCapabilityAxsmV2R0160,
       "cwAtmConnCapabilityAxsmeV2R0160": cwAtmConnCapabilityAxsmeV2R0160,
       "cwAtmConnCapabilityRpmprV2R0160": cwAtmConnCapabilityRpmprV2R0160,
       "cwAtmConnCapabilityBpxsesV3R00": cwAtmConnCapabilityBpxsesV3R00,
       "cwAtmConnCapabilityAxsmV3R00": cwAtmConnCapabilityAxsmV3R00,
       "cwAtmConnCapabilityAxsmeV3R00": cwAtmConnCapabilityAxsmeV3R00,
       "cwAtmConnCapabilityPxm1eV3R00": cwAtmConnCapabilityPxm1eV3R00,
       "cwAtmConnCapabilityRpmprV3R00": cwAtmConnCapabilityRpmprV3R00,
       "cwAtmConnCapabilityRpmxfV12R02": cwAtmConnCapabilityRpmxfV12R02,
       "cwAtmConnCapabilityV5R00": cwAtmConnCapabilityV5R00}
)
