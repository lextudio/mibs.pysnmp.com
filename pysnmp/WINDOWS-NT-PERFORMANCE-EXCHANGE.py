# SNMP MIB module (WINDOWS-NT-PERFORMANCE-EXCHANGE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WINDOWS-NT-PERFORMANCE-EXCHANGE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:59 2024
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

_Microsoft_ObjectIdentity = ObjectIdentity
microsoft = _Microsoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1)
)
_Os_ObjectIdentity = ObjectIdentity
os = _Os_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3)
)
_Winnt_ObjectIdentity = ObjectIdentity
winnt = _Winnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1)
)
_MSExchangeMTA_ObjectIdentity = ObjectIdentity
mSExchangeMTA = _MSExchangeMTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1)
)
_MtaAdjacentMTAAssociations_Type = Integer32
_MtaAdjacentMTAAssociations_Object = MibScalar
mtaAdjacentMTAAssociations = _MtaAdjacentMTAAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 1),
    _MtaAdjacentMTAAssociations_Type()
)
mtaAdjacentMTAAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdjacentMTAAssociations.setStatus("mandatory")
_MtaMessagesPerSec_Type = Counter32
_MtaMessagesPerSec_Object = MibScalar
mtaMessagesPerSec = _MtaMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 2),
    _MtaMessagesPerSec_Type()
)
mtaMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaMessagesPerSec.setStatus("mandatory")
_MtaMessageBytesPerSec_Type = Counter32
_MtaMessageBytesPerSec_Object = MibScalar
mtaMessageBytesPerSec = _MtaMessageBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 3),
    _MtaMessageBytesPerSec_Type()
)
mtaMessageBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaMessageBytesPerSec.setStatus("mandatory")
_MtaFreeElements_Type = Integer32
_MtaFreeElements_Object = MibScalar
mtaFreeElements = _MtaFreeElements_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 4),
    _MtaFreeElements_Type()
)
mtaFreeElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFreeElements.setStatus("mandatory")
_MtaFreeHeaders_Type = Integer32
_MtaFreeHeaders_Object = MibScalar
mtaFreeHeaders = _MtaFreeHeaders_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 5),
    _MtaFreeHeaders_Type()
)
mtaFreeHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaFreeHeaders.setStatus("mandatory")
_MtaAdminConnections_Type = Integer32
_MtaAdminConnections_Object = MibScalar
mtaAdminConnections = _MtaAdminConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 6),
    _MtaAdminConnections_Type()
)
mtaAdminConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdminConnections.setStatus("mandatory")
_MtaThreadsInUse_Type = Integer32
_MtaThreadsInUse_Object = MibScalar
mtaThreadsInUse = _MtaThreadsInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 7),
    _MtaThreadsInUse_Type()
)
mtaThreadsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaThreadsInUse.setStatus("mandatory")
_MtaWorkQueueLength_Type = Integer32
_MtaWorkQueueLength_Object = MibScalar
mtaWorkQueueLength = _MtaWorkQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 8),
    _MtaWorkQueueLength_Type()
)
mtaWorkQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaWorkQueueLength.setStatus("mandatory")
_MtaXAPIGateways_Type = Integer32
_MtaXAPIGateways_Object = MibScalar
mtaXAPIGateways = _MtaXAPIGateways_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 9),
    _MtaXAPIGateways_Type()
)
mtaXAPIGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaXAPIGateways.setStatus("mandatory")
_MtaXAPIClients_Type = Integer32
_MtaXAPIClients_Object = MibScalar
mtaXAPIClients = _MtaXAPIClients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 10),
    _MtaXAPIClients_Type()
)
mtaXAPIClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaXAPIClients.setStatus("mandatory")
_MtaDiskFileDeletesPerSec_Type = Counter32
_MtaDiskFileDeletesPerSec_Object = MibScalar
mtaDiskFileDeletesPerSec = _MtaDiskFileDeletesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 11),
    _MtaDiskFileDeletesPerSec_Type()
)
mtaDiskFileDeletesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDiskFileDeletesPerSec.setStatus("mandatory")
_MtaDiskFileSyncsPerSec_Type = Counter32
_MtaDiskFileSyncsPerSec_Object = MibScalar
mtaDiskFileSyncsPerSec = _MtaDiskFileSyncsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 12),
    _MtaDiskFileSyncsPerSec_Type()
)
mtaDiskFileSyncsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDiskFileSyncsPerSec.setStatus("mandatory")
_MtaDiskFileOpensPerSec_Type = Counter32
_MtaDiskFileOpensPerSec_Object = MibScalar
mtaDiskFileOpensPerSec = _MtaDiskFileOpensPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 13),
    _MtaDiskFileOpensPerSec_Type()
)
mtaDiskFileOpensPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDiskFileOpensPerSec.setStatus("mandatory")
_MtaDiskFileReadsPerSec_Type = Counter32
_MtaDiskFileReadsPerSec_Object = MibScalar
mtaDiskFileReadsPerSec = _MtaDiskFileReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 14),
    _MtaDiskFileReadsPerSec_Type()
)
mtaDiskFileReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDiskFileReadsPerSec.setStatus("mandatory")
_MtaDiskFileWritesPerSec_Type = Counter32
_MtaDiskFileWritesPerSec_Object = MibScalar
mtaDiskFileWritesPerSec = _MtaDiskFileWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 15),
    _MtaDiskFileWritesPerSec_Type()
)
mtaDiskFileWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDiskFileWritesPerSec.setStatus("mandatory")
_MtaExDSReadCallsPerSec_Type = Counter32
_MtaExDSReadCallsPerSec_Object = MibScalar
mtaExDSReadCallsPerSec = _MtaExDSReadCallsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 16),
    _MtaExDSReadCallsPerSec_Type()
)
mtaExDSReadCallsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaExDSReadCallsPerSec.setStatus("mandatory")
_MtaXAPIReceiveBytesPerSec_Type = Counter32
_MtaXAPIReceiveBytesPerSec_Object = MibScalar
mtaXAPIReceiveBytesPerSec = _MtaXAPIReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 17),
    _MtaXAPIReceiveBytesPerSec_Type()
)
mtaXAPIReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaXAPIReceiveBytesPerSec.setStatus("mandatory")
_MtaXAPITransmitBytesPerSec_Type = Counter32
_MtaXAPITransmitBytesPerSec_Object = MibScalar
mtaXAPITransmitBytesPerSec = _MtaXAPITransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 18),
    _MtaXAPITransmitBytesPerSec_Type()
)
mtaXAPITransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaXAPITransmitBytesPerSec.setStatus("mandatory")
_MtaAdminInterfaceReceiveBytesPerSec_Type = Counter32
_MtaAdminInterfaceReceiveBytesPerSec_Object = MibScalar
mtaAdminInterfaceReceiveBytesPerSec = _MtaAdminInterfaceReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 19),
    _MtaAdminInterfaceReceiveBytesPerSec_Type()
)
mtaAdminInterfaceReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdminInterfaceReceiveBytesPerSec.setStatus("mandatory")
_MtaAdminInterfaceTransmitBytesPerSec_Type = Counter32
_MtaAdminInterfaceTransmitBytesPerSec_Object = MibScalar
mtaAdminInterfaceTransmitBytesPerSec = _MtaAdminInterfaceTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 20),
    _MtaAdminInterfaceTransmitBytesPerSec_Type()
)
mtaAdminInterfaceTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaAdminInterfaceTransmitBytesPerSec.setStatus("mandatory")
_MtaLANReceiveBytesPerSec_Type = Counter32
_MtaLANReceiveBytesPerSec_Object = MibScalar
mtaLANReceiveBytesPerSec = _MtaLANReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 21),
    _MtaLANReceiveBytesPerSec_Type()
)
mtaLANReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLANReceiveBytesPerSec.setStatus("mandatory")
_MtaLANTransmitBytesPerSec_Type = Counter32
_MtaLANTransmitBytesPerSec_Object = MibScalar
mtaLANTransmitBytesPerSec = _MtaLANTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 22),
    _MtaLANTransmitBytesPerSec_Type()
)
mtaLANTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaLANTransmitBytesPerSec.setStatus("mandatory")
_MtaRASReceiveBytesPerSec_Type = Counter32
_MtaRASReceiveBytesPerSec_Object = MibScalar
mtaRASReceiveBytesPerSec = _MtaRASReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 23),
    _MtaRASReceiveBytesPerSec_Type()
)
mtaRASReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaRASReceiveBytesPerSec.setStatus("mandatory")
_MtaRASTransmitBytesPerSec_Type = Counter32
_MtaRASTransmitBytesPerSec_Object = MibScalar
mtaRASTransmitBytesPerSec = _MtaRASTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 24),
    _MtaRASTransmitBytesPerSec_Type()
)
mtaRASTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaRASTransmitBytesPerSec.setStatus("mandatory")
_MtaTCPPerIPReceiveBytesPerSec_Type = Counter32
_MtaTCPPerIPReceiveBytesPerSec_Object = MibScalar
mtaTCPPerIPReceiveBytesPerSec = _MtaTCPPerIPReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 25),
    _MtaTCPPerIPReceiveBytesPerSec_Type()
)
mtaTCPPerIPReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTCPPerIPReceiveBytesPerSec.setStatus("mandatory")
_MtaTCPPerIPTransmitBytesPerSec_Type = Counter32
_MtaTCPPerIPTransmitBytesPerSec_Object = MibScalar
mtaTCPPerIPTransmitBytesPerSec = _MtaTCPPerIPTransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 26),
    _MtaTCPPerIPTransmitBytesPerSec_Type()
)
mtaTCPPerIPTransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTCPPerIPTransmitBytesPerSec.setStatus("mandatory")
_MtaTP4ReceiveBytesPerSec_Type = Counter32
_MtaTP4ReceiveBytesPerSec_Object = MibScalar
mtaTP4ReceiveBytesPerSec = _MtaTP4ReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 27),
    _MtaTP4ReceiveBytesPerSec_Type()
)
mtaTP4ReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTP4ReceiveBytesPerSec.setStatus("mandatory")
_MtaTP4TransmitBytesPerSec_Type = Counter32
_MtaTP4TransmitBytesPerSec_Object = MibScalar
mtaTP4TransmitBytesPerSec = _MtaTP4TransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 28),
    _MtaTP4TransmitBytesPerSec_Type()
)
mtaTP4TransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTP4TransmitBytesPerSec.setStatus("mandatory")
_MtaX25ReceiveBytesPerSec_Type = Counter32
_MtaX25ReceiveBytesPerSec_Object = MibScalar
mtaX25ReceiveBytesPerSec = _MtaX25ReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 29),
    _MtaX25ReceiveBytesPerSec_Type()
)
mtaX25ReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaX25ReceiveBytesPerSec.setStatus("mandatory")
_MtaX25TransmitBytesPerSec_Type = Counter32
_MtaX25TransmitBytesPerSec_Object = MibScalar
mtaX25TransmitBytesPerSec = _MtaX25TransmitBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 30),
    _MtaX25TransmitBytesPerSec_Type()
)
mtaX25TransmitBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaX25TransmitBytesPerSec.setStatus("mandatory")
_MtaDeferredDeliveryMsgs_Type = Integer32
_MtaDeferredDeliveryMsgs_Object = MibScalar
mtaDeferredDeliveryMsgs = _MtaDeferredDeliveryMsgs_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 31),
    _MtaDeferredDeliveryMsgs_Type()
)
mtaDeferredDeliveryMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaDeferredDeliveryMsgs.setStatus("mandatory")
_MtaTotalRecipientsQueued_Type = Integer32
_MtaTotalRecipientsQueued_Object = MibScalar
mtaTotalRecipientsQueued = _MtaTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 32),
    _MtaTotalRecipientsQueued_Type()
)
mtaTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalRecipientsQueued.setStatus("mandatory")
_MtaTotalSuccessfulConversions_Type = Integer32
_MtaTotalSuccessfulConversions_Object = MibScalar
mtaTotalSuccessfulConversions = _MtaTotalSuccessfulConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 33),
    _MtaTotalSuccessfulConversions_Type()
)
mtaTotalSuccessfulConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalSuccessfulConversions.setStatus("mandatory")
_MtaTotalFailedConversions_Type = Integer32
_MtaTotalFailedConversions_Object = MibScalar
mtaTotalFailedConversions = _MtaTotalFailedConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 34),
    _MtaTotalFailedConversions_Type()
)
mtaTotalFailedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalFailedConversions.setStatus("mandatory")
_MtaTotalLoopsDetected_Type = Integer32
_MtaTotalLoopsDetected_Object = MibScalar
mtaTotalLoopsDetected = _MtaTotalLoopsDetected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 35),
    _MtaTotalLoopsDetected_Type()
)
mtaTotalLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalLoopsDetected.setStatus("mandatory")
_MtaInboundMessagesTotal_Type = Counter32
_MtaInboundMessagesTotal_Object = MibScalar
mtaInboundMessagesTotal = _MtaInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 36),
    _MtaInboundMessagesTotal_Type()
)
mtaInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaInboundMessagesTotal.setStatus("mandatory")
_MtaOutboundMessagesTotal_Type = Counter32
_MtaOutboundMessagesTotal_Object = MibScalar
mtaOutboundMessagesTotal = _MtaOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 37),
    _MtaOutboundMessagesTotal_Type()
)
mtaOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOutboundMessagesTotal.setStatus("mandatory")
_MtaInboundBytesTotal_Type = Counter32
_MtaInboundBytesTotal_Object = MibScalar
mtaInboundBytesTotal = _MtaInboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 38),
    _MtaInboundBytesTotal_Type()
)
mtaInboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaInboundBytesTotal.setStatus("mandatory")
_MtaWorkQueueBytes_Type = Counter32
_MtaWorkQueueBytes_Object = MibScalar
mtaWorkQueueBytes = _MtaWorkQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 39),
    _MtaWorkQueueBytes_Type()
)
mtaWorkQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaWorkQueueBytes.setStatus("mandatory")
_MtaOutboundBytesTotal_Type = Counter32
_MtaOutboundBytesTotal_Object = MibScalar
mtaOutboundBytesTotal = _MtaOutboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 40),
    _MtaOutboundBytesTotal_Type()
)
mtaOutboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaOutboundBytesTotal.setStatus("mandatory")
_MtaTotalRecipientsInbound_Type = Counter32
_MtaTotalRecipientsInbound_Object = MibScalar
mtaTotalRecipientsInbound = _MtaTotalRecipientsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 41),
    _MtaTotalRecipientsInbound_Type()
)
mtaTotalRecipientsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalRecipientsInbound.setStatus("mandatory")
_MtaTotalRecipientsOutbound_Type = Counter32
_MtaTotalRecipientsOutbound_Object = MibScalar
mtaTotalRecipientsOutbound = _MtaTotalRecipientsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 1, 42),
    _MtaTotalRecipientsOutbound_Type()
)
mtaTotalRecipientsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtaTotalRecipientsOutbound.setStatus("mandatory")
_ConnmSExchangeMTA_ConnectionsTable_Object = MibTable
connmSExchangeMTA_ConnectionsTable = _ConnmSExchangeMTA_ConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    connmSExchangeMTA_ConnectionsTable.setStatus("mandatory")
_ConnmSExchangeMTA_ConnectionsEntry_Object = MibTableRow
connmSExchangeMTA_ConnectionsEntry = _ConnmSExchangeMTA_ConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1)
)
connmSExchangeMTA_ConnectionsEntry.setIndexNames(
    (0, "WINDOWS-NT-PERFORMANCE-EXCHANGE", "connmSExchangeMTA-ConnectionsIndex"),
)
if mibBuilder.loadTexts:
    connmSExchangeMTA_ConnectionsEntry.setStatus("mandatory")
