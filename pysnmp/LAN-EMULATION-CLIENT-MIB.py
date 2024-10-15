# SNMP MIB module (LAN-EMULATION-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LAN-EMULATION-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:31 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

leClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1)
)


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""



# TEXTUAL-CONVENTIONS



class AtmLaneAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )



class VpiInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class VciInteger(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LeConnectionInterface(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class LecState(Integer32, TextualConvention):
    status = "current"
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
        *(("busConnect", 6),
          ("configure", 3),
          ("initialRegistration", 5),
          ("initialState", 1),
          ("join", 4),
          ("lecsConnect", 2),
          ("operational", 7))
    )



class LecDataFrameFormat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aflane8023", 2),
          ("aflane8025", 3),
          ("unspecified", 1))
    )



class LecDataFrameSize(Integer32, TextualConvention):
    status = "current"
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
        *(("max1516", 2),
          ("max18190", 5),
          ("max4544", 3),
          ("max9234", 4),
          ("unspecified", 1))
    )



class LeArpTableEntryType(Integer32, TextualConvention):
    status = "current"
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
        *(("learnedViaControl", 2),
          ("learnedViaData", 3),
          ("other", 1),
          ("staticNonVolatile", 5),
          ("staticVolatile", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AtmfLanEmulation_ObjectIdentity = ObjectIdentity
atmfLanEmulation = _AtmfLanEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3)
)
_LeClientMIBObjects_ObjectIdentity = ObjectIdentity
leClientMIBObjects = _LeClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1)
)
_LecConfigTable_Object = MibTable
lecConfigTable = _LecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lecConfigTable.setStatus("current")
_LecConfigEntry_Object = MibTableRow
lecConfigEntry = _LecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1)
)
lecConfigEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecConfigEntry.setStatus("current")


class _LecIndex_Type(Integer32):
    """Custom type lecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LecIndex_Type.__name__ = "Integer32"
_LecIndex_Object = MibTableColumn
lecIndex = _LecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 1),
    _LecIndex_Type()
)
lecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecIndex.setStatus("current")
_LecRowStatus_Type = RowStatus
_LecRowStatus_Object = MibTableColumn
lecRowStatus = _LecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 2),
    _LecRowStatus_Type()
)
lecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecRowStatus.setStatus("current")


class _LecOwner_Type(OwnerString):
    """Custom type lecOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LecOwner_Type.__name__ = "OwnerString"
_LecOwner_Object = MibTableColumn
lecOwner = _LecOwner_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 3),
    _LecOwner_Type()
)
lecOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecOwner.setStatus("current")


class _LecConfigMode_Type(Integer32):
    """Custom type lecConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_LecConfigMode_Type.__name__ = "Integer32"
_LecConfigMode_Object = MibTableColumn
lecConfigMode = _LecConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 4),
    _LecConfigMode_Type()
)
lecConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfigMode.setStatus("current")


class _LecConfigLanType_Type(LecDataFrameFormat):
    """Custom type lecConfigLanType based on LecDataFrameFormat"""


_LecConfigLanType_Object = MibTableColumn
lecConfigLanType = _LecConfigLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 5),
    _LecConfigLanType_Type()
)
lecConfigLanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfigLanType.setStatus("current")


class _LecConfigMaxDataFrameSize_Type(LecDataFrameSize):
    """Custom type lecConfigMaxDataFrameSize based on LecDataFrameSize"""


_LecConfigMaxDataFrameSize_Object = MibTableColumn
lecConfigMaxDataFrameSize = _LecConfigMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 6),
    _LecConfigMaxDataFrameSize_Type()
)
lecConfigMaxDataFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfigMaxDataFrameSize.setStatus("current")


class _LecConfigLanName_Type(OctetString):
    """Custom type lecConfigLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecConfigLanName_Type.__name__ = "OctetString"
_LecConfigLanName_Object = MibTableColumn
lecConfigLanName = _LecConfigLanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 7),
    _LecConfigLanName_Type()
)
lecConfigLanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfigLanName.setStatus("current")
_LecConfigLesAtmAddress_Type = AtmLaneAddress
_LecConfigLesAtmAddress_Object = MibTableColumn
lecConfigLesAtmAddress = _LecConfigLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 8),
    _LecConfigLesAtmAddress_Type()
)
lecConfigLesAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConfigLesAtmAddress.setStatus("current")


class _LecControlTimeout_Type(Integer32):
    """Custom type lecControlTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LecControlTimeout_Type.__name__ = "Integer32"
_LecControlTimeout_Object = MibTableColumn
lecControlTimeout = _LecControlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 9),
    _LecControlTimeout_Type()
)
lecControlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecControlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    lecControlTimeout.setUnits("seconds")


class _LecMaxUnknownFrameCount_Type(Integer32):
    """Custom type lecMaxUnknownFrameCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LecMaxUnknownFrameCount_Type.__name__ = "Integer32"
_LecMaxUnknownFrameCount_Object = MibTableColumn
lecMaxUnknownFrameCount = _LecMaxUnknownFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 10),
    _LecMaxUnknownFrameCount_Type()
)
lecMaxUnknownFrameCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameCount.setUnits("frames")


