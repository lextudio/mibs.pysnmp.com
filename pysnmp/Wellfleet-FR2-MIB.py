# SNMP MIB module (Wellfleet-FR2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-FR2-MIB
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

(wfFrameRelay2Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfFrameRelay2Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfFrIfDlcmiTable_Object = MibTable
wfFrIfDlcmiTable = _WfFrIfDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1)
)
if mibBuilder.loadTexts:
    wfFrIfDlcmiTable.setStatus("mandatory")
_WfFrIfDlcmiEntry_Object = MibTableRow
wfFrIfDlcmiEntry = _WfFrIfDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1)
)
wfFrIfDlcmiEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrDlcmiLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrDlcmiLLIndex"),
)
if mibBuilder.loadTexts:
    wfFrIfDlcmiEntry.setStatus("mandatory")


class _WfFrDlcmiDelete_Type(Integer32):
    """Custom type wfFrDlcmiDelete based on Integer32"""
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


_WfFrDlcmiDelete_Type.__name__ = "Integer32"
_WfFrDlcmiDelete_Object = MibTableColumn
wfFrDlcmiDelete = _WfFrDlcmiDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 1),
    _WfFrDlcmiDelete_Type()
)
wfFrDlcmiDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDelete.setStatus("mandatory")


class _WfFrDlcmiDisable_Type(Integer32):
    """Custom type wfFrDlcmiDisable based on Integer32"""
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


_WfFrDlcmiDisable_Type.__name__ = "Integer32"
_WfFrDlcmiDisable_Object = MibTableColumn
wfFrDlcmiDisable = _WfFrDlcmiDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 2),
    _WfFrDlcmiDisable_Type()
)
wfFrDlcmiDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDisable.setStatus("mandatory")
_WfFrDlcmiLineNumber_Type = Integer32
_WfFrDlcmiLineNumber_Object = MibTableColumn
wfFrDlcmiLineNumber = _WfFrDlcmiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 3),
    _WfFrDlcmiLineNumber_Type()
)
wfFrDlcmiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiLineNumber.setStatus("mandatory")
_WfFrDlcmiLLIndex_Type = Integer32
_WfFrDlcmiLLIndex_Object = MibTableColumn
wfFrDlcmiLLIndex = _WfFrDlcmiLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 4),
    _WfFrDlcmiLLIndex_Type()
)
wfFrDlcmiLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiLLIndex.setStatus("mandatory")
_WfFrDlcmiCircuit_Type = Integer32
_WfFrDlcmiCircuit_Object = MibTableColumn
wfFrDlcmiCircuit = _WfFrDlcmiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 5),
    _WfFrDlcmiCircuit_Type()
)
wfFrDlcmiCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiCircuit.setStatus("mandatory")


class _WfFrDlcmiManagementType_Type(Integer32):
    """Custom type wfFrDlcmiManagementType based on Integer32"""
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


_WfFrDlcmiManagementType_Type.__name__ = "Integer32"
_WfFrDlcmiManagementType_Object = MibTableColumn
wfFrDlcmiManagementType = _WfFrDlcmiManagementType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 6),
    _WfFrDlcmiManagementType_Type()
)
wfFrDlcmiManagementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiManagementType.setStatus("mandatory")


class _WfFrDlcmiStatus_Type(Integer32):
    """Custom type wfFrDlcmiStatus based on Integer32"""
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
          ("running", 1))
    )


_WfFrDlcmiStatus_Type.__name__ = "Integer32"
_WfFrDlcmiStatus_Object = MibTableColumn
wfFrDlcmiStatus = _WfFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 7),
    _WfFrDlcmiStatus_Type()
)
wfFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiStatus.setStatus("mandatory")


class _WfFrDlcmiAddress_Type(Integer32):
    """Custom type wfFrDlcmiAddress based on Integer32"""
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


_WfFrDlcmiAddress_Type.__name__ = "Integer32"
_WfFrDlcmiAddress_Object = MibTableColumn
wfFrDlcmiAddress = _WfFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 8),
    _WfFrDlcmiAddress_Type()
)
wfFrDlcmiAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAddress.setStatus("mandatory")


class _WfFrDlcmiAddressLen_Type(Integer32):
    """Custom type wfFrDlcmiAddressLen based on Integer32"""
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


_WfFrDlcmiAddressLen_Type.__name__ = "Integer32"
_WfFrDlcmiAddressLen_Object = MibTableColumn
wfFrDlcmiAddressLen = _WfFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 9),
    _WfFrDlcmiAddressLen_Type()
)
wfFrDlcmiAddressLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAddressLen.setStatus("mandatory")


class _WfFrDlcmiPollingInterval_Type(Integer32):
    """Custom type wfFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_WfFrDlcmiPollingInterval_Object = MibTableColumn
wfFrDlcmiPollingInterval = _WfFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 10),
    _WfFrDlcmiPollingInterval_Type()
)
wfFrDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiPollingInterval.setStatus("mandatory")


class _WfFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type wfFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFrDlcmiFullEnquiryInterval_Object = MibTableColumn
wfFrDlcmiFullEnquiryInterval = _WfFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 11),
    _WfFrDlcmiFullEnquiryInterval_Type()
)
wfFrDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiFullEnquiryInterval.setStatus("mandatory")


class _WfFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type wfFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_WfFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_WfFrDlcmiErrorThreshold_Object = MibTableColumn
wfFrDlcmiErrorThreshold = _WfFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 12),
    _WfFrDlcmiErrorThreshold_Type()
)
wfFrDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiErrorThreshold.setStatus("mandatory")


class _WfFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type wfFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_WfFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_WfFrDlcmiMonitoredEvents_Object = MibTableColumn
wfFrDlcmiMonitoredEvents = _WfFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 13),
    _WfFrDlcmiMonitoredEvents_Type()
)
wfFrDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiMonitoredEvents.setStatus("mandatory")
_WfFrDlcmiMaxSupportedVCs_Type = Integer32
_WfFrDlcmiMaxSupportedVCs_Object = MibTableColumn
wfFrDlcmiMaxSupportedVCs = _WfFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 14),
    _WfFrDlcmiMaxSupportedVCs_Type()
)
wfFrDlcmiMaxSupportedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiMaxSupportedVCs.setStatus("mandatory")
_WfFrDlcmiVCsConfigured_Type = Integer32
_WfFrDlcmiVCsConfigured_Object = MibTableColumn
wfFrDlcmiVCsConfigured = _WfFrDlcmiVCsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 15),
    _WfFrDlcmiVCsConfigured_Type()
)
wfFrDlcmiVCsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiVCsConfigured.setStatus("mandatory")


class _WfFrDlcmiMulticast_Type(Integer32):
    """Custom type wfFrDlcmiMulticast based on Integer32"""
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


_WfFrDlcmiMulticast_Type.__name__ = "Integer32"
_WfFrDlcmiMulticast_Object = MibTableColumn
wfFrDlcmiMulticast = _WfFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 16),
    _WfFrDlcmiMulticast_Type()
)
wfFrDlcmiMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiMulticast.setStatus("mandatory")


class _WfFrDlcmiSeqCount_Type(Integer32):
    """Custom type wfFrDlcmiSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrDlcmiSeqCount_Type.__name__ = "Integer32"
_WfFrDlcmiSeqCount_Object = MibTableColumn
wfFrDlcmiSeqCount = _WfFrDlcmiSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 17),
    _WfFrDlcmiSeqCount_Type()
)
wfFrDlcmiSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiSeqCount.setStatus("mandatory")


class _WfFrDlcmiLastReceived_Type(Integer32):
    """Custom type wfFrDlcmiLastReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrDlcmiLastReceived_Type.__name__ = "Integer32"
_WfFrDlcmiLastReceived_Object = MibTableColumn
wfFrDlcmiLastReceived = _WfFrDlcmiLastReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 18),
    _WfFrDlcmiLastReceived_Type()
)
wfFrDlcmiLastReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiLastReceived.setStatus("mandatory")


class _WfFrDlcmiPassiveSeqCount_Type(Integer32):
    """Custom type wfFrDlcmiPassiveSeqCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrDlcmiPassiveSeqCount_Type.__name__ = "Integer32"
_WfFrDlcmiPassiveSeqCount_Object = MibTableColumn
wfFrDlcmiPassiveSeqCount = _WfFrDlcmiPassiveSeqCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 19),
    _WfFrDlcmiPassiveSeqCount_Type()
)
wfFrDlcmiPassiveSeqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPassiveSeqCount.setStatus("mandatory")


class _WfFrDlcmiPassiveReceived_Type(Integer32):
    """Custom type wfFrDlcmiPassiveReceived based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrDlcmiPassiveReceived_Type.__name__ = "Integer32"
_WfFrDlcmiPassiveReceived_Object = MibTableColumn
wfFrDlcmiPassiveReceived = _WfFrDlcmiPassiveReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 20),
    _WfFrDlcmiPassiveReceived_Type()
)
wfFrDlcmiPassiveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPassiveReceived.setStatus("mandatory")
_WfFrDlcmiPolls_Type = Integer32
_WfFrDlcmiPolls_Object = MibTableColumn
wfFrDlcmiPolls = _WfFrDlcmiPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 21),
    _WfFrDlcmiPolls_Type()
)
wfFrDlcmiPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiPolls.setStatus("mandatory")


class _WfFrDlcmiCongestionDisable_Type(Integer32):
    """Custom type wfFrDlcmiCongestionDisable based on Integer32"""
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


_WfFrDlcmiCongestionDisable_Type.__name__ = "Integer32"
_WfFrDlcmiCongestionDisable_Object = MibTableColumn
wfFrDlcmiCongestionDisable = _WfFrDlcmiCongestionDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 22),
    _WfFrDlcmiCongestionDisable_Type()
)
wfFrDlcmiCongestionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiCongestionDisable.setStatus("mandatory")


class _WfFrDlcmiCongestionTmr_Type(Integer32):
    """Custom type wfFrDlcmiCongestionTmr based on Integer32"""
    defaultValue = 2

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
        *(("five", 10),
          ("four", 8),
          ("fourandhalf", 9),
          ("half", 1),
          ("one", 2),
          ("oneandhalf", 3),
          ("three", 6),
          ("threeandhalf", 7),
          ("two", 4),
          ("twoandhalf", 5))
    )


_WfFrDlcmiCongestionTmr_Type.__name__ = "Integer32"
_WfFrDlcmiCongestionTmr_Object = MibTableColumn
wfFrDlcmiCongestionTmr = _WfFrDlcmiCongestionTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 23),
    _WfFrDlcmiCongestionTmr_Type()
)
wfFrDlcmiCongestionTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiCongestionTmr.setStatus("mandatory")


class _WfFrDlcmiCongestionCtr_Type(Integer32):
    """Custom type wfFrDlcmiCongestionCtr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfFrDlcmiCongestionCtr_Type.__name__ = "Integer32"
_WfFrDlcmiCongestionCtr_Object = MibTableColumn
wfFrDlcmiCongestionCtr = _WfFrDlcmiCongestionCtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 24),
    _WfFrDlcmiCongestionCtr_Type()
)
wfFrDlcmiCongestionCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiCongestionCtr.setStatus("mandatory")


class _WfFrErrType_Type(Integer32):
    """Custom type wfFrErrType based on Integer32"""
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


_WfFrErrType_Type.__name__ = "Integer32"
_WfFrErrType_Object = MibTableColumn
wfFrErrType = _WfFrErrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 25),
    _WfFrErrType_Type()
)
wfFrErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrType.setStatus("mandatory")
_WfFrErrData_Type = OctetString
_WfFrErrData_Object = MibTableColumn
wfFrErrData = _WfFrErrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 26),
    _WfFrErrData_Type()
)
wfFrErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrData.setStatus("mandatory")
_WfFrErrTime_Type = TimeTicks
_WfFrErrTime_Object = MibTableColumn
wfFrErrTime = _WfFrErrTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 27),
    _WfFrErrTime_Type()
)
wfFrErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrTime.setStatus("mandatory")
_WfFrErrDiscards_Type = Counter32
_WfFrErrDiscards_Object = MibTableColumn
wfFrErrDiscards = _WfFrErrDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 28),
    _WfFrErrDiscards_Type()
)
wfFrErrDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrDiscards.setStatus("mandatory")
_WfFrErrDrops_Type = Counter32
_WfFrErrDrops_Object = MibTableColumn
wfFrErrDrops = _WfFrErrDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 29),
    _WfFrErrDrops_Type()
)
wfFrErrDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrDrops.setStatus("mandatory")
_WfFrErrFaults_Type = Counter32
_WfFrErrFaults_Object = MibTableColumn
wfFrErrFaults = _WfFrErrFaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 30),
    _WfFrErrFaults_Type()
)
wfFrErrFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrFaults.setStatus("mandatory")
_WfFrErrFaultTime_Type = TimeTicks
_WfFrErrFaultTime_Object = MibTableColumn
wfFrErrFaultTime = _WfFrErrFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 31),
    _WfFrErrFaultTime_Type()
)
wfFrErrFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrErrFaultTime.setStatus("mandatory")


class _WfFrDlcmiDialFailureDisable_Type(Integer32):
    """Custom type wfFrDlcmiDialFailureDisable based on Integer32"""
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


_WfFrDlcmiDialFailureDisable_Type.__name__ = "Integer32"
_WfFrDlcmiDialFailureDisable_Object = MibTableColumn
wfFrDlcmiDialFailureDisable = _WfFrDlcmiDialFailureDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 32),
    _WfFrDlcmiDialFailureDisable_Type()
)
wfFrDlcmiDialFailureDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDialFailureDisable.setStatus("mandatory")


class _WfFrDlcmiInterfaceType_Type(Integer32):
    """Custom type wfFrDlcmiInterfaceType based on Integer32"""
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
        *(("backup", 3),
          ("backupDup", 4),
          ("demand", 5),
          ("normal", 1),
          ("primary", 2))
    )


_WfFrDlcmiInterfaceType_Type.__name__ = "Integer32"
_WfFrDlcmiInterfaceType_Object = MibTableColumn
wfFrDlcmiInterfaceType = _WfFrDlcmiInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 33),
    _WfFrDlcmiInterfaceType_Type()
)
wfFrDlcmiInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiInterfaceType.setStatus("mandatory")


class _WfFrDlcmiBackupFilterCct_Type(Integer32):
    """Custom type wfFrDlcmiBackupFilterCct based on Integer32"""
    defaultValue = 0


_WfFrDlcmiBackupFilterCct_Object = MibTableColumn
wfFrDlcmiBackupFilterCct = _WfFrDlcmiBackupFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 34),
    _WfFrDlcmiBackupFilterCct_Type()
)
wfFrDlcmiBackupFilterCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiBackupFilterCct.setStatus("mandatory")


class _WfFrDlcmiDebugLevel_Type(Integer32):
    """Custom type wfFrDlcmiDebugLevel based on Integer32"""
    defaultValue = 0


_WfFrDlcmiDebugLevel_Object = MibTableColumn
wfFrDlcmiDebugLevel = _WfFrDlcmiDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 35),
    _WfFrDlcmiDebugLevel_Type()
)
wfFrDlcmiDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiDebugLevel.setStatus("mandatory")


class _WfFrDlcmiTraceLevel_Type(Integer32):
    """Custom type wfFrDlcmiTraceLevel based on Integer32"""
    defaultValue = 0


_WfFrDlcmiTraceLevel_Object = MibTableColumn
wfFrDlcmiTraceLevel = _WfFrDlcmiTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 36),
    _WfFrDlcmiTraceLevel_Type()
)
wfFrDlcmiTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiTraceLevel.setStatus("mandatory")


class _WfFrDlcmiCongestionMethod_Type(Integer32):
    """Custom type wfFrDlcmiCongestionMethod based on Integer32"""
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
        *(("shutdown", 1),
          ("throttle", 2),
          ("throttleThenShutdown", 3))
    )


_WfFrDlcmiCongestionMethod_Type.__name__ = "Integer32"
_WfFrDlcmiCongestionMethod_Object = MibTableColumn
wfFrDlcmiCongestionMethod = _WfFrDlcmiCongestionMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 37),
    _WfFrDlcmiCongestionMethod_Type()
)
wfFrDlcmiCongestionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiCongestionMethod.setStatus("mandatory")


class _WfFrDlcmiShapingTmr_Type(Integer32):
    """Custom type wfFrDlcmiShapingTmr based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8196),
    )


_WfFrDlcmiShapingTmr_Type.__name__ = "Integer32"
_WfFrDlcmiShapingTmr_Object = MibTableColumn
wfFrDlcmiShapingTmr = _WfFrDlcmiShapingTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 38),
    _WfFrDlcmiShapingTmr_Type()
)
wfFrDlcmiShapingTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiShapingTmr.setStatus("mandatory")


class _WfFrDlcmiShapingHiQueueLimit_Type(Integer32):
    """Custom type wfFrDlcmiShapingHiQueueLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrDlcmiShapingHiQueueLimit_Type.__name__ = "Integer32"
_WfFrDlcmiShapingHiQueueLimit_Object = MibTableColumn
wfFrDlcmiShapingHiQueueLimit = _WfFrDlcmiShapingHiQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 39),
    _WfFrDlcmiShapingHiQueueLimit_Type()
)
wfFrDlcmiShapingHiQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiShapingHiQueueLimit.setStatus("mandatory")


class _WfFrDlcmiShapingNormalQueueLimit_Type(Integer32):
    """Custom type wfFrDlcmiShapingNormalQueueLimit based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrDlcmiShapingNormalQueueLimit_Type.__name__ = "Integer32"
_WfFrDlcmiShapingNormalQueueLimit_Object = MibTableColumn
wfFrDlcmiShapingNormalQueueLimit = _WfFrDlcmiShapingNormalQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 40),
    _WfFrDlcmiShapingNormalQueueLimit_Type()
)
wfFrDlcmiShapingNormalQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiShapingNormalQueueLimit.setStatus("mandatory")


class _WfFrDlcmiShapingLoQueueLimit_Type(Integer32):
    """Custom type wfFrDlcmiShapingLoQueueLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrDlcmiShapingLoQueueLimit_Type.__name__ = "Integer32"
_WfFrDlcmiShapingLoQueueLimit_Object = MibTableColumn
wfFrDlcmiShapingLoQueueLimit = _WfFrDlcmiShapingLoQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 41),
    _WfFrDlcmiShapingLoQueueLimit_Type()
)
wfFrDlcmiShapingLoQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiShapingLoQueueLimit.setStatus("mandatory")


class _WfFrDlcmiXoffDisable_Type(Integer32):
    """Custom type wfFrDlcmiXoffDisable based on Integer32"""
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


_WfFrDlcmiXoffDisable_Type.__name__ = "Integer32"
_WfFrDlcmiXoffDisable_Object = MibTableColumn
wfFrDlcmiXoffDisable = _WfFrDlcmiXoffDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 42),
    _WfFrDlcmiXoffDisable_Type()
)
wfFrDlcmiXoffDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiXoffDisable.setStatus("mandatory")
_WfFrDlcmiMissingPolls_Type = Counter32
_WfFrDlcmiMissingPolls_Object = MibTableColumn
wfFrDlcmiMissingPolls = _WfFrDlcmiMissingPolls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 43),
    _WfFrDlcmiMissingPolls_Type()
)
wfFrDlcmiMissingPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrDlcmiMissingPolls.setStatus("mandatory")
_WfFrDlcmiName_Type = DisplayString
_WfFrDlcmiName_Object = MibTableColumn
wfFrDlcmiName = _WfFrDlcmiName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 44),
    _WfFrDlcmiName_Type()
)
wfFrDlcmiName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiName.setStatus("mandatory")


class _WfFrDlcmiEnableSinglePVCUpdate_Type(Integer32):
    """Custom type wfFrDlcmiEnableSinglePVCUpdate based on Integer32"""
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


_WfFrDlcmiEnableSinglePVCUpdate_Type.__name__ = "Integer32"
_WfFrDlcmiEnableSinglePVCUpdate_Object = MibTableColumn
wfFrDlcmiEnableSinglePVCUpdate = _WfFrDlcmiEnableSinglePVCUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 45),
    _WfFrDlcmiEnableSinglePVCUpdate_Type()
)
wfFrDlcmiEnableSinglePVCUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiEnableSinglePVCUpdate.setStatus("mandatory")


class _WfFrDlcmiAnnexSwEnq_Type(Integer32):
    """Custom type wfFrDlcmiAnnexSwEnq based on Integer32"""
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


_WfFrDlcmiAnnexSwEnq_Type.__name__ = "Integer32"
_WfFrDlcmiAnnexSwEnq_Object = MibTableColumn
wfFrDlcmiAnnexSwEnq = _WfFrDlcmiAnnexSwEnq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 46),
    _WfFrDlcmiAnnexSwEnq_Type()
)
wfFrDlcmiAnnexSwEnq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAnnexSwEnq.setStatus("mandatory")


class _WfFrDlcmiAnnexSwEnqTmr_Type(Integer32):
    """Custom type wfFrDlcmiAnnexSwEnqTmr based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfFrDlcmiAnnexSwEnqTmr_Type.__name__ = "Integer32"
_WfFrDlcmiAnnexSwEnqTmr_Object = MibTableColumn
wfFrDlcmiAnnexSwEnqTmr = _WfFrDlcmiAnnexSwEnqTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 47),
    _WfFrDlcmiAnnexSwEnqTmr_Type()
)
wfFrDlcmiAnnexSwEnqTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiAnnexSwEnqTmr.setStatus("mandatory")


class _WfFrDlcmiExtraStatusInfoEnable_Type(Integer32):
    """Custom type wfFrDlcmiExtraStatusInfoEnable based on Integer32"""
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


_WfFrDlcmiExtraStatusInfoEnable_Type.__name__ = "Integer32"
_WfFrDlcmiExtraStatusInfoEnable_Object = MibTableColumn
wfFrDlcmiExtraStatusInfoEnable = _WfFrDlcmiExtraStatusInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 1, 1, 48),
    _WfFrDlcmiExtraStatusInfoEnable_Type()
)
wfFrDlcmiExtraStatusInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrDlcmiExtraStatusInfoEnable.setStatus("mandatory")
_WfFrVCircuitTable_Object = MibTable
wfFrVCircuitTable = _WfFrVCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2)
)
if mibBuilder.loadTexts:
    wfFrVCircuitTable.setStatus("mandatory")
_WfFrVCircuitEntry_Object = MibTableRow
wfFrVCircuitEntry = _WfFrVCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1)
)
wfFrVCircuitEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrCircuitLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrCircuitLLIndex"),
    (0, "Wellfleet-FR2-MIB", "wfFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    wfFrVCircuitEntry.setStatus("mandatory")


class _WfFrCircuitDelete_Type(Integer32):
    """Custom type wfFrCircuitDelete based on Integer32"""
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


_WfFrCircuitDelete_Type.__name__ = "Integer32"
_WfFrCircuitDelete_Object = MibTableColumn
wfFrCircuitDelete = _WfFrCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 1),
    _WfFrCircuitDelete_Type()
)
wfFrCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitDelete.setStatus("mandatory")
_WfFrCircuitLineNumber_Type = Integer32
_WfFrCircuitLineNumber_Object = MibTableColumn
wfFrCircuitLineNumber = _WfFrCircuitLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 2),
    _WfFrCircuitLineNumber_Type()
)
wfFrCircuitLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitLineNumber.setStatus("mandatory")
_WfFrCircuitLLIndex_Type = Integer32
_WfFrCircuitLLIndex_Object = MibTableColumn
wfFrCircuitLLIndex = _WfFrCircuitLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 3),
    _WfFrCircuitLLIndex_Type()
)
wfFrCircuitLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitLLIndex.setStatus("mandatory")
_WfFrCircuitNumber_Type = Integer32
_WfFrCircuitNumber_Object = MibTableColumn
wfFrCircuitNumber = _WfFrCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 4),
    _WfFrCircuitNumber_Type()
)
wfFrCircuitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitNumber.setStatus("mandatory")


class _WfFrCircuitDlci_Type(Integer32):
    """Custom type wfFrCircuitDlci based on Integer32"""
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


_WfFrCircuitDlci_Type.__name__ = "Integer32"
_WfFrCircuitDlci_Object = MibTableColumn
wfFrCircuitDlci = _WfFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 5),
    _WfFrCircuitDlci_Type()
)
wfFrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDlci.setStatus("mandatory")


class _WfFrCircuitState_Type(Integer32):
    """Custom type wfFrCircuitState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("control", 5),
          ("disabled", 7),
          ("inactive", 3),
          ("invalid", 1),
          ("starting", 6),
          ("xoff", 4))
    )


_WfFrCircuitState_Type.__name__ = "Integer32"
_WfFrCircuitState_Object = MibTableColumn
wfFrCircuitState = _WfFrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 6),
    _WfFrCircuitState_Type()
)
wfFrCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitState.setStatus("mandatory")


class _WfFrCircuitStateSet_Type(Integer32):
    """Custom type wfFrCircuitStateSet based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("disabled", 7),
          ("inactive", 3),
          ("invalid", 1))
    )


_WfFrCircuitStateSet_Type.__name__ = "Integer32"
_WfFrCircuitStateSet_Object = MibTableColumn
wfFrCircuitStateSet = _WfFrCircuitStateSet_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 7),
    _WfFrCircuitStateSet_Type()
)
wfFrCircuitStateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitStateSet.setStatus("mandatory")
_WfFrCircuitReceivedFECNs_Type = Counter32
_WfFrCircuitReceivedFECNs_Object = MibTableColumn
wfFrCircuitReceivedFECNs = _WfFrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 8),
    _WfFrCircuitReceivedFECNs_Type()
)
wfFrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedFECNs.setStatus("mandatory")
_WfFrCircuitReceivedBECNs_Type = Counter32
_WfFrCircuitReceivedBECNs_Object = MibTableColumn
wfFrCircuitReceivedBECNs = _WfFrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 9),
    _WfFrCircuitReceivedBECNs_Type()
)
wfFrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedBECNs.setStatus("mandatory")
_WfFrCircuitSentFrames_Type = Counter32
_WfFrCircuitSentFrames_Object = MibTableColumn
wfFrCircuitSentFrames = _WfFrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 10),
    _WfFrCircuitSentFrames_Type()
)
wfFrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitSentFrames.setStatus("mandatory")
_WfFrCircuitSentOctets_Type = Counter32
_WfFrCircuitSentOctets_Object = MibTableColumn
wfFrCircuitSentOctets = _WfFrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 11),
    _WfFrCircuitSentOctets_Type()
)
wfFrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitSentOctets.setStatus("mandatory")
_WfFrCircuitReceivedFrames_Type = Counter32
_WfFrCircuitReceivedFrames_Object = MibTableColumn
wfFrCircuitReceivedFrames = _WfFrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 12),
    _WfFrCircuitReceivedFrames_Type()
)
wfFrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedFrames.setStatus("mandatory")
_WfFrCircuitReceivedOctets_Type = Counter32
_WfFrCircuitReceivedOctets_Object = MibTableColumn
wfFrCircuitReceivedOctets = _WfFrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 13),
    _WfFrCircuitReceivedOctets_Type()
)
wfFrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedOctets.setStatus("mandatory")
_WfFrCircuitCreationTime_Type = TimeTicks
_WfFrCircuitCreationTime_Object = MibTableColumn
wfFrCircuitCreationTime = _WfFrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 14),
    _WfFrCircuitCreationTime_Type()
)
wfFrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCreationTime.setStatus("mandatory")
_WfFrCircuitLastTimeChange_Type = TimeTicks
_WfFrCircuitLastTimeChange_Object = MibTableColumn
wfFrCircuitLastTimeChange = _WfFrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 15),
    _WfFrCircuitLastTimeChange_Type()
)
wfFrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitLastTimeChange.setStatus("mandatory")
_WfFrCircuitCommittedBurst_Type = Integer32
_WfFrCircuitCommittedBurst_Object = MibTableColumn
wfFrCircuitCommittedBurst = _WfFrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 16),
    _WfFrCircuitCommittedBurst_Type()
)
wfFrCircuitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCommittedBurst.setStatus("mandatory")
_WfFrCircuitExcessBurst_Type = Integer32
_WfFrCircuitExcessBurst_Object = MibTableColumn
wfFrCircuitExcessBurst = _WfFrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 17),
    _WfFrCircuitExcessBurst_Type()
)
wfFrCircuitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitExcessBurst.setStatus("mandatory")
_WfFrCircuitThroughput_Type = Integer32
_WfFrCircuitThroughput_Object = MibTableColumn
wfFrCircuitThroughput = _WfFrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 18),
    _WfFrCircuitThroughput_Type()
)
wfFrCircuitThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitThroughput.setStatus("mandatory")


class _WfFrCircuitMulticast_Type(Integer32):
    """Custom type wfFrCircuitMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_WfFrCircuitMulticast_Type.__name__ = "Integer32"
