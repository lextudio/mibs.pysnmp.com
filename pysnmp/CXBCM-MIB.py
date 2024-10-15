# SNMP MIB module (CXBCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXBCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:07 2024
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
 SapIndex,
 cxBCM) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxBCM")

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
 NotificationType,
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
    "NotificationType",
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



class LSapIndex(Integer32):
    """Custom type LSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )





class CHIndex(Integer32):
    """Custom type CHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _BcmTraps_Type(Integer32):
    """Custom type bcmTraps based on Integer32"""
    defaultValue = 1

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


_BcmTraps_Type.__name__ = "Integer32"
_BcmTraps_Object = MibScalar
bcmTraps = _BcmTraps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 1),
    _BcmTraps_Type()
)
bcmTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmTraps.setStatus("obsolete")


class _BcmCallHistoryTraps_Type(Integer32):
    """Custom type bcmCallHistoryTraps based on Integer32"""
    defaultValue = 1

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


_BcmCallHistoryTraps_Type.__name__ = "Integer32"
_BcmCallHistoryTraps_Object = MibScalar
bcmCallHistoryTraps = _BcmCallHistoryTraps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 2),
    _BcmCallHistoryTraps_Type()
)
bcmCallHistoryTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmCallHistoryTraps.setStatus("mandatory")
_BcmSoftwareVersion_Type = DisplayString
_BcmSoftwareVersion_Object = MibScalar
bcmSoftwareVersion = _BcmSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 3),
    _BcmSoftwareVersion_Type()
)
bcmSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmSoftwareVersion.setStatus("mandatory")


class _BcmMibLevel_Type(Integer32):
    """Custom type bcmMibLevel based on Integer32"""
    defaultValue = 2


_BcmMibLevel_Object = MibScalar
bcmMibLevel = _BcmMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 4),
    _BcmMibLevel_Type()
)
bcmMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmMibLevel.setStatus("mandatory")


class _BcmModuleState_Type(Integer32):
    """Custom type bcmModuleState based on Integer32"""
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
        *(("initializing", 2),
          ("operational", 4),
          ("registering", 3),
          ("uninitialized", 1))
    )


_BcmModuleState_Type.__name__ = "Integer32"
_BcmModuleState_Object = MibScalar
bcmModuleState = _BcmModuleState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 40),
    _BcmModuleState_Type()
)
bcmModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmModuleState.setStatus("mandatory")


class _BcmNbActiveUSap_Type(Integer32):
    """Custom type bcmNbActiveUSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_BcmNbActiveUSap_Type.__name__ = "Integer32"
_BcmNbActiveUSap_Object = MibScalar
bcmNbActiveUSap = _BcmNbActiveUSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 41),
    _BcmNbActiveUSap_Type()
)
bcmNbActiveUSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbActiveUSap.setStatus("mandatory")


class _BcmNbActiveDsl_Type(Integer32):
    """Custom type bcmNbActiveDsl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BcmNbActiveDsl_Type.__name__ = "Integer32"
_BcmNbActiveDsl_Object = MibScalar
bcmNbActiveDsl = _BcmNbActiveDsl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 42),
    _BcmNbActiveDsl_Type()
)
bcmNbActiveDsl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmNbActiveDsl.setStatus("mandatory")
_BcmLSapTable_Object = MibTable
bcmLSapTable = _BcmLSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50)
)
if mibBuilder.loadTexts:
    bcmLSapTable.setStatus("mandatory")
_BcmLSapEntry_Object = MibTableRow
bcmLSapEntry = _BcmLSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1)
)
bcmLSapEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmLSapDslNumber"),
    (0, "CXBCM-MIB", "bcmLSapNumber"),
)
if mibBuilder.loadTexts:
    bcmLSapEntry.setStatus("mandatory")
_BcmLSapDslNumber_Type = SapIndex
_BcmLSapDslNumber_Object = MibTableColumn
bcmLSapDslNumber = _BcmLSapDslNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 1),
    _BcmLSapDslNumber_Type()
)
bcmLSapDslNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapDslNumber.setStatus("mandatory")
_BcmLSapNumber_Type = LSapIndex
_BcmLSapNumber_Object = MibTableColumn
bcmLSapNumber = _BcmLSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 2),
    _BcmLSapNumber_Type()
)
bcmLSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapNumber.setStatus("mandatory")
_BcmLSapAlias_Type = Alias
_BcmLSapAlias_Object = MibTableColumn
bcmLSapAlias = _BcmLSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 3),
    _BcmLSapAlias_Type()
)
bcmLSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmLSapAlias.setStatus("mandatory")
_BcmLSapCompanionAlias_Type = Alias
_BcmLSapCompanionAlias_Object = MibTableColumn
bcmLSapCompanionAlias = _BcmLSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 4),
    _BcmLSapCompanionAlias_Type()
)
bcmLSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmLSapCompanionAlias.setStatus("mandatory")


class _BcmLSapDirectoryIndex_Type(Integer32):
    """Custom type bcmLSapDirectoryIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmLSapDirectoryIndex_Type.__name__ = "Integer32"
_BcmLSapDirectoryIndex_Object = MibTableColumn
bcmLSapDirectoryIndex = _BcmLSapDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 10),
    _BcmLSapDirectoryIndex_Type()
)
bcmLSapDirectoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmLSapDirectoryIndex.setStatus("mandatory")


class _BcmLSapLowDirectoryIndex_Type(Integer32):
    """Custom type bcmLSapLowDirectoryIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmLSapLowDirectoryIndex_Type.__name__ = "Integer32"
_BcmLSapLowDirectoryIndex_Object = MibTableColumn
bcmLSapLowDirectoryIndex = _BcmLSapLowDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 11),
    _BcmLSapLowDirectoryIndex_Type()
)
bcmLSapLowDirectoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmLSapLowDirectoryIndex.setStatus("mandatory")


