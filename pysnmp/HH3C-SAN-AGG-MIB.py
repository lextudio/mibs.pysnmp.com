# SNMP MIB module (HH3C-SAN-AGG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SAN-AGG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:50 2024
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

(hh3cSan,) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan")

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

hh3cSanAgg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2)
)
hh3cSanAgg.setRevisions(
        ("2013-02-25 09:40",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMemberList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hh3cSanAggMibObjects_ObjectIdentity = ObjectIdentity
hh3cSanAggMibObjects = _Hh3cSanAggMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 1)
)
_Hh3cSanAggMaxMemberNumber_Type = Integer32
_Hh3cSanAggMaxMemberNumber_Object = MibScalar
hh3cSanAggMaxMemberNumber = _Hh3cSanAggMaxMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 1, 1),
    _Hh3cSanAggMaxMemberNumber_Type()
)
hh3cSanAggMaxMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSanAggMaxMemberNumber.setStatus("current")
_Hh3cSanAggGroupTable_Object = MibTable
hh3cSanAggGroupTable = _Hh3cSanAggGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cSanAggGroupTable.setStatus("current")
_Hh3cSanAggGroupEntry_Object = MibTableRow
hh3cSanAggGroupEntry = _Hh3cSanAggGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1)
)
hh3cSanAggGroupEntry.setIndexNames(
    (0, "HH3C-SAN-AGG-MIB", "hh3cSanAggGroupNumber"),
)
if mibBuilder.loadTexts:
    hh3cSanAggGroupEntry.setStatus("current")


class _Hh3cSanAggGroupNumber_Type(Integer32):
    """Custom type hh3cSanAggGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSanAggGroupNumber_Type.__name__ = "Integer32"
_Hh3cSanAggGroupNumber_Object = MibTableColumn
hh3cSanAggGroupNumber = _Hh3cSanAggGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1, 1),
    _Hh3cSanAggGroupNumber_Type()
)
hh3cSanAggGroupNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSanAggGroupNumber.setStatus("current")
_Hh3cSanAggGroupIndex_Type = Integer32
_Hh3cSanAggGroupIndex_Object = MibTableColumn
hh3cSanAggGroupIndex = _Hh3cSanAggGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1, 2),
    _Hh3cSanAggGroupIndex_Type()
)
hh3cSanAggGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSanAggGroupIndex.setStatus("current")
_Hh3cSanAggMemberList_Type = Hh3cMemberList
_Hh3cSanAggMemberList_Object = MibTableColumn
hh3cSanAggMemberList = _Hh3cSanAggMemberList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1, 3),
    _Hh3cSanAggMemberList_Type()
)
hh3cSanAggMemberList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSanAggMemberList.setStatus("current")
_Hh3cSanAggMemberStateList_Type = Hh3cMemberList
_Hh3cSanAggMemberStateList_Object = MibTableColumn
hh3cSanAggMemberStateList = _Hh3cSanAggMemberStateList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1, 4),
    _Hh3cSanAggMemberStateList_Type()
)
hh3cSanAggMemberStateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSanAggMemberStateList.setStatus("current")
_Hh3cSanAggGroupRowStatus_Type = RowStatus
_Hh3cSanAggGroupRowStatus_Object = MibTableColumn
hh3cSanAggGroupRowStatus = _Hh3cSanAggGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 2, 1, 5),
    _Hh3cSanAggGroupRowStatus_Type()
)
hh3cSanAggGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSanAggGroupRowStatus.setStatus("current")
_Hh3cSanAggObjForNotification_ObjectIdentity = ObjectIdentity
hh3cSanAggObjForNotification = _Hh3cSanAggObjForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 3)
)
_Hh3cSanAggGroupPreviousSpeed_Type = Integer32
_Hh3cSanAggGroupPreviousSpeed_Object = MibScalar
hh3cSanAggGroupPreviousSpeed = _Hh3cSanAggGroupPreviousSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 3, 1),
    _Hh3cSanAggGroupPreviousSpeed_Type()
)
hh3cSanAggGroupPreviousSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSanAggGroupPreviousSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSanAggGroupPreviousSpeed.setUnits("gigabit bps")
_Hh3cSanAggGroupCurrentSpeed_Type = Integer32
_Hh3cSanAggGroupCurrentSpeed_Object = MibScalar
hh3cSanAggGroupCurrentSpeed = _Hh3cSanAggGroupCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 3, 2),
    _Hh3cSanAggGroupCurrentSpeed_Type()
)
hh3cSanAggGroupCurrentSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSanAggGroupCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSanAggGroupCurrentSpeed.setUnits("gigabit bps")
_Hh3cSanAggNotifications_ObjectIdentity = ObjectIdentity
hh3cSanAggNotifications = _Hh3cSanAggNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 4)
)
_Hh3cSanAggNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cSanAggNotificationPrefix = _Hh3cSanAggNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

hh3cSanAggGroupSpeedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 4, 0, 1)
)
hh3cSanAggGroupSpeedChange.setObjects(
      *(("HH3C-SAN-AGG-MIB", "hh3cSanAggGroupNumber"),
        ("HH3C-SAN-AGG-MIB", "hh3cSanAggGroupPreviousSpeed"),
        ("HH3C-SAN-AGG-MIB", "hh3cSanAggGroupCurrentSpeed"))
)
if mibBuilder.loadTexts:
    hh3cSanAggGroupSpeedChange.setStatus(
        "current"
    )

hh3cSanAggMemberInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 4, 0, 2)
)
hh3cSanAggMemberInactive.setObjects(
      *(("HH3C-SAN-AGG-MIB", "hh3cSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cSanAggMemberInactive.setStatus(
        "current"
    )

hh3cSanAggMemberActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 2, 4, 0, 3)
)
hh3cSanAggMemberActive.setObjects(
      *(("HH3C-SAN-AGG-MIB", "hh3cSanAggGroupNumber"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cSanAggMemberActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SAN-AGG-MIB",
    **{"Hh3cMemberList": Hh3cMemberList,
       "hh3cSanAgg": hh3cSanAgg,
       "hh3cSanAggMibObjects": hh3cSanAggMibObjects,
       "hh3cSanAggMaxMemberNumber": hh3cSanAggMaxMemberNumber,
       "hh3cSanAggGroupTable": hh3cSanAggGroupTable,
       "hh3cSanAggGroupEntry": hh3cSanAggGroupEntry,
       "hh3cSanAggGroupNumber": hh3cSanAggGroupNumber,
       "hh3cSanAggGroupIndex": hh3cSanAggGroupIndex,
       "hh3cSanAggMemberList": hh3cSanAggMemberList,
       "hh3cSanAggMemberStateList": hh3cSanAggMemberStateList,
       "hh3cSanAggGroupRowStatus": hh3cSanAggGroupRowStatus,
       "hh3cSanAggObjForNotification": hh3cSanAggObjForNotification,
       "hh3cSanAggGroupPreviousSpeed": hh3cSanAggGroupPreviousSpeed,
       "hh3cSanAggGroupCurrentSpeed": hh3cSanAggGroupCurrentSpeed,
       "hh3cSanAggNotifications": hh3cSanAggNotifications,
       "hh3cSanAggNotificationPrefix": hh3cSanAggNotificationPrefix,
       "hh3cSanAggGroupSpeedChange": hh3cSanAggGroupSpeedChange,
       "hh3cSanAggMemberInactive": hh3cSanAggMemberInactive,
       "hh3cSanAggMemberActive": hh3cSanAggMemberActive}
)
