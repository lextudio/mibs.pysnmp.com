# SNMP MIB module (HUAWEI-DAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:25 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwDadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 575),
    )



# MIB Managed Objects in the order of their OIDs

_HwDadTraps_ObjectIdentity = ObjectIdentity
hwDadTraps = _HwDadTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1)
)
_HwDadConformance_ObjectIdentity = ObjectIdentity
hwDadConformance = _HwDadConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2)
)
_HwDadCompliances_ObjectIdentity = ObjectIdentity
hwDadCompliances = _HwDadCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1)
)
_HwDadGroups_ObjectIdentity = ObjectIdentity
hwDadGroups = _HwDadGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2)
)

# Managed Objects groups


# Notification objects

hwDadConflictDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 1)
)
if mibBuilder.loadTexts:
    hwDadConflictDetect.setStatus(
        "current"
    )

hwDadConflictResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 1, 2)
)
if mibBuilder.loadTexts:
    hwDadConflictResume.setStatus(
        "current"
    )


# Notifications groups

hwDadTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 2, 1)
)
hwDadTrapGroup.setObjects(
      *(("HUAWEI-DAD-MIB", "hwDadConflictDetect"),
        ("HUAWEI-DAD-MIB", "hwDadConflictResume"))
)
if mibBuilder.loadTexts:
    hwDadTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwDadCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 246, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwDadCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DAD-MIB",
    **{"PortIndex": PortIndex,
       "hwDadMIB": hwDadMIB,
       "hwDadTraps": hwDadTraps,
       "hwDadConflictDetect": hwDadConflictDetect,
       "hwDadConflictResume": hwDadConflictResume,
       "hwDadConformance": hwDadConformance,
       "hwDadCompliances": hwDadCompliances,
       "hwDadCompliance": hwDadCompliance,
       "hwDadGroups": hwDadGroups,
       "hwDadTrapGroup": hwDadTrapGroup}
)
