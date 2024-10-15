# SNMP MIB module (Wellfleet-FRSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FRSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:15 2024
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

(wfFrswGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFrswGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFrSwDlcmiTable_Object = MibTable
wfFrSwDlcmiTable = _WfFrSwDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1)
)
if mibBuilder.loadTexts:
    wfFrSwDlcmiTable.setStatus("mandatory")
_WfFrSwDlcmiEntry_Object = MibTableRow
wfFrSwDlcmiEntry = _WfFrSwDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1)
)
wfFrSwDlcmiEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwDlcmiCircuit"),
)
if mibBuilder.loadTexts:
    wfFrSwDlcmiEntry.setStatus("mandatory")


class _WfFrSwDlcmiDelete_Type(Integer32):
    """Custom type wfFrSwDlcmiDelete based on Integer32"""
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


_WfFrSwDlcmiDelete_Type.__name__ = "Integer32"
_WfFrSwDlcmiDelete_Object = MibTableColumn
wfFrSwDlcmiDelete = _WfFrSwDlcmiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 1),
    _WfFrSwDlcmiDelete_Type()
)
wfFrSwDlcmiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDelete.setStatus("mandatory")


class _WfFrSwDlcmiState_Type(Integer32):
    """Custom type wfFrSwDlcmiState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfFrSwDlcmiState_Type.__name__ = "Integer32"
_WfFrSwDlcmiState_Object = MibTableColumn
wfFrSwDlcmiState = _WfFrSwDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 2),
    _WfFrSwDlcmiState_Type()
)
wfFrSwDlcmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiState.setStatus("mandatory")


class _WfFrSwDlcmiNniEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiNniEnable based on Integer32"""
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


_WfFrSwDlcmiNniEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiNniEnable_Object = MibTableColumn
wfFrSwDlcmiNniEnable = _WfFrSwDlcmiNniEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 3),
    _WfFrSwDlcmiNniEnable_Type()
)
wfFrSwDlcmiNniEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiNniEnable.setStatus("mandatory")
_WfFrSwDlcmiCircuit_Type = Integer32
_WfFrSwDlcmiCircuit_Object = MibTableColumn
wfFrSwDlcmiCircuit = _WfFrSwDlcmiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 4),
    _WfFrSwDlcmiCircuit_Type()
)
wfFrSwDlcmiCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCircuit.setStatus("mandatory")


class _WfFrSwDlcmiManagementType_Type(Integer32):
    """Custom type wfFrSwDlcmiManagementType based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("annexa", 5),
          ("annexaswitch", 8),
          ("annexdswitch", 7),
          ("iwfoamdisabled", 10),
          ("iwfoamenabled", 9),
          ("lmi", 2),
          ("lmiswitch", 6),
          ("none", 1),
          ("t1617b", 4),
          ("t1617d", 3))
    )


_WfFrSwDlcmiManagementType_Type.__name__ = "Integer32"
_WfFrSwDlcmiManagementType_Object = MibTableColumn
wfFrSwDlcmiManagementType = _WfFrSwDlcmiManagementType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 5),
    _WfFrSwDlcmiManagementType_Type()
)
wfFrSwDlcmiManagementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiManagementType.setStatus("mandatory")
_WfFrSwL3NetAddress_Type = IpAddress
_WfFrSwL3NetAddress_Object = MibTableColumn
wfFrSwL3NetAddress = _WfFrSwL3NetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 6),
    _WfFrSwL3NetAddress_Type()
)
wfFrSwL3NetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwL3NetAddress.setStatus("mandatory")


class _WfFrSwDlcmiAddressLen_Type(Integer32):
    """Custom type wfFrSwDlcmiAddressLen based on Integer32"""
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


_WfFrSwDlcmiAddressLen_Type.__name__ = "Integer32"
_WfFrSwDlcmiAddressLen_Object = MibTableColumn
wfFrSwDlcmiAddressLen = _WfFrSwDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 7),
    _WfFrSwDlcmiAddressLen_Type()
)
wfFrSwDlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiAddressLen.setStatus("mandatory")


class _WfFrSwDlcmiControlByteDisable_Type(Integer32):
    """Custom type wfFrSwDlcmiControlByteDisable based on Integer32"""
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


_WfFrSwDlcmiControlByteDisable_Type.__name__ = "Integer32"
_WfFrSwDlcmiControlByteDisable_Object = MibTableColumn
wfFrSwDlcmiControlByteDisable = _WfFrSwDlcmiControlByteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 8),
    _WfFrSwDlcmiControlByteDisable_Type()
)
wfFrSwDlcmiControlByteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiControlByteDisable.setStatus("mandatory")


class _WfFrSwDlcmiPollingInterval_Type(Integer32):
    """Custom type wfFrSwDlcmiPollingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfFrSwDlcmiPollingInterval_Type.__name__ = "Integer32"
_WfFrSwDlcmiPollingInterval_Object = MibTableColumn
wfFrSwDlcmiPollingInterval = _WfFrSwDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 9),
    _WfFrSwDlcmiPollingInterval_Type()
)
wfFrSwDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiPollingInterval.setStatus("mandatory")


class _WfFrSwDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type wfFrSwDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFrSwDlcmiFullEnquiryInterval_Object = MibTableColumn
wfFrSwDlcmiFullEnquiryInterval = _WfFrSwDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 10),
    _WfFrSwDlcmiFullEnquiryInterval_Type()
)
wfFrSwDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiFullEnquiryInterval.setStatus("mandatory")


class _WfFrSwDlcmiErrorThreshold_Type(Integer32):
    """Custom type wfFrSwDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3


_WfFrSwDlcmiErrorThreshold_Object = MibTableColumn
wfFrSwDlcmiErrorThreshold = _WfFrSwDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 11),
    _WfFrSwDlcmiErrorThreshold_Type()
)
wfFrSwDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiErrorThreshold.setStatus("mandatory")


class _WfFrSwDlcmiMonitoredEvents_Type(Integer32):
    """Custom type wfFrSwDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4


_WfFrSwDlcmiMonitoredEvents_Object = MibTableColumn
wfFrSwDlcmiMonitoredEvents = _WfFrSwDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 12),
    _WfFrSwDlcmiMonitoredEvents_Type()
)
wfFrSwDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiMonitoredEvents.setStatus("mandatory")
_WfFrSwDlcmiRecoveryCounts_Type = Integer32
_WfFrSwDlcmiRecoveryCounts_Object = MibTableColumn
wfFrSwDlcmiRecoveryCounts = _WfFrSwDlcmiRecoveryCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 13),
    _WfFrSwDlcmiRecoveryCounts_Type()
)
wfFrSwDlcmiRecoveryCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiRecoveryCounts.setStatus("mandatory")


class _WfFrSwDlcmiMaxSupportedVCs_Type(Integer32):
    """Custom type wfFrSwDlcmiMaxSupportedVCs based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_WfFrSwDlcmiMaxSupportedVCs_Type.__name__ = "Integer32"
_WfFrSwDlcmiMaxSupportedVCs_Object = MibTableColumn
wfFrSwDlcmiMaxSupportedVCs = _WfFrSwDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 14),
    _WfFrSwDlcmiMaxSupportedVCs_Type()
)
wfFrSwDlcmiMaxSupportedVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiMaxSupportedVCs.setStatus("mandatory")
_WfFrSwDlcmiVCsInUse_Type = Integer32
_WfFrSwDlcmiVCsInUse_Object = MibTableColumn
wfFrSwDlcmiVCsInUse = _WfFrSwDlcmiVCsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 15),
    _WfFrSwDlcmiVCsInUse_Type()
)
wfFrSwDlcmiVCsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiVCsInUse.setStatus("mandatory")
_WfFrSwSwitchHdrErrors_Type = Counter32
_WfFrSwSwitchHdrErrors_Object = MibTableColumn
wfFrSwSwitchHdrErrors = _WfFrSwSwitchHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 16),
    _WfFrSwSwitchHdrErrors_Type()
)
wfFrSwSwitchHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSwitchHdrErrors.setStatus("mandatory")


class _WfFrSwDlcmiSequenceCount_Type(Integer32):
    """Custom type wfFrSwDlcmiSequenceCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiSequenceCount_Type.__name__ = "Integer32"
_WfFrSwDlcmiSequenceCount_Object = MibTableColumn
wfFrSwDlcmiSequenceCount = _WfFrSwDlcmiSequenceCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 17),
    _WfFrSwDlcmiSequenceCount_Type()
)
wfFrSwDlcmiSequenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiSequenceCount.setStatus("mandatory")


class _WfFrSwDlcmiLastReceived_Type(Integer32):
    """Custom type wfFrSwDlcmiLastReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiLastReceived_Type.__name__ = "Integer32"
_WfFrSwDlcmiLastReceived_Object = MibTableColumn
wfFrSwDlcmiLastReceived = _WfFrSwDlcmiLastReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 18),
    _WfFrSwDlcmiLastReceived_Type()
)
wfFrSwDlcmiLastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiLastReceived.setStatus("mandatory")


class _WfFrSwDlcmiActiveSeqCount_Type(Integer32):
    """Custom type wfFrSwDlcmiActiveSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiActiveSeqCount_Type.__name__ = "Integer32"
_WfFrSwDlcmiActiveSeqCount_Object = MibTableColumn
wfFrSwDlcmiActiveSeqCount = _WfFrSwDlcmiActiveSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 19),
    _WfFrSwDlcmiActiveSeqCount_Type()
)
wfFrSwDlcmiActiveSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiActiveSeqCount.setStatus("mandatory")


class _WfFrSwDlcmiActiveReceived_Type(Integer32):
    """Custom type wfFrSwDlcmiActiveReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiActiveReceived_Type.__name__ = "Integer32"
_WfFrSwDlcmiActiveReceived_Object = MibTableColumn
wfFrSwDlcmiActiveReceived = _WfFrSwDlcmiActiveReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 20),
    _WfFrSwDlcmiActiveReceived_Type()
)
wfFrSwDlcmiActiveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiActiveReceived.setStatus("mandatory")
_WfFrSwDlcmiPolls_Type = Counter32
_WfFrSwDlcmiPolls_Object = MibTableColumn
wfFrSwDlcmiPolls = _WfFrSwDlcmiPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 21),
    _WfFrSwDlcmiPolls_Type()
)
wfFrSwDlcmiPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiPolls.setStatus("mandatory")
_WfFrSwDlcmiAlarmTimer_Type = Integer32
_WfFrSwDlcmiAlarmTimer_Object = MibTableColumn
wfFrSwDlcmiAlarmTimer = _WfFrSwDlcmiAlarmTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 22),
    _WfFrSwDlcmiAlarmTimer_Type()
)
wfFrSwDlcmiAlarmTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiAlarmTimer.setStatus("mandatory")


class _WfFrSwErrType_Type(Integer32):
    """Custom type wfFrSwErrType based on Integer32"""
    defaultValue = 1

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("byteerr", 11),
          ("formaterr", 13),
          ("hdrerr", 12),
          ("illegaldlci", 5),
          ("long", 4),
          ("other", 2),
          ("protoerr", 7),
          ("reset", 1),
          ("sequenceerr", 9),
          ("short", 3),
          ("unknowndlci", 6),
          ("unknownie", 8),
          ("unknownrpt", 10))
    )


_WfFrSwErrType_Type.__name__ = "Integer32"
_WfFrSwErrType_Object = MibTableColumn
wfFrSwErrType = _WfFrSwErrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 23),
    _WfFrSwErrType_Type()
)
wfFrSwErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwErrType.setStatus("mandatory")
_WfFrSwErrData_Type = OctetString
_WfFrSwErrData_Object = MibTableColumn
wfFrSwErrData = _WfFrSwErrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 24),
    _WfFrSwErrData_Type()
)
wfFrSwErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwErrData.setStatus("mandatory")
_WfFrSwErrTime_Type = TimeTicks
_WfFrSwErrTime_Object = MibTableColumn
wfFrSwErrTime = _WfFrSwErrTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 25),
    _WfFrSwErrTime_Type()
)
wfFrSwErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwErrTime.setStatus("mandatory")


class _WfFrSwBcMeasurementInterval_Type(Integer32):
    """Custom type wfFrSwBcMeasurementInterval based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000),
    )


_WfFrSwBcMeasurementInterval_Type.__name__ = "Integer32"
_WfFrSwBcMeasurementInterval_Object = MibTableColumn
wfFrSwBcMeasurementInterval = _WfFrSwBcMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 26),
    _WfFrSwBcMeasurementInterval_Type()
)
wfFrSwBcMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwBcMeasurementInterval.setStatus("mandatory")
_WfFrSwDlcmiMcastNoBufferErrors_Type = Counter32
_WfFrSwDlcmiMcastNoBufferErrors_Object = MibTableColumn
wfFrSwDlcmiMcastNoBufferErrors = _WfFrSwDlcmiMcastNoBufferErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 27),
    _WfFrSwDlcmiMcastNoBufferErrors_Type()
)
wfFrSwDlcmiMcastNoBufferErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiMcastNoBufferErrors.setStatus("mandatory")
_WfFrSwDlcmiFrameTooShortErrors_Type = Counter32
_WfFrSwDlcmiFrameTooShortErrors_Object = MibTableColumn
wfFrSwDlcmiFrameTooShortErrors = _WfFrSwDlcmiFrameTooShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 28),
    _WfFrSwDlcmiFrameTooShortErrors_Type()
)
wfFrSwDlcmiFrameTooShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiFrameTooShortErrors.setStatus("mandatory")
_WfFrSwDlcmiFrameTooLongErrors_Type = Counter32
_WfFrSwDlcmiFrameTooLongErrors_Object = MibTableColumn
wfFrSwDlcmiFrameTooLongErrors = _WfFrSwDlcmiFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 29),
    _WfFrSwDlcmiFrameTooLongErrors_Type()
)
wfFrSwDlcmiFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiFrameTooLongErrors.setStatus("mandatory")
_WfFrSwDlcmiIllegalDlciErrors_Type = Counter32
_WfFrSwDlcmiIllegalDlciErrors_Object = MibTableColumn
wfFrSwDlcmiIllegalDlciErrors = _WfFrSwDlcmiIllegalDlciErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 30),
    _WfFrSwDlcmiIllegalDlciErrors_Type()
)
wfFrSwDlcmiIllegalDlciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiIllegalDlciErrors.setStatus("mandatory")
_WfFrSwDlcmiUnknownDlciErrors_Type = Counter32
_WfFrSwDlcmiUnknownDlciErrors_Object = MibTableColumn
wfFrSwDlcmiUnknownDlciErrors = _WfFrSwDlcmiUnknownDlciErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 31),
    _WfFrSwDlcmiUnknownDlciErrors_Type()
)
wfFrSwDlcmiUnknownDlciErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiUnknownDlciErrors.setStatus("mandatory")
_WfFrSwDlcmiProtocolErrors_Type = Counter32
_WfFrSwDlcmiProtocolErrors_Object = MibTableColumn
wfFrSwDlcmiProtocolErrors = _WfFrSwDlcmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 32),
    _WfFrSwDlcmiProtocolErrors_Type()
)
wfFrSwDlcmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiProtocolErrors.setStatus("mandatory")
_WfFrSwDlcmiUnknownIEErrors_Type = Counter32
_WfFrSwDlcmiUnknownIEErrors_Object = MibTableColumn
wfFrSwDlcmiUnknownIEErrors = _WfFrSwDlcmiUnknownIEErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 33),
    _WfFrSwDlcmiUnknownIEErrors_Type()
)
wfFrSwDlcmiUnknownIEErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiUnknownIEErrors.setStatus("mandatory")
_WfFrSwDlcmiSequenceErrors_Type = Counter32
_WfFrSwDlcmiSequenceErrors_Object = MibTableColumn
wfFrSwDlcmiSequenceErrors = _WfFrSwDlcmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 34),
    _WfFrSwDlcmiSequenceErrors_Type()
)
wfFrSwDlcmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiSequenceErrors.setStatus("mandatory")
_WfFrSwDlcmiUnknownRPTErrors_Type = Counter32
_WfFrSwDlcmiUnknownRPTErrors_Object = MibTableColumn
wfFrSwDlcmiUnknownRPTErrors = _WfFrSwDlcmiUnknownRPTErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 35),
    _WfFrSwDlcmiUnknownRPTErrors_Type()
)
wfFrSwDlcmiUnknownRPTErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiUnknownRPTErrors.setStatus("mandatory")
_WfFrSwDlcmiControlByteErrors_Type = Counter32
_WfFrSwDlcmiControlByteErrors_Object = MibTableColumn
wfFrSwDlcmiControlByteErrors = _WfFrSwDlcmiControlByteErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 36),
    _WfFrSwDlcmiControlByteErrors_Type()
)
wfFrSwDlcmiControlByteErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiControlByteErrors.setStatus("mandatory")
_WfFrSwDlcmiFormatErrors_Type = Counter32
_WfFrSwDlcmiFormatErrors_Object = MibTableColumn
wfFrSwDlcmiFormatErrors = _WfFrSwDlcmiFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 37),
    _WfFrSwDlcmiFormatErrors_Type()
)
wfFrSwDlcmiFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiFormatErrors.setStatus("mandatory")
_WfFrSwDlcmiOtherErrors_Type = Counter32
_WfFrSwDlcmiOtherErrors_Object = MibTableColumn
wfFrSwDlcmiOtherErrors = _WfFrSwDlcmiOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 38),
    _WfFrSwDlcmiOtherErrors_Type()
)
wfFrSwDlcmiOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiOtherErrors.setStatus("mandatory")


class _WfFrSwDlcmiStatus_Type(Integer32):
    """Custom type wfFrSwDlcmiStatus based on Integer32"""
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
        *(("fault", 3),
          ("recovered", 2),
          ("running", 1),
          ("start", 4))
    )


_WfFrSwDlcmiStatus_Type.__name__ = "Integer32"
_WfFrSwDlcmiStatus_Object = MibTableColumn
wfFrSwDlcmiStatus = _WfFrSwDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 39),
    _WfFrSwDlcmiStatus_Type()
)
wfFrSwDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiStatus.setStatus("mandatory")
_WfFrSwDlcmiNewVCs_Type = Counter32
_WfFrSwDlcmiNewVCs_Object = MibTableColumn
wfFrSwDlcmiNewVCs = _WfFrSwDlcmiNewVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 40),
    _WfFrSwDlcmiNewVCs_Type()
)
wfFrSwDlcmiNewVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiNewVCs.setStatus("mandatory")
_WfFrSwDlcmiDeletedVCs_Type = Counter32
_WfFrSwDlcmiDeletedVCs_Object = MibTableColumn
wfFrSwDlcmiDeletedVCs = _WfFrSwDlcmiDeletedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 41),
    _WfFrSwDlcmiDeletedVCs_Type()
)
wfFrSwDlcmiDeletedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDeletedVCs.setStatus("mandatory")
_WfFrSwDlcmiFullStatusSeq_Type = Counter32
_WfFrSwDlcmiFullStatusSeq_Object = MibTableColumn
wfFrSwDlcmiFullStatusSeq = _WfFrSwDlcmiFullStatusSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 42),
    _WfFrSwDlcmiFullStatusSeq_Type()
)
wfFrSwDlcmiFullStatusSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiFullStatusSeq.setStatus("mandatory")


class _WfFrSwDlcmiBidirect_Type(Integer32):
    """Custom type wfFrSwDlcmiBidirect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFrSwDlcmiBidirect_Type.__name__ = "Integer32"
_WfFrSwDlcmiBidirect_Object = MibTableColumn
wfFrSwDlcmiBidirect = _WfFrSwDlcmiBidirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 43),
    _WfFrSwDlcmiBidirect_Type()
)
wfFrSwDlcmiBidirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiBidirect.setStatus("mandatory")


class _WfFrSwDlcmiDteStatus_Type(Integer32):
    """Custom type wfFrSwDlcmiDteStatus based on Integer32"""
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
        *(("fault", 3),
          ("recovered", 2),
          ("running", 1),
          ("start", 4))
    )


_WfFrSwDlcmiDteStatus_Type.__name__ = "Integer32"
_WfFrSwDlcmiDteStatus_Object = MibTableColumn
wfFrSwDlcmiDteStatus = _WfFrSwDlcmiDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 44),
    _WfFrSwDlcmiDteStatus_Type()
)
wfFrSwDlcmiDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteStatus.setStatus("mandatory")


class _WfFrSwDlcmiDteSeqCount_Type(Integer32):
    """Custom type wfFrSwDlcmiDteSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiDteSeqCount_Type.__name__ = "Integer32"
_WfFrSwDlcmiDteSeqCount_Object = MibTableColumn
wfFrSwDlcmiDteSeqCount = _WfFrSwDlcmiDteSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 45),
    _WfFrSwDlcmiDteSeqCount_Type()
)
wfFrSwDlcmiDteSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteSeqCount.setStatus("mandatory")


class _WfFrSwDlcmiDteReceived_Type(Integer32):
    """Custom type wfFrSwDlcmiDteReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiDteReceived_Type.__name__ = "Integer32"
_WfFrSwDlcmiDteReceived_Object = MibTableColumn
wfFrSwDlcmiDteReceived = _WfFrSwDlcmiDteReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 46),
    _WfFrSwDlcmiDteReceived_Type()
)
wfFrSwDlcmiDteReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteReceived.setStatus("mandatory")


class _WfFrSwDlcmiDteLastReceived_Type(Integer32):
    """Custom type wfFrSwDlcmiDteLastReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiDteLastReceived_Type.__name__ = "Integer32"
_WfFrSwDlcmiDteLastReceived_Object = MibTableColumn
wfFrSwDlcmiDteLastReceived = _WfFrSwDlcmiDteLastReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 47),
    _WfFrSwDlcmiDteLastReceived_Type()
)
wfFrSwDlcmiDteLastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteLastReceived.setStatus("mandatory")
_WfFrSwDlcmiDtePolls_Type = Counter32
_WfFrSwDlcmiDtePolls_Object = MibTableColumn
wfFrSwDlcmiDtePolls = _WfFrSwDlcmiDtePolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 48),
    _WfFrSwDlcmiDtePolls_Type()
)
wfFrSwDlcmiDtePolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDtePolls.setStatus("mandatory")


class _WfFrSwDlcmiDtePollingInterval_Type(Integer32):
    """Custom type wfFrSwDlcmiDtePollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfFrSwDlcmiDtePollingInterval_Type.__name__ = "Integer32"
_WfFrSwDlcmiDtePollingInterval_Object = MibTableColumn
wfFrSwDlcmiDtePollingInterval = _WfFrSwDlcmiDtePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 49),
    _WfFrSwDlcmiDtePollingInterval_Type()
)
wfFrSwDlcmiDtePollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDtePollingInterval.setStatus("mandatory")


class _WfFrSwDlcmiDteFullEnquiryInterval_Type(Integer32):
    """Custom type wfFrSwDlcmiDteFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrSwDlcmiDteFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFrSwDlcmiDteFullEnquiryInterval_Object = MibTableColumn
wfFrSwDlcmiDteFullEnquiryInterval = _WfFrSwDlcmiDteFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 50),
    _WfFrSwDlcmiDteFullEnquiryInterval_Type()
)
wfFrSwDlcmiDteFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteFullEnquiryInterval.setStatus("mandatory")


class _WfFrSwDlcmiDteErrorThreshold_Type(Integer32):
    """Custom type wfFrSwDlcmiDteErrorThreshold based on Integer32"""
    defaultValue = 3


_WfFrSwDlcmiDteErrorThreshold_Object = MibTableColumn
wfFrSwDlcmiDteErrorThreshold = _WfFrSwDlcmiDteErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 51),
    _WfFrSwDlcmiDteErrorThreshold_Type()
)
wfFrSwDlcmiDteErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiDteErrorThreshold.setStatus("mandatory")


class _WfFrSwDlcmiCrossNetEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiCrossNetEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFrSwDlcmiCrossNetEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiCrossNetEnable_Object = MibTableColumn
wfFrSwDlcmiCrossNetEnable = _WfFrSwDlcmiCrossNetEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 52),
    _WfFrSwDlcmiCrossNetEnable_Type()
)
wfFrSwDlcmiCrossNetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCrossNetEnable.setStatus("mandatory")


class _WfFrSwDlcmiCrossNetPollingInterval_Type(Integer32):
    """Custom type wfFrSwDlcmiCrossNetPollingInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_WfFrSwDlcmiCrossNetPollingInterval_Type.__name__ = "Integer32"
_WfFrSwDlcmiCrossNetPollingInterval_Object = MibTableColumn
wfFrSwDlcmiCrossNetPollingInterval = _WfFrSwDlcmiCrossNetPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 53),
    _WfFrSwDlcmiCrossNetPollingInterval_Type()
)
wfFrSwDlcmiCrossNetPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCrossNetPollingInterval.setStatus("mandatory")


class _WfFrSwDlcmiCrossNetErrorThreshold_Type(Integer32):
    """Custom type wfFrSwDlcmiCrossNetErrorThreshold based on Integer32"""
    defaultValue = 3


_WfFrSwDlcmiCrossNetErrorThreshold_Object = MibTableColumn
wfFrSwDlcmiCrossNetErrorThreshold = _WfFrSwDlcmiCrossNetErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 54),
    _WfFrSwDlcmiCrossNetErrorThreshold_Type()
)
wfFrSwDlcmiCrossNetErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCrossNetErrorThreshold.setStatus("mandatory")


class _WfFrSwDlcmiCrossNetAsyncUpdateEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiCrossNetAsyncUpdateEnable based on Integer32"""
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


_WfFrSwDlcmiCrossNetAsyncUpdateEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiCrossNetAsyncUpdateEnable_Object = MibTableColumn
wfFrSwDlcmiCrossNetAsyncUpdateEnable = _WfFrSwDlcmiCrossNetAsyncUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 55),
    _WfFrSwDlcmiCrossNetAsyncUpdateEnable_Type()
)
wfFrSwDlcmiCrossNetAsyncUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCrossNetAsyncUpdateEnable.setStatus("mandatory")


class _WfFrSwDlcmiBcMeasurementEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiBcMeasurementEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFrSwDlcmiBcMeasurementEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiBcMeasurementEnable_Object = MibTableColumn
wfFrSwDlcmiBcMeasurementEnable = _WfFrSwDlcmiBcMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 56),
    _WfFrSwDlcmiBcMeasurementEnable_Type()
)
wfFrSwDlcmiBcMeasurementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiBcMeasurementEnable.setStatus("mandatory")


class _WfFrSwDlcmiAsyncUpdateEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiAsyncUpdateEnable based on Integer32"""
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


_WfFrSwDlcmiAsyncUpdateEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiAsyncUpdateEnable_Object = MibTableColumn
wfFrSwDlcmiAsyncUpdateEnable = _WfFrSwDlcmiAsyncUpdateEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 57),
    _WfFrSwDlcmiAsyncUpdateEnable_Type()
)
wfFrSwDlcmiAsyncUpdateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiAsyncUpdateEnable.setStatus("mandatory")


class _WfFrSwDlcmiCrossNetListenEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiCrossNetListenEnable based on Integer32"""
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


_WfFrSwDlcmiCrossNetListenEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiCrossNetListenEnable_Object = MibTableColumn
wfFrSwDlcmiCrossNetListenEnable = _WfFrSwDlcmiCrossNetListenEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 58),
    _WfFrSwDlcmiCrossNetListenEnable_Type()
)
wfFrSwDlcmiCrossNetListenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCrossNetListenEnable.setStatus("mandatory")


class _WfFrSwDlcmiSvcDisable_Type(Integer32):
    """Custom type wfFrSwDlcmiSvcDisable based on Integer32"""
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


_WfFrSwDlcmiSvcDisable_Type.__name__ = "Integer32"
_WfFrSwDlcmiSvcDisable_Object = MibTableColumn
wfFrSwDlcmiSvcDisable = _WfFrSwDlcmiSvcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 59),
    _WfFrSwDlcmiSvcDisable_Type()
)
wfFrSwDlcmiSvcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiSvcDisable.setStatus("mandatory")


class _WfFrSwDlcmiL2AddrType_Type(Integer32):
    """Custom type wfFrSwDlcmiL2AddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 2))
    )


_WfFrSwDlcmiL2AddrType_Type.__name__ = "Integer32"
_WfFrSwDlcmiL2AddrType_Object = MibTableColumn
wfFrSwDlcmiL2AddrType = _WfFrSwDlcmiL2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 60),
    _WfFrSwDlcmiL2AddrType_Type()
)
wfFrSwDlcmiL2AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiL2AddrType.setStatus("mandatory")


class _WfFrSwDlcmiEscapeMode_Type(Integer32):
    """Custom type wfFrSwDlcmiEscapeMode based on Integer32"""
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
        *(("disabled", 1),
          ("egress", 3),
          ("ingress", 2))
    )


_WfFrSwDlcmiEscapeMode_Type.__name__ = "Integer32"
_WfFrSwDlcmiEscapeMode_Object = MibTableColumn
wfFrSwDlcmiEscapeMode = _WfFrSwDlcmiEscapeMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 61),
    _WfFrSwDlcmiEscapeMode_Type()
)
wfFrSwDlcmiEscapeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiEscapeMode.setStatus("mandatory")
_WfFrSwDlcmiEscapeCircuit_Type = Integer32
_WfFrSwDlcmiEscapeCircuit_Object = MibTableColumn
wfFrSwDlcmiEscapeCircuit = _WfFrSwDlcmiEscapeCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 62),
    _WfFrSwDlcmiEscapeCircuit_Type()
)
wfFrSwDlcmiEscapeCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiEscapeCircuit.setStatus("mandatory")


class _WfFrSwDlcmiEscapeVcCount_Type(Integer32):
    """Custom type wfFrSwDlcmiEscapeVcCount based on Integer32"""
    defaultValue = 0


_WfFrSwDlcmiEscapeVcCount_Object = MibTableColumn
wfFrSwDlcmiEscapeVcCount = _WfFrSwDlcmiEscapeVcCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 63),
    _WfFrSwDlcmiEscapeVcCount_Type()
)
wfFrSwDlcmiEscapeVcCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiEscapeVcCount.setStatus("mandatory")


class _WfFrSwDlcmiIwfMode_Type(Integer32):
    """Custom type wfFrSwDlcmiIwfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sdlc2frsw", 2))
    )


