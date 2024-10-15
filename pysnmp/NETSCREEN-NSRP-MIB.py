# SNMP MIB module (NETSCREEN-NSRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-NSRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:47 2024
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

(netscreenNsrp,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenNsrp")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netscreenNsrpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 0)
)
netscreenNsrpMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-14 00:00",
         "2003-06-04 00:00",
         "2001-01-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetscreenNsrpGeneral_ObjectIdentity = ObjectIdentity
netscreenNsrpGeneral = _NetscreenNsrpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1)
)
_NsrpGeneralClusterId_Type = Integer32
_NsrpGeneralClusterId_Object = MibScalar
nsrpGeneralClusterId = _NsrpGeneralClusterId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 1),
    _NsrpGeneralClusterId_Type()
)
nsrpGeneralClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralClusterId.setStatus("current")
_NsrpGeneralLocalUnitId_Type = Integer32
_NsrpGeneralLocalUnitId_Object = MibScalar
nsrpGeneralLocalUnitId = _NsrpGeneralLocalUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 2),
    _NsrpGeneralLocalUnitId_Type()
)
nsrpGeneralLocalUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralLocalUnitId.setStatus("current")


class _NsrpGeneralEncrypEnable_Type(Integer32):
    """Custom type nsrpGeneralEncrypEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NsrpGeneralEncrypEnable_Type.__name__ = "Integer32"
_NsrpGeneralEncrypEnable_Object = MibScalar
nsrpGeneralEncrypEnable = _NsrpGeneralEncrypEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 3),
    _NsrpGeneralEncrypEnable_Type()
)
nsrpGeneralEncrypEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralEncrypEnable.setStatus("current")


class _NsrpGeneralAuthEnable_Type(Integer32):
    """Custom type nsrpGeneralAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NsrpGeneralAuthEnable_Type.__name__ = "Integer32"
_NsrpGeneralAuthEnable_Object = MibScalar
nsrpGeneralAuthEnable = _NsrpGeneralAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 4),
    _NsrpGeneralAuthEnable_Type()
)
nsrpGeneralAuthEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralAuthEnable.setStatus("current")


class _NsrpGeneralIfMonitor_Type(DisplayString):
    """Custom type nsrpGeneralIfMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NsrpGeneralIfMonitor_Type.__name__ = "DisplayString"
_NsrpGeneralIfMonitor_Object = MibScalar
nsrpGeneralIfMonitor = _NsrpGeneralIfMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 5),
    _NsrpGeneralIfMonitor_Type()
)
nsrpGeneralIfMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralIfMonitor.setStatus("current")
_NsrpGeneralGratArps_Type = Integer32
_NsrpGeneralGratArps_Object = MibScalar
nsrpGeneralGratArps = _NsrpGeneralGratArps_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 1, 6),
    _NsrpGeneralGratArps_Type()
)
nsrpGeneralGratArps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpGeneralGratArps.setStatus("current")
_NetscreenNsrpVSD_ObjectIdentity = ObjectIdentity
netscreenNsrpVSD = _NetscreenNsrpVSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2)
)
_NsrpVsdGroupTable_Object = MibTable
nsrpVsdGroupTable = _NsrpVsdGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1)
)
if mibBuilder.loadTexts:
    nsrpVsdGroupTable.setStatus("current")
_NsrpVsdGroupEntry_Object = MibTableRow
nsrpVsdGroupEntry = _NsrpVsdGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1)
)
nsrpVsdGroupEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpVsdGroupID"),
)
if mibBuilder.loadTexts:
    nsrpVsdGroupEntry.setStatus("current")


class _NsrpVsdGroupID_Type(Integer32):
    """Custom type nsrpVsdGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpVsdGroupID_Type.__name__ = "Integer32"
