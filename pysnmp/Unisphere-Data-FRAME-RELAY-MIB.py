# SNMP MIB module (Unisphere-Data-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:44 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10)
)
usdFrameRelayMIB.setRevisions(
        ("2000-09-26 17:30",
         "1999-06-01 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdFrObjects_ObjectIdentity = ObjectIdentity
usdFrObjects = _UsdFrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1)
)
_UsdFrIfLayer_ObjectIdentity = ObjectIdentity
usdFrIfLayer = _UsdFrIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1)
)
_UsdFrNextIfIndex_Type = UsdNextIfIndex
_UsdFrNextIfIndex_Object = MibScalar
usdFrNextIfIndex = _UsdFrNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 1),
    _UsdFrNextIfIndex_Type()
)
usdFrNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrNextIfIndex.setStatus("current")
_UsdFrDlcmiTable_Object = MibTable
usdFrDlcmiTable = _UsdFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdFrDlcmiTable.setStatus("current")
_UsdFrDlcmiEntry_Object = MibTableRow
usdFrDlcmiEntry = _UsdFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1)
)
usdFrDlcmiEntry.setIndexNames(
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    usdFrDlcmiEntry.setStatus("current")
_UsdFrDlcmiIfIndex_Type = InterfaceIndex
_UsdFrDlcmiIfIndex_Object = MibTableColumn
usdFrDlcmiIfIndex = _UsdFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 1),
    _UsdFrDlcmiIfIndex_Type()
)
usdFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiIfIndex.setStatus("current")


class _UsdFrDlcmiState_Type(Integer32):
    """Custom type usdFrDlcmiState based on Integer32"""
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
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ansiT1617D1994", 6),
          ("itut933A", 5),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_UsdFrDlcmiState_Type.__name__ = "Integer32"
_UsdFrDlcmiState_Object = MibTableColumn
usdFrDlcmiState = _UsdFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 2),
    _UsdFrDlcmiState_Type()
)
usdFrDlcmiState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiState.setStatus("current")


class _UsdFrDlcmiAddress_Type(Integer32):
    """Custom type usdFrDlcmiAddress based on Integer32"""
    defaultValue = 4

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
        *(("q921", 1),
          ("q922", 4),
          ("q922March90", 2),
          ("q922November90", 3))
    )


_UsdFrDlcmiAddress_Type.__name__ = "Integer32"
_UsdFrDlcmiAddress_Object = MibTableColumn
usdFrDlcmiAddress = _UsdFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 3),
    _UsdFrDlcmiAddress_Type()
)
usdFrDlcmiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiAddress.setStatus("current")


class _UsdFrDlcmiAddressLen_Type(Integer32):
    """Custom type usdFrDlcmiAddressLen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourOctets", 4),
          ("threeOctets", 3),
          ("twoOctets", 2))
    )


_UsdFrDlcmiAddressLen_Type.__name__ = "Integer32"
_UsdFrDlcmiAddressLen_Object = MibTableColumn
usdFrDlcmiAddressLen = _UsdFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 4),
    _UsdFrDlcmiAddressLen_Type()
)
usdFrDlcmiAddressLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiAddressLen.setStatus("current")


class _UsdFrDlcmiPollingInterval_Type(Integer32):
    """Custom type usdFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_UsdFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_UsdFrDlcmiPollingInterval_Object = MibTableColumn
usdFrDlcmiPollingInterval = _UsdFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 5),
    _UsdFrDlcmiPollingInterval_Type()
)
usdFrDlcmiPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdFrDlcmiPollingInterval.setUnits("seconds")


class _UsdFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type usdFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_UsdFrDlcmiFullEnquiryInterval_Object = MibTableColumn
usdFrDlcmiFullEnquiryInterval = _UsdFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 6),
    _UsdFrDlcmiFullEnquiryInterval_Type()
)
usdFrDlcmiFullEnquiryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiFullEnquiryInterval.setStatus("current")


class _UsdFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type usdFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UsdFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_UsdFrDlcmiErrorThreshold_Object = MibTableColumn
usdFrDlcmiErrorThreshold = _UsdFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 7),
    _UsdFrDlcmiErrorThreshold_Type()
)
usdFrDlcmiErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiErrorThreshold.setStatus("current")


class _UsdFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type usdFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UsdFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_UsdFrDlcmiMonitoredEvents_Object = MibTableColumn
usdFrDlcmiMonitoredEvents = _UsdFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 8),
    _UsdFrDlcmiMonitoredEvents_Type()
)
usdFrDlcmiMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiMonitoredEvents.setStatus("current")
_UsdFrDlcmiMaxSupportedVCs_Type = DLCI
_UsdFrDlcmiMaxSupportedVCs_Object = MibTableColumn
usdFrDlcmiMaxSupportedVCs = _UsdFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 9),
    _UsdFrDlcmiMaxSupportedVCs_Type()
)
usdFrDlcmiMaxSupportedVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiMaxSupportedVCs.setStatus("current")