_WfFrCircuitMulticast_Object = MibTableColumn
wfFrCircuitMulticast = _WfFrCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 19),
    _WfFrCircuitMulticast_Type()
)
wfFrCircuitMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitMulticast.setStatus("mandatory")


class _WfFrCircuitType_Type(Integer32):
    """Custom type wfFrCircuitType based on Integer32"""
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
        *(("dynamic", 2),
          ("dynamicsvc", 3),
          ("static", 1))
    )


_WfFrCircuitType_Type.__name__ = "Integer32"
_WfFrCircuitType_Object = MibTableColumn
wfFrCircuitType = _WfFrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 20),
    _WfFrCircuitType_Type()
)
wfFrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitType.setStatus("mandatory")
_WfFrCircuitDiscards_Type = Counter32
_WfFrCircuitDiscards_Object = MibTableColumn
wfFrCircuitDiscards = _WfFrCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 21),
    _WfFrCircuitDiscards_Type()
)
wfFrCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDiscards.setStatus("mandatory")
_WfFrCircuitDrops_Type = Counter32
_WfFrCircuitDrops_Object = MibTableColumn
wfFrCircuitDrops = _WfFrCircuitDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 22),
    _WfFrCircuitDrops_Type()
)
wfFrCircuitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitDrops.setStatus("mandatory")
_WfFrCircuitSubCct_Type = Integer32
_WfFrCircuitSubCct_Object = MibTableColumn
wfFrCircuitSubCct = _WfFrCircuitSubCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 23),
    _WfFrCircuitSubCct_Type()
)
wfFrCircuitSubCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitSubCct.setStatus("mandatory")


class _WfFrCircuitMode_Type(Integer32):
    """Custom type wfFrCircuitMode based on Integer32"""
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


_WfFrCircuitMode_Type.__name__ = "Integer32"
_WfFrCircuitMode_Object = MibTableColumn
wfFrCircuitMode = _WfFrCircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 24),
    _WfFrCircuitMode_Type()
)
wfFrCircuitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitMode.setStatus("mandatory")


class _WfFrCircuitCongestionDisable_Type(Integer32):
    """Custom type wfFrCircuitCongestionDisable based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("inherit", 3))
    )


_WfFrCircuitCongestionDisable_Type.__name__ = "Integer32"
_WfFrCircuitCongestionDisable_Object = MibTableColumn
wfFrCircuitCongestionDisable = _WfFrCircuitCongestionDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 25),
    _WfFrCircuitCongestionDisable_Type()
)
wfFrCircuitCongestionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCongestionDisable.setStatus("mandatory")


class _WfFrCircuitCongestionState_Type(Integer32):
    """Custom type wfFrCircuitCongestionState based on Integer32"""
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
        *(("congested", 2),
          ("forwarding", 1),
          ("throttling", 3))
    )


_WfFrCircuitCongestionState_Type.__name__ = "Integer32"
_WfFrCircuitCongestionState_Object = MibTableColumn
wfFrCircuitCongestionState = _WfFrCircuitCongestionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 26),
    _WfFrCircuitCongestionState_Type()
)
wfFrCircuitCongestionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCongestionState.setStatus("mandatory")


class _WfFrCircuitCongestionTmr_Type(Integer32):
    """Custom type wfFrCircuitCongestionTmr based on Integer32"""
    defaultValue = 2

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
        *(("five", 10),
          ("four", 8),
          ("fourandhalf", 9),
          ("half", 1),
          ("one", 2),
          ("oneandhalf", 3),
          ("three", 6),
          ("threeandhalf", 7),
          ("two", 4),
          ("twoandhalf", 5))
    )


_WfFrCircuitCongestionTmr_Type.__name__ = "Integer32"
_WfFrCircuitCongestionTmr_Object = MibTableColumn
wfFrCircuitCongestionTmr = _WfFrCircuitCongestionTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 27),
    _WfFrCircuitCongestionTmr_Type()
)
wfFrCircuitCongestionTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCongestionTmr.setStatus("mandatory")


class _WfFrCircuitCongestionCtr_Type(Integer32):
    """Custom type wfFrCircuitCongestionCtr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfFrCircuitCongestionCtr_Type.__name__ = "Integer32"
_WfFrCircuitCongestionCtr_Object = MibTableColumn
wfFrCircuitCongestionCtr = _WfFrCircuitCongestionCtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 28),
    _WfFrCircuitCongestionCtr_Type()
)
wfFrCircuitCongestionCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCongestionCtr.setStatus("mandatory")


class _WfFrCircuitWcpEnable_Type(Integer32):
    """Custom type wfFrCircuitWcpEnable based on Integer32"""
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


_WfFrCircuitWcpEnable_Type.__name__ = "Integer32"
_WfFrCircuitWcpEnable_Object = MibTableColumn
wfFrCircuitWcpEnable = _WfFrCircuitWcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 29),
    _WfFrCircuitWcpEnable_Type()
)
wfFrCircuitWcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitWcpEnable.setStatus("mandatory")


class _WfFrCircuitPrimaryHoldTmr_Type(Integer32):
    """Custom type wfFrCircuitPrimaryHoldTmr based on Integer32"""
    defaultValue = 30


_WfFrCircuitPrimaryHoldTmr_Object = MibTableColumn
wfFrCircuitPrimaryHoldTmr = _WfFrCircuitPrimaryHoldTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 30),
    _WfFrCircuitPrimaryHoldTmr_Type()
)
wfFrCircuitPrimaryHoldTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitPrimaryHoldTmr.setStatus("mandatory")


class _WfFrCircuitInactivityTimer_Type(Integer32):
    """Custom type wfFrCircuitInactivityTimer based on Integer32"""
    defaultValue = 0


_WfFrCircuitInactivityTimer_Object = MibTableColumn
wfFrCircuitInactivityTimer = _WfFrCircuitInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 31),
    _WfFrCircuitInactivityTimer_Type()
)
wfFrCircuitInactivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitInactivityTimer.setStatus("mandatory")


class _WfFrCircuitInactivityMode_Type(Integer32):
    """Custom type wfFrCircuitInactivityMode based on Integer32"""
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
        *(("bothdirections", 1),
          ("eitherdirection", 4),
          ("receiveonly", 3),
          ("transmitonly", 2))
    )


_WfFrCircuitInactivityMode_Type.__name__ = "Integer32"
_WfFrCircuitInactivityMode_Object = MibTableColumn
wfFrCircuitInactivityMode = _WfFrCircuitInactivityMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 32),
    _WfFrCircuitInactivityMode_Type()
)
wfFrCircuitInactivityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitInactivityMode.setStatus("mandatory")


class _WfFrCircuitCongestionMethod_Type(Integer32):
    """Custom type wfFrCircuitCongestionMethod based on Integer32"""
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
        *(("inherit", 4),
          ("shutdown", 1),
          ("throttle", 2),
          ("throttleThenShutdown", 3))
    )


_WfFrCircuitCongestionMethod_Type.__name__ = "Integer32"
_WfFrCircuitCongestionMethod_Object = MibTableColumn
wfFrCircuitCongestionMethod = _WfFrCircuitCongestionMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 33),
    _WfFrCircuitCongestionMethod_Type()
)
wfFrCircuitCongestionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitCongestionMethod.setStatus("mandatory")
_WfFrCircuitShapedHiXmits_Type = Counter32
_WfFrCircuitShapedHiXmits_Object = MibTableColumn
wfFrCircuitShapedHiXmits = _WfFrCircuitShapedHiXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 34),
    _WfFrCircuitShapedHiXmits_Type()
)
wfFrCircuitShapedHiXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHiXmits.setStatus("mandatory")
_WfFrCircuitShapedNormalXmits_Type = Counter32
_WfFrCircuitShapedNormalXmits_Object = MibTableColumn
wfFrCircuitShapedNormalXmits = _WfFrCircuitShapedNormalXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 35),
    _WfFrCircuitShapedNormalXmits_Type()
)
wfFrCircuitShapedNormalXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedNormalXmits.setStatus("mandatory")
_WfFrCircuitShapedLoXmits_Type = Counter32
_WfFrCircuitShapedLoXmits_Object = MibTableColumn
wfFrCircuitShapedLoXmits = _WfFrCircuitShapedLoXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 36),
    _WfFrCircuitShapedLoXmits_Type()
)
wfFrCircuitShapedLoXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLoXmits.setStatus("mandatory")
_WfFrCircuitShapedHiClippedPkts_Type = Counter32
_WfFrCircuitShapedHiClippedPkts_Object = MibTableColumn
wfFrCircuitShapedHiClippedPkts = _WfFrCircuitShapedHiClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 37),
    _WfFrCircuitShapedHiClippedPkts_Type()
)
wfFrCircuitShapedHiClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHiClippedPkts.setStatus("mandatory")
_WfFrCircuitShapedNormalClippedPkts_Type = Counter32
_WfFrCircuitShapedNormalClippedPkts_Object = MibTableColumn
wfFrCircuitShapedNormalClippedPkts = _WfFrCircuitShapedNormalClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 38),
    _WfFrCircuitShapedNormalClippedPkts_Type()
)
wfFrCircuitShapedNormalClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedNormalClippedPkts.setStatus("mandatory")
_WfFrCircuitShapedLoClippedPkts_Type = Counter32
_WfFrCircuitShapedLoClippedPkts_Object = MibTableColumn
wfFrCircuitShapedLoClippedPkts = _WfFrCircuitShapedLoClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 39),
    _WfFrCircuitShapedLoClippedPkts_Type()
)
wfFrCircuitShapedLoClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLoClippedPkts.setStatus("mandatory")
_WfFrCircuitShapedHiQHighWaterPkts_Type = Gauge32
_WfFrCircuitShapedHiQHighWaterPkts_Object = MibTableColumn
wfFrCircuitShapedHiQHighWaterPkts = _WfFrCircuitShapedHiQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 40),
    _WfFrCircuitShapedHiQHighWaterPkts_Type()
)
wfFrCircuitShapedHiQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHiQHighWaterPkts.setStatus("mandatory")
_WfFrCircuitShapedNormalQHighWaterPkts_Type = Gauge32
_WfFrCircuitShapedNormalQHighWaterPkts_Object = MibTableColumn
wfFrCircuitShapedNormalQHighWaterPkts = _WfFrCircuitShapedNormalQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 41),
    _WfFrCircuitShapedNormalQHighWaterPkts_Type()
)
wfFrCircuitShapedNormalQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedNormalQHighWaterPkts.setStatus("mandatory")
_WfFrCircuitShapedLoQHighWaterPkts_Type = Gauge32
_WfFrCircuitShapedLoQHighWaterPkts_Object = MibTableColumn
wfFrCircuitShapedLoQHighWaterPkts = _WfFrCircuitShapedLoQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 42),
    _WfFrCircuitShapedLoQHighWaterPkts_Type()
)
wfFrCircuitShapedLoQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLoQHighWaterPkts.setStatus("mandatory")
_WfFrCircuitShapedDroppedPkts_Type = Counter32
_WfFrCircuitShapedDroppedPkts_Object = MibTableColumn
wfFrCircuitShapedDroppedPkts = _WfFrCircuitShapedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 43),
    _WfFrCircuitShapedDroppedPkts_Type()
)
wfFrCircuitShapedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedDroppedPkts.setStatus("mandatory")
_WfFrCircuitShapedLargePkts_Type = Counter32
_WfFrCircuitShapedLargePkts_Object = MibTableColumn
wfFrCircuitShapedLargePkts = _WfFrCircuitShapedLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 44),
    _WfFrCircuitShapedLargePkts_Type()
)
wfFrCircuitShapedLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLargePkts.setStatus("mandatory")
_WfFrCircuitShapedHiTotalOctets_Type = Counter32
_WfFrCircuitShapedHiTotalOctets_Object = MibTableColumn
wfFrCircuitShapedHiTotalOctets = _WfFrCircuitShapedHiTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 45),
    _WfFrCircuitShapedHiTotalOctets_Type()
)
wfFrCircuitShapedHiTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHiTotalOctets.setStatus("mandatory")
_WfFrCircuitShapedNormalTotalOctets_Type = Counter32
_WfFrCircuitShapedNormalTotalOctets_Object = MibTableColumn
wfFrCircuitShapedNormalTotalOctets = _WfFrCircuitShapedNormalTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 46),
    _WfFrCircuitShapedNormalTotalOctets_Type()
)
wfFrCircuitShapedNormalTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedNormalTotalOctets.setStatus("mandatory")
_WfFrCircuitShapedLoTotalOctets_Type = Counter32
_WfFrCircuitShapedLoTotalOctets_Object = MibTableColumn
wfFrCircuitShapedLoTotalOctets = _WfFrCircuitShapedLoTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 47),
    _WfFrCircuitShapedLoTotalOctets_Type()
)
wfFrCircuitShapedLoTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLoTotalOctets.setStatus("mandatory")
_WfFrCircuitShapedPktsNotQueued_Type = Counter32
_WfFrCircuitShapedPktsNotQueued_Object = MibTableColumn
wfFrCircuitShapedPktsNotQueued = _WfFrCircuitShapedPktsNotQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 48),
    _WfFrCircuitShapedPktsNotQueued_Type()
)
wfFrCircuitShapedPktsNotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapedPktsNotQueued.setStatus("mandatory")


class _WfFrCircuitShapedHighWaterPktsClear_Type(Integer32):
    """Custom type wfFrCircuitShapedHighWaterPktsClear based on Integer32"""
    defaultValue = 0


_WfFrCircuitShapedHighWaterPktsClear_Object = MibTableColumn
wfFrCircuitShapedHighWaterPktsClear = _WfFrCircuitShapedHighWaterPktsClear_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 49),
    _WfFrCircuitShapedHighWaterPktsClear_Type()
)
wfFrCircuitShapedHighWaterPktsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHighWaterPktsClear.setStatus("mandatory")


class _WfFrCircuitShapedHiQueueLimit_Type(Integer32):
    """Custom type wfFrCircuitShapedHiQueueLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrCircuitShapedHiQueueLimit_Type.__name__ = "Integer32"
_WfFrCircuitShapedHiQueueLimit_Object = MibTableColumn
wfFrCircuitShapedHiQueueLimit = _WfFrCircuitShapedHiQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 50),
    _WfFrCircuitShapedHiQueueLimit_Type()
)
wfFrCircuitShapedHiQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitShapedHiQueueLimit.setStatus("mandatory")


class _WfFrCircuitShapedNormalQueueLimit_Type(Integer32):
    """Custom type wfFrCircuitShapedNormalQueueLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrCircuitShapedNormalQueueLimit_Type.__name__ = "Integer32"
_WfFrCircuitShapedNormalQueueLimit_Object = MibTableColumn
wfFrCircuitShapedNormalQueueLimit = _WfFrCircuitShapedNormalQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 51),
    _WfFrCircuitShapedNormalQueueLimit_Type()
)
wfFrCircuitShapedNormalQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitShapedNormalQueueLimit.setStatus("mandatory")


class _WfFrCircuitShapedLoQueueLimit_Type(Integer32):
    """Custom type wfFrCircuitShapedLoQueueLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfFrCircuitShapedLoQueueLimit_Type.__name__ = "Integer32"
_WfFrCircuitShapedLoQueueLimit_Object = MibTableColumn
wfFrCircuitShapedLoQueueLimit = _WfFrCircuitShapedLoQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 52),
    _WfFrCircuitShapedLoQueueLimit_Type()
)
wfFrCircuitShapedLoQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitShapedLoQueueLimit.setStatus("mandatory")


class _WfFrCircuitStartupDelay_Type(Integer32):
    """Custom type wfFrCircuitStartupDelay based on Integer32"""
    defaultValue = 0


_WfFrCircuitStartupDelay_Object = MibTableColumn
wfFrCircuitStartupDelay = _WfFrCircuitStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 53),
    _WfFrCircuitStartupDelay_Type()
)
wfFrCircuitStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitStartupDelay.setStatus("mandatory")


class _WfFrCircuitCurHiQueueLimit_Type(Gauge32):
    """Custom type wfFrCircuitCurHiQueueLimit based on Gauge32"""
    defaultValue = 0


_WfFrCircuitCurHiQueueLimit_Object = MibTableColumn
wfFrCircuitCurHiQueueLimit = _WfFrCircuitCurHiQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 54),
    _WfFrCircuitCurHiQueueLimit_Type()
)
wfFrCircuitCurHiQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCurHiQueueLimit.setStatus("mandatory")


class _WfFrCircuitCurNormalQueueLimit_Type(Gauge32):
    """Custom type wfFrCircuitCurNormalQueueLimit based on Gauge32"""
    defaultValue = 0


_WfFrCircuitCurNormalQueueLimit_Object = MibTableColumn
wfFrCircuitCurNormalQueueLimit = _WfFrCircuitCurNormalQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 55),
    _WfFrCircuitCurNormalQueueLimit_Type()
)
wfFrCircuitCurNormalQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCurNormalQueueLimit.setStatus("mandatory")


class _WfFrCircuitCurLoQueueLimit_Type(Gauge32):
    """Custom type wfFrCircuitCurLoQueueLimit based on Gauge32"""
    defaultValue = 0


_WfFrCircuitCurLoQueueLimit_Object = MibTableColumn
wfFrCircuitCurLoQueueLimit = _WfFrCircuitCurLoQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 56),
    _WfFrCircuitCurLoQueueLimit_Type()
)
wfFrCircuitCurLoQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitCurLoQueueLimit.setStatus("mandatory")


class _WfFrCircuitShapingState_Type(Integer32):
    """Custom type wfFrCircuitShapingState based on Integer32"""
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
        *(("committed-shaping", 3),
          ("disabled", 1),
          ("excess-shaping", 4),
          ("invalid", 2),
          ("zero-cir", 5))
    )


_WfFrCircuitShapingState_Type.__name__ = "Integer32"
_WfFrCircuitShapingState_Object = MibTableColumn
wfFrCircuitShapingState = _WfFrCircuitShapingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 57),
    _WfFrCircuitShapingState_Type()
)
wfFrCircuitShapingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitShapingState.setStatus("mandatory")


class _WfFrCircuitBwThreshold_Type(Integer32):
    """Custom type wfFrCircuitBwThreshold based on Integer32"""
    defaultValue = 0


_WfFrCircuitBwThreshold_Object = MibTableColumn
wfFrCircuitBwThreshold = _WfFrCircuitBwThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 58),
    _WfFrCircuitBwThreshold_Type()
)
wfFrCircuitBwThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrCircuitBwThreshold.setStatus("mandatory")
_WfFrCircuitReceivedDEs_Type = Counter32
_WfFrCircuitReceivedDEs_Object = MibTableColumn
wfFrCircuitReceivedDEs = _WfFrCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 59),
    _WfFrCircuitReceivedDEs_Type()
)
wfFrCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitReceivedDEs.setStatus("mandatory")
_WfFrCircuitSentDEs_Type = Counter32
_WfFrCircuitSentDEs_Object = MibTableColumn
wfFrCircuitSentDEs = _WfFrCircuitSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 2, 1, 60),
    _WfFrCircuitSentDEs_Type()
)
wfFrCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCircuitSentDEs.setStatus("mandatory")
_WfFrCctErrorTable_Object = MibTable
wfFrCctErrorTable = _WfFrCctErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 4)
)
if mibBuilder.loadTexts:
    wfFrCctErrorTable.setStatus("mandatory")
_WfFrCctErrorEntry_Object = MibTableRow
wfFrCctErrorEntry = _WfFrCctErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 4, 1)
)
wfFrCctErrorEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrCctErrorCct"),
)
if mibBuilder.loadTexts:
    wfFrCctErrorEntry.setStatus("mandatory")
_WfFrCctErrorCct_Type = Integer32
_WfFrCctErrorCct_Object = MibTableColumn
wfFrCctErrorCct = _WfFrCctErrorCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 4, 1, 1),
    _WfFrCctErrorCct_Type()
)
wfFrCctErrorCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCctErrorCct.setStatus("mandatory")
_WfFrCctErrorDrops_Type = Counter32
_WfFrCctErrorDrops_Object = MibTableColumn
wfFrCctErrorDrops = _WfFrCctErrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 4, 1, 2),
    _WfFrCctErrorDrops_Type()
)
wfFrCctErrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCctErrorDrops.setStatus("mandatory")
_WfFrCctErrorDiscards_Type = Counter32
_WfFrCctErrorDiscards_Object = MibTableColumn
wfFrCctErrorDiscards = _WfFrCctErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 4, 1, 3),
    _WfFrCctErrorDiscards_Type()
)
wfFrCctErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrCctErrorDiscards.setStatus("mandatory")
_WfFrServiceRecordTable_Object = MibTable
wfFrServiceRecordTable = _WfFrServiceRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5)
)
if mibBuilder.loadTexts:
    wfFrServiceRecordTable.setStatus("mandatory")
_WfFrServiceRecordEntry_Object = MibTableRow
wfFrServiceRecordEntry = _WfFrServiceRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1)
)
wfFrServiceRecordEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrServiceRecordLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrServiceRecordLLIndex"),
    (0, "Wellfleet-FR2-MIB", "wfFrServiceRecordCircuitNumber"),
)
if mibBuilder.loadTexts:
    wfFrServiceRecordEntry.setStatus("mandatory")


class _WfFrServiceRecordDelete_Type(Integer32):
    """Custom type wfFrServiceRecordDelete based on Integer32"""
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


_WfFrServiceRecordDelete_Type.__name__ = "Integer32"
_WfFrServiceRecordDelete_Object = MibTableColumn
wfFrServiceRecordDelete = _WfFrServiceRecordDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 1),
    _WfFrServiceRecordDelete_Type()
)
wfFrServiceRecordDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordDelete.setStatus("mandatory")
_WfFrServiceRecordLineNumber_Type = Integer32
_WfFrServiceRecordLineNumber_Object = MibTableColumn
wfFrServiceRecordLineNumber = _WfFrServiceRecordLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 2),
    _WfFrServiceRecordLineNumber_Type()
)
wfFrServiceRecordLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordLineNumber.setStatus("mandatory")
_WfFrServiceRecordLLIndex_Type = Integer32
_WfFrServiceRecordLLIndex_Object = MibTableColumn
wfFrServiceRecordLLIndex = _WfFrServiceRecordLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 3),
    _WfFrServiceRecordLLIndex_Type()
)
wfFrServiceRecordLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordLLIndex.setStatus("mandatory")
_WfFrServiceRecordCircuitNumber_Type = Integer32
_WfFrServiceRecordCircuitNumber_Object = MibTableColumn
wfFrServiceRecordCircuitNumber = _WfFrServiceRecordCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 4),
    _WfFrServiceRecordCircuitNumber_Type()
)
wfFrServiceRecordCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordCircuitNumber.setStatus("mandatory")


class _WfFrServiceRecordDefaultFlag_Type(Integer32):
    """Custom type wfFrServiceRecordDefaultFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_WfFrServiceRecordDefaultFlag_Type.__name__ = "Integer32"
_WfFrServiceRecordDefaultFlag_Object = MibTableColumn
wfFrServiceRecordDefaultFlag = _WfFrServiceRecordDefaultFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 5),
    _WfFrServiceRecordDefaultFlag_Type()
)
wfFrServiceRecordDefaultFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordDefaultFlag.setStatus("mandatory")
_WfFrServiceRecordNumberVCs_Type = Integer32
_WfFrServiceRecordNumberVCs_Object = MibTableColumn
wfFrServiceRecordNumberVCs = _WfFrServiceRecordNumberVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 6),
    _WfFrServiceRecordNumberVCs_Type()
)
wfFrServiceRecordNumberVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordNumberVCs.setStatus("mandatory")
_WfFrServiceRecordName_Type = DisplayString
_WfFrServiceRecordName_Object = MibTableColumn
wfFrServiceRecordName = _WfFrServiceRecordName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 7),
    _WfFrServiceRecordName_Type()
)
wfFrServiceRecordName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordName.setStatus("mandatory")


class _WfFrServiceRecordState_Type(Integer32):
    """Custom type wfFrServiceRecordState based on Integer32"""
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
          ("inactive", 1),
          ("invalid", 3))
    )


_WfFrServiceRecordState_Type.__name__ = "Integer32"
_WfFrServiceRecordState_Object = MibTableColumn
wfFrServiceRecordState = _WfFrServiceRecordState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 8),
    _WfFrServiceRecordState_Type()
)
wfFrServiceRecordState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordState.setStatus("mandatory")


class _WfFrServiceRecordPreMultiCircuit_Type(Integer32):
    """Custom type wfFrServiceRecordPreMultiCircuit based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordPreMultiCircuit_Object = MibTableColumn
wfFrServiceRecordPreMultiCircuit = _WfFrServiceRecordPreMultiCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 9),
    _WfFrServiceRecordPreMultiCircuit_Type()
)
wfFrServiceRecordPreMultiCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordPreMultiCircuit.setStatus("mandatory")


class _WfFrServiceRecordBackupFilterCct_Type(Integer32):
    """Custom type wfFrServiceRecordBackupFilterCct based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordBackupFilterCct_Object = MibTableColumn
wfFrServiceRecordBackupFilterCct = _WfFrServiceRecordBackupFilterCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 10),
    _WfFrServiceRecordBackupFilterCct_Type()
)
wfFrServiceRecordBackupFilterCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordBackupFilterCct.setStatus("mandatory")


class _WfFrServiceRecordBackupLineNumber_Type(Integer32):
    """Custom type wfFrServiceRecordBackupLineNumber based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordBackupLineNumber_Object = MibTableColumn
wfFrServiceRecordBackupLineNumber = _WfFrServiceRecordBackupLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 11),
    _WfFrServiceRecordBackupLineNumber_Type()
)
wfFrServiceRecordBackupLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordBackupLineNumber.setStatus("mandatory")


class _WfFrServiceRecordBackupLLIndex_Type(Integer32):
    """Custom type wfFrServiceRecordBackupLLIndex based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordBackupLLIndex_Object = MibTableColumn
wfFrServiceRecordBackupLLIndex = _WfFrServiceRecordBackupLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 12),
    _WfFrServiceRecordBackupLLIndex_Type()
)
wfFrServiceRecordBackupLLIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordBackupLLIndex.setStatus("mandatory")


class _WfFrServiceRecordBackupMainCct_Type(Integer32):
    """Custom type wfFrServiceRecordBackupMainCct based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordBackupMainCct_Object = MibTableColumn
wfFrServiceRecordBackupMainCct = _WfFrServiceRecordBackupMainCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 13),
    _WfFrServiceRecordBackupMainCct_Type()
)
wfFrServiceRecordBackupMainCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordBackupMainCct.setStatus("mandatory")


class _WfFrServiceRecordPrimaryLineNumber_Type(Integer32):
    """Custom type wfFrServiceRecordPrimaryLineNumber based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordPrimaryLineNumber_Object = MibTableColumn
wfFrServiceRecordPrimaryLineNumber = _WfFrServiceRecordPrimaryLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 14),
    _WfFrServiceRecordPrimaryLineNumber_Type()
)
wfFrServiceRecordPrimaryLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordPrimaryLineNumber.setStatus("mandatory")