_NsrpVsdGroupID_Object = MibTableColumn
nsrpVsdGroupID = _NsrpVsdGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 1),
    _NsrpVsdGroupID_Type()
)
nsrpVsdGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupID.setStatus("current")
_NsrpVsdGroupPriority_Type = Integer32
_NsrpVsdGroupPriority_Object = MibTableColumn
nsrpVsdGroupPriority = _NsrpVsdGroupPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 2),
    _NsrpVsdGroupPriority_Type()
)
nsrpVsdGroupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupPriority.setStatus("current")
_NsrpVsdGroupPreempt_Type = Integer32
_NsrpVsdGroupPreempt_Object = MibTableColumn
nsrpVsdGroupPreempt = _NsrpVsdGroupPreempt_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 3),
    _NsrpVsdGroupPreempt_Type()
)
nsrpVsdGroupPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupPreempt.setStatus("current")
_NsrpVsdGroupHoldDownTime_Type = Integer32
_NsrpVsdGroupHoldDownTime_Object = MibTableColumn
nsrpVsdGroupHoldDownTime = _NsrpVsdGroupHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 4),
    _NsrpVsdGroupHoldDownTime_Type()
)
nsrpVsdGroupHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupHoldDownTime.setStatus("current")
_NsrpVsdGroupNumberOfUnit_Type = Integer32
_NsrpVsdGroupNumberOfUnit_Object = MibTableColumn
nsrpVsdGroupNumberOfUnit = _NsrpVsdGroupNumberOfUnit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 5),
    _NsrpVsdGroupNumberOfUnit_Type()
)
nsrpVsdGroupNumberOfUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupNumberOfUnit.setStatus("current")
_NsrpVsdGroupCntStateChange_Type = Integer32
_NsrpVsdGroupCntStateChange_Object = MibTableColumn
nsrpVsdGroupCntStateChange = _NsrpVsdGroupCntStateChange_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 6),
    _NsrpVsdGroupCntStateChange_Type()
)
nsrpVsdGroupCntStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntStateChange.setStatus("current")
_NsrpVsdGroupCntToInit_Type = Integer32
_NsrpVsdGroupCntToInit_Object = MibTableColumn
nsrpVsdGroupCntToInit = _NsrpVsdGroupCntToInit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 7),
    _NsrpVsdGroupCntToInit_Type()
)
nsrpVsdGroupCntToInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToInit.setStatus("current")
_NsrpVsdGroupCntToMaster_Type = Integer32
_NsrpVsdGroupCntToMaster_Object = MibTableColumn
nsrpVsdGroupCntToMaster = _NsrpVsdGroupCntToMaster_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 8),
    _NsrpVsdGroupCntToMaster_Type()
)
nsrpVsdGroupCntToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToMaster.setStatus("current")
_NsrpVsdGroupCntToPBackup_Type = Integer32
_NsrpVsdGroupCntToPBackup_Object = MibTableColumn
nsrpVsdGroupCntToPBackup = _NsrpVsdGroupCntToPBackup_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 9),
    _NsrpVsdGroupCntToPBackup_Type()
)
nsrpVsdGroupCntToPBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToPBackup.setStatus("current")
_NsrpVsdGroupCntToBackup_Type = Integer32
_NsrpVsdGroupCntToBackup_Object = MibTableColumn
nsrpVsdGroupCntToBackup = _NsrpVsdGroupCntToBackup_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 10),
    _NsrpVsdGroupCntToBackup_Type()
)
nsrpVsdGroupCntToBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToBackup.setStatus("current")
_NsrpVsdGroupCntToIneligible_Type = Integer32
_NsrpVsdGroupCntToIneligible_Object = MibTableColumn
nsrpVsdGroupCntToIneligible = _NsrpVsdGroupCntToIneligible_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 11),
    _NsrpVsdGroupCntToIneligible_Type()
)
nsrpVsdGroupCntToIneligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToIneligible.setStatus("current")
_NsrpVsdGroupCntToInoperable_Type = Integer32
_NsrpVsdGroupCntToInoperable_Object = MibTableColumn
nsrpVsdGroupCntToInoperable = _NsrpVsdGroupCntToInoperable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 12),
    _NsrpVsdGroupCntToInoperable_Type()
)
nsrpVsdGroupCntToInoperable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntToInoperable.setStatus("current")
_NsrpVsdGroupCntMasterConflict_Type = Integer32
_NsrpVsdGroupCntMasterConflict_Object = MibTableColumn
nsrpVsdGroupCntMasterConflict = _NsrpVsdGroupCntMasterConflict_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 13),
    _NsrpVsdGroupCntMasterConflict_Type()
)
nsrpVsdGroupCntMasterConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntMasterConflict.setStatus("current")
_NsrpVsdGroupCntPbConfilict_Type = Integer32
_NsrpVsdGroupCntPbConfilict_Object = MibTableColumn
nsrpVsdGroupCntPbConfilict = _NsrpVsdGroupCntPbConfilict_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 14),
    _NsrpVsdGroupCntPbConfilict_Type()
)
nsrpVsdGroupCntPbConfilict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntPbConfilict.setStatus("current")
_NsrpVsdGroupCntHeartbeatTx_Type = Integer32
_NsrpVsdGroupCntHeartbeatTx_Object = MibTableColumn
nsrpVsdGroupCntHeartbeatTx = _NsrpVsdGroupCntHeartbeatTx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 15),
    _NsrpVsdGroupCntHeartbeatTx_Type()
)
nsrpVsdGroupCntHeartbeatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntHeartbeatTx.setStatus("current")
_NsrpVsdGroupCntHeartbeatRx_Type = Integer32
_NsrpVsdGroupCntHeartbeatRx_Object = MibTableColumn
nsrpVsdGroupCntHeartbeatRx = _NsrpVsdGroupCntHeartbeatRx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 1, 1, 16),
    _NsrpVsdGroupCntHeartbeatRx_Type()
)
nsrpVsdGroupCntHeartbeatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGroupCntHeartbeatRx.setStatus("current")
_NsrpVsdMemberTable_Object = MibTable
nsrpVsdMemberTable = _NsrpVsdMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2)
)
if mibBuilder.loadTexts:
    nsrpVsdMemberTable.setStatus("current")
_NsrpVsdMemberEntry_Object = MibTableRow
nsrpVsdMemberEntry = _NsrpVsdMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1)
)
nsrpVsdMemberEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpVsdMemberGroupId"),
    (0, "NETSCREEN-NSRP-MIB", "nsrpVsdMemberUnitId"),
)
if mibBuilder.loadTexts:
    nsrpVsdMemberEntry.setStatus("current")


class _NsrpVsdMemberGroupId_Type(Integer32):
    """Custom type nsrpVsdMemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpVsdMemberGroupId_Type.__name__ = "Integer32"
_NsrpVsdMemberGroupId_Object = MibTableColumn
nsrpVsdMemberGroupId = _NsrpVsdMemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 1),
    _NsrpVsdMemberGroupId_Type()
)
nsrpVsdMemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdMemberGroupId.setStatus("current")


class _NsrpVsdMemberUnitId_Type(Integer32):
    """Custom type nsrpVsdMemberUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpVsdMemberUnitId_Type.__name__ = "Integer32"
_NsrpVsdMemberUnitId_Object = MibTableColumn
nsrpVsdMemberUnitId = _NsrpVsdMemberUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 2),
    _NsrpVsdMemberUnitId_Type()
)
nsrpVsdMemberUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdMemberUnitId.setStatus("current")


class _NsrpVsdMemberStatus_Type(Integer32):
    """Custom type nsrpVsdMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("backup", 4),
          ("ineligible", 5),
          ("init", 1),
          ("inoperable", 6),
          ("master", 2),
          ("primary-backup", 3),
          ("undefined", 0))
    )


_NsrpVsdMemberStatus_Type.__name__ = "Integer32"
_NsrpVsdMemberStatus_Object = MibTableColumn
nsrpVsdMemberStatus = _NsrpVsdMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 3),
    _NsrpVsdMemberStatus_Type()
)
nsrpVsdMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdMemberStatus.setStatus("current")
_NsrpVsdMemberPriority_Type = Integer32
_NsrpVsdMemberPriority_Object = MibTableColumn
nsrpVsdMemberPriority = _NsrpVsdMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 4),
    _NsrpVsdMemberPriority_Type()
)
nsrpVsdMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdMemberPriority.setStatus("current")
_NsrpVsdMemberPreempt_Type = Integer32
_NsrpVsdMemberPreempt_Object = MibTableColumn
nsrpVsdMemberPreempt = _NsrpVsdMemberPreempt_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 2, 1, 5),
    _NsrpVsdMemberPreempt_Type()
)
nsrpVsdMemberPreempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdMemberPreempt.setStatus("current")
_NsrpVsdInterfaceTable_Object = MibTable
nsrpVsdInterfaceTable = _NsrpVsdInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3)
)
if mibBuilder.loadTexts:
    nsrpVsdInterfaceTable.setStatus("current")
_NsrpVsdInterfaceEntry_Object = MibTableRow
nsrpVsdInterfaceEntry = _NsrpVsdInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1)
)
nsrpVsdInterfaceEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpVsdIfIndex"),
)
if mibBuilder.loadTexts:
    nsrpVsdInterfaceEntry.setStatus("current")


class _NsrpVsdIfIndex_Type(Integer32):
    """Custom type nsrpVsdIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpVsdIfIndex_Type.__name__ = "Integer32"
