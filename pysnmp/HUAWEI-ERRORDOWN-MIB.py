# SNMP MIB module (HUAWEI-ERRORDOWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ERRORDOWN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:45 2024
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

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwErrordownMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257)
)
hwErrordownMIB.setRevisions(
        ("2011-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwErrordownObjects_ObjectIdentity = ObjectIdentity
hwErrordownObjects = _HwErrordownObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1)
)
_HwErrordownCause_Type = DisplayString
_HwErrordownCause_Object = MibScalar
hwErrordownCause = _HwErrordownCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 1),
    _HwErrordownCause_Type()
)
hwErrordownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwErrordownCause.setStatus("current")
_HwErrordownRecoverType_Type = DisplayString
_HwErrordownRecoverType_Object = MibScalar
hwErrordownRecoverType = _HwErrordownRecoverType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 1, 2),
    _HwErrordownRecoverType_Type()
)
hwErrordownRecoverType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwErrordownRecoverType.setStatus("current")
_HwErrordownNotifications_ObjectIdentity = ObjectIdentity
hwErrordownNotifications = _HwErrordownNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2)
)
_HwErrordownConformance_ObjectIdentity = ObjectIdentity
hwErrordownConformance = _HwErrordownConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3)
)
_HwErrordownCompliances_ObjectIdentity = ObjectIdentity
hwErrordownCompliances = _HwErrordownCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1)
)
_HwErrordownGroups_ObjectIdentity = ObjectIdentity
hwErrordownGroups = _HwErrordownGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2)
)

# Managed Objects groups

hwErrordownObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 1)
)
hwErrordownObjectGroup.setObjects(
      *(("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"),
        ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
)
if mibBuilder.loadTexts:
    hwErrordownObjectGroup.setStatus("current")


# Notification objects

hwErrordown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 1)
)
hwErrordown.setObjects(
      *(("IF-MIB", "ifName"),
        ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"))
)
if mibBuilder.loadTexts:
    hwErrordown.setStatus(
        "current"
    )

hwErrordownRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 2, 2)
)
hwErrordownRecovery.setObjects(
      *(("IF-MIB", "ifName"),
        ("HUAWEI-ERRORDOWN-MIB", "hwErrordownCause"),
        ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecoverType"))
)
if mibBuilder.loadTexts:
    hwErrordownRecovery.setStatus(
        "current"
    )


# Notifications groups

hwErrordownNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 2, 2)
)
hwErrordownNotificationGroup.setObjects(
      *(("HUAWEI-ERRORDOWN-MIB", "hwErrordown"),
        ("HUAWEI-ERRORDOWN-MIB", "hwErrordownRecovery"))
)
if mibBuilder.loadTexts:
    hwErrordownNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwErrordowFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 257, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwErrordowFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ERRORDOWN-MIB",
    **{"hwErrordownMIB": hwErrordownMIB,
       "hwErrordownObjects": hwErrordownObjects,
       "hwErrordownCause": hwErrordownCause,
       "hwErrordownRecoverType": hwErrordownRecoverType,
       "hwErrordownNotifications": hwErrordownNotifications,
       "hwErrordown": hwErrordown,
       "hwErrordownRecovery": hwErrordownRecovery,
       "hwErrordownConformance": hwErrordownConformance,
       "hwErrordownCompliances": hwErrordownCompliances,
       "hwErrordowFullCompliance": hwErrordowFullCompliance,
       "hwErrordownGroups": hwErrordownGroups,
       "hwErrordownObjectGroup": hwErrordownObjectGroup,
       "hwErrordownNotificationGroup": hwErrordownNotificationGroup}
)