class _BcmLSapHighDirectoryIndex_Type(Integer32):
    """Custom type bcmLSapHighDirectoryIndex based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmLSapHighDirectoryIndex_Type.__name__ = "Integer32"
_BcmLSapHighDirectoryIndex_Object = MibTableColumn
bcmLSapHighDirectoryIndex = _BcmLSapHighDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 12),
    _BcmLSapHighDirectoryIndex_Type()
)
bcmLSapHighDirectoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmLSapHighDirectoryIndex.setStatus("mandatory")


class _BcmLSapState_Type(Integer32):
    """Custom type bcmLSapState based on Integer32"""
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
        *(("active", 8),
          ("bound", 3),
          ("idle", 5),
          ("incoming", 7),
          ("not-used", 1),
          ("outgoing", 6),
          ("overlap-rx", 11),
          ("pending", 10),
          ("registering", 4),
          ("release", 9),
          ("unbound", 2))
    )


_BcmLSapState_Type.__name__ = "Integer32"
_BcmLSapState_Object = MibTableColumn
bcmLSapState = _BcmLSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 40),
    _BcmLSapState_Type()
)
bcmLSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapState.setStatus("mandatory")


class _BcmLSapStatusEvent_Type(Integer32):
    """Custom type bcmLSapStatusEvent based on Integer32"""
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
        *(("dslOutOfRange", 2),
          ("lsapMngmtRegistrationFailed", 4),
          ("lsapOutOfRange", 3),
          ("noEvent", 1))
    )


_BcmLSapStatusEvent_Type.__name__ = "Integer32"
_BcmLSapStatusEvent_Object = MibTableColumn
bcmLSapStatusEvent = _BcmLSapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 41),
    _BcmLSapStatusEvent_Type()
)
bcmLSapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapStatusEvent.setStatus("obsolete")
_BcmLSapPeerAddress_Type = DisplayString
_BcmLSapPeerAddress_Object = MibTableColumn
bcmLSapPeerAddress = _BcmLSapPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 42),
    _BcmLSapPeerAddress_Type()
)
bcmLSapPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapPeerAddress.setStatus("mandatory")
_BcmLSapPeerSubAddress_Type = DisplayString
_BcmLSapPeerSubAddress_Object = MibTableColumn
bcmLSapPeerSubAddress = _BcmLSapPeerSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 43),
    _BcmLSapPeerSubAddress_Type()
)
bcmLSapPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapPeerSubAddress.setStatus("mandatory")


class _BcmLSapCallOrigin_Type(Integer32):
    """Custom type bcmLSapCallOrigin based on Integer32"""
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
        *(("answer", 3),
          ("callback", 4),
          ("originate", 2),
          ("unknown", 1))
    )


_BcmLSapCallOrigin_Type.__name__ = "Integer32"
_BcmLSapCallOrigin_Object = MibTableColumn
bcmLSapCallOrigin = _BcmLSapCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 44),
    _BcmLSapCallOrigin_Type()
)
bcmLSapCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapCallOrigin.setStatus("mandatory")


class _BcmLSapInfoType_Type(Integer32):
    """Custom type bcmLSapInfoType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("audio-31", 5),
          ("audio-7", 6),
          ("packet", 8),
          ("restricted-digital", 4),
          ("speech", 2),
          ("unknown", 1),
          ("unrestricted-digital", 3),
          ("video", 7))
    )


_BcmLSapInfoType_Type.__name__ = "Integer32"
_BcmLSapInfoType_Object = MibTableColumn
bcmLSapInfoType = _BcmLSapInfoType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 45),
    _BcmLSapInfoType_Type()
)
bcmLSapInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapInfoType.setStatus("mandatory")


class _BcmLSapCallId_Type(DisplayString):
    """Custom type bcmLSapCallId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BcmLSapCallId_Type.__name__ = "DisplayString"
_BcmLSapCallId_Object = MibTableColumn
bcmLSapCallId = _BcmLSapCallId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 46),
    _BcmLSapCallId_Type()
)
bcmLSapCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapCallId.setStatus("mandatory")


class _BcmLSapUSapId_Type(Integer32):
    """Custom type bcmLSapUSapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BcmLSapUSapId_Type.__name__ = "Integer32"
_BcmLSapUSapId_Object = MibTableColumn
bcmLSapUSapId = _BcmLSapUSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 47),
    _BcmLSapUSapId_Type()
)
bcmLSapUSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapUSapId.setStatus("mandatory")


class _BcmLSapChannelCES_Type(Integer32):
    """Custom type bcmLSapChannelCES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_BcmLSapChannelCES_Type.__name__ = "Integer32"
_BcmLSapChannelCES_Object = MibTableColumn
bcmLSapChannelCES = _BcmLSapChannelCES_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 48),
    _BcmLSapChannelCES_Type()
)
bcmLSapChannelCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapChannelCES.setStatus("mandatory")
_BcmLSapCallSetupTime_Type = TimeTicks
_BcmLSapCallSetupTime_Object = MibTableColumn
bcmLSapCallSetupTime = _BcmLSapCallSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 49),
    _BcmLSapCallSetupTime_Type()
)
bcmLSapCallSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapCallSetupTime.setStatus("mandatory")
_BcmLSapCallConnectTime_Type = TimeTicks
_BcmLSapCallConnectTime_Object = MibTableColumn
bcmLSapCallConnectTime = _BcmLSapCallConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 50),
    _BcmLSapCallConnectTime_Type()
)
bcmLSapCallConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapCallConnectTime.setStatus("mandatory")
_BcmLSapCallDisconnectTime_Type = TimeTicks
_BcmLSapCallDisconnectTime_Object = MibTableColumn
bcmLSapCallDisconnectTime = _BcmLSapCallDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 51),
    _BcmLSapCallDisconnectTime_Type()
)
bcmLSapCallDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapCallDisconnectTime.setStatus("mandatory")
_BcmLSapNbInCalls_Type = Counter32
_BcmLSapNbInCalls_Object = MibTableColumn
bcmLSapNbInCalls = _BcmLSapNbInCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 60),
    _BcmLSapNbInCalls_Type()
)
bcmLSapNbInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapNbInCalls.setStatus("mandatory")
_BcmLSapNbInCallsConnected_Type = Counter32
_BcmLSapNbInCallsConnected_Object = MibTableColumn
bcmLSapNbInCallsConnected = _BcmLSapNbInCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 61),
    _BcmLSapNbInCallsConnected_Type()
)
bcmLSapNbInCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapNbInCallsConnected.setStatus("mandatory")
_BcmLSapNbOutCalls_Type = Counter32
_BcmLSapNbOutCalls_Object = MibTableColumn
bcmLSapNbOutCalls = _BcmLSapNbOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 62),
    _BcmLSapNbOutCalls_Type()
)
bcmLSapNbOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapNbOutCalls.setStatus("mandatory")
_BcmLSapNbOutCallsConnected_Type = Counter32
_BcmLSapNbOutCallsConnected_Object = MibTableColumn
bcmLSapNbOutCallsConnected = _BcmLSapNbOutCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 50, 1, 63),
    _BcmLSapNbOutCallsConnected_Type()
)
bcmLSapNbOutCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmLSapNbOutCallsConnected.setStatus("mandatory")
_BcmDslTable_Object = MibTable
bcmDslTable = _BcmDslTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51)
)
if mibBuilder.loadTexts:
    bcmDslTable.setStatus("mandatory")
_BcmDslEntry_Object = MibTableRow
bcmDslEntry = _BcmDslEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1)
)
bcmDslEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmDslNumber"),
)
if mibBuilder.loadTexts:
    bcmDslEntry.setStatus("mandatory")
_BcmDslNumber_Type = SapIndex
_BcmDslNumber_Object = MibTableColumn
bcmDslNumber = _BcmDslNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 1),
    _BcmDslNumber_Type()
)
bcmDslNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslNumber.setStatus("mandatory")


class _BcmDslRowStatus_Type(Integer32):
    """Custom type bcmDslRowStatus based on Integer32"""
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


_BcmDslRowStatus_Type.__name__ = "Integer32"
_BcmDslRowStatus_Object = MibTableColumn
bcmDslRowStatus = _BcmDslRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 2),
    _BcmDslRowStatus_Type()
)
bcmDslRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslRowStatus.setStatus("mandatory")


class _BcmDslSwitchType_Type(Integer32):
    """Custom type bcmDslSwitchType based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bri-5ESS", 3),
          ("bri-DMS100", 5),
          ("bri-NI1", 8),
          ("bri-NI2", 9),
          ("unspecified", 1))
    )