_NsrpVsdIfIndex_Object = MibTableColumn
nsrpVsdIfIndex = _NsrpVsdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 1),
    _NsrpVsdIfIndex_Type()
)
nsrpVsdIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfIndex.setStatus("current")


class _NsrpVsdIfStatus_Type(Integer32):
    """Custom type nsrpVsdIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("down", 0),
          ("inactive", 1))
    )


_NsrpVsdIfStatus_Type.__name__ = "Integer32"
_NsrpVsdIfStatus_Object = MibTableColumn
nsrpVsdIfStatus = _NsrpVsdIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 2),
    _NsrpVsdIfStatus_Type()
)
nsrpVsdIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfStatus.setStatus("current")
_NsrpVsdIfGroupId_Type = Integer32
_NsrpVsdIfGroupId_Object = MibTableColumn
nsrpVsdIfGroupId = _NsrpVsdIfGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 3),
    _NsrpVsdIfGroupId_Type()
)
nsrpVsdIfGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfGroupId.setStatus("current")
_NsrpVsdIfIp_Type = IpAddress
_NsrpVsdIfIp_Object = MibTableColumn
nsrpVsdIfIp = _NsrpVsdIfIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 4),
    _NsrpVsdIfIp_Type()
)
nsrpVsdIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfIp.setStatus("current")
_NsrpVsdIfNetmask_Type = IpAddress
_NsrpVsdIfNetmask_Object = MibTableColumn
nsrpVsdIfNetmask = _NsrpVsdIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 5),
    _NsrpVsdIfNetmask_Type()
)
nsrpVsdIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfNetmask.setStatus("current")
_NsrpVsdIfGateway_Type = IpAddress
_NsrpVsdIfGateway_Object = MibTableColumn
nsrpVsdIfGateway = _NsrpVsdIfGateway_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 6),
    _NsrpVsdIfGateway_Type()
)
nsrpVsdIfGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfGateway.setStatus("current")


class _NsrpVsdIfName_Type(DisplayString):
    """Custom type nsrpVsdIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsrpVsdIfName_Type.__name__ = "DisplayString"
_NsrpVsdIfName_Object = MibTableColumn
nsrpVsdIfName = _NsrpVsdIfName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 7),
    _NsrpVsdIfName_Type()
)
nsrpVsdIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfName.setStatus("current")
_NsrpVsdIfVLAN_Type = Integer32
_NsrpVsdIfVLAN_Object = MibTableColumn
nsrpVsdIfVLAN = _NsrpVsdIfVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 8),
    _NsrpVsdIfVLAN_Type()
)
nsrpVsdIfVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfVLAN.setStatus("current")
_NsrpVsdIfMAC_Type = PhysAddress
_NsrpVsdIfMAC_Object = MibTableColumn
nsrpVsdIfMAC = _NsrpVsdIfMAC_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 9),
    _NsrpVsdIfMAC_Type()
)
nsrpVsdIfMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMAC.setStatus("current")


class _NsrpVsdIfVSys_Type(DisplayString):
    """Custom type nsrpVsdIfVSys based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsrpVsdIfVSys_Type.__name__ = "DisplayString"
_NsrpVsdIfVSys_Object = MibTableColumn
nsrpVsdIfVSys = _NsrpVsdIfVSys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 10),
    _NsrpVsdIfVSys_Type()
)
nsrpVsdIfVSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfVSys.setStatus("current")


class _NsrpVsdIfMngTelnet_Type(Integer32):
    """Custom type nsrpVsdIfMngTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngTelnet_Type.__name__ = "Integer32"
_NsrpVsdIfMngTelnet_Object = MibTableColumn
nsrpVsdIfMngTelnet = _NsrpVsdIfMngTelnet_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 11),
    _NsrpVsdIfMngTelnet_Type()
)
nsrpVsdIfMngTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngTelnet.setStatus("current")


class _NsrpVsdIfMngSCS_Type(Integer32):
    """Custom type nsrpVsdIfMngSCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngSCS_Type.__name__ = "Integer32"
_NsrpVsdIfMngSCS_Object = MibTableColumn
nsrpVsdIfMngSCS = _NsrpVsdIfMngSCS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 12),
    _NsrpVsdIfMngSCS_Type()
)
nsrpVsdIfMngSCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngSCS.setStatus("current")


class _NsrpVsdIfMngWEB_Type(Integer32):
    """Custom type nsrpVsdIfMngWEB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngWEB_Type.__name__ = "Integer32"
_NsrpVsdIfMngWEB_Object = MibTableColumn
nsrpVsdIfMngWEB = _NsrpVsdIfMngWEB_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 13),
    _NsrpVsdIfMngWEB_Type()
)
nsrpVsdIfMngWEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngWEB.setStatus("current")


class _NsrpVsdIfMngSSL_Type(Integer32):
    """Custom type nsrpVsdIfMngSSL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngSSL_Type.__name__ = "Integer32"
_NsrpVsdIfMngSSL_Object = MibTableColumn
nsrpVsdIfMngSSL = _NsrpVsdIfMngSSL_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 14),
    _NsrpVsdIfMngSSL_Type()
)
nsrpVsdIfMngSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngSSL.setStatus("current")


class _NsrpVsdIfMngSNMP_Type(Integer32):
    """Custom type nsrpVsdIfMngSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngSNMP_Type.__name__ = "Integer32"
_NsrpVsdIfMngSNMP_Object = MibTableColumn
nsrpVsdIfMngSNMP = _NsrpVsdIfMngSNMP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 15),
    _NsrpVsdIfMngSNMP_Type()
)
nsrpVsdIfMngSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngSNMP.setStatus("current")


class _NsrpVsdIfMngGlobal_Type(Integer32):
    """Custom type nsrpVsdIfMngGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngGlobal_Type.__name__ = "Integer32"
_NsrpVsdIfMngGlobal_Object = MibTableColumn
nsrpVsdIfMngGlobal = _NsrpVsdIfMngGlobal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 16),
    _NsrpVsdIfMngGlobal_Type()
)
nsrpVsdIfMngGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngGlobal.setStatus("current")


class _NsrpVsdIfMngGlobalPro_Type(Integer32):
    """Custom type nsrpVsdIfMngGlobalPro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngGlobalPro_Type.__name__ = "Integer32"
_NsrpVsdIfMngGlobalPro_Object = MibTableColumn
nsrpVsdIfMngGlobalPro = _NsrpVsdIfMngGlobalPro_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 17),
    _NsrpVsdIfMngGlobalPro_Type()
)
nsrpVsdIfMngGlobalPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngGlobalPro.setStatus("current")


