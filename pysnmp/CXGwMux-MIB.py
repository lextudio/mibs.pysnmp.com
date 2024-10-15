# SNMP MIB module (CXGwMux-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXGwMux-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:31 2024
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

(Alias,
 cxGwMux) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxGwMux")

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



class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GmfConfig_ObjectIdentity = ObjectIdentity
gmfConfig = _GmfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1)
)


class _GmfMuxInterPassPeriodInMs_Type(Integer32):
    """Custom type gmfMuxInterPassPeriodInMs based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_GmfMuxInterPassPeriodInMs_Type.__name__ = "Integer32"
_GmfMuxInterPassPeriodInMs_Object = MibScalar
gmfMuxInterPassPeriodInMs = _GmfMuxInterPassPeriodInMs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 1),
    _GmfMuxInterPassPeriodInMs_Type()
)
gmfMuxInterPassPeriodInMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfMuxInterPassPeriodInMs.setStatus("mandatory")


class _GmfVoiceOverDataPriorityFactor_Type(Integer32):
    """Custom type gmfVoiceOverDataPriorityFactor based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_GmfVoiceOverDataPriorityFactor_Type.__name__ = "Integer32"
_GmfVoiceOverDataPriorityFactor_Object = MibScalar
gmfVoiceOverDataPriorityFactor = _GmfVoiceOverDataPriorityFactor_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 2),
    _GmfVoiceOverDataPriorityFactor_Type()
)
gmfVoiceOverDataPriorityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfVoiceOverDataPriorityFactor.setStatus("mandatory")


class _GmfStatSamplingPeriod_Type(Integer32):
    """Custom type gmfStatSamplingPeriod based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_GmfStatSamplingPeriod_Type.__name__ = "Integer32"
_GmfStatSamplingPeriod_Object = MibScalar
gmfStatSamplingPeriod = _GmfStatSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 3),
    _GmfStatSamplingPeriod_Type()
)
gmfStatSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfStatSamplingPeriod.setStatus("mandatory")


class _GmfNoOfLinkSupported_Type(Integer32):
    """Custom type gmfNoOfLinkSupported based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_GmfNoOfLinkSupported_Type.__name__ = "Integer32"
_GmfNoOfLinkSupported_Object = MibScalar
gmfNoOfLinkSupported = _GmfNoOfLinkSupported_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 4),
    _GmfNoOfLinkSupported_Type()
)
gmfNoOfLinkSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfNoOfLinkSupported.setStatus("mandatory")


class _GmfNoOfEntryPerFiFo_Type(Integer32):
    """Custom type gmfNoOfEntryPerFiFo based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 10000),
    )


_GmfNoOfEntryPerFiFo_Type.__name__ = "Integer32"
_GmfNoOfEntryPerFiFo_Object = MibScalar
gmfNoOfEntryPerFiFo = _GmfNoOfEntryPerFiFo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 5),
    _GmfNoOfEntryPerFiFo_Type()
)
gmfNoOfEntryPerFiFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfNoOfEntryPerFiFo.setStatus("mandatory")


class _GmfToFrCouplingLevel_Type(Integer32):
    """Custom type gmfToFrCouplingLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GmfToFrCouplingLevel_Type.__name__ = "Integer32"
_GmfToFrCouplingLevel_Object = MibScalar
gmfToFrCouplingLevel = _GmfToFrCouplingLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 6),
    _GmfToFrCouplingLevel_Type()
)
gmfToFrCouplingLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfToFrCouplingLevel.setStatus("mandatory")


class _GmfOutputFlowControlFactor_Type(Integer32):
    """Custom type gmfOutputFlowControlFactor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_GmfOutputFlowControlFactor_Type.__name__ = "Integer32"
_GmfOutputFlowControlFactor_Object = MibScalar
gmfOutputFlowControlFactor = _GmfOutputFlowControlFactor_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 7),
    _GmfOutputFlowControlFactor_Type()
)
gmfOutputFlowControlFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfOutputFlowControlFactor.setStatus("mandatory")


class _GmfState_Type(Integer32):
    """Custom type gmfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dead", 1),
          ("general-conf", 3),
          ("gmf-task-conf", 2),
          ("init-appl-completed", 7),
          ("init-gmf-completed", 6),
          ("mci-only", 8),
          ("reg-to-iam", 9),
          ("route-conf", 5),
          ("sap-conf", 4))
    )


