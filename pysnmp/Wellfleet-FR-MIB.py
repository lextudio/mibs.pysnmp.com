# SNMP MIB module (Wellfleet-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:14 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfFrameRelayGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFrameRelayGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFrDlcmiTable_Object = MibTable
wfFrDlcmiTable = _WfFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1)
)
if mibBuilder.loadTexts:
    wfFrDlcmiTable.setStatus("mandatory")
_WfFrDlcmiEntry_Object = MibTableRow
wfFrDlcmiEntry = _WfFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1)
)
wfFrDlcmiEntry.setIndexNames(
    (0, "Wellfleet-FR-MIB", "wfFr1DlcmiCircuit"),
)
if mibBuilder.loadTexts:
    wfFrDlcmiEntry.setStatus("mandatory")


class _WfFr1DlcmiDelete_Type(Integer32):
    """Custom type wfFr1DlcmiDelete based on Integer32"""
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


_WfFr1DlcmiDelete_Type.__name__ = "Integer32"
_WfFr1DlcmiDelete_Object = MibTableColumn
wfFr1DlcmiDelete = _WfFr1DlcmiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 1),
    _WfFr1DlcmiDelete_Type()
)
wfFr1DlcmiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiDelete.setStatus("mandatory")


class _WfFr1DlcmiDisable_Type(Integer32):
    """Custom type wfFr1DlcmiDisable based on Integer32"""
    defaultValue = 1

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


_WfFr1DlcmiDisable_Type.__name__ = "Integer32"
_WfFr1DlcmiDisable_Object = MibTableColumn
wfFr1DlcmiDisable = _WfFr1DlcmiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 2),
    _WfFr1DlcmiDisable_Type()
)
wfFr1DlcmiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiDisable.setStatus("mandatory")


class _WfFr1DlcmiState_Type(Integer32):
    """Custom type wfFr1DlcmiState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfFr1DlcmiState_Type.__name__ = "Integer32"
_WfFr1DlcmiState_Object = MibTableColumn
wfFr1DlcmiState = _WfFr1DlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 3),
    _WfFr1DlcmiState_Type()
)
wfFr1DlcmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiState.setStatus("mandatory")
_WfFr1DlcmiCircuit_Type = Integer32
_WfFr1DlcmiCircuit_Object = MibTableColumn
wfFr1DlcmiCircuit = _WfFr1DlcmiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 4),
    _WfFr1DlcmiCircuit_Type()
)
wfFr1DlcmiCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiCircuit.setStatus("mandatory")


class _WfFr1DlcmiManagementType_Type(Integer32):
    """Custom type wfFr1DlcmiManagementType based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("annexa", 5),
          ("annexaswitch", 8),
          ("annexdswitch", 7),
          ("lmi", 2),
          ("lmiswitch", 6),
          ("none", 1),
          ("t1617b", 4),
          ("t1617d", 3))
    )


_WfFr1DlcmiManagementType_Type.__name__ = "Integer32"
_WfFr1DlcmiManagementType_Object = MibTableColumn
wfFr1DlcmiManagementType = _WfFr1DlcmiManagementType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 5),
    _WfFr1DlcmiManagementType_Type()
)
wfFr1DlcmiManagementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiManagementType.setStatus("mandatory")


class _WfFr1DlcmiStatus_Type(Integer32):
    """Custom type wfFr1DlcmiStatus based on Integer32"""
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
        *(("fault", 3),
          ("recovered", 4),
          ("running", 2),
          ("start", 1))
    )


_WfFr1DlcmiStatus_Type.__name__ = "Integer32"
_WfFr1DlcmiStatus_Object = MibTableColumn
wfFr1DlcmiStatus = _WfFr1DlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 6),
    _WfFr1DlcmiStatus_Type()
)
wfFr1DlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiStatus.setStatus("mandatory")


class _WfFr1DlcmiAddress_Type(Integer32):
    """Custom type wfFr1DlcmiAddress based on Integer32"""
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
          ("q922march90", 2),
          ("q922november90", 3))
    )


_WfFr1DlcmiAddress_Type.__name__ = "Integer32"
_WfFr1DlcmiAddress_Object = MibTableColumn
wfFr1DlcmiAddress = _WfFr1DlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 7),
    _WfFr1DlcmiAddress_Type()
)
wfFr1DlcmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiAddress.setStatus("mandatory")