class _NsrpVsdIfMngPing_Type(Integer32):
    """Custom type nsrpVsdIfMngPing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngPing_Type.__name__ = "Integer32"
_NsrpVsdIfMngPing_Object = MibTableColumn
nsrpVsdIfMngPing = _NsrpVsdIfMngPing_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 18),
    _NsrpVsdIfMngPing_Type()
)
nsrpVsdIfMngPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngPing.setStatus("current")


class _NsrpVsdIfMngIdentReset_Type(Integer32):
    """Custom type nsrpVsdIfMngIdentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NsrpVsdIfMngIdentReset_Type.__name__ = "Integer32"
_NsrpVsdIfMngIdentReset_Object = MibTableColumn
nsrpVsdIfMngIdentReset = _NsrpVsdIfMngIdentReset_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 3, 1, 19),
    _NsrpVsdIfMngIdentReset_Type()
)
nsrpVsdIfMngIdentReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdIfMngIdentReset.setStatus("current")
_NsrpVsdGeneral_ObjectIdentity = ObjectIdentity
nsrpVsdGeneral = _NsrpVsdGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 4)
)
_NsrpVsdGeneralInitHoldTime_Type = Counter32
_NsrpVsdGeneralInitHoldTime_Object = MibScalar
nsrpVsdGeneralInitHoldTime = _NsrpVsdGeneralInitHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 1),
    _NsrpVsdGeneralInitHoldTime_Type()
)
nsrpVsdGeneralInitHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGeneralInitHoldTime.setStatus("current")
_NsrpVsdGeneralHbInterval_Type = Counter32
_NsrpVsdGeneralHbInterval_Object = MibScalar
nsrpVsdGeneralHbInterval = _NsrpVsdGeneralHbInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 2),
    _NsrpVsdGeneralHbInterval_Type()
)
nsrpVsdGeneralHbInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGeneralHbInterval.setStatus("current")
_NsrpVsdGeneralHbLostThres_Type = Counter32
_NsrpVsdGeneralHbLostThres_Object = MibScalar
nsrpVsdGeneralHbLostThres = _NsrpVsdGeneralHbLostThres_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 2, 4, 3),
    _NsrpVsdGeneralHbLostThres_Type()
)
nsrpVsdGeneralHbLostThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpVsdGeneralHbLostThres.setStatus("current")
_NetscreenNsrpRTO_ObjectIdentity = ObjectIdentity
netscreenNsrpRTO = _NetscreenNsrpRTO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3)
)
_NsrpRtoGroupTable_Object = MibTable
nsrpRtoGroupTable = _NsrpRtoGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nsrpRtoGroupTable.setStatus("current")
_NsrpRtoGroupEntry_Object = MibTableRow
nsrpRtoGroupEntry = _NsrpRtoGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1)
)
nsrpRtoGroupEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpRtoGroupId"),
)
if mibBuilder.loadTexts:
    nsrpRtoGroupEntry.setStatus("current")


class _NsrpRtoGroupId_Type(Integer32):
    """Custom type nsrpRtoGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpRtoGroupId_Type.__name__ = "Integer32"
_NsrpRtoGroupId_Object = MibTableColumn
nsrpRtoGroupId = _NsrpRtoGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1, 1),
    _NsrpRtoGroupId_Type()
)
nsrpRtoGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoGroupId.setStatus("current")
_NsrpRtoNumOfUnit_Type = Integer32
_NsrpRtoNumOfUnit_Object = MibTableColumn
nsrpRtoNumOfUnit = _NsrpRtoNumOfUnit_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 1, 1, 2),
    _NsrpRtoNumOfUnit_Type()
)
nsrpRtoNumOfUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoNumOfUnit.setStatus("current")
_NsrpRtoUnitTable_Object = MibTable
nsrpRtoUnitTable = _NsrpRtoUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2)
)
if mibBuilder.loadTexts:
    nsrpRtoUnitTable.setStatus("current")
_NsrpRtoUnitEntry_Object = MibTableRow
nsrpRtoUnitEntry = _NsrpRtoUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1)
)
nsrpRtoUnitEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpRtoUnitGroupId"),
    (0, "NETSCREEN-NSRP-MIB", "nsrpRtoUnitId"),
)
if mibBuilder.loadTexts:
    nsrpRtoUnitEntry.setStatus("current")


class _NsrpRtoUnitGroupId_Type(Integer32):
    """Custom type nsrpRtoUnitGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpRtoUnitGroupId_Type.__name__ = "Integer32"
_NsrpRtoUnitGroupId_Object = MibTableColumn
nsrpRtoUnitGroupId = _NsrpRtoUnitGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 1),
    _NsrpRtoUnitGroupId_Type()
)
nsrpRtoUnitGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitGroupId.setStatus("current")


class _NsrpRtoUnitId_Type(Integer32):
    """Custom type nsrpRtoUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpRtoUnitId_Type.__name__ = "Integer32"
_NsrpRtoUnitId_Object = MibTableColumn
nsrpRtoUnitId = _NsrpRtoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 2),
    _NsrpRtoUnitId_Type()
)
nsrpRtoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitId.setStatus("current")


class _NsrpRtoUnitStatus_Type(Integer32):
    """Custom type nsrpRtoUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("set", 1),
          ("undefined", 0))
    )


_NsrpRtoUnitStatus_Type.__name__ = "Integer32"
_NsrpRtoUnitStatus_Object = MibTableColumn
nsrpRtoUnitStatus = _NsrpRtoUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 3),
    _NsrpRtoUnitStatus_Type()
)
nsrpRtoUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitStatus.setStatus("current")