_GmfState_Type.__name__ = "Integer32"
_GmfState_Object = MibScalar
gmfState = _GmfState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 8),
    _GmfState_Type()
)
gmfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfState.setStatus("mandatory")
_GmfCntInfoMsgRelFromBus_Type = Counter32
_GmfCntInfoMsgRelFromBus_Object = MibScalar
gmfCntInfoMsgRelFromBus = _GmfCntInfoMsgRelFromBus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 9),
    _GmfCntInfoMsgRelFromBus_Type()
)
gmfCntInfoMsgRelFromBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntInfoMsgRelFromBus.setStatus("mandatory")
_GmfCntInfoMsgRelFromWan_Type = Counter32
_GmfCntInfoMsgRelFromWan_Object = MibScalar
gmfCntInfoMsgRelFromWan = _GmfCntInfoMsgRelFromWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 10),
    _GmfCntInfoMsgRelFromWan_Type()
)
gmfCntInfoMsgRelFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntInfoMsgRelFromWan.setStatus("mandatory")
_GmfCntTxAckToWan_Type = Counter32
_GmfCntTxAckToWan_Object = MibScalar
gmfCntTxAckToWan = _GmfCntTxAckToWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 11),
    _GmfCntTxAckToWan_Type()
)
gmfCntTxAckToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntTxAckToWan.setStatus("mandatory")
_GmfCntUnexpLinkNoFromWan_Type = Counter32
_GmfCntUnexpLinkNoFromWan_Object = MibScalar
gmfCntUnexpLinkNoFromWan = _GmfCntUnexpLinkNoFromWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 12),
    _GmfCntUnexpLinkNoFromWan_Type()
)
gmfCntUnexpLinkNoFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntUnexpLinkNoFromWan.setStatus("mandatory")
_GmfCntFrmTooShortFromWan_Type = Counter32
_GmfCntFrmTooShortFromWan_Object = MibScalar
gmfCntFrmTooShortFromWan = _GmfCntFrmTooShortFromWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 13),
    _GmfCntFrmTooShortFromWan_Type()
)
gmfCntFrmTooShortFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntFrmTooShortFromWan.setStatus("mandatory")
_GmfCntFrmTooLongFromWan_Type = Counter32
_GmfCntFrmTooLongFromWan_Object = MibScalar
gmfCntFrmTooLongFromWan = _GmfCntFrmTooLongFromWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 14),
    _GmfCntFrmTooLongFromWan_Type()
)
gmfCntFrmTooLongFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntFrmTooLongFromWan.setStatus("mandatory")
_GmfLongestTimeToMux_Type = Counter32
_GmfLongestTimeToMux_Object = MibScalar
gmfLongestTimeToMux = _GmfLongestTimeToMux_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 15),
    _GmfLongestTimeToMux_Type()
)
gmfLongestTimeToMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLongestTimeToMux.setStatus("mandatory")
_GmfCntSilentConnections_Type = Counter32
_GmfCntSilentConnections_Object = MibScalar
gmfCntSilentConnections = _GmfCntSilentConnections_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 16),
    _GmfCntSilentConnections_Type()
)
gmfCntSilentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntSilentConnections.setStatus("mandatory")
_GmfCntMuxPassTimeExceeded_Type = Counter32
_GmfCntMuxPassTimeExceeded_Object = MibScalar
gmfCntMuxPassTimeExceeded = _GmfCntMuxPassTimeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 17),
    _GmfCntMuxPassTimeExceeded_Type()
)
gmfCntMuxPassTimeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntMuxPassTimeExceeded.setStatus("obsolete")
_GmfMciCurrentConnection_Type = Integer32
_GmfMciCurrentConnection_Object = MibScalar
gmfMciCurrentConnection = _GmfMciCurrentConnection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 18),
    _GmfMciCurrentConnection_Type()
)
gmfMciCurrentConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfMciCurrentConnection.setStatus("obsolete")
_GmfCntInfoMsgRelFromVce_Type = Counter32
_GmfCntInfoMsgRelFromVce_Object = MibScalar
gmfCntInfoMsgRelFromVce = _GmfCntInfoMsgRelFromVce_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 19),
    _GmfCntInfoMsgRelFromVce_Type()
)
gmfCntInfoMsgRelFromVce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntInfoMsgRelFromVce.setStatus("mandatory")
_GmfCntGlobalFlowCtlCond_Type = Counter32
_GmfCntGlobalFlowCtlCond_Object = MibScalar
gmfCntGlobalFlowCtlCond = _GmfCntGlobalFlowCtlCond_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 20),
    _GmfCntGlobalFlowCtlCond_Type()
)
gmfCntGlobalFlowCtlCond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntGlobalFlowCtlCond.setStatus("mandatory")