class _LecMaxUnknownFrameTime_Type(Integer32):
    """Custom type lecMaxUnknownFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_LecMaxUnknownFrameTime_Type.__name__ = "Integer32"
_LecMaxUnknownFrameTime_Object = MibTableColumn
lecMaxUnknownFrameTime = _LecMaxUnknownFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 11),
    _LecMaxUnknownFrameTime_Type()
)
lecMaxUnknownFrameTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameTime.setStatus("current")
if mibBuilder.loadTexts:
    lecMaxUnknownFrameTime.setUnits("seconds")


class _LecVccTimeoutPeriod_Type(Integer32):
    """Custom type lecVccTimeoutPeriod based on Integer32"""
    defaultValue = 1200


_LecVccTimeoutPeriod_Object = MibTableColumn
lecVccTimeoutPeriod = _LecVccTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 12),
    _LecVccTimeoutPeriod_Type()
)
lecVccTimeoutPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecVccTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    lecVccTimeoutPeriod.setUnits("seconds")


class _LecMaxRetryCount_Type(Integer32):
    """Custom type lecMaxRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LecMaxRetryCount_Type.__name__ = "Integer32"
_LecMaxRetryCount_Object = MibTableColumn
lecMaxRetryCount = _LecMaxRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 13),
    _LecMaxRetryCount_Type()
)
lecMaxRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMaxRetryCount.setStatus("current")


class _LecAgingTime_Type(Integer32):
    """Custom type lecAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_LecAgingTime_Type.__name__ = "Integer32"
_LecAgingTime_Object = MibTableColumn
lecAgingTime = _LecAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 14),
    _LecAgingTime_Type()
)
lecAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    lecAgingTime.setUnits("seconds")


class _LecForwardDelayTime_Type(Integer32):
    """Custom type lecForwardDelayTime based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_LecForwardDelayTime_Type.__name__ = "Integer32"
_LecForwardDelayTime_Object = MibTableColumn
lecForwardDelayTime = _LecForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 15),
    _LecForwardDelayTime_Type()
)
lecForwardDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecForwardDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    lecForwardDelayTime.setUnits("seconds")


class _LecExpectedArpResponseTime_Type(Integer32):
    """Custom type lecExpectedArpResponseTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_LecExpectedArpResponseTime_Type.__name__ = "Integer32"
_LecExpectedArpResponseTime_Object = MibTableColumn
lecExpectedArpResponseTime = _LecExpectedArpResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 16),
    _LecExpectedArpResponseTime_Type()
)
lecExpectedArpResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecExpectedArpResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    lecExpectedArpResponseTime.setUnits("seconds")


class _LecFlushTimeOut_Type(Integer32):
    """Custom type lecFlushTimeOut based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_LecFlushTimeOut_Type.__name__ = "Integer32"
_LecFlushTimeOut_Object = MibTableColumn
lecFlushTimeOut = _LecFlushTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 17),
    _LecFlushTimeOut_Type()
)
lecFlushTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecFlushTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    lecFlushTimeOut.setUnits("seconds")


class _LecPathSwitchingDelay_Type(Integer32):
    """Custom type lecPathSwitchingDelay based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LecPathSwitchingDelay_Type.__name__ = "Integer32"
_LecPathSwitchingDelay_Object = MibTableColumn
lecPathSwitchingDelay = _LecPathSwitchingDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 18),
    _LecPathSwitchingDelay_Type()
)
lecPathSwitchingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecPathSwitchingDelay.setStatus("current")
if mibBuilder.loadTexts:
    lecPathSwitchingDelay.setUnits("seconds")


class _LecLocalSegmentID_Type(Integer32):
    """Custom type lecLocalSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecLocalSegmentID_Type.__name__ = "Integer32"
_LecLocalSegmentID_Object = MibTableColumn
lecLocalSegmentID = _LecLocalSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 19),
    _LecLocalSegmentID_Type()
)
lecLocalSegmentID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecLocalSegmentID.setStatus("current")


class _LecMulticastSendType_Type(Integer32):
    """Custom type lecMulticastSendType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 1),
          ("constantBitRate", 3),
          ("variableBitRate", 2))
    )


_LecMulticastSendType_Type.__name__ = "Integer32"
_LecMulticastSendType_Object = MibTableColumn
lecMulticastSendType = _LecMulticastSendType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 20),
    _LecMulticastSendType_Type()
)
lecMulticastSendType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMulticastSendType.setStatus("current")
_LecMulticastSendAvgRate_Type = Integer32
_LecMulticastSendAvgRate_Object = MibTableColumn
lecMulticastSendAvgRate = _LecMulticastSendAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 21),
    _LecMulticastSendAvgRate_Type()
)
lecMulticastSendAvgRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMulticastSendAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    lecMulticastSendAvgRate.setUnits("cells per second")
_LecMulticastSendPeakRate_Type = Integer32
_LecMulticastSendPeakRate_Object = MibTableColumn
lecMulticastSendPeakRate = _LecMulticastSendPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 22),
    _LecMulticastSendPeakRate_Type()
)
lecMulticastSendPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecMulticastSendPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    lecMulticastSendPeakRate.setUnits("cells per second")


class _LecConnectionCompleteTimer_Type(Integer32):
    """Custom type lecConnectionCompleteTimer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LecConnectionCompleteTimer_Type.__name__ = "Integer32"
_LecConnectionCompleteTimer_Object = MibTableColumn
lecConnectionCompleteTimer = _LecConnectionCompleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 1, 1, 23),
    _LecConnectionCompleteTimer_Type()
)
lecConnectionCompleteTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecConnectionCompleteTimer.setStatus("current")
if mibBuilder.loadTexts:
    lecConnectionCompleteTimer.setUnits("seconds")
_LecStatusTable_Object = MibTable
lecStatusTable = _LecStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lecStatusTable.setStatus("current")
_LecStatusEntry_Object = MibTableRow
lecStatusEntry = _LecStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1)
)
lecStatusEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecStatusEntry.setStatus("current")
_LecIfIndex_Type = Integer32
_LecIfIndex_Object = MibTableColumn
lecIfIndex = _LecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 1),
    _LecIfIndex_Type()
)
lecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecIfIndex.setStatus("current")
_LecPrimaryAtmAddress_Type = AtmLaneAddress
_LecPrimaryAtmAddress_Object = MibTableColumn
lecPrimaryAtmAddress = _LecPrimaryAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 2),
    _LecPrimaryAtmAddress_Type()
)
lecPrimaryAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecPrimaryAtmAddress.setStatus("current")


