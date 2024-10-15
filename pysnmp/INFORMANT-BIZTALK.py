# SNMP MIB module (INFORMANT-BIZTALK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INFORMANT-BIZTALK
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:11 2024
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

(InstanceName,
 informant) = mibBuilder.importSymbols(
    "WTCS",
    "InstanceName",
    "informant")


# MODULE-IDENTITY

bizTalkServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4)
)
bizTalkServer.setRevisions(
        ("2007-05-24 22:10",
         "2004-02-29 06:33",
         "2004-01-22 06:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BizTalkFILEReceiveAdapterTable_Object = MibTable
bizTalkFILEReceiveAdapterTable = _BizTalkFILEReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bizTalkFILEReceiveAdapterTable.setStatus("current")
_BizTalkFILEReceiveAdapterEntry_Object = MibTableRow
bizTalkFILEReceiveAdapterEntry = _BizTalkFILEReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1)
)
bizTalkFILEReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btfileraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkFILEReceiveAdapterEntry.setStatus("current")
_BtfileraInstance_Type = InstanceName
_BtfileraInstance_Object = MibTableColumn
btfileraInstance = _BtfileraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 1),
    _BtfileraInstance_Type()
)
btfileraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraInstance.setStatus("current")
_BtfileraBytesReceived_Type = Gauge32
_BtfileraBytesReceived_Object = MibTableColumn
btfileraBytesReceived = _BtfileraBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 2),
    _BtfileraBytesReceived_Type()
)
btfileraBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraBytesReceived.setStatus("current")
_BtfileraBytesReceivedPerSec_Type = Gauge32
_BtfileraBytesReceivedPerSec_Object = MibTableColumn
btfileraBytesReceivedPerSec = _BtfileraBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 3),
    _BtfileraBytesReceivedPerSec_Type()
)
btfileraBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraBytesReceivedPerSec.setStatus("current")
_BtfileraDeleteRetries_Type = Gauge32
_BtfileraDeleteRetries_Object = MibTableColumn
btfileraDeleteRetries = _BtfileraDeleteRetries_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 4),
    _BtfileraDeleteRetries_Type()
)
btfileraDeleteRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraDeleteRetries.setStatus("current")
_BtfileraLockFailures_Type = Gauge32
_BtfileraLockFailures_Object = MibTableColumn
btfileraLockFailures = _BtfileraLockFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 5),
    _BtfileraLockFailures_Type()
)
btfileraLockFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraLockFailures.setStatus("current")
_BtfileraLockFailuresPerSec_Type = Gauge32
_BtfileraLockFailuresPerSec_Object = MibTableColumn
btfileraLockFailuresPerSec = _BtfileraLockFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 6),
    _BtfileraLockFailuresPerSec_Type()
)
btfileraLockFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraLockFailuresPerSec.setStatus("current")
_BtfileraMessagesReceived_Type = Gauge32
_BtfileraMessagesReceived_Object = MibTableColumn
btfileraMessagesReceived = _BtfileraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 7),
    _BtfileraMessagesReceived_Type()
)
btfileraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraMessagesReceived.setStatus("current")
_BtfileraMessagesReceivedPerSec_Type = Gauge32
_BtfileraMessagesReceivedPerSec_Object = MibTableColumn
btfileraMessagesReceivedPerSec = _BtfileraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 8),
    _BtfileraMessagesReceivedPerSec_Type()
)
btfileraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraMessagesReceivedPerSec.setStatus("current")
_BtfileraTimeToBuildBatch_Type = Gauge32
_BtfileraTimeToBuildBatch_Object = MibTableColumn
btfileraTimeToBuildBatch = _BtfileraTimeToBuildBatch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 1, 1, 9),
    _BtfileraTimeToBuildBatch_Type()
)
btfileraTimeToBuildBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfileraTimeToBuildBatch.setStatus("current")
_BizTalkFILESendAdapterTable_Object = MibTable
bizTalkFILESendAdapterTable = _BizTalkFILESendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bizTalkFILESendAdapterTable.setStatus("current")
_BizTalkFILESendAdapterEntry_Object = MibTableRow
bizTalkFILESendAdapterEntry = _BizTalkFILESendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1)
)
bizTalkFILESendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btfilesaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkFILESendAdapterEntry.setStatus("current")
_BtfilesaInstance_Type = InstanceName
_BtfilesaInstance_Object = MibTableColumn
btfilesaInstance = _BtfilesaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1, 1),
    _BtfilesaInstance_Type()
)
btfilesaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfilesaInstance.setStatus("current")
_BtfilesaBytesSent_Type = Gauge32
_BtfilesaBytesSent_Object = MibTableColumn
btfilesaBytesSent = _BtfilesaBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1, 2),
    _BtfilesaBytesSent_Type()
)
btfilesaBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfilesaBytesSent.setStatus("current")
_BtfilesaBytesSentPerSec_Type = Gauge32
_BtfilesaBytesSentPerSec_Object = MibTableColumn
btfilesaBytesSentPerSec = _BtfilesaBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1, 3),
    _BtfilesaBytesSentPerSec_Type()
)
btfilesaBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfilesaBytesSentPerSec.setStatus("current")
_BtfilesaMessagesSent_Type = Gauge32
_BtfilesaMessagesSent_Object = MibTableColumn
btfilesaMessagesSent = _BtfilesaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1, 4),
    _BtfilesaMessagesSent_Type()
)
btfilesaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfilesaMessagesSent.setStatus("current")
_BtfilesaMessagesSentPerSec_Type = Gauge32
_BtfilesaMessagesSentPerSec_Object = MibTableColumn
btfilesaMessagesSentPerSec = _BtfilesaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 2, 1, 5),
    _BtfilesaMessagesSentPerSec_Type()
)
btfilesaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btfilesaMessagesSentPerSec.setStatus("current")
_BizTalkFTPReceiveAdapterTable_Object = MibTable
bizTalkFTPReceiveAdapterTable = _BizTalkFTPReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3)
)
if mibBuilder.loadTexts:
    bizTalkFTPReceiveAdapterTable.setStatus("current")
_BizTalkFTPReceiveAdapterEntry_Object = MibTableRow
bizTalkFTPReceiveAdapterEntry = _BizTalkFTPReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1)
)
bizTalkFTPReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btftpraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkFTPReceiveAdapterEntry.setStatus("current")
_BtftpraInstance_Type = InstanceName
_BtftpraInstance_Object = MibTableColumn
btftpraInstance = _BtftpraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1, 1),
    _BtftpraInstance_Type()
)
btftpraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpraInstance.setStatus("current")
_BtftpraBytesReceived_Type = Gauge32
_BtftpraBytesReceived_Object = MibTableColumn
btftpraBytesReceived = _BtftpraBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1, 2),
    _BtftpraBytesReceived_Type()
)
btftpraBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpraBytesReceived.setStatus("current")
_BtftpraBytesReceivedPerSec_Type = Gauge32
_BtftpraBytesReceivedPerSec_Object = MibTableColumn
btftpraBytesReceivedPerSec = _BtftpraBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1, 3),
    _BtftpraBytesReceivedPerSec_Type()
)
btftpraBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpraBytesReceivedPerSec.setStatus("current")
_BtftpraMessagesReceived_Type = Gauge32
_BtftpraMessagesReceived_Object = MibTableColumn
btftpraMessagesReceived = _BtftpraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1, 4),
    _BtftpraMessagesReceived_Type()
)
btftpraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpraMessagesReceived.setStatus("current")
_BtftpraMessagesReceivedPerSec_Type = Gauge32
_BtftpraMessagesReceivedPerSec_Object = MibTableColumn
btftpraMessagesReceivedPerSec = _BtftpraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 3, 1, 5),
    _BtftpraMessagesReceivedPerSec_Type()
)
btftpraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpraMessagesReceivedPerSec.setStatus("current")
_BizTalkFTPSendAdapterTable_Object = MibTable
bizTalkFTPSendAdapterTable = _BizTalkFTPSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4)
)
if mibBuilder.loadTexts:
    bizTalkFTPSendAdapterTable.setStatus("current")
_BizTalkFTPSendAdapterEntry_Object = MibTableRow
bizTalkFTPSendAdapterEntry = _BizTalkFTPSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1)
)
bizTalkFTPSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btftpsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkFTPSendAdapterEntry.setStatus("current")
_BtftpsaInstance_Type = InstanceName
_BtftpsaInstance_Object = MibTableColumn
btftpsaInstance = _BtftpsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1, 1),
    _BtftpsaInstance_Type()
)
btftpsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpsaInstance.setStatus("current")
_BtftpsaBytesSent_Type = Gauge32
_BtftpsaBytesSent_Object = MibTableColumn
btftpsaBytesSent = _BtftpsaBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1, 2),
    _BtftpsaBytesSent_Type()
)
btftpsaBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpsaBytesSent.setStatus("current")
_BtftpsaBytesSentPerSec_Type = Gauge32
_BtftpsaBytesSentPerSec_Object = MibTableColumn
btftpsaBytesSentPerSec = _BtftpsaBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1, 3),
    _BtftpsaBytesSentPerSec_Type()
)
btftpsaBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpsaBytesSentPerSec.setStatus("current")
_BtftpsaMessagesSent_Type = Gauge32
_BtftpsaMessagesSent_Object = MibTableColumn
btftpsaMessagesSent = _BtftpsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1, 4),
    _BtftpsaMessagesSent_Type()
)
btftpsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpsaMessagesSent.setStatus("current")
_BtftpsaMessagesSentPerSec_Type = Gauge32
_BtftpsaMessagesSentPerSec_Object = MibTableColumn
btftpsaMessagesSentPerSec = _BtftpsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 4, 1, 5),
    _BtftpsaMessagesSentPerSec_Type()
)
btftpsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btftpsaMessagesSentPerSec.setStatus("current")
_BizTalkHTTPReceiveAdapterTable_Object = MibTable
bizTalkHTTPReceiveAdapterTable = _BizTalkHTTPReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5)
)
if mibBuilder.loadTexts:
    bizTalkHTTPReceiveAdapterTable.setStatus("current")
_BizTalkHTTPReceiveAdapterEntry_Object = MibTableRow
bizTalkHTTPReceiveAdapterEntry = _BizTalkHTTPReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1)
)
bizTalkHTTPReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "bthttpraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkHTTPReceiveAdapterEntry.setStatus("current")
_BthttpraInstance_Type = InstanceName
_BthttpraInstance_Object = MibTableColumn
bthttpraInstance = _BthttpraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 1),
    _BthttpraInstance_Type()
)
bthttpraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraInstance.setStatus("current")
_BthttpraMemoryQueueSize_Type = Gauge32
_BthttpraMemoryQueueSize_Object = MibTableColumn
bthttpraMemoryQueueSize = _BthttpraMemoryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 2),
    _BthttpraMemoryQueueSize_Type()
)
bthttpraMemoryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraMemoryQueueSize.setStatus("current")
_BthttpraMessagesReceived_Type = Gauge32
_BthttpraMessagesReceived_Object = MibTableColumn
bthttpraMessagesReceived = _BthttpraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 3),
    _BthttpraMessagesReceived_Type()
)
bthttpraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraMessagesReceived.setStatus("current")
_BthttpraMessagesReceivedPerSec_Type = Gauge32
_BthttpraMessagesReceivedPerSec_Object = MibTableColumn
bthttpraMessagesReceivedPerSec = _BthttpraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 4),
    _BthttpraMessagesReceivedPerSec_Type()
)
bthttpraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraMessagesReceivedPerSec.setStatus("current")
_BthttpraMessagesSent_Type = Gauge32
_BthttpraMessagesSent_Object = MibTableColumn
bthttpraMessagesSent = _BthttpraMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 5),
    _BthttpraMessagesSent_Type()
)
bthttpraMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraMessagesSent.setStatus("current")
_BthttpraMessagesSentPerSec_Type = Gauge32
_BthttpraMessagesSentPerSec_Object = MibTableColumn
bthttpraMessagesSentPerSec = _BthttpraMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 6),
    _BthttpraMessagesSentPerSec_Type()
)
bthttpraMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraMessagesSentPerSec.setStatus("current")
_BthttpraTimeToAddMessageToBatch_Type = Gauge32
_BthttpraTimeToAddMessageToBatch_Object = MibTableColumn
bthttpraTimeToAddMessageToBatch = _BthttpraTimeToAddMessageToBatch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 7),
    _BthttpraTimeToAddMessageToBatch_Type()
)
bthttpraTimeToAddMessageToBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraTimeToAddMessageToBatch.setStatus("current")
_BthttpraTimeToBuildBatch_Type = Gauge32
_BthttpraTimeToBuildBatch_Object = MibTableColumn
bthttpraTimeToBuildBatch = _BthttpraTimeToBuildBatch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 5, 1, 8),
    _BthttpraTimeToBuildBatch_Type()
)
bthttpraTimeToBuildBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpraTimeToBuildBatch.setStatus("current")
_BizTalkHTTPSendAdapterTable_Object = MibTable
bizTalkHTTPSendAdapterTable = _BizTalkHTTPSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6)
)
if mibBuilder.loadTexts:
    bizTalkHTTPSendAdapterTable.setStatus("current")