class _GmfNoOfVoicePacketQueued_Type(Integer32):
    """Custom type gmfNoOfVoicePacketQueued based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GmfNoOfVoicePacketQueued_Type.__name__ = "Integer32"
_GmfNoOfVoicePacketQueued_Object = MibScalar
gmfNoOfVoicePacketQueued = _GmfNoOfVoicePacketQueued_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 21),
    _GmfNoOfVoicePacketQueued_Type()
)
gmfNoOfVoicePacketQueued.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfNoOfVoicePacketQueued.setStatus("mandatory")


class _GmfControlStats_Type(Integer32):
    """Custom type gmfControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_GmfControlStats_Type.__name__ = "Integer32"
_GmfControlStats_Object = MibScalar
gmfControlStats = _GmfControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 1, 22),
    _GmfControlStats_Type()
)
gmfControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gmfControlStats.setStatus("mandatory")
_GmfRouteTable_Object = MibTable
gmfRouteTable = _GmfRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    gmfRouteTable.setStatus("mandatory")
_GmfRouteEntry_Object = MibTableRow
gmfRouteEntry = _GmfRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2, 1)
)
gmfRouteEntry.setIndexNames(
    (0, "CXGwMux-MIB", "gmfOrigin"),
    (0, "CXGwMux-MIB", "gmfLink"),
)
if mibBuilder.loadTexts:
    gmfRouteEntry.setStatus("mandatory")


class _GmfOrigin_Type(Integer32):
    """Custom type gmfOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GmfOrigin_Type.__name__ = "Integer32"
_GmfOrigin_Object = MibTableColumn
gmfOrigin = _GmfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2, 1, 1),
    _GmfOrigin_Type()
)
gmfOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfOrigin.setStatus("mandatory")


class _GmfLink_Type(Integer32):
    """Custom type gmfLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GmfLink_Type.__name__ = "Integer32"
_GmfLink_Object = MibTableColumn
gmfLink = _GmfLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2, 1, 2),
    _GmfLink_Type()
)
gmfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLink.setStatus("mandatory")


class _GmfDest_Type(Integer32):
    """Custom type gmfDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GmfDest_Type.__name__ = "Integer32"
_GmfDest_Object = MibTableColumn
gmfDest = _GmfDest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2, 1, 3),
    _GmfDest_Type()
)
gmfDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfDest.setStatus("mandatory")


class _GmfRouteRowStatus_Type(Integer32):
    """Custom type gmfRouteRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_GmfRouteRowStatus_Type.__name__ = "Integer32"
