# SNMP MIB module (Subagent-Supervision-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Subagent-Supervision-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:23 2024
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniSupervisor_ObjectIdentity = ObjectIdentity
sniSupervisor = _SniSupervisor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34)
)
_SuperVisObjects_ObjectIdentity = ObjectIdentity
superVisObjects = _SuperVisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1)
)
_SuperVisGlobalDatas_ObjectIdentity = ObjectIdentity
superVisGlobalDatas = _SuperVisGlobalDatas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1)
)
_SuperVisVersion_Type = DisplayString
_SuperVisVersion_Object = MibScalar
superVisVersion = _SuperVisVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1, 1),
    _SuperVisVersion_Type()
)
superVisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisVersion.setStatus("mandatory")
_SuperVisActiveNumber_Type = Integer32
_SuperVisActiveNumber_Object = MibScalar
superVisActiveNumber = _SuperVisActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1, 2),
    _SuperVisActiveNumber_Type()
)
superVisActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisActiveNumber.setStatus("mandatory")
_SuperVisMaxSubagentNumber_Type = Integer32
_SuperVisMaxSubagentNumber_Object = MibScalar
superVisMaxSubagentNumber = _SuperVisMaxSubagentNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1, 3),
    _SuperVisMaxSubagentNumber_Type()
)
superVisMaxSubagentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisMaxSubagentNumber.setStatus("mandatory")
_SuperVisObjectNumber_Type = Integer32
_SuperVisObjectNumber_Object = MibScalar
superVisObjectNumber = _SuperVisObjectNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1, 4),
    _SuperVisObjectNumber_Type()
)
superVisObjectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisObjectNumber.setStatus("mandatory")
_SuperVisTrapAckId_Type = Integer32
_SuperVisTrapAckId_Object = MibScalar
superVisTrapAckId = _SuperVisTrapAckId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 1, 5),
    _SuperVisTrapAckId_Type()
)
superVisTrapAckId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superVisTrapAckId.setStatus("mandatory")
_SuperVisSubagents_ObjectIdentity = ObjectIdentity
superVisSubagents = _SuperVisSubagents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2)
)
_SuperVisSubagentNumber_Type = Integer32
_SuperVisSubagentNumber_Object = MibScalar
superVisSubagentNumber = _SuperVisSubagentNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 1),
    _SuperVisSubagentNumber_Type()
)
superVisSubagentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentNumber.setStatus("mandatory")
_SuperVisSubagentTable_Object = MibTable
superVisSubagentTable = _SuperVisSubagentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    superVisSubagentTable.setStatus("mandatory")
_SuperVisSubagentEntry_Object = MibTableRow
superVisSubagentEntry = _SuperVisSubagentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1)
)
superVisSubagentEntry.setIndexNames(
    (0, "Subagent-Supervision-MIB", "superVisSubagentName"),
)
if mibBuilder.loadTexts:
    superVisSubagentEntry.setStatus("mandatory")
_SuperVisSubagentName_Type = DisplayString
_SuperVisSubagentName_Object = MibTableColumn
superVisSubagentName = _SuperVisSubagentName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 1),
    _SuperVisSubagentName_Type()
)
superVisSubagentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentName.setStatus("mandatory")
_SuperVisSubagentSID_Type = Integer32
_SuperVisSubagentSID_Object = MibTableColumn
superVisSubagentSID = _SuperVisSubagentSID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 2),
    _SuperVisSubagentSID_Type()
)
superVisSubagentSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentSID.setStatus("mandatory")