class _WfFr1DlcmiAddressLen_Type(Integer32):
    """Custom type wfFr1DlcmiAddressLen based on Integer32"""
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
        *(("fourbyte", 4),
          ("threebyte", 3),
          ("twobyte", 2))
    )


_WfFr1DlcmiAddressLen_Type.__name__ = "Integer32"
_WfFr1DlcmiAddressLen_Object = MibTableColumn
wfFr1DlcmiAddressLen = _WfFr1DlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 8),
    _WfFr1DlcmiAddressLen_Type()
)
wfFr1DlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiAddressLen.setStatus("mandatory")


class _WfFr1DlcmiPollingInterval_Type(Integer32):
    """Custom type wfFr1DlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfFr1DlcmiPollingInterval_Type.__name__ = "Integer32"
_WfFr1DlcmiPollingInterval_Object = MibTableColumn
wfFr1DlcmiPollingInterval = _WfFr1DlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 9),
    _WfFr1DlcmiPollingInterval_Type()
)
wfFr1DlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiPollingInterval.setStatus("mandatory")


class _WfFr1DlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type wfFr1DlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFr1DlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFr1DlcmiFullEnquiryInterval_Object = MibTableColumn
wfFr1DlcmiFullEnquiryInterval = _WfFr1DlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 10),
    _WfFr1DlcmiFullEnquiryInterval_Type()
)
wfFr1DlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiFullEnquiryInterval.setStatus("mandatory")


class _WfFr1DlcmiErrorThreshold_Type(Integer32):
    """Custom type wfFr1DlcmiErrorThreshold based on Integer32"""
    defaultValue = 3


_WfFr1DlcmiErrorThreshold_Object = MibTableColumn
wfFr1DlcmiErrorThreshold = _WfFr1DlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 11),
    _WfFr1DlcmiErrorThreshold_Type()
)
wfFr1DlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiErrorThreshold.setStatus("mandatory")


class _WfFr1DlcmiMonitoredEvents_Type(Integer32):
    """Custom type wfFr1DlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4


_WfFr1DlcmiMonitoredEvents_Object = MibTableColumn
wfFr1DlcmiMonitoredEvents = _WfFr1DlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 12),
    _WfFr1DlcmiMonitoredEvents_Type()
)
wfFr1DlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiMonitoredEvents.setStatus("mandatory")
_WfFr1DlcmiMaxSupportedVCs_Type = Integer32
_WfFr1DlcmiMaxSupportedVCs_Object = MibTableColumn
wfFr1DlcmiMaxSupportedVCs = _WfFr1DlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 13),
    _WfFr1DlcmiMaxSupportedVCs_Type()
)
wfFr1DlcmiMaxSupportedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiMaxSupportedVCs.setStatus("mandatory")


class _WfFr1DlcmiMulticast_Type(Integer32):
    """Custom type wfFr1DlcmiMulticast based on Integer32"""
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


_WfFr1DlcmiMulticast_Type.__name__ = "Integer32"
_WfFr1DlcmiMulticast_Object = MibTableColumn
wfFr1DlcmiMulticast = _WfFr1DlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 14),
    _WfFr1DlcmiMulticast_Type()
)
wfFr1DlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1DlcmiMulticast.setStatus("mandatory")


class _WfFr1DlcmiSeqCount_Type(Integer32):
    """Custom type wfFr1DlcmiSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFr1DlcmiSeqCount_Type.__name__ = "Integer32"
_WfFr1DlcmiSeqCount_Object = MibTableColumn
wfFr1DlcmiSeqCount = _WfFr1DlcmiSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 15),
    _WfFr1DlcmiSeqCount_Type()
)
wfFr1DlcmiSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiSeqCount.setStatus("mandatory")


class _WfFr1DlcmiLastReceived_Type(Integer32):
    """Custom type wfFr1DlcmiLastReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFr1DlcmiLastReceived_Type.__name__ = "Integer32"
_WfFr1DlcmiLastReceived_Object = MibTableColumn
wfFr1DlcmiLastReceived = _WfFr1DlcmiLastReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 16),
    _WfFr1DlcmiLastReceived_Type()
)
wfFr1DlcmiLastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiLastReceived.setStatus("mandatory")