_GmfRouteRowStatus_Object = MibTableColumn
gmfRouteRowStatus = _GmfRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 2, 1, 4),
    _GmfRouteRowStatus_Type()
)
gmfRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfRouteRowStatus.setStatus("mandatory")
_GmfLinkStatTable_Object = MibTable
gmfLinkStatTable = _GmfLinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3)
)
if mibBuilder.loadTexts:
    gmfLinkStatTable.setStatus("mandatory")
_GmfLinkStatEntry_Object = MibTableRow
gmfLinkStatEntry = _GmfLinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1)
)
gmfLinkStatEntry.setIndexNames(
    (0, "CXGwMux-MIB", "gmfLinkIndex"),
)
if mibBuilder.loadTexts:
    gmfLinkStatEntry.setStatus("mandatory")
_GmfLinkIndex_Type = Integer32
_GmfLinkIndex_Object = MibTableColumn
gmfLinkIndex = _GmfLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 1),
    _GmfLinkIndex_Type()
)
gmfLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkIndex.setStatus("mandatory")


class _GmfLinkStatus_Type(Integer32):
    """Custom type gmfLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("init", 2),
          ("up", 3))
    )


_GmfLinkStatus_Type.__name__ = "Integer32"
_GmfLinkStatus_Object = MibTableColumn
gmfLinkStatus = _GmfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 2),
    _GmfLinkStatus_Type()
)
gmfLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkStatus.setStatus("mandatory")


class _GmfLinkType_Type(Integer32):
    """Custom type gmfLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound-to-FR", 1),
          ("in-loopback", 3),
          ("routed-to-IAM", 2))
    )


