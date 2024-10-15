# SNMP MIB module (Wellfleet-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:54 2024
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

(wfPingGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfPingGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfPingTable_Object = MibTable
wfPingTable = _WfPingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1)
)
if mibBuilder.loadTexts:
    wfPingTable.setStatus("mandatory")
_WfPingEntry_Object = MibTableRow
wfPingEntry = _WfPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1)
)
wfPingEntry.setIndexNames(
    (0, "Wellfleet-PING-MIB", "wfPingType"),
    (0, "Wellfleet-PING-MIB", "wfPingIndex"),
)
if mibBuilder.loadTexts:
    wfPingEntry.setStatus("mandatory")


class _WfPingDelete_Type(Integer32):
    """Custom type wfPingDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfPingDelete_Type.__name__ = "Integer32"
_WfPingDelete_Object = MibTableColumn
wfPingDelete = _WfPingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 1),
    _WfPingDelete_Type()
)
wfPingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingDelete.setStatus("mandatory")
_WfPingIndex_Type = Integer32
_WfPingIndex_Object = MibTableColumn
wfPingIndex = _WfPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 2),
    _WfPingIndex_Type()
)
wfPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingIndex.setStatus("mandatory")


class _WfPingType_Type(Integer32):
    """Custom type wfPingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 6),
          ("ip", 1),
          ("ipx", 2),
          ("llc", 3),
          ("osi", 4),
          ("vines", 5))
    )


_WfPingType_Type.__name__ = "Integer32"
_WfPingType_Object = MibTableColumn
wfPingType = _WfPingType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 3),
    _WfPingType_Type()
)
wfPingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingType.setStatus("mandatory")
_WfPingAddress_Type = OctetString
_WfPingAddress_Object = MibTableColumn
wfPingAddress = _WfPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 4),
    _WfPingAddress_Type()
)
wfPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingAddress.setStatus("mandatory")


class _WfPingSize_Type(Integer32):
    """Custom type wfPingSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4850),
    )


_WfPingSize_Type.__name__ = "Integer32"
_WfPingSize_Object = MibTableColumn
wfPingSize = _WfPingSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 5),
    _WfPingSize_Type()
)
wfPingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSize.setStatus("mandatory")


class _WfPingTimeOut_Type(Integer32):
    """Custom type wfPingTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfPingTimeOut_Type.__name__ = "Integer32"
_WfPingTimeOut_Object = MibTableColumn
wfPingTimeOut = _WfPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 6),
    _WfPingTimeOut_Type()
)
wfPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingTimeOut.setStatus("mandatory")


class _WfPingRetry_Type(Integer32):
    """Custom type wfPingRetry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfPingRetry_Type.__name__ = "Integer32"
_WfPingRetry_Object = MibTableColumn
wfPingRetry = _WfPingRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 7),
    _WfPingRetry_Type()
)
wfPingRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingRetry.setStatus("mandatory")


class _WfPingTraceRoute_Type(Integer32):
    """Custom type wfPingTraceRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notrace", 2),
          ("trace", 1))
    )


_WfPingTraceRoute_Type.__name__ = "Integer32"
_WfPingTraceRoute_Object = MibTableColumn
wfPingTraceRoute = _WfPingTraceRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 8),
    _WfPingTraceRoute_Type()
)
wfPingTraceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingTraceRoute.setStatus("mandatory")


class _WfPingDelay_Type(Integer32):
    """Custom type wfPingDelay based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfPingDelay_Type.__name__ = "Integer32"
_WfPingDelay_Object = MibTableColumn
wfPingDelay = _WfPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 9),
    _WfPingDelay_Type()
)
wfPingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingDelay.setStatus("mandatory")
_WfPingRemaining_Type = Integer32
_WfPingRemaining_Object = MibTableColumn
wfPingRemaining = _WfPingRemaining_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 10),
    _WfPingRemaining_Type()
)
wfPingRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingRemaining.setStatus("mandatory")


class _WfPingTimer_Type(Integer32):
    """Custom type wfPingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfPingTimer_Type.__name__ = "Integer32"
_WfPingTimer_Object = MibTableColumn
wfPingTimer = _WfPingTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 11),
    _WfPingTimer_Type()
)
wfPingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingTimer.setStatus("mandatory")


