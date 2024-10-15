# SNMP MIB module (CISCO-ENTITY-DIAG-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-DIAG-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:31 2024
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

ciscoEntityDiagCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 529)
)
ciscoEntityDiagCapability.setRevisions(
        ("2010-11-03 00:00",
         "2009-07-02 00:00",
         "2009-06-01 00:00",
         "2008-10-30 00:00",
         "2008-02-29 00:00",
         "2007-07-23 00:00",
         "2007-01-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ceDiagCapCatOSV08R0601Cat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 1)
)
if mibBuilder.loadTexts:
    ceDiagCapCatOSV08R0601Cat6K.setProductRelease("""\
Cisco CatOS 8.6(1) on Catalyst 6000/6500 series 
                     devices with Supervisor 720 or Supervisor 32 
                     present.""")
if mibBuilder.loadTexts:
    ceDiagCapCatOSV08R0601Cat6K.setStatus(
        "current"
    )

ceDiagCapV12R0233SXHPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 2)
)
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXHPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXH on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXHPCat6K.setStatus(
        "current"
    )

ceDiagCapV12R0233SXIPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 3)
)
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXIPCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXIPCat6K.setStatus(
        "current"
    )

ceDiagCapV12R0252SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 4)
)
if mibBuilder.loadTexts:
    ceDiagCapV12R0252SGPCat4K.setProductRelease("""\
Cisco IOS 12.2(52)SG on CAT4K family 
                    switches.""")
if mibBuilder.loadTexts:
    ceDiagCapV12R0252SGPCat4K.setStatus(
        "current"
    )

ceDiagCapV12R0233SXI2PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 5)
)
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXI2PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    ceDiagCapV12R0233SXI2PCat6K.setStatus(
        "current"
    )

ceDiagCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 529, 6)
)
if mibBuilder.loadTexts:
    ceDiagCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                         series devices.""")
if mibBuilder.loadTexts:
    ceDiagCapV12R0250SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-DIAG-CAPABILITY",
    **{"ciscoEntityDiagCapability": ciscoEntityDiagCapability,
       "ceDiagCapCatOSV08R0601Cat6K": ceDiagCapCatOSV08R0601Cat6K,
       "ceDiagCapV12R0233SXHPCat6K": ceDiagCapV12R0233SXHPCat6K,
       "ceDiagCapV12R0233SXIPCat6K": ceDiagCapV12R0233SXIPCat6K,
       "ceDiagCapV12R0252SGPCat4K": ceDiagCapV12R0252SGPCat4K,
       "ceDiagCapV12R0233SXI2PCat6K": ceDiagCapV12R0233SXI2PCat6K,
       "ceDiagCapV12R0250SYPCat6K": ceDiagCapV12R0250SYPCat6K}
)