_WfFrSwDlcmiIwfMode_Type.__name__ = "Integer32"
_WfFrSwDlcmiIwfMode_Object = MibTableColumn
wfFrSwDlcmiIwfMode = _WfFrSwDlcmiIwfMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 64),
    _WfFrSwDlcmiIwfMode_Type()
)
wfFrSwDlcmiIwfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiIwfMode.setStatus("mandatory")


class _WfFrSwDlcmiSvcBillingEnable_Type(Integer32):
    """Custom type wfFrSwDlcmiSvcBillingEnable based on Integer32"""
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


_WfFrSwDlcmiSvcBillingEnable_Type.__name__ = "Integer32"
_WfFrSwDlcmiSvcBillingEnable_Object = MibTableColumn
wfFrSwDlcmiSvcBillingEnable = _WfFrSwDlcmiSvcBillingEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 65),
    _WfFrSwDlcmiSvcBillingEnable_Type()
)
wfFrSwDlcmiSvcBillingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiSvcBillingEnable.setStatus("mandatory")


class _WfFrSwDlcmiSpvcAgent_Type(Integer32):
    """Custom type wfFrSwDlcmiSpvcAgent based on Integer32"""
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
        *(("caa", 3),
          ("cra", 2),
          ("craandcaa", 4),
          ("none", 1))
    )


_WfFrSwDlcmiSpvcAgent_Type.__name__ = "Integer32"
_WfFrSwDlcmiSpvcAgent_Object = MibTableColumn
wfFrSwDlcmiSpvcAgent = _WfFrSwDlcmiSpvcAgent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 66),
    _WfFrSwDlcmiSpvcAgent_Type()
)
wfFrSwDlcmiSpvcAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiSpvcAgent.setStatus("mandatory")


class _WfFrSwDlcmiCallAccDlciSelectionType_Type(Integer32):
    """Custom type wfFrSwDlcmiCallAccDlciSelectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_WfFrSwDlcmiCallAccDlciSelectionType_Type.__name__ = "Integer32"
_WfFrSwDlcmiCallAccDlciSelectionType_Object = MibTableColumn
wfFrSwDlcmiCallAccDlciSelectionType = _WfFrSwDlcmiCallAccDlciSelectionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 1, 1, 67),
    _WfFrSwDlcmiCallAccDlciSelectionType_Type()
)
wfFrSwDlcmiCallAccDlciSelectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwDlcmiCallAccDlciSelectionType.setStatus("mandatory")
_WfFrSwCctTable_Object = MibTable
wfFrSwCctTable = _WfFrSwCctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2)
)
if mibBuilder.loadTexts:
    wfFrSwCctTable.setStatus("obsolete")
_WfFrSwCctEntry_Object = MibTableRow
wfFrSwCctEntry = _WfFrSwCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1)
)
wfFrSwCctEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwCctNumber"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwCctDlci"),
)
if mibBuilder.loadTexts:
    wfFrSwCctEntry.setStatus("obsolete")


class _WfFrSwCctDelete_Type(Integer32):
    """Custom type wfFrSwCctDelete based on Integer32"""
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


_WfFrSwCctDelete_Type.__name__ = "Integer32"
_WfFrSwCctDelete_Object = MibTableColumn
wfFrSwCctDelete = _WfFrSwCctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 1),
    _WfFrSwCctDelete_Type()
)
wfFrSwCctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctDelete.setStatus("obsolete")
_WfFrSwCctNumber_Type = Integer32
_WfFrSwCctNumber_Object = MibTableColumn
wfFrSwCctNumber = _WfFrSwCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 2),
    _WfFrSwCctNumber_Type()
)
wfFrSwCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctNumber.setStatus("obsolete")


class _WfFrSwCctDlci_Type(Integer32):
    """Custom type wfFrSwCctDlci based on Integer32"""
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


_WfFrSwCctDlci_Type.__name__ = "Integer32"
_WfFrSwCctDlci_Object = MibTableColumn
wfFrSwCctDlci = _WfFrSwCctDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 3),
    _WfFrSwCctDlci_Type()
)
wfFrSwCctDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctDlci.setStatus("obsolete")


class _WfFrSwCctState_Type(Integer32):
    """Custom type wfFrSwCctState based on Integer32"""
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
          ("control", 4),
          ("inactive", 3),
          ("invalid", 1),
          ("user", 5))
    )


_WfFrSwCctState_Type.__name__ = "Integer32"
_WfFrSwCctState_Object = MibTableColumn
wfFrSwCctState = _WfFrSwCctState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 4),
    _WfFrSwCctState_Type()
)
wfFrSwCctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctState.setStatus("obsolete")


class _WfFrSwCctMulticast_Type(Integer32):
    """Custom type wfFrSwCctMulticast based on Integer32"""
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


_WfFrSwCctMulticast_Type.__name__ = "Integer32"
_WfFrSwCctMulticast_Object = MibTableColumn
wfFrSwCctMulticast = _WfFrSwCctMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 5),
    _WfFrSwCctMulticast_Type()
)
wfFrSwCctMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctMulticast.setStatus("obsolete")
_WfFrSwCctInBc_Type = Integer32
_WfFrSwCctInBc_Object = MibTableColumn
wfFrSwCctInBc = _WfFrSwCctInBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 6),
    _WfFrSwCctInBc_Type()
)
wfFrSwCctInBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctInBc.setStatus("obsolete")
_WfFrSwCctOutBc_Type = Integer32
_WfFrSwCctOutBc_Object = MibTableColumn
wfFrSwCctOutBc = _WfFrSwCctOutBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 7),
    _WfFrSwCctOutBc_Type()
)
wfFrSwCctOutBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctOutBc.setStatus("obsolete")
_WfFrSwCctInBe_Type = Integer32
_WfFrSwCctInBe_Object = MibTableColumn
wfFrSwCctInBe = _WfFrSwCctInBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 8),
    _WfFrSwCctInBe_Type()
)
wfFrSwCctInBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctInBe.setStatus("obsolete")
_WfFrSwCctOutBe_Type = Integer32
_WfFrSwCctOutBe_Object = MibTableColumn
wfFrSwCctOutBe = _WfFrSwCctOutBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 9),
    _WfFrSwCctOutBe_Type()
)
wfFrSwCctOutBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctOutBe.setStatus("obsolete")
_WfFrSwCctInThroughput_Type = Integer32
_WfFrSwCctInThroughput_Object = MibTableColumn
wfFrSwCctInThroughput = _WfFrSwCctInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 10),
    _WfFrSwCctInThroughput_Type()
)
wfFrSwCctInThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctInThroughput.setStatus("obsolete")
_WfFrSwCctOutThroughput_Type = Integer32
_WfFrSwCctOutThroughput_Object = MibTableColumn
wfFrSwCctOutThroughput = _WfFrSwCctOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 11),
    _WfFrSwCctOutThroughput_Type()
)
wfFrSwCctOutThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctOutThroughput.setStatus("obsolete")
_WfFrSwCctCreationTime_Type = TimeTicks
_WfFrSwCctCreationTime_Object = MibTableColumn
wfFrSwCctCreationTime = _WfFrSwCctCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 12),
    _WfFrSwCctCreationTime_Type()
)
wfFrSwCctCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctCreationTime.setStatus("obsolete")
_WfFrSwCctLastTimeChange_Type = TimeTicks
_WfFrSwCctLastTimeChange_Object = MibTableColumn
wfFrSwCctLastTimeChange = _WfFrSwCctLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 13),
    _WfFrSwCctLastTimeChange_Type()
)
wfFrSwCctLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLastTimeChange.setStatus("obsolete")
_WfFrSwCctLocalSentNonDEFrames_Type = Counter32
_WfFrSwCctLocalSentNonDEFrames_Object = MibTableColumn
wfFrSwCctLocalSentNonDEFrames = _WfFrSwCctLocalSentNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 14),
    _WfFrSwCctLocalSentNonDEFrames_Type()
)
wfFrSwCctLocalSentNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSentNonDEFrames.setStatus("obsolete")
_WfFrSwCctLocalSentNonDEOctets_Type = Counter32
_WfFrSwCctLocalSentNonDEOctets_Object = MibTableColumn
wfFrSwCctLocalSentNonDEOctets = _WfFrSwCctLocalSentNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 15),
    _WfFrSwCctLocalSentNonDEOctets_Type()
)
wfFrSwCctLocalSentNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSentNonDEOctets.setStatus("obsolete")
_WfFrSwCctLocalSentDEFrames_Type = Counter32
_WfFrSwCctLocalSentDEFrames_Object = MibTableColumn
wfFrSwCctLocalSentDEFrames = _WfFrSwCctLocalSentDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 16),
    _WfFrSwCctLocalSentDEFrames_Type()
)
wfFrSwCctLocalSentDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSentDEFrames.setStatus("obsolete")
_WfFrSwCctLocalSentDEOctets_Type = Counter32
_WfFrSwCctLocalSentDEOctets_Object = MibTableColumn
wfFrSwCctLocalSentDEOctets = _WfFrSwCctLocalSentDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 17),
    _WfFrSwCctLocalSentDEOctets_Type()
)
wfFrSwCctLocalSentDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSentDEOctets.setStatus("obsolete")
_WfFrSwCctLocalSetFECNFrames_Type = Counter32
_WfFrSwCctLocalSetFECNFrames_Object = MibTableColumn
wfFrSwCctLocalSetFECNFrames = _WfFrSwCctLocalSetFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 18),
    _WfFrSwCctLocalSetFECNFrames_Type()
)
wfFrSwCctLocalSetFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetFECNFrames.setStatus("obsolete")
_WfFrSwCctLocalSetFECNOctets_Type = Counter32
_WfFrSwCctLocalSetFECNOctets_Object = MibTableColumn
wfFrSwCctLocalSetFECNOctets = _WfFrSwCctLocalSetFECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 19),
    _WfFrSwCctLocalSetFECNOctets_Type()
)
wfFrSwCctLocalSetFECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetFECNOctets.setStatus("obsolete")
_WfFrSwCctLocalSetBECNFrames_Type = Counter32
_WfFrSwCctLocalSetBECNFrames_Object = MibTableColumn
wfFrSwCctLocalSetBECNFrames = _WfFrSwCctLocalSetBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 20),
    _WfFrSwCctLocalSetBECNFrames_Type()
)
wfFrSwCctLocalSetBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetBECNFrames.setStatus("obsolete")
_WfFrSwCctLocalSetBECNOctets_Type = Counter32
_WfFrSwCctLocalSetBECNOctets_Object = MibTableColumn
wfFrSwCctLocalSetBECNOctets = _WfFrSwCctLocalSetBECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 21),
    _WfFrSwCctLocalSetBECNOctets_Type()
)
wfFrSwCctLocalSetBECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetBECNOctets.setStatus("obsolete")
_WfFrSwCctLocalSetDEFrames_Type = Counter32
_WfFrSwCctLocalSetDEFrames_Object = MibTableColumn
wfFrSwCctLocalSetDEFrames = _WfFrSwCctLocalSetDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 22),
    _WfFrSwCctLocalSetDEFrames_Type()
)
wfFrSwCctLocalSetDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetDEFrames.setStatus("obsolete")
_WfFrSwCctLocalSetDEOctets_Type = Counter32
_WfFrSwCctLocalSetDEOctets_Object = MibTableColumn
wfFrSwCctLocalSetDEOctets = _WfFrSwCctLocalSetDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 23),
    _WfFrSwCctLocalSetDEOctets_Type()
)
wfFrSwCctLocalSetDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalSetDEOctets.setStatus("obsolete")
_WfFrSwCctLocalDropNonDEFrames_Type = Counter32
_WfFrSwCctLocalDropNonDEFrames_Object = MibTableColumn
wfFrSwCctLocalDropNonDEFrames = _WfFrSwCctLocalDropNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 24),
    _WfFrSwCctLocalDropNonDEFrames_Type()
)
wfFrSwCctLocalDropNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalDropNonDEFrames.setStatus("obsolete")
_WfFrSwCctLocalDropNonDEOctets_Type = Counter32
_WfFrSwCctLocalDropNonDEOctets_Object = MibTableColumn
wfFrSwCctLocalDropNonDEOctets = _WfFrSwCctLocalDropNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 25),
    _WfFrSwCctLocalDropNonDEOctets_Type()
)
wfFrSwCctLocalDropNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalDropNonDEOctets.setStatus("obsolete")
_WfFrSwCctLocalDropDEFrames_Type = Counter32
_WfFrSwCctLocalDropDEFrames_Object = MibTableColumn
wfFrSwCctLocalDropDEFrames = _WfFrSwCctLocalDropDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 26),
    _WfFrSwCctLocalDropDEFrames_Type()
)
wfFrSwCctLocalDropDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalDropDEFrames.setStatus("obsolete")
_WfFrSwCctLocalDropDEOctets_Type = Counter32
_WfFrSwCctLocalDropDEOctets_Object = MibTableColumn
wfFrSwCctLocalDropDEOctets = _WfFrSwCctLocalDropDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 27),
    _WfFrSwCctLocalDropDEOctets_Type()
)
wfFrSwCctLocalDropDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalDropDEOctets.setStatus("obsolete")
_WfFrSwCctInactiveVCDropFrames_Type = Counter32
_WfFrSwCctInactiveVCDropFrames_Object = MibTableColumn
wfFrSwCctInactiveVCDropFrames = _WfFrSwCctInactiveVCDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 28),
    _WfFrSwCctInactiveVCDropFrames_Type()
)
wfFrSwCctInactiveVCDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctInactiveVCDropFrames.setStatus("obsolete")
_WfFrSwCctInactiveVCDropOctets_Type = Counter32
_WfFrSwCctInactiveVCDropOctets_Object = MibTableColumn
wfFrSwCctInactiveVCDropOctets = _WfFrSwCctInactiveVCDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 29),
    _WfFrSwCctInactiveVCDropOctets_Type()
)
wfFrSwCctInactiveVCDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctInactiveVCDropOctets.setStatus("obsolete")
_WfFrSwCctLocalRecvNonDEFrames_Type = Counter32
_WfFrSwCctLocalRecvNonDEFrames_Object = MibTableColumn
wfFrSwCctLocalRecvNonDEFrames = _WfFrSwCctLocalRecvNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 30),
    _WfFrSwCctLocalRecvNonDEFrames_Type()
)
wfFrSwCctLocalRecvNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvNonDEFrames.setStatus("obsolete")
_WfFrSwCctLocalRecvNonDEOctets_Type = Counter32
_WfFrSwCctLocalRecvNonDEOctets_Object = MibTableColumn
wfFrSwCctLocalRecvNonDEOctets = _WfFrSwCctLocalRecvNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 31),
    _WfFrSwCctLocalRecvNonDEOctets_Type()
)
wfFrSwCctLocalRecvNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvNonDEOctets.setStatus("obsolete")
_WfFrSwCctLocalRecvDEFrames_Type = Counter32
_WfFrSwCctLocalRecvDEFrames_Object = MibTableColumn
wfFrSwCctLocalRecvDEFrames = _WfFrSwCctLocalRecvDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 32),
    _WfFrSwCctLocalRecvDEFrames_Type()
)
wfFrSwCctLocalRecvDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvDEFrames.setStatus("obsolete")
_WfFrSwCctLocalRecvDEOctets_Type = Counter32
_WfFrSwCctLocalRecvDEOctets_Object = MibTableColumn
wfFrSwCctLocalRecvDEOctets = _WfFrSwCctLocalRecvDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 33),
    _WfFrSwCctLocalRecvDEOctets_Type()
)
wfFrSwCctLocalRecvDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvDEOctets.setStatus("obsolete")
_WfFrSwCctLocalRecvFECNFrames_Type = Counter32
_WfFrSwCctLocalRecvFECNFrames_Object = MibTableColumn
wfFrSwCctLocalRecvFECNFrames = _WfFrSwCctLocalRecvFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 34),
    _WfFrSwCctLocalRecvFECNFrames_Type()
)
wfFrSwCctLocalRecvFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvFECNFrames.setStatus("obsolete")
_WfFrSwCctLocalRecvFECNOctets_Type = Counter32
_WfFrSwCctLocalRecvFECNOctets_Object = MibTableColumn
wfFrSwCctLocalRecvFECNOctets = _WfFrSwCctLocalRecvFECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 35),
    _WfFrSwCctLocalRecvFECNOctets_Type()
)
wfFrSwCctLocalRecvFECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvFECNOctets.setStatus("obsolete")
_WfFrSwCctLocalRecvBECNFrames_Type = Counter32
_WfFrSwCctLocalRecvBECNFrames_Object = MibTableColumn
wfFrSwCctLocalRecvBECNFrames = _WfFrSwCctLocalRecvBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 36),
    _WfFrSwCctLocalRecvBECNFrames_Type()
)
wfFrSwCctLocalRecvBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvBECNFrames.setStatus("obsolete")
_WfFrSwCctLocalRecvBECNOctets_Type = Counter32
_WfFrSwCctLocalRecvBECNOctets_Object = MibTableColumn
wfFrSwCctLocalRecvBECNOctets = _WfFrSwCctLocalRecvBECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 37),
    _WfFrSwCctLocalRecvBECNOctets_Type()
)
wfFrSwCctLocalRecvBECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecvBECNOctets.setStatus("obsolete")
_WfFrSwCctLocalRecentNonDEOctets_Type = Counter32
_WfFrSwCctLocalRecentNonDEOctets_Object = MibTableColumn
wfFrSwCctLocalRecentNonDEOctets = _WfFrSwCctLocalRecentNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 38),
    _WfFrSwCctLocalRecentNonDEOctets_Type()
)
wfFrSwCctLocalRecentNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalRecentNonDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteSentNonDEFrames_Type = Counter32
_WfFrSwCctRemoteSentNonDEFrames_Object = MibTableColumn
wfFrSwCctRemoteSentNonDEFrames = _WfFrSwCctRemoteSentNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 39),
    _WfFrSwCctRemoteSentNonDEFrames_Type()
)
wfFrSwCctRemoteSentNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSentNonDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteSentNonDEOctets_Type = Counter32
_WfFrSwCctRemoteSentNonDEOctets_Object = MibTableColumn
wfFrSwCctRemoteSentNonDEOctets = _WfFrSwCctRemoteSentNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 40),
    _WfFrSwCctRemoteSentNonDEOctets_Type()
)
wfFrSwCctRemoteSentNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSentNonDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteSentDEFrames_Type = Counter32
_WfFrSwCctRemoteSentDEFrames_Object = MibTableColumn
wfFrSwCctRemoteSentDEFrames = _WfFrSwCctRemoteSentDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 41),
    _WfFrSwCctRemoteSentDEFrames_Type()
)
wfFrSwCctRemoteSentDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSentDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteSentDEOctets_Type = Counter32
_WfFrSwCctRemoteSentDEOctets_Object = MibTableColumn
wfFrSwCctRemoteSentDEOctets = _WfFrSwCctRemoteSentDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 42),
    _WfFrSwCctRemoteSentDEOctets_Type()
)
wfFrSwCctRemoteSentDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSentDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteSetFECNFrames_Type = Counter32
_WfFrSwCctRemoteSetFECNFrames_Object = MibTableColumn
wfFrSwCctRemoteSetFECNFrames = _WfFrSwCctRemoteSetFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 43),
    _WfFrSwCctRemoteSetFECNFrames_Type()
)
wfFrSwCctRemoteSetFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSetFECNFrames.setStatus("obsolete")
_WfFrSwCctRemoteSetFECNOctets_Type = Counter32
_WfFrSwCctRemoteSetFECNOctets_Object = MibTableColumn
wfFrSwCctRemoteSetFECNOctets = _WfFrSwCctRemoteSetFECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 44),
    _WfFrSwCctRemoteSetFECNOctets_Type()
)
wfFrSwCctRemoteSetFECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSetFECNOctets.setStatus("obsolete")
_WfFrSwCctRemoteSetBECNFrames_Type = Counter32
_WfFrSwCctRemoteSetBECNFrames_Object = MibTableColumn
wfFrSwCctRemoteSetBECNFrames = _WfFrSwCctRemoteSetBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 45),
    _WfFrSwCctRemoteSetBECNFrames_Type()
)
wfFrSwCctRemoteSetBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSetBECNFrames.setStatus("obsolete")
_WfFrSwCctRemoteSetBECNOctets_Type = Counter32
_WfFrSwCctRemoteSetBECNOctets_Object = MibTableColumn
wfFrSwCctRemoteSetBECNOctets = _WfFrSwCctRemoteSetBECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 46),
    _WfFrSwCctRemoteSetBECNOctets_Type()
)
wfFrSwCctRemoteSetBECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteSetBECNOctets.setStatus("obsolete")
_WfFrSwCctRemoteDropNonDEFrames_Type = Counter32
_WfFrSwCctRemoteDropNonDEFrames_Object = MibTableColumn
wfFrSwCctRemoteDropNonDEFrames = _WfFrSwCctRemoteDropNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 47),
    _WfFrSwCctRemoteDropNonDEFrames_Type()
)
wfFrSwCctRemoteDropNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteDropNonDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteDropNonDEOctets_Type = Counter32
_WfFrSwCctRemoteDropNonDEOctets_Object = MibTableColumn
wfFrSwCctRemoteDropNonDEOctets = _WfFrSwCctRemoteDropNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 48),
    _WfFrSwCctRemoteDropNonDEOctets_Type()
)
wfFrSwCctRemoteDropNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteDropNonDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteDropDEFrames_Type = Counter32
_WfFrSwCctRemoteDropDEFrames_Object = MibTableColumn
wfFrSwCctRemoteDropDEFrames = _WfFrSwCctRemoteDropDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 49),
    _WfFrSwCctRemoteDropDEFrames_Type()
)
wfFrSwCctRemoteDropDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteDropDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteDropDEOctets_Type = Counter32
_WfFrSwCctRemoteDropDEOctets_Object = MibTableColumn
wfFrSwCctRemoteDropDEOctets = _WfFrSwCctRemoteDropDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 50),
    _WfFrSwCctRemoteDropDEOctets_Type()
)
wfFrSwCctRemoteDropDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteDropDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteRecvNonDEFrames_Type = Counter32
_WfFrSwCctRemoteRecvNonDEFrames_Object = MibTableColumn
wfFrSwCctRemoteRecvNonDEFrames = _WfFrSwCctRemoteRecvNonDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 51),
    _WfFrSwCctRemoteRecvNonDEFrames_Type()
)
wfFrSwCctRemoteRecvNonDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvNonDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteRecvNonDEOctets_Type = Counter32
_WfFrSwCctRemoteRecvNonDEOctets_Object = MibTableColumn
wfFrSwCctRemoteRecvNonDEOctets = _WfFrSwCctRemoteRecvNonDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 52),
    _WfFrSwCctRemoteRecvNonDEOctets_Type()
)
wfFrSwCctRemoteRecvNonDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvNonDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteRecvDEFrames_Type = Counter32
_WfFrSwCctRemoteRecvDEFrames_Object = MibTableColumn
wfFrSwCctRemoteRecvDEFrames = _WfFrSwCctRemoteRecvDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 53),
    _WfFrSwCctRemoteRecvDEFrames_Type()
)
wfFrSwCctRemoteRecvDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvDEFrames.setStatus("obsolete")
_WfFrSwCctRemoteRecvDEOctets_Type = Counter32
_WfFrSwCctRemoteRecvDEOctets_Object = MibTableColumn
wfFrSwCctRemoteRecvDEOctets = _WfFrSwCctRemoteRecvDEOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 54),
    _WfFrSwCctRemoteRecvDEOctets_Type()
)
wfFrSwCctRemoteRecvDEOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvDEOctets.setStatus("obsolete")
_WfFrSwCctRemoteRecvFECNFrames_Type = Counter32
_WfFrSwCctRemoteRecvFECNFrames_Object = MibTableColumn
wfFrSwCctRemoteRecvFECNFrames = _WfFrSwCctRemoteRecvFECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 55),
    _WfFrSwCctRemoteRecvFECNFrames_Type()
)
wfFrSwCctRemoteRecvFECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvFECNFrames.setStatus("obsolete")
_WfFrSwCctRemoteRecvFECNOctets_Type = Counter32
_WfFrSwCctRemoteRecvFECNOctets_Object = MibTableColumn
wfFrSwCctRemoteRecvFECNOctets = _WfFrSwCctRemoteRecvFECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 56),
    _WfFrSwCctRemoteRecvFECNOctets_Type()
)
wfFrSwCctRemoteRecvFECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvFECNOctets.setStatus("obsolete")
_WfFrSwCctRemoteRecvBECNFrames_Type = Counter32
_WfFrSwCctRemoteRecvBECNFrames_Object = MibTableColumn
wfFrSwCctRemoteRecvBECNFrames = _WfFrSwCctRemoteRecvBECNFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 57),
    _WfFrSwCctRemoteRecvBECNFrames_Type()
)
wfFrSwCctRemoteRecvBECNFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvBECNFrames.setStatus("obsolete")
_WfFrSwCctRemoteRecvBECNOctets_Type = Counter32
_WfFrSwCctRemoteRecvBECNOctets_Object = MibTableColumn
wfFrSwCctRemoteRecvBECNOctets = _WfFrSwCctRemoteRecvBECNOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 58),
    _WfFrSwCctRemoteRecvBECNOctets_Type()
)
wfFrSwCctRemoteRecvBECNOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteRecvBECNOctets.setStatus("obsolete")
_WfFrSwCctLocalBecnState_Type = Integer32
_WfFrSwCctLocalBecnState_Object = MibTableColumn
wfFrSwCctLocalBecnState = _WfFrSwCctLocalBecnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 59),
    _WfFrSwCctLocalBecnState_Type()
)
wfFrSwCctLocalBecnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalBecnState.setStatus("obsolete")
_WfFrSwCctRemoteBecnState_Type = Integer32
_WfFrSwCctRemoteBecnState_Object = MibTableColumn
wfFrSwCctRemoteBecnState = _WfFrSwCctRemoteBecnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 60),
    _WfFrSwCctRemoteBecnState_Type()
)
wfFrSwCctRemoteBecnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctRemoteBecnState.setStatus("obsolete")


class _WfFrSwCctLocalOrRemoteConnection_Type(Integer32):
    """Custom type wfFrSwCctLocalOrRemoteConnection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_WfFrSwCctLocalOrRemoteConnection_Type.__name__ = "Integer32"
_WfFrSwCctLocalOrRemoteConnection_Object = MibTableColumn
wfFrSwCctLocalOrRemoteConnection = _WfFrSwCctLocalOrRemoteConnection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 61),
    _WfFrSwCctLocalOrRemoteConnection_Type()
)
wfFrSwCctLocalOrRemoteConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctLocalOrRemoteConnection.setStatus("obsolete")
_WfFrSwCctInBcOctets_Type = Integer32
_WfFrSwCctInBcOctets_Object = MibTableColumn
wfFrSwCctInBcOctets = _WfFrSwCctInBcOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 62),
    _WfFrSwCctInBcOctets_Type()
)
wfFrSwCctInBcOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctInBcOctets.setStatus("obsolete")


class _WfFrSwCctStateSet_Type(Integer32):
    """Custom type wfFrSwCctStateSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwCctStateSet_Type.__name__ = "Integer32"
_WfFrSwCctStateSet_Object = MibTableColumn
wfFrSwCctStateSet = _WfFrSwCctStateSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 63),
    _WfFrSwCctStateSet_Type()
)
wfFrSwCctStateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCctStateSet.setStatus("obsolete")


class _WfFrSwCctReportedStatus_Type(Integer32):
    """Custom type wfFrSwCctReportedStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acked", 1),
          ("unacked", 2),
          ("unreported", 3))
    )


_WfFrSwCctReportedStatus_Type.__name__ = "Integer32"
_WfFrSwCctReportedStatus_Object = MibTableColumn
wfFrSwCctReportedStatus = _WfFrSwCctReportedStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 64),
    _WfFrSwCctReportedStatus_Type()
)
wfFrSwCctReportedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctReportedStatus.setStatus("obsolete")


