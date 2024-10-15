# SNMP MIB module (BW-BroadworksXtendedServicesPlatform) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksXtendedServicesPlatform
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:05 2024
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

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2008-10-28 10:54",
         "2008-07-18 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_BwXtendedServicesPlatform_ObjectIdentity = ObjectIdentity
bwXtendedServicesPlatform = _BwXtendedServicesPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12)
)
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1)
)
_Bcct_ObjectIdentity = ObjectIdentity
bcct = _Bcct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1)
)
_BwXspCommonCommStatsTable_Object = MibTable
bwXspCommonCommStatsTable = _BwXspCommonCommStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bwXspCommonCommStatsTable.setStatus("current")
_BwXspCommonCommStatsEntry_Object = MibTableRow
bwXspCommonCommStatsEntry = _BwXspCommonCommStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1)
)
bwXspCommonCommStatsEntry.setIndexNames(
    (0, "BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommStatsIndex"),
)
if mibBuilder.loadTexts:
    bwXspCommonCommStatsEntry.setStatus("current")
_BwXspCommonCommStatsIndex_Type = Unsigned32
_BwXspCommonCommStatsIndex_Object = MibTableColumn
bwXspCommonCommStatsIndex = _BwXspCommonCommStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 1),
    _BwXspCommonCommStatsIndex_Type()
)
bwXspCommonCommStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwXspCommonCommStatsIndex.setStatus("current")
_BwXspCommonCommHost_Type = DisplayString
_BwXspCommonCommHost_Object = MibTableColumn
bwXspCommonCommHost = _BwXspCommonCommHost_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 2),
    _BwXspCommonCommHost_Type()
)
bwXspCommonCommHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwXspCommonCommHost.setStatus("current")
_BwXspCommonCommInterface_Type = DisplayString
_BwXspCommonCommInterface_Object = MibTableColumn
bwXspCommonCommInterface = _BwXspCommonCommInterface_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 3),
    _BwXspCommonCommInterface_Type()
)
bwXspCommonCommInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwXspCommonCommInterface.setStatus("current")
_BwXspCommonCommProtocol_Type = DisplayString
_BwXspCommonCommProtocol_Object = MibTableColumn
bwXspCommonCommProtocol = _BwXspCommonCommProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 4),
    _BwXspCommonCommProtocol_Type()
)
bwXspCommonCommProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwXspCommonCommProtocol.setStatus("current")
_BwXspCommonCommAcceptedOutboundConnections_Type = Counter32
_BwXspCommonCommAcceptedOutboundConnections_Object = MibTableColumn
bwXspCommonCommAcceptedOutboundConnections = _BwXspCommonCommAcceptedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 5),
    _BwXspCommonCommAcceptedOutboundConnections_Type()
)
bwXspCommonCommAcceptedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommAcceptedOutboundConnections.setStatus("current")
_BwXspCommonCommAcceptedInboundConnections_Type = Counter32
_BwXspCommonCommAcceptedInboundConnections_Object = MibTableColumn
bwXspCommonCommAcceptedInboundConnections = _BwXspCommonCommAcceptedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 6),
    _BwXspCommonCommAcceptedInboundConnections_Type()
)
bwXspCommonCommAcceptedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommAcceptedInboundConnections.setStatus("current")
_BwXspCommonCommRejectedOutboundConnections_Type = Counter32
_BwXspCommonCommRejectedOutboundConnections_Object = MibTableColumn
bwXspCommonCommRejectedOutboundConnections = _BwXspCommonCommRejectedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 7),
    _BwXspCommonCommRejectedOutboundConnections_Type()
)
bwXspCommonCommRejectedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommRejectedOutboundConnections.setStatus("current")
_BwXspCommonCommRejectedInboundConnections_Type = Counter32
_BwXspCommonCommRejectedInboundConnections_Object = MibTableColumn
bwXspCommonCommRejectedInboundConnections = _BwXspCommonCommRejectedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 8),
    _BwXspCommonCommRejectedInboundConnections_Type()
)
bwXspCommonCommRejectedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommRejectedInboundConnections.setStatus("current")
_BwXspCommonCommOutputMessagesProcessed_Type = Counter32
_BwXspCommonCommOutputMessagesProcessed_Object = MibTableColumn
bwXspCommonCommOutputMessagesProcessed = _BwXspCommonCommOutputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 9),
    _BwXspCommonCommOutputMessagesProcessed_Type()
)
bwXspCommonCommOutputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommOutputMessagesProcessed.setStatus("current")
_BwXspCommonCommInputMessagesProcessed_Type = Counter32
_BwXspCommonCommInputMessagesProcessed_Object = MibTableColumn
bwXspCommonCommInputMessagesProcessed = _BwXspCommonCommInputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 10),
    _BwXspCommonCommInputMessagesProcessed_Type()
)
bwXspCommonCommInputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommInputMessagesProcessed.setStatus("current")
_BwXspCommonCommOutputCommunicationErrors_Type = Counter32
_BwXspCommonCommOutputCommunicationErrors_Object = MibTableColumn
bwXspCommonCommOutputCommunicationErrors = _BwXspCommonCommOutputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 11),
    _BwXspCommonCommOutputCommunicationErrors_Type()
)
bwXspCommonCommOutputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommOutputCommunicationErrors.setStatus("current")
_BwXspCommonCommInputCommunicationErrors_Type = Counter32
_BwXspCommonCommInputCommunicationErrors_Object = MibTableColumn
bwXspCommonCommInputCommunicationErrors = _BwXspCommonCommInputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 1, 1, 1, 12),
    _BwXspCommonCommInputCommunicationErrors_Type()
)
bwXspCommonCommInputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspCommonCommInputCommunicationErrors.setStatus("current")
_Auth_ObjectIdentity = ObjectIdentity
auth = _Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 2)
)
_BwXspAuthenticationAttempts_Type = Counter32
_BwXspAuthenticationAttempts_Object = MibScalar
bwXspAuthenticationAttempts = _BwXspAuthenticationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 2, 1),
    _BwXspAuthenticationAttempts_Type()
)
bwXspAuthenticationAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspAuthenticationAttempts.setStatus("current")
_BwXspAuthenticationFailed_Type = Counter32
_BwXspAuthenticationFailed_Object = MibScalar
bwXspAuthenticationFailed = _BwXspAuthenticationFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 2, 2),
    _BwXspAuthenticationFailed_Type()
)
bwXspAuthenticationFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspAuthenticationFailed.setStatus("current")
_Oci_ObjectIdentity = ObjectIdentity
oci = _Oci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3)
)
_BwXspOCIRequests_Type = Counter32
_BwXspOCIRequests_Object = MibScalar
bwXspOCIRequests = _BwXspOCIRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 1),
    _BwXspOCIRequests_Type()
)
bwXspOCIRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCIRequests.setStatus("current")
_BwXspOCIResponses_Type = Counter32
_BwXspOCIResponses_Object = MibScalar
bwXspOCIResponses = _BwXspOCIResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 2),
    _BwXspOCIResponses_Type()
)
bwXspOCIResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCIResponses.setStatus("current")
_BwXspOCIUnauthorizedMessage_Type = Counter32
_BwXspOCIUnauthorizedMessage_Object = MibScalar
bwXspOCIUnauthorizedMessage = _BwXspOCIUnauthorizedMessage_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 3),
    _BwXspOCIUnauthorizedMessage_Type()
)
bwXspOCIUnauthorizedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCIUnauthorizedMessage.setStatus("current")
_BwXspOCICRequests_Type = Counter32
_BwXspOCICRequests_Object = MibScalar
bwXspOCICRequests = _BwXspOCICRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 4),
    _BwXspOCICRequests_Type()
)
bwXspOCICRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICRequests.setStatus("current")
_BwXspOCICResponses_Type = Counter32
_BwXspOCICResponses_Object = MibScalar
bwXspOCICResponses = _BwXspOCICResponses_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 5),
    _BwXspOCICResponses_Type()
)
bwXspOCICResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICResponses.setStatus("current")
_BwXspOCICMessagesReceived_Type = Counter32
_BwXspOCICMessagesReceived_Object = MibScalar
bwXspOCICMessagesReceived = _BwXspOCICMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 6),
    _BwXspOCICMessagesReceived_Type()
)
bwXspOCICMessagesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICMessagesReceived.setStatus("current")
_BwXspOCICMessagesRejected_Type = Counter32
_BwXspOCICMessagesRejected_Object = MibScalar
bwXspOCICMessagesRejected = _BwXspOCICMessagesRejected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 7),
    _BwXspOCICMessagesRejected_Type()
)
bwXspOCICMessagesRejected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICMessagesRejected.setStatus("current")
_BwXspOCICMessagesDelivered_Type = Counter32
_BwXspOCICMessagesDelivered_Object = MibScalar
bwXspOCICMessagesDelivered = _BwXspOCICMessagesDelivered_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 8),
    _BwXspOCICMessagesDelivered_Type()
)
bwXspOCICMessagesDelivered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICMessagesDelivered.setStatus("current")
_BwXspOCICMessagesReplied_Type = Counter32
_BwXspOCICMessagesReplied_Object = MibScalar
bwXspOCICMessagesReplied = _BwXspOCICMessagesReplied_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 3, 9),
    _BwXspOCICMessagesReplied_Type()
)
bwXspOCICMessagesReplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspOCICMessagesReplied.setStatus("current")
_NsLocationAPI_ObjectIdentity = ObjectIdentity
nsLocationAPI = _NsLocationAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 4)
)
_BwXspNsLocAPIAttempts_Type = Counter32
_BwXspNsLocAPIAttempts_Object = MibScalar
bwXspNsLocAPIAttempts = _BwXspNsLocAPIAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 4, 1),
    _BwXspNsLocAPIAttempts_Type()
)
bwXspNsLocAPIAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspNsLocAPIAttempts.setStatus("current")
_BwXspNsLocAPIResponseFailed_Type = Counter32
_BwXspNsLocAPIResponseFailed_Object = MibScalar
bwXspNsLocAPIResponseFailed = _BwXspNsLocAPIResponseFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 4, 2),
    _BwXspNsLocAPIResponseFailed_Type()
)
bwXspNsLocAPIResponseFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspNsLocAPIResponseFailed.setStatus("current")
_NsPortalAPI_ObjectIdentity = ObjectIdentity
nsPortalAPI = _NsPortalAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 5)
)
_BwXspNsASDiscoveryAttempts_Type = Counter32
_BwXspNsASDiscoveryAttempts_Object = MibScalar
bwXspNsASDiscoveryAttempts = _BwXspNsASDiscoveryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 5, 1),
    _BwXspNsASDiscoveryAttempts_Type()
)
bwXspNsASDiscoveryAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspNsASDiscoveryAttempts.setStatus("current")
_BwXspNsASDiscoveryAttemptsFailed_Type = Counter32
_BwXspNsASDiscoveryAttemptsFailed_Object = MibScalar
bwXspNsASDiscoveryAttemptsFailed = _BwXspNsASDiscoveryAttemptsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1, 5, 2),
    _BwXspNsASDiscoveryAttemptsFailed_Type()
)
bwXspNsASDiscoveryAttemptsFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwXspNsASDiscoveryAttemptsFailed.setStatus("current")
_BwXspMibConformance_ObjectIdentity = ObjectIdentity
bwXspMibConformance = _BwXspMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000)
)
_BwXspMibGroups_ObjectIdentity = ObjectIdentity
bwXspMibGroups = _BwXspMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1)
)
_BwXspMibCompliancy_ObjectIdentity = ObjectIdentity
bwXspMibCompliancy = _BwXspMibCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 2)
)