class _LecID_Type(Integer32):
    """Custom type lecID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65279),
    )


_LecID_Type.__name__ = "Integer32"
_LecID_Object = MibTableColumn
lecID = _LecID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 3),
    _LecID_Type()
)
lecID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecID.setStatus("current")
_LecInterfaceState_Type = LecState
_LecInterfaceState_Object = MibTableColumn
lecInterfaceState = _LecInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 4),
    _LecInterfaceState_Type()
)
lecInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecInterfaceState.setStatus("current")


class _LecLastFailureRespCode_Type(Integer32):
    """Custom type lecLastFailureRespCode based on Integer32"""
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
        *(("accessDenied", 9),
          ("duplicateAtmAddress", 7),
          ("duplicateLanDestination", 6),
          ("insufficientInformation", 15),
          ("insufficientResources", 8),
          ("invalidAtmAddress", 12),
          ("invalidLanDestination", 11),
          ("invalidRequestParameters", 5),
          ("invalidRequesterId", 10),
          ("leConfigureError", 14),
          ("noConfiguration", 13),
          ("none", 1),
          ("timeout", 2),
          ("undefinedError", 3),
          ("versionNotSupported", 4))
    )


_LecLastFailureRespCode_Type.__name__ = "Integer32"
_LecLastFailureRespCode_Object = MibTableColumn
lecLastFailureRespCode = _LecLastFailureRespCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 5),
    _LecLastFailureRespCode_Type()
)
lecLastFailureRespCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureRespCode.setStatus("current")
_LecLastFailureState_Type = LecState
_LecLastFailureState_Object = MibTableColumn
lecLastFailureState = _LecLastFailureState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 6),
    _LecLastFailureState_Type()
)
lecLastFailureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecLastFailureState.setStatus("current")


class _LecProtocol_Type(Integer32):
    """Custom type lecProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LecProtocol_Type.__name__ = "Integer32"
_LecProtocol_Object = MibTableColumn
lecProtocol = _LecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 7),
    _LecProtocol_Type()
)
lecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecProtocol.setStatus("current")


class _LecVersion_Type(Integer32):
    """Custom type lecVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LecVersion_Type.__name__ = "Integer32"
_LecVersion_Object = MibTableColumn
lecVersion = _LecVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 8),
    _LecVersion_Type()
)
lecVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecVersion.setStatus("current")
_LecTopologyChange_Type = TruthValue
_LecTopologyChange_Object = MibTableColumn
lecTopologyChange = _LecTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 9),
    _LecTopologyChange_Type()
)
lecTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecTopologyChange.setStatus("current")
_LecConfigServerAtmAddress_Type = AtmLaneAddress
_LecConfigServerAtmAddress_Object = MibTableColumn
lecConfigServerAtmAddress = _LecConfigServerAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 10),
    _LecConfigServerAtmAddress_Type()
)
lecConfigServerAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigServerAtmAddress.setStatus("current")


class _LecConfigSource_Type(Integer32):
    """Custom type lecConfigSource based on Integer32"""
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
        *(("didNotUseLecs", 4),
          ("gotAddressViaIlmi", 1),
          ("usedLecsPvc", 3),
          ("usedWellKnownAddress", 2))
    )


_LecConfigSource_Type.__name__ = "Integer32"
_LecConfigSource_Object = MibTableColumn
lecConfigSource = _LecConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 11),
    _LecConfigSource_Type()
)
lecConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigSource.setStatus("current")
_LecActualLanType_Type = LecDataFrameFormat
_LecActualLanType_Object = MibTableColumn
lecActualLanType = _LecActualLanType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 12),
    _LecActualLanType_Type()
)
lecActualLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanType.setStatus("current")
_LecActualMaxDataFrameSize_Type = LecDataFrameSize
_LecActualMaxDataFrameSize_Object = MibTableColumn
lecActualMaxDataFrameSize = _LecActualMaxDataFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 13),
    _LecActualMaxDataFrameSize_Type()
)
lecActualMaxDataFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualMaxDataFrameSize.setStatus("current")


class _LecActualLanName_Type(OctetString):
    """Custom type lecActualLanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LecActualLanName_Type.__name__ = "OctetString"
_LecActualLanName_Object = MibTableColumn
lecActualLanName = _LecActualLanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 14),
    _LecActualLanName_Type()
)
lecActualLanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLanName.setStatus("current")
_LecActualLesAtmAddress_Type = AtmLaneAddress
_LecActualLesAtmAddress_Object = MibTableColumn
lecActualLesAtmAddress = _LecActualLesAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 15),
    _LecActualLesAtmAddress_Type()
)
lecActualLesAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecActualLesAtmAddress.setStatus("current")
_LecProxyClient_Type = TruthValue
_LecProxyClient_Object = MibTableColumn
lecProxyClient = _LecProxyClient_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 2, 1, 16),
    _LecProxyClient_Type()
)
lecProxyClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecProxyClient.setStatus("current")
_LecMappingTable_Object = MibTable
lecMappingTable = _LecMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lecMappingTable.setStatus("current")
_LecMappingEntry_Object = MibTableRow
lecMappingEntry = _LecMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3, 1)
)
lecMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lecMappingEntry.setStatus("current")


