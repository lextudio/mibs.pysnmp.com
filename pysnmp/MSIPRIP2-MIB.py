# SNMP MIB module (MSIPRIP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSIPRIP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:58 2024
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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

_Msiprip2_ObjectIdentity = ObjectIdentity
msiprip2 = _Msiprip2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 11)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1)
)
_GlobalSystemRouteChanges_Type = Counter32
_GlobalSystemRouteChanges_Object = MibScalar
globalSystemRouteChanges = _GlobalSystemRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 1),
    _GlobalSystemRouteChanges_Type()
)
globalSystemRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalSystemRouteChanges.setStatus("mandatory")
_GlobalTotalResponseSends_Type = Counter32
_GlobalTotalResponseSends_Object = MibScalar
globalTotalResponseSends = _GlobalTotalResponseSends_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 2),
    _GlobalTotalResponseSends_Type()
)
globalTotalResponseSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTotalResponseSends.setStatus("mandatory")


class _GlobalLoggingLevel_Type(Integer32):
    """Custom type globalLoggingLevel based on Integer32"""
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
        *(("error", 2),
          ("information", 4),
          ("none", 1),
          ("warning", 3))
    )


_GlobalLoggingLevel_Type.__name__ = "Integer32"
_GlobalLoggingLevel_Object = MibScalar
globalLoggingLevel = _GlobalLoggingLevel_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 3),
    _GlobalLoggingLevel_Type()
)
globalLoggingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalLoggingLevel.setStatus("mandatory")
_GlobalMaxRecQueueSize_Type = Integer32
_GlobalMaxRecQueueSize_Object = MibScalar
globalMaxRecQueueSize = _GlobalMaxRecQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 4),
    _GlobalMaxRecQueueSize_Type()
)
globalMaxRecQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalMaxRecQueueSize.setStatus("mandatory")
_GlobalMaxSendQueueSize_Type = Integer32
_GlobalMaxSendQueueSize_Object = MibScalar
globalMaxSendQueueSize = _GlobalMaxSendQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 5),
    _GlobalMaxSendQueueSize_Type()
)
globalMaxSendQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalMaxSendQueueSize.setStatus("mandatory")
_GlobalMinTriggeredUpdateInterval_Type = TimeTicks
_GlobalMinTriggeredUpdateInterval_Object = MibScalar
globalMinTriggeredUpdateInterval = _GlobalMinTriggeredUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 6),
    _GlobalMinTriggeredUpdateInterval_Type()
)
globalMinTriggeredUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalMinTriggeredUpdateInterval.setStatus("mandatory")


class _GlobalPeerFilterMode_Type(Integer32):
    """Custom type globalPeerFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("exclude", 3),
          ("include", 2))
    )


_GlobalPeerFilterMode_Type.__name__ = "Integer32"
_GlobalPeerFilterMode_Object = MibScalar
globalPeerFilterMode = _GlobalPeerFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 7),
    _GlobalPeerFilterMode_Type()
)
globalPeerFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPeerFilterMode.setStatus("mandatory")
_GlobalPeerFilterCount_Type = Integer32
_GlobalPeerFilterCount_Object = MibScalar
globalPeerFilterCount = _GlobalPeerFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 8),
    _GlobalPeerFilterCount_Type()
)
globalPeerFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPeerFilterCount.setStatus("mandatory")
_GlobalPeerFilterTable_Object = MibTable
globalPeerFilterTable = _GlobalPeerFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9)
)
if mibBuilder.loadTexts:
    globalPeerFilterTable.setStatus("mandatory")
_GlobalPeerFilterEntry_Object = MibTableRow
globalPeerFilterEntry = _GlobalPeerFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1)
)
globalPeerFilterEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "globalPFAddr"),
)
if mibBuilder.loadTexts:
    globalPeerFilterEntry.setStatus("mandatory")
_GlobalPFAddr_Type = IpAddress
_GlobalPFAddr_Object = MibTableColumn
globalPFAddr = _GlobalPFAddr_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1, 1),
    _GlobalPFAddr_Type()
)
globalPFAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPFAddr.setStatus("mandatory")


class _GlobalPFTag_Type(Integer32):
    """Custom type globalPFTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_GlobalPFTag_Type.__name__ = "Integer32"
