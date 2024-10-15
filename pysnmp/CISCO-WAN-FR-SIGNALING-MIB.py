# SNMP MIB module (CISCO-WAN-FR-SIGNALING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-SIGNALING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:05 2024
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

(frPortCnfSig,
 frPortCntSig) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frPortCnfSig",
    "frPortCntSig")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanFrSignalingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 46)
)
ciscoWanFrSignalingMIB.setRevisions(
        ("2003-03-24 00:00",
         "2002-09-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrPortCnfSigLMIGrp_ObjectIdentity = ObjectIdentity
frPortCnfSigLMIGrp = _FrPortCnfSigLMIGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1)
)
_FrPortCnfSigLMIGrpTable_Object = MibTable
frPortCnfSigLMIGrpTable = _FrPortCnfSigLMIGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frPortCnfSigLMIGrpTable.setStatus("current")
_FrPortCnfSigLMIGrpEntry_Object = MibTableRow
frPortCnfSigLMIGrpEntry = _FrPortCnfSigLMIGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1)
)
frPortCnfSigLMIGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-SIGNALING-MIB", "lmiCnfPortNum"),
)
if mibBuilder.loadTexts:
    frPortCnfSigLMIGrpEntry.setStatus("current")


class _LmiCnfPortNum_Type(Integer32):
    """Custom type lmiCnfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LmiCnfPortNum_Type.__name__ = "Integer32"
_LmiCnfPortNum_Object = MibTableColumn
lmiCnfPortNum = _LmiCnfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 1),
    _LmiCnfPortNum_Type()
)
lmiCnfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmiCnfPortNum.setStatus("current")


class _SignallingProtocolType_Type(Integer32):
    """Custom type signallingProtocolType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("annexANNI", 6),
          ("annexAUNI", 4),
          ("annexDNNI", 7),
          ("annexDUNI", 5),
          ("noSignalling", 2),
          ("other", 1),
          ("strataLMI", 3))
    )


_SignallingProtocolType_Type.__name__ = "Integer32"
_SignallingProtocolType_Object = MibTableColumn
signallingProtocolType = _SignallingProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 2),
    _SignallingProtocolType_Type()
)
signallingProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signallingProtocolType.setStatus("current")


class _AsynchronousUpdates_Type(Integer32):
    """Custom type asynchronousUpdates based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("fsenable", 3),
          ("updfsenable", 4))
    )


_AsynchronousUpdates_Type.__name__ = "Integer32"
_AsynchronousUpdates_Object = MibTableColumn
asynchronousUpdates = _AsynchronousUpdates_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 3),
    _AsynchronousUpdates_Type()
)
asynchronousUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asynchronousUpdates.setStatus("current")


class _T391LinkIntegrityTimer_Type(Integer32):
    """Custom type t391LinkIntegrityTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T391LinkIntegrityTimer_Type.__name__ = "Integer32"
_T391LinkIntegrityTimer_Object = MibTableColumn
t391LinkIntegrityTimer = _T391LinkIntegrityTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 4),
    _T391LinkIntegrityTimer_Type()
)
t391LinkIntegrityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t391LinkIntegrityTimer.setStatus("current")
if mibBuilder.loadTexts:
    t391LinkIntegrityTimer.setUnits("seconds")


class _T392PollingVerificationTimer_Type(Integer32):
    """Custom type t392PollingVerificationTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T392PollingVerificationTimer_Type.__name__ = "Integer32"
_T392PollingVerificationTimer_Object = MibTableColumn
t392PollingVerificationTimer = _T392PollingVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 5),
    _T392PollingVerificationTimer_Type()
)
t392PollingVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t392PollingVerificationTimer.setStatus("current")
if mibBuilder.loadTexts:
    t392PollingVerificationTimer.setUnits("seconds")


class _N391FullStatusPollingCounter_Type(Integer32):
    """Custom type n391FullStatusPollingCounter based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_N391FullStatusPollingCounter_Type.__name__ = "Integer32"