_BcmDslSwitchType_Type.__name__ = "Integer32"
_BcmDslSwitchType_Object = MibTableColumn
bcmDslSwitchType = _BcmDslSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 10),
    _BcmDslSwitchType_Type()
)
bcmDslSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslSwitchType.setStatus("obsolete")


class _BcmDslBChannelCount_Type(Integer32):
    """Custom type bcmDslBChannelCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BcmDslBChannelCount_Type.__name__ = "Integer32"
_BcmDslBChannelCount_Object = MibTableColumn
bcmDslBChannelCount = _BcmDslBChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 11),
    _BcmDslBChannelCount_Type()
)
bcmDslBChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslBChannelCount.setStatus("mandatory")


class _BcmDslBChannelType_Type(Integer32):
    """Custom type bcmDslBChannelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialup", 1),
          ("leased", 2))
    )


_BcmDslBChannelType_Type.__name__ = "Integer32"
_BcmDslBChannelType_Object = MibTableColumn
bcmDslBChannelType = _BcmDslBChannelType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 12),
    _BcmDslBChannelType_Type()
)
bcmDslBChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslBChannelType.setStatus("mandatory")


class _BcmDslMngmtTimer_Type(Integer32):
    """Custom type bcmDslMngmtTimer based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BcmDslMngmtTimer_Type.__name__ = "Integer32"
_BcmDslMngmtTimer_Object = MibTableColumn
bcmDslMngmtTimer = _BcmDslMngmtTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 13),
    _BcmDslMngmtTimer_Type()
)
bcmDslMngmtTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslMngmtTimer.setStatus("mandatory")


class _BcmDslInfoRate_Type(Integer32):
    """Custom type bcmDslInfoRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56kbps", 1),
          ("rate64kbps", 2))
    )


_BcmDslInfoRate_Type.__name__ = "Integer32"
_BcmDslInfoRate_Object = MibTableColumn
bcmDslInfoRate = _BcmDslInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 14),
    _BcmDslInfoRate_Type()
)
bcmDslInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslInfoRate.setStatus("mandatory")


class _BcmDslSendingProceed_Type(Integer32):
    """Custom type bcmDslSendingProceed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("en-bloc", 1),
          ("overlap", 2))
    )


_BcmDslSendingProceed_Type.__name__ = "Integer32"
_BcmDslSendingProceed_Object = MibTableColumn
bcmDslSendingProceed = _BcmDslSendingProceed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 15),
    _BcmDslSendingProceed_Type()
)
bcmDslSendingProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDslSendingProceed.setStatus("obsolete")


class _BcmDslInterfaceType_Type(Integer32):
    """Custom type bcmDslInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bri", 2),
          ("none", 1),
          ("pri", 3))
    )


_BcmDslInterfaceType_Type.__name__ = "Integer32"
_BcmDslInterfaceType_Object = MibTableColumn
bcmDslInterfaceType = _BcmDslInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 40),
    _BcmDslInterfaceType_Type()
)
bcmDslInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslInterfaceType.setStatus("mandatory")


class _BcmDslBriType_Type(Integer32):
    """Custom type bcmDslBriType based on Integer32"""
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
        *(("none", 1),
          ("s-t", 3),
          ("u", 2))
    )


_BcmDslBriType_Type.__name__ = "Integer32"
_BcmDslBriType_Object = MibTableColumn
bcmDslBriType = _BcmDslBriType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 41),
    _BcmDslBriType_Type()
)
bcmDslBriType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslBriType.setStatus("mandatory")


class _BcmDslPriType_Type(Integer32):
    """Custom type bcmDslPriType based on Integer32"""
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
        *(("ansi", 2),
          ("cept", 3),
          ("none", 1))
    )


_BcmDslPriType_Type.__name__ = "Integer32"
_BcmDslPriType_Object = MibTableColumn
bcmDslPriType = _BcmDslPriType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 42),
    _BcmDslPriType_Type()
)
bcmDslPriType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslPriType.setStatus("mandatory")


class _BcmDslNbChannelInUse_Type(Integer32):
    """Custom type bcmDslNbChannelInUse based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BcmDslNbChannelInUse_Type.__name__ = "Integer32"
_BcmDslNbChannelInUse_Object = MibTableColumn
bcmDslNbChannelInUse = _BcmDslNbChannelInUse_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 43),
    _BcmDslNbChannelInUse_Type()
)
bcmDslNbChannelInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslNbChannelInUse.setStatus("mandatory")


class _BcmDslOutGoingCallId_Type(DisplayString):
    """Custom type bcmDslOutGoingCallId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_BcmDslOutGoingCallId_Type.__name__ = "DisplayString"
_BcmDslOutGoingCallId_Object = MibTableColumn
bcmDslOutGoingCallId = _BcmDslOutGoingCallId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 44),
    _BcmDslOutGoingCallId_Type()
)
bcmDslOutGoingCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslOutGoingCallId.setStatus("mandatory")


class _BcmDslEffectiveRetries_Type(Integer32):
    """Custom type bcmDslEffectiveRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BcmDslEffectiveRetries_Type.__name__ = "Integer32"
_BcmDslEffectiveRetries_Object = MibTableColumn
bcmDslEffectiveRetries = _BcmDslEffectiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 51, 1, 45),
    _BcmDslEffectiveRetries_Type()
)
bcmDslEffectiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDslEffectiveRetries.setStatus("mandatory")
_BcmUSapTable_Object = MibTable
bcmUSapTable = _BcmUSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52)
)
if mibBuilder.loadTexts:
    bcmUSapTable.setStatus("mandatory")
_BcmUSapEntry_Object = MibTableRow
bcmUSapEntry = _BcmUSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1)
)
bcmUSapEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmUSapNumber"),
)
if mibBuilder.loadTexts:
    bcmUSapEntry.setStatus("mandatory")
_BcmUSapNumber_Type = SapIndex
_BcmUSapNumber_Object = MibTableColumn
bcmUSapNumber = _BcmUSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 1),
    _BcmUSapNumber_Type()
)
bcmUSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapNumber.setStatus("mandatory")


class _BcmUSapRowStatus_Type(Integer32):
    """Custom type bcmUSapRowStatus based on Integer32"""
    defaultValue = 1

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


_BcmUSapRowStatus_Type.__name__ = "Integer32"
_BcmUSapRowStatus_Object = MibTableColumn
bcmUSapRowStatus = _BcmUSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 2),
    _BcmUSapRowStatus_Type()
)
bcmUSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapRowStatus.setStatus("mandatory")
_BcmUSapAlias_Type = Alias
_BcmUSapAlias_Object = MibTableColumn
bcmUSapAlias = _BcmUSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 3),
    _BcmUSapAlias_Type()
)
bcmUSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapAlias.setStatus("mandatory")


class _BcmUSapLowDirectoryIndex_Type(Integer32):
    """Custom type bcmUSapLowDirectoryIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmUSapLowDirectoryIndex_Type.__name__ = "Integer32"