class _SuperVisSubagentStatus_Type(Integer32):
    """Custom type superVisSubagentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disconnected", 2),
          ("undefined", 3))
    )


_SuperVisSubagentStatus_Type.__name__ = "Integer32"
_SuperVisSubagentStatus_Object = MibTableColumn
superVisSubagentStatus = _SuperVisSubagentStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 4),
    _SuperVisSubagentStatus_Type()
)
superVisSubagentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentStatus.setStatus("mandatory")
_SuperVisSubagentConnTime_Type = DisplayString
_SuperVisSubagentConnTime_Object = MibTableColumn
superVisSubagentConnTime = _SuperVisSubagentConnTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 5),
    _SuperVisSubagentConnTime_Type()
)
superVisSubagentConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentConnTime.setStatus("mandatory")
_SuperVisSubagentDisconnTime_Type = DisplayString
_SuperVisSubagentDisconnTime_Object = MibTableColumn
superVisSubagentDisconnTime = _SuperVisSubagentDisconnTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 6),
    _SuperVisSubagentDisconnTime_Type()
)
superVisSubagentDisconnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentDisconnTime.setStatus("mandatory")
_SuperVisSubagentLastResponseTime_Type = DisplayString
_SuperVisSubagentLastResponseTime_Object = MibTableColumn
superVisSubagentLastResponseTime = _SuperVisSubagentLastResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 7),
    _SuperVisSubagentLastResponseTime_Type()
)
superVisSubagentLastResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentLastResponseTime.setStatus("mandatory")
_SuperVisSubagentRequestsDone_Type = Integer32
_SuperVisSubagentRequestsDone_Object = MibTableColumn
superVisSubagentRequestsDone = _SuperVisSubagentRequestsDone_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 8),
    _SuperVisSubagentRequestsDone_Type()
)
superVisSubagentRequestsDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentRequestsDone.setStatus("mandatory")
_SuperVisSubagentTrapsSent_Type = Integer32
_SuperVisSubagentTrapsSent_Object = MibTableColumn
superVisSubagentTrapsSent = _SuperVisSubagentTrapsSent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 9),
    _SuperVisSubagentTrapsSent_Type()
)
superVisSubagentTrapsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentTrapsSent.setStatus("mandatory")
_SuperVisSubagentOID_Type = ObjectIdentifier
_SuperVisSubagentOID_Object = MibTableColumn
superVisSubagentOID = _SuperVisSubagentOID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 10),
    _SuperVisSubagentOID_Type()
)
superVisSubagentOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentOID.setStatus("mandatory")
_SuperVisSubagentProcessID_Type = Integer32
_SuperVisSubagentProcessID_Object = MibTableColumn
superVisSubagentProcessID = _SuperVisSubagentProcessID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 11),
    _SuperVisSubagentProcessID_Type()
)
superVisSubagentProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentProcessID.setStatus("mandatory")
_SuperVisSubagentUserId_Type = DisplayString
_SuperVisSubagentUserId_Object = MibTableColumn
superVisSubagentUserId = _SuperVisSubagentUserId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 12),
    _SuperVisSubagentUserId_Type()
)
superVisSubagentUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentUserId.setStatus("mandatory")
_SuperVisSubagentCpuTime_Type = Integer32
_SuperVisSubagentCpuTime_Object = MibTableColumn
superVisSubagentCpuTime = _SuperVisSubagentCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 13),
    _SuperVisSubagentCpuTime_Type()
)
superVisSubagentCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentCpuTime.setStatus("mandatory")
_SuperVisSubagentCommand_Type = DisplayString
_SuperVisSubagentCommand_Object = MibTableColumn
superVisSubagentCommand = _SuperVisSubagentCommand_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 2, 2, 1, 14),
    _SuperVisSubagentCommand_Type()
)
superVisSubagentCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superVisSubagentCommand.setStatus("mandatory")
_SuperVisTrpAck_ObjectIdentity = ObjectIdentity
superVisTrpAck = _SuperVisTrpAck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 3)
)


class _SuperVisTrpAckState_Type(Integer32):
    """Custom type superVisTrpAckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactiv", 2),
          ("undefined", 3))
    )


