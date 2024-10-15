# SNMP MIB module (CT-MSGXFERSERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-MSGXFERSERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:18 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_CtMessageTransferService_ObjectIdentity = ObjectIdentity
ctMessageTransferService = _CtMessageTransferService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7)
)
_NumberOfMTSInstances_Type = Integer32
_NumberOfMTSInstances_Object = MibScalar
numberOfMTSInstances = _NumberOfMTSInstances_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 1),
    _NumberOfMTSInstances_Type()
)
numberOfMTSInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfMTSInstances.setStatus("mandatory")
_MessageTransferServiceTable_Object = MibTable
messageTransferServiceTable = _MessageTransferServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2)
)
if mibBuilder.loadTexts:
    messageTransferServiceTable.setStatus("mandatory")
_MessageTransferServiceEntry_Object = MibTableRow
messageTransferServiceEntry = _MessageTransferServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1)
)
messageTransferServiceEntry.setIndexNames(
    (0, "CT-MSGXFERSERVICE-MIB", "mtsInstanceID"),
)
if mibBuilder.loadTexts:
    messageTransferServiceEntry.setStatus("mandatory")
_MtsInstanceID_Type = Integer32
_MtsInstanceID_Object = MibTableColumn
mtsInstanceID = _MtsInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 1),
    _MtsInstanceID_Type()
)
mtsInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsInstanceID.setStatus("mandatory")
_MtsMBusID_Type = Integer32
_MtsMBusID_Object = MibTableColumn
mtsMBusID = _MtsMBusID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 2),
    _MtsMBusID_Type()
)
mtsMBusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsMBusID.setStatus("mandatory")
_MtsNumberOfMTSUsers_Type = Integer32
_MtsNumberOfMTSUsers_Object = MibTableColumn
mtsNumberOfMTSUsers = _MtsNumberOfMTSUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 3),
    _MtsNumberOfMTSUsers_Type()
)
mtsNumberOfMTSUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsNumberOfMTSUsers.setStatus("mandatory")
_MtsNumberOfMTSBuffers_Type = Integer32
_MtsNumberOfMTSBuffers_Object = MibTableColumn
mtsNumberOfMTSBuffers = _MtsNumberOfMTSBuffers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 4),
    _MtsNumberOfMTSBuffers_Type()
)
mtsNumberOfMTSBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsNumberOfMTSBuffers.setStatus("mandatory")
_MtsSizeOfMTSBuffers_Type = Integer32
_MtsSizeOfMTSBuffers_Object = MibTableColumn
mtsSizeOfMTSBuffers = _MtsSizeOfMTSBuffers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 5),
    _MtsSizeOfMTSBuffers_Type()
)
mtsSizeOfMTSBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsSizeOfMTSBuffers.setStatus("mandatory")
_MtsNumberOfPostedMsgs_Type = Counter32
_MtsNumberOfPostedMsgs_Object = MibTableColumn
mtsNumberOfPostedMsgs = _MtsNumberOfPostedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 6),
    _MtsNumberOfPostedMsgs_Type()
)
mtsNumberOfPostedMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfPostedMsgs.setStatus("mandatory")
_MtsNumberOfPostedBytes_Type = Counter32
_MtsNumberOfPostedBytes_Object = MibTableColumn
mtsNumberOfPostedBytes = _MtsNumberOfPostedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 7),
    _MtsNumberOfPostedBytes_Type()
)
mtsNumberOfPostedBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfPostedBytes.setStatus("mandatory")
_MtsNumberOfPostedPriorityMsgs_Type = Counter32
_MtsNumberOfPostedPriorityMsgs_Object = MibTableColumn
mtsNumberOfPostedPriorityMsgs = _MtsNumberOfPostedPriorityMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 8),
    _MtsNumberOfPostedPriorityMsgs_Type()
)
mtsNumberOfPostedPriorityMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfPostedPriorityMsgs.setStatus("mandatory")
_MtsNumberOfPostedPriorityBytes_Type = Counter32
_MtsNumberOfPostedPriorityBytes_Object = MibTableColumn
mtsNumberOfPostedPriorityBytes = _MtsNumberOfPostedPriorityBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 9),
    _MtsNumberOfPostedPriorityBytes_Type()
)
mtsNumberOfPostedPriorityBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfPostedPriorityBytes.setStatus("mandatory")
_MtsNumberOfSentMsgs_Type = Counter32
_MtsNumberOfSentMsgs_Object = MibTableColumn
mtsNumberOfSentMsgs = _MtsNumberOfSentMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 10),
    _MtsNumberOfSentMsgs_Type()
)
mtsNumberOfSentMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfSentMsgs.setStatus("mandatory")
_MtsNumberOfSentBytes_Type = Counter32
_MtsNumberOfSentBytes_Object = MibTableColumn
mtsNumberOfSentBytes = _MtsNumberOfSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 11),
    _MtsNumberOfSentBytes_Type()
)
mtsNumberOfSentBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfSentBytes.setStatus("mandatory")
_MtsNumberOfPendingMsgs_Type = Gauge32
_MtsNumberOfPendingMsgs_Object = MibTableColumn
mtsNumberOfPendingMsgs = _MtsNumberOfPendingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 12),
    _MtsNumberOfPendingMsgs_Type()
)
mtsNumberOfPendingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsNumberOfPendingMsgs.setStatus("mandatory")
_MtsNumberOfPendingBytes_Type = Gauge32
_MtsNumberOfPendingBytes_Object = MibTableColumn
mtsNumberOfPendingBytes = _MtsNumberOfPendingBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 13),
    _MtsNumberOfPendingBytes_Type()
)
mtsNumberOfPendingBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsNumberOfPendingBytes.setStatus("mandatory")
_MtsHighWaterForPendingMsgs_Type = Integer32
_MtsHighWaterForPendingMsgs_Object = MibTableColumn
mtsHighWaterForPendingMsgs = _MtsHighWaterForPendingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 14),
    _MtsHighWaterForPendingMsgs_Type()
)
mtsHighWaterForPendingMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsHighWaterForPendingMsgs.setStatus("mandatory")
_MtsHighWaterForPendingBytes_Type = Integer32
_MtsHighWaterForPendingBytes_Object = MibTableColumn
mtsHighWaterForPendingBytes = _MtsHighWaterForPendingBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 15),
    _MtsHighWaterForPendingBytes_Type()
)
mtsHighWaterForPendingBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsHighWaterForPendingBytes.setStatus("mandatory")
_MtsNumberOfTransmissions_Type = Counter32
_MtsNumberOfTransmissions_Object = MibTableColumn
mtsNumberOfTransmissions = _MtsNumberOfTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 16),
    _MtsNumberOfTransmissions_Type()
)
mtsNumberOfTransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfTransmissions.setStatus("mandatory")
_MtsNumberOfReceptions_Type = Counter32
_MtsNumberOfReceptions_Object = MibTableColumn
mtsNumberOfReceptions = _MtsNumberOfReceptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 17),
    _MtsNumberOfReceptions_Type()
)
mtsNumberOfReceptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfReceptions.setStatus("mandatory")
_MtsNumberOfReceivedMsgs_Type = Counter32
_MtsNumberOfReceivedMsgs_Object = MibTableColumn
mtsNumberOfReceivedMsgs = _MtsNumberOfReceivedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 18),
    _MtsNumberOfReceivedMsgs_Type()
)
mtsNumberOfReceivedMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfReceivedMsgs.setStatus("mandatory")
_MtsNumberOfRcvNoBufs_Type = Counter32
_MtsNumberOfRcvNoBufs_Object = MibTableColumn
mtsNumberOfRcvNoBufs = _MtsNumberOfRcvNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 19),
    _MtsNumberOfRcvNoBufs_Type()
)
mtsNumberOfRcvNoBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfRcvNoBufs.setStatus("mandatory")
_MtsNumberOfRcvNoUsers_Type = Counter32
_MtsNumberOfRcvNoUsers_Object = MibTableColumn
mtsNumberOfRcvNoUsers = _MtsNumberOfRcvNoUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 20),
    _MtsNumberOfRcvNoUsers_Type()
)
mtsNumberOfRcvNoUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfRcvNoUsers.setStatus("mandatory")
_MtsNumberOfSentPriorityMsgs_Type = Counter32
_MtsNumberOfSentPriorityMsgs_Object = MibTableColumn
mtsNumberOfSentPriorityMsgs = _MtsNumberOfSentPriorityMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 21),
    _MtsNumberOfSentPriorityMsgs_Type()
)
mtsNumberOfSentPriorityMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfSentPriorityMsgs.setStatus("mandatory")
_MtsNumberOfSentPriorityBytes_Type = Counter32
_MtsNumberOfSentPriorityBytes_Object = MibTableColumn
mtsNumberOfSentPriorityBytes = _MtsNumberOfSentPriorityBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 22),
    _MtsNumberOfSentPriorityBytes_Type()
)
mtsNumberOfSentPriorityBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfSentPriorityBytes.setStatus("mandatory")
_MtsNumberOfReceivedBytes_Type = Counter32
_MtsNumberOfReceivedBytes_Object = MibTableColumn
mtsNumberOfReceivedBytes = _MtsNumberOfReceivedBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 23),
    _MtsNumberOfReceivedBytes_Type()
)
mtsNumberOfReceivedBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfReceivedBytes.setStatus("mandatory")
_MtsNumberOfReceivedPriorityMsgs_Type = Counter32
_MtsNumberOfReceivedPriorityMsgs_Object = MibTableColumn
mtsNumberOfReceivedPriorityMsgs = _MtsNumberOfReceivedPriorityMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 24),
    _MtsNumberOfReceivedPriorityMsgs_Type()
)
mtsNumberOfReceivedPriorityMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfReceivedPriorityMsgs.setStatus("mandatory")
_MtsNumberOfReceivedPriorityBytes_Type = Counter32
_MtsNumberOfReceivedPriorityBytes_Object = MibTableColumn
mtsNumberOfReceivedPriorityBytes = _MtsNumberOfReceivedPriorityBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 25),
    _MtsNumberOfReceivedPriorityBytes_Type()
)
mtsNumberOfReceivedPriorityBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfReceivedPriorityBytes.setStatus("mandatory")
_MtsNumberOfAckdMsgs_Type = Counter32
_MtsNumberOfAckdMsgs_Object = MibTableColumn
mtsNumberOfAckdMsgs = _MtsNumberOfAckdMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 26),
    _MtsNumberOfAckdMsgs_Type()
)
mtsNumberOfAckdMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfAckdMsgs.setStatus("mandatory")
_MtsNumberOfAckdPriorityMsgs_Type = Counter32
_MtsNumberOfAckdPriorityMsgs_Object = MibTableColumn
mtsNumberOfAckdPriorityMsgs = _MtsNumberOfAckdPriorityMsgs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 27),
    _MtsNumberOfAckdPriorityMsgs_Type()
)
mtsNumberOfAckdPriorityMsgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsNumberOfAckdPriorityMsgs.setStatus("mandatory")
_MtsHighWaterForMsgsPerTransmission_Type = Integer32
_MtsHighWaterForMsgsPerTransmission_Object = MibTableColumn
mtsHighWaterForMsgsPerTransmission = _MtsHighWaterForMsgsPerTransmission_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 28),
    _MtsHighWaterForMsgsPerTransmission_Type()
)
mtsHighWaterForMsgsPerTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsHighWaterForMsgsPerTransmission.setStatus("mandatory")
_MtsHighWaterForMsgsPerReception_Type = Integer32
_MtsHighWaterForMsgsPerReception_Object = MibTableColumn
mtsHighWaterForMsgsPerReception = _MtsHighWaterForMsgsPerReception_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 7, 2, 1, 29),
    _MtsHighWaterForMsgsPerReception_Type()
)
mtsHighWaterForMsgsPerReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtsHighWaterForMsgsPerReception.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-MSGXFERSERVICE-MIB",
    **{"ctSSA": ctSSA,
       "ctMessageTransferService": ctMessageTransferService,
       "numberOfMTSInstances": numberOfMTSInstances,
       "messageTransferServiceTable": messageTransferServiceTable,
       "messageTransferServiceEntry": messageTransferServiceEntry,
       "mtsInstanceID": mtsInstanceID,
       "mtsMBusID": mtsMBusID,
       "mtsNumberOfMTSUsers": mtsNumberOfMTSUsers,
       "mtsNumberOfMTSBuffers": mtsNumberOfMTSBuffers,
       "mtsSizeOfMTSBuffers": mtsSizeOfMTSBuffers,
       "mtsNumberOfPostedMsgs": mtsNumberOfPostedMsgs,
       "mtsNumberOfPostedBytes": mtsNumberOfPostedBytes,
       "mtsNumberOfPostedPriorityMsgs": mtsNumberOfPostedPriorityMsgs,
       "mtsNumberOfPostedPriorityBytes": mtsNumberOfPostedPriorityBytes,
       "mtsNumberOfSentMsgs": mtsNumberOfSentMsgs,
       "mtsNumberOfSentBytes": mtsNumberOfSentBytes,
       "mtsNumberOfPendingMsgs": mtsNumberOfPendingMsgs,
       "mtsNumberOfPendingBytes": mtsNumberOfPendingBytes,
       "mtsHighWaterForPendingMsgs": mtsHighWaterForPendingMsgs,
       "mtsHighWaterForPendingBytes": mtsHighWaterForPendingBytes,
       "mtsNumberOfTransmissions": mtsNumberOfTransmissions,
       "mtsNumberOfReceptions": mtsNumberOfReceptions,
       "mtsNumberOfReceivedMsgs": mtsNumberOfReceivedMsgs,
       "mtsNumberOfRcvNoBufs": mtsNumberOfRcvNoBufs,
       "mtsNumberOfRcvNoUsers": mtsNumberOfRcvNoUsers,
       "mtsNumberOfSentPriorityMsgs": mtsNumberOfSentPriorityMsgs,
       "mtsNumberOfSentPriorityBytes": mtsNumberOfSentPriorityBytes,
       "mtsNumberOfReceivedBytes": mtsNumberOfReceivedBytes,
       "mtsNumberOfReceivedPriorityMsgs": mtsNumberOfReceivedPriorityMsgs,
       "mtsNumberOfReceivedPriorityBytes": mtsNumberOfReceivedPriorityBytes,
       "mtsNumberOfAckdMsgs": mtsNumberOfAckdMsgs,
       "mtsNumberOfAckdPriorityMsgs": mtsNumberOfAckdPriorityMsgs,
       "mtsHighWaterForMsgsPerTransmission": mtsHighWaterForMsgsPerTransmission,
       "mtsHighWaterForMsgsPerReception": mtsHighWaterForMsgsPerReception}
)