class _WfFrSwCctReceivedStatus_Type(Integer32):
    """Custom type wfFrSwCctReceivedStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwCctReceivedStatus_Type.__name__ = "Integer32"
_WfFrSwCctReceivedStatus_Object = MibTableColumn
wfFrSwCctReceivedStatus = _WfFrSwCctReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 65),
    _WfFrSwCctReceivedStatus_Type()
)
wfFrSwCctReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctReceivedStatus.setStatus("obsolete")


class _WfFrSwCctCrossNetStatus_Type(Integer32):
    """Custom type wfFrSwCctCrossNetStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwCctCrossNetStatus_Type.__name__ = "Integer32"
_WfFrSwCctCrossNetStatus_Object = MibTableColumn
wfFrSwCctCrossNetStatus = _WfFrSwCctCrossNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 66),
    _WfFrSwCctCrossNetStatus_Type()
)
wfFrSwCctCrossNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctCrossNetStatus.setStatus("obsolete")


class _WfFrSwCctXNetSent_Type(Integer32):
    """Custom type wfFrSwCctXNetSent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sent", 2),
          ("unsent", 1))
    )


_WfFrSwCctXNetSent_Type.__name__ = "Integer32"
_WfFrSwCctXNetSent_Object = MibTableColumn
wfFrSwCctXNetSent = _WfFrSwCctXNetSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 67),
    _WfFrSwCctXNetSent_Type()
)
wfFrSwCctXNetSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctXNetSent.setStatus("obsolete")


class _WfFrSwCctXNetReceived_Type(Integer32):
    """Custom type wfFrSwCctXNetReceived based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recv", 1),
          ("unrecv", 2))
    )


_WfFrSwCctXNetReceived_Type.__name__ = "Integer32"
_WfFrSwCctXNetReceived_Object = MibTableColumn
wfFrSwCctXNetReceived = _WfFrSwCctXNetReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 68),
    _WfFrSwCctXNetReceived_Type()
)
wfFrSwCctXNetReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctXNetReceived.setStatus("obsolete")
_WfFrSwCctXNetErrors_Type = Counter32
_WfFrSwCctXNetErrors_Object = MibTableColumn
wfFrSwCctXNetErrors = _WfFrSwCctXNetErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 2, 1, 69),
    _WfFrSwCctXNetErrors_Type()
)
wfFrSwCctXNetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCctXNetErrors.setStatus("obsolete")
_WfFrSwTupleTable_Object = MibTable
wfFrSwTupleTable = _WfFrSwTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3)
)
if mibBuilder.loadTexts:
    wfFrSwTupleTable.setStatus("obsolete")
_WfFrSwTupleEntry_Object = MibTableRow
wfFrSwTupleEntry = _WfFrSwTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1)
)
wfFrSwTupleEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwTupleIpAddrA"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwTupleDlciA"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwTupleIpAddrB"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwTupleDlciB"),
)
if mibBuilder.loadTexts:
    wfFrSwTupleEntry.setStatus("obsolete")


class _WfFrSwTupleDelete_Type(Integer32):
    """Custom type wfFrSwTupleDelete based on Integer32"""
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


_WfFrSwTupleDelete_Type.__name__ = "Integer32"
_WfFrSwTupleDelete_Object = MibTableColumn
wfFrSwTupleDelete = _WfFrSwTupleDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1, 1),
    _WfFrSwTupleDelete_Type()
)
wfFrSwTupleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwTupleDelete.setStatus("obsolete")
_WfFrSwTupleIpAddrA_Type = IpAddress
_WfFrSwTupleIpAddrA_Object = MibTableColumn
wfFrSwTupleIpAddrA = _WfFrSwTupleIpAddrA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1, 2),
    _WfFrSwTupleIpAddrA_Type()
)
wfFrSwTupleIpAddrA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwTupleIpAddrA.setStatus("obsolete")
_WfFrSwTupleDlciA_Type = Integer32
_WfFrSwTupleDlciA_Object = MibTableColumn
wfFrSwTupleDlciA = _WfFrSwTupleDlciA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1, 3),
    _WfFrSwTupleDlciA_Type()
)
wfFrSwTupleDlciA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwTupleDlciA.setStatus("obsolete")
_WfFrSwTupleIpAddrB_Type = IpAddress
_WfFrSwTupleIpAddrB_Object = MibTableColumn
wfFrSwTupleIpAddrB = _WfFrSwTupleIpAddrB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1, 4),
    _WfFrSwTupleIpAddrB_Type()
)
wfFrSwTupleIpAddrB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwTupleIpAddrB.setStatus("obsolete")
_WfFrSwTupleDlciB_Type = Integer32
_WfFrSwTupleDlciB_Object = MibTableColumn
wfFrSwTupleDlciB = _WfFrSwTupleDlciB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 3, 1, 5),
    _WfFrSwTupleDlciB_Type()
)
wfFrSwTupleDlciB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwTupleDlciB.setStatus("obsolete")
_WfFrSwMcastTable_Object = MibTable
wfFrSwMcastTable = _WfFrSwMcastTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4)
)
if mibBuilder.loadTexts:
    wfFrSwMcastTable.setStatus("mandatory")
_WfFrSwMcastEntry_Object = MibTableRow
wfFrSwMcastEntry = _WfFrSwMcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1)
)
wfFrSwMcastEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwMcastIndex"),
)
if mibBuilder.loadTexts:
    wfFrSwMcastEntry.setStatus("mandatory")


class _WfFrSwMcastDelete_Type(Integer32):
    """Custom type wfFrSwMcastDelete based on Integer32"""
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


_WfFrSwMcastDelete_Type.__name__ = "Integer32"
_WfFrSwMcastDelete_Object = MibTableColumn
wfFrSwMcastDelete = _WfFrSwMcastDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1, 1),
    _WfFrSwMcastDelete_Type()
)
wfFrSwMcastDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwMcastDelete.setStatus("mandatory")
_WfFrSwMcastIndex_Type = Integer32
_WfFrSwMcastIndex_Object = MibTableColumn
wfFrSwMcastIndex = _WfFrSwMcastIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1, 2),
    _WfFrSwMcastIndex_Type()
)
wfFrSwMcastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwMcastIndex.setStatus("mandatory")
_WfFrSwMcastIpAddr_Type = IpAddress
_WfFrSwMcastIpAddr_Object = MibTableColumn
wfFrSwMcastIpAddr = _WfFrSwMcastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1, 3),
    _WfFrSwMcastIpAddr_Type()
)
wfFrSwMcastIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwMcastIpAddr.setStatus("mandatory")
_WfFrSwMcastDlci_Type = Integer32
_WfFrSwMcastDlci_Object = MibTableColumn
wfFrSwMcastDlci = _WfFrSwMcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1, 4),
    _WfFrSwMcastDlci_Type()
)
wfFrSwMcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwMcastDlci.setStatus("mandatory")
_WfFrSwMcastIndividualDlci_Type = Integer32
_WfFrSwMcastIndividualDlci_Object = MibTableColumn
wfFrSwMcastIndividualDlci = _WfFrSwMcastIndividualDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 4, 1, 5),
    _WfFrSwMcastIndividualDlci_Type()
)
wfFrSwMcastIndividualDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwMcastIndividualDlci.setStatus("mandatory")
_WfFrSwUsage_ObjectIdentity = ObjectIdentity
wfFrSwUsage = _WfFrSwUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5)
)


class _WfFrSwUsageEnable_Type(Integer32):
    """Custom type wfFrSwUsageEnable based on Integer32"""
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


_WfFrSwUsageEnable_Type.__name__ = "Integer32"
_WfFrSwUsageEnable_Object = MibScalar
wfFrSwUsageEnable = _WfFrSwUsageEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 1),
    _WfFrSwUsageEnable_Type()
)
wfFrSwUsageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageEnable.setStatus("mandatory")


class _WfFrSwUsageVolume_Type(Integer32):
    """Custom type wfFrSwUsageVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwUsageVolume_Type.__name__ = "Integer32"
_WfFrSwUsageVolume_Object = MibScalar
wfFrSwUsageVolume = _WfFrSwUsageVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 2),
    _WfFrSwUsageVolume_Type()
)
wfFrSwUsageVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageVolume.setStatus("mandatory")


class _WfFrSwUsageVolumeBackup_Type(Integer32):
    """Custom type wfFrSwUsageVolumeBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwUsageVolumeBackup_Type.__name__ = "Integer32"
_WfFrSwUsageVolumeBackup_Object = MibScalar
wfFrSwUsageVolumeBackup = _WfFrSwUsageVolumeBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 3),
    _WfFrSwUsageVolumeBackup_Type()
)
wfFrSwUsageVolumeBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageVolumeBackup.setStatus("mandatory")
_WfFrSwUsageDirectory_Type = DisplayString
_WfFrSwUsageDirectory_Object = MibScalar
wfFrSwUsageDirectory = _WfFrSwUsageDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 4),
    _WfFrSwUsageDirectory_Type()
)
wfFrSwUsageDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageDirectory.setStatus("mandatory")
_WfFrSwUsageFilePrefix_Type = DisplayString
_WfFrSwUsageFilePrefix_Object = MibScalar
wfFrSwUsageFilePrefix = _WfFrSwUsageFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 5),
    _WfFrSwUsageFilePrefix_Type()
)
wfFrSwUsageFilePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageFilePrefix.setStatus("mandatory")


class _WfFrSwUsageTimerInterval_Type(Integer32):
    """Custom type wfFrSwUsageTimerInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfFrSwUsageTimerInterval_Type.__name__ = "Integer32"
_WfFrSwUsageTimerInterval_Object = MibScalar
wfFrSwUsageTimerInterval = _WfFrSwUsageTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 6),
    _WfFrSwUsageTimerInterval_Type()
)
wfFrSwUsageTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageTimerInterval.setStatus("mandatory")


class _WfFrSwUsageUpdateInterval_Type(Integer32):
    """Custom type wfFrSwUsageUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageUpdateInterval_Type.__name__ = "Integer32"
_WfFrSwUsageUpdateInterval_Object = MibScalar
wfFrSwUsageUpdateInterval = _WfFrSwUsageUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 7),
    _WfFrSwUsageUpdateInterval_Type()
)
wfFrSwUsageUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageUpdateInterval.setStatus("mandatory")


class _WfFrSwUsageStoreInterval_Type(Integer32):
    """Custom type wfFrSwUsageStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageStoreInterval_Type.__name__ = "Integer32"
_WfFrSwUsageStoreInterval_Object = MibScalar
wfFrSwUsageStoreInterval = _WfFrSwUsageStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 8),
    _WfFrSwUsageStoreInterval_Type()
)
wfFrSwUsageStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageStoreInterval.setStatus("mandatory")


class _WfFrSwUsageFlushInterval_Type(Integer32):
    """Custom type wfFrSwUsageFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageFlushInterval_Type.__name__ = "Integer32"
_WfFrSwUsageFlushInterval_Object = MibScalar
wfFrSwUsageFlushInterval = _WfFrSwUsageFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 9),
    _WfFrSwUsageFlushInterval_Type()
)
wfFrSwUsageFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageFlushInterval.setStatus("mandatory")


class _WfFrSwUsageCleanupInterval_Type(Integer32):
    """Custom type wfFrSwUsageCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageCleanupInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCleanupInterval_Object = MibScalar
wfFrSwUsageCleanupInterval = _WfFrSwUsageCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 10),
    _WfFrSwUsageCleanupInterval_Type()
)
wfFrSwUsageCleanupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageCleanupInterval.setStatus("mandatory")
_WfFrSwUsageLocalTimeZone_Type = Integer32
_WfFrSwUsageLocalTimeZone_Object = MibScalar
wfFrSwUsageLocalTimeZone = _WfFrSwUsageLocalTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 11),
    _WfFrSwUsageLocalTimeZone_Type()
)
wfFrSwUsageLocalTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLocalTimeZone.setStatus("mandatory")
_WfFrSwUsageUpdateTimeStamp_Type = TimeTicks
_WfFrSwUsageUpdateTimeStamp_Object = MibScalar
wfFrSwUsageUpdateTimeStamp = _WfFrSwUsageUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 12),
    _WfFrSwUsageUpdateTimeStamp_Type()
)
wfFrSwUsageUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageUpdateTimeStamp.setStatus("mandatory")
_WfFrSwUsageStoreTimeStamp_Type = TimeTicks
_WfFrSwUsageStoreTimeStamp_Object = MibScalar
wfFrSwUsageStoreTimeStamp = _WfFrSwUsageStoreTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 13),
    _WfFrSwUsageStoreTimeStamp_Type()
)
wfFrSwUsageStoreTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageStoreTimeStamp.setStatus("mandatory")
_WfFrSwUsageFlushTimeStamp_Type = TimeTicks
_WfFrSwUsageFlushTimeStamp_Object = MibScalar
wfFrSwUsageFlushTimeStamp = _WfFrSwUsageFlushTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 14),
    _WfFrSwUsageFlushTimeStamp_Type()
)
wfFrSwUsageFlushTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageFlushTimeStamp.setStatus("mandatory")
_WfFrSwUsageCleanupTimeStamp_Type = TimeTicks
_WfFrSwUsageCleanupTimeStamp_Object = MibScalar
wfFrSwUsageCleanupTimeStamp = _WfFrSwUsageCleanupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 15),
    _WfFrSwUsageCleanupTimeStamp_Type()
)
wfFrSwUsageCleanupTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCleanupTimeStamp.setStatus("mandatory")
_WfFrSwUsageUpdateData_Type = Integer32
_WfFrSwUsageUpdateData_Object = MibScalar
wfFrSwUsageUpdateData = _WfFrSwUsageUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 16),
    _WfFrSwUsageUpdateData_Type()
)
wfFrSwUsageUpdateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageUpdateData.setStatus("mandatory")
_WfFrSwUsageStoreData_Type = Integer32
_WfFrSwUsageStoreData_Object = MibScalar
wfFrSwUsageStoreData = _WfFrSwUsageStoreData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 17),
    _WfFrSwUsageStoreData_Type()
)
wfFrSwUsageStoreData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageStoreData.setStatus("mandatory")
_WfFrSwUsageFlushData_Type = Integer32
_WfFrSwUsageFlushData_Object = MibScalar
wfFrSwUsageFlushData = _WfFrSwUsageFlushData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 18),
    _WfFrSwUsageFlushData_Type()
)
wfFrSwUsageFlushData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageFlushData.setStatus("mandatory")
_WfFrSwUsageFileCleanup_Type = Integer32
_WfFrSwUsageFileCleanup_Object = MibScalar
wfFrSwUsageFileCleanup = _WfFrSwUsageFileCleanup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 19),
    _WfFrSwUsageFileCleanup_Type()
)
wfFrSwUsageFileCleanup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageFileCleanup.setStatus("mandatory")


class _WfFrSwUsageState_Type(Integer32):
    """Custom type wfFrSwUsageState based on Integer32"""
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


_WfFrSwUsageState_Type.__name__ = "Integer32"
_WfFrSwUsageState_Object = MibScalar
wfFrSwUsageState = _WfFrSwUsageState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 20),
    _WfFrSwUsageState_Type()
)
wfFrSwUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageState.setStatus("mandatory")


class _WfFrSwUsageCurVolume_Type(Integer32):
    """Custom type wfFrSwUsageCurVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwUsageCurVolume_Type.__name__ = "Integer32"
_WfFrSwUsageCurVolume_Object = MibScalar
wfFrSwUsageCurVolume = _WfFrSwUsageCurVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 21),
    _WfFrSwUsageCurVolume_Type()
)
wfFrSwUsageCurVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurVolume.setStatus("mandatory")


class _WfFrSwUsageCurVolumeBackup_Type(Integer32):
    """Custom type wfFrSwUsageCurVolumeBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwUsageCurVolumeBackup_Type.__name__ = "Integer32"
_WfFrSwUsageCurVolumeBackup_Object = MibScalar
wfFrSwUsageCurVolumeBackup = _WfFrSwUsageCurVolumeBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 22),
    _WfFrSwUsageCurVolumeBackup_Type()
)
wfFrSwUsageCurVolumeBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurVolumeBackup.setStatus("mandatory")
_WfFrSwUsageCurDirectory_Type = DisplayString
_WfFrSwUsageCurDirectory_Object = MibScalar
wfFrSwUsageCurDirectory = _WfFrSwUsageCurDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 23),
    _WfFrSwUsageCurDirectory_Type()
)
wfFrSwUsageCurDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurDirectory.setStatus("mandatory")
_WfFrSwUsageCurFilePrefix_Type = DisplayString
_WfFrSwUsageCurFilePrefix_Object = MibScalar
wfFrSwUsageCurFilePrefix = _WfFrSwUsageCurFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 24),
    _WfFrSwUsageCurFilePrefix_Type()
)
wfFrSwUsageCurFilePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurFilePrefix.setStatus("mandatory")


class _WfFrSwUsageCurTimerInterval_Type(Integer32):
    """Custom type wfFrSwUsageCurTimerInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfFrSwUsageCurTimerInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCurTimerInterval_Object = MibScalar
wfFrSwUsageCurTimerInterval = _WfFrSwUsageCurTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 25),
    _WfFrSwUsageCurTimerInterval_Type()
)
wfFrSwUsageCurTimerInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurTimerInterval.setStatus("mandatory")


class _WfFrSwUsageCurUpdateInterval_Type(Integer32):
    """Custom type wfFrSwUsageCurUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageCurUpdateInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCurUpdateInterval_Object = MibScalar
wfFrSwUsageCurUpdateInterval = _WfFrSwUsageCurUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 26),
    _WfFrSwUsageCurUpdateInterval_Type()
)
wfFrSwUsageCurUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurUpdateInterval.setStatus("mandatory")


class _WfFrSwUsageCurStoreInterval_Type(Integer32):
    """Custom type wfFrSwUsageCurStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageCurStoreInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCurStoreInterval_Object = MibScalar
wfFrSwUsageCurStoreInterval = _WfFrSwUsageCurStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 27),
    _WfFrSwUsageCurStoreInterval_Type()
)
wfFrSwUsageCurStoreInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurStoreInterval.setStatus("mandatory")


class _WfFrSwUsageCurFlushInterval_Type(Integer32):
    """Custom type wfFrSwUsageCurFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageCurFlushInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCurFlushInterval_Object = MibScalar
wfFrSwUsageCurFlushInterval = _WfFrSwUsageCurFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 28),
    _WfFrSwUsageCurFlushInterval_Type()
)
wfFrSwUsageCurFlushInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurFlushInterval.setStatus("mandatory")


class _WfFrSwUsageCurCleanupInterval_Type(Integer32):
    """Custom type wfFrSwUsageCurCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwUsageCurCleanupInterval_Type.__name__ = "Integer32"
_WfFrSwUsageCurCleanupInterval_Object = MibScalar
wfFrSwUsageCurCleanupInterval = _WfFrSwUsageCurCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 29),
    _WfFrSwUsageCurCleanupInterval_Type()
)
wfFrSwUsageCurCleanupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurCleanupInterval.setStatus("mandatory")


class _WfFrSwUsageDebug_Type(Integer32):
    """Custom type wfFrSwUsageDebug based on Integer32"""
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


_WfFrSwUsageDebug_Type.__name__ = "Integer32"
_WfFrSwUsageDebug_Object = MibScalar
wfFrSwUsageDebug = _WfFrSwUsageDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 30),
    _WfFrSwUsageDebug_Type()
)
wfFrSwUsageDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageDebug.setStatus("mandatory")


class _WfFrSwUsageCurDebug_Type(Integer32):
    """Custom type wfFrSwUsageCurDebug based on Integer32"""
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


_WfFrSwUsageCurDebug_Type.__name__ = "Integer32"
_WfFrSwUsageCurDebug_Object = MibScalar
wfFrSwUsageCurDebug = _WfFrSwUsageCurDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 31),
    _WfFrSwUsageCurDebug_Type()
)
wfFrSwUsageCurDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCurDebug.setStatus("mandatory")
_WfFrSwUsageSwitchId_Type = Integer32
_WfFrSwUsageSwitchId_Object = MibScalar
wfFrSwUsageSwitchId = _WfFrSwUsageSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 32),
    _WfFrSwUsageSwitchId_Type()
)
wfFrSwUsageSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSwitchId.setStatus("mandatory")
_WfFrSwUsageNumEntries_Type = Integer32
_WfFrSwUsageNumEntries_Object = MibScalar
wfFrSwUsageNumEntries = _WfFrSwUsageNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 33),
    _WfFrSwUsageNumEntries_Type()
)
wfFrSwUsageNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageNumEntries.setStatus("mandatory")


class _WfFrSwSvcUsageEnable_Type(Integer32):
    """Custom type wfFrSwSvcUsageEnable based on Integer32"""
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


_WfFrSwSvcUsageEnable_Type.__name__ = "Integer32"
_WfFrSwSvcUsageEnable_Object = MibScalar
wfFrSwSvcUsageEnable = _WfFrSwSvcUsageEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 34),
    _WfFrSwSvcUsageEnable_Type()
)
wfFrSwSvcUsageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageEnable.setStatus("mandatory")


class _WfFrSwSvcUsageInterimRecordEnable_Type(Integer32):
    """Custom type wfFrSwSvcUsageInterimRecordEnable based on Integer32"""
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


_WfFrSwSvcUsageInterimRecordEnable_Type.__name__ = "Integer32"
_WfFrSwSvcUsageInterimRecordEnable_Object = MibScalar
wfFrSwSvcUsageInterimRecordEnable = _WfFrSwSvcUsageInterimRecordEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 35),
    _WfFrSwSvcUsageInterimRecordEnable_Type()
)
wfFrSwSvcUsageInterimRecordEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageInterimRecordEnable.setStatus("mandatory")


class _WfFrSwSvcUsageVolume_Type(Integer32):
    """Custom type wfFrSwSvcUsageVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwSvcUsageVolume_Type.__name__ = "Integer32"
_WfFrSwSvcUsageVolume_Object = MibScalar
wfFrSwSvcUsageVolume = _WfFrSwSvcUsageVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 36),
    _WfFrSwSvcUsageVolume_Type()
)
wfFrSwSvcUsageVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageVolume.setStatus("mandatory")
_WfFrSwSvcUsageDirectory_Type = DisplayString
_WfFrSwSvcUsageDirectory_Object = MibScalar
wfFrSwSvcUsageDirectory = _WfFrSwSvcUsageDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 37),
    _WfFrSwSvcUsageDirectory_Type()
)
wfFrSwSvcUsageDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageDirectory.setStatus("mandatory")
_WfFrSwSvcUsageFilePrefix_Type = DisplayString
_WfFrSwSvcUsageFilePrefix_Object = MibScalar
wfFrSwSvcUsageFilePrefix = _WfFrSwSvcUsageFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 38),
    _WfFrSwSvcUsageFilePrefix_Type()
)
wfFrSwSvcUsageFilePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFilePrefix.setStatus("mandatory")


class _WfFrSwSvcUsageUpdateInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageUpdateInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageUpdateInterval_Object = MibScalar
wfFrSwSvcUsageUpdateInterval = _WfFrSwSvcUsageUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 39),
    _WfFrSwSvcUsageUpdateInterval_Type()
)
wfFrSwSvcUsageUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageUpdateInterval.setStatus("mandatory")


class _WfFrSwSvcUsageStoreInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageStoreInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageStoreInterval_Object = MibScalar
wfFrSwSvcUsageStoreInterval = _WfFrSwSvcUsageStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 40),
    _WfFrSwSvcUsageStoreInterval_Type()
)
wfFrSwSvcUsageStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageStoreInterval.setStatus("mandatory")


class _WfFrSwSvcUsageFlushInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageFlushInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageFlushInterval_Object = MibScalar
wfFrSwSvcUsageFlushInterval = _WfFrSwSvcUsageFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 41),
    _WfFrSwSvcUsageFlushInterval_Type()
)
wfFrSwSvcUsageFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFlushInterval.setStatus("mandatory")


class _WfFrSwSvcUsageCleanupInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageCleanupInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCleanupInterval_Object = MibScalar
wfFrSwSvcUsageCleanupInterval = _WfFrSwSvcUsageCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 42),
    _WfFrSwSvcUsageCleanupInterval_Type()
)
wfFrSwSvcUsageCleanupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCleanupInterval.setStatus("mandatory")
_WfFrSwSvcUsageUpdateTimeStamp_Type = TimeTicks
_WfFrSwSvcUsageUpdateTimeStamp_Object = MibScalar
wfFrSwSvcUsageUpdateTimeStamp = _WfFrSwSvcUsageUpdateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 43),
    _WfFrSwSvcUsageUpdateTimeStamp_Type()
)
wfFrSwSvcUsageUpdateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageUpdateTimeStamp.setStatus("mandatory")
_WfFrSwSvcUsageStoreTimeStamp_Type = TimeTicks
_WfFrSwSvcUsageStoreTimeStamp_Object = MibScalar
wfFrSwSvcUsageStoreTimeStamp = _WfFrSwSvcUsageStoreTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 44),
    _WfFrSwSvcUsageStoreTimeStamp_Type()
)
wfFrSwSvcUsageStoreTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageStoreTimeStamp.setStatus("mandatory")
_WfFrSwSvcUsageFlushTimeStamp_Type = TimeTicks
_WfFrSwSvcUsageFlushTimeStamp_Object = MibScalar
wfFrSwSvcUsageFlushTimeStamp = _WfFrSwSvcUsageFlushTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 45),
    _WfFrSwSvcUsageFlushTimeStamp_Type()
)
wfFrSwSvcUsageFlushTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFlushTimeStamp.setStatus("mandatory")
_WfFrSwSvcUsageCleanupTimeStamp_Type = TimeTicks
_WfFrSwSvcUsageCleanupTimeStamp_Object = MibScalar
wfFrSwSvcUsageCleanupTimeStamp = _WfFrSwSvcUsageCleanupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 46),
    _WfFrSwSvcUsageCleanupTimeStamp_Type()
)
wfFrSwSvcUsageCleanupTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCleanupTimeStamp.setStatus("mandatory")
_WfFrSwSvcUsageUpdateData_Type = Integer32
_WfFrSwSvcUsageUpdateData_Object = MibScalar
wfFrSwSvcUsageUpdateData = _WfFrSwSvcUsageUpdateData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 47),
    _WfFrSwSvcUsageUpdateData_Type()
)
wfFrSwSvcUsageUpdateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageUpdateData.setStatus("mandatory")
_WfFrSwSvcUsageStoreData_Type = Integer32
_WfFrSwSvcUsageStoreData_Object = MibScalar
wfFrSwSvcUsageStoreData = _WfFrSwSvcUsageStoreData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 48),
    _WfFrSwSvcUsageStoreData_Type()
)
wfFrSwSvcUsageStoreData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageStoreData.setStatus("mandatory")
_WfFrSwSvcUsageFlushData_Type = Integer32
_WfFrSwSvcUsageFlushData_Object = MibScalar
wfFrSwSvcUsageFlushData = _WfFrSwSvcUsageFlushData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 49),
    _WfFrSwSvcUsageFlushData_Type()
)
wfFrSwSvcUsageFlushData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFlushData.setStatus("mandatory")
_WfFrSwSvcUsageFileCleanup_Type = Integer32
_WfFrSwSvcUsageFileCleanup_Object = MibScalar
wfFrSwSvcUsageFileCleanup = _WfFrSwSvcUsageFileCleanup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 50),
    _WfFrSwSvcUsageFileCleanup_Type()
)
wfFrSwSvcUsageFileCleanup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFileCleanup.setStatus("mandatory")


class _WfFrSwSvcUsageState_Type(Integer32):
    """Custom type wfFrSwSvcUsageState based on Integer32"""
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


_WfFrSwSvcUsageState_Type.__name__ = "Integer32"
_WfFrSwSvcUsageState_Object = MibScalar
wfFrSwSvcUsageState = _WfFrSwSvcUsageState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 51),
    _WfFrSwSvcUsageState_Type()
)
wfFrSwSvcUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageState.setStatus("mandatory")


class _WfFrSwSvcUsageCurVolume_Type(Integer32):
    """Custom type wfFrSwSvcUsageCurVolume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfFrSwSvcUsageCurVolume_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCurVolume_Object = MibScalar
wfFrSwSvcUsageCurVolume = _WfFrSwSvcUsageCurVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 52),
    _WfFrSwSvcUsageCurVolume_Type()
)
wfFrSwSvcUsageCurVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurVolume.setStatus("mandatory")
_WfFrSwSvcUsageCurDirectory_Type = DisplayString
_WfFrSwSvcUsageCurDirectory_Object = MibScalar
wfFrSwSvcUsageCurDirectory = _WfFrSwSvcUsageCurDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 53),
    _WfFrSwSvcUsageCurDirectory_Type()
)
wfFrSwSvcUsageCurDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurDirectory.setStatus("mandatory")
_WfFrSwSvcUsageCurFilePrefix_Type = DisplayString
_WfFrSwSvcUsageCurFilePrefix_Object = MibScalar
wfFrSwSvcUsageCurFilePrefix = _WfFrSwSvcUsageCurFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 54),
    _WfFrSwSvcUsageCurFilePrefix_Type()
)
wfFrSwSvcUsageCurFilePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurFilePrefix.setStatus("mandatory")


class _WfFrSwSvcUsageCurUpdateInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageCurUpdateInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageCurUpdateInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCurUpdateInterval_Object = MibScalar
wfFrSwSvcUsageCurUpdateInterval = _WfFrSwSvcUsageCurUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 55),
    _WfFrSwSvcUsageCurUpdateInterval_Type()
)
wfFrSwSvcUsageCurUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurUpdateInterval.setStatus("mandatory")


class _WfFrSwSvcUsageCurStoreInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageCurStoreInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageCurStoreInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCurStoreInterval_Object = MibScalar
wfFrSwSvcUsageCurStoreInterval = _WfFrSwSvcUsageCurStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 56),
    _WfFrSwSvcUsageCurStoreInterval_Type()
)
wfFrSwSvcUsageCurStoreInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurStoreInterval.setStatus("mandatory")


class _WfFrSwSvcUsageCurFlushInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageCurFlushInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageCurFlushInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCurFlushInterval_Object = MibScalar
wfFrSwSvcUsageCurFlushInterval = _WfFrSwSvcUsageCurFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 57),
    _WfFrSwSvcUsageCurFlushInterval_Type()
)
wfFrSwSvcUsageCurFlushInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurFlushInterval.setStatus("mandatory")


class _WfFrSwSvcUsageCurCleanupInterval_Type(Integer32):
    """Custom type wfFrSwSvcUsageCurCleanupInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrSwSvcUsageCurCleanupInterval_Type.__name__ = "Integer32"
_WfFrSwSvcUsageCurCleanupInterval_Object = MibScalar
wfFrSwSvcUsageCurCleanupInterval = _WfFrSwSvcUsageCurCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 58),
    _WfFrSwSvcUsageCurCleanupInterval_Type()
)
wfFrSwSvcUsageCurCleanupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageCurCleanupInterval.setStatus("mandatory")
_WfFrSwSvcUsageNumEntries_Type = Integer32
_WfFrSwSvcUsageNumEntries_Object = MibScalar
wfFrSwSvcUsageNumEntries = _WfFrSwSvcUsageNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 59),
    _WfFrSwSvcUsageNumEntries_Type()
)
wfFrSwSvcUsageNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageNumEntries.setStatus("mandatory")
_WfFrSwSvcUsageVersionId_Type = Integer32
_WfFrSwSvcUsageVersionId_Object = MibScalar
wfFrSwSvcUsageVersionId = _WfFrSwSvcUsageVersionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 60),
    _WfFrSwSvcUsageVersionId_Type()
)
wfFrSwSvcUsageVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageVersionId.setStatus("mandatory")
_WfFrSwUsageSwitchName_Type = DisplayString
_WfFrSwUsageSwitchName_Object = MibScalar
wfFrSwUsageSwitchName = _WfFrSwUsageSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 61),
    _WfFrSwUsageSwitchName_Type()
)
wfFrSwUsageSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwUsageSwitchName.setStatus("mandatory")
_WfFrSwPvcUsageFileLayout_Type = Integer32
_WfFrSwPvcUsageFileLayout_Object = MibScalar
wfFrSwPvcUsageFileLayout = _WfFrSwPvcUsageFileLayout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 62),
    _WfFrSwPvcUsageFileLayout_Type()
)
wfFrSwPvcUsageFileLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwPvcUsageFileLayout.setStatus("mandatory")
_WfFrSwSvcUsageFileLayout_Type = Integer32
_WfFrSwSvcUsageFileLayout_Object = MibScalar
wfFrSwSvcUsageFileLayout = _WfFrSwSvcUsageFileLayout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 5, 63),
    _WfFrSwSvcUsageFileLayout_Type()
)
wfFrSwSvcUsageFileLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSvcUsageFileLayout.setStatus("mandatory")
_WfFrSwUsageTable_Object = MibTable
wfFrSwUsageTable = _WfFrSwUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6)
)
if mibBuilder.loadTexts:
    wfFrSwUsageTable.setStatus("obsolete")
_WfFrSwUsageEntry_Object = MibTableRow
wfFrSwUsageEntry = _WfFrSwUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1)
)
wfFrSwUsageEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwUsageCircuitNumber"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwUsageDlci"),
)
if mibBuilder.loadTexts:
    wfFrSwUsageEntry.setStatus("obsolete")


class _WfFrSwUsageDelete_Type(Integer32):
    """Custom type wfFrSwUsageDelete based on Integer32"""
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


_WfFrSwUsageDelete_Type.__name__ = "Integer32"
_WfFrSwUsageDelete_Object = MibTableColumn
wfFrSwUsageDelete = _WfFrSwUsageDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 1),
    _WfFrSwUsageDelete_Type()
)
wfFrSwUsageDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageDelete.setStatus("obsolete")
_WfFrSwUsageCircuitNumber_Type = Integer32
_WfFrSwUsageCircuitNumber_Object = MibTableColumn
wfFrSwUsageCircuitNumber = _WfFrSwUsageCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 2),
    _WfFrSwUsageCircuitNumber_Type()
)
wfFrSwUsageCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageCircuitNumber.setStatus("obsolete")


class _WfFrSwUsageDlci_Type(Integer32):
    """Custom type wfFrSwUsageDlci based on Integer32"""
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


_WfFrSwUsageDlci_Type.__name__ = "Integer32"
_WfFrSwUsageDlci_Object = MibTableColumn
wfFrSwUsageDlci = _WfFrSwUsageDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 3),
    _WfFrSwUsageDlci_Type()
)
wfFrSwUsageDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageDlci.setStatus("obsolete")
_WfFrSwUsageIPAddress_Type = IpAddress
_WfFrSwUsageIPAddress_Object = MibTableColumn
wfFrSwUsageIPAddress = _WfFrSwUsageIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 4),
    _WfFrSwUsageIPAddress_Type()
)
wfFrSwUsageIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageIPAddress.setStatus("obsolete")
_WfFrSwUsageStartTimeStampHigh_Type = Integer32
_WfFrSwUsageStartTimeStampHigh_Object = MibTableColumn
wfFrSwUsageStartTimeStampHigh = _WfFrSwUsageStartTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 5),
    _WfFrSwUsageStartTimeStampHigh_Type()
)
wfFrSwUsageStartTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageStartTimeStampHigh.setStatus("obsolete")
_WfFrSwUsageStartTimeStampLow_Type = Integer32
_WfFrSwUsageStartTimeStampLow_Object = MibTableColumn
wfFrSwUsageStartTimeStampLow = _WfFrSwUsageStartTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 6),
    _WfFrSwUsageStartTimeStampLow_Type()
)
wfFrSwUsageStartTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageStartTimeStampLow.setStatus("obsolete")
_WfFrSwUsageEndTimeStampHigh_Type = Integer32
_WfFrSwUsageEndTimeStampHigh_Object = MibTableColumn
wfFrSwUsageEndTimeStampHigh = _WfFrSwUsageEndTimeStampHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 7),
    _WfFrSwUsageEndTimeStampHigh_Type()
)
wfFrSwUsageEndTimeStampHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageEndTimeStampHigh.setStatus("obsolete")
_WfFrSwUsageEndTimeStampLow_Type = Integer32
_WfFrSwUsageEndTimeStampLow_Object = MibTableColumn
wfFrSwUsageEndTimeStampLow = _WfFrSwUsageEndTimeStampLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 8),
    _WfFrSwUsageEndTimeStampLow_Type()
)
wfFrSwUsageEndTimeStampLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageEndTimeStampLow.setStatus("obsolete")
_WfFrSwUsageSentNonDEFramesHigh_Type = Integer32
_WfFrSwUsageSentNonDEFramesHigh_Object = MibTableColumn
wfFrSwUsageSentNonDEFramesHigh = _WfFrSwUsageSentNonDEFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 9),
    _WfFrSwUsageSentNonDEFramesHigh_Type()
)
wfFrSwUsageSentNonDEFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentNonDEFramesHigh.setStatus("obsolete")
_WfFrSwUsageSentNonDEFramesLow_Type = Integer32
_WfFrSwUsageSentNonDEFramesLow_Object = MibTableColumn
wfFrSwUsageSentNonDEFramesLow = _WfFrSwUsageSentNonDEFramesLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 10),
    _WfFrSwUsageSentNonDEFramesLow_Type()
)
wfFrSwUsageSentNonDEFramesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentNonDEFramesLow.setStatus("obsolete")
_WfFrSwUsageSentNonDEOctetsHigh_Type = Integer32
_WfFrSwUsageSentNonDEOctetsHigh_Object = MibTableColumn
wfFrSwUsageSentNonDEOctetsHigh = _WfFrSwUsageSentNonDEOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 11),
    _WfFrSwUsageSentNonDEOctetsHigh_Type()
)
wfFrSwUsageSentNonDEOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentNonDEOctetsHigh.setStatus("obsolete")
_WfFrSwUsageSentNonDEOctetsLow_Type = Integer32
_WfFrSwUsageSentNonDEOctetsLow_Object = MibTableColumn
wfFrSwUsageSentNonDEOctetsLow = _WfFrSwUsageSentNonDEOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 12),
    _WfFrSwUsageSentNonDEOctetsLow_Type()
)
wfFrSwUsageSentNonDEOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentNonDEOctetsLow.setStatus("obsolete")
_WfFrSwUsageSentDEFramesHigh_Type = Integer32
_WfFrSwUsageSentDEFramesHigh_Object = MibTableColumn
wfFrSwUsageSentDEFramesHigh = _WfFrSwUsageSentDEFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 13),
    _WfFrSwUsageSentDEFramesHigh_Type()
)
wfFrSwUsageSentDEFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentDEFramesHigh.setStatus("obsolete")
_WfFrSwUsageSentDEFramesLow_Type = Integer32
_WfFrSwUsageSentDEFramesLow_Object = MibTableColumn
wfFrSwUsageSentDEFramesLow = _WfFrSwUsageSentDEFramesLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 14),
    _WfFrSwUsageSentDEFramesLow_Type()
)
wfFrSwUsageSentDEFramesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentDEFramesLow.setStatus("obsolete")
_WfFrSwUsageSentDEOctetsHigh_Type = Integer32
_WfFrSwUsageSentDEOctetsHigh_Object = MibTableColumn
wfFrSwUsageSentDEOctetsHigh = _WfFrSwUsageSentDEOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 15),
    _WfFrSwUsageSentDEOctetsHigh_Type()
)
wfFrSwUsageSentDEOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentDEOctetsHigh.setStatus("obsolete")
_WfFrSwUsageSentDEOctetsLow_Type = Integer32
_WfFrSwUsageSentDEOctetsLow_Object = MibTableColumn
wfFrSwUsageSentDEOctetsLow = _WfFrSwUsageSentDEOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 16),
    _WfFrSwUsageSentDEOctetsLow_Type()
)
wfFrSwUsageSentDEOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageSentDEOctetsLow.setStatus("obsolete")
_WfFrSwUsageLastNonDEFramesHigh_Type = Integer32
_WfFrSwUsageLastNonDEFramesHigh_Object = MibTableColumn
wfFrSwUsageLastNonDEFramesHigh = _WfFrSwUsageLastNonDEFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 17),
    _WfFrSwUsageLastNonDEFramesHigh_Type()
)
wfFrSwUsageLastNonDEFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastNonDEFramesHigh.setStatus("obsolete")
_WfFrSwUsageLastNonDEFramesLow_Type = Integer32
_WfFrSwUsageLastNonDEFramesLow_Object = MibTableColumn
wfFrSwUsageLastNonDEFramesLow = _WfFrSwUsageLastNonDEFramesLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 18),
    _WfFrSwUsageLastNonDEFramesLow_Type()
)
wfFrSwUsageLastNonDEFramesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastNonDEFramesLow.setStatus("obsolete")
_WfFrSwUsageLastNonDEOctetsHigh_Type = Integer32
_WfFrSwUsageLastNonDEOctetsHigh_Object = MibTableColumn
wfFrSwUsageLastNonDEOctetsHigh = _WfFrSwUsageLastNonDEOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 19),
    _WfFrSwUsageLastNonDEOctetsHigh_Type()
)
wfFrSwUsageLastNonDEOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastNonDEOctetsHigh.setStatus("obsolete")
_WfFrSwUsageLastNonDEOctetsLow_Type = Integer32
_WfFrSwUsageLastNonDEOctetsLow_Object = MibTableColumn
wfFrSwUsageLastNonDEOctetsLow = _WfFrSwUsageLastNonDEOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 20),
    _WfFrSwUsageLastNonDEOctetsLow_Type()
)
wfFrSwUsageLastNonDEOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastNonDEOctetsLow.setStatus("obsolete")
_WfFrSwUsageLastDEFramesHigh_Type = Integer32
_WfFrSwUsageLastDEFramesHigh_Object = MibTableColumn
wfFrSwUsageLastDEFramesHigh = _WfFrSwUsageLastDEFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 21),
    _WfFrSwUsageLastDEFramesHigh_Type()
)
wfFrSwUsageLastDEFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastDEFramesHigh.setStatus("obsolete")
_WfFrSwUsageLastDEFramesLow_Type = Integer32
_WfFrSwUsageLastDEFramesLow_Object = MibTableColumn
wfFrSwUsageLastDEFramesLow = _WfFrSwUsageLastDEFramesLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 22),
    _WfFrSwUsageLastDEFramesLow_Type()
)
wfFrSwUsageLastDEFramesLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastDEFramesLow.setStatus("obsolete")
_WfFrSwUsageLastDEOctetsHigh_Type = Integer32
_WfFrSwUsageLastDEOctetsHigh_Object = MibTableColumn
wfFrSwUsageLastDEOctetsHigh = _WfFrSwUsageLastDEOctetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 23),
    _WfFrSwUsageLastDEOctetsHigh_Type()
)
wfFrSwUsageLastDEOctetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastDEOctetsHigh.setStatus("obsolete")
_WfFrSwUsageLastDEOctetsLow_Type = Integer32
_WfFrSwUsageLastDEOctetsLow_Object = MibTableColumn
wfFrSwUsageLastDEOctetsLow = _WfFrSwUsageLastDEOctetsLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 24),
    _WfFrSwUsageLastDEOctetsLow_Type()
)
wfFrSwUsageLastDEOctetsLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageLastDEOctetsLow.setStatus("obsolete")
_WfFrSwUsageRemoteIPAddress_Type = IpAddress
_WfFrSwUsageRemoteIPAddress_Object = MibTableColumn
wfFrSwUsageRemoteIPAddress = _WfFrSwUsageRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 25),
    _WfFrSwUsageRemoteIPAddress_Type()
)
wfFrSwUsageRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageRemoteIPAddress.setStatus("obsolete")


class _WfFrSwUsageRemoteDlci_Type(Integer32):
    """Custom type wfFrSwUsageRemoteDlci based on Integer32"""
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


_WfFrSwUsageRemoteDlci_Type.__name__ = "Integer32"
_WfFrSwUsageRemoteDlci_Object = MibTableColumn
wfFrSwUsageRemoteDlci = _WfFrSwUsageRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 6, 1, 26),
    _WfFrSwUsageRemoteDlci_Type()
)
wfFrSwUsageRemoteDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwUsageRemoteDlci.setStatus("obsolete")
_WfFrSwVcTable_Object = MibTable
wfFrSwVcTable = _WfFrSwVcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7)
)
if mibBuilder.loadTexts:
    wfFrSwVcTable.setStatus("mandatory")
_WfFrSwVcEntry_Object = MibTableRow
wfFrSwVcEntry = _WfFrSwVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1)
)
wfFrSwVcEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwVcCircuit"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwVcDlci"),
)
if mibBuilder.loadTexts:
    wfFrSwVcEntry.setStatus("mandatory")


class _WfFrSwVcDelete_Type(Integer32):
    """Custom type wfFrSwVcDelete based on Integer32"""
    defaultValue = 1

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
        *(("created", 1),
          ("deleted", 2),
          ("spvccaa", 6),
          ("spvccra", 5),
          ("svc", 4),
          ("system", 3))
    )


_WfFrSwVcDelete_Type.__name__ = "Integer32"
_WfFrSwVcDelete_Object = MibTableColumn
wfFrSwVcDelete = _WfFrSwVcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 1),
    _WfFrSwVcDelete_Type()
)
wfFrSwVcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcDelete.setStatus("mandatory")
_WfFrSwVcCircuit_Type = Integer32
_WfFrSwVcCircuit_Object = MibTableColumn
wfFrSwVcCircuit = _WfFrSwVcCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 2),
    _WfFrSwVcCircuit_Type()
)
wfFrSwVcCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcCircuit.setStatus("mandatory")
_WfFrSwVcDlci_Type = Integer32
_WfFrSwVcDlci_Object = MibTableColumn
wfFrSwVcDlci = _WfFrSwVcDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 3),
    _WfFrSwVcDlci_Type()
)
wfFrSwVcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDlci.setStatus("mandatory")


class _WfFrSwVcState_Type(Integer32):
    """Custom type wfFrSwVcState based on Integer32"""
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
          ("control", 4),
          ("inactive", 3),
          ("invalid", 1),
          ("user", 5))
    )


_WfFrSwVcState_Type.__name__ = "Integer32"
_WfFrSwVcState_Object = MibTableColumn
wfFrSwVcState = _WfFrSwVcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 4),
    _WfFrSwVcState_Type()
)
wfFrSwVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcState.setStatus("mandatory")


class _WfFrSwVcStateSet_Type(Integer32):
    """Custom type wfFrSwVcStateSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwVcStateSet_Type.__name__ = "Integer32"
_WfFrSwVcStateSet_Object = MibTableColumn
wfFrSwVcStateSet = _WfFrSwVcStateSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 5),
    _WfFrSwVcStateSet_Type()
)
wfFrSwVcStateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcStateSet.setStatus("mandatory")


class _WfFrSwVcMulticast_Type(Integer32):
    """Custom type wfFrSwVcMulticast based on Integer32"""
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


_WfFrSwVcMulticast_Type.__name__ = "Integer32"
_WfFrSwVcMulticast_Object = MibTableColumn
wfFrSwVcMulticast = _WfFrSwVcMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 6),
    _WfFrSwVcMulticast_Type()
)
wfFrSwVcMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcMulticast.setStatus("mandatory")


class _WfFrSwVcInBe_Type(Integer32):
    """Custom type wfFrSwVcInBe based on Integer32"""
    defaultValue = 2147483647


_WfFrSwVcInBe_Object = MibTableColumn
wfFrSwVcInBe = _WfFrSwVcInBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 7),
    _WfFrSwVcInBe_Type()
)
wfFrSwVcInBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInBe.setStatus("mandatory")
_WfFrSwVcOutBe_Type = Integer32
_WfFrSwVcOutBe_Object = MibTableColumn
wfFrSwVcOutBe = _WfFrSwVcOutBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 8),
    _WfFrSwVcOutBe_Type()
)
wfFrSwVcOutBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcOutBe.setStatus("mandatory")
_WfFrSwVcInThroughput_Type = Integer32
_WfFrSwVcInThroughput_Object = MibTableColumn
wfFrSwVcInThroughput = _WfFrSwVcInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 9),
    _WfFrSwVcInThroughput_Type()
)
wfFrSwVcInThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcInThroughput.setStatus("mandatory")
_WfFrSwVcOutThroughput_Type = Integer32
_WfFrSwVcOutThroughput_Object = MibTableColumn
wfFrSwVcOutThroughput = _WfFrSwVcOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 10),
    _WfFrSwVcOutThroughput_Type()
)
wfFrSwVcOutThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcOutThroughput.setStatus("mandatory")
_WfFrSwVcOutBc_Type = Integer32
_WfFrSwVcOutBc_Object = MibTableColumn
wfFrSwVcOutBc = _WfFrSwVcOutBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 11),
    _WfFrSwVcOutBc_Type()
)
wfFrSwVcOutBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcOutBc.setStatus("mandatory")
_WfFrSwVcInBc_Type = Integer32
_WfFrSwVcInBc_Object = MibTableColumn
wfFrSwVcInBc = _WfFrSwVcInBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 12),
    _WfFrSwVcInBc_Type()
)
wfFrSwVcInBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInBc.setStatus("mandatory")
_WfFrSwVcInBcOctets_Type = Integer32
_WfFrSwVcInBcOctets_Object = MibTableColumn
wfFrSwVcInBcOctets = _WfFrSwVcInBcOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 13),
    _WfFrSwVcInBcOctets_Type()
)
wfFrSwVcInBcOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInBcOctets.setStatus("mandatory")
_WfFrSwVcBecnState_Type = Integer32
_WfFrSwVcBecnState_Object = MibTableColumn
wfFrSwVcBecnState = _WfFrSwVcBecnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 14),
    _WfFrSwVcBecnState_Type()
)
wfFrSwVcBecnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcBecnState.setStatus("mandatory")


class _WfFrSwVcReportedStatus_Type(Integer32):
    """Custom type wfFrSwVcReportedStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acked", 1),
          ("unacked", 2),
          ("unreported", 3))
    )


_WfFrSwVcReportedStatus_Type.__name__ = "Integer32"
_WfFrSwVcReportedStatus_Object = MibTableColumn
wfFrSwVcReportedStatus = _WfFrSwVcReportedStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 15),
    _WfFrSwVcReportedStatus_Type()
)
wfFrSwVcReportedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcReportedStatus.setStatus("mandatory")


class _WfFrSwVcReceivedStatus_Type(Integer32):
    """Custom type wfFrSwVcReceivedStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwVcReceivedStatus_Type.__name__ = "Integer32"
_WfFrSwVcReceivedStatus_Object = MibTableColumn
wfFrSwVcReceivedStatus = _WfFrSwVcReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 16),
    _WfFrSwVcReceivedStatus_Type()
)
wfFrSwVcReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcReceivedStatus.setStatus("mandatory")


class _WfFrSwVcCrossNetStatus_Type(Integer32):
    """Custom type wfFrSwVcCrossNetStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwVcCrossNetStatus_Type.__name__ = "Integer32"
_WfFrSwVcCrossNetStatus_Object = MibTableColumn
wfFrSwVcCrossNetStatus = _WfFrSwVcCrossNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 17),
    _WfFrSwVcCrossNetStatus_Type()
)
wfFrSwVcCrossNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcCrossNetStatus.setStatus("mandatory")


class _WfFrSwVcXNetSent_Type(Integer32):
    """Custom type wfFrSwVcXNetSent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sent", 2),
          ("unsent", 1))
    )


_WfFrSwVcXNetSent_Type.__name__ = "Integer32"
_WfFrSwVcXNetSent_Object = MibTableColumn
wfFrSwVcXNetSent = _WfFrSwVcXNetSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 18),
    _WfFrSwVcXNetSent_Type()
)
wfFrSwVcXNetSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcXNetSent.setStatus("mandatory")


class _WfFrSwVcXNetReceived_Type(Integer32):
    """Custom type wfFrSwVcXNetReceived based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recv", 1),
          ("unrecv", 2))
    )


_WfFrSwVcXNetReceived_Type.__name__ = "Integer32"
_WfFrSwVcXNetReceived_Object = MibTableColumn
wfFrSwVcXNetReceived = _WfFrSwVcXNetReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 19),
    _WfFrSwVcXNetReceived_Type()
)
wfFrSwVcXNetReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcXNetReceived.setStatus("mandatory")
_WfFrSwVcCalledIpAddr_Type = IpAddress
_WfFrSwVcCalledIpAddr_Object = MibTableColumn
wfFrSwVcCalledIpAddr = _WfFrSwVcCalledIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 20),
    _WfFrSwVcCalledIpAddr_Type()
)
wfFrSwVcCalledIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCalledIpAddr.setStatus("mandatory")


class _WfFrSwVcCalledDlci_Type(Integer32):
    """Custom type wfFrSwVcCalledDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8257535),
    )


_WfFrSwVcCalledDlci_Type.__name__ = "Integer32"
_WfFrSwVcCalledDlci_Object = MibTableColumn
wfFrSwVcCalledDlci = _WfFrSwVcCalledDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 21),
    _WfFrSwVcCalledDlci_Type()
)
wfFrSwVcCalledDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCalledDlci.setStatus("mandatory")