_BizTalkHTTPSendAdapterEntry_Object = MibTableRow
bizTalkHTTPSendAdapterEntry = _BizTalkHTTPSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1)
)
bizTalkHTTPSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "bthttpsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkHTTPSendAdapterEntry.setStatus("current")
_BthttpsaInstance_Type = InstanceName
_BthttpsaInstance_Object = MibTableColumn
bthttpsaInstance = _BthttpsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 1),
    _BthttpsaInstance_Type()
)
bthttpsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaInstance.setStatus("current")
_BthttpsaMemoryQueueSize_Type = Gauge32
_BthttpsaMemoryQueueSize_Object = MibTableColumn
bthttpsaMemoryQueueSize = _BthttpsaMemoryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 2),
    _BthttpsaMemoryQueueSize_Type()
)
bthttpsaMemoryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaMemoryQueueSize.setStatus("current")
_BthttpsaMessagesReceived_Type = Gauge32
_BthttpsaMessagesReceived_Object = MibTableColumn
bthttpsaMessagesReceived = _BthttpsaMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 3),
    _BthttpsaMessagesReceived_Type()
)
bthttpsaMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaMessagesReceived.setStatus("current")
_BthttpsaMessagesReceivedPerSec_Type = Gauge32
_BthttpsaMessagesReceivedPerSec_Object = MibTableColumn
bthttpsaMessagesReceivedPerSec = _BthttpsaMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 4),
    _BthttpsaMessagesReceivedPerSec_Type()
)
bthttpsaMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaMessagesReceivedPerSec.setStatus("current")
_BthttpsaMessagesSent_Type = Gauge32
_BthttpsaMessagesSent_Object = MibTableColumn
bthttpsaMessagesSent = _BthttpsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 5),
    _BthttpsaMessagesSent_Type()
)
bthttpsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaMessagesSent.setStatus("current")
_BthttpsaMessagesSentPerSec_Type = Gauge32
_BthttpsaMessagesSentPerSec_Object = MibTableColumn
bthttpsaMessagesSentPerSec = _BthttpsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 6, 1, 6),
    _BthttpsaMessagesSentPerSec_Type()
)
bthttpsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bthttpsaMessagesSentPerSec.setStatus("current")
_BizTalkMSMQReceiveAdapterTable_Object = MibTable
bizTalkMSMQReceiveAdapterTable = _BizTalkMSMQReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7)
)
if mibBuilder.loadTexts:
    bizTalkMSMQReceiveAdapterTable.setStatus("current")
_BizTalkMSMQReceiveAdapterEntry_Object = MibTableRow
bizTalkMSMQReceiveAdapterEntry = _BizTalkMSMQReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1)
)
bizTalkMSMQReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmsmqraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMSMQReceiveAdapterEntry.setStatus("current")
_BtmsmqraInstance_Type = InstanceName
_BtmsmqraInstance_Object = MibTableColumn
btmsmqraInstance = _BtmsmqraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1, 1),
    _BtmsmqraInstance_Type()
)
btmsmqraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqraInstance.setStatus("current")
_BtmsmqraBytesReceived_Type = Gauge32
_BtmsmqraBytesReceived_Object = MibTableColumn
btmsmqraBytesReceived = _BtmsmqraBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1, 2),
    _BtmsmqraBytesReceived_Type()
)
btmsmqraBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqraBytesReceived.setStatus("current")
_BtmsmqraBytesReceivedPerSec_Type = Gauge32
_BtmsmqraBytesReceivedPerSec_Object = MibTableColumn
btmsmqraBytesReceivedPerSec = _BtmsmqraBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1, 3),
    _BtmsmqraBytesReceivedPerSec_Type()
)
btmsmqraBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqraBytesReceivedPerSec.setStatus("current")
_BtmsmqraMessagesReceived_Type = Gauge32
_BtmsmqraMessagesReceived_Object = MibTableColumn
btmsmqraMessagesReceived = _BtmsmqraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1, 4),
    _BtmsmqraMessagesReceived_Type()
)
btmsmqraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqraMessagesReceived.setStatus("current")
_BtmsmqraMessagesReceivedPerSec_Type = Gauge32
_BtmsmqraMessagesReceivedPerSec_Object = MibTableColumn
btmsmqraMessagesReceivedPerSec = _BtmsmqraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 7, 1, 5),
    _BtmsmqraMessagesReceivedPerSec_Type()
)
btmsmqraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqraMessagesReceivedPerSec.setStatus("current")
_BizTalkMSMQSendAdapterTable_Object = MibTable
bizTalkMSMQSendAdapterTable = _BizTalkMSMQSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8)
)
if mibBuilder.loadTexts:
    bizTalkMSMQSendAdapterTable.setStatus("current")
_BizTalkMSMQSendAdapterEntry_Object = MibTableRow
bizTalkMSMQSendAdapterEntry = _BizTalkMSMQSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1)
)
bizTalkMSMQSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmsmqsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMSMQSendAdapterEntry.setStatus("current")
_BtmsmqsaInstance_Type = InstanceName
_BtmsmqsaInstance_Object = MibTableColumn
btmsmqsaInstance = _BtmsmqsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1, 1),
    _BtmsmqsaInstance_Type()
)
btmsmqsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqsaInstance.setStatus("current")
_BtmsmqsaBytesSent_Type = Gauge32
_BtmsmqsaBytesSent_Object = MibTableColumn
btmsmqsaBytesSent = _BtmsmqsaBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1, 2),
    _BtmsmqsaBytesSent_Type()
)
btmsmqsaBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqsaBytesSent.setStatus("current")
_BtmsmqsaBytesSentPerSec_Type = Gauge32
_BtmsmqsaBytesSentPerSec_Object = MibTableColumn
btmsmqsaBytesSentPerSec = _BtmsmqsaBytesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1, 3),
    _BtmsmqsaBytesSentPerSec_Type()
)
btmsmqsaBytesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqsaBytesSentPerSec.setStatus("current")
_BtmsmqsaMessagesSent_Type = Gauge32
_BtmsmqsaMessagesSent_Object = MibTableColumn
btmsmqsaMessagesSent = _BtmsmqsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1, 4),
    _BtmsmqsaMessagesSent_Type()
)
btmsmqsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqsaMessagesSent.setStatus("current")
_BtmsmqsaMessagesSentPerSec_Type = Gauge32
_BtmsmqsaMessagesSentPerSec_Object = MibTableColumn
btmsmqsaMessagesSentPerSec = _BtmsmqsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 8, 1, 5),
    _BtmsmqsaMessagesSentPerSec_Type()
)
btmsmqsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmsmqsaMessagesSentPerSec.setStatus("current")
_BizTalkMessageAgentTable_Object = MibTable
bizTalkMessageAgentTable = _BizTalkMessageAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9)
)
if mibBuilder.loadTexts:
    bizTalkMessageAgentTable.setStatus("current")