class _WfPingSourceRoute_Type(Integer32):
    """Custom type wfPingSourceRoute based on Integer32"""
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
        *(("loosesourceroute", 3),
          ("nosourceroute", 1),
          ("strictsourceroute", 2))
    )


_WfPingSourceRoute_Type.__name__ = "Integer32"
_WfPingSourceRoute_Object = MibTableColumn
wfPingSourceRoute = _WfPingSourceRoute_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 12),
    _WfPingSourceRoute_Type()
)
wfPingSourceRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSourceRoute.setStatus("mandatory")
_WfPingSourceAddress_Type = OctetString
_WfPingSourceAddress_Object = MibTableColumn
wfPingSourceAddress = _WfPingSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 13),
    _WfPingSourceAddress_Type()
)
wfPingSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSourceAddress.setStatus("mandatory")


class _WfPingTypeOfService_Type(Integer32):
    """Custom type wfPingTypeOfService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tosnormal", 1)
    )


_WfPingTypeOfService_Type.__name__ = "Integer32"
_WfPingTypeOfService_Object = MibTableColumn
wfPingTypeOfService = _WfPingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 14),
    _WfPingTypeOfService_Type()
)
wfPingTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingTypeOfService.setStatus("mandatory")


class _WfPingNumHistBucketsRequested_Type(Integer32):
    """Custom type wfPingNumHistBucketsRequested based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfPingNumHistBucketsRequested_Type.__name__ = "Integer32"
_WfPingNumHistBucketsRequested_Object = MibTableColumn
wfPingNumHistBucketsRequested = _WfPingNumHistBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 15),
    _WfPingNumHistBucketsRequested_Type()
)
wfPingNumHistBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingNumHistBucketsRequested.setStatus("mandatory")
_WfPingNumHistBucketsGranted_Type = Integer32
_WfPingNumHistBucketsGranted_Object = MibTableColumn
wfPingNumHistBucketsGranted = _WfPingNumHistBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 16),
    _WfPingNumHistBucketsGranted_Type()
)
wfPingNumHistBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingNumHistBucketsGranted.setStatus("mandatory")
_WfPingSiteName_Type = DisplayString
_WfPingSiteName_Object = MibTableColumn
wfPingSiteName = _WfPingSiteName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 17),
    _WfPingSiteName_Type()
)
wfPingSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSiteName.setStatus("mandatory")


class _WfPingStatus_Type(Integer32):
    """Custom type wfPingStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("badaddress", 3),
          ("busy", 2),
          ("done", 1),
          ("error", 4),
          ("fragneeded", 20),
          ("icmpdestunreach", 10),
          ("icmphostunreach", 13),
          ("icmpnetunreach", 14),
          ("icmpprohibhost", 16),
          ("icmpprohibnet", 15),
          ("icmpsrcrtefail", 17),
          ("invalidparams", 6),
          ("ipunavail", 9),
          ("notimplemented", 12),
          ("portunreach", 19),
          ("protounreach", 18),
          ("resourceerror", 7),
          ("targetunreach", 8),
          ("timeout", 5),
          ("ttlexceeded", 11))
    )


_WfPingStatus_Type.__name__ = "Integer32"
_WfPingStatus_Object = MibTableColumn
wfPingStatus = _WfPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 18),
    _WfPingStatus_Type()
)
wfPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingStatus.setStatus("mandatory")


class _WfPingAction_Type(Integer32):
    """Custom type wfPingAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("go", 1),
          ("waiting", 2))
    )


