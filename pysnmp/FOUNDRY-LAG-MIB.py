# SNMP MIB module (FOUNDRY-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:44 2024
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

(snSwitch,
 snTraps) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "snSwitch",
    "snTraps")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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

fdryLinkAggregationGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33)
)
fdryLinkAggregationGroupMIB.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryLinkAggregationGroupNotifyObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupNotifyObjects = _FdryLinkAggregationGroupNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0)
)


class _FdryLAGName_Type(DisplayString):
    """Custom type fdryLAGName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FdryLAGName_Type.__name__ = "DisplayString"
_FdryLAGName_Object = MibScalar
fdryLAGName = _FdryLAGName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 0, 1),
    _FdryLAGName_Type()
)
fdryLAGName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fdryLAGName.setStatus("current")
_FdryLinkAggregationGroupTableObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupTableObjects = _FdryLinkAggregationGroupTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1)
)
_FdryLinkAggregationGroupTable_Object = MibTable
fdryLinkAggregationGroupTable = _FdryLinkAggregationGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTable.setStatus("current")
_FdryLinkAggregationGroupEntry_Object = MibTableRow
fdryLinkAggregationGroupEntry = _FdryLinkAggregationGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1)
)
fdryLinkAggregationGroupEntry.setIndexNames(
    (0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"),
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupEntry.setStatus("current")


class _FdryLinkAggregationGroupName_Type(DisplayString):
    """Custom type fdryLinkAggregationGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FdryLinkAggregationGroupName_Type.__name__ = "DisplayString"
_FdryLinkAggregationGroupName_Object = MibTableColumn
fdryLinkAggregationGroupName = _FdryLinkAggregationGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 1),
    _FdryLinkAggregationGroupName_Type()
)
fdryLinkAggregationGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupName.setStatus("current")


class _FdryLinkAggregationGroupType_Type(Integer32):
    """Custom type fdryLinkAggregationGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("keepalive", 3),
          ("static", 1))
    )


_FdryLinkAggregationGroupType_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupType_Object = MibTableColumn
fdryLinkAggregationGroupType = _FdryLinkAggregationGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 2),
    _FdryLinkAggregationGroupType_Type()
)
fdryLinkAggregationGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupType.setStatus("current")


class _FdryLinkAggregationGroupAdminStatus_Type(Integer32):
    """Custom type fdryLinkAggregationGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deploy", 1),
          ("deployPassive", 2),
          ("undeploy", 3),
          ("undeployForced", 4))
    )


_FdryLinkAggregationGroupAdminStatus_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupAdminStatus_Object = MibTableColumn
fdryLinkAggregationGroupAdminStatus = _FdryLinkAggregationGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 3),
    _FdryLinkAggregationGroupAdminStatus_Type()
)
fdryLinkAggregationGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupAdminStatus.setStatus("current")
_FdryLinkAggregationGroupIfList_Type = OctetString
_FdryLinkAggregationGroupIfList_Object = MibTableColumn
fdryLinkAggregationGroupIfList = _FdryLinkAggregationGroupIfList_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 4),
    _FdryLinkAggregationGroupIfList_Type()
)
fdryLinkAggregationGroupIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupIfList.setStatus("current")
_FdryLinkAggregationGroupPrimaryPort_Type = InterfaceIndex
_FdryLinkAggregationGroupPrimaryPort_Object = MibTableColumn
fdryLinkAggregationGroupPrimaryPort = _FdryLinkAggregationGroupPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 5),
    _FdryLinkAggregationGroupPrimaryPort_Type()
)
fdryLinkAggregationGroupPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPrimaryPort.setStatus("current")


class _FdryLinkAggregationGroupTrunkType_Type(Integer32):
    """Custom type fdryLinkAggregationGroupTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashBased", 1),
          ("perPacket", 2))
    )


_FdryLinkAggregationGroupTrunkType_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupTrunkType_Object = MibTableColumn
fdryLinkAggregationGroupTrunkType = _FdryLinkAggregationGroupTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 6),
    _FdryLinkAggregationGroupTrunkType_Type()
)
fdryLinkAggregationGroupTrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTrunkType.setStatus("current")
_FdryLinkAggregationGroupTrunkThreshold_Type = Unsigned32
_FdryLinkAggregationGroupTrunkThreshold_Object = MibTableColumn
fdryLinkAggregationGroupTrunkThreshold = _FdryLinkAggregationGroupTrunkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 7),
    _FdryLinkAggregationGroupTrunkThreshold_Type()
)
fdryLinkAggregationGroupTrunkThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupTrunkThreshold.setStatus("current")


class _FdryLinkAggregationGroupLacpTimeout_Type(Integer32):
    """Custom type fdryLinkAggregationGroupLacpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("long", 2),
          ("short", 3))
    )