_SuperVisTrpAckState_Type.__name__ = "Integer32"
_SuperVisTrpAckState_Object = MibScalar
superVisTrpAckState = _SuperVisTrpAckState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 3, 1),
    _SuperVisTrpAckState_Type()
)
superVisTrpAckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superVisTrpAckState.setStatus("mandatory")
_SuperVisTrpAckId_Type = Integer32
_SuperVisTrpAckId_Object = MibScalar
superVisTrpAckId = _SuperVisTrpAckId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 3, 2),
    _SuperVisTrpAckId_Type()
)
superVisTrpAckId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superVisTrpAckId.setStatus("mandatory")
_SuperVisTrpAckQueueCnt_Type = Integer32
_SuperVisTrpAckQueueCnt_Object = MibScalar
superVisTrpAckQueueCnt = _SuperVisTrpAckQueueCnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 1, 3, 3),
    _SuperVisTrpAckQueueCnt_Type()
)
superVisTrpAckQueueCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superVisTrpAckQueueCnt.setStatus("mandatory")
_SuperVisTraps_ObjectIdentity = ObjectIdentity
superVisTraps = _SuperVisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 2)
)

# Managed Objects groups


# Notification objects

superVisSubAgentConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 2, 0, 301)
)
superVisSubAgentConnected.setObjects(
    ("Subagent-Supervision-MIB", "superVisSubagentName")
)
if mibBuilder.loadTexts:
    superVisSubAgentConnected.setStatus(
        ""
    )

superVisSubAgentDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 2, 0, 302)
)
superVisSubAgentDisconnected.setObjects(
    ("Subagent-Supervision-MIB", "superVisSubagentName")
)
if mibBuilder.loadTexts:
    superVisSubAgentDisconnected.setStatus(
        ""
    )

superVisSubAgentNoAnswer = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 34, 2, 0, 303)
)
superVisSubAgentNoAnswer.setObjects(
    ("Subagent-Supervision-MIB", "superVisSubagentName")
)
if mibBuilder.loadTexts:
    superVisSubAgentNoAnswer.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Subagent-Supervision-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniSupervisor": sniSupervisor,
       "superVisObjects": superVisObjects,
       "superVisGlobalDatas": superVisGlobalDatas,
       "superVisVersion": superVisVersion,
       "superVisActiveNumber": superVisActiveNumber,
       "superVisMaxSubagentNumber": superVisMaxSubagentNumber,
       "superVisObjectNumber": superVisObjectNumber,
       "superVisTrapAckId": superVisTrapAckId,
       "superVisSubagents": superVisSubagents,
       "superVisSubagentNumber": superVisSubagentNumber,
       "superVisSubagentTable": superVisSubagentTable,
       "superVisSubagentEntry": superVisSubagentEntry,
       "superVisSubagentName": superVisSubagentName,
       "superVisSubagentSID": superVisSubagentSID,
       "superVisSubagentStatus": superVisSubagentStatus,
       "superVisSubagentConnTime": superVisSubagentConnTime,
       "superVisSubagentDisconnTime": superVisSubagentDisconnTime,
       "superVisSubagentLastResponseTime": superVisSubagentLastResponseTime,
       "superVisSubagentRequestsDone": superVisSubagentRequestsDone,
       "superVisSubagentTrapsSent": superVisSubagentTrapsSent,
       "superVisSubagentOID": superVisSubagentOID,
       "superVisSubagentProcessID": superVisSubagentProcessID,
       "superVisSubagentUserId": superVisSubagentUserId,
       "superVisSubagentCpuTime": superVisSubagentCpuTime,
       "superVisSubagentCommand": superVisSubagentCommand,
       "superVisTrpAck": superVisTrpAck,
       "superVisTrpAckState": superVisTrpAckState,
       "superVisTrpAckId": superVisTrpAckId,
       "superVisTrpAckQueueCnt": superVisTrpAckQueueCnt,
       "superVisTraps": superVisTraps,
       "superVisSubAgentConnected": superVisSubAgentConnected,
       "superVisSubAgentDisconnected": superVisSubAgentDisconnected,
       "superVisSubAgentNoAnswer": superVisSubAgentNoAnswer}
)
