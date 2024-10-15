# SNMP MIB module (CISCO-VIRTUAL-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VIRTUAL-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:45 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVirtualSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388)
)
ciscoVirtualSwitchMIB.setRevisions(
        ("2015-03-04 00:00",
         "2012-04-10 00:00",
         "2010-01-21 00:00",
         "2007-09-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VSSwitchID(Unsigned32, TextualConvention):
    status = "current"


class VSSwitchCapability(Bits, TextualConvention):
    status = "current"


class VSSwitchMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiNode", 2),
          ("standalone", 1))
    )



class VSSwitchRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standalone", 1),
          ("standby", 3))
    )



class VSConnectStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_CiscoVirtualSwitchMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVirtualSwitchMIBNotifs = _CiscoVirtualSwitchMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 0)
)
_CiscoVirtualSwitchMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVirtualSwitchMIBObjects = _CiscoVirtualSwitchMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1)
)
_CvsGlobalObjects_ObjectIdentity = ObjectIdentity
cvsGlobalObjects = _CvsGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1)
)
_CvsDomain_Type = Unsigned32
_CvsDomain_Object = MibScalar
cvsDomain = _CvsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 1),
    _CvsDomain_Type()
)
cvsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsDomain.setStatus("current")
_CvsSwitchID_Type = VSSwitchID
_CvsSwitchID_Object = MibScalar
cvsSwitchID = _CvsSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 2),
    _CvsSwitchID_Type()
)
cvsSwitchID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsSwitchID.setStatus("current")
_CvsSwitchCapability_Type = VSSwitchCapability
_CvsSwitchCapability_Object = MibScalar
cvsSwitchCapability = _CvsSwitchCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 3),
    _CvsSwitchCapability_Type()
)
cvsSwitchCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsSwitchCapability.setStatus("current")
_CvsSwitchMode_Type = VSSwitchMode
_CvsSwitchMode_Object = MibScalar
cvsSwitchMode = _CvsSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 4),
    _CvsSwitchMode_Type()
)
cvsSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsSwitchMode.setStatus("current")
_CvsSwitchConvertingStatus_Type = TruthValue
_CvsSwitchConvertingStatus_Object = MibScalar
cvsSwitchConvertingStatus = _CvsSwitchConvertingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 5),
    _CvsSwitchConvertingStatus_Type()
)
cvsSwitchConvertingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsSwitchConvertingStatus.setStatus("current")
_CvsVSLChangeNotifEnable_Type = TruthValue
_CvsVSLChangeNotifEnable_Object = MibScalar
cvsVSLChangeNotifEnable = _CvsVSLChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 1, 6),
    _CvsVSLChangeNotifEnable_Type()
)
cvsVSLChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsVSLChangeNotifEnable.setStatus("current")
_CvsChassisObjects_ObjectIdentity = ObjectIdentity
cvsChassisObjects = _CvsChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2)
)
_CvsCoreSwitchConfigTable_Object = MibTable
cvsCoreSwitchConfigTable = _CvsCoreSwitchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cvsCoreSwitchConfigTable.setStatus("current")
_CvsCoreSwitchConfigEntry_Object = MibTableRow
cvsCoreSwitchConfigEntry = _CvsCoreSwitchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1)
)
cvsCoreSwitchConfigEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchID"),
)
if mibBuilder.loadTexts:
    cvsCoreSwitchConfigEntry.setStatus("current")
_CvsCoreSwitchID_Type = VSSwitchID
_CvsCoreSwitchID_Object = MibTableColumn
cvsCoreSwitchID = _CvsCoreSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 1),
    _CvsCoreSwitchID_Type()
)
cvsCoreSwitchID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvsCoreSwitchID.setStatus("current")
_CvsCoreSwitchPriority_Type = Unsigned32
_CvsCoreSwitchPriority_Object = MibTableColumn
cvsCoreSwitchPriority = _CvsCoreSwitchPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 2),
    _CvsCoreSwitchPriority_Type()
)
cvsCoreSwitchPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsCoreSwitchPriority.setStatus("current")
_CvsCoreSwitchPreempt_Type = TruthValue
_CvsCoreSwitchPreempt_Object = MibTableColumn
cvsCoreSwitchPreempt = _CvsCoreSwitchPreempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 3),
    _CvsCoreSwitchPreempt_Type()
)
cvsCoreSwitchPreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsCoreSwitchPreempt.setStatus("current")
_CvsCoreSwitchLocation_Type = SnmpAdminString
_CvsCoreSwitchLocation_Object = MibTableColumn
cvsCoreSwitchLocation = _CvsCoreSwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 1, 1, 4),
    _CvsCoreSwitchLocation_Type()
)
cvsCoreSwitchLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsCoreSwitchLocation.setStatus("current")
_CvsChassisTable_Object = MibTable
cvsChassisTable = _CvsChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cvsChassisTable.setStatus("current")
_CvsChassisEntry_Object = MibTableRow
cvsChassisEntry = _CvsChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1)
)
cvsChassisEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cvsChassisEntry.setStatus("current")
_CvsChassisSwitchID_Type = VSSwitchID
_CvsChassisSwitchID_Object = MibTableColumn
cvsChassisSwitchID = _CvsChassisSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 1),
    _CvsChassisSwitchID_Type()
)
cvsChassisSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsChassisSwitchID.setStatus("current")
_CvsChassisRole_Type = VSSwitchRole
_CvsChassisRole_Object = MibTableColumn
cvsChassisRole = _CvsChassisRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 2),
    _CvsChassisRole_Type()
)
cvsChassisRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsChassisRole.setStatus("current")
_CvsChassisUpTime_Type = TimeStamp
_CvsChassisUpTime_Object = MibTableColumn
cvsChassisUpTime = _CvsChassisUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 2, 2, 1, 3),
    _CvsChassisUpTime_Type()
)
cvsChassisUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsChassisUpTime.setStatus("current")
_CvsVSLObjects_ObjectIdentity = ObjectIdentity
cvsVSLObjects = _CvsVSLObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3)
)
_CvsVSLConnectionTable_Object = MibTable
cvsVSLConnectionTable = _CvsVSLConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cvsVSLConnectionTable.setStatus("current")
_CvsVSLConnectionEntry_Object = MibTableRow
cvsVSLConnectionEntry = _CvsVSLConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1)
)
cvsVSLConnectionEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"),
)
if mibBuilder.loadTexts:
    cvsVSLConnectionEntry.setStatus("current")
