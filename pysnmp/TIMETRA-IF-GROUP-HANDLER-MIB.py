# SNMP MIB module (TIMETRA-IF-GROUP-HANDLER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-IF-GROUP-HANDLER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:26 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(tmnxChassisIndex,) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortPortID,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortPortID")

(TItemDescription,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState")


# MODULE-IDENTITY

timetraIfGroupMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 69)
)
timetraIfGroupMIBModule.setRevisions(
        ("1909-02-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIfGroupHandlerIndex(Unsigned32, TextualConvention):
    status = "current"


class TmnxIfGroupProtocolIndex(Integer32, TextualConvention):
    status = "current"
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
        *(("ipcp", 1),
          ("ipv6cp", 2),
          ("mplscp", 3),
          ("osicp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxIfGroupConformance_ObjectIdentity = ObjectIdentity
tmnxIfGroupConformance = _TmnxIfGroupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69)
)
_TmnxIfGroupCompliances_ObjectIdentity = ObjectIdentity
tmnxIfGroupCompliances = _TmnxIfGroupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 1)
)
_TmnxIfGroupGroups_ObjectIdentity = ObjectIdentity
tmnxIfGroupGroups = _TmnxIfGroupGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2)
)
_TmnxIfGroupObjs_ObjectIdentity = ObjectIdentity
tmnxIfGroupObjs = _TmnxIfGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69)
)
_TmnxIfGroupConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxIfGroupConfigTimeStamps = _TmnxIfGroupConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 0)
)
_TmnxIfGrpHndlrCfgTblLastChanged_Type = TimeStamp
_TmnxIfGrpHndlrCfgTblLastChanged_Object = MibScalar
tmnxIfGrpHndlrCfgTblLastChanged = _TmnxIfGrpHndlrCfgTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 0, 1),
    _TmnxIfGrpHndlrCfgTblLastChanged_Type()
)
tmnxIfGrpHndlrCfgTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGrpHndlrCfgTblLastChanged.setStatus("current")
_TmnxIfGrpHndlrMbrTblLastChanged_Type = TimeStamp
_TmnxIfGrpHndlrMbrTblLastChanged_Object = MibScalar
tmnxIfGrpHndlrMbrTblLastChanged = _TmnxIfGrpHndlrMbrTblLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 0, 2),
    _TmnxIfGrpHndlrMbrTblLastChanged_Type()
)
tmnxIfGrpHndlrMbrTblLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGrpHndlrMbrTblLastChanged.setStatus("current")
_TmnxIfGroupConfigurations_ObjectIdentity = ObjectIdentity
tmnxIfGroupConfigurations = _TmnxIfGroupConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1)
)
_TmnxIfGroupHandlerConfigTable_Object = MibTable
tmnxIfGroupHandlerConfigTable = _TmnxIfGroupHandlerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerConfigTable.setStatus("current")
_TmnxIfGroupHandlerConfigEntry_Object = MibTableRow
tmnxIfGroupHandlerConfigEntry = _TmnxIfGroupHandlerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1)
)
tmnxIfGroupHandlerConfigEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerIndex"),
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerConfigEntry.setStatus("current")


class _TmnxIfGroupHandlerIndex_Type(TmnxIfGroupHandlerIndex):
    """Custom type tmnxIfGroupHandlerIndex based on TmnxIfGroupHandlerIndex"""
    subtypeSpec = TmnxIfGroupHandlerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxIfGroupHandlerIndex_Type.__name__ = "TmnxIfGroupHandlerIndex"
_TmnxIfGroupHandlerIndex_Object = MibTableColumn
tmnxIfGroupHandlerIndex = _TmnxIfGroupHandlerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1, 1),
    _TmnxIfGroupHandlerIndex_Type()
)
tmnxIfGroupHandlerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerIndex.setStatus("current")
_TmnxIfGroupHandlerRowStatus_Type = RowStatus
_TmnxIfGroupHandlerRowStatus_Object = MibTableColumn
tmnxIfGroupHandlerRowStatus = _TmnxIfGroupHandlerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1, 2),
    _TmnxIfGroupHandlerRowStatus_Type()
)
tmnxIfGroupHandlerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerRowStatus.setStatus("current")
_TmnxIfGroupHandlerTimeStamp_Type = TimeStamp
_TmnxIfGroupHandlerTimeStamp_Object = MibTableColumn
tmnxIfGroupHandlerTimeStamp = _TmnxIfGroupHandlerTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1, 3),
    _TmnxIfGroupHandlerTimeStamp_Type()
)
tmnxIfGroupHandlerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerTimeStamp.setStatus("current")


