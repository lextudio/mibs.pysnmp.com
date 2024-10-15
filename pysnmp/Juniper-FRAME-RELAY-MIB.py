# SNMP MIB module (Juniper-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:18 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniNextIfIndex,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10)
)
juniFrameRelayMIB.setRevisions(
        ("2002-12-13 14:35",
         "2000-09-26 17:30",
         "1999-06-01 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniFrMlFrBundleName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_JuniFrObjects_ObjectIdentity = ObjectIdentity
juniFrObjects = _JuniFrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1)
)
_JuniFrIfLayer_ObjectIdentity = ObjectIdentity
juniFrIfLayer = _JuniFrIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1)
)
_JuniFrNextIfIndex_Type = JuniNextIfIndex
_JuniFrNextIfIndex_Object = MibScalar
juniFrNextIfIndex = _JuniFrNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 1),
    _JuniFrNextIfIndex_Type()
)
juniFrNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrNextIfIndex.setStatus("current")
_JuniFrDlcmiTable_Object = MibTable
juniFrDlcmiTable = _JuniFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniFrDlcmiTable.setStatus("current")
_JuniFrDlcmiEntry_Object = MibTableRow
juniFrDlcmiEntry = _JuniFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1)
)
juniFrDlcmiEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrDlcmiEntry.setStatus("current")
_JuniFrDlcmiIfIndex_Type = InterfaceIndex
_JuniFrDlcmiIfIndex_Object = MibTableColumn
juniFrDlcmiIfIndex = _JuniFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 1),
    _JuniFrDlcmiIfIndex_Type()
)
juniFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiIfIndex.setStatus("current")


class _JuniFrDlcmiState_Type(Integer32):
    """Custom type juniFrDlcmiState based on Integer32"""
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


_JuniFrDlcmiState_Type.__name__ = "Integer32"
_JuniFrDlcmiState_Object = MibTableColumn
juniFrDlcmiState = _JuniFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 2),
    _JuniFrDlcmiState_Type()
)
juniFrDlcmiState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiState.setStatus("current")


class _JuniFrDlcmiAddress_Type(Integer32):
    """Custom type juniFrDlcmiAddress based on Integer32"""
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


_JuniFrDlcmiAddress_Type.__name__ = "Integer32"
_JuniFrDlcmiAddress_Object = MibTableColumn
juniFrDlcmiAddress = _JuniFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 3),
    _JuniFrDlcmiAddress_Type()
)
juniFrDlcmiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiAddress.setStatus("current")


class _JuniFrDlcmiAddressLen_Type(Integer32):
    """Custom type juniFrDlcmiAddressLen based on Integer32"""
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


_JuniFrDlcmiAddressLen_Type.__name__ = "Integer32"
_JuniFrDlcmiAddressLen_Object = MibTableColumn
juniFrDlcmiAddressLen = _JuniFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 4),
    _JuniFrDlcmiAddressLen_Type()
)
juniFrDlcmiAddressLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiAddressLen.setStatus("current")


class _JuniFrDlcmiPollingInterval_Type(Integer32):
    """Custom type juniFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_JuniFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_JuniFrDlcmiPollingInterval_Object = MibTableColumn
juniFrDlcmiPollingInterval = _JuniFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 5),
    _JuniFrDlcmiPollingInterval_Type()
)
juniFrDlcmiPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniFrDlcmiPollingInterval.setUnits("seconds")


class _JuniFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type juniFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_JuniFrDlcmiFullEnquiryInterval_Object = MibTableColumn
juniFrDlcmiFullEnquiryInterval = _JuniFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 6),
    _JuniFrDlcmiFullEnquiryInterval_Type()
)
juniFrDlcmiFullEnquiryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiFullEnquiryInterval.setStatus("current")


class _JuniFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type juniFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JuniFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_JuniFrDlcmiErrorThreshold_Object = MibTableColumn
juniFrDlcmiErrorThreshold = _JuniFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 7),
    _JuniFrDlcmiErrorThreshold_Type()
)
juniFrDlcmiErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiErrorThreshold.setStatus("current")


class _JuniFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type juniFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JuniFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_JuniFrDlcmiMonitoredEvents_Object = MibTableColumn
juniFrDlcmiMonitoredEvents = _JuniFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 8),
    _JuniFrDlcmiMonitoredEvents_Type()
)
juniFrDlcmiMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiMonitoredEvents.setStatus("current")
_JuniFrDlcmiMaxSupportedVCs_Type = DLCI
_JuniFrDlcmiMaxSupportedVCs_Object = MibTableColumn
juniFrDlcmiMaxSupportedVCs = _JuniFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 9),
    _JuniFrDlcmiMaxSupportedVCs_Type()
)
juniFrDlcmiMaxSupportedVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiMaxSupportedVCs.setStatus("current")


class _JuniFrDlcmiMulticast_Type(Integer32):
    """Custom type juniFrDlcmiMulticast based on Integer32"""
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


_JuniFrDlcmiMulticast_Type.__name__ = "Integer32"
_JuniFrDlcmiMulticast_Object = MibTableColumn
juniFrDlcmiMulticast = _JuniFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 10),
    _JuniFrDlcmiMulticast_Type()
)
juniFrDlcmiMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiMulticast.setStatus("current")


class _JuniFrDlcmiStatus_Type(Integer32):
    """Custom type juniFrDlcmiStatus based on Integer32"""
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


_JuniFrDlcmiStatus_Type.__name__ = "Integer32"
_JuniFrDlcmiStatus_Object = MibTableColumn
juniFrDlcmiStatus = _JuniFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 11),
    _JuniFrDlcmiStatus_Type()
)
juniFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatus.setStatus("current")
_JuniFrDlcmiRowStatus_Type = RowStatus
_JuniFrDlcmiRowStatus_Object = MibTableColumn
juniFrDlcmiRowStatus = _JuniFrDlcmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 12),
    _JuniFrDlcmiRowStatus_Type()
)
juniFrDlcmiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiRowStatus.setStatus("current")
_JuniFrDlcmiLowerIfIndex_Type = InterfaceIndexOrZero
_JuniFrDlcmiLowerIfIndex_Object = MibTableColumn
juniFrDlcmiLowerIfIndex = _JuniFrDlcmiLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 13),
    _JuniFrDlcmiLowerIfIndex_Type()
)
juniFrDlcmiLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiLowerIfIndex.setStatus("current")


class _JuniFrDlcmiRole_Type(Integer32):
    """Custom type juniFrDlcmiRole based on Integer32"""
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


_JuniFrDlcmiRole_Type.__name__ = "Integer32"
_JuniFrDlcmiRole_Object = MibTableColumn
juniFrDlcmiRole = _JuniFrDlcmiRole_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 14),
    _JuniFrDlcmiRole_Type()
)
juniFrDlcmiRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiRole.setStatus("current")


class _JuniFrDlcmiDcePollingInterval_Type(Integer32):
    """Custom type juniFrDlcmiDcePollingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_JuniFrDlcmiDcePollingInterval_Type.__name__ = "Integer32"