_GlobalPFTag_Object = MibTableColumn
globalPFTag = _GlobalPFTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 1, 9, 1, 2),
    _GlobalPFTag_Type()
)
globalPFTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalPFTag.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2)
)
_IfStatsTable_Object = MibTable
ifStatsTable = _IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    ifStatsTable.setStatus("mandatory")
_IfStatsEntry_Object = MibTableRow
ifStatsEntry = _IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1)
)
ifStatsEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifSEIndex"),
)
if mibBuilder.loadTexts:
    ifStatsEntry.setStatus("mandatory")
_IfSEIndex_Type = Integer32
_IfSEIndex_Object = MibTableColumn
ifSEIndex = _IfSEIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 1),
    _IfSEIndex_Type()
)
ifSEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEIndex.setStatus("mandatory")


class _IfSEState_Type(Integer32):
    """Custom type ifSEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfSEState_Type.__name__ = "Integer32"
_IfSEState_Object = MibTableColumn
ifSEState = _IfSEState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 2),
    _IfSEState_Type()
)
ifSEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEState.setStatus("mandatory")
_IfSESendFailures_Type = Counter32
_IfSESendFailures_Object = MibTableColumn
ifSESendFailures = _IfSESendFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 3),
    _IfSESendFailures_Type()
)
ifSESendFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSESendFailures.setStatus("mandatory")
_IfSEReceiveFailures_Type = Counter32
_IfSEReceiveFailures_Object = MibTableColumn
ifSEReceiveFailures = _IfSEReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 4),
    _IfSEReceiveFailures_Type()
)
ifSEReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEReceiveFailures.setStatus("mandatory")
_IfSERequestSends_Type = Counter32
_IfSERequestSends_Object = MibTableColumn
ifSERequestSends = _IfSERequestSends_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 5),
    _IfSERequestSends_Type()
)
ifSERequestSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSERequestSends.setStatus("mandatory")
_IfSERequestReceiveds_Type = Counter32
_IfSERequestReceiveds_Object = MibTableColumn
ifSERequestReceiveds = _IfSERequestReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 6),
    _IfSERequestReceiveds_Type()
)
ifSERequestReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSERequestReceiveds.setStatus("mandatory")
_IfSEResponseSends_Type = Counter32
_IfSEResponseSends_Object = MibTableColumn
ifSEResponseSends = _IfSEResponseSends_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 7),
    _IfSEResponseSends_Type()
)
ifSEResponseSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEResponseSends.setStatus("mandatory")
_IfSEResponseReceiveds_Type = Counter32
_IfSEResponseReceiveds_Object = MibTableColumn
ifSEResponseReceiveds = _IfSEResponseReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 8),
    _IfSEResponseReceiveds_Type()
)
ifSEResponseReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEResponseReceiveds.setStatus("mandatory")
_IfSEBadResponsePacketReceiveds_Type = Counter32
_IfSEBadResponsePacketReceiveds_Object = MibTableColumn
ifSEBadResponsePacketReceiveds = _IfSEBadResponsePacketReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 9),
    _IfSEBadResponsePacketReceiveds_Type()
)
ifSEBadResponsePacketReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEBadResponsePacketReceiveds.setStatus("mandatory")
_IfSEBadResponseEntriesReceiveds_Type = Counter32
_IfSEBadResponseEntriesReceiveds_Object = MibTableColumn
ifSEBadResponseEntriesReceiveds = _IfSEBadResponseEntriesReceiveds_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 10),
    _IfSEBadResponseEntriesReceiveds_Type()
)
ifSEBadResponseEntriesReceiveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSEBadResponseEntriesReceiveds.setStatus("mandatory")
_IfSETriggeredUpdateSends_Type = Counter32
_IfSETriggeredUpdateSends_Object = MibTableColumn
ifSETriggeredUpdateSends = _IfSETriggeredUpdateSends_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 1, 1, 11),
    _IfSETriggeredUpdateSends_Type()
)
ifSETriggeredUpdateSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSETriggeredUpdateSends.setStatus("mandatory")
_IfConfigTable_Object = MibTable
ifConfigTable = _IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    ifConfigTable.setStatus("mandatory")
_IfConfigEntry_Object = MibTableRow
ifConfigEntry = _IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1)
)
ifConfigEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifCEIndex"),
)
if mibBuilder.loadTexts:
    ifConfigEntry.setStatus("mandatory")
_IfCEIndex_Type = Integer32
_IfCEIndex_Object = MibTableColumn
ifCEIndex = _IfCEIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 1),
    _IfCEIndex_Type()
)
ifCEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCEIndex.setStatus("mandatory")


class _IfCEState_Type(Integer32):
    """Custom type ifCEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfCEState_Type.__name__ = "Integer32"