class _UsdFrDlcmiMulticast_Type(Integer32):
    """Custom type usdFrDlcmiMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 1))
    )


_UsdFrDlcmiMulticast_Type.__name__ = "Integer32"
_UsdFrDlcmiMulticast_Object = MibTableColumn
usdFrDlcmiMulticast = _UsdFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 10),
    _UsdFrDlcmiMulticast_Type()
)
usdFrDlcmiMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiMulticast.setStatus("current")


class _UsdFrDlcmiStatus_Type(Integer32):
    """Custom type usdFrDlcmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("initializing", 3),
          ("running", 1))
    )


_UsdFrDlcmiStatus_Type.__name__ = "Integer32"
_UsdFrDlcmiStatus_Object = MibTableColumn
usdFrDlcmiStatus = _UsdFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 11),
    _UsdFrDlcmiStatus_Type()
)
usdFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatus.setStatus("current")
_UsdFrDlcmiRowStatus_Type = RowStatus
_UsdFrDlcmiRowStatus_Object = MibTableColumn
usdFrDlcmiRowStatus = _UsdFrDlcmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 12),
    _UsdFrDlcmiRowStatus_Type()
)
usdFrDlcmiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiRowStatus.setStatus("current")
_UsdFrDlcmiLowerIfIndex_Type = InterfaceIndexOrZero
_UsdFrDlcmiLowerIfIndex_Object = MibTableColumn
usdFrDlcmiLowerIfIndex = _UsdFrDlcmiLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 13),
    _UsdFrDlcmiLowerIfIndex_Type()
)
usdFrDlcmiLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiLowerIfIndex.setStatus("current")


class _UsdFrDlcmiRole_Type(Integer32):
    """Custom type usdFrDlcmiRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 0),
          ("nni", 2))
    )


_UsdFrDlcmiRole_Type.__name__ = "Integer32"
_UsdFrDlcmiRole_Object = MibTableColumn
usdFrDlcmiRole = _UsdFrDlcmiRole_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 14),
    _UsdFrDlcmiRole_Type()
)
usdFrDlcmiRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiRole.setStatus("current")


class _UsdFrDlcmiDcePollingInterval_Type(Integer32):
    """Custom type usdFrDlcmiDcePollingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_UsdFrDlcmiDcePollingInterval_Type.__name__ = "Integer32"
_UsdFrDlcmiDcePollingInterval_Object = MibTableColumn
usdFrDlcmiDcePollingInterval = _UsdFrDlcmiDcePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 15),
    _UsdFrDlcmiDcePollingInterval_Type()
)
usdFrDlcmiDcePollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiDcePollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdFrDlcmiDcePollingInterval.setUnits("seconds")


class _UsdFrDlcmiDceErrorThreshold_Type(Integer32):
    """Custom type usdFrDlcmiDceErrorThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UsdFrDlcmiDceErrorThreshold_Type.__name__ = "Integer32"
_UsdFrDlcmiDceErrorThreshold_Object = MibTableColumn
usdFrDlcmiDceErrorThreshold = _UsdFrDlcmiDceErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 16),
    _UsdFrDlcmiDceErrorThreshold_Type()
)
usdFrDlcmiDceErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiDceErrorThreshold.setStatus("current")


class _UsdFrDlcmiDceMonitoredEvents_Type(Integer32):
    """Custom type usdFrDlcmiDceMonitoredEvents based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_UsdFrDlcmiDceMonitoredEvents_Type.__name__ = "Integer32"
