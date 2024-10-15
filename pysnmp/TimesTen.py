# SNMP MIB module (TimesTen) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TimesTen
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:10 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Timesten_ObjectIdentity = ObjectIdentity
timesten = _Timesten_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549)
)
_TtSystem_ObjectIdentity = ObjectIdentity
ttSystem = _TtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 1)
)
_TtTimeStamp_Type = OctetString
_TtTimeStamp_Object = MibScalar
ttTimeStamp = _TtTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 1),
    _TtTimeStamp_Type()
)
ttTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTimeStamp.setStatus("mandatory")
_TtVersion_Type = OctetString
_TtVersion_Object = MibScalar
ttVersion = _TtVersion_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 2),
    _TtVersion_Type()
)
ttVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttVersion.setStatus("mandatory")
_TtPid_Type = Integer32
_TtPid_Object = MibScalar
ttPid = _TtPid_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 3),
    _TtPid_Type()
)
ttPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttPid.setStatus("mandatory")
_TtProcessName_Type = OctetString
_TtProcessName_Object = MibScalar
ttProcessName = _TtProcessName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 4),
    _TtProcessName_Type()
)
ttProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttProcessName.setStatus("obsolete")
_TtUid_Type = OctetString
_TtUid_Object = MibScalar
ttUid = _TtUid_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 5),
    _TtUid_Type()
)
ttUid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttUid.setStatus("mandatory")
_TtUserName_Type = OctetString
_TtUserName_Object = MibScalar
ttUserName = _TtUserName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 1, 6),
    _TtUserName_Type()
)
ttUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttUserName.setStatus("obsolete")
_TtMsg_ObjectIdentity = ObjectIdentity
ttMsg = _TtMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 2)
)
_TtMesg_Type = OctetString
_TtMesg_Object = MibScalar
ttMesg = _TtMesg_Object(
    (1, 3, 6, 1, 4, 1, 5549, 2, 1),
    _TtMesg_Type()
)
ttMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttMesg.setStatus("mandatory")
_TtTraps_ObjectIdentity = ObjectIdentity
ttTraps = _TtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5)
)
_TtAssertTraps_ObjectIdentity = ObjectIdentity
ttAssertTraps = _TtAssertTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 1)
)
_TtDSTraps_ObjectIdentity = ObjectIdentity
ttDSTraps = _TtDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 10)
)
_TtFileTraps_ObjectIdentity = ObjectIdentity
ttFileTraps = _TtFileTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 20)
)
_TtDaemonTraps_ObjectIdentity = ObjectIdentity
ttDaemonTraps = _TtDaemonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 40)
)
_TtRepTraps_ObjectIdentity = ObjectIdentity
ttRepTraps = _TtRepTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50)
)
_TtOraTraps_ObjectIdentity = ObjectIdentity
ttOraTraps = _TtOraTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60)
)
_TtRecoveryTraps_ObjectIdentity = ObjectIdentity
ttRecoveryTraps = _TtRecoveryTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 5, 70)
)
_TtTrapTruncated_Type = Integer32
_TtTrapTruncated_Object = MibScalar
ttTrapTruncated = _TtTrapTruncated_Object(
    (1, 3, 6, 1, 4, 1, 5549, 5, 100),
    _TtTrapTruncated_Type()
)
ttTrapTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttTrapTruncated.setStatus("mandatory")
_TtDataStore_ObjectIdentity = ObjectIdentity
ttDataStore = _TtDataStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 10)
)
_TtDSName_Type = OctetString
_TtDSName_Object = MibScalar
ttDSName = _TtDSName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 2),
    _TtDSName_Type()
)
ttDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSName.setStatus("mandatory")
_TtDSPath_Type = OctetString
_TtDSPath_Object = MibScalar
ttDSPath = _TtDSPath_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 3),
    _TtDSPath_Type()
)
ttDSPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSPath.setStatus("mandatory")
_TtDSShmKey_Type = OctetString
_TtDSShmKey_Object = MibScalar
ttDSShmKey = _TtDSShmKey_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 4),
    _TtDSShmKey_Type()
)
ttDSShmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSShmKey.setStatus("mandatory")
_TtDSNConn_Type = Integer32
_TtDSNConn_Object = MibScalar
ttDSNConn = _TtDSNConn_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 7),
    _TtDSNConn_Type()
)
ttDSNConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSNConn.setStatus("mandatory")
_TtDSMaxSize_Type = Integer32
_TtDSMaxSize_Object = MibScalar
ttDSMaxSize = _TtDSMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 8),
    _TtDSMaxSize_Type()
)
ttDSMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSMaxSize.setStatus("mandatory")
_TtDSCurSize_Type = Integer32
_TtDSCurSize_Object = MibScalar
ttDSCurSize = _TtDSCurSize_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 9),
    _TtDSCurSize_Type()
)
ttDSCurSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSCurSize.setStatus("mandatory")
_TtDSReqSize_Type = Integer32
_TtDSReqSize_Object = MibScalar
ttDSReqSize = _TtDSReqSize_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 10),
    _TtDSReqSize_Type()
)
ttDSReqSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSReqSize.setStatus("mandatory")
_TtDSPartition_Type = OctetString
_TtDSPartition_Object = MibScalar
ttDSPartition = _TtDSPartition_Object(
    (1, 3, 6, 1, 4, 1, 5549, 10, 11),
    _TtDSPartition_Type()
)
ttDSPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDSPartition.setStatus("mandatory")
_TtFile_ObjectIdentity = ObjectIdentity
ttFile = _TtFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 20)
)
_TtFilePath_Type = OctetString
_TtFilePath_Object = MibScalar
ttFilePath = _TtFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5549, 20, 3),
    _TtFilePath_Type()
)
ttFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttFilePath.setStatus("mandatory")
_TtReadSize_Type = OctetString
_TtReadSize_Object = MibScalar
ttReadSize = _TtReadSize_Object(
    (1, 3, 6, 1, 4, 1, 5549, 20, 6),
    _TtReadSize_Type()
)
ttReadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ttReadSize.setStatus("mandatory")
_TtReadReq_Type = OctetString
_TtReadReq_Object = MibScalar
ttReadReq = _TtReadReq_Object(
    (1, 3, 6, 1, 4, 1, 5549, 20, 7),
    _TtReadReq_Type()
)
ttReadReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttReadReq.setStatus("mandatory")
_TtWriteSize_Type = OctetString
_TtWriteSize_Object = MibScalar
ttWriteSize = _TtWriteSize_Object(
    (1, 3, 6, 1, 4, 1, 5549, 20, 8),
    _TtWriteSize_Type()
)
ttWriteSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttWriteSize.setStatus("mandatory")
_TtWriteReq_Type = OctetString
_TtWriteReq_Object = MibScalar
ttWriteReq = _TtWriteReq_Object(
    (1, 3, 6, 1, 4, 1, 5549, 20, 9),
    _TtWriteReq_Type()
)
ttWriteReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttWriteReq.setStatus("mandatory")
_TtDaemon_ObjectIdentity = ObjectIdentity
ttDaemon = _TtDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 40)
)
_TtDaeName_Type = OctetString
_TtDaeName_Object = MibScalar
ttDaeName = _TtDaeName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 40, 2),
    _TtDaeName_Type()
)
ttDaeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDaeName.setStatus("mandatory")
_TtDaePid_Type = Integer32
_TtDaePid_Object = MibScalar
ttDaePid = _TtDaePid_Object(
    (1, 3, 6, 1, 4, 1, 5549, 40, 4),
    _TtDaePid_Type()
)
ttDaePid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDaePid.setStatus("mandatory")
_TtDaeInst_Type = Integer32
_TtDaeInst_Object = MibScalar
ttDaeInst = _TtDaeInst_Object(
    (1, 3, 6, 1, 4, 1, 5549, 40, 6),
    _TtDaeInst_Type()
)
ttDaeInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttDaeInst.setStatus("mandatory")
_TtReplication_ObjectIdentity = ObjectIdentity
ttReplication = _TtReplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 50)
)
_TtRepPid_Type = Integer32
_TtRepPid_Object = MibScalar
ttRepPid = _TtRepPid_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 1),
    _TtRepPid_Type()
)
ttRepPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepPid.setStatus("mandatory")
_TtRepName_Type = OctetString
_TtRepName_Object = MibScalar
ttRepName = _TtRepName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 2),
    _TtRepName_Type()
)
ttRepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepName.setStatus("mandatory")
_TtRepPeerStoreID_Type = OctetString
_TtRepPeerStoreID_Object = MibScalar
ttRepPeerStoreID = _TtRepPeerStoreID_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 3),
    _TtRepPeerStoreID_Type()
)
ttRepPeerStoreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepPeerStoreID.setStatus("mandatory")
_TtRepPeerName_Type = OctetString
_TtRepPeerName_Object = MibScalar
ttRepPeerName = _TtRepPeerName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 4),
    _TtRepPeerName_Type()
)
ttRepPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepPeerName.setStatus("mandatory")
_TtRepMasterHost_Type = OctetString
_TtRepMasterHost_Object = MibScalar
ttRepMasterHost = _TtRepMasterHost_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 5),
    _TtRepMasterHost_Type()
)
ttRepMasterHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepMasterHost.setStatus("mandatory")
_TtRepMasterPort_Type = Integer32
_TtRepMasterPort_Object = MibScalar
ttRepMasterPort = _TtRepMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 6),
    _TtRepMasterPort_Type()
)
ttRepMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepMasterPort.setStatus("mandatory")
_TtRepSubscriberHost_Type = OctetString
_TtRepSubscriberHost_Object = MibScalar
ttRepSubscriberHost = _TtRepSubscriberHost_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 7),
    _TtRepSubscriberHost_Type()
)
ttRepSubscriberHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepSubscriberHost.setStatus("mandatory")
_TtRepSubscriberPort_Type = Integer32
_TtRepSubscriberPort_Object = MibScalar
ttRepSubscriberPort = _TtRepSubscriberPort_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 8),
    _TtRepSubscriberPort_Type()
)
ttRepSubscriberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepSubscriberPort.setStatus("mandatory")
_TtRepTable_Type = OctetString
_TtRepTable_Object = MibScalar
ttRepTable = _TtRepTable_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 9),
    _TtRepTable_Type()
)
ttRepTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepTable.setStatus("mandatory")
_TtRepAction_Type = OctetString
_TtRepAction_Object = MibScalar
ttRepAction = _TtRepAction_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 10),
    _TtRepAction_Type()
)
ttRepAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepAction.setStatus("mandatory")
_TtRepReason_Type = OctetString
_TtRepReason_Object = MibScalar
ttRepReason = _TtRepReason_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 11),
    _TtRepReason_Type()
)
ttRepReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepReason.setStatus("mandatory")
_TtRepConflictKey_Type = OctetString
_TtRepConflictKey_Object = MibScalar
ttRepConflictKey = _TtRepConflictKey_Object(
    (1, 3, 6, 1, 4, 1, 5549, 50, 12),
    _TtRepConflictKey_Type()
)
ttRepConflictKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttRepConflictKey.setStatus("mandatory")
_TtOraCache_ObjectIdentity = ObjectIdentity
ttOraCache = _TtOraCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 60)
)
_TtOraAgentName_Type = OctetString
_TtOraAgentName_Object = MibScalar
ttOraAgentName = _TtOraAgentName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 60, 2),
    _TtOraAgentName_Type()
)
ttOraAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttOraAgentName.setStatus("mandatory")
_TtOraAgentPid_Type = Integer32
_TtOraAgentPid_Object = MibScalar
ttOraAgentPid = _TtOraAgentPid_Object(
    (1, 3, 6, 1, 4, 1, 5549, 60, 3),
    _TtOraAgentPid_Type()
)
ttOraAgentPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttOraAgentPid.setStatus("mandatory")
_TtOraDSName_Type = OctetString
_TtOraDSName_Object = MibScalar
ttOraDSName = _TtOraDSName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 60, 4),
    _TtOraDSName_Type()
)
ttOraDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttOraDSName.setStatus("mandatory")
_TtOraCacheGroupName_Type = OctetString
_TtOraCacheGroupName_Object = MibScalar
ttOraCacheGroupName = _TtOraCacheGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5549, 60, 5),
    _TtOraCacheGroupName_Type()
)
ttOraCacheGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttOraCacheGroupName.setStatus("mandatory")
_TtRecovery_ObjectIdentity = ObjectIdentity
ttRecovery = _TtRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5549, 70)
)
_EndLFN_Type = OctetString
_EndLFN_Object = MibScalar
endLFN = _EndLFN_Object(
    (1, 3, 6, 1, 4, 1, 5549, 70, 1),
    _EndLFN_Type()
)
endLFN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endLFN.setStatus("mandatory")
_EndLFO_Type = OctetString
_EndLFO_Object = MibScalar
endLFO = _EndLFO_Object(
    (1, 3, 6, 1, 4, 1, 5549, 70, 2),
    _EndLFO_Type()
)
endLFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endLFO.setStatus("mandatory")
_MaxLFN_Type = OctetString
_MaxLFN_Object = MibScalar
maxLFN = _MaxLFN_Object(
    (1, 3, 6, 1, 4, 1, 5549, 70, 3),
    _MaxLFN_Type()
)
maxLFN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLFN.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ttAssertFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 1, 0, 1)
)
ttAssertFailTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"))
)
if mibBuilder.loadTexts:
    ttAssertFailTrap.setStatus(
        ""
    )

ttDSGoingInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 10, 0, 5)
)
ttDSGoingInvalidTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttDSShmKey"),
        ("TimesTen", "ttDSNConn"))
)
if mibBuilder.loadTexts:
    ttDSGoingInvalidTrap.setStatus(
        ""
    )

ttPartitionSpaceStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 10, 0, 11)
)
ttPartitionSpaceStateTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttDSMaxSize"),
        ("TimesTen", "ttDSCurSize"),
        ("TimesTen", "ttDSReqSize"),
        ("TimesTen", "ttDSPartition"))
)
if mibBuilder.loadTexts:
    ttPartitionSpaceStateTrap.setStatus(
        ""
    )

ttPartitionSpaceExhaustedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 10, 0, 12)
)
ttPartitionSpaceExhaustedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttDSMaxSize"),
        ("TimesTen", "ttDSCurSize"),
        ("TimesTen", "ttDSReqSize"),
        ("TimesTen", "ttDSPartition"))
)
if mibBuilder.loadTexts:
    ttPartitionSpaceExhaustedTrap.setStatus(
        ""
    )

ttDSDataCorruptionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 10, 0, 21)
)
ttDSDataCorruptionTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"))
)
if mibBuilder.loadTexts:
    ttDSDataCorruptionTrap.setStatus(
        ""
    )

ttFileWriteErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 20, 0, 20)
)
ttFileWriteErrorTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttFilePath"),
        ("TimesTen", "ttWriteSize"),
        ("TimesTen", "ttWriteReq"))
)
if mibBuilder.loadTexts:
    ttFileWriteErrorTrap.setStatus(
        ""
    )

ttMainDaemonReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 40, 0, 2)
)
ttMainDaemonReadyTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDaeName"),
        ("TimesTen", "ttDaeInst"),
        ("TimesTen", "ttDaePid"))
)
if mibBuilder.loadTexts:
    ttMainDaemonReadyTrap.setStatus(
        ""
    )

ttMainDaemonExitingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 40, 0, 3)
)
ttMainDaemonExitingTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDaeName"),
        ("TimesTen", "ttDaeInst"),
        ("TimesTen", "ttDaePid"))
)
if mibBuilder.loadTexts:
    ttMainDaemonExitingTrap.setStatus(
        ""
    )

ttMainDaemonDiedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 40, 0, 4)
)
ttMainDaemonDiedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDaeName"),
        ("TimesTen", "ttDaeInst"),
        ("TimesTen", "ttDaePid"))
)
if mibBuilder.loadTexts:
    ttMainDaemonDiedTrap.setStatus(
        ""
    )

ttDaemonOutOfMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 40, 0, 13)
)
ttDaemonOutOfMemoryTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDaeName"),
        ("TimesTen", "ttDaeInst"))
)
if mibBuilder.loadTexts:
    ttDaemonOutOfMemoryTrap.setStatus(
        ""
    )

ttRepAgentStartingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 6)
)
ttRepAgentStartingTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"))
)
if mibBuilder.loadTexts:
    ttRepAgentStartingTrap.setStatus(
        ""
    )

ttRepAgentExitingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 7)
)
ttRepAgentExitingTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"))
)
if mibBuilder.loadTexts:
    ttRepAgentExitingTrap.setStatus(
        ""
    )

ttRepAgentDiedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 8)
)
ttRepAgentDiedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttRepPid"))
)
if mibBuilder.loadTexts:
    ttRepAgentDiedTrap.setStatus(
        ""
    )

ttRepUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 9)
)
ttRepUpdateFailedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttRepPeerStoreID"),
        ("TimesTen", "ttRepName"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttRepReason"),
        ("TimesTen", "ttRepTable"),
        ("TimesTen", "ttRepAction"),
        ("TimesTen", "ttRepPeerName"),
        ("TimesTen", "ttRepConflictKey"))
)
if mibBuilder.loadTexts:
    ttRepUpdateFailedTrap.setStatus(
        ""
    )

ttRepSubscriberFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 10)
)
ttRepSubscriberFailedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttRepPeerStoreID"),
        ("TimesTen", "ttRepName"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttRepReason"),
        ("TimesTen", "ttRepSubscriberHost"),
        ("TimesTen", "ttRepSubscriberPort"))
)
if mibBuilder.loadTexts:
    ttRepSubscriberFailedTrap.setStatus(
        ""
    )

ttRepReturnReceiptTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 19)
)
ttRepReturnReceiptTransitionTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttRepPeerStoreID"),
        ("TimesTen", "ttRepName"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "ttRepReason"),
        ("TimesTen", "ttRepSubscriberHost"))
)
if mibBuilder.loadTexts:
    ttRepReturnReceiptTransitionTrap.setStatus(
        ""
    )

ttRepCatchupStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 23)
)
ttRepCatchupStartTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"))
)
if mibBuilder.loadTexts:
    ttRepCatchupStartTrap.setStatus(
        ""
    )

ttRepCatchupStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 50, 0, 24)
)
ttRepCatchupStopTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"))
)
if mibBuilder.loadTexts:
    ttRepCatchupStopTrap.setStatus(
        ""
    )

ttOraAutoRefQueFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 14)
)
ttOraAutoRefQueFullTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraAgentName"))
)
if mibBuilder.loadTexts:
    ttOraAutoRefQueFullTrap.setStatus(
        ""
    )

ttOraIncAutoRefFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 15)
)
ttOraIncAutoRefFailedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraAgentName"),
        ("TimesTen", "ttOraDSName"))
)
if mibBuilder.loadTexts:
    ttOraIncAutoRefFailedTrap.setStatus(
        ""
    )

ttOraAgentDiedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 17)
)
ttOraAgentDiedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraDSName"))
)
if mibBuilder.loadTexts:
    ttOraAgentDiedTrap.setStatus(
        ""
    )

ttOraValidationErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 25)
)
ttOraValidationErrorTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraAgentName"),
        ("TimesTen", "ttOraDSName"))
)
if mibBuilder.loadTexts:
    ttOraValidationErrorTrap.setStatus(
        ""
    )

ttOraValidationWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 26)
)
ttOraValidationWarningTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraAgentName"),
        ("TimesTen", "ttOraDSName"))
)
if mibBuilder.loadTexts:
    ttOraValidationWarningTrap.setStatus(
        ""
    )

ttOraValidationAbortedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 60, 0, 27)
)
ttOraValidationAbortedTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttOraAgentPid"),
        ("TimesTen", "ttOraAgentName"),
        ("TimesTen", "ttOraDSName"))
)
if mibBuilder.loadTexts:
    ttOraValidationAbortedTrap.setStatus(
        ""
    )

ttUnexpectedEndOfLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5549, 5, 70, 0, 22)
)
ttUnexpectedEndOfLogTrap.setObjects(
      *(("TimesTen", "ttTimeStamp"),
        ("TimesTen", "ttPid"),
        ("TimesTen", "ttUid"),
        ("TimesTen", "ttVersion"),
        ("TimesTen", "ttMesg"),
        ("TimesTen", "ttDSName"),
        ("TimesTen", "endLFN"),
        ("TimesTen", "endLFO"),
        ("TimesTen", "maxLFN"))
)
if mibBuilder.loadTexts:
    ttUnexpectedEndOfLogTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TimesTen",
    **{"timesten": timesten,
       "ttSystem": ttSystem,
       "ttTimeStamp": ttTimeStamp,
       "ttVersion": ttVersion,
       "ttPid": ttPid,
       "ttProcessName": ttProcessName,
       "ttUid": ttUid,
       "ttUserName": ttUserName,
       "ttMsg": ttMsg,
       "ttMesg": ttMesg,
       "ttTraps": ttTraps,
       "ttAssertTraps": ttAssertTraps,
       "ttAssertFailTrap": ttAssertFailTrap,
       "ttDSTraps": ttDSTraps,
       "ttDSGoingInvalidTrap": ttDSGoingInvalidTrap,
       "ttPartitionSpaceStateTrap": ttPartitionSpaceStateTrap,
       "ttPartitionSpaceExhaustedTrap": ttPartitionSpaceExhaustedTrap,
       "ttDSDataCorruptionTrap": ttDSDataCorruptionTrap,
       "ttFileTraps": ttFileTraps,
       "ttFileWriteErrorTrap": ttFileWriteErrorTrap,
       "ttDaemonTraps": ttDaemonTraps,
       "ttMainDaemonReadyTrap": ttMainDaemonReadyTrap,
       "ttMainDaemonExitingTrap": ttMainDaemonExitingTrap,
       "ttMainDaemonDiedTrap": ttMainDaemonDiedTrap,
       "ttDaemonOutOfMemoryTrap": ttDaemonOutOfMemoryTrap,
       "ttRepTraps": ttRepTraps,
       "ttRepAgentStartingTrap": ttRepAgentStartingTrap,
       "ttRepAgentExitingTrap": ttRepAgentExitingTrap,
       "ttRepAgentDiedTrap": ttRepAgentDiedTrap,
       "ttRepUpdateFailedTrap": ttRepUpdateFailedTrap,
       "ttRepSubscriberFailedTrap": ttRepSubscriberFailedTrap,
       "ttRepReturnReceiptTransitionTrap": ttRepReturnReceiptTransitionTrap,
       "ttRepCatchupStartTrap": ttRepCatchupStartTrap,
       "ttRepCatchupStopTrap": ttRepCatchupStopTrap,
       "ttOraTraps": ttOraTraps,
       "ttOraAutoRefQueFullTrap": ttOraAutoRefQueFullTrap,
       "ttOraIncAutoRefFailedTrap": ttOraIncAutoRefFailedTrap,
       "ttOraAgentDiedTrap": ttOraAgentDiedTrap,
       "ttOraValidationErrorTrap": ttOraValidationErrorTrap,
       "ttOraValidationWarningTrap": ttOraValidationWarningTrap,
       "ttOraValidationAbortedTrap": ttOraValidationAbortedTrap,
       "ttRecoveryTraps": ttRecoveryTraps,
       "ttUnexpectedEndOfLogTrap": ttUnexpectedEndOfLogTrap,
       "ttTrapTruncated": ttTrapTruncated,
       "ttDataStore": ttDataStore,
       "ttDSName": ttDSName,
       "ttDSPath": ttDSPath,
       "ttDSShmKey": ttDSShmKey,
       "ttDSNConn": ttDSNConn,
       "ttDSMaxSize": ttDSMaxSize,
       "ttDSCurSize": ttDSCurSize,
       "ttDSReqSize": ttDSReqSize,
       "ttDSPartition": ttDSPartition,
       "ttFile": ttFile,
       "ttFilePath": ttFilePath,
       "ttReadSize": ttReadSize,
       "ttReadReq": ttReadReq,
       "ttWriteSize": ttWriteSize,
       "ttWriteReq": ttWriteReq,
       "ttDaemon": ttDaemon,
       "ttDaeName": ttDaeName,
       "ttDaePid": ttDaePid,
       "ttDaeInst": ttDaeInst,
       "ttReplication": ttReplication,
       "ttRepPid": ttRepPid,
       "ttRepName": ttRepName,
       "ttRepPeerStoreID": ttRepPeerStoreID,
       "ttRepPeerName": ttRepPeerName,
       "ttRepMasterHost": ttRepMasterHost,
       "ttRepMasterPort": ttRepMasterPort,
       "ttRepSubscriberHost": ttRepSubscriberHost,
       "ttRepSubscriberPort": ttRepSubscriberPort,
       "ttRepTable": ttRepTable,
       "ttRepAction": ttRepAction,
       "ttRepReason": ttRepReason,
       "ttRepConflictKey": ttRepConflictKey,
       "ttOraCache": ttOraCache,
       "ttOraAgentName": ttOraAgentName,
       "ttOraAgentPid": ttOraAgentPid,
       "ttOraDSName": ttOraDSName,
       "ttOraCacheGroupName": ttOraCacheGroupName,
       "ttRecovery": ttRecovery,
       "endLFN": endLFN,
       "endLFO": endLFO,
       "maxLFN": maxLFN}
)
