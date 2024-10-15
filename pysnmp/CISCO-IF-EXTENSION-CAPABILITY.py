# SNMP MIB module (CISCO-IF-EXTENSION-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-EXTENSION-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:09 2024
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

ciscoIfExtensionCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 395)
)
ciscoIfExtensionCapability.setRevisions(
        ("2015-06-03 00:00",
         "2013-09-05 00:00",
         "2012-03-01 00:00",
         "2011-03-21 00:00",
         "2008-03-24 00:00",
         "2007-11-05 00:00",
         "2007-08-30 00:00",
         "2007-04-19 00:00",
         "2006-02-21 00:00",
         "2005-04-14 00:00",
         "2005-03-04 00:00",
         "2004-01-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ciscoIfExtensionCapV08R0301 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 1)
)
if mibBuilder.loadTexts:
    ciscoIfExtensionCapV08R0301.setProductRelease("""\
Cisco CatOS 8.3(1) on Catalyst 6000/6500 and
                         Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfExtensionCapV08R0301.setStatus(
        "current"
    )

ciscoIfExtCapV12R0217bSXAPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 2)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0217bSXAPCat6K.setProductRelease("""\
Cisco IOS 12.2(17b)SXA on Catalyst 6000/6500
                        and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0217bSXAPCat6K.setStatus(
        "current"
    )

ciscoIfExtCapSanOSV30R1MDS9000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 3)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapSanOSV30R1MDS9000.setProductRelease("""\
Cisco SanOS 3.0 on Cisco MDS 9000
                          series devices.""")
if mibBuilder.loadTexts:
    ciscoIfExtCapSanOSV30R1MDS9000.setStatus(
        "current"
    )

ciscoIfExtCapabilityACSWV03R000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 4)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapabilityACSWV03R000.setProductRelease("ACSW (Application Control Software) 3.0")
if mibBuilder.loadTexts:
    ciscoIfExtCapabilityACSWV03R000.setStatus(
        "current"
    )

ciscoIfExtCapV12R0229SM1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 5)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0229SM1.setProductRelease("Cisco IOS 12.2(29)SM1")
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0229SM1.setStatus(
        "current"
    )

ciscoIfExtCapV12R0412MR1 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 6)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0412MR1.setProductRelease("Cisco IOS 12.4(2)MR1")
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0412MR1.setStatus(
        "current"
    )

ciscoIfExtCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 7)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                    and Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfExtCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

ciscoIfExtCapc4710aceVA1R700 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 8)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapc4710aceVA1R700.setProductRelease("""\
ACSW (Application Control Software) A1(7)
                     for ACE 4710 Application Control Engine 
                     Appliance""")
if mibBuilder.loadTexts:
    ciscoIfExtCapc4710aceVA1R700.setStatus(
        "current"
    )

ciscoIfExtCapCatOSV08R0701PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 9)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapCatOSV08R0701PCat6K.setProductRelease("""\
Cisco CatOS 8.7(1) on Catalyst 6000/6500 and
                     Cisco 7600 series devices.""")
if mibBuilder.loadTexts:
    ciscoIfExtCapCatOSV08R0701PCat6K.setStatus(
        "current"
    )

ciscoIfExtCapNXOSV52R1MDS9000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 10)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapNXOSV52R1MDS9000.setProductRelease("Cisco NXOS 5.2(1) on MDS 9000.")
if mibBuilder.loadTexts:
    ciscoIfExtCapNXOSV52R1MDS9000.setStatus(
        "current"
    )

ciscoIfExtCapV15R0002SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 11)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapV15R0002SGPCat4K.setProductRelease("""\
Cisco IOS 15.0(2)SG on Catalyst 4000 family
                    switches.""")
if mibBuilder.loadTexts:
    ciscoIfExtCapV15R0002SGPCat4K.setStatus(
        "current"
    )

ciscoIfExtCapNxOSV06R0201PMDS9000 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 12)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapNxOSV06R0201PMDS9000.setProductRelease("Cisco NX-OS 6.2(1) on MDS 9000 series devices.")
if mibBuilder.loadTexts:
    ciscoIfExtCapNxOSV06R0201PMDS9000.setStatus(
        "current"
    )

ciscoIfExtCapNxOSV06R0202PN7K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 395, 13)
)
if mibBuilder.loadTexts:
    ciscoIfExtCapNxOSV06R0202PN7K.setProductRelease("Cisco NX-OS 6.2(2) on Nexus 7000 series devices.")
if mibBuilder.loadTexts:
    ciscoIfExtCapNxOSV06R0202PN7K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-EXTENSION-CAPABILITY",
    **{"ciscoIfExtensionCapability": ciscoIfExtensionCapability,
       "ciscoIfExtensionCapV08R0301": ciscoIfExtensionCapV08R0301,
       "ciscoIfExtCapV12R0217bSXAPCat6K": ciscoIfExtCapV12R0217bSXAPCat6K,
       "ciscoIfExtCapSanOSV30R1MDS9000": ciscoIfExtCapSanOSV30R1MDS9000,
       "ciscoIfExtCapabilityACSWV03R000": ciscoIfExtCapabilityACSWV03R000,
       "ciscoIfExtCapV12R0229SM1": ciscoIfExtCapV12R0229SM1,
       "ciscoIfExtCapV12R0412MR1": ciscoIfExtCapV12R0412MR1,
       "ciscoIfExtCapV12R0233SXHPCat6K": ciscoIfExtCapV12R0233SXHPCat6K,
       "ciscoIfExtCapc4710aceVA1R700": ciscoIfExtCapc4710aceVA1R700,
       "ciscoIfExtCapCatOSV08R0701PCat6K": ciscoIfExtCapCatOSV08R0701PCat6K,
       "ciscoIfExtCapNXOSV52R1MDS9000": ciscoIfExtCapNXOSV52R1MDS9000,
       "ciscoIfExtCapV15R0002SGPCat4K": ciscoIfExtCapV15R0002SGPCat4K,
       "ciscoIfExtCapNxOSV06R0201PMDS9000": ciscoIfExtCapNxOSV06R0201PMDS9000,
       "ciscoIfExtCapNxOSV06R0202PN7K": ciscoIfExtCapNxOSV06R0202PN7K}
)
