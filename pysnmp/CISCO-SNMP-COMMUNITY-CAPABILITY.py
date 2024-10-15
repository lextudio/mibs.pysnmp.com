# SNMP MIB module (CISCO-SNMP-COMMUNITY-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNMP-COMMUNITY-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:31 2024
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

ciscoSnmpCommunityCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 318)
)
ciscoSnmpCommunityCapability.setRevisions(
        ("2008-08-04 00:00",
         "2006-03-29 00:00",
         "2004-01-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cSnmpCommunityCapCatOSV06R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 318, 1)
)
if mibBuilder.loadTexts:
    cSnmpCommunityCapCatOSV06R0301.setProductRelease("Cisco CatOS 6.3(1).")
if mibBuilder.loadTexts:
    cSnmpCommunityCapCatOSV06R0301.setStatus(
        "current"
    )

cSnmpCommunityCapACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 318, 2)
)
if mibBuilder.loadTexts:
    cSnmpCommunityCapACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    cSnmpCommunityCapACSWV03R000.setStatus(
        "current"
    )

cSnmpCommunityCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 318, 3)
)
if mibBuilder.loadTexts:
    cSnmpCommunityCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                    for ACE 4710 Application Control Engine 
                    Appliance""")
if mibBuilder.loadTexts:
    cSnmpCommunityCapc4710aceVA1R700.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNMP-COMMUNITY-CAPABILITY",
    **{"ciscoSnmpCommunityCapability": ciscoSnmpCommunityCapability,
       "cSnmpCommunityCapCatOSV06R0301": cSnmpCommunityCapCatOSV06R0301,
       "cSnmpCommunityCapACSWV03R000": cSnmpCommunityCapACSWV03R000,
       "cSnmpCommunityCapc4710aceVA1R700": cSnmpCommunityCapc4710aceVA1R700}
)