_IfCEState_Object = MibTableColumn
ifCEState = _IfCEState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 2),
    _IfCEState_Type()
)
ifCEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCEState.setStatus("mandatory")


class _IfCEMetric_Type(Integer32):
    """Custom type ifCEMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_IfCEMetric_Type.__name__ = "Integer32"
_IfCEMetric_Object = MibTableColumn
ifCEMetric = _IfCEMetric_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 3),
    _IfCEMetric_Type()
)
ifCEMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEMetric.setStatus("mandatory")


class _IfCEUpdateMode_Type(Integer32):
    """Custom type ifCEUpdateMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demand", 2),
          ("periodic", 1))
    )


_IfCEUpdateMode_Type.__name__ = "Integer32"
_IfCEUpdateMode_Object = MibTableColumn
ifCEUpdateMode = _IfCEUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 4),
    _IfCEUpdateMode_Type()
)
ifCEUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEUpdateMode.setStatus("mandatory")


class _IfCEAcceptMode_Type(Integer32):
    """Custom type ifCEAcceptMode based on Integer32"""
    defaultValue = 3

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
        *(("disable", 1),
          ("rip1", 2),
          ("rip1Compat", 3),
          ("rip2", 4))
    )


_IfCEAcceptMode_Type.__name__ = "Integer32"
_IfCEAcceptMode_Object = MibTableColumn
ifCEAcceptMode = _IfCEAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 5),
    _IfCEAcceptMode_Type()
)
ifCEAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAcceptMode.setStatus("mandatory")


class _IfCEAnnounceMode_Type(Integer32):
    """Custom type ifCEAnnounceMode based on Integer32"""
    defaultValue = 3

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
        *(("disable", 1),
          ("rip1", 2),
          ("rip1Compat", 3),
          ("rip2", 4))
    )


_IfCEAnnounceMode_Type.__name__ = "Integer32"
_IfCEAnnounceMode_Object = MibTableColumn
ifCEAnnounceMode = _IfCEAnnounceMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 6),
    _IfCEAnnounceMode_Type()
)
ifCEAnnounceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAnnounceMode.setStatus("mandatory")


class _IfCEProtocolFlags_Type(Integer32):
    """Custom type ifCEProtocolFlags based on Integer32"""
    defaultValue = 240


_IfCEProtocolFlags_Object = MibTableColumn
ifCEProtocolFlags = _IfCEProtocolFlags_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 7),
    _IfCEProtocolFlags_Type()
)
ifCEProtocolFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEProtocolFlags.setStatus("mandatory")


class _IfCERouteExpirationInterval_Type(TimeTicks):
    """Custom type ifCERouteExpirationInterval based on TimeTicks"""
    defaultValue = 180


_IfCERouteExpirationInterval_Object = MibTableColumn
ifCERouteExpirationInterval = _IfCERouteExpirationInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 8),
    _IfCERouteExpirationInterval_Type()
)
ifCERouteExpirationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCERouteExpirationInterval.setStatus("mandatory")


class _IfCERouteRemovalInterval_Type(TimeTicks):
    """Custom type ifCERouteRemovalInterval based on TimeTicks"""
    defaultValue = 120


_IfCERouteRemovalInterval_Object = MibTableColumn
ifCERouteRemovalInterval = _IfCERouteRemovalInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 9),
    _IfCERouteRemovalInterval_Type()
)
ifCERouteRemovalInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCERouteRemovalInterval.setStatus("mandatory")


class _IfCEFullUpdateInterval_Type(TimeTicks):
    """Custom type ifCEFullUpdateInterval based on TimeTicks"""
    defaultValue = 30


