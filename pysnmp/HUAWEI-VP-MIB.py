# SNMP MIB module (HUAWEI-VP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:33 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwVpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307)
)
hwVpMIB.setRevisions(
        ("2014-07-16 13:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVpObjects_ObjectIdentity = ObjectIdentity
hwVpObjects = _HwVpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1)
)
_HwVpVmTable_Object = MibTable
hwVpVmTable = _HwVpVmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1)
)
if mibBuilder.loadTexts:
    hwVpVmTable.setStatus("current")
_HwVpVmEntry_Object = MibTableRow
hwVpVmEntry = _HwVpVmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1)
)
hwVpVmEntry.setIndexNames(
    (0, "HUAWEI-VP-MIB", "hwVpVmVlan"),
    (0, "HUAWEI-VP-MIB", "hwVpVmMac"),
)
if mibBuilder.loadTexts:
    hwVpVmEntry.setStatus("current")


class _HwVpVmVlan_Type(Integer32):
    """Custom type hwVpVmVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwVpVmVlan_Type.__name__ = "Integer32"
_HwVpVmVlan_Object = MibTableColumn
hwVpVmVlan = _HwVpVmVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 1),
    _HwVpVmVlan_Type()
)
hwVpVmVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpVmVlan.setStatus("current")
_HwVpVmMac_Type = MacAddress
_HwVpVmMac_Object = MibTableColumn
hwVpVmMac = _HwVpVmMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 2),
    _HwVpVmMac_Type()
)
hwVpVmMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpVmMac.setStatus("current")


class _HwVpVmProfileId_Type(DisplayString):
    """Custom type hwVpVmProfileId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwVpVmProfileId_Type.__name__ = "DisplayString"
_HwVpVmProfileId_Object = MibTableColumn
hwVpVmProfileId = _HwVpVmProfileId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 3),
    _HwVpVmProfileId_Type()
)
hwVpVmProfileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpVmProfileId.setStatus("current")
_HwVpNotifications_ObjectIdentity = ObjectIdentity
hwVpNotifications = _HwVpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2)
)
_HwVpConformance_ObjectIdentity = ObjectIdentity
hwVpConformance = _HwVpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3)
)
_HwVpCompliances_ObjectIdentity = ObjectIdentity
hwVpCompliances = _HwVpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 1)
)
_HwVpGroups_ObjectIdentity = ObjectIdentity
hwVpGroups = _HwVpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2)
)

# Managed Objects groups

hwVpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2, 1)
)
hwVpObjectGroup.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmMac"),
        ("HUAWEI-VP-MIB", "hwVpVmVlan"),
        ("HUAWEI-VP-MIB", "hwVpVmProfileId"))
)
if mibBuilder.loadTexts:
    hwVpObjectGroup.setStatus("current")


# Notification objects

hwVpVmDownloadProfileFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 1)
)
hwVpVmDownloadProfileFault.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmVlan"),
        ("HUAWEI-VP-MIB", "hwVpVmMac"),
        ("HUAWEI-VP-MIB", "hwVpVmProfileId"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVpVmDownloadProfileFault.setStatus(
        "current"
    )

hwVpVmDownloadProfileFaultResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 2)
)
hwVpVmDownloadProfileFaultResume.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmVlan"),
        ("HUAWEI-VP-MIB", "hwVpVmMac"),
        ("HUAWEI-VP-MIB", "hwVpVmProfileId"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVpVmDownloadProfileFaultResume.setStatus(
        "current"
    )

hwVpVmAuthenticateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 3)
)
hwVpVmAuthenticateFail.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmVlan"),
        ("HUAWEI-VP-MIB", "hwVpVmMac"),
        ("HUAWEI-VP-MIB", "hwVpVmProfileId"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVpVmAuthenticateFail.setStatus(
        "current"
    )

hwVpVmDeliverAuthorInformationFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 4)
)
hwVpVmDeliverAuthorInformationFail.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmVlan"),
        ("HUAWEI-VP-MIB", "hwVpVmMac"),
        ("HUAWEI-VP-MIB", "hwVpVmProfileId"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwVpVmDeliverAuthorInformationFail.setStatus(
        "current"
    )


# Notifications groups

hwVpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2, 2)
)
hwVpNotificationGroup.setObjects(
      *(("HUAWEI-VP-MIB", "hwVpVmDownloadProfileFault"),
        ("HUAWEI-VP-MIB", "hwVpVmDownloadProfileFaultResume"),
        ("HUAWEI-VP-MIB", "hwVpVmAuthenticateFail"),
        ("HUAWEI-VP-MIB", "hwVpVmDeliverAuthorInformationFail"))
)
if mibBuilder.loadTexts:
    hwVpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwVpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwVpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VP-MIB",
    **{"hwVpMIB": hwVpMIB,
       "hwVpObjects": hwVpObjects,
       "hwVpVmTable": hwVpVmTable,
       "hwVpVmEntry": hwVpVmEntry,
       "hwVpVmVlan": hwVpVmVlan,
       "hwVpVmMac": hwVpVmMac,
       "hwVpVmProfileId": hwVpVmProfileId,
       "hwVpNotifications": hwVpNotifications,
       "hwVpVmDownloadProfileFault": hwVpVmDownloadProfileFault,
       "hwVpVmDownloadProfileFaultResume": hwVpVmDownloadProfileFaultResume,
       "hwVpVmAuthenticateFail": hwVpVmAuthenticateFail,
       "hwVpVmDeliverAuthorInformationFail": hwVpVmDeliverAuthorInformationFail,
       "hwVpConformance": hwVpConformance,
       "hwVpCompliances": hwVpCompliances,
       "hwVpCompliance": hwVpCompliance,
       "hwVpGroups": hwVpGroups,
       "hwVpObjectGroup": hwVpObjectGroup,
       "hwVpNotificationGroup": hwVpNotificationGroup}
)
