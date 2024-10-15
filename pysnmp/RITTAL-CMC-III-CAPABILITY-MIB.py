# SNMP MIB module (RITTAL-CMC-III-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RITTAL-CMC-III-CAPABILITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:38 2024
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

(cmcIII,) = mibBuilder.importSymbols(
    "RITTAL-CMC-III-MIB",
    "cmcIII")

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

cmcIIICapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2606, 7, 8)
)
cmcIIICapability.setRevisions(
        ("2015-10-27 00:00",
         "2014-10-06 00:00",
         "2013-03-30 00:00",
         "2012-08-30 00:00",
         "2011-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

cmcIIIPuCapsV102 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2606, 7, 8, 30102)
)
if mibBuilder.loadTexts:
    cmcIIIPuCapsV102.setProductRelease("V1.02")
if mibBuilder.loadTexts:
    cmcIIIPuCapsV102.setStatus(
        "current"
    )

cmcIIIPuCapsV103 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2606, 7, 8, 30103)
)
if mibBuilder.loadTexts:
    cmcIIIPuCapsV103.setProductRelease("V1.03")
if mibBuilder.loadTexts:
    cmcIIIPuCapsV103.setStatus(
        "current"
    )

cmcIIIPuCapsV104 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2606, 7, 8, 30104)
)
if mibBuilder.loadTexts:
    cmcIIIPuCapsV104.setProductRelease("V1.04")
if mibBuilder.loadTexts:
    cmcIIIPuCapsV104.setStatus(
        "current"
    )

cmcIIIPduCapsV104 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 2606, 7, 8, 34104)
)
if mibBuilder.loadTexts:
    cmcIIIPduCapsV104.setProductRelease("V1.04")
if mibBuilder.loadTexts:
    cmcIIIPduCapsV104.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RITTAL-CMC-III-CAPABILITY-MIB",
    **{"cmcIIICapability": cmcIIICapability,
       "cmcIIIPuCapsV102": cmcIIIPuCapsV102,
       "cmcIIIPuCapsV103": cmcIIIPuCapsV103,
       "cmcIIIPuCapsV104": cmcIIIPuCapsV104,
       "cmcIIIPduCapsV104": cmcIIIPduCapsV104}
)