_IfCEFullUpdateInterval_Object = MibTableColumn
ifCEFullUpdateInterval = _IfCEFullUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 10),
    _IfCEFullUpdateInterval_Type()
)
ifCEFullUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCEFullUpdateInterval.setStatus("mandatory")


class _IfCEAuthenticationType_Type(Integer32):
    """Custom type ifCEAuthenticationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_IfCEAuthenticationType_Type.__name__ = "Integer32"
_IfCEAuthenticationType_Object = MibTableColumn
ifCEAuthenticationType = _IfCEAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 11),
    _IfCEAuthenticationType_Type()
)
ifCEAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAuthenticationType.setStatus("mandatory")


class _IfCEAuthenticationKey_Type(OctetString):
    """Custom type ifCEAuthenticationKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IfCEAuthenticationKey_Type.__name__ = "OctetString"
_IfCEAuthenticationKey_Object = MibTableColumn
ifCEAuthenticationKey = _IfCEAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 12),
    _IfCEAuthenticationKey_Type()
)
ifCEAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAuthenticationKey.setStatus("mandatory")


class _IfCERouteTag_Type(Integer32):
    """Custom type ifCERouteTag based on Integer32"""
    defaultValue = 0


_IfCERouteTag_Object = MibTableColumn
ifCERouteTag = _IfCERouteTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 13),
    _IfCERouteTag_Type()
)
ifCERouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCERouteTag.setStatus("mandatory")


class _IfCEUnicastPeerMode_Type(Integer32):
    """Custom type ifCEUnicastPeerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("peerAlso", 2),
          ("peerOnly", 3))
    )


_IfCEUnicastPeerMode_Type.__name__ = "Integer32"
_IfCEUnicastPeerMode_Object = MibTableColumn
ifCEUnicastPeerMode = _IfCEUnicastPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 14),
    _IfCEUnicastPeerMode_Type()
)
ifCEUnicastPeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEUnicastPeerMode.setStatus("mandatory")


class _IfCEAcceptFilterMode_Type(Integer32):
    """Custom type ifCEAcceptFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("exclude", 3),
          ("include", 2))
    )


_IfCEAcceptFilterMode_Type.__name__ = "Integer32"
_IfCEAcceptFilterMode_Object = MibTableColumn
ifCEAcceptFilterMode = _IfCEAcceptFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 15),
    _IfCEAcceptFilterMode_Type()
)
ifCEAcceptFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAcceptFilterMode.setStatus("mandatory")


class _IfCEAnnounceFilterMode_Type(Integer32):
    """Custom type ifCEAnnounceFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("exclude", 3),
          ("include", 2))
    )


_IfCEAnnounceFilterMode_Type.__name__ = "Integer32"
_IfCEAnnounceFilterMode_Object = MibTableColumn
ifCEAnnounceFilterMode = _IfCEAnnounceFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 16),
    _IfCEAnnounceFilterMode_Type()
)
ifCEAnnounceFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAnnounceFilterMode.setStatus("mandatory")


class _IfCEUnicastPeerCount_Type(Integer32):
    """Custom type ifCEUnicastPeerCount based on Integer32"""
    defaultValue = 0


_IfCEUnicastPeerCount_Object = MibTableColumn
ifCEUnicastPeerCount = _IfCEUnicastPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 17),
    _IfCEUnicastPeerCount_Type()
)
ifCEUnicastPeerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEUnicastPeerCount.setStatus("mandatory")


class _IfCEAcceptFilterCount_Type(Integer32):
    """Custom type ifCEAcceptFilterCount based on Integer32"""
    defaultValue = 0


_IfCEAcceptFilterCount_Object = MibTableColumn
ifCEAcceptFilterCount = _IfCEAcceptFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 18),
    _IfCEAcceptFilterCount_Type()
)
ifCEAcceptFilterCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAcceptFilterCount.setStatus("mandatory")


class _IfCEAnnounceFilterCount_Type(Integer32):
    """Custom type ifCEAnnounceFilterCount based on Integer32"""
    defaultValue = 0


_IfCEAnnounceFilterCount_Object = MibTableColumn
ifCEAnnounceFilterCount = _IfCEAnnounceFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 2, 1, 19),
    _IfCEAnnounceFilterCount_Type()
)
ifCEAnnounceFilterCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifCEAnnounceFilterCount.setStatus("mandatory")
_IfUnicastPeersTable_Object = MibTable
ifUnicastPeersTable = _IfUnicastPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    ifUnicastPeersTable.setStatus("mandatory")
_IfUnicastPeersEntry_Object = MibTableRow
ifUnicastPeersEntry = _IfUnicastPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1)
)
ifUnicastPeersEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifUPIfIndex"),
    (0, "MSIPRIP2-MIB", "ifUPAddress"),
)
if mibBuilder.loadTexts:
    ifUnicastPeersEntry.setStatus("mandatory")
_IfUPIfIndex_Type = Integer32
_IfUPIfIndex_Object = MibTableColumn
ifUPIfIndex = _IfUPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 1),
    _IfUPIfIndex_Type()
)
ifUPIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUPIfIndex.setStatus("mandatory")
_IfUPAddress_Type = IpAddress
_IfUPAddress_Object = MibTableColumn
ifUPAddress = _IfUPAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 2),
    _IfUPAddress_Type()
)
ifUPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUPAddress.setStatus("mandatory")


class _IfUPTag_Type(Integer32):
    """Custom type ifUPTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_IfUPTag_Type.__name__ = "Integer32"