_BcmUSapLowDirectoryIndex_Object = MibTableColumn
bcmUSapLowDirectoryIndex = _BcmUSapLowDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 10),
    _BcmUSapLowDirectoryIndex_Type()
)
bcmUSapLowDirectoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapLowDirectoryIndex.setStatus("mandatory")


class _BcmUSapHighDirectoryIndex_Type(Integer32):
    """Custom type bcmUSapHighDirectoryIndex based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmUSapHighDirectoryIndex_Type.__name__ = "Integer32"
_BcmUSapHighDirectoryIndex_Object = MibTableColumn
bcmUSapHighDirectoryIndex = _BcmUSapHighDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 11),
    _BcmUSapHighDirectoryIndex_Type()
)
bcmUSapHighDirectoryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapHighDirectoryIndex.setStatus("mandatory")


class _BcmUSapAnswerMode_Type(Integer32):
    """Custom type bcmUSapAnswerMode based on Integer32"""
    defaultValue = 2

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
        *(("answer-address", 3),
          ("answer-all", 2),
          ("answer-none", 1),
          ("answer-subaddress", 4))
    )


_BcmUSapAnswerMode_Type.__name__ = "Integer32"
_BcmUSapAnswerMode_Object = MibTableColumn
bcmUSapAnswerMode = _BcmUSapAnswerMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 12),
    _BcmUSapAnswerMode_Type()
)
bcmUSapAnswerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapAnswerMode.setStatus("mandatory")


class _BcmUSapPermission_Type(Integer32):
    """Custom type bcmUSapPermission based on Integer32"""
    defaultValue = 3

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
        *(("answer", 2),
          ("both", 3),
          ("callback", 4),
          ("originate", 1))
    )


_BcmUSapPermission_Type.__name__ = "Integer32"
_BcmUSapPermission_Object = MibTableColumn
bcmUSapPermission = _BcmUSapPermission_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 13),
    _BcmUSapPermission_Type()
)
bcmUSapPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapPermission.setStatus("mandatory")


class _BcmUSapCallTypeAccepted_Type(Integer32):
    """Custom type bcmUSapCallTypeAccepted based on Integer32"""
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
        *(("data-call", 2),
          ("packet-call", 3),
          ("voice-call", 1))
    )


_BcmUSapCallTypeAccepted_Type.__name__ = "Integer32"
_BcmUSapCallTypeAccepted_Object = MibTableColumn
bcmUSapCallTypeAccepted = _BcmUSapCallTypeAccepted_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 14),
    _BcmUSapCallTypeAccepted_Type()
)
bcmUSapCallTypeAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapCallTypeAccepted.setStatus("mandatory")


class _BcmUSapSendingProceed_Type(Integer32):
    """Custom type bcmUSapSendingProceed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("en-bloc", 1),
          ("overlap", 2))
    )


_BcmUSapSendingProceed_Type.__name__ = "Integer32"
_BcmUSapSendingProceed_Object = MibTableColumn
bcmUSapSendingProceed = _BcmUSapSendingProceed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 15),
    _BcmUSapSendingProceed_Type()
)
bcmUSapSendingProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapSendingProceed.setStatus("mandatory")


class _BcmUSapVoiceInterDigitTimer_Type(Integer32):
    """Custom type bcmUSapVoiceInterDigitTimer based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BcmUSapVoiceInterDigitTimer_Type.__name__ = "Integer32"
_BcmUSapVoiceInterDigitTimer_Object = MibTableColumn
bcmUSapVoiceInterDigitTimer = _BcmUSapVoiceInterDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 16),
    _BcmUSapVoiceInterDigitTimer_Type()
)
bcmUSapVoiceInterDigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceInterDigitTimer.setStatus("mandatory")


class _BcmUSapVoiceHuntGroup_Type(Integer32):
    """Custom type bcmUSapVoiceHuntGroup based on Integer32"""
    defaultHexValue = 1073741823


_BcmUSapVoiceHuntGroup_Object = MibTableColumn
bcmUSapVoiceHuntGroup = _BcmUSapVoiceHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 17),
    _BcmUSapVoiceHuntGroup_Type()
)
bcmUSapVoiceHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceHuntGroup.setStatus("mandatory")


class _BcmUSapVoiceHuntDsl_Type(Integer32):
    """Custom type bcmUSapVoiceHuntDsl based on Integer32"""
    defaultHexValue = 3


_BcmUSapVoiceHuntDsl_Object = MibTableColumn
bcmUSapVoiceHuntDsl = _BcmUSapVoiceHuntDsl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 18),
    _BcmUSapVoiceHuntDsl_Type()
)
bcmUSapVoiceHuntDsl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceHuntDsl.setStatus("mandatory")


class _BcmUSapVoiceAddressPlan_Type(Integer32):
    """Custom type bcmUSapVoiceAddressPlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("national", 9),
          ("private", 10),
          ("telephony", 3),
          ("telex", 5),
          ("unknown", 1),
          ("x-121", 4))
    )


_BcmUSapVoiceAddressPlan_Type.__name__ = "Integer32"
_BcmUSapVoiceAddressPlan_Object = MibTableColumn
bcmUSapVoiceAddressPlan = _BcmUSapVoiceAddressPlan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 19),
    _BcmUSapVoiceAddressPlan_Type()
)
bcmUSapVoiceAddressPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceAddressPlan.setStatus("mandatory")


class _BcmUSapVoiceAddressType_Type(Integer32):
    """Custom type bcmUSapVoiceAddressType based on Integer32"""
    defaultValue = 2

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
        *(("international", 2),
          ("national", 3),
          ("private", 4),
          ("subscriber", 5),
          ("unknown", 1))
    )


_BcmUSapVoiceAddressType_Type.__name__ = "Integer32"
_BcmUSapVoiceAddressType_Object = MibTableColumn
bcmUSapVoiceAddressType = _BcmUSapVoiceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 20),
    _BcmUSapVoiceAddressType_Type()
)
bcmUSapVoiceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceAddressType.setStatus("mandatory")


class _BcmUSapVoiceCodingScheme_Type(Integer32):
    """Custom type bcmUSapVoiceCodingScheme based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a-law", 2),
          ("mu-law", 1))
    )


_BcmUSapVoiceCodingScheme_Type.__name__ = "Integer32"
_BcmUSapVoiceCodingScheme_Object = MibTableColumn
bcmUSapVoiceCodingScheme = _BcmUSapVoiceCodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 21),
    _BcmUSapVoiceCodingScheme_Type()
)
bcmUSapVoiceCodingScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceCodingScheme.setStatus("mandatory")


class _BcmUSapVoiceCallRoutingMode_Type(Integer32):
    """Custom type bcmUSapVoiceCallRoutingMode based on Integer32"""
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
        *(("address", 2),
          ("address-and-subaddress", 4),
          ("not-used", 1),
          ("subaddress", 3))
    )


_BcmUSapVoiceCallRoutingMode_Type.__name__ = "Integer32"
_BcmUSapVoiceCallRoutingMode_Object = MibTableColumn
bcmUSapVoiceCallRoutingMode = _BcmUSapVoiceCallRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 22),
    _BcmUSapVoiceCallRoutingMode_Type()
)
bcmUSapVoiceCallRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmUSapVoiceCallRoutingMode.setStatus("mandatory")


class _BcmUSapState_Type(Integer32):
    """Custom type bcmUSapState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("bound", 3),
          ("idle", 5),
          ("incoming", 7),
          ("not-used", 1),
          ("outgoing", 6),
          ("overlap-rx", 11),
          ("registering", 4),
          ("release", 9),
          ("unbound", 2))
    )