class _WfFr1DlcmiPassiveSeqCount_Type(Integer32):
    """Custom type wfFr1DlcmiPassiveSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFr1DlcmiPassiveSeqCount_Type.__name__ = "Integer32"
_WfFr1DlcmiPassiveSeqCount_Object = MibTableColumn
wfFr1DlcmiPassiveSeqCount = _WfFr1DlcmiPassiveSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 17),
    _WfFr1DlcmiPassiveSeqCount_Type()
)
wfFr1DlcmiPassiveSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiPassiveSeqCount.setStatus("mandatory")


class _WfFr1DlcmiPassiveReceived_Type(Integer32):
    """Custom type wfFr1DlcmiPassiveReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFr1DlcmiPassiveReceived_Type.__name__ = "Integer32"
_WfFr1DlcmiPassiveReceived_Object = MibTableColumn
wfFr1DlcmiPassiveReceived = _WfFr1DlcmiPassiveReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 18),
    _WfFr1DlcmiPassiveReceived_Type()
)
wfFr1DlcmiPassiveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiPassiveReceived.setStatus("mandatory")
_WfFr1DlcmiPolls_Type = Integer32
_WfFr1DlcmiPolls_Object = MibTableColumn
wfFr1DlcmiPolls = _WfFr1DlcmiPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 19),
    _WfFr1DlcmiPolls_Type()
)
wfFr1DlcmiPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiPolls.setStatus("mandatory")
_WfFr1DlcmiAlarmTimer_Type = Integer32
_WfFr1DlcmiAlarmTimer_Object = MibTableColumn
wfFr1DlcmiAlarmTimer = _WfFr1DlcmiAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 20),
    _WfFr1DlcmiAlarmTimer_Type()
)
wfFr1DlcmiAlarmTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1DlcmiAlarmTimer.setStatus("mandatory")


class _WfFr1ErrType_Type(Integer32):
    """Custom type wfFr1ErrType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cntrl", 11),
          ("illegaldlci", 4),
          ("long", 3),
          ("protoerr", 6),
          ("reset", 10),
          ("sequenceerr", 8),
          ("short", 2),
          ("unknown", 1),
          ("unknowndlci", 5),
          ("unknownie", 7),
          ("unknownrpt", 9))
    )


_WfFr1ErrType_Type.__name__ = "Integer32"
_WfFr1ErrType_Object = MibTableColumn
wfFr1ErrType = _WfFr1ErrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 21),
    _WfFr1ErrType_Type()
)
wfFr1ErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1ErrType.setStatus("mandatory")
_WfFr1ErrData_Type = OctetString
_WfFr1ErrData_Object = MibTableColumn
wfFr1ErrData = _WfFr1ErrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 22),
    _WfFr1ErrData_Type()
)
wfFr1ErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1ErrData.setStatus("mandatory")
_WfFr1ErrTime_Type = TimeTicks
_WfFr1ErrTime_Object = MibTableColumn
wfFr1ErrTime = _WfFr1ErrTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 23),
    _WfFr1ErrTime_Type()
)
wfFr1ErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1ErrTime.setStatus("mandatory")
_WfFr1ErrDiscards_Type = Counter32
_WfFr1ErrDiscards_Object = MibTableColumn
wfFr1ErrDiscards = _WfFr1ErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 24),
    _WfFr1ErrDiscards_Type()
)
wfFr1ErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1ErrDiscards.setStatus("mandatory")
_WfFr1ErrDrops_Type = Counter32
_WfFr1ErrDrops_Object = MibTableColumn
wfFr1ErrDrops = _WfFr1ErrDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 25),
    _WfFr1ErrDrops_Type()
)
wfFr1ErrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1ErrDrops.setStatus("mandatory")
_WfFrCircuitTable_Object = MibTable
wfFrCircuitTable = _WfFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    wfFrCircuitTable.setStatus("mandatory")
_WfFrCircuitEntry_Object = MibTableRow
wfFrCircuitEntry = _WfFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1)
)
wfFrCircuitEntry.setIndexNames(
    (0, "Wellfleet-FR-MIB", "wfFr1CircuitNumber"),
    (0, "Wellfleet-FR-MIB", "wfFr1CircuitDlci"),
)
if mibBuilder.loadTexts:
    wfFrCircuitEntry.setStatus("mandatory")


class _WfFr1CircuitDelete_Type(Integer32):
    """Custom type wfFr1CircuitDelete based on Integer32"""
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
        *(("created", 1),
          ("deleted", 2),
          ("system", 3))
    )


_WfFr1CircuitDelete_Type.__name__ = "Integer32"
_WfFr1CircuitDelete_Object = MibTableColumn
wfFr1CircuitDelete = _WfFr1CircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 1),
    _WfFr1CircuitDelete_Type()
)
wfFr1CircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitDelete.setStatus("mandatory")
_WfFr1CircuitNumber_Type = Integer32
_WfFr1CircuitNumber_Object = MibTableColumn
wfFr1CircuitNumber = _WfFr1CircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 2),
    _WfFr1CircuitNumber_Type()
)
wfFr1CircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitNumber.setStatus("mandatory")


class _WfFr1CircuitDlci_Type(Integer32):
    """Custom type wfFr1CircuitDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              1007,
              1024,
              64511,
              131072,
              8257535)
        )
    )
    namedValues = NamedValues(
        *(("fourbytemaximum", 8257535),
          ("fourbyteminimum", 131072),
          ("threebytemaximum", 64511),
          ("threebyteminimum", 1024),
          ("twobytemaximum", 1007),
          ("twobyteminimum", 16))
    )


