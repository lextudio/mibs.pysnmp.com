# SNMP MIB module (ACC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:39 2024
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

(accCommon,) = mibBuilder.importSymbols(
    "ANDOVER-CONTROLS-MIB",
    "accCommon")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

accNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1)
)
accNotificationMIB.setRevisions(
        ("2002-10-30 09:46",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccNotifyObjects_ObjectIdentity = ObjectIdentity
accNotifyObjects = _AccNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1)
)
_AccNotifyList_ObjectIdentity = ObjectIdentity
accNotifyList = _AccNotifyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1)
)
_AccNotifyNumber_Type = Integer32
_AccNotifyNumber_Object = MibScalar
accNotifyNumber = _AccNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 1),
    _AccNotifyNumber_Type()
)
accNotifyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNotifyNumber.setStatus("current")
_AccNotifyTable_Object = MibTable
accNotifyTable = _AccNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    accNotifyTable.setStatus("current")
_AccNotifyEntry_Object = MibTableRow
accNotifyEntry = _AccNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1)
)
accNotifyEntry.setIndexNames(
    (0, "ACC-NOTIFICATION-MIB", "notifyIndex"),
)
if mibBuilder.loadTexts:
    accNotifyEntry.setStatus("current")
_NotifyIndex_Type = Unsigned32
_NotifyIndex_Object = MibTableColumn
notifyIndex = _NotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1, 1),
    _NotifyIndex_Type()
)
notifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyIndex.setStatus("current")
_NotifyAddress_Type = IpAddress
_NotifyAddress_Object = MibTableColumn
notifyAddress = _NotifyAddress_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1, 2),
    _NotifyAddress_Type()
)
notifyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyAddress.setStatus("current")


class _NotifyType_Type(Integer32):
    """Custom type notifyType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trap", 1))
    )


_NotifyType_Type.__name__ = "Integer32"
_NotifyType_Object = MibTableColumn
notifyType = _NotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1, 3),
    _NotifyType_Type()
)
notifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyType.setStatus("current")
_NotifyStorageType_Type = StorageType
_NotifyStorageType_Object = MibTableColumn
notifyStorageType = _NotifyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1, 4),
    _NotifyStorageType_Type()
)
notifyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notifyStorageType.setStatus("current")


class _NotifyRowStatus_Type(Integer32):
    """Custom type notifyRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_NotifyRowStatus_Type.__name__ = "Integer32"
_NotifyRowStatus_Object = MibTableColumn
notifyRowStatus = _NotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 1, 1, 2, 1, 5),
    _NotifyRowStatus_Type()
)
notifyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    notifyRowStatus.setStatus("current")
_AccNotifyConformance_ObjectIdentity = ObjectIdentity
accNotifyConformance = _AccNotifyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 3)
)
_AccNotifyCompliances_ObjectIdentity = ObjectIdentity
accNotifyCompliances = _AccNotifyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 3, 1)
)
_AccNotifyGroups_ObjectIdentity = ObjectIdentity
accNotifyGroups = _AccNotifyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 3, 2)
)

# Managed Objects groups

accNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 3, 2, 1)
)
accNotifyGroup.setObjects(
      *(("ACC-NOTIFICATION-MIB", "notifyIndex"),
        ("ACC-NOTIFICATION-MIB", "notifyAddress"),
        ("ACC-NOTIFICATION-MIB", "notifyType"),
        ("ACC-NOTIFICATION-MIB", "notifyStorageType"),
        ("ACC-NOTIFICATION-MIB", "notifyRowStatus"),
        ("ACC-NOTIFICATION-MIB", "accNotifyNumber"))
)
if mibBuilder.loadTexts:
    accNotifyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

accNotifyBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10829, 4, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    accNotifyBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-NOTIFICATION-MIB",
    **{"accNotificationMIB": accNotificationMIB,
       "accNotifyObjects": accNotifyObjects,
       "accNotifyList": accNotifyList,
       "accNotifyNumber": accNotifyNumber,
       "accNotifyTable": accNotifyTable,
       "accNotifyEntry": accNotifyEntry,
       "notifyIndex": notifyIndex,
       "notifyAddress": notifyAddress,
       "notifyType": notifyType,
       "notifyStorageType": notifyStorageType,
       "notifyRowStatus": notifyRowStatus,
       "accNotifyConformance": accNotifyConformance,
       "accNotifyCompliances": accNotifyCompliances,
       "accNotifyBasicCompliance": accNotifyBasicCompliance,
       "accNotifyGroups": accNotifyGroups,
       "accNotifyGroup": accNotifyGroup}
)