# Managed Objects groups

bwXspBcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1, 1)
)
bwXspBcctGroup.setObjects(
      *(("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommStatsIndex"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommHost"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommInterface"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommProtocol"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommAcceptedOutboundConnections"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommAcceptedInboundConnections"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommRejectedOutboundConnections"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommRejectedInboundConnections"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommOutputMessagesProcessed"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommInputMessagesProcessed"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommOutputCommunicationErrors"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspCommonCommInputCommunicationErrors"))
)
if mibBuilder.loadTexts:
    bwXspBcctGroup.setStatus("current")

bwXspAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1, 2)
)
bwXspAuthGroup.setObjects(
      *(("BW-BroadworksXtendedServicesPlatform", "bwXspAuthenticationAttempts"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspAuthenticationFailed"))
)
if mibBuilder.loadTexts:
    bwXspAuthGroup.setStatus("current")

bwXspOciGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1, 3)
)
bwXspOciGroup.setObjects(
      *(("BW-BroadworksXtendedServicesPlatform", "bwXspOCIRequests"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCIResponses"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCIUnauthorizedMessage"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICRequests"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICResponses"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICMessagesReceived"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICMessagesRejected"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICMessagesDelivered"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspOCICMessagesReplied"))
)
if mibBuilder.loadTexts:
    bwXspOciGroup.setStatus("current")

bwXspNsLocAPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1, 4)
)
bwXspNsLocAPIGroup.setObjects(
      *(("BW-BroadworksXtendedServicesPlatform", "bwXspNsLocAPIAttempts"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspNsLocAPIResponseFailed"))
)
if mibBuilder.loadTexts:
    bwXspNsLocAPIGroup.setStatus("current")

bwXspNsPortalAPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 1, 5)
)
bwXspNsPortalAPIGroup.setObjects(
      *(("BW-BroadworksXtendedServicesPlatform", "bwXspNsASDiscoveryAttempts"),
        ("BW-BroadworksXtendedServicesPlatform", "bwXspNsASDiscoveryAttemptsFailed"))
)
if mibBuilder.loadTexts:
    bwXspNsPortalAPIGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwXspBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 12, 1000, 2, 1)
)
if mibBuilder.loadTexts:
    bwXspBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksXtendedServicesPlatform",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "bwXtendedServicesPlatform": bwXtendedServicesPlatform,
       "protocols": protocols,
       "bcct": bcct,
       "bwXspCommonCommStatsTable": bwXspCommonCommStatsTable,
       "bwXspCommonCommStatsEntry": bwXspCommonCommStatsEntry,
       "bwXspCommonCommStatsIndex": bwXspCommonCommStatsIndex,
       "bwXspCommonCommHost": bwXspCommonCommHost,
       "bwXspCommonCommInterface": bwXspCommonCommInterface,
       "bwXspCommonCommProtocol": bwXspCommonCommProtocol,
       "bwXspCommonCommAcceptedOutboundConnections": bwXspCommonCommAcceptedOutboundConnections,
       "bwXspCommonCommAcceptedInboundConnections": bwXspCommonCommAcceptedInboundConnections,
       "bwXspCommonCommRejectedOutboundConnections": bwXspCommonCommRejectedOutboundConnections,
       "bwXspCommonCommRejectedInboundConnections": bwXspCommonCommRejectedInboundConnections,
       "bwXspCommonCommOutputMessagesProcessed": bwXspCommonCommOutputMessagesProcessed,
       "bwXspCommonCommInputMessagesProcessed": bwXspCommonCommInputMessagesProcessed,
       "bwXspCommonCommOutputCommunicationErrors": bwXspCommonCommOutputCommunicationErrors,
       "bwXspCommonCommInputCommunicationErrors": bwXspCommonCommInputCommunicationErrors,
       "auth": auth,
       "bwXspAuthenticationAttempts": bwXspAuthenticationAttempts,
       "bwXspAuthenticationFailed": bwXspAuthenticationFailed,
       "oci": oci,
       "bwXspOCIRequests": bwXspOCIRequests,
       "bwXspOCIResponses": bwXspOCIResponses,
       "bwXspOCIUnauthorizedMessage": bwXspOCIUnauthorizedMessage,
       "bwXspOCICRequests": bwXspOCICRequests,
       "bwXspOCICResponses": bwXspOCICResponses,
       "bwXspOCICMessagesReceived": bwXspOCICMessagesReceived,
       "bwXspOCICMessagesRejected": bwXspOCICMessagesRejected,
       "bwXspOCICMessagesDelivered": bwXspOCICMessagesDelivered,
       "bwXspOCICMessagesReplied": bwXspOCICMessagesReplied,
       "nsLocationAPI": nsLocationAPI,
       "bwXspNsLocAPIAttempts": bwXspNsLocAPIAttempts,
       "bwXspNsLocAPIResponseFailed": bwXspNsLocAPIResponseFailed,
       "nsPortalAPI": nsPortalAPI,
       "bwXspNsASDiscoveryAttempts": bwXspNsASDiscoveryAttempts,
       "bwXspNsASDiscoveryAttemptsFailed": bwXspNsASDiscoveryAttemptsFailed,
       "bwXspMibConformance": bwXspMibConformance,
       "bwXspMibGroups": bwXspMibGroups,
       "bwXspBcctGroup": bwXspBcctGroup,
       "bwXspAuthGroup": bwXspAuthGroup,
       "bwXspOciGroup": bwXspOciGroup,
       "bwXspNsLocAPIGroup": bwXspNsLocAPIGroup,
       "bwXspNsPortalAPIGroup": bwXspNsPortalAPIGroup,
       "bwXspMibCompliancy": bwXspMibCompliancy,
       "bwXspBasicCompliance": bwXspBasicCompliance}
)