_UsdFrDlcmiDceMonitoredEvents_Object = MibTableColumn
usdFrDlcmiDceMonitoredEvents = _UsdFrDlcmiDceMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 17),
    _UsdFrDlcmiDceMonitoredEvents_Type()
)
usdFrDlcmiDceMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrDlcmiDceMonitoredEvents.setStatus("current")
_UsdFrDlcmiStatsTable_Object = MibTable
usdFrDlcmiStatsTable = _UsdFrDlcmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdFrDlcmiStatsTable.setStatus("current")
_UsdFrDlcmiStatsEntry_Object = MibTableRow
usdFrDlcmiStatsEntry = _UsdFrDlcmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1)
)
usdFrDlcmiStatsEntry.setIndexNames(
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    usdFrDlcmiStatsEntry.setStatus("current")
_UsdFrDlcmiStatsDteEnquiries_Type = Counter32
_UsdFrDlcmiStatsDteEnquiries_Object = MibTableColumn
usdFrDlcmiStatsDteEnquiries = _UsdFrDlcmiStatsDteEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 1),
    _UsdFrDlcmiStatsDteEnquiries_Type()
)
usdFrDlcmiStatsDteEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteEnquiries.setStatus("current")
_UsdFrDlcmiStatsDteFullEnquiries_Type = Counter32
_UsdFrDlcmiStatsDteFullEnquiries_Object = MibTableColumn
usdFrDlcmiStatsDteFullEnquiries = _UsdFrDlcmiStatsDteFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 2),
    _UsdFrDlcmiStatsDteFullEnquiries_Type()
)
usdFrDlcmiStatsDteFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteFullEnquiries.setStatus("current")
_UsdFrDlcmiStatsDteEnquiryResponses_Type = Counter32
_UsdFrDlcmiStatsDteEnquiryResponses_Object = MibTableColumn
usdFrDlcmiStatsDteEnquiryResponses = _UsdFrDlcmiStatsDteEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 3),
    _UsdFrDlcmiStatsDteEnquiryResponses_Type()
)
usdFrDlcmiStatsDteEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteEnquiryResponses.setStatus("current")
_UsdFrDlcmiStatsDteFullEnquiryResponses_Type = Counter32
_UsdFrDlcmiStatsDteFullEnquiryResponses_Object = MibTableColumn
usdFrDlcmiStatsDteFullEnquiryResponses = _UsdFrDlcmiStatsDteFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 4),
    _UsdFrDlcmiStatsDteFullEnquiryResponses_Type()
)
usdFrDlcmiStatsDteFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteFullEnquiryResponses.setStatus("current")
_UsdFrDlcmiStatsDteAsyncUpdates_Type = Counter32
_UsdFrDlcmiStatsDteAsyncUpdates_Object = MibTableColumn
usdFrDlcmiStatsDteAsyncUpdates = _UsdFrDlcmiStatsDteAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 5),
    _UsdFrDlcmiStatsDteAsyncUpdates_Type()
)
usdFrDlcmiStatsDteAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteAsyncUpdates.setStatus("current")
_UsdFrDlcmiStatsDteUnknownRxMessages_Type = Counter32
_UsdFrDlcmiStatsDteUnknownRxMessages_Object = MibTableColumn
usdFrDlcmiStatsDteUnknownRxMessages = _UsdFrDlcmiStatsDteUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 6),
    _UsdFrDlcmiStatsDteUnknownRxMessages_Type()
)
usdFrDlcmiStatsDteUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteUnknownRxMessages.setStatus("current")
_UsdFrDlcmiStatsDteLossOfSequences_Type = Counter32
_UsdFrDlcmiStatsDteLossOfSequences_Object = MibTableColumn
usdFrDlcmiStatsDteLossOfSequences = _UsdFrDlcmiStatsDteLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 7),
    _UsdFrDlcmiStatsDteLossOfSequences_Type()
)
usdFrDlcmiStatsDteLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteLossOfSequences.setStatus("current")
_UsdFrDlcmiStatsDteNoResponseTimeouts_Type = Counter32
_UsdFrDlcmiStatsDteNoResponseTimeouts_Object = MibTableColumn
usdFrDlcmiStatsDteNoResponseTimeouts = _UsdFrDlcmiStatsDteNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 8),
    _UsdFrDlcmiStatsDteNoResponseTimeouts_Type()
)
usdFrDlcmiStatsDteNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDteNoResponseTimeouts.setStatus("current")
_UsdFrDlcmiStatsDceEnquiries_Type = Counter32
_UsdFrDlcmiStatsDceEnquiries_Object = MibTableColumn
usdFrDlcmiStatsDceEnquiries = _UsdFrDlcmiStatsDceEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 9),
    _UsdFrDlcmiStatsDceEnquiries_Type()
)
usdFrDlcmiStatsDceEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceEnquiries.setStatus("current")
_UsdFrDlcmiStatsDceFullEnquiries_Type = Counter32
_UsdFrDlcmiStatsDceFullEnquiries_Object = MibTableColumn
usdFrDlcmiStatsDceFullEnquiries = _UsdFrDlcmiStatsDceFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 10),
    _UsdFrDlcmiStatsDceFullEnquiries_Type()
)
usdFrDlcmiStatsDceFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceFullEnquiries.setStatus("current")
_UsdFrDlcmiStatsDceEnquiryResponses_Type = Counter32
_UsdFrDlcmiStatsDceEnquiryResponses_Object = MibTableColumn
usdFrDlcmiStatsDceEnquiryResponses = _UsdFrDlcmiStatsDceEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 11),
    _UsdFrDlcmiStatsDceEnquiryResponses_Type()
)
usdFrDlcmiStatsDceEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceEnquiryResponses.setStatus("current")
_UsdFrDlcmiStatsDceFullEnquiryResponses_Type = Counter32
_UsdFrDlcmiStatsDceFullEnquiryResponses_Object = MibTableColumn
usdFrDlcmiStatsDceFullEnquiryResponses = _UsdFrDlcmiStatsDceFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 12),
    _UsdFrDlcmiStatsDceFullEnquiryResponses_Type()
)
usdFrDlcmiStatsDceFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceFullEnquiryResponses.setStatus("current")
_UsdFrDlcmiStatsDceAsyncUpdates_Type = Counter32
_UsdFrDlcmiStatsDceAsyncUpdates_Object = MibTableColumn
usdFrDlcmiStatsDceAsyncUpdates = _UsdFrDlcmiStatsDceAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 13),
    _UsdFrDlcmiStatsDceAsyncUpdates_Type()
)
usdFrDlcmiStatsDceAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceAsyncUpdates.setStatus("current")
_UsdFrDlcmiStatsDceUnknownRxMessages_Type = Counter32
_UsdFrDlcmiStatsDceUnknownRxMessages_Object = MibTableColumn
usdFrDlcmiStatsDceUnknownRxMessages = _UsdFrDlcmiStatsDceUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 14),
    _UsdFrDlcmiStatsDceUnknownRxMessages_Type()
)
usdFrDlcmiStatsDceUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceUnknownRxMessages.setStatus("current")
_UsdFrDlcmiStatsDceLossOfSequences_Type = Counter32
_UsdFrDlcmiStatsDceLossOfSequences_Object = MibTableColumn
usdFrDlcmiStatsDceLossOfSequences = _UsdFrDlcmiStatsDceLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 15),
    _UsdFrDlcmiStatsDceLossOfSequences_Type()
)
usdFrDlcmiStatsDceLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceLossOfSequences.setStatus("current")
_UsdFrDlcmiStatsDceNoResponseTimeouts_Type = Counter32
_UsdFrDlcmiStatsDceNoResponseTimeouts_Object = MibTableColumn
usdFrDlcmiStatsDceNoResponseTimeouts = _UsdFrDlcmiStatsDceNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 16),
    _UsdFrDlcmiStatsDceNoResponseTimeouts_Type()
)
usdFrDlcmiStatsDceNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDceNoResponseTimeouts.setStatus("current")
_UsdFrDlcmiStatsDiscontinuityTime_Type = TimeTicks
_UsdFrDlcmiStatsDiscontinuityTime_Object = MibTableColumn
usdFrDlcmiStatsDiscontinuityTime = _UsdFrDlcmiStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 17),
    _UsdFrDlcmiStatsDiscontinuityTime_Type()
)
usdFrDlcmiStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrDlcmiStatsDiscontinuityTime.setStatus("current")
_UsdFrCircuitTable_Object = MibTable
usdFrCircuitTable = _UsdFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdFrCircuitTable.setStatus("current")
_UsdFrCircuitEntry_Object = MibTableRow
usdFrCircuitEntry = _UsdFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1)
)
usdFrCircuitEntry.setIndexNames(
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitIfIndex"),
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    usdFrCircuitEntry.setStatus("current")
_UsdFrCircuitIfIndex_Type = InterfaceIndex
_UsdFrCircuitIfIndex_Object = MibTableColumn
usdFrCircuitIfIndex = _UsdFrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 1),
    _UsdFrCircuitIfIndex_Type()
)
usdFrCircuitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdFrCircuitIfIndex.setStatus("current")
_UsdFrCircuitDlci_Type = DLCI
_UsdFrCircuitDlci_Object = MibTableColumn
usdFrCircuitDlci = _UsdFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 2),
    _UsdFrCircuitDlci_Type()
)
usdFrCircuitDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdFrCircuitDlci.setStatus("current")