class _TmnxIfGroupHandlerThreshold_Type(Unsigned32):
    """Custom type tmnxIfGroupHandlerThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxIfGroupHandlerThreshold_Type.__name__ = "Unsigned32"
_TmnxIfGroupHandlerThreshold_Object = MibTableColumn
tmnxIfGroupHandlerThreshold = _TmnxIfGroupHandlerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1, 4),
    _TmnxIfGroupHandlerThreshold_Type()
)
tmnxIfGroupHandlerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerThreshold.setStatus("current")


class _TmnxIfGroupHandlerAdminStatus_Type(TmnxAdminState):
    """Custom type tmnxIfGroupHandlerAdminStatus based on TmnxAdminState"""


_TmnxIfGroupHandlerAdminStatus_Object = MibTableColumn
tmnxIfGroupHandlerAdminStatus = _TmnxIfGroupHandlerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 1, 1, 5),
    _TmnxIfGroupHandlerAdminStatus_Type()
)
tmnxIfGroupHandlerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerAdminStatus.setStatus("current")
_TmnxIfGroupHandlerProtoTable_Object = MibTable
tmnxIfGroupHandlerProtoTable = _TmnxIfGroupHandlerProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerProtoTable.setStatus("current")
_TmnxIfGroupHandlerProtoEntry_Object = MibTableRow
tmnxIfGroupHandlerProtoEntry = _TmnxIfGroupHandlerProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2, 1)
)
tmnxIfGroupHandlerProtoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerIndex"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoIndex"),
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerProtoEntry.setStatus("current")
_TmnxIfGroupHdlrProtoIndex_Type = TmnxIfGroupProtocolIndex
_TmnxIfGroupHdlrProtoIndex_Object = MibTableColumn
tmnxIfGroupHdlrProtoIndex = _TmnxIfGroupHdlrProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2, 1, 1),
    _TmnxIfGroupHdlrProtoIndex_Type()
)
tmnxIfGroupHdlrProtoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrProtoIndex.setStatus("current")


class _TmnxIfGroupHdlrProtoStatus_Type(Integer32):
    """Custom type tmnxIfGroupHdlrProtoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("inhibited", 2),
          ("none", 0),
          ("pending", 4),
          ("up", 5),
          ("waiting", 3))
    )


_TmnxIfGroupHdlrProtoStatus_Type.__name__ = "Integer32"
_TmnxIfGroupHdlrProtoStatus_Object = MibTableColumn
tmnxIfGroupHdlrProtoStatus = _TmnxIfGroupHdlrProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2, 1, 2),
    _TmnxIfGroupHdlrProtoStatus_Type()
)
tmnxIfGroupHdlrProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrProtoStatus.setStatus("current")
_TmnxIfGroupHdlrProtoActLinks_Type = Unsigned32
_TmnxIfGroupHdlrProtoActLinks_Object = MibTableColumn
tmnxIfGroupHdlrProtoActLinks = _TmnxIfGroupHdlrProtoActLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2, 1, 3),
    _TmnxIfGroupHdlrProtoActLinks_Type()
)
tmnxIfGroupHdlrProtoActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrProtoActLinks.setStatus("current")
_TmnxIfGroupHdlrProtoUpTime_Type = Unsigned32
_TmnxIfGroupHdlrProtoUpTime_Object = MibTableColumn
tmnxIfGroupHdlrProtoUpTime = _TmnxIfGroupHdlrProtoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 2, 1, 4),
    _TmnxIfGroupHdlrProtoUpTime_Type()
)
tmnxIfGroupHdlrProtoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrProtoUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrProtoUpTime.setUnits("seconds")
_TmnxIfGroupHandlerMemberTable_Object = MibTable
tmnxIfGroupHandlerMemberTable = _TmnxIfGroupHandlerMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerMemberTable.setStatus("current")
_TmnxIfGroupHandlerMemberEntry_Object = MibTableRow
tmnxIfGroupHandlerMemberEntry = _TmnxIfGroupHandlerMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 3, 1)
)
tmnxIfGroupHandlerMemberEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerMemberEntry.setStatus("current")
_TmnxIfGrpHandlerMemberRowStatus_Type = RowStatus
_TmnxIfGrpHandlerMemberRowStatus_Object = MibTableColumn
tmnxIfGrpHandlerMemberRowStatus = _TmnxIfGrpHandlerMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 3, 1, 1),
    _TmnxIfGrpHandlerMemberRowStatus_Type()
)
tmnxIfGrpHandlerMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIfGrpHandlerMemberRowStatus.setStatus("current")
_TmnxIfGroupHdlrMemberProtoTable_Object = MibTable
tmnxIfGroupHdlrMemberProtoTable = _TmnxIfGroupHdlrMemberProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoTable.setStatus("current")
_TmnxIfGroupHdlrMemberProtoEntry_Object = MibTableRow
tmnxIfGroupHdlrMemberProtoEntry = _TmnxIfGroupHdlrMemberProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 4, 1)
)
tmnxIfGroupHdlrMemberProtoEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrMemberProtoIndex"),
)
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoEntry.setStatus("current")
_TmnxIfGroupHdlrMemberProtoIndex_Type = TmnxIfGroupProtocolIndex
_TmnxIfGroupHdlrMemberProtoIndex_Object = MibTableColumn
tmnxIfGroupHdlrMemberProtoIndex = _TmnxIfGroupHdlrMemberProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 4, 1, 1),
    _TmnxIfGroupHdlrMemberProtoIndex_Type()
)
tmnxIfGroupHdlrMemberProtoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoIndex.setStatus("current")