class _WfFrServiceRecordPrimaryLLIndex_Type(Integer32):
    """Custom type wfFrServiceRecordPrimaryLLIndex based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordPrimaryLLIndex_Object = MibTableColumn
wfFrServiceRecordPrimaryLLIndex = _WfFrServiceRecordPrimaryLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 15),
    _WfFrServiceRecordPrimaryLLIndex_Type()
)
wfFrServiceRecordPrimaryLLIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordPrimaryLLIndex.setStatus("mandatory")


class _WfFrServiceRecordPrimaryMainCct_Type(Integer32):
    """Custom type wfFrServiceRecordPrimaryMainCct based on Integer32"""
    defaultValue = 0


_WfFrServiceRecordPrimaryMainCct_Object = MibTableColumn
wfFrServiceRecordPrimaryMainCct = _WfFrServiceRecordPrimaryMainCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 16),
    _WfFrServiceRecordPrimaryMainCct_Type()
)
wfFrServiceRecordPrimaryMainCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordPrimaryMainCct.setStatus("mandatory")


class _WfFrServiceRecordSVCDisable_Type(Integer32):
    """Custom type wfFrServiceRecordSVCDisable based on Integer32"""
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


_WfFrServiceRecordSVCDisable_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCDisable_Object = MibTableColumn
wfFrServiceRecordSVCDisable = _WfFrServiceRecordSVCDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 17),
    _WfFrServiceRecordSVCDisable_Type()
)
wfFrServiceRecordSVCDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCDisable.setStatus("mandatory")
_WfFrServiceRecordSVCLocNum_Type = DisplayString
_WfFrServiceRecordSVCLocNum_Object = MibTableColumn
wfFrServiceRecordSVCLocNum = _WfFrServiceRecordSVCLocNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 18),
    _WfFrServiceRecordSVCLocNum_Type()
)
wfFrServiceRecordSVCLocNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCLocNum.setStatus("mandatory")
_WfFrServiceRecordSVCLocSubAdr_Type = DisplayString
_WfFrServiceRecordSVCLocSubAdr_Object = MibTableColumn
wfFrServiceRecordSVCLocSubAdr = _WfFrServiceRecordSVCLocSubAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 19),
    _WfFrServiceRecordSVCLocSubAdr_Type()
)
wfFrServiceRecordSVCLocSubAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCLocSubAdr.setStatus("mandatory")


class _WfFrServiceRecordSVCLocPlan_Type(Integer32):
    """Custom type wfFrServiceRecordSVCLocPlan based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 3))
    )


_WfFrServiceRecordSVCLocPlan_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCLocPlan_Object = MibTableColumn
wfFrServiceRecordSVCLocPlan = _WfFrServiceRecordSVCLocPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 20),
    _WfFrServiceRecordSVCLocPlan_Type()
)
wfFrServiceRecordSVCLocPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCLocPlan.setStatus("mandatory")


class _WfFrServiceRecordSVCLocTypeNum_Type(Integer32):
    """Custom type wfFrServiceRecordSVCLocTypeNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("unknown", 1))
    )


_WfFrServiceRecordSVCLocTypeNum_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCLocTypeNum_Object = MibTableColumn
wfFrServiceRecordSVCLocTypeNum = _WfFrServiceRecordSVCLocTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 21),
    _WfFrServiceRecordSVCLocTypeNum_Type()
)
wfFrServiceRecordSVCLocTypeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCLocTypeNum.setStatus("mandatory")


class _WfFrServiceRecordSVCCallBlock_Type(Integer32):
    """Custom type wfFrServiceRecordSVCCallBlock based on Integer32"""
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
        *(("all", 4),
          ("inbound", 2),
          ("none", 1),
          ("outbound", 3))
    )


_WfFrServiceRecordSVCCallBlock_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCCallBlock_Object = MibTableColumn
wfFrServiceRecordSVCCallBlock = _WfFrServiceRecordSVCCallBlock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 22),
    _WfFrServiceRecordSVCCallBlock_Type()
)
wfFrServiceRecordSVCCallBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCCallBlock.setStatus("mandatory")


class _WfFrServiceRecordSVCInScrnDisable_Type(Integer32):
    """Custom type wfFrServiceRecordSVCInScrnDisable based on Integer32"""
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


_WfFrServiceRecordSVCInScrnDisable_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCInScrnDisable_Object = MibTableColumn
wfFrServiceRecordSVCInScrnDisable = _WfFrServiceRecordSVCInScrnDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 23),
    _WfFrServiceRecordSVCInScrnDisable_Type()
)
wfFrServiceRecordSVCInScrnDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCInScrnDisable.setStatus("mandatory")


class _WfFrServiceRecordSVCInScrnUsage_Type(Integer32):
    """Custom type wfFrServiceRecordSVCInScrnUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_WfFrServiceRecordSVCInScrnUsage_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCInScrnUsage_Object = MibTableColumn
wfFrServiceRecordSVCInScrnUsage = _WfFrServiceRecordSVCInScrnUsage_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 24),
    _WfFrServiceRecordSVCInScrnUsage_Type()
)
wfFrServiceRecordSVCInScrnUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCInScrnUsage.setStatus("mandatory")


class _WfFrServiceRecordSVCInactTimer_Type(Integer32):
    """Custom type wfFrServiceRecordSVCInactTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrServiceRecordSVCInactTimer_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCInactTimer_Object = MibTableColumn
wfFrServiceRecordSVCInactTimer = _WfFrServiceRecordSVCInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 25),
    _WfFrServiceRecordSVCInactTimer_Type()
)
wfFrServiceRecordSVCInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCInactTimer.setStatus("mandatory")


class _WfFrServiceRecordSVCInactMode_Type(Integer32):
    """Custom type wfFrServiceRecordSVCInactMode based on Integer32"""
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
        *(("bothdirections", 1),
          ("eitherdirection", 4),
          ("receiveonly", 3),
          ("transmitonly", 2))
    )


_WfFrServiceRecordSVCInactMode_Type.__name__ = "Integer32"
_WfFrServiceRecordSVCInactMode_Object = MibTableColumn
wfFrServiceRecordSVCInactMode = _WfFrServiceRecordSVCInactMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 26),
    _WfFrServiceRecordSVCInactMode_Type()
)
wfFrServiceRecordSVCInactMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrServiceRecordSVCInactMode.setStatus("mandatory")
_WfFrServiceRecordNumberStaticVCs_Type = Integer32
_WfFrServiceRecordNumberStaticVCs_Object = MibTableColumn
wfFrServiceRecordNumberStaticVCs = _WfFrServiceRecordNumberStaticVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 27),
    _WfFrServiceRecordNumberStaticVCs_Type()
)
wfFrServiceRecordNumberStaticVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordNumberStaticVCs.setStatus("mandatory")
_WfFrServiceRecordNumberDynamicVCs_Type = Integer32
_WfFrServiceRecordNumberDynamicVCs_Object = MibTableColumn
wfFrServiceRecordNumberDynamicVCs = _WfFrServiceRecordNumberDynamicVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 28),
    _WfFrServiceRecordNumberDynamicVCs_Type()
)
wfFrServiceRecordNumberDynamicVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordNumberDynamicVCs.setStatus("mandatory")
_WfFrServiceRecordNumberSVCs_Type = Integer32
_WfFrServiceRecordNumberSVCs_Object = MibTableColumn
wfFrServiceRecordNumberSVCs = _WfFrServiceRecordNumberSVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 29),
    _WfFrServiceRecordNumberSVCs_Type()
)
wfFrServiceRecordNumberSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordNumberSVCs.setStatus("mandatory")
_WfFrServiceRecordNumberActiveVCs_Type = Integer32
_WfFrServiceRecordNumberActiveVCs_Object = MibTableColumn
wfFrServiceRecordNumberActiveVCs = _WfFrServiceRecordNumberActiveVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 30),
    _WfFrServiceRecordNumberActiveVCs_Type()
)
wfFrServiceRecordNumberActiveVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordNumberActiveVCs.setStatus("mandatory")
_WfFrServiceRecordifLastChange_Type = TimeTicks
_WfFrServiceRecordifLastChange_Object = MibTableColumn
wfFrServiceRecordifLastChange = _WfFrServiceRecordifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 31),
    _WfFrServiceRecordifLastChange_Type()
)
wfFrServiceRecordifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifLastChange.setStatus("mandatory")
_WfFrServiceRecordifInOctets_Type = Counter32
_WfFrServiceRecordifInOctets_Object = MibTableColumn
wfFrServiceRecordifInOctets = _WfFrServiceRecordifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 32),
    _WfFrServiceRecordifInOctets_Type()
)
wfFrServiceRecordifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifInOctets.setStatus("mandatory")
_WfFrServiceRecordifInDiscards_Type = Counter32
_WfFrServiceRecordifInDiscards_Object = MibTableColumn
wfFrServiceRecordifInDiscards = _WfFrServiceRecordifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 33),
    _WfFrServiceRecordifInDiscards_Type()
)
wfFrServiceRecordifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifInDiscards.setStatus("mandatory")
_WfFrServiceRecordifOutOctets_Type = Counter32
_WfFrServiceRecordifOutOctets_Object = MibTableColumn
wfFrServiceRecordifOutOctets = _WfFrServiceRecordifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 34),
    _WfFrServiceRecordifOutOctets_Type()
)
wfFrServiceRecordifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifOutOctets.setStatus("mandatory")
_WfFrServiceRecordifOutDiscards_Type = Counter32
_WfFrServiceRecordifOutDiscards_Object = MibTableColumn
wfFrServiceRecordifOutDiscards = _WfFrServiceRecordifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 35),
    _WfFrServiceRecordifOutDiscards_Type()
)
wfFrServiceRecordifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifOutDiscards.setStatus("mandatory")
_WfFrServiceRecordifOutCtrlPkts_Type = Counter32
_WfFrServiceRecordifOutCtrlPkts_Object = MibTableColumn
wfFrServiceRecordifOutCtrlPkts = _WfFrServiceRecordifOutCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 36),
    _WfFrServiceRecordifOutCtrlPkts_Type()
)
wfFrServiceRecordifOutCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifOutCtrlPkts.setStatus("mandatory")
_WfFrServiceRecordifInCtrlPkts_Type = Counter32
_WfFrServiceRecordifInCtrlPkts_Object = MibTableColumn
wfFrServiceRecordifInCtrlPkts = _WfFrServiceRecordifInCtrlPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 5, 1, 37),
    _WfFrServiceRecordifInCtrlPkts_Type()
)
wfFrServiceRecordifInCtrlPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrServiceRecordifInCtrlPkts.setStatus("mandatory")
_WfFrSigTable_Object = MibTable
wfFrSigTable = _WfFrSigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6)
)
if mibBuilder.loadTexts:
    wfFrSigTable.setStatus("mandatory")
_WfFrSigEntry_Object = MibTableRow
wfFrSigEntry = _WfFrSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1)
)
wfFrSigEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrSigLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrSigLLIndex"),
)
if mibBuilder.loadTexts:
    wfFrSigEntry.setStatus("mandatory")


class _WfFrSigDelete_Type(Integer32):
    """Custom type wfFrSigDelete based on Integer32"""
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


_WfFrSigDelete_Type.__name__ = "Integer32"
_WfFrSigDelete_Object = MibTableColumn
wfFrSigDelete = _WfFrSigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 1),
    _WfFrSigDelete_Type()
)
wfFrSigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigDelete.setStatus("mandatory")


class _WfFrSigDisable_Type(Integer32):
    """Custom type wfFrSigDisable based on Integer32"""
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


_WfFrSigDisable_Type.__name__ = "Integer32"
_WfFrSigDisable_Object = MibTableColumn
wfFrSigDisable = _WfFrSigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 2),
    _WfFrSigDisable_Type()
)
wfFrSigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigDisable.setStatus("mandatory")
_WfFrSigLineNumber_Type = Integer32
_WfFrSigLineNumber_Object = MibTableColumn
wfFrSigLineNumber = _WfFrSigLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 3),
    _WfFrSigLineNumber_Type()
)
wfFrSigLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigLineNumber.setStatus("mandatory")
_WfFrSigLLIndex_Type = Integer32
_WfFrSigLLIndex_Object = MibTableColumn
wfFrSigLLIndex = _WfFrSigLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 4),
    _WfFrSigLLIndex_Type()
)
wfFrSigLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigLLIndex.setStatus("mandatory")


class _WfFrSigStatus_Type(Integer32):
    """Custom type wfFrSigStatus based on Integer32"""
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
          ("running", 1))
    )


_WfFrSigStatus_Type.__name__ = "Integer32"
_WfFrSigStatus_Object = MibTableColumn
wfFrSigStatus = _WfFrSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 5),
    _WfFrSigStatus_Type()
)
wfFrSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigStatus.setStatus("mandatory")
_WfFrSigCircuit_Type = Integer32
_WfFrSigCircuit_Object = MibTableColumn
wfFrSigCircuit = _WfFrSigCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 6),
    _WfFrSigCircuit_Type()
)
wfFrSigCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigCircuit.setStatus("mandatory")


class _WfFrSigConformance_Type(Integer32):
    """Custom type wfFrSigConformance based on Integer32"""
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
        *(("frf4", 1),
          ("priority", 2),
          ("q933", 3),
          ("t1617", 4))
    )


_WfFrSigConformance_Type.__name__ = "Integer32"
_WfFrSigConformance_Object = MibTableColumn
wfFrSigConformance = _WfFrSigConformance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 7),
    _WfFrSigConformance_Type()
)
wfFrSigConformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigConformance.setStatus("mandatory")


class _WfFrSigSvcIdleTimer_Type(Integer32):
    """Custom type wfFrSigSvcIdleTimer based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              360,
              14400)
        )
    )
    namedValues = NamedValues(
        *(("default", 360),
          ("max", 14400),
          ("min", 10))
    )


_WfFrSigSvcIdleTimer_Type.__name__ = "Integer32"
_WfFrSigSvcIdleTimer_Object = MibTableColumn
wfFrSigSvcIdleTimer = _WfFrSigSvcIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 8),
    _WfFrSigSvcIdleTimer_Type()
)
wfFrSigSvcIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigSvcIdleTimer.setStatus("mandatory")


class _WfFrSigMaxSvcs_Type(Integer32):
    """Custom type wfFrSigMaxSvcs based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("default", 16),
          ("max", 1024),
          ("min", 1))
    )


_WfFrSigMaxSvcs_Type.__name__ = "Integer32"
_WfFrSigMaxSvcs_Object = MibTableColumn
wfFrSigMaxSvcs = _WfFrSigMaxSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 9),
    _WfFrSigMaxSvcs_Type()
)
wfFrSigMaxSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigMaxSvcs.setStatus("mandatory")


class _WfFrSigSvcDeletePolicy_Type(Integer32):
    """Custom type wfFrSigSvcDeletePolicy based on Integer32"""
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
        *(("always", 1),
          ("never", 3),
          ("use", 2))
    )


_WfFrSigSvcDeletePolicy_Type.__name__ = "Integer32"
_WfFrSigSvcDeletePolicy_Object = MibTableColumn
wfFrSigSvcDeletePolicy = _WfFrSigSvcDeletePolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 10),
    _WfFrSigSvcDeletePolicy_Type()
)
wfFrSigSvcDeletePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigSvcDeletePolicy.setStatus("mandatory")


class _WfFrSigSvcReplacePolicy_Type(Integer32):
    """Custom type wfFrSigSvcReplacePolicy based on Integer32"""
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
        *(("always", 1),
          ("idle", 2),
          ("never", 3))
    )


_WfFrSigSvcReplacePolicy_Type.__name__ = "Integer32"
_WfFrSigSvcReplacePolicy_Object = MibTableColumn
wfFrSigSvcReplacePolicy = _WfFrSigSvcReplacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 11),
    _WfFrSigSvcReplacePolicy_Type()
)
wfFrSigSvcReplacePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigSvcReplacePolicy.setStatus("mandatory")


class _WfFrSigT303_Type(Integer32):
    """Custom type wfFrSigT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              120)
        )
    )
    namedValues = NamedValues(
        *(("default", 4),
          ("max", 120),
          ("min", 1))
    )


_WfFrSigT303_Type.__name__ = "Integer32"
_WfFrSigT303_Object = MibTableColumn
wfFrSigT303 = _WfFrSigT303_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 12),
    _WfFrSigT303_Type()
)
wfFrSigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigT303.setStatus("mandatory")


class _WfFrSigT305_Type(Integer32):
    """Custom type wfFrSigT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              30,
              120)
        )
    )
    namedValues = NamedValues(
        *(("default", 30),
          ("max", 120),
          ("min", 1))
    )


_WfFrSigT305_Type.__name__ = "Integer32"
_WfFrSigT305_Object = MibTableColumn
wfFrSigT305 = _WfFrSigT305_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 13),
    _WfFrSigT305_Type()
)
wfFrSigT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigT305.setStatus("mandatory")


class _WfFrSigT308_Type(Integer32):
    """Custom type wfFrSigT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              120)
        )
    )
    namedValues = NamedValues(
        *(("default", 4),
          ("max", 120),
          ("min", 1))
    )


_WfFrSigT308_Type.__name__ = "Integer32"
_WfFrSigT308_Object = MibTableColumn
wfFrSigT308 = _WfFrSigT308_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 14),
    _WfFrSigT308_Type()
)
wfFrSigT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigT308.setStatus("mandatory")


class _WfFrSigT310_Type(Integer32):
    """Custom type wfFrSigT310 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              30,
              120)
        )
    )
    namedValues = NamedValues(
        *(("default", 30),
          ("max", 120),
          ("min", 1))
    )


_WfFrSigT310_Type.__name__ = "Integer32"
_WfFrSigT310_Object = MibTableColumn
wfFrSigT310 = _WfFrSigT310_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 15),
    _WfFrSigT310_Type()
)
wfFrSigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigT310.setStatus("mandatory")


class _WfFrSigT322_Type(Integer32):
    """Custom type wfFrSigT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              120)
        )
    )
    namedValues = NamedValues(
        *(("default", 4),
          ("max", 120),
          ("min", 1))
    )


_WfFrSigT322_Type.__name__ = "Integer32"
_WfFrSigT322_Object = MibTableColumn
wfFrSigT322 = _WfFrSigT322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 16),
    _WfFrSigT322_Type()
)
wfFrSigT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigT322.setStatus("mandatory")


class _WfFrSigN322_Type(Integer32):
    """Custom type wfFrSigN322 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("max", 100),
          ("min", 1))
    )


_WfFrSigN322_Type.__name__ = "Integer32"
_WfFrSigN322_Object = MibTableColumn
wfFrSigN322 = _WfFrSigN322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 17),
    _WfFrSigN322_Type()
)
wfFrSigN322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSigN322.setStatus("mandatory")
_WfFrSigNumMaxSVCs_Type = Integer32
_WfFrSigNumMaxSVCs_Object = MibTableColumn
wfFrSigNumMaxSVCs = _WfFrSigNumMaxSVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 18),
    _WfFrSigNumMaxSVCs_Type()
)
wfFrSigNumMaxSVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigNumMaxSVCs.setStatus("mandatory")
_WfFrSigNumConnRej_Type = Counter32
_WfFrSigNumConnRej_Object = MibTableColumn
wfFrSigNumConnRej = _WfFrSigNumConnRej_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 19),
    _WfFrSigNumConnRej_Type()
)
wfFrSigNumConnRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigNumConnRej.setStatus("mandatory")
_WfFrSigNumSvcRej_Type = Counter32
_WfFrSigNumSvcRej_Object = MibTableColumn
wfFrSigNumSvcRej = _WfFrSigNumSvcRej_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 20),
    _WfFrSigNumSvcRej_Type()
)
wfFrSigNumSvcRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigNumSvcRej.setStatus("mandatory")
_WfFrSigNumSvcFailed_Type = Counter32
_WfFrSigNumSvcFailed_Object = MibTableColumn
wfFrSigNumSvcFailed = _WfFrSigNumSvcFailed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 6, 1, 21),
    _WfFrSigNumSvcFailed_Type()
)
wfFrSigNumSvcFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSigNumSvcFailed.setStatus("mandatory")
_WfFrLapfTable_Object = MibTable
wfFrLapfTable = _WfFrLapfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7)
)
if mibBuilder.loadTexts:
    wfFrLapfTable.setStatus("mandatory")
_WfFrLapfEntry_Object = MibTableRow
wfFrLapfEntry = _WfFrLapfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1)
)
wfFrLapfEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfLapfLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfLapfLLIndex"),
)
if mibBuilder.loadTexts:
    wfFrLapfEntry.setStatus("mandatory")


class _WfLapfDelete_Type(Integer32):
    """Custom type wfLapfDelete based on Integer32"""
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


_WfLapfDelete_Type.__name__ = "Integer32"
_WfLapfDelete_Object = MibTableColumn
wfLapfDelete = _WfLapfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 1),
    _WfLapfDelete_Type()
)
wfLapfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfDelete.setStatus("mandatory")


class _WfLapfDisable_Type(Integer32):
    """Custom type wfLapfDisable based on Integer32"""
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


_WfLapfDisable_Type.__name__ = "Integer32"
_WfLapfDisable_Object = MibTableColumn
wfLapfDisable = _WfLapfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 2),
    _WfLapfDisable_Type()
)
wfLapfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfDisable.setStatus("mandatory")
_WfLapfLineNumber_Type = Integer32
_WfLapfLineNumber_Object = MibTableColumn
wfLapfLineNumber = _WfLapfLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 3),
    _WfLapfLineNumber_Type()
)
wfLapfLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfLineNumber.setStatus("mandatory")
_WfLapfLLIndex_Type = Integer32
_WfLapfLLIndex_Object = MibTableColumn
wfLapfLLIndex = _WfLapfLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 4),
    _WfLapfLLIndex_Type()
)
wfLapfLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfLLIndex.setStatus("mandatory")


class _WfLapfStatus_Type(Integer32):
    """Custom type wfLapfStatus based on Integer32"""
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
          ("running", 1))
    )


_WfLapfStatus_Type.__name__ = "Integer32"
_WfLapfStatus_Object = MibTableColumn
wfLapfStatus = _WfLapfStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 5),
    _WfLapfStatus_Type()
)
wfLapfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfStatus.setStatus("mandatory")


class _WfLapfStationType_Type(Integer32):
    """Custom type wfLapfStationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkside", 1),
          ("userside", 2))
    )


_WfLapfStationType_Type.__name__ = "Integer32"
_WfLapfStationType_Object = MibTableColumn
wfLapfStationType = _WfLapfStationType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 6),
    _WfLapfStationType_Type()
)
wfLapfStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfStationType.setStatus("mandatory")


class _WfLapfActionInitiate_Type(Integer32):
    """Custom type wfLapfActionInitiate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfLapfActionInitiate_Type.__name__ = "Integer32"
_WfLapfActionInitiate_Object = MibTableColumn
wfLapfActionInitiate = _WfLapfActionInitiate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 7),
    _WfLapfActionInitiate_Type()
)
wfLapfActionInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfActionInitiate.setStatus("mandatory")


class _WfLapfT200_Type(Integer32):
    """Custom type wfLapfT200 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_WfLapfT200_Type.__name__ = "Integer32"
_WfLapfT200_Object = MibTableColumn
wfLapfT200 = _WfLapfT200_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 8),
    _WfLapfT200_Type()
)
wfLapfT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfT200.setStatus("mandatory")


class _WfLapfT203_Type(Integer32):
    """Custom type wfLapfT203 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfLapfT203_Type.__name__ = "Integer32"
_WfLapfT203_Object = MibTableColumn
wfLapfT203 = _WfLapfT203_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 9),
    _WfLapfT203_Type()
)
wfLapfT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfT203.setStatus("mandatory")


class _WfLapfN200_Type(Integer32):
    """Custom type wfLapfN200 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfLapfN200_Type.__name__ = "Integer32"
_WfLapfN200_Object = MibTableColumn
wfLapfN200 = _WfLapfN200_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 10),
    _WfLapfN200_Type()
)
wfLapfN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfN200.setStatus("mandatory")


class _WfLapfN201_Type(Integer32):
    """Custom type wfLapfN201 based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(260, 2052),
    )


_WfLapfN201_Type.__name__ = "Integer32"
_WfLapfN201_Object = MibTableColumn
wfLapfN201 = _WfLapfN201_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 11),
    _WfLapfN201_Type()
)
wfLapfN201.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfN201.setStatus("mandatory")


class _WfLapfK_Type(Integer32):
    """Custom type wfLapfK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLapfK_Type.__name__ = "Integer32"
_WfLapfK_Object = MibTableColumn
wfLapfK = _WfLapfK_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 12),
    _WfLapfK_Type()
)
wfLapfK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLapfK.setStatus("mandatory")
_WfLapfRxWin_Type = Integer32
_WfLapfRxWin_Object = MibTableColumn
wfLapfRxWin = _WfLapfRxWin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 13),
    _WfLapfRxWin_Type()
)
wfLapfRxWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfRxWin.setStatus("mandatory")
_WfLapfTxWin_Type = Integer32
_WfLapfTxWin_Object = MibTableColumn
wfLapfTxWin = _WfLapfTxWin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 14),
    _WfLapfTxWin_Type()
)
wfLapfTxWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfTxWin.setStatus("mandatory")
_WfLapfSABMESent_Type = Counter32
_WfLapfSABMESent_Object = MibTableColumn
wfLapfSABMESent = _WfLapfSABMESent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 15),
    _WfLapfSABMESent_Type()
)
wfLapfSABMESent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfSABMESent.setStatus("mandatory")
_WfLapfSABMERcvd_Type = Counter32
_WfLapfSABMERcvd_Object = MibTableColumn
wfLapfSABMERcvd = _WfLapfSABMERcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 16),
    _WfLapfSABMERcvd_Type()
)
wfLapfSABMERcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfSABMERcvd.setStatus("mandatory")
_WfLapfUASent_Type = Counter32
_WfLapfUASent_Object = MibTableColumn
wfLapfUASent = _WfLapfUASent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 17),
    _WfLapfUASent_Type()
)
wfLapfUASent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfUASent.setStatus("mandatory")
_WfLapfUARcvd_Type = Counter32
_WfLapfUARcvd_Object = MibTableColumn
wfLapfUARcvd = _WfLapfUARcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 18),
    _WfLapfUARcvd_Type()
)
wfLapfUARcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfUARcvd.setStatus("mandatory")
_WfLapfDISCSent_Type = Counter32
_WfLapfDISCSent_Object = MibTableColumn
wfLapfDISCSent = _WfLapfDISCSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 19),
    _WfLapfDISCSent_Type()
)
wfLapfDISCSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfDISCSent.setStatus("mandatory")
_WfLapfDISCRcvd_Type = Counter32
_WfLapfDISCRcvd_Object = MibTableColumn
wfLapfDISCRcvd = _WfLapfDISCRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 20),
    _WfLapfDISCRcvd_Type()
)
wfLapfDISCRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfDISCRcvd.setStatus("mandatory")
_WfLapfDMSent_Type = Counter32
_WfLapfDMSent_Object = MibTableColumn
wfLapfDMSent = _WfLapfDMSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 21),
    _WfLapfDMSent_Type()
)
wfLapfDMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfDMSent.setStatus("mandatory")
_WfLapfDMRcvd_Type = Counter32
_WfLapfDMRcvd_Object = MibTableColumn
wfLapfDMRcvd = _WfLapfDMRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 22),
    _WfLapfDMRcvd_Type()
)
wfLapfDMRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfDMRcvd.setStatus("mandatory")
_WfLapfFRMRSent_Type = Counter32
_WfLapfFRMRSent_Object = MibTableColumn
wfLapfFRMRSent = _WfLapfFRMRSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 23),
    _WfLapfFRMRSent_Type()
)
wfLapfFRMRSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfFRMRSent.setStatus("mandatory")
_WfLapfFRMRRcvd_Type = Counter32
_WfLapfFRMRRcvd_Object = MibTableColumn
wfLapfFRMRRcvd = _WfLapfFRMRRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 24),
    _WfLapfFRMRRcvd_Type()
)
wfLapfFRMRRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfFRMRRcvd.setStatus("mandatory")
_WfLapfRNRsSent_Type = Counter32
_WfLapfRNRsSent_Object = MibTableColumn
wfLapfRNRsSent = _WfLapfRNRsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 25),
    _WfLapfRNRsSent_Type()
)
wfLapfRNRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfRNRsSent.setStatus("mandatory")
_WfLapfRNRsRcvd_Type = Counter32
_WfLapfRNRsRcvd_Object = MibTableColumn
wfLapfRNRsRcvd = _WfLapfRNRsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 26),
    _WfLapfRNRsRcvd_Type()
)
wfLapfRNRsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfRNRsRcvd.setStatus("mandatory")
_WfLapfREJsSent_Type = Counter32
_WfLapfREJsSent_Object = MibTableColumn
wfLapfREJsSent = _WfLapfREJsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 27),
    _WfLapfREJsSent_Type()
)
wfLapfREJsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfREJsSent.setStatus("mandatory")
_WfLapfREJsRcvd_Type = Counter32
_WfLapfREJsRcvd_Object = MibTableColumn
wfLapfREJsRcvd = _WfLapfREJsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 28),
    _WfLapfREJsRcvd_Type()
)
wfLapfREJsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfREJsRcvd.setStatus("mandatory")
_WfLapfIFramesSent_Type = Counter32
_WfLapfIFramesSent_Object = MibTableColumn
wfLapfIFramesSent = _WfLapfIFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 29),
    _WfLapfIFramesSent_Type()
)
wfLapfIFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfIFramesSent.setStatus("mandatory")
_WfLapfIFramesRcvd_Type = Counter32
_WfLapfIFramesRcvd_Object = MibTableColumn
wfLapfIFramesRcvd = _WfLapfIFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 30),
    _WfLapfIFramesRcvd_Type()
)
wfLapfIFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfIFramesRcvd.setStatus("mandatory")
_WfLapfUISent_Type = Counter32
_WfLapfUISent_Object = MibTableColumn
wfLapfUISent = _WfLapfUISent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 31),
    _WfLapfUISent_Type()
)
wfLapfUISent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfUISent.setStatus("mandatory")
_WfLapfUIRcvd_Type = Counter32
_WfLapfUIRcvd_Object = MibTableColumn
wfLapfUIRcvd = _WfLapfUIRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 32),
    _WfLapfUIRcvd_Type()
)
wfLapfUIRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfUIRcvd.setStatus("mandatory")
_WfLapfRRsSent_Type = Counter32
_WfLapfRRsSent_Object = MibTableColumn
wfLapfRRsSent = _WfLapfRRsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 33),
    _WfLapfRRsSent_Type()
)
wfLapfRRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfRRsSent.setStatus("mandatory")
_WfLapfRRsRcvd_Type = Counter32
_WfLapfRRsRcvd_Object = MibTableColumn
wfLapfRRsRcvd = _WfLapfRRsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 34),
    _WfLapfRRsRcvd_Type()
)
wfLapfRRsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfRRsRcvd.setStatus("mandatory")
_WfLapfXIDSent_Type = Counter32
_WfLapfXIDSent_Object = MibTableColumn
wfLapfXIDSent = _WfLapfXIDSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 35),
    _WfLapfXIDSent_Type()
)
wfLapfXIDSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfXIDSent.setStatus("mandatory")
_WfLapfXIDRcvd_Type = Counter32
_WfLapfXIDRcvd_Object = MibTableColumn
wfLapfXIDRcvd = _WfLapfXIDRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 36),
    _WfLapfXIDRcvd_Type()
)
wfLapfXIDRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfXIDRcvd.setStatus("mandatory")
_WfLapfT200Timeouts_Type = Counter32
_WfLapfT200Timeouts_Object = MibTableColumn
wfLapfT200Timeouts = _WfLapfT200Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 37),
    _WfLapfT200Timeouts_Type()
)
wfLapfT200Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfT200Timeouts.setStatus("mandatory")
_WfLapfT203Timeouts_Type = Counter32
_WfLapfT203Timeouts_Object = MibTableColumn
wfLapfT203Timeouts = _WfLapfT203Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 38),
    _WfLapfT203Timeouts_Type()
)
wfLapfT203Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfT203Timeouts.setStatus("mandatory")
_WfLapfN200Exceeded_Type = Counter32
_WfLapfN200Exceeded_Object = MibTableColumn
wfLapfN200Exceeded = _WfLapfN200Exceeded_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 39),
    _WfLapfN200Exceeded_Type()
)
wfLapfN200Exceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfN200Exceeded.setStatus("mandatory")
_WfLapfN201Error_Type = Counter32
_WfLapfN201Error_Object = MibTableColumn
wfLapfN201Error = _WfLapfN201Error_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 7, 1, 40),
    _WfLapfN201Error_Type()
)
wfLapfN201Error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLapfN201Error.setStatus("mandatory")
_WfFrFRF4SigTable_Object = MibTable
wfFrFRF4SigTable = _WfFrFRF4SigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9)
)
if mibBuilder.loadTexts:
    wfFrFRF4SigTable.setStatus("mandatory")
