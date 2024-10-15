# SNMP MIB module (CXQLLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXQLLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:48 2024
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
 ThruputClass,
 cxQLLC) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "ThruputClass",
    "cxQLLC")

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


# MODULE-IDENTITY


# Types definitions



class X25Address(DisplayString):
    """Custom type X25Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )





class PacketSize(Integer32):
    """Custom type PacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes16", 4),
          ("bytes2048", 11),
          ("bytes256", 8),
          ("bytes32", 5),
          ("bytes4096", 12),
          ("bytes512", 9),
          ("bytes64", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QllcSapTable_Object = MibTable
qllcSapTable = _QllcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1)
)
if mibBuilder.loadTexts:
    qllcSapTable.setStatus("mandatory")
_QllcSapEntry_Object = MibTableRow
qllcSapEntry = _QllcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1)
)
qllcSapEntry.setIndexNames(
    (0, "CXQLLC-MIB", "qllcSapNumber"),
)
if mibBuilder.loadTexts:
    qllcSapEntry.setStatus("mandatory")
_QllcSapNumber_Type = SapIndex
_QllcSapNumber_Object = MibTableColumn
qllcSapNumber = _QllcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 1),
    _QllcSapNumber_Type()
)
qllcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcSapNumber.setStatus("mandatory")


class _QllcSapRowStatus_Type(Integer32):
    """Custom type qllcSapRowStatus based on Integer32"""
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


_QllcSapRowStatus_Type.__name__ = "Integer32"
_QllcSapRowStatus_Object = MibTableColumn
qllcSapRowStatus = _QllcSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 2),
    _QllcSapRowStatus_Type()
)
qllcSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcSapRowStatus.setStatus("mandatory")


class _QllcSapType_Type(Integer32):
    """Custom type qllcSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_QllcSapType_Type.__name__ = "Integer32"
_QllcSapType_Object = MibTableColumn
qllcSapType = _QllcSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 3),
    _QllcSapType_Type()
)
qllcSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcSapType.setStatus("mandatory")
_QllcSapAlias_Type = Alias
_QllcSapAlias_Object = MibTableColumn
qllcSapAlias = _QllcSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 4),
    _QllcSapAlias_Type()
)
qllcSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcSapAlias.setStatus("mandatory")
_QllcSapCompanionAlias_Type = Alias
_QllcSapCompanionAlias_Object = MibTableColumn
qllcSapCompanionAlias = _QllcSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 5),
    _QllcSapCompanionAlias_Type()
)
qllcSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcSapCompanionAlias.setStatus("mandatory")


class _QllcSapSnalcRef_Type(Integer32):
    """Custom type qllcSapSnalcRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QllcSapSnalcRef_Type.__name__ = "Integer32"
_QllcSapSnalcRef_Object = MibTableColumn
qllcSapSnalcRef = _QllcSapSnalcRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 6),
    _QllcSapSnalcRef_Type()
)
qllcSapSnalcRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcSapSnalcRef.setStatus("mandatory")


class _QllcSapOperationalMode_Type(Integer32):
    """Custom type qllcSapOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_QllcSapOperationalMode_Type.__name__ = "Integer32"
_QllcSapOperationalMode_Object = MibTableColumn
qllcSapOperationalMode = _QllcSapOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 1, 1, 20),
    _QllcSapOperationalMode_Type()
)
qllcSapOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcSapOperationalMode.setStatus("mandatory")
_QllcDteTable_Object = MibTable
qllcDteTable = _QllcDteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2)
)
if mibBuilder.loadTexts:
    qllcDteTable.setStatus("mandatory")
_QllcDteEntry_Object = MibTableRow
qllcDteEntry = _QllcDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1)
)
qllcDteEntry.setIndexNames(
    (0, "CXQLLC-MIB", "qllcDteSap"),
    (0, "CXQLLC-MIB", "qllcDteIndex"),
)
if mibBuilder.loadTexts:
    qllcDteEntry.setStatus("mandatory")
_QllcDteSap_Type = SapIndex
_QllcDteSap_Object = MibTableColumn
qllcDteSap = _QllcDteSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 1),
    _QllcDteSap_Type()
)
qllcDteSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteSap.setStatus("mandatory")


class _QllcDteIndex_Type(Integer32):
    """Custom type qllcDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QllcDteIndex_Type.__name__ = "Integer32"
_QllcDteIndex_Object = MibTableColumn
qllcDteIndex = _QllcDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 2),
    _QllcDteIndex_Type()
)
qllcDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteIndex.setStatus("mandatory")


class _QllcDteRowStatus_Type(Integer32):
    """Custom type qllcDteRowStatus based on Integer32"""
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