_IfUPTag_Object = MibTableColumn
ifUPTag = _IfUPTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 3, 1, 3),
    _IfUPTag_Type()
)
ifUPTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifUPTag.setStatus("mandatory")
_IfAcceptRouteFilterTable_Object = MibTable
ifAcceptRouteFilterTable = _IfAcceptRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4)
)
if mibBuilder.loadTexts:
    ifAcceptRouteFilterTable.setStatus("mandatory")
_IfAcceptRouteFilterEntry_Object = MibTableRow
ifAcceptRouteFilterEntry = _IfAcceptRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1)
)
ifAcceptRouteFilterEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifAcceptRFIfIndex"),
    (0, "MSIPRIP2-MIB", "ifAcceptRFLoAddress"),
    (0, "MSIPRIP2-MIB", "ifAcceptRFHiAddress"),
    (0, "MSIPRIP2-MIB", "ifAcceptRFTag"),
)
if mibBuilder.loadTexts:
    ifAcceptRouteFilterEntry.setStatus("mandatory")
_IfAcceptRFIfIndex_Type = Integer32
_IfAcceptRFIfIndex_Object = MibTableColumn
ifAcceptRFIfIndex = _IfAcceptRFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 1),
    _IfAcceptRFIfIndex_Type()
)
ifAcceptRFIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAcceptRFIfIndex.setStatus("mandatory")
_IfAcceptRFLoAddress_Type = IpAddress
_IfAcceptRFLoAddress_Object = MibTableColumn
ifAcceptRFLoAddress = _IfAcceptRFLoAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 2),
    _IfAcceptRFLoAddress_Type()
)
ifAcceptRFLoAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAcceptRFLoAddress.setStatus("mandatory")
_IfAcceptRFHiAddress_Type = IpAddress
_IfAcceptRFHiAddress_Object = MibTableColumn
ifAcceptRFHiAddress = _IfAcceptRFHiAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 3),
    _IfAcceptRFHiAddress_Type()
)
ifAcceptRFHiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAcceptRFHiAddress.setStatus("mandatory")


