# SNMP MIB module (HUAWEI-GTL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-GTL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:54 2024
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwGtl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwGtlMibObjects_ObjectIdentity = ObjectIdentity
hwGtlMibObjects = _HwGtlMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1)
)


class _HwGtlDefaultValueReason_Type(OctetString):
    """Custom type hwGtlDefaultValueReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwGtlDefaultValueReason_Type.__name__ = "OctetString"
_HwGtlDefaultValueReason_Object = MibScalar
hwGtlDefaultValueReason = _HwGtlDefaultValueReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 1),
    _HwGtlDefaultValueReason_Type()
)
hwGtlDefaultValueReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlDefaultValueReason.setStatus("current")


class _HwGtlResourceItem_Type(OctetString):
    """Custom type hwGtlResourceItem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwGtlResourceItem_Type.__name__ = "OctetString"
_HwGtlResourceItem_Object = MibScalar
hwGtlResourceItem = _HwGtlResourceItem_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 2),
    _HwGtlResourceItem_Type()
)
hwGtlResourceItem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlResourceItem.setStatus("current")


class _HwGtlFeatureName_Type(OctetString):
    """Custom type hwGtlFeatureName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwGtlFeatureName_Type.__name__ = "OctetString"
_HwGtlFeatureName_Object = MibScalar
hwGtlFeatureName = _HwGtlFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 3),
    _HwGtlFeatureName_Type()
)
hwGtlFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlFeatureName.setStatus("current")
_HwGtlRemainTime_Type = Integer32
_HwGtlRemainTime_Object = MibScalar
hwGtlRemainTime = _HwGtlRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 4),
    _HwGtlRemainTime_Type()
)
hwGtlRemainTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlRemainTime.setStatus("current")
_HwGtlVerifyCode_Type = Integer32
_HwGtlVerifyCode_Object = MibScalar
hwGtlVerifyCode = _HwGtlVerifyCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 5),
    _HwGtlVerifyCode_Type()
)
hwGtlVerifyCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlVerifyCode.setStatus("current")


class _HwGtlActive_Type(OctetString):
    """Custom type hwGtlActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 127),
    )


_HwGtlActive_Type.__name__ = "OctetString"
_HwGtlActive_Object = MibScalar
hwGtlActive = _HwGtlActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 6),
    _HwGtlActive_Type()
)
hwGtlActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwGtlActive.setStatus("current")


class _HwGtlShowActLCSName_Type(OctetString):
    """Custom type hwGtlShowActLCSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 127),
    )


_HwGtlShowActLCSName_Type.__name__ = "OctetString"
_HwGtlShowActLCSName_Object = MibScalar
hwGtlShowActLCSName = _HwGtlShowActLCSName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 7),
    _HwGtlShowActLCSName_Type()
)
hwGtlShowActLCSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGtlShowActLCSName.setStatus("current")
_HwGtlItemTable_Object = MibTable
hwGtlItemTable = _HwGtlItemTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8)
)
if mibBuilder.loadTexts:
    hwGtlItemTable.setStatus("current")
_HwGtlItemEntry_Object = MibTableRow
hwGtlItemEntry = _HwGtlItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1)
)
hwGtlItemEntry.setIndexNames(
    (0, "HUAWEI-GTL-MIB", "hwGtlItemIndex"),
)
if mibBuilder.loadTexts:
    hwGtlItemEntry.setStatus("current")
_HwGtlItemIndex_Type = Unsigned32
_HwGtlItemIndex_Object = MibTableColumn
hwGtlItemIndex = _HwGtlItemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 1),
    _HwGtlItemIndex_Type()
)
hwGtlItemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGtlItemIndex.setStatus("current")
_HwGtlItemName_Type = DisplayString
_HwGtlItemName_Object = MibTableColumn
hwGtlItemName = _HwGtlItemName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 2),
    _HwGtlItemName_Type()
)
hwGtlItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGtlItemName.setStatus("current")
_HwGtlItemControlValue_Type = Unsigned32
_HwGtlItemControlValue_Object = MibTableColumn
hwGtlItemControlValue = _HwGtlItemControlValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 3),
    _HwGtlItemControlValue_Type()
)
hwGtlItemControlValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGtlItemControlValue.setStatus("current")
_HwGtlItemUsedValue_Type = Unsigned32
_HwGtlItemUsedValue_Object = MibTableColumn
hwGtlItemUsedValue = _HwGtlItemUsedValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 4),
    _HwGtlItemUsedValue_Type()
)
hwGtlItemUsedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGtlItemUsedValue.setStatus("current")
_HwGtlItemDescription_Type = DisplayString
_HwGtlItemDescription_Object = MibTableColumn
hwGtlItemDescription = _HwGtlItemDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 8, 1, 5),
    _HwGtlItemDescription_Type()
)
hwGtlItemDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGtlItemDescription.setStatus("current")


class _HwGtlChassisID_Type(OctetString):
    """Custom type hwGtlChassisID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwGtlChassisID_Type.__name__ = "OctetString"
_HwGtlChassisID_Object = MibScalar
hwGtlChassisID = _HwGtlChassisID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 1, 9),
    _HwGtlChassisID_Type()
)
hwGtlChassisID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwGtlChassisID.setStatus("current")
_HwGtlNotifications_ObjectIdentity = ObjectIdentity
hwGtlNotifications = _HwGtlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2)
)
_HwGtlConformance_ObjectIdentity = ObjectIdentity
hwGtlConformance = _HwGtlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3)
)
_HwGtlCompliances_ObjectIdentity = ObjectIdentity
hwGtlCompliances = _HwGtlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 1)
)
_HwGtlGroups_ObjectIdentity = ObjectIdentity
hwGtlGroups = _HwGtlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2)
)