_WfFrFRF4SigEntry_Object = MibTableRow
wfFrFRF4SigEntry = _WfFrFRF4SigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1)
)
wfFrFRF4SigEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrFRF4SigLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrFRF4SigLLIndex"),
)
if mibBuilder.loadTexts:
    wfFrFRF4SigEntry.setStatus("mandatory")


class _WfFrFRF4SigDelete_Type(Integer32):
    """Custom type wfFrFRF4SigDelete based on Integer32"""
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


_WfFrFRF4SigDelete_Type.__name__ = "Integer32"
_WfFrFRF4SigDelete_Object = MibTableColumn
wfFrFRF4SigDelete = _WfFrFRF4SigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 1),
    _WfFrFRF4SigDelete_Type()
)
wfFrFRF4SigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigDelete.setStatus("mandatory")


class _WfFrFRF4SigDisable_Type(Integer32):
    """Custom type wfFrFRF4SigDisable based on Integer32"""
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


_WfFrFRF4SigDisable_Type.__name__ = "Integer32"
_WfFrFRF4SigDisable_Object = MibTableColumn
wfFrFRF4SigDisable = _WfFrFRF4SigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 2),
    _WfFrFRF4SigDisable_Type()
)
wfFrFRF4SigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigDisable.setStatus("mandatory")
_WfFrFRF4SigLineNumber_Type = Integer32
_WfFrFRF4SigLineNumber_Object = MibTableColumn
wfFrFRF4SigLineNumber = _WfFrFRF4SigLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 3),
    _WfFrFRF4SigLineNumber_Type()
)
wfFrFRF4SigLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigLineNumber.setStatus("mandatory")
_WfFrFRF4SigLLIndex_Type = Integer32
_WfFrFRF4SigLLIndex_Object = MibTableColumn
wfFrFRF4SigLLIndex = _WfFrFRF4SigLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 4),
    _WfFrFRF4SigLLIndex_Type()
)
wfFrFRF4SigLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigLLIndex.setStatus("mandatory")


class _WfFrFRF4SigMaxSvcs_Type(Integer32):
    """Custom type wfFrFRF4SigMaxSvcs based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrFRF4SigMaxSvcs_Type.__name__ = "Integer32"
_WfFrFRF4SigMaxSvcs_Object = MibTableColumn
wfFrFRF4SigMaxSvcs = _WfFrFRF4SigMaxSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 5),
    _WfFrFRF4SigMaxSvcs_Type()
)
wfFrFRF4SigMaxSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigMaxSvcs.setStatus("mandatory")


class _WfFrFRF4SigT303_Type(Integer32):
    """Custom type wfFrFRF4SigT303 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrFRF4SigT303_Type.__name__ = "Integer32"
_WfFrFRF4SigT303_Object = MibTableColumn
wfFrFRF4SigT303 = _WfFrFRF4SigT303_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 6),
    _WfFrFRF4SigT303_Type()
)
wfFrFRF4SigT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigT303.setStatus("mandatory")


class _WfFrFRF4SigT305_Type(Integer32):
    """Custom type wfFrFRF4SigT305 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 90),
    )


_WfFrFRF4SigT305_Type.__name__ = "Integer32"
_WfFrFRF4SigT305_Object = MibTableColumn
wfFrFRF4SigT305 = _WfFrFRF4SigT305_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 7),
    _WfFrFRF4SigT305_Type()
)
wfFrFRF4SigT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigT305.setStatus("mandatory")


class _WfFrFRF4SigT308_Type(Integer32):
    """Custom type wfFrFRF4SigT308 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrFRF4SigT308_Type.__name__ = "Integer32"
_WfFrFRF4SigT308_Object = MibTableColumn
wfFrFRF4SigT308 = _WfFrFRF4SigT308_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 8),
    _WfFrFRF4SigT308_Type()
)
wfFrFRF4SigT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigT308.setStatus("mandatory")


class _WfFrFRF4SigT310_Type(Integer32):
    """Custom type wfFrFRF4SigT310 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrFRF4SigT310_Type.__name__ = "Integer32"
_WfFrFRF4SigT310_Object = MibTableColumn
wfFrFRF4SigT310 = _WfFrFRF4SigT310_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 9),
    _WfFrFRF4SigT310_Type()
)
wfFrFRF4SigT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigT310.setStatus("mandatory")


class _WfFrFRF4SigT322_Type(Integer32):
    """Custom type wfFrFRF4SigT322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 90),
    )


_WfFrFRF4SigT322_Type.__name__ = "Integer32"
_WfFrFRF4SigT322_Object = MibTableColumn
wfFrFRF4SigT322 = _WfFrFRF4SigT322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 10),
    _WfFrFRF4SigT322_Type()
)
wfFrFRF4SigT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigT322.setStatus("mandatory")


class _WfFrFRF4SigN322_Type(Integer32):
    """Custom type wfFrFRF4SigN322 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfFrFRF4SigN322_Type.__name__ = "Integer32"
_WfFrFRF4SigN322_Object = MibTableColumn
wfFrFRF4SigN322 = _WfFrFRF4SigN322_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 11),
    _WfFrFRF4SigN322_Type()
)
wfFrFRF4SigN322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrFRF4SigN322.setStatus("mandatory")
_WfFrFRF4SigFramesSent_Type = Counter32
_WfFrFRF4SigFramesSent_Object = MibTableColumn
wfFrFRF4SigFramesSent = _WfFrFRF4SigFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 12),
    _WfFrFRF4SigFramesSent_Type()
)
wfFrFRF4SigFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigFramesSent.setStatus("mandatory")
_WfFrFRF4SigOctetsSent_Type = Counter32
_WfFrFRF4SigOctetsSent_Object = MibTableColumn
wfFrFRF4SigOctetsSent = _WfFrFRF4SigOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 13),
    _WfFrFRF4SigOctetsSent_Type()
)
wfFrFRF4SigOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigOctetsSent.setStatus("mandatory")
_WfFrFRF4SigFramesReceived_Type = Counter32
_WfFrFRF4SigFramesReceived_Object = MibTableColumn
wfFrFRF4SigFramesReceived = _WfFrFRF4SigFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 14),
    _WfFrFRF4SigFramesReceived_Type()
)
wfFrFRF4SigFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigFramesReceived.setStatus("mandatory")
_WfFrFRF4SigOctetsReceived_Type = Counter32
_WfFrFRF4SigOctetsReceived_Object = MibTableColumn
wfFrFRF4SigOctetsReceived = _WfFrFRF4SigOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 15),
    _WfFrFRF4SigOctetsReceived_Type()
)
wfFrFRF4SigOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigOctetsReceived.setStatus("mandatory")
_WfFrFRF4SigFramesDropped_Type = Counter32
_WfFrFRF4SigFramesDropped_Object = MibTableColumn
wfFrFRF4SigFramesDropped = _WfFrFRF4SigFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 16),
    _WfFrFRF4SigFramesDropped_Type()
)
wfFrFRF4SigFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigFramesDropped.setStatus("mandatory")
_WfFrFRF4SigFramesDiscarded_Type = Counter32
_WfFrFRF4SigFramesDiscarded_Object = MibTableColumn
wfFrFRF4SigFramesDiscarded = _WfFrFRF4SigFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 17),
    _WfFrFRF4SigFramesDiscarded_Type()
)
wfFrFRF4SigFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigFramesDiscarded.setStatus("mandatory")
_WfFrFRF4SigSetupRx_Type = Counter32
_WfFrFRF4SigSetupRx_Object = MibTableColumn
wfFrFRF4SigSetupRx = _WfFrFRF4SigSetupRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 18),
    _WfFrFRF4SigSetupRx_Type()
)
wfFrFRF4SigSetupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigSetupRx.setStatus("mandatory")
_WfFrFRF4SigCallProcRx_Type = Counter32
_WfFrFRF4SigCallProcRx_Object = MibTableColumn
wfFrFRF4SigCallProcRx = _WfFrFRF4SigCallProcRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 19),
    _WfFrFRF4SigCallProcRx_Type()
)
wfFrFRF4SigCallProcRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigCallProcRx.setStatus("mandatory")
_WfFrFRF4SigConnectRx_Type = Counter32
_WfFrFRF4SigConnectRx_Object = MibTableColumn
wfFrFRF4SigConnectRx = _WfFrFRF4SigConnectRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 20),
    _WfFrFRF4SigConnectRx_Type()
)
wfFrFRF4SigConnectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigConnectRx.setStatus("mandatory")
_WfFrFRF4SigDisconnectRx_Type = Counter32
_WfFrFRF4SigDisconnectRx_Object = MibTableColumn
wfFrFRF4SigDisconnectRx = _WfFrFRF4SigDisconnectRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 21),
    _WfFrFRF4SigDisconnectRx_Type()
)
wfFrFRF4SigDisconnectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigDisconnectRx.setStatus("mandatory")
_WfFrFRF4SigReleaseRx_Type = Counter32
_WfFrFRF4SigReleaseRx_Object = MibTableColumn
wfFrFRF4SigReleaseRx = _WfFrFRF4SigReleaseRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 22),
    _WfFrFRF4SigReleaseRx_Type()
)
wfFrFRF4SigReleaseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigReleaseRx.setStatus("mandatory")
_WfFrFRF4SigReleaseCompleteRx_Type = Counter32
_WfFrFRF4SigReleaseCompleteRx_Object = MibTableColumn
wfFrFRF4SigReleaseCompleteRx = _WfFrFRF4SigReleaseCompleteRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 23),
    _WfFrFRF4SigReleaseCompleteRx_Type()
)
wfFrFRF4SigReleaseCompleteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigReleaseCompleteRx.setStatus("mandatory")
_WfFrFRF4SigStatusRx_Type = Counter32
_WfFrFRF4SigStatusRx_Object = MibTableColumn
wfFrFRF4SigStatusRx = _WfFrFRF4SigStatusRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 24),
    _WfFrFRF4SigStatusRx_Type()
)
wfFrFRF4SigStatusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigStatusRx.setStatus("mandatory")
_WfFrFRF4SigStatusEnquiryRx_Type = Counter32
_WfFrFRF4SigStatusEnquiryRx_Object = MibTableColumn
wfFrFRF4SigStatusEnquiryRx = _WfFrFRF4SigStatusEnquiryRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 25),
    _WfFrFRF4SigStatusEnquiryRx_Type()
)
wfFrFRF4SigStatusEnquiryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigStatusEnquiryRx.setStatus("mandatory")
_WfFrFRF4SigSetupTx_Type = Counter32
_WfFrFRF4SigSetupTx_Object = MibTableColumn
wfFrFRF4SigSetupTx = _WfFrFRF4SigSetupTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 26),
    _WfFrFRF4SigSetupTx_Type()
)
wfFrFRF4SigSetupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigSetupTx.setStatus("mandatory")
_WfFrFRF4SigCallProcTx_Type = Counter32
_WfFrFRF4SigCallProcTx_Object = MibTableColumn
wfFrFRF4SigCallProcTx = _WfFrFRF4SigCallProcTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 27),
    _WfFrFRF4SigCallProcTx_Type()
)
wfFrFRF4SigCallProcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigCallProcTx.setStatus("mandatory")
_WfFrFRF4SigConnectTx_Type = Counter32
_WfFrFRF4SigConnectTx_Object = MibTableColumn
wfFrFRF4SigConnectTx = _WfFrFRF4SigConnectTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 28),
    _WfFrFRF4SigConnectTx_Type()
)
wfFrFRF4SigConnectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigConnectTx.setStatus("mandatory")
_WfFrFRF4SigDisconnectTx_Type = Counter32
_WfFrFRF4SigDisconnectTx_Object = MibTableColumn
wfFrFRF4SigDisconnectTx = _WfFrFRF4SigDisconnectTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 29),
    _WfFrFRF4SigDisconnectTx_Type()
)
wfFrFRF4SigDisconnectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigDisconnectTx.setStatus("mandatory")
_WfFrFRF4SigReleaseTx_Type = Counter32
_WfFrFRF4SigReleaseTx_Object = MibTableColumn
wfFrFRF4SigReleaseTx = _WfFrFRF4SigReleaseTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 30),
    _WfFrFRF4SigReleaseTx_Type()
)
wfFrFRF4SigReleaseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigReleaseTx.setStatus("mandatory")
_WfFrFRF4SigReleaseCompleteTx_Type = Counter32
_WfFrFRF4SigReleaseCompleteTx_Object = MibTableColumn
wfFrFRF4SigReleaseCompleteTx = _WfFrFRF4SigReleaseCompleteTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 31),
    _WfFrFRF4SigReleaseCompleteTx_Type()
)
wfFrFRF4SigReleaseCompleteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigReleaseCompleteTx.setStatus("mandatory")
_WfFrFRF4SigStatusTx_Type = Counter32
_WfFrFRF4SigStatusTx_Object = MibTableColumn
wfFrFRF4SigStatusTx = _WfFrFRF4SigStatusTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 32),
    _WfFrFRF4SigStatusTx_Type()
)
wfFrFRF4SigStatusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigStatusTx.setStatus("mandatory")
_WfFrFRF4SigStatusEnquiryTx_Type = Counter32
_WfFrFRF4SigStatusEnquiryTx_Object = MibTableColumn
wfFrFRF4SigStatusEnquiryTx = _WfFrFRF4SigStatusEnquiryTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 9, 1, 33),
    _WfFrFRF4SigStatusEnquiryTx_Type()
)
wfFrFRF4SigStatusEnquiryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrFRF4SigStatusEnquiryTx.setStatus("mandatory")
_WfFrSVCOptionsTable_Object = MibTable
wfFrSVCOptionsTable = _WfFrSVCOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10)
)
if mibBuilder.loadTexts:
    wfFrSVCOptionsTable.setStatus("mandatory")
_WfFrSVCOptionsEntry_Object = MibTableRow
wfFrSVCOptionsEntry = _WfFrSVCOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1)
)
wfFrSVCOptionsEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrSVCOptionsLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrSVCOptionsLLIndex"),
    (0, "Wellfleet-FR2-MIB", "wfFrSVCOptionsCircuitNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrSVCOptionsInstanceIndex"),
)
if mibBuilder.loadTexts:
    wfFrSVCOptionsEntry.setStatus("mandatory")


class _WfFrSVCOptionsDelete_Type(Integer32):
    """Custom type wfFrSVCOptionsDelete based on Integer32"""
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


_WfFrSVCOptionsDelete_Type.__name__ = "Integer32"
_WfFrSVCOptionsDelete_Object = MibTableColumn
wfFrSVCOptionsDelete = _WfFrSVCOptionsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 1),
    _WfFrSVCOptionsDelete_Type()
)
wfFrSVCOptionsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsDelete.setStatus("mandatory")


class _WfFrSVCOptionsDisable_Type(Integer32):
    """Custom type wfFrSVCOptionsDisable based on Integer32"""
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


_WfFrSVCOptionsDisable_Type.__name__ = "Integer32"
_WfFrSVCOptionsDisable_Object = MibTableColumn
wfFrSVCOptionsDisable = _WfFrSVCOptionsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 2),
    _WfFrSVCOptionsDisable_Type()
)
wfFrSVCOptionsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsDisable.setStatus("mandatory")
_WfFrSVCOptionsLineNumber_Type = Integer32
_WfFrSVCOptionsLineNumber_Object = MibTableColumn
wfFrSVCOptionsLineNumber = _WfFrSVCOptionsLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 3),
    _WfFrSVCOptionsLineNumber_Type()
)
wfFrSVCOptionsLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLineNumber.setStatus("mandatory")
_WfFrSVCOptionsLLIndex_Type = Integer32
_WfFrSVCOptionsLLIndex_Object = MibTableColumn
wfFrSVCOptionsLLIndex = _WfFrSVCOptionsLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 4),
    _WfFrSVCOptionsLLIndex_Type()
)
wfFrSVCOptionsLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLIndex.setStatus("mandatory")
_WfFrSVCOptionsCircuitNumber_Type = Integer32
_WfFrSVCOptionsCircuitNumber_Object = MibTableColumn
wfFrSVCOptionsCircuitNumber = _WfFrSVCOptionsCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 5),
    _WfFrSVCOptionsCircuitNumber_Type()
)
wfFrSVCOptionsCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCOptionsCircuitNumber.setStatus("mandatory")
_WfFrSVCOptionsInstanceIndex_Type = Integer32
_WfFrSVCOptionsInstanceIndex_Object = MibTableColumn
wfFrSVCOptionsInstanceIndex = _WfFrSVCOptionsInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 6),
    _WfFrSVCOptionsInstanceIndex_Type()
)
wfFrSVCOptionsInstanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCOptionsInstanceIndex.setStatus("mandatory")
_WfFrSVCOptionsRemNum_Type = DisplayString
_WfFrSVCOptionsRemNum_Object = MibTableColumn
wfFrSVCOptionsRemNum = _WfFrSVCOptionsRemNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 7),
    _WfFrSVCOptionsRemNum_Type()
)
wfFrSVCOptionsRemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsRemNum.setStatus("mandatory")
_WfFrSVCOptionsRemSubAdr_Type = DisplayString
_WfFrSVCOptionsRemSubAdr_Object = MibTableColumn
wfFrSVCOptionsRemSubAdr = _WfFrSVCOptionsRemSubAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 8),
    _WfFrSVCOptionsRemSubAdr_Type()
)
wfFrSVCOptionsRemSubAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsRemSubAdr.setStatus("mandatory")


class _WfFrSVCOptionsRemPlan_Type(Integer32):
    """Custom type wfFrSVCOptionsRemPlan based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 3))
    )


_WfFrSVCOptionsRemPlan_Type.__name__ = "Integer32"
_WfFrSVCOptionsRemPlan_Object = MibTableColumn
wfFrSVCOptionsRemPlan = _WfFrSVCOptionsRemPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 9),
    _WfFrSVCOptionsRemPlan_Type()
)
wfFrSVCOptionsRemPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsRemPlan.setStatus("mandatory")


class _WfFrSVCOptionsRemTypeNum_Type(Integer32):
    """Custom type wfFrSVCOptionsRemTypeNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("unknown", 1))
    )


_WfFrSVCOptionsRemTypeNum_Type.__name__ = "Integer32"
_WfFrSVCOptionsRemTypeNum_Object = MibTableColumn
wfFrSVCOptionsRemTypeNum = _WfFrSVCOptionsRemTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 10),
    _WfFrSVCOptionsRemTypeNum_Type()
)
wfFrSVCOptionsRemTypeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsRemTypeNum.setStatus("mandatory")


class _WfFrSVCOptionsBroadcastDisable_Type(Integer32):
    """Custom type wfFrSVCOptionsBroadcastDisable based on Integer32"""
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


_WfFrSVCOptionsBroadcastDisable_Type.__name__ = "Integer32"
_WfFrSVCOptionsBroadcastDisable_Object = MibTableColumn
wfFrSVCOptionsBroadcastDisable = _WfFrSVCOptionsBroadcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 11),
    _WfFrSVCOptionsBroadcastDisable_Type()
)
wfFrSVCOptionsBroadcastDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsBroadcastDisable.setStatus("mandatory")


class _WfFrSVCOptionsInactTimer_Type(Integer32):
    """Custom type wfFrSVCOptionsInactTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsInactTimer_Type.__name__ = "Integer32"
_WfFrSVCOptionsInactTimer_Object = MibTableColumn
wfFrSVCOptionsInactTimer = _WfFrSVCOptionsInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 12),
    _WfFrSVCOptionsInactTimer_Type()
)
wfFrSVCOptionsInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsInactTimer.setStatus("mandatory")


class _WfFrSVCOptionsInactMode_Type(Integer32):
    """Custom type wfFrSVCOptionsInactMode based on Integer32"""
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
        *(("bothdirections", 1),
          ("eitherdirection", 4),
          ("receiveonly", 3),
          ("transmitonly", 2))
    )


_WfFrSVCOptionsInactMode_Type.__name__ = "Integer32"
_WfFrSVCOptionsInactMode_Object = MibTableColumn
wfFrSVCOptionsInactMode = _WfFrSVCOptionsInactMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 13),
    _WfFrSVCOptionsInactMode_Type()
)
wfFrSVCOptionsInactMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsInactMode.setStatus("mandatory")


class _WfFrSVCOptionsX213DataPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213DataPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213DataPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213DataPriority_Object = MibTableColumn
wfFrSVCOptionsX213DataPriority = _WfFrSVCOptionsX213DataPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 14),
    _WfFrSVCOptionsX213DataPriority_Type()
)
wfFrSVCOptionsX213DataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213DataPriority.setStatus("mandatory")


class _WfFrSVCOptionsX213DataLQAPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213DataLQAPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213DataLQAPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213DataLQAPriority_Object = MibTableColumn
wfFrSVCOptionsX213DataLQAPriority = _WfFrSVCOptionsX213DataLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 15),
    _WfFrSVCOptionsX213DataLQAPriority_Type()
)
wfFrSVCOptionsX213DataLQAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213DataLQAPriority.setStatus("mandatory")


class _WfFrSVCOptionsX213GainPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213GainPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213GainPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213GainPriority_Object = MibTableColumn
wfFrSVCOptionsX213GainPriority = _WfFrSVCOptionsX213GainPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 16),
    _WfFrSVCOptionsX213GainPriority_Type()
)
wfFrSVCOptionsX213GainPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213GainPriority.setStatus("mandatory")


class _WfFrSVCOptionsX213GainLQAPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213GainLQAPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213GainLQAPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213GainLQAPriority_Object = MibTableColumn
wfFrSVCOptionsX213GainLQAPriority = _WfFrSVCOptionsX213GainLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 17),
    _WfFrSVCOptionsX213GainLQAPriority_Type()
)
wfFrSVCOptionsX213GainLQAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213GainLQAPriority.setStatus("mandatory")


class _WfFrSVCOptionsX213KeepPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213KeepPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213KeepPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213KeepPriority_Object = MibTableColumn
wfFrSVCOptionsX213KeepPriority = _WfFrSVCOptionsX213KeepPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 18),
    _WfFrSVCOptionsX213KeepPriority_Type()
)
wfFrSVCOptionsX213KeepPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213KeepPriority.setStatus("mandatory")


class _WfFrSVCOptionsX213KeepLQAPriority_Type(Integer32):
    """Custom type wfFrSVCOptionsX213KeepLQAPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfFrSVCOptionsX213KeepLQAPriority_Type.__name__ = "Integer32"
_WfFrSVCOptionsX213KeepLQAPriority_Object = MibTableColumn
wfFrSVCOptionsX213KeepLQAPriority = _WfFrSVCOptionsX213KeepLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 19),
    _WfFrSVCOptionsX213KeepLQAPriority_Type()
)
wfFrSVCOptionsX213KeepLQAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsX213KeepLQAPriority.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreOutThroughput_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreOutThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreOutThroughput_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreOutThroughput_Object = MibTableColumn
wfFrSVCOptionsLLCoreOutThroughput = _WfFrSVCOptionsLLCoreOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 20),
    _WfFrSVCOptionsLLCoreOutThroughput_Type()
)
wfFrSVCOptionsLLCoreOutThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreOutThroughput.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreInThroughput_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreInThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreInThroughput_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreInThroughput_Object = MibTableColumn
wfFrSVCOptionsLLCoreInThroughput = _WfFrSVCOptionsLLCoreInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 21),
    _WfFrSVCOptionsLLCoreInThroughput_Type()
)
wfFrSVCOptionsLLCoreInThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreInThroughput.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreMinOutThroughput_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreMinOutThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreMinOutThroughput_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreMinOutThroughput_Object = MibTableColumn
wfFrSVCOptionsLLCoreMinOutThroughput = _WfFrSVCOptionsLLCoreMinOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 22),
    _WfFrSVCOptionsLLCoreMinOutThroughput_Type()
)
wfFrSVCOptionsLLCoreMinOutThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreMinOutThroughput.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreMinInThroughput_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreMinInThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreMinInThroughput_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreMinInThroughput_Object = MibTableColumn
wfFrSVCOptionsLLCoreMinInThroughput = _WfFrSVCOptionsLLCoreMinInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 23),
    _WfFrSVCOptionsLLCoreMinInThroughput_Type()
)
wfFrSVCOptionsLLCoreMinInThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreMinInThroughput.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreOutBc_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreOutBc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreOutBc_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreOutBc_Object = MibTableColumn
wfFrSVCOptionsLLCoreOutBc = _WfFrSVCOptionsLLCoreOutBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 24),
    _WfFrSVCOptionsLLCoreOutBc_Type()
)
wfFrSVCOptionsLLCoreOutBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreOutBc.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreInBc_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreInBc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreInBc_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreInBc_Object = MibTableColumn
wfFrSVCOptionsLLCoreInBc = _WfFrSVCOptionsLLCoreInBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 25),
    _WfFrSVCOptionsLLCoreInBc_Type()
)
wfFrSVCOptionsLLCoreInBc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreInBc.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreOutBe_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreOutBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreOutBe_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreOutBe_Object = MibTableColumn
wfFrSVCOptionsLLCoreOutBe = _WfFrSVCOptionsLLCoreOutBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 26),
    _WfFrSVCOptionsLLCoreOutBe_Type()
)
wfFrSVCOptionsLLCoreOutBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreOutBe.setStatus("mandatory")


class _WfFrSVCOptionsLLCoreInBe_Type(Integer32):
    """Custom type wfFrSVCOptionsLLCoreInBe based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrSVCOptionsLLCoreInBe_Type.__name__ = "Integer32"
