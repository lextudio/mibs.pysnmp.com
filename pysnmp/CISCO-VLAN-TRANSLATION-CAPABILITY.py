# SNMP MIB module (CISCO-VLAN-TRANSLATION-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-TRANSLATION-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:08 2024
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

ciscoVlanTranslationCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 405)
)
ciscoVlanTranslationCapability.setRevisions(
        ("2012-01-09 00:00",
         "2006-02-08 00:00",
         "2004-08-11 00:00",
         "2004-06-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cVlanTranslationCapCatOSV08R0401 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 405, 1)
)
if mibBuilder.loadTexts:
    cVlanTranslationCapCatOSV08R0401.setProductRelease("Cisco CatOS 8.4(1).")
if mibBuilder.loadTexts:
    cVlanTranslationCapCatOSV08R0401.setStatus(
        "current"
    )

cVlanTransCapV12R0218SXEPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 405, 2)
)
if mibBuilder.loadTexts:
    cVlanTransCapV12R0218SXEPCat6K.setProductRelease("""\
Cisco IOS 12.2(18)SXE on Catalyst 6000/6500
                         and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    cVlanTransCapV12R0218SXEPCat6K.setStatus(
        "current"
    )

cVlanTransCapV15R0001SYPCat6kSup2T = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 405, 3)
)
if mibBuilder.loadTexts:
    cVlanTransCapV15R0001SYPCat6kSup2T.setProductRelease("""\
Cisco IOS 15.0(1)SY on Catalyst 6000/6500
                     series devices with Supervisor 2T present.""")
if mibBuilder.loadTexts:
    cVlanTransCapV15R0001SYPCat6kSup2T.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-TRANSLATION-CAPABILITY",
    **{"ciscoVlanTranslationCapability": ciscoVlanTranslationCapability,
       "cVlanTranslationCapCatOSV08R0401": cVlanTranslationCapCatOSV08R0401,
       "cVlanTransCapV12R0218SXEPCat6K": cVlanTransCapV12R0218SXEPCat6K,
       "cVlanTransCapV15R0001SYPCat6kSup2T": cVlanTransCapV15R0001SYPCat6kSup2T}
)