_GmfLinkType_Type.__name__ = "Integer32"
_GmfLinkType_Object = MibTableColumn
gmfLinkType = _GmfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 3),
    _GmfLinkType_Type()
)
gmfLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkType.setStatus("mandatory")
_GmfCntDataFrmMx_Type = Counter32
_GmfCntDataFrmMx_Object = MibTableColumn
gmfCntDataFrmMx = _GmfCntDataFrmMx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 4),
    _GmfCntDataFrmMx_Type()
)
gmfCntDataFrmMx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntDataFrmMx.setStatus("mandatory")
_GmfCntDataFrmDmx_Type = Counter32
_GmfCntDataFrmDmx_Object = MibTableColumn
gmfCntDataFrmDmx = _GmfCntDataFrmDmx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 5),
    _GmfCntDataFrmDmx_Type()
)
gmfCntDataFrmDmx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntDataFrmDmx.setStatus("mandatory")
_GmfCntVoiceFrmMx_Type = Counter32
_GmfCntVoiceFrmMx_Object = MibTableColumn
gmfCntVoiceFrmMx = _GmfCntVoiceFrmMx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 6),
    _GmfCntVoiceFrmMx_Type()
)
gmfCntVoiceFrmMx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntVoiceFrmMx.setStatus("mandatory")
_GmfCntVoiceFrmDmx_Type = Counter32
_GmfCntVoiceFrmDmx_Object = MibTableColumn
gmfCntVoiceFrmDmx = _GmfCntVoiceFrmDmx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 7),
    _GmfCntVoiceFrmDmx_Type()
)
gmfCntVoiceFrmDmx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntVoiceFrmDmx.setStatus("mandatory")
_GmfCntLinkDown_Type = Counter32
_GmfCntLinkDown_Object = MibTableColumn
gmfCntLinkDown = _GmfCntLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 8),
    _GmfCntLinkDown_Type()
)
gmfCntLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntLinkDown.setStatus("mandatory")
_GmfLinkUtilizationTx_Type = Counter32
_GmfLinkUtilizationTx_Object = MibTableColumn
gmfLinkUtilizationTx = _GmfLinkUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 9),
    _GmfLinkUtilizationTx_Type()
)
gmfLinkUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkUtilizationTx.setStatus("mandatory")
_GmfLinkUtilizationRx_Type = Counter32
_GmfLinkUtilizationRx_Object = MibTableColumn
gmfLinkUtilizationRx = _GmfLinkUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 10),
    _GmfLinkUtilizationRx_Type()
)
gmfLinkUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkUtilizationRx.setStatus("mandatory")
_GmfLinkErrorRate_Type = Counter32
_GmfLinkErrorRate_Object = MibTableColumn
gmfLinkErrorRate = _GmfLinkErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 11),
    _GmfLinkErrorRate_Type()
)
gmfLinkErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfLinkErrorRate.setStatus("mandatory")
_GmfCntInFlowCtrlMuxSide_Type = Counter32
_GmfCntInFlowCtrlMuxSide_Object = MibTableColumn
gmfCntInFlowCtrlMuxSide = _GmfCntInFlowCtrlMuxSide_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 12),
    _GmfCntInFlowCtrlMuxSide_Type()
)
gmfCntInFlowCtrlMuxSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntInFlowCtrlMuxSide.setStatus("mandatory")
_GmfCntOutFlowCtrlWanSide_Type = Counter32
_GmfCntOutFlowCtrlWanSide_Object = MibTableColumn
gmfCntOutFlowCtrlWanSide = _GmfCntOutFlowCtrlWanSide_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 13),
    _GmfCntOutFlowCtrlWanSide_Type()
)
gmfCntOutFlowCtrlWanSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntOutFlowCtrlWanSide.setStatus("mandatory")
_GmfCntSeqErrorFromMux_Type = Counter32
_GmfCntSeqErrorFromMux_Object = MibTableColumn
gmfCntSeqErrorFromMux = _GmfCntSeqErrorFromMux_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 14),
    _GmfCntSeqErrorFromMux_Type()
)
gmfCntSeqErrorFromMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntSeqErrorFromMux.setStatus("mandatory")
_GmfCntSeqErrorFromWan_Type = Counter32
_GmfCntSeqErrorFromWan_Object = MibTableColumn
gmfCntSeqErrorFromWan = _GmfCntSeqErrorFromWan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 15),
    _GmfCntSeqErrorFromWan_Type()
)
gmfCntSeqErrorFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntSeqErrorFromWan.setStatus("mandatory")
_GmfCntSilentLink_Type = Counter32
_GmfCntSilentLink_Object = MibTableColumn
gmfCntSilentLink = _GmfCntSilentLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 16),
    _GmfCntSilentLink_Type()
)
gmfCntSilentLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntSilentLink.setStatus("mandatory")
_GmfCntSeqErrorForced_Type = Counter32
_GmfCntSeqErrorForced_Object = MibTableColumn
gmfCntSeqErrorForced = _GmfCntSeqErrorForced_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 17),
    _GmfCntSeqErrorForced_Type()
)
gmfCntSeqErrorForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntSeqErrorForced.setStatus("mandatory")
_GmfCntUnexpLoopBack_Type = Counter32
_GmfCntUnexpLoopBack_Object = MibTableColumn
gmfCntUnexpLoopBack = _GmfCntUnexpLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 18),
    _GmfCntUnexpLoopBack_Type()
)
gmfCntUnexpLoopBack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntUnexpLoopBack.setStatus("mandatory")
_GmfCntRemoteRestarted_Type = Counter32
_GmfCntRemoteRestarted_Object = MibTableColumn
gmfCntRemoteRestarted = _GmfCntRemoteRestarted_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 19),
    _GmfCntRemoteRestarted_Type()
)
gmfCntRemoteRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntRemoteRestarted.setStatus("mandatory")
_GmfCntVoiceMuxInterrupted_Type = Counter32
_GmfCntVoiceMuxInterrupted_Object = MibTableColumn
gmfCntVoiceMuxInterrupted = _GmfCntVoiceMuxInterrupted_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 20),
    _GmfCntVoiceMuxInterrupted_Type()
)
gmfCntVoiceMuxInterrupted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntVoiceMuxInterrupted.setStatus("mandatory")
_GmfCntDataQueueFull_Type = Counter32
_GmfCntDataQueueFull_Object = MibTableColumn
gmfCntDataQueueFull = _GmfCntDataQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 21),
    _GmfCntDataQueueFull_Type()
)
gmfCntDataQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntDataQueueFull.setStatus("mandatory")
_GmfCntVoiceQueueFull_Type = Counter32
_GmfCntVoiceQueueFull_Object = MibTableColumn
gmfCntVoiceQueueFull = _GmfCntVoiceQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 22),
    _GmfCntVoiceQueueFull_Type()
)
gmfCntVoiceQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntVoiceQueueFull.setStatus("mandatory")
_GmfCntUnexpSliceType_Type = Counter32
_GmfCntUnexpSliceType_Object = MibTableColumn
gmfCntUnexpSliceType = _GmfCntUnexpSliceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 23),
    _GmfCntUnexpSliceType_Type()
)
gmfCntUnexpSliceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntUnexpSliceType.setStatus("mandatory")
_GmfCntRouteChange_Type = Counter32
_GmfCntRouteChange_Object = MibTableColumn
gmfCntRouteChange = _GmfCntRouteChange_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 24),
    _GmfCntRouteChange_Type()
)
gmfCntRouteChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntRouteChange.setStatus("mandatory")
_GmfCntTooManyCodes_Type = Counter32
_GmfCntTooManyCodes_Object = MibTableColumn
gmfCntTooManyCodes = _GmfCntTooManyCodes_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 25),
    _GmfCntTooManyCodes_Type()
)
gmfCntTooManyCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntTooManyCodes.setStatus("mandatory")
_GmfCntPosValidation_Type = Counter32
_GmfCntPosValidation_Object = MibTableColumn
gmfCntPosValidation = _GmfCntPosValidation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 26),
    _GmfCntPosValidation_Type()
)
gmfCntPosValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntPosValidation.setStatus("mandatory")
_GmfCntNegValidation_Type = Counter32
_GmfCntNegValidation_Object = MibTableColumn
gmfCntNegValidation = _GmfCntNegValidation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 27),
    _GmfCntNegValidation_Type()
)
gmfCntNegValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfCntNegValidation.setStatus("mandatory")


