# SNMP MIB module (CISCO-WAN-RSRC-PART-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-RSRC-PART-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:15 2024
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

ciscoWanRsrcPartCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 260)
)
ciscoWanRsrcPartCapability.setRevisions(
        ("2005-04-26 00:00",
         "2004-09-29 00:00",
         "2003-11-13 00:00",
         "2002-11-11 00:00",
         "2002-03-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cwRsrcPartCapabilityV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 1)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV2R00.setProductRelease("""\
MGX8850 Release 2.0.00
                          and Release 2.1.00""")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV2R00.setStatus(
        "current"
    )

cwRsrcPartCapabilityRpmV2R0160 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 2)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityRpmV2R0160.setProductRelease("MGX8850 Release 2.1.60")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityRpmV2R0160.setStatus(
        "current"
    )

cwRsrcPartCapabilityRpmxfV12R02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 3)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityRpmxfV12R02.setProductRelease("""\
IOS Release 12.2.
                          MGX8850 Release 3.0.00.""")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityRpmxfV12R02.setStatus(
        "current"
    )

cwRsrcPartCapabilityV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 4)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV4R00.setProductRelease("MGX8850 Release 4.0.00")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV4R00.setStatus(
        "current"
    )

cwRsrcPartCapabilityV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 5)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV5R00.setProductRelease("MGX8850 Release 5.0.0")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityV5R00.setStatus(
        "current"
    )

cwRsrcPartCapabilityAxsmeV2R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 6)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV2R00.setProductRelease("""\
MGX8850 Release 2.0.00
                          and Release 2.1.00""")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV2R00.setStatus(
        "current"
    )

cwRsrcPartCapabilityAxsmeV4R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 7)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV4R00.setProductRelease("MGX8850 Release 4.0.00")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV4R00.setStatus(
        "current"
    )

cwRsrcPartCapabilityAxsmeV5R00 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 260, 8)
)
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV5R00.setProductRelease("MGX8850 Release 5.0.00")
if mibBuilder.loadTexts:
    cwRsrcPartCapabilityAxsmeV5R00.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-RSRC-PART-CAPABILITY",
    **{"ciscoWanRsrcPartCapability": ciscoWanRsrcPartCapability,
       "cwRsrcPartCapabilityV2R00": cwRsrcPartCapabilityV2R00,
       "cwRsrcPartCapabilityRpmV2R0160": cwRsrcPartCapabilityRpmV2R0160,
       "cwRsrcPartCapabilityRpmxfV12R02": cwRsrcPartCapabilityRpmxfV12R02,
       "cwRsrcPartCapabilityV4R00": cwRsrcPartCapabilityV4R00,
       "cwRsrcPartCapabilityV5R00": cwRsrcPartCapabilityV5R00,
       "cwRsrcPartCapabilityAxsmeV2R00": cwRsrcPartCapabilityAxsmeV2R00,
       "cwRsrcPartCapabilityAxsmeV4R00": cwRsrcPartCapabilityAxsmeV4R00,
       "cwRsrcPartCapabilityAxsmeV5R00": cwRsrcPartCapabilityAxsmeV5R00}
)
