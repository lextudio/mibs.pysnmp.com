# SNMP MIB module (WWP-LEOS-MPLS-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-MPLS-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:57 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosMPLSOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36)
)
wwpLeosMPLSOamMIB.setRevisions(
        ("2006-05-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OperationResponseStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("maxConcurrentLimitReached", 6),
          ("requestTimedOut", 4),
          ("responseReceived", 1),
          ("unknown", 2),
          ("unknownLsp", 5))
    )



class LspPingReturnCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("downstreamMappingMismatch", 5),
          ("egressForFec", 3),
          ("labelSwitchedFec", 8),
          ("labelSwitchedNoForwardingFec", 9),
          ("malformedEchoRequest", 1),
          ("noLabel", 11),
          ("noMappingForFec", 4),
          ("noReturnCode", 0),
          ("oneOrMoreTlvsNotUnderstood", 2),
          ("unknownFec", 12),
          ("upstreamInterfaceIndexUnknown", 6),
          ("wrongLabel", 10))
    )



class LspType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rsvpTeTunnel", 1)
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosMPLSOamObjects_ObjectIdentity = ObjectIdentity
wwpLeosMPLSOamObjects = _WwpLeosMPLSOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1)
)
_WwpLeosMPLSOAMLspPingMax_Type = Unsigned32
_WwpLeosMPLSOAMLspPingMax_Object = MibScalar
wwpLeosMPLSOAMLspPingMax = _WwpLeosMPLSOAMLspPingMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 1),
    _WwpLeosMPLSOAMLspPingMax_Type()
)
wwpLeosMPLSOAMLspPingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOAMLspPingMax.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOAMLspPingMax.setUnits("requests")
_WwpLeosMPLSOAMLspTraceRtMax_Type = Unsigned32
_WwpLeosMPLSOAMLspTraceRtMax_Object = MibScalar
wwpLeosMPLSOAMLspTraceRtMax = _WwpLeosMPLSOAMLspTraceRtMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 2),
    _WwpLeosMPLSOAMLspTraceRtMax_Type()
)
wwpLeosMPLSOAMLspTraceRtMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOAMLspTraceRtMax.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOAMLspTraceRtMax.setUnits("requests")
_WwpLeosMPLSOamLspPingCtlTable_Object = MibTable
wwpLeosMPLSOamLspPingCtlTable = _WwpLeosMPLSOamLspPingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlTable.setStatus("current")
_WwpLeosMPLSOamLspPingCtlEntry_Object = MibTableRow
wwpLeosMPLSOamLspPingCtlEntry = _WwpLeosMPLSOamLspPingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1)
)
wwpLeosMPLSOamLspPingCtlEntry.setIndexNames(
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspPingCtlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlEntry.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlIndex_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspPingCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosMPLSOamLspPingCtlIndex_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspPingCtlIndex_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlIndex = _WwpLeosMPLSOamLspPingCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 1),
    _WwpLeosMPLSOamLspPingCtlIndex_Type()
)
wwpLeosMPLSOamLspPingCtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlIndex.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlLspType_Type(LspType):
    """Custom type wwpLeosMPLSOamLspPingCtlLspType based on LspType"""


_WwpLeosMPLSOamLspPingCtlLspType_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlLspType = _WwpLeosMPLSOamLspPingCtlLspType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 3),
    _WwpLeosMPLSOamLspPingCtlLspType_Type()
)
wwpLeosMPLSOamLspPingCtlLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlLspType.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlLspName_Type(DisplayString):
    """Custom type wwpLeosMPLSOamLspPingCtlLspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosMPLSOamLspPingCtlLspName_Type.__name__ = "DisplayString"
_WwpLeosMPLSOamLspPingCtlLspName_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlLspName = _WwpLeosMPLSOamLspPingCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 4),
    _WwpLeosMPLSOamLspPingCtlLspName_Type()
)
wwpLeosMPLSOamLspPingCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlLspName.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlPktSize_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspPingCtlPktSize based on Unsigned32"""
    defaultValue = 96

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 1464),
    )