_BizTalkMessageAgentEntry_Object = MibTableRow
bizTalkMessageAgentEntry = _BizTalkMessageAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1)
)
bizTalkMessageAgentEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMessageAgentEntry.setStatus("current")
_BtmaInstance_Type = InstanceName
_BtmaInstance_Object = MibTableColumn
btmaInstance = _BtmaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 1),
    _BtmaInstance_Type()
)
btmaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaInstance.setStatus("current")
_BtmaActiveInstanceCount_Type = Gauge32
_BtmaActiveInstanceCount_Object = MibTableColumn
btmaActiveInstanceCount = _BtmaActiveInstanceCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 2),
    _BtmaActiveInstanceCount_Type()
)
btmaActiveInstanceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaActiveInstanceCount.setStatus("current")
_BtmaDatabaseSession_Type = Gauge32
_BtmaDatabaseSession_Object = MibTableColumn
btmaDatabaseSession = _BtmaDatabaseSession_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 3),
    _BtmaDatabaseSession_Type()
)
btmaDatabaseSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaDatabaseSession.setStatus("current")
_BtmaDatabaseSessionThreshold_Type = Gauge32
_BtmaDatabaseSessionThreshold_Object = MibTableColumn
btmaDatabaseSessionThreshold = _BtmaDatabaseSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 4),
    _BtmaDatabaseSessionThreshold_Type()
)
btmaDatabaseSessionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaDatabaseSessionThreshold.setStatus("current")
_BtmaDatabaseSize_Type = Gauge32
_BtmaDatabaseSize_Object = MibTableColumn
btmaDatabaseSize = _BtmaDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 5),
    _BtmaDatabaseSize_Type()
)
btmaDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaDatabaseSize.setStatus("current")
_BtmaHighDatabaseSession_Type = Gauge32
_BtmaHighDatabaseSession_Object = MibTableColumn
btmaHighDatabaseSession = _BtmaHighDatabaseSession_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 6),
    _BtmaHighDatabaseSession_Type()
)
btmaHighDatabaseSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighDatabaseSession.setStatus("current")
_BtmaHighDatabaseSize_Type = Gauge32
_BtmaHighDatabaseSize_Object = MibTableColumn
btmaHighDatabaseSize = _BtmaHighDatabaseSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 7),
    _BtmaHighDatabaseSize_Type()
)
btmaHighDatabaseSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighDatabaseSize.setStatus("current")
_BtmaHighInprocessMessageCount_Type = Gauge32
_BtmaHighInprocessMessageCount_Object = MibTableColumn
btmaHighInprocessMessageCount = _BtmaHighInprocessMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 8),
    _BtmaHighInprocessMessageCount_Type()
)
btmaHighInprocessMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighInprocessMessageCount.setStatus("current")
_BtmaHighMessageDeliveryRate_Type = Gauge32
_BtmaHighMessageDeliveryRate_Object = MibTableColumn
btmaHighMessageDeliveryRate = _BtmaHighMessageDeliveryRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 9),
    _BtmaHighMessageDeliveryRate_Type()
)
btmaHighMessageDeliveryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighMessageDeliveryRate.setStatus("current")
_BtmaHighMessagePublishingRate_Type = Gauge32
_BtmaHighMessagePublishingRate_Object = MibTableColumn
btmaHighMessagePublishingRate = _BtmaHighMessagePublishingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 10),
    _BtmaHighMessagePublishingRate_Type()
)
btmaHighMessagePublishingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighMessagePublishingRate.setStatus("current")
_BtmaHighProcessMemory_Type = Gauge32
_BtmaHighProcessMemory_Object = MibTableColumn
btmaHighProcessMemory = _BtmaHighProcessMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 11),
    _BtmaHighProcessMemory_Type()
)
btmaHighProcessMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighProcessMemory.setStatus("current")
_BtmaHighSystemMemory_Type = Gauge32
_BtmaHighSystemMemory_Object = MibTableColumn
btmaHighSystemMemory = _BtmaHighSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 12),
    _BtmaHighSystemMemory_Type()
)
btmaHighSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighSystemMemory.setStatus("current")
_BtmaHighThreadCount_Type = Gauge32
_BtmaHighThreadCount_Object = MibTableColumn
btmaHighThreadCount = _BtmaHighThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 13),
    _BtmaHighThreadCount_Type()
)
btmaHighThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaHighThreadCount.setStatus("current")
_BtmaInprocessMessageCount_Type = Gauge32
_BtmaInprocessMessageCount_Object = MibTableColumn
btmaInprocessMessageCount = _BtmaInprocessMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 14),
    _BtmaInprocessMessageCount_Type()
)
btmaInprocessMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaInprocessMessageCount.setStatus("current")
_BtmaInprocessMsgCountThreshold_Type = Gauge32
_BtmaInprocessMsgCountThreshold_Object = MibTableColumn
btmaInprocessMsgCountThreshold = _BtmaInprocessMsgCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 15),
    _BtmaInprocessMsgCountThreshold_Type()
)
btmaInprocessMsgCountThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaInprocessMsgCountThreshold.setStatus("current")
_BtmaMsgDeliveryDelayms_Type = Gauge32
_BtmaMsgDeliveryDelayms_Object = MibTableColumn
btmaMsgDeliveryDelayms = _BtmaMsgDeliveryDelayms_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 16),
    _BtmaMsgDeliveryDelayms_Type()
)
btmaMsgDeliveryDelayms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDeliveryDelayms.setStatus("current")
_BtmaMsgDeliveryIncomingRate_Type = Gauge32
_BtmaMsgDeliveryIncomingRate_Object = MibTableColumn
btmaMsgDeliveryIncomingRate = _BtmaMsgDeliveryIncomingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 17),
    _BtmaMsgDeliveryIncomingRate_Type()
)
btmaMsgDeliveryIncomingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDeliveryIncomingRate.setStatus("current")
_BtmaMsgDeliveryOutgoingRate_Type = Gauge32
_BtmaMsgDeliveryOutgoingRate_Object = MibTableColumn
btmaMsgDeliveryOutgoingRate = _BtmaMsgDeliveryOutgoingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 18),
    _BtmaMsgDeliveryOutgoingRate_Type()
)
btmaMsgDeliveryOutgoingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDeliveryOutgoingRate.setStatus("current")
_BtmaMsgDeliveryThrottlingState_Type = Gauge32
_BtmaMsgDeliveryThrottlingState_Object = MibTableColumn
btmaMsgDeliveryThrottlingState = _BtmaMsgDeliveryThrottlingState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 19),
    _BtmaMsgDeliveryThrottlingState_Type()
)
btmaMsgDeliveryThrottlingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDeliveryThrottlingState.setStatus("current")
_BtmaMsgDlvryThrottlingStDuration_Type = Gauge32
_BtmaMsgDlvryThrottlingStDuration_Object = MibTableColumn
btmaMsgDlvryThrottlingStDuration = _BtmaMsgDlvryThrottlingStDuration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 20),
    _BtmaMsgDlvryThrottlingStDuration_Type()
)
btmaMsgDlvryThrottlingStDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDlvryThrottlingStDuration.setStatus("current")
_BtmaMsgDlvryThrottleUserOverride_Type = Gauge32
_BtmaMsgDlvryThrottleUserOverride_Object = MibTableColumn
btmaMsgDlvryThrottleUserOverride = _BtmaMsgDlvryThrottleUserOverride_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 21),
    _BtmaMsgDlvryThrottleUserOverride_Type()
)
btmaMsgDlvryThrottleUserOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgDlvryThrottleUserOverride.setStatus("current")
_BtmaMsgPublishingDelay_Type = Gauge32
_BtmaMsgPublishingDelay_Object = MibTableColumn
btmaMsgPublishingDelay = _BtmaMsgPublishingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 22),
    _BtmaMsgPublishingDelay_Type()
)
btmaMsgPublishingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPublishingDelay.setStatus("current")
_BtmaMsgPublishingIncomingRate_Type = Gauge32
_BtmaMsgPublishingIncomingRate_Object = MibTableColumn
btmaMsgPublishingIncomingRate = _BtmaMsgPublishingIncomingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 23),
    _BtmaMsgPublishingIncomingRate_Type()
)
btmaMsgPublishingIncomingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPublishingIncomingRate.setStatus("current")
_BtmaMsgPublishingOutgoingRate_Type = Gauge32
_BtmaMsgPublishingOutgoingRate_Object = MibTableColumn
btmaMsgPublishingOutgoingRate = _BtmaMsgPublishingOutgoingRate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 24),
    _BtmaMsgPublishingOutgoingRate_Type()
)
btmaMsgPublishingOutgoingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPublishingOutgoingRate.setStatus("current")
_BtmaMsgPublishingThrottlingState_Type = Gauge32
_BtmaMsgPublishingThrottlingState_Object = MibTableColumn
btmaMsgPublishingThrottlingState = _BtmaMsgPublishingThrottlingState_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 25),
    _BtmaMsgPublishingThrottlingState_Type()
)
btmaMsgPublishingThrottlingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPublishingThrottlingState.setStatus("current")
_BtmaMsgPubThrottlingStDuration_Type = Gauge32
_BtmaMsgPubThrottlingStDuration_Object = MibTableColumn
btmaMsgPubThrottlingStDuration = _BtmaMsgPubThrottlingStDuration_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 26),
    _BtmaMsgPubThrottlingStDuration_Type()
)
btmaMsgPubThrottlingStDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPubThrottlingStDuration.setStatus("current")
_BtmaMsgPubThrottlingUsrOverride_Type = Gauge32
_BtmaMsgPubThrottlingUsrOverride_Object = MibTableColumn
btmaMsgPubThrottlingUsrOverride = _BtmaMsgPubThrottlingUsrOverride_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 27),
    _BtmaMsgPubThrottlingUsrOverride_Type()
)
btmaMsgPubThrottlingUsrOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaMsgPubThrottlingUsrOverride.setStatus("current")
_BtmaPhysicalMemoryUsageMB_Type = Gauge32
_BtmaPhysicalMemoryUsageMB_Object = MibTableColumn
btmaPhysicalMemoryUsageMB = _BtmaPhysicalMemoryUsageMB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 28),
    _BtmaPhysicalMemoryUsageMB_Type()
)
btmaPhysicalMemoryUsageMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaPhysicalMemoryUsageMB.setStatus("current")
_BtmaProcessMemoryUsageMB_Type = Gauge32
_BtmaProcessMemoryUsageMB_Object = MibTableColumn
btmaProcessMemoryUsageMB = _BtmaProcessMemoryUsageMB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 29),
    _BtmaProcessMemoryUsageMB_Type()
)
btmaProcessMemoryUsageMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaProcessMemoryUsageMB.setStatus("current")
_BtmaProcessMemUsageThresholdMB_Type = Gauge32
_BtmaProcessMemUsageThresholdMB_Object = MibTableColumn
btmaProcessMemUsageThresholdMB = _BtmaProcessMemUsageThresholdMB_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 30),
    _BtmaProcessMemUsageThresholdMB_Type()
)
btmaProcessMemUsageThresholdMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaProcessMemUsageThresholdMB.setStatus("current")
_BtmaServiceClassID_Type = Gauge32
_BtmaServiceClassID_Object = MibTableColumn
btmaServiceClassID = _BtmaServiceClassID_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 31),
    _BtmaServiceClassID_Type()
)
btmaServiceClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaServiceClassID.setStatus("current")
_BtmaThreadCount_Type = Gauge32
_BtmaThreadCount_Object = MibTableColumn
btmaThreadCount = _BtmaThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 32),
    _BtmaThreadCount_Type()
)
btmaThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaThreadCount.setStatus("current")
_BtmaThreadCountThreshold_Type = Gauge32
_BtmaThreadCountThreshold_Object = MibTableColumn
btmaThreadCountThreshold = _BtmaThreadCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 33),
    _BtmaThreadCountThreshold_Type()
)
btmaThreadCountThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaThreadCountThreshold.setStatus("current")
_BtmaTotalBatchesCommitted_Type = Gauge32
_BtmaTotalBatchesCommitted_Object = MibTableColumn
btmaTotalBatchesCommitted = _BtmaTotalBatchesCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 34),
    _BtmaTotalBatchesCommitted_Type()
)
btmaTotalBatchesCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaTotalBatchesCommitted.setStatus("current")
_BtmaTotalMessagesDelivered_Type = Gauge32
_BtmaTotalMessagesDelivered_Object = MibTableColumn
btmaTotalMessagesDelivered = _BtmaTotalMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 35),
    _BtmaTotalMessagesDelivered_Type()
)
btmaTotalMessagesDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaTotalMessagesDelivered.setStatus("current")
_BtmaTotalMessagesPublished_Type = Gauge32
_BtmaTotalMessagesPublished_Object = MibTableColumn
btmaTotalMessagesPublished = _BtmaTotalMessagesPublished_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 9, 1, 36),
    _BtmaTotalMessagesPublished_Type()
)
btmaTotalMessagesPublished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmaTotalMessagesPublished.setStatus("current")
_BizTalkMsgBoxGeneralCounterTable_Object = MibTable
bizTalkMsgBoxGeneralCounterTable = _BizTalkMsgBoxGeneralCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10)
)
if mibBuilder.loadTexts:
    bizTalkMsgBoxGeneralCounterTable.setStatus("current")
_BizTalkMsgBoxGeneralCounterEntry_Object = MibTableRow
bizTalkMsgBoxGeneralCounterEntry = _BizTalkMsgBoxGeneralCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1)
)
bizTalkMsgBoxGeneralCounterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmbgcInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMsgBoxGeneralCounterEntry.setStatus("current")
_BtmbgcInstance_Type = InstanceName
_BtmbgcInstance_Object = MibTableColumn
btmbgcInstance = _BtmbgcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 1),
    _BtmbgcInstance_Type()
)
btmbgcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcInstance.setStatus("current")
_BtmbgcInstancesTotalNumber_Type = Gauge32
_BtmbgcInstancesTotalNumber_Object = MibTableColumn
btmbgcInstancesTotalNumber = _BtmbgcInstancesTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 2),
    _BtmbgcInstancesTotalNumber_Type()
)
btmbgcInstancesTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcInstancesTotalNumber.setStatus("current")
_BtmbgcMsgBoxDeadProcCleanup_Type = Gauge32
_BtmbgcMsgBoxDeadProcCleanup_Object = MibTableColumn
btmbgcMsgBoxDeadProcCleanup = _BtmbgcMsgBoxDeadProcCleanup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 3),
    _BtmbgcMsgBoxDeadProcCleanup_Type()
)
btmbgcMsgBoxDeadProcCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcMsgBoxDeadProcCleanup.setStatus("current")
_BtmbgcMsgBoxMsgCleanupPurgeJobs_Type = Gauge32
_BtmbgcMsgBoxMsgCleanupPurgeJobs_Object = MibTableColumn
btmbgcMsgBoxMsgCleanupPurgeJobs = _BtmbgcMsgBoxMsgCleanupPurgeJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 4),
    _BtmbgcMsgBoxMsgCleanupPurgeJobs_Type()
)
btmbgcMsgBoxMsgCleanupPurgeJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcMsgBoxMsgCleanupPurgeJobs.setStatus("current")
_BtmbgcMsgBoxPartsCleanupPurgeJob_Type = Gauge32
_BtmbgcMsgBoxPartsCleanupPurgeJob_Object = MibTableColumn
btmbgcMsgBoxPartsCleanupPurgeJob = _BtmbgcMsgBoxPartsCleanupPurgeJob_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 5),
    _BtmbgcMsgBoxPartsCleanupPurgeJob_Type()
)
btmbgcMsgBoxPartsCleanupPurgeJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcMsgBoxPartsCleanupPurgeJob.setStatus("current")
_BtmbgcMsgBoxPurgeSubPurgeJobs_Type = Gauge32
_BtmbgcMsgBoxPurgeSubPurgeJobs_Object = MibTableColumn
btmbgcMsgBoxPurgeSubPurgeJobs = _BtmbgcMsgBoxPurgeSubPurgeJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 6),
    _BtmbgcMsgBoxPurgeSubPurgeJobs_Type()
)
btmbgcMsgBoxPurgeSubPurgeJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcMsgBoxPurgeSubPurgeJobs.setStatus("current")
_BtmbgcSpoolSize_Type = Gauge32
_BtmbgcSpoolSize_Object = MibTableColumn
btmbgcSpoolSize = _BtmbgcSpoolSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 7),
    _BtmbgcSpoolSize_Type()
)
btmbgcSpoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcSpoolSize.setStatus("current")
_BtmbgcTrackedMsgsCopyPurgeJobs_Type = Gauge32
_BtmbgcTrackedMsgsCopyPurgeJobs_Object = MibTableColumn
btmbgcTrackedMsgsCopyPurgeJobs = _BtmbgcTrackedMsgsCopyPurgeJobs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 8),
    _BtmbgcTrackedMsgsCopyPurgeJobs_Type()
)
btmbgcTrackedMsgsCopyPurgeJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcTrackedMsgsCopyPurgeJobs.setStatus("current")
_BtmbgcTrackingDataSize_Type = Gauge32
_BtmbgcTrackingDataSize_Object = MibTableColumn
btmbgcTrackingDataSize = _BtmbgcTrackingDataSize_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 9),
    _BtmbgcTrackingDataSize_Type()
)
btmbgcTrackingDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcTrackingDataSize.setStatus("current")
_BtmbgcTrackingSpoolCleanup_Type = Gauge32
_BtmbgcTrackingSpoolCleanup_Object = MibTableColumn
btmbgcTrackingSpoolCleanup = _BtmbgcTrackingSpoolCleanup_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 10, 1, 10),
    _BtmbgcTrackingSpoolCleanup_Type()
)
btmbgcTrackingSpoolCleanup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbgcTrackingSpoolCleanup.setStatus("current")
_BizTalkMsgBoxHostCountersTable_Object = MibTable
bizTalkMsgBoxHostCountersTable = _BizTalkMsgBoxHostCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11)
)
if mibBuilder.loadTexts:
    bizTalkMsgBoxHostCountersTable.setStatus("current")