_JuniFrDlcmiDcePollingInterval_Object = MibTableColumn
juniFrDlcmiDcePollingInterval = _JuniFrDlcmiDcePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 15),
    _JuniFrDlcmiDcePollingInterval_Type()
)
juniFrDlcmiDcePollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiDcePollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniFrDlcmiDcePollingInterval.setUnits("seconds")


class _JuniFrDlcmiDceErrorThreshold_Type(Integer32):
    """Custom type juniFrDlcmiDceErrorThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JuniFrDlcmiDceErrorThreshold_Type.__name__ = "Integer32"
_JuniFrDlcmiDceErrorThreshold_Object = MibTableColumn
juniFrDlcmiDceErrorThreshold = _JuniFrDlcmiDceErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 16),
    _JuniFrDlcmiDceErrorThreshold_Type()
)
juniFrDlcmiDceErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiDceErrorThreshold.setStatus("current")


class _JuniFrDlcmiDceMonitoredEvents_Type(Integer32):
    """Custom type juniFrDlcmiDceMonitoredEvents based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_JuniFrDlcmiDceMonitoredEvents_Type.__name__ = "Integer32"
_JuniFrDlcmiDceMonitoredEvents_Object = MibTableColumn
juniFrDlcmiDceMonitoredEvents = _JuniFrDlcmiDceMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 17),
    _JuniFrDlcmiDceMonitoredEvents_Type()
)
juniFrDlcmiDceMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiDceMonitoredEvents.setStatus("current")
_JuniFrDlcmiMultilinkFrBundleName_Type = JuniFrMlFrBundleName
_JuniFrDlcmiMultilinkFrBundleName_Object = MibTableColumn
juniFrDlcmiMultilinkFrBundleName = _JuniFrDlcmiMultilinkFrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 2, 1, 18),
    _JuniFrDlcmiMultilinkFrBundleName_Type()
)
juniFrDlcmiMultilinkFrBundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrDlcmiMultilinkFrBundleName.setStatus("current")
_JuniFrDlcmiStatsTable_Object = MibTable
juniFrDlcmiStatsTable = _JuniFrDlcmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniFrDlcmiStatsTable.setStatus("current")
_JuniFrDlcmiStatsEntry_Object = MibTableRow
juniFrDlcmiStatsEntry = _JuniFrDlcmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1)
)
juniFrDlcmiStatsEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrDlcmiStatsEntry.setStatus("current")
_JuniFrDlcmiStatsDteEnquiries_Type = Counter32
_JuniFrDlcmiStatsDteEnquiries_Object = MibTableColumn
juniFrDlcmiStatsDteEnquiries = _JuniFrDlcmiStatsDteEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 1),
    _JuniFrDlcmiStatsDteEnquiries_Type()
)
juniFrDlcmiStatsDteEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteEnquiries.setStatus("current")
_JuniFrDlcmiStatsDteFullEnquiries_Type = Counter32
_JuniFrDlcmiStatsDteFullEnquiries_Object = MibTableColumn
juniFrDlcmiStatsDteFullEnquiries = _JuniFrDlcmiStatsDteFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 2),
    _JuniFrDlcmiStatsDteFullEnquiries_Type()
)
juniFrDlcmiStatsDteFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteFullEnquiries.setStatus("current")
_JuniFrDlcmiStatsDteEnquiryResponses_Type = Counter32
_JuniFrDlcmiStatsDteEnquiryResponses_Object = MibTableColumn
juniFrDlcmiStatsDteEnquiryResponses = _JuniFrDlcmiStatsDteEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 3),
    _JuniFrDlcmiStatsDteEnquiryResponses_Type()
)
juniFrDlcmiStatsDteEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteEnquiryResponses.setStatus("current")
_JuniFrDlcmiStatsDteFullEnquiryResponses_Type = Counter32
_JuniFrDlcmiStatsDteFullEnquiryResponses_Object = MibTableColumn
juniFrDlcmiStatsDteFullEnquiryResponses = _JuniFrDlcmiStatsDteFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 4),
    _JuniFrDlcmiStatsDteFullEnquiryResponses_Type()
)
juniFrDlcmiStatsDteFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteFullEnquiryResponses.setStatus("current")
_JuniFrDlcmiStatsDteAsyncUpdates_Type = Counter32
_JuniFrDlcmiStatsDteAsyncUpdates_Object = MibTableColumn
juniFrDlcmiStatsDteAsyncUpdates = _JuniFrDlcmiStatsDteAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 5),
    _JuniFrDlcmiStatsDteAsyncUpdates_Type()
)
juniFrDlcmiStatsDteAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteAsyncUpdates.setStatus("current")
_JuniFrDlcmiStatsDteUnknownRxMessages_Type = Counter32
_JuniFrDlcmiStatsDteUnknownRxMessages_Object = MibTableColumn
juniFrDlcmiStatsDteUnknownRxMessages = _JuniFrDlcmiStatsDteUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 6),
    _JuniFrDlcmiStatsDteUnknownRxMessages_Type()
)
juniFrDlcmiStatsDteUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteUnknownRxMessages.setStatus("current")
_JuniFrDlcmiStatsDteLossOfSequences_Type = Counter32
_JuniFrDlcmiStatsDteLossOfSequences_Object = MibTableColumn
juniFrDlcmiStatsDteLossOfSequences = _JuniFrDlcmiStatsDteLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 7),
    _JuniFrDlcmiStatsDteLossOfSequences_Type()
)
juniFrDlcmiStatsDteLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteLossOfSequences.setStatus("current")
_JuniFrDlcmiStatsDteNoResponseTimeouts_Type = Counter32
_JuniFrDlcmiStatsDteNoResponseTimeouts_Object = MibTableColumn
juniFrDlcmiStatsDteNoResponseTimeouts = _JuniFrDlcmiStatsDteNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 8),
    _JuniFrDlcmiStatsDteNoResponseTimeouts_Type()
)
juniFrDlcmiStatsDteNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDteNoResponseTimeouts.setStatus("current")
_JuniFrDlcmiStatsDceEnquiries_Type = Counter32
_JuniFrDlcmiStatsDceEnquiries_Object = MibTableColumn
juniFrDlcmiStatsDceEnquiries = _JuniFrDlcmiStatsDceEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 9),
    _JuniFrDlcmiStatsDceEnquiries_Type()
)
juniFrDlcmiStatsDceEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceEnquiries.setStatus("current")
_JuniFrDlcmiStatsDceFullEnquiries_Type = Counter32
_JuniFrDlcmiStatsDceFullEnquiries_Object = MibTableColumn
juniFrDlcmiStatsDceFullEnquiries = _JuniFrDlcmiStatsDceFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 10),
    _JuniFrDlcmiStatsDceFullEnquiries_Type()
)
juniFrDlcmiStatsDceFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceFullEnquiries.setStatus("current")
_JuniFrDlcmiStatsDceEnquiryResponses_Type = Counter32
_JuniFrDlcmiStatsDceEnquiryResponses_Object = MibTableColumn
juniFrDlcmiStatsDceEnquiryResponses = _JuniFrDlcmiStatsDceEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 11),
    _JuniFrDlcmiStatsDceEnquiryResponses_Type()
)
juniFrDlcmiStatsDceEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceEnquiryResponses.setStatus("current")
_JuniFrDlcmiStatsDceFullEnquiryResponses_Type = Counter32
_JuniFrDlcmiStatsDceFullEnquiryResponses_Object = MibTableColumn
juniFrDlcmiStatsDceFullEnquiryResponses = _JuniFrDlcmiStatsDceFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 12),
    _JuniFrDlcmiStatsDceFullEnquiryResponses_Type()
)
juniFrDlcmiStatsDceFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceFullEnquiryResponses.setStatus("current")
_JuniFrDlcmiStatsDceAsyncUpdates_Type = Counter32
_JuniFrDlcmiStatsDceAsyncUpdates_Object = MibTableColumn
juniFrDlcmiStatsDceAsyncUpdates = _JuniFrDlcmiStatsDceAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 13),
    _JuniFrDlcmiStatsDceAsyncUpdates_Type()
)
juniFrDlcmiStatsDceAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceAsyncUpdates.setStatus("current")
_JuniFrDlcmiStatsDceUnknownRxMessages_Type = Counter32
_JuniFrDlcmiStatsDceUnknownRxMessages_Object = MibTableColumn
juniFrDlcmiStatsDceUnknownRxMessages = _JuniFrDlcmiStatsDceUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 14),
    _JuniFrDlcmiStatsDceUnknownRxMessages_Type()
)
juniFrDlcmiStatsDceUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceUnknownRxMessages.setStatus("current")
_JuniFrDlcmiStatsDceLossOfSequences_Type = Counter32
_JuniFrDlcmiStatsDceLossOfSequences_Object = MibTableColumn
juniFrDlcmiStatsDceLossOfSequences = _JuniFrDlcmiStatsDceLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 15),
    _JuniFrDlcmiStatsDceLossOfSequences_Type()
)
juniFrDlcmiStatsDceLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceLossOfSequences.setStatus("current")
_JuniFrDlcmiStatsDceNoResponseTimeouts_Type = Counter32
_JuniFrDlcmiStatsDceNoResponseTimeouts_Object = MibTableColumn
juniFrDlcmiStatsDceNoResponseTimeouts = _JuniFrDlcmiStatsDceNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 16),
    _JuniFrDlcmiStatsDceNoResponseTimeouts_Type()
)
juniFrDlcmiStatsDceNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDceNoResponseTimeouts.setStatus("current")
_JuniFrDlcmiStatsDiscontinuityTime_Type = TimeTicks
_JuniFrDlcmiStatsDiscontinuityTime_Object = MibTableColumn
juniFrDlcmiStatsDiscontinuityTime = _JuniFrDlcmiStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 3, 1, 17),
    _JuniFrDlcmiStatsDiscontinuityTime_Type()
)
juniFrDlcmiStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrDlcmiStatsDiscontinuityTime.setStatus("current")
_JuniFrCircuitTable_Object = MibTable
juniFrCircuitTable = _JuniFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniFrCircuitTable.setStatus("current")
_JuniFrCircuitEntry_Object = MibTableRow
juniFrCircuitEntry = _JuniFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1)
)
juniFrCircuitEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrCircuitIfIndex"),
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    juniFrCircuitEntry.setStatus("current")
_JuniFrCircuitIfIndex_Type = InterfaceIndex
_JuniFrCircuitIfIndex_Object = MibTableColumn
juniFrCircuitIfIndex = _JuniFrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 1),
    _JuniFrCircuitIfIndex_Type()
)
juniFrCircuitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrCircuitIfIndex.setStatus("current")
_JuniFrCircuitDlci_Type = DLCI
_JuniFrCircuitDlci_Object = MibTableColumn
juniFrCircuitDlci = _JuniFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 2),
    _JuniFrCircuitDlci_Type()
)
juniFrCircuitDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrCircuitDlci.setStatus("current")


