# SNMP MIB module (Juniper-SONET-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SONET-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:21 2024
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

juniSonetAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40)
)
juniSonetAgent.setRevisions(
        ("2005-09-15 20:26",
         "2003-07-16 17:22",
         "2003-01-31 20:09",
         "2002-04-09 23:44",
         "2002-02-04 21:35",
         "2001-04-03 22:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniSonetBasicAgent_ObjectIdentity = ObjectIdentity
juniSonetBasicAgent = _JuniSonetBasicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5)
)
_JuniSonetVTAgent_ObjectIdentity = ObjectIdentity
juniSonetVTAgent = _JuniSonetVTAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniSonetAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 1)
)
if mibBuilder.loadTexts:
    juniSonetAgentV1.setProductRelease("""\
Version 1 of the SONET component of the JUNOSe SNMP agent.  This
        version of the SONET component was supported in JUNOSe 1.x system
        releases.""")
if mibBuilder.loadTexts:
    juniSonetAgentV1.setStatus(
        "obsolete"
    )

juniSonetAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 2)
)
if mibBuilder.loadTexts:
    juniSonetAgentV2.setProductRelease("""\
Version 2 of the SONET component of the JUNOSe SNMP agent.  This
        version of the SONET component was supported in JUNOSe 2.x system
        releases.""")
if mibBuilder.loadTexts:
    juniSonetAgentV2.setStatus(
        "obsolete"
    )

juniSonetAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 3)
)
if mibBuilder.loadTexts:
    juniSonetAgentV3.setProductRelease("""\
Version 3 of the SONET component of the JUNOSe SNMP agent.  This
        version of the SONET component was supported in JUNOSe 3.0 and 3.1
        system releases.""")
if mibBuilder.loadTexts:
    juniSonetAgentV3.setStatus(
        "obsolete"
    )

juniSonetAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 4)
)
if mibBuilder.loadTexts:
    juniSonetAgentV4.setProductRelease("""\
Version 4 of the SONET component of the JUNOSe SNMP agent.  This
        version of the SONET component was supported in JUNOSe 3.2 system
        releases.""")
if mibBuilder.loadTexts:
    juniSonetAgentV4.setStatus(
        "obsolete"
    )

juniSonetBasicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 1)
)
if mibBuilder.loadTexts:
    juniSonetBasicAgentV1.setProductRelease("""\
Version 1 of the basic SONET component of the JUNOSe SNMP agent.  It
        does not include Virtual Tributary (VT) support.  This version of the
        basic SONET component was supported in JUNOSe 3.3 and subsequent 3.x
        system releases.""")
if mibBuilder.loadTexts:
    juniSonetBasicAgentV1.setStatus(
        "obsolete"
    )

juniSonetBasicAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 2)
)
if mibBuilder.loadTexts:
    juniSonetBasicAgentV2.setProductRelease("""\
Version 2 of the basic SONET component of the JUNOSe SNMP agent.  It
        does not include Virtual Tributary (VT) support.  This version of the
        basic SONET component was supported in JUNOSe 4.x system releases.""")
if mibBuilder.loadTexts:
    juniSonetBasicAgentV2.setStatus(
        "obsolete"
    )

juniSonetBasicAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 3)
)
if mibBuilder.loadTexts:
    juniSonetBasicAgentV3.setProductRelease("""\
Version 3 of the basic SONET component of the JUNOSe SNMP agent.  It
        does not include Virtual Tributary (VT) support.  This version of the
        basic SONET component was supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniSonetBasicAgentV3.setStatus(
        "obsolete"
    )

juniSonetBasicAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 4)
)
if mibBuilder.loadTexts:
    juniSonetBasicAgentV4.setProductRelease("""\
Version 4 of the basic SONET component of the JUNOSe SNMP agent.  It
        does not include Virtual Tributary (VT) support.  This version of the
        basic SONET component is supported in JUNOSe 5.1 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniSonetBasicAgentV4.setStatus(
        "obsolete"
    )

juniSonetBasicAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 5, 5)
)
if mibBuilder.loadTexts:
    juniSonetBasicAgentV5.setProductRelease("""\
Version 5 of the basic SONET component of the JUNOSe SNMP agent.  It
        does not include Virtual Tributary (VT) support.  This version of the
        basic SONET component is supported in JUNOSe 7.2 and subsequent system
        releases.""")
if mibBuilder.loadTexts:
    juniSonetBasicAgentV5.setStatus(
        "current"
    )

juniSonetVTAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 40, 6, 1)
)
if mibBuilder.loadTexts:
    juniSonetVTAgentV1.setProductRelease("""\
Version 1 of the SONET VT component of the JUNOSe SNMP agent.  This
        version of the SONET component is supported in JUNOSe 3.3 and subsequent
        system releases.""")
if mibBuilder.loadTexts:
    juniSonetVTAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SONET-CONF",
    **{"juniSonetAgent": juniSonetAgent,
       "juniSonetAgentV1": juniSonetAgentV1,
       "juniSonetAgentV2": juniSonetAgentV2,
       "juniSonetAgentV3": juniSonetAgentV3,
       "juniSonetAgentV4": juniSonetAgentV4,
       "juniSonetBasicAgent": juniSonetBasicAgent,
       "juniSonetBasicAgentV1": juniSonetBasicAgentV1,
       "juniSonetBasicAgentV2": juniSonetBasicAgentV2,
       "juniSonetBasicAgentV3": juniSonetBasicAgentV3,
       "juniSonetBasicAgentV4": juniSonetBasicAgentV4,
       "juniSonetBasicAgentV5": juniSonetBasicAgentV5,
       "juniSonetVTAgent": juniSonetVTAgent,
       "juniSonetVTAgentV1": juniSonetVTAgentV1}
)