_QllcDteRowStatus_Type.__name__ = "Integer32"
_QllcDteRowStatus_Object = MibTableColumn
qllcDteRowStatus = _QllcDteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 3),
    _QllcDteRowStatus_Type()
)
qllcDteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteRowStatus.setStatus("mandatory")


class _QllcDteType_Type(Integer32):
    """Custom type qllcDteType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostInterfaceUnit", 2),
          ("terminalInterfaceUnit", 1))
    )


_QllcDteType_Type.__name__ = "Integer32"
_QllcDteType_Object = MibTableColumn
qllcDteType = _QllcDteType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 4),
    _QllcDteType_Type()
)
qllcDteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteType.setStatus("mandatory")
_QllcDteCalledAddress_Type = X25Address
_QllcDteCalledAddress_Object = MibTableColumn
qllcDteCalledAddress = _QllcDteCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 5),
    _QllcDteCalledAddress_Type()
)
qllcDteCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteCalledAddress.setStatus("mandatory")
_QllcDteCallingAddress_Type = X25Address
_QllcDteCallingAddress_Object = MibTableColumn
qllcDteCallingAddress = _QllcDteCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 6),
    _QllcDteCallingAddress_Type()
)
qllcDteCallingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteCallingAddress.setStatus("mandatory")


class _QllcDteDBitCall_Type(Integer32):
    """Custom type qllcDteDBitCall based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QllcDteDBitCall_Type.__name__ = "Integer32"
_QllcDteDBitCall_Object = MibTableColumn
qllcDteDBitCall = _QllcDteDBitCall_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 7),
    _QllcDteDBitCall_Type()
)
qllcDteDBitCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteDBitCall.setStatus("mandatory")


class _QllcDteWindow_Type(Integer32):
    """Custom type qllcDteWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_QllcDteWindow_Type.__name__ = "Integer32"
_QllcDteWindow_Object = MibTableColumn
qllcDteWindow = _QllcDteWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 8),
    _QllcDteWindow_Type()
)
qllcDteWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteWindow.setStatus("mandatory")


class _QllcDtePacketSize_Type(PacketSize):
    """Custom type qllcDtePacketSize based on PacketSize"""


_QllcDtePacketSize_Object = MibTableColumn
qllcDtePacketSize = _QllcDtePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 9),
    _QllcDtePacketSize_Type()
)
qllcDtePacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDtePacketSize.setStatus("mandatory")


class _QllcDteThroughput_Type(ThruputClass):
    """Custom type qllcDteThroughput based on ThruputClass"""


_QllcDteThroughput_Object = MibTableColumn
qllcDteThroughput = _QllcDteThroughput_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 10),
    _QllcDteThroughput_Type()
)
qllcDteThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteThroughput.setStatus("mandatory")


class _QllcDteUserData_Type(DisplayString):
    """Custom type qllcDteUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_QllcDteUserData_Type.__name__ = "DisplayString"
_QllcDteUserData_Object = MibTableColumn
qllcDteUserData = _QllcDteUserData_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 11),
    _QllcDteUserData_Type()
)
qllcDteUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteUserData.setStatus("mandatory")
_QllcDteFacility_Type = OctetString
_QllcDteFacility_Object = MibTableColumn
qllcDteFacility = _QllcDteFacility_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 12),
    _QllcDteFacility_Type()
)
qllcDteFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteFacility.setStatus("mandatory")


class _QllcDteMemotec_Type(Integer32):
    """Custom type qllcDteMemotec based on Integer32"""
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
        *(("cx900", 2),
          ("legacy", 3),
          ("nonmemotec", 1),
          ("pvc", 4))
    )


_QllcDteMemotec_Type.__name__ = "Integer32"
_QllcDteMemotec_Object = MibTableColumn
qllcDteMemotec = _QllcDteMemotec_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 13),
    _QllcDteMemotec_Type()
)
qllcDteMemotec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteMemotec.setStatus("mandatory")


class _QllcDtePvc_Type(Integer32):
    """Custom type qllcDtePvc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_QllcDtePvc_Type.__name__ = "Integer32"
_QllcDtePvc_Object = MibTableColumn
qllcDtePvc = _QllcDtePvc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 14),
    _QllcDtePvc_Type()
)
qllcDtePvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDtePvc.setStatus("mandatory")


class _QllcDteConnectMethod_Type(Integer32):
    """Custom type qllcDteConnectMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callingaddress", 2),
          ("userdata", 1))
    )