_CvsVSLChannelIfindex_Type = InterfaceIndex
_CvsVSLChannelIfindex_Object = MibTableColumn
cvsVSLChannelIfindex = _CvsVSLChannelIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 1),
    _CvsVSLChannelIfindex_Type()
)
cvsVSLChannelIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvsVSLChannelIfindex.setStatus("current")
_CvsVSLCoreSwitchID_Type = VSSwitchID
_CvsVSLCoreSwitchID_Object = MibTableColumn
cvsVSLCoreSwitchID = _CvsVSLCoreSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 2),
    _CvsVSLCoreSwitchID_Type()
)
cvsVSLCoreSwitchID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvsVSLCoreSwitchID.setStatus("current")
_CvsVSLConnectOperStatus_Type = VSConnectStatus
_CvsVSLConnectOperStatus_Object = MibTableColumn
cvsVSLConnectOperStatus = _CvsVSLConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 3),
    _CvsVSLConnectOperStatus_Type()
)
cvsVSLConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLConnectOperStatus.setStatus("current")
_CvsVSLLastConnectionStateChange_Type = DateAndTime
_CvsVSLLastConnectionStateChange_Object = MibTableColumn
cvsVSLLastConnectionStateChange = _CvsVSLLastConnectionStateChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 4),
    _CvsVSLLastConnectionStateChange_Type()
)
cvsVSLLastConnectionStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLLastConnectionStateChange.setStatus("current")
_CvsVSLConfiguredPortCount_Type = Unsigned32
_CvsVSLConfiguredPortCount_Object = MibTableColumn
cvsVSLConfiguredPortCount = _CvsVSLConfiguredPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 5),
    _CvsVSLConfiguredPortCount_Type()
)
cvsVSLConfiguredPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLConfiguredPortCount.setStatus("current")
_CvsVSLOperationalPortCount_Type = Unsigned32
_CvsVSLOperationalPortCount_Object = MibTableColumn
cvsVSLOperationalPortCount = _CvsVSLOperationalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 6),
    _CvsVSLOperationalPortCount_Type()
)
cvsVSLOperationalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLOperationalPortCount.setStatus("current")
_CvsVSLConnectionRowStatus_Type = RowStatus
_CvsVSLConnectionRowStatus_Object = MibTableColumn
cvsVSLConnectionRowStatus = _CvsVSLConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 1, 1, 7),
    _CvsVSLConnectionRowStatus_Type()
)
cvsVSLConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvsVSLConnectionRowStatus.setStatus("current")
_CvsVSLStatsTable_Object = MibTable
cvsVSLStatsTable = _CvsVSLStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cvsVSLStatsTable.setStatus("current")
_CvsVSLStatsEntry_Object = MibTableRow
cvsVSLStatsEntry = _CvsVSLStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1)
)
cvsVSLStatsEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"),
)
if mibBuilder.loadTexts:
    cvsVSLStatsEntry.setStatus("current")
