# SNMP MIB module (BENU-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:02 2024
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

bVLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8)
)
bVLANMIB.setRevisions(
        ("2015-05-07 00:00",
         "2015-04-14 00:00",
         "2015-01-06 00:00",
         "2014-11-17 00:00",
         "2014-08-04 00:00",
         "2014-06-24 00:00",
         "2014-05-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BVLANNotifObjects_ObjectIdentity = ObjectIdentity
bVLANNotifObjects = _BVLANNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0)
)
if mibBuilder.loadTexts:
    bVLANNotifObjects.setStatus("current")
_BVLANMIBObjects_ObjectIdentity = ObjectIdentity
bVLANMIBObjects = _BVLANMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    bVLANMIBObjects.setStatus("current")
_BVlanTable_Object = MibTable
bVlanTable = _BVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    bVlanTable.setStatus("current")
_BVlanEntry_Object = MibTableRow
bVlanEntry = _BVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1)
)
bVlanEntry.setIndexNames(
    (0, "BENU-VLAN-MIB", "bVlanPortIndex"),
    (0, "BENU-VLAN-MIB", "bVlanIndex"),
)
if mibBuilder.loadTexts:
    bVlanEntry.setStatus("current")
_BVlanPortIndex_Type = Integer32
_BVlanPortIndex_Object = MibTableColumn
bVlanPortIndex = _BVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 1),
    _BVlanPortIndex_Type()
)
bVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bVlanPortIndex.setStatus("current")
_BVlanIndex_Type = Integer32
_BVlanIndex_Object = MibTableColumn
bVlanIndex = _BVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 2),
    _BVlanIndex_Type()
)
bVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bVlanIndex.setStatus("current")
_BVlanName_Type = DisplayString
_BVlanName_Object = MibTableColumn
bVlanName = _BVlanName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 3),
    _BVlanName_Type()
)
bVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanName.setStatus("current")
_BVlanMTU_Type = Unsigned32
_BVlanMTU_Object = MibTableColumn
bVlanMTU = _BVlanMTU_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 4),
    _BVlanMTU_Type()
)
bVlanMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanMTU.setStatus("current")
_BVlanEncapName_Type = DisplayString
_BVlanEncapName_Object = MibTableColumn
bVlanEncapName = _BVlanEncapName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 5),
    _BVlanEncapName_Type()
)
bVlanEncapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanEncapName.setStatus("current")


class _BVlanAdminStatus_Type(Integer32):
    """Custom type bVlanAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_BVlanAdminStatus_Type.__name__ = "Integer32"
_BVlanAdminStatus_Object = MibTableColumn
bVlanAdminStatus = _BVlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 6),
    _BVlanAdminStatus_Type()
)
bVlanAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanAdminStatus.setStatus("current")


class _BVlanOperStatus_Type(Integer32):
    """Custom type bVlanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_BVlanOperStatus_Type.__name__ = "Integer32"
_BVlanOperStatus_Object = MibTableColumn
bVlanOperStatus = _BVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 1, 1, 7),
    _BVlanOperStatus_Type()
)
bVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanOperStatus.setStatus("current")
_BWagVlanTable_Object = MibTable
bWagVlanTable = _BWagVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    bWagVlanTable.setStatus("current")
_BWagVlanEntry_Object = MibTableRow
bWagVlanEntry = _BWagVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1)
)
bWagVlanEntry.setIndexNames(
    (0, "BENU-VLAN-MIB", "bWagVlanPortIndex"),
    (0, "BENU-VLAN-MIB", "bWagVlanIndex"),
)
if mibBuilder.loadTexts:
    bWagVlanEntry.setStatus("current")