class _LecMappingIndex_Type(Integer32):
    """Custom type lecMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LecMappingIndex_Type.__name__ = "Integer32"
_LecMappingIndex_Object = MibTableColumn
lecMappingIndex = _LecMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 3, 1, 1),
    _LecMappingIndex_Type()
)
lecMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMappingIndex.setStatus("current")
_LecStatisticsTable_Object = MibTable
lecStatisticsTable = _LecStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lecStatisticsTable.setStatus("current")
_LecStatisticsEntry_Object = MibTableRow
lecStatisticsEntry = _LecStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1)
)
lecStatisticsEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecStatisticsEntry.setStatus("current")
_LecArpRequestsOut_Type = Counter32
_LecArpRequestsOut_Object = MibTableColumn
lecArpRequestsOut = _LecArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 1),
    _LecArpRequestsOut_Type()
)
lecArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsOut.setStatus("current")
_LecArpRequestsIn_Type = Counter32
_LecArpRequestsIn_Object = MibTableColumn
lecArpRequestsIn = _LecArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 2),
    _LecArpRequestsIn_Type()
)
lecArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRequestsIn.setStatus("current")
_LecArpRepliesOut_Type = Counter32
_LecArpRepliesOut_Object = MibTableColumn
lecArpRepliesOut = _LecArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 3),
    _LecArpRepliesOut_Type()
)
lecArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesOut.setStatus("current")
_LecArpRepliesIn_Type = Counter32
_LecArpRepliesIn_Object = MibTableColumn
lecArpRepliesIn = _LecArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 4),
    _LecArpRepliesIn_Type()
)
lecArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecArpRepliesIn.setStatus("current")
_LecControlFramesOut_Type = Counter32
_LecControlFramesOut_Object = MibTableColumn
lecControlFramesOut = _LecControlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 5),
    _LecControlFramesOut_Type()
)
lecControlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesOut.setStatus("current")
_LecControlFramesIn_Type = Counter32
_LecControlFramesIn_Object = MibTableColumn
lecControlFramesIn = _LecControlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 6),
    _LecControlFramesIn_Type()
)
lecControlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlFramesIn.setStatus("current")
_LecSvcFailures_Type = Counter32
_LecSvcFailures_Object = MibTableColumn
lecSvcFailures = _LecSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 4, 1, 7),
    _LecSvcFailures_Type()
)
lecSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecSvcFailures.setStatus("current")
_LecServerVccTable_Object = MibTable
lecServerVccTable = _LecServerVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lecServerVccTable.setStatus("current")
_LecServerVccEntry_Object = MibTableRow
lecServerVccEntry = _LecServerVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1)
)
lecServerVccEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
)
if mibBuilder.loadTexts:
    lecServerVccEntry.setStatus("current")
_LecConfigDirectInterface_Type = LeConnectionInterface
_LecConfigDirectInterface_Object = MibTableColumn
lecConfigDirectInterface = _LecConfigDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 1),
    _LecConfigDirectInterface_Type()
)
lecConfigDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectInterface.setStatus("current")
_LecConfigDirectVpi_Type = VpiInteger
_LecConfigDirectVpi_Object = MibTableColumn
lecConfigDirectVpi = _LecConfigDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 2),
    _LecConfigDirectVpi_Type()
)
lecConfigDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectVpi.setStatus("current")
_LecConfigDirectVci_Type = VciInteger
_LecConfigDirectVci_Object = MibTableColumn
lecConfigDirectVci = _LecConfigDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 3),
    _LecConfigDirectVci_Type()
)
lecConfigDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecConfigDirectVci.setStatus("current")
_LecControlDirectInterface_Type = LeConnectionInterface
_LecControlDirectInterface_Object = MibTableColumn
lecControlDirectInterface = _LecControlDirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 4),
    _LecControlDirectInterface_Type()
)
lecControlDirectInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectInterface.setStatus("current")
_LecControlDirectVpi_Type = VpiInteger
_LecControlDirectVpi_Object = MibTableColumn
lecControlDirectVpi = _LecControlDirectVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 5),
    _LecControlDirectVpi_Type()
)
lecControlDirectVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectVpi.setStatus("current")
_LecControlDirectVci_Type = VciInteger
_LecControlDirectVci_Object = MibTableColumn
lecControlDirectVci = _LecControlDirectVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 6),
    _LecControlDirectVci_Type()
)
lecControlDirectVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDirectVci.setStatus("current")
_LecControlDistributeInterface_Type = LeConnectionInterface
_LecControlDistributeInterface_Object = MibTableColumn
lecControlDistributeInterface = _LecControlDistributeInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 7),
    _LecControlDistributeInterface_Type()
)
lecControlDistributeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeInterface.setStatus("current")
_LecControlDistributeVpi_Type = VpiInteger
_LecControlDistributeVpi_Object = MibTableColumn
lecControlDistributeVpi = _LecControlDistributeVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 8),
    _LecControlDistributeVpi_Type()
)
lecControlDistributeVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeVpi.setStatus("current")
_LecControlDistributeVci_Type = VciInteger
_LecControlDistributeVci_Object = MibTableColumn
lecControlDistributeVci = _LecControlDistributeVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 9),
    _LecControlDistributeVci_Type()
)
lecControlDistributeVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecControlDistributeVci.setStatus("current")
_LecMulticastSendInterface_Type = LeConnectionInterface
_LecMulticastSendInterface_Object = MibTableColumn
lecMulticastSendInterface = _LecMulticastSendInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 10),
    _LecMulticastSendInterface_Type()
)
lecMulticastSendInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendInterface.setStatus("current")
_LecMulticastSendVpi_Type = VpiInteger
_LecMulticastSendVpi_Object = MibTableColumn
lecMulticastSendVpi = _LecMulticastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 11),
    _LecMulticastSendVpi_Type()
)
lecMulticastSendVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendVpi.setStatus("current")
_LecMulticastSendVci_Type = VciInteger
_LecMulticastSendVci_Object = MibTableColumn
lecMulticastSendVci = _LecMulticastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 12),
    _LecMulticastSendVci_Type()
)
lecMulticastSendVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastSendVci.setStatus("current")
_LecMulticastForwardInterface_Type = LeConnectionInterface
_LecMulticastForwardInterface_Object = MibTableColumn
lecMulticastForwardInterface = _LecMulticastForwardInterface_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 13),
    _LecMulticastForwardInterface_Type()
)
lecMulticastForwardInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardInterface.setStatus("current")
_LecMulticastForwardVpi_Type = VpiInteger
_LecMulticastForwardVpi_Object = MibTableColumn
lecMulticastForwardVpi = _LecMulticastForwardVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 14),
    _LecMulticastForwardVpi_Type()
)
lecMulticastForwardVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardVpi.setStatus("current")
_LecMulticastForwardVci_Type = VciInteger
_LecMulticastForwardVci_Object = MibTableColumn
lecMulticastForwardVci = _LecMulticastForwardVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 5, 1, 15),
    _LecMulticastForwardVci_Type()
)
lecMulticastForwardVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMulticastForwardVci.setStatus("current")
_LecAtmAddressTable_Object = MibTable
lecAtmAddressTable = _LecAtmAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lecAtmAddressTable.setStatus("current")
_LecAtmAddressEntry_Object = MibTableRow
lecAtmAddressEntry = _LecAtmAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1)
)
lecAtmAddressEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecAtmAddress"),
)
if mibBuilder.loadTexts:
    lecAtmAddressEntry.setStatus("current")
_LecAtmAddress_Type = AtmLaneAddress
_LecAtmAddress_Object = MibTableColumn
lecAtmAddress = _LecAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1, 1),
    _LecAtmAddress_Type()
)
lecAtmAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecAtmAddress.setStatus("current")
_LecAtmAddressStatus_Type = RowStatus
_LecAtmAddressStatus_Object = MibTableColumn
lecAtmAddressStatus = _LecAtmAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 6, 1, 2),
    _LecAtmAddressStatus_Type()
)
lecAtmAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lecAtmAddressStatus.setStatus("current")
_LecMacAddressTable_Object = MibTable
lecMacAddressTable = _LecMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lecMacAddressTable.setStatus("current")
_LecMacAddressEntry_Object = MibTableRow
lecMacAddressEntry = _LecMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1)
)
lecMacAddressEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecMacAddress"),
)
if mibBuilder.loadTexts:
    lecMacAddressEntry.setStatus("current")
_LecMacAddress_Type = MacAddress
_LecMacAddress_Object = MibTableColumn
lecMacAddress = _LecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 1),
    _LecMacAddress_Type()
)
lecMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecMacAddress.setStatus("current")
_LecMacAddressAtmBinding_Type = AtmLaneAddress
_LecMacAddressAtmBinding_Object = MibTableColumn
lecMacAddressAtmBinding = _LecMacAddressAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 7, 1, 2),
    _LecMacAddressAtmBinding_Type()
)
lecMacAddressAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecMacAddressAtmBinding.setStatus("current")
_LecRouteDescrTable_Object = MibTable
lecRouteDescrTable = _LecRouteDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    lecRouteDescrTable.setStatus("current")
_LecRouteDescrEntry_Object = MibTableRow
lecRouteDescrEntry = _LecRouteDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1)
)
lecRouteDescrEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecRouteDescrSegmentID"),
    (0, "LAN-EMULATION-CLIENT-MIB", "lecRouteDescrBridgeNumber"),
)
if mibBuilder.loadTexts:
    lecRouteDescrEntry.setStatus("current")


class _LecRouteDescrSegmentID_Type(Integer32):
    """Custom type lecRouteDescrSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LecRouteDescrSegmentID_Type.__name__ = "Integer32"