class _JuniFrCircuitState_Type(Integer32):
    """Custom type juniFrCircuitState based on Integer32"""
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


_JuniFrCircuitState_Type.__name__ = "Integer32"
_JuniFrCircuitState_Object = MibTableColumn
juniFrCircuitState = _JuniFrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 3),
    _JuniFrCircuitState_Type()
)
juniFrCircuitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitState.setStatus("current")
_JuniFrCircuitReceivedFECNs_Type = Counter32
_JuniFrCircuitReceivedFECNs_Object = MibTableColumn
juniFrCircuitReceivedFECNs = _JuniFrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 4),
    _JuniFrCircuitReceivedFECNs_Type()
)
juniFrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitReceivedFECNs.setStatus("current")
_JuniFrCircuitReceivedBECNs_Type = Counter32
_JuniFrCircuitReceivedBECNs_Object = MibTableColumn
juniFrCircuitReceivedBECNs = _JuniFrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 5),
    _JuniFrCircuitReceivedBECNs_Type()
)
juniFrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitReceivedBECNs.setStatus("current")
_JuniFrCircuitSentFrames_Type = Counter32
_JuniFrCircuitSentFrames_Object = MibTableColumn
juniFrCircuitSentFrames = _JuniFrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 6),
    _JuniFrCircuitSentFrames_Type()
)
juniFrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitSentFrames.setStatus("current")
_JuniFrCircuitSentOctets_Type = Counter32
_JuniFrCircuitSentOctets_Object = MibTableColumn
juniFrCircuitSentOctets = _JuniFrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 7),
    _JuniFrCircuitSentOctets_Type()
)
juniFrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitSentOctets.setStatus("current")
_JuniFrCircuitReceivedFrames_Type = Counter32
_JuniFrCircuitReceivedFrames_Object = MibTableColumn
juniFrCircuitReceivedFrames = _JuniFrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 8),
    _JuniFrCircuitReceivedFrames_Type()
)
juniFrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitReceivedFrames.setStatus("current")
_JuniFrCircuitReceivedOctets_Type = Counter32
_JuniFrCircuitReceivedOctets_Object = MibTableColumn
juniFrCircuitReceivedOctets = _JuniFrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 9),
    _JuniFrCircuitReceivedOctets_Type()
)
juniFrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitReceivedOctets.setStatus("current")
_JuniFrCircuitCreationTime_Type = TimeStamp
_JuniFrCircuitCreationTime_Object = MibTableColumn
juniFrCircuitCreationTime = _JuniFrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 10),
    _JuniFrCircuitCreationTime_Type()
)
juniFrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitCreationTime.setStatus("current")
_JuniFrCircuitLastTimeChange_Type = TimeStamp
_JuniFrCircuitLastTimeChange_Object = MibTableColumn
juniFrCircuitLastTimeChange = _JuniFrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 11),
    _JuniFrCircuitLastTimeChange_Type()
)
juniFrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitLastTimeChange.setStatus("current")