_BWagVlanPortIndex_Type = Integer32
_BWagVlanPortIndex_Object = MibTableColumn
bWagVlanPortIndex = _BWagVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 1),
    _BWagVlanPortIndex_Type()
)
bWagVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagVlanPortIndex.setStatus("current")
_BWagVlanIndex_Type = Integer32
_BWagVlanIndex_Object = MibTableColumn
bWagVlanIndex = _BWagVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 2),
    _BWagVlanIndex_Type()
)
bWagVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagVlanIndex.setStatus("current")
_BWagVlanSubscriberCount_Type = Unsigned32
_BWagVlanSubscriberCount_Object = MibTableColumn
bWagVlanSubscriberCount = _BWagVlanSubscriberCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 2, 1, 3),
    _BWagVlanSubscriberCount_Type()
)
bWagVlanSubscriberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagVlanSubscriberCount.setStatus("current")
_BWagVlanStatsTable_Object = MibTable
bWagVlanStatsTable = _BWagVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    bWagVlanStatsTable.setStatus("current")
_BWagVlanStatsEntry_Object = MibTableRow
bWagVlanStatsEntry = _BWagVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1)
)
bWagVlanStatsEntry.setIndexNames(
    (0, "BENU-VLAN-MIB", "bWagVlanStatsPortIndex"),
    (0, "BENU-VLAN-MIB", "bWagVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagVlanStatsEntry.setStatus("current")
_BWagVlanStatsPortIndex_Type = Integer32
_BWagVlanStatsPortIndex_Object = MibTableColumn
bWagVlanStatsPortIndex = _BWagVlanStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 1),
    _BWagVlanStatsPortIndex_Type()
)
bWagVlanStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagVlanStatsPortIndex.setStatus("current")
_BWagVlanStatsIndex_Type = Integer32
_BWagVlanStatsIndex_Object = MibTableColumn
bWagVlanStatsIndex = _BWagVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 2),
    _BWagVlanStatsIndex_Type()
)
bWagVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagVlanStatsIndex.setStatus("current")
_BWagVlanTotalPktsRcvd_Type = Counter64
_BWagVlanTotalPktsRcvd_Object = MibTableColumn
bWagVlanTotalPktsRcvd = _BWagVlanTotalPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 3),
    _BWagVlanTotalPktsRcvd_Type()
)
bWagVlanTotalPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagVlanTotalPktsRcvd.setStatus("current")
_BWagVlanTotalPktsSent_Type = Counter64
_BWagVlanTotalPktsSent_Object = MibTableColumn
bWagVlanTotalPktsSent = _BWagVlanTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 4),
    _BWagVlanTotalPktsSent_Type()
)
bWagVlanTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagVlanTotalPktsSent.setStatus("current")
_BWagVlanTotalBytesRcvd_Type = Counter64
_BWagVlanTotalBytesRcvd_Object = MibTableColumn
bWagVlanTotalBytesRcvd = _BWagVlanTotalBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 5),
    _BWagVlanTotalBytesRcvd_Type()
)
bWagVlanTotalBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagVlanTotalBytesRcvd.setStatus("current")
_BWagVlanTotalBytesSent_Type = Counter64
_BWagVlanTotalBytesSent_Object = MibTableColumn
bWagVlanTotalBytesSent = _BWagVlanTotalBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 3, 1, 6),
    _BWagVlanTotalBytesSent_Type()
)
bWagVlanTotalBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagVlanTotalBytesSent.setStatus("current")
_BVlanPortTable_Object = MibTable
bVlanPortTable = _BVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4)
)
if mibBuilder.loadTexts:
    bVlanPortTable.setStatus("current")
_BVlanPortEntry_Object = MibTableRow
bVlanPortEntry = _BVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1)
)
bVlanPortEntry.setIndexNames(
    (0, "BENU-VLAN-MIB", "bVlanPerPortIndex"),
)
if mibBuilder.loadTexts:
    bVlanPortEntry.setStatus("current")
_BVlanPerPortIndex_Type = Integer32
_BVlanPerPortIndex_Object = MibTableColumn
bVlanPerPortIndex = _BVlanPerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 1),
    _BVlanPerPortIndex_Type()
)
bVlanPerPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bVlanPerPortIndex.setStatus("current")
_BVlanTotal_Type = Unsigned32
_BVlanTotal_Object = MibTableColumn
bVlanTotal = _BVlanTotal_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 2),
    _BVlanTotal_Type()
)
bVlanTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanTotal.setStatus("current")
_BVlanActive_Type = Unsigned32
_BVlanActive_Object = MibTableColumn
bVlanActive = _BVlanActive_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 4, 1, 3),
    _BVlanActive_Type()
)
bVlanActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanActive.setStatus("current")


