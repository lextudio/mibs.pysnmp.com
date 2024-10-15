# SNMP MIB module (Unisphere-Data-System-Clock-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-System-Clock-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:44 2024
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

(usdNtpAccessGroupGroup,
 usdNtpClientGroup,
 usdNtpPeersGroup,
 usdNtpServerGroup,
 usdNtpSysClockGroup,
 usdSysClockDstGroup,
 usdSysClockTimeGroup) = mibBuilder.importSymbols(
    "Unisphere-Data-System-Clock-MIB",
    "usdNtpAccessGroupGroup",
    "usdNtpClientGroup",
    "usdNtpPeersGroup",
    "usdNtpServerGroup",
    "usdNtpSysClockGroup",
    "usdSysClockDstGroup",
    "usdSysClockTimeGroup")


# MODULE-IDENTITY

usdSysClockAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52)
)
usdSysClockAgent.setRevisions(
        ("2002-04-04 18:47",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

usdSysClockAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1)
)
if mibBuilder.loadTexts:
    usdSysClockAgentV1.setProductRelease("""\
Version 1 of the system clock component of the Unisphere Routing Switch
        SNMP agent.  This version of the system clock component is supported in
        the Unisphere RX 4.0 and subsequent system releases.""")
if mibBuilder.loadTexts:
    usdSysClockAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-System-Clock-CONF",
    **{"usdSysClockAgent": usdSysClockAgent,
       "usdSysClockAgentV1": usdSysClockAgentV1}
)