class _GmfControlLink_Type(Integer32):
    """Custom type gmfControlLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceLoopback", 2),
          ("forceNormal", 1))
    )


_GmfControlLink_Type.__name__ = "Integer32"
_GmfControlLink_Object = MibTableColumn
gmfControlLink = _GmfControlLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 29),
    _GmfControlLink_Type()
)
gmfControlLink.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gmfControlLink.setStatus("mandatory")


class _GmfDataOutWindowWidth_Type(Integer32):
    """Custom type gmfDataOutWindowWidth based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GmfDataOutWindowWidth_Type.__name__ = "Integer32"
_GmfDataOutWindowWidth_Object = MibTableColumn
gmfDataOutWindowWidth = _GmfDataOutWindowWidth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 30),
    _GmfDataOutWindowWidth_Type()
)
gmfDataOutWindowWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfDataOutWindowWidth.setStatus("mandatory")


class _GmfDataOutPriority_Type(Integer32):
    """Custom type gmfDataOutPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_GmfDataOutPriority_Type.__name__ = "Integer32"
_GmfDataOutPriority_Object = MibTableColumn
gmfDataOutPriority = _GmfDataOutPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 3, 1, 31),
    _GmfDataOutPriority_Type()
)
gmfDataOutPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfDataOutPriority.setStatus("mandatory")
_GmfSRTable_Object = MibTable
gmfSRTable = _GmfSRTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    gmfSRTable.setStatus("mandatory")
_GmfSREntry_Object = MibTableRow
gmfSREntry = _GmfSREntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1)
)
gmfSREntry.setIndexNames(
    (0, "CXGwMux-MIB", "gmfSRLink"),
)
if mibBuilder.loadTexts:
    gmfSREntry.setStatus("mandatory")


class _GmfSRLink_Type(Integer32):
    """Custom type gmfSRLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_GmfSRLink_Type.__name__ = "Integer32"