_CvsVSLTxTotalPkts_Type = Counter32
_CvsVSLTxTotalPkts_Object = MibTableColumn
cvsVSLTxTotalPkts = _CvsVSLTxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 1),
    _CvsVSLTxTotalPkts_Type()
)
cvsVSLTxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxTotalPkts.setStatus("current")
_CvsVSLTxErrorPkts_Type = Counter32
_CvsVSLTxErrorPkts_Object = MibTableColumn
cvsVSLTxErrorPkts = _CvsVSLTxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 2),
    _CvsVSLTxErrorPkts_Type()
)
cvsVSLTxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxErrorPkts.setStatus("current")
_CvsVSLTxChksumErrPkts_Type = Counter32
_CvsVSLTxChksumErrPkts_Object = MibTableColumn
cvsVSLTxChksumErrPkts = _CvsVSLTxChksumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 3),
    _CvsVSLTxChksumErrPkts_Type()
)
cvsVSLTxChksumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxChksumErrPkts.setStatus("current")
_CvsVSLRxTotalPkts_Type = Counter32
_CvsVSLRxTotalPkts_Object = MibTableColumn
cvsVSLRxTotalPkts = _CvsVSLRxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 4),
    _CvsVSLRxTotalPkts_Type()
)
cvsVSLRxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxTotalPkts.setStatus("current")
_CvsVSLRxErrorPkts_Type = Counter32
_CvsVSLRxErrorPkts_Object = MibTableColumn
cvsVSLRxErrorPkts = _CvsVSLRxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 5),
    _CvsVSLRxErrorPkts_Type()
)
cvsVSLRxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxErrorPkts.setStatus("current")
_CvsVSLRxChksumErrPkts_Type = Counter32
_CvsVSLRxChksumErrPkts_Object = MibTableColumn
cvsVSLRxChksumErrPkts = _CvsVSLRxChksumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 6),
    _CvsVSLRxChksumErrPkts_Type()
)
cvsVSLRxChksumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxChksumErrPkts.setStatus("current")
_CvsVSLTxLmpPkts_Type = Counter64
_CvsVSLTxLmpPkts_Object = MibTableColumn
cvsVSLTxLmpPkts = _CvsVSLTxLmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 7),
    _CvsVSLTxLmpPkts_Type()
)
cvsVSLTxLmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxLmpPkts.setStatus("current")
_CvsVSLTxRrpPkts_Type = Counter64
_CvsVSLTxRrpPkts_Object = MibTableColumn
cvsVSLTxRrpPkts = _CvsVSLTxRrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 8),
    _CvsVSLTxRrpPkts_Type()
)
cvsVSLTxRrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxRrpPkts.setStatus("current")
_CvsVSLTxPingPkts_Type = Counter64
_CvsVSLTxPingPkts_Object = MibTableColumn
cvsVSLTxPingPkts = _CvsVSLTxPingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 9),
    _CvsVSLTxPingPkts_Type()
)
cvsVSLTxPingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxPingPkts.setStatus("current")
_CvsVSLTxProtoPkts_Type = Counter64
_CvsVSLTxProtoPkts_Object = MibTableColumn
cvsVSLTxProtoPkts = _CvsVSLTxProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 10),
    _CvsVSLTxProtoPkts_Type()
)
cvsVSLTxProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxProtoPkts.setStatus("current")
_CvsVSLTxDataPkts_Type = Counter64
_CvsVSLTxDataPkts_Object = MibTableColumn
cvsVSLTxDataPkts = _CvsVSLTxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 11),
    _CvsVSLTxDataPkts_Type()
)
cvsVSLTxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxDataPkts.setStatus("current")
_CvsVSLTxAckPkts_Type = Counter64
_CvsVSLTxAckPkts_Object = MibTableColumn
cvsVSLTxAckPkts = _CvsVSLTxAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 12),
    _CvsVSLTxAckPkts_Type()
)
cvsVSLTxAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxAckPkts.setStatus("current")
_CvsVSLRxLmpPkts_Type = Counter64
_CvsVSLRxLmpPkts_Object = MibTableColumn
cvsVSLRxLmpPkts = _CvsVSLRxLmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 13),
    _CvsVSLRxLmpPkts_Type()
)
cvsVSLRxLmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxLmpPkts.setStatus("current")
_CvsVSLRxRrpPkts_Type = Counter64
_CvsVSLRxRrpPkts_Object = MibTableColumn
cvsVSLRxRrpPkts = _CvsVSLRxRrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 14),
    _CvsVSLRxRrpPkts_Type()
)
cvsVSLRxRrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxRrpPkts.setStatus("current")
_CvsVSLRxPingPkts_Type = Counter64
_CvsVSLRxPingPkts_Object = MibTableColumn
cvsVSLRxPingPkts = _CvsVSLRxPingPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 15),
    _CvsVSLRxPingPkts_Type()
)
cvsVSLRxPingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxPingPkts.setStatus("current")
_CvsVSLRxProtoPkts_Type = Counter64
_CvsVSLRxProtoPkts_Object = MibTableColumn
cvsVSLRxProtoPkts = _CvsVSLRxProtoPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 16),
    _CvsVSLRxProtoPkts_Type()
)
cvsVSLRxProtoPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxProtoPkts.setStatus("current")
_CvsVSLRxDataPkts_Type = Counter64
_CvsVSLRxDataPkts_Object = MibTableColumn
cvsVSLRxDataPkts = _CvsVSLRxDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 17),
    _CvsVSLRxDataPkts_Type()
)
cvsVSLRxDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxDataPkts.setStatus("current")
_CvsVSLRxAckPkts_Type = Counter64
_CvsVSLRxAckPkts_Object = MibTableColumn
cvsVSLRxAckPkts = _CvsVSLRxAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 18),
    _CvsVSLRxAckPkts_Type()
)
cvsVSLRxAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxAckPkts.setStatus("current")
_CvsVSLTxTotalEobcPkts_Type = Counter64
_CvsVSLTxTotalEobcPkts_Object = MibTableColumn
cvsVSLTxTotalEobcPkts = _CvsVSLTxTotalEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 19),
    _CvsVSLTxTotalEobcPkts_Type()
)
cvsVSLTxTotalEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxTotalEobcPkts.setStatus("current")
_CvsVSLTxLmpEobcPkts_Type = Counter64
_CvsVSLTxLmpEobcPkts_Object = MibTableColumn
cvsVSLTxLmpEobcPkts = _CvsVSLTxLmpEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 20),
    _CvsVSLTxLmpEobcPkts_Type()
)
cvsVSLTxLmpEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxLmpEobcPkts.setStatus("current")
_CvsVSLTxRrpEobcPkts_Type = Counter64
_CvsVSLTxRrpEobcPkts_Object = MibTableColumn
cvsVSLTxRrpEobcPkts = _CvsVSLTxRrpEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 21),
    _CvsVSLTxRrpEobcPkts_Type()
)
cvsVSLTxRrpEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxRrpEobcPkts.setStatus("current")
_CvsVSLTxPingEobcPkts_Type = Counter64
_CvsVSLTxPingEobcPkts_Object = MibTableColumn
cvsVSLTxPingEobcPkts = _CvsVSLTxPingEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 22),
    _CvsVSLTxPingEobcPkts_Type()
)
cvsVSLTxPingEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxPingEobcPkts.setStatus("current")
_CvsVSLTxProtoEobcPkts_Type = Counter64
_CvsVSLTxProtoEobcPkts_Object = MibTableColumn
cvsVSLTxProtoEobcPkts = _CvsVSLTxProtoEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 23),
    _CvsVSLTxProtoEobcPkts_Type()
)
cvsVSLTxProtoEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxProtoEobcPkts.setStatus("current")
_CvsVSLTxDataEobcPkts_Type = Counter64
_CvsVSLTxDataEobcPkts_Object = MibTableColumn
cvsVSLTxDataEobcPkts = _CvsVSLTxDataEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 24),
    _CvsVSLTxDataEobcPkts_Type()
)
cvsVSLTxDataEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxDataEobcPkts.setStatus("current")
_CvsVSLTxAckEobcPkts_Type = Counter64
_CvsVSLTxAckEobcPkts_Object = MibTableColumn
cvsVSLTxAckEobcPkts = _CvsVSLTxAckEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 25),
    _CvsVSLTxAckEobcPkts_Type()
)
cvsVSLTxAckEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxAckEobcPkts.setStatus("current")
_CvsVSLRxTotalEobcPkts_Type = Counter64
_CvsVSLRxTotalEobcPkts_Object = MibTableColumn
cvsVSLRxTotalEobcPkts = _CvsVSLRxTotalEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 26),
    _CvsVSLRxTotalEobcPkts_Type()
)
cvsVSLRxTotalEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxTotalEobcPkts.setStatus("current")
_CvsVSLRxLmpEobcPkts_Type = Counter64
_CvsVSLRxLmpEobcPkts_Object = MibTableColumn
cvsVSLRxLmpEobcPkts = _CvsVSLRxLmpEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 27),
    _CvsVSLRxLmpEobcPkts_Type()
)
cvsVSLRxLmpEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxLmpEobcPkts.setStatus("current")
_CvsVSLRxRrpEobcPkts_Type = Counter64
_CvsVSLRxRrpEobcPkts_Object = MibTableColumn
cvsVSLRxRrpEobcPkts = _CvsVSLRxRrpEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 28),
    _CvsVSLRxRrpEobcPkts_Type()
)
cvsVSLRxRrpEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxRrpEobcPkts.setStatus("current")
_CvsVSLRxPingEobcPkts_Type = Counter64
_CvsVSLRxPingEobcPkts_Object = MibTableColumn
cvsVSLRxPingEobcPkts = _CvsVSLRxPingEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 29),
    _CvsVSLRxPingEobcPkts_Type()
)
cvsVSLRxPingEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxPingEobcPkts.setStatus("current")
_CvsVSLRxProtoEobcPkts_Type = Counter64
_CvsVSLRxProtoEobcPkts_Object = MibTableColumn
cvsVSLRxProtoEobcPkts = _CvsVSLRxProtoEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 30),
    _CvsVSLRxProtoEobcPkts_Type()
)
cvsVSLRxProtoEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxProtoEobcPkts.setStatus("current")
_CvsVSLRxDataEobcPkts_Type = Counter64
_CvsVSLRxDataEobcPkts_Object = MibTableColumn
cvsVSLRxDataEobcPkts = _CvsVSLRxDataEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 31),
    _CvsVSLRxDataEobcPkts_Type()
)
cvsVSLRxDataEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxDataEobcPkts.setStatus("current")
_CvsVSLRxAckEobcPkts_Type = Counter64
_CvsVSLRxAckEobcPkts_Object = MibTableColumn
cvsVSLRxAckEobcPkts = _CvsVSLRxAckEobcPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 32),
    _CvsVSLRxAckEobcPkts_Type()
)
cvsVSLRxAckEobcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxAckEobcPkts.setStatus("current")
_CvsVSLTxTotalHCPkts_Type = Counter64
_CvsVSLTxTotalHCPkts_Object = MibTableColumn
cvsVSLTxTotalHCPkts = _CvsVSLTxTotalHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 33),
    _CvsVSLTxTotalHCPkts_Type()
)
cvsVSLTxTotalHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxTotalHCPkts.setStatus("current")
_CvsVSLTxErrorHCPkts_Type = Counter64
_CvsVSLTxErrorHCPkts_Object = MibTableColumn
cvsVSLTxErrorHCPkts = _CvsVSLTxErrorHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 34),
    _CvsVSLTxErrorHCPkts_Type()
)
cvsVSLTxErrorHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxErrorHCPkts.setStatus("current")
_CvsVSLTxChksumErrHCPkts_Type = Counter64
_CvsVSLTxChksumErrHCPkts_Object = MibTableColumn
cvsVSLTxChksumErrHCPkts = _CvsVSLTxChksumErrHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 35),
    _CvsVSLTxChksumErrHCPkts_Type()
)
cvsVSLTxChksumErrHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLTxChksumErrHCPkts.setStatus("current")
_CvsVSLRxTotalHCPkts_Type = Counter64
_CvsVSLRxTotalHCPkts_Object = MibTableColumn
cvsVSLRxTotalHCPkts = _CvsVSLRxTotalHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 36),
    _CvsVSLRxTotalHCPkts_Type()
)
cvsVSLRxTotalHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxTotalHCPkts.setStatus("current")
_CvsVSLRxErrorHCPkts_Type = Counter64
_CvsVSLRxErrorHCPkts_Object = MibTableColumn
cvsVSLRxErrorHCPkts = _CvsVSLRxErrorHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 37),
    _CvsVSLRxErrorHCPkts_Type()
)
cvsVSLRxErrorHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxErrorHCPkts.setStatus("current")
_CvsVSLRxChksumErrHCPkts_Type = Counter64
_CvsVSLRxChksumErrHCPkts_Object = MibTableColumn
cvsVSLRxChksumErrHCPkts = _CvsVSLRxChksumErrHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 2, 1, 38),
    _CvsVSLRxChksumErrHCPkts_Type()
)
cvsVSLRxChksumErrHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLRxChksumErrHCPkts.setStatus("current")
_CvsVSLPortStatsTable_Object = MibTable
cvsVSLPortStatsTable = _CvsVSLPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cvsVSLPortStatsTable.setStatus("current")
_CvsVSLPortStatsEntry_Object = MibTableRow
cvsVSLPortStatsEntry = _CvsVSLPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1)
)
cvsVSLPortStatsEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"),
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortStatsIfindex"),
)
if mibBuilder.loadTexts:
    cvsVSLPortStatsEntry.setStatus("current")