# Managed Objects groups

hwGtlObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2, 1)
)
hwGtlObjectGroup.setObjects(
      *(("HUAWEI-GTL-MIB", "hwGtlDefaultValueReason"),
        ("HUAWEI-GTL-MIB", "hwGtlResourceItem"),
        ("HUAWEI-GTL-MIB", "hwGtlFeatureName"),
        ("HUAWEI-GTL-MIB", "hwGtlRemainTime"),
        ("HUAWEI-GTL-MIB", "hwGtlVerifyCode"),
        ("HUAWEI-GTL-MIB", "hwGtlActive"),
        ("HUAWEI-GTL-MIB", "hwGtlShowActLCSName"),
        ("HUAWEI-GTL-MIB", "hwGtlItemName"),
        ("HUAWEI-GTL-MIB", "hwGtlItemControlValue"),
        ("HUAWEI-GTL-MIB", "hwGtlItemUsedValue"),
        ("HUAWEI-GTL-MIB", "hwGtlItemDescription"))
)
if mibBuilder.loadTexts:
    hwGtlObjectGroup.setStatus("current")


# Notification objects

hwGtlDefaultValue = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 1)
)
hwGtlDefaultValue.setObjects(
      *(("HUAWEI-GTL-MIB", "hwGtlDefaultValueReason"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwGtlDefaultValue.setStatus(
        "current"
    )

hwGtlResourceUsedUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 2)
)
hwGtlResourceUsedUp.setObjects(
    ("HUAWEI-GTL-MIB", "hwGtlResourceItem")
)
if mibBuilder.loadTexts:
    hwGtlResourceUsedUp.setStatus(
        "current"
    )

hwGtlNearDeadline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 3)
)
hwGtlNearDeadline.setObjects(
      *(("HUAWEI-GTL-MIB", "hwGtlFeatureName"),
        ("HUAWEI-GTL-MIB", "hwGtlRemainTime"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwGtlNearDeadline.setStatus(
        "current"
    )

hwGtlLicenseVerifyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 4)
)
hwGtlLicenseVerifyFailed.setObjects(
    ("HUAWEI-GTL-MIB", "hwGtlVerifyCode")
)
if mibBuilder.loadTexts:
    hwGtlLicenseVerifyFailed.setStatus(
        "current"
    )

hwGtlExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 5)
)
if mibBuilder.loadTexts:
    hwGtlExpired.setStatus(
        "current"
    )

hwGtlItemMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 2, 6)
)
hwGtlItemMismatch.setObjects(
    ("HUAWEI-GTL-MIB", "hwGtlChassisID")
)
if mibBuilder.loadTexts:
    hwGtlItemMismatch.setStatus(
        "current"
    )


# Notifications groups

hwGtlNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 2, 2)
)
hwGtlNotificationGroup.setObjects(
      *(("HUAWEI-GTL-MIB", "hwGtlDefaultValue"),
        ("HUAWEI-GTL-MIB", "hwGtlResourceUsedUp"),
        ("HUAWEI-GTL-MIB", "hwGtlNearDeadline"),
        ("HUAWEI-GTL-MIB", "hwGtlLicenseVerifyFailed"),
        ("HUAWEI-GTL-MIB", "hwGtlExpired"))
)
if mibBuilder.loadTexts:
    hwGtlNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwGtlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 142, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwGtlCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-GTL-MIB",
    **{"hwGtl": hwGtl,
       "hwGtlMibObjects": hwGtlMibObjects,
       "hwGtlDefaultValueReason": hwGtlDefaultValueReason,
       "hwGtlResourceItem": hwGtlResourceItem,
       "hwGtlFeatureName": hwGtlFeatureName,
       "hwGtlRemainTime": hwGtlRemainTime,
       "hwGtlVerifyCode": hwGtlVerifyCode,
       "hwGtlActive": hwGtlActive,
       "hwGtlShowActLCSName": hwGtlShowActLCSName,
       "hwGtlItemTable": hwGtlItemTable,
       "hwGtlItemEntry": hwGtlItemEntry,
       "hwGtlItemIndex": hwGtlItemIndex,
       "hwGtlItemName": hwGtlItemName,
       "hwGtlItemControlValue": hwGtlItemControlValue,
       "hwGtlItemUsedValue": hwGtlItemUsedValue,
       "hwGtlItemDescription": hwGtlItemDescription,
       "hwGtlChassisID": hwGtlChassisID,
       "hwGtlNotifications": hwGtlNotifications,
       "hwGtlDefaultValue": hwGtlDefaultValue,
       "hwGtlResourceUsedUp": hwGtlResourceUsedUp,
       "hwGtlNearDeadline": hwGtlNearDeadline,
       "hwGtlLicenseVerifyFailed": hwGtlLicenseVerifyFailed,
       "hwGtlExpired": hwGtlExpired,
       "hwGtlItemMismatch": hwGtlItemMismatch,
       "hwGtlConformance": hwGtlConformance,
       "hwGtlCompliances": hwGtlCompliances,
       "hwGtlCompliance": hwGtlCompliance,
       "hwGtlGroups": hwGtlGroups,
       "hwGtlObjectGroup": hwGtlObjectGroup,
       "hwGtlNotificationGroup": hwGtlNotificationGroup}
)