_GmfSRLink_Object = MibTableColumn
gmfSRLink = _GmfSRLink_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 1),
    _GmfSRLink_Type()
)
gmfSRLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfSRLink.setStatus("mandatory")
_GmfSRDestCircuitAlias_Type = Alias
_GmfSRDestCircuitAlias_Object = MibTableColumn
gmfSRDestCircuitAlias = _GmfSRDestCircuitAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 2),
    _GmfSRDestCircuitAlias_Type()
)
gmfSRDestCircuitAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfSRDestCircuitAlias.setStatus("mandatory")


class _GmfSRSubRef_Type(SubRef):
    """Custom type gmfSRSubRef based on SubRef"""
    defaultValue = 1


_GmfSRSubRef_Object = MibTableColumn
gmfSRSubRef = _GmfSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 3),
    _GmfSRSubRef_Type()
)
gmfSRSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfSRSubRef.setStatus("mandatory")


class _GmfSRConStatus_Type(Integer32):
    """Custom type gmfSRConStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("not-init", 1),
          ("opened", 5),
          ("waitForOpenConf", 4),
          ("waitForQueryConf", 3))
    )


_GmfSRConStatus_Type.__name__ = "Integer32"
_GmfSRConStatus_Object = MibTableColumn
gmfSRConStatus = _GmfSRConStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 4),
    _GmfSRConStatus_Type()
)
gmfSRConStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfSRConStatus.setStatus("mandatory")


class _GmfSRFailStatus_Type(Integer32):
    """Custom type gmfSRFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("adjaCardReset", 14),
          ("internalError", 2),
          ("linkNotSupported", 15),
          ("localDsnFailure", 10),
          ("localFcnFailure", 8),
          ("localMemAllocFailure", 3),
          ("noFailure", 1),
          ("openReqTimeout", 13),
          ("remoteAliasNotFound", 11),
          ("remoteFcnFailure", 9),
          ("remoteMemAllocFailure", 4),
          ("remoteNoAccess", 5),
          ("remoteNoPvcService", 12),
          ("remotePvcBusy", 7),
          ("remotePvcDown", 6))
    )


_GmfSRFailStatus_Type.__name__ = "Integer32"
_GmfSRFailStatus_Object = MibTableColumn
gmfSRFailStatus = _GmfSRFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 5),
    _GmfSRFailStatus_Type()
)
gmfSRFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmfSRFailStatus.setStatus("mandatory")