_WwpLeosMPLSOamLspPingCtlPktSize_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspPingCtlPktSize_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlPktSize = _WwpLeosMPLSOamLspPingCtlPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 5),
    _WwpLeosMPLSOamLspPingCtlPktSize_Type()
)
wwpLeosMPLSOamLspPingCtlPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlPktSize.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlTimeOut_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspPingCtlTimeOut based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_WwpLeosMPLSOamLspPingCtlTimeOut_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspPingCtlTimeOut_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlTimeOut = _WwpLeosMPLSOamLspPingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 6),
    _WwpLeosMPLSOamLspPingCtlTimeOut_Type()
)
wwpLeosMPLSOamLspPingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlTimeOut.setUnits("seconds")


class _WwpLeosMPLSOamLspPingCtlCount_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspPingCtlCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosMPLSOamLspPingCtlCount_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspPingCtlCount_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlCount = _WwpLeosMPLSOamLspPingCtlCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 7),
    _WwpLeosMPLSOamLspPingCtlCount_Type()
)
wwpLeosMPLSOamLspPingCtlCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlCount.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlAdminState_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspPingCtlAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosMPLSOamLspPingCtlAdminState_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspPingCtlAdminState_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlAdminState = _WwpLeosMPLSOamLspPingCtlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 8),
    _WwpLeosMPLSOamLspPingCtlAdminState_Type()
)
wwpLeosMPLSOamLspPingCtlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlAdminState.setStatus("current")


class _WwpLeosMPLSOamLspPingCtlTtl_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspPingCtlTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosMPLSOamLspPingCtlTtl_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspPingCtlTtl_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlTtl = _WwpLeosMPLSOamLspPingCtlTtl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 9),
    _WwpLeosMPLSOamLspPingCtlTtl_Type()
)
wwpLeosMPLSOamLspPingCtlTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlTtl.setStatus("current")
_WwpLeosMPLSOamLspPingCtlRowStatus_Type = RowStatus
_WwpLeosMPLSOamLspPingCtlRowStatus_Object = MibTableColumn
wwpLeosMPLSOamLspPingCtlRowStatus = _WwpLeosMPLSOamLspPingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 3, 1, 10),
    _WwpLeosMPLSOamLspPingCtlRowStatus_Type()
)
wwpLeosMPLSOamLspPingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingCtlRowStatus.setStatus("current")
_WwpLeosMPLSOamLspPingResultsTable_Object = MibTable
wwpLeosMPLSOamLspPingResultsTable = _WwpLeosMPLSOamLspPingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsTable.setStatus("current")
_WwpLeosMPLSOamLspPingResultsEntry_Object = MibTableRow
wwpLeosMPLSOamLspPingResultsEntry = _WwpLeosMPLSOamLspPingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1)
)
wwpLeosMPLSOamLspPingResultsEntry.setIndexNames(
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspPingCtlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsEntry.setStatus("current")


class _WwpLeosMPLSOamLspPingResultsOperStatus_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspPingResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosMPLSOamLspPingResultsOperStatus_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspPingResultsOperStatus_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsOperStatus = _WwpLeosMPLSOamLspPingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 1),
    _WwpLeosMPLSOamLspPingResultsOperStatus_Type()
)
wwpLeosMPLSOamLspPingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsOperStatus.setStatus("current")


class _WwpLeosMPLSOamLspPingResultsStatus_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspPingResultsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("success", 2),
          ("unknown", 1))
    )


_WwpLeosMPLSOamLspPingResultsStatus_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspPingResultsStatus_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsStatus = _WwpLeosMPLSOamLspPingResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 2),
    _WwpLeosMPLSOamLspPingResultsStatus_Type()
)
wwpLeosMPLSOamLspPingResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsStatus.setStatus("current")
_WwpLeosMPLSOamLspPingResultsLspType_Type = LspType
_WwpLeosMPLSOamLspPingResultsLspType_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsLspType = _WwpLeosMPLSOamLspPingResultsLspType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 3),
    _WwpLeosMPLSOamLspPingResultsLspType_Type()
)
wwpLeosMPLSOamLspPingResultsLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsLspType.setStatus("current")