class _WfFrSwVcTrfPriority_Type(Integer32):
    """Custom type wfFrSwVcTrfPriority based on Integer32"""
    defaultValue = 999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              999)
        )
    )
    namedValues = NamedValues(
        *(("default", 999),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfFrSwVcTrfPriority_Type.__name__ = "Integer32"
_WfFrSwVcTrfPriority_Object = MibTableColumn
wfFrSwVcTrfPriority = _WfFrSwVcTrfPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 22),
    _WfFrSwVcTrfPriority_Type()
)
wfFrSwVcTrfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcTrfPriority.setStatus("mandatory")
_WfFrSwVcCreationTime_Type = TimeTicks
_WfFrSwVcCreationTime_Object = MibTableColumn
wfFrSwVcCreationTime = _WfFrSwVcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 23),
    _WfFrSwVcCreationTime_Type()
)
wfFrSwVcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcCreationTime.setStatus("mandatory")
_WfFrSwVcLastTimeChange_Type = TimeTicks
_WfFrSwVcLastTimeChange_Object = MibTableColumn
wfFrSwVcLastTimeChange = _WfFrSwVcLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 24),
    _WfFrSwVcLastTimeChange_Type()
)
wfFrSwVcLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcLastTimeChange.setStatus("mandatory")
_WfFrSwVcTxNonDeFrames_Type = Counter32
_WfFrSwVcTxNonDeFrames_Object = MibTableColumn
wfFrSwVcTxNonDeFrames = _WfFrSwVcTxNonDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 25),
    _WfFrSwVcTxNonDeFrames_Type()
)
wfFrSwVcTxNonDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcTxNonDeFrames.setStatus("mandatory")
_WfFrSwVcTxNonDeOctets_Type = Counter32
_WfFrSwVcTxNonDeOctets_Object = MibTableColumn
wfFrSwVcTxNonDeOctets = _WfFrSwVcTxNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 26),
    _WfFrSwVcTxNonDeOctets_Type()
)
wfFrSwVcTxNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcTxNonDeOctets.setStatus("mandatory")
_WfFrSwVcTxDeFrames_Type = Counter32
_WfFrSwVcTxDeFrames_Object = MibTableColumn
wfFrSwVcTxDeFrames = _WfFrSwVcTxDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 27),
    _WfFrSwVcTxDeFrames_Type()
)
wfFrSwVcTxDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcTxDeFrames.setStatus("mandatory")
_WfFrSwVcTxDeOctets_Type = Counter32
_WfFrSwVcTxDeOctets_Object = MibTableColumn
wfFrSwVcTxDeOctets = _WfFrSwVcTxDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 28),
    _WfFrSwVcTxDeOctets_Type()
)
wfFrSwVcTxDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcTxDeOctets.setStatus("mandatory")
_WfFrSwVcSetFecnFrames_Type = Counter32
_WfFrSwVcSetFecnFrames_Object = MibTableColumn
wfFrSwVcSetFecnFrames = _WfFrSwVcSetFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 29),
    _WfFrSwVcSetFecnFrames_Type()
)
wfFrSwVcSetFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetFecnFrames.setStatus("mandatory")
_WfFrSwVcSetFecnOctets_Type = Counter32
_WfFrSwVcSetFecnOctets_Object = MibTableColumn
wfFrSwVcSetFecnOctets = _WfFrSwVcSetFecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 30),
    _WfFrSwVcSetFecnOctets_Type()
)
wfFrSwVcSetFecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetFecnOctets.setStatus("mandatory")
_WfFrSwVcSetBecnFrames_Type = Counter32
_WfFrSwVcSetBecnFrames_Object = MibTableColumn
wfFrSwVcSetBecnFrames = _WfFrSwVcSetBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 31),
    _WfFrSwVcSetBecnFrames_Type()
)
wfFrSwVcSetBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetBecnFrames.setStatus("mandatory")
_WfFrSwVcSetBecnOctets_Type = Counter32
_WfFrSwVcSetBecnOctets_Object = MibTableColumn
wfFrSwVcSetBecnOctets = _WfFrSwVcSetBecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 32),
    _WfFrSwVcSetBecnOctets_Type()
)
wfFrSwVcSetBecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetBecnOctets.setStatus("mandatory")
_WfFrSwVcSetDeFrames_Type = Counter32
_WfFrSwVcSetDeFrames_Object = MibTableColumn
wfFrSwVcSetDeFrames = _WfFrSwVcSetDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 33),
    _WfFrSwVcSetDeFrames_Type()
)
wfFrSwVcSetDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetDeFrames.setStatus("mandatory")
_WfFrSwVcSetDeOctets_Type = Counter32
_WfFrSwVcSetDeOctets_Object = MibTableColumn
wfFrSwVcSetDeOctets = _WfFrSwVcSetDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 34),
    _WfFrSwVcSetDeOctets_Type()
)
wfFrSwVcSetDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSetDeOctets.setStatus("mandatory")
_WfFrSwVcDropNonDeFrames_Type = Counter32
_WfFrSwVcDropNonDeFrames_Object = MibTableColumn
wfFrSwVcDropNonDeFrames = _WfFrSwVcDropNonDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 35),
    _WfFrSwVcDropNonDeFrames_Type()
)
wfFrSwVcDropNonDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropNonDeFrames.setStatus("mandatory")
_WfFrSwVcDropNonDeOctets_Type = Counter32
_WfFrSwVcDropNonDeOctets_Object = MibTableColumn
wfFrSwVcDropNonDeOctets = _WfFrSwVcDropNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 36),
    _WfFrSwVcDropNonDeOctets_Type()
)
wfFrSwVcDropNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropNonDeOctets.setStatus("mandatory")
_WfFrSwVcDropDeFrames_Type = Counter32
_WfFrSwVcDropDeFrames_Object = MibTableColumn
wfFrSwVcDropDeFrames = _WfFrSwVcDropDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 37),
    _WfFrSwVcDropDeFrames_Type()
)
wfFrSwVcDropDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropDeFrames.setStatus("mandatory")
_WfFrSwVcDropDeOctets_Type = Counter32
_WfFrSwVcDropDeOctets_Object = MibTableColumn
wfFrSwVcDropDeOctets = _WfFrSwVcDropDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 38),
    _WfFrSwVcDropDeOctets_Type()
)
wfFrSwVcDropDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropDeOctets.setStatus("mandatory")
_WfFrSwVcInactiveVcDropFrames_Type = Counter32
_WfFrSwVcInactiveVcDropFrames_Object = MibTableColumn
wfFrSwVcInactiveVcDropFrames = _WfFrSwVcInactiveVcDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 39),
    _WfFrSwVcInactiveVcDropFrames_Type()
)
wfFrSwVcInactiveVcDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInactiveVcDropFrames.setStatus("mandatory")
_WfFrSwVcInactiveVcDropOctets_Type = Counter32
_WfFrSwVcInactiveVcDropOctets_Object = MibTableColumn
wfFrSwVcInactiveVcDropOctets = _WfFrSwVcInactiveVcDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 40),
    _WfFrSwVcInactiveVcDropOctets_Type()
)
wfFrSwVcInactiveVcDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInactiveVcDropOctets.setStatus("mandatory")
_WfFrSwVcRecvNonDeFrames_Type = Counter32
_WfFrSwVcRecvNonDeFrames_Object = MibTableColumn
wfFrSwVcRecvNonDeFrames = _WfFrSwVcRecvNonDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 41),
    _WfFrSwVcRecvNonDeFrames_Type()
)
wfFrSwVcRecvNonDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvNonDeFrames.setStatus("mandatory")
_WfFrSwVcRecvNonDeOctets_Type = Counter32
_WfFrSwVcRecvNonDeOctets_Object = MibTableColumn
wfFrSwVcRecvNonDeOctets = _WfFrSwVcRecvNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 42),
    _WfFrSwVcRecvNonDeOctets_Type()
)
wfFrSwVcRecvNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvNonDeOctets.setStatus("mandatory")
_WfFrSwVcRecvDeFrames_Type = Counter32
_WfFrSwVcRecvDeFrames_Object = MibTableColumn
wfFrSwVcRecvDeFrames = _WfFrSwVcRecvDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 43),
    _WfFrSwVcRecvDeFrames_Type()
)
wfFrSwVcRecvDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvDeFrames.setStatus("mandatory")
_WfFrSwVcRecvDeOctets_Type = Counter32
_WfFrSwVcRecvDeOctets_Object = MibTableColumn
wfFrSwVcRecvDeOctets = _WfFrSwVcRecvDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 44),
    _WfFrSwVcRecvDeOctets_Type()
)
wfFrSwVcRecvDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvDeOctets.setStatus("mandatory")
_WfFrSwVcRecvFecnFrames_Type = Counter32
_WfFrSwVcRecvFecnFrames_Object = MibTableColumn
wfFrSwVcRecvFecnFrames = _WfFrSwVcRecvFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 45),
    _WfFrSwVcRecvFecnFrames_Type()
)
wfFrSwVcRecvFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvFecnFrames.setStatus("mandatory")
_WfFrSwVcRecvFecnOctets_Type = Counter32
_WfFrSwVcRecvFecnOctets_Object = MibTableColumn
wfFrSwVcRecvFecnOctets = _WfFrSwVcRecvFecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 46),
    _WfFrSwVcRecvFecnOctets_Type()
)
wfFrSwVcRecvFecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvFecnOctets.setStatus("mandatory")
_WfFrSwVcRecvBecnFrames_Type = Counter32
_WfFrSwVcRecvBecnFrames_Object = MibTableColumn
wfFrSwVcRecvBecnFrames = _WfFrSwVcRecvBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 47),
    _WfFrSwVcRecvBecnFrames_Type()
)
wfFrSwVcRecvBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvBecnFrames.setStatus("mandatory")
_WfFrSwVcRecvBecnOctets_Type = Counter32
_WfFrSwVcRecvBecnOctets_Object = MibTableColumn
wfFrSwVcRecvBecnOctets = _WfFrSwVcRecvBecnOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 48),
    _WfFrSwVcRecvBecnOctets_Type()
)
wfFrSwVcRecvBecnOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecvBecnOctets.setStatus("mandatory")
_WfFrSwVcRecentNonDeOctets_Type = Counter32
_WfFrSwVcRecentNonDeOctets_Object = MibTableColumn
wfFrSwVcRecentNonDeOctets = _WfFrSwVcRecentNonDeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 49),
    _WfFrSwVcRecentNonDeOctets_Type()
)
wfFrSwVcRecentNonDeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRecentNonDeOctets.setStatus("mandatory")
_WfFrSwVcXNetErrors_Type = Counter32
_WfFrSwVcXNetErrors_Object = MibTableColumn
wfFrSwVcXNetErrors = _WfFrSwVcXNetErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 50),
    _WfFrSwVcXNetErrors_Type()
)
wfFrSwVcXNetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcXNetErrors.setStatus("mandatory")
_WfFrSwVcDropExcessBurstFrames_Type = Counter32
_WfFrSwVcDropExcessBurstFrames_Object = MibTableColumn
wfFrSwVcDropExcessBurstFrames = _WfFrSwVcDropExcessBurstFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 51),
    _WfFrSwVcDropExcessBurstFrames_Type()
)
wfFrSwVcDropExcessBurstFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropExcessBurstFrames.setStatus("mandatory")
_WfFrSwVcDropExcessBurstOctets_Type = Counter32
_WfFrSwVcDropExcessBurstOctets_Object = MibTableColumn
wfFrSwVcDropExcessBurstOctets = _WfFrSwVcDropExcessBurstOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 52),
    _WfFrSwVcDropExcessBurstOctets_Type()
)
wfFrSwVcDropExcessBurstOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcDropExcessBurstOctets.setStatus("mandatory")
_WfFrSwVcInBeOctets_Type = Integer32
_WfFrSwVcInBeOctets_Object = MibTableColumn
wfFrSwVcInBeOctets = _WfFrSwVcInBeOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 53),
    _WfFrSwVcInBeOctets_Type()
)
wfFrSwVcInBeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcInBeOctets.setStatus("mandatory")


class _WfFrSwVcCfgInBe_Type(Integer32):
    """Custom type wfFrSwVcCfgInBe based on Integer32"""
    defaultValue = 2147483647


_WfFrSwVcCfgInBe_Object = MibTableColumn
wfFrSwVcCfgInBe = _WfFrSwVcCfgInBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 54),
    _WfFrSwVcCfgInBe_Type()
)
wfFrSwVcCfgInBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCfgInBe.setStatus("mandatory")


class _WfFrSwVcRedirectAction_Type(Integer32):
    """Custom type wfFrSwVcRedirectAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("redirecttobackup", 3),
          ("redirecttoprimary", 2),
          ("switchondemand", 4),
          ("swondemandtobackup", 6),
          ("swondemandtoprimary", 5))
    )


_WfFrSwVcRedirectAction_Type.__name__ = "Integer32"
_WfFrSwVcRedirectAction_Object = MibTableColumn
wfFrSwVcRedirectAction = _WfFrSwVcRedirectAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 55),
    _WfFrSwVcRedirectAction_Type()
)
wfFrSwVcRedirectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcRedirectAction.setStatus("mandatory")


class _WfFrSwVcRedirectType_Type(Integer32):
    """Custom type wfFrSwVcRedirectType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intrusivea", 3),
          ("intrusiven", 2),
          ("transparent", 1))
    )


_WfFrSwVcRedirectType_Type.__name__ = "Integer32"
_WfFrSwVcRedirectType_Object = MibTableColumn
wfFrSwVcRedirectType = _WfFrSwVcRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 56),
    _WfFrSwVcRedirectType_Type()
)
wfFrSwVcRedirectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcRedirectType.setStatus("mandatory")


class _WfFrSwVcRedirectState_Type(Integer32):
    """Custom type wfFrSwVcRedirectState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              12,
              13,
              21)
        )
    )
    namedValues = NamedValues(
        *(("backupactive", 12),
          ("backupinactive", 1),
          ("holddown", 21),
          ("primaryactive", 2),
          ("switchtobackup", 3),
          ("switchtoprimary", 13))
    )


_WfFrSwVcRedirectState_Type.__name__ = "Integer32"
_WfFrSwVcRedirectState_Object = MibTableColumn
wfFrSwVcRedirectState = _WfFrSwVcRedirectState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 57),
    _WfFrSwVcRedirectState_Type()
)
wfFrSwVcRedirectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcRedirectState.setStatus("mandatory")
_WfFrSwVcBackupCalledIpAddr_Type = IpAddress
_WfFrSwVcBackupCalledIpAddr_Object = MibTableColumn
wfFrSwVcBackupCalledIpAddr = _WfFrSwVcBackupCalledIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 58),
    _WfFrSwVcBackupCalledIpAddr_Type()
)
wfFrSwVcBackupCalledIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcBackupCalledIpAddr.setStatus("mandatory")


class _WfFrSwVcBackupCalledDlci_Type(Integer32):
    """Custom type wfFrSwVcBackupCalledDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8257535),
    )


_WfFrSwVcBackupCalledDlci_Type.__name__ = "Integer32"
_WfFrSwVcBackupCalledDlci_Object = MibTableColumn
wfFrSwVcBackupCalledDlci = _WfFrSwVcBackupCalledDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 59),
    _WfFrSwVcBackupCalledDlci_Type()
)
wfFrSwVcBackupCalledDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcBackupCalledDlci.setStatus("mandatory")


class _WfFrSwVcBackupCrossNetStatus_Type(Integer32):
    """Custom type wfFrSwVcBackupCrossNetStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_WfFrSwVcBackupCrossNetStatus_Type.__name__ = "Integer32"
_WfFrSwVcBackupCrossNetStatus_Object = MibTableColumn
wfFrSwVcBackupCrossNetStatus = _WfFrSwVcBackupCrossNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 60),
    _WfFrSwVcBackupCrossNetStatus_Type()
)
wfFrSwVcBackupCrossNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcBackupCrossNetStatus.setStatus("mandatory")
_WfFrSwVcBackupCrossNetErrors_Type = Integer32
_WfFrSwVcBackupCrossNetErrors_Object = MibTableColumn
wfFrSwVcBackupCrossNetErrors = _WfFrSwVcBackupCrossNetErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 61),
    _WfFrSwVcBackupCrossNetErrors_Type()
)
wfFrSwVcBackupCrossNetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcBackupCrossNetErrors.setStatus("mandatory")


class _WfFrSwVcAtmIwfMode_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfMode based on Integer32"""
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
        *(("atmDisableIwfMode", 1),
          ("atmNetworkIwfMode", 4),
          ("atmServiceIwfTranslationMode", 3),
          ("atmServiceIwfTransparentMode", 2))
    )


_WfFrSwVcAtmIwfMode_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfMode_Object = MibTableColumn
wfFrSwVcAtmIwfMode = _WfFrSwVcAtmIwfMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 62),
    _WfFrSwVcAtmIwfMode_Type()
)
wfFrSwVcAtmIwfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfMode.setStatus("mandatory")


class _WfFrSwVcAtmIwfVPI_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfVPI based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfFrSwVcAtmIwfVPI_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfVPI_Object = MibTableColumn
wfFrSwVcAtmIwfVPI = _WfFrSwVcAtmIwfVPI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 63),
    _WfFrSwVcAtmIwfVPI_Type()
)
wfFrSwVcAtmIwfVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfVPI.setStatus("mandatory")


class _WfFrSwVcAtmIwfVCI_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfVCI based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 65535),
    )


_WfFrSwVcAtmIwfVCI_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfVCI_Object = MibTableColumn
wfFrSwVcAtmIwfVCI = _WfFrSwVcAtmIwfVCI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 64),
    _WfFrSwVcAtmIwfVCI_Type()
)
wfFrSwVcAtmIwfVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfVCI.setStatus("mandatory")


class _WfFrSwVcAtmIwfLossPriorityPolicy_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfLossPriorityPolicy based on Integer32"""
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
        *(("atmiwfmapDe", 1),
          ("atmiwfsetDe0", 3),
          ("atmiwfsetDe1", 2))
    )


_WfFrSwVcAtmIwfLossPriorityPolicy_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfLossPriorityPolicy_Object = MibTableColumn
wfFrSwVcAtmIwfLossPriorityPolicy = _WfFrSwVcAtmIwfLossPriorityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 65),
    _WfFrSwVcAtmIwfLossPriorityPolicy_Type()
)
wfFrSwVcAtmIwfLossPriorityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfLossPriorityPolicy.setStatus("mandatory")


class _WfFrSwVcAtmIwfDePolicy_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfDePolicy based on Integer32"""
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
        *(("atmiwfmapClp", 1),
          ("atmiwfsetClp0", 3),
          ("atmiwfsetClp1", 2))
    )


_WfFrSwVcAtmIwfDePolicy_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfDePolicy_Object = MibTableColumn
wfFrSwVcAtmIwfDePolicy = _WfFrSwVcAtmIwfDePolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 66),
    _WfFrSwVcAtmIwfDePolicy_Type()
)
wfFrSwVcAtmIwfDePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfDePolicy.setStatus("mandatory")


class _WfFrSwVcAtmIwfEfciPolicy_Type(Integer32):
    """Custom type wfFrSwVcAtmIwfEfciPolicy based on Integer32"""
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
        *(("atmiwfmapFecn", 1),
          ("atmiwfsetFecn0", 3),
          ("atmiwfsetFecn1", 2))
    )


_WfFrSwVcAtmIwfEfciPolicy_Type.__name__ = "Integer32"
_WfFrSwVcAtmIwfEfciPolicy_Object = MibTableColumn
wfFrSwVcAtmIwfEfciPolicy = _WfFrSwVcAtmIwfEfciPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 67),
    _WfFrSwVcAtmIwfEfciPolicy_Type()
)
wfFrSwVcAtmIwfEfciPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcAtmIwfEfciPolicy.setStatus("mandatory")


class _WfFrSwVcEscapeEnable_Type(Integer32):
    """Custom type wfFrSwVcEscapeEnable based on Integer32"""
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


_WfFrSwVcEscapeEnable_Type.__name__ = "Integer32"
_WfFrSwVcEscapeEnable_Object = MibTableColumn
wfFrSwVcEscapeEnable = _WfFrSwVcEscapeEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 68),
    _WfFrSwVcEscapeEnable_Type()
)
wfFrSwVcEscapeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcEscapeEnable.setStatus("mandatory")


class _WfFrSwVcSpvcCallState_Type(Integer32):
    """Custom type wfFrSwVcSpvcCallState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("inprogress", 2))
    )


_WfFrSwVcSpvcCallState_Type.__name__ = "Integer32"
_WfFrSwVcSpvcCallState_Object = MibTableColumn
wfFrSwVcSpvcCallState = _WfFrSwVcSpvcCallState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 69),
    _WfFrSwVcSpvcCallState_Type()
)
wfFrSwVcSpvcCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVcSpvcCallState.setStatus("mandatory")
_WfFrSwVcCallReqCalledAddr_Type = DisplayString
_WfFrSwVcCallReqCalledAddr_Object = MibTableColumn
wfFrSwVcCallReqCalledAddr = _WfFrSwVcCallReqCalledAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 70),
    _WfFrSwVcCallReqCalledAddr_Type()
)
wfFrSwVcCallReqCalledAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCallReqCalledAddr.setStatus("mandatory")


class _WfFrSwVcCallReqDlciSelectionType_Type(Integer32):
    """Custom type wfFrSwVcCallReqDlciSelectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("specific", 2))
    )


_WfFrSwVcCallReqDlciSelectionType_Type.__name__ = "Integer32"
_WfFrSwVcCallReqDlciSelectionType_Object = MibTableColumn
wfFrSwVcCallReqDlciSelectionType = _WfFrSwVcCallReqDlciSelectionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 71),
    _WfFrSwVcCallReqDlciSelectionType_Type()
)
wfFrSwVcCallReqDlciSelectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCallReqDlciSelectionType.setStatus("mandatory")


class _WfFrSwVcCallReqCalledDlci_Type(Integer32):
    """Custom type wfFrSwVcCallReqCalledDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 8257535),
    )


_WfFrSwVcCallReqCalledDlci_Type.__name__ = "Integer32"
_WfFrSwVcCallReqCalledDlci_Object = MibTableColumn
wfFrSwVcCallReqCalledDlci = _WfFrSwVcCallReqCalledDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 72),
    _WfFrSwVcCallReqCalledDlci_Type()
)
wfFrSwVcCallReqCalledDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCallReqCalledDlci.setStatus("mandatory")


class _WfFrSwVcCallReqRetryTimer_Type(Integer32):
    """Custom type wfFrSwVcCallReqRetryTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfFrSwVcCallReqRetryTimer_Type.__name__ = "Integer32"
_WfFrSwVcCallReqRetryTimer_Object = MibTableColumn
wfFrSwVcCallReqRetryTimer = _WfFrSwVcCallReqRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 73),
    _WfFrSwVcCallReqRetryTimer_Type()
)
wfFrSwVcCallReqRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCallReqRetryTimer.setStatus("mandatory")


class _WfFrSwVcCallReqMaxRetries_Type(Integer32):
    """Custom type wfFrSwVcCallReqMaxRetries based on Integer32"""
    defaultValue = 2147483647


_WfFrSwVcCallReqMaxRetries_Object = MibTableColumn
wfFrSwVcCallReqMaxRetries = _WfFrSwVcCallReqMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 7, 1, 74),
    _WfFrSwVcCallReqMaxRetries_Type()
)
wfFrSwVcCallReqMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVcCallReqMaxRetries.setStatus("mandatory")
_WfFrSwIsdnBaseTable_Object = MibTable
wfFrSwIsdnBaseTable = _WfFrSwIsdnBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 8)
)
if mibBuilder.loadTexts:
    wfFrSwIsdnBaseTable.setStatus("mandatory")
_WfFrSwIsdnBaseEntry_Object = MibTableRow
wfFrSwIsdnBaseEntry = _WfFrSwIsdnBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 8, 1)
)
wfFrSwIsdnBaseEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnBaseSlotNum"),
)
if mibBuilder.loadTexts:
    wfFrSwIsdnBaseEntry.setStatus("mandatory")


class _WfFrSwIsdnBaseDelete_Type(Integer32):
    """Custom type wfFrSwIsdnBaseDelete based on Integer32"""
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


_WfFrSwIsdnBaseDelete_Type.__name__ = "Integer32"
_WfFrSwIsdnBaseDelete_Object = MibTableColumn
wfFrSwIsdnBaseDelete = _WfFrSwIsdnBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 8, 1, 1),
    _WfFrSwIsdnBaseDelete_Type()
)
wfFrSwIsdnBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnBaseDelete.setStatus("mandatory")
_WfFrSwIsdnBaseSlotNum_Type = Integer32
_WfFrSwIsdnBaseSlotNum_Object = MibTableColumn
wfFrSwIsdnBaseSlotNum = _WfFrSwIsdnBaseSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 8, 1, 2),
    _WfFrSwIsdnBaseSlotNum_Type()
)
wfFrSwIsdnBaseSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnBaseSlotNum.setStatus("mandatory")


class _WfFrSwIsdnBaseAssocType_Type(Integer32):
    """Custom type wfFrSwIsdnBaseAssocType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ani", 2),
          ("dnis", 1))
    )


_WfFrSwIsdnBaseAssocType_Type.__name__ = "Integer32"
_WfFrSwIsdnBaseAssocType_Object = MibTableColumn
wfFrSwIsdnBaseAssocType = _WfFrSwIsdnBaseAssocType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 8, 1, 3),
    _WfFrSwIsdnBaseAssocType_Type()
)
wfFrSwIsdnBaseAssocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnBaseAssocType.setStatus("mandatory")
_WfFrSwIsdnAssocTable_Object = MibTable
wfFrSwIsdnAssocTable = _WfFrSwIsdnAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9)
)
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocTable.setStatus("mandatory")
_WfFrSwIsdnAssocEntry_Object = MibTableRow
wfFrSwIsdnAssocEntry = _WfFrSwIsdnAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1)
)
wfFrSwIsdnAssocEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnAssocSlotNum"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnAssocNum"),
)
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocEntry.setStatus("mandatory")


class _WfFrSwIsdnAssocDelete_Type(Integer32):
    """Custom type wfFrSwIsdnAssocDelete based on Integer32"""
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


_WfFrSwIsdnAssocDelete_Type.__name__ = "Integer32"
_WfFrSwIsdnAssocDelete_Object = MibTableColumn
wfFrSwIsdnAssocDelete = _WfFrSwIsdnAssocDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1, 1),
    _WfFrSwIsdnAssocDelete_Type()
)
wfFrSwIsdnAssocDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocDelete.setStatus("mandatory")
_WfFrSwIsdnAssocSlotNum_Type = Integer32
_WfFrSwIsdnAssocSlotNum_Object = MibTableColumn
wfFrSwIsdnAssocSlotNum = _WfFrSwIsdnAssocSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1, 2),
    _WfFrSwIsdnAssocSlotNum_Type()
)
wfFrSwIsdnAssocSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocSlotNum.setStatus("mandatory")
_WfFrSwIsdnAssocNum_Type = OctetString
_WfFrSwIsdnAssocNum_Object = MibTableColumn
wfFrSwIsdnAssocNum = _WfFrSwIsdnAssocNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1, 3),
    _WfFrSwIsdnAssocNum_Type()
)
wfFrSwIsdnAssocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocNum.setStatus("mandatory")


class _WfFrSwIsdnAssocScrnEnable_Type(Integer32):
    """Custom type wfFrSwIsdnAssocScrnEnable based on Integer32"""
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


_WfFrSwIsdnAssocScrnEnable_Type.__name__ = "Integer32"
_WfFrSwIsdnAssocScrnEnable_Object = MibTableColumn
wfFrSwIsdnAssocScrnEnable = _WfFrSwIsdnAssocScrnEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1, 4),
    _WfFrSwIsdnAssocScrnEnable_Type()
)
wfFrSwIsdnAssocScrnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocScrnEnable.setStatus("mandatory")


class _WfFrSwIsdnAssocIndex_Type(Integer32):
    """Custom type wfFrSwIsdnAssocIndex based on Integer32"""
    defaultValue = 2147483647


_WfFrSwIsdnAssocIndex_Object = MibTableColumn
wfFrSwIsdnAssocIndex = _WfFrSwIsdnAssocIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 9, 1, 5),
    _WfFrSwIsdnAssocIndex_Type()
)
wfFrSwIsdnAssocIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnAssocIndex.setStatus("mandatory")
_WfFrSwIsdnUniTable_Object = MibTable
wfFrSwIsdnUniTable = _WfFrSwIsdnUniTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10)
)
if mibBuilder.loadTexts:
    wfFrSwIsdnUniTable.setStatus("mandatory")
_WfFrSwIsdnUniEntry_Object = MibTableRow
wfFrSwIsdnUniEntry = _WfFrSwIsdnUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10, 1)
)
wfFrSwIsdnUniEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnUniIndex"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnUniNum"),
)
if mibBuilder.loadTexts:
    wfFrSwIsdnUniEntry.setStatus("mandatory")


class _WfFrSwIsdnUniDelete_Type(Integer32):
    """Custom type wfFrSwIsdnUniDelete based on Integer32"""
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


_WfFrSwIsdnUniDelete_Type.__name__ = "Integer32"
_WfFrSwIsdnUniDelete_Object = MibTableColumn
wfFrSwIsdnUniDelete = _WfFrSwIsdnUniDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10, 1, 1),
    _WfFrSwIsdnUniDelete_Type()
)
wfFrSwIsdnUniDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnUniDelete.setStatus("mandatory")
_WfFrSwIsdnUniIndex_Type = Integer32
_WfFrSwIsdnUniIndex_Object = MibTableColumn
wfFrSwIsdnUniIndex = _WfFrSwIsdnUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10, 1, 2),
    _WfFrSwIsdnUniIndex_Type()
)
wfFrSwIsdnUniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnUniIndex.setStatus("mandatory")
_WfFrSwIsdnUniNum_Type = Integer32
_WfFrSwIsdnUniNum_Object = MibTableColumn
wfFrSwIsdnUniNum = _WfFrSwIsdnUniNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10, 1, 3),
    _WfFrSwIsdnUniNum_Type()
)
wfFrSwIsdnUniNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnUniNum.setStatus("mandatory")


class _WfFrSwIsdnUniState_Type(Integer32):
    """Custom type wfFrSwIsdnUniState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("inuse", 2))
    )


_WfFrSwIsdnUniState_Type.__name__ = "Integer32"
_WfFrSwIsdnUniState_Object = MibTableColumn
wfFrSwIsdnUniState = _WfFrSwIsdnUniState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 10, 1, 4),
    _WfFrSwIsdnUniState_Type()
)
wfFrSwIsdnUniState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnUniState.setStatus("mandatory")
_WfFrSwIsdnScrnTable_Object = MibTable
wfFrSwIsdnScrnTable = _WfFrSwIsdnScrnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 11)
)
if mibBuilder.loadTexts:
    wfFrSwIsdnScrnTable.setStatus("mandatory")
_WfFrSwIsdnScrnEntry_Object = MibTableRow
wfFrSwIsdnScrnEntry = _WfFrSwIsdnScrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 11, 1)
)
wfFrSwIsdnScrnEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnScrnIndex"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwIsdnScrnNum"),
)
if mibBuilder.loadTexts:
    wfFrSwIsdnScrnEntry.setStatus("mandatory")


class _WfFrSwIsdnScrnDelete_Type(Integer32):
    """Custom type wfFrSwIsdnScrnDelete based on Integer32"""
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


_WfFrSwIsdnScrnDelete_Type.__name__ = "Integer32"
_WfFrSwIsdnScrnDelete_Object = MibTableColumn
wfFrSwIsdnScrnDelete = _WfFrSwIsdnScrnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 11, 1, 1),
    _WfFrSwIsdnScrnDelete_Type()
)
wfFrSwIsdnScrnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwIsdnScrnDelete.setStatus("mandatory")
_WfFrSwIsdnScrnIndex_Type = Integer32
_WfFrSwIsdnScrnIndex_Object = MibTableColumn
wfFrSwIsdnScrnIndex = _WfFrSwIsdnScrnIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 11, 1, 2),
    _WfFrSwIsdnScrnIndex_Type()
)
wfFrSwIsdnScrnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnScrnIndex.setStatus("mandatory")
_WfFrSwIsdnScrnNum_Type = OctetString
_WfFrSwIsdnScrnNum_Object = MibTableColumn
wfFrSwIsdnScrnNum = _WfFrSwIsdnScrnNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 11, 1, 3),
    _WfFrSwIsdnScrnNum_Type()
)
wfFrSwIsdnScrnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwIsdnScrnNum.setStatus("mandatory")
_WfFrSwSigTable_Object = MibTable
wfFrSwSigTable = _WfFrSwSigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12)
)
if mibBuilder.loadTexts:
    wfFrSwSigTable.setStatus("mandatory")
_WfFrSwSigEntry_Object = MibTableRow
wfFrSwSigEntry = _WfFrSwSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1)
)
wfFrSwSigEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwSigCircuit"),
)
if mibBuilder.loadTexts:
    wfFrSwSigEntry.setStatus("mandatory")


class _WfFrSwSigDelete_Type(Integer32):
    """Custom type wfFrSwSigDelete based on Integer32"""
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


_WfFrSwSigDelete_Type.__name__ = "Integer32"
_WfFrSwSigDelete_Object = MibTableColumn
wfFrSwSigDelete = _WfFrSwSigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 1),
    _WfFrSwSigDelete_Type()
)
wfFrSwSigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDelete.setStatus("mandatory")
_WfFrSwSigCircuit_Type = Integer32
_WfFrSwSigCircuit_Object = MibTableColumn
wfFrSwSigCircuit = _WfFrSwSigCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 2),
    _WfFrSwSigCircuit_Type()
)
wfFrSwSigCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigCircuit.setStatus("mandatory")