_N391FullStatusPollingCounter_Object = MibTableColumn
n391FullStatusPollingCounter = _N391FullStatusPollingCounter_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 6),
    _N391FullStatusPollingCounter_Type()
)
n391FullStatusPollingCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n391FullStatusPollingCounter.setStatus("current")
if mibBuilder.loadTexts:
    n391FullStatusPollingCounter.setUnits("Polls")


class _N392ErrorThreshold_Type(Integer32):
    """Custom type n392ErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N392ErrorThreshold_Type.__name__ = "Integer32"
_N392ErrorThreshold_Object = MibTableColumn
n392ErrorThreshold = _N392ErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 7),
    _N392ErrorThreshold_Type()
)
n392ErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n392ErrorThreshold.setStatus("current")


class _N393MonitoredEventCount_Type(Integer32):
    """Custom type n393MonitoredEventCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_N393MonitoredEventCount_Type.__name__ = "Integer32"
_N393MonitoredEventCount_Object = MibTableColumn
n393MonitoredEventCount = _N393MonitoredEventCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 8),
    _N393MonitoredEventCount_Type()
)
n393MonitoredEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    n393MonitoredEventCount.setStatus("current")
if mibBuilder.loadTexts:
    n393MonitoredEventCount.setUnits("Events")


class _EnhancedLmi_Type(Integer32):
    """Custom type enhancedLmi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnhancedLmi_Type.__name__ = "Integer32"
_EnhancedLmi_Object = MibTableColumn
enhancedLmi = _EnhancedLmi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 9),
    _EnhancedLmi_Type()
)
enhancedLmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enhancedLmi.setStatus("current")


class _PortFRF1Dot2Support_Type(Integer32):
    """Custom type portFRF1Dot2Support based on Integer32"""
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


_PortFRF1Dot2Support_Type.__name__ = "Integer32"
_PortFRF1Dot2Support_Object = MibTableColumn
portFRF1Dot2Support = _PortFRF1Dot2Support_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 10),
    _PortFRF1Dot2Support_Type()
)
portFRF1Dot2Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFRF1Dot2Support.setStatus("current")


class _PortLmiSigConfMethod_Type(Integer32):
    """Custom type portLmiSigConfMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autosense", 2),
          ("manual", 1))
    )


_PortLmiSigConfMethod_Type.__name__ = "Integer32"
_PortLmiSigConfMethod_Object = MibTableColumn
portLmiSigConfMethod = _PortLmiSigConfMethod_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 1, 1, 1, 11),
    _PortLmiSigConfMethod_Type()
)
portLmiSigConfMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLmiSigConfMethod.setStatus("current")
_FrPortCnfSigCLLMGrp_ObjectIdentity = ObjectIdentity
frPortCnfSigCLLMGrp = _FrPortCnfSigCLLMGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2)
)
_FrPortCnfSigCLLMGrpTable_Object = MibTable
frPortCnfSigCLLMGrpTable = _FrPortCnfSigCLLMGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    frPortCnfSigCLLMGrpTable.setStatus("current")
_FrPortCnfSigCLLMGrpEntry_Object = MibTableRow
frPortCnfSigCLLMGrpEntry = _FrPortCnfSigCLLMGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1, 1)
)
frPortCnfSigCLLMGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-SIGNALING-MIB", "cllmCnfPortNum"),
)
if mibBuilder.loadTexts:
    frPortCnfSigCLLMGrpEntry.setStatus("current")


class _CllmCnfPortNum_Type(Integer32):
    """Custom type cllmCnfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CllmCnfPortNum_Type.__name__ = "Integer32"
_CllmCnfPortNum_Object = MibTableColumn
cllmCnfPortNum = _CllmCnfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1, 1, 1),
    _CllmCnfPortNum_Type()
)
cllmCnfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cllmCnfPortNum.setStatus("current")


class _CllmEnable_Type(Integer32):
    """Custom type cllmEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CllmEnable_Type.__name__ = "Integer32"