class _GmfSRRowStatus_Type(Integer32):
    """Custom type gmfSRRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_GmfSRRowStatus_Type.__name__ = "Integer32"
_GmfSRRowStatus_Object = MibTableColumn
gmfSRRowStatus = _GmfSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 5, 4, 1, 6),
    _GmfSRRowStatus_Type()
)
gmfSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gmfSRRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXGwMux-MIB",
    **{"SubRef": SubRef,
       "gmfConfig": gmfConfig,
       "gmfMuxInterPassPeriodInMs": gmfMuxInterPassPeriodInMs,
       "gmfVoiceOverDataPriorityFactor": gmfVoiceOverDataPriorityFactor,
       "gmfStatSamplingPeriod": gmfStatSamplingPeriod,
       "gmfNoOfLinkSupported": gmfNoOfLinkSupported,
       "gmfNoOfEntryPerFiFo": gmfNoOfEntryPerFiFo,
       "gmfToFrCouplingLevel": gmfToFrCouplingLevel,
       "gmfOutputFlowControlFactor": gmfOutputFlowControlFactor,
       "gmfState": gmfState,
       "gmfCntInfoMsgRelFromBus": gmfCntInfoMsgRelFromBus,
       "gmfCntInfoMsgRelFromWan": gmfCntInfoMsgRelFromWan,
       "gmfCntTxAckToWan": gmfCntTxAckToWan,
       "gmfCntUnexpLinkNoFromWan": gmfCntUnexpLinkNoFromWan,
       "gmfCntFrmTooShortFromWan": gmfCntFrmTooShortFromWan,
       "gmfCntFrmTooLongFromWan": gmfCntFrmTooLongFromWan,
       "gmfLongestTimeToMux": gmfLongestTimeToMux,
       "gmfCntSilentConnections": gmfCntSilentConnections,
       "gmfCntMuxPassTimeExceeded": gmfCntMuxPassTimeExceeded,
       "gmfMciCurrentConnection": gmfMciCurrentConnection,
       "gmfCntInfoMsgRelFromVce": gmfCntInfoMsgRelFromVce,
       "gmfCntGlobalFlowCtlCond": gmfCntGlobalFlowCtlCond,
       "gmfNoOfVoicePacketQueued": gmfNoOfVoicePacketQueued,
       "gmfControlStats": gmfControlStats,
       "gmfRouteTable": gmfRouteTable,
       "gmfRouteEntry": gmfRouteEntry,
       "gmfOrigin": gmfOrigin,
       "gmfLink": gmfLink,
       "gmfDest": gmfDest,
       "gmfRouteRowStatus": gmfRouteRowStatus,
       "gmfLinkStatTable": gmfLinkStatTable,
       "gmfLinkStatEntry": gmfLinkStatEntry,
       "gmfLinkIndex": gmfLinkIndex,
       "gmfLinkStatus": gmfLinkStatus,
       "gmfLinkType": gmfLinkType,
       "gmfCntDataFrmMx": gmfCntDataFrmMx,
       "gmfCntDataFrmDmx": gmfCntDataFrmDmx,
       "gmfCntVoiceFrmMx": gmfCntVoiceFrmMx,
       "gmfCntVoiceFrmDmx": gmfCntVoiceFrmDmx,
       "gmfCntLinkDown": gmfCntLinkDown,
       "gmfLinkUtilizationTx": gmfLinkUtilizationTx,
       "gmfLinkUtilizationRx": gmfLinkUtilizationRx,
       "gmfLinkErrorRate": gmfLinkErrorRate,
       "gmfCntInFlowCtrlMuxSide": gmfCntInFlowCtrlMuxSide,
       "gmfCntOutFlowCtrlWanSide": gmfCntOutFlowCtrlWanSide,
       "gmfCntSeqErrorFromMux": gmfCntSeqErrorFromMux,
       "gmfCntSeqErrorFromWan": gmfCntSeqErrorFromWan,
       "gmfCntSilentLink": gmfCntSilentLink,
       "gmfCntSeqErrorForced": gmfCntSeqErrorForced,
       "gmfCntUnexpLoopBack": gmfCntUnexpLoopBack,
       "gmfCntRemoteRestarted": gmfCntRemoteRestarted,
       "gmfCntVoiceMuxInterrupted": gmfCntVoiceMuxInterrupted,
       "gmfCntDataQueueFull": gmfCntDataQueueFull,
       "gmfCntVoiceQueueFull": gmfCntVoiceQueueFull,
       "gmfCntUnexpSliceType": gmfCntUnexpSliceType,
       "gmfCntRouteChange": gmfCntRouteChange,
       "gmfCntTooManyCodes": gmfCntTooManyCodes,
       "gmfCntPosValidation": gmfCntPosValidation,
       "gmfCntNegValidation": gmfCntNegValidation,
       "gmfControlLink": gmfControlLink,
       "gmfDataOutWindowWidth": gmfDataOutWindowWidth,
       "gmfDataOutPriority": gmfDataOutPriority,
       "gmfSRTable": gmfSRTable,
       "gmfSREntry": gmfSREntry,
       "gmfSRLink": gmfSRLink,
       "gmfSRDestCircuitAlias": gmfSRDestCircuitAlias,
       "gmfSRSubRef": gmfSRSubRef,
       "gmfSRConStatus": gmfSRConStatus,
       "gmfSRFailStatus": gmfSRFailStatus,
       "gmfSRRowStatus": gmfSRRowStatus}
)