class _WfFrSwSigSvcDlciLow_Type(Integer32):
    """Custom type wfFrSwSigSvcDlciLow based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigSvcDlciLow_Type.__name__ = "Integer32"
_WfFrSwSigSvcDlciLow_Object = MibTableColumn
wfFrSwSigSvcDlciLow = _WfFrSwSigSvcDlciLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 3),
    _WfFrSwSigSvcDlciLow_Type()
)
wfFrSwSigSvcDlciLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigSvcDlciLow.setStatus("mandatory")


class _WfFrSwSigSvcDlciHigh_Type(Integer32):
    """Custom type wfFrSwSigSvcDlciHigh based on Integer32"""
    defaultValue = 991

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigSvcDlciHigh_Type.__name__ = "Integer32"
_WfFrSwSigSvcDlciHigh_Object = MibTableColumn
wfFrSwSigSvcDlciHigh = _WfFrSwSigSvcDlciHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 4),
    _WfFrSwSigSvcDlciHigh_Type()
)
wfFrSwSigSvcDlciHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigSvcDlciHigh.setStatus("mandatory")


class _WfFrSwSigDlciAssign_Type(Integer32):
    """Custom type wfFrSwSigDlciAssign based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 2),
          ("increment", 1))
    )


_WfFrSwSigDlciAssign_Type.__name__ = "Integer32"
_WfFrSwSigDlciAssign_Object = MibTableColumn
wfFrSwSigDlciAssign = _WfFrSwSigDlciAssign_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 5),
    _WfFrSwSigDlciAssign_Type()
)
wfFrSwSigDlciAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDlciAssign.setStatus("mandatory")


class _WfFrSwSigMaxNumOfSvcs_Type(Integer32):
    """Custom type wfFrSwSigMaxNumOfSvcs based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfFrSwSigMaxNumOfSvcs_Type.__name__ = "Integer32"
_WfFrSwSigMaxNumOfSvcs_Object = MibTableColumn
wfFrSwSigMaxNumOfSvcs = _WfFrSwSigMaxNumOfSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 6),
    _WfFrSwSigMaxNumOfSvcs_Type()
)
wfFrSwSigMaxNumOfSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigMaxNumOfSvcs.setStatus("mandatory")
_WfFrSwSigNumOfSvcsInUse_Type = Integer32
_WfFrSwSigNumOfSvcsInUse_Object = MibTableColumn
wfFrSwSigNumOfSvcsInUse = _WfFrSwSigNumOfSvcsInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 7),
    _WfFrSwSigNumOfSvcsInUse_Type()
)
wfFrSwSigNumOfSvcsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigNumOfSvcsInUse.setStatus("mandatory")


class _WfFrSwSigDefaultThroughput_Type(Integer32):
    """Custom type wfFrSwSigDefaultThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigDefaultThroughput_Type.__name__ = "Integer32"
_WfFrSwSigDefaultThroughput_Object = MibTableColumn
wfFrSwSigDefaultThroughput = _WfFrSwSigDefaultThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 8),
    _WfFrSwSigDefaultThroughput_Type()
)
wfFrSwSigDefaultThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDefaultThroughput.setStatus("mandatory")


class _WfFrSwSigDefaultMinAcceptThroughput_Type(Integer32):
    """Custom type wfFrSwSigDefaultMinAcceptThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigDefaultMinAcceptThroughput_Type.__name__ = "Integer32"
_WfFrSwSigDefaultMinAcceptThroughput_Object = MibTableColumn
wfFrSwSigDefaultMinAcceptThroughput = _WfFrSwSigDefaultMinAcceptThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 9),
    _WfFrSwSigDefaultMinAcceptThroughput_Type()
)
wfFrSwSigDefaultMinAcceptThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDefaultMinAcceptThroughput.setStatus("mandatory")


class _WfFrSwSigDefaultBc_Type(Integer32):
    """Custom type wfFrSwSigDefaultBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigDefaultBc_Type.__name__ = "Integer32"
_WfFrSwSigDefaultBc_Object = MibTableColumn
wfFrSwSigDefaultBc = _WfFrSwSigDefaultBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 10),
    _WfFrSwSigDefaultBc_Type()
)
wfFrSwSigDefaultBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigDefaultBc.setStatus("mandatory")


class _WfFrSwSigDefaultBe_Type(Integer32):
    """Custom type wfFrSwSigDefaultBe based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigDefaultBe_Type.__name__ = "Integer32"
_WfFrSwSigDefaultBe_Object = MibTableColumn
wfFrSwSigDefaultBe = _WfFrSwSigDefaultBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 11),
    _WfFrSwSigDefaultBe_Type()
)
wfFrSwSigDefaultBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDefaultBe.setStatus("mandatory")


class _WfFrSwSigMaxInThroughputPerSvc_Type(Integer32):
    """Custom type wfFrSwSigMaxInThroughputPerSvc based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigMaxInThroughputPerSvc_Type.__name__ = "Integer32"
_WfFrSwSigMaxInThroughputPerSvc_Object = MibTableColumn
wfFrSwSigMaxInThroughputPerSvc = _WfFrSwSigMaxInThroughputPerSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 12),
    _WfFrSwSigMaxInThroughputPerSvc_Type()
)
wfFrSwSigMaxInThroughputPerSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigMaxInThroughputPerSvc.setStatus("mandatory")


class _WfFrSwSigMaxOutThroughputPerSvc_Type(Integer32):
    """Custom type wfFrSwSigMaxOutThroughputPerSvc based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigMaxOutThroughputPerSvc_Type.__name__ = "Integer32"
_WfFrSwSigMaxOutThroughputPerSvc_Object = MibTableColumn
wfFrSwSigMaxOutThroughputPerSvc = _WfFrSwSigMaxOutThroughputPerSvc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 13),
    _WfFrSwSigMaxOutThroughputPerSvc_Type()
)
wfFrSwSigMaxOutThroughputPerSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigMaxOutThroughputPerSvc.setStatus("mandatory")


class _WfFrSwSigTotalInNegotiableThroughput_Type(Integer32):
    """Custom type wfFrSwSigTotalInNegotiableThroughput based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigTotalInNegotiableThroughput_Type.__name__ = "Integer32"
_WfFrSwSigTotalInNegotiableThroughput_Object = MibTableColumn
wfFrSwSigTotalInNegotiableThroughput = _WfFrSwSigTotalInNegotiableThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 14),
    _WfFrSwSigTotalInNegotiableThroughput_Type()
)
wfFrSwSigTotalInNegotiableThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigTotalInNegotiableThroughput.setStatus("mandatory")
_WfFrSwSigTotalInCurrentThroughput_Type = Integer32
_WfFrSwSigTotalInCurrentThroughput_Object = MibTableColumn
wfFrSwSigTotalInCurrentThroughput = _WfFrSwSigTotalInCurrentThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 15),
    _WfFrSwSigTotalInCurrentThroughput_Type()
)
wfFrSwSigTotalInCurrentThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigTotalInCurrentThroughput.setStatus("mandatory")


class _WfFrSwSigTotalOutNegotiableThroughput_Type(Integer32):
    """Custom type wfFrSwSigTotalOutNegotiableThroughput based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigTotalOutNegotiableThroughput_Type.__name__ = "Integer32"
_WfFrSwSigTotalOutNegotiableThroughput_Object = MibTableColumn
wfFrSwSigTotalOutNegotiableThroughput = _WfFrSwSigTotalOutNegotiableThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 16),
    _WfFrSwSigTotalOutNegotiableThroughput_Type()
)
wfFrSwSigTotalOutNegotiableThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigTotalOutNegotiableThroughput.setStatus("mandatory")
_WfFrSwSigTotalOutCurrentThroughput_Type = Integer32
_WfFrSwSigTotalOutCurrentThroughput_Object = MibTableColumn
wfFrSwSigTotalOutCurrentThroughput = _WfFrSwSigTotalOutCurrentThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 17),
    _WfFrSwSigTotalOutCurrentThroughput_Type()
)
wfFrSwSigTotalOutCurrentThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigTotalOutCurrentThroughput.setStatus("mandatory")


class _WfFrSwSigXNetClearingDisable_Type(Integer32):
    """Custom type wfFrSwSigXNetClearingDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfFrSwSigXNetClearingDisable_Type.__name__ = "Integer32"
_WfFrSwSigXNetClearingDisable_Object = MibTableColumn
wfFrSwSigXNetClearingDisable = _WfFrSwSigXNetClearingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 18),
    _WfFrSwSigXNetClearingDisable_Type()
)
wfFrSwSigXNetClearingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigXNetClearingDisable.setStatus("mandatory")


class _WfFrSwSigCallingPartyIEMandatory_Type(Integer32):
    """Custom type wfFrSwSigCallingPartyIEMandatory based on Integer32"""
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


_WfFrSwSigCallingPartyIEMandatory_Type.__name__ = "Integer32"
_WfFrSwSigCallingPartyIEMandatory_Object = MibTableColumn
wfFrSwSigCallingPartyIEMandatory = _WfFrSwSigCallingPartyIEMandatory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 19),
    _WfFrSwSigCallingPartyIEMandatory_Type()
)
wfFrSwSigCallingPartyIEMandatory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigCallingPartyIEMandatory.setStatus("mandatory")


class _WfFrSwSigT301_Type(Integer32):
    """Custom type wfFrSwSigT301 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfFrSwSigT301_Type.__name__ = "Integer32"
_WfFrSwSigT301_Object = MibTableColumn
wfFrSwSigT301 = _WfFrSwSigT301_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 20),
    _WfFrSwSigT301_Type()
)
wfFrSwSigT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT301.setStatus("mandatory")


class _WfFrSwSigT303_Type(Integer32):
    """Custom type wfFrSwSigT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrSwSigT303_Type.__name__ = "Integer32"
_WfFrSwSigT303_Object = MibTableColumn
wfFrSwSigT303 = _WfFrSwSigT303_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 21),
    _WfFrSwSigT303_Type()
)
wfFrSwSigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT303.setStatus("mandatory")


class _WfFrSwSigT305_Type(Integer32):
    """Custom type wfFrSwSigT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 90),
    )


_WfFrSwSigT305_Type.__name__ = "Integer32"
_WfFrSwSigT305_Object = MibTableColumn
wfFrSwSigT305 = _WfFrSwSigT305_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 22),
    _WfFrSwSigT305_Type()
)
wfFrSwSigT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT305.setStatus("mandatory")


class _WfFrSwSigT308_Type(Integer32):
    """Custom type wfFrSwSigT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrSwSigT308_Type.__name__ = "Integer32"
_WfFrSwSigT308_Object = MibTableColumn
wfFrSwSigT308 = _WfFrSwSigT308_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 23),
    _WfFrSwSigT308_Type()
)
wfFrSwSigT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT308.setStatus("mandatory")


class _WfFrSwSigT310_Type(Integer32):
    """Custom type wfFrSwSigT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrSwSigT310_Type.__name__ = "Integer32"
_WfFrSwSigT310_Object = MibTableColumn
wfFrSwSigT310 = _WfFrSwSigT310_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 24),
    _WfFrSwSigT310_Type()
)
wfFrSwSigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT310.setStatus("mandatory")


class _WfFrSwSigT322_Type(Integer32):
    """Custom type wfFrSwSigT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrSwSigT322_Type.__name__ = "Integer32"
_WfFrSwSigT322_Object = MibTableColumn
wfFrSwSigT322 = _WfFrSwSigT322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 25),
    _WfFrSwSigT322_Type()
)
wfFrSwSigT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigT322.setStatus("mandatory")
_WfFrSwSigInSetupPkts_Type = Counter32
_WfFrSwSigInSetupPkts_Object = MibTableColumn
wfFrSwSigInSetupPkts = _WfFrSwSigInSetupPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 26),
    _WfFrSwSigInSetupPkts_Type()
)
wfFrSwSigInSetupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInSetupPkts.setStatus("mandatory")
_WfFrSwSigInCallProceedingPkts_Type = Counter32
_WfFrSwSigInCallProceedingPkts_Object = MibTableColumn
wfFrSwSigInCallProceedingPkts = _WfFrSwSigInCallProceedingPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 27),
    _WfFrSwSigInCallProceedingPkts_Type()
)
wfFrSwSigInCallProceedingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInCallProceedingPkts.setStatus("mandatory")
_WfFrSwSigInConnectPkts_Type = Counter32
_WfFrSwSigInConnectPkts_Object = MibTableColumn
wfFrSwSigInConnectPkts = _WfFrSwSigInConnectPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 28),
    _WfFrSwSigInConnectPkts_Type()
)
wfFrSwSigInConnectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInConnectPkts.setStatus("mandatory")
_WfFrSwSigInDisconnectPkts_Type = Counter32
_WfFrSwSigInDisconnectPkts_Object = MibTableColumn
wfFrSwSigInDisconnectPkts = _WfFrSwSigInDisconnectPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 29),
    _WfFrSwSigInDisconnectPkts_Type()
)
wfFrSwSigInDisconnectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInDisconnectPkts.setStatus("mandatory")
_WfFrSwSigInReleasePkts_Type = Counter32
_WfFrSwSigInReleasePkts_Object = MibTableColumn
wfFrSwSigInReleasePkts = _WfFrSwSigInReleasePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 30),
    _WfFrSwSigInReleasePkts_Type()
)
wfFrSwSigInReleasePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInReleasePkts.setStatus("mandatory")
_WfFrSwSigInReleaseCompletePkts_Type = Counter32
_WfFrSwSigInReleaseCompletePkts_Object = MibTableColumn
wfFrSwSigInReleaseCompletePkts = _WfFrSwSigInReleaseCompletePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 31),
    _WfFrSwSigInReleaseCompletePkts_Type()
)
wfFrSwSigInReleaseCompletePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInReleaseCompletePkts.setStatus("mandatory")
_WfFrSwSigInStatusEnquiryPkts_Type = Counter32
_WfFrSwSigInStatusEnquiryPkts_Object = MibTableColumn
wfFrSwSigInStatusEnquiryPkts = _WfFrSwSigInStatusEnquiryPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 32),
    _WfFrSwSigInStatusEnquiryPkts_Type()
)
wfFrSwSigInStatusEnquiryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInStatusEnquiryPkts.setStatus("mandatory")
_WfFrSwSigInStatusPkts_Type = Counter32
_WfFrSwSigInStatusPkts_Object = MibTableColumn
wfFrSwSigInStatusPkts = _WfFrSwSigInStatusPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 33),
    _WfFrSwSigInStatusPkts_Type()
)
wfFrSwSigInStatusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInStatusPkts.setStatus("mandatory")
_WfFrSwSigInUnknownPkts_Type = Counter32
_WfFrSwSigInUnknownPkts_Object = MibTableColumn
wfFrSwSigInUnknownPkts = _WfFrSwSigInUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 34),
    _WfFrSwSigInUnknownPkts_Type()
)
wfFrSwSigInUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigInUnknownPkts.setStatus("mandatory")
_WfFrSwSigOutSetupPkts_Type = Counter32
_WfFrSwSigOutSetupPkts_Object = MibTableColumn
wfFrSwSigOutSetupPkts = _WfFrSwSigOutSetupPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 35),
    _WfFrSwSigOutSetupPkts_Type()
)
wfFrSwSigOutSetupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutSetupPkts.setStatus("mandatory")
_WfFrSwSigOutCallProceedingPkts_Type = Counter32
_WfFrSwSigOutCallProceedingPkts_Object = MibTableColumn
wfFrSwSigOutCallProceedingPkts = _WfFrSwSigOutCallProceedingPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 36),
    _WfFrSwSigOutCallProceedingPkts_Type()
)
wfFrSwSigOutCallProceedingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutCallProceedingPkts.setStatus("mandatory")
_WfFrSwSigOutConnectPkts_Type = Counter32
_WfFrSwSigOutConnectPkts_Object = MibTableColumn
wfFrSwSigOutConnectPkts = _WfFrSwSigOutConnectPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 37),
    _WfFrSwSigOutConnectPkts_Type()
)
wfFrSwSigOutConnectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutConnectPkts.setStatus("mandatory")
_WfFrSwSigOutDisconnectPkts_Type = Counter32
_WfFrSwSigOutDisconnectPkts_Object = MibTableColumn
wfFrSwSigOutDisconnectPkts = _WfFrSwSigOutDisconnectPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 38),
    _WfFrSwSigOutDisconnectPkts_Type()
)
wfFrSwSigOutDisconnectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutDisconnectPkts.setStatus("mandatory")
_WfFrSwSigOutReleasePkts_Type = Counter32
_WfFrSwSigOutReleasePkts_Object = MibTableColumn
wfFrSwSigOutReleasePkts = _WfFrSwSigOutReleasePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 39),
    _WfFrSwSigOutReleasePkts_Type()
)
wfFrSwSigOutReleasePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutReleasePkts.setStatus("mandatory")
_WfFrSwSigOutReleaseCompletePkts_Type = Counter32
_WfFrSwSigOutReleaseCompletePkts_Object = MibTableColumn
wfFrSwSigOutReleaseCompletePkts = _WfFrSwSigOutReleaseCompletePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 40),
    _WfFrSwSigOutReleaseCompletePkts_Type()
)
wfFrSwSigOutReleaseCompletePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutReleaseCompletePkts.setStatus("mandatory")
_WfFrSwSigOutStatusEnquiryPkts_Type = Counter32
_WfFrSwSigOutStatusEnquiryPkts_Object = MibTableColumn
wfFrSwSigOutStatusEnquiryPkts = _WfFrSwSigOutStatusEnquiryPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 41),
    _WfFrSwSigOutStatusEnquiryPkts_Type()
)
wfFrSwSigOutStatusEnquiryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutStatusEnquiryPkts.setStatus("mandatory")
_WfFrSwSigOutStatusPkts_Type = Counter32
_WfFrSwSigOutStatusPkts_Object = MibTableColumn
wfFrSwSigOutStatusPkts = _WfFrSwSigOutStatusPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 42),
    _WfFrSwSigOutStatusPkts_Type()
)
wfFrSwSigOutStatusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigOutStatusPkts.setStatus("mandatory")
_WfFrSwSigRejectedConnRequests_Type = Counter32
_WfFrSwSigRejectedConnRequests_Object = MibTableColumn
wfFrSwSigRejectedConnRequests = _WfFrSwSigRejectedConnRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 43),
    _WfFrSwSigRejectedConnRequests_Type()
)
wfFrSwSigRejectedConnRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigRejectedConnRequests.setStatus("mandatory")
_WfFrSwSigNwrkAbortedConnections_Type = Counter32
_WfFrSwSigNwrkAbortedConnections_Object = MibTableColumn
wfFrSwSigNwrkAbortedConnections = _WfFrSwSigNwrkAbortedConnections_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 44),
    _WfFrSwSigNwrkAbortedConnections_Type()
)
wfFrSwSigNwrkAbortedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigNwrkAbortedConnections.setStatus("mandatory")
_WfFrSwSigL2Resets_Type = Counter32
_WfFrSwSigL2Resets_Object = MibTableColumn
wfFrSwSigL2Resets = _WfFrSwSigL2Resets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 45),
    _WfFrSwSigL2Resets_Type()
)
wfFrSwSigL2Resets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwSigL2Resets.setStatus("mandatory")


class _WfFrSwSigDlciIEAllowed_Type(Integer32):
    """Custom type wfFrSwSigDlciIEAllowed based on Integer32"""
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


_WfFrSwSigDlciIEAllowed_Type.__name__ = "Integer32"
_WfFrSwSigDlciIEAllowed_Object = MibTableColumn
wfFrSwSigDlciIEAllowed = _WfFrSwSigDlciIEAllowed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 46),
    _WfFrSwSigDlciIEAllowed_Type()
)
wfFrSwSigDlciIEAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigDlciIEAllowed.setStatus("mandatory")


class _WfFrSwSigX213PriorityIEAllowed_Type(Integer32):
    """Custom type wfFrSwSigX213PriorityIEAllowed based on Integer32"""
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


_WfFrSwSigX213PriorityIEAllowed_Type.__name__ = "Integer32"
_WfFrSwSigX213PriorityIEAllowed_Object = MibTableColumn
wfFrSwSigX213PriorityIEAllowed = _WfFrSwSigX213PriorityIEAllowed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 47),
    _WfFrSwSigX213PriorityIEAllowed_Type()
)
wfFrSwSigX213PriorityIEAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigX213PriorityIEAllowed.setStatus("mandatory")


class _WfFrSwSigMaximumBe_Type(Integer32):
    """Custom type wfFrSwSigMaximumBe based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSwSigMaximumBe_Type.__name__ = "Integer32"
_WfFrSwSigMaximumBe_Object = MibTableColumn
wfFrSwSigMaximumBe = _WfFrSwSigMaximumBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 12, 1, 48),
    _WfFrSwSigMaximumBe_Type()
)
wfFrSwSigMaximumBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwSigMaximumBe.setStatus("mandatory")
_WfFrSwGlobalE164AddrTable_Object = MibTable
wfFrSwGlobalE164AddrTable = _WfFrSwGlobalE164AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13)
)
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrTable.setStatus("mandatory")
_WfFrSwGlobalE164AddrEntry_Object = MibTableRow
wfFrSwGlobalE164AddrEntry = _WfFrSwGlobalE164AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13, 1)
)
wfFrSwGlobalE164AddrEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwGlobalE164AddrLow"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwGlobalE164AddrHigh"),
)
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrEntry.setStatus("mandatory")


class _WfFrSwGlobalE164AddrDelete_Type(Integer32):
    """Custom type wfFrSwGlobalE164AddrDelete based on Integer32"""
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


_WfFrSwGlobalE164AddrDelete_Type.__name__ = "Integer32"
_WfFrSwGlobalE164AddrDelete_Object = MibTableColumn
wfFrSwGlobalE164AddrDelete = _WfFrSwGlobalE164AddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13, 1, 1),
    _WfFrSwGlobalE164AddrDelete_Type()
)
wfFrSwGlobalE164AddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrDelete.setStatus("mandatory")
_WfFrSwGlobalE164AddrLow_Type = OctetString
_WfFrSwGlobalE164AddrLow_Object = MibTableColumn
wfFrSwGlobalE164AddrLow = _WfFrSwGlobalE164AddrLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13, 1, 2),
    _WfFrSwGlobalE164AddrLow_Type()
)
wfFrSwGlobalE164AddrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrLow.setStatus("mandatory")
_WfFrSwGlobalE164AddrHigh_Type = OctetString
_WfFrSwGlobalE164AddrHigh_Object = MibTableColumn
wfFrSwGlobalE164AddrHigh = _WfFrSwGlobalE164AddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13, 1, 3),
    _WfFrSwGlobalE164AddrHigh_Type()
)
wfFrSwGlobalE164AddrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrHigh.setStatus("mandatory")
_WfFrSwGlobalE164AddrIPAddr_Type = IpAddress
_WfFrSwGlobalE164AddrIPAddr_Object = MibTableColumn
wfFrSwGlobalE164AddrIPAddr = _WfFrSwGlobalE164AddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 13, 1, 4),
    _WfFrSwGlobalE164AddrIPAddr_Type()
)
wfFrSwGlobalE164AddrIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwGlobalE164AddrIPAddr.setStatus("mandatory")
_WfFrSwGlobalX121AddrTable_Object = MibTable
wfFrSwGlobalX121AddrTable = _WfFrSwGlobalX121AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14)
)
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrTable.setStatus("mandatory")
_WfFrSwGlobalX121AddrEntry_Object = MibTableRow
wfFrSwGlobalX121AddrEntry = _WfFrSwGlobalX121AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14, 1)
)
wfFrSwGlobalX121AddrEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwGlobalX121AddrLow"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwGlobalX121AddrHigh"),
)
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrEntry.setStatus("mandatory")


class _WfFrSwGlobalX121AddrDelete_Type(Integer32):
    """Custom type wfFrSwGlobalX121AddrDelete based on Integer32"""
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


_WfFrSwGlobalX121AddrDelete_Type.__name__ = "Integer32"
_WfFrSwGlobalX121AddrDelete_Object = MibTableColumn
wfFrSwGlobalX121AddrDelete = _WfFrSwGlobalX121AddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14, 1, 1),
    _WfFrSwGlobalX121AddrDelete_Type()
)
wfFrSwGlobalX121AddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrDelete.setStatus("mandatory")
_WfFrSwGlobalX121AddrLow_Type = OctetString
_WfFrSwGlobalX121AddrLow_Object = MibTableColumn
wfFrSwGlobalX121AddrLow = _WfFrSwGlobalX121AddrLow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14, 1, 2),
    _WfFrSwGlobalX121AddrLow_Type()
)
wfFrSwGlobalX121AddrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrLow.setStatus("mandatory")
_WfFrSwGlobalX121AddrHigh_Type = OctetString
_WfFrSwGlobalX121AddrHigh_Object = MibTableColumn
wfFrSwGlobalX121AddrHigh = _WfFrSwGlobalX121AddrHigh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14, 1, 3),
    _WfFrSwGlobalX121AddrHigh_Type()
)
wfFrSwGlobalX121AddrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrHigh.setStatus("mandatory")
_WfFrSwGlobalX121AddrIPAddr_Type = IpAddress
_WfFrSwGlobalX121AddrIPAddr_Object = MibTableColumn
wfFrSwGlobalX121AddrIPAddr = _WfFrSwGlobalX121AddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 14, 1, 4),
    _WfFrSwGlobalX121AddrIPAddr_Type()
)
wfFrSwGlobalX121AddrIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwGlobalX121AddrIPAddr.setStatus("mandatory")
_WfFrSwLocalE164AddrTable_Object = MibTable
wfFrSwLocalE164AddrTable = _WfFrSwLocalE164AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15)
)
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrTable.setStatus("mandatory")
_WfFrSwLocalE164AddrEntry_Object = MibTableRow
wfFrSwLocalE164AddrEntry = _WfFrSwLocalE164AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1)
)
wfFrSwLocalE164AddrEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwLocalE164AddrCct"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwLocalE164Address"),
)
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrEntry.setStatus("mandatory")


class _WfFrSwLocalE164AddrDelete_Type(Integer32):
    """Custom type wfFrSwLocalE164AddrDelete based on Integer32"""
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


_WfFrSwLocalE164AddrDelete_Type.__name__ = "Integer32"
_WfFrSwLocalE164AddrDelete_Object = MibTableColumn
wfFrSwLocalE164AddrDelete = _WfFrSwLocalE164AddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1, 1),
    _WfFrSwLocalE164AddrDelete_Type()
)
wfFrSwLocalE164AddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrDelete.setStatus("mandatory")
_WfFrSwLocalE164AddrCct_Type = Integer32
_WfFrSwLocalE164AddrCct_Object = MibTableColumn
wfFrSwLocalE164AddrCct = _WfFrSwLocalE164AddrCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1, 2),
    _WfFrSwLocalE164AddrCct_Type()
)
wfFrSwLocalE164AddrCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrCct.setStatus("mandatory")
_WfFrSwLocalE164Address_Type = OctetString
_WfFrSwLocalE164Address_Object = MibTableColumn
wfFrSwLocalE164Address = _WfFrSwLocalE164Address_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1, 3),
    _WfFrSwLocalE164Address_Type()
)
wfFrSwLocalE164Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwLocalE164Address.setStatus("mandatory")
_WfFrSwLocalE164AddrCUG_Type = OctetString
_WfFrSwLocalE164AddrCUG_Object = MibTableColumn
wfFrSwLocalE164AddrCUG = _WfFrSwLocalE164AddrCUG_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1, 4),
    _WfFrSwLocalE164AddrCUG_Type()
)
wfFrSwLocalE164AddrCUG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrCUG.setStatus("mandatory")


class _WfFrSwLocalE164AddrLocalFlag_Type(Integer32):
    """Custom type wfFrSwLocalE164AddrLocalFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("nonlocal", 2))
    )


_WfFrSwLocalE164AddrLocalFlag_Type.__name__ = "Integer32"
_WfFrSwLocalE164AddrLocalFlag_Object = MibTableColumn
wfFrSwLocalE164AddrLocalFlag = _WfFrSwLocalE164AddrLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 15, 1, 5),
    _WfFrSwLocalE164AddrLocalFlag_Type()
)
wfFrSwLocalE164AddrLocalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalE164AddrLocalFlag.setStatus("mandatory")
_WfFrSwLocalX121AddrTable_Object = MibTable
wfFrSwLocalX121AddrTable = _WfFrSwLocalX121AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16)
)
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrTable.setStatus("mandatory")
_WfFrSwLocalX121AddrEntry_Object = MibTableRow
wfFrSwLocalX121AddrEntry = _WfFrSwLocalX121AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1)
)
wfFrSwLocalX121AddrEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwLocalX121AddrCct"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwLocalX121Address"),
)
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrEntry.setStatus("mandatory")


class _WfFrSwLocalX121AddrDelete_Type(Integer32):
    """Custom type wfFrSwLocalX121AddrDelete based on Integer32"""
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