_BcmUSapState_Type.__name__ = "Integer32"
_BcmUSapState_Object = MibTableColumn
bcmUSapState = _BcmUSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 40),
    _BcmUSapState_Type()
)
bcmUSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapState.setStatus("mandatory")


class _BcmUSapStatusEvent_Type(Integer32):
    """Custom type bcmUSapStatusEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEvent", 1),
          ("usapOutOfRange", 2))
    )


_BcmUSapStatusEvent_Type.__name__ = "Integer32"
_BcmUSapStatusEvent_Object = MibTableColumn
bcmUSapStatusEvent = _BcmUSapStatusEvent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 41),
    _BcmUSapStatusEvent_Type()
)
bcmUSapStatusEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapStatusEvent.setStatus("obsolete")


class _BcmUSapNbChannelBound_Type(Integer32):
    """Custom type bcmUSapNbChannelBound based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BcmUSapNbChannelBound_Type.__name__ = "Integer32"
_BcmUSapNbChannelBound_Object = MibTableColumn
bcmUSapNbChannelBound = _BcmUSapNbChannelBound_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 42),
    _BcmUSapNbChannelBound_Type()
)
bcmUSapNbChannelBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapNbChannelBound.setStatus("mandatory")
_BcmUSapTotalConnectTime_Type = TimeTicks
_BcmUSapTotalConnectTime_Object = MibTableColumn
bcmUSapTotalConnectTime = _BcmUSapTotalConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 43),
    _BcmUSapTotalConnectTime_Type()
)
bcmUSapTotalConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapTotalConnectTime.setStatus("mandatory")
_BcmUSapLastSetupTime_Type = TimeTicks
_BcmUSapLastSetupTime_Object = MibTableColumn
bcmUSapLastSetupTime = _BcmUSapLastSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 44),
    _BcmUSapLastSetupTime_Type()
)
bcmUSapLastSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapLastSetupTime.setStatus("mandatory")
_BcmUSapLastConnectTime_Type = TimeTicks
_BcmUSapLastConnectTime_Object = MibTableColumn
bcmUSapLastConnectTime = _BcmUSapLastConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 45),
    _BcmUSapLastConnectTime_Type()
)
bcmUSapLastConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapLastConnectTime.setStatus("mandatory")
_BcmUSapLastDisconnectTime_Type = TimeTicks
_BcmUSapLastDisconnectTime_Object = MibTableColumn
bcmUSapLastDisconnectTime = _BcmUSapLastDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 46),
    _BcmUSapLastDisconnectTime_Type()
)
bcmUSapLastDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapLastDisconnectTime.setStatus("mandatory")


class _BcmUSapLastDisconnectCause_Type(Integer32):
    """Custom type bcmUSapLastDisconnectCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_BcmUSapLastDisconnectCause_Type.__name__ = "Integer32"
_BcmUSapLastDisconnectCause_Object = MibTableColumn
bcmUSapLastDisconnectCause = _BcmUSapLastDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 47),
    _BcmUSapLastDisconnectCause_Type()
)
bcmUSapLastDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapLastDisconnectCause.setStatus("mandatory")


class _BcmUSapDslId_Type(Integer32):
    """Custom type bcmUSapDslId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BcmUSapDslId_Type.__name__ = "Integer32"
_BcmUSapDslId_Object = MibTableColumn
bcmUSapDslId = _BcmUSapDslId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 48),
    _BcmUSapDslId_Type()
)
bcmUSapDslId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapDslId.setStatus("mandatory")


class _BcmUSapLocalSapId_Type(Integer32):
    """Custom type bcmUSapLocalSapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BcmUSapLocalSapId_Type.__name__ = "Integer32"
_BcmUSapLocalSapId_Object = MibTableColumn
bcmUSapLocalSapId = _BcmUSapLocalSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 49),
    _BcmUSapLocalSapId_Type()
)
bcmUSapLocalSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapLocalSapId.setStatus("obsolete")


class _BcmUSapSpeedDialDirectoryIndex_Type(Integer32):
    """Custom type bcmUSapSpeedDialDirectoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BcmUSapSpeedDialDirectoryIndex_Type.__name__ = "Integer32"
_BcmUSapSpeedDialDirectoryIndex_Object = MibTableColumn
bcmUSapSpeedDialDirectoryIndex = _BcmUSapSpeedDialDirectoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 50),
    _BcmUSapSpeedDialDirectoryIndex_Type()
)
bcmUSapSpeedDialDirectoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapSpeedDialDirectoryIndex.setStatus("mandatory")


class _BcmUSapVoiceChannelUsed_Type(Integer32):
    """Custom type bcmUSapVoiceChannelUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BcmUSapVoiceChannelUsed_Type.__name__ = "Integer32"
_BcmUSapVoiceChannelUsed_Object = MibTableColumn
bcmUSapVoiceChannelUsed = _BcmUSapVoiceChannelUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 51),
    _BcmUSapVoiceChannelUsed_Type()
)
bcmUSapVoiceChannelUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapVoiceChannelUsed.setStatus("mandatory")
_BcmUSapNbSuccessCalls_Type = Counter32
_BcmUSapNbSuccessCalls_Object = MibTableColumn
bcmUSapNbSuccessCalls = _BcmUSapNbSuccessCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 60),
    _BcmUSapNbSuccessCalls_Type()
)
bcmUSapNbSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapNbSuccessCalls.setStatus("mandatory")
_BcmUSapNbFailedCalls_Type = Counter32
_BcmUSapNbFailedCalls_Object = MibTableColumn
bcmUSapNbFailedCalls = _BcmUSapNbFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 61),
    _BcmUSapNbFailedCalls_Type()
)
bcmUSapNbFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapNbFailedCalls.setStatus("mandatory")
_BcmUSapNbRefusedCalls_Type = Counter32
_BcmUSapNbRefusedCalls_Object = MibTableColumn
bcmUSapNbRefusedCalls = _BcmUSapNbRefusedCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 52, 1, 62),
    _BcmUSapNbRefusedCalls_Type()
)
bcmUSapNbRefusedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmUSapNbRefusedCalls.setStatus("mandatory")
_BcmDirectoryTable_Object = MibTable
bcmDirectoryTable = _BcmDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53)
)
if mibBuilder.loadTexts:
    bcmDirectoryTable.setStatus("mandatory")
_BcmDirectoryEntry_Object = MibTableRow
bcmDirectoryEntry = _BcmDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1)
)
bcmDirectoryEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmDirectoryNumber"),
)
if mibBuilder.loadTexts:
    bcmDirectoryEntry.setStatus("mandatory")
_BcmDirectoryNumber_Type = SapIndex
_BcmDirectoryNumber_Object = MibTableColumn
bcmDirectoryNumber = _BcmDirectoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 1),
    _BcmDirectoryNumber_Type()
)
bcmDirectoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDirectoryNumber.setStatus("mandatory")


class _BcmDirectoryRowStatus_Type(Integer32):
    """Custom type bcmDirectoryRowStatus based on Integer32"""
    defaultValue = 1

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


_BcmDirectoryRowStatus_Type.__name__ = "Integer32"
_BcmDirectoryRowStatus_Object = MibTableColumn
bcmDirectoryRowStatus = _BcmDirectoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 2),
    _BcmDirectoryRowStatus_Type()
)
bcmDirectoryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectoryRowStatus.setStatus("mandatory")
_BcmDirectoryAddress_Type = DisplayString
_BcmDirectoryAddress_Object = MibTableColumn
bcmDirectoryAddress = _BcmDirectoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 10),
    _BcmDirectoryAddress_Type()
)
bcmDirectoryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectoryAddress.setStatus("mandatory")


class _BcmDirectoryAddressPlan_Type(Integer32):
    """Custom type bcmDirectoryAddressPlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 2),
          ("national", 9),
          ("private", 10),
          ("telephony", 3),
          ("telex", 5),
          ("unknown", 1),
          ("x-121", 4))
    )