_CllmEnable_Object = MibTableColumn
cllmEnable = _CllmEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1, 1, 2),
    _CllmEnable_Type()
)
cllmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllmEnable.setStatus("current")


class _XmtCLLMStatusTimer_Type(Integer32):
    """Custom type xmtCLLMStatusTimer based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 5000),
    )


_XmtCLLMStatusTimer_Type.__name__ = "Integer32"
_XmtCLLMStatusTimer_Object = MibTableColumn
xmtCLLMStatusTimer = _XmtCLLMStatusTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1, 1, 3),
    _XmtCLLMStatusTimer_Type()
)
xmtCLLMStatusTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xmtCLLMStatusTimer.setStatus("current")
if mibBuilder.loadTexts:
    xmtCLLMStatusTimer.setUnits("milli-seconds")


class _RcvCLLMStatusTimer_Type(Integer32):
    """Custom type rcvCLLMStatusTimer based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1000
        )
    )
    namedValues = NamedValues(
        ("rcvCLLMTimerValue", 1000)
    )


_RcvCLLMStatusTimer_Type.__name__ = "Integer32"
_RcvCLLMStatusTimer_Object = MibTableColumn
rcvCLLMStatusTimer = _RcvCLLMStatusTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 1, 2, 2, 1, 1, 4),
    _RcvCLLMStatusTimer_Type()
)
rcvCLLMStatusTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvCLLMStatusTimer.setStatus("current")
_FrPortCntSigLMIGrp_ObjectIdentity = ObjectIdentity
frPortCntSigLMIGrp = _FrPortCntSigLMIGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1)
)
_FrPortCntSigLMIGrpTable_Object = MibTable
frPortCntSigLMIGrpTable = _FrPortCntSigLMIGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frPortCntSigLMIGrpTable.setStatus("current")
_FrPortCntSigLMIGrpEntry_Object = MibTableRow
frPortCntSigLMIGrpEntry = _FrPortCntSigLMIGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1)
)
frPortCntSigLMIGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-SIGNALING-MIB", "lmiSigPortNum"),
)
if mibBuilder.loadTexts:
    frPortCntSigLMIGrpEntry.setStatus("current")