class _NsrpRtoUnitDirection_Type(Integer32):
    """Custom type nsrpRtoUnitDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 2),
          ("out", 1))
    )


_NsrpRtoUnitDirection_Type.__name__ = "Integer32"
_NsrpRtoUnitDirection_Object = MibTableColumn
nsrpRtoUnitDirection = _NsrpRtoUnitDirection_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 4),
    _NsrpRtoUnitDirection_Type()
)
nsrpRtoUnitDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitDirection.setStatus("current")
_NsrpRtoUnitLostHeartbeat_Type = Counter32
_NsrpRtoUnitLostHeartbeat_Object = MibTableColumn
nsrpRtoUnitLostHeartbeat = _NsrpRtoUnitLostHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 5),
    _NsrpRtoUnitLostHeartbeat_Type()
)
nsrpRtoUnitLostHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitLostHeartbeat.setStatus("current")
_NsrpRtoUnitToActive_Type = Counter32
_NsrpRtoUnitToActive_Object = MibTableColumn
nsrpRtoUnitToActive = _NsrpRtoUnitToActive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 6),
    _NsrpRtoUnitToActive_Type()
)
nsrpRtoUnitToActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitToActive.setStatus("current")
_NsrpRtoUnitToSet_Type = Counter32
_NsrpRtoUnitToSet_Object = MibTableColumn
nsrpRtoUnitToSet = _NsrpRtoUnitToSet_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 7),
    _NsrpRtoUnitToSet_Type()
)
nsrpRtoUnitToSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitToSet.setStatus("current")
_NsrpRtoUnitLostPeer_Type = Counter32
_NsrpRtoUnitLostPeer_Object = MibTableColumn
nsrpRtoUnitLostPeer = _NsrpRtoUnitLostPeer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 8),
    _NsrpRtoUnitLostPeer_Type()
)
nsrpRtoUnitLostPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitLostPeer.setStatus("current")
_NsrpRtoUnitGroupDetach_Type = Counter32
_NsrpRtoUnitGroupDetach_Object = MibTableColumn
nsrpRtoUnitGroupDetach = _NsrpRtoUnitGroupDetach_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 2, 1, 9),
    _NsrpRtoUnitGroupDetach_Type()
)
nsrpRtoUnitGroupDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoUnitGroupDetach.setStatus("current")
_NsrpRtoCounter_ObjectIdentity = ObjectIdentity
nsrpRtoCounter = _NsrpRtoCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3)
)
_NsrpRtoCounterPakForwarded_Type = Counter32
_NsrpRtoCounterPakForwarded_Object = MibScalar
nsrpRtoCounterPakForwarded = _NsrpRtoCounterPakForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 1),
    _NsrpRtoCounterPakForwarded_Type()
)
nsrpRtoCounterPakForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterPakForwarded.setStatus("current")
_NsrpRtoCounterPakReceived_Type = Counter32
_NsrpRtoCounterPakReceived_Object = MibScalar
nsrpRtoCounterPakReceived = _NsrpRtoCounterPakReceived_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 2),
    _NsrpRtoCounterPakReceived_Type()
)
nsrpRtoCounterPakReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterPakReceived.setStatus("current")
_NsrpRtoCounterTable_Object = MibTable
nsrpRtoCounterTable = _NsrpRtoCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3)
)
if mibBuilder.loadTexts:
    nsrpRtoCounterTable.setStatus("current")
_NsrpRtoCounterEntry_Object = MibTableRow
nsrpRtoCounterEntry = _NsrpRtoCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1)
)
nsrpRtoCounterEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpRtoCounterIdx"),
)
if mibBuilder.loadTexts:
    nsrpRtoCounterEntry.setStatus("current")


class _NsrpRtoCounterIdx_Type(Integer32):
    """Custom type nsrpRtoCounterIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpRtoCounterIdx_Type.__name__ = "Integer32"
_NsrpRtoCounterIdx_Object = MibTableColumn
nsrpRtoCounterIdx = _NsrpRtoCounterIdx_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 1),
    _NsrpRtoCounterIdx_Type()
)
nsrpRtoCounterIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterIdx.setStatus("current")


class _NsrpRtoCounterName_Type(DisplayString):
    """Custom type nsrpRtoCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsrpRtoCounterName_Type.__name__ = "DisplayString"
_NsrpRtoCounterName_Object = MibTableColumn
nsrpRtoCounterName = _NsrpRtoCounterName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 2),
    _NsrpRtoCounterName_Type()
)
nsrpRtoCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterName.setStatus("current")
_NsrpRtoCounterSend_Type = Counter32
_NsrpRtoCounterSend_Object = MibTableColumn
nsrpRtoCounterSend = _NsrpRtoCounterSend_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 3),
    _NsrpRtoCounterSend_Type()
)
nsrpRtoCounterSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterSend.setStatus("current")
_NsrpRtoCounterReceive_Type = Counter32
_NsrpRtoCounterReceive_Object = MibTableColumn
nsrpRtoCounterReceive = _NsrpRtoCounterReceive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 4),
    _NsrpRtoCounterReceive_Type()
)
nsrpRtoCounterReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterReceive.setStatus("current")
_NsrpRtoCounterDrop_Type = Counter32
_NsrpRtoCounterDrop_Object = MibTableColumn
nsrpRtoCounterDrop = _NsrpRtoCounterDrop_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 3, 3, 1, 5),
    _NsrpRtoCounterDrop_Type()
)
nsrpRtoCounterDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoCounterDrop.setStatus("current")
_NsrpRtoGeneral_ObjectIdentity = ObjectIdentity
nsrpRtoGeneral = _NsrpRtoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 4)
)
_NsrpRtoGeneralHbInterval_Type = Counter32
_NsrpRtoGeneralHbInterval_Object = MibScalar
nsrpRtoGeneralHbInterval = _NsrpRtoGeneralHbInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 1),
    _NsrpRtoGeneralHbInterval_Type()
)
nsrpRtoGeneralHbInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoGeneralHbInterval.setStatus("current")
_NsrpRtoGeneralHbLostThres_Type = Counter32
_NsrpRtoGeneralHbLostThres_Object = MibScalar
nsrpRtoGeneralHbLostThres = _NsrpRtoGeneralHbLostThres_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 2),
    _NsrpRtoGeneralHbLostThres_Type()
)
nsrpRtoGeneralHbLostThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoGeneralHbLostThres.setStatus("current")


class _NsrpRtoGeneralSessSyncEnable_Type(Integer32):
    """Custom type nsrpRtoGeneralSessSyncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NsrpRtoGeneralSessSyncEnable_Type.__name__ = "Integer32"
_NsrpRtoGeneralSessSyncEnable_Object = MibScalar
nsrpRtoGeneralSessSyncEnable = _NsrpRtoGeneralSessSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 3, 4, 3),
    _NsrpRtoGeneralSessSyncEnable_Type()
)
nsrpRtoGeneralSessSyncEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpRtoGeneralSessSyncEnable.setStatus("current")
_NetscreenNsrpTrack_ObjectIdentity = ObjectIdentity
netscreenNsrpTrack = _NetscreenNsrpTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4)
)
_NsrpTrackEnable_Type = Integer32
_NsrpTrackEnable_Object = MibScalar
nsrpTrackEnable = _NsrpTrackEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 1),
    _NsrpTrackEnable_Type()
)
nsrpTrackEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackEnable.setStatus("current")
_NsrpTrackThreshold_Type = Integer32
_NsrpTrackThreshold_Object = MibScalar
nsrpTrackThreshold = _NsrpTrackThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 2),
    _NsrpTrackThreshold_Type()
)
nsrpTrackThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackThreshold.setStatus("current")
_NsrpTrackFailoverEnalble_Type = Integer32
_NsrpTrackFailoverEnalble_Object = MibScalar
nsrpTrackFailoverEnalble = _NsrpTrackFailoverEnalble_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 3),
    _NsrpTrackFailoverEnalble_Type()
)
nsrpTrackFailoverEnalble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackFailoverEnalble.setStatus("current")
_NsrpTrackTable_Object = MibTable
nsrpTrackTable = _NsrpTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4)
)
if mibBuilder.loadTexts:
    nsrpTrackTable.setStatus("current")