class _UsdFrCircuitState_Type(Integer32):
    """Custom type usdFrCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_UsdFrCircuitState_Type.__name__ = "Integer32"
_UsdFrCircuitState_Object = MibTableColumn
usdFrCircuitState = _UsdFrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 3),
    _UsdFrCircuitState_Type()
)
usdFrCircuitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitState.setStatus("current")
_UsdFrCircuitReceivedFECNs_Type = Counter32
_UsdFrCircuitReceivedFECNs_Object = MibTableColumn
usdFrCircuitReceivedFECNs = _UsdFrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 4),
    _UsdFrCircuitReceivedFECNs_Type()
)
usdFrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitReceivedFECNs.setStatus("current")
_UsdFrCircuitReceivedBECNs_Type = Counter32
_UsdFrCircuitReceivedBECNs_Object = MibTableColumn
usdFrCircuitReceivedBECNs = _UsdFrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 5),
    _UsdFrCircuitReceivedBECNs_Type()
)
usdFrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitReceivedBECNs.setStatus("current")
_UsdFrCircuitSentFrames_Type = Counter32
_UsdFrCircuitSentFrames_Object = MibTableColumn
usdFrCircuitSentFrames = _UsdFrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 6),
    _UsdFrCircuitSentFrames_Type()
)
usdFrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitSentFrames.setStatus("current")
_UsdFrCircuitSentOctets_Type = Counter32
_UsdFrCircuitSentOctets_Object = MibTableColumn
usdFrCircuitSentOctets = _UsdFrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 7),
    _UsdFrCircuitSentOctets_Type()
)
usdFrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitSentOctets.setStatus("current")
_UsdFrCircuitReceivedFrames_Type = Counter32
_UsdFrCircuitReceivedFrames_Object = MibTableColumn
usdFrCircuitReceivedFrames = _UsdFrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 8),
    _UsdFrCircuitReceivedFrames_Type()
)
usdFrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitReceivedFrames.setStatus("current")
_UsdFrCircuitReceivedOctets_Type = Counter32
_UsdFrCircuitReceivedOctets_Object = MibTableColumn
usdFrCircuitReceivedOctets = _UsdFrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 9),
    _UsdFrCircuitReceivedOctets_Type()
)
usdFrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitReceivedOctets.setStatus("current")
_UsdFrCircuitCreationTime_Type = TimeStamp
_UsdFrCircuitCreationTime_Object = MibTableColumn
usdFrCircuitCreationTime = _UsdFrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 10),
    _UsdFrCircuitCreationTime_Type()
)
usdFrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitCreationTime.setStatus("current")
_UsdFrCircuitLastTimeChange_Type = TimeStamp
_UsdFrCircuitLastTimeChange_Object = MibTableColumn
usdFrCircuitLastTimeChange = _UsdFrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 11),
    _UsdFrCircuitLastTimeChange_Type()
)
usdFrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitLastTimeChange.setStatus("current")


class _UsdFrCircuitCommittedBurst_Type(Integer32):
    """Custom type usdFrCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdFrCircuitCommittedBurst_Type.__name__ = "Integer32"