_WfFrSVCOptionsLLCoreInBe_Object = MibTableColumn
wfFrSVCOptionsLLCoreInBe = _WfFrSVCOptionsLLCoreInBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 27),
    _WfFrSVCOptionsLLCoreInBe_Type()
)
wfFrSVCOptionsLLCoreInBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsLLCoreInBe.setStatus("mandatory")


class _WfFrSVCOptionsCongestionDisable_Type(Integer32):
    """Custom type wfFrSVCOptionsCongestionDisable based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("inherit", 3))
    )


_WfFrSVCOptionsCongestionDisable_Type.__name__ = "Integer32"
_WfFrSVCOptionsCongestionDisable_Object = MibTableColumn
wfFrSVCOptionsCongestionDisable = _WfFrSVCOptionsCongestionDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 28),
    _WfFrSVCOptionsCongestionDisable_Type()
)
wfFrSVCOptionsCongestionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsCongestionDisable.setStatus("mandatory")


class _WfFrSVCOptionsCongestionTmr_Type(Integer32):
    """Custom type wfFrSVCOptionsCongestionTmr based on Integer32"""
    defaultValue = 2

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
        *(("five", 10),
          ("four", 8),
          ("fourandhalf", 9),
          ("half", 1),
          ("one", 2),
          ("oneandhalf", 3),
          ("three", 6),
          ("threeandhalf", 7),
          ("two", 4),
          ("twoandhalf", 5))
    )


_WfFrSVCOptionsCongestionTmr_Type.__name__ = "Integer32"
_WfFrSVCOptionsCongestionTmr_Object = MibTableColumn
wfFrSVCOptionsCongestionTmr = _WfFrSVCOptionsCongestionTmr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 29),
    _WfFrSVCOptionsCongestionTmr_Type()
)
wfFrSVCOptionsCongestionTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsCongestionTmr.setStatus("mandatory")


class _WfFrSVCOptionsCongestionCtr_Type(Integer32):
    """Custom type wfFrSVCOptionsCongestionCtr based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_WfFrSVCOptionsCongestionCtr_Type.__name__ = "Integer32"
_WfFrSVCOptionsCongestionCtr_Object = MibTableColumn
wfFrSVCOptionsCongestionCtr = _WfFrSVCOptionsCongestionCtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 30),
    _WfFrSVCOptionsCongestionCtr_Type()
)
wfFrSVCOptionsCongestionCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsCongestionCtr.setStatus("mandatory")


class _WfFrSVCOptionsCongestionMethod_Type(Integer32):
    """Custom type wfFrSVCOptionsCongestionMethod based on Integer32"""
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
        *(("inherit", 4),
          ("shutdown", 1),
          ("throttle", 2),
          ("throttlethenshutdown", 3))
    )


_WfFrSVCOptionsCongestionMethod_Type.__name__ = "Integer32"
_WfFrSVCOptionsCongestionMethod_Object = MibTableColumn
wfFrSVCOptionsCongestionMethod = _WfFrSVCOptionsCongestionMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 31),
    _WfFrSVCOptionsCongestionMethod_Type()
)
wfFrSVCOptionsCongestionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsCongestionMethod.setStatus("mandatory")


class _WfFrSVCOptionsTrafficShapingDisable_Type(Integer32):
    """Custom type wfFrSVCOptionsTrafficShapingDisable based on Integer32"""
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


_WfFrSVCOptionsTrafficShapingDisable_Type.__name__ = "Integer32"
_WfFrSVCOptionsTrafficShapingDisable_Object = MibTableColumn
wfFrSVCOptionsTrafficShapingDisable = _WfFrSVCOptionsTrafficShapingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 32),
    _WfFrSVCOptionsTrafficShapingDisable_Type()
)
wfFrSVCOptionsTrafficShapingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsTrafficShapingDisable.setStatus("mandatory")


class _WfFrSVCOptionsWcpEnable_Type(Integer32):
    """Custom type wfFrSVCOptionsWcpEnable based on Integer32"""
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


_WfFrSVCOptionsWcpEnable_Type.__name__ = "Integer32"
_WfFrSVCOptionsWcpEnable_Object = MibTableColumn
wfFrSVCOptionsWcpEnable = _WfFrSVCOptionsWcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 33),
    _WfFrSVCOptionsWcpEnable_Type()
)
wfFrSVCOptionsWcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsWcpEnable.setStatus("mandatory")
_WfFrSVCOptionsName_Type = DisplayString
_WfFrSVCOptionsName_Object = MibTableColumn
wfFrSVCOptionsName = _WfFrSVCOptionsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 10, 1, 34),
    _WfFrSVCOptionsName_Type()
)
wfFrSVCOptionsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCOptionsName.setStatus("mandatory")
_WfFrSVCActiveCallTable_Object = MibTable
wfFrSVCActiveCallTable = _WfFrSVCActiveCallTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11)
)
if mibBuilder.loadTexts:
    wfFrSVCActiveCallTable.setStatus("mandatory")
_WfFrSVCActiveCallEntry_Object = MibTableRow
wfFrSVCActiveCallEntry = _WfFrSVCActiveCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1)
)
wfFrSVCActiveCallEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrSVCActiveCallLineNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrSVCActiveCallLLIndex"),
    (0, "Wellfleet-FR2-MIB", "wfFrSVCActiveCallDLCI"),
)
if mibBuilder.loadTexts:
    wfFrSVCActiveCallEntry.setStatus("mandatory")


class _WfFrSVCActiveCallDelete_Type(Integer32):
    """Custom type wfFrSVCActiveCallDelete based on Integer32"""
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


_WfFrSVCActiveCallDelete_Type.__name__ = "Integer32"
_WfFrSVCActiveCallDelete_Object = MibTableColumn
wfFrSVCActiveCallDelete = _WfFrSVCActiveCallDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 1),
    _WfFrSVCActiveCallDelete_Type()
)
wfFrSVCActiveCallDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallDelete.setStatus("mandatory")
_WfFrSVCActiveCallLineNumber_Type = Integer32
_WfFrSVCActiveCallLineNumber_Object = MibTableColumn
wfFrSVCActiveCallLineNumber = _WfFrSVCActiveCallLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 2),
    _WfFrSVCActiveCallLineNumber_Type()
)
wfFrSVCActiveCallLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLineNumber.setStatus("mandatory")
_WfFrSVCActiveCallLLIndex_Type = Integer32
_WfFrSVCActiveCallLLIndex_Object = MibTableColumn
wfFrSVCActiveCallLLIndex = _WfFrSVCActiveCallLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 3),
    _WfFrSVCActiveCallLLIndex_Type()
)
wfFrSVCActiveCallLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLIndex.setStatus("mandatory")
_WfFrSVCActiveCallDLCI_Type = Integer32
_WfFrSVCActiveCallDLCI_Object = MibTableColumn
wfFrSVCActiveCallDLCI = _WfFrSVCActiveCallDLCI_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 4),
    _WfFrSVCActiveCallDLCI_Type()
)
wfFrSVCActiveCallDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallDLCI.setStatus("mandatory")


class _WfFrSVCActiveCallDirection_Type(Integer32):
    """Custom type wfFrSVCActiveCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_WfFrSVCActiveCallDirection_Type.__name__ = "Integer32"
_WfFrSVCActiveCallDirection_Object = MibTableColumn
wfFrSVCActiveCallDirection = _WfFrSVCActiveCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 5),
    _WfFrSVCActiveCallDirection_Type()
)
wfFrSVCActiveCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallDirection.setStatus("mandatory")


class _WfFrSVCActiveCallCircuitNumber_Type(Integer32):
    """Custom type wfFrSVCActiveCallCircuitNumber based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallCircuitNumber_Object = MibTableColumn
wfFrSVCActiveCallCircuitNumber = _WfFrSVCActiveCallCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 6),
    _WfFrSVCActiveCallCircuitNumber_Type()
)
wfFrSVCActiveCallCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCircuitNumber.setStatus("mandatory")
_WfFrSVCActiveCallCalledNum_Type = DisplayString
_WfFrSVCActiveCallCalledNum_Object = MibTableColumn
wfFrSVCActiveCallCalledNum = _WfFrSVCActiveCallCalledNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 7),
    _WfFrSVCActiveCallCalledNum_Type()
)
wfFrSVCActiveCallCalledNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCalledNum.setStatus("mandatory")
_WfFrSVCActiveCallCalledSubAdr_Type = DisplayString
_WfFrSVCActiveCallCalledSubAdr_Object = MibTableColumn
wfFrSVCActiveCallCalledSubAdr = _WfFrSVCActiveCallCalledSubAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 8),
    _WfFrSVCActiveCallCalledSubAdr_Type()
)
wfFrSVCActiveCallCalledSubAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCalledSubAdr.setStatus("mandatory")


class _WfFrSVCActiveCallCalledPlan_Type(Integer32):
    """Custom type wfFrSVCActiveCallCalledPlan based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallCalledPlan_Object = MibTableColumn
wfFrSVCActiveCallCalledPlan = _WfFrSVCActiveCallCalledPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 9),
    _WfFrSVCActiveCallCalledPlan_Type()
)
wfFrSVCActiveCallCalledPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCalledPlan.setStatus("mandatory")


class _WfFrSVCActiveCallCalledTypeNum_Type(Integer32):
    """Custom type wfFrSVCActiveCallCalledTypeNum based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallCalledTypeNum_Object = MibTableColumn
wfFrSVCActiveCallCalledTypeNum = _WfFrSVCActiveCallCalledTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 10),
    _WfFrSVCActiveCallCalledTypeNum_Type()
)
wfFrSVCActiveCallCalledTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCalledTypeNum.setStatus("mandatory")
_WfFrSVCActiveCallCallingNum_Type = DisplayString
_WfFrSVCActiveCallCallingNum_Object = MibTableColumn
wfFrSVCActiveCallCallingNum = _WfFrSVCActiveCallCallingNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 11),
    _WfFrSVCActiveCallCallingNum_Type()
)
wfFrSVCActiveCallCallingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCallingNum.setStatus("mandatory")
_WfFrSVCActiveCallCallingSubAdr_Type = DisplayString
_WfFrSVCActiveCallCallingSubAdr_Object = MibTableColumn
wfFrSVCActiveCallCallingSubAdr = _WfFrSVCActiveCallCallingSubAdr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 12),
    _WfFrSVCActiveCallCallingSubAdr_Type()
)
wfFrSVCActiveCallCallingSubAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCallingSubAdr.setStatus("mandatory")


class _WfFrSVCActiveCallCallingPlan_Type(Integer32):
    """Custom type wfFrSVCActiveCallCallingPlan based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallCallingPlan_Object = MibTableColumn
wfFrSVCActiveCallCallingPlan = _WfFrSVCActiveCallCallingPlan_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 13),
    _WfFrSVCActiveCallCallingPlan_Type()
)
wfFrSVCActiveCallCallingPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCallingPlan.setStatus("mandatory")


class _WfFrSVCActiveCallCallingTypeNum_Type(Integer32):
    """Custom type wfFrSVCActiveCallCallingTypeNum based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallCallingTypeNum_Object = MibTableColumn
wfFrSVCActiveCallCallingTypeNum = _WfFrSVCActiveCallCallingTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 14),
    _WfFrSVCActiveCallCallingTypeNum_Type()
)
wfFrSVCActiveCallCallingTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallCallingTypeNum.setStatus("mandatory")


class _WfFrSVCActiveCallX213DataPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213DataPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213DataPriority_Object = MibTableColumn
wfFrSVCActiveCallX213DataPriority = _WfFrSVCActiveCallX213DataPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 15),
    _WfFrSVCActiveCallX213DataPriority_Type()
)
wfFrSVCActiveCallX213DataPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213DataPriority.setStatus("mandatory")


class _WfFrSVCActiveCallX213DataLQAPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213DataLQAPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213DataLQAPriority_Object = MibTableColumn
wfFrSVCActiveCallX213DataLQAPriority = _WfFrSVCActiveCallX213DataLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 16),
    _WfFrSVCActiveCallX213DataLQAPriority_Type()
)
wfFrSVCActiveCallX213DataLQAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213DataLQAPriority.setStatus("mandatory")


class _WfFrSVCActiveCallX213GainPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213GainPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213GainPriority_Object = MibTableColumn
wfFrSVCActiveCallX213GainPriority = _WfFrSVCActiveCallX213GainPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 17),
    _WfFrSVCActiveCallX213GainPriority_Type()
)
wfFrSVCActiveCallX213GainPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213GainPriority.setStatus("mandatory")


class _WfFrSVCActiveCallX213GainLQAPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213GainLQAPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213GainLQAPriority_Object = MibTableColumn
wfFrSVCActiveCallX213GainLQAPriority = _WfFrSVCActiveCallX213GainLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 18),
    _WfFrSVCActiveCallX213GainLQAPriority_Type()
)
wfFrSVCActiveCallX213GainLQAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213GainLQAPriority.setStatus("mandatory")


class _WfFrSVCActiveCallX213KeepPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213KeepPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213KeepPriority_Object = MibTableColumn
wfFrSVCActiveCallX213KeepPriority = _WfFrSVCActiveCallX213KeepPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 19),
    _WfFrSVCActiveCallX213KeepPriority_Type()
)
wfFrSVCActiveCallX213KeepPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213KeepPriority.setStatus("mandatory")


class _WfFrSVCActiveCallX213KeepLQAPriority_Type(Integer32):
    """Custom type wfFrSVCActiveCallX213KeepLQAPriority based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallX213KeepLQAPriority_Object = MibTableColumn
wfFrSVCActiveCallX213KeepLQAPriority = _WfFrSVCActiveCallX213KeepLQAPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 20),
    _WfFrSVCActiveCallX213KeepLQAPriority_Type()
)
wfFrSVCActiveCallX213KeepLQAPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallX213KeepLQAPriority.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreOutThroughput_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreOutThroughput based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreOutThroughput_Object = MibTableColumn
wfFrSVCActiveCallLLCoreOutThroughput = _WfFrSVCActiveCallLLCoreOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 21),
    _WfFrSVCActiveCallLLCoreOutThroughput_Type()
)
wfFrSVCActiveCallLLCoreOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreOutThroughput.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreInThroughput_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreInThroughput based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreInThroughput_Object = MibTableColumn
wfFrSVCActiveCallLLCoreInThroughput = _WfFrSVCActiveCallLLCoreInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 22),
    _WfFrSVCActiveCallLLCoreInThroughput_Type()
)
wfFrSVCActiveCallLLCoreInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreInThroughput.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreMinOutThroughput_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreMinOutThroughput based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreMinOutThroughput_Object = MibTableColumn
wfFrSVCActiveCallLLCoreMinOutThroughput = _WfFrSVCActiveCallLLCoreMinOutThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 23),
    _WfFrSVCActiveCallLLCoreMinOutThroughput_Type()
)
wfFrSVCActiveCallLLCoreMinOutThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreMinOutThroughput.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreMinInThroughput_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreMinInThroughput based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreMinInThroughput_Object = MibTableColumn
wfFrSVCActiveCallLLCoreMinInThroughput = _WfFrSVCActiveCallLLCoreMinInThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 24),
    _WfFrSVCActiveCallLLCoreMinInThroughput_Type()
)
wfFrSVCActiveCallLLCoreMinInThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreMinInThroughput.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreOutBc_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreOutBc based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreOutBc_Object = MibTableColumn
wfFrSVCActiveCallLLCoreOutBc = _WfFrSVCActiveCallLLCoreOutBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 25),
    _WfFrSVCActiveCallLLCoreOutBc_Type()
)
wfFrSVCActiveCallLLCoreOutBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreOutBc.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreInBc_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreInBc based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreInBc_Object = MibTableColumn
wfFrSVCActiveCallLLCoreInBc = _WfFrSVCActiveCallLLCoreInBc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 26),
    _WfFrSVCActiveCallLLCoreInBc_Type()
)
wfFrSVCActiveCallLLCoreInBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreInBc.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreOutBe_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreOutBe based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreOutBe_Object = MibTableColumn
wfFrSVCActiveCallLLCoreOutBe = _WfFrSVCActiveCallLLCoreOutBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 27),
    _WfFrSVCActiveCallLLCoreOutBe_Type()
)
wfFrSVCActiveCallLLCoreOutBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreOutBe.setStatus("mandatory")


class _WfFrSVCActiveCallLLCoreInBe_Type(Integer32):
    """Custom type wfFrSVCActiveCallLLCoreInBe based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallLLCoreInBe_Object = MibTableColumn
wfFrSVCActiveCallLLCoreInBe = _WfFrSVCActiveCallLLCoreInBe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 28),
    _WfFrSVCActiveCallLLCoreInBe_Type()
)
wfFrSVCActiveCallLLCoreInBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallLLCoreInBe.setStatus("mandatory")


class _WfFrSVCActiveCallConnectTime_Type(Integer32):
    """Custom type wfFrSVCActiveCallConnectTime based on Integer32"""
    defaultValue = 0


_WfFrSVCActiveCallConnectTime_Object = MibTableColumn
wfFrSVCActiveCallConnectTime = _WfFrSVCActiveCallConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 11, 1, 29),
    _WfFrSVCActiveCallConnectTime_Type()
)
wfFrSVCActiveCallConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrSVCActiveCallConnectTime.setStatus("mandatory")
_WfFrPtIntfTable_Object = MibTable
wfFrPtIntfTable = _WfFrPtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12)
)
if mibBuilder.loadTexts:
    wfFrPtIntfTable.setStatus("mandatory")
_WfFrPtIntfEntry_Object = MibTableRow
wfFrPtIntfEntry = _WfFrPtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1)
)
wfFrPtIntfEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrPtIntfCct"),
    (0, "Wellfleet-FR2-MIB", "wfFrPtIntfDlci"),
)
if mibBuilder.loadTexts:
    wfFrPtIntfEntry.setStatus("mandatory")


class _WfFrPtIntfDelete_Type(Integer32):
    """Custom type wfFrPtIntfDelete based on Integer32"""
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


_WfFrPtIntfDelete_Type.__name__ = "Integer32"
_WfFrPtIntfDelete_Object = MibTableColumn
wfFrPtIntfDelete = _WfFrPtIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 1),
    _WfFrPtIntfDelete_Type()
)
wfFrPtIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrPtIntfDelete.setStatus("mandatory")


class _WfFrPtIntfDisable_Type(Integer32):
    """Custom type wfFrPtIntfDisable based on Integer32"""
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


_WfFrPtIntfDisable_Type.__name__ = "Integer32"
_WfFrPtIntfDisable_Object = MibTableColumn
wfFrPtIntfDisable = _WfFrPtIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 2),
    _WfFrPtIntfDisable_Type()
)
wfFrPtIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrPtIntfDisable.setStatus("mandatory")
_WfFrPtIntfCct_Type = Integer32
_WfFrPtIntfCct_Object = MibTableColumn
wfFrPtIntfCct = _WfFrPtIntfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 3),
    _WfFrPtIntfCct_Type()
)
wfFrPtIntfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfCct.setStatus("mandatory")
_WfFrPtIntfDlci_Type = Integer32
_WfFrPtIntfDlci_Object = MibTableColumn
wfFrPtIntfDlci = _WfFrPtIntfDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 4),
    _WfFrPtIntfDlci_Type()
)
wfFrPtIntfDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfDlci.setStatus("mandatory")


class _WfFrPtIntfState_Type(Integer32):
    """Custom type wfFrPtIntfState based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("invalid", 3),
          ("notpresent", 4))
    )


_WfFrPtIntfState_Type.__name__ = "Integer32"
_WfFrPtIntfState_Object = MibTableColumn
wfFrPtIntfState = _WfFrPtIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 5),
    _WfFrPtIntfState_Type()
)
wfFrPtIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfState.setStatus("mandatory")
_WfFrPtIntfRxFrames_Type = Counter32
_WfFrPtIntfRxFrames_Object = MibTableColumn
wfFrPtIntfRxFrames = _WfFrPtIntfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 6),
    _WfFrPtIntfRxFrames_Type()
)
wfFrPtIntfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfRxFrames.setStatus("mandatory")
_WfFrPtIntfTxFrames_Type = Counter32
_WfFrPtIntfTxFrames_Object = MibTableColumn
wfFrPtIntfTxFrames = _WfFrPtIntfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 7),
    _WfFrPtIntfTxFrames_Type()
)
wfFrPtIntfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfTxFrames.setStatus("mandatory")
_WfFrPtIntfDiscards_Type = Counter32
_WfFrPtIntfDiscards_Object = MibTableColumn
wfFrPtIntfDiscards = _WfFrPtIntfDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 8),
    _WfFrPtIntfDiscards_Type()
)
wfFrPtIntfDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfDiscards.setStatus("mandatory")
_WfFrPtIntfDrops_Type = Counter32
_WfFrPtIntfDrops_Object = MibTableColumn
wfFrPtIntfDrops = _WfFrPtIntfDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 12, 1, 9),
    _WfFrPtIntfDrops_Type()
)
wfFrPtIntfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtIntfDrops.setStatus("mandatory")
_WfFrPtMappingTable_Object = MibTable
wfFrPtMappingTable = _WfFrPtMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13)
)
if mibBuilder.loadTexts:
    wfFrPtMappingTable.setStatus("mandatory")
_WfFrPtMappingEntry_Object = MibTableRow
wfFrPtMappingEntry = _WfFrPtMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1)
)
wfFrPtMappingEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrPtMappingCctA"),
    (0, "Wellfleet-FR2-MIB", "wfFrPtMappingDlciA"),
    (0, "Wellfleet-FR2-MIB", "wfFrPtMappingCctB"),
    (0, "Wellfleet-FR2-MIB", "wfFrPtMappingDlciB"),
)
if mibBuilder.loadTexts:
    wfFrPtMappingEntry.setStatus("mandatory")


class _WfFrPtMappingDelete_Type(Integer32):
    """Custom type wfFrPtMappingDelete based on Integer32"""
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


_WfFrPtMappingDelete_Type.__name__ = "Integer32"
_WfFrPtMappingDelete_Object = MibTableColumn
wfFrPtMappingDelete = _WfFrPtMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 1),
    _WfFrPtMappingDelete_Type()
)
wfFrPtMappingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrPtMappingDelete.setStatus("mandatory")


class _WfFrPtMappingDisable_Type(Integer32):
    """Custom type wfFrPtMappingDisable based on Integer32"""
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


_WfFrPtMappingDisable_Type.__name__ = "Integer32"
_WfFrPtMappingDisable_Object = MibTableColumn
wfFrPtMappingDisable = _WfFrPtMappingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 2),
    _WfFrPtMappingDisable_Type()
)
wfFrPtMappingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrPtMappingDisable.setStatus("mandatory")
_WfFrPtMappingCctA_Type = Integer32
_WfFrPtMappingCctA_Object = MibTableColumn
wfFrPtMappingCctA = _WfFrPtMappingCctA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 3),
    _WfFrPtMappingCctA_Type()
)
wfFrPtMappingCctA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtMappingCctA.setStatus("mandatory")
_WfFrPtMappingDlciA_Type = Integer32
_WfFrPtMappingDlciA_Object = MibTableColumn
wfFrPtMappingDlciA = _WfFrPtMappingDlciA_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 4),
    _WfFrPtMappingDlciA_Type()
)
wfFrPtMappingDlciA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtMappingDlciA.setStatus("mandatory")
_WfFrPtMappingCctB_Type = Integer32
_WfFrPtMappingCctB_Object = MibTableColumn
wfFrPtMappingCctB = _WfFrPtMappingCctB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 5),
    _WfFrPtMappingCctB_Type()
)
wfFrPtMappingCctB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtMappingCctB.setStatus("mandatory")
_WfFrPtMappingDlciB_Type = Integer32
_WfFrPtMappingDlciB_Object = MibTableColumn
wfFrPtMappingDlciB = _WfFrPtMappingDlciB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 6),
    _WfFrPtMappingDlciB_Type()
)
wfFrPtMappingDlciB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtMappingDlciB.setStatus("mandatory")


class _WfFrPtMappingState_Type(Integer32):
    """Custom type wfFrPtMappingState based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("invalid", 3),
          ("notpresent", 4))
    )


_WfFrPtMappingState_Type.__name__ = "Integer32"
_WfFrPtMappingState_Object = MibTableColumn
wfFrPtMappingState = _WfFrPtMappingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 13, 1, 7),
    _WfFrPtMappingState_Type()
)
wfFrPtMappingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrPtMappingState.setStatus("mandatory")
_WfFrMlTable_Object = MibTable
wfFrMlTable = _WfFrMlTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14)
)
if mibBuilder.loadTexts:
    wfFrMlTable.setStatus("mandatory")
_WfFrMlEntry_Object = MibTableRow
wfFrMlEntry = _WfFrMlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1)
)
wfFrMlEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrMlCircuitNumber"),
)
if mibBuilder.loadTexts:
    wfFrMlEntry.setStatus("mandatory")


class _WfFrMlDelete_Type(Integer32):
    """Custom type wfFrMlDelete based on Integer32"""
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


_WfFrMlDelete_Type.__name__ = "Integer32"
_WfFrMlDelete_Object = MibTableColumn
wfFrMlDelete = _WfFrMlDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 1),
    _WfFrMlDelete_Type()
)
wfFrMlDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlDelete.setStatus("mandatory")


class _WfFrMlCircuitNumber_Type(Integer32):
    """Custom type wfFrMlCircuitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfFrMlCircuitNumber_Type.__name__ = "Integer32"
_WfFrMlCircuitNumber_Object = MibTableColumn
wfFrMlCircuitNumber = _WfFrMlCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 2),
    _WfFrMlCircuitNumber_Type()
)
wfFrMlCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlCircuitNumber.setStatus("mandatory")


class _WfFrMlMode_Type(Integer32):
    """Custom type wfFrMlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtedte", 1),
          ("uni", 2))
    )


_WfFrMlMode_Type.__name__ = "Integer32"
_WfFrMlMode_Object = MibTableColumn
wfFrMlMode = _WfFrMlMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 3),
    _WfFrMlMode_Type()
)
wfFrMlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlMode.setStatus("mandatory")


class _WfFrMlFragPermEnable_Type(Integer32):
    """Custom type wfFrMlFragPermEnable based on Integer32"""
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


_WfFrMlFragPermEnable_Type.__name__ = "Integer32"
_WfFrMlFragPermEnable_Object = MibTableColumn
wfFrMlFragPermEnable = _WfFrMlFragPermEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 4),
    _WfFrMlFragPermEnable_Type()
)
wfFrMlFragPermEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlFragPermEnable.setStatus("mandatory")