_NsrpTrackEntry_Object = MibTableRow
nsrpTrackEntry = _NsrpTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1)
)
nsrpTrackEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpTrackIpIndex"),
)
if mibBuilder.loadTexts:
    nsrpTrackEntry.setStatus("current")


class _NsrpTrackIpIndex_Type(Integer32):
    """Custom type nsrpTrackIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpTrackIpIndex_Type.__name__ = "Integer32"
_NsrpTrackIpIndex_Object = MibTableColumn
nsrpTrackIpIndex = _NsrpTrackIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 1),
    _NsrpTrackIpIndex_Type()
)
nsrpTrackIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpIndex.setStatus("current")
_NsrpTrackIpAddr_Type = IpAddress
_NsrpTrackIpAddr_Object = MibTableColumn
nsrpTrackIpAddr = _NsrpTrackIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 2),
    _NsrpTrackIpAddr_Type()
)
nsrpTrackIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpAddr.setStatus("current")


class _NsrpTrackIpStatus_Type(Integer32):
    """Custom type nsrpTrackIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("success", 0))
    )


_NsrpTrackIpStatus_Type.__name__ = "Integer32"
_NsrpTrackIpStatus_Object = MibTableColumn
nsrpTrackIpStatus = _NsrpTrackIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 3),
    _NsrpTrackIpStatus_Type()
)
nsrpTrackIpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpStatus.setStatus("current")
_NsrpTrackIpTimestamp_Type = Integer32
_NsrpTrackIpTimestamp_Object = MibTableColumn
nsrpTrackIpTimestamp = _NsrpTrackIpTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 4),
    _NsrpTrackIpTimestamp_Type()
)
nsrpTrackIpTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpTimestamp.setStatus("current")
_NsrpTrackIpInterval_Type = Integer32
_NsrpTrackIpInterval_Object = MibTableColumn
nsrpTrackIpInterval = _NsrpTrackIpInterval_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 5),
    _NsrpTrackIpInterval_Type()
)
nsrpTrackIpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpInterval.setStatus("current")
_NsrpTrackIpThreshhold_Type = Integer32
_NsrpTrackIpThreshhold_Object = MibTableColumn
nsrpTrackIpThreshhold = _NsrpTrackIpThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 6),
    _NsrpTrackIpThreshhold_Type()
)
nsrpTrackIpThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpThreshhold.setStatus("current")


class _NsrpTrackIpMethod_Type(Integer32):
    """Custom type nsrpTrackIpMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("ping", 0))
    )


_NsrpTrackIpMethod_Type.__name__ = "Integer32"
_NsrpTrackIpMethod_Object = MibTableColumn
nsrpTrackIpMethod = _NsrpTrackIpMethod_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 7),
    _NsrpTrackIpMethod_Type()
)
nsrpTrackIpMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpMethod.setStatus("current")
_NsrpTrackIpWeight_Type = Integer32
_NsrpTrackIpWeight_Object = MibTableColumn
nsrpTrackIpWeight = _NsrpTrackIpWeight_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 8),
    _NsrpTrackIpWeight_Type()
)
nsrpTrackIpWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpWeight.setStatus("current")


class _NsrpTrackIpIfName_Type(DisplayString):
    """Custom type nsrpTrackIpIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsrpTrackIpIfName_Type.__name__ = "DisplayString"
_NsrpTrackIpIfName_Object = MibTableColumn
nsrpTrackIpIfName = _NsrpTrackIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 9),
    _NsrpTrackIpIfName_Type()
)
nsrpTrackIpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpIfName.setStatus("current")
_NsrpTrackIpTotalCheck_Type = Integer32
_NsrpTrackIpTotalCheck_Object = MibTableColumn
nsrpTrackIpTotalCheck = _NsrpTrackIpTotalCheck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 10),
    _NsrpTrackIpTotalCheck_Type()
)
nsrpTrackIpTotalCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpTotalCheck.setStatus("current")
_NsrpTrackIpTotalFailedCheck_Type = Integer32
_NsrpTrackIpTotalFailedCheck_Object = MibTableColumn
nsrpTrackIpTotalFailedCheck = _NsrpTrackIpTotalFailedCheck_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 4, 4, 1, 11),
    _NsrpTrackIpTotalFailedCheck_Type()
)
nsrpTrackIpTotalFailedCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpTrackIpTotalFailedCheck.setStatus("current")
_NetscreenNsrpCluster_ObjectIdentity = ObjectIdentity
netscreenNsrpCluster = _NetscreenNsrpCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5)
)
_NsrpClusterTable_Object = MibTable
nsrpClusterTable = _NsrpClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1)
)
if mibBuilder.loadTexts:
    nsrpClusterTable.setStatus("current")
_NsrpClusterEntry_Object = MibTableRow
nsrpClusterEntry = _NsrpClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1)
)
nsrpClusterEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpClusterTblIndex"),
)
if mibBuilder.loadTexts:
    nsrpClusterEntry.setStatus("current")