_ConnmSExchangeMTA_ConnectionsIndex_Type = Integer32
_ConnmSExchangeMTA_ConnectionsIndex_Object = MibScalar
connmSExchangeMTA_ConnectionsIndex = _ConnmSExchangeMTA_ConnectionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 1),
    _ConnmSExchangeMTA_ConnectionsIndex_Type()
)
connmSExchangeMTA_ConnectionsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connmSExchangeMTA_ConnectionsIndex.setStatus("mandatory")
_ConnmSExchangeMTA_ConnectionsInstance_Type = DisplayString
_ConnmSExchangeMTA_ConnectionsInstance_Object = MibScalar
connmSExchangeMTA_ConnectionsInstance = _ConnmSExchangeMTA_ConnectionsInstance_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 2),
    _ConnmSExchangeMTA_ConnectionsInstance_Type()
)
connmSExchangeMTA_ConnectionsInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connmSExchangeMTA_ConnectionsInstance.setStatus("mandatory")
_ConnAssociations_Type = Integer32
_ConnAssociations_Object = MibTableColumn
connAssociations = _ConnAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 3),
    _ConnAssociations_Type()
)
connAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connAssociations.setStatus("mandatory")
_ConnReceiveBytesPerSec_Type = Counter32
_ConnReceiveBytesPerSec_Object = MibTableColumn
connReceiveBytesPerSec = _ConnReceiveBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 4),
    _ConnReceiveBytesPerSec_Type()
)
connReceiveBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connReceiveBytesPerSec.setStatus("mandatory")
_ConnSendBytesPerSec_Type = Counter32
_ConnSendBytesPerSec_Object = MibTableColumn
connSendBytesPerSec = _ConnSendBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 5),
    _ConnSendBytesPerSec_Type()
)
connSendBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSendBytesPerSec.setStatus("mandatory")
_ConnReceiveMessagesPerSec_Type = Counter32
_ConnReceiveMessagesPerSec_Object = MibTableColumn
connReceiveMessagesPerSec = _ConnReceiveMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 6),
    _ConnReceiveMessagesPerSec_Type()
)
connReceiveMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connReceiveMessagesPerSec.setStatus("mandatory")
_ConnSendMessagesPerSec_Type = Counter32
_ConnSendMessagesPerSec_Object = MibTableColumn
connSendMessagesPerSec = _ConnSendMessagesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 7),
    _ConnSendMessagesPerSec_Type()
)
connSendMessagesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSendMessagesPerSec.setStatus("mandatory")
_ConnQueueLength_Type = Integer32
_ConnQueueLength_Object = MibTableColumn
connQueueLength = _ConnQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 8),
    _ConnQueueLength_Type()
)
connQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connQueueLength.setStatus("mandatory")
_ConnConnectorIndex_Type = Integer32
_ConnConnectorIndex_Object = MibTableColumn
connConnectorIndex = _ConnConnectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 9),
    _ConnConnectorIndex_Type()
)
connConnectorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connConnectorIndex.setStatus("mandatory")
_ConnInboundRejectedTotal_Type = Integer32
_ConnInboundRejectedTotal_Object = MibTableColumn
connInboundRejectedTotal = _ConnInboundRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 10),
    _ConnInboundRejectedTotal_Type()
)
connInboundRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connInboundRejectedTotal.setStatus("mandatory")
_ConnTotalRecipientsQueued_Type = Integer32
_ConnTotalRecipientsQueued_Object = MibTableColumn
connTotalRecipientsQueued = _ConnTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 11),
    _ConnTotalRecipientsQueued_Type()
)
connTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connTotalRecipientsQueued.setStatus("mandatory")
_ConnOldestMessageQueued_Type = TimeTicks
_ConnOldestMessageQueued_Object = MibTableColumn
connOldestMessageQueued = _ConnOldestMessageQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 12),
    _ConnOldestMessageQueued_Type()
)
connOldestMessageQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOldestMessageQueued.setStatus("mandatory")
_ConnCurrentInboundAssociations_Type = Integer32
_ConnCurrentInboundAssociations_Object = MibTableColumn
connCurrentInboundAssociations = _ConnCurrentInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 13),
    _ConnCurrentInboundAssociations_Type()
)
connCurrentInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCurrentInboundAssociations.setStatus("mandatory")
_ConnCurrentOutboundAssociations_Type = Integer32
_ConnCurrentOutboundAssociations_Object = MibTableColumn
connCurrentOutboundAssociations = _ConnCurrentOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 14),
    _ConnCurrentOutboundAssociations_Type()
)
connCurrentOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCurrentOutboundAssociations.setStatus("mandatory")
_ConnCumulativeInboundAssociations_Type = Integer32
_ConnCumulativeInboundAssociations_Object = MibTableColumn
connCumulativeInboundAssociations = _ConnCumulativeInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 15),
    _ConnCumulativeInboundAssociations_Type()
)
connCumulativeInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCumulativeInboundAssociations.setStatus("mandatory")
_ConnCumulativeOutboundAssociations_Type = Integer32
_ConnCumulativeOutboundAssociations_Object = MibTableColumn
connCumulativeOutboundAssociations = _ConnCumulativeOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 16),
    _ConnCumulativeOutboundAssociations_Type()
)
connCumulativeOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connCumulativeOutboundAssociations.setStatus("mandatory")
_ConnLastInboundAssociation_Type = TimeTicks
_ConnLastInboundAssociation_Object = MibTableColumn
connLastInboundAssociation = _ConnLastInboundAssociation_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 17),
    _ConnLastInboundAssociation_Type()
)
connLastInboundAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLastInboundAssociation.setStatus("mandatory")
_ConnLastOutboundAssociation_Type = TimeTicks
_ConnLastOutboundAssociation_Object = MibTableColumn
connLastOutboundAssociation = _ConnLastOutboundAssociation_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 18),
    _ConnLastOutboundAssociation_Type()
)
connLastOutboundAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLastOutboundAssociation.setStatus("mandatory")
_ConnRejectedInboundAssociations_Type = Integer32
_ConnRejectedInboundAssociations_Object = MibTableColumn
connRejectedInboundAssociations = _ConnRejectedInboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 19),
    _ConnRejectedInboundAssociations_Type()
)
connRejectedInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connRejectedInboundAssociations.setStatus("mandatory")
_ConnFailedOutboundAssociations_Type = Integer32
_ConnFailedOutboundAssociations_Object = MibTableColumn
connFailedOutboundAssociations = _ConnFailedOutboundAssociations_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 20),
    _ConnFailedOutboundAssociations_Type()
)
connFailedOutboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connFailedOutboundAssociations.setStatus("mandatory")
_ConnNextAssociationRetry_Type = Integer32
_ConnNextAssociationRetry_Object = MibTableColumn
connNextAssociationRetry = _ConnNextAssociationRetry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 21),
    _ConnNextAssociationRetry_Type()
)
connNextAssociationRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNextAssociationRetry.setStatus("mandatory")
_ConnInboundRejectReason_Type = Integer32
_ConnInboundRejectReason_Object = MibTableColumn
connInboundRejectReason = _ConnInboundRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 22),
    _ConnInboundRejectReason_Type()
)
connInboundRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connInboundRejectReason.setStatus("mandatory")
_ConnOutboundFailureReason_Type = Integer32
_ConnOutboundFailureReason_Object = MibTableColumn
connOutboundFailureReason = _ConnOutboundFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 23),
    _ConnOutboundFailureReason_Type()
)
connOutboundFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOutboundFailureReason.setStatus("mandatory")
_ConnInboundMessagesTotal_Type = Counter32
_ConnInboundMessagesTotal_Object = MibTableColumn
connInboundMessagesTotal = _ConnInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 24),
    _ConnInboundMessagesTotal_Type()
)
connInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connInboundMessagesTotal.setStatus("mandatory")
_ConnOutboundMessagesTotal_Type = Counter32
_ConnOutboundMessagesTotal_Object = MibTableColumn
connOutboundMessagesTotal = _ConnOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 25),
    _ConnOutboundMessagesTotal_Type()
)
connOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOutboundMessagesTotal.setStatus("mandatory")
_ConnInboundBytesTotal_Type = Counter32
_ConnInboundBytesTotal_Object = MibTableColumn
connInboundBytesTotal = _ConnInboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 26),
    _ConnInboundBytesTotal_Type()
)
connInboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connInboundBytesTotal.setStatus("mandatory")
_ConnQueuedBytes_Type = Counter32
_ConnQueuedBytes_Object = MibTableColumn
connQueuedBytes = _ConnQueuedBytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 27),
    _ConnQueuedBytes_Type()
)
connQueuedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connQueuedBytes.setStatus("mandatory")
_ConnOutboundBytesTotal_Type = Counter32
_ConnOutboundBytesTotal_Object = MibTableColumn
connOutboundBytesTotal = _ConnOutboundBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 28),
    _ConnOutboundBytesTotal_Type()
)
connOutboundBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connOutboundBytesTotal.setStatus("mandatory")
_ConnTotalRecipientsInbound_Type = Counter32
_ConnTotalRecipientsInbound_Object = MibTableColumn
connTotalRecipientsInbound = _ConnTotalRecipientsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 29),
    _ConnTotalRecipientsInbound_Type()
)
connTotalRecipientsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connTotalRecipientsInbound.setStatus("mandatory")
_ConnTotalRecipientsOutbound_Type = Counter32
_ConnTotalRecipientsOutbound_Object = MibTableColumn
connTotalRecipientsOutbound = _ConnTotalRecipientsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 2, 1, 30),
    _ConnTotalRecipientsOutbound_Type()
)
connTotalRecipientsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connTotalRecipientsOutbound.setStatus("mandatory")
_MSExchangeIMC_ObjectIdentity = ObjectIdentity
mSExchangeIMC = _MSExchangeIMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3)
)
_ImsQueuedMTS_IN_Type = Integer32
_ImsQueuedMTS_IN_Object = MibScalar
imsQueuedMTS_IN = _ImsQueuedMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 1),
    _ImsQueuedMTS_IN_Type()
)
imsQueuedMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsQueuedMTS_IN.setStatus("mandatory")
_ImsBytesQueuedMTS_IN_Type = Integer32
_ImsBytesQueuedMTS_IN_Object = MibScalar
imsBytesQueuedMTS_IN = _ImsBytesQueuedMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 2),
    _ImsBytesQueuedMTS_IN_Type()
)
imsBytesQueuedMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsBytesQueuedMTS_IN.setStatus("mandatory")
_ImsMessagesEnteringMTS_IN_Type = Integer32
_ImsMessagesEnteringMTS_IN_Object = MibScalar
imsMessagesEnteringMTS_IN = _ImsMessagesEnteringMTS_IN_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 3),
    _ImsMessagesEnteringMTS_IN_Type()
)
imsMessagesEnteringMTS_IN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsMessagesEnteringMTS_IN.setStatus("mandatory")
_ImsQueuedMTS_OUT_Type = Integer32
_ImsQueuedMTS_OUT_Object = MibScalar
imsQueuedMTS_OUT = _ImsQueuedMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 4),
    _ImsQueuedMTS_OUT_Type()
)
imsQueuedMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsQueuedMTS_OUT.setStatus("mandatory")
_ImsBytesQueuedMTS_OUT_Type = Integer32
_ImsBytesQueuedMTS_OUT_Object = MibScalar
imsBytesQueuedMTS_OUT = _ImsBytesQueuedMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 5),
    _ImsBytesQueuedMTS_OUT_Type()
)
imsBytesQueuedMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsBytesQueuedMTS_OUT.setStatus("mandatory")
_ImsMessagesEnteringMTS_OUT_Type = Integer32
_ImsMessagesEnteringMTS_OUT_Object = MibScalar
imsMessagesEnteringMTS_OUT = _ImsMessagesEnteringMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 6),
    _ImsMessagesEnteringMTS_OUT_Type()
)
imsMessagesEnteringMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsMessagesEnteringMTS_OUT.setStatus("mandatory")
_ImsMessagesLeavingMTS_OUT_Type = Integer32
_ImsMessagesLeavingMTS_OUT_Object = MibScalar
imsMessagesLeavingMTS_OUT = _ImsMessagesLeavingMTS_OUT_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 7),
    _ImsMessagesLeavingMTS_OUT_Type()
)
imsMessagesLeavingMTS_OUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsMessagesLeavingMTS_OUT.setStatus("mandatory")
_ImsConnectionsInbound_Type = Integer32
_ImsConnectionsInbound_Object = MibScalar
imsConnectionsInbound = _ImsConnectionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 8),
    _ImsConnectionsInbound_Type()
)
imsConnectionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsInbound.setStatus("mandatory")
_ImsConnectionsOutbound_Type = Integer32
_ImsConnectionsOutbound_Object = MibScalar
imsConnectionsOutbound = _ImsConnectionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 9),
    _ImsConnectionsOutbound_Type()
)
imsConnectionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsOutbound.setStatus("mandatory")
_ImsConnectionsTotalOutbound_Type = Integer32
_ImsConnectionsTotalOutbound_Object = MibScalar
imsConnectionsTotalOutbound = _ImsConnectionsTotalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 10),
    _ImsConnectionsTotalOutbound_Type()
)
imsConnectionsTotalOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsTotalOutbound.setStatus("mandatory")
_ImsConnectionsTotalInbound_Type = Integer32
_ImsConnectionsTotalInbound_Object = MibScalar
imsConnectionsTotalInbound = _ImsConnectionsTotalInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 11),
    _ImsConnectionsTotalInbound_Type()
)
imsConnectionsTotalInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsTotalInbound.setStatus("mandatory")
_ImsConnectionsTotalRejected_Type = Integer32
_ImsConnectionsTotalRejected_Object = MibScalar
imsConnectionsTotalRejected = _ImsConnectionsTotalRejected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 12),
    _ImsConnectionsTotalRejected_Type()
)
imsConnectionsTotalRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsTotalRejected.setStatus("mandatory")
_ImsConnectionsTotalFailed_Type = Integer32
_ImsConnectionsTotalFailed_Object = MibScalar
imsConnectionsTotalFailed = _ImsConnectionsTotalFailed_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 13),
    _ImsConnectionsTotalFailed_Type()
)
imsConnectionsTotalFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsConnectionsTotalFailed.setStatus("mandatory")
_ImsQueuedOutbound_Type = Integer32
_ImsQueuedOutbound_Object = MibScalar
imsQueuedOutbound = _ImsQueuedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 14),
    _ImsQueuedOutbound_Type()
)
imsQueuedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsQueuedOutbound.setStatus("mandatory")
_ImsQueuedInbound_Type = Integer32
_ImsQueuedInbound_Object = MibScalar
imsQueuedInbound = _ImsQueuedInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 15),
    _ImsQueuedInbound_Type()
)
imsQueuedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsQueuedInbound.setStatus("mandatory")
_ImsNDRsTotalInbound_Type = Integer32
_ImsNDRsTotalInbound_Object = MibScalar
imsNDRsTotalInbound = _ImsNDRsTotalInbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 16),
    _ImsNDRsTotalInbound_Type()
)
imsNDRsTotalInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsNDRsTotalInbound.setStatus("mandatory")
_ImsNDRsTotalOutbound_Type = Integer32
_ImsNDRsTotalOutbound_Object = MibScalar
imsNDRsTotalOutbound = _ImsNDRsTotalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 17),
    _ImsNDRsTotalOutbound_Type()
)
imsNDRsTotalOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsNDRsTotalOutbound.setStatus("mandatory")
_ImsTotalInboundKilobytes_Type = Integer32
_ImsTotalInboundKilobytes_Object = MibScalar
imsTotalInboundKilobytes = _ImsTotalInboundKilobytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 18),
    _ImsTotalInboundKilobytes_Type()
)
imsTotalInboundKilobytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalInboundKilobytes.setStatus("mandatory")
_ImsTotalOutboundKilobytes_Type = Integer32
_ImsTotalOutboundKilobytes_Object = MibScalar
imsTotalOutboundKilobytes = _ImsTotalOutboundKilobytes_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 19),
    _ImsTotalOutboundKilobytes_Type()
)
imsTotalOutboundKilobytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalOutboundKilobytes.setStatus("mandatory")
_ImsInboundMessagesTotal_Type = Integer32
_ImsInboundMessagesTotal_Object = MibScalar
imsInboundMessagesTotal = _ImsInboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 20),
    _ImsInboundMessagesTotal_Type()
)
imsInboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsInboundMessagesTotal.setStatus("mandatory")
_ImsOutboundMessagesTotal_Type = Integer32
_ImsOutboundMessagesTotal_Object = MibScalar
imsOutboundMessagesTotal = _ImsOutboundMessagesTotal_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 21),
    _ImsOutboundMessagesTotal_Type()
)
imsOutboundMessagesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsOutboundMessagesTotal.setStatus("mandatory")
_ImsInboundBytesPerHr_Type = Integer32
_ImsInboundBytesPerHr_Object = MibScalar
imsInboundBytesPerHr = _ImsInboundBytesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 22),
    _ImsInboundBytesPerHr_Type()
)
imsInboundBytesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsInboundBytesPerHr.setStatus("mandatory")
_ImsOutboundBytesPerHr_Type = Integer32
_ImsOutboundBytesPerHr_Object = MibScalar
imsOutboundBytesPerHr = _ImsOutboundBytesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 23),
    _ImsOutboundBytesPerHr_Type()
)
imsOutboundBytesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsOutboundBytesPerHr.setStatus("mandatory")
_ImsInboundMessagesPerHr_Type = Integer32
_ImsInboundMessagesPerHr_Object = MibScalar
imsInboundMessagesPerHr = _ImsInboundMessagesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 24),
    _ImsInboundMessagesPerHr_Type()
)
imsInboundMessagesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsInboundMessagesPerHr.setStatus("mandatory")
_ImsOutboundMessagesPerHr_Type = Integer32
_ImsOutboundMessagesPerHr_Object = MibScalar
imsOutboundMessagesPerHr = _ImsOutboundMessagesPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 25),
    _ImsOutboundMessagesPerHr_Type()
)
imsOutboundMessagesPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsOutboundMessagesPerHr.setStatus("mandatory")
_ImsOutboundConnectionsPerHr_Type = Integer32
_ImsOutboundConnectionsPerHr_Object = MibScalar
imsOutboundConnectionsPerHr = _ImsOutboundConnectionsPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 26),
    _ImsOutboundConnectionsPerHr_Type()
)
imsOutboundConnectionsPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsOutboundConnectionsPerHr.setStatus("mandatory")
_ImsInboundConnectionsPerHr_Type = Integer32
_ImsInboundConnectionsPerHr_Object = MibScalar
imsInboundConnectionsPerHr = _ImsInboundConnectionsPerHr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 27),
    _ImsInboundConnectionsPerHr_Type()
)
imsInboundConnectionsPerHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsInboundConnectionsPerHr.setStatus("mandatory")
_ImsTotalMessagesQueued_Type = Integer32
_ImsTotalMessagesQueued_Object = MibScalar
imsTotalMessagesQueued = _ImsTotalMessagesQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 28),
    _ImsTotalMessagesQueued_Type()
)
imsTotalMessagesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalMessagesQueued.setStatus("mandatory")
_ImsTotalKilobytesQueued_Type = Integer32
_ImsTotalKilobytesQueued_Object = MibScalar
imsTotalKilobytesQueued = _ImsTotalKilobytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 29),
    _ImsTotalKilobytesQueued_Type()
)
imsTotalKilobytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalKilobytesQueued.setStatus("mandatory")
_ImsTotalInboundRecipients_Type = Integer32
_ImsTotalInboundRecipients_Object = MibScalar
imsTotalInboundRecipients = _ImsTotalInboundRecipients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 30),
    _ImsTotalInboundRecipients_Type()
)
imsTotalInboundRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalInboundRecipients.setStatus("mandatory")
_ImsTotalOutboundRecipients_Type = Integer32
_ImsTotalOutboundRecipients_Object = MibScalar
imsTotalOutboundRecipients = _ImsTotalOutboundRecipients_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 31),
    _ImsTotalOutboundRecipients_Type()
)
imsTotalOutboundRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalOutboundRecipients.setStatus("mandatory")
_ImsTotalRecipientsQueued_Type = Integer32
_ImsTotalRecipientsQueued_Object = MibScalar
imsTotalRecipientsQueued = _ImsTotalRecipientsQueued_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 32),
    _ImsTotalRecipientsQueued_Type()
)
imsTotalRecipientsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalRecipientsQueued.setStatus("mandatory")
_ImsTotalSuccessfulConversions_Type = Integer32
_ImsTotalSuccessfulConversions_Object = MibScalar
imsTotalSuccessfulConversions = _ImsTotalSuccessfulConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 33),
    _ImsTotalSuccessfulConversions_Type()
)
imsTotalSuccessfulConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalSuccessfulConversions.setStatus("mandatory")
_ImsTotalFailedConversions_Type = Integer32
_ImsTotalFailedConversions_Object = MibScalar
imsTotalFailedConversions = _ImsTotalFailedConversions_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 34),
    _ImsTotalFailedConversions_Type()
)
imsTotalFailedConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalFailedConversions.setStatus("mandatory")
_ImsTotalLoopsDetected_Type = Integer32
_ImsTotalLoopsDetected_Object = MibScalar
imsTotalLoopsDetected = _ImsTotalLoopsDetected_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 1, 3, 1, 1, 3, 35),
    _ImsTotalLoopsDetected_Type()
)
imsTotalLoopsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsTotalLoopsDetected.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WINDOWS-NT-PERFORMANCE-EXCHANGE",
    **{"microsoft": microsoft,
       "software": software,
       "systems": systems,
       "os": os,
       "winnt": winnt,
       "performance": performance,
       "mSExchangeMTA": mSExchangeMTA,
       "mtaAdjacentMTAAssociations": mtaAdjacentMTAAssociations,
       "mtaMessagesPerSec": mtaMessagesPerSec,
       "mtaMessageBytesPerSec": mtaMessageBytesPerSec,
       "mtaFreeElements": mtaFreeElements,
       "mtaFreeHeaders": mtaFreeHeaders,
       "mtaAdminConnections": mtaAdminConnections,
       "mtaThreadsInUse": mtaThreadsInUse,
       "mtaWorkQueueLength": mtaWorkQueueLength,
       "mtaXAPIGateways": mtaXAPIGateways,
       "mtaXAPIClients": mtaXAPIClients,
       "mtaDiskFileDeletesPerSec": mtaDiskFileDeletesPerSec,
       "mtaDiskFileSyncsPerSec": mtaDiskFileSyncsPerSec,
       "mtaDiskFileOpensPerSec": mtaDiskFileOpensPerSec,
       "mtaDiskFileReadsPerSec": mtaDiskFileReadsPerSec,
       "mtaDiskFileWritesPerSec": mtaDiskFileWritesPerSec,
       "mtaExDSReadCallsPerSec": mtaExDSReadCallsPerSec,
       "mtaXAPIReceiveBytesPerSec": mtaXAPIReceiveBytesPerSec,
       "mtaXAPITransmitBytesPerSec": mtaXAPITransmitBytesPerSec,
       "mtaAdminInterfaceReceiveBytesPerSec": mtaAdminInterfaceReceiveBytesPerSec,
       "mtaAdminInterfaceTransmitBytesPerSec": mtaAdminInterfaceTransmitBytesPerSec,
       "mtaLANReceiveBytesPerSec": mtaLANReceiveBytesPerSec,
       "mtaLANTransmitBytesPerSec": mtaLANTransmitBytesPerSec,
       "mtaRASReceiveBytesPerSec": mtaRASReceiveBytesPerSec,
       "mtaRASTransmitBytesPerSec": mtaRASTransmitBytesPerSec,
       "mtaTCPPerIPReceiveBytesPerSec": mtaTCPPerIPReceiveBytesPerSec,
       "mtaTCPPerIPTransmitBytesPerSec": mtaTCPPerIPTransmitBytesPerSec,
       "mtaTP4ReceiveBytesPerSec": mtaTP4ReceiveBytesPerSec,
       "mtaTP4TransmitBytesPerSec": mtaTP4TransmitBytesPerSec,
       "mtaX25ReceiveBytesPerSec": mtaX25ReceiveBytesPerSec,
       "mtaX25TransmitBytesPerSec": mtaX25TransmitBytesPerSec,
       "mtaDeferredDeliveryMsgs": mtaDeferredDeliveryMsgs,
       "mtaTotalRecipientsQueued": mtaTotalRecipientsQueued,
       "mtaTotalSuccessfulConversions": mtaTotalSuccessfulConversions,
       "mtaTotalFailedConversions": mtaTotalFailedConversions,
       "mtaTotalLoopsDetected": mtaTotalLoopsDetected,
       "mtaInboundMessagesTotal": mtaInboundMessagesTotal,
       "mtaOutboundMessagesTotal": mtaOutboundMessagesTotal,
       "mtaInboundBytesTotal": mtaInboundBytesTotal,
       "mtaWorkQueueBytes": mtaWorkQueueBytes,
       "mtaOutboundBytesTotal": mtaOutboundBytesTotal,
       "mtaTotalRecipientsInbound": mtaTotalRecipientsInbound,
       "mtaTotalRecipientsOutbound": mtaTotalRecipientsOutbound,
       "connmSExchangeMTA-ConnectionsTable": connmSExchangeMTA_ConnectionsTable,
       "connmSExchangeMTA-ConnectionsEntry": connmSExchangeMTA_ConnectionsEntry,
       "connmSExchangeMTA-ConnectionsIndex": connmSExchangeMTA_ConnectionsIndex,
       "connmSExchangeMTA-ConnectionsInstance": connmSExchangeMTA_ConnectionsInstance,
       "connAssociations": connAssociations,
       "connReceiveBytesPerSec": connReceiveBytesPerSec,
       "connSendBytesPerSec": connSendBytesPerSec,
       "connReceiveMessagesPerSec": connReceiveMessagesPerSec,
       "connSendMessagesPerSec": connSendMessagesPerSec,
       "connQueueLength": connQueueLength,
       "connConnectorIndex": connConnectorIndex,
       "connInboundRejectedTotal": connInboundRejectedTotal,
       "connTotalRecipientsQueued": connTotalRecipientsQueued,
       "connOldestMessageQueued": connOldestMessageQueued,
       "connCurrentInboundAssociations": connCurrentInboundAssociations,
       "connCurrentOutboundAssociations": connCurrentOutboundAssociations,
       "connCumulativeInboundAssociations": connCumulativeInboundAssociations,
       "connCumulativeOutboundAssociations": connCumulativeOutboundAssociations,
       "connLastInboundAssociation": connLastInboundAssociation,
       "connLastOutboundAssociation": connLastOutboundAssociation,
       "connRejectedInboundAssociations": connRejectedInboundAssociations,
       "connFailedOutboundAssociations": connFailedOutboundAssociations,
       "connNextAssociationRetry": connNextAssociationRetry,
       "connInboundRejectReason": connInboundRejectReason,
       "connOutboundFailureReason": connOutboundFailureReason,
       "connInboundMessagesTotal": connInboundMessagesTotal,
       "connOutboundMessagesTotal": connOutboundMessagesTotal,
       "connInboundBytesTotal": connInboundBytesTotal,
       "connQueuedBytes": connQueuedBytes,
       "connOutboundBytesTotal": connOutboundBytesTotal,
       "connTotalRecipientsInbound": connTotalRecipientsInbound,
       "connTotalRecipientsOutbound": connTotalRecipientsOutbound,
       "mSExchangeIMC": mSExchangeIMC,
       "imsQueuedMTS-IN": imsQueuedMTS_IN,
       "imsBytesQueuedMTS-IN": imsBytesQueuedMTS_IN,
       "imsMessagesEnteringMTS-IN": imsMessagesEnteringMTS_IN,
       "imsQueuedMTS-OUT": imsQueuedMTS_OUT,
       "imsBytesQueuedMTS-OUT": imsBytesQueuedMTS_OUT,
       "imsMessagesEnteringMTS-OUT": imsMessagesEnteringMTS_OUT,
       "imsMessagesLeavingMTS-OUT": imsMessagesLeavingMTS_OUT,
       "imsConnectionsInbound": imsConnectionsInbound,
       "imsConnectionsOutbound": imsConnectionsOutbound,
       "imsConnectionsTotalOutbound": imsConnectionsTotalOutbound,
       "imsConnectionsTotalInbound": imsConnectionsTotalInbound,
       "imsConnectionsTotalRejected": imsConnectionsTotalRejected,
       "imsConnectionsTotalFailed": imsConnectionsTotalFailed,
       "imsQueuedOutbound": imsQueuedOutbound,
       "imsQueuedInbound": imsQueuedInbound,
       "imsNDRsTotalInbound": imsNDRsTotalInbound,
       "imsNDRsTotalOutbound": imsNDRsTotalOutbound,
       "imsTotalInboundKilobytes": imsTotalInboundKilobytes,
       "imsTotalOutboundKilobytes": imsTotalOutboundKilobytes,
       "imsInboundMessagesTotal": imsInboundMessagesTotal,
       "imsOutboundMessagesTotal": imsOutboundMessagesTotal,
       "imsInboundBytesPerHr": imsInboundBytesPerHr,
       "imsOutboundBytesPerHr": imsOutboundBytesPerHr,
       "imsInboundMessagesPerHr": imsInboundMessagesPerHr,
       "imsOutboundMessagesPerHr": imsOutboundMessagesPerHr,
       "imsOutboundConnectionsPerHr": imsOutboundConnectionsPerHr,
       "imsInboundConnectionsPerHr": imsInboundConnectionsPerHr,
       "imsTotalMessagesQueued": imsTotalMessagesQueued,
       "imsTotalKilobytesQueued": imsTotalKilobytesQueued,
       "imsTotalInboundRecipients": imsTotalInboundRecipients,
       "imsTotalOutboundRecipients": imsTotalOutboundRecipients,
       "imsTotalRecipientsQueued": imsTotalRecipientsQueued,
       "imsTotalSuccessfulConversions": imsTotalSuccessfulConversions,
       "imsTotalFailedConversions": imsTotalFailedConversions,
       "imsTotalLoopsDetected": imsTotalLoopsDetected}
)