class _WfFrMlCircuitMaxBuffers_Type(Integer32):
    """Custom type wfFrMlCircuitMaxBuffers based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_WfFrMlCircuitMaxBuffers_Type.__name__ = "Integer32"
_WfFrMlCircuitMaxBuffers_Object = MibTableColumn
wfFrMlCircuitMaxBuffers = _WfFrMlCircuitMaxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 5),
    _WfFrMlCircuitMaxBuffers_Type()
)
wfFrMlCircuitMaxBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlCircuitMaxBuffers.setStatus("mandatory")


class _WfFrMlFragTriggerSize_Type(Integer32):
    """Custom type wfFrMlFragTriggerSize based on Integer32"""
    defaultValue = 256


_WfFrMlFragTriggerSize_Object = MibTableColumn
wfFrMlFragTriggerSize = _WfFrMlFragTriggerSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 6),
    _WfFrMlFragTriggerSize_Type()
)
wfFrMlFragTriggerSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlFragTriggerSize.setStatus("mandatory")


class _WfFrMlFragStrict_Type(Integer32):
    """Custom type wfFrMlFragStrict based on Integer32"""
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


_WfFrMlFragStrict_Type.__name__ = "Integer32"
_WfFrMlFragStrict_Object = MibTableColumn
wfFrMlFragStrict = _WfFrMlFragStrict_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 7),
    _WfFrMlFragStrict_Type()
)
wfFrMlFragStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlFragStrict.setStatus("mandatory")


class _WfFrMlAggVCStatusMode_Type(Integer32):
    """Custom type wfFrMlAggVCStatusMode based on Integer32"""
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
        *(("allactive", 2),
          ("anyactive", 1),
          ("other", 3))
    )


_WfFrMlAggVCStatusMode_Type.__name__ = "Integer32"
_WfFrMlAggVCStatusMode_Object = MibTableColumn
wfFrMlAggVCStatusMode = _WfFrMlAggVCStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 8),
    _WfFrMlAggVCStatusMode_Type()
)
wfFrMlAggVCStatusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlAggVCStatusMode.setStatus("mandatory")


class _WfFrMlCompressionEnable_Type(Integer32):
    """Custom type wfFrMlCompressionEnable based on Integer32"""
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


_WfFrMlCompressionEnable_Type.__name__ = "Integer32"
_WfFrMlCompressionEnable_Object = MibTableColumn
wfFrMlCompressionEnable = _WfFrMlCompressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 9),
    _WfFrMlCompressionEnable_Type()
)
wfFrMlCompressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlCompressionEnable.setStatus("mandatory")
_WfFrMlHomeSlot_Type = Integer32
_WfFrMlHomeSlot_Object = MibTableColumn
wfFrMlHomeSlot = _WfFrMlHomeSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 10),
    _WfFrMlHomeSlot_Type()
)
wfFrMlHomeSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlHomeSlot.setStatus("mandatory")
_WfFrMlStatsLineCnt_Type = Gauge32
_WfFrMlStatsLineCnt_Object = MibTableColumn
wfFrMlStatsLineCnt = _WfFrMlStatsLineCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 11),
    _WfFrMlStatsLineCnt_Type()
)
wfFrMlStatsLineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsLineCnt.setStatus("mandatory")
_WfFrMlStatsBundleSpd_Type = Gauge32
_WfFrMlStatsBundleSpd_Object = MibTableColumn
wfFrMlStatsBundleSpd = _WfFrMlStatsBundleSpd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 12),
    _WfFrMlStatsBundleSpd_Type()
)
wfFrMlStatsBundleSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsBundleSpd.setStatus("mandatory")
_WfFrMlStatsTxOctets_Type = Counter32
_WfFrMlStatsTxOctets_Object = MibTableColumn
wfFrMlStatsTxOctets = _WfFrMlStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 13),
    _WfFrMlStatsTxOctets_Type()
)
wfFrMlStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsTxOctets.setStatus("mandatory")
_WfFrMlStatsTxPkts_Type = Counter32
_WfFrMlStatsTxPkts_Object = MibTableColumn
wfFrMlStatsTxPkts = _WfFrMlStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 14),
    _WfFrMlStatsTxPkts_Type()
)
wfFrMlStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsTxPkts.setStatus("mandatory")
_WfFrMlStatsAvgTxListLen_Type = Gauge32
_WfFrMlStatsAvgTxListLen_Object = MibTableColumn
wfFrMlStatsAvgTxListLen = _WfFrMlStatsAvgTxListLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 15),
    _WfFrMlStatsAvgTxListLen_Type()
)
wfFrMlStatsAvgTxListLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsAvgTxListLen.setStatus("mandatory")
_WfFrMlStatsRxOctets_Type = Counter32
_WfFrMlStatsRxOctets_Object = MibTableColumn
wfFrMlStatsRxOctets = _WfFrMlStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 16),
    _WfFrMlStatsRxOctets_Type()
)
wfFrMlStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsRxOctets.setStatus("mandatory")
_WfFrMlStatsRxPkts_Type = Counter32
_WfFrMlStatsRxPkts_Object = MibTableColumn
wfFrMlStatsRxPkts = _WfFrMlStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 17),
    _WfFrMlStatsRxPkts_Type()
)
wfFrMlStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsRxPkts.setStatus("mandatory")
_WfFrMlStatsReasmFails_Type = Counter32
_WfFrMlStatsReasmFails_Object = MibTableColumn
wfFrMlStatsReasmFails = _WfFrMlStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 18),
    _WfFrMlStatsReasmFails_Type()
)
wfFrMlStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsReasmFails.setStatus("mandatory")
_WfFrMlStatsSeqNumberLost_Type = Counter32
_WfFrMlStatsSeqNumberLost_Object = MibTableColumn
wfFrMlStatsSeqNumberLost = _WfFrMlStatsSeqNumberLost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 19),
    _WfFrMlStatsSeqNumberLost_Type()
)
wfFrMlStatsSeqNumberLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsSeqNumberLost.setStatus("mandatory")
_WfFrMlStatsSeqNumberArrivedLate_Type = Counter32
_WfFrMlStatsSeqNumberArrivedLate_Object = MibTableColumn
wfFrMlStatsSeqNumberArrivedLate = _WfFrMlStatsSeqNumberArrivedLate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 20),
    _WfFrMlStatsSeqNumberArrivedLate_Type()
)
wfFrMlStatsSeqNumberArrivedLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsSeqNumberArrivedLate.setStatus("mandatory")
_WfFrMlStatsReSeqBufferCnt_Type = Gauge32
_WfFrMlStatsReSeqBufferCnt_Object = MibTableColumn
wfFrMlStatsReSeqBufferCnt = _WfFrMlStatsReSeqBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 21),
    _WfFrMlStatsReSeqBufferCnt_Type()
)
wfFrMlStatsReSeqBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsReSeqBufferCnt.setStatus("mandatory")
_WfFrMlStatsReSeqBufferMax_Type = Counter32
_WfFrMlStatsReSeqBufferMax_Object = MibTableColumn
wfFrMlStatsReSeqBufferMax = _WfFrMlStatsReSeqBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 22),
    _WfFrMlStatsReSeqBufferMax_Type()
)
wfFrMlStatsReSeqBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsReSeqBufferMax.setStatus("mandatory")
_WfFrMlStatsExceededBufferMax_Type = Counter32
_WfFrMlStatsExceededBufferMax_Object = MibTableColumn
wfFrMlStatsExceededBufferMax = _WfFrMlStatsExceededBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 23),
    _WfFrMlStatsExceededBufferMax_Type()
)
wfFrMlStatsExceededBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsExceededBufferMax.setStatus("mandatory")
_WfFrMlStatsLinkIdleEvents_Type = Counter32
_WfFrMlStatsLinkIdleEvents_Object = MibTableColumn
wfFrMlStatsLinkIdleEvents = _WfFrMlStatsLinkIdleEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 24),
    _WfFrMlStatsLinkIdleEvents_Type()
)
wfFrMlStatsLinkIdleEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsLinkIdleEvents.setStatus("mandatory")


class _WfFrMlStatsCalcPercent_Type(Integer32):
    """Custom type wfFrMlStatsCalcPercent based on Integer32"""
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


_WfFrMlStatsCalcPercent_Type.__name__ = "Integer32"
_WfFrMlStatsCalcPercent_Object = MibTableColumn
wfFrMlStatsCalcPercent = _WfFrMlStatsCalcPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 25),
    _WfFrMlStatsCalcPercent_Type()
)
wfFrMlStatsCalcPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlStatsCalcPercent.setStatus("mandatory")
_WfFrMlStatsDebug_Type = Integer32
_WfFrMlStatsDebug_Object = MibTableColumn
wfFrMlStatsDebug = _WfFrMlStatsDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 26),
    _WfFrMlStatsDebug_Type()
)
wfFrMlStatsDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlStatsDebug.setStatus("mandatory")
_WfFrMlStatsReassmBufferCnt_Type = Gauge32
_WfFrMlStatsReassmBufferCnt_Object = MibTableColumn
wfFrMlStatsReassmBufferCnt = _WfFrMlStatsReassmBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 27),
    _WfFrMlStatsReassmBufferCnt_Type()
)
wfFrMlStatsReassmBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsReassmBufferCnt.setStatus("mandatory")
_WfFrMlStatsReassmBufferMax_Type = Counter32
_WfFrMlStatsReassmBufferMax_Object = MibTableColumn
wfFrMlStatsReassmBufferMax = _WfFrMlStatsReassmBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 28),
    _WfFrMlStatsReassmBufferMax_Type()
)
wfFrMlStatsReassmBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsReassmBufferMax.setStatus("mandatory")
_WfFrMlStatsNumPktsFragmented_Type = Counter32
_WfFrMlStatsNumPktsFragmented_Object = MibTableColumn
wfFrMlStatsNumPktsFragmented = _WfFrMlStatsNumPktsFragmented_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 29),
    _WfFrMlStatsNumPktsFragmented_Type()
)
wfFrMlStatsNumPktsFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsNumPktsFragmented.setStatus("mandatory")
_WfFrMlStatsPQHiXmits_Type = Counter32
_WfFrMlStatsPQHiXmits_Object = MibTableColumn
wfFrMlStatsPQHiXmits = _WfFrMlStatsPQHiXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 30),
    _WfFrMlStatsPQHiXmits_Type()
)
wfFrMlStatsPQHiXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQHiXmits.setStatus("mandatory")
_WfFrMlStatsPQNormalXmits_Type = Counter32
_WfFrMlStatsPQNormalXmits_Object = MibTableColumn
wfFrMlStatsPQNormalXmits = _WfFrMlStatsPQNormalXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 31),
    _WfFrMlStatsPQNormalXmits_Type()
)
wfFrMlStatsPQNormalXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQNormalXmits.setStatus("mandatory")
_WfFrMlStatsPQLoXmits_Type = Counter32
_WfFrMlStatsPQLoXmits_Object = MibTableColumn
wfFrMlStatsPQLoXmits = _WfFrMlStatsPQLoXmits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 32),
    _WfFrMlStatsPQLoXmits_Type()
)
wfFrMlStatsPQLoXmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQLoXmits.setStatus("mandatory")
_WfFrMlStatsPQHiClippedPkts_Type = Counter32
_WfFrMlStatsPQHiClippedPkts_Object = MibTableColumn
wfFrMlStatsPQHiClippedPkts = _WfFrMlStatsPQHiClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 33),
    _WfFrMlStatsPQHiClippedPkts_Type()
)
wfFrMlStatsPQHiClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQHiClippedPkts.setStatus("mandatory")
_WfFrMlStatsPQNormalClippedPkts_Type = Counter32
_WfFrMlStatsPQNormalClippedPkts_Object = MibTableColumn
wfFrMlStatsPQNormalClippedPkts = _WfFrMlStatsPQNormalClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 34),
    _WfFrMlStatsPQNormalClippedPkts_Type()
)
wfFrMlStatsPQNormalClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQNormalClippedPkts.setStatus("mandatory")
_WfFrMlStatsPQLoClippedPkts_Type = Counter32
_WfFrMlStatsPQLoClippedPkts_Object = MibTableColumn
wfFrMlStatsPQLoClippedPkts = _WfFrMlStatsPQLoClippedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 35),
    _WfFrMlStatsPQLoClippedPkts_Type()
)
wfFrMlStatsPQLoClippedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQLoClippedPkts.setStatus("mandatory")
_WfFrMlStatsPQIntrQHighWaterPkts_Type = Gauge32
_WfFrMlStatsPQIntrQHighWaterPkts_Object = MibTableColumn
wfFrMlStatsPQIntrQHighWaterPkts = _WfFrMlStatsPQIntrQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 36),
    _WfFrMlStatsPQIntrQHighWaterPkts_Type()
)
wfFrMlStatsPQIntrQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQIntrQHighWaterPkts.setStatus("mandatory")
_WfFrMlStatsPQHiQHighWaterPkts_Type = Gauge32
_WfFrMlStatsPQHiQHighWaterPkts_Object = MibTableColumn
wfFrMlStatsPQHiQHighWaterPkts = _WfFrMlStatsPQHiQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 37),
    _WfFrMlStatsPQHiQHighWaterPkts_Type()
)
wfFrMlStatsPQHiQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQHiQHighWaterPkts.setStatus("mandatory")
_WfFrMlStatsPQNormalQHighWaterPkts_Type = Gauge32
_WfFrMlStatsPQNormalQHighWaterPkts_Object = MibTableColumn
wfFrMlStatsPQNormalQHighWaterPkts = _WfFrMlStatsPQNormalQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 38),
    _WfFrMlStatsPQNormalQHighWaterPkts_Type()
)
wfFrMlStatsPQNormalQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQNormalQHighWaterPkts.setStatus("mandatory")
_WfFrMlStatsPQLoQHighWaterPkts_Type = Gauge32
_WfFrMlStatsPQLoQHighWaterPkts_Object = MibTableColumn
wfFrMlStatsPQLoQHighWaterPkts = _WfFrMlStatsPQLoQHighWaterPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 39),
    _WfFrMlStatsPQLoQHighWaterPkts_Type()
)
wfFrMlStatsPQLoQHighWaterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQLoQHighWaterPkts.setStatus("mandatory")
_WfFrMlStatsPQHighWaterPktsClear_Type = Integer32
_WfFrMlStatsPQHighWaterPktsClear_Object = MibTableColumn
wfFrMlStatsPQHighWaterPktsClear = _WfFrMlStatsPQHighWaterPktsClear_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 40),
    _WfFrMlStatsPQHighWaterPktsClear_Type()
)
wfFrMlStatsPQHighWaterPktsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlStatsPQHighWaterPktsClear.setStatus("mandatory")
_WfFrMlStatsPQDroppedPkts_Type = Counter32
_WfFrMlStatsPQDroppedPkts_Object = MibTableColumn
wfFrMlStatsPQDroppedPkts = _WfFrMlStatsPQDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 41),
    _WfFrMlStatsPQDroppedPkts_Type()
)
wfFrMlStatsPQDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQDroppedPkts.setStatus("mandatory")
_WfFrMlStatsPQLargePkts_Type = Counter32
_WfFrMlStatsPQLargePkts_Object = MibTableColumn
wfFrMlStatsPQLargePkts = _WfFrMlStatsPQLargePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 42),
    _WfFrMlStatsPQLargePkts_Type()
)
wfFrMlStatsPQLargePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQLargePkts.setStatus("mandatory")
_WfFrMlStatsPQHiTotalOctets_Type = Counter32
_WfFrMlStatsPQHiTotalOctets_Object = MibTableColumn
wfFrMlStatsPQHiTotalOctets = _WfFrMlStatsPQHiTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 43),
    _WfFrMlStatsPQHiTotalOctets_Type()
)
wfFrMlStatsPQHiTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQHiTotalOctets.setStatus("mandatory")
_WfFrMlStatsPQNormalTotalOctets_Type = Counter32
_WfFrMlStatsPQNormalTotalOctets_Object = MibTableColumn
wfFrMlStatsPQNormalTotalOctets = _WfFrMlStatsPQNormalTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 44),
    _WfFrMlStatsPQNormalTotalOctets_Type()
)
wfFrMlStatsPQNormalTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQNormalTotalOctets.setStatus("mandatory")
_WfFrMlStatsPQLoTotalOctets_Type = Counter32
_WfFrMlStatsPQLoTotalOctets_Object = MibTableColumn
wfFrMlStatsPQLoTotalOctets = _WfFrMlStatsPQLoTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 45),
    _WfFrMlStatsPQLoTotalOctets_Type()
)
wfFrMlStatsPQLoTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQLoTotalOctets.setStatus("mandatory")
_WfFrMlStatsPQPktsNotQueued_Type = Counter32
_WfFrMlStatsPQPktsNotQueued_Object = MibTableColumn
wfFrMlStatsPQPktsNotQueued = _WfFrMlStatsPQPktsNotQueued_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 14, 1, 46),
    _WfFrMlStatsPQPktsNotQueued_Type()
)
wfFrMlStatsPQPktsNotQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlStatsPQPktsNotQueued.setStatus("mandatory")
_WfFrMlVCTable_Object = MibTable
wfFrMlVCTable = _WfFrMlVCTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15)
)
if mibBuilder.loadTexts:
    wfFrMlVCTable.setStatus("mandatory")
_WfFrMlVCEntry_Object = MibTableRow
wfFrMlVCEntry = _WfFrMlVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1)
)
wfFrMlVCEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrMlVCCircuitNumber"),
    (0, "Wellfleet-FR2-MIB", "wfFrMlVCDlci"),
)
if mibBuilder.loadTexts:
    wfFrMlVCEntry.setStatus("mandatory")


class _WfFrMlVCDelete_Type(Integer32):
    """Custom type wfFrMlVCDelete based on Integer32"""
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


_WfFrMlVCDelete_Type.__name__ = "Integer32"
_WfFrMlVCDelete_Object = MibTableColumn
wfFrMlVCDelete = _WfFrMlVCDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 1),
    _WfFrMlVCDelete_Type()
)
wfFrMlVCDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCDelete.setStatus("mandatory")


class _WfFrMlVCCircuitNumber_Type(Integer32):
    """Custom type wfFrMlVCCircuitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfFrMlVCCircuitNumber_Type.__name__ = "Integer32"
_WfFrMlVCCircuitNumber_Object = MibTableColumn
wfFrMlVCCircuitNumber = _WfFrMlVCCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 2),
    _WfFrMlVCCircuitNumber_Type()
)
wfFrMlVCCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCCircuitNumber.setStatus("mandatory")
_WfFrMlVCDlci_Type = Integer32
_WfFrMlVCDlci_Object = MibTableColumn
wfFrMlVCDlci = _WfFrMlVCDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 3),
    _WfFrMlVCDlci_Type()
)
wfFrMlVCDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCDlci.setStatus("mandatory")


class _WfFrMlVCAggState_Type(Integer32):
    """Custom type wfFrMlVCAggState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_WfFrMlVCAggState_Type.__name__ = "Integer32"
_WfFrMlVCAggState_Object = MibTableColumn
wfFrMlVCAggState = _WfFrMlVCAggState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 4),
    _WfFrMlVCAggState_Type()
)
wfFrMlVCAggState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCAggState.setStatus("mandatory")
_WfFrMlVCAggNumberVCs_Type = Integer32
_WfFrMlVCAggNumberVCs_Object = MibTableColumn
wfFrMlVCAggNumberVCs = _WfFrMlVCAggNumberVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 5),
    _WfFrMlVCAggNumberVCs_Type()
)
wfFrMlVCAggNumberVCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCAggNumberVCs.setStatus("mandatory")
_WfFrMlVCAggNumberVCsActive_Type = Integer32
_WfFrMlVCAggNumberVCsActive_Object = MibTableColumn
wfFrMlVCAggNumberVCsActive = _WfFrMlVCAggNumberVCsActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 6),
    _WfFrMlVCAggNumberVCsActive_Type()
)
wfFrMlVCAggNumberVCsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCAggNumberVCsActive.setStatus("mandatory")
_WfFrMlVCStatsLineCnt_Type = Gauge32
_WfFrMlVCStatsLineCnt_Object = MibTableColumn
wfFrMlVCStatsLineCnt = _WfFrMlVCStatsLineCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 7),
    _WfFrMlVCStatsLineCnt_Type()
)
wfFrMlVCStatsLineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsLineCnt.setStatus("mandatory")
_WfFrMlVCStatsBundleSpd_Type = Gauge32
_WfFrMlVCStatsBundleSpd_Object = MibTableColumn
wfFrMlVCStatsBundleSpd = _WfFrMlVCStatsBundleSpd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 8),
    _WfFrMlVCStatsBundleSpd_Type()
)
wfFrMlVCStatsBundleSpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsBundleSpd.setStatus("mandatory")
_WfFrMlVCStatsTxOctets_Type = Counter32
_WfFrMlVCStatsTxOctets_Object = MibTableColumn
wfFrMlVCStatsTxOctets = _WfFrMlVCStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 9),
    _WfFrMlVCStatsTxOctets_Type()
)
wfFrMlVCStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsTxOctets.setStatus("mandatory")
_WfFrMlVCStatsTxPkts_Type = Counter32
_WfFrMlVCStatsTxPkts_Object = MibTableColumn
wfFrMlVCStatsTxPkts = _WfFrMlVCStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 10),
    _WfFrMlVCStatsTxPkts_Type()
)
wfFrMlVCStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsTxPkts.setStatus("mandatory")
_WfFrMlVCStatsAvgTxListLen_Type = Gauge32
_WfFrMlVCStatsAvgTxListLen_Object = MibTableColumn
wfFrMlVCStatsAvgTxListLen = _WfFrMlVCStatsAvgTxListLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 11),
    _WfFrMlVCStatsAvgTxListLen_Type()
)
wfFrMlVCStatsAvgTxListLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsAvgTxListLen.setStatus("mandatory")
_WfFrMlVCStatsRxOctets_Type = Counter32
_WfFrMlVCStatsRxOctets_Object = MibTableColumn
wfFrMlVCStatsRxOctets = _WfFrMlVCStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 12),
    _WfFrMlVCStatsRxOctets_Type()
)
wfFrMlVCStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsRxOctets.setStatus("mandatory")
_WfFrMlVCStatsRxPkts_Type = Counter32
_WfFrMlVCStatsRxPkts_Object = MibTableColumn
wfFrMlVCStatsRxPkts = _WfFrMlVCStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 13),
    _WfFrMlVCStatsRxPkts_Type()
)
wfFrMlVCStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsRxPkts.setStatus("mandatory")
_WfFrMlVCStatsReasmFails_Type = Counter32
_WfFrMlVCStatsReasmFails_Object = MibTableColumn
wfFrMlVCStatsReasmFails = _WfFrMlVCStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 14),
    _WfFrMlVCStatsReasmFails_Type()
)
wfFrMlVCStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsReasmFails.setStatus("mandatory")
_WfFrMlVCStatsSeqNumberLost_Type = Counter32
_WfFrMlVCStatsSeqNumberLost_Object = MibTableColumn
wfFrMlVCStatsSeqNumberLost = _WfFrMlVCStatsSeqNumberLost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 15),
    _WfFrMlVCStatsSeqNumberLost_Type()
)
wfFrMlVCStatsSeqNumberLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsSeqNumberLost.setStatus("mandatory")
_WfFrMlVCStatsSeqNumberArrivedLate_Type = Counter32
_WfFrMlVCStatsSeqNumberArrivedLate_Object = MibTableColumn
wfFrMlVCStatsSeqNumberArrivedLate = _WfFrMlVCStatsSeqNumberArrivedLate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 16),
    _WfFrMlVCStatsSeqNumberArrivedLate_Type()
)
wfFrMlVCStatsSeqNumberArrivedLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsSeqNumberArrivedLate.setStatus("mandatory")
_WfFrMlVCStatsReSeqBufferCnt_Type = Gauge32
_WfFrMlVCStatsReSeqBufferCnt_Object = MibTableColumn
wfFrMlVCStatsReSeqBufferCnt = _WfFrMlVCStatsReSeqBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 17),
    _WfFrMlVCStatsReSeqBufferCnt_Type()
)
wfFrMlVCStatsReSeqBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsReSeqBufferCnt.setStatus("mandatory")
_WfFrMlVCStatsReSeqBufferMax_Type = Counter32
_WfFrMlVCStatsReSeqBufferMax_Object = MibTableColumn
wfFrMlVCStatsReSeqBufferMax = _WfFrMlVCStatsReSeqBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 18),
    _WfFrMlVCStatsReSeqBufferMax_Type()
)
wfFrMlVCStatsReSeqBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsReSeqBufferMax.setStatus("mandatory")
_WfFrMlVCStatsExceededBufferMax_Type = Counter32
_WfFrMlVCStatsExceededBufferMax_Object = MibTableColumn
wfFrMlVCStatsExceededBufferMax = _WfFrMlVCStatsExceededBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 19),
    _WfFrMlVCStatsExceededBufferMax_Type()
)
wfFrMlVCStatsExceededBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsExceededBufferMax.setStatus("mandatory")
_WfFrMlVCStatsLinkIdleEvents_Type = Counter32
_WfFrMlVCStatsLinkIdleEvents_Object = MibTableColumn
wfFrMlVCStatsLinkIdleEvents = _WfFrMlVCStatsLinkIdleEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 20),
    _WfFrMlVCStatsLinkIdleEvents_Type()
)
wfFrMlVCStatsLinkIdleEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsLinkIdleEvents.setStatus("mandatory")


class _WfFrMlVCStatsCalcPercent_Type(Integer32):
    """Custom type wfFrMlVCStatsCalcPercent based on Integer32"""
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


_WfFrMlVCStatsCalcPercent_Type.__name__ = "Integer32"
_WfFrMlVCStatsCalcPercent_Object = MibTableColumn
wfFrMlVCStatsCalcPercent = _WfFrMlVCStatsCalcPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 21),
    _WfFrMlVCStatsCalcPercent_Type()
)
wfFrMlVCStatsCalcPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCStatsCalcPercent.setStatus("mandatory")
_WfFrMlVCStatsDebug_Type = Integer32
_WfFrMlVCStatsDebug_Object = MibTableColumn
wfFrMlVCStatsDebug = _WfFrMlVCStatsDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 22),
    _WfFrMlVCStatsDebug_Type()
)
wfFrMlVCStatsDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfFrMlVCStatsDebug.setStatus("mandatory")
_WfFrMlVCStatsReassmBufferCnt_Type = Gauge32
_WfFrMlVCStatsReassmBufferCnt_Object = MibTableColumn
wfFrMlVCStatsReassmBufferCnt = _WfFrMlVCStatsReassmBufferCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 23),
    _WfFrMlVCStatsReassmBufferCnt_Type()
)
wfFrMlVCStatsReassmBufferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsReassmBufferCnt.setStatus("mandatory")
_WfFrMlVCStatsReassmBufferMax_Type = Counter32
_WfFrMlVCStatsReassmBufferMax_Object = MibTableColumn
wfFrMlVCStatsReassmBufferMax = _WfFrMlVCStatsReassmBufferMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 24),
    _WfFrMlVCStatsReassmBufferMax_Type()
)
wfFrMlVCStatsReassmBufferMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsReassmBufferMax.setStatus("mandatory")
_WfFrMlVCStatsNumPktsFragmented_Type = Counter32
_WfFrMlVCStatsNumPktsFragmented_Object = MibTableColumn
wfFrMlVCStatsNumPktsFragmented = _WfFrMlVCStatsNumPktsFragmented_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 15, 1, 25),
    _WfFrMlVCStatsNumPktsFragmented_Type()
)
wfFrMlVCStatsNumPktsFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMlVCStatsNumPktsFragmented.setStatus("mandatory")
_WfFrMapDlcmiTable_Object = MibTable
wfFrMapDlcmiTable = _WfFrMapDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16)
)
if mibBuilder.loadTexts:
    wfFrMapDlcmiTable.setStatus("mandatory")
_WfFrMapDlcmiEntry_Object = MibTableRow
wfFrMapDlcmiEntry = _WfFrMapDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1)
)
wfFrMapDlcmiEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrMapDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    wfFrMapDlcmiEntry.setStatus("mandatory")


class _WfFrMapDlcmiIfIndex_Type(Integer32):
    """Custom type wfFrMapDlcmiIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrMapDlcmiIfIndex_Type.__name__ = "Integer32"
_WfFrMapDlcmiIfIndex_Object = MibTableColumn
wfFrMapDlcmiIfIndex = _WfFrMapDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 1),
    _WfFrMapDlcmiIfIndex_Type()
)
wfFrMapDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiIfIndex.setStatus("mandatory")


class _WfFrMapDlcmiState_Type(Integer32):
    """Custom type wfFrMapDlcmiState based on Integer32"""
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


_WfFrMapDlcmiState_Type.__name__ = "Integer32"
_WfFrMapDlcmiState_Object = MibTableColumn
wfFrMapDlcmiState = _WfFrMapDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 2),
    _WfFrMapDlcmiState_Type()
)
wfFrMapDlcmiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiState.setStatus("mandatory")


class _WfFrMapDlcmiAddress_Type(Integer32):
    """Custom type wfFrMapDlcmiAddress based on Integer32"""
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


_WfFrMapDlcmiAddress_Type.__name__ = "Integer32"
_WfFrMapDlcmiAddress_Object = MibTableColumn
wfFrMapDlcmiAddress = _WfFrMapDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 3),
    _WfFrMapDlcmiAddress_Type()
)
wfFrMapDlcmiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiAddress.setStatus("mandatory")


class _WfFrMapDlcmiAddressLen_Type(Integer32):
    """Custom type wfFrMapDlcmiAddressLen based on Integer32"""
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


_WfFrMapDlcmiAddressLen_Type.__name__ = "Integer32"
_WfFrMapDlcmiAddressLen_Object = MibTableColumn
wfFrMapDlcmiAddressLen = _WfFrMapDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 4),
    _WfFrMapDlcmiAddressLen_Type()
)
wfFrMapDlcmiAddressLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiAddressLen.setStatus("mandatory")