_WfPingAction_Type.__name__ = "Integer32"
_WfPingAction_Object = MibTableColumn
wfPingAction = _WfPingAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 19),
    _WfPingAction_Type()
)
wfPingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingAction.setStatus("mandatory")
_WfPingLastMinRoundTripTime_Type = Integer32
_WfPingLastMinRoundTripTime_Object = MibTableColumn
wfPingLastMinRoundTripTime = _WfPingLastMinRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 20),
    _WfPingLastMinRoundTripTime_Type()
)
wfPingLastMinRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingLastMinRoundTripTime.setStatus("mandatory")
_WfPingLastMaxRoundTripTime_Type = Integer32
_WfPingLastMaxRoundTripTime_Object = MibTableColumn
wfPingLastMaxRoundTripTime = _WfPingLastMaxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 21),
    _WfPingLastMaxRoundTripTime_Type()
)
wfPingLastMaxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingLastMaxRoundTripTime.setStatus("mandatory")
_WfPingLastTotalRoundTripTime_Type = Integer32
_WfPingLastTotalRoundTripTime_Object = MibTableColumn
wfPingLastTotalRoundTripTime = _WfPingLastTotalRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 22),
    _WfPingLastTotalRoundTripTime_Type()
)
wfPingLastTotalRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingLastTotalRoundTripTime.setStatus("mandatory")
_WfPingIPAddress_Type = IpAddress
_WfPingIPAddress_Object = MibTableColumn
wfPingIPAddress = _WfPingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 23),
    _WfPingIPAddress_Type()
)
wfPingIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingIPAddress.setStatus("mandatory")
_WfPingSuccessStatus_Type = Integer32
_WfPingSuccessStatus_Object = MibTableColumn
wfPingSuccessStatus = _WfPingSuccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 24),
    _WfPingSuccessStatus_Type()
)
wfPingSuccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingSuccessStatus.setStatus("mandatory")


class _WfPingMaxHopCount_Type(Integer32):
    """Custom type wfPingMaxHopCount based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfPingMaxHopCount_Type.__name__ = "Integer32"
_WfPingMaxHopCount_Object = MibTableColumn
wfPingMaxHopCount = _WfPingMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 1, 1, 25),
    _WfPingMaxHopCount_Type()
)
wfPingMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingMaxHopCount.setStatus("mandatory")
_WfPingTraceTable_Object = MibTable
wfPingTraceTable = _WfPingTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2)
)
if mibBuilder.loadTexts:
    wfPingTraceTable.setStatus("mandatory")
_WfPingTraceEntry_Object = MibTableRow
wfPingTraceEntry = _WfPingTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2, 1)
)
wfPingTraceEntry.setIndexNames(
    (0, "Wellfleet-PING-MIB", "wfPingTraceType"),
    (0, "Wellfleet-PING-MIB", "wfPingEntryIndex"),
    (0, "Wellfleet-PING-MIB", "wfPingTraceIndex"),
)
if mibBuilder.loadTexts:
    wfPingTraceEntry.setStatus("mandatory")
_WfPingTraceType_Type = Integer32
_WfPingTraceType_Object = MibTableColumn
wfPingTraceType = _WfPingTraceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2, 1, 1),
    _WfPingTraceType_Type()
)
wfPingTraceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingTraceType.setStatus("mandatory")
_WfPingEntryIndex_Type = Integer32
_WfPingEntryIndex_Object = MibTableColumn
wfPingEntryIndex = _WfPingEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2, 1, 2),
    _WfPingEntryIndex_Type()
)
wfPingEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingEntryIndex.setStatus("mandatory")
_WfPingTraceIndex_Type = Integer32
_WfPingTraceIndex_Object = MibTableColumn
wfPingTraceIndex = _WfPingTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2, 1, 3),
    _WfPingTraceIndex_Type()
)
wfPingTraceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingTraceIndex.setStatus("mandatory")
_WfPingTraceAddress_Type = OctetString
_WfPingTraceAddress_Object = MibTableColumn
wfPingTraceAddress = _WfPingTraceAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 2, 1, 4),
    _WfPingTraceAddress_Type()
)
wfPingTraceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingTraceAddress.setStatus("mandatory")
_WfPingSourceTable_Object = MibTable
wfPingSourceTable = _WfPingSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3)
)
if mibBuilder.loadTexts:
    wfPingSourceTable.setStatus("mandatory")
_WfPingSourceEntry_Object = MibTableRow
wfPingSourceEntry = _WfPingSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1)
)
wfPingSourceEntry.setIndexNames(
    (0, "Wellfleet-PING-MIB", "wfPingSourceType"),
    (0, "Wellfleet-PING-MIB", "wfPingSourceEntryIndex"),
    (0, "Wellfleet-PING-MIB", "wfPingSourceIndex"),
)
if mibBuilder.loadTexts:
    wfPingSourceEntry.setStatus("mandatory")


class _WfPingSourceDelete_Type(Integer32):
    """Custom type wfPingSourceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sourcecreated", 1),
          ("sourcedeleted", 2))
    )