_BcmDirectoryAddressPlan_Type.__name__ = "Integer32"
_BcmDirectoryAddressPlan_Object = MibTableColumn
bcmDirectoryAddressPlan = _BcmDirectoryAddressPlan_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 11),
    _BcmDirectoryAddressPlan_Type()
)
bcmDirectoryAddressPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectoryAddressPlan.setStatus("mandatory")


class _BcmDirectoryAddressType_Type(Integer32):
    """Custom type bcmDirectoryAddressType based on Integer32"""
    defaultValue = 2

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
        *(("international", 2),
          ("national", 3),
          ("private", 4),
          ("subscriber", 5),
          ("unknown", 1))
    )


_BcmDirectoryAddressType_Type.__name__ = "Integer32"
_BcmDirectoryAddressType_Object = MibTableColumn
bcmDirectoryAddressType = _BcmDirectoryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 12),
    _BcmDirectoryAddressType_Type()
)
bcmDirectoryAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectoryAddressType.setStatus("mandatory")
_BcmDirectorySubAddress_Type = DisplayString
_BcmDirectorySubAddress_Object = MibTableColumn
bcmDirectorySubAddress = _BcmDirectorySubAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 13),
    _BcmDirectorySubAddress_Type()
)
bcmDirectorySubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectorySubAddress.setStatus("mandatory")


class _BcmDirectorySubAddressType_Type(Integer32):
    """Custom type bcmDirectorySubAddressType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nsap", 1),
          ("user-defines", 3))
    )


_BcmDirectorySubAddressType_Type.__name__ = "Integer32"
_BcmDirectorySubAddressType_Object = MibTableColumn
bcmDirectorySubAddressType = _BcmDirectorySubAddressType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 14),
    _BcmDirectorySubAddressType_Type()
)
bcmDirectorySubAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectorySubAddressType.setStatus("mandatory")
_BcmDirectorySpid_Type = DisplayString
_BcmDirectorySpid_Object = MibTableColumn
bcmDirectorySpid = _BcmDirectorySpid_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 53, 1, 15),
    _BcmDirectorySpid_Type()
)
bcmDirectorySpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcmDirectorySpid.setStatus("mandatory")
_BcmCallHistoryTable_Object = MibTable
bcmCallHistoryTable = _BcmCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54)
)
if mibBuilder.loadTexts:
    bcmCallHistoryTable.setStatus("mandatory")
_BcmCallHistoryEntry_Object = MibTableRow
bcmCallHistoryEntry = _BcmCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1)
)
bcmCallHistoryEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmCallHistoryUSapNumber"),
    (0, "CXBCM-MIB", "bcmCallHistoryNumber"),
)
if mibBuilder.loadTexts:
    bcmCallHistoryEntry.setStatus("mandatory")
_BcmCallHistoryUSapNumber_Type = SapIndex
_BcmCallHistoryUSapNumber_Object = MibTableColumn
bcmCallHistoryUSapNumber = _BcmCallHistoryUSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 1),
    _BcmCallHistoryUSapNumber_Type()
)
bcmCallHistoryUSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryUSapNumber.setStatus("mandatory")
_BcmCallHistoryNumber_Type = CHIndex
_BcmCallHistoryNumber_Object = MibTableColumn
bcmCallHistoryNumber = _BcmCallHistoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 2),
    _BcmCallHistoryNumber_Type()
)
bcmCallHistoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryNumber.setStatus("mandatory")


class _BcmCallHistoryDslChannelUsed_Type(Integer32):
    """Custom type bcmCallHistoryDslChannelUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BcmCallHistoryDslChannelUsed_Type.__name__ = "Integer32"
_BcmCallHistoryDslChannelUsed_Object = MibTableColumn
bcmCallHistoryDslChannelUsed = _BcmCallHistoryDslChannelUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 40),
    _BcmCallHistoryDslChannelUsed_Type()
)
bcmCallHistoryDslChannelUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryDslChannelUsed.setStatus("mandatory")