_BizTalkMsgBoxHostCountersEntry_Object = MibTableRow
bizTalkMsgBoxHostCountersEntry = _BizTalkMsgBoxHostCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1)
)
bizTalkMsgBoxHostCountersEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmbhcInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMsgBoxHostCountersEntry.setStatus("current")
_BtmbhcInstance_Type = InstanceName
_BtmbhcInstance_Object = MibTableColumn
btmbhcInstance = _BtmbhcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1, 1),
    _BtmbhcInstance_Type()
)
btmbhcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbhcInstance.setStatus("current")
_BtmbhcHostQueInstStateMsgRefsLen_Type = Gauge32
_BtmbhcHostQueInstStateMsgRefsLen_Object = MibTableColumn
btmbhcHostQueInstStateMsgRefsLen = _BtmbhcHostQueInstStateMsgRefsLen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1, 2),
    _BtmbhcHostQueInstStateMsgRefsLen_Type()
)
btmbhcHostQueInstStateMsgRefsLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbhcHostQueInstStateMsgRefsLen.setStatus("current")
_BtmbhcHostQueueLength_Type = Gauge32
_BtmbhcHostQueueLength_Object = MibTableColumn
btmbhcHostQueueLength = _BtmbhcHostQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1, 3),
    _BtmbhcHostQueueLength_Type()
)
btmbhcHostQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbhcHostQueueLength.setStatus("current")
_BtmbhcHostQueueNumberOfInstances_Type = Gauge32
_BtmbhcHostQueueNumberOfInstances_Object = MibTableColumn
btmbhcHostQueueNumberOfInstances = _BtmbhcHostQueueNumberOfInstances_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1, 4),
    _BtmbhcHostQueueNumberOfInstances_Type()
)
btmbhcHostQueueNumberOfInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbhcHostQueueNumberOfInstances.setStatus("current")
_BtmbhcHostQueueSuspendedMsgsLen_Type = Gauge32
_BtmbhcHostQueueSuspendedMsgsLen_Object = MibTableColumn
btmbhcHostQueueSuspendedMsgsLen = _BtmbhcHostQueueSuspendedMsgsLen_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 11, 1, 5),
    _BtmbhcHostQueueSuspendedMsgsLen_Type()
)
btmbhcHostQueueSuspendedMsgsLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmbhcHostQueueSuspendedMsgsLen.setStatus("current")
_BizTalkMessagingTable_Object = MibTable
bizTalkMessagingTable = _BizTalkMessagingTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12)
)
if mibBuilder.loadTexts:
    bizTalkMessagingTable.setStatus("current")
_BizTalkMessagingEntry_Object = MibTableRow
bizTalkMessagingEntry = _BizTalkMessagingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1)
)
bizTalkMessagingEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMessagingEntry.setStatus("current")
_BtmInstance_Type = InstanceName
_BtmInstance_Object = MibTableColumn
btmInstance = _BtmInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 1),
    _BtmInstance_Type()
)
btmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmInstance.setStatus("current")
_BtmActiveReceiveLocations_Type = Gauge32
_BtmActiveReceiveLocations_Object = MibTableColumn
btmActiveReceiveLocations = _BtmActiveReceiveLocations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 2),
    _BtmActiveReceiveLocations_Type()
)
btmActiveReceiveLocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmActiveReceiveLocations.setStatus("current")
_BtmActiveReceiveThreads_Type = Gauge32
_BtmActiveReceiveThreads_Object = MibTableColumn
btmActiveReceiveThreads = _BtmActiveReceiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 3),
    _BtmActiveReceiveThreads_Type()
)
btmActiveReceiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmActiveReceiveThreads.setStatus("current")
_BtmActiveSendMessages_Type = Gauge32
_BtmActiveSendMessages_Object = MibTableColumn
btmActiveSendMessages = _BtmActiveSendMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 4),
    _BtmActiveSendMessages_Type()
)
btmActiveSendMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmActiveSendMessages.setStatus("current")
_BtmActiveSendThreads_Type = Gauge32
_BtmActiveSendThreads_Object = MibTableColumn
btmActiveSendThreads = _BtmActiveSendThreads_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 5),
    _BtmActiveSendThreads_Type()
)
btmActiveSendThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmActiveSendThreads.setStatus("current")
_BtmDocumentsProcessed_Type = Gauge32
_BtmDocumentsProcessed_Object = MibTableColumn
btmDocumentsProcessed = _BtmDocumentsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 6),
    _BtmDocumentsProcessed_Type()
)
btmDocumentsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsProcessed.setStatus("current")
_BtmDocumentsProcessedPerSec_Type = Gauge32
_BtmDocumentsProcessedPerSec_Object = MibTableColumn
btmDocumentsProcessedPerSec = _BtmDocumentsProcessedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 7),
    _BtmDocumentsProcessedPerSec_Type()
)
btmDocumentsProcessedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsProcessedPerSec.setStatus("current")
_BtmDocumentsReceived_Type = Gauge32
_BtmDocumentsReceived_Object = MibTableColumn
btmDocumentsReceived = _BtmDocumentsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 8),
    _BtmDocumentsReceived_Type()
)
btmDocumentsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsReceived.setStatus("current")
_BtmDocumentsReceivedPerSec_Type = Gauge32
_BtmDocumentsReceivedPerSec_Object = MibTableColumn
btmDocumentsReceivedPerSec = _BtmDocumentsReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 9),
    _BtmDocumentsReceivedPerSec_Type()
)
btmDocumentsReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsReceivedPerSec.setStatus("current")
_BtmDocumentsResubmitted_Type = Gauge32
_BtmDocumentsResubmitted_Object = MibTableColumn
btmDocumentsResubmitted = _BtmDocumentsResubmitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 10),
    _BtmDocumentsResubmitted_Type()
)
btmDocumentsResubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsResubmitted.setStatus("current")
_BtmDocumentsSubmittedPerBatch_Type = Gauge32
_BtmDocumentsSubmittedPerBatch_Object = MibTableColumn
btmDocumentsSubmittedPerBatch = _BtmDocumentsSubmittedPerBatch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 11),
    _BtmDocumentsSubmittedPerBatch_Type()
)
btmDocumentsSubmittedPerBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsSubmittedPerBatch.setStatus("current")
_BtmDocumentsSuspended_Type = Gauge32
_BtmDocumentsSuspended_Object = MibTableColumn
btmDocumentsSuspended = _BtmDocumentsSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 12),
    _BtmDocumentsSuspended_Type()
)
btmDocumentsSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsSuspended.setStatus("current")
_BtmDocumentsSuspendedPerSec_Type = Gauge32
_BtmDocumentsSuspendedPerSec_Object = MibTableColumn
btmDocumentsSuspendedPerSec = _BtmDocumentsSuspendedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 13),
    _BtmDocumentsSuspendedPerSec_Type()
)
btmDocumentsSuspendedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsSuspendedPerSec.setStatus("current")
_BtmDocumentsTransmittedPerBatch_Type = Gauge32
_BtmDocumentsTransmittedPerBatch_Object = MibTableColumn
btmDocumentsTransmittedPerBatch = _BtmDocumentsTransmittedPerBatch_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 14),
    _BtmDocumentsTransmittedPerBatch_Type()
)
btmDocumentsTransmittedPerBatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmDocumentsTransmittedPerBatch.setStatus("current")
_BtmIDProcess_Type = Gauge32
_BtmIDProcess_Object = MibTableColumn
btmIDProcess = _BtmIDProcess_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 15),
    _BtmIDProcess_Type()
)
btmIDProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmIDProcess.setStatus("current")
_BtmPendingReceiveBatches_Type = Gauge32
_BtmPendingReceiveBatches_Object = MibTableColumn
btmPendingReceiveBatches = _BtmPendingReceiveBatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 16),
    _BtmPendingReceiveBatches_Type()
)
btmPendingReceiveBatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmPendingReceiveBatches.setStatus("current")
_BtmPendingTransmittedMessages_Type = Gauge32
_BtmPendingTransmittedMessages_Object = MibTableColumn
btmPendingTransmittedMessages = _BtmPendingTransmittedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 17),
    _BtmPendingTransmittedMessages_Type()
)
btmPendingTransmittedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmPendingTransmittedMessages.setStatus("current")
_BtmRequestPerResponseTimeouts_Type = Gauge32
_BtmRequestPerResponseTimeouts_Object = MibTableColumn
btmRequestPerResponseTimeouts = _BtmRequestPerResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 18),
    _BtmRequestPerResponseTimeouts_Type()
)
btmRequestPerResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmRequestPerResponseTimeouts.setStatus("current")
_BtmThrottledReceiveBatches_Type = Gauge32
_BtmThrottledReceiveBatches_Object = MibTableColumn
btmThrottledReceiveBatches = _BtmThrottledReceiveBatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 12, 1, 19),
    _BtmThrottledReceiveBatches_Type()
)
btmThrottledReceiveBatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmThrottledReceiveBatches.setStatus("current")
_BizTalkMessagingLatencyTable_Object = MibTable
bizTalkMessagingLatencyTable = _BizTalkMessagingLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13)
)
if mibBuilder.loadTexts:
    bizTalkMessagingLatencyTable.setStatus("current")
_BizTalkMessagingLatencyEntry_Object = MibTableRow
bizTalkMessagingLatencyEntry = _BizTalkMessagingLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1)
)
bizTalkMessagingLatencyEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btmlInstance"),
)
if mibBuilder.loadTexts:
    bizTalkMessagingLatencyEntry.setStatus("current")
_BtmlInstance_Type = InstanceName
_BtmlInstance_Object = MibTableColumn
btmlInstance = _BtmlInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1, 1),
    _BtmlInstance_Type()
)
btmlInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmlInstance.setStatus("current")
_BtmlInboundLatencysec_Type = Gauge32
_BtmlInboundLatencysec_Object = MibTableColumn
btmlInboundLatencysec = _BtmlInboundLatencysec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1, 2),
    _BtmlInboundLatencysec_Type()
)
btmlInboundLatencysec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmlInboundLatencysec.setStatus("current")
_BtmlOutboundAdapterLatencysec_Type = Gauge32
_BtmlOutboundAdapterLatencysec_Object = MibTableColumn
btmlOutboundAdapterLatencysec = _BtmlOutboundAdapterLatencysec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1, 3),
    _BtmlOutboundAdapterLatencysec_Type()
)
btmlOutboundAdapterLatencysec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmlOutboundAdapterLatencysec.setStatus("current")
_BtmlOutboundLatencysec_Type = Gauge32
_BtmlOutboundLatencysec_Object = MibTableColumn
btmlOutboundLatencysec = _BtmlOutboundLatencysec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1, 4),
    _BtmlOutboundLatencysec_Type()
)
btmlOutboundLatencysec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmlOutboundLatencysec.setStatus("current")
_BtmlRequestResponseLatencysec_Type = Gauge32
_BtmlRequestResponseLatencysec_Object = MibTableColumn
btmlRequestResponseLatencysec = _BtmlRequestResponseLatencysec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 13, 1, 5),
    _BtmlRequestResponseLatencysec_Type()
)
btmlRequestResponseLatencysec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btmlRequestResponseLatencysec.setStatus("current")
_BizTalkPOP3ReceiveAdapterTable_Object = MibTable
bizTalkPOP3ReceiveAdapterTable = _BizTalkPOP3ReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14)
)
if mibBuilder.loadTexts:
    bizTalkPOP3ReceiveAdapterTable.setStatus("current")
_BizTalkPOP3ReceiveAdapterEntry_Object = MibTableRow
bizTalkPOP3ReceiveAdapterEntry = _BizTalkPOP3ReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1)
)
bizTalkPOP3ReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btpopraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkPOP3ReceiveAdapterEntry.setStatus("current")
_BtpopraInstance_Type = InstanceName
_BtpopraInstance_Object = MibTableColumn
btpopraInstance = _BtpopraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 1),
    _BtpopraInstance_Type()
)
btpopraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraInstance.setStatus("current")
_BtpopraActiveSessions_Type = Gauge32
_BtpopraActiveSessions_Object = MibTableColumn
btpopraActiveSessions = _BtpopraActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 2),
    _BtpopraActiveSessions_Type()
)
btpopraActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraActiveSessions.setStatus("current")
_BtpopraBytesReceived_Type = Gauge32
_BtpopraBytesReceived_Object = MibTableColumn
btpopraBytesReceived = _BtpopraBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 3),
    _BtpopraBytesReceived_Type()
)
btpopraBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraBytesReceived.setStatus("current")
_BtpopraBytesReceivedPerSec_Type = Gauge32
_BtpopraBytesReceivedPerSec_Object = MibTableColumn
btpopraBytesReceivedPerSec = _BtpopraBytesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 4),
    _BtpopraBytesReceivedPerSec_Type()
)
btpopraBytesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraBytesReceivedPerSec.setStatus("current")
_BtpopraMessagesReceived_Type = Gauge32
_BtpopraMessagesReceived_Object = MibTableColumn
btpopraMessagesReceived = _BtpopraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 5),
    _BtpopraMessagesReceived_Type()
)
btpopraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraMessagesReceived.setStatus("current")
_BtpopraMessagesReceivedPerSec_Type = Gauge32
_BtpopraMessagesReceivedPerSec_Object = MibTableColumn
btpopraMessagesReceivedPerSec = _BtpopraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 14, 1, 6),
    _BtpopraMessagesReceivedPerSec_Type()
)
btpopraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btpopraMessagesReceivedPerSec.setStatus("current")
_BizTalkSMTPSendAdapterTable_Object = MibTable
bizTalkSMTPSendAdapterTable = _BizTalkSMTPSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 15)
)
if mibBuilder.loadTexts:
    bizTalkSMTPSendAdapterTable.setStatus("current")