class _JuniFrCircuitCommittedBurst_Type(Integer32):
    """Custom type juniFrCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniFrCircuitCommittedBurst_Type.__name__ = "Integer32"
_JuniFrCircuitCommittedBurst_Object = MibTableColumn
juniFrCircuitCommittedBurst = _JuniFrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 12),
    _JuniFrCircuitCommittedBurst_Type()
)
juniFrCircuitCommittedBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitCommittedBurst.setStatus("current")


class _JuniFrCircuitExcessBurst_Type(Integer32):
    """Custom type juniFrCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniFrCircuitExcessBurst_Type.__name__ = "Integer32"
_JuniFrCircuitExcessBurst_Object = MibTableColumn
juniFrCircuitExcessBurst = _JuniFrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 13),
    _JuniFrCircuitExcessBurst_Type()
)
juniFrCircuitExcessBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitExcessBurst.setStatus("current")


class _JuniFrCircuitThroughput_Type(Integer32):
    """Custom type juniFrCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniFrCircuitThroughput_Type.__name__ = "Integer32"
_JuniFrCircuitThroughput_Object = MibTableColumn
juniFrCircuitThroughput = _JuniFrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 14),
    _JuniFrCircuitThroughput_Type()
)
juniFrCircuitThroughput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitThroughput.setStatus("current")


class _JuniFrCircuitMulticast_Type(Integer32):
    """Custom type juniFrCircuitMulticast based on Integer32"""
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


_JuniFrCircuitMulticast_Type.__name__ = "Integer32"
_JuniFrCircuitMulticast_Object = MibTableColumn
juniFrCircuitMulticast = _JuniFrCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 15),
    _JuniFrCircuitMulticast_Type()
)
juniFrCircuitMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitMulticast.setStatus("current")


class _JuniFrCircuitType_Type(Integer32):
    """Custom type juniFrCircuitType based on Integer32"""
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


_JuniFrCircuitType_Type.__name__ = "Integer32"
_JuniFrCircuitType_Object = MibTableColumn
juniFrCircuitType = _JuniFrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 16),
    _JuniFrCircuitType_Type()
)
juniFrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitType.setStatus("current")
_JuniFrCircuitDiscards_Type = Counter32
_JuniFrCircuitDiscards_Object = MibTableColumn
juniFrCircuitDiscards = _JuniFrCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 17),
    _JuniFrCircuitDiscards_Type()
)
juniFrCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitDiscards.setStatus("current")
_JuniFrCircuitReceivedDEs_Type = Counter32
_JuniFrCircuitReceivedDEs_Object = MibTableColumn
juniFrCircuitReceivedDEs = _JuniFrCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 18),
    _JuniFrCircuitReceivedDEs_Type()
)
juniFrCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitReceivedDEs.setStatus("current")
_JuniFrCircuitSentDEs_Type = Counter32
_JuniFrCircuitSentDEs_Object = MibTableColumn
juniFrCircuitSentDEs = _JuniFrCircuitSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 19),
    _JuniFrCircuitSentDEs_Type()
)
juniFrCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitSentDEs.setStatus("current")
_JuniFrCircuitLogicalIfIndex_Type = InterfaceIndex
_JuniFrCircuitLogicalIfIndex_Object = MibTableColumn
juniFrCircuitLogicalIfIndex = _JuniFrCircuitLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 20),
    _JuniFrCircuitLogicalIfIndex_Type()
)
juniFrCircuitLogicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitLogicalIfIndex.setStatus("current")
_JuniFrCircuitRowStatus_Type = RowStatus
_JuniFrCircuitRowStatus_Object = MibTableColumn
juniFrCircuitRowStatus = _JuniFrCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 21),
    _JuniFrCircuitRowStatus_Type()
)
juniFrCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrCircuitRowStatus.setStatus("current")
_JuniFrCircuitSentFECNs_Type = Counter32
_JuniFrCircuitSentFECNs_Object = MibTableColumn
juniFrCircuitSentFECNs = _JuniFrCircuitSentFECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 22),
    _JuniFrCircuitSentFECNs_Type()
)
juniFrCircuitSentFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitSentFECNs.setStatus("current")
_JuniFrCircuitSentBECNs_Type = Counter32
_JuniFrCircuitSentBECNs_Object = MibTableColumn
juniFrCircuitSentBECNs = _JuniFrCircuitSentBECNs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 1, 4, 1, 23),
    _JuniFrCircuitSentBECNs_Type()
)
juniFrCircuitSentBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrCircuitSentBECNs.setStatus("current")
_JuniFrSubIfLayer_ObjectIdentity = ObjectIdentity
juniFrSubIfLayer = _JuniFrSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2)
)
_JuniFrSubIfNextIfIndex_Type = JuniNextIfIndex
_JuniFrSubIfNextIfIndex_Object = MibScalar
juniFrSubIfNextIfIndex = _JuniFrSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 1),
    _JuniFrSubIfNextIfIndex_Type()
)
juniFrSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrSubIfNextIfIndex.setStatus("current")
_JuniFrSubIfTable_Object = MibTable
juniFrSubIfTable = _JuniFrSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniFrSubIfTable.setStatus("current")
_JuniFrSubIfEntry_Object = MibTableRow
juniFrSubIfEntry = _JuniFrSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1)
)
juniFrSubIfEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrSubIfEntry.setStatus("current")
_JuniFrSubIfIndex_Type = InterfaceIndex
_JuniFrSubIfIndex_Object = MibTableColumn
juniFrSubIfIndex = _JuniFrSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 1),
    _JuniFrSubIfIndex_Type()
)
juniFrSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrSubIfIndex.setStatus("current")
_JuniFrSubIfRowStatus_Type = RowStatus
_JuniFrSubIfRowStatus_Object = MibTableColumn
juniFrSubIfRowStatus = _JuniFrSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 2),
    _JuniFrSubIfRowStatus_Type()
)
juniFrSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrSubIfRowStatus.setStatus("current")
_JuniFrSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniFrSubIfLowerIfIndex_Object = MibTableColumn
juniFrSubIfLowerIfIndex = _JuniFrSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 3),
    _JuniFrSubIfLowerIfIndex_Type()
)
juniFrSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrSubIfLowerIfIndex.setStatus("current")


class _JuniFrSubIfId_Type(Integer32):
    """Custom type juniFrSubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniFrSubIfId_Type.__name__ = "Integer32"