class _IfAcceptRFTag_Type(Integer32):
    """Custom type ifAcceptRFTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_IfAcceptRFTag_Type.__name__ = "Integer32"
_IfAcceptRFTag_Object = MibTableColumn
ifAcceptRFTag = _IfAcceptRFTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 4, 1, 4),
    _IfAcceptRFTag_Type()
)
ifAcceptRFTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAcceptRFTag.setStatus("mandatory")
_IfAnnounceRouteFilterTable_Object = MibTable
ifAnnounceRouteFilterTable = _IfAnnounceRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5)
)
if mibBuilder.loadTexts:
    ifAnnounceRouteFilterTable.setStatus("mandatory")
_IfAnnounceRouteFilterEntry_Object = MibTableRow
ifAnnounceRouteFilterEntry = _IfAnnounceRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1)
)
ifAnnounceRouteFilterEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifAnnounceRFIfIndex"),
    (0, "MSIPRIP2-MIB", "ifAnnounceRFLoAddress"),
    (0, "MSIPRIP2-MIB", "ifAnnounceRFHiAddress"),
)
if mibBuilder.loadTexts:
    ifAnnounceRouteFilterEntry.setStatus("mandatory")
_IfAnnounceRFIfIndex_Type = Integer32
_IfAnnounceRFIfIndex_Object = MibTableColumn
ifAnnounceRFIfIndex = _IfAnnounceRFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 1),
    _IfAnnounceRFIfIndex_Type()
)
ifAnnounceRFIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAnnounceRFIfIndex.setStatus("mandatory")
_IfAnnounceRFLoAddress_Type = IpAddress
_IfAnnounceRFLoAddress_Object = MibTableColumn
ifAnnounceRFLoAddress = _IfAnnounceRFLoAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 2),
    _IfAnnounceRFLoAddress_Type()
)
ifAnnounceRFLoAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAnnounceRFLoAddress.setStatus("mandatory")
_IfAnnounceRFHiAddress_Type = IpAddress
_IfAnnounceRFHiAddress_Object = MibTableColumn
ifAnnounceRFHiAddress = _IfAnnounceRFHiAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 3),
    _IfAnnounceRFHiAddress_Type()
)
ifAnnounceRFHiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAnnounceRFHiAddress.setStatus("mandatory")


class _IfAnnounceRFTag_Type(Integer32):
    """Custom type ifAnnounceRFTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_IfAnnounceRFTag_Type.__name__ = "Integer32"
_IfAnnounceRFTag_Object = MibTableColumn
ifAnnounceRFTag = _IfAnnounceRFTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 5, 1, 4),
    _IfAnnounceRFTag_Type()
)
ifAnnounceRFTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAnnounceRFTag.setStatus("mandatory")
_IfBindingTable_Object = MibTable
ifBindingTable = _IfBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6)
)
if mibBuilder.loadTexts:
    ifBindingTable.setStatus("mandatory")
_IfBindingEntry_Object = MibTableRow
ifBindingEntry = _IfBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1)
)
ifBindingEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifBindingIndex"),
)
if mibBuilder.loadTexts:
    ifBindingEntry.setStatus("mandatory")
_IfBindingIndex_Type = Integer32
_IfBindingIndex_Object = MibTableColumn
ifBindingIndex = _IfBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 1),
    _IfBindingIndex_Type()
)
ifBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingIndex.setStatus("mandatory")


class _IfBindingState_Type(Integer32):
    """Custom type ifBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 2),
          ("enabled", 1))
    )


_IfBindingState_Type.__name__ = "Integer32"
_IfBindingState_Object = MibTableColumn
ifBindingState = _IfBindingState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 2),
    _IfBindingState_Type()
)
ifBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingState.setStatus("mandatory")
_IfBindingCounts_Type = Counter32
_IfBindingCounts_Object = MibTableColumn
ifBindingCounts = _IfBindingCounts_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 6, 1, 3),
    _IfBindingCounts_Type()
)
ifBindingCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBindingCounts.setStatus("mandatory")
_IfAddressTable_Object = MibTable
ifAddressTable = _IfAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7)
)
if mibBuilder.loadTexts:
    ifAddressTable.setStatus("mandatory")
_IfAddressEntry_Object = MibTableRow
ifAddressEntry = _IfAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1)
)
ifAddressEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifAEIfIndex"),
    (0, "MSIPRIP2-MIB", "ifAEAddress"),
    (0, "MSIPRIP2-MIB", "ifAEMask"),
)
if mibBuilder.loadTexts:
    ifAddressEntry.setStatus("mandatory")
_IfAEIfIndex_Type = Integer32
_IfAEIfIndex_Object = MibTableColumn
ifAEIfIndex = _IfAEIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 1),
    _IfAEIfIndex_Type()
)
ifAEIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEIfIndex.setStatus("mandatory")
_IfAEAddress_Type = IpAddress
_IfAEAddress_Object = MibTableColumn
ifAEAddress = _IfAEAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 2),
    _IfAEAddress_Type()
)
ifAEAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEAddress.setStatus("mandatory")
_IfAEMask_Type = IpAddress
_IfAEMask_Object = MibTableColumn
ifAEMask = _IfAEMask_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 2, 7, 1, 3),
    _IfAEMask_Type()
)
ifAEMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAEMask.setStatus("mandatory")
_Peer_ObjectIdentity = ObjectIdentity
peer = _Peer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3)
)
_IfPeerStatsTable_Object = MibTable
ifPeerStatsTable = _IfPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    ifPeerStatsTable.setStatus("mandatory")
_IfPeerStatsEntry_Object = MibTableRow
ifPeerStatsEntry = _IfPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1)
)
ifPeerStatsEntry.setIndexNames(
    (0, "MSIPRIP2-MIB", "ifPSAddress"),
)
if mibBuilder.loadTexts:
    ifPeerStatsEntry.setStatus("mandatory")
_IfPSAddress_Type = IpAddress
_IfPSAddress_Object = MibTableColumn
ifPSAddress = _IfPSAddress_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 1),
    _IfPSAddress_Type()
)
ifPSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSAddress.setStatus("mandatory")
_IfPSLastPeerRouteTag_Type = Integer32
_IfPSLastPeerRouteTag_Object = MibTableColumn
ifPSLastPeerRouteTag = _IfPSLastPeerRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 2),
    _IfPSLastPeerRouteTag_Type()
)
ifPSLastPeerRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSLastPeerRouteTag.setStatus("mandatory")
_IfPSLastPeerUpdateTickCount_Type = TimeTicks
_IfPSLastPeerUpdateTickCount_Object = MibTableColumn
ifPSLastPeerUpdateTickCount = _IfPSLastPeerUpdateTickCount_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 3),
    _IfPSLastPeerUpdateTickCount_Type()
)
ifPSLastPeerUpdateTickCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSLastPeerUpdateTickCount.setStatus("mandatory")


class _IfPSLastPeerUpdateVersion_Type(Integer32):
    """Custom type ifPSLastPeerUpdateVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfPSLastPeerUpdateVersion_Type.__name__ = "Integer32"
