# SNMP MIB module (CISCO-SSL-PROXY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SSL-PROXY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:47 2024
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

ciscoSslProxyCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 364)
)
ciscoSslProxyCapability.setRevisions(
        ("2008-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoSslProxyCapCat6KV02R01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 364, 1)
)
if mibBuilder.loadTexts:
    ciscoSslProxyCapCat6KV02R01.setProductRelease("Cisco Catalyst 6000 SSL Module Release 2.1")
if mibBuilder.loadTexts:
    ciscoSslProxyCapCat6KV02R01.setStatus(
        "current"
    )

ciscoSslProxyCapACSWV03RA3006 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 364, 2)
)
if mibBuilder.loadTexts:
    ciscoSslProxyCapACSWV03RA3006.setProductRelease("ACSW (Application Control Software) 3.0(0)A3(0.0.6)")
if mibBuilder.loadTexts:
    ciscoSslProxyCapACSWV03RA3006.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SSL-PROXY-CAPABILITY",
    **{"ciscoSslProxyCapability": ciscoSslProxyCapability,
       "ciscoSslProxyCapCat6KV02R01": ciscoSslProxyCapCat6KV02R01,
       "ciscoSslProxyCapACSWV03RA3006": ciscoSslProxyCapACSWV03RA3006}
)