_WfFr1CircuitDlci_Type.__name__ = "Integer32"
_WfFr1CircuitDlci_Object = MibTableColumn
wfFr1CircuitDlci = _WfFr1CircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 3),
    _WfFr1CircuitDlci_Type()
)
wfFr1CircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitDlci.setStatus("mandatory")


class _WfFr1CircuitState_Type(Integer32):
    """Custom type wfFr1CircuitState based on Integer32"""
    defaultValue = 1

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
        *(("active", 2),
          ("control", 5),
          ("inactive", 3),
          ("invalid", 1),
          ("xoff", 4))
    )


_WfFr1CircuitState_Type.__name__ = "Integer32"
_WfFr1CircuitState_Object = MibTableColumn
wfFr1CircuitState = _WfFr1CircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 4),
    _WfFr1CircuitState_Type()
)
wfFr1CircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitState.setStatus("mandatory")


class _WfFr1CircuitStateSet_Type(Integer32):
    """Custom type wfFr1CircuitStateSet based on Integer32"""
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
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_WfFr1CircuitStateSet_Type.__name__ = "Integer32"
_WfFr1CircuitStateSet_Object = MibTableColumn
wfFr1CircuitStateSet = _WfFr1CircuitStateSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 5),
    _WfFr1CircuitStateSet_Type()
)
wfFr1CircuitStateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitStateSet.setStatus("mandatory")
_WfFr1CircuitReceivedFECNs_Type = Counter32
_WfFr1CircuitReceivedFECNs_Object = MibTableColumn
wfFr1CircuitReceivedFECNs = _WfFr1CircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 6),
    _WfFr1CircuitReceivedFECNs_Type()
)
wfFr1CircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitReceivedFECNs.setStatus("mandatory")
_WfFr1CircuitReceivedBECNs_Type = Counter32
_WfFr1CircuitReceivedBECNs_Object = MibTableColumn
wfFr1CircuitReceivedBECNs = _WfFr1CircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 7),
    _WfFr1CircuitReceivedBECNs_Type()
)
wfFr1CircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitReceivedBECNs.setStatus("mandatory")
_WfFr1CircuitSentFrames_Type = Counter32
_WfFr1CircuitSentFrames_Object = MibTableColumn
wfFr1CircuitSentFrames = _WfFr1CircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 8),
    _WfFr1CircuitSentFrames_Type()
)
wfFr1CircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitSentFrames.setStatus("mandatory")
_WfFr1CircuitSentOctets_Type = Counter32
_WfFr1CircuitSentOctets_Object = MibTableColumn
wfFr1CircuitSentOctets = _WfFr1CircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 9),
    _WfFr1CircuitSentOctets_Type()
)
wfFr1CircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitSentOctets.setStatus("mandatory")
_WfFr1CircuitReceivedFrames_Type = Counter32
_WfFr1CircuitReceivedFrames_Object = MibTableColumn
wfFr1CircuitReceivedFrames = _WfFr1CircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 10),
    _WfFr1CircuitReceivedFrames_Type()
)
wfFr1CircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitReceivedFrames.setStatus("mandatory")
_WfFr1CircuitReceivedOctets_Type = Counter32
_WfFr1CircuitReceivedOctets_Object = MibTableColumn
wfFr1CircuitReceivedOctets = _WfFr1CircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 11),
    _WfFr1CircuitReceivedOctets_Type()
)
wfFr1CircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitReceivedOctets.setStatus("mandatory")
_WfFr1CircuitCreationTime_Type = TimeTicks
_WfFr1CircuitCreationTime_Object = MibTableColumn
wfFr1CircuitCreationTime = _WfFr1CircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 12),
    _WfFr1CircuitCreationTime_Type()
)
wfFr1CircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitCreationTime.setStatus("mandatory")
_WfFr1CircuitLastTimeChange_Type = TimeTicks
_WfFr1CircuitLastTimeChange_Object = MibTableColumn
wfFr1CircuitLastTimeChange = _WfFr1CircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 13),
    _WfFr1CircuitLastTimeChange_Type()
)
wfFr1CircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitLastTimeChange.setStatus("mandatory")
_WfFr1CircuitCommittedBurst_Type = Integer32
_WfFr1CircuitCommittedBurst_Object = MibTableColumn
wfFr1CircuitCommittedBurst = _WfFr1CircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 14),
    _WfFr1CircuitCommittedBurst_Type()
)
wfFr1CircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitCommittedBurst.setStatus("mandatory")
_WfFr1CircuitExcessBurst_Type = Integer32
_WfFr1CircuitExcessBurst_Object = MibTableColumn
wfFr1CircuitExcessBurst = _WfFr1CircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 15),
    _WfFr1CircuitExcessBurst_Type()
)
wfFr1CircuitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitExcessBurst.setStatus("mandatory")
_WfFr1CircuitThroughput_Type = Integer32
_WfFr1CircuitThroughput_Object = MibTableColumn
wfFr1CircuitThroughput = _WfFr1CircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 16),
    _WfFr1CircuitThroughput_Type()
)
wfFr1CircuitThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitThroughput.setStatus("mandatory")


