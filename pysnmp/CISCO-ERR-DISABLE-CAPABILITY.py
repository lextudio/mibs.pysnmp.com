# SNMP MIB module (CISCO-ERR-DISABLE-CAPABILITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ERR-DISABLE-CAPABILITY
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:51 2024
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

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

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

ciscoErrDisableCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 7, 589)
)
ciscoErrDisableCapability.setRevisions(
        ("2013-09-25 00:00",
         "2010-10-29 00:00",
         "2010-05-05 00:00",
         "2010-03-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cErrDisableCapV12R0233SXI4PCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 589, 1)
)
if mibBuilder.loadTexts:
    cErrDisableCapV12R0233SXI4PCat6K.setProductRelease("""\
Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cErrDisableCapV12R0233SXI4PCat6K.setStatus(
        "current"
    )

cErrDisableCapV12R0254SGPCat4K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 589, 2)
)
if mibBuilder.loadTexts:
    cErrDisableCapV12R0254SGPCat4K.setProductRelease("Cisco IOS 12.2(54)SG on CAT4K family switches.")
if mibBuilder.loadTexts:
    cErrDisableCapV12R0254SGPCat4K.setStatus(
        "current"
    )

cErrDisableCapV12R0250SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 589, 3)
)
if mibBuilder.loadTexts:
    cErrDisableCapV12R0250SYPCat6K.setProductRelease("""\
Cisco IOS 12.2(50)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cErrDisableCapV12R0250SYPCat6K.setStatus(
        "current"
    )

cErrDisableCapV15R0102SYPCat6K = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9, 7, 589, 4)
)
if mibBuilder.loadTexts:
    cErrDisableCapV15R0102SYPCat6K.setProductRelease("""\
Cisco IOS 15.1(2)SY on Catalyst 6000/6500
                     series devices.""")
if mibBuilder.loadTexts:
    cErrDisableCapV15R0102SYPCat6K.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ERR-DISABLE-CAPABILITY",
    **{"ciscoErrDisableCapability": ciscoErrDisableCapability,
       "cErrDisableCapV12R0233SXI4PCat6K": cErrDisableCapV12R0233SXI4PCat6K,
       "cErrDisableCapV12R0254SGPCat4K": cErrDisableCapV12R0254SGPCat4K,
       "cErrDisableCapV12R0250SYPCat6K": cErrDisableCapV12R0250SYPCat6K,
       "cErrDisableCapV15R0102SYPCat6K": cErrDisableCapV15R0102SYPCat6K}
)