_BizTalkSMTPSendAdapterEntry_Object = MibTableRow
bizTalkSMTPSendAdapterEntry = _BizTalkSMTPSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 15, 1)
)
bizTalkSMTPSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btsmtpsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkSMTPSendAdapterEntry.setStatus("current")
_BtsmtpsaInstance_Type = InstanceName
_BtsmtpsaInstance_Object = MibTableColumn
btsmtpsaInstance = _BtsmtpsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 15, 1, 1),
    _BtsmtpsaInstance_Type()
)
btsmtpsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsmtpsaInstance.setStatus("current")
_BtsmtpsaMessagesSent_Type = Gauge32
_BtsmtpsaMessagesSent_Object = MibTableColumn
btsmtpsaMessagesSent = _BtsmtpsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 15, 1, 2),
    _BtsmtpsaMessagesSent_Type()
)
btsmtpsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsmtpsaMessagesSent.setStatus("current")
_BtsmtpsaMessagesSentPerSec_Type = Gauge32
_BtsmtpsaMessagesSentPerSec_Object = MibTableColumn
btsmtpsaMessagesSentPerSec = _BtsmtpsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 15, 1, 3),
    _BtsmtpsaMessagesSentPerSec_Type()
)
btsmtpsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsmtpsaMessagesSentPerSec.setStatus("current")
_BizTalkSOAPReceiveAdapterTable_Object = MibTable
bizTalkSOAPReceiveAdapterTable = _BizTalkSOAPReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 16)
)
if mibBuilder.loadTexts:
    bizTalkSOAPReceiveAdapterTable.setStatus("current")
_BizTalkSOAPReceiveAdapterEntry_Object = MibTableRow
bizTalkSOAPReceiveAdapterEntry = _BizTalkSOAPReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 16, 1)
)
bizTalkSOAPReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btsoapraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkSOAPReceiveAdapterEntry.setStatus("current")
_BtsoapraInstance_Type = InstanceName
_BtsoapraInstance_Object = MibTableColumn
btsoapraInstance = _BtsoapraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 16, 1, 1),
    _BtsoapraInstance_Type()
)
btsoapraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapraInstance.setStatus("current")
_BtsoapraMessagesReceived_Type = Gauge32
_BtsoapraMessagesReceived_Object = MibTableColumn
btsoapraMessagesReceived = _BtsoapraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 16, 1, 2),
    _BtsoapraMessagesReceived_Type()
)
btsoapraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapraMessagesReceived.setStatus("current")
_BtsoapraMessagesReceivedPerSec_Type = Gauge32
_BtsoapraMessagesReceivedPerSec_Object = MibTableColumn
btsoapraMessagesReceivedPerSec = _BtsoapraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 16, 1, 3),
    _BtsoapraMessagesReceivedPerSec_Type()
)
btsoapraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapraMessagesReceivedPerSec.setStatus("current")
_BizTalkSOAPSendAdapterTable_Object = MibTable
bizTalkSOAPSendAdapterTable = _BizTalkSOAPSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 17)
)
if mibBuilder.loadTexts:
    bizTalkSOAPSendAdapterTable.setStatus("current")
_BizTalkSOAPSendAdapterEntry_Object = MibTableRow
bizTalkSOAPSendAdapterEntry = _BizTalkSOAPSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 17, 1)
)
bizTalkSOAPSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btsoapsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkSOAPSendAdapterEntry.setStatus("current")
_BtsoapsaInstance_Type = InstanceName
_BtsoapsaInstance_Object = MibTableColumn
btsoapsaInstance = _BtsoapsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 17, 1, 1),
    _BtsoapsaInstance_Type()
)
btsoapsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapsaInstance.setStatus("current")
_BtsoapsaMessagesSent_Type = Gauge32
_BtsoapsaMessagesSent_Object = MibTableColumn
btsoapsaMessagesSent = _BtsoapsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 17, 1, 2),
    _BtsoapsaMessagesSent_Type()
)
btsoapsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapsaMessagesSent.setStatus("current")
_BtsoapsaMessagesSentPerSec_Type = Gauge32
_BtsoapsaMessagesSentPerSec_Object = MibTableColumn
btsoapsaMessagesSentPerSec = _BtsoapsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 17, 1, 3),
    _BtsoapsaMessagesSentPerSec_Type()
)
btsoapsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsoapsaMessagesSentPerSec.setStatus("current")
_BizTalkSQLReceiveAdapterTable_Object = MibTable
bizTalkSQLReceiveAdapterTable = _BizTalkSQLReceiveAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 18)
)
if mibBuilder.loadTexts:
    bizTalkSQLReceiveAdapterTable.setStatus("current")
_BizTalkSQLReceiveAdapterEntry_Object = MibTableRow
bizTalkSQLReceiveAdapterEntry = _BizTalkSQLReceiveAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 18, 1)
)
bizTalkSQLReceiveAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btsqlraInstance"),
)
if mibBuilder.loadTexts:
    bizTalkSQLReceiveAdapterEntry.setStatus("current")
_BtsqlraInstance_Type = InstanceName
_BtsqlraInstance_Object = MibTableColumn
btsqlraInstance = _BtsqlraInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 18, 1, 1),
    _BtsqlraInstance_Type()
)
btsqlraInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlraInstance.setStatus("current")
_BtsqlraMessagesReceived_Type = Gauge32
_BtsqlraMessagesReceived_Object = MibTableColumn
btsqlraMessagesReceived = _BtsqlraMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 18, 1, 2),
    _BtsqlraMessagesReceived_Type()
)
btsqlraMessagesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlraMessagesReceived.setStatus("current")
_BtsqlraMessagesReceivedPerSec_Type = Gauge32
_BtsqlraMessagesReceivedPerSec_Object = MibTableColumn
btsqlraMessagesReceivedPerSec = _BtsqlraMessagesReceivedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 18, 1, 3),
    _BtsqlraMessagesReceivedPerSec_Type()
)
btsqlraMessagesReceivedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlraMessagesReceivedPerSec.setStatus("current")
_BizTalkSQLSendAdapterTable_Object = MibTable
bizTalkSQLSendAdapterTable = _BizTalkSQLSendAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 19)
)
if mibBuilder.loadTexts:
    bizTalkSQLSendAdapterTable.setStatus("current")
_BizTalkSQLSendAdapterEntry_Object = MibTableRow
bizTalkSQLSendAdapterEntry = _BizTalkSQLSendAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 19, 1)
)
bizTalkSQLSendAdapterEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btsqlsaInstance"),
)
if mibBuilder.loadTexts:
    bizTalkSQLSendAdapterEntry.setStatus("current")
_BtsqlsaInstance_Type = InstanceName
_BtsqlsaInstance_Object = MibTableColumn
btsqlsaInstance = _BtsqlsaInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 19, 1, 1),
    _BtsqlsaInstance_Type()
)
btsqlsaInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlsaInstance.setStatus("current")
_BtsqlsaMessagesSent_Type = Gauge32
_BtsqlsaMessagesSent_Object = MibTableColumn
btsqlsaMessagesSent = _BtsqlsaMessagesSent_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 19, 1, 2),
    _BtsqlsaMessagesSent_Type()
)
btsqlsaMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlsaMessagesSent.setStatus("current")
_BtsqlsaMessagesSentPerSec_Type = Gauge32
_BtsqlsaMessagesSentPerSec_Object = MibTableColumn
btsqlsaMessagesSentPerSec = _BtsqlsaMessagesSentPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 19, 1, 3),
    _BtsqlsaMessagesSentPerSec_Type()
)
btsqlsaMessagesSentPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btsqlsaMessagesSentPerSec.setStatus("current")
_BizTalkTDDSTable_Object = MibTable
bizTalkTDDSTable = _BizTalkTDDSTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20)
)
if mibBuilder.loadTexts:
    bizTalkTDDSTable.setStatus("current")
_BizTalkTDDSEntry_Object = MibTableRow
bizTalkTDDSEntry = _BizTalkTDDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1)
)
bizTalkTDDSEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "bttddsInstance"),
)
if mibBuilder.loadTexts:
    bizTalkTDDSEntry.setStatus("current")
_BttddsInstance_Type = InstanceName
_BttddsInstance_Object = MibTableColumn
bttddsInstance = _BttddsInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 1),
    _BttddsInstance_Type()
)
bttddsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsInstance.setStatus("current")
_BttddsBatchesCommitted_Type = Gauge32
_BttddsBatchesCommitted_Object = MibTableColumn
bttddsBatchesCommitted = _BttddsBatchesCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 2),
    _BttddsBatchesCommitted_Type()
)
bttddsBatchesCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsBatchesCommitted.setStatus("current")
_BttddsBatchesBeingProcessed_Type = Gauge32
_BttddsBatchesBeingProcessed_Object = MibTableColumn
bttddsBatchesBeingProcessed = _BttddsBatchesBeingProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 3),
    _BttddsBatchesBeingProcessed_Type()
)
bttddsBatchesBeingProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsBatchesBeingProcessed.setStatus("current")
_BttddsEventsCommitted_Type = Gauge32
_BttddsEventsCommitted_Object = MibTableColumn
bttddsEventsCommitted = _BttddsEventsCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 4),
    _BttddsEventsCommitted_Type()
)
bttddsEventsCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsEventsCommitted.setStatus("current")
_BttddsEventsBeingProcessed_Type = Gauge32
_BttddsEventsBeingProcessed_Object = MibTableColumn
bttddsEventsBeingProcessed = _BttddsEventsBeingProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 5),
    _BttddsEventsBeingProcessed_Type()
)
bttddsEventsBeingProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsEventsBeingProcessed.setStatus("current")
_BttddsRecordsCommitted_Type = Gauge32
_BttddsRecordsCommitted_Object = MibTableColumn
bttddsRecordsCommitted = _BttddsRecordsCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 6),
    _BttddsRecordsCommitted_Type()
)
bttddsRecordsCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsRecordsCommitted.setStatus("current")
_BttddsRecordsBeingProcessed_Type = Gauge32
_BttddsRecordsBeingProcessed_Object = MibTableColumn
bttddsRecordsBeingProcessed = _BttddsRecordsBeingProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 7),
    _BttddsRecordsBeingProcessed_Type()
)
bttddsRecordsBeingProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsRecordsBeingProcessed.setStatus("current")
_BttddsTotalBatches_Type = Gauge32
_BttddsTotalBatches_Object = MibTableColumn
bttddsTotalBatches = _BttddsTotalBatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 8),
    _BttddsTotalBatches_Type()
)
bttddsTotalBatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsTotalBatches.setStatus("current")
_BttddsTotalEvents_Type = Gauge32
_BttddsTotalEvents_Object = MibTableColumn
bttddsTotalEvents = _BttddsTotalEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 9),
    _BttddsTotalEvents_Type()
)
bttddsTotalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsTotalEvents.setStatus("current")
_BttddsTotalFailedBatches_Type = Gauge32
_BttddsTotalFailedBatches_Object = MibTableColumn
bttddsTotalFailedBatches = _BttddsTotalFailedBatches_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 10),
    _BttddsTotalFailedBatches_Type()
)
bttddsTotalFailedBatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsTotalFailedBatches.setStatus("current")
_BttddsTotalFailedEvents_Type = Gauge32
_BttddsTotalFailedEvents_Object = MibTableColumn
bttddsTotalFailedEvents = _BttddsTotalFailedEvents_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 11),
    _BttddsTotalFailedEvents_Type()
)
bttddsTotalFailedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsTotalFailedEvents.setStatus("current")
_BttddsTotalRecords_Type = Gauge32
_BttddsTotalRecords_Object = MibTableColumn
bttddsTotalRecords = _BttddsTotalRecords_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 20, 1, 12),
    _BttddsTotalRecords_Type()
)
bttddsTotalRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bttddsTotalRecords.setStatus("current")
_BizTalkSharePointServicesAdapter_ObjectIdentity = ObjectIdentity
bizTalkSharePointServicesAdapter = _BizTalkSharePointServicesAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21)
)
_BtwspsaPercentReceiveMsgFailures_Type = Gauge32
_BtwspsaPercentReceiveMsgFailures_Object = MibScalar
btwspsaPercentReceiveMsgFailures = _BtwspsaPercentReceiveMsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 1),
    _BtwspsaPercentReceiveMsgFailures_Type()
)
btwspsaPercentReceiveMsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaPercentReceiveMsgFailures.setStatus("current")
_BtwspsaPercentSendMsgFailures_Type = Gauge32
_BtwspsaPercentSendMsgFailures_Object = MibScalar
btwspsaPercentSendMsgFailures = _BtwspsaPercentSendMsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 2),
    _BtwspsaPercentSendMsgFailures_Type()
)
btwspsaPercentSendMsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaPercentSendMsgFailures.setStatus("current")
_BtwspsaPercentWebServiceCallFail_Type = Gauge32
_BtwspsaPercentWebServiceCallFail_Object = MibScalar
btwspsaPercentWebServiceCallFail = _BtwspsaPercentWebServiceCallFail_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 3),
    _BtwspsaPercentWebServiceCallFail_Type()
)
btwspsaPercentWebServiceCallFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaPercentWebServiceCallFail.setStatus("current")
_BtwspsaTotalReceiveCommitFailure_Type = Gauge32
_BtwspsaTotalReceiveCommitFailure_Object = MibScalar
btwspsaTotalReceiveCommitFailure = _BtwspsaTotalReceiveCommitFailure_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 4),
    _BtwspsaTotalReceiveCommitFailure_Type()
)
btwspsaTotalReceiveCommitFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalReceiveCommitFailure.setStatus("current")
_BtwspsaTotalReceiveMsgFailures_Type = Gauge32
_BtwspsaTotalReceiveMsgFailures_Object = MibScalar
btwspsaTotalReceiveMsgFailures = _BtwspsaTotalReceiveMsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 5),
    _BtwspsaTotalReceiveMsgFailures_Type()
)
btwspsaTotalReceiveMsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalReceiveMsgFailures.setStatus("current")
_BtwspsaTotalReceivedMsgs_Type = Gauge32
_BtwspsaTotalReceivedMsgs_Object = MibScalar
btwspsaTotalReceivedMsgs = _BtwspsaTotalReceivedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 6),
    _BtwspsaTotalReceivedMsgs_Type()
)
btwspsaTotalReceivedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalReceivedMsgs.setStatus("current")
_BtwspsaTotalSendMsgFailures_Type = Gauge32
_BtwspsaTotalSendMsgFailures_Object = MibScalar
btwspsaTotalSendMsgFailures = _BtwspsaTotalSendMsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 7),
    _BtwspsaTotalSendMsgFailures_Type()
)
btwspsaTotalSendMsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalSendMsgFailures.setStatus("current")
_BtwspsaTotalSentMsgs_Type = Gauge32
_BtwspsaTotalSentMsgs_Object = MibScalar
btwspsaTotalSentMsgs = _BtwspsaTotalSentMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 8),
    _BtwspsaTotalSentMsgs_Type()
)
btwspsaTotalSentMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalSentMsgs.setStatus("current")
_BtwspsaTotalWebServiceCallFail_Type = Gauge32
_BtwspsaTotalWebServiceCallFail_Object = MibScalar
btwspsaTotalWebServiceCallFail = _BtwspsaTotalWebServiceCallFail_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 9),
    _BtwspsaTotalWebServiceCallFail_Type()
)
btwspsaTotalWebServiceCallFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaTotalWebServiceCallFail.setStatus("current")
_BtwspsaWebServiceCallsPerSecond_Type = Gauge32
_BtwspsaWebServiceCallsPerSecond_Object = MibScalar
btwspsaWebServiceCallsPerSecond = _BtwspsaWebServiceCallsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 21, 10),
    _BtwspsaWebServiceCallsPerSecond_Type()
)
btwspsaWebServiceCallsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btwspsaWebServiceCallsPerSecond.setStatus("current")
_XLANGPerSOrchestrationsTable_Object = MibTable
xLANGPerSOrchestrationsTable = _XLANGPerSOrchestrationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22)
)
if mibBuilder.loadTexts:
    xLANGPerSOrchestrationsTable.setStatus("current")