class _BcmCallHistoryBChannelsUsed_Type(DisplayString):
    """Custom type bcmCallHistoryBChannelsUsed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_BcmCallHistoryBChannelsUsed_Type.__name__ = "DisplayString"
_BcmCallHistoryBChannelsUsed_Object = MibTableColumn
bcmCallHistoryBChannelsUsed = _BcmCallHistoryBChannelsUsed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 41),
    _BcmCallHistoryBChannelsUsed_Type()
)
bcmCallHistoryBChannelsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryBChannelsUsed.setStatus("mandatory")
_BcmCallHistoryPeerAddress_Type = DisplayString
_BcmCallHistoryPeerAddress_Object = MibTableColumn
bcmCallHistoryPeerAddress = _BcmCallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 42),
    _BcmCallHistoryPeerAddress_Type()
)
bcmCallHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryPeerAddress.setStatus("mandatory")
_BcmCallHistoryPeerSubAddress_Type = DisplayString
_BcmCallHistoryPeerSubAddress_Object = MibTableColumn
bcmCallHistoryPeerSubAddress = _BcmCallHistoryPeerSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 43),
    _BcmCallHistoryPeerSubAddress_Type()
)
bcmCallHistoryPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryPeerSubAddress.setStatus("mandatory")


class _BcmCallHistoryOrigin_Type(Integer32):
    """Custom type bcmCallHistoryOrigin based on Integer32"""
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
        *(("answer-src", 3),
          ("callback-src", 4),
          ("originate-src", 2),
          ("unknown-src", 1))
    )


_BcmCallHistoryOrigin_Type.__name__ = "Integer32"
_BcmCallHistoryOrigin_Object = MibTableColumn
bcmCallHistoryOrigin = _BcmCallHistoryOrigin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 44),
    _BcmCallHistoryOrigin_Type()
)
bcmCallHistoryOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryOrigin.setStatus("mandatory")
_BcmCallHistorySetupTime_Type = TimeTicks
_BcmCallHistorySetupTime_Object = MibTableColumn
bcmCallHistorySetupTime = _BcmCallHistorySetupTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 45),
    _BcmCallHistorySetupTime_Type()
)
bcmCallHistorySetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistorySetupTime.setStatus("mandatory")
_BcmCallHistoryConnectTime_Type = TimeTicks
_BcmCallHistoryConnectTime_Object = MibTableColumn
bcmCallHistoryConnectTime = _BcmCallHistoryConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 46),
    _BcmCallHistoryConnectTime_Type()
)
bcmCallHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryConnectTime.setStatus("mandatory")
_BcmCallHistoryDisconnectTime_Type = TimeTicks
_BcmCallHistoryDisconnectTime_Object = MibTableColumn
bcmCallHistoryDisconnectTime = _BcmCallHistoryDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 54, 1, 47),
    _BcmCallHistoryDisconnectTime_Type()
)
bcmCallHistoryDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmCallHistoryDisconnectTime.setStatus("mandatory")
_BcmDebugTable_Object = MibTable
bcmDebugTable = _BcmDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55)
)
if mibBuilder.loadTexts:
    bcmDebugTable.setStatus("mandatory")
_BcmDebugEntry_Object = MibTableRow
bcmDebugEntry = _BcmDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1)
)
bcmDebugEntry.setIndexNames(
    (0, "CXBCM-MIB", "bcmDebugNumber"),
)
if mibBuilder.loadTexts:
    bcmDebugEntry.setStatus("mandatory")
_BcmDebugNumber_Type = SapIndex
_BcmDebugNumber_Object = MibTableColumn
bcmDebugNumber = _BcmDebugNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 1),
    _BcmDebugNumber_Type()
)
bcmDebugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcmDebugNumber.setStatus("mandatory")


class _BcmDebugDslCB_Type(Integer32):
    """Custom type bcmDebugDslCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BcmDebugDslCB_Type.__name__ = "Integer32"
_BcmDebugDslCB_Object = MibTableColumn
bcmDebugDslCB = _BcmDebugDslCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 10),
    _BcmDebugDslCB_Type()
)
bcmDebugDslCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugDslCB.setStatus("mandatory")


class _BcmDebugLSapCB_Type(Integer32):
    """Custom type bcmDebugLSapCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_BcmDebugLSapCB_Type.__name__ = "Integer32"
_BcmDebugLSapCB_Object = MibTableColumn
bcmDebugLSapCB = _BcmDebugLSapCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 11),
    _BcmDebugLSapCB_Type()
)
bcmDebugLSapCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugLSapCB.setStatus("mandatory")


class _BcmDebugUSapCB_Type(Integer32):
    """Custom type bcmDebugUSapCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BcmDebugUSapCB_Type.__name__ = "Integer32"
_BcmDebugUSapCB_Object = MibTableColumn
bcmDebugUSapCB = _BcmDebugUSapCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 12),
    _BcmDebugUSapCB_Type()
)
bcmDebugUSapCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugUSapCB.setStatus("mandatory")


class _BcmDebugCallHistoryCB_Type(Integer32):
    """Custom type bcmDebugCallHistoryCB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BcmDebugCallHistoryCB_Type.__name__ = "Integer32"
_BcmDebugCallHistoryCB_Object = MibTableColumn
bcmDebugCallHistoryCB = _BcmDebugCallHistoryCB_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 13),
    _BcmDebugCallHistoryCB_Type()
)
bcmDebugCallHistoryCB.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugCallHistoryCB.setStatus("mandatory")


class _BcmDebugDataScope_Type(Integer32):
    """Custom type bcmDebugDataScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BcmDebugDataScope_Type.__name__ = "Integer32"
_BcmDebugDataScope_Object = MibTableColumn
bcmDebugDataScope = _BcmDebugDataScope_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 14),
    _BcmDebugDataScope_Type()
)
bcmDebugDataScope.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugDataScope.setStatus("mandatory")