_QllcDteConnectMethod_Type.__name__ = "Integer32"
_QllcDteConnectMethod_Object = MibTableColumn
qllcDteConnectMethod = _QllcDteConnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 15),
    _QllcDteConnectMethod_Type()
)
qllcDteConnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qllcDteConnectMethod.setStatus("mandatory")


class _QllcDteControl_Type(Integer32):
    """Custom type qllcDteControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_QllcDteControl_Type.__name__ = "Integer32"
_QllcDteControl_Object = MibTableColumn
qllcDteControl = _QllcDteControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 20),
    _QllcDteControl_Type()
)
qllcDteControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    qllcDteControl.setStatus("mandatory")


class _QllcDteStatus_Type(Integer32):
    """Custom type qllcDteStatus based on Integer32"""
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
        *(("connected", 1),
          ("disconnected", 3),
          ("pendingConnect", 2),
          ("pendingDisconnect", 4))
    )


_QllcDteStatus_Type.__name__ = "Integer32"
_QllcDteStatus_Object = MibTableColumn
qllcDteStatus = _QllcDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 30),
    _QllcDteStatus_Type()
)
qllcDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteStatus.setStatus("mandatory")


class _QllcDteOperationalMode_Type(Integer32):
    """Custom type qllcDteOperationalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_QllcDteOperationalMode_Type.__name__ = "Integer32"
_QllcDteOperationalMode_Object = MibTableColumn
qllcDteOperationalMode = _QllcDteOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 31),
    _QllcDteOperationalMode_Type()
)
qllcDteOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteOperationalMode.setStatus("mandatory")


class _QllcDteState_Type(Integer32):
    """Custom type qllcDteState based on Integer32"""
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
        *(("closed", 2),
          ("disc", 9),
          ("opened", 1),
          ("reqdisc", 10),
          ("reset", 7),
          ("setmode", 8),
          ("tstcmd", 4),
          ("tstrsp", 6),
          ("unknown", 11),
          ("xidcmd", 3),
          ("xidrsp", 5))
    )


_QllcDteState_Type.__name__ = "Integer32"
_QllcDteState_Object = MibTableColumn
qllcDteState = _QllcDteState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 32),
    _QllcDteState_Type()
)
qllcDteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteState.setStatus("mandatory")


class _QllcDteConnectionType_Type(Integer32):
    """Custom type qllcDteConnectionType based on Integer32"""
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
          ("pvc", 3),
          ("svc", 2))
    )


_QllcDteConnectionType_Type.__name__ = "Integer32"
_QllcDteConnectionType_Object = MibTableColumn
qllcDteConnectionType = _QllcDteConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 33),
    _QllcDteConnectionType_Type()
)
qllcDteConnectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteConnectionType.setStatus("mandatory")
_QllcDteCalls_Type = Counter32
_QllcDteCalls_Object = MibTableColumn
qllcDteCalls = _QllcDteCalls_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 40),
    _QllcDteCalls_Type()
)
qllcDteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteCalls.setStatus("mandatory")
_QllcDteClears_Type = Counter32
_QllcDteClears_Object = MibTableColumn
qllcDteClears = _QllcDteClears_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 41),
    _QllcDteClears_Type()
)
qllcDteClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteClears.setStatus("mandatory")
_QllcDteTxPackets_Type = Counter32
_QllcDteTxPackets_Object = MibTableColumn
qllcDteTxPackets = _QllcDteTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 42),
    _QllcDteTxPackets_Type()
)
qllcDteTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteTxPackets.setStatus("mandatory")
_QllcDteRxPackets_Type = Counter32
_QllcDteRxPackets_Object = MibTableColumn
qllcDteRxPackets = _QllcDteRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 43),
    _QllcDteRxPackets_Type()
)
qllcDteRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteRxPackets.setStatus("mandatory")
_QllcDteQdc_Type = Counter32
_QllcDteQdc_Object = MibTableColumn
qllcDteQdc = _QllcDteQdc_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 44),
    _QllcDteQdc_Type()
)
qllcDteQdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteQdc.setStatus("mandatory")
_QllcDteQxid_Type = Counter32
_QllcDteQxid_Object = MibTableColumn
qllcDteQxid = _QllcDteQxid_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 45),
    _QllcDteQxid_Type()
)
qllcDteQxid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteQxid.setStatus("mandatory")
_QllcDteQua_Type = Counter32
_QllcDteQua_Object = MibTableColumn
qllcDteQua = _QllcDteQua_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 46),
    _QllcDteQua_Type()
)
qllcDteQua.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteQua.setStatus("mandatory")
_QllcDteQsm_Type = Counter32
_QllcDteQsm_Object = MibTableColumn
qllcDteQsm = _QllcDteQsm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 47),
    _QllcDteQsm_Type()
)
qllcDteQsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteQsm.setStatus("mandatory")
_QllcDteX25Reset_Type = Counter32
_QllcDteX25Reset_Object = MibTableColumn
qllcDteX25Reset = _QllcDteX25Reset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 48),
    _QllcDteX25Reset_Type()
)
qllcDteX25Reset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteX25Reset.setStatus("mandatory")
_QllcDteSnalcRnr_Type = Counter32
_QllcDteSnalcRnr_Object = MibTableColumn
qllcDteSnalcRnr = _QllcDteSnalcRnr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 49),
    _QllcDteSnalcRnr_Type()
)
qllcDteSnalcRnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteSnalcRnr.setStatus("mandatory")
_QllcDteSnalcRr_Type = Counter32
_QllcDteSnalcRr_Object = MibTableColumn
qllcDteSnalcRr = _QllcDteSnalcRr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 50),
    _QllcDteSnalcRr_Type()
)
qllcDteSnalcRr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteSnalcRr.setStatus("mandatory")
_QllcDteX25Rnr_Type = Counter32
_QllcDteX25Rnr_Object = MibTableColumn
qllcDteX25Rnr = _QllcDteX25Rnr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 51),
    _QllcDteX25Rnr_Type()
)
qllcDteX25Rnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteX25Rnr.setStatus("mandatory")
_QllcDteX25Rr_Type = Counter32
_QllcDteX25Rr_Object = MibTableColumn
qllcDteX25Rr = _QllcDteX25Rr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 2, 1, 52),
    _QllcDteX25Rr_Type()
)
qllcDteX25Rr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcDteX25Rr.setStatus("mandatory")