_JuniFrSubIfId_Object = MibTableColumn
juniFrSubIfId = _JuniFrSubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 2, 1, 4),
    _JuniFrSubIfId_Type()
)
juniFrSubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrSubIfId.setStatus("current")
_JuniFrSubIfCktTable_Object = MibTable
juniFrSubIfCktTable = _JuniFrSubIfCktTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniFrSubIfCktTable.setStatus("current")
_JuniFrSubIfCktEntry_Object = MibTableRow
juniFrSubIfCktEntry = _JuniFrSubIfCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1)
)
juniFrSubIfCktEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrSubIfIndex"),
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrSubIfCktDlci"),
)
if mibBuilder.loadTexts:
    juniFrSubIfCktEntry.setStatus("current")
_JuniFrSubIfCktDlci_Type = DLCI
_JuniFrSubIfCktDlci_Object = MibTableColumn
juniFrSubIfCktDlci = _JuniFrSubIfCktDlci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1, 1),
    _JuniFrSubIfCktDlci_Type()
)
juniFrSubIfCktDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrSubIfCktDlci.setStatus("current")
_JuniFrSubIfCktRowStatus_Type = RowStatus
_JuniFrSubIfCktRowStatus_Object = MibTableColumn
juniFrSubIfCktRowStatus = _JuniFrSubIfCktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 2, 3, 1, 2),
    _JuniFrSubIfCktRowStatus_Type()
)
juniFrSubIfCktRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrSubIfCktRowStatus.setStatus("current")
_JuniFrMlFr_ObjectIdentity = ObjectIdentity
juniFrMlFr = _JuniFrMlFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3)
)
_JuniFrMlFrBundleTable_Object = MibTable
juniFrMlFrBundleTable = _JuniFrMlFrBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniFrMlFrBundleTable.setStatus("current")
_JuniFrMlFrBundleEntry_Object = MibTableRow
juniFrMlFrBundleEntry = _JuniFrMlFrBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 1, 1)
)
juniFrMlFrBundleEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrMlFrBundleName"),
)
if mibBuilder.loadTexts:
    juniFrMlFrBundleEntry.setStatus("current")
_JuniFrMlFrBundleName_Type = JuniFrMlFrBundleName
_JuniFrMlFrBundleName_Object = MibTableColumn
juniFrMlFrBundleName = _JuniFrMlFrBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 1, 1, 1),
    _JuniFrMlFrBundleName_Type()
)
juniFrMlFrBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrMlFrBundleName.setStatus("current")
_JuniFrMlFrBundleRowStatus_Type = RowStatus
_JuniFrMlFrBundleRowStatus_Object = MibTableColumn
juniFrMlFrBundleRowStatus = _JuniFrMlFrBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 1, 1, 2),
    _JuniFrMlFrBundleRowStatus_Type()
)
juniFrMlFrBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrBundleRowStatus.setStatus("current")
_JuniFrMlFrNextLinkIfIndex_Type = JuniNextIfIndex
_JuniFrMlFrNextLinkIfIndex_Object = MibScalar
juniFrMlFrNextLinkIfIndex = _JuniFrMlFrNextLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 2),
    _JuniFrMlFrNextLinkIfIndex_Type()
)
juniFrMlFrNextLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniFrMlFrNextLinkIfIndex.setStatus("current")
_JuniFrMlFrLinkConfigTable_Object = MibTable
juniFrMlFrLinkConfigTable = _JuniFrMlFrLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniFrMlFrLinkConfigTable.setStatus("current")
_JuniFrMlFrLinkConfigEntry_Object = MibTableRow
juniFrMlFrLinkConfigEntry = _JuniFrMlFrLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 3, 1)
)
juniFrMlFrLinkConfigEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrMlFrLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrMlFrLinkConfigEntry.setStatus("current")
_JuniFrMlFrLinkConfigIfIndex_Type = InterfaceIndex
_JuniFrMlFrLinkConfigIfIndex_Object = MibTableColumn
juniFrMlFrLinkConfigIfIndex = _JuniFrMlFrLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 3, 1, 1),
    _JuniFrMlFrLinkConfigIfIndex_Type()
)
juniFrMlFrLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrMlFrLinkConfigIfIndex.setStatus("current")
_JuniFrMlFrLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_JuniFrMlFrLinkConfigLowerIfIndex_Object = MibTableColumn
juniFrMlFrLinkConfigLowerIfIndex = _JuniFrMlFrLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 3, 1, 2),
    _JuniFrMlFrLinkConfigLowerIfIndex_Type()
)
juniFrMlFrLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrLinkConfigLowerIfIndex.setStatus("current")
_JuniFrMlFrLinkConfigRowStatus_Type = RowStatus
_JuniFrMlFrLinkConfigRowStatus_Object = MibTableColumn
juniFrMlFrLinkConfigRowStatus = _JuniFrMlFrLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 3, 1, 3),
    _JuniFrMlFrLinkConfigRowStatus_Type()
)
juniFrMlFrLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrLinkConfigRowStatus.setStatus("current")
_JuniFrMlFrMajorConfigTable_Object = MibTable
juniFrMlFrMajorConfigTable = _JuniFrMlFrMajorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4)
)
if mibBuilder.loadTexts:
    juniFrMlFrMajorConfigTable.setStatus("current")