_WfFrSwLocalX121AddrDelete_Type.__name__ = "Integer32"
_WfFrSwLocalX121AddrDelete_Object = MibTableColumn
wfFrSwLocalX121AddrDelete = _WfFrSwLocalX121AddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1, 1),
    _WfFrSwLocalX121AddrDelete_Type()
)
wfFrSwLocalX121AddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrDelete.setStatus("mandatory")
_WfFrSwLocalX121AddrCct_Type = Integer32
_WfFrSwLocalX121AddrCct_Object = MibTableColumn
wfFrSwLocalX121AddrCct = _WfFrSwLocalX121AddrCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1, 2),
    _WfFrSwLocalX121AddrCct_Type()
)
wfFrSwLocalX121AddrCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrCct.setStatus("mandatory")
_WfFrSwLocalX121Address_Type = OctetString
_WfFrSwLocalX121Address_Object = MibTableColumn
wfFrSwLocalX121Address = _WfFrSwLocalX121Address_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1, 3),
    _WfFrSwLocalX121Address_Type()
)
wfFrSwLocalX121Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwLocalX121Address.setStatus("mandatory")
_WfFrSwLocalX121AddrCUG_Type = OctetString
_WfFrSwLocalX121AddrCUG_Object = MibTableColumn
wfFrSwLocalX121AddrCUG = _WfFrSwLocalX121AddrCUG_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1, 4),
    _WfFrSwLocalX121AddrCUG_Type()
)
wfFrSwLocalX121AddrCUG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrCUG.setStatus("mandatory")