_WfPingSourceDelete_Type.__name__ = "Integer32"
_WfPingSourceDelete_Object = MibTableColumn
wfPingSourceDelete = _WfPingSourceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1, 1),
    _WfPingSourceDelete_Type()
)
wfPingSourceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSourceDelete.setStatus("mandatory")
_WfPingSourceType_Type = Integer32
_WfPingSourceType_Object = MibTableColumn
wfPingSourceType = _WfPingSourceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1, 2),
    _WfPingSourceType_Type()
)
wfPingSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingSourceType.setStatus("mandatory")
_WfPingSourceEntryIndex_Type = Integer32
_WfPingSourceEntryIndex_Object = MibTableColumn
wfPingSourceEntryIndex = _WfPingSourceEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1, 3),
    _WfPingSourceEntryIndex_Type()
)
wfPingSourceEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingSourceEntryIndex.setStatus("mandatory")
_WfPingSourceIndex_Type = Integer32
_WfPingSourceIndex_Object = MibTableColumn
wfPingSourceIndex = _WfPingSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1, 4),
    _WfPingSourceIndex_Type()
)
wfPingSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingSourceIndex.setStatus("mandatory")
_WfPingSourceRouteAddress_Type = OctetString
_WfPingSourceRouteAddress_Object = MibTableColumn
wfPingSourceRouteAddress = _WfPingSourceRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 3, 1, 5),
    _WfPingSourceRouteAddress_Type()
)
wfPingSourceRouteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPingSourceRouteAddress.setStatus("mandatory")
_WfPingHistoryTable_Object = MibTable
wfPingHistoryTable = _WfPingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4)
)
if mibBuilder.loadTexts:
    wfPingHistoryTable.setStatus("mandatory")
_WfPingHistoryEntry_Object = MibTableRow
wfPingHistoryEntry = _WfPingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1)
)
wfPingHistoryEntry.setIndexNames(
    (0, "Wellfleet-PING-MIB", "wfPingHistoryType"),
    (0, "Wellfleet-PING-MIB", "wfPingHistoryEntryIndex"),
    (0, "Wellfleet-PING-MIB", "wfPingHistoryIndex"),
)
if mibBuilder.loadTexts:
    wfPingHistoryEntry.setStatus("mandatory")