_JuniFrMlFrMajorConfigEntry_Object = MibTableRow
juniFrMlFrMajorConfigEntry = _JuniFrMlFrMajorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4, 1)
)
juniFrMlFrMajorConfigEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrMlFrMajorConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrMlFrMajorConfigEntry.setStatus("current")
_JuniFrMlFrMajorConfigIfIndex_Type = InterfaceIndex
_JuniFrMlFrMajorConfigIfIndex_Object = MibTableColumn
juniFrMlFrMajorConfigIfIndex = _JuniFrMlFrMajorConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4, 1, 1),
    _JuniFrMlFrMajorConfigIfIndex_Type()
)
juniFrMlFrMajorConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrMlFrMajorConfigIfIndex.setStatus("current")
_JuniFrMlFrMajorConfigLowerIfIndex_Type = InterfaceIndex
_JuniFrMlFrMajorConfigLowerIfIndex_Object = MibTableColumn
juniFrMlFrMajorConfigLowerIfIndex = _JuniFrMlFrMajorConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4, 1, 2),
    _JuniFrMlFrMajorConfigLowerIfIndex_Type()
)
juniFrMlFrMajorConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrMajorConfigLowerIfIndex.setStatus("current")
_JuniFrMlFrMajorBundleName_Type = JuniFrMlFrBundleName
_JuniFrMlFrMajorBundleName_Object = MibTableColumn
juniFrMlFrMajorBundleName = _JuniFrMlFrMajorBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4, 1, 3),
    _JuniFrMlFrMajorBundleName_Type()
)
juniFrMlFrMajorBundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrMajorBundleName.setStatus("current")
_JuniFrMlFrMajorRowStatus_Type = RowStatus
_JuniFrMlFrMajorRowStatus_Object = MibTableColumn
juniFrMlFrMajorRowStatus = _JuniFrMlFrMajorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 4, 1, 4),
    _JuniFrMlFrMajorRowStatus_Type()
)
juniFrMlFrMajorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrMajorRowStatus.setStatus("current")
_JuniFrMlFrLinkBindTable_Object = MibTable
juniFrMlFrLinkBindTable = _JuniFrMlFrLinkBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 5)
)
if mibBuilder.loadTexts:
    juniFrMlFrLinkBindTable.setStatus("current")
_JuniFrMlFrLinkBindEntry_Object = MibTableRow
juniFrMlFrLinkBindEntry = _JuniFrMlFrLinkBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 5, 1)
)
juniFrMlFrLinkBindEntry.setIndexNames(
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrMlFrBindMajorIfIndex"),
    (0, "Juniper-FRAME-RELAY-MIB", "juniFrMlFrBindLinkIfIndex"),
)
if mibBuilder.loadTexts:
    juniFrMlFrLinkBindEntry.setStatus("current")
_JuniFrMlFrBindMajorIfIndex_Type = InterfaceIndex
_JuniFrMlFrBindMajorIfIndex_Object = MibTableColumn
juniFrMlFrBindMajorIfIndex = _JuniFrMlFrBindMajorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 5, 1, 1),
    _JuniFrMlFrBindMajorIfIndex_Type()
)
juniFrMlFrBindMajorIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrMlFrBindMajorIfIndex.setStatus("current")
_JuniFrMlFrBindLinkIfIndex_Type = InterfaceIndex
_JuniFrMlFrBindLinkIfIndex_Object = MibTableColumn
juniFrMlFrBindLinkIfIndex = _JuniFrMlFrBindLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 5, 1, 2),
    _JuniFrMlFrBindLinkIfIndex_Type()
)
juniFrMlFrBindLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniFrMlFrBindLinkIfIndex.setStatus("current")
_JuniFrMlFrBindRowStatus_Type = RowStatus
_JuniFrMlFrBindRowStatus_Object = MibTableColumn
juniFrMlFrBindRowStatus = _JuniFrMlFrBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 1, 3, 5, 1, 3),
    _JuniFrMlFrBindRowStatus_Type()
)
juniFrMlFrBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFrMlFrBindRowStatus.setStatus("current")
_JuniFrConformance_ObjectIdentity = ObjectIdentity
juniFrConformance = _JuniFrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4)
)
_JuniFrCompliances_ObjectIdentity = ObjectIdentity
juniFrCompliances = _JuniFrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 1)
)
_JuniFrGroups_ObjectIdentity = ObjectIdentity
juniFrGroups = _JuniFrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2)
)

# Managed Objects groups

juniFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 1)
)
juniFrGroup.setObjects(
      *(("Juniper-FRAME-RELAY-MIB", "juniFrNextIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiState"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiAddress"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiAddressLen"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiPollingInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiFullEnquiryInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiErrorThreshold"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMonitoredEvents"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMaxSupportedVCs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMulticast"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiLowerIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiRole"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDcePollingInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDceErrorThreshold"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDceMonitoredEvents"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteFullEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteFullEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteAsyncUpdates"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteUnknownRxMessages"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteLossOfSequences"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteNoResponseTimeouts"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceFullEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceFullEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceAsyncUpdates"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceUnknownRxMessages"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceLossOfSequences"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceNoResponseTimeouts"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDiscontinuityTime"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitState"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedFECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedBECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentFrames"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentOctets"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedFrames"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedOctets"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitCreationTime"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitLastTimeChange"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitCommittedBurst"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitExcessBurst"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitThroughput"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitMulticast"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitType"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitDiscards"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedDEs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentDEs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitLogicalIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentFECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentBECNs"))
)
if mibBuilder.loadTexts:
    juniFrGroup.setStatus("obsolete")

juniFrSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 2)
)
juniFrSubIfGroup.setObjects(
      *(("Juniper-FRAME-RELAY-MIB", "juniFrSubIfNextIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrSubIfRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrSubIfLowerIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrSubIfId"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrSubIfCktRowStatus"))
)
if mibBuilder.loadTexts:
    juniFrSubIfGroup.setStatus("current")

juniFrGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 3)
)
juniFrGroup2.setObjects(
      *(("Juniper-FRAME-RELAY-MIB", "juniFrNextIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiState"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiAddress"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiAddressLen"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiPollingInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiFullEnquiryInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiErrorThreshold"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMonitoredEvents"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMaxSupportedVCs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMulticast"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiLowerIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiRole"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDcePollingInterval"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDceErrorThreshold"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiDceMonitoredEvents"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiMultilinkFrBundleName"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteFullEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteFullEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteAsyncUpdates"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteUnknownRxMessages"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteLossOfSequences"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDteNoResponseTimeouts"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceFullEnquiries"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceFullEnquiryResponses"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceAsyncUpdates"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceUnknownRxMessages"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceLossOfSequences"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDceNoResponseTimeouts"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrDlcmiStatsDiscontinuityTime"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitState"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedFECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedBECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentFrames"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentOctets"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedFrames"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedOctets"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitCreationTime"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitLastTimeChange"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitCommittedBurst"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitExcessBurst"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitThroughput"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitMulticast"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitType"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitDiscards"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitReceivedDEs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentDEs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitLogicalIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentFECNs"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrCircuitSentBECNs"))
)
if mibBuilder.loadTexts:
    juniFrGroup2.setStatus("current")

juniFrMlFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 2, 4)
)
juniFrMlFrGroup.setObjects(
      *(("Juniper-FRAME-RELAY-MIB", "juniFrMlFrBundleRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrNextLinkIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrLinkConfigLowerIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrLinkConfigRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrMajorConfigLowerIfIndex"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrMajorBundleName"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrMajorRowStatus"),
        ("Juniper-FRAME-RELAY-MIB", "juniFrMlFrBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniFrMlFrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniFrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniFrCompliance.setStatus(
        "obsolete"
    )

juniFrCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 10, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniFrCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-FRAME-RELAY-MIB",
    **{"JuniFrMlFrBundleName": JuniFrMlFrBundleName,
       "juniFrameRelayMIB": juniFrameRelayMIB,
       "juniFrObjects": juniFrObjects,
       "juniFrIfLayer": juniFrIfLayer,
       "juniFrNextIfIndex": juniFrNextIfIndex,
       "juniFrDlcmiTable": juniFrDlcmiTable,
       "juniFrDlcmiEntry": juniFrDlcmiEntry,
       "juniFrDlcmiIfIndex": juniFrDlcmiIfIndex,
       "juniFrDlcmiState": juniFrDlcmiState,
       "juniFrDlcmiAddress": juniFrDlcmiAddress,
       "juniFrDlcmiAddressLen": juniFrDlcmiAddressLen,
       "juniFrDlcmiPollingInterval": juniFrDlcmiPollingInterval,
       "juniFrDlcmiFullEnquiryInterval": juniFrDlcmiFullEnquiryInterval,
       "juniFrDlcmiErrorThreshold": juniFrDlcmiErrorThreshold,
       "juniFrDlcmiMonitoredEvents": juniFrDlcmiMonitoredEvents,
       "juniFrDlcmiMaxSupportedVCs": juniFrDlcmiMaxSupportedVCs,
       "juniFrDlcmiMulticast": juniFrDlcmiMulticast,
       "juniFrDlcmiStatus": juniFrDlcmiStatus,
       "juniFrDlcmiRowStatus": juniFrDlcmiRowStatus,
       "juniFrDlcmiLowerIfIndex": juniFrDlcmiLowerIfIndex,
       "juniFrDlcmiRole": juniFrDlcmiRole,
       "juniFrDlcmiDcePollingInterval": juniFrDlcmiDcePollingInterval,
       "juniFrDlcmiDceErrorThreshold": juniFrDlcmiDceErrorThreshold,
       "juniFrDlcmiDceMonitoredEvents": juniFrDlcmiDceMonitoredEvents,
       "juniFrDlcmiMultilinkFrBundleName": juniFrDlcmiMultilinkFrBundleName,
       "juniFrDlcmiStatsTable": juniFrDlcmiStatsTable,
       "juniFrDlcmiStatsEntry": juniFrDlcmiStatsEntry,
       "juniFrDlcmiStatsDteEnquiries": juniFrDlcmiStatsDteEnquiries,
       "juniFrDlcmiStatsDteFullEnquiries": juniFrDlcmiStatsDteFullEnquiries,
       "juniFrDlcmiStatsDteEnquiryResponses": juniFrDlcmiStatsDteEnquiryResponses,
       "juniFrDlcmiStatsDteFullEnquiryResponses": juniFrDlcmiStatsDteFullEnquiryResponses,
       "juniFrDlcmiStatsDteAsyncUpdates": juniFrDlcmiStatsDteAsyncUpdates,
       "juniFrDlcmiStatsDteUnknownRxMessages": juniFrDlcmiStatsDteUnknownRxMessages,
       "juniFrDlcmiStatsDteLossOfSequences": juniFrDlcmiStatsDteLossOfSequences,
       "juniFrDlcmiStatsDteNoResponseTimeouts": juniFrDlcmiStatsDteNoResponseTimeouts,
       "juniFrDlcmiStatsDceEnquiries": juniFrDlcmiStatsDceEnquiries,
       "juniFrDlcmiStatsDceFullEnquiries": juniFrDlcmiStatsDceFullEnquiries,
       "juniFrDlcmiStatsDceEnquiryResponses": juniFrDlcmiStatsDceEnquiryResponses,
       "juniFrDlcmiStatsDceFullEnquiryResponses": juniFrDlcmiStatsDceFullEnquiryResponses,
       "juniFrDlcmiStatsDceAsyncUpdates": juniFrDlcmiStatsDceAsyncUpdates,
       "juniFrDlcmiStatsDceUnknownRxMessages": juniFrDlcmiStatsDceUnknownRxMessages,
       "juniFrDlcmiStatsDceLossOfSequences": juniFrDlcmiStatsDceLossOfSequences,
       "juniFrDlcmiStatsDceNoResponseTimeouts": juniFrDlcmiStatsDceNoResponseTimeouts,
       "juniFrDlcmiStatsDiscontinuityTime": juniFrDlcmiStatsDiscontinuityTime,
       "juniFrCircuitTable": juniFrCircuitTable,
       "juniFrCircuitEntry": juniFrCircuitEntry,
       "juniFrCircuitIfIndex": juniFrCircuitIfIndex,
       "juniFrCircuitDlci": juniFrCircuitDlci,
       "juniFrCircuitState": juniFrCircuitState,
       "juniFrCircuitReceivedFECNs": juniFrCircuitReceivedFECNs,
       "juniFrCircuitReceivedBECNs": juniFrCircuitReceivedBECNs,
       "juniFrCircuitSentFrames": juniFrCircuitSentFrames,
       "juniFrCircuitSentOctets": juniFrCircuitSentOctets,
       "juniFrCircuitReceivedFrames": juniFrCircuitReceivedFrames,
       "juniFrCircuitReceivedOctets": juniFrCircuitReceivedOctets,
       "juniFrCircuitCreationTime": juniFrCircuitCreationTime,
       "juniFrCircuitLastTimeChange": juniFrCircuitLastTimeChange,
       "juniFrCircuitCommittedBurst": juniFrCircuitCommittedBurst,
       "juniFrCircuitExcessBurst": juniFrCircuitExcessBurst,
       "juniFrCircuitThroughput": juniFrCircuitThroughput,
       "juniFrCircuitMulticast": juniFrCircuitMulticast,
       "juniFrCircuitType": juniFrCircuitType,
       "juniFrCircuitDiscards": juniFrCircuitDiscards,
       "juniFrCircuitReceivedDEs": juniFrCircuitReceivedDEs,
       "juniFrCircuitSentDEs": juniFrCircuitSentDEs,
       "juniFrCircuitLogicalIfIndex": juniFrCircuitLogicalIfIndex,
       "juniFrCircuitRowStatus": juniFrCircuitRowStatus,
       "juniFrCircuitSentFECNs": juniFrCircuitSentFECNs,
       "juniFrCircuitSentBECNs": juniFrCircuitSentBECNs,
       "juniFrSubIfLayer": juniFrSubIfLayer,
       "juniFrSubIfNextIfIndex": juniFrSubIfNextIfIndex,
       "juniFrSubIfTable": juniFrSubIfTable,
       "juniFrSubIfEntry": juniFrSubIfEntry,
       "juniFrSubIfIndex": juniFrSubIfIndex,
       "juniFrSubIfRowStatus": juniFrSubIfRowStatus,
       "juniFrSubIfLowerIfIndex": juniFrSubIfLowerIfIndex,
       "juniFrSubIfId": juniFrSubIfId,
       "juniFrSubIfCktTable": juniFrSubIfCktTable,
       "juniFrSubIfCktEntry": juniFrSubIfCktEntry,
       "juniFrSubIfCktDlci": juniFrSubIfCktDlci,
       "juniFrSubIfCktRowStatus": juniFrSubIfCktRowStatus,
       "juniFrMlFr": juniFrMlFr,
       "juniFrMlFrBundleTable": juniFrMlFrBundleTable,
       "juniFrMlFrBundleEntry": juniFrMlFrBundleEntry,
       "juniFrMlFrBundleName": juniFrMlFrBundleName,
       "juniFrMlFrBundleRowStatus": juniFrMlFrBundleRowStatus,
       "juniFrMlFrNextLinkIfIndex": juniFrMlFrNextLinkIfIndex,
       "juniFrMlFrLinkConfigTable": juniFrMlFrLinkConfigTable,
       "juniFrMlFrLinkConfigEntry": juniFrMlFrLinkConfigEntry,
       "juniFrMlFrLinkConfigIfIndex": juniFrMlFrLinkConfigIfIndex,
       "juniFrMlFrLinkConfigLowerIfIndex": juniFrMlFrLinkConfigLowerIfIndex,
       "juniFrMlFrLinkConfigRowStatus": juniFrMlFrLinkConfigRowStatus,
       "juniFrMlFrMajorConfigTable": juniFrMlFrMajorConfigTable,
       "juniFrMlFrMajorConfigEntry": juniFrMlFrMajorConfigEntry,
       "juniFrMlFrMajorConfigIfIndex": juniFrMlFrMajorConfigIfIndex,
       "juniFrMlFrMajorConfigLowerIfIndex": juniFrMlFrMajorConfigLowerIfIndex,
       "juniFrMlFrMajorBundleName": juniFrMlFrMajorBundleName,
       "juniFrMlFrMajorRowStatus": juniFrMlFrMajorRowStatus,
       "juniFrMlFrLinkBindTable": juniFrMlFrLinkBindTable,
       "juniFrMlFrLinkBindEntry": juniFrMlFrLinkBindEntry,
       "juniFrMlFrBindMajorIfIndex": juniFrMlFrBindMajorIfIndex,
       "juniFrMlFrBindLinkIfIndex": juniFrMlFrBindLinkIfIndex,
       "juniFrMlFrBindRowStatus": juniFrMlFrBindRowStatus,
       "juniFrConformance": juniFrConformance,
       "juniFrCompliances": juniFrCompliances,
       "juniFrCompliance": juniFrCompliance,
       "juniFrCompliance2": juniFrCompliance2,
       "juniFrGroups": juniFrGroups,
       "juniFrGroup": juniFrGroup,
       "juniFrSubIfGroup": juniFrSubIfGroup,
       "juniFrGroup2": juniFrGroup2,
       "juniFrMlFrGroup": juniFrMlFrGroup}
)