class _WfFrSwLocalX121AddrLocalFlag_Type(Integer32):
    """Custom type wfFrSwLocalX121AddrLocalFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("nonlocal", 2))
    )


_WfFrSwLocalX121AddrLocalFlag_Type.__name__ = "Integer32"
_WfFrSwLocalX121AddrLocalFlag_Object = MibTableColumn
wfFrSwLocalX121AddrLocalFlag = _WfFrSwLocalX121AddrLocalFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 16, 1, 5),
    _WfFrSwLocalX121AddrLocalFlag_Type()
)
wfFrSwLocalX121AddrLocalFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwLocalX121AddrLocalFlag.setStatus("mandatory")
_WfFrSwBase_ObjectIdentity = ObjectIdentity
wfFrSwBase = _WfFrSwBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 17)
)


class _WfFrSwBaseDelete_Type(Integer32):
    """Custom type wfFrSwBaseDelete based on Integer32"""
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


_WfFrSwBaseDelete_Type.__name__ = "Integer32"
_WfFrSwBaseDelete_Object = MibScalar
wfFrSwBaseDelete = _WfFrSwBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 17, 1),
    _WfFrSwBaseDelete_Type()
)
wfFrSwBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwBaseDelete.setStatus("mandatory")
_WfFrSwBaseIpAddr_Type = IpAddress
_WfFrSwBaseIpAddr_Object = MibScalar
wfFrSwBaseIpAddr = _WfFrSwBaseIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 17, 2),
    _WfFrSwBaseIpAddr_Type()
)
wfFrSwBaseIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwBaseIpAddr.setStatus("mandatory")
_WfFrSwBaseShutDown_Type = Counter32
_WfFrSwBaseShutDown_Object = MibScalar
wfFrSwBaseShutDown = _WfFrSwBaseShutDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 17, 3),
    _WfFrSwBaseShutDown_Type()
)
wfFrSwBaseShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwBaseShutDown.setStatus("mandatory")
_WfFrSwCngcMonTable_Object = MibTable
wfFrSwCngcMonTable = _WfFrSwCngcMonTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18)
)
if mibBuilder.loadTexts:
    wfFrSwCngcMonTable.setStatus("mandatory")
_WfFrSwCngcMonEntry_Object = MibTableRow
wfFrSwCngcMonEntry = _WfFrSwCngcMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1)
)
wfFrSwCngcMonEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwCngcMonCct"),
)
if mibBuilder.loadTexts:
    wfFrSwCngcMonEntry.setStatus("mandatory")
_WfFrSwCngcMonReset_Type = Integer32
_WfFrSwCngcMonReset_Object = MibTableColumn
wfFrSwCngcMonReset = _WfFrSwCngcMonReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 1),
    _WfFrSwCngcMonReset_Type()
)
wfFrSwCngcMonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwCngcMonReset.setStatus("mandatory")
_WfFrSwCngcMonCct_Type = Integer32
_WfFrSwCngcMonCct_Object = MibTableColumn
wfFrSwCngcMonCct = _WfFrSwCngcMonCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 2),
    _WfFrSwCngcMonCct_Type()
)
wfFrSwCngcMonCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonCct.setStatus("mandatory")
_WfFrSwCngcMonP0Level1Percent_Type = Gauge32
_WfFrSwCngcMonP0Level1Percent_Object = MibTableColumn
wfFrSwCngcMonP0Level1Percent = _WfFrSwCngcMonP0Level1Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 3),
    _WfFrSwCngcMonP0Level1Percent_Type()
)
wfFrSwCngcMonP0Level1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP0Level1Percent.setStatus("mandatory")
_WfFrSwCngcMonP0Level2Percent_Type = Gauge32
_WfFrSwCngcMonP0Level2Percent_Object = MibTableColumn
wfFrSwCngcMonP0Level2Percent = _WfFrSwCngcMonP0Level2Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 4),
    _WfFrSwCngcMonP0Level2Percent_Type()
)
wfFrSwCngcMonP0Level2Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP0Level2Percent.setStatus("mandatory")
_WfFrSwCngcMonP0Level3Percent_Type = Gauge32
_WfFrSwCngcMonP0Level3Percent_Object = MibTableColumn
wfFrSwCngcMonP0Level3Percent = _WfFrSwCngcMonP0Level3Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 5),
    _WfFrSwCngcMonP0Level3Percent_Type()
)
wfFrSwCngcMonP0Level3Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP0Level3Percent.setStatus("mandatory")
_WfFrSwCngcMonP0Level4Percent_Type = Gauge32
_WfFrSwCngcMonP0Level4Percent_Object = MibTableColumn
wfFrSwCngcMonP0Level4Percent = _WfFrSwCngcMonP0Level4Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 6),
    _WfFrSwCngcMonP0Level4Percent_Type()
)
wfFrSwCngcMonP0Level4Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP0Level4Percent.setStatus("mandatory")
_WfFrSwCngcMonP1Level1Percent_Type = Gauge32
_WfFrSwCngcMonP1Level1Percent_Object = MibTableColumn
wfFrSwCngcMonP1Level1Percent = _WfFrSwCngcMonP1Level1Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 7),
    _WfFrSwCngcMonP1Level1Percent_Type()
)
wfFrSwCngcMonP1Level1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP1Level1Percent.setStatus("mandatory")
_WfFrSwCngcMonP1Level2Percent_Type = Gauge32
_WfFrSwCngcMonP1Level2Percent_Object = MibTableColumn
wfFrSwCngcMonP1Level2Percent = _WfFrSwCngcMonP1Level2Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 8),
    _WfFrSwCngcMonP1Level2Percent_Type()
)
wfFrSwCngcMonP1Level2Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP1Level2Percent.setStatus("mandatory")
_WfFrSwCngcMonP1Level3Percent_Type = Gauge32
_WfFrSwCngcMonP1Level3Percent_Object = MibTableColumn
wfFrSwCngcMonP1Level3Percent = _WfFrSwCngcMonP1Level3Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 9),
    _WfFrSwCngcMonP1Level3Percent_Type()
)
wfFrSwCngcMonP1Level3Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP1Level3Percent.setStatus("mandatory")
_WfFrSwCngcMonP1Level4Percent_Type = Gauge32
_WfFrSwCngcMonP1Level4Percent_Object = MibTableColumn
wfFrSwCngcMonP1Level4Percent = _WfFrSwCngcMonP1Level4Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 10),
    _WfFrSwCngcMonP1Level4Percent_Type()
)
wfFrSwCngcMonP1Level4Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP1Level4Percent.setStatus("mandatory")
_WfFrSwCngcMonP2Level1Percent_Type = Gauge32
_WfFrSwCngcMonP2Level1Percent_Object = MibTableColumn
wfFrSwCngcMonP2Level1Percent = _WfFrSwCngcMonP2Level1Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 11),
    _WfFrSwCngcMonP2Level1Percent_Type()
)
wfFrSwCngcMonP2Level1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP2Level1Percent.setStatus("mandatory")
_WfFrSwCngcMonP2Level2Percent_Type = Gauge32
_WfFrSwCngcMonP2Level2Percent_Object = MibTableColumn
wfFrSwCngcMonP2Level2Percent = _WfFrSwCngcMonP2Level2Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 12),
    _WfFrSwCngcMonP2Level2Percent_Type()
)
wfFrSwCngcMonP2Level2Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP2Level2Percent.setStatus("mandatory")
_WfFrSwCngcMonP2Level3Percent_Type = Gauge32
_WfFrSwCngcMonP2Level3Percent_Object = MibTableColumn
wfFrSwCngcMonP2Level3Percent = _WfFrSwCngcMonP2Level3Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 13),
    _WfFrSwCngcMonP2Level3Percent_Type()
)
wfFrSwCngcMonP2Level3Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP2Level3Percent.setStatus("mandatory")
_WfFrSwCngcMonP2Level4Percent_Type = Gauge32
_WfFrSwCngcMonP2Level4Percent_Object = MibTableColumn
wfFrSwCngcMonP2Level4Percent = _WfFrSwCngcMonP2Level4Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 14),
    _WfFrSwCngcMonP2Level4Percent_Type()
)
wfFrSwCngcMonP2Level4Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP2Level4Percent.setStatus("mandatory")
_WfFrSwCngcMonP3Level1Percent_Type = Gauge32
_WfFrSwCngcMonP3Level1Percent_Object = MibTableColumn
wfFrSwCngcMonP3Level1Percent = _WfFrSwCngcMonP3Level1Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 15),
    _WfFrSwCngcMonP3Level1Percent_Type()
)
wfFrSwCngcMonP3Level1Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP3Level1Percent.setStatus("mandatory")
_WfFrSwCngcMonP3Level2Percent_Type = Gauge32
_WfFrSwCngcMonP3Level2Percent_Object = MibTableColumn
wfFrSwCngcMonP3Level2Percent = _WfFrSwCngcMonP3Level2Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 16),
    _WfFrSwCngcMonP3Level2Percent_Type()
)
wfFrSwCngcMonP3Level2Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP3Level2Percent.setStatus("mandatory")
_WfFrSwCngcMonP3Level3Percent_Type = Gauge32
_WfFrSwCngcMonP3Level3Percent_Object = MibTableColumn
wfFrSwCngcMonP3Level3Percent = _WfFrSwCngcMonP3Level3Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 17),
    _WfFrSwCngcMonP3Level3Percent_Type()
)
wfFrSwCngcMonP3Level3Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP3Level3Percent.setStatus("mandatory")
_WfFrSwCngcMonP3Level4Percent_Type = Gauge32
_WfFrSwCngcMonP3Level4Percent_Object = MibTableColumn
wfFrSwCngcMonP3Level4Percent = _WfFrSwCngcMonP3Level4Percent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 18, 1, 18),
    _WfFrSwCngcMonP3Level4Percent_Type()
)
wfFrSwCngcMonP3Level4Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwCngcMonP3Level4Percent.setStatus("mandatory")
_WfFrSwVirtualIntfTable_Object = MibTable
wfFrSwVirtualIntfTable = _WfFrSwVirtualIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19)
)
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfTable.setStatus("mandatory")
_WfFrSwVirtualIntfEntry_Object = MibTableRow
wfFrSwVirtualIntfEntry = _WfFrSwVirtualIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19, 1)
)
wfFrSwVirtualIntfEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwVirtualIntfSlot"),
    (0, "Wellfleet-FRSW-MIB", "wfFrSwVirtualIntfCct"),
)
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfEntry.setStatus("mandatory")


class _WfFrSwVirtualIntfDelete_Type(Integer32):
    """Custom type wfFrSwVirtualIntfDelete based on Integer32"""
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


_WfFrSwVirtualIntfDelete_Type.__name__ = "Integer32"
_WfFrSwVirtualIntfDelete_Object = MibTableColumn
wfFrSwVirtualIntfDelete = _WfFrSwVirtualIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19, 1, 1),
    _WfFrSwVirtualIntfDelete_Type()
)
wfFrSwVirtualIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfDelete.setStatus("mandatory")
_WfFrSwVirtualIntfSlot_Type = Integer32
_WfFrSwVirtualIntfSlot_Object = MibTableColumn
wfFrSwVirtualIntfSlot = _WfFrSwVirtualIntfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19, 1, 2),
    _WfFrSwVirtualIntfSlot_Type()
)
wfFrSwVirtualIntfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfSlot.setStatus("mandatory")
_WfFrSwVirtualIntfCct_Type = Integer32
_WfFrSwVirtualIntfCct_Object = MibTableColumn
wfFrSwVirtualIntfCct = _WfFrSwVirtualIntfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19, 1, 3),
    _WfFrSwVirtualIntfCct_Type()
)
wfFrSwVirtualIntfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfCct.setStatus("mandatory")
_WfFrSwVirtualIntfLineNum_Type = Integer32
_WfFrSwVirtualIntfLineNum_Object = MibTableColumn
wfFrSwVirtualIntfLineNum = _WfFrSwVirtualIntfLineNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 19, 1, 4),
    _WfFrSwVirtualIntfLineNum_Type()
)
wfFrSwVirtualIntfLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwVirtualIntfLineNum.setStatus("mandatory")
_WfFrSwExtFileSysTable_Object = MibTable
wfFrSwExtFileSysTable = _WfFrSwExtFileSysTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20)
)
if mibBuilder.loadTexts:
    wfFrSwExtFileSysTable.setStatus("mandatory")
_WfFrSwExtFileSysEntry_Object = MibTableRow
wfFrSwExtFileSysEntry = _WfFrSwExtFileSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1)
)
wfFrSwExtFileSysEntry.setIndexNames(
    (0, "Wellfleet-FRSW-MIB", "wfFrSwExtFileSysSlot"),
)
if mibBuilder.loadTexts:
    wfFrSwExtFileSysEntry.setStatus("mandatory")


class _WfFrSwExtFileSysDelete_Type(Integer32):
    """Custom type wfFrSwExtFileSysDelete based on Integer32"""
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


_WfFrSwExtFileSysDelete_Type.__name__ = "Integer32"
_WfFrSwExtFileSysDelete_Object = MibTableColumn
wfFrSwExtFileSysDelete = _WfFrSwExtFileSysDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1, 1),
    _WfFrSwExtFileSysDelete_Type()
)
wfFrSwExtFileSysDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwExtFileSysDelete.setStatus("mandatory")
_WfFrSwExtFileSysSlot_Type = Integer32
_WfFrSwExtFileSysSlot_Object = MibTableColumn
wfFrSwExtFileSysSlot = _WfFrSwExtFileSysSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1, 2),
    _WfFrSwExtFileSysSlot_Type()
)
wfFrSwExtFileSysSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwExtFileSysSlot.setStatus("mandatory")


class _WfFrSwExtFileSysSize_Type(Integer32):
    """Custom type wfFrSwExtFileSysSize based on Integer32"""
    defaultValue = 0


_WfFrSwExtFileSysSize_Object = MibTableColumn
wfFrSwExtFileSysSize = _WfFrSwExtFileSysSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1, 3),
    _WfFrSwExtFileSysSize_Type()
)
wfFrSwExtFileSysSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSwExtFileSysSize.setStatus("mandatory")


class _WfFrSwExtFileSysActualSize_Type(Integer32):
    """Custom type wfFrSwExtFileSysActualSize based on Integer32"""
    defaultValue = 0


_WfFrSwExtFileSysActualSize_Object = MibTableColumn
wfFrSwExtFileSysActualSize = _WfFrSwExtFileSysActualSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1, 4),
    _WfFrSwExtFileSysActualSize_Type()
)
wfFrSwExtFileSysActualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwExtFileSysActualSize.setStatus("mandatory")


class _WfFrSwExtFileSysState_Type(Integer32):
    """Custom type wfFrSwExtFileSysState based on Integer32"""
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
        *(("fault", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfFrSwExtFileSysState_Type.__name__ = "Integer32"
_WfFrSwExtFileSysState_Object = MibTableColumn
wfFrSwExtFileSysState = _WfFrSwExtFileSysState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 6, 20, 1, 5),
    _WfFrSwExtFileSysState_Type()
)
wfFrSwExtFileSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSwExtFileSysState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FRSW-MIB",
    **{"wfFrSwDlcmiTable": wfFrSwDlcmiTable,
       "wfFrSwDlcmiEntry": wfFrSwDlcmiEntry,
       "wfFrSwDlcmiDelete": wfFrSwDlcmiDelete,
       "wfFrSwDlcmiState": wfFrSwDlcmiState,
       "wfFrSwDlcmiNniEnable": wfFrSwDlcmiNniEnable,
       "wfFrSwDlcmiCircuit": wfFrSwDlcmiCircuit,
       "wfFrSwDlcmiManagementType": wfFrSwDlcmiManagementType,
       "wfFrSwL3NetAddress": wfFrSwL3NetAddress,
       "wfFrSwDlcmiAddressLen": wfFrSwDlcmiAddressLen,
       "wfFrSwDlcmiControlByteDisable": wfFrSwDlcmiControlByteDisable,
       "wfFrSwDlcmiPollingInterval": wfFrSwDlcmiPollingInterval,
       "wfFrSwDlcmiFullEnquiryInterval": wfFrSwDlcmiFullEnquiryInterval,
       "wfFrSwDlcmiErrorThreshold": wfFrSwDlcmiErrorThreshold,
       "wfFrSwDlcmiMonitoredEvents": wfFrSwDlcmiMonitoredEvents,
       "wfFrSwDlcmiRecoveryCounts": wfFrSwDlcmiRecoveryCounts,
       "wfFrSwDlcmiMaxSupportedVCs": wfFrSwDlcmiMaxSupportedVCs,
       "wfFrSwDlcmiVCsInUse": wfFrSwDlcmiVCsInUse,
       "wfFrSwSwitchHdrErrors": wfFrSwSwitchHdrErrors,
       "wfFrSwDlcmiSequenceCount": wfFrSwDlcmiSequenceCount,
       "wfFrSwDlcmiLastReceived": wfFrSwDlcmiLastReceived,
       "wfFrSwDlcmiActiveSeqCount": wfFrSwDlcmiActiveSeqCount,
       "wfFrSwDlcmiActiveReceived": wfFrSwDlcmiActiveReceived,
       "wfFrSwDlcmiPolls": wfFrSwDlcmiPolls,
       "wfFrSwDlcmiAlarmTimer": wfFrSwDlcmiAlarmTimer,
       "wfFrSwErrType": wfFrSwErrType,
       "wfFrSwErrData": wfFrSwErrData,
       "wfFrSwErrTime": wfFrSwErrTime,
       "wfFrSwBcMeasurementInterval": wfFrSwBcMeasurementInterval,
       "wfFrSwDlcmiMcastNoBufferErrors": wfFrSwDlcmiMcastNoBufferErrors,
       "wfFrSwDlcmiFrameTooShortErrors": wfFrSwDlcmiFrameTooShortErrors,
       "wfFrSwDlcmiFrameTooLongErrors": wfFrSwDlcmiFrameTooLongErrors,
       "wfFrSwDlcmiIllegalDlciErrors": wfFrSwDlcmiIllegalDlciErrors,
       "wfFrSwDlcmiUnknownDlciErrors": wfFrSwDlcmiUnknownDlciErrors,
       "wfFrSwDlcmiProtocolErrors": wfFrSwDlcmiProtocolErrors,
       "wfFrSwDlcmiUnknownIEErrors": wfFrSwDlcmiUnknownIEErrors,
       "wfFrSwDlcmiSequenceErrors": wfFrSwDlcmiSequenceErrors,
       "wfFrSwDlcmiUnknownRPTErrors": wfFrSwDlcmiUnknownRPTErrors,
       "wfFrSwDlcmiControlByteErrors": wfFrSwDlcmiControlByteErrors,
       "wfFrSwDlcmiFormatErrors": wfFrSwDlcmiFormatErrors,
       "wfFrSwDlcmiOtherErrors": wfFrSwDlcmiOtherErrors,
       "wfFrSwDlcmiStatus": wfFrSwDlcmiStatus,
       "wfFrSwDlcmiNewVCs": wfFrSwDlcmiNewVCs,
       "wfFrSwDlcmiDeletedVCs": wfFrSwDlcmiDeletedVCs,
       "wfFrSwDlcmiFullStatusSeq": wfFrSwDlcmiFullStatusSeq,
       "wfFrSwDlcmiBidirect": wfFrSwDlcmiBidirect,
       "wfFrSwDlcmiDteStatus": wfFrSwDlcmiDteStatus,
       "wfFrSwDlcmiDteSeqCount": wfFrSwDlcmiDteSeqCount,
       "wfFrSwDlcmiDteReceived": wfFrSwDlcmiDteReceived,
       "wfFrSwDlcmiDteLastReceived": wfFrSwDlcmiDteLastReceived,
       "wfFrSwDlcmiDtePolls": wfFrSwDlcmiDtePolls,
       "wfFrSwDlcmiDtePollingInterval": wfFrSwDlcmiDtePollingInterval,
       "wfFrSwDlcmiDteFullEnquiryInterval": wfFrSwDlcmiDteFullEnquiryInterval,
       "wfFrSwDlcmiDteErrorThreshold": wfFrSwDlcmiDteErrorThreshold,
       "wfFrSwDlcmiCrossNetEnable": wfFrSwDlcmiCrossNetEnable,
       "wfFrSwDlcmiCrossNetPollingInterval": wfFrSwDlcmiCrossNetPollingInterval,
       "wfFrSwDlcmiCrossNetErrorThreshold": wfFrSwDlcmiCrossNetErrorThreshold,
       "wfFrSwDlcmiCrossNetAsyncUpdateEnable": wfFrSwDlcmiCrossNetAsyncUpdateEnable,
       "wfFrSwDlcmiBcMeasurementEnable": wfFrSwDlcmiBcMeasurementEnable,
       "wfFrSwDlcmiAsyncUpdateEnable": wfFrSwDlcmiAsyncUpdateEnable,
       "wfFrSwDlcmiCrossNetListenEnable": wfFrSwDlcmiCrossNetListenEnable,
       "wfFrSwDlcmiSvcDisable": wfFrSwDlcmiSvcDisable,
       "wfFrSwDlcmiL2AddrType": wfFrSwDlcmiL2AddrType,
       "wfFrSwDlcmiEscapeMode": wfFrSwDlcmiEscapeMode,
       "wfFrSwDlcmiEscapeCircuit": wfFrSwDlcmiEscapeCircuit,
       "wfFrSwDlcmiEscapeVcCount": wfFrSwDlcmiEscapeVcCount,
       "wfFrSwDlcmiIwfMode": wfFrSwDlcmiIwfMode,
       "wfFrSwDlcmiSvcBillingEnable": wfFrSwDlcmiSvcBillingEnable,
       "wfFrSwDlcmiSpvcAgent": wfFrSwDlcmiSpvcAgent,
       "wfFrSwDlcmiCallAccDlciSelectionType": wfFrSwDlcmiCallAccDlciSelectionType,
       "wfFrSwCctTable": wfFrSwCctTable,
       "wfFrSwCctEntry": wfFrSwCctEntry,
       "wfFrSwCctDelete": wfFrSwCctDelete,
       "wfFrSwCctNumber": wfFrSwCctNumber,
       "wfFrSwCctDlci": wfFrSwCctDlci,
       "wfFrSwCctState": wfFrSwCctState,
       "wfFrSwCctMulticast": wfFrSwCctMulticast,
       "wfFrSwCctInBc": wfFrSwCctInBc,
       "wfFrSwCctOutBc": wfFrSwCctOutBc,
       "wfFrSwCctInBe": wfFrSwCctInBe,
       "wfFrSwCctOutBe": wfFrSwCctOutBe,
       "wfFrSwCctInThroughput": wfFrSwCctInThroughput,
       "wfFrSwCctOutThroughput": wfFrSwCctOutThroughput,
       "wfFrSwCctCreationTime": wfFrSwCctCreationTime,
       "wfFrSwCctLastTimeChange": wfFrSwCctLastTimeChange,
       "wfFrSwCctLocalSentNonDEFrames": wfFrSwCctLocalSentNonDEFrames,
       "wfFrSwCctLocalSentNonDEOctets": wfFrSwCctLocalSentNonDEOctets,
       "wfFrSwCctLocalSentDEFrames": wfFrSwCctLocalSentDEFrames,
       "wfFrSwCctLocalSentDEOctets": wfFrSwCctLocalSentDEOctets,
       "wfFrSwCctLocalSetFECNFrames": wfFrSwCctLocalSetFECNFrames,
       "wfFrSwCctLocalSetFECNOctets": wfFrSwCctLocalSetFECNOctets,
       "wfFrSwCctLocalSetBECNFrames": wfFrSwCctLocalSetBECNFrames,
       "wfFrSwCctLocalSetBECNOctets": wfFrSwCctLocalSetBECNOctets,
       "wfFrSwCctLocalSetDEFrames": wfFrSwCctLocalSetDEFrames,
       "wfFrSwCctLocalSetDEOctets": wfFrSwCctLocalSetDEOctets,
       "wfFrSwCctLocalDropNonDEFrames": wfFrSwCctLocalDropNonDEFrames,
       "wfFrSwCctLocalDropNonDEOctets": wfFrSwCctLocalDropNonDEOctets,
       "wfFrSwCctLocalDropDEFrames": wfFrSwCctLocalDropDEFrames,
       "wfFrSwCctLocalDropDEOctets": wfFrSwCctLocalDropDEOctets,
       "wfFrSwCctInactiveVCDropFrames": wfFrSwCctInactiveVCDropFrames,
       "wfFrSwCctInactiveVCDropOctets": wfFrSwCctInactiveVCDropOctets,
       "wfFrSwCctLocalRecvNonDEFrames": wfFrSwCctLocalRecvNonDEFrames,
       "wfFrSwCctLocalRecvNonDEOctets": wfFrSwCctLocalRecvNonDEOctets,
       "wfFrSwCctLocalRecvDEFrames": wfFrSwCctLocalRecvDEFrames,
       "wfFrSwCctLocalRecvDEOctets": wfFrSwCctLocalRecvDEOctets,
       "wfFrSwCctLocalRecvFECNFrames": wfFrSwCctLocalRecvFECNFrames,
       "wfFrSwCctLocalRecvFECNOctets": wfFrSwCctLocalRecvFECNOctets,
       "wfFrSwCctLocalRecvBECNFrames": wfFrSwCctLocalRecvBECNFrames,
       "wfFrSwCctLocalRecvBECNOctets": wfFrSwCctLocalRecvBECNOctets,
       "wfFrSwCctLocalRecentNonDEOctets": wfFrSwCctLocalRecentNonDEOctets,
       "wfFrSwCctRemoteSentNonDEFrames": wfFrSwCctRemoteSentNonDEFrames,
       "wfFrSwCctRemoteSentNonDEOctets": wfFrSwCctRemoteSentNonDEOctets,
       "wfFrSwCctRemoteSentDEFrames": wfFrSwCctRemoteSentDEFrames,
       "wfFrSwCctRemoteSentDEOctets": wfFrSwCctRemoteSentDEOctets,
       "wfFrSwCctRemoteSetFECNFrames": wfFrSwCctRemoteSetFECNFrames,
       "wfFrSwCctRemoteSetFECNOctets": wfFrSwCctRemoteSetFECNOctets,
       "wfFrSwCctRemoteSetBECNFrames": wfFrSwCctRemoteSetBECNFrames,
       "wfFrSwCctRemoteSetBECNOctets": wfFrSwCctRemoteSetBECNOctets,
       "wfFrSwCctRemoteDropNonDEFrames": wfFrSwCctRemoteDropNonDEFrames,
       "wfFrSwCctRemoteDropNonDEOctets": wfFrSwCctRemoteDropNonDEOctets,
       "wfFrSwCctRemoteDropDEFrames": wfFrSwCctRemoteDropDEFrames,
       "wfFrSwCctRemoteDropDEOctets": wfFrSwCctRemoteDropDEOctets,
       "wfFrSwCctRemoteRecvNonDEFrames": wfFrSwCctRemoteRecvNonDEFrames,
       "wfFrSwCctRemoteRecvNonDEOctets": wfFrSwCctRemoteRecvNonDEOctets,
       "wfFrSwCctRemoteRecvDEFrames": wfFrSwCctRemoteRecvDEFrames,
       "wfFrSwCctRemoteRecvDEOctets": wfFrSwCctRemoteRecvDEOctets,
       "wfFrSwCctRemoteRecvFECNFrames": wfFrSwCctRemoteRecvFECNFrames,
       "wfFrSwCctRemoteRecvFECNOctets": wfFrSwCctRemoteRecvFECNOctets,
       "wfFrSwCctRemoteRecvBECNFrames": wfFrSwCctRemoteRecvBECNFrames,
       "wfFrSwCctRemoteRecvBECNOctets": wfFrSwCctRemoteRecvBECNOctets,
       "wfFrSwCctLocalBecnState": wfFrSwCctLocalBecnState,
       "wfFrSwCctRemoteBecnState": wfFrSwCctRemoteBecnState,
       "wfFrSwCctLocalOrRemoteConnection": wfFrSwCctLocalOrRemoteConnection,
       "wfFrSwCctInBcOctets": wfFrSwCctInBcOctets,
       "wfFrSwCctStateSet": wfFrSwCctStateSet,
       "wfFrSwCctReportedStatus": wfFrSwCctReportedStatus,
       "wfFrSwCctReceivedStatus": wfFrSwCctReceivedStatus,
       "wfFrSwCctCrossNetStatus": wfFrSwCctCrossNetStatus,
       "wfFrSwCctXNetSent": wfFrSwCctXNetSent,
       "wfFrSwCctXNetReceived": wfFrSwCctXNetReceived,
       "wfFrSwCctXNetErrors": wfFrSwCctXNetErrors,
       "wfFrSwTupleTable": wfFrSwTupleTable,
       "wfFrSwTupleEntry": wfFrSwTupleEntry,
       "wfFrSwTupleDelete": wfFrSwTupleDelete,
       "wfFrSwTupleIpAddrA": wfFrSwTupleIpAddrA,
       "wfFrSwTupleDlciA": wfFrSwTupleDlciA,
       "wfFrSwTupleIpAddrB": wfFrSwTupleIpAddrB,
       "wfFrSwTupleDlciB": wfFrSwTupleDlciB,
       "wfFrSwMcastTable": wfFrSwMcastTable,
       "wfFrSwMcastEntry": wfFrSwMcastEntry,
       "wfFrSwMcastDelete": wfFrSwMcastDelete,
       "wfFrSwMcastIndex": wfFrSwMcastIndex,
       "wfFrSwMcastIpAddr": wfFrSwMcastIpAddr,
       "wfFrSwMcastDlci": wfFrSwMcastDlci,
       "wfFrSwMcastIndividualDlci": wfFrSwMcastIndividualDlci,
       "wfFrSwUsage": wfFrSwUsage,
       "wfFrSwUsageEnable": wfFrSwUsageEnable,
       "wfFrSwUsageVolume": wfFrSwUsageVolume,
       "wfFrSwUsageVolumeBackup": wfFrSwUsageVolumeBackup,
       "wfFrSwUsageDirectory": wfFrSwUsageDirectory,
       "wfFrSwUsageFilePrefix": wfFrSwUsageFilePrefix,
       "wfFrSwUsageTimerInterval": wfFrSwUsageTimerInterval,
       "wfFrSwUsageUpdateInterval": wfFrSwUsageUpdateInterval,
       "wfFrSwUsageStoreInterval": wfFrSwUsageStoreInterval,
       "wfFrSwUsageFlushInterval": wfFrSwUsageFlushInterval,
       "wfFrSwUsageCleanupInterval": wfFrSwUsageCleanupInterval,
       "wfFrSwUsageLocalTimeZone": wfFrSwUsageLocalTimeZone,
       "wfFrSwUsageUpdateTimeStamp": wfFrSwUsageUpdateTimeStamp,
       "wfFrSwUsageStoreTimeStamp": wfFrSwUsageStoreTimeStamp,
       "wfFrSwUsageFlushTimeStamp": wfFrSwUsageFlushTimeStamp,
       "wfFrSwUsageCleanupTimeStamp": wfFrSwUsageCleanupTimeStamp,
       "wfFrSwUsageUpdateData": wfFrSwUsageUpdateData,
       "wfFrSwUsageStoreData": wfFrSwUsageStoreData,
       "wfFrSwUsageFlushData": wfFrSwUsageFlushData,
       "wfFrSwUsageFileCleanup": wfFrSwUsageFileCleanup,
       "wfFrSwUsageState": wfFrSwUsageState,
       "wfFrSwUsageCurVolume": wfFrSwUsageCurVolume,
       "wfFrSwUsageCurVolumeBackup": wfFrSwUsageCurVolumeBackup,
       "wfFrSwUsageCurDirectory": wfFrSwUsageCurDirectory,
       "wfFrSwUsageCurFilePrefix": wfFrSwUsageCurFilePrefix,
       "wfFrSwUsageCurTimerInterval": wfFrSwUsageCurTimerInterval,
       "wfFrSwUsageCurUpdateInterval": wfFrSwUsageCurUpdateInterval,
       "wfFrSwUsageCurStoreInterval": wfFrSwUsageCurStoreInterval,
       "wfFrSwUsageCurFlushInterval": wfFrSwUsageCurFlushInterval,
       "wfFrSwUsageCurCleanupInterval": wfFrSwUsageCurCleanupInterval,
       "wfFrSwUsageDebug": wfFrSwUsageDebug,
       "wfFrSwUsageCurDebug": wfFrSwUsageCurDebug,
       "wfFrSwUsageSwitchId": wfFrSwUsageSwitchId,
       "wfFrSwUsageNumEntries": wfFrSwUsageNumEntries,
       "wfFrSwSvcUsageEnable": wfFrSwSvcUsageEnable,
       "wfFrSwSvcUsageInterimRecordEnable": wfFrSwSvcUsageInterimRecordEnable,
       "wfFrSwSvcUsageVolume": wfFrSwSvcUsageVolume,
       "wfFrSwSvcUsageDirectory": wfFrSwSvcUsageDirectory,
       "wfFrSwSvcUsageFilePrefix": wfFrSwSvcUsageFilePrefix,
       "wfFrSwSvcUsageUpdateInterval": wfFrSwSvcUsageUpdateInterval,
       "wfFrSwSvcUsageStoreInterval": wfFrSwSvcUsageStoreInterval,
       "wfFrSwSvcUsageFlushInterval": wfFrSwSvcUsageFlushInterval,
       "wfFrSwSvcUsageCleanupInterval": wfFrSwSvcUsageCleanupInterval,
       "wfFrSwSvcUsageUpdateTimeStamp": wfFrSwSvcUsageUpdateTimeStamp,
       "wfFrSwSvcUsageStoreTimeStamp": wfFrSwSvcUsageStoreTimeStamp,
       "wfFrSwSvcUsageFlushTimeStamp": wfFrSwSvcUsageFlushTimeStamp,
       "wfFrSwSvcUsageCleanupTimeStamp": wfFrSwSvcUsageCleanupTimeStamp,
       "wfFrSwSvcUsageUpdateData": wfFrSwSvcUsageUpdateData,
       "wfFrSwSvcUsageStoreData": wfFrSwSvcUsageStoreData,
       "wfFrSwSvcUsageFlushData": wfFrSwSvcUsageFlushData,
       "wfFrSwSvcUsageFileCleanup": wfFrSwSvcUsageFileCleanup,
       "wfFrSwSvcUsageState": wfFrSwSvcUsageState,
       "wfFrSwSvcUsageCurVolume": wfFrSwSvcUsageCurVolume,
       "wfFrSwSvcUsageCurDirectory": wfFrSwSvcUsageCurDirectory,
       "wfFrSwSvcUsageCurFilePrefix": wfFrSwSvcUsageCurFilePrefix,
       "wfFrSwSvcUsageCurUpdateInterval": wfFrSwSvcUsageCurUpdateInterval,
       "wfFrSwSvcUsageCurStoreInterval": wfFrSwSvcUsageCurStoreInterval,
       "wfFrSwSvcUsageCurFlushInterval": wfFrSwSvcUsageCurFlushInterval,
       "wfFrSwSvcUsageCurCleanupInterval": wfFrSwSvcUsageCurCleanupInterval,
       "wfFrSwSvcUsageNumEntries": wfFrSwSvcUsageNumEntries,
       "wfFrSwSvcUsageVersionId": wfFrSwSvcUsageVersionId,
       "wfFrSwUsageSwitchName": wfFrSwUsageSwitchName,
       "wfFrSwPvcUsageFileLayout": wfFrSwPvcUsageFileLayout,
       "wfFrSwSvcUsageFileLayout": wfFrSwSvcUsageFileLayout,
       "wfFrSwUsageTable": wfFrSwUsageTable,
       "wfFrSwUsageEntry": wfFrSwUsageEntry,
       "wfFrSwUsageDelete": wfFrSwUsageDelete,
       "wfFrSwUsageCircuitNumber": wfFrSwUsageCircuitNumber,
       "wfFrSwUsageDlci": wfFrSwUsageDlci,
       "wfFrSwUsageIPAddress": wfFrSwUsageIPAddress,
       "wfFrSwUsageStartTimeStampHigh": wfFrSwUsageStartTimeStampHigh,
       "wfFrSwUsageStartTimeStampLow": wfFrSwUsageStartTimeStampLow,
       "wfFrSwUsageEndTimeStampHigh": wfFrSwUsageEndTimeStampHigh,
       "wfFrSwUsageEndTimeStampLow": wfFrSwUsageEndTimeStampLow,
       "wfFrSwUsageSentNonDEFramesHigh": wfFrSwUsageSentNonDEFramesHigh,
       "wfFrSwUsageSentNonDEFramesLow": wfFrSwUsageSentNonDEFramesLow,
       "wfFrSwUsageSentNonDEOctetsHigh": wfFrSwUsageSentNonDEOctetsHigh,
       "wfFrSwUsageSentNonDEOctetsLow": wfFrSwUsageSentNonDEOctetsLow,
       "wfFrSwUsageSentDEFramesHigh": wfFrSwUsageSentDEFramesHigh,
       "wfFrSwUsageSentDEFramesLow": wfFrSwUsageSentDEFramesLow,
       "wfFrSwUsageSentDEOctetsHigh": wfFrSwUsageSentDEOctetsHigh,
       "wfFrSwUsageSentDEOctetsLow": wfFrSwUsageSentDEOctetsLow,
       "wfFrSwUsageLastNonDEFramesHigh": wfFrSwUsageLastNonDEFramesHigh,
       "wfFrSwUsageLastNonDEFramesLow": wfFrSwUsageLastNonDEFramesLow,
       "wfFrSwUsageLastNonDEOctetsHigh": wfFrSwUsageLastNonDEOctetsHigh,
       "wfFrSwUsageLastNonDEOctetsLow": wfFrSwUsageLastNonDEOctetsLow,
       "wfFrSwUsageLastDEFramesHigh": wfFrSwUsageLastDEFramesHigh,
       "wfFrSwUsageLastDEFramesLow": wfFrSwUsageLastDEFramesLow,
       "wfFrSwUsageLastDEOctetsHigh": wfFrSwUsageLastDEOctetsHigh,
       "wfFrSwUsageLastDEOctetsLow": wfFrSwUsageLastDEOctetsLow,
       "wfFrSwUsageRemoteIPAddress": wfFrSwUsageRemoteIPAddress,
       "wfFrSwUsageRemoteDlci": wfFrSwUsageRemoteDlci,
       "wfFrSwVcTable": wfFrSwVcTable,
       "wfFrSwVcEntry": wfFrSwVcEntry,
       "wfFrSwVcDelete": wfFrSwVcDelete,
       "wfFrSwVcCircuit": wfFrSwVcCircuit,
       "wfFrSwVcDlci": wfFrSwVcDlci,
       "wfFrSwVcState": wfFrSwVcState,
       "wfFrSwVcStateSet": wfFrSwVcStateSet,
       "wfFrSwVcMulticast": wfFrSwVcMulticast,
       "wfFrSwVcInBe": wfFrSwVcInBe,
       "wfFrSwVcOutBe": wfFrSwVcOutBe,
       "wfFrSwVcInThroughput": wfFrSwVcInThroughput,
       "wfFrSwVcOutThroughput": wfFrSwVcOutThroughput,
       "wfFrSwVcOutBc": wfFrSwVcOutBc,
       "wfFrSwVcInBc": wfFrSwVcInBc,
       "wfFrSwVcInBcOctets": wfFrSwVcInBcOctets,
       "wfFrSwVcBecnState": wfFrSwVcBecnState,
       "wfFrSwVcReportedStatus": wfFrSwVcReportedStatus,
       "wfFrSwVcReceivedStatus": wfFrSwVcReceivedStatus,
       "wfFrSwVcCrossNetStatus": wfFrSwVcCrossNetStatus,
       "wfFrSwVcXNetSent": wfFrSwVcXNetSent,
       "wfFrSwVcXNetReceived": wfFrSwVcXNetReceived,
       "wfFrSwVcCalledIpAddr": wfFrSwVcCalledIpAddr,
       "wfFrSwVcCalledDlci": wfFrSwVcCalledDlci,
       "wfFrSwVcTrfPriority": wfFrSwVcTrfPriority,
       "wfFrSwVcCreationTime": wfFrSwVcCreationTime,
       "wfFrSwVcLastTimeChange": wfFrSwVcLastTimeChange,
       "wfFrSwVcTxNonDeFrames": wfFrSwVcTxNonDeFrames,
       "wfFrSwVcTxNonDeOctets": wfFrSwVcTxNonDeOctets,
       "wfFrSwVcTxDeFrames": wfFrSwVcTxDeFrames,
       "wfFrSwVcTxDeOctets": wfFrSwVcTxDeOctets,
       "wfFrSwVcSetFecnFrames": wfFrSwVcSetFecnFrames,
       "wfFrSwVcSetFecnOctets": wfFrSwVcSetFecnOctets,
       "wfFrSwVcSetBecnFrames": wfFrSwVcSetBecnFrames,
       "wfFrSwVcSetBecnOctets": wfFrSwVcSetBecnOctets,
       "wfFrSwVcSetDeFrames": wfFrSwVcSetDeFrames,
       "wfFrSwVcSetDeOctets": wfFrSwVcSetDeOctets,
       "wfFrSwVcDropNonDeFrames": wfFrSwVcDropNonDeFrames,
       "wfFrSwVcDropNonDeOctets": wfFrSwVcDropNonDeOctets,
       "wfFrSwVcDropDeFrames": wfFrSwVcDropDeFrames,
       "wfFrSwVcDropDeOctets": wfFrSwVcDropDeOctets,
       "wfFrSwVcInactiveVcDropFrames": wfFrSwVcInactiveVcDropFrames,
       "wfFrSwVcInactiveVcDropOctets": wfFrSwVcInactiveVcDropOctets,
       "wfFrSwVcRecvNonDeFrames": wfFrSwVcRecvNonDeFrames,
       "wfFrSwVcRecvNonDeOctets": wfFrSwVcRecvNonDeOctets,
       "wfFrSwVcRecvDeFrames": wfFrSwVcRecvDeFrames,
       "wfFrSwVcRecvDeOctets": wfFrSwVcRecvDeOctets,
       "wfFrSwVcRecvFecnFrames": wfFrSwVcRecvFecnFrames,
       "wfFrSwVcRecvFecnOctets": wfFrSwVcRecvFecnOctets,
       "wfFrSwVcRecvBecnFrames": wfFrSwVcRecvBecnFrames,
       "wfFrSwVcRecvBecnOctets": wfFrSwVcRecvBecnOctets,
       "wfFrSwVcRecentNonDeOctets": wfFrSwVcRecentNonDeOctets,
       "wfFrSwVcXNetErrors": wfFrSwVcXNetErrors,
       "wfFrSwVcDropExcessBurstFrames": wfFrSwVcDropExcessBurstFrames,
       "wfFrSwVcDropExcessBurstOctets": wfFrSwVcDropExcessBurstOctets,
       "wfFrSwVcInBeOctets": wfFrSwVcInBeOctets,
       "wfFrSwVcCfgInBe": wfFrSwVcCfgInBe,
       "wfFrSwVcRedirectAction": wfFrSwVcRedirectAction,
       "wfFrSwVcRedirectType": wfFrSwVcRedirectType,
       "wfFrSwVcRedirectState": wfFrSwVcRedirectState,
       "wfFrSwVcBackupCalledIpAddr": wfFrSwVcBackupCalledIpAddr,
       "wfFrSwVcBackupCalledDlci": wfFrSwVcBackupCalledDlci,
       "wfFrSwVcBackupCrossNetStatus": wfFrSwVcBackupCrossNetStatus,
       "wfFrSwVcBackupCrossNetErrors": wfFrSwVcBackupCrossNetErrors,
       "wfFrSwVcAtmIwfMode": wfFrSwVcAtmIwfMode,
       "wfFrSwVcAtmIwfVPI": wfFrSwVcAtmIwfVPI,
       "wfFrSwVcAtmIwfVCI": wfFrSwVcAtmIwfVCI,
       "wfFrSwVcAtmIwfLossPriorityPolicy": wfFrSwVcAtmIwfLossPriorityPolicy,
       "wfFrSwVcAtmIwfDePolicy": wfFrSwVcAtmIwfDePolicy,
       "wfFrSwVcAtmIwfEfciPolicy": wfFrSwVcAtmIwfEfciPolicy,
       "wfFrSwVcEscapeEnable": wfFrSwVcEscapeEnable,
       "wfFrSwVcSpvcCallState": wfFrSwVcSpvcCallState,
       "wfFrSwVcCallReqCalledAddr": wfFrSwVcCallReqCalledAddr,
       "wfFrSwVcCallReqDlciSelectionType": wfFrSwVcCallReqDlciSelectionType,
       "wfFrSwVcCallReqCalledDlci": wfFrSwVcCallReqCalledDlci,
       "wfFrSwVcCallReqRetryTimer": wfFrSwVcCallReqRetryTimer,
       "wfFrSwVcCallReqMaxRetries": wfFrSwVcCallReqMaxRetries,
       "wfFrSwIsdnBaseTable": wfFrSwIsdnBaseTable,
       "wfFrSwIsdnBaseEntry": wfFrSwIsdnBaseEntry,
       "wfFrSwIsdnBaseDelete": wfFrSwIsdnBaseDelete,
       "wfFrSwIsdnBaseSlotNum": wfFrSwIsdnBaseSlotNum,
       "wfFrSwIsdnBaseAssocType": wfFrSwIsdnBaseAssocType,
       "wfFrSwIsdnAssocTable": wfFrSwIsdnAssocTable,
       "wfFrSwIsdnAssocEntry": wfFrSwIsdnAssocEntry,
       "wfFrSwIsdnAssocDelete": wfFrSwIsdnAssocDelete,
       "wfFrSwIsdnAssocSlotNum": wfFrSwIsdnAssocSlotNum,
       "wfFrSwIsdnAssocNum": wfFrSwIsdnAssocNum,
       "wfFrSwIsdnAssocScrnEnable": wfFrSwIsdnAssocScrnEnable,
       "wfFrSwIsdnAssocIndex": wfFrSwIsdnAssocIndex,
       "wfFrSwIsdnUniTable": wfFrSwIsdnUniTable,
       "wfFrSwIsdnUniEntry": wfFrSwIsdnUniEntry,
       "wfFrSwIsdnUniDelete": wfFrSwIsdnUniDelete,
       "wfFrSwIsdnUniIndex": wfFrSwIsdnUniIndex,
       "wfFrSwIsdnUniNum": wfFrSwIsdnUniNum,
       "wfFrSwIsdnUniState": wfFrSwIsdnUniState,
       "wfFrSwIsdnScrnTable": wfFrSwIsdnScrnTable,
       "wfFrSwIsdnScrnEntry": wfFrSwIsdnScrnEntry,
       "wfFrSwIsdnScrnDelete": wfFrSwIsdnScrnDelete,
       "wfFrSwIsdnScrnIndex": wfFrSwIsdnScrnIndex,
       "wfFrSwIsdnScrnNum": wfFrSwIsdnScrnNum,
       "wfFrSwSigTable": wfFrSwSigTable,
       "wfFrSwSigEntry": wfFrSwSigEntry,
       "wfFrSwSigDelete": wfFrSwSigDelete,
       "wfFrSwSigCircuit": wfFrSwSigCircuit,
       "wfFrSwSigSvcDlciLow": wfFrSwSigSvcDlciLow,
       "wfFrSwSigSvcDlciHigh": wfFrSwSigSvcDlciHigh,
       "wfFrSwSigDlciAssign": wfFrSwSigDlciAssign,
       "wfFrSwSigMaxNumOfSvcs": wfFrSwSigMaxNumOfSvcs,
       "wfFrSwSigNumOfSvcsInUse": wfFrSwSigNumOfSvcsInUse,
       "wfFrSwSigDefaultThroughput": wfFrSwSigDefaultThroughput,
       "wfFrSwSigDefaultMinAcceptThroughput": wfFrSwSigDefaultMinAcceptThroughput,
       "wfFrSwSigDefaultBc": wfFrSwSigDefaultBc,
       "wfFrSwSigDefaultBe": wfFrSwSigDefaultBe,
       "wfFrSwSigMaxInThroughputPerSvc": wfFrSwSigMaxInThroughputPerSvc,
       "wfFrSwSigMaxOutThroughputPerSvc": wfFrSwSigMaxOutThroughputPerSvc,
       "wfFrSwSigTotalInNegotiableThroughput": wfFrSwSigTotalInNegotiableThroughput,
       "wfFrSwSigTotalInCurrentThroughput": wfFrSwSigTotalInCurrentThroughput,
       "wfFrSwSigTotalOutNegotiableThroughput": wfFrSwSigTotalOutNegotiableThroughput,
       "wfFrSwSigTotalOutCurrentThroughput": wfFrSwSigTotalOutCurrentThroughput,
       "wfFrSwSigXNetClearingDisable": wfFrSwSigXNetClearingDisable,
       "wfFrSwSigCallingPartyIEMandatory": wfFrSwSigCallingPartyIEMandatory,
       "wfFrSwSigT301": wfFrSwSigT301,
       "wfFrSwSigT303": wfFrSwSigT303,
       "wfFrSwSigT305": wfFrSwSigT305,
       "wfFrSwSigT308": wfFrSwSigT308,
       "wfFrSwSigT310": wfFrSwSigT310,
       "wfFrSwSigT322": wfFrSwSigT322,
       "wfFrSwSigInSetupPkts": wfFrSwSigInSetupPkts,
       "wfFrSwSigInCallProceedingPkts": wfFrSwSigInCallProceedingPkts,
       "wfFrSwSigInConnectPkts": wfFrSwSigInConnectPkts,
       "wfFrSwSigInDisconnectPkts": wfFrSwSigInDisconnectPkts,
       "wfFrSwSigInReleasePkts": wfFrSwSigInReleasePkts,
       "wfFrSwSigInReleaseCompletePkts": wfFrSwSigInReleaseCompletePkts,
       "wfFrSwSigInStatusEnquiryPkts": wfFrSwSigInStatusEnquiryPkts,
       "wfFrSwSigInStatusPkts": wfFrSwSigInStatusPkts,
       "wfFrSwSigInUnknownPkts": wfFrSwSigInUnknownPkts,
       "wfFrSwSigOutSetupPkts": wfFrSwSigOutSetupPkts,
       "wfFrSwSigOutCallProceedingPkts": wfFrSwSigOutCallProceedingPkts,
       "wfFrSwSigOutConnectPkts": wfFrSwSigOutConnectPkts,
       "wfFrSwSigOutDisconnectPkts": wfFrSwSigOutDisconnectPkts,
       "wfFrSwSigOutReleasePkts": wfFrSwSigOutReleasePkts,
       "wfFrSwSigOutReleaseCompletePkts": wfFrSwSigOutReleaseCompletePkts,
       "wfFrSwSigOutStatusEnquiryPkts": wfFrSwSigOutStatusEnquiryPkts,
       "wfFrSwSigOutStatusPkts": wfFrSwSigOutStatusPkts,
       "wfFrSwSigRejectedConnRequests": wfFrSwSigRejectedConnRequests,
       "wfFrSwSigNwrkAbortedConnections": wfFrSwSigNwrkAbortedConnections,
       "wfFrSwSigL2Resets": wfFrSwSigL2Resets,
       "wfFrSwSigDlciIEAllowed": wfFrSwSigDlciIEAllowed,
       "wfFrSwSigX213PriorityIEAllowed": wfFrSwSigX213PriorityIEAllowed,
       "wfFrSwSigMaximumBe": wfFrSwSigMaximumBe,
       "wfFrSwGlobalE164AddrTable": wfFrSwGlobalE164AddrTable,
       "wfFrSwGlobalE164AddrEntry": wfFrSwGlobalE164AddrEntry,
       "wfFrSwGlobalE164AddrDelete": wfFrSwGlobalE164AddrDelete,
       "wfFrSwGlobalE164AddrLow": wfFrSwGlobalE164AddrLow,
       "wfFrSwGlobalE164AddrHigh": wfFrSwGlobalE164AddrHigh,
       "wfFrSwGlobalE164AddrIPAddr": wfFrSwGlobalE164AddrIPAddr,
       "wfFrSwGlobalX121AddrTable": wfFrSwGlobalX121AddrTable,
       "wfFrSwGlobalX121AddrEntry": wfFrSwGlobalX121AddrEntry,
       "wfFrSwGlobalX121AddrDelete": wfFrSwGlobalX121AddrDelete,
       "wfFrSwGlobalX121AddrLow": wfFrSwGlobalX121AddrLow,
       "wfFrSwGlobalX121AddrHigh": wfFrSwGlobalX121AddrHigh,
       "wfFrSwGlobalX121AddrIPAddr": wfFrSwGlobalX121AddrIPAddr,
       "wfFrSwLocalE164AddrTable": wfFrSwLocalE164AddrTable,
       "wfFrSwLocalE164AddrEntry": wfFrSwLocalE164AddrEntry,
       "wfFrSwLocalE164AddrDelete": wfFrSwLocalE164AddrDelete,
       "wfFrSwLocalE164AddrCct": wfFrSwLocalE164AddrCct,
       "wfFrSwLocalE164Address": wfFrSwLocalE164Address,
       "wfFrSwLocalE164AddrCUG": wfFrSwLocalE164AddrCUG,
       "wfFrSwLocalE164AddrLocalFlag": wfFrSwLocalE164AddrLocalFlag,
       "wfFrSwLocalX121AddrTable": wfFrSwLocalX121AddrTable,
       "wfFrSwLocalX121AddrEntry": wfFrSwLocalX121AddrEntry,
       "wfFrSwLocalX121AddrDelete": wfFrSwLocalX121AddrDelete,
       "wfFrSwLocalX121AddrCct": wfFrSwLocalX121AddrCct,
       "wfFrSwLocalX121Address": wfFrSwLocalX121Address,
       "wfFrSwLocalX121AddrCUG": wfFrSwLocalX121AddrCUG,
       "wfFrSwLocalX121AddrLocalFlag": wfFrSwLocalX121AddrLocalFlag,
       "wfFrSwBase": wfFrSwBase,
       "wfFrSwBaseDelete": wfFrSwBaseDelete,
       "wfFrSwBaseIpAddr": wfFrSwBaseIpAddr,
       "wfFrSwBaseShutDown": wfFrSwBaseShutDown,
       "wfFrSwCngcMonTable": wfFrSwCngcMonTable,
       "wfFrSwCngcMonEntry": wfFrSwCngcMonEntry,
       "wfFrSwCngcMonReset": wfFrSwCngcMonReset,
       "wfFrSwCngcMonCct": wfFrSwCngcMonCct,
       "wfFrSwCngcMonP0Level1Percent": wfFrSwCngcMonP0Level1Percent,
       "wfFrSwCngcMonP0Level2Percent": wfFrSwCngcMonP0Level2Percent,
       "wfFrSwCngcMonP0Level3Percent": wfFrSwCngcMonP0Level3Percent,
       "wfFrSwCngcMonP0Level4Percent": wfFrSwCngcMonP0Level4Percent,
       "wfFrSwCngcMonP1Level1Percent": wfFrSwCngcMonP1Level1Percent,
       "wfFrSwCngcMonP1Level2Percent": wfFrSwCngcMonP1Level2Percent,
       "wfFrSwCngcMonP1Level3Percent": wfFrSwCngcMonP1Level3Percent,
       "wfFrSwCngcMonP1Level4Percent": wfFrSwCngcMonP1Level4Percent,
       "wfFrSwCngcMonP2Level1Percent": wfFrSwCngcMonP2Level1Percent,
       "wfFrSwCngcMonP2Level2Percent": wfFrSwCngcMonP2Level2Percent,
       "wfFrSwCngcMonP2Level3Percent": wfFrSwCngcMonP2Level3Percent,
       "wfFrSwCngcMonP2Level4Percent": wfFrSwCngcMonP2Level4Percent,
       "wfFrSwCngcMonP3Level1Percent": wfFrSwCngcMonP3Level1Percent,
       "wfFrSwCngcMonP3Level2Percent": wfFrSwCngcMonP3Level2Percent,
       "wfFrSwCngcMonP3Level3Percent": wfFrSwCngcMonP3Level3Percent,
       "wfFrSwCngcMonP3Level4Percent": wfFrSwCngcMonP3Level4Percent,
       "wfFrSwVirtualIntfTable": wfFrSwVirtualIntfTable,
       "wfFrSwVirtualIntfEntry": wfFrSwVirtualIntfEntry,
       "wfFrSwVirtualIntfDelete": wfFrSwVirtualIntfDelete,
       "wfFrSwVirtualIntfSlot": wfFrSwVirtualIntfSlot,
       "wfFrSwVirtualIntfCct": wfFrSwVirtualIntfCct,
       "wfFrSwVirtualIntfLineNum": wfFrSwVirtualIntfLineNum,
       "wfFrSwExtFileSysTable": wfFrSwExtFileSysTable,
       "wfFrSwExtFileSysEntry": wfFrSwExtFileSysEntry,
       "wfFrSwExtFileSysDelete": wfFrSwExtFileSysDelete,
       "wfFrSwExtFileSysSlot": wfFrSwExtFileSysSlot,
       "wfFrSwExtFileSysSize": wfFrSwExtFileSysSize,
       "wfFrSwExtFileSysActualSize": wfFrSwExtFileSysActualSize,
       "wfFrSwExtFileSysState": wfFrSwExtFileSysState}
)