_CvsVSLPortStatsIfindex_Type = InterfaceIndex
_CvsVSLPortStatsIfindex_Object = MibTableColumn
cvsVSLPortStatsIfindex = _CvsVSLPortStatsIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 1),
    _CvsVSLPortStatsIfindex_Type()
)
cvsVSLPortStatsIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvsVSLPortStatsIfindex.setStatus("current")
_CvsVSLPortTxOkPkts_Type = Counter32
_CvsVSLPortTxOkPkts_Object = MibTableColumn
cvsVSLPortTxOkPkts = _CvsVSLPortTxOkPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 2),
    _CvsVSLPortTxOkPkts_Type()
)
cvsVSLPortTxOkPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortTxOkPkts.setStatus("current")
_CvsVSLPortTxFailPkts_Type = Counter32
_CvsVSLPortTxFailPkts_Object = MibTableColumn
cvsVSLPortTxFailPkts = _CvsVSLPortTxFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 3),
    _CvsVSLPortTxFailPkts_Type()
)
cvsVSLPortTxFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortTxFailPkts.setStatus("current")
_CvsVSLPortRxBidirPkts_Type = Counter32
_CvsVSLPortRxBidirPkts_Object = MibTableColumn
cvsVSLPortRxBidirPkts = _CvsVSLPortRxBidirPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 4),
    _CvsVSLPortRxBidirPkts_Type()
)
cvsVSLPortRxBidirPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxBidirPkts.setStatus("current")
_CvsVSLPortRxUnidirPkts_Type = Counter32
_CvsVSLPortRxUnidirPkts_Object = MibTableColumn
cvsVSLPortRxUnidirPkts = _CvsVSLPortRxUnidirPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 5),
    _CvsVSLPortRxUnidirPkts_Type()
)
cvsVSLPortRxUnidirPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxUnidirPkts.setStatus("current")
_CvsVSLPortRxFailPkts_Type = Counter32
_CvsVSLPortRxFailPkts_Object = MibTableColumn
cvsVSLPortRxFailPkts = _CvsVSLPortRxFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 6),
    _CvsVSLPortRxFailPkts_Type()
)
cvsVSLPortRxFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxFailPkts.setStatus("current")
_CvsVSLPortRxBadPkts_Type = Counter32
_CvsVSLPortRxBadPkts_Object = MibTableColumn
cvsVSLPortRxBadPkts = _CvsVSLPortRxBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 7),
    _CvsVSLPortRxBadPkts_Type()
)
cvsVSLPortRxBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxBadPkts.setStatus("current")
_CvsVSLPortRxMyInfoMismatchPkts_Type = Counter32
_CvsVSLPortRxMyInfoMismatchPkts_Object = MibTableColumn
cvsVSLPortRxMyInfoMismatchPkts = _CvsVSLPortRxMyInfoMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 8),
    _CvsVSLPortRxMyInfoMismatchPkts_Type()
)
cvsVSLPortRxMyInfoMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxMyInfoMismatchPkts.setStatus("current")
_CvsVSLPortRxMyInfoAbsentPkts_Type = Counter32
_CvsVSLPortRxMyInfoAbsentPkts_Object = MibTableColumn
cvsVSLPortRxMyInfoAbsentPkts = _CvsVSLPortRxMyInfoAbsentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 9),
    _CvsVSLPortRxMyInfoAbsentPkts_Type()
)
cvsVSLPortRxMyInfoAbsentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxMyInfoAbsentPkts.setStatus("current")
_CvsVSLPortRxBadMacAddressPkts_Type = Counter32
_CvsVSLPortRxBadMacAddressPkts_Object = MibTableColumn
cvsVSLPortRxBadMacAddressPkts = _CvsVSLPortRxBadMacAddressPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 10),
    _CvsVSLPortRxBadMacAddressPkts_Type()
)
cvsVSLPortRxBadMacAddressPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxBadMacAddressPkts.setStatus("current")
_CvsVSLPortRxBadSwitchIdPkts_Type = Counter32
_CvsVSLPortRxBadSwitchIdPkts_Object = MibTableColumn
cvsVSLPortRxBadSwitchIdPkts = _CvsVSLPortRxBadSwitchIdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 11),
    _CvsVSLPortRxBadSwitchIdPkts_Type()
)
cvsVSLPortRxBadSwitchIdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxBadSwitchIdPkts.setStatus("current")
_CvsVSLPortRxDomainIdMismatchPkts_Type = Counter32
_CvsVSLPortRxDomainIdMismatchPkts_Object = MibTableColumn
cvsVSLPortRxDomainIdMismatchPkts = _CvsVSLPortRxDomainIdMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 12),
    _CvsVSLPortRxDomainIdMismatchPkts_Type()
)
cvsVSLPortRxDomainIdMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxDomainIdMismatchPkts.setStatus("current")
_CvsVSLPortRxPeerInfoMismatchPkts_Type = Counter32
_CvsVSLPortRxPeerInfoMismatchPkts_Object = MibTableColumn
cvsVSLPortRxPeerInfoMismatchPkts = _CvsVSLPortRxPeerInfoMismatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 3, 1, 13),
    _CvsVSLPortRxPeerInfoMismatchPkts_Type()
)
cvsVSLPortRxPeerInfoMismatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLPortRxPeerInfoMismatchPkts.setStatus("current")
_CvsVSLLinkPortTable_Object = MibTable
cvsVSLLinkPortTable = _CvsVSLLinkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cvsVSLLinkPortTable.setStatus("current")
_CvsVSLLinkPortEntry_Object = MibTableRow
cvsVSLLinkPortEntry = _CvsVSLLinkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4, 1)
)
cvsVSLLinkPortEntry.setIndexNames(
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChannelIfindex"),
    (0, "CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortStatsIfindex"),
)
if mibBuilder.loadTexts:
    cvsVSLLinkPortEntry.setStatus("current")
