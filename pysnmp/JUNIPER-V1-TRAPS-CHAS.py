# SNMP MIB module (JUNIPER-V1-TRAPS-CHAS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-V1-TRAPS-CHAS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:24 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniperMIB_ObjectIdentity = ObjectIdentity
juniperMIB = _JuniperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)
_JnxMibs_ObjectIdentity = ObjectIdentity
jnxMibs = _JnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3)
)
_JnxBoxAnatomy_ObjectIdentity = ObjectIdentity
jnxBoxAnatomy = _JnxBoxAnatomy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1)
)
_JnxContentsTable_ObjectIdentity = ObjectIdentity
jnxContentsTable = _JnxContentsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8)
)
_JnxContentsEntry_ObjectIdentity = ObjectIdentity
jnxContentsEntry = _JnxContentsEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1)
)
_JnxContentsContainerIndex_ObjectIdentity = ObjectIdentity
jnxContentsContainerIndex = _JnxContentsContainerIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 1)
)
_JnxContentsL1Index_ObjectIdentity = ObjectIdentity
jnxContentsL1Index = _JnxContentsL1Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 2)
)
_JnxContentsL2Index_ObjectIdentity = ObjectIdentity
jnxContentsL2Index = _JnxContentsL2Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 3)
)
_JnxContentsL3Index_ObjectIdentity = ObjectIdentity
jnxContentsL3Index = _JnxContentsL3Index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 4)
)
_JnxContentsDescr_ObjectIdentity = ObjectIdentity
jnxContentsDescr = _JnxContentsDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 6)
)

# Managed Objects groups


# Notification objects

jnxPowerSupplyFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 1)
)
jnxPowerSupplyFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxPowerSupplyFailureV1.setStatus(
        ""
    )

jnxFanFailureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 2)
)
jnxFanFailureV1.setObjects(
      *(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxFanFailureV1.setStatus(
        ""
    )

jnxOverTemperatureV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 0, 3)
)
jnxOverTemperatureV1.setObjects(
      *(("JUNIPER-V1-TRAPS-CHAS", "jnxContentsContainerIndex"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL1Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL2Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsL3Index"),
        ("JUNIPER-V1-TRAPS-CHAS", "jnxContentsDescr"))
)
if mibBuilder.loadTexts:
    jnxOverTemperatureV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-V1-TRAPS-CHAS",
    **{"juniperMIB": juniperMIB,
       "jnxPowerSupplyFailureV1": jnxPowerSupplyFailureV1,
       "jnxFanFailureV1": jnxFanFailureV1,
       "jnxOverTemperatureV1": jnxOverTemperatureV1,
       "jnxMibs": jnxMibs,
       "jnxBoxAnatomy": jnxBoxAnatomy,
       "jnxContentsTable": jnxContentsTable,
       "jnxContentsEntry": jnxContentsEntry,
       "jnxContentsContainerIndex": jnxContentsContainerIndex,
       "jnxContentsL1Index": jnxContentsL1Index,
       "jnxContentsL2Index": jnxContentsL2Index,
       "jnxContentsL3Index": jnxContentsL3Index,
       "jnxContentsDescr": jnxContentsDescr}
)