class _WfFrMapDlcmiPollingInterval_Type(Integer32):
    """Custom type wfFrMapDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfFrMapDlcmiPollingInterval_Type.__name__ = "Integer32"
_WfFrMapDlcmiPollingInterval_Object = MibTableColumn
wfFrMapDlcmiPollingInterval = _WfFrMapDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 5),
    _WfFrMapDlcmiPollingInterval_Type()
)
wfFrMapDlcmiPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiPollingInterval.setStatus("mandatory")


class _WfFrMapDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type wfFrMapDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfFrMapDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_WfFrMapDlcmiFullEnquiryInterval_Object = MibTableColumn
wfFrMapDlcmiFullEnquiryInterval = _WfFrMapDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 6),
    _WfFrMapDlcmiFullEnquiryInterval_Type()
)
wfFrMapDlcmiFullEnquiryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiFullEnquiryInterval.setStatus("mandatory")


class _WfFrMapDlcmiErrorThreshold_Type(Integer32):
    """Custom type wfFrMapDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfFrMapDlcmiErrorThreshold_Type.__name__ = "Integer32"
_WfFrMapDlcmiErrorThreshold_Object = MibTableColumn
wfFrMapDlcmiErrorThreshold = _WfFrMapDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 7),
    _WfFrMapDlcmiErrorThreshold_Type()
)
wfFrMapDlcmiErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiErrorThreshold.setStatus("mandatory")


class _WfFrMapDlcmiMonitoredEvents_Type(Integer32):
    """Custom type wfFrMapDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfFrMapDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_WfFrMapDlcmiMonitoredEvents_Object = MibTableColumn
wfFrMapDlcmiMonitoredEvents = _WfFrMapDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 8),
    _WfFrMapDlcmiMonitoredEvents_Type()
)
wfFrMapDlcmiMonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiMonitoredEvents.setStatus("mandatory")
_WfFrMapDlcmiMaxSupportedVCs_Type = Integer32
_WfFrMapDlcmiMaxSupportedVCs_Object = MibTableColumn
wfFrMapDlcmiMaxSupportedVCs = _WfFrMapDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 9),
    _WfFrMapDlcmiMaxSupportedVCs_Type()
)
wfFrMapDlcmiMaxSupportedVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiMaxSupportedVCs.setStatus("mandatory")


class _WfFrMapDlcmiMulticast_Type(Integer32):
    """Custom type wfFrMapDlcmiMulticast based on Integer32"""
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


_WfFrMapDlcmiMulticast_Type.__name__ = "Integer32"
_WfFrMapDlcmiMulticast_Object = MibTableColumn
wfFrMapDlcmiMulticast = _WfFrMapDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 10),
    _WfFrMapDlcmiMulticast_Type()
)
wfFrMapDlcmiMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiMulticast.setStatus("mandatory")


class _WfFrMapDlcmiStatus_Type(Integer32):
    """Custom type wfFrMapDlcmiStatus based on Integer32"""
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


_WfFrMapDlcmiStatus_Type.__name__ = "Integer32"
_WfFrMapDlcmiStatus_Object = MibTableColumn
wfFrMapDlcmiStatus = _WfFrMapDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 11),
    _WfFrMapDlcmiStatus_Type()
)
wfFrMapDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiStatus.setStatus("mandatory")
_WfFrMapDlcmiRowStatus_Type = Integer32
_WfFrMapDlcmiRowStatus_Object = MibTableColumn
wfFrMapDlcmiRowStatus = _WfFrMapDlcmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 12),
    _WfFrMapDlcmiRowStatus_Type()
)
wfFrMapDlcmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiRowStatus.setStatus("mandatory")
_WfFrMapDlcmiLineNumber_Type = Integer32
_WfFrMapDlcmiLineNumber_Object = MibTableColumn
wfFrMapDlcmiLineNumber = _WfFrMapDlcmiLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 13),
    _WfFrMapDlcmiLineNumber_Type()
)
wfFrMapDlcmiLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiLineNumber.setStatus("mandatory")
_WfFrMapDlcmiLLIndex_Type = Integer32
_WfFrMapDlcmiLLIndex_Object = MibTableColumn
wfFrMapDlcmiLLIndex = _WfFrMapDlcmiLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 16, 1, 14),
    _WfFrMapDlcmiLLIndex_Type()
)
wfFrMapDlcmiLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapDlcmiLLIndex.setStatus("mandatory")
_WfFrMapCircuitTable_Object = MibTable
wfFrMapCircuitTable = _WfFrMapCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17)
)
if mibBuilder.loadTexts:
    wfFrMapCircuitTable.setStatus("mandatory")
_WfFrMapCircuitEntry_Object = MibTableRow
wfFrMapCircuitEntry = _WfFrMapCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1)
)
wfFrMapCircuitEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrMapCircuitIfIndex"),
    (0, "Wellfleet-FR2-MIB", "wfFrMapCircuitDlci"),
)
if mibBuilder.loadTexts:
    wfFrMapCircuitEntry.setStatus("mandatory")


class _WfFrMapCircuitIfIndex_Type(Integer32):
    """Custom type wfFrMapCircuitIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrMapCircuitIfIndex_Type.__name__ = "Integer32"
_WfFrMapCircuitIfIndex_Object = MibTableColumn
wfFrMapCircuitIfIndex = _WfFrMapCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 1),
    _WfFrMapCircuitIfIndex_Type()
)
wfFrMapCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitIfIndex.setStatus("mandatory")
_WfFrMapCircuitDlci_Type = Integer32
_WfFrMapCircuitDlci_Object = MibTableColumn
wfFrMapCircuitDlci = _WfFrMapCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 2),
    _WfFrMapCircuitDlci_Type()
)
wfFrMapCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitDlci.setStatus("mandatory")


class _WfFrMapCircuitState_Type(Integer32):
    """Custom type wfFrMapCircuitState based on Integer32"""
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


_WfFrMapCircuitState_Type.__name__ = "Integer32"
_WfFrMapCircuitState_Object = MibTableColumn
wfFrMapCircuitState = _WfFrMapCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 3),
    _WfFrMapCircuitState_Type()
)
wfFrMapCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitState.setStatus("mandatory")
_WfFrMapCircuitReceivedFECNs_Type = Counter32
_WfFrMapCircuitReceivedFECNs_Object = MibTableColumn
wfFrMapCircuitReceivedFECNs = _WfFrMapCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 4),
    _WfFrMapCircuitReceivedFECNs_Type()
)
wfFrMapCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitReceivedFECNs.setStatus("mandatory")
_WfFrMapCircuitReceivedBECNs_Type = Counter32
_WfFrMapCircuitReceivedBECNs_Object = MibTableColumn
wfFrMapCircuitReceivedBECNs = _WfFrMapCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 5),
    _WfFrMapCircuitReceivedBECNs_Type()
)
wfFrMapCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitReceivedBECNs.setStatus("mandatory")
_WfFrMapCircuitSentFrames_Type = Counter32
_WfFrMapCircuitSentFrames_Object = MibTableColumn
wfFrMapCircuitSentFrames = _WfFrMapCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 6),
    _WfFrMapCircuitSentFrames_Type()
)
wfFrMapCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitSentFrames.setStatus("mandatory")
_WfFrMapCircuitSentOctets_Type = Counter32
_WfFrMapCircuitSentOctets_Object = MibTableColumn
wfFrMapCircuitSentOctets = _WfFrMapCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 7),
    _WfFrMapCircuitSentOctets_Type()
)
wfFrMapCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitSentOctets.setStatus("mandatory")
_WfFrMapCircuitReceivedFrames_Type = Counter32
_WfFrMapCircuitReceivedFrames_Object = MibTableColumn
wfFrMapCircuitReceivedFrames = _WfFrMapCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 8),
    _WfFrMapCircuitReceivedFrames_Type()
)
wfFrMapCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitReceivedFrames.setStatus("mandatory")
_WfFrMapCircuitReceivedOctets_Type = Counter32
_WfFrMapCircuitReceivedOctets_Object = MibTableColumn
wfFrMapCircuitReceivedOctets = _WfFrMapCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 9),
    _WfFrMapCircuitReceivedOctets_Type()
)
wfFrMapCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitReceivedOctets.setStatus("mandatory")
_WfFrMapCircuitCreationTime_Type = TimeTicks
_WfFrMapCircuitCreationTime_Object = MibTableColumn
wfFrMapCircuitCreationTime = _WfFrMapCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 10),
    _WfFrMapCircuitCreationTime_Type()
)
wfFrMapCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitCreationTime.setStatus("mandatory")
_WfFrMapCircuitLastTimeChange_Type = TimeTicks
_WfFrMapCircuitLastTimeChange_Object = MibTableColumn
wfFrMapCircuitLastTimeChange = _WfFrMapCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 11),
    _WfFrMapCircuitLastTimeChange_Type()
)
wfFrMapCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitLastTimeChange.setStatus("mandatory")


class _WfFrMapCircuitCommittedBurst_Type(Integer32):
    """Custom type wfFrMapCircuitCommittedBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrMapCircuitCommittedBurst_Type.__name__ = "Integer32"
_WfFrMapCircuitCommittedBurst_Object = MibTableColumn
wfFrMapCircuitCommittedBurst = _WfFrMapCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 12),
    _WfFrMapCircuitCommittedBurst_Type()
)
wfFrMapCircuitCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitCommittedBurst.setStatus("mandatory")


class _WfFrMapCircuitExcessBurst_Type(Integer32):
    """Custom type wfFrMapCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrMapCircuitExcessBurst_Type.__name__ = "Integer32"
_WfFrMapCircuitExcessBurst_Object = MibTableColumn
wfFrMapCircuitExcessBurst = _WfFrMapCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 13),
    _WfFrMapCircuitExcessBurst_Type()
)
wfFrMapCircuitExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitExcessBurst.setStatus("mandatory")


class _WfFrMapCircuitThroughput_Type(Integer32):
    """Custom type wfFrMapCircuitThroughput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfFrMapCircuitThroughput_Type.__name__ = "Integer32"
_WfFrMapCircuitThroughput_Object = MibTableColumn
wfFrMapCircuitThroughput = _WfFrMapCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 14),
    _WfFrMapCircuitThroughput_Type()
)
wfFrMapCircuitThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitThroughput.setStatus("mandatory")


class _WfFrMapCircuitMulticast_Type(Integer32):
    """Custom type wfFrMapCircuitMulticast based on Integer32"""
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


_WfFrMapCircuitMulticast_Type.__name__ = "Integer32"
_WfFrMapCircuitMulticast_Object = MibTableColumn
wfFrMapCircuitMulticast = _WfFrMapCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 15),
    _WfFrMapCircuitMulticast_Type()
)
wfFrMapCircuitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitMulticast.setStatus("mandatory")


class _WfFrMapCircuitType_Type(Integer32):
    """Custom type wfFrMapCircuitType based on Integer32"""
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


_WfFrMapCircuitType_Type.__name__ = "Integer32"
_WfFrMapCircuitType_Object = MibTableColumn
wfFrMapCircuitType = _WfFrMapCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 16),
    _WfFrMapCircuitType_Type()
)
wfFrMapCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitType.setStatus("mandatory")
_WfFrMapCircuitDiscards_Type = Counter32
_WfFrMapCircuitDiscards_Object = MibTableColumn
wfFrMapCircuitDiscards = _WfFrMapCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 17),
    _WfFrMapCircuitDiscards_Type()
)
wfFrMapCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitDiscards.setStatus("mandatory")
_WfFrMapCircuitReceivedDEs_Type = Counter32
_WfFrMapCircuitReceivedDEs_Object = MibTableColumn
wfFrMapCircuitReceivedDEs = _WfFrMapCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 18),
    _WfFrMapCircuitReceivedDEs_Type()
)
wfFrMapCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitReceivedDEs.setStatus("mandatory")
_WfFrMapCircuitSentDEs_Type = Counter32
_WfFrMapCircuitSentDEs_Object = MibTableColumn
wfFrMapCircuitSentDEs = _WfFrMapCircuitSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 19),
    _WfFrMapCircuitSentDEs_Type()
)
wfFrMapCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitSentDEs.setStatus("mandatory")


class _WfFrMapCircuitLogicalIfIndex_Type(Integer32):
    """Custom type wfFrMapCircuitLogicalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrMapCircuitLogicalIfIndex_Type.__name__ = "Integer32"
_WfFrMapCircuitLogicalIfIndex_Object = MibTableColumn
wfFrMapCircuitLogicalIfIndex = _WfFrMapCircuitLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 20),
    _WfFrMapCircuitLogicalIfIndex_Type()
)
wfFrMapCircuitLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitLogicalIfIndex.setStatus("mandatory")
_WfFrMapCircuitRowStatus_Type = Integer32
_WfFrMapCircuitRowStatus_Object = MibTableColumn
wfFrMapCircuitRowStatus = _WfFrMapCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 21),
    _WfFrMapCircuitRowStatus_Type()
)
wfFrMapCircuitRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitRowStatus.setStatus("mandatory")
_WfFrMapCircuitLineNumber_Type = Integer32
_WfFrMapCircuitLineNumber_Object = MibTableColumn
wfFrMapCircuitLineNumber = _WfFrMapCircuitLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 22),
    _WfFrMapCircuitLineNumber_Type()
)
wfFrMapCircuitLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitLineNumber.setStatus("mandatory")
_WfFrMapCircuitLLIndex_Type = Integer32
_WfFrMapCircuitLLIndex_Object = MibTableColumn
wfFrMapCircuitLLIndex = _WfFrMapCircuitLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 17, 1, 23),
    _WfFrMapCircuitLLIndex_Type()
)
wfFrMapCircuitLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapCircuitLLIndex.setStatus("mandatory")
_WfFrMapErrTable_Object = MibTable
wfFrMapErrTable = _WfFrMapErrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18)
)
if mibBuilder.loadTexts:
    wfFrMapErrTable.setStatus("mandatory")
_WfFrMapErrEntry_Object = MibTableRow
wfFrMapErrEntry = _WfFrMapErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1)
)
wfFrMapErrEntry.setIndexNames(
    (0, "Wellfleet-FR2-MIB", "wfFrMapErrIfIndex"),
)
if mibBuilder.loadTexts:
    wfFrMapErrEntry.setStatus("mandatory")


class _WfFrMapErrIfIndex_Type(Integer32):
    """Custom type wfFrMapErrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfFrMapErrIfIndex_Type.__name__ = "Integer32"
_WfFrMapErrIfIndex_Object = MibTableColumn
wfFrMapErrIfIndex = _WfFrMapErrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 1),
    _WfFrMapErrIfIndex_Type()
)
wfFrMapErrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrIfIndex.setStatus("mandatory")


class _WfFrMapErrType_Type(Integer32):
    """Custom type wfFrMapErrType based on Integer32"""
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
        *(("dlcmiProtoErr", 6),
          ("dlcmiSequenceErr", 8),
          ("dlcmiUnknownIE", 7),
          ("dlcmiUnknownRpt", 9),
          ("illegalAddress", 4),
          ("noErrorSinceReset", 10),
          ("receiveLong", 3),
          ("receiveShort", 2),
          ("unknownAddress", 5),
          ("unknownError", 1))
    )


_WfFrMapErrType_Type.__name__ = "Integer32"
_WfFrMapErrType_Object = MibTableColumn
wfFrMapErrType = _WfFrMapErrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 2),
    _WfFrMapErrType_Type()
)
wfFrMapErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrType.setStatus("mandatory")


class _WfFrMapErrData_Type(OctetString):
    """Custom type wfFrMapErrData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1600),
    )