class _LmiSigPortNum_Type(Integer32):
    """Custom type lmiSigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LmiSigPortNum_Type.__name__ = "Integer32"
_LmiSigPortNum_Object = MibTableColumn
lmiSigPortNum = _LmiSigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 1),
    _LmiSigPortNum_Type()
)
lmiSigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmiSigPortNum.setStatus("current")
_RcvStatusInquiry_Type = Counter32
_RcvStatusInquiry_Object = MibTableColumn
rcvStatusInquiry = _RcvStatusInquiry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 2),
    _RcvStatusInquiry_Type()
)
rcvStatusInquiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvStatusInquiry.setStatus("current")
_RcvInvalidRequest_Type = Counter32
_RcvInvalidRequest_Object = MibTableColumn
rcvInvalidRequest = _RcvInvalidRequest_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 3),
    _RcvInvalidRequest_Type()
)
rcvInvalidRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvInvalidRequest.setStatus("current")
_RcvUNISeqMismatch_Type = Counter32
_RcvUNISeqMismatch_Object = MibTableColumn
rcvUNISeqMismatch = _RcvUNISeqMismatch_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 4),
    _RcvUNISeqMismatch_Type()
)
rcvUNISeqMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvUNISeqMismatch.setStatus("current")
_XmtStatus_Type = Counter32
_XmtStatus_Object = MibTableColumn
xmtStatus = _XmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 5),
    _XmtStatus_Type()
)
xmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtStatus.setStatus("current")
_XmtAsynchUpdate_Type = Counter32
_XmtAsynchUpdate_Object = MibTableColumn
xmtAsynchUpdate = _XmtAsynchUpdate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 6),
    _XmtAsynchUpdate_Type()
)
xmtAsynchUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtAsynchUpdate.setStatus("current")
_UniSignalingTimeout_Type = Counter32
_UniSignalingTimeout_Object = MibTableColumn
uniSignalingTimeout = _UniSignalingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 7),
    _UniSignalingTimeout_Type()
)
uniSignalingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniSignalingTimeout.setStatus("current")
_XmtStatusInquiry_Type = Counter32
_XmtStatusInquiry_Object = MibTableColumn
xmtStatusInquiry = _XmtStatusInquiry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 8),
    _XmtStatusInquiry_Type()
)
xmtStatusInquiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtStatusInquiry.setStatus("current")
_RcvStatus_Type = Counter32
_RcvStatus_Object = MibTableColumn
rcvStatus = _RcvStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 9),
    _RcvStatus_Type()
)
rcvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvStatus.setStatus("current")
_RcvAsynchUpdate_Type = Counter32
_RcvAsynchUpdate_Object = MibTableColumn
rcvAsynchUpdate = _RcvAsynchUpdate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 10),
    _RcvAsynchUpdate_Type()
)
rcvAsynchUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvAsynchUpdate.setStatus("current")
_RcvNNISeqMismatch_Type = Counter32
_RcvNNISeqMismatch_Object = MibTableColumn
rcvNNISeqMismatch = _RcvNNISeqMismatch_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 11),
    _RcvNNISeqMismatch_Type()
)
rcvNNISeqMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvNNISeqMismatch.setStatus("current")
_NniSignalingTimeout_Type = Counter32
_NniSignalingTimeout_Object = MibTableColumn
nniSignalingTimeout = _NniSignalingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 1, 1, 1, 12),
    _NniSignalingTimeout_Type()
)
nniSignalingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nniSignalingTimeout.setStatus("current")
_FrPortCntSigCLLMGrp_ObjectIdentity = ObjectIdentity
frPortCntSigCLLMGrp = _FrPortCntSigCLLMGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2)
)
_FrPortCntSigCLLMGrpTable_Object = MibTable
frPortCntSigCLLMGrpTable = _FrPortCntSigCLLMGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    frPortCntSigCLLMGrpTable.setStatus("current")
_FrPortCntSigCLLMGrpEntry_Object = MibTableRow
frPortCntSigCLLMGrpEntry = _FrPortCntSigCLLMGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1)
)
frPortCntSigCLLMGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-SIGNALING-MIB", "cllmSigPortNum"),
)
if mibBuilder.loadTexts:
    frPortCntSigCLLMGrpEntry.setStatus("current")


class _CllmSigPortNum_Type(Integer32):
    """Custom type cllmSigPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CllmSigPortNum_Type.__name__ = "Integer32"
_CllmSigPortNum_Object = MibTableColumn
cllmSigPortNum = _CllmSigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 1),
    _CllmSigPortNum_Type()
)
cllmSigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cllmSigPortNum.setStatus("current")
_RcvFramesCLLM_Type = Counter32
_RcvFramesCLLM_Object = MibTableColumn
rcvFramesCLLM = _RcvFramesCLLM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 2),
    _RcvFramesCLLM_Type()
)
rcvFramesCLLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFramesCLLM.setStatus("current")
if mibBuilder.loadTexts:
    rcvFramesCLLM.setUnits("frames")
_RcvBytesCLLM_Type = Counter32
_RcvBytesCLLM_Object = MibTableColumn
rcvBytesCLLM = _RcvBytesCLLM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 3),
    _RcvBytesCLLM_Type()
)
rcvBytesCLLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvBytesCLLM.setStatus("current")
if mibBuilder.loadTexts:
    rcvBytesCLLM.setUnits("bytes")
