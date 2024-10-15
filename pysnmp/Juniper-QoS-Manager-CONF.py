# SNMP MIB module (Juniper-QoS-Manager-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-QoS-Manager-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:08 2024
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

(juniAgents,) = mibBuilder.importSymbols(
    "Juniper-Agents",
    "juniAgents")

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

juniQosManagerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50)
)
juniQosManagerAgent.setRevisions(
        ("2004-01-26 14:43",
         "2003-05-08 18:55",
         "2002-09-27 18:03",
         "2001-12-06 16:09")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniQosManagerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 1)
)
if mibBuilder.loadTexts:
    juniQosManagerAgentV1.setProductRelease("""\
Version 1 of the QoS Manager component of the JUNOSe SNMP agent.  This
        version of the QoS Manager component was supported in JUNOSe 4.x system
        releases.""")
if mibBuilder.loadTexts:
    juniQosManagerAgentV1.setStatus(
        "obsolete"
    )

juniQosManagerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 2)
)
if mibBuilder.loadTexts:
    juniQosManagerAgentV2.setProductRelease("""\
Version 2 of the QoS Manager component of the JUNOSe SNMP agent.  This
        version of the QoS Manager component was supported in JUNOSe 5.0 system
        releases.""")
if mibBuilder.loadTexts:
    juniQosManagerAgentV2.setStatus(
        "obsolete"
    )

juniQosManagerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 3)
)
if mibBuilder.loadTexts:
    juniQosManagerAgentV3.setProductRelease("""\
Version 3 of the QoS Manager component of the JUNOSe SNMP agent.  This
        version of the QoS Manager component was supported in JUNOSe 5.1 and
        subsequent 5.x system releases.""")
if mibBuilder.loadTexts:
    juniQosManagerAgentV3.setStatus(
        "obsolete"
    )

juniQosManagerAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 4)
)
if mibBuilder.loadTexts:
    juniQosManagerAgentV4.setProductRelease("""\
Version 4 of the QoS Manager component of the JUNOSe SNMP agent.  This
        version of the QoS Manager component is supported in JUNOSe 6.0 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniQosManagerAgentV4.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-QoS-Manager-CONF",
    **{"juniQosManagerAgent": juniQosManagerAgent,
       "juniQosManagerAgentV1": juniQosManagerAgentV1,
       "juniQosManagerAgentV2": juniQosManagerAgentV2,
       "juniQosManagerAgentV3": juniQosManagerAgentV3,
       "juniQosManagerAgentV4": juniQosManagerAgentV4}
)