class _NsrpClusterTblIndex_Type(Integer32):
    """Custom type nsrpClusterTblIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpClusterTblIndex_Type.__name__ = "Integer32"
_NsrpClusterTblIndex_Object = MibTableColumn
nsrpClusterTblIndex = _NsrpClusterTblIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 1),
    _NsrpClusterTblIndex_Type()
)
nsrpClusterTblIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpClusterTblIndex.setStatus("current")
_NsrpClusterUnitId_Type = Integer32
_NsrpClusterUnitId_Object = MibTableColumn
nsrpClusterUnitId = _NsrpClusterUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 2),
    _NsrpClusterUnitId_Type()
)
nsrpClusterUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpClusterUnitId.setStatus("current")
_NsrpClusterUnitCtrlMac_Type = PhysAddress
_NsrpClusterUnitCtrlMac_Object = MibTableColumn
nsrpClusterUnitCtrlMac = _NsrpClusterUnitCtrlMac_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 3),
    _NsrpClusterUnitCtrlMac_Type()
)
nsrpClusterUnitCtrlMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpClusterUnitCtrlMac.setStatus("current")
_NsrpClusterUnitDataMac_Type = PhysAddress
_NsrpClusterUnitDataMac_Object = MibTableColumn
nsrpClusterUnitDataMac = _NsrpClusterUnitDataMac_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 5, 1, 1, 4),
    _NsrpClusterUnitDataMac_Type()
)
nsrpClusterUnitDataMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpClusterUnitDataMac.setStatus("current")
_NetscreenNsrpLinkInfo_ObjectIdentity = ObjectIdentity
netscreenNsrpLinkInfo = _NetscreenNsrpLinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6)
)
_NsrpLinkInfoTable_Object = MibTable
nsrpLinkInfoTable = _NsrpLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1)
)
if mibBuilder.loadTexts:
    nsrpLinkInfoTable.setStatus("current")
_NsrpLinkInfoEntry_Object = MibTableRow
nsrpLinkInfoEntry = _NsrpLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1)
)
nsrpLinkInfoEntry.setIndexNames(
    (0, "NETSCREEN-NSRP-MIB", "nsrpLinkInfoIndex"),
)
if mibBuilder.loadTexts:
    nsrpLinkInfoEntry.setStatus("current")


class _NsrpLinkInfoIndex_Type(Integer32):
    """Custom type nsrpLinkInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsrpLinkInfoIndex_Type.__name__ = "Integer32"
_NsrpLinkInfoIndex_Object = MibTableColumn
nsrpLinkInfoIndex = _NsrpLinkInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 1),
    _NsrpLinkInfoIndex_Type()
)
nsrpLinkInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpLinkInfoIndex.setStatus("current")


class _NsrpLinkInfoLinkType_Type(Integer32):
    """Custom type nsrpLinkInfoLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("control", 0),
          ("data", 1),
          ("hapath2", 3),
          ("unused", 2))
    )


_NsrpLinkInfoLinkType_Type.__name__ = "Integer32"
_NsrpLinkInfoLinkType_Object = MibTableColumn
nsrpLinkInfoLinkType = _NsrpLinkInfoLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 2),
    _NsrpLinkInfoLinkType_Type()
)
nsrpLinkInfoLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpLinkInfoLinkType.setStatus("current")


class _NsrpLinkInfoChannel_Type(DisplayString):
    """Custom type nsrpLinkInfoChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsrpLinkInfoChannel_Type.__name__ = "DisplayString"
_NsrpLinkInfoChannel_Object = MibTableColumn
nsrpLinkInfoChannel = _NsrpLinkInfoChannel_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 3),
    _NsrpLinkInfoChannel_Type()
)
nsrpLinkInfoChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpLinkInfoChannel.setStatus("current")
_NsrpLinkInfoMac_Type = PhysAddress
_NsrpLinkInfoMac_Object = MibTableColumn
nsrpLinkInfoMac = _NsrpLinkInfoMac_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 4),
    _NsrpLinkInfoMac_Type()
)
nsrpLinkInfoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpLinkInfoMac.setStatus("current")


