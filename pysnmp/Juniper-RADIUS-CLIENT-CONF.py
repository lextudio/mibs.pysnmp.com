# SNMP MIB module (Juniper-RADIUS-CLIENT-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-RADIUS-CLIENT-CONF
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

juniRadiusClientAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35)
)
juniRadiusClientAgent.setRevisions(
        ("2009-02-10 15:20",
         "2007-12-14 15:00",
         "2007-09-18 18:22",
         "2007-04-10 01:03",
         "2006-02-17 22:00",
         "2006-01-12 22:00",
         "2004-12-06 02:32",
         "2004-12-03 22:12",
         "2003-12-18 21:03",
         "2003-05-21 19:18",
         "2003-03-10 19:51",
         "2003-01-27 18:36",
         "2002-11-21 19:26",
         "2001-10-19 14:44",
         "2001-10-16 20:45",
         "2001-09-07 12:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniRadiusClientDynamicAgent_ObjectIdentity = ObjectIdentity
juniRadiusClientDynamicAgent = _JuniRadiusClientDynamicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgent.setStatus("current")
_JuniRadiusClientBasicAgent_ObjectIdentity = ObjectIdentity
juniRadiusClientBasicAgent = _JuniRadiusClientBasicAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2)
)
if mibBuilder.loadTexts:
    juniRadiusClientBasicAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniRadiusClientDynamicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV1.setProductRelease("""\
Version 1 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 1.x system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV1.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV2.setProductRelease("""\
Version 2 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 2.x system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV2.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV3.setProductRelease("""\
Version 3 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 3.0 system release.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV3.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 4)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV4.setProductRelease("""\
Version 4 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 3.1 system release.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV4.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 5)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV5.setProductRelease("""\
Version 5 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 3.2 system release.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV5.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 6)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV6.setProductRelease("""\
Version 6 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 3.3 and subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV6.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 7)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV7.setProductRelease("""\
Version 7 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV7.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 8)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV8.setProductRelease("""\
Version 8 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 4.1 system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV8.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 9)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV9.setProductRelease("""\
Version 9 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV9.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 10)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV10.setProductRelease("""\
Version 10 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 5.1 system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV10.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 11)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV11.setProductRelease("""\
Version 11 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component was
        supported in JUNOSe 5.2 system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV11.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 12)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV12.setProductRelease("""\
Version 12 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  These capabilities became obsolete when a new
        B-RAS object was added.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV12.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV13 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 13)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV13.setProductRelease("""\
Version 13 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 6.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV13.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV14 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 14)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV14.setProductRelease("""\
Version 14 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 6.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV14.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV15 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 15)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV15.setProductRelease("""\
Version 15 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 6.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV15.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV16 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 16)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV16.setProductRelease("""\
Version 16 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 7.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV16.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV17 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 17)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV17.setProductRelease("""\
Version 17 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 7.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV17.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV18 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 18)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV18.setProductRelease("""\
Version 18 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 8.1.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV18.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV19 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 19)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV19.setProductRelease("""\
Version 19 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 8.2.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV19.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV20 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 20)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV20.setProductRelease("""\
Version 20 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 9.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV20.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV21 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 21)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV21.setProductRelease("""\
Version 21 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 10.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV21.setStatus(
        "obsolete"
    )

juniRadiusClientDynamicAgentV22 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 1, 22)
)
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV22.setProductRelease("""\
Version 22 of the RADIUS Client dynamic interface component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 10.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientDynamicAgentV22.setStatus(
        "current"
    )

juniRadiusClientBasicAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 35, 2, 1)
)
if mibBuilder.loadTexts:
    juniRadiusClientBasicAgentV1.setProductRelease("""\
Version 1 of the basic authentication RADIUS Client component of the
        JUNOSe SNMP agent.  This version of the RADIUS Client component is
        supported in JUNOSe 3.2 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniRadiusClientBasicAgentV1.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-RADIUS-CLIENT-CONF",
    **{"juniRadiusClientAgent": juniRadiusClientAgent,
       "juniRadiusClientDynamicAgent": juniRadiusClientDynamicAgent,
       "juniRadiusClientDynamicAgentV1": juniRadiusClientDynamicAgentV1,
       "juniRadiusClientDynamicAgentV2": juniRadiusClientDynamicAgentV2,
       "juniRadiusClientDynamicAgentV3": juniRadiusClientDynamicAgentV3,
       "juniRadiusClientDynamicAgentV4": juniRadiusClientDynamicAgentV4,
       "juniRadiusClientDynamicAgentV5": juniRadiusClientDynamicAgentV5,
       "juniRadiusClientDynamicAgentV6": juniRadiusClientDynamicAgentV6,
       "juniRadiusClientDynamicAgentV7": juniRadiusClientDynamicAgentV7,
       "juniRadiusClientDynamicAgentV8": juniRadiusClientDynamicAgentV8,
       "juniRadiusClientDynamicAgentV9": juniRadiusClientDynamicAgentV9,
       "juniRadiusClientDynamicAgentV10": juniRadiusClientDynamicAgentV10,
       "juniRadiusClientDynamicAgentV11": juniRadiusClientDynamicAgentV11,
       "juniRadiusClientDynamicAgentV12": juniRadiusClientDynamicAgentV12,
       "juniRadiusClientDynamicAgentV13": juniRadiusClientDynamicAgentV13,
       "juniRadiusClientDynamicAgentV14": juniRadiusClientDynamicAgentV14,
       "juniRadiusClientDynamicAgentV15": juniRadiusClientDynamicAgentV15,
       "juniRadiusClientDynamicAgentV16": juniRadiusClientDynamicAgentV16,
       "juniRadiusClientDynamicAgentV17": juniRadiusClientDynamicAgentV17,
       "juniRadiusClientDynamicAgentV18": juniRadiusClientDynamicAgentV18,
       "juniRadiusClientDynamicAgentV19": juniRadiusClientDynamicAgentV19,
       "juniRadiusClientDynamicAgentV20": juniRadiusClientDynamicAgentV20,
       "juniRadiusClientDynamicAgentV21": juniRadiusClientDynamicAgentV21,
       "juniRadiusClientDynamicAgentV22": juniRadiusClientDynamicAgentV22,
       "juniRadiusClientBasicAgent": juniRadiusClientBasicAgent,
       "juniRadiusClientBasicAgentV1": juniRadiusClientBasicAgentV1}
)