_UsdFrCircuitCommittedBurst_Object = MibTableColumn
usdFrCircuitCommittedBurst = _UsdFrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 12),
    _UsdFrCircuitCommittedBurst_Type()
)
usdFrCircuitCommittedBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitCommittedBurst.setStatus("current")


class _UsdFrCircuitExcessBurst_Type(Integer32):
    """Custom type usdFrCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdFrCircuitExcessBurst_Type.__name__ = "Integer32"
_UsdFrCircuitExcessBurst_Object = MibTableColumn
usdFrCircuitExcessBurst = _UsdFrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 13),
    _UsdFrCircuitExcessBurst_Type()
)
usdFrCircuitExcessBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitExcessBurst.setStatus("current")


class _UsdFrCircuitThroughput_Type(Integer32):
    """Custom type usdFrCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdFrCircuitThroughput_Type.__name__ = "Integer32"
_UsdFrCircuitThroughput_Object = MibTableColumn
usdFrCircuitThroughput = _UsdFrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 14),
    _UsdFrCircuitThroughput_Type()
)
usdFrCircuitThroughput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitThroughput.setStatus("current")


class _UsdFrCircuitMulticast_Type(Integer32):
    """Custom type usdFrCircuitMulticast based on Integer32"""
    defaultValue = 1

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
        *(("nWay", 4),
          ("oneWay", 2),
          ("twoWay", 3),
          ("unicast", 1))
    )


_UsdFrCircuitMulticast_Type.__name__ = "Integer32"
_UsdFrCircuitMulticast_Object = MibTableColumn
usdFrCircuitMulticast = _UsdFrCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 15),
    _UsdFrCircuitMulticast_Type()
)
usdFrCircuitMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitMulticast.setStatus("current")