class _QllcMibLevel_Type(Integer32):
    """Custom type qllcMibLevel based on Integer32"""
    defaultValue = 0


_QllcMibLevel_Object = MibScalar
qllcMibLevel = _QllcMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 38, 3),
    _QllcMibLevel_Type()
)
qllcMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qllcMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXQLLC-MIB",
    **{"X25Address": X25Address,
       "PacketSize": PacketSize,
       "qllcSapTable": qllcSapTable,
       "qllcSapEntry": qllcSapEntry,
       "qllcSapNumber": qllcSapNumber,
       "qllcSapRowStatus": qllcSapRowStatus,
       "qllcSapType": qllcSapType,
       "qllcSapAlias": qllcSapAlias,
       "qllcSapCompanionAlias": qllcSapCompanionAlias,
       "qllcSapSnalcRef": qllcSapSnalcRef,
       "qllcSapOperationalMode": qllcSapOperationalMode,
       "qllcDteTable": qllcDteTable,
       "qllcDteEntry": qllcDteEntry,
       "qllcDteSap": qllcDteSap,
       "qllcDteIndex": qllcDteIndex,
       "qllcDteRowStatus": qllcDteRowStatus,
       "qllcDteType": qllcDteType,
       "qllcDteCalledAddress": qllcDteCalledAddress,
       "qllcDteCallingAddress": qllcDteCallingAddress,
       "qllcDteDBitCall": qllcDteDBitCall,
       "qllcDteWindow": qllcDteWindow,
       "qllcDtePacketSize": qllcDtePacketSize,
       "qllcDteThroughput": qllcDteThroughput,
       "qllcDteUserData": qllcDteUserData,
       "qllcDteFacility": qllcDteFacility,
       "qllcDteMemotec": qllcDteMemotec,
       "qllcDtePvc": qllcDtePvc,
       "qllcDteConnectMethod": qllcDteConnectMethod,
       "qllcDteControl": qllcDteControl,
       "qllcDteStatus": qllcDteStatus,
       "qllcDteOperationalMode": qllcDteOperationalMode,
       "qllcDteState": qllcDteState,
       "qllcDteConnectionType": qllcDteConnectionType,
       "qllcDteCalls": qllcDteCalls,
       "qllcDteClears": qllcDteClears,
       "qllcDteTxPackets": qllcDteTxPackets,
       "qllcDteRxPackets": qllcDteRxPackets,
       "qllcDteQdc": qllcDteQdc,
       "qllcDteQxid": qllcDteQxid,
       "qllcDteQua": qllcDteQua,
       "qllcDteQsm": qllcDteQsm,
       "qllcDteX25Reset": qllcDteX25Reset,
       "qllcDteSnalcRnr": qllcDteSnalcRnr,
       "qllcDteSnalcRr": qllcDteSnalcRr,
       "qllcDteX25Rnr": qllcDteX25Rnr,
       "qllcDteX25Rr": qllcDteX25Rr,
       "qllcMibLevel": qllcMibLevel}
)