class _WfFr1CircuitMulticast_Type(Integer32):
    """Custom type wfFr1CircuitMulticast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )


_WfFr1CircuitMulticast_Type.__name__ = "Integer32"
_WfFr1CircuitMulticast_Object = MibTableColumn
wfFr1CircuitMulticast = _WfFr1CircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 17),
    _WfFr1CircuitMulticast_Type()
)
wfFr1CircuitMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitMulticast.setStatus("mandatory")
_WfFr1CircuitDiscards_Type = Counter32
_WfFr1CircuitDiscards_Object = MibTableColumn
wfFr1CircuitDiscards = _WfFr1CircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 18),
    _WfFr1CircuitDiscards_Type()
)
wfFr1CircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitDiscards.setStatus("mandatory")
_WfFr1CircuitDrops_Type = Counter32
_WfFr1CircuitDrops_Object = MibTableColumn
wfFr1CircuitDrops = _WfFr1CircuitDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 19),
    _WfFr1CircuitDrops_Type()
)
wfFr1CircuitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFr1CircuitDrops.setStatus("mandatory")
_WfFr1CircuitSubCct_Type = Integer32
_WfFr1CircuitSubCct_Object = MibTableColumn
wfFr1CircuitSubCct = _WfFr1CircuitSubCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 20),
    _WfFr1CircuitSubCct_Type()
)
wfFr1CircuitSubCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitSubCct.setStatus("mandatory")


class _WfFr1CircuitMode_Type(Integer32):
    """Custom type wfFr1CircuitMode based on Integer32"""
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
        *(("direct", 3),
          ("group", 1),
          ("hybrid", 2))
    )


_WfFr1CircuitMode_Type.__name__ = "Integer32"
_WfFr1CircuitMode_Object = MibTableColumn
wfFr1CircuitMode = _WfFr1CircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 21),
    _WfFr1CircuitMode_Type()
)
wfFr1CircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFr1CircuitMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FR-MIB",
    **{"wfFrDlcmiTable": wfFrDlcmiTable,
       "wfFrDlcmiEntry": wfFrDlcmiEntry,
       "wfFr1DlcmiDelete": wfFr1DlcmiDelete,
       "wfFr1DlcmiDisable": wfFr1DlcmiDisable,
       "wfFr1DlcmiState": wfFr1DlcmiState,
       "wfFr1DlcmiCircuit": wfFr1DlcmiCircuit,
       "wfFr1DlcmiManagementType": wfFr1DlcmiManagementType,
       "wfFr1DlcmiStatus": wfFr1DlcmiStatus,
       "wfFr1DlcmiAddress": wfFr1DlcmiAddress,
       "wfFr1DlcmiAddressLen": wfFr1DlcmiAddressLen,
       "wfFr1DlcmiPollingInterval": wfFr1DlcmiPollingInterval,
       "wfFr1DlcmiFullEnquiryInterval": wfFr1DlcmiFullEnquiryInterval,
       "wfFr1DlcmiErrorThreshold": wfFr1DlcmiErrorThreshold,
       "wfFr1DlcmiMonitoredEvents": wfFr1DlcmiMonitoredEvents,
       "wfFr1DlcmiMaxSupportedVCs": wfFr1DlcmiMaxSupportedVCs,
       "wfFr1DlcmiMulticast": wfFr1DlcmiMulticast,
       "wfFr1DlcmiSeqCount": wfFr1DlcmiSeqCount,
       "wfFr1DlcmiLastReceived": wfFr1DlcmiLastReceived,
       "wfFr1DlcmiPassiveSeqCount": wfFr1DlcmiPassiveSeqCount,
       "wfFr1DlcmiPassiveReceived": wfFr1DlcmiPassiveReceived,
       "wfFr1DlcmiPolls": wfFr1DlcmiPolls,
       "wfFr1DlcmiAlarmTimer": wfFr1DlcmiAlarmTimer,
       "wfFr1ErrType": wfFr1ErrType,
       "wfFr1ErrData": wfFr1ErrData,
       "wfFr1ErrTime": wfFr1ErrTime,
       "wfFr1ErrDiscards": wfFr1ErrDiscards,
       "wfFr1ErrDrops": wfFr1ErrDrops,
       "wfFrCircuitTable": wfFrCircuitTable,
       "wfFrCircuitEntry": wfFrCircuitEntry,
       "wfFr1CircuitDelete": wfFr1CircuitDelete,
       "wfFr1CircuitNumber": wfFr1CircuitNumber,
       "wfFr1CircuitDlci": wfFr1CircuitDlci,
       "wfFr1CircuitState": wfFr1CircuitState,
       "wfFr1CircuitStateSet": wfFr1CircuitStateSet,
       "wfFr1CircuitReceivedFECNs": wfFr1CircuitReceivedFECNs,
       "wfFr1CircuitReceivedBECNs": wfFr1CircuitReceivedBECNs,
       "wfFr1CircuitSentFrames": wfFr1CircuitSentFrames,
       "wfFr1CircuitSentOctets": wfFr1CircuitSentOctets,
       "wfFr1CircuitReceivedFrames": wfFr1CircuitReceivedFrames,
       "wfFr1CircuitReceivedOctets": wfFr1CircuitReceivedOctets,
       "wfFr1CircuitCreationTime": wfFr1CircuitCreationTime,
       "wfFr1CircuitLastTimeChange": wfFr1CircuitLastTimeChange,
       "wfFr1CircuitCommittedBurst": wfFr1CircuitCommittedBurst,
       "wfFr1CircuitExcessBurst": wfFr1CircuitExcessBurst,
       "wfFr1CircuitThroughput": wfFr1CircuitThroughput,
       "wfFr1CircuitMulticast": wfFr1CircuitMulticast,
       "wfFr1CircuitDiscards": wfFr1CircuitDiscards,
       "wfFr1CircuitDrops": wfFr1CircuitDrops,
       "wfFr1CircuitSubCct": wfFr1CircuitSubCct,
       "wfFr1CircuitMode": wfFr1CircuitMode}
)