_WfFrMapErrData_Type.__name__ = "OctetString"
_WfFrMapErrData_Object = MibTableColumn
wfFrMapErrData = _WfFrMapErrData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 3),
    _WfFrMapErrData_Type()
)
wfFrMapErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrData.setStatus("mandatory")
_WfFrMapErrTime_Type = TimeTicks
_WfFrMapErrTime_Object = MibTableColumn
wfFrMapErrTime = _WfFrMapErrTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 4),
    _WfFrMapErrTime_Type()
)
wfFrMapErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrTime.setStatus("mandatory")
_WfFrMapErrFaults_Type = Counter32
_WfFrMapErrFaults_Object = MibTableColumn
wfFrMapErrFaults = _WfFrMapErrFaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 5),
    _WfFrMapErrFaults_Type()
)
wfFrMapErrFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrFaults.setStatus("mandatory")
_WfFrMapErrFaultTime_Type = TimeTicks
_WfFrMapErrFaultTime_Object = MibTableColumn
wfFrMapErrFaultTime = _WfFrMapErrFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 6),
    _WfFrMapErrFaultTime_Type()
)
wfFrMapErrFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrFaultTime.setStatus("mandatory")
_WfFrMapErrLineNumber_Type = Integer32
_WfFrMapErrLineNumber_Object = MibTableColumn
wfFrMapErrLineNumber = _WfFrMapErrLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 7),
    _WfFrMapErrLineNumber_Type()
)
wfFrMapErrLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrLineNumber.setStatus("mandatory")
_WfFrMapErrLLIndex_Type = Integer32
_WfFrMapErrLLIndex_Object = MibTableColumn
wfFrMapErrLLIndex = _WfFrMapErrLLIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 9, 18, 1, 8),
    _WfFrMapErrLLIndex_Type()
)
wfFrMapErrLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFrMapErrLLIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-FR2-MIB",
    **{"wfFrIfDlcmiTable": wfFrIfDlcmiTable,
       "wfFrIfDlcmiEntry": wfFrIfDlcmiEntry,
       "wfFrDlcmiDelete": wfFrDlcmiDelete,
       "wfFrDlcmiDisable": wfFrDlcmiDisable,
       "wfFrDlcmiLineNumber": wfFrDlcmiLineNumber,
       "wfFrDlcmiLLIndex": wfFrDlcmiLLIndex,
       "wfFrDlcmiCircuit": wfFrDlcmiCircuit,
       "wfFrDlcmiManagementType": wfFrDlcmiManagementType,
       "wfFrDlcmiStatus": wfFrDlcmiStatus,
       "wfFrDlcmiAddress": wfFrDlcmiAddress,
       "wfFrDlcmiAddressLen": wfFrDlcmiAddressLen,
       "wfFrDlcmiPollingInterval": wfFrDlcmiPollingInterval,
       "wfFrDlcmiFullEnquiryInterval": wfFrDlcmiFullEnquiryInterval,
       "wfFrDlcmiErrorThreshold": wfFrDlcmiErrorThreshold,
       "wfFrDlcmiMonitoredEvents": wfFrDlcmiMonitoredEvents,
       "wfFrDlcmiMaxSupportedVCs": wfFrDlcmiMaxSupportedVCs,
       "wfFrDlcmiVCsConfigured": wfFrDlcmiVCsConfigured,
       "wfFrDlcmiMulticast": wfFrDlcmiMulticast,
       "wfFrDlcmiSeqCount": wfFrDlcmiSeqCount,
       "wfFrDlcmiLastReceived": wfFrDlcmiLastReceived,
       "wfFrDlcmiPassiveSeqCount": wfFrDlcmiPassiveSeqCount,
       "wfFrDlcmiPassiveReceived": wfFrDlcmiPassiveReceived,
       "wfFrDlcmiPolls": wfFrDlcmiPolls,
       "wfFrDlcmiCongestionDisable": wfFrDlcmiCongestionDisable,
       "wfFrDlcmiCongestionTmr": wfFrDlcmiCongestionTmr,
       "wfFrDlcmiCongestionCtr": wfFrDlcmiCongestionCtr,
       "wfFrErrType": wfFrErrType,
       "wfFrErrData": wfFrErrData,
       "wfFrErrTime": wfFrErrTime,
       "wfFrErrDiscards": wfFrErrDiscards,
       "wfFrErrDrops": wfFrErrDrops,
       "wfFrErrFaults": wfFrErrFaults,
       "wfFrErrFaultTime": wfFrErrFaultTime,
       "wfFrDlcmiDialFailureDisable": wfFrDlcmiDialFailureDisable,
       "wfFrDlcmiInterfaceType": wfFrDlcmiInterfaceType,
       "wfFrDlcmiBackupFilterCct": wfFrDlcmiBackupFilterCct,
       "wfFrDlcmiDebugLevel": wfFrDlcmiDebugLevel,
       "wfFrDlcmiTraceLevel": wfFrDlcmiTraceLevel,
       "wfFrDlcmiCongestionMethod": wfFrDlcmiCongestionMethod,
       "wfFrDlcmiShapingTmr": wfFrDlcmiShapingTmr,
       "wfFrDlcmiShapingHiQueueLimit": wfFrDlcmiShapingHiQueueLimit,
       "wfFrDlcmiShapingNormalQueueLimit": wfFrDlcmiShapingNormalQueueLimit,
       "wfFrDlcmiShapingLoQueueLimit": wfFrDlcmiShapingLoQueueLimit,
       "wfFrDlcmiXoffDisable": wfFrDlcmiXoffDisable,
       "wfFrDlcmiMissingPolls": wfFrDlcmiMissingPolls,
       "wfFrDlcmiName": wfFrDlcmiName,
       "wfFrDlcmiEnableSinglePVCUpdate": wfFrDlcmiEnableSinglePVCUpdate,
       "wfFrDlcmiAnnexSwEnq": wfFrDlcmiAnnexSwEnq,
       "wfFrDlcmiAnnexSwEnqTmr": wfFrDlcmiAnnexSwEnqTmr,
       "wfFrDlcmiExtraStatusInfoEnable": wfFrDlcmiExtraStatusInfoEnable,
       "wfFrVCircuitTable": wfFrVCircuitTable,
       "wfFrVCircuitEntry": wfFrVCircuitEntry,
       "wfFrCircuitDelete": wfFrCircuitDelete,
       "wfFrCircuitLineNumber": wfFrCircuitLineNumber,
       "wfFrCircuitLLIndex": wfFrCircuitLLIndex,
       "wfFrCircuitNumber": wfFrCircuitNumber,
       "wfFrCircuitDlci": wfFrCircuitDlci,
       "wfFrCircuitState": wfFrCircuitState,
       "wfFrCircuitStateSet": wfFrCircuitStateSet,
       "wfFrCircuitReceivedFECNs": wfFrCircuitReceivedFECNs,
       "wfFrCircuitReceivedBECNs": wfFrCircuitReceivedBECNs,
       "wfFrCircuitSentFrames": wfFrCircuitSentFrames,
       "wfFrCircuitSentOctets": wfFrCircuitSentOctets,
       "wfFrCircuitReceivedFrames": wfFrCircuitReceivedFrames,
       "wfFrCircuitReceivedOctets": wfFrCircuitReceivedOctets,
       "wfFrCircuitCreationTime": wfFrCircuitCreationTime,
       "wfFrCircuitLastTimeChange": wfFrCircuitLastTimeChange,
       "wfFrCircuitCommittedBurst": wfFrCircuitCommittedBurst,
       "wfFrCircuitExcessBurst": wfFrCircuitExcessBurst,
       "wfFrCircuitThroughput": wfFrCircuitThroughput,
       "wfFrCircuitMulticast": wfFrCircuitMulticast,
       "wfFrCircuitType": wfFrCircuitType,
       "wfFrCircuitDiscards": wfFrCircuitDiscards,
       "wfFrCircuitDrops": wfFrCircuitDrops,
       "wfFrCircuitSubCct": wfFrCircuitSubCct,
       "wfFrCircuitMode": wfFrCircuitMode,
       "wfFrCircuitCongestionDisable": wfFrCircuitCongestionDisable,
       "wfFrCircuitCongestionState": wfFrCircuitCongestionState,
       "wfFrCircuitCongestionTmr": wfFrCircuitCongestionTmr,
       "wfFrCircuitCongestionCtr": wfFrCircuitCongestionCtr,
       "wfFrCircuitWcpEnable": wfFrCircuitWcpEnable,
       "wfFrCircuitPrimaryHoldTmr": wfFrCircuitPrimaryHoldTmr,
       "wfFrCircuitInactivityTimer": wfFrCircuitInactivityTimer,
       "wfFrCircuitInactivityMode": wfFrCircuitInactivityMode,
       "wfFrCircuitCongestionMethod": wfFrCircuitCongestionMethod,
       "wfFrCircuitShapedHiXmits": wfFrCircuitShapedHiXmits,
       "wfFrCircuitShapedNormalXmits": wfFrCircuitShapedNormalXmits,
       "wfFrCircuitShapedLoXmits": wfFrCircuitShapedLoXmits,
       "wfFrCircuitShapedHiClippedPkts": wfFrCircuitShapedHiClippedPkts,
       "wfFrCircuitShapedNormalClippedPkts": wfFrCircuitShapedNormalClippedPkts,
       "wfFrCircuitShapedLoClippedPkts": wfFrCircuitShapedLoClippedPkts,
       "wfFrCircuitShapedHiQHighWaterPkts": wfFrCircuitShapedHiQHighWaterPkts,
       "wfFrCircuitShapedNormalQHighWaterPkts": wfFrCircuitShapedNormalQHighWaterPkts,
       "wfFrCircuitShapedLoQHighWaterPkts": wfFrCircuitShapedLoQHighWaterPkts,
       "wfFrCircuitShapedDroppedPkts": wfFrCircuitShapedDroppedPkts,
       "wfFrCircuitShapedLargePkts": wfFrCircuitShapedLargePkts,
       "wfFrCircuitShapedHiTotalOctets": wfFrCircuitShapedHiTotalOctets,
       "wfFrCircuitShapedNormalTotalOctets": wfFrCircuitShapedNormalTotalOctets,
       "wfFrCircuitShapedLoTotalOctets": wfFrCircuitShapedLoTotalOctets,
       "wfFrCircuitShapedPktsNotQueued": wfFrCircuitShapedPktsNotQueued,
       "wfFrCircuitShapedHighWaterPktsClear": wfFrCircuitShapedHighWaterPktsClear,
       "wfFrCircuitShapedHiQueueLimit": wfFrCircuitShapedHiQueueLimit,
       "wfFrCircuitShapedNormalQueueLimit": wfFrCircuitShapedNormalQueueLimit,
       "wfFrCircuitShapedLoQueueLimit": wfFrCircuitShapedLoQueueLimit,
       "wfFrCircuitStartupDelay": wfFrCircuitStartupDelay,
       "wfFrCircuitCurHiQueueLimit": wfFrCircuitCurHiQueueLimit,
       "wfFrCircuitCurNormalQueueLimit": wfFrCircuitCurNormalQueueLimit,
       "wfFrCircuitCurLoQueueLimit": wfFrCircuitCurLoQueueLimit,
       "wfFrCircuitShapingState": wfFrCircuitShapingState,
       "wfFrCircuitBwThreshold": wfFrCircuitBwThreshold,
       "wfFrCircuitReceivedDEs": wfFrCircuitReceivedDEs,
       "wfFrCircuitSentDEs": wfFrCircuitSentDEs,
       "wfFrCctErrorTable": wfFrCctErrorTable,
       "wfFrCctErrorEntry": wfFrCctErrorEntry,
       "wfFrCctErrorCct": wfFrCctErrorCct,
       "wfFrCctErrorDrops": wfFrCctErrorDrops,
       "wfFrCctErrorDiscards": wfFrCctErrorDiscards,
       "wfFrServiceRecordTable": wfFrServiceRecordTable,
       "wfFrServiceRecordEntry": wfFrServiceRecordEntry,
       "wfFrServiceRecordDelete": wfFrServiceRecordDelete,
       "wfFrServiceRecordLineNumber": wfFrServiceRecordLineNumber,
       "wfFrServiceRecordLLIndex": wfFrServiceRecordLLIndex,
       "wfFrServiceRecordCircuitNumber": wfFrServiceRecordCircuitNumber,
       "wfFrServiceRecordDefaultFlag": wfFrServiceRecordDefaultFlag,
       "wfFrServiceRecordNumberVCs": wfFrServiceRecordNumberVCs,
       "wfFrServiceRecordName": wfFrServiceRecordName,
       "wfFrServiceRecordState": wfFrServiceRecordState,
       "wfFrServiceRecordPreMultiCircuit": wfFrServiceRecordPreMultiCircuit,
       "wfFrServiceRecordBackupFilterCct": wfFrServiceRecordBackupFilterCct,
       "wfFrServiceRecordBackupLineNumber": wfFrServiceRecordBackupLineNumber,
       "wfFrServiceRecordBackupLLIndex": wfFrServiceRecordBackupLLIndex,
       "wfFrServiceRecordBackupMainCct": wfFrServiceRecordBackupMainCct,
       "wfFrServiceRecordPrimaryLineNumber": wfFrServiceRecordPrimaryLineNumber,
       "wfFrServiceRecordPrimaryLLIndex": wfFrServiceRecordPrimaryLLIndex,
       "wfFrServiceRecordPrimaryMainCct": wfFrServiceRecordPrimaryMainCct,
       "wfFrServiceRecordSVCDisable": wfFrServiceRecordSVCDisable,
       "wfFrServiceRecordSVCLocNum": wfFrServiceRecordSVCLocNum,
       "wfFrServiceRecordSVCLocSubAdr": wfFrServiceRecordSVCLocSubAdr,
       "wfFrServiceRecordSVCLocPlan": wfFrServiceRecordSVCLocPlan,
       "wfFrServiceRecordSVCLocTypeNum": wfFrServiceRecordSVCLocTypeNum,
       "wfFrServiceRecordSVCCallBlock": wfFrServiceRecordSVCCallBlock,
       "wfFrServiceRecordSVCInScrnDisable": wfFrServiceRecordSVCInScrnDisable,
       "wfFrServiceRecordSVCInScrnUsage": wfFrServiceRecordSVCInScrnUsage,
       "wfFrServiceRecordSVCInactTimer": wfFrServiceRecordSVCInactTimer,
       "wfFrServiceRecordSVCInactMode": wfFrServiceRecordSVCInactMode,
       "wfFrServiceRecordNumberStaticVCs": wfFrServiceRecordNumberStaticVCs,
       "wfFrServiceRecordNumberDynamicVCs": wfFrServiceRecordNumberDynamicVCs,
       "wfFrServiceRecordNumberSVCs": wfFrServiceRecordNumberSVCs,
       "wfFrServiceRecordNumberActiveVCs": wfFrServiceRecordNumberActiveVCs,
       "wfFrServiceRecordifLastChange": wfFrServiceRecordifLastChange,
       "wfFrServiceRecordifInOctets": wfFrServiceRecordifInOctets,
       "wfFrServiceRecordifInDiscards": wfFrServiceRecordifInDiscards,
       "wfFrServiceRecordifOutOctets": wfFrServiceRecordifOutOctets,
       "wfFrServiceRecordifOutDiscards": wfFrServiceRecordifOutDiscards,
       "wfFrServiceRecordifOutCtrlPkts": wfFrServiceRecordifOutCtrlPkts,
       "wfFrServiceRecordifInCtrlPkts": wfFrServiceRecordifInCtrlPkts,
       "wfFrSigTable": wfFrSigTable,
       "wfFrSigEntry": wfFrSigEntry,
       "wfFrSigDelete": wfFrSigDelete,
       "wfFrSigDisable": wfFrSigDisable,
       "wfFrSigLineNumber": wfFrSigLineNumber,
       "wfFrSigLLIndex": wfFrSigLLIndex,
       "wfFrSigStatus": wfFrSigStatus,
       "wfFrSigCircuit": wfFrSigCircuit,
       "wfFrSigConformance": wfFrSigConformance,
       "wfFrSigSvcIdleTimer": wfFrSigSvcIdleTimer,
       "wfFrSigMaxSvcs": wfFrSigMaxSvcs,
       "wfFrSigSvcDeletePolicy": wfFrSigSvcDeletePolicy,
       "wfFrSigSvcReplacePolicy": wfFrSigSvcReplacePolicy,
       "wfFrSigT303": wfFrSigT303,
       "wfFrSigT305": wfFrSigT305,
       "wfFrSigT308": wfFrSigT308,
       "wfFrSigT310": wfFrSigT310,
       "wfFrSigT322": wfFrSigT322,
       "wfFrSigN322": wfFrSigN322,
       "wfFrSigNumMaxSVCs": wfFrSigNumMaxSVCs,
       "wfFrSigNumConnRej": wfFrSigNumConnRej,
       "wfFrSigNumSvcRej": wfFrSigNumSvcRej,
       "wfFrSigNumSvcFailed": wfFrSigNumSvcFailed,
       "wfFrLapfTable": wfFrLapfTable,
       "wfFrLapfEntry": wfFrLapfEntry,
       "wfLapfDelete": wfLapfDelete,
       "wfLapfDisable": wfLapfDisable,
       "wfLapfLineNumber": wfLapfLineNumber,
       "wfLapfLLIndex": wfLapfLLIndex,
       "wfLapfStatus": wfLapfStatus,
       "wfLapfStationType": wfLapfStationType,
       "wfLapfActionInitiate": wfLapfActionInitiate,
       "wfLapfT200": wfLapfT200,
       "wfLapfT203": wfLapfT203,
       "wfLapfN200": wfLapfN200,
       "wfLapfN201": wfLapfN201,
       "wfLapfK": wfLapfK,
       "wfLapfRxWin": wfLapfRxWin,
       "wfLapfTxWin": wfLapfTxWin,
       "wfLapfSABMESent": wfLapfSABMESent,
       "wfLapfSABMERcvd": wfLapfSABMERcvd,
       "wfLapfUASent": wfLapfUASent,
       "wfLapfUARcvd": wfLapfUARcvd,
       "wfLapfDISCSent": wfLapfDISCSent,
       "wfLapfDISCRcvd": wfLapfDISCRcvd,
       "wfLapfDMSent": wfLapfDMSent,
       "wfLapfDMRcvd": wfLapfDMRcvd,
       "wfLapfFRMRSent": wfLapfFRMRSent,
       "wfLapfFRMRRcvd": wfLapfFRMRRcvd,
       "wfLapfRNRsSent": wfLapfRNRsSent,
       "wfLapfRNRsRcvd": wfLapfRNRsRcvd,
       "wfLapfREJsSent": wfLapfREJsSent,
       "wfLapfREJsRcvd": wfLapfREJsRcvd,
       "wfLapfIFramesSent": wfLapfIFramesSent,
       "wfLapfIFramesRcvd": wfLapfIFramesRcvd,
       "wfLapfUISent": wfLapfUISent,
       "wfLapfUIRcvd": wfLapfUIRcvd,
       "wfLapfRRsSent": wfLapfRRsSent,
       "wfLapfRRsRcvd": wfLapfRRsRcvd,
       "wfLapfXIDSent": wfLapfXIDSent,
       "wfLapfXIDRcvd": wfLapfXIDRcvd,
       "wfLapfT200Timeouts": wfLapfT200Timeouts,
       "wfLapfT203Timeouts": wfLapfT203Timeouts,
       "wfLapfN200Exceeded": wfLapfN200Exceeded,
       "wfLapfN201Error": wfLapfN201Error,
       "wfFrFRF4SigTable": wfFrFRF4SigTable,
       "wfFrFRF4SigEntry": wfFrFRF4SigEntry,
       "wfFrFRF4SigDelete": wfFrFRF4SigDelete,
       "wfFrFRF4SigDisable": wfFrFRF4SigDisable,
       "wfFrFRF4SigLineNumber": wfFrFRF4SigLineNumber,
       "wfFrFRF4SigLLIndex": wfFrFRF4SigLLIndex,
       "wfFrFRF4SigMaxSvcs": wfFrFRF4SigMaxSvcs,
       "wfFrFRF4SigT303": wfFrFRF4SigT303,
       "wfFrFRF4SigT305": wfFrFRF4SigT305,
       "wfFrFRF4SigT308": wfFrFRF4SigT308,
       "wfFrFRF4SigT310": wfFrFRF4SigT310,
       "wfFrFRF4SigT322": wfFrFRF4SigT322,
       "wfFrFRF4SigN322": wfFrFRF4SigN322,
       "wfFrFRF4SigFramesSent": wfFrFRF4SigFramesSent,
       "wfFrFRF4SigOctetsSent": wfFrFRF4SigOctetsSent,
       "wfFrFRF4SigFramesReceived": wfFrFRF4SigFramesReceived,
       "wfFrFRF4SigOctetsReceived": wfFrFRF4SigOctetsReceived,
       "wfFrFRF4SigFramesDropped": wfFrFRF4SigFramesDropped,
       "wfFrFRF4SigFramesDiscarded": wfFrFRF4SigFramesDiscarded,
       "wfFrFRF4SigSetupRx": wfFrFRF4SigSetupRx,
       "wfFrFRF4SigCallProcRx": wfFrFRF4SigCallProcRx,
       "wfFrFRF4SigConnectRx": wfFrFRF4SigConnectRx,
       "wfFrFRF4SigDisconnectRx": wfFrFRF4SigDisconnectRx,
       "wfFrFRF4SigReleaseRx": wfFrFRF4SigReleaseRx,
       "wfFrFRF4SigReleaseCompleteRx": wfFrFRF4SigReleaseCompleteRx,
       "wfFrFRF4SigStatusRx": wfFrFRF4SigStatusRx,
       "wfFrFRF4SigStatusEnquiryRx": wfFrFRF4SigStatusEnquiryRx,
       "wfFrFRF4SigSetupTx": wfFrFRF4SigSetupTx,
       "wfFrFRF4SigCallProcTx": wfFrFRF4SigCallProcTx,
       "wfFrFRF4SigConnectTx": wfFrFRF4SigConnectTx,
       "wfFrFRF4SigDisconnectTx": wfFrFRF4SigDisconnectTx,
       "wfFrFRF4SigReleaseTx": wfFrFRF4SigReleaseTx,
       "wfFrFRF4SigReleaseCompleteTx": wfFrFRF4SigReleaseCompleteTx,
       "wfFrFRF4SigStatusTx": wfFrFRF4SigStatusTx,
       "wfFrFRF4SigStatusEnquiryTx": wfFrFRF4SigStatusEnquiryTx,
       "wfFrSVCOptionsTable": wfFrSVCOptionsTable,
       "wfFrSVCOptionsEntry": wfFrSVCOptionsEntry,
       "wfFrSVCOptionsDelete": wfFrSVCOptionsDelete,
       "wfFrSVCOptionsDisable": wfFrSVCOptionsDisable,
       "wfFrSVCOptionsLineNumber": wfFrSVCOptionsLineNumber,
       "wfFrSVCOptionsLLIndex": wfFrSVCOptionsLLIndex,
       "wfFrSVCOptionsCircuitNumber": wfFrSVCOptionsCircuitNumber,
       "wfFrSVCOptionsInstanceIndex": wfFrSVCOptionsInstanceIndex,
       "wfFrSVCOptionsRemNum": wfFrSVCOptionsRemNum,
       "wfFrSVCOptionsRemSubAdr": wfFrSVCOptionsRemSubAdr,
       "wfFrSVCOptionsRemPlan": wfFrSVCOptionsRemPlan,
       "wfFrSVCOptionsRemTypeNum": wfFrSVCOptionsRemTypeNum,
       "wfFrSVCOptionsBroadcastDisable": wfFrSVCOptionsBroadcastDisable,
       "wfFrSVCOptionsInactTimer": wfFrSVCOptionsInactTimer,
       "wfFrSVCOptionsInactMode": wfFrSVCOptionsInactMode,
       "wfFrSVCOptionsX213DataPriority": wfFrSVCOptionsX213DataPriority,
       "wfFrSVCOptionsX213DataLQAPriority": wfFrSVCOptionsX213DataLQAPriority,
       "wfFrSVCOptionsX213GainPriority": wfFrSVCOptionsX213GainPriority,
       "wfFrSVCOptionsX213GainLQAPriority": wfFrSVCOptionsX213GainLQAPriority,
       "wfFrSVCOptionsX213KeepPriority": wfFrSVCOptionsX213KeepPriority,
       "wfFrSVCOptionsX213KeepLQAPriority": wfFrSVCOptionsX213KeepLQAPriority,
       "wfFrSVCOptionsLLCoreOutThroughput": wfFrSVCOptionsLLCoreOutThroughput,
       "wfFrSVCOptionsLLCoreInThroughput": wfFrSVCOptionsLLCoreInThroughput,
       "wfFrSVCOptionsLLCoreMinOutThroughput": wfFrSVCOptionsLLCoreMinOutThroughput,
       "wfFrSVCOptionsLLCoreMinInThroughput": wfFrSVCOptionsLLCoreMinInThroughput,
       "wfFrSVCOptionsLLCoreOutBc": wfFrSVCOptionsLLCoreOutBc,
       "wfFrSVCOptionsLLCoreInBc": wfFrSVCOptionsLLCoreInBc,
       "wfFrSVCOptionsLLCoreOutBe": wfFrSVCOptionsLLCoreOutBe,
       "wfFrSVCOptionsLLCoreInBe": wfFrSVCOptionsLLCoreInBe,
       "wfFrSVCOptionsCongestionDisable": wfFrSVCOptionsCongestionDisable,
       "wfFrSVCOptionsCongestionTmr": wfFrSVCOptionsCongestionTmr,
       "wfFrSVCOptionsCongestionCtr": wfFrSVCOptionsCongestionCtr,
       "wfFrSVCOptionsCongestionMethod": wfFrSVCOptionsCongestionMethod,
       "wfFrSVCOptionsTrafficShapingDisable": wfFrSVCOptionsTrafficShapingDisable,
       "wfFrSVCOptionsWcpEnable": wfFrSVCOptionsWcpEnable,
       "wfFrSVCOptionsName": wfFrSVCOptionsName,
       "wfFrSVCActiveCallTable": wfFrSVCActiveCallTable,
       "wfFrSVCActiveCallEntry": wfFrSVCActiveCallEntry,
       "wfFrSVCActiveCallDelete": wfFrSVCActiveCallDelete,
       "wfFrSVCActiveCallLineNumber": wfFrSVCActiveCallLineNumber,
       "wfFrSVCActiveCallLLIndex": wfFrSVCActiveCallLLIndex,
       "wfFrSVCActiveCallDLCI": wfFrSVCActiveCallDLCI,
       "wfFrSVCActiveCallDirection": wfFrSVCActiveCallDirection,
       "wfFrSVCActiveCallCircuitNumber": wfFrSVCActiveCallCircuitNumber,
       "wfFrSVCActiveCallCalledNum": wfFrSVCActiveCallCalledNum,
       "wfFrSVCActiveCallCalledSubAdr": wfFrSVCActiveCallCalledSubAdr,
       "wfFrSVCActiveCallCalledPlan": wfFrSVCActiveCallCalledPlan,
       "wfFrSVCActiveCallCalledTypeNum": wfFrSVCActiveCallCalledTypeNum,
       "wfFrSVCActiveCallCallingNum": wfFrSVCActiveCallCallingNum,
       "wfFrSVCActiveCallCallingSubAdr": wfFrSVCActiveCallCallingSubAdr,
       "wfFrSVCActiveCallCallingPlan": wfFrSVCActiveCallCallingPlan,
       "wfFrSVCActiveCallCallingTypeNum": wfFrSVCActiveCallCallingTypeNum,
       "wfFrSVCActiveCallX213DataPriority": wfFrSVCActiveCallX213DataPriority,
       "wfFrSVCActiveCallX213DataLQAPriority": wfFrSVCActiveCallX213DataLQAPriority,
       "wfFrSVCActiveCallX213GainPriority": wfFrSVCActiveCallX213GainPriority,
       "wfFrSVCActiveCallX213GainLQAPriority": wfFrSVCActiveCallX213GainLQAPriority,
       "wfFrSVCActiveCallX213KeepPriority": wfFrSVCActiveCallX213KeepPriority,
       "wfFrSVCActiveCallX213KeepLQAPriority": wfFrSVCActiveCallX213KeepLQAPriority,
       "wfFrSVCActiveCallLLCoreOutThroughput": wfFrSVCActiveCallLLCoreOutThroughput,
       "wfFrSVCActiveCallLLCoreInThroughput": wfFrSVCActiveCallLLCoreInThroughput,
       "wfFrSVCActiveCallLLCoreMinOutThroughput": wfFrSVCActiveCallLLCoreMinOutThroughput,
       "wfFrSVCActiveCallLLCoreMinInThroughput": wfFrSVCActiveCallLLCoreMinInThroughput,
       "wfFrSVCActiveCallLLCoreOutBc": wfFrSVCActiveCallLLCoreOutBc,
       "wfFrSVCActiveCallLLCoreInBc": wfFrSVCActiveCallLLCoreInBc,
       "wfFrSVCActiveCallLLCoreOutBe": wfFrSVCActiveCallLLCoreOutBe,
       "wfFrSVCActiveCallLLCoreInBe": wfFrSVCActiveCallLLCoreInBe,
       "wfFrSVCActiveCallConnectTime": wfFrSVCActiveCallConnectTime,
       "wfFrPtIntfTable": wfFrPtIntfTable,
       "wfFrPtIntfEntry": wfFrPtIntfEntry,
       "wfFrPtIntfDelete": wfFrPtIntfDelete,
       "wfFrPtIntfDisable": wfFrPtIntfDisable,
       "wfFrPtIntfCct": wfFrPtIntfCct,
       "wfFrPtIntfDlci": wfFrPtIntfDlci,
       "wfFrPtIntfState": wfFrPtIntfState,
       "wfFrPtIntfRxFrames": wfFrPtIntfRxFrames,
       "wfFrPtIntfTxFrames": wfFrPtIntfTxFrames,
       "wfFrPtIntfDiscards": wfFrPtIntfDiscards,
       "wfFrPtIntfDrops": wfFrPtIntfDrops,
       "wfFrPtMappingTable": wfFrPtMappingTable,
       "wfFrPtMappingEntry": wfFrPtMappingEntry,
       "wfFrPtMappingDelete": wfFrPtMappingDelete,
       "wfFrPtMappingDisable": wfFrPtMappingDisable,
       "wfFrPtMappingCctA": wfFrPtMappingCctA,
       "wfFrPtMappingDlciA": wfFrPtMappingDlciA,
       "wfFrPtMappingCctB": wfFrPtMappingCctB,
       "wfFrPtMappingDlciB": wfFrPtMappingDlciB,
       "wfFrPtMappingState": wfFrPtMappingState,
       "wfFrMlTable": wfFrMlTable,
       "wfFrMlEntry": wfFrMlEntry,
       "wfFrMlDelete": wfFrMlDelete,
       "wfFrMlCircuitNumber": wfFrMlCircuitNumber,
       "wfFrMlMode": wfFrMlMode,
       "wfFrMlFragPermEnable": wfFrMlFragPermEnable,
       "wfFrMlCircuitMaxBuffers": wfFrMlCircuitMaxBuffers,
       "wfFrMlFragTriggerSize": wfFrMlFragTriggerSize,
       "wfFrMlFragStrict": wfFrMlFragStrict,
       "wfFrMlAggVCStatusMode": wfFrMlAggVCStatusMode,
       "wfFrMlCompressionEnable": wfFrMlCompressionEnable,
       "wfFrMlHomeSlot": wfFrMlHomeSlot,
       "wfFrMlStatsLineCnt": wfFrMlStatsLineCnt,
       "wfFrMlStatsBundleSpd": wfFrMlStatsBundleSpd,
       "wfFrMlStatsTxOctets": wfFrMlStatsTxOctets,
       "wfFrMlStatsTxPkts": wfFrMlStatsTxPkts,
       "wfFrMlStatsAvgTxListLen": wfFrMlStatsAvgTxListLen,
       "wfFrMlStatsRxOctets": wfFrMlStatsRxOctets,
       "wfFrMlStatsRxPkts": wfFrMlStatsRxPkts,
       "wfFrMlStatsReasmFails": wfFrMlStatsReasmFails,
       "wfFrMlStatsSeqNumberLost": wfFrMlStatsSeqNumberLost,
       "wfFrMlStatsSeqNumberArrivedLate": wfFrMlStatsSeqNumberArrivedLate,
       "wfFrMlStatsReSeqBufferCnt": wfFrMlStatsReSeqBufferCnt,
       "wfFrMlStatsReSeqBufferMax": wfFrMlStatsReSeqBufferMax,
       "wfFrMlStatsExceededBufferMax": wfFrMlStatsExceededBufferMax,
       "wfFrMlStatsLinkIdleEvents": wfFrMlStatsLinkIdleEvents,
       "wfFrMlStatsCalcPercent": wfFrMlStatsCalcPercent,
       "wfFrMlStatsDebug": wfFrMlStatsDebug,
       "wfFrMlStatsReassmBufferCnt": wfFrMlStatsReassmBufferCnt,
       "wfFrMlStatsReassmBufferMax": wfFrMlStatsReassmBufferMax,
       "wfFrMlStatsNumPktsFragmented": wfFrMlStatsNumPktsFragmented,
       "wfFrMlStatsPQHiXmits": wfFrMlStatsPQHiXmits,
       "wfFrMlStatsPQNormalXmits": wfFrMlStatsPQNormalXmits,
       "wfFrMlStatsPQLoXmits": wfFrMlStatsPQLoXmits,
       "wfFrMlStatsPQHiClippedPkts": wfFrMlStatsPQHiClippedPkts,
       "wfFrMlStatsPQNormalClippedPkts": wfFrMlStatsPQNormalClippedPkts,
       "wfFrMlStatsPQLoClippedPkts": wfFrMlStatsPQLoClippedPkts,
       "wfFrMlStatsPQIntrQHighWaterPkts": wfFrMlStatsPQIntrQHighWaterPkts,
       "wfFrMlStatsPQHiQHighWaterPkts": wfFrMlStatsPQHiQHighWaterPkts,
       "wfFrMlStatsPQNormalQHighWaterPkts": wfFrMlStatsPQNormalQHighWaterPkts,
       "wfFrMlStatsPQLoQHighWaterPkts": wfFrMlStatsPQLoQHighWaterPkts,
       "wfFrMlStatsPQHighWaterPktsClear": wfFrMlStatsPQHighWaterPktsClear,
       "wfFrMlStatsPQDroppedPkts": wfFrMlStatsPQDroppedPkts,
       "wfFrMlStatsPQLargePkts": wfFrMlStatsPQLargePkts,
       "wfFrMlStatsPQHiTotalOctets": wfFrMlStatsPQHiTotalOctets,
       "wfFrMlStatsPQNormalTotalOctets": wfFrMlStatsPQNormalTotalOctets,
       "wfFrMlStatsPQLoTotalOctets": wfFrMlStatsPQLoTotalOctets,
       "wfFrMlStatsPQPktsNotQueued": wfFrMlStatsPQPktsNotQueued,
       "wfFrMlVCTable": wfFrMlVCTable,
       "wfFrMlVCEntry": wfFrMlVCEntry,
       "wfFrMlVCDelete": wfFrMlVCDelete,
       "wfFrMlVCCircuitNumber": wfFrMlVCCircuitNumber,
       "wfFrMlVCDlci": wfFrMlVCDlci,
       "wfFrMlVCAggState": wfFrMlVCAggState,
       "wfFrMlVCAggNumberVCs": wfFrMlVCAggNumberVCs,
       "wfFrMlVCAggNumberVCsActive": wfFrMlVCAggNumberVCsActive,
       "wfFrMlVCStatsLineCnt": wfFrMlVCStatsLineCnt,
       "wfFrMlVCStatsBundleSpd": wfFrMlVCStatsBundleSpd,
       "wfFrMlVCStatsTxOctets": wfFrMlVCStatsTxOctets,
       "wfFrMlVCStatsTxPkts": wfFrMlVCStatsTxPkts,
       "wfFrMlVCStatsAvgTxListLen": wfFrMlVCStatsAvgTxListLen,
       "wfFrMlVCStatsRxOctets": wfFrMlVCStatsRxOctets,
       "wfFrMlVCStatsRxPkts": wfFrMlVCStatsRxPkts,
       "wfFrMlVCStatsReasmFails": wfFrMlVCStatsReasmFails,
       "wfFrMlVCStatsSeqNumberLost": wfFrMlVCStatsSeqNumberLost,
       "wfFrMlVCStatsSeqNumberArrivedLate": wfFrMlVCStatsSeqNumberArrivedLate,
       "wfFrMlVCStatsReSeqBufferCnt": wfFrMlVCStatsReSeqBufferCnt,
       "wfFrMlVCStatsReSeqBufferMax": wfFrMlVCStatsReSeqBufferMax,
       "wfFrMlVCStatsExceededBufferMax": wfFrMlVCStatsExceededBufferMax,
       "wfFrMlVCStatsLinkIdleEvents": wfFrMlVCStatsLinkIdleEvents,
       "wfFrMlVCStatsCalcPercent": wfFrMlVCStatsCalcPercent,
       "wfFrMlVCStatsDebug": wfFrMlVCStatsDebug,
       "wfFrMlVCStatsReassmBufferCnt": wfFrMlVCStatsReassmBufferCnt,
       "wfFrMlVCStatsReassmBufferMax": wfFrMlVCStatsReassmBufferMax,
       "wfFrMlVCStatsNumPktsFragmented": wfFrMlVCStatsNumPktsFragmented,
       "wfFrMapDlcmiTable": wfFrMapDlcmiTable,
       "wfFrMapDlcmiEntry": wfFrMapDlcmiEntry,
       "wfFrMapDlcmiIfIndex": wfFrMapDlcmiIfIndex,
       "wfFrMapDlcmiState": wfFrMapDlcmiState,
       "wfFrMapDlcmiAddress": wfFrMapDlcmiAddress,
       "wfFrMapDlcmiAddressLen": wfFrMapDlcmiAddressLen,
       "wfFrMapDlcmiPollingInterval": wfFrMapDlcmiPollingInterval,
       "wfFrMapDlcmiFullEnquiryInterval": wfFrMapDlcmiFullEnquiryInterval,
       "wfFrMapDlcmiErrorThreshold": wfFrMapDlcmiErrorThreshold,
       "wfFrMapDlcmiMonitoredEvents": wfFrMapDlcmiMonitoredEvents,
       "wfFrMapDlcmiMaxSupportedVCs": wfFrMapDlcmiMaxSupportedVCs,
       "wfFrMapDlcmiMulticast": wfFrMapDlcmiMulticast,
       "wfFrMapDlcmiStatus": wfFrMapDlcmiStatus,
       "wfFrMapDlcmiRowStatus": wfFrMapDlcmiRowStatus,
       "wfFrMapDlcmiLineNumber": wfFrMapDlcmiLineNumber,
       "wfFrMapDlcmiLLIndex": wfFrMapDlcmiLLIndex,
       "wfFrMapCircuitTable": wfFrMapCircuitTable,
       "wfFrMapCircuitEntry": wfFrMapCircuitEntry,
       "wfFrMapCircuitIfIndex": wfFrMapCircuitIfIndex,
       "wfFrMapCircuitDlci": wfFrMapCircuitDlci,
       "wfFrMapCircuitState": wfFrMapCircuitState,
       "wfFrMapCircuitReceivedFECNs": wfFrMapCircuitReceivedFECNs,
       "wfFrMapCircuitReceivedBECNs": wfFrMapCircuitReceivedBECNs,
       "wfFrMapCircuitSentFrames": wfFrMapCircuitSentFrames,
       "wfFrMapCircuitSentOctets": wfFrMapCircuitSentOctets,
       "wfFrMapCircuitReceivedFrames": wfFrMapCircuitReceivedFrames,
       "wfFrMapCircuitReceivedOctets": wfFrMapCircuitReceivedOctets,
       "wfFrMapCircuitCreationTime": wfFrMapCircuitCreationTime,
       "wfFrMapCircuitLastTimeChange": wfFrMapCircuitLastTimeChange,
       "wfFrMapCircuitCommittedBurst": wfFrMapCircuitCommittedBurst,
       "wfFrMapCircuitExcessBurst": wfFrMapCircuitExcessBurst,
       "wfFrMapCircuitThroughput": wfFrMapCircuitThroughput,
       "wfFrMapCircuitMulticast": wfFrMapCircuitMulticast,
       "wfFrMapCircuitType": wfFrMapCircuitType,
       "wfFrMapCircuitDiscards": wfFrMapCircuitDiscards,
       "wfFrMapCircuitReceivedDEs": wfFrMapCircuitReceivedDEs,
       "wfFrMapCircuitSentDEs": wfFrMapCircuitSentDEs,
       "wfFrMapCircuitLogicalIfIndex": wfFrMapCircuitLogicalIfIndex,
       "wfFrMapCircuitRowStatus": wfFrMapCircuitRowStatus,
       "wfFrMapCircuitLineNumber": wfFrMapCircuitLineNumber,
       "wfFrMapCircuitLLIndex": wfFrMapCircuitLLIndex,
       "wfFrMapErrTable": wfFrMapErrTable,
       "wfFrMapErrEntry": wfFrMapErrEntry,
       "wfFrMapErrIfIndex": wfFrMapErrIfIndex,
       "wfFrMapErrType": wfFrMapErrType,
       "wfFrMapErrData": wfFrMapErrData,
       "wfFrMapErrTime": wfFrMapErrTime,
       "wfFrMapErrFaults": wfFrMapErrFaults,
       "wfFrMapErrFaultTime": wfFrMapErrFaultTime,
       "wfFrMapErrLineNumber": wfFrMapErrLineNumber,
       "wfFrMapErrLLIndex": wfFrMapErrLLIndex}
)