_XmtFramesCLLM_Type = Counter32
_XmtFramesCLLM_Object = MibTableColumn
xmtFramesCLLM = _XmtFramesCLLM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 4),
    _XmtFramesCLLM_Type()
)
xmtFramesCLLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtFramesCLLM.setStatus("current")
if mibBuilder.loadTexts:
    xmtFramesCLLM.setUnits("frames")
_XmtBytesCLLM_Type = Counter32
_XmtBytesCLLM_Object = MibTableColumn
xmtBytesCLLM = _XmtBytesCLLM_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 5),
    _XmtBytesCLLM_Type()
)
xmtBytesCLLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtBytesCLLM.setStatus("current")
if mibBuilder.loadTexts:
    xmtBytesCLLM.setUnits("bytes")
_CllmFailures_Type = Counter32
_CllmFailures_Object = MibTableColumn
cllmFailures = _CllmFailures_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 1, 2, 2, 2, 1, 1, 6),
    _CllmFailures_Type()
)
cllmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cllmFailures.setStatus("current")
_CwfSignalingMIBConformance_ObjectIdentity = ObjectIdentity
cwfSignalingMIBConformance = _CwfSignalingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2)
)
_CwfSignalingMIBGroups_ObjectIdentity = ObjectIdentity
cwfSignalingMIBGroups = _CwfSignalingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 1)
)
_CwfSignalingMIBCompliances_ObjectIdentity = ObjectIdentity
cwfSignalingMIBCompliances = _CwfSignalingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 2)
)

# Managed Objects groups

ciscoWanFrLmiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 1, 1)
)
ciscoWanFrLmiConfigGroup.setObjects(
      *(("CISCO-WAN-FR-SIGNALING-MIB", "lmiCnfPortNum"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "signallingProtocolType"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "asynchronousUpdates"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "t391LinkIntegrityTimer"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "t392PollingVerificationTimer"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "n391FullStatusPollingCounter"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "n392ErrorThreshold"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "n393MonitoredEventCount"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "enhancedLmi"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "portFRF1Dot2Support"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "portLmiSigConfMethod"))
)
if mibBuilder.loadTexts:
    ciscoWanFrLmiConfigGroup.setStatus("current")

ciscoWanFrLmiStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 1, 2)
)
ciscoWanFrLmiStatsGroup.setObjects(
      *(("CISCO-WAN-FR-SIGNALING-MIB", "lmiSigPortNum"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvStatusInquiry"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvInvalidRequest"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvUNISeqMismatch"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtStatus"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtAsynchUpdate"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "uniSignalingTimeout"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtStatusInquiry"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvStatus"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvAsynchUpdate"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvNNISeqMismatch"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "nniSignalingTimeout"))
)
if mibBuilder.loadTexts:
    ciscoWanFrLmiStatsGroup.setStatus("current")

ciscoWanFrCllmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 1, 3)
)
ciscoWanFrCllmGroup.setObjects(
      *(("CISCO-WAN-FR-SIGNALING-MIB", "cllmCnfPortNum"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "cllmEnable"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtCLLMStatusTimer"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvCLLMStatusTimer"))
)
if mibBuilder.loadTexts:
    ciscoWanFrCllmGroup.setStatus("current")

ciscoWanFrCllmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 1, 4)
)
ciscoWanFrCllmStatsGroup.setObjects(
      *(("CISCO-WAN-FR-SIGNALING-MIB", "cllmSigPortNum"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvFramesCLLM"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "rcvBytesCLLM"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtFramesCLLM"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "xmtBytesCLLM"),
        ("CISCO-WAN-FR-SIGNALING-MIB", "cllmFailures"))
)
if mibBuilder.loadTexts:
    ciscoWanFrCllmStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwfSignalingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 46, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwfSignalingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-SIGNALING-MIB",
    **{"frPortCnfSigLMIGrp": frPortCnfSigLMIGrp,
       "frPortCnfSigLMIGrpTable": frPortCnfSigLMIGrpTable,
       "frPortCnfSigLMIGrpEntry": frPortCnfSigLMIGrpEntry,
       "lmiCnfPortNum": lmiCnfPortNum,
       "signallingProtocolType": signallingProtocolType,
       "asynchronousUpdates": asynchronousUpdates,
       "t391LinkIntegrityTimer": t391LinkIntegrityTimer,
       "t392PollingVerificationTimer": t392PollingVerificationTimer,
       "n391FullStatusPollingCounter": n391FullStatusPollingCounter,
       "n392ErrorThreshold": n392ErrorThreshold,
       "n393MonitoredEventCount": n393MonitoredEventCount,
       "enhancedLmi": enhancedLmi,
       "portFRF1Dot2Support": portFRF1Dot2Support,
       "portLmiSigConfMethod": portLmiSigConfMethod,
       "frPortCnfSigCLLMGrp": frPortCnfSigCLLMGrp,
       "frPortCnfSigCLLMGrpTable": frPortCnfSigCLLMGrpTable,
       "frPortCnfSigCLLMGrpEntry": frPortCnfSigCLLMGrpEntry,
       "cllmCnfPortNum": cllmCnfPortNum,
       "cllmEnable": cllmEnable,
       "xmtCLLMStatusTimer": xmtCLLMStatusTimer,
       "rcvCLLMStatusTimer": rcvCLLMStatusTimer,
       "frPortCntSigLMIGrp": frPortCntSigLMIGrp,
       "frPortCntSigLMIGrpTable": frPortCntSigLMIGrpTable,
       "frPortCntSigLMIGrpEntry": frPortCntSigLMIGrpEntry,
       "lmiSigPortNum": lmiSigPortNum,
       "rcvStatusInquiry": rcvStatusInquiry,
       "rcvInvalidRequest": rcvInvalidRequest,
       "rcvUNISeqMismatch": rcvUNISeqMismatch,
       "xmtStatus": xmtStatus,
       "xmtAsynchUpdate": xmtAsynchUpdate,
       "uniSignalingTimeout": uniSignalingTimeout,
       "xmtStatusInquiry": xmtStatusInquiry,
       "rcvStatus": rcvStatus,
       "rcvAsynchUpdate": rcvAsynchUpdate,
       "rcvNNISeqMismatch": rcvNNISeqMismatch,
       "nniSignalingTimeout": nniSignalingTimeout,
       "frPortCntSigCLLMGrp": frPortCntSigCLLMGrp,
       "frPortCntSigCLLMGrpTable": frPortCntSigCLLMGrpTable,
       "frPortCntSigCLLMGrpEntry": frPortCntSigCLLMGrpEntry,
       "cllmSigPortNum": cllmSigPortNum,
       "rcvFramesCLLM": rcvFramesCLLM,
       "rcvBytesCLLM": rcvBytesCLLM,
       "xmtFramesCLLM": xmtFramesCLLM,
       "xmtBytesCLLM": xmtBytesCLLM,
       "cllmFailures": cllmFailures,
       "ciscoWanFrSignalingMIB": ciscoWanFrSignalingMIB,
       "cwfSignalingMIBConformance": cwfSignalingMIBConformance,
       "cwfSignalingMIBGroups": cwfSignalingMIBGroups,
       "ciscoWanFrLmiConfigGroup": ciscoWanFrLmiConfigGroup,
       "ciscoWanFrLmiStatsGroup": ciscoWanFrLmiStatsGroup,
       "ciscoWanFrCllmGroup": ciscoWanFrCllmGroup,
       "ciscoWanFrCllmStatsGroup": ciscoWanFrCllmStatsGroup,
       "cwfSignalingMIBCompliances": cwfSignalingMIBCompliances,
       "cwfSignalingMIBCompliance": cwfSignalingMIBCompliance}
)