_LecRouteDescrSegmentID_Object = MibTableColumn
lecRouteDescrSegmentID = _LecRouteDescrSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 1),
    _LecRouteDescrSegmentID_Type()
)
lecRouteDescrSegmentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecRouteDescrSegmentID.setStatus("current")


class _LecRouteDescrBridgeNumber_Type(Integer32):
    """Custom type lecRouteDescrBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LecRouteDescrBridgeNumber_Type.__name__ = "Integer32"
_LecRouteDescrBridgeNumber_Object = MibTableColumn
lecRouteDescrBridgeNumber = _LecRouteDescrBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 2),
    _LecRouteDescrBridgeNumber_Type()
)
lecRouteDescrBridgeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lecRouteDescrBridgeNumber.setStatus("current")
_LecRouteDescrAtmBinding_Type = AtmLaneAddress
_LecRouteDescrAtmBinding_Object = MibTableColumn
lecRouteDescrAtmBinding = _LecRouteDescrAtmBinding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 8, 1, 3),
    _LecRouteDescrAtmBinding_Type()
)
lecRouteDescrAtmBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lecRouteDescrAtmBinding.setStatus("current")
_LeArpTable_Object = MibTable
leArpTable = _LeArpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9)
)
if mibBuilder.loadTexts:
    leArpTable.setStatus("current")
_LeArpEntry_Object = MibTableRow
leArpEntry = _LeArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1)
)
leArpEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leArpMacAddress"),
)
if mibBuilder.loadTexts:
    leArpEntry.setStatus("current")
_LeArpMacAddress_Type = MacAddress
_LeArpMacAddress_Object = MibTableColumn
leArpMacAddress = _LeArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 1),
    _LeArpMacAddress_Type()
)
leArpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leArpMacAddress.setStatus("current")
_LeArpAtmAddress_Type = AtmLaneAddress
_LeArpAtmAddress_Object = MibTableColumn
leArpAtmAddress = _LeArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 2),
    _LeArpAtmAddress_Type()
)
leArpAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leArpAtmAddress.setStatus("current")
_LeArpIsRemoteAddress_Type = TruthValue
_LeArpIsRemoteAddress_Object = MibTableColumn
leArpIsRemoteAddress = _LeArpIsRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 3),
    _LeArpIsRemoteAddress_Type()
)
leArpIsRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leArpIsRemoteAddress.setStatus("current")


class _LeArpEntryType_Type(LeArpTableEntryType):
    """Custom type leArpEntryType based on LeArpTableEntryType"""


_LeArpEntryType_Object = MibTableColumn
leArpEntryType = _LeArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 4),
    _LeArpEntryType_Type()
)
leArpEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leArpEntryType.setStatus("current")
_LeArpRowStatus_Type = RowStatus
_LeArpRowStatus_Object = MibTableColumn
leArpRowStatus = _LeArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 9, 1, 5),
    _LeArpRowStatus_Type()
)
leArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leArpRowStatus.setStatus("current")
_LeRDArpTable_Object = MibTable
leRDArpTable = _LeRDArpTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    leRDArpTable.setStatus("current")
_LeRDArpEntry_Object = MibTableRow
leRDArpEntry = _LeRDArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1)
)
leRDArpEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leRDArpSegmentID"),
    (0, "LAN-EMULATION-CLIENT-MIB", "leRDArpBridgeNumber"),
)
if mibBuilder.loadTexts:
    leRDArpEntry.setStatus("current")


class _LeRDArpSegmentID_Type(Integer32):
    """Custom type leRDArpSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LeRDArpSegmentID_Type.__name__ = "Integer32"