_FdryLinkAggregationGroupLacpTimeout_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupLacpTimeout_Object = MibTableColumn
fdryLinkAggregationGroupLacpTimeout = _FdryLinkAggregationGroupLacpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 8),
    _FdryLinkAggregationGroupLacpTimeout_Type()
)
fdryLinkAggregationGroupLacpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupLacpTimeout.setStatus("current")
_FdryLinkAggregationGroupIfIndex_Type = InterfaceIndexOrZero
_FdryLinkAggregationGroupIfIndex_Object = MibTableColumn
fdryLinkAggregationGroupIfIndex = _FdryLinkAggregationGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 9),
    _FdryLinkAggregationGroupIfIndex_Type()
)
fdryLinkAggregationGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupIfIndex.setStatus("current")
_FdryLinkAggregationGroupPortCount_Type = Unsigned32
_FdryLinkAggregationGroupPortCount_Object = MibTableColumn
fdryLinkAggregationGroupPortCount = _FdryLinkAggregationGroupPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 10),
    _FdryLinkAggregationGroupPortCount_Type()
)
fdryLinkAggregationGroupPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortCount.setStatus("current")
_FdryLinkAggregationGroupRowStatus_Type = RowStatus
_FdryLinkAggregationGroupRowStatus_Object = MibTableColumn
fdryLinkAggregationGroupRowStatus = _FdryLinkAggregationGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 11),
    _FdryLinkAggregationGroupRowStatus_Type()
)
fdryLinkAggregationGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupRowStatus.setStatus("current")
_FdryLinkAggregationGroupId_Type = Unsigned32
_FdryLinkAggregationGroupId_Object = MibTableColumn
fdryLinkAggregationGroupId = _FdryLinkAggregationGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 1, 1, 1, 12),
    _FdryLinkAggregationGroupId_Type()
)
fdryLinkAggregationGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupId.setStatus("current")
_FdryLinkAggregationGroupPortTableObjects_ObjectIdentity = ObjectIdentity
fdryLinkAggregationGroupPortTableObjects = _FdryLinkAggregationGroupPortTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2)
)
_FdryLinkAggregationGroupPortTable_Object = MibTable
fdryLinkAggregationGroupPortTable = _FdryLinkAggregationGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1)
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortTable.setStatus("current")
_FdryLinkAggregationGroupPortEntry_Object = MibTableRow
fdryLinkAggregationGroupPortEntry = _FdryLinkAggregationGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1)
)
fdryLinkAggregationGroupPortEntry.setIndexNames(
    (0, "FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupName"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortEntry.setStatus("current")


class _FdryLinkAggregationGroupPortLacpPriority_Type(Integer32):
    """Custom type fdryLinkAggregationGroupPortLacpPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdryLinkAggregationGroupPortLacpPriority_Type.__name__ = "Integer32"
_FdryLinkAggregationGroupPortLacpPriority_Object = MibTableColumn
fdryLinkAggregationGroupPortLacpPriority = _FdryLinkAggregationGroupPortLacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 33, 2, 1, 1, 1),
    _FdryLinkAggregationGroupPortLacpPriority_Type()
)
fdryLinkAggregationGroupPortLacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryLinkAggregationGroupPortLacpPriority.setStatus("current")

# Managed Objects groups


# Notification objects

fdryTrapLagDeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1204)
)
fdryTrapLagDeployed.setObjects(
      *(("FOUNDRY-LAG-MIB", "fdryLAGName"),
        ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
)
if mibBuilder.loadTexts:
    fdryTrapLagDeployed.setStatus(
        "current"
    )

fdryTrapLagUndeployed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1991, 0, 1205)
)
fdryTrapLagUndeployed.setObjects(
      *(("FOUNDRY-LAG-MIB", "fdryLAGName"),
        ("FOUNDRY-LAG-MIB", "fdryLinkAggregationGroupIfIndex"))
)
if mibBuilder.loadTexts:
    fdryTrapLagUndeployed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-LAG-MIB",
    **{"fdryTrapLagDeployed": fdryTrapLagDeployed,
       "fdryTrapLagUndeployed": fdryTrapLagUndeployed,
       "fdryLinkAggregationGroupMIB": fdryLinkAggregationGroupMIB,
       "fdryLinkAggregationGroupNotifyObjects": fdryLinkAggregationGroupNotifyObjects,
       "fdryLAGName": fdryLAGName,
       "fdryLinkAggregationGroupTableObjects": fdryLinkAggregationGroupTableObjects,
       "fdryLinkAggregationGroupTable": fdryLinkAggregationGroupTable,
       "fdryLinkAggregationGroupEntry": fdryLinkAggregationGroupEntry,
       "fdryLinkAggregationGroupName": fdryLinkAggregationGroupName,
       "fdryLinkAggregationGroupType": fdryLinkAggregationGroupType,
       "fdryLinkAggregationGroupAdminStatus": fdryLinkAggregationGroupAdminStatus,
       "fdryLinkAggregationGroupIfList": fdryLinkAggregationGroupIfList,
       "fdryLinkAggregationGroupPrimaryPort": fdryLinkAggregationGroupPrimaryPort,
       "fdryLinkAggregationGroupTrunkType": fdryLinkAggregationGroupTrunkType,
       "fdryLinkAggregationGroupTrunkThreshold": fdryLinkAggregationGroupTrunkThreshold,
       "fdryLinkAggregationGroupLacpTimeout": fdryLinkAggregationGroupLacpTimeout,
       "fdryLinkAggregationGroupIfIndex": fdryLinkAggregationGroupIfIndex,
       "fdryLinkAggregationGroupPortCount": fdryLinkAggregationGroupPortCount,
       "fdryLinkAggregationGroupRowStatus": fdryLinkAggregationGroupRowStatus,
       "fdryLinkAggregationGroupId": fdryLinkAggregationGroupId,
       "fdryLinkAggregationGroupPortTableObjects": fdryLinkAggregationGroupPortTableObjects,
       "fdryLinkAggregationGroupPortTable": fdryLinkAggregationGroupPortTable,
       "fdryLinkAggregationGroupPortEntry": fdryLinkAggregationGroupPortEntry,
       "fdryLinkAggregationGroupPortLacpPriority": fdryLinkAggregationGroupPortLacpPriority}
)