_WfPingHistoryType_Type = Integer32
_WfPingHistoryType_Object = MibTableColumn
wfPingHistoryType = _WfPingHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 1),
    _WfPingHistoryType_Type()
)
wfPingHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingHistoryType.setStatus("mandatory")
_WfPingHistoryEntryIndex_Type = Integer32
_WfPingHistoryEntryIndex_Object = MibTableColumn
wfPingHistoryEntryIndex = _WfPingHistoryEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 2),
    _WfPingHistoryEntryIndex_Type()
)
wfPingHistoryEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingHistoryEntryIndex.setStatus("mandatory")
_WfPingHistoryIndex_Type = Integer32
_WfPingHistoryIndex_Object = MibTableColumn
wfPingHistoryIndex = _WfPingHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 3),
    _WfPingHistoryIndex_Type()
)
wfPingHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingHistoryIndex.setStatus("mandatory")
_WfPingReceived_Type = Gauge32
_WfPingReceived_Object = MibTableColumn
wfPingReceived = _WfPingReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 4),
    _WfPingReceived_Type()
)
wfPingReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingReceived.setStatus("mandatory")
_WfPingDropped_Type = Gauge32
_WfPingDropped_Object = MibTableColumn
wfPingDropped = _WfPingDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 5),
    _WfPingDropped_Type()
)
wfPingDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingDropped.setStatus("mandatory")
_WfPingRoundTripTime_Type = Integer32
_WfPingRoundTripTime_Object = MibTableColumn
wfPingRoundTripTime = _WfPingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 6),
    _WfPingRoundTripTime_Type()
)
wfPingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingRoundTripTime.setStatus("mandatory")
_WfPingTotalRoundTripTime_Type = Integer32
_WfPingTotalRoundTripTime_Object = MibTableColumn
wfPingTotalRoundTripTime = _WfPingTotalRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 7),
    _WfPingTotalRoundTripTime_Type()
)
wfPingTotalRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingTotalRoundTripTime.setStatus("mandatory")
_WfPingMinRoundTripTime_Type = Integer32
_WfPingMinRoundTripTime_Object = MibTableColumn
wfPingMinRoundTripTime = _WfPingMinRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 8),
    _WfPingMinRoundTripTime_Type()
)
wfPingMinRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingMinRoundTripTime.setStatus("mandatory")
_WfPingMaxRoundTripTime_Type = Integer32
_WfPingMaxRoundTripTime_Object = MibTableColumn
wfPingMaxRoundTripTime = _WfPingMaxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 9),
    _WfPingMaxRoundTripTime_Type()
)
wfPingMaxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingMaxRoundTripTime.setStatus("mandatory")
_WfPingBegan_Type = OctetString
_WfPingBegan_Object = MibTableColumn
wfPingBegan = _WfPingBegan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 13, 4, 1, 10),
    _WfPingBegan_Type()
)
wfPingBegan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPingBegan.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PING-MIB",
    **{"wfPingTable": wfPingTable,
       "wfPingEntry": wfPingEntry,
       "wfPingDelete": wfPingDelete,
       "wfPingIndex": wfPingIndex,
       "wfPingType": wfPingType,
       "wfPingAddress": wfPingAddress,
       "wfPingSize": wfPingSize,
       "wfPingTimeOut": wfPingTimeOut,
       "wfPingRetry": wfPingRetry,
       "wfPingTraceRoute": wfPingTraceRoute,
       "wfPingDelay": wfPingDelay,
       "wfPingRemaining": wfPingRemaining,
       "wfPingTimer": wfPingTimer,
       "wfPingSourceRoute": wfPingSourceRoute,
       "wfPingSourceAddress": wfPingSourceAddress,
       "wfPingTypeOfService": wfPingTypeOfService,
       "wfPingNumHistBucketsRequested": wfPingNumHistBucketsRequested,
       "wfPingNumHistBucketsGranted": wfPingNumHistBucketsGranted,
       "wfPingSiteName": wfPingSiteName,
       "wfPingStatus": wfPingStatus,
       "wfPingAction": wfPingAction,
       "wfPingLastMinRoundTripTime": wfPingLastMinRoundTripTime,
       "wfPingLastMaxRoundTripTime": wfPingLastMaxRoundTripTime,
       "wfPingLastTotalRoundTripTime": wfPingLastTotalRoundTripTime,
       "wfPingIPAddress": wfPingIPAddress,
       "wfPingSuccessStatus": wfPingSuccessStatus,
       "wfPingMaxHopCount": wfPingMaxHopCount,
       "wfPingTraceTable": wfPingTraceTable,
       "wfPingTraceEntry": wfPingTraceEntry,
       "wfPingTraceType": wfPingTraceType,
       "wfPingEntryIndex": wfPingEntryIndex,
       "wfPingTraceIndex": wfPingTraceIndex,
       "wfPingTraceAddress": wfPingTraceAddress,
       "wfPingSourceTable": wfPingSourceTable,
       "wfPingSourceEntry": wfPingSourceEntry,
       "wfPingSourceDelete": wfPingSourceDelete,
       "wfPingSourceType": wfPingSourceType,
       "wfPingSourceEntryIndex": wfPingSourceEntryIndex,
       "wfPingSourceIndex": wfPingSourceIndex,
       "wfPingSourceRouteAddress": wfPingSourceRouteAddress,
       "wfPingHistoryTable": wfPingHistoryTable,
       "wfPingHistoryEntry": wfPingHistoryEntry,
       "wfPingHistoryType": wfPingHistoryType,
       "wfPingHistoryEntryIndex": wfPingHistoryEntryIndex,
       "wfPingHistoryIndex": wfPingHistoryIndex,
       "wfPingReceived": wfPingReceived,
       "wfPingDropped": wfPingDropped,
       "wfPingRoundTripTime": wfPingRoundTripTime,
       "wfPingTotalRoundTripTime": wfPingTotalRoundTripTime,
       "wfPingMinRoundTripTime": wfPingMinRoundTripTime,
       "wfPingMaxRoundTripTime": wfPingMaxRoundTripTime,
       "wfPingBegan": wfPingBegan}
)