class _UsdFrCircuitType_Type(Integer32):
    """Custom type usdFrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_UsdFrCircuitType_Type.__name__ = "Integer32"
_UsdFrCircuitType_Object = MibTableColumn
usdFrCircuitType = _UsdFrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 16),
    _UsdFrCircuitType_Type()
)
usdFrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitType.setStatus("current")
_UsdFrCircuitDiscards_Type = Counter32
_UsdFrCircuitDiscards_Object = MibTableColumn
usdFrCircuitDiscards = _UsdFrCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 17),
    _UsdFrCircuitDiscards_Type()
)
usdFrCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitDiscards.setStatus("current")
_UsdFrCircuitReceivedDEs_Type = Counter32
_UsdFrCircuitReceivedDEs_Object = MibTableColumn
usdFrCircuitReceivedDEs = _UsdFrCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 18),
    _UsdFrCircuitReceivedDEs_Type()
)
usdFrCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitReceivedDEs.setStatus("current")
_UsdFrCircuitSentDEs_Type = Counter32
_UsdFrCircuitSentDEs_Object = MibTableColumn
usdFrCircuitSentDEs = _UsdFrCircuitSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 19),
    _UsdFrCircuitSentDEs_Type()
)
usdFrCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitSentDEs.setStatus("current")
_UsdFrCircuitLogicalIfIndex_Type = InterfaceIndex
_UsdFrCircuitLogicalIfIndex_Object = MibTableColumn
usdFrCircuitLogicalIfIndex = _UsdFrCircuitLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 20),
    _UsdFrCircuitLogicalIfIndex_Type()
)
usdFrCircuitLogicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitLogicalIfIndex.setStatus("current")
_UsdFrCircuitRowStatus_Type = RowStatus
_UsdFrCircuitRowStatus_Object = MibTableColumn
usdFrCircuitRowStatus = _UsdFrCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 21),
    _UsdFrCircuitRowStatus_Type()
)
usdFrCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrCircuitRowStatus.setStatus("current")
_UsdFrCircuitSentFECNs_Type = Counter32
_UsdFrCircuitSentFECNs_Object = MibTableColumn
usdFrCircuitSentFECNs = _UsdFrCircuitSentFECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 22),
    _UsdFrCircuitSentFECNs_Type()
)
usdFrCircuitSentFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitSentFECNs.setStatus("current")
_UsdFrCircuitSentBECNs_Type = Counter32
_UsdFrCircuitSentBECNs_Object = MibTableColumn
usdFrCircuitSentBECNs = _UsdFrCircuitSentBECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 23),
    _UsdFrCircuitSentBECNs_Type()
)
usdFrCircuitSentBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrCircuitSentBECNs.setStatus("current")
_UsdFrSubIfLayer_ObjectIdentity = ObjectIdentity
usdFrSubIfLayer = _UsdFrSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2)
)
_UsdFrSubIfNextIfIndex_Type = UsdNextIfIndex
_UsdFrSubIfNextIfIndex_Object = MibScalar
usdFrSubIfNextIfIndex = _UsdFrSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 1),
    _UsdFrSubIfNextIfIndex_Type()
)
usdFrSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdFrSubIfNextIfIndex.setStatus("current")
_UsdFrSubIfTable_Object = MibTable
usdFrSubIfTable = _UsdFrSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdFrSubIfTable.setStatus("current")
_UsdFrSubIfEntry_Object = MibTableRow
usdFrSubIfEntry = _UsdFrSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1)
)
usdFrSubIfEntry.setIndexNames(
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfIndex"),
)
if mibBuilder.loadTexts:
    usdFrSubIfEntry.setStatus("current")
_UsdFrSubIfIndex_Type = InterfaceIndex
_UsdFrSubIfIndex_Object = MibTableColumn
usdFrSubIfIndex = _UsdFrSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 1),
    _UsdFrSubIfIndex_Type()
)
usdFrSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdFrSubIfIndex.setStatus("current")
_UsdFrSubIfRowStatus_Type = RowStatus
_UsdFrSubIfRowStatus_Object = MibTableColumn
usdFrSubIfRowStatus = _UsdFrSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 2),
    _UsdFrSubIfRowStatus_Type()
)
usdFrSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrSubIfRowStatus.setStatus("current")
_UsdFrSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdFrSubIfLowerIfIndex_Object = MibTableColumn
usdFrSubIfLowerIfIndex = _UsdFrSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 3),
    _UsdFrSubIfLowerIfIndex_Type()
)
usdFrSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrSubIfLowerIfIndex.setStatus("current")


class _UsdFrSubIfId_Type(Integer32):
    """Custom type usdFrSubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UsdFrSubIfId_Type.__name__ = "Integer32"
_UsdFrSubIfId_Object = MibTableColumn
usdFrSubIfId = _UsdFrSubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 4),
    _UsdFrSubIfId_Type()
)
usdFrSubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrSubIfId.setStatus("current")
_UsdFrSubIfCktTable_Object = MibTable
usdFrSubIfCktTable = _UsdFrSubIfCktTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    usdFrSubIfCktTable.setStatus("current")
_UsdFrSubIfCktEntry_Object = MibTableRow
usdFrSubIfCktEntry = _UsdFrSubIfCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1)
)
usdFrSubIfCktEntry.setIndexNames(
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfIndex"),
    (0, "Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfCktDlci"),
)
if mibBuilder.loadTexts:
    usdFrSubIfCktEntry.setStatus("current")
_UsdFrSubIfCktDlci_Type = DLCI
_UsdFrSubIfCktDlci_Object = MibTableColumn
usdFrSubIfCktDlci = _UsdFrSubIfCktDlci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1, 1),
    _UsdFrSubIfCktDlci_Type()
)
usdFrSubIfCktDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdFrSubIfCktDlci.setStatus("current")
_UsdFrSubIfCktRowStatus_Type = RowStatus
_UsdFrSubIfCktRowStatus_Object = MibTableColumn
usdFrSubIfCktRowStatus = _UsdFrSubIfCktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1, 2),
    _UsdFrSubIfCktRowStatus_Type()
)
usdFrSubIfCktRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFrSubIfCktRowStatus.setStatus("current")
_UsdFrConformance_ObjectIdentity = ObjectIdentity
usdFrConformance = _UsdFrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4)
)
_UsdFrCompliances_ObjectIdentity = ObjectIdentity
usdFrCompliances = _UsdFrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 1)
)
_UsdFrGroups_ObjectIdentity = ObjectIdentity
usdFrGroups = _UsdFrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2)
)