_CvsVSLLinkPeerInterface_Type = SnmpAdminString
_CvsVSLLinkPeerInterface_Object = MibTableColumn
cvsVSLLinkPeerInterface = _CvsVSLLinkPeerInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 3, 4, 1, 1),
    _CvsVSLLinkPeerInterface_Type()
)
cvsVSLLinkPeerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsVSLLinkPeerInterface.setStatus("current")
_CvsModuleObjects_ObjectIdentity = ObjectIdentity
cvsModuleObjects = _CvsModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4)
)
_CvsModuleTable_Object = MibTable
cvsModuleTable = _CvsModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvsModuleTable.setStatus("current")
_CvsModuleEntry_Object = MibTableRow
cvsModuleEntry = _CvsModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1)
)
cvsModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cvsModuleEntry.setStatus("current")
_CvsModuleVSSupported_Type = TruthValue
_CvsModuleVSSupported_Object = MibTableColumn
cvsModuleVSSupported = _CvsModuleVSSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 1),
    _CvsModuleVSSupported_Type()
)
cvsModuleVSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsModuleVSSupported.setStatus("current")
_CvsModuleVSLCapable_Type = TruthValue
_CvsModuleVSLCapable_Object = MibTableColumn
cvsModuleVSLCapable = _CvsModuleVSLCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 2),
    _CvsModuleVSLCapable_Type()
)
cvsModuleVSLCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsModuleVSLCapable.setStatus("current")
_CvsModuleSlotNumber_Type = Unsigned32
_CvsModuleSlotNumber_Object = MibTableColumn
cvsModuleSlotNumber = _CvsModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 3),
    _CvsModuleSlotNumber_Type()
)
cvsModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsModuleSlotNumber.setStatus("current")