_XLANGPerSOrchestrationsEntry_Object = MibTableRow
xLANGPerSOrchestrationsEntry = _XLANGPerSOrchestrationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1)
)
xLANGPerSOrchestrationsEntry.setIndexNames(
    (0, "INFORMANT-BIZTALK", "btoInstance"),
)
if mibBuilder.loadTexts:
    xLANGPerSOrchestrationsEntry.setStatus("current")
_BtoInstance_Type = InstanceName
_BtoInstance_Object = MibTableColumn
btoInstance = _BtoInstance_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 1),
    _BtoInstance_Type()
)
btoInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoInstance.setStatus("current")
_BtoPercentUsedPhysicalMemory_Type = Gauge32
_BtoPercentUsedPhysicalMemory_Object = MibTableColumn
btoPercentUsedPhysicalMemory = _BtoPercentUsedPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 2),
    _BtoPercentUsedPhysicalMemory_Type()
)
btoPercentUsedPhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoPercentUsedPhysicalMemory.setStatus("current")
_BtoActiveApplicationDomains_Type = Gauge32
_BtoActiveApplicationDomains_Object = MibTableColumn
btoActiveApplicationDomains = _BtoActiveApplicationDomains_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 3),
    _BtoActiveApplicationDomains_Type()
)
btoActiveApplicationDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoActiveApplicationDomains.setStatus("current")
_BtoAverageBatchFactor_Type = Gauge32
_BtoAverageBatchFactor_Object = MibTableColumn
btoAverageBatchFactor = _BtoAverageBatchFactor_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 4),
    _BtoAverageBatchFactor_Type()
)
btoAverageBatchFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoAverageBatchFactor.setStatus("current")
_BtoDatabaseTransactions_Type = Gauge32
_BtoDatabaseTransactions_Object = MibTableColumn
btoDatabaseTransactions = _BtoDatabaseTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 5),
    _BtoDatabaseTransactions_Type()
)
btoDatabaseTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDatabaseTransactions.setStatus("current")
_BtoDatabaseTransactionsPerSec_Type = Gauge32
_BtoDatabaseTransactionsPerSec_Object = MibTableColumn
btoDatabaseTransactionsPerSec = _BtoDatabaseTransactionsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 6),
    _BtoDatabaseTransactionsPerSec_Type()
)
btoDatabaseTransactionsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDatabaseTransactionsPerSec.setStatus("current")
_BtoDehydratableOrchestrations_Type = Gauge32
_BtoDehydratableOrchestrations_Object = MibTableColumn
btoDehydratableOrchestrations = _BtoDehydratableOrchestrations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 7),
    _BtoDehydratableOrchestrations_Type()
)
btoDehydratableOrchestrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDehydratableOrchestrations.setStatus("current")
_BtoDehydratingOrchestrations_Type = Gauge32
_BtoDehydratingOrchestrations_Object = MibTableColumn
btoDehydratingOrchestrations = _BtoDehydratingOrchestrations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 8),
    _BtoDehydratingOrchestrations_Type()
)
btoDehydratingOrchestrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDehydratingOrchestrations.setStatus("current")
_BtoDehydrationCycleInProgress_Type = Gauge32
_BtoDehydrationCycleInProgress_Object = MibTableColumn
btoDehydrationCycleInProgress = _BtoDehydrationCycleInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 9),
    _BtoDehydrationCycleInProgress_Type()
)
btoDehydrationCycleInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDehydrationCycleInProgress.setStatus("current")
_BtoDehydrationCycles_Type = Gauge32
_BtoDehydrationCycles_Object = MibTableColumn
btoDehydrationCycles = _BtoDehydrationCycles_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 10),
    _BtoDehydrationCycles_Type()
)
btoDehydrationCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDehydrationCycles.setStatus("current")
_BtoDehydrationThreshold_Type = Gauge32
_BtoDehydrationThreshold_Object = MibTableColumn
btoDehydrationThreshold = _BtoDehydrationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 11),
    _BtoDehydrationThreshold_Type()
)
btoDehydrationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoDehydrationThreshold.setStatus("current")
_BtoIdleOrchestrations_Type = Gauge32
_BtoIdleOrchestrations_Object = MibTableColumn
btoIdleOrchestrations = _BtoIdleOrchestrations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 12),
    _BtoIdleOrchestrations_Type()
)
btoIdleOrchestrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoIdleOrchestrations.setStatus("current")
_BtoMBAllocatedPrivateMemory_Type = Gauge32
_BtoMBAllocatedPrivateMemory_Object = MibTableColumn
btoMBAllocatedPrivateMemory = _BtoMBAllocatedPrivateMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 13),
    _BtoMBAllocatedPrivateMemory_Type()
)
btoMBAllocatedPrivateMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoMBAllocatedPrivateMemory.setStatus("current")
_BtoMBAllocatedVirtualMemory_Type = Gauge32
_BtoMBAllocatedVirtualMemory_Object = MibTableColumn
btoMBAllocatedVirtualMemory = _BtoMBAllocatedVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 14),
    _BtoMBAllocatedVirtualMemory_Type()
)
btoMBAllocatedVirtualMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoMBAllocatedVirtualMemory.setStatus("current")
_BtoMsgBoxDBConnectionFailures_Type = Gauge32
_BtoMsgBoxDBConnectionFailures_Object = MibTableColumn
btoMsgBoxDBConnectionFailures = _BtoMsgBoxDBConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 15),
    _BtoMsgBoxDBConnectionFailures_Type()
)
btoMsgBoxDBConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoMsgBoxDBConnectionFailures.setStatus("current")
_BtoOnlineMessageBoxDatabases_Type = Gauge32
_BtoOnlineMessageBoxDatabases_Object = MibTableColumn
btoOnlineMessageBoxDatabases = _BtoOnlineMessageBoxDatabases_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 16),
    _BtoOnlineMessageBoxDatabases_Type()
)
btoOnlineMessageBoxDatabases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOnlineMessageBoxDatabases.setStatus("current")
_BtoOrchestrationsCompleted_Type = Gauge32
_BtoOrchestrationsCompleted_Object = MibTableColumn
btoOrchestrationsCompleted = _BtoOrchestrationsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 17),
    _BtoOrchestrationsCompleted_Type()
)
btoOrchestrationsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsCompleted.setStatus("current")
_BtoOrchestrationsCompletedPerSec_Type = Gauge32
_BtoOrchestrationsCompletedPerSec_Object = MibTableColumn
btoOrchestrationsCompletedPerSec = _BtoOrchestrationsCompletedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 18),
    _BtoOrchestrationsCompletedPerSec_Type()
)
btoOrchestrationsCompletedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsCompletedPerSec.setStatus("current")
_BtoOrchestrationsCreated_Type = Gauge32
_BtoOrchestrationsCreated_Object = MibTableColumn
btoOrchestrationsCreated = _BtoOrchestrationsCreated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 19),
    _BtoOrchestrationsCreated_Type()
)
btoOrchestrationsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsCreated.setStatus("current")
_BtoOrchestrationsCreatedPerSec_Type = Gauge32
_BtoOrchestrationsCreatedPerSec_Object = MibTableColumn
btoOrchestrationsCreatedPerSec = _BtoOrchestrationsCreatedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 20),
    _BtoOrchestrationsCreatedPerSec_Type()
)
btoOrchestrationsCreatedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsCreatedPerSec.setStatus("current")
_BtoOrchestrationsDehydrated_Type = Gauge32
_BtoOrchestrationsDehydrated_Object = MibTableColumn
btoOrchestrationsDehydrated = _BtoOrchestrationsDehydrated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 21),
    _BtoOrchestrationsDehydrated_Type()
)
btoOrchestrationsDehydrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsDehydrated.setStatus("current")
_BtoOrchestrationDehydratedPerSec_Type = Gauge32
_BtoOrchestrationDehydratedPerSec_Object = MibTableColumn
btoOrchestrationDehydratedPerSec = _BtoOrchestrationDehydratedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 22),
    _BtoOrchestrationDehydratedPerSec_Type()
)
btoOrchestrationDehydratedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationDehydratedPerSec.setStatus("current")
_BtoOrchestrationsDiscarded_Type = Gauge32
_BtoOrchestrationsDiscarded_Object = MibTableColumn
btoOrchestrationsDiscarded = _BtoOrchestrationsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 23),
    _BtoOrchestrationsDiscarded_Type()
)
btoOrchestrationsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsDiscarded.setStatus("current")
_BtoOrchestrationsDiscardedPerSec_Type = Gauge32
_BtoOrchestrationsDiscardedPerSec_Object = MibTableColumn
btoOrchestrationsDiscardedPerSec = _BtoOrchestrationsDiscardedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 24),
    _BtoOrchestrationsDiscardedPerSec_Type()
)
btoOrchestrationsDiscardedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsDiscardedPerSec.setStatus("current")
_BtoOrchestrationsRehydrated_Type = Gauge32
_BtoOrchestrationsRehydrated_Object = MibTableColumn
btoOrchestrationsRehydrated = _BtoOrchestrationsRehydrated_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 25),
    _BtoOrchestrationsRehydrated_Type()
)
btoOrchestrationsRehydrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsRehydrated.setStatus("current")
_BtoOrchestrationRehydratedPerSec_Type = Gauge32
_BtoOrchestrationRehydratedPerSec_Object = MibTableColumn
btoOrchestrationRehydratedPerSec = _BtoOrchestrationRehydratedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 26),
    _BtoOrchestrationRehydratedPerSec_Type()
)
btoOrchestrationRehydratedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationRehydratedPerSec.setStatus("current")
_BtoOrchestrationResidentInmemory_Type = Gauge32
_BtoOrchestrationResidentInmemory_Object = MibTableColumn
btoOrchestrationResidentInmemory = _BtoOrchestrationResidentInmemory_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 27),
    _BtoOrchestrationResidentInmemory_Type()
)
btoOrchestrationResidentInmemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationResidentInmemory.setStatus("current")
_BtoOrchestrationsSchedForDehyd_Type = Gauge32
_BtoOrchestrationsSchedForDehyd_Object = MibTableColumn
btoOrchestrationsSchedForDehyd = _BtoOrchestrationsSchedForDehyd_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 28),
    _BtoOrchestrationsSchedForDehyd_Type()
)
btoOrchestrationsSchedForDehyd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsSchedForDehyd.setStatus("current")
_BtoOrchestrationsSuspended_Type = Gauge32
_BtoOrchestrationsSuspended_Object = MibTableColumn
btoOrchestrationsSuspended = _BtoOrchestrationsSuspended_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 29),
    _BtoOrchestrationsSuspended_Type()
)
btoOrchestrationsSuspended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsSuspended.setStatus("current")
_BtoOrchestrationsSuspendedPerSec_Type = Gauge32
_BtoOrchestrationsSuspendedPerSec_Object = MibTableColumn
btoOrchestrationsSuspendedPerSec = _BtoOrchestrationsSuspendedPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 30),
    _BtoOrchestrationsSuspendedPerSec_Type()
)
btoOrchestrationsSuspendedPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoOrchestrationsSuspendedPerSec.setStatus("current")
_BtoPendingMessages_Type = Gauge32
_BtoPendingMessages_Object = MibTableColumn
btoPendingMessages = _BtoPendingMessages_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 31),
    _BtoPendingMessages_Type()
)
btoPendingMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoPendingMessages.setStatus("current")
_BtoPendingWorkItems_Type = Gauge32
_BtoPendingWorkItems_Object = MibTableColumn
btoPendingWorkItems = _BtoPendingWorkItems_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 32),
    _BtoPendingWorkItems_Type()
)
btoPendingWorkItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoPendingWorkItems.setStatus("current")
_BtoPersistencePoints_Type = Gauge32
_BtoPersistencePoints_Object = MibTableColumn
btoPersistencePoints = _BtoPersistencePoints_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 33),
    _BtoPersistencePoints_Type()
)
btoPersistencePoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoPersistencePoints.setStatus("current")
_BtoPersistencePointsPerSec_Type = Gauge32
_BtoPersistencePointsPerSec_Object = MibTableColumn
btoPersistencePointsPerSec = _BtoPersistencePointsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 34),
    _BtoPersistencePointsPerSec_Type()
)
btoPersistencePointsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoPersistencePointsPerSec.setStatus("current")
_BtoRunnableOrchestrations_Type = Gauge32
_BtoRunnableOrchestrations_Object = MibTableColumn
btoRunnableOrchestrations = _BtoRunnableOrchestrations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 35),
    _BtoRunnableOrchestrations_Type()
)
btoRunnableOrchestrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoRunnableOrchestrations.setStatus("current")
_BtoRunningOrchestrations_Type = Gauge32
_BtoRunningOrchestrations_Object = MibTableColumn
btoRunningOrchestrations = _BtoRunningOrchestrations_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 36),
    _BtoRunningOrchestrations_Type()
)
btoRunningOrchestrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoRunningOrchestrations.setStatus("current")
_BtoTransactionalScopesAborted_Type = Gauge32
_BtoTransactionalScopesAborted_Object = MibTableColumn
btoTransactionalScopesAborted = _BtoTransactionalScopesAborted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 37),
    _BtoTransactionalScopesAborted_Type()
)
btoTransactionalScopesAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransactionalScopesAborted.setStatus("current")
_BtoTransactionalScopeAbortPerSec_Type = Gauge32
_BtoTransactionalScopeAbortPerSec_Object = MibTableColumn
btoTransactionalScopeAbortPerSec = _BtoTransactionalScopeAbortPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 38),
    _BtoTransactionalScopeAbortPerSec_Type()
)
btoTransactionalScopeAbortPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransactionalScopeAbortPerSec.setStatus("current")
_BtoTransactionalScopesCommitted_Type = Gauge32
_BtoTransactionalScopesCommitted_Object = MibTableColumn
btoTransactionalScopesCommitted = _BtoTransactionalScopesCommitted_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 39),
    _BtoTransactionalScopesCommitted_Type()
)
btoTransactionalScopesCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransactionalScopesCommitted.setStatus("current")
_BtoTransactionScopeCommitPerSec_Type = Gauge32
_BtoTransactionScopeCommitPerSec_Object = MibTableColumn
btoTransactionScopeCommitPerSec = _BtoTransactionScopeCommitPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 40),
    _BtoTransactionScopeCommitPerSec_Type()
)
btoTransactionScopeCommitPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransactionScopeCommitPerSec.setStatus("current")
_BtoTransactionalScopesCompensate_Type = Gauge32
_BtoTransactionalScopesCompensate_Object = MibTableColumn
btoTransactionalScopesCompensate = _BtoTransactionalScopesCompensate_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 41),
    _BtoTransactionalScopesCompensate_Type()
)
btoTransactionalScopesCompensate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransactionalScopesCompensate.setStatus("current")
_BtoTransScopeCompensatePerSec_Type = Gauge32
_BtoTransScopeCompensatePerSec_Object = MibTableColumn
btoTransScopeCompensatePerSec = _BtoTransScopeCompensatePerSec_Object(
    (1, 3, 6, 1, 4, 1, 9600, 1, 4, 22, 1, 42),
    _BtoTransScopeCompensatePerSec_Type()
)
btoTransScopeCompensatePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btoTransScopeCompensatePerSec.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFORMANT-BIZTALK",
    **{"bizTalkServer": bizTalkServer,
       "bizTalkFILEReceiveAdapterTable": bizTalkFILEReceiveAdapterTable,
       "bizTalkFILEReceiveAdapterEntry": bizTalkFILEReceiveAdapterEntry,
       "btfileraInstance": btfileraInstance,
       "btfileraBytesReceived": btfileraBytesReceived,
       "btfileraBytesReceivedPerSec": btfileraBytesReceivedPerSec,
       "btfileraDeleteRetries": btfileraDeleteRetries,
       "btfileraLockFailures": btfileraLockFailures,
       "btfileraLockFailuresPerSec": btfileraLockFailuresPerSec,
       "btfileraMessagesReceived": btfileraMessagesReceived,
       "btfileraMessagesReceivedPerSec": btfileraMessagesReceivedPerSec,
       "btfileraTimeToBuildBatch": btfileraTimeToBuildBatch,
       "bizTalkFILESendAdapterTable": bizTalkFILESendAdapterTable,
       "bizTalkFILESendAdapterEntry": bizTalkFILESendAdapterEntry,
       "btfilesaInstance": btfilesaInstance,
       "btfilesaBytesSent": btfilesaBytesSent,
       "btfilesaBytesSentPerSec": btfilesaBytesSentPerSec,
       "btfilesaMessagesSent": btfilesaMessagesSent,
       "btfilesaMessagesSentPerSec": btfilesaMessagesSentPerSec,
       "bizTalkFTPReceiveAdapterTable": bizTalkFTPReceiveAdapterTable,
       "bizTalkFTPReceiveAdapterEntry": bizTalkFTPReceiveAdapterEntry,
       "btftpraInstance": btftpraInstance,
       "btftpraBytesReceived": btftpraBytesReceived,
       "btftpraBytesReceivedPerSec": btftpraBytesReceivedPerSec,
       "btftpraMessagesReceived": btftpraMessagesReceived,
       "btftpraMessagesReceivedPerSec": btftpraMessagesReceivedPerSec,
       "bizTalkFTPSendAdapterTable": bizTalkFTPSendAdapterTable,
       "bizTalkFTPSendAdapterEntry": bizTalkFTPSendAdapterEntry,
       "btftpsaInstance": btftpsaInstance,
       "btftpsaBytesSent": btftpsaBytesSent,
       "btftpsaBytesSentPerSec": btftpsaBytesSentPerSec,
       "btftpsaMessagesSent": btftpsaMessagesSent,
       "btftpsaMessagesSentPerSec": btftpsaMessagesSentPerSec,
       "bizTalkHTTPReceiveAdapterTable": bizTalkHTTPReceiveAdapterTable,
       "bizTalkHTTPReceiveAdapterEntry": bizTalkHTTPReceiveAdapterEntry,
       "bthttpraInstance": bthttpraInstance,
       "bthttpraMemoryQueueSize": bthttpraMemoryQueueSize,
       "bthttpraMessagesReceived": bthttpraMessagesReceived,
       "bthttpraMessagesReceivedPerSec": bthttpraMessagesReceivedPerSec,
       "bthttpraMessagesSent": bthttpraMessagesSent,
       "bthttpraMessagesSentPerSec": bthttpraMessagesSentPerSec,
       "bthttpraTimeToAddMessageToBatch": bthttpraTimeToAddMessageToBatch,
       "bthttpraTimeToBuildBatch": bthttpraTimeToBuildBatch,
       "bizTalkHTTPSendAdapterTable": bizTalkHTTPSendAdapterTable,
       "bizTalkHTTPSendAdapterEntry": bizTalkHTTPSendAdapterEntry,
       "bthttpsaInstance": bthttpsaInstance,
       "bthttpsaMemoryQueueSize": bthttpsaMemoryQueueSize,
       "bthttpsaMessagesReceived": bthttpsaMessagesReceived,
       "bthttpsaMessagesReceivedPerSec": bthttpsaMessagesReceivedPerSec,
       "bthttpsaMessagesSent": bthttpsaMessagesSent,
       "bthttpsaMessagesSentPerSec": bthttpsaMessagesSentPerSec,
       "bizTalkMSMQReceiveAdapterTable": bizTalkMSMQReceiveAdapterTable,
       "bizTalkMSMQReceiveAdapterEntry": bizTalkMSMQReceiveAdapterEntry,
       "btmsmqraInstance": btmsmqraInstance,
       "btmsmqraBytesReceived": btmsmqraBytesReceived,
       "btmsmqraBytesReceivedPerSec": btmsmqraBytesReceivedPerSec,
       "btmsmqraMessagesReceived": btmsmqraMessagesReceived,
       "btmsmqraMessagesReceivedPerSec": btmsmqraMessagesReceivedPerSec,
       "bizTalkMSMQSendAdapterTable": bizTalkMSMQSendAdapterTable,
       "bizTalkMSMQSendAdapterEntry": bizTalkMSMQSendAdapterEntry,
       "btmsmqsaInstance": btmsmqsaInstance,
       "btmsmqsaBytesSent": btmsmqsaBytesSent,
       "btmsmqsaBytesSentPerSec": btmsmqsaBytesSentPerSec,
       "btmsmqsaMessagesSent": btmsmqsaMessagesSent,
       "btmsmqsaMessagesSentPerSec": btmsmqsaMessagesSentPerSec,
       "bizTalkMessageAgentTable": bizTalkMessageAgentTable,
       "bizTalkMessageAgentEntry": bizTalkMessageAgentEntry,
       "btmaInstance": btmaInstance,
       "btmaActiveInstanceCount": btmaActiveInstanceCount,
       "btmaDatabaseSession": btmaDatabaseSession,
       "btmaDatabaseSessionThreshold": btmaDatabaseSessionThreshold,
       "btmaDatabaseSize": btmaDatabaseSize,
       "btmaHighDatabaseSession": btmaHighDatabaseSession,
       "btmaHighDatabaseSize": btmaHighDatabaseSize,
       "btmaHighInprocessMessageCount": btmaHighInprocessMessageCount,
       "btmaHighMessageDeliveryRate": btmaHighMessageDeliveryRate,
       "btmaHighMessagePublishingRate": btmaHighMessagePublishingRate,
       "btmaHighProcessMemory": btmaHighProcessMemory,
       "btmaHighSystemMemory": btmaHighSystemMemory,
       "btmaHighThreadCount": btmaHighThreadCount,
       "btmaInprocessMessageCount": btmaInprocessMessageCount,
       "btmaInprocessMsgCountThreshold": btmaInprocessMsgCountThreshold,
       "btmaMsgDeliveryDelayms": btmaMsgDeliveryDelayms,
       "btmaMsgDeliveryIncomingRate": btmaMsgDeliveryIncomingRate,
       "btmaMsgDeliveryOutgoingRate": btmaMsgDeliveryOutgoingRate,
       "btmaMsgDeliveryThrottlingState": btmaMsgDeliveryThrottlingState,
       "btmaMsgDlvryThrottlingStDuration": btmaMsgDlvryThrottlingStDuration,
       "btmaMsgDlvryThrottleUserOverride": btmaMsgDlvryThrottleUserOverride,
       "btmaMsgPublishingDelay": btmaMsgPublishingDelay,
       "btmaMsgPublishingIncomingRate": btmaMsgPublishingIncomingRate,
       "btmaMsgPublishingOutgoingRate": btmaMsgPublishingOutgoingRate,
       "btmaMsgPublishingThrottlingState": btmaMsgPublishingThrottlingState,
       "btmaMsgPubThrottlingStDuration": btmaMsgPubThrottlingStDuration,
       "btmaMsgPubThrottlingUsrOverride": btmaMsgPubThrottlingUsrOverride,
       "btmaPhysicalMemoryUsageMB": btmaPhysicalMemoryUsageMB,
       "btmaProcessMemoryUsageMB": btmaProcessMemoryUsageMB,
       "btmaProcessMemUsageThresholdMB": btmaProcessMemUsageThresholdMB,
       "btmaServiceClassID": btmaServiceClassID,
       "btmaThreadCount": btmaThreadCount,
       "btmaThreadCountThreshold": btmaThreadCountThreshold,
       "btmaTotalBatchesCommitted": btmaTotalBatchesCommitted,
       "btmaTotalMessagesDelivered": btmaTotalMessagesDelivered,
       "btmaTotalMessagesPublished": btmaTotalMessagesPublished,
       "bizTalkMsgBoxGeneralCounterTable": bizTalkMsgBoxGeneralCounterTable,
       "bizTalkMsgBoxGeneralCounterEntry": bizTalkMsgBoxGeneralCounterEntry,
       "btmbgcInstance": btmbgcInstance,
       "btmbgcInstancesTotalNumber": btmbgcInstancesTotalNumber,
       "btmbgcMsgBoxDeadProcCleanup": btmbgcMsgBoxDeadProcCleanup,
       "btmbgcMsgBoxMsgCleanupPurgeJobs": btmbgcMsgBoxMsgCleanupPurgeJobs,
       "btmbgcMsgBoxPartsCleanupPurgeJob": btmbgcMsgBoxPartsCleanupPurgeJob,
       "btmbgcMsgBoxPurgeSubPurgeJobs": btmbgcMsgBoxPurgeSubPurgeJobs,
       "btmbgcSpoolSize": btmbgcSpoolSize,
       "btmbgcTrackedMsgsCopyPurgeJobs": btmbgcTrackedMsgsCopyPurgeJobs,
       "btmbgcTrackingDataSize": btmbgcTrackingDataSize,
       "btmbgcTrackingSpoolCleanup": btmbgcTrackingSpoolCleanup,
       "bizTalkMsgBoxHostCountersTable": bizTalkMsgBoxHostCountersTable,
       "bizTalkMsgBoxHostCountersEntry": bizTalkMsgBoxHostCountersEntry,
       "btmbhcInstance": btmbhcInstance,
       "btmbhcHostQueInstStateMsgRefsLen": btmbhcHostQueInstStateMsgRefsLen,
       "btmbhcHostQueueLength": btmbhcHostQueueLength,
       "btmbhcHostQueueNumberOfInstances": btmbhcHostQueueNumberOfInstances,
       "btmbhcHostQueueSuspendedMsgsLen": btmbhcHostQueueSuspendedMsgsLen,
       "bizTalkMessagingTable": bizTalkMessagingTable,
       "bizTalkMessagingEntry": bizTalkMessagingEntry,
       "btmInstance": btmInstance,
       "btmActiveReceiveLocations": btmActiveReceiveLocations,
       "btmActiveReceiveThreads": btmActiveReceiveThreads,
       "btmActiveSendMessages": btmActiveSendMessages,
       "btmActiveSendThreads": btmActiveSendThreads,
       "btmDocumentsProcessed": btmDocumentsProcessed,
       "btmDocumentsProcessedPerSec": btmDocumentsProcessedPerSec,
       "btmDocumentsReceived": btmDocumentsReceived,
       "btmDocumentsReceivedPerSec": btmDocumentsReceivedPerSec,
       "btmDocumentsResubmitted": btmDocumentsResubmitted,
       "btmDocumentsSubmittedPerBatch": btmDocumentsSubmittedPerBatch,
       "btmDocumentsSuspended": btmDocumentsSuspended,
       "btmDocumentsSuspendedPerSec": btmDocumentsSuspendedPerSec,
       "btmDocumentsTransmittedPerBatch": btmDocumentsTransmittedPerBatch,
       "btmIDProcess": btmIDProcess,
       "btmPendingReceiveBatches": btmPendingReceiveBatches,
       "btmPendingTransmittedMessages": btmPendingTransmittedMessages,
       "btmRequestPerResponseTimeouts": btmRequestPerResponseTimeouts,
       "btmThrottledReceiveBatches": btmThrottledReceiveBatches,
       "bizTalkMessagingLatencyTable": bizTalkMessagingLatencyTable,
       "bizTalkMessagingLatencyEntry": bizTalkMessagingLatencyEntry,
       "btmlInstance": btmlInstance,
       "btmlInboundLatencysec": btmlInboundLatencysec,
       "btmlOutboundAdapterLatencysec": btmlOutboundAdapterLatencysec,
       "btmlOutboundLatencysec": btmlOutboundLatencysec,
       "btmlRequestResponseLatencysec": btmlRequestResponseLatencysec,
       "bizTalkPOP3ReceiveAdapterTable": bizTalkPOP3ReceiveAdapterTable,
       "bizTalkPOP3ReceiveAdapterEntry": bizTalkPOP3ReceiveAdapterEntry,
       "btpopraInstance": btpopraInstance,
       "btpopraActiveSessions": btpopraActiveSessions,
       "btpopraBytesReceived": btpopraBytesReceived,
       "btpopraBytesReceivedPerSec": btpopraBytesReceivedPerSec,
       "btpopraMessagesReceived": btpopraMessagesReceived,
       "btpopraMessagesReceivedPerSec": btpopraMessagesReceivedPerSec,
       "bizTalkSMTPSendAdapterTable": bizTalkSMTPSendAdapterTable,
       "bizTalkSMTPSendAdapterEntry": bizTalkSMTPSendAdapterEntry,
       "btsmtpsaInstance": btsmtpsaInstance,
       "btsmtpsaMessagesSent": btsmtpsaMessagesSent,
       "btsmtpsaMessagesSentPerSec": btsmtpsaMessagesSentPerSec,
       "bizTalkSOAPReceiveAdapterTable": bizTalkSOAPReceiveAdapterTable,
       "bizTalkSOAPReceiveAdapterEntry": bizTalkSOAPReceiveAdapterEntry,
       "btsoapraInstance": btsoapraInstance,
       "btsoapraMessagesReceived": btsoapraMessagesReceived,
       "btsoapraMessagesReceivedPerSec": btsoapraMessagesReceivedPerSec,
       "bizTalkSOAPSendAdapterTable": bizTalkSOAPSendAdapterTable,
       "bizTalkSOAPSendAdapterEntry": bizTalkSOAPSendAdapterEntry,
       "btsoapsaInstance": btsoapsaInstance,
       "btsoapsaMessagesSent": btsoapsaMessagesSent,
       "btsoapsaMessagesSentPerSec": btsoapsaMessagesSentPerSec,
       "bizTalkSQLReceiveAdapterTable": bizTalkSQLReceiveAdapterTable,
       "bizTalkSQLReceiveAdapterEntry": bizTalkSQLReceiveAdapterEntry,
       "btsqlraInstance": btsqlraInstance,
       "btsqlraMessagesReceived": btsqlraMessagesReceived,
       "btsqlraMessagesReceivedPerSec": btsqlraMessagesReceivedPerSec,
       "bizTalkSQLSendAdapterTable": bizTalkSQLSendAdapterTable,
       "bizTalkSQLSendAdapterEntry": bizTalkSQLSendAdapterEntry,
       "btsqlsaInstance": btsqlsaInstance,
       "btsqlsaMessagesSent": btsqlsaMessagesSent,
       "btsqlsaMessagesSentPerSec": btsqlsaMessagesSentPerSec,
       "bizTalkTDDSTable": bizTalkTDDSTable,
       "bizTalkTDDSEntry": bizTalkTDDSEntry,
       "bttddsInstance": bttddsInstance,
       "bttddsBatchesCommitted": bttddsBatchesCommitted,
       "bttddsBatchesBeingProcessed": bttddsBatchesBeingProcessed,
       "bttddsEventsCommitted": bttddsEventsCommitted,
       "bttddsEventsBeingProcessed": bttddsEventsBeingProcessed,
       "bttddsRecordsCommitted": bttddsRecordsCommitted,
       "bttddsRecordsBeingProcessed": bttddsRecordsBeingProcessed,
       "bttddsTotalBatches": bttddsTotalBatches,
       "bttddsTotalEvents": bttddsTotalEvents,
       "bttddsTotalFailedBatches": bttddsTotalFailedBatches,
       "bttddsTotalFailedEvents": bttddsTotalFailedEvents,
       "bttddsTotalRecords": bttddsTotalRecords,
       "bizTalkSharePointServicesAdapter": bizTalkSharePointServicesAdapter,
       "btwspsaPercentReceiveMsgFailures": btwspsaPercentReceiveMsgFailures,
       "btwspsaPercentSendMsgFailures": btwspsaPercentSendMsgFailures,
       "btwspsaPercentWebServiceCallFail": btwspsaPercentWebServiceCallFail,
       "btwspsaTotalReceiveCommitFailure": btwspsaTotalReceiveCommitFailure,
       "btwspsaTotalReceiveMsgFailures": btwspsaTotalReceiveMsgFailures,
       "btwspsaTotalReceivedMsgs": btwspsaTotalReceivedMsgs,
       "btwspsaTotalSendMsgFailures": btwspsaTotalSendMsgFailures,
       "btwspsaTotalSentMsgs": btwspsaTotalSentMsgs,
       "btwspsaTotalWebServiceCallFail": btwspsaTotalWebServiceCallFail,
       "btwspsaWebServiceCallsPerSecond": btwspsaWebServiceCallsPerSecond,
       "xLANGPerSOrchestrationsTable": xLANGPerSOrchestrationsTable,
       "xLANGPerSOrchestrationsEntry": xLANGPerSOrchestrationsEntry,
       "btoInstance": btoInstance,
       "btoPercentUsedPhysicalMemory": btoPercentUsedPhysicalMemory,
       "btoActiveApplicationDomains": btoActiveApplicationDomains,
       "btoAverageBatchFactor": btoAverageBatchFactor,
       "btoDatabaseTransactions": btoDatabaseTransactions,
       "btoDatabaseTransactionsPerSec": btoDatabaseTransactionsPerSec,
       "btoDehydratableOrchestrations": btoDehydratableOrchestrations,
       "btoDehydratingOrchestrations": btoDehydratingOrchestrations,
       "btoDehydrationCycleInProgress": btoDehydrationCycleInProgress,
       "btoDehydrationCycles": btoDehydrationCycles,
       "btoDehydrationThreshold": btoDehydrationThreshold,
       "btoIdleOrchestrations": btoIdleOrchestrations,
       "btoMBAllocatedPrivateMemory": btoMBAllocatedPrivateMemory,
       "btoMBAllocatedVirtualMemory": btoMBAllocatedVirtualMemory,
       "btoMsgBoxDBConnectionFailures": btoMsgBoxDBConnectionFailures,
       "btoOnlineMessageBoxDatabases": btoOnlineMessageBoxDatabases,
       "btoOrchestrationsCompleted": btoOrchestrationsCompleted,
       "btoOrchestrationsCompletedPerSec": btoOrchestrationsCompletedPerSec,
       "btoOrchestrationsCreated": btoOrchestrationsCreated,
       "btoOrchestrationsCreatedPerSec": btoOrchestrationsCreatedPerSec,
       "btoOrchestrationsDehydrated": btoOrchestrationsDehydrated,
       "btoOrchestrationDehydratedPerSec": btoOrchestrationDehydratedPerSec,
       "btoOrchestrationsDiscarded": btoOrchestrationsDiscarded,
       "btoOrchestrationsDiscardedPerSec": btoOrchestrationsDiscardedPerSec,
       "btoOrchestrationsRehydrated": btoOrchestrationsRehydrated,
       "btoOrchestrationRehydratedPerSec": btoOrchestrationRehydratedPerSec,
       "btoOrchestrationResidentInmemory": btoOrchestrationResidentInmemory,
       "btoOrchestrationsSchedForDehyd": btoOrchestrationsSchedForDehyd,
       "btoOrchestrationsSuspended": btoOrchestrationsSuspended,
       "btoOrchestrationsSuspendedPerSec": btoOrchestrationsSuspendedPerSec,
       "btoPendingMessages": btoPendingMessages,
       "btoPendingWorkItems": btoPendingWorkItems,
       "btoPersistencePoints": btoPersistencePoints,
       "btoPersistencePointsPerSec": btoPersistencePointsPerSec,
       "btoRunnableOrchestrations": btoRunnableOrchestrations,
       "btoRunningOrchestrations": btoRunningOrchestrations,
       "btoTransactionalScopesAborted": btoTransactionalScopesAborted,
       "btoTransactionalScopeAbortPerSec": btoTransactionalScopeAbortPerSec,
       "btoTransactionalScopesCommitted": btoTransactionalScopesCommitted,
       "btoTransactionScopeCommitPerSec": btoTransactionScopeCommitPerSec,
       "btoTransactionalScopesCompensate": btoTransactionalScopesCompensate,
       "btoTransScopeCompensatePerSec": btoTransScopeCompensatePerSec}
)