class _WwpLeosMPLSOamLspPingResultsLspName_Type(OctetString):
    """Custom type wwpLeosMPLSOamLspPingResultsLspName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosMPLSOamLspPingResultsLspName_Type.__name__ = "OctetString"
_WwpLeosMPLSOamLspPingResultsLspName_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsLspName = _WwpLeosMPLSOamLspPingResultsLspName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 4),
    _WwpLeosMPLSOamLspPingResultsLspName_Type()
)
wwpLeosMPLSOamLspPingResultsLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsLspName.setStatus("current")
_WwpLeosMPLSOamLspPingResultsMinRtt_Type = Unsigned32
_WwpLeosMPLSOamLspPingResultsMinRtt_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsMinRtt = _WwpLeosMPLSOamLspPingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 5),
    _WwpLeosMPLSOamLspPingResultsMinRtt_Type()
)
wwpLeosMPLSOamLspPingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsMinRtt.setUnits("milliseconds")
_WwpLeosMPLSOamLspPingResultsMaxRtt_Type = Unsigned32
_WwpLeosMPLSOamLspPingResultsMaxRtt_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsMaxRtt = _WwpLeosMPLSOamLspPingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 6),
    _WwpLeosMPLSOamLspPingResultsMaxRtt_Type()
)
wwpLeosMPLSOamLspPingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsMaxRtt.setUnits("milliseconds")
_WwpLeosMPLSOamLspPingResultsAverageRtt_Type = Unsigned32
_WwpLeosMPLSOamLspPingResultsAverageRtt_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsAverageRtt = _WwpLeosMPLSOamLspPingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 7),
    _WwpLeosMPLSOamLspPingResultsAverageRtt_Type()
)
wwpLeosMPLSOamLspPingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsAverageRtt.setUnits("milliseconds")
_WwpLeosMPLSOamLspPingResultsProbesSent_Type = Unsigned32
_WwpLeosMPLSOamLspPingResultsProbesSent_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsProbesSent = _WwpLeosMPLSOamLspPingResultsProbesSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 8),
    _WwpLeosMPLSOamLspPingResultsProbesSent_Type()
)
wwpLeosMPLSOamLspPingResultsProbesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsProbesSent.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsProbesSent.setUnits("probes")
_WwpLeosMPLSOamLspPingResultsProbeResponses_Type = Unsigned32
_WwpLeosMPLSOamLspPingResultsProbeResponses_Object = MibTableColumn
wwpLeosMPLSOamLspPingResultsProbeResponses = _WwpLeosMPLSOamLspPingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 4, 1, 9),
    _WwpLeosMPLSOamLspPingResultsProbeResponses_Type()
)
wwpLeosMPLSOamLspPingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspPingResultsProbeResponses.setUnits("responses")
_WwpLeosMPLSOamLspTraceRouteCtlTable_Object = MibTable
wwpLeosMPLSOamLspTraceRouteCtlTable = _WwpLeosMPLSOamLspTraceRouteCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlTable.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteCtlEntry_Object = MibTableRow
wwpLeosMPLSOamLspTraceRouteCtlEntry = _WwpLeosMPLSOamLspTraceRouteCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1)
)
wwpLeosMPLSOamLspTraceRouteCtlEntry.setIndexNames(
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspTraceRouteCtlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlEntry.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteCtlIndex_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosMPLSOamLspTraceRouteCtlIndex_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspTraceRouteCtlIndex_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlIndex = _WwpLeosMPLSOamLspTraceRouteCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 1),
    _WwpLeosMPLSOamLspTraceRouteCtlIndex_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlIndex.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteCtlLspType_Type(LspType):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlLspType based on LspType"""