class _CvsModuleRprWarm_Type(Integer32):
    """Custom type cvsModuleRprWarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cSSO", 3),
          ("notApplicable", 1),
          ("rprWarm", 2))
    )


_CvsModuleRprWarm_Type.__name__ = "Integer32"
_CvsModuleRprWarm_Object = MibTableColumn
cvsModuleRprWarm = _CvsModuleRprWarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 4, 1, 1, 4),
    _CvsModuleRprWarm_Type()
)
cvsModuleRprWarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvsModuleRprWarm.setStatus("current")
_CvsDualActiveDetection_ObjectIdentity = ObjectIdentity
cvsDualActiveDetection = _CvsDualActiveDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5)
)
_CvsDualActiveDetectionNotifEnable_Type = TruthValue
_CvsDualActiveDetectionNotifEnable_Object = MibScalar
cvsDualActiveDetectionNotifEnable = _CvsDualActiveDetectionNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5, 1),
    _CvsDualActiveDetectionNotifEnable_Type()
)
cvsDualActiveDetectionNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvsDualActiveDetectionNotifEnable.setStatus("current")
_CvsDualActiveDetectionInformation_Type = SnmpAdminString
_CvsDualActiveDetectionInformation_Object = MibScalar
cvsDualActiveDetectionInformation = _CvsDualActiveDetectionInformation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 1, 5, 2),
    _CvsDualActiveDetectionInformation_Type()
)
cvsDualActiveDetectionInformation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvsDualActiveDetectionInformation.setStatus("current")
_CiscoVirtualSwitchMIBConform_ObjectIdentity = ObjectIdentity
ciscoVirtualSwitchMIBConform = _CiscoVirtualSwitchMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2)
)
_CvsMIBCompliances_ObjectIdentity = ObjectIdentity
cvsMIBCompliances = _CvsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1)
)
_CvsMIBGroups_ObjectIdentity = ObjectIdentity
cvsMIBGroups = _CvsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2)
)

# Managed Objects groups

cvsGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 1)
)
cvsGlobalGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsDomain"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchID"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchCapability"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchMode"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchConvertingStatus"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLChangeNotifEnable"))
)
if mibBuilder.loadTexts:
    cvsGlobalGroup.setStatus("current")

cvsCoreSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 2)
)
cvsCoreSwitchGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchPriority"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchPreempt"))
)
if mibBuilder.loadTexts:
    cvsCoreSwitchGroup.setStatus("current")

cvsChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 3)
)
cvsChassisGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisSwitchID"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisRole"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsChassisUpTime"))
)
if mibBuilder.loadTexts:
    cvsChassisGroup.setStatus("current")

cvsVSLConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 4)
)
cvsVSLConnectionGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLCoreSwitchID"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectOperStatus"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLLastConnectionStateChange"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConfiguredPortCount"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLOperationalPortCount"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionRowStatus"))
)
if mibBuilder.loadTexts:
    cvsVSLConnectionGroup.setStatus("current")

cvsVSLStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 5)
)
cvsVSLStatisticsGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxErrorPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxChksumErrPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxErrorPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxChksumErrPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortTxOkPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortTxFailPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBidirPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxUnidirPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxFailPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadPkts"))
)
if mibBuilder.loadTexts:
    cvsVSLStatisticsGroup.setStatus("current")

cvsModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 6)
)
cvsModuleGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleVSSupported"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleVSLCapable"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleSlotNumber"))
)
if mibBuilder.loadTexts:
    cvsModuleGroup.setStatus("current")

cvsVSLStatisticsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 8)
)
cvsVSLStatisticsExtGroup.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxLmpPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxRrpPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxPingPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxProtoPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxDataPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxAckPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxLmpPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxRrpPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxPingPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxProtoPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxDataPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxAckPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxLmpEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxRrpEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxPingEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxProtoEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxDataEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxAckEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxLmpEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxRrpEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxPingEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxProtoEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxDataEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxAckEobcPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxTotalHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxErrorHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLTxChksumErrHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxTotalHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxErrorHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLRxChksumErrHCPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxMyInfoMismatchPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxMyInfoAbsentPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadMacAddressPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxBadSwitchIdPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxDomainIdMismatchPkts"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLPortRxPeerInfoMismatchPkts"))
)
if mibBuilder.loadTexts:
    cvsVSLStatisticsExtGroup.setStatus("current")

cvsVssModuleStandbyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 9)
)
cvsVssModuleStandbyGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsModuleRprWarm")
)
if mibBuilder.loadTexts:
    cvsVssModuleStandbyGroup.setStatus("current")

cvsCoreSwitchLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 10)
)
cvsCoreSwitchLocationGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsCoreSwitchLocation")
)
if mibBuilder.loadTexts:
    cvsCoreSwitchLocationGroup.setStatus("current")

cvsDualActiveDetectionNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 11)
)
cvsDualActiveDetectionNotifsControlGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotifEnable")
)
if mibBuilder.loadTexts:
    cvsDualActiveDetectionNotifsControlGroup.setStatus("current")

cvsDualActiveDetectionNotifsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 12)
)
cvsDualActiveDetectionNotifsInfoGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionInformation")
)
if mibBuilder.loadTexts:
    cvsDualActiveDetectionNotifsInfoGroup.setStatus("current")

cvsVSLLinkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 14)
)
cvsVSLLinkPortGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLLinkPeerInterface")
)
if mibBuilder.loadTexts:
    cvsVSLLinkPortGroup.setStatus("current")


# Notification objects

cvsVSLConnectionChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 0, 1)
)
cvsVSLConnectionChangeNotif.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectOperStatus")
)
if mibBuilder.loadTexts:
    cvsVSLConnectionChangeNotif.setStatus(
        "current"
    )

cvsDualActiveDetectionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 0, 2)
)
cvsDualActiveDetectionNotif.setObjects(
      *(("CISCO-VIRTUAL-SWITCH-MIB", "cvsSwitchID"),
        ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionInformation"))
)
if mibBuilder.loadTexts:
    cvsDualActiveDetectionNotif.setStatus(
        "current"
    )


# Notifications groups

cvsConnectionNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 7)
)
cvsConnectionNotifsGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsVSLConnectionChangeNotif")
)
if mibBuilder.loadTexts:
    cvsConnectionNotifsGroup.setStatus(
        "current"
    )

cvsDualActiveDetectionNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 2, 13)
)
cvsDualActiveDetectionNotifsGroup.setObjects(
    ("CISCO-VIRTUAL-SWITCH-MIB", "cvsDualActiveDetectionNotif")
)
if mibBuilder.loadTexts:
    cvsDualActiveDetectionNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvsMIBCompliance.setStatus(
        "deprecated"
    )

cvsMIBComplianceV02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvsMIBComplianceV02.setStatus(
        "deprecated"
    )

cvsMIBComplianceV03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cvsMIBComplianceV03.setStatus(
        "deprecated"
    )

cvsMIBComplianceV04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 388, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cvsMIBComplianceV04.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIRTUAL-SWITCH-MIB",
    **{"VSSwitchID": VSSwitchID,
       "VSSwitchCapability": VSSwitchCapability,
       "VSSwitchMode": VSSwitchMode,
       "VSSwitchRole": VSSwitchRole,
       "VSConnectStatus": VSConnectStatus,
       "ciscoVirtualSwitchMIB": ciscoVirtualSwitchMIB,
       "ciscoVirtualSwitchMIBNotifs": ciscoVirtualSwitchMIBNotifs,
       "cvsVSLConnectionChangeNotif": cvsVSLConnectionChangeNotif,
       "cvsDualActiveDetectionNotif": cvsDualActiveDetectionNotif,
       "ciscoVirtualSwitchMIBObjects": ciscoVirtualSwitchMIBObjects,
       "cvsGlobalObjects": cvsGlobalObjects,
       "cvsDomain": cvsDomain,
       "cvsSwitchID": cvsSwitchID,
       "cvsSwitchCapability": cvsSwitchCapability,
       "cvsSwitchMode": cvsSwitchMode,
       "cvsSwitchConvertingStatus": cvsSwitchConvertingStatus,
       "cvsVSLChangeNotifEnable": cvsVSLChangeNotifEnable,
       "cvsChassisObjects": cvsChassisObjects,
       "cvsCoreSwitchConfigTable": cvsCoreSwitchConfigTable,
       "cvsCoreSwitchConfigEntry": cvsCoreSwitchConfigEntry,
       "cvsCoreSwitchID": cvsCoreSwitchID,
       "cvsCoreSwitchPriority": cvsCoreSwitchPriority,
       "cvsCoreSwitchPreempt": cvsCoreSwitchPreempt,
       "cvsCoreSwitchLocation": cvsCoreSwitchLocation,
       "cvsChassisTable": cvsChassisTable,
       "cvsChassisEntry": cvsChassisEntry,
       "cvsChassisSwitchID": cvsChassisSwitchID,
       "cvsChassisRole": cvsChassisRole,
       "cvsChassisUpTime": cvsChassisUpTime,
       "cvsVSLObjects": cvsVSLObjects,
       "cvsVSLConnectionTable": cvsVSLConnectionTable,
       "cvsVSLConnectionEntry": cvsVSLConnectionEntry,
       "cvsVSLChannelIfindex": cvsVSLChannelIfindex,
       "cvsVSLCoreSwitchID": cvsVSLCoreSwitchID,
       "cvsVSLConnectOperStatus": cvsVSLConnectOperStatus,
       "cvsVSLLastConnectionStateChange": cvsVSLLastConnectionStateChange,
       "cvsVSLConfiguredPortCount": cvsVSLConfiguredPortCount,
       "cvsVSLOperationalPortCount": cvsVSLOperationalPortCount,
       "cvsVSLConnectionRowStatus": cvsVSLConnectionRowStatus,
       "cvsVSLStatsTable": cvsVSLStatsTable,
       "cvsVSLStatsEntry": cvsVSLStatsEntry,
       "cvsVSLTxTotalPkts": cvsVSLTxTotalPkts,
       "cvsVSLTxErrorPkts": cvsVSLTxErrorPkts,
       "cvsVSLTxChksumErrPkts": cvsVSLTxChksumErrPkts,
       "cvsVSLRxTotalPkts": cvsVSLRxTotalPkts,
       "cvsVSLRxErrorPkts": cvsVSLRxErrorPkts,
       "cvsVSLRxChksumErrPkts": cvsVSLRxChksumErrPkts,
       "cvsVSLTxLmpPkts": cvsVSLTxLmpPkts,
       "cvsVSLTxRrpPkts": cvsVSLTxRrpPkts,
       "cvsVSLTxPingPkts": cvsVSLTxPingPkts,
       "cvsVSLTxProtoPkts": cvsVSLTxProtoPkts,
       "cvsVSLTxDataPkts": cvsVSLTxDataPkts,
       "cvsVSLTxAckPkts": cvsVSLTxAckPkts,
       "cvsVSLRxLmpPkts": cvsVSLRxLmpPkts,
       "cvsVSLRxRrpPkts": cvsVSLRxRrpPkts,
       "cvsVSLRxPingPkts": cvsVSLRxPingPkts,
       "cvsVSLRxProtoPkts": cvsVSLRxProtoPkts,
       "cvsVSLRxDataPkts": cvsVSLRxDataPkts,
       "cvsVSLRxAckPkts": cvsVSLRxAckPkts,
       "cvsVSLTxTotalEobcPkts": cvsVSLTxTotalEobcPkts,
       "cvsVSLTxLmpEobcPkts": cvsVSLTxLmpEobcPkts,
       "cvsVSLTxRrpEobcPkts": cvsVSLTxRrpEobcPkts,
       "cvsVSLTxPingEobcPkts": cvsVSLTxPingEobcPkts,
       "cvsVSLTxProtoEobcPkts": cvsVSLTxProtoEobcPkts,
       "cvsVSLTxDataEobcPkts": cvsVSLTxDataEobcPkts,
       "cvsVSLTxAckEobcPkts": cvsVSLTxAckEobcPkts,
       "cvsVSLRxTotalEobcPkts": cvsVSLRxTotalEobcPkts,
       "cvsVSLRxLmpEobcPkts": cvsVSLRxLmpEobcPkts,
       "cvsVSLRxRrpEobcPkts": cvsVSLRxRrpEobcPkts,
       "cvsVSLRxPingEobcPkts": cvsVSLRxPingEobcPkts,
       "cvsVSLRxProtoEobcPkts": cvsVSLRxProtoEobcPkts,
       "cvsVSLRxDataEobcPkts": cvsVSLRxDataEobcPkts,
       "cvsVSLRxAckEobcPkts": cvsVSLRxAckEobcPkts,
       "cvsVSLTxTotalHCPkts": cvsVSLTxTotalHCPkts,
       "cvsVSLTxErrorHCPkts": cvsVSLTxErrorHCPkts,
       "cvsVSLTxChksumErrHCPkts": cvsVSLTxChksumErrHCPkts,
       "cvsVSLRxTotalHCPkts": cvsVSLRxTotalHCPkts,
       "cvsVSLRxErrorHCPkts": cvsVSLRxErrorHCPkts,
       "cvsVSLRxChksumErrHCPkts": cvsVSLRxChksumErrHCPkts,
       "cvsVSLPortStatsTable": cvsVSLPortStatsTable,
       "cvsVSLPortStatsEntry": cvsVSLPortStatsEntry,
       "cvsVSLPortStatsIfindex": cvsVSLPortStatsIfindex,
       "cvsVSLPortTxOkPkts": cvsVSLPortTxOkPkts,
       "cvsVSLPortTxFailPkts": cvsVSLPortTxFailPkts,
       "cvsVSLPortRxBidirPkts": cvsVSLPortRxBidirPkts,
       "cvsVSLPortRxUnidirPkts": cvsVSLPortRxUnidirPkts,
       "cvsVSLPortRxFailPkts": cvsVSLPortRxFailPkts,
       "cvsVSLPortRxBadPkts": cvsVSLPortRxBadPkts,
       "cvsVSLPortRxMyInfoMismatchPkts": cvsVSLPortRxMyInfoMismatchPkts,
       "cvsVSLPortRxMyInfoAbsentPkts": cvsVSLPortRxMyInfoAbsentPkts,
       "cvsVSLPortRxBadMacAddressPkts": cvsVSLPortRxBadMacAddressPkts,
       "cvsVSLPortRxBadSwitchIdPkts": cvsVSLPortRxBadSwitchIdPkts,
       "cvsVSLPortRxDomainIdMismatchPkts": cvsVSLPortRxDomainIdMismatchPkts,
       "cvsVSLPortRxPeerInfoMismatchPkts": cvsVSLPortRxPeerInfoMismatchPkts,
       "cvsVSLLinkPortTable": cvsVSLLinkPortTable,
       "cvsVSLLinkPortEntry": cvsVSLLinkPortEntry,
       "cvsVSLLinkPeerInterface": cvsVSLLinkPeerInterface,
       "cvsModuleObjects": cvsModuleObjects,
       "cvsModuleTable": cvsModuleTable,
       "cvsModuleEntry": cvsModuleEntry,
       "cvsModuleVSSupported": cvsModuleVSSupported,
       "cvsModuleVSLCapable": cvsModuleVSLCapable,
       "cvsModuleSlotNumber": cvsModuleSlotNumber,
       "cvsModuleRprWarm": cvsModuleRprWarm,
       "cvsDualActiveDetection": cvsDualActiveDetection,
       "cvsDualActiveDetectionNotifEnable": cvsDualActiveDetectionNotifEnable,
       "cvsDualActiveDetectionInformation": cvsDualActiveDetectionInformation,
       "ciscoVirtualSwitchMIBConform": ciscoVirtualSwitchMIBConform,
       "cvsMIBCompliances": cvsMIBCompliances,
       "cvsMIBCompliance": cvsMIBCompliance,
       "cvsMIBComplianceV02": cvsMIBComplianceV02,
       "cvsMIBComplianceV03": cvsMIBComplianceV03,
       "cvsMIBComplianceV04": cvsMIBComplianceV04,
       "cvsMIBGroups": cvsMIBGroups,
       "cvsGlobalGroup": cvsGlobalGroup,
       "cvsCoreSwitchGroup": cvsCoreSwitchGroup,
       "cvsChassisGroup": cvsChassisGroup,
       "cvsVSLConnectionGroup": cvsVSLConnectionGroup,
       "cvsVSLStatisticsGroup": cvsVSLStatisticsGroup,
       "cvsModuleGroup": cvsModuleGroup,
       "cvsConnectionNotifsGroup": cvsConnectionNotifsGroup,
       "cvsVSLStatisticsExtGroup": cvsVSLStatisticsExtGroup,
       "cvsVssModuleStandbyGroup": cvsVssModuleStandbyGroup,
       "cvsCoreSwitchLocationGroup": cvsCoreSwitchLocationGroup,
       "cvsDualActiveDetectionNotifsControlGroup": cvsDualActiveDetectionNotifsControlGroup,
       "cvsDualActiveDetectionNotifsInfoGroup": cvsDualActiveDetectionNotifsInfoGroup,
       "cvsDualActiveDetectionNotifsGroup": cvsDualActiveDetectionNotifsGroup,
       "cvsVSLLinkPortGroup": cvsVSLLinkPortGroup}
)