class _BcmDebugDisconnect_Type(Integer32):
    """Custom type bcmDebugDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_BcmDebugDisconnect_Type.__name__ = "Integer32"
_BcmDebugDisconnect_Object = MibTableColumn
bcmDebugDisconnect = _BcmDebugDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 55, 1, 15),
    _BcmDebugDisconnect_Type()
)
bcmDebugDisconnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bcmDebugDisconnect.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bcmLSapStatusIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 0, 1)
)
bcmLSapStatusIndication.setObjects(
      *(("CXBCM-MIB", "bcmLSapDslNumber"),
        ("CXBCM-MIB", "bcmLSapNumber"),
        ("CXBCM-MIB", "bcmLSapStatusEvent"))
)
if mibBuilder.loadTexts:
    bcmLSapStatusIndication.setStatus(
        ""
    )

bcmCallHistoryStatusIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 48, 0, 2)
)
bcmCallHistoryStatusIndication.setObjects(
      *(("CXBCM-MIB", "bcmCallHistoryUSapNumber"),
        ("CXBCM-MIB", "bcmCallHistoryNumber"),
        ("CXBCM-MIB", "bcmCallHistoryDslChannelUsed"),
        ("CXBCM-MIB", "bcmCallHistoryBChannelsUsed"),
        ("CXBCM-MIB", "bcmCallHistoryPeerAddress"),
        ("CXBCM-MIB", "bcmCallHistoryPeerSubAddress"),
        ("CXBCM-MIB", "bcmCallHistoryOrigin"),
        ("CXBCM-MIB", "bcmCallHistorySetupTime"),
        ("CXBCM-MIB", "bcmCallHistoryConnectTime"),
        ("CXBCM-MIB", "bcmCallHistoryDisconnectTime"))
)
if mibBuilder.loadTexts:
    bcmCallHistoryStatusIndication.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXBCM-MIB",
    **{"LSapIndex": LSapIndex,
       "CHIndex": CHIndex,
       "bcmLSapStatusIndication": bcmLSapStatusIndication,
       "bcmCallHistoryStatusIndication": bcmCallHistoryStatusIndication,
       "bcmTraps": bcmTraps,
       "bcmCallHistoryTraps": bcmCallHistoryTraps,
       "bcmSoftwareVersion": bcmSoftwareVersion,
       "bcmMibLevel": bcmMibLevel,
       "bcmModuleState": bcmModuleState,
       "bcmNbActiveUSap": bcmNbActiveUSap,
       "bcmNbActiveDsl": bcmNbActiveDsl,
       "bcmLSapTable": bcmLSapTable,
       "bcmLSapEntry": bcmLSapEntry,
       "bcmLSapDslNumber": bcmLSapDslNumber,
       "bcmLSapNumber": bcmLSapNumber,
       "bcmLSapAlias": bcmLSapAlias,
       "bcmLSapCompanionAlias": bcmLSapCompanionAlias,
       "bcmLSapDirectoryIndex": bcmLSapDirectoryIndex,
       "bcmLSapLowDirectoryIndex": bcmLSapLowDirectoryIndex,
       "bcmLSapHighDirectoryIndex": bcmLSapHighDirectoryIndex,
       "bcmLSapState": bcmLSapState,
       "bcmLSapStatusEvent": bcmLSapStatusEvent,
       "bcmLSapPeerAddress": bcmLSapPeerAddress,
       "bcmLSapPeerSubAddress": bcmLSapPeerSubAddress,
       "bcmLSapCallOrigin": bcmLSapCallOrigin,
       "bcmLSapInfoType": bcmLSapInfoType,
       "bcmLSapCallId": bcmLSapCallId,
       "bcmLSapUSapId": bcmLSapUSapId,
       "bcmLSapChannelCES": bcmLSapChannelCES,
       "bcmLSapCallSetupTime": bcmLSapCallSetupTime,
       "bcmLSapCallConnectTime": bcmLSapCallConnectTime,
       "bcmLSapCallDisconnectTime": bcmLSapCallDisconnectTime,
       "bcmLSapNbInCalls": bcmLSapNbInCalls,
       "bcmLSapNbInCallsConnected": bcmLSapNbInCallsConnected,
       "bcmLSapNbOutCalls": bcmLSapNbOutCalls,
       "bcmLSapNbOutCallsConnected": bcmLSapNbOutCallsConnected,
       "bcmDslTable": bcmDslTable,
       "bcmDslEntry": bcmDslEntry,
       "bcmDslNumber": bcmDslNumber,
       "bcmDslRowStatus": bcmDslRowStatus,
       "bcmDslSwitchType": bcmDslSwitchType,
       "bcmDslBChannelCount": bcmDslBChannelCount,
       "bcmDslBChannelType": bcmDslBChannelType,
       "bcmDslMngmtTimer": bcmDslMngmtTimer,
       "bcmDslInfoRate": bcmDslInfoRate,
       "bcmDslSendingProceed": bcmDslSendingProceed,
       "bcmDslInterfaceType": bcmDslInterfaceType,
       "bcmDslBriType": bcmDslBriType,
       "bcmDslPriType": bcmDslPriType,
       "bcmDslNbChannelInUse": bcmDslNbChannelInUse,
       "bcmDslOutGoingCallId": bcmDslOutGoingCallId,
       "bcmDslEffectiveRetries": bcmDslEffectiveRetries,
       "bcmUSapTable": bcmUSapTable,
       "bcmUSapEntry": bcmUSapEntry,
       "bcmUSapNumber": bcmUSapNumber,
       "bcmUSapRowStatus": bcmUSapRowStatus,
       "bcmUSapAlias": bcmUSapAlias,
       "bcmUSapLowDirectoryIndex": bcmUSapLowDirectoryIndex,
       "bcmUSapHighDirectoryIndex": bcmUSapHighDirectoryIndex,
       "bcmUSapAnswerMode": bcmUSapAnswerMode,
       "bcmUSapPermission": bcmUSapPermission,
       "bcmUSapCallTypeAccepted": bcmUSapCallTypeAccepted,
       "bcmUSapSendingProceed": bcmUSapSendingProceed,
       "bcmUSapVoiceInterDigitTimer": bcmUSapVoiceInterDigitTimer,
       "bcmUSapVoiceHuntGroup": bcmUSapVoiceHuntGroup,
       "bcmUSapVoiceHuntDsl": bcmUSapVoiceHuntDsl,
       "bcmUSapVoiceAddressPlan": bcmUSapVoiceAddressPlan,
       "bcmUSapVoiceAddressType": bcmUSapVoiceAddressType,
       "bcmUSapVoiceCodingScheme": bcmUSapVoiceCodingScheme,
       "bcmUSapVoiceCallRoutingMode": bcmUSapVoiceCallRoutingMode,
       "bcmUSapState": bcmUSapState,
       "bcmUSapStatusEvent": bcmUSapStatusEvent,
       "bcmUSapNbChannelBound": bcmUSapNbChannelBound,
       "bcmUSapTotalConnectTime": bcmUSapTotalConnectTime,
       "bcmUSapLastSetupTime": bcmUSapLastSetupTime,
       "bcmUSapLastConnectTime": bcmUSapLastConnectTime,
       "bcmUSapLastDisconnectTime": bcmUSapLastDisconnectTime,
       "bcmUSapLastDisconnectCause": bcmUSapLastDisconnectCause,
       "bcmUSapDslId": bcmUSapDslId,
       "bcmUSapLocalSapId": bcmUSapLocalSapId,
       "bcmUSapSpeedDialDirectoryIndex": bcmUSapSpeedDialDirectoryIndex,
       "bcmUSapVoiceChannelUsed": bcmUSapVoiceChannelUsed,
       "bcmUSapNbSuccessCalls": bcmUSapNbSuccessCalls,
       "bcmUSapNbFailedCalls": bcmUSapNbFailedCalls,
       "bcmUSapNbRefusedCalls": bcmUSapNbRefusedCalls,
       "bcmDirectoryTable": bcmDirectoryTable,
       "bcmDirectoryEntry": bcmDirectoryEntry,
       "bcmDirectoryNumber": bcmDirectoryNumber,
       "bcmDirectoryRowStatus": bcmDirectoryRowStatus,
       "bcmDirectoryAddress": bcmDirectoryAddress,
       "bcmDirectoryAddressPlan": bcmDirectoryAddressPlan,
       "bcmDirectoryAddressType": bcmDirectoryAddressType,
       "bcmDirectorySubAddress": bcmDirectorySubAddress,
       "bcmDirectorySubAddressType": bcmDirectorySubAddressType,
       "bcmDirectorySpid": bcmDirectorySpid,
       "bcmCallHistoryTable": bcmCallHistoryTable,
       "bcmCallHistoryEntry": bcmCallHistoryEntry,
       "bcmCallHistoryUSapNumber": bcmCallHistoryUSapNumber,
       "bcmCallHistoryNumber": bcmCallHistoryNumber,
       "bcmCallHistoryDslChannelUsed": bcmCallHistoryDslChannelUsed,
       "bcmCallHistoryBChannelsUsed": bcmCallHistoryBChannelsUsed,
       "bcmCallHistoryPeerAddress": bcmCallHistoryPeerAddress,
       "bcmCallHistoryPeerSubAddress": bcmCallHistoryPeerSubAddress,
       "bcmCallHistoryOrigin": bcmCallHistoryOrigin,
       "bcmCallHistorySetupTime": bcmCallHistorySetupTime,
       "bcmCallHistoryConnectTime": bcmCallHistoryConnectTime,
       "bcmCallHistoryDisconnectTime": bcmCallHistoryDisconnectTime,
       "bcmDebugTable": bcmDebugTable,
       "bcmDebugEntry": bcmDebugEntry,
       "bcmDebugNumber": bcmDebugNumber,
       "bcmDebugDslCB": bcmDebugDslCB,
       "bcmDebugLSapCB": bcmDebugLSapCB,
       "bcmDebugUSapCB": bcmDebugUSapCB,
       "bcmDebugCallHistoryCB": bcmDebugCallHistoryCB,
       "bcmDebugDataScope": bcmDebugDataScope,
       "bcmDebugDisconnect": bcmDebugDisconnect}
)