_WwpLeosMPLSOamLspTraceRouteCtlLspType_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlLspType = _WwpLeosMPLSOamLspTraceRouteCtlLspType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 2),
    _WwpLeosMPLSOamLspTraceRouteCtlLspType_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlLspType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlLspType.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteCtlLspName_Type(DisplayString):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlLspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_WwpLeosMPLSOamLspTraceRouteCtlLspName_Type.__name__ = "DisplayString"
_WwpLeosMPLSOamLspTraceRouteCtlLspName_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlLspName = _WwpLeosMPLSOamLspTraceRouteCtlLspName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 3),
    _WwpLeosMPLSOamLspTraceRouteCtlLspName_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlLspName.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlTimeOut = _WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 4),
    _WwpLeosMPLSOamLspTraceRouteCtlTimeOut_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlTimeOut.setUnits("seconds")


class _WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlMaxTtl = _WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 5),
    _WwpLeosMPLSOamLspTraceRouteCtlMaxTtl_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlMaxTtl.setUnits("time-to-live value")


class _WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspTraceRouteCtlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlAdminStatus = _WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 6),
    _WwpLeosMPLSOamLspTraceRouteCtlAdminStatus_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlAdminStatus.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Type = RowStatus
_WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteCtlRowStatus = _WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 5, 1, 7),
    _WwpLeosMPLSOamLspTraceRouteCtlRowStatus_Type()
)
wwpLeosMPLSOamLspTraceRouteCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteCtlRowStatus.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteResultsTable_Object = MibTable
wwpLeosMPLSOamLspTraceRouteResultsTable = _WwpLeosMPLSOamLspTraceRouteResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsTable.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteResultsEntry_Object = MibTableRow
wwpLeosMPLSOamLspTraceRouteResultsEntry = _WwpLeosMPLSOamLspTraceRouteResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 6, 1)
)
wwpLeosMPLSOamLspTraceRouteResultsEntry.setIndexNames(
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspTraceRouteCtlIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsEntry.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspTraceRouteResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsOperStatus = _WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 6, 1, 1),
    _WwpLeosMPLSOamLspTraceRouteResultsOperStatus_Type()
)
wwpLeosMPLSOamLspTraceRouteResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsOperStatus.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteResultsStatus_Type(Integer32):
    """Custom type wwpLeosMPLSOamLspTraceRouteResultsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("success", 2),
          ("unknown", 1))
    )


_WwpLeosMPLSOamLspTraceRouteResultsStatus_Type.__name__ = "Integer32"
_WwpLeosMPLSOamLspTraceRouteResultsStatus_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsStatus = _WwpLeosMPLSOamLspTraceRouteResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 6, 1, 2),
    _WwpLeosMPLSOamLspTraceRouteResultsStatus_Type()
)
wwpLeosMPLSOamLspTraceRouteResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsStatus.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Type = Gauge32
_WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteResultsCurHopCount = _WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 6, 1, 3),
    _WwpLeosMPLSOamLspTraceRouteResultsCurHopCount_Type()
)
wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteResultsCurHopCount.setUnits("hops")
_WwpLeosMPLSOamLspTraceRouteHopTable_Object = MibTable
wwpLeosMPLSOamLspTraceRouteHopTable = _WwpLeosMPLSOamLspTraceRouteHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopTable.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteHopEntry_Object = MibTableRow
wwpLeosMPLSOamLspTraceRouteHopEntry = _WwpLeosMPLSOamLspTraceRouteHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 7, 1)
)
wwpLeosMPLSOamLspTraceRouteHopEntry.setIndexNames(
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspTraceRouteCtlIndex"),
    (0, "WWP-LEOS-MPLS-OAM-MIB", "wwpLeosMPLSOamLspTraceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopEntry.setStatus("current")


class _WwpLeosMPLSOamLspTraceRouteHopIndex_Type(Unsigned32):
    """Custom type wwpLeosMPLSOamLspTraceRouteHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosMPLSOamLspTraceRouteHopIndex_Type.__name__ = "Unsigned32"