class _NsrpLinkInfoState_Type(Integer32):
    """Custom type nsrpLinkInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_NsrpLinkInfoState_Type.__name__ = "Integer32"
_NsrpLinkInfoState_Object = MibTableColumn
nsrpLinkInfoState = _NsrpLinkInfoState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 6, 6, 1, 1, 5),
    _NsrpLinkInfoState_Type()
)
nsrpLinkInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsrpLinkInfoState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-NSRP-MIB",
    **{"netscreenNsrpMibModule": netscreenNsrpMibModule,
       "netscreenNsrpGeneral": netscreenNsrpGeneral,
       "nsrpGeneralClusterId": nsrpGeneralClusterId,
       "nsrpGeneralLocalUnitId": nsrpGeneralLocalUnitId,
       "nsrpGeneralEncrypEnable": nsrpGeneralEncrypEnable,
       "nsrpGeneralAuthEnable": nsrpGeneralAuthEnable,
       "nsrpGeneralIfMonitor": nsrpGeneralIfMonitor,
       "nsrpGeneralGratArps": nsrpGeneralGratArps,
       "netscreenNsrpVSD": netscreenNsrpVSD,
       "nsrpVsdGroupTable": nsrpVsdGroupTable,
       "nsrpVsdGroupEntry": nsrpVsdGroupEntry,
       "nsrpVsdGroupID": nsrpVsdGroupID,
       "nsrpVsdGroupPriority": nsrpVsdGroupPriority,
       "nsrpVsdGroupPreempt": nsrpVsdGroupPreempt,
       "nsrpVsdGroupHoldDownTime": nsrpVsdGroupHoldDownTime,
       "nsrpVsdGroupNumberOfUnit": nsrpVsdGroupNumberOfUnit,
       "nsrpVsdGroupCntStateChange": nsrpVsdGroupCntStateChange,
       "nsrpVsdGroupCntToInit": nsrpVsdGroupCntToInit,
       "nsrpVsdGroupCntToMaster": nsrpVsdGroupCntToMaster,
       "nsrpVsdGroupCntToPBackup": nsrpVsdGroupCntToPBackup,
       "nsrpVsdGroupCntToBackup": nsrpVsdGroupCntToBackup,
       "nsrpVsdGroupCntToIneligible": nsrpVsdGroupCntToIneligible,
       "nsrpVsdGroupCntToInoperable": nsrpVsdGroupCntToInoperable,
       "nsrpVsdGroupCntMasterConflict": nsrpVsdGroupCntMasterConflict,
       "nsrpVsdGroupCntPbConfilict": nsrpVsdGroupCntPbConfilict,
       "nsrpVsdGroupCntHeartbeatTx": nsrpVsdGroupCntHeartbeatTx,
       "nsrpVsdGroupCntHeartbeatRx": nsrpVsdGroupCntHeartbeatRx,
       "nsrpVsdMemberTable": nsrpVsdMemberTable,
       "nsrpVsdMemberEntry": nsrpVsdMemberEntry,
       "nsrpVsdMemberGroupId": nsrpVsdMemberGroupId,
       "nsrpVsdMemberUnitId": nsrpVsdMemberUnitId,
       "nsrpVsdMemberStatus": nsrpVsdMemberStatus,
       "nsrpVsdMemberPriority": nsrpVsdMemberPriority,
       "nsrpVsdMemberPreempt": nsrpVsdMemberPreempt,
       "nsrpVsdInterfaceTable": nsrpVsdInterfaceTable,
       "nsrpVsdInterfaceEntry": nsrpVsdInterfaceEntry,
       "nsrpVsdIfIndex": nsrpVsdIfIndex,
       "nsrpVsdIfStatus": nsrpVsdIfStatus,
       "nsrpVsdIfGroupId": nsrpVsdIfGroupId,
       "nsrpVsdIfIp": nsrpVsdIfIp,
       "nsrpVsdIfNetmask": nsrpVsdIfNetmask,
       "nsrpVsdIfGateway": nsrpVsdIfGateway,
       "nsrpVsdIfName": nsrpVsdIfName,
       "nsrpVsdIfVLAN": nsrpVsdIfVLAN,
       "nsrpVsdIfMAC": nsrpVsdIfMAC,
       "nsrpVsdIfVSys": nsrpVsdIfVSys,
       "nsrpVsdIfMngTelnet": nsrpVsdIfMngTelnet,
       "nsrpVsdIfMngSCS": nsrpVsdIfMngSCS,
       "nsrpVsdIfMngWEB": nsrpVsdIfMngWEB,
       "nsrpVsdIfMngSSL": nsrpVsdIfMngSSL,
       "nsrpVsdIfMngSNMP": nsrpVsdIfMngSNMP,
       "nsrpVsdIfMngGlobal": nsrpVsdIfMngGlobal,
       "nsrpVsdIfMngGlobalPro": nsrpVsdIfMngGlobalPro,
       "nsrpVsdIfMngPing": nsrpVsdIfMngPing,
       "nsrpVsdIfMngIdentReset": nsrpVsdIfMngIdentReset,
       "nsrpVsdGeneral": nsrpVsdGeneral,
       "nsrpVsdGeneralInitHoldTime": nsrpVsdGeneralInitHoldTime,
       "nsrpVsdGeneralHbInterval": nsrpVsdGeneralHbInterval,
       "nsrpVsdGeneralHbLostThres": nsrpVsdGeneralHbLostThres,
       "netscreenNsrpRTO": netscreenNsrpRTO,
       "nsrpRtoGroupTable": nsrpRtoGroupTable,
       "nsrpRtoGroupEntry": nsrpRtoGroupEntry,
       "nsrpRtoGroupId": nsrpRtoGroupId,
       "nsrpRtoNumOfUnit": nsrpRtoNumOfUnit,
       "nsrpRtoUnitTable": nsrpRtoUnitTable,
       "nsrpRtoUnitEntry": nsrpRtoUnitEntry,
       "nsrpRtoUnitGroupId": nsrpRtoUnitGroupId,
       "nsrpRtoUnitId": nsrpRtoUnitId,
       "nsrpRtoUnitStatus": nsrpRtoUnitStatus,
       "nsrpRtoUnitDirection": nsrpRtoUnitDirection,
       "nsrpRtoUnitLostHeartbeat": nsrpRtoUnitLostHeartbeat,
       "nsrpRtoUnitToActive": nsrpRtoUnitToActive,
       "nsrpRtoUnitToSet": nsrpRtoUnitToSet,
       "nsrpRtoUnitLostPeer": nsrpRtoUnitLostPeer,
       "nsrpRtoUnitGroupDetach": nsrpRtoUnitGroupDetach,
       "nsrpRtoCounter": nsrpRtoCounter,
       "nsrpRtoCounterPakForwarded": nsrpRtoCounterPakForwarded,
       "nsrpRtoCounterPakReceived": nsrpRtoCounterPakReceived,
       "nsrpRtoCounterTable": nsrpRtoCounterTable,
       "nsrpRtoCounterEntry": nsrpRtoCounterEntry,
       "nsrpRtoCounterIdx": nsrpRtoCounterIdx,
       "nsrpRtoCounterName": nsrpRtoCounterName,
       "nsrpRtoCounterSend": nsrpRtoCounterSend,
       "nsrpRtoCounterReceive": nsrpRtoCounterReceive,
       "nsrpRtoCounterDrop": nsrpRtoCounterDrop,
       "nsrpRtoGeneral": nsrpRtoGeneral,
       "nsrpRtoGeneralHbInterval": nsrpRtoGeneralHbInterval,
       "nsrpRtoGeneralHbLostThres": nsrpRtoGeneralHbLostThres,
       "nsrpRtoGeneralSessSyncEnable": nsrpRtoGeneralSessSyncEnable,
       "netscreenNsrpTrack": netscreenNsrpTrack,
       "nsrpTrackEnable": nsrpTrackEnable,
       "nsrpTrackThreshold": nsrpTrackThreshold,
       "nsrpTrackFailoverEnalble": nsrpTrackFailoverEnalble,
       "nsrpTrackTable": nsrpTrackTable,
       "nsrpTrackEntry": nsrpTrackEntry,
       "nsrpTrackIpIndex": nsrpTrackIpIndex,
       "nsrpTrackIpAddr": nsrpTrackIpAddr,
       "nsrpTrackIpStatus": nsrpTrackIpStatus,
       "nsrpTrackIpTimestamp": nsrpTrackIpTimestamp,
       "nsrpTrackIpInterval": nsrpTrackIpInterval,
       "nsrpTrackIpThreshhold": nsrpTrackIpThreshhold,
       "nsrpTrackIpMethod": nsrpTrackIpMethod,
       "nsrpTrackIpWeight": nsrpTrackIpWeight,
       "nsrpTrackIpIfName": nsrpTrackIpIfName,
       "nsrpTrackIpTotalCheck": nsrpTrackIpTotalCheck,
       "nsrpTrackIpTotalFailedCheck": nsrpTrackIpTotalFailedCheck,
       "netscreenNsrpCluster": netscreenNsrpCluster,
       "nsrpClusterTable": nsrpClusterTable,
       "nsrpClusterEntry": nsrpClusterEntry,
       "nsrpClusterTblIndex": nsrpClusterTblIndex,
       "nsrpClusterUnitId": nsrpClusterUnitId,
       "nsrpClusterUnitCtrlMac": nsrpClusterUnitCtrlMac,
       "nsrpClusterUnitDataMac": nsrpClusterUnitDataMac,
       "netscreenNsrpLinkInfo": netscreenNsrpLinkInfo,
       "nsrpLinkInfoTable": nsrpLinkInfoTable,
       "nsrpLinkInfoEntry": nsrpLinkInfoEntry,
       "nsrpLinkInfoIndex": nsrpLinkInfoIndex,
       "nsrpLinkInfoLinkType": nsrpLinkInfoLinkType,
       "nsrpLinkInfoChannel": nsrpLinkInfoChannel,
       "nsrpLinkInfoMac": nsrpLinkInfoMac,
       "nsrpLinkInfoState": nsrpLinkInfoState}
)
