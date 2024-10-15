# SNMP MIB module (HPN-ICF-SAN-AGG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SAN-AGG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:46 2024
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

(hpnicfSan,) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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

hpnicfSanAgg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2)
)
hpnicfSanAgg.setRevisions(
        ("2013-02-25 09:40",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMemberList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HpnicfSanAggMibObjects_ObjectIdentity = ObjectIdentity
hpnicfSanAggMibObjects = _HpnicfSanAggMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 1)
)
_HpnicfSanAggMaxMemberNumber_Type = Integer32
_HpnicfSanAggMaxMemberNumber_Object = MibScalar
hpnicfSanAggMaxMemberNumber = _HpnicfSanAggMaxMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 1, 1),
    _HpnicfSanAggMaxMemberNumber_Type()
)
hpnicfSanAggMaxMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSanAggMaxMemberNumber.setStatus("current")
_HpnicfSanAggGroupTable_Object = MibTable
hpnicfSanAggGroupTable = _HpnicfSanAggGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfSanAggGroupTable.setStatus("current")
_HpnicfSanAggGroupEntry_Object = MibTableRow
hpnicfSanAggGroupEntry = _HpnicfSanAggGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1)
)
hpnicfSanAggGroupEntry.setIndexNames(
    (0, "HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupNumber"),
)
if mibBuilder.loadTexts:
    hpnicfSanAggGroupEntry.setStatus("current")


class _HpnicfSanAggGroupNumber_Type(Integer32):
    """Custom type hpnicfSanAggGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSanAggGroupNumber_Type.__name__ = "Integer32"
_HpnicfSanAggGroupNumber_Object = MibTableColumn
hpnicfSanAggGroupNumber = _HpnicfSanAggGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1, 1),
    _HpnicfSanAggGroupNumber_Type()
)
hpnicfSanAggGroupNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupNumber.setStatus("current")
_HpnicfSanAggGroupIndex_Type = Integer32
_HpnicfSanAggGroupIndex_Object = MibTableColumn
hpnicfSanAggGroupIndex = _HpnicfSanAggGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1, 2),
    _HpnicfSanAggGroupIndex_Type()
)
hpnicfSanAggGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupIndex.setStatus("current")
_HpnicfSanAggMemberList_Type = HpnicfMemberList
_HpnicfSanAggMemberList_Object = MibTableColumn
hpnicfSanAggMemberList = _HpnicfSanAggMemberList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1, 3),
    _HpnicfSanAggMemberList_Type()
)
hpnicfSanAggMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSanAggMemberList.setStatus("current")
_HpnicfSanAggMemberStateList_Type = HpnicfMemberList
_HpnicfSanAggMemberStateList_Object = MibTableColumn
hpnicfSanAggMemberStateList = _HpnicfSanAggMemberStateList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1, 4),
    _HpnicfSanAggMemberStateList_Type()
)
hpnicfSanAggMemberStateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSanAggMemberStateList.setStatus("current")
_HpnicfSanAggGroupRowStatus_Type = RowStatus
_HpnicfSanAggGroupRowStatus_Object = MibTableColumn
hpnicfSanAggGroupRowStatus = _HpnicfSanAggGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 2, 1, 5),
    _HpnicfSanAggGroupRowStatus_Type()
)
hpnicfSanAggGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupRowStatus.setStatus("current")
_HpnicfSanAggObjForNotification_ObjectIdentity = ObjectIdentity
hpnicfSanAggObjForNotification = _HpnicfSanAggObjForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 3)
)
_HpnicfSanAggGroupPreviousSpeed_Type = Integer32
_HpnicfSanAggGroupPreviousSpeed_Object = MibScalar
hpnicfSanAggGroupPreviousSpeed = _HpnicfSanAggGroupPreviousSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 3, 1),
    _HpnicfSanAggGroupPreviousSpeed_Type()
)
hpnicfSanAggGroupPreviousSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupPreviousSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupPreviousSpeed.setUnits("gigabit bps")
_HpnicfSanAggGroupCurrentSpeed_Type = Integer32
_HpnicfSanAggGroupCurrentSpeed_Object = MibScalar
hpnicfSanAggGroupCurrentSpeed = _HpnicfSanAggGroupCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 3, 2),
    _HpnicfSanAggGroupCurrentSpeed_Type()
)
hpnicfSanAggGroupCurrentSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSanAggGroupCurrentSpeed.setUnits("gigabit bps")
_HpnicfSanAggNotifications_ObjectIdentity = ObjectIdentity
hpnicfSanAggNotifications = _HpnicfSanAggNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 4)
)
_HpnicfSanAggNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfSanAggNotificationPrefix = _HpnicfSanAggNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

hpnicfSanAggGroupSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 4, 0, 1)
)
hpnicfSanAggGroupSpeedChange.setObjects(
      *(("HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupNumber"),
        ("HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupPreviousSpeed"),
        ("HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupCurrentSpeed"))
)
if mibBuilder.loadTexts:
    hpnicfSanAggGroupSpeedChange.setStatus(
        "current"
    )

hpnicfSanAggMemberInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 4, 0, 2)
)
hpnicfSanAggMemberInactive.setObjects(
      *(("HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfSanAggMemberInactive.setStatus(
        "current"
    )

hpnicfSanAggMemberActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 2, 4, 0, 3)
)
hpnicfSanAggMemberActive.setObjects(
      *(("HPN-ICF-SAN-AGG-MIB", "hpnicfSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfSanAggMemberActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SAN-AGG-MIB",
    **{"HpnicfMemberList": HpnicfMemberList,
       "hpnicfSanAgg": hpnicfSanAgg,
       "hpnicfSanAggMibObjects": hpnicfSanAggMibObjects,
       "hpnicfSanAggMaxMemberNumber": hpnicfSanAggMaxMemberNumber,
       "hpnicfSanAggGroupTable": hpnicfSanAggGroupTable,
       "hpnicfSanAggGroupEntry": hpnicfSanAggGroupEntry,
       "hpnicfSanAggGroupNumber": hpnicfSanAggGroupNumber,
       "hpnicfSanAggGroupIndex": hpnicfSanAggGroupIndex,
       "hpnicfSanAggMemberList": hpnicfSanAggMemberList,
       "hpnicfSanAggMemberStateList": hpnicfSanAggMemberStateList,
       "hpnicfSanAggGroupRowStatus": hpnicfSanAggGroupRowStatus,
       "hpnicfSanAggObjForNotification": hpnicfSanAggObjForNotification,
       "hpnicfSanAggGroupPreviousSpeed": hpnicfSanAggGroupPreviousSpeed,
       "hpnicfSanAggGroupCurrentSpeed": hpnicfSanAggGroupCurrentSpeed,
       "hpnicfSanAggNotifications": hpnicfSanAggNotifications,
       "hpnicfSanAggNotificationPrefix": hpnicfSanAggNotificationPrefix,
       "hpnicfSanAggGroupSpeedChange": hpnicfSanAggGroupSpeedChange,
       "hpnicfSanAggMemberInactive": hpnicfSanAggMemberInactive,
       "hpnicfSanAggMemberActive": hpnicfSanAggMemberActive}
)