_WwpLeosMPLSOamLspTraceRouteHopIndex_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopIndex = _WwpLeosMPLSOamLspTraceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 7, 1, 1),
    _WwpLeosMPLSOamLspTraceRouteHopIndex_Type()
)
wwpLeosMPLSOamLspTraceRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopIndex.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopIndex.setUnits("hops")
_WwpLeosMPLSOamLspTraceRouteHopIp_Type = IpAddress
_WwpLeosMPLSOamLspTraceRouteHopIp_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopIp = _WwpLeosMPLSOamLspTraceRouteHopIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 7, 1, 2),
    _WwpLeosMPLSOamLspTraceRouteHopIp_Type()
)
wwpLeosMPLSOamLspTraceRouteHopIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopIp.setStatus("current")
_WwpLeosMPLSOamLspTraceRouteHopLabel_Type = Unsigned32
_WwpLeosMPLSOamLspTraceRouteHopLabel_Object = MibTableColumn
wwpLeosMPLSOamLspTraceRouteHopLabel = _WwpLeosMPLSOamLspTraceRouteHopLabel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 1, 7, 1, 3),
    _WwpLeosMPLSOamLspTraceRouteHopLabel_Type()
)
wwpLeosMPLSOamLspTraceRouteHopLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMPLSOamLspTraceRouteHopLabel.setStatus("current")
_WwpLeosMPLSOamNotifications_ObjectIdentity = ObjectIdentity
wwpLeosMPLSOamNotifications = _WwpLeosMPLSOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 2)
)
_WwpLeosMPLSOamConformance_ObjectIdentity = ObjectIdentity
wwpLeosMPLSOamConformance = _WwpLeosMPLSOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 36, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-MPLS-OAM-MIB",
    **{"OperationResponseStatus": OperationResponseStatus,
       "LspPingReturnCode": LspPingReturnCode,
       "LspType": LspType,
       "wwpLeosMPLSOamMIB": wwpLeosMPLSOamMIB,
       "wwpLeosMPLSOamObjects": wwpLeosMPLSOamObjects,
       "wwpLeosMPLSOAMLspPingMax": wwpLeosMPLSOAMLspPingMax,
       "wwpLeosMPLSOAMLspTraceRtMax": wwpLeosMPLSOAMLspTraceRtMax,
       "wwpLeosMPLSOamLspPingCtlTable": wwpLeosMPLSOamLspPingCtlTable,
       "wwpLeosMPLSOamLspPingCtlEntry": wwpLeosMPLSOamLspPingCtlEntry,
       "wwpLeosMPLSOamLspPingCtlIndex": wwpLeosMPLSOamLspPingCtlIndex,
       "wwpLeosMPLSOamLspPingCtlLspType": wwpLeosMPLSOamLspPingCtlLspType,
       "wwpLeosMPLSOamLspPingCtlLspName": wwpLeosMPLSOamLspPingCtlLspName,
       "wwpLeosMPLSOamLspPingCtlPktSize": wwpLeosMPLSOamLspPingCtlPktSize,
       "wwpLeosMPLSOamLspPingCtlTimeOut": wwpLeosMPLSOamLspPingCtlTimeOut,
       "wwpLeosMPLSOamLspPingCtlCount": wwpLeosMPLSOamLspPingCtlCount,
       "wwpLeosMPLSOamLspPingCtlAdminState": wwpLeosMPLSOamLspPingCtlAdminState,
       "wwpLeosMPLSOamLspPingCtlTtl": wwpLeosMPLSOamLspPingCtlTtl,
       "wwpLeosMPLSOamLspPingCtlRowStatus": wwpLeosMPLSOamLspPingCtlRowStatus,
       "wwpLeosMPLSOamLspPingResultsTable": wwpLeosMPLSOamLspPingResultsTable,
       "wwpLeosMPLSOamLspPingResultsEntry": wwpLeosMPLSOamLspPingResultsEntry,
       "wwpLeosMPLSOamLspPingResultsOperStatus": wwpLeosMPLSOamLspPingResultsOperStatus,
       "wwpLeosMPLSOamLspPingResultsStatus": wwpLeosMPLSOamLspPingResultsStatus,
       "wwpLeosMPLSOamLspPingResultsLspType": wwpLeosMPLSOamLspPingResultsLspType,
       "wwpLeosMPLSOamLspPingResultsLspName": wwpLeosMPLSOamLspPingResultsLspName,
       "wwpLeosMPLSOamLspPingResultsMinRtt": wwpLeosMPLSOamLspPingResultsMinRtt,
       "wwpLeosMPLSOamLspPingResultsMaxRtt": wwpLeosMPLSOamLspPingResultsMaxRtt,
       "wwpLeosMPLSOamLspPingResultsAverageRtt": wwpLeosMPLSOamLspPingResultsAverageRtt,
       "wwpLeosMPLSOamLspPingResultsProbesSent": wwpLeosMPLSOamLspPingResultsProbesSent,
       "wwpLeosMPLSOamLspPingResultsProbeResponses": wwpLeosMPLSOamLspPingResultsProbeResponses,
       "wwpLeosMPLSOamLspTraceRouteCtlTable": wwpLeosMPLSOamLspTraceRouteCtlTable,
       "wwpLeosMPLSOamLspTraceRouteCtlEntry": wwpLeosMPLSOamLspTraceRouteCtlEntry,
       "wwpLeosMPLSOamLspTraceRouteCtlIndex": wwpLeosMPLSOamLspTraceRouteCtlIndex,
       "wwpLeosMPLSOamLspTraceRouteCtlLspType": wwpLeosMPLSOamLspTraceRouteCtlLspType,
       "wwpLeosMPLSOamLspTraceRouteCtlLspName": wwpLeosMPLSOamLspTraceRouteCtlLspName,
       "wwpLeosMPLSOamLspTraceRouteCtlTimeOut": wwpLeosMPLSOamLspTraceRouteCtlTimeOut,
       "wwpLeosMPLSOamLspTraceRouteCtlMaxTtl": wwpLeosMPLSOamLspTraceRouteCtlMaxTtl,
       "wwpLeosMPLSOamLspTraceRouteCtlAdminStatus": wwpLeosMPLSOamLspTraceRouteCtlAdminStatus,
       "wwpLeosMPLSOamLspTraceRouteCtlRowStatus": wwpLeosMPLSOamLspTraceRouteCtlRowStatus,
       "wwpLeosMPLSOamLspTraceRouteResultsTable": wwpLeosMPLSOamLspTraceRouteResultsTable,
       "wwpLeosMPLSOamLspTraceRouteResultsEntry": wwpLeosMPLSOamLspTraceRouteResultsEntry,
       "wwpLeosMPLSOamLspTraceRouteResultsOperStatus": wwpLeosMPLSOamLspTraceRouteResultsOperStatus,
       "wwpLeosMPLSOamLspTraceRouteResultsStatus": wwpLeosMPLSOamLspTraceRouteResultsStatus,
       "wwpLeosMPLSOamLspTraceRouteResultsCurHopCount": wwpLeosMPLSOamLspTraceRouteResultsCurHopCount,
       "wwpLeosMPLSOamLspTraceRouteHopTable": wwpLeosMPLSOamLspTraceRouteHopTable,
       "wwpLeosMPLSOamLspTraceRouteHopEntry": wwpLeosMPLSOamLspTraceRouteHopEntry,
       "wwpLeosMPLSOamLspTraceRouteHopIndex": wwpLeosMPLSOamLspTraceRouteHopIndex,
       "wwpLeosMPLSOamLspTraceRouteHopIp": wwpLeosMPLSOamLspTraceRouteHopIp,
       "wwpLeosMPLSOamLspTraceRouteHopLabel": wwpLeosMPLSOamLspTraceRouteHopLabel,
       "wwpLeosMPLSOamNotifications": wwpLeosMPLSOamNotifications,
       "wwpLeosMPLSOamConformance": wwpLeosMPLSOamConformance}
)
