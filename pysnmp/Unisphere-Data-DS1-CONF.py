# SNMP MIB module (Unisphere-Data-DS1-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DS1-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:33 2024
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

(dsx1ConfigEntry,
 dsx1CurrentEntry,
 dsx1FarEndCurrentEntry,
 dsx1FarEndIntervalEntry,
 dsx1FarEndTotalEntry,
 dsx1FracEntry,
 dsx1IntervalEntry,
 dsx1TotalEntry) = mibBuilder.importSymbols(
    "RFC1406-MIB",
    "dsx1ConfigEntry",
    "dsx1CurrentEntry",
    "dsx1FarEndCurrentEntry",
    "dsx1FarEndIntervalEntry",
    "dsx1FarEndTotalEntry",
    "dsx1FracEntry",
    "dsx1IntervalEntry",
    "dsx1TotalEntry")

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

(usDataAgents,) = mibBuilder.importSymbols(
    "Unisphere-Data-Agents",
    "usDataAgents")

(usdDs1Group,
 usdDs1Group1,
 usdDs1Group2,
 usdDs1Group3) = mibBuilder.importSymbols(
    "Unisphere-Data-DS1-MIB",
    "usdDs1Group",
    "usdDs1Group1",
    "usdDs1Group2",
    "usdDs1Group3")


# MODULE-IDENTITY

usdDs1Agent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10)
)
usdDs1Agent.setRevisions(
        ("2002-05-13 16:34",
         "2001-03-29 20:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdDs1AgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 1)
)
if mibBuilder.loadTexts:
    usdDs1AgentV1.setProductRelease("""\
Version 1 of the DS1 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS1 component was supported in the Unisphere
        RX 1.0 system releases.""")
if mibBuilder.loadTexts:
    usdDs1AgentV1.setStatus(
        "obsolete"
    )

usdDs1AgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 2)
)
if mibBuilder.loadTexts:
    usdDs1AgentV2.setProductRelease("""\
Version 2 of the DS1 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS1 component was supported in the Unisphere
        RX 1.1 thru RX 2.x system releases.""")
if mibBuilder.loadTexts:
    usdDs1AgentV2.setStatus(
        "obsolete"
    )

usdDs1AgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 3)
)
if mibBuilder.loadTexts:
    usdDs1AgentV3.setProductRelease("""\
Version 3 of the DS1 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS1 component was supported in the Unisphere
        RX 3.x system releases.""")
if mibBuilder.loadTexts:
    usdDs1AgentV3.setStatus(
        "obsolete"
    )

usdDs1AgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 10, 4)
)
if mibBuilder.loadTexts:
    usdDs1AgentV4.setProductRelease("""\
Version 4 of the DS1 component of the Unisphere Routing Switch SNMP
        agent.  This version of the DS1 component is supported in the Unisphere
        RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdDs1AgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DS1-CONF",
    **{"usdDs1Agent": usdDs1Agent,
       "usdDs1AgentV1": usdDs1AgentV1,
       "usdDs1AgentV2": usdDs1AgentV2,
       "usdDs1AgentV3": usdDs1AgentV3,
       "usdDs1AgentV4": usdDs1AgentV4}
)