_LeRDArpSegmentID_Object = MibTableColumn
leRDArpSegmentID = _LeRDArpSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 1),
    _LeRDArpSegmentID_Type()
)
leRDArpSegmentID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leRDArpSegmentID.setStatus("current")


class _LeRDArpBridgeNumber_Type(Integer32):
    """Custom type leRDArpBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LeRDArpBridgeNumber_Type.__name__ = "Integer32"
_LeRDArpBridgeNumber_Object = MibTableColumn
leRDArpBridgeNumber = _LeRDArpBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 2),
    _LeRDArpBridgeNumber_Type()
)
leRDArpBridgeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    leRDArpBridgeNumber.setStatus("current")
_LeRDArpAtmAddress_Type = AtmLaneAddress
_LeRDArpAtmAddress_Object = MibTableColumn
leRDArpAtmAddress = _LeRDArpAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 3),
    _LeRDArpAtmAddress_Type()
)
leRDArpAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leRDArpAtmAddress.setStatus("current")


class _LeRDArpEntryType_Type(LeArpTableEntryType):
    """Custom type leRDArpEntryType based on LeArpTableEntryType"""


_LeRDArpEntryType_Object = MibTableColumn
leRDArpEntryType = _LeRDArpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 4),
    _LeRDArpEntryType_Type()
)
leRDArpEntryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leRDArpEntryType.setStatus("current")
_LeRDArpRowStatus_Type = RowStatus
_LeRDArpRowStatus_Object = MibTableColumn
leRDArpRowStatus = _LeRDArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 1, 10, 1, 5),
    _LeRDArpRowStatus_Type()
)
leRDArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    leRDArpRowStatus.setStatus("current")
_LeClientMIBConformance_ObjectIdentity = ObjectIdentity
leClientMIBConformance = _LeClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2)
)
_LeClientMIBGroups_ObjectIdentity = ObjectIdentity
leClientMIBGroups = _LeClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1)
)
_LeClientMIBCompliances_ObjectIdentity = ObjectIdentity
leClientMIBCompliances = _LeClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 2)
)

# Managed Objects groups

leClientConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 1)
)
leClientConfigGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "lecRowStatus"),
        ("LAN-EMULATION-CLIENT-MIB", "lecOwner"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigMode"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigLanType"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigMaxDataFrameSize"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigLanName"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigLesAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlTimeout"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMaxUnknownFrameCount"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMaxUnknownFrameTime"),
        ("LAN-EMULATION-CLIENT-MIB", "lecVccTimeoutPeriod"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMaxRetryCount"),
        ("LAN-EMULATION-CLIENT-MIB", "lecAgingTime"),
        ("LAN-EMULATION-CLIENT-MIB", "lecForwardDelayTime"),
        ("LAN-EMULATION-CLIENT-MIB", "lecExpectedArpResponseTime"),
        ("LAN-EMULATION-CLIENT-MIB", "lecFlushTimeOut"),
        ("LAN-EMULATION-CLIENT-MIB", "lecPathSwitchingDelay"),
        ("LAN-EMULATION-CLIENT-MIB", "lecLocalSegmentID"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendType"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendAvgRate"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendPeakRate"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConnectionCompleteTimer"))
)
if mibBuilder.loadTexts:
    leClientConfigGroup.setStatus("current")

leClientStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 2)
)
leClientStatusGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "lecIfIndex"),
        ("LAN-EMULATION-CLIENT-MIB", "lecPrimaryAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "lecID"),
        ("LAN-EMULATION-CLIENT-MIB", "lecInterfaceState"),
        ("LAN-EMULATION-CLIENT-MIB", "lecLastFailureRespCode"),
        ("LAN-EMULATION-CLIENT-MIB", "lecLastFailureState"),
        ("LAN-EMULATION-CLIENT-MIB", "lecProtocol"),
        ("LAN-EMULATION-CLIENT-MIB", "lecVersion"),
        ("LAN-EMULATION-CLIENT-MIB", "lecTopologyChange"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigServerAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigSource"),
        ("LAN-EMULATION-CLIENT-MIB", "lecActualLanType"),
        ("LAN-EMULATION-CLIENT-MIB", "lecActualMaxDataFrameSize"),
        ("LAN-EMULATION-CLIENT-MIB", "lecActualLanName"),
        ("LAN-EMULATION-CLIENT-MIB", "lecActualLesAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "lecProxyClient"))
)
if mibBuilder.loadTexts:
    leClientStatusGroup.setStatus("current")

leClientMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 3)
)
leClientMappingGroup.setObjects(
    ("LAN-EMULATION-CLIENT-MIB", "lecMappingIndex")
)
if mibBuilder.loadTexts:
    leClientMappingGroup.setStatus("current")

leClientStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 4)
)
leClientStatisticsGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "lecArpRequestsOut"),
        ("LAN-EMULATION-CLIENT-MIB", "lecArpRequestsIn"),
        ("LAN-EMULATION-CLIENT-MIB", "lecArpRepliesOut"),
        ("LAN-EMULATION-CLIENT-MIB", "lecArpRepliesIn"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlFramesOut"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlFramesIn"),
        ("LAN-EMULATION-CLIENT-MIB", "lecSvcFailures"))
)
if mibBuilder.loadTexts:
    leClientStatisticsGroup.setStatus("current")

leClientServerVccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 5)
)
leClientServerVccGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "lecConfigDirectInterface"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigDirectVpi"),
        ("LAN-EMULATION-CLIENT-MIB", "lecConfigDirectVci"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDirectInterface"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDirectVpi"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDirectVci"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDistributeInterface"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDistributeVpi"),
        ("LAN-EMULATION-CLIENT-MIB", "lecControlDistributeVci"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendInterface"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendVpi"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastSendVci"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastForwardInterface"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastForwardVpi"),
        ("LAN-EMULATION-CLIENT-MIB", "lecMulticastForwardVci"))
)
if mibBuilder.loadTexts:
    leClientServerVccGroup.setStatus("current")

leClientAtmAddressesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 6)
)
leClientAtmAddressesGroup.setObjects(
    ("LAN-EMULATION-CLIENT-MIB", "lecAtmAddressStatus")
)
if mibBuilder.loadTexts:
    leClientAtmAddressesGroup.setStatus("current")

leClientMacAddressesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 7)
)
leClientMacAddressesGroup.setObjects(
    ("LAN-EMULATION-CLIENT-MIB", "lecMacAddressAtmBinding")
)
if mibBuilder.loadTexts:
    leClientMacAddressesGroup.setStatus("current")

leClientRouteDescriptorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 8)
)
leClientRouteDescriptorsGroup.setObjects(
    ("LAN-EMULATION-CLIENT-MIB", "lecRouteDescrAtmBinding")
)
if mibBuilder.loadTexts:
    leClientRouteDescriptorsGroup.setStatus("current")

leClientArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 9)
)
leClientArpGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "leArpAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "leArpIsRemoteAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "leArpEntryType"),
        ("LAN-EMULATION-CLIENT-MIB", "leArpRowStatus"))
)
if mibBuilder.loadTexts:
    leClientArpGroup.setStatus("current")

leClientRDArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 1, 10)
)
leClientRDArpGroup.setObjects(
      *(("LAN-EMULATION-CLIENT-MIB", "leRDArpAtmAddress"),
        ("LAN-EMULATION-CLIENT-MIB", "leRDArpEntryType"),
        ("LAN-EMULATION-CLIENT-MIB", "leRDArpRowStatus"))
)
if mibBuilder.loadTexts:
    leClientRDArpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

leClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    leClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    **{"OwnerString": OwnerString,
       "AtmLaneAddress": AtmLaneAddress,
       "VpiInteger": VpiInteger,
       "VciInteger": VciInteger,
       "LeConnectionInterface": LeConnectionInterface,
       "LecState": LecState,
       "LecDataFrameFormat": LecDataFrameFormat,
       "LecDataFrameSize": LecDataFrameSize,
       "LeArpTableEntryType": LeArpTableEntryType,
       "atmfLanEmulation": atmfLanEmulation,
       "leClientMIB": leClientMIB,
       "leClientMIBObjects": leClientMIBObjects,
       "lecConfigTable": lecConfigTable,
       "lecConfigEntry": lecConfigEntry,
       "lecIndex": lecIndex,
       "lecRowStatus": lecRowStatus,
       "lecOwner": lecOwner,
       "lecConfigMode": lecConfigMode,
       "lecConfigLanType": lecConfigLanType,
       "lecConfigMaxDataFrameSize": lecConfigMaxDataFrameSize,
       "lecConfigLanName": lecConfigLanName,
       "lecConfigLesAtmAddress": lecConfigLesAtmAddress,
       "lecControlTimeout": lecControlTimeout,
       "lecMaxUnknownFrameCount": lecMaxUnknownFrameCount,
       "lecMaxUnknownFrameTime": lecMaxUnknownFrameTime,
       "lecVccTimeoutPeriod": lecVccTimeoutPeriod,
       "lecMaxRetryCount": lecMaxRetryCount,
       "lecAgingTime": lecAgingTime,
       "lecForwardDelayTime": lecForwardDelayTime,
       "lecExpectedArpResponseTime": lecExpectedArpResponseTime,
       "lecFlushTimeOut": lecFlushTimeOut,
       "lecPathSwitchingDelay": lecPathSwitchingDelay,
       "lecLocalSegmentID": lecLocalSegmentID,
       "lecMulticastSendType": lecMulticastSendType,
       "lecMulticastSendAvgRate": lecMulticastSendAvgRate,
       "lecMulticastSendPeakRate": lecMulticastSendPeakRate,
       "lecConnectionCompleteTimer": lecConnectionCompleteTimer,
       "lecStatusTable": lecStatusTable,
       "lecStatusEntry": lecStatusEntry,
       "lecIfIndex": lecIfIndex,
       "lecPrimaryAtmAddress": lecPrimaryAtmAddress,
       "lecID": lecID,
       "lecInterfaceState": lecInterfaceState,
       "lecLastFailureRespCode": lecLastFailureRespCode,
       "lecLastFailureState": lecLastFailureState,
       "lecProtocol": lecProtocol,
       "lecVersion": lecVersion,
       "lecTopologyChange": lecTopologyChange,
       "lecConfigServerAtmAddress": lecConfigServerAtmAddress,
       "lecConfigSource": lecConfigSource,
       "lecActualLanType": lecActualLanType,
       "lecActualMaxDataFrameSize": lecActualMaxDataFrameSize,
       "lecActualLanName": lecActualLanName,
       "lecActualLesAtmAddress": lecActualLesAtmAddress,
       "lecProxyClient": lecProxyClient,
       "lecMappingTable": lecMappingTable,
       "lecMappingEntry": lecMappingEntry,
       "lecMappingIndex": lecMappingIndex,
       "lecStatisticsTable": lecStatisticsTable,
       "lecStatisticsEntry": lecStatisticsEntry,
       "lecArpRequestsOut": lecArpRequestsOut,
       "lecArpRequestsIn": lecArpRequestsIn,
       "lecArpRepliesOut": lecArpRepliesOut,
       "lecArpRepliesIn": lecArpRepliesIn,
       "lecControlFramesOut": lecControlFramesOut,
       "lecControlFramesIn": lecControlFramesIn,
       "lecSvcFailures": lecSvcFailures,
       "lecServerVccTable": lecServerVccTable,
       "lecServerVccEntry": lecServerVccEntry,
       "lecConfigDirectInterface": lecConfigDirectInterface,
       "lecConfigDirectVpi": lecConfigDirectVpi,
       "lecConfigDirectVci": lecConfigDirectVci,
       "lecControlDirectInterface": lecControlDirectInterface,
       "lecControlDirectVpi": lecControlDirectVpi,
       "lecControlDirectVci": lecControlDirectVci,
       "lecControlDistributeInterface": lecControlDistributeInterface,
       "lecControlDistributeVpi": lecControlDistributeVpi,
       "lecControlDistributeVci": lecControlDistributeVci,
       "lecMulticastSendInterface": lecMulticastSendInterface,
       "lecMulticastSendVpi": lecMulticastSendVpi,
       "lecMulticastSendVci": lecMulticastSendVci,
       "lecMulticastForwardInterface": lecMulticastForwardInterface,
       "lecMulticastForwardVpi": lecMulticastForwardVpi,
       "lecMulticastForwardVci": lecMulticastForwardVci,
       "lecAtmAddressTable": lecAtmAddressTable,
       "lecAtmAddressEntry": lecAtmAddressEntry,
       "lecAtmAddress": lecAtmAddress,
       "lecAtmAddressStatus": lecAtmAddressStatus,
       "lecMacAddressTable": lecMacAddressTable,
       "lecMacAddressEntry": lecMacAddressEntry,
       "lecMacAddress": lecMacAddress,
       "lecMacAddressAtmBinding": lecMacAddressAtmBinding,
       "lecRouteDescrTable": lecRouteDescrTable,
       "lecRouteDescrEntry": lecRouteDescrEntry,
       "lecRouteDescrSegmentID": lecRouteDescrSegmentID,
       "lecRouteDescrBridgeNumber": lecRouteDescrBridgeNumber,
       "lecRouteDescrAtmBinding": lecRouteDescrAtmBinding,
       "leArpTable": leArpTable,
       "leArpEntry": leArpEntry,
       "leArpMacAddress": leArpMacAddress,
       "leArpAtmAddress": leArpAtmAddress,
       "leArpIsRemoteAddress": leArpIsRemoteAddress,
       "leArpEntryType": leArpEntryType,
       "leArpRowStatus": leArpRowStatus,
       "leRDArpTable": leRDArpTable,
       "leRDArpEntry": leRDArpEntry,
       "leRDArpSegmentID": leRDArpSegmentID,
       "leRDArpBridgeNumber": leRDArpBridgeNumber,
       "leRDArpAtmAddress": leRDArpAtmAddress,
       "leRDArpEntryType": leRDArpEntryType,
       "leRDArpRowStatus": leRDArpRowStatus,
       "leClientMIBConformance": leClientMIBConformance,
       "leClientMIBGroups": leClientMIBGroups,
       "leClientConfigGroup": leClientConfigGroup,
       "leClientStatusGroup": leClientStatusGroup,
       "leClientMappingGroup": leClientMappingGroup,
       "leClientStatisticsGroup": leClientStatisticsGroup,
       "leClientServerVccGroup": leClientServerVccGroup,
       "leClientAtmAddressesGroup": leClientAtmAddressesGroup,
       "leClientMacAddressesGroup": leClientMacAddressesGroup,
       "leClientRouteDescriptorsGroup": leClientRouteDescriptorsGroup,
       "leClientArpGroup": leClientArpGroup,
       "leClientRDArpGroup": leClientRDArpGroup,
       "leClientMIBCompliances": leClientMIBCompliances,
       "leClientMIBCompliance": leClientMIBCompliance}
)