# Managed Objects groups

usdFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 1)
)
usdFrGroup.setObjects(
      *(("Unisphere-Data-FRAME-RELAY-MIB", "usdFrNextIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiState"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiAddress"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiAddressLen"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiPollingInterval"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiFullEnquiryInterval"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiErrorThreshold"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiMonitoredEvents"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiMaxSupportedVCs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiMulticast"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatus"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiRowStatus"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiLowerIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiRole"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiDcePollingInterval"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiDceErrorThreshold"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiDceMonitoredEvents"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteEnquiries"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteFullEnquiries"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteEnquiryResponses"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteFullEnquiryResponses"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteAsyncUpdates"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteUnknownRxMessages"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteLossOfSequences"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDteNoResponseTimeouts"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceEnquiries"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceFullEnquiries"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceEnquiryResponses"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceFullEnquiryResponses"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceAsyncUpdates"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceUnknownRxMessages"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceLossOfSequences"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDceNoResponseTimeouts"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrDlcmiStatsDiscontinuityTime"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitState"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitReceivedFECNs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitReceivedBECNs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitSentFrames"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitSentOctets"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitReceivedFrames"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitReceivedOctets"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitCreationTime"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitLastTimeChange"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitCommittedBurst"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitExcessBurst"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitThroughput"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitMulticast"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitType"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitDiscards"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitReceivedDEs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitSentDEs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitLogicalIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitRowStatus"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitSentFECNs"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrCircuitSentBECNs"))
)
if mibBuilder.loadTexts:
    usdFrGroup.setStatus("current")

usdFrSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 2)
)
usdFrSubIfGroup.setObjects(
      *(("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfNextIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfRowStatus"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfLowerIfIndex"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfId"),
        ("Unisphere-Data-FRAME-RELAY-MIB", "usdFrSubIfCktRowStatus"))
)
if mibBuilder.loadTexts:
    usdFrSubIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdFrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdFrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-FRAME-RELAY-MIB",
    **{"usdFrameRelayMIB": usdFrameRelayMIB,
       "usdFrObjects": usdFrObjects,
       "usdFrIfLayer": usdFrIfLayer,
       "usdFrNextIfIndex": usdFrNextIfIndex,
       "usdFrDlcmiTable": usdFrDlcmiTable,
       "usdFrDlcmiEntry": usdFrDlcmiEntry,
       "usdFrDlcmiIfIndex": usdFrDlcmiIfIndex,
       "usdFrDlcmiState": usdFrDlcmiState,
       "usdFrDlcmiAddress": usdFrDlcmiAddress,
       "usdFrDlcmiAddressLen": usdFrDlcmiAddressLen,
       "usdFrDlcmiPollingInterval": usdFrDlcmiPollingInterval,
       "usdFrDlcmiFullEnquiryInterval": usdFrDlcmiFullEnquiryInterval,
       "usdFrDlcmiErrorThreshold": usdFrDlcmiErrorThreshold,
       "usdFrDlcmiMonitoredEvents": usdFrDlcmiMonitoredEvents,
       "usdFrDlcmiMaxSupportedVCs": usdFrDlcmiMaxSupportedVCs,
       "usdFrDlcmiMulticast": usdFrDlcmiMulticast,
       "usdFrDlcmiStatus": usdFrDlcmiStatus,
       "usdFrDlcmiRowStatus": usdFrDlcmiRowStatus,
       "usdFrDlcmiLowerIfIndex": usdFrDlcmiLowerIfIndex,
       "usdFrDlcmiRole": usdFrDlcmiRole,
       "usdFrDlcmiDcePollingInterval": usdFrDlcmiDcePollingInterval,
       "usdFrDlcmiDceErrorThreshold": usdFrDlcmiDceErrorThreshold,
       "usdFrDlcmiDceMonitoredEvents": usdFrDlcmiDceMonitoredEvents,
       "usdFrDlcmiStatsTable": usdFrDlcmiStatsTable,
       "usdFrDlcmiStatsEntry": usdFrDlcmiStatsEntry,
       "usdFrDlcmiStatsDteEnquiries": usdFrDlcmiStatsDteEnquiries,
       "usdFrDlcmiStatsDteFullEnquiries": usdFrDlcmiStatsDteFullEnquiries,
       "usdFrDlcmiStatsDteEnquiryResponses": usdFrDlcmiStatsDteEnquiryResponses,
       "usdFrDlcmiStatsDteFullEnquiryResponses": usdFrDlcmiStatsDteFullEnquiryResponses,
       "usdFrDlcmiStatsDteAsyncUpdates": usdFrDlcmiStatsDteAsyncUpdates,
       "usdFrDlcmiStatsDteUnknownRxMessages": usdFrDlcmiStatsDteUnknownRxMessages,
       "usdFrDlcmiStatsDteLossOfSequences": usdFrDlcmiStatsDteLossOfSequences,
       "usdFrDlcmiStatsDteNoResponseTimeouts": usdFrDlcmiStatsDteNoResponseTimeouts,
       "usdFrDlcmiStatsDceEnquiries": usdFrDlcmiStatsDceEnquiries,
       "usdFrDlcmiStatsDceFullEnquiries": usdFrDlcmiStatsDceFullEnquiries,
       "usdFrDlcmiStatsDceEnquiryResponses": usdFrDlcmiStatsDceEnquiryResponses,
       "usdFrDlcmiStatsDceFullEnquiryResponses": usdFrDlcmiStatsDceFullEnquiryResponses,
       "usdFrDlcmiStatsDceAsyncUpdates": usdFrDlcmiStatsDceAsyncUpdates,
       "usdFrDlcmiStatsDceUnknownRxMessages": usdFrDlcmiStatsDceUnknownRxMessages,
       "usdFrDlcmiStatsDceLossOfSequences": usdFrDlcmiStatsDceLossOfSequences,
       "usdFrDlcmiStatsDceNoResponseTimeouts": usdFrDlcmiStatsDceNoResponseTimeouts,
       "usdFrDlcmiStatsDiscontinuityTime": usdFrDlcmiStatsDiscontinuityTime,
       "usdFrCircuitTable": usdFrCircuitTable,
       "usdFrCircuitEntry": usdFrCircuitEntry,
       "usdFrCircuitIfIndex": usdFrCircuitIfIndex,
       "usdFrCircuitDlci": usdFrCircuitDlci,
       "usdFrCircuitState": usdFrCircuitState,
       "usdFrCircuitReceivedFECNs": usdFrCircuitReceivedFECNs,
       "usdFrCircuitReceivedBECNs": usdFrCircuitReceivedBECNs,
       "usdFrCircuitSentFrames": usdFrCircuitSentFrames,
       "usdFrCircuitSentOctets": usdFrCircuitSentOctets,
       "usdFrCircuitReceivedFrames": usdFrCircuitReceivedFrames,
       "usdFrCircuitReceivedOctets": usdFrCircuitReceivedOctets,
       "usdFrCircuitCreationTime": usdFrCircuitCreationTime,
       "usdFrCircuitLastTimeChange": usdFrCircuitLastTimeChange,
       "usdFrCircuitCommittedBurst": usdFrCircuitCommittedBurst,
       "usdFrCircuitExcessBurst": usdFrCircuitExcessBurst,
       "usdFrCircuitThroughput": usdFrCircuitThroughput,
       "usdFrCircuitMulticast": usdFrCircuitMulticast,
       "usdFrCircuitType": usdFrCircuitType,
       "usdFrCircuitDiscards": usdFrCircuitDiscards,
       "usdFrCircuitReceivedDEs": usdFrCircuitReceivedDEs,
       "usdFrCircuitSentDEs": usdFrCircuitSentDEs,
       "usdFrCircuitLogicalIfIndex": usdFrCircuitLogicalIfIndex,
       "usdFrCircuitRowStatus": usdFrCircuitRowStatus,
       "usdFrCircuitSentFECNs": usdFrCircuitSentFECNs,
       "usdFrCircuitSentBECNs": usdFrCircuitSentBECNs,
       "usdFrSubIfLayer": usdFrSubIfLayer,
       "usdFrSubIfNextIfIndex": usdFrSubIfNextIfIndex,
       "usdFrSubIfTable": usdFrSubIfTable,
       "usdFrSubIfEntry": usdFrSubIfEntry,
       "usdFrSubIfIndex": usdFrSubIfIndex,
       "usdFrSubIfRowStatus": usdFrSubIfRowStatus,
       "usdFrSubIfLowerIfIndex": usdFrSubIfLowerIfIndex,
       "usdFrSubIfId": usdFrSubIfId,
       "usdFrSubIfCktTable": usdFrSubIfCktTable,
       "usdFrSubIfCktEntry": usdFrSubIfCktEntry,
       "usdFrSubIfCktDlci": usdFrSubIfCktDlci,
       "usdFrSubIfCktRowStatus": usdFrSubIfCktRowStatus,
       "usdFrConformance": usdFrConformance,
       "usdFrCompliances": usdFrCompliances,
       "usdFrCompliance": usdFrCompliance,
       "usdFrGroups": usdFrGroups,
       "usdFrGroup": usdFrGroup,
       "usdFrSubIfGroup": usdFrSubIfGroup}
)