class _BVlanCurrentNumber_Type(Integer32):
    """Custom type bVlanCurrentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BVlanCurrentNumber_Type.__name__ = "Integer32"
_BVlanCurrentNumber_Object = MibScalar
bVlanCurrentNumber = _BVlanCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 5),
    _BVlanCurrentNumber_Type()
)
bVlanCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanCurrentNumber.setStatus("current")
_BVlanAssocSub_Type = Integer32
_BVlanAssocSub_Object = MibScalar
bVlanAssocSub = _BVlanAssocSub_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 1, 6),
    _BVlanAssocSub_Type()
)
bVlanAssocSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bVlanAssocSub.setStatus("current")
_BVLANNotifVariables_ObjectIdentity = ObjectIdentity
bVLANNotifVariables = _BVLANNotifVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    bVLANNotifVariables.setStatus("current")
_BVlanPortId_Type = Unsigned32
_BVlanPortId_Object = MibScalar
bVlanPortId = _BVlanPortId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2, 1),
    _BVlanPortId_Type()
)
bVlanPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bVlanPortId.setStatus("current")
_BVlanId_Type = Unsigned32
_BVlanId_Object = MibScalar
bVlanId = _BVlanId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 2, 2),
    _BVlanId_Type()
)
bVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bVlanId.setStatus("current")

# Managed Objects groups


# Notification objects

bVlanEncapEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 1)
)
bVlanEncapEnable.setObjects(
    ("BENU-VLAN-MIB", "bVlanPortId")
)
if mibBuilder.loadTexts:
    bVlanEncapEnable.setStatus(
        "current"
    )

bVlanEncapDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 2)
)
bVlanEncapDisable.setObjects(
    ("BENU-VLAN-MIB", "bVlanPortId")
)
if mibBuilder.loadTexts:
    bVlanEncapDisable.setStatus(
        "current"
    )

bVlanCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 3)
)
bVlanCreate.setObjects(
      *(("BENU-VLAN-MIB", "bVlanPortId"),
        ("BENU-VLAN-MIB", "bVlanId"))
)
if mibBuilder.loadTexts:
    bVlanCreate.setStatus(
        "current"
    )

bVlanDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 8, 0, 4)
)
bVlanDelete.setObjects(
      *(("BENU-VLAN-MIB", "bVlanPortId"),
        ("BENU-VLAN-MIB", "bVlanId"))
)
if mibBuilder.loadTexts:
    bVlanDelete.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-VLAN-MIB",
    **{"bVLANMIB": bVLANMIB,
       "bVLANNotifObjects": bVLANNotifObjects,
       "bVlanEncapEnable": bVlanEncapEnable,
       "bVlanEncapDisable": bVlanEncapDisable,
       "bVlanCreate": bVlanCreate,
       "bVlanDelete": bVlanDelete,
       "bVLANMIBObjects": bVLANMIBObjects,
       "bVlanTable": bVlanTable,
       "bVlanEntry": bVlanEntry,
       "bVlanPortIndex": bVlanPortIndex,
       "bVlanIndex": bVlanIndex,
       "bVlanName": bVlanName,
       "bVlanMTU": bVlanMTU,
       "bVlanEncapName": bVlanEncapName,
       "bVlanAdminStatus": bVlanAdminStatus,
       "bVlanOperStatus": bVlanOperStatus,
       "bWagVlanTable": bWagVlanTable,
       "bWagVlanEntry": bWagVlanEntry,
       "bWagVlanPortIndex": bWagVlanPortIndex,
       "bWagVlanIndex": bWagVlanIndex,
       "bWagVlanSubscriberCount": bWagVlanSubscriberCount,
       "bWagVlanStatsTable": bWagVlanStatsTable,
       "bWagVlanStatsEntry": bWagVlanStatsEntry,
       "bWagVlanStatsPortIndex": bWagVlanStatsPortIndex,
       "bWagVlanStatsIndex": bWagVlanStatsIndex,
       "bWagVlanTotalPktsRcvd": bWagVlanTotalPktsRcvd,
       "bWagVlanTotalPktsSent": bWagVlanTotalPktsSent,
       "bWagVlanTotalBytesRcvd": bWagVlanTotalBytesRcvd,
       "bWagVlanTotalBytesSent": bWagVlanTotalBytesSent,
       "bVlanPortTable": bVlanPortTable,
       "bVlanPortEntry": bVlanPortEntry,
       "bVlanPerPortIndex": bVlanPerPortIndex,
       "bVlanTotal": bVlanTotal,
       "bVlanActive": bVlanActive,
       "bVlanCurrentNumber": bVlanCurrentNumber,
       "bVlanAssocSub": bVlanAssocSub,
       "bVLANNotifVariables": bVLANNotifVariables,
       "bVlanPortId": bVlanPortId,
       "bVlanId": bVlanId}
)
