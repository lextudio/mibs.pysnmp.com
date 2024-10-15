# SNMP MIB module (Juniper-AAA-Server-CONF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-AAA-Server-CONF
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:36 2024
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

juniAaaServerAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1)
)
juniAaaServerAgent.setRevisions(
        ("2008-10-24 09:16",
         "2008-09-04 10:34",
         "2008-06-05 03:48",
         "2007-10-23 19:34",
         "2007-10-04 01:33",
         "2007-07-31 19:34",
         "2006-08-02 18:34",
         "2006-04-26 18:52",
         "2005-09-16 15:58",
         "2005-03-24 18:37",
         "2004-12-14 18:37",
         "2004-12-03 22:12",
         "2004-05-20 21:33",
         "2004-07-26 17:02",
         "2003-03-07 20:51",
         "2002-12-02 18:44",
         "2002-08-16 15:10",
         "2002-05-13 19:32",
         "2002-01-03 20:30",
         "2001-09-18 21:13",
         "2001-04-10 14:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniAaaServerBaseAgent_ObjectIdentity = ObjectIdentity
juniAaaServerBaseAgent = _JuniAaaServerBaseAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniAaaServerBaseAgent.setStatus("current")
_JuniAaaServerBrasAgent_ObjectIdentity = ObjectIdentity
juniAaaServerBrasAgent = _JuniAaaServerBrasAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgent.setStatus("current")
_JuniAaaServerTunnelAgent_ObjectIdentity = ObjectIdentity
juniAaaServerTunnelAgent = _JuniAaaServerTunnelAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgent.setStatus("current")
_JuniAaaServerAccountingAgent_ObjectIdentity = ObjectIdentity
juniAaaServerAccountingAgent = _JuniAaaServerAccountingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgent.setStatus("current")
_JuniAaaServerAddressAgent_ObjectIdentity = ObjectIdentity
juniAaaServerAddressAgent = _JuniAaaServerAddressAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    juniAaaServerAddressAgent.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

juniAaaServerAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerAgentV1.setProductRelease("""\
Version 1 of the AAA Server component of the JUNOSe SNMP agent.  This
        version was supported in JUNOSe 1.x system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerAgentV2.setProductRelease("""\
Version 2 of the AAA Server component of the JUNOSe SNMP agent.  This
        version was supported in JUNOSe 2.x system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAgentV2.setStatus(
        "obsolete"
    )

juniAaaServerAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniAaaServerAgentV3.setProductRelease("""\
Version 3 of the AAA Server component of the JUNOSe SNMP agent.  This
        version was supported in JUNOSe 3.0 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAgentV3.setStatus(
        "obsolete"
    )

juniAaaServerAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniAaaServerAgentV4.setProductRelease("""\
Version 4 of the AAA Server component of the JUNOSe SNMP
        agent.  This version was supported in JUNOSe 3.1 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAgentV4.setStatus(
        "obsolete"
    )

juniAaaServerAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniAaaServerAgentV5.setProductRelease("""\
Version 5 of the AAA Server component of the JUNOSe SNMP agent.  This
        version was supported in JUNOSe 3.2 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAgentV5.setStatus(
        "obsolete"
    )

juniAaaServerBaseAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV1.setProductRelease("""\
Version 1 of the basic AAA Server component of the JUNOSe SNMP agent.
        This version is supported in JUNOSe 3.3 through 5.2.""")
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerBaseAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV2.setProductRelease("""\
Version 2 of the basic AAA Server component of the JUNOSe SNMP agent.
        This version is supported in JUNOSe 5.3 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV2.setStatus(
        "obsolete"
    )

juniAaaServerBaseAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV3.setProductRelease("""\
Version 3 of the basic AAA Server component of the JUNOSe SNMP agent.
        This version is supported in JUNOSe 6.1 and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBaseAgentV3.setStatus(
        "current"
    )

juniAaaServerBrasAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV1.setProductRelease("""\
Version 1 of the B-RAS option of the AAA Server component of the JUNOSe
        SNMP agent.  This version was supported in JUNOSe 3.3 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV2.setProductRelease("""\
Version 2 of the B-RAS option of the AAA Server component of the JUNOSe
        SNMP agent.  This version was supported in JUNOSe 3.4 and subsequent 3.x
        system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV2.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV3.setProductRelease("""\
Version 3 of the B-RAS option of the AAA Server component of the JUNOSe
        SNMP agent.  This version was supported in JUNOSe 4.0 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV3.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV4.setProductRelease("""\
Version 4 of the B-RAS option of the AAA Server component of the JUNOSe
        SNMP agent.  This version was supported in JUNOSe 4.1 and subsequent 4.x
        system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV4.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV5.setProductRelease("""\
Version 5 of the B-RAS option of the AAA Server component of the JUNOSe
        SNMP agent.  This version was supported in JUNOSe 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV5.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 6)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV6.setProductRelease("""\
Version 6 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV6.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV7 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 7)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV7.setProductRelease("""\
Version 7 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV7.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV8 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 8)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV8.setProductRelease("""\
Obsolete Version 8 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV8.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV9 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 9)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV9.setProductRelease("""\
Obsolete Version 9 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV9.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV10 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 10)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV10.setProductRelease("""\
Obsolete Version 10 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV10.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV11 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 11)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV11.setProductRelease("""\
Obsolete Version 11 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV11.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV12 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 12)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV12.setProductRelease("""\
Version 12 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV12.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV13 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 13)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV13.setProductRelease("""\
Version 13 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.3
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV13.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV14 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 14)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV14.setProductRelease("""\
Version 14 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.0
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV14.setStatus(
        "obsolete"
    )

juniAaaServerBrasAgentV15 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 7, 15)
)
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV15.setProductRelease("""\
Version 15 of the B-RAS option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 10.1
        and subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerBrasAgentV15.setStatus(
        "current"
    )

juniAaaServerTunnelAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV1.setProductRelease("""\
Version 1 of the tunneling option of the AAA Server component of the
        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 through 4.0
        system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerTunnelAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV2.setProductRelease("""\
Version 2 of the tunneling option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV2.setStatus(
        "obsolete"
    )

juniAaaServerTunnelAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV3.setProductRelease("""\
Version 3 of the tunneling option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.0 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV3.setStatus(
        "obsolete"
    )

juniAaaServerTunnelAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV4.setProductRelease("""\
Version 4 of the tunneling option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 7.0 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV4.setStatus(
        "obsolete"
    )

juniAaaServerTunnelAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV5.setProductRelease("""\
Version 5 of the tunneling option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 8.0 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerTunnelAgentV5.setStatus(
        "current"
    )

juniAaaServerAccountingAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV1.setProductRelease("""\
Version 1 of the accounting option of the AAA Server component of the
        JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3 and
        subsequent 3.x system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerAccountingAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV2.setProductRelease("""\
Version 2 of the accounting option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 4.0 through
        5.2 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV2.setStatus(
        "obsolete"
    )

juniAaaServerAccountingAgentV3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV3.setProductRelease("""\
Version 3 of the accounting option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 5.3 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV3.setStatus(
        "obsolete"
    )

juniAaaServerAccountingAgentV4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV4.setProductRelease("""\
Version 4 of the accounting option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 6.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV4.setStatus(
        "current"
    )

juniAaaServerAccountingAgentV5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 9, 5)
)
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV5.setProductRelease("""\
Version 5 of the accounting option of the AAA Server component of the
        JUNOSe SNMP agent.  This version is supported in JUNOSe 9.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAccountingAgentV5.setStatus(
        "current"
    )

juniAaaServerAddressAgentV1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    juniAaaServerAddressAgentV1.setProductRelease("""\
Version 1 of the address assignment option of the AAA Server component
        of the JUNOSe SNMP agent.  This version was supported in JUNOSe 3.3
        through 5.0 system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAddressAgentV1.setStatus(
        "obsolete"
    )

juniAaaServerAddressAgentV2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 4874, 5, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    juniAaaServerAddressAgentV2.setProductRelease("""\
Version 2 of the address assignment option of the AAA Server component
        of the JUNOSe SNMP agent.  This version is supported in JUNOSe 5.1 and
        subsequent system releases.""")
if mibBuilder.loadTexts:
    juniAaaServerAddressAgentV2.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-AAA-Server-CONF",
    **{"juniAaaServerAgent": juniAaaServerAgent,
       "juniAaaServerAgentV1": juniAaaServerAgentV1,
       "juniAaaServerAgentV2": juniAaaServerAgentV2,
       "juniAaaServerAgentV3": juniAaaServerAgentV3,
       "juniAaaServerAgentV4": juniAaaServerAgentV4,
       "juniAaaServerAgentV5": juniAaaServerAgentV5,
       "juniAaaServerBaseAgent": juniAaaServerBaseAgent,
       "juniAaaServerBaseAgentV1": juniAaaServerBaseAgentV1,
       "juniAaaServerBaseAgentV2": juniAaaServerBaseAgentV2,
       "juniAaaServerBaseAgentV3": juniAaaServerBaseAgentV3,
       "juniAaaServerBrasAgent": juniAaaServerBrasAgent,
       "juniAaaServerBrasAgentV1": juniAaaServerBrasAgentV1,
       "juniAaaServerBrasAgentV2": juniAaaServerBrasAgentV2,
       "juniAaaServerBrasAgentV3": juniAaaServerBrasAgentV3,
       "juniAaaServerBrasAgentV4": juniAaaServerBrasAgentV4,
       "juniAaaServerBrasAgentV5": juniAaaServerBrasAgentV5,
       "juniAaaServerBrasAgentV6": juniAaaServerBrasAgentV6,
       "juniAaaServerBrasAgentV7": juniAaaServerBrasAgentV7,
       "juniAaaServerBrasAgentV8": juniAaaServerBrasAgentV8,
       "juniAaaServerBrasAgentV9": juniAaaServerBrasAgentV9,
       "juniAaaServerBrasAgentV10": juniAaaServerBrasAgentV10,
       "juniAaaServerBrasAgentV11": juniAaaServerBrasAgentV11,
       "juniAaaServerBrasAgentV12": juniAaaServerBrasAgentV12,
       "juniAaaServerBrasAgentV13": juniAaaServerBrasAgentV13,
       "juniAaaServerBrasAgentV14": juniAaaServerBrasAgentV14,
       "juniAaaServerBrasAgentV15": juniAaaServerBrasAgentV15,
       "juniAaaServerTunnelAgent": juniAaaServerTunnelAgent,
       "juniAaaServerTunnelAgentV1": juniAaaServerTunnelAgentV1,
       "juniAaaServerTunnelAgentV2": juniAaaServerTunnelAgentV2,
       "juniAaaServerTunnelAgentV3": juniAaaServerTunnelAgentV3,
       "juniAaaServerTunnelAgentV4": juniAaaServerTunnelAgentV4,
       "juniAaaServerTunnelAgentV5": juniAaaServerTunnelAgentV5,
       "juniAaaServerAccountingAgent": juniAaaServerAccountingAgent,
       "juniAaaServerAccountingAgentV1": juniAaaServerAccountingAgentV1,
       "juniAaaServerAccountingAgentV2": juniAaaServerAccountingAgentV2,
       "juniAaaServerAccountingAgentV3": juniAaaServerAccountingAgentV3,
       "juniAaaServerAccountingAgentV4": juniAaaServerAccountingAgentV4,
       "juniAaaServerAccountingAgentV5": juniAaaServerAccountingAgentV5,
       "juniAaaServerAddressAgent": juniAaaServerAddressAgent,
       "juniAaaServerAddressAgentV1": juniAaaServerAddressAgentV1,
       "juniAaaServerAddressAgentV2": juniAaaServerAddressAgentV2}
)