class _TmnxIfGroupHdlrMemberProtoStatus_Type(Integer32):
    """Custom type tmnxIfGroupHdlrMemberProtoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("none", 0),
          ("operational", 4),
          ("ready", 2),
          ("running", 3),
          ("up", 5))
    )


_TmnxIfGroupHdlrMemberProtoStatus_Type.__name__ = "Integer32"
_TmnxIfGroupHdlrMemberProtoStatus_Object = MibTableColumn
tmnxIfGroupHdlrMemberProtoStatus = _TmnxIfGroupHdlrMemberProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 4, 1, 2),
    _TmnxIfGroupHdlrMemberProtoStatus_Type()
)
tmnxIfGroupHdlrMemberProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoStatus.setStatus("current")
_TmnxIfGroupHdlrMemberProtoUpTime_Type = Unsigned32
_TmnxIfGroupHdlrMemberProtoUpTime_Object = MibTableColumn
tmnxIfGroupHdlrMemberProtoUpTime = _TmnxIfGroupHdlrMemberProtoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 1, 4, 1, 3),
    _TmnxIfGroupHdlrMemberProtoUpTime_Type()
)
tmnxIfGroupHdlrMemberProtoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMemberProtoUpTime.setUnits("seconds")
_TmnxIfGroupStatistics_ObjectIdentity = ObjectIdentity
tmnxIfGroupStatistics = _TmnxIfGroupStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 69, 2)
)
_TmnxIfGroupNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxIfGroupNotifyPrefix = _TmnxIfGroupNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 69)
)
_TmnxIfGroupNotifications_ObjectIdentity = ObjectIdentity
tmnxIfGroupNotifications = _TmnxIfGroupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 69, 0)
)

# Managed Objects groups

tmnxIfGroupHandlerTimeStampGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2, 1)
)
tmnxIfGroupHandlerTimeStampGroup.setObjects(
      *(("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGrpHndlrCfgTblLastChanged"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerTimeStamp"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGrpHndlrMbrTblLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerTimeStampGroup.setStatus("current")

tmnxIfGroupHandlerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2, 2)
)
tmnxIfGroupHandlerConfigGroup.setObjects(
      *(("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerRowStatus"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerThreshold"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerAdminStatus"))
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerConfigGroup.setStatus("current")

tmnxIfGroupHandlerMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2, 3)
)
tmnxIfGroupHandlerMemberGroup.setObjects(
    ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGrpHandlerMemberRowStatus")
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerMemberGroup.setStatus("current")

tmnxIfGroupHandlerProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2, 4)
)
tmnxIfGroupHandlerProtocolGroup.setObjects(
      *(("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrMemberProtoStatus"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrMemberProtoUpTime"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoStatus"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoActLinks"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoUpTime"))
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerProtocolGroup.setStatus("current")


# Notification objects

tmnxIfGroupHandlerProtoOprChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 69, 0, 1)
)
tmnxIfGroupHandlerProtoOprChange.setObjects(
      *(("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerThreshold"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerAdminStatus"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoStatus"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrProtoActLinks"))
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerProtoOprChange.setStatus(
        "current"
    )

tmnxIfGroupHdlrMbrProtoOprChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 69, 0, 2)
)
tmnxIfGroupHdlrMbrProtoOprChange.setObjects(
    ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrMemberProtoStatus")
)
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrMbrProtoOprChange.setStatus(
        "current"
    )


# Notifications groups

tmnxIfGroupHdlrNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 2, 5)
)
tmnxIfGroupHdlrNotificationGroup.setObjects(
      *(("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHandlerProtoOprChange"),
        ("TIMETRA-IF-GROUP-HANDLER-MIB", "tmnxIfGroupHdlrMbrProtoOprChange"))
)
if mibBuilder.loadTexts:
    tmnxIfGroupHdlrNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxIfGroupHandlerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 69, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxIfGroupHandlerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IF-GROUP-HANDLER-MIB",
    **{"TmnxIfGroupHandlerIndex": TmnxIfGroupHandlerIndex,
       "TmnxIfGroupProtocolIndex": TmnxIfGroupProtocolIndex,
       "timetraIfGroupMIBModule": timetraIfGroupMIBModule,
       "tmnxIfGroupConformance": tmnxIfGroupConformance,
       "tmnxIfGroupCompliances": tmnxIfGroupCompliances,
       "tmnxIfGroupHandlerCompliance": tmnxIfGroupHandlerCompliance,
       "tmnxIfGroupGroups": tmnxIfGroupGroups,
       "tmnxIfGroupHandlerTimeStampGroup": tmnxIfGroupHandlerTimeStampGroup,
       "tmnxIfGroupHandlerConfigGroup": tmnxIfGroupHandlerConfigGroup,
       "tmnxIfGroupHandlerMemberGroup": tmnxIfGroupHandlerMemberGroup,
       "tmnxIfGroupHandlerProtocolGroup": tmnxIfGroupHandlerProtocolGroup,
       "tmnxIfGroupHdlrNotificationGroup": tmnxIfGroupHdlrNotificationGroup,
       "tmnxIfGroupObjs": tmnxIfGroupObjs,
       "tmnxIfGroupConfigTimeStamps": tmnxIfGroupConfigTimeStamps,
       "tmnxIfGrpHndlrCfgTblLastChanged": tmnxIfGrpHndlrCfgTblLastChanged,
       "tmnxIfGrpHndlrMbrTblLastChanged": tmnxIfGrpHndlrMbrTblLastChanged,
       "tmnxIfGroupConfigurations": tmnxIfGroupConfigurations,
       "tmnxIfGroupHandlerConfigTable": tmnxIfGroupHandlerConfigTable,
       "tmnxIfGroupHandlerConfigEntry": tmnxIfGroupHandlerConfigEntry,
       "tmnxIfGroupHandlerIndex": tmnxIfGroupHandlerIndex,
       "tmnxIfGroupHandlerRowStatus": tmnxIfGroupHandlerRowStatus,
       "tmnxIfGroupHandlerTimeStamp": tmnxIfGroupHandlerTimeStamp,
       "tmnxIfGroupHandlerThreshold": tmnxIfGroupHandlerThreshold,
       "tmnxIfGroupHandlerAdminStatus": tmnxIfGroupHandlerAdminStatus,
       "tmnxIfGroupHandlerProtoTable": tmnxIfGroupHandlerProtoTable,
       "tmnxIfGroupHandlerProtoEntry": tmnxIfGroupHandlerProtoEntry,
       "tmnxIfGroupHdlrProtoIndex": tmnxIfGroupHdlrProtoIndex,
       "tmnxIfGroupHdlrProtoStatus": tmnxIfGroupHdlrProtoStatus,
       "tmnxIfGroupHdlrProtoActLinks": tmnxIfGroupHdlrProtoActLinks,
       "tmnxIfGroupHdlrProtoUpTime": tmnxIfGroupHdlrProtoUpTime,
       "tmnxIfGroupHandlerMemberTable": tmnxIfGroupHandlerMemberTable,
       "tmnxIfGroupHandlerMemberEntry": tmnxIfGroupHandlerMemberEntry,
       "tmnxIfGrpHandlerMemberRowStatus": tmnxIfGrpHandlerMemberRowStatus,
       "tmnxIfGroupHdlrMemberProtoTable": tmnxIfGroupHdlrMemberProtoTable,
       "tmnxIfGroupHdlrMemberProtoEntry": tmnxIfGroupHdlrMemberProtoEntry,
       "tmnxIfGroupHdlrMemberProtoIndex": tmnxIfGroupHdlrMemberProtoIndex,
       "tmnxIfGroupHdlrMemberProtoStatus": tmnxIfGroupHdlrMemberProtoStatus,
       "tmnxIfGroupHdlrMemberProtoUpTime": tmnxIfGroupHdlrMemberProtoUpTime,
       "tmnxIfGroupStatistics": tmnxIfGroupStatistics,
       "tmnxIfGroupNotifyPrefix": tmnxIfGroupNotifyPrefix,
       "tmnxIfGroupNotifications": tmnxIfGroupNotifications,
       "tmnxIfGroupHandlerProtoOprChange": tmnxIfGroupHandlerProtoOprChange,
       "tmnxIfGroupHdlrMbrProtoOprChange": tmnxIfGroupHdlrMbrProtoOprChange}
)