_IfPSLastPeerUpdateVersion_Object = MibTableColumn
ifPSLastPeerUpdateVersion = _IfPSLastPeerUpdateVersion_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 4),
    _IfPSLastPeerUpdateVersion_Type()
)
ifPSLastPeerUpdateVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSLastPeerUpdateVersion.setStatus("mandatory")
_IfPSPeerBadResponsePackets_Type = Counter32
_IfPSPeerBadResponsePackets_Object = MibTableColumn
ifPSPeerBadResponsePackets = _IfPSPeerBadResponsePackets_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 5),
    _IfPSPeerBadResponsePackets_Type()
)
ifPSPeerBadResponsePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSPeerBadResponsePackets.setStatus("mandatory")
_IfPSPeerBadResponseEntries_Type = Counter32
_IfPSPeerBadResponseEntries_Object = MibTableColumn
ifPSPeerBadResponseEntries = _IfPSPeerBadResponseEntries_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 11, 3, 1, 1, 6),
    _IfPSPeerBadResponseEntries_Type()
)
ifPSPeerBadResponseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPSPeerBadResponseEntries.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSIPRIP2-MIB",
    **{"msiprip2": msiprip2,
       "global": _pysmi_global,
       "globalSystemRouteChanges": globalSystemRouteChanges,
       "globalTotalResponseSends": globalTotalResponseSends,
       "globalLoggingLevel": globalLoggingLevel,
       "globalMaxRecQueueSize": globalMaxRecQueueSize,
       "globalMaxSendQueueSize": globalMaxSendQueueSize,
       "globalMinTriggeredUpdateInterval": globalMinTriggeredUpdateInterval,
       "globalPeerFilterMode": globalPeerFilterMode,
       "globalPeerFilterCount": globalPeerFilterCount,
       "globalPeerFilterTable": globalPeerFilterTable,
       "globalPeerFilterEntry": globalPeerFilterEntry,
       "globalPFAddr": globalPFAddr,
       "globalPFTag": globalPFTag,
       "interface": interface,
       "ifStatsTable": ifStatsTable,
       "ifStatsEntry": ifStatsEntry,
       "ifSEIndex": ifSEIndex,
       "ifSEState": ifSEState,
       "ifSESendFailures": ifSESendFailures,
       "ifSEReceiveFailures": ifSEReceiveFailures,
       "ifSERequestSends": ifSERequestSends,
       "ifSERequestReceiveds": ifSERequestReceiveds,
       "ifSEResponseSends": ifSEResponseSends,
       "ifSEResponseReceiveds": ifSEResponseReceiveds,
       "ifSEBadResponsePacketReceiveds": ifSEBadResponsePacketReceiveds,
       "ifSEBadResponseEntriesReceiveds": ifSEBadResponseEntriesReceiveds,
       "ifSETriggeredUpdateSends": ifSETriggeredUpdateSends,
       "ifConfigTable": ifConfigTable,
       "ifConfigEntry": ifConfigEntry,
       "ifCEIndex": ifCEIndex,
       "ifCEState": ifCEState,
       "ifCEMetric": ifCEMetric,
       "ifCEUpdateMode": ifCEUpdateMode,
       "ifCEAcceptMode": ifCEAcceptMode,
       "ifCEAnnounceMode": ifCEAnnounceMode,
       "ifCEProtocolFlags": ifCEProtocolFlags,
       "ifCERouteExpirationInterval": ifCERouteExpirationInterval,
       "ifCERouteRemovalInterval": ifCERouteRemovalInterval,
       "ifCEFullUpdateInterval": ifCEFullUpdateInterval,
       "ifCEAuthenticationType": ifCEAuthenticationType,
       "ifCEAuthenticationKey": ifCEAuthenticationKey,
       "ifCERouteTag": ifCERouteTag,
       "ifCEUnicastPeerMode": ifCEUnicastPeerMode,
       "ifCEAcceptFilterMode": ifCEAcceptFilterMode,
       "ifCEAnnounceFilterMode": ifCEAnnounceFilterMode,
       "ifCEUnicastPeerCount": ifCEUnicastPeerCount,
       "ifCEAcceptFilterCount": ifCEAcceptFilterCount,
       "ifCEAnnounceFilterCount": ifCEAnnounceFilterCount,
       "ifUnicastPeersTable": ifUnicastPeersTable,
       "ifUnicastPeersEntry": ifUnicastPeersEntry,
       "ifUPIfIndex": ifUPIfIndex,
       "ifUPAddress": ifUPAddress,
       "ifUPTag": ifUPTag,
       "ifAcceptRouteFilterTable": ifAcceptRouteFilterTable,
       "ifAcceptRouteFilterEntry": ifAcceptRouteFilterEntry,
       "ifAcceptRFIfIndex": ifAcceptRFIfIndex,
       "ifAcceptRFLoAddress": ifAcceptRFLoAddress,
       "ifAcceptRFHiAddress": ifAcceptRFHiAddress,
       "ifAcceptRFTag": ifAcceptRFTag,
       "ifAnnounceRouteFilterTable": ifAnnounceRouteFilterTable,
       "ifAnnounceRouteFilterEntry": ifAnnounceRouteFilterEntry,
       "ifAnnounceRFIfIndex": ifAnnounceRFIfIndex,
       "ifAnnounceRFLoAddress": ifAnnounceRFLoAddress,
       "ifAnnounceRFHiAddress": ifAnnounceRFHiAddress,
       "ifAnnounceRFTag": ifAnnounceRFTag,
       "ifBindingTable": ifBindingTable,
       "ifBindingEntry": ifBindingEntry,
       "ifBindingIndex": ifBindingIndex,
       "ifBindingState": ifBindingState,
       "ifBindingCounts": ifBindingCounts,
       "ifAddressTable": ifAddressTable,
       "ifAddressEntry": ifAddressEntry,
       "ifAEIfIndex": ifAEIfIndex,
       "ifAEAddress": ifAEAddress,
       "ifAEMask": ifAEMask,
       "peer": peer,
       "ifPeerStatsTable": ifPeerStatsTable,
       "ifPeerStatsEntry": ifPeerStatsEntry,
       "ifPSAddress": ifPSAddress,
       "ifPSLastPeerRouteTag": ifPSLastPeerRouteTag,
       "ifPSLastPeerUpdateTickCount": ifPSLastPeerUpdateTickCount,
       "ifPSLastPeerUpdateVersion": ifPSLastPeerUpdateVersion,
       "ifPSPeerBadResponsePackets": ifPSPeerBadResponsePackets,
       "ifPSPeerBadResponseEntries": ifPSPeerBadResponseEntries}
)
