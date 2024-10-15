# SNMP MIB module (HUAWEI-DETECT-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DETECT-ENGINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:28 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

(AutonomousType,
 DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDetectEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308)
)
hwDetectEngineMIB.setRevisions(
        ("2012-08-30 09:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDetectEngineObject_ObjectIdentity = ObjectIdentity
hwDetectEngineObject = _HwDetectEngineObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1)
)
_HwDetectEngineGlobalObjects_ObjectIdentity = ObjectIdentity
hwDetectEngineGlobalObjects = _HwDetectEngineGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1)
)
_HwDetectEngineOAMEnable_Type = EnabledStatus
_HwDetectEngineOAMEnable_Object = MibScalar
hwDetectEngineOAMEnable = _HwDetectEngineOAMEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 1),
    _HwDetectEngineOAMEnable_Type()
)
hwDetectEngineOAMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDetectEngineOAMEnable.setStatus("current")
_HwDetectEngineNQAEnable_Type = EnabledStatus
_HwDetectEngineNQAEnable_Object = MibScalar
hwDetectEngineNQAEnable = _HwDetectEngineNQAEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 1, 1, 2),
    _HwDetectEngineNQAEnable_Type()
)
hwDetectEngineNQAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDetectEngineNQAEnable.setStatus("current")
_HwDetectEngineConformance_ObjectIdentity = ObjectIdentity
hwDetectEngineConformance = _HwDetectEngineConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100)
)
_HwDetectEngineCompliances_ObjectIdentity = ObjectIdentity
hwDetectEngineCompliances = _HwDetectEngineCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1)
)
_HwDetectEngineGroups_ObjectIdentity = ObjectIdentity
hwDetectEngineGroups = _HwDetectEngineGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2)
)

# Managed Objects groups

hwDetectEngineGlobalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 2, 1)
)
hwDetectEngineGlobalObjectGroup.setObjects(
      *(("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineOAMEnable"),
        ("HUAWEI-DETECT-ENGINE-MIB", "hwDetectEngineNQAEnable"))
)
if mibBuilder.loadTexts:
    hwDetectEngineGlobalObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwDetectEngineCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 308, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwDetectEngineCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DETECT-ENGINE-MIB",
    **{"hwDetectEngineMIB": hwDetectEngineMIB,
       "hwDetectEngineObject": hwDetectEngineObject,
       "hwDetectEngineGlobalObjects": hwDetectEngineGlobalObjects,
       "hwDetectEngineOAMEnable": hwDetectEngineOAMEnable,
       "hwDetectEngineNQAEnable": hwDetectEngineNQAEnable,
       "hwDetectEngineConformance": hwDetectEngineConformance,
       "hwDetectEngineCompliances": hwDetectEngineCompliances,
       "hwDetectEngineCompliance": hwDetectEngineCompliance,
       "hwDetectEngineGroups": hwDetectEngineGroups,
       "hwDetectEngineGlobalObjectGroup": hwDetectEngineGlobalObjectGroup}
)
