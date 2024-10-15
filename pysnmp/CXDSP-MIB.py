# SNMP MIB module (CXDSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXDSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:18 2024
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
 cxDsp) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxDsp")

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





class DspCuAddress(Integer32):
    """Custom type DspCuAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )





class DspDevAddress(Integer32):
    """Custom type DspDevAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )





class DspRowStatus(Integer32):
    """Custom type DspRowStatus based on Integer32"""
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





class DspCircuitType(Integer32):
    """Custom type DspCircuitType based on Integer32"""
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
        *(("mes-usr-reqcirc", 4),
          ("multuser-reqcirc", 3),
          ("singusr-noreqcirc", 1),
          ("singusr-reqcirc", 2))
    )





class DspOperationalMode(Integer32):
    """Custom type DspOperationalMode based on Integer32"""
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





class DspPartner(Integer32):
    """Custom type DspPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host-terminal", 2),
          ("terminal-terminal", 1))
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





class ThruputClass(Integer32):
    """Custom type ThruputClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
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
        *(("bps1200", 7),
          ("bps150", 4),
          ("bps19200", 11),
          ("bps2400", 8),
          ("bps300", 5),
          ("bps38400", 12),
          ("bps4800", 9),
          ("bps600", 6),
          ("bps64000", 13),
          ("bps75", 3),
          ("bps9600", 10))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DspSapTable_Object = MibTable
dspSapTable = _DspSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1)
)
if mibBuilder.loadTexts:
    dspSapTable.setStatus("mandatory")
_DspSapEntry_Object = MibTableRow
dspSapEntry = _DspSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1)
)
dspSapEntry.setIndexNames(
    (0, "CXDSP-MIB", "dspSapNumber"),
)
if mibBuilder.loadTexts:
    dspSapEntry.setStatus("mandatory")
_DspSapNumber_Type = SapIndex
_DspSapNumber_Object = MibTableColumn
dspSapNumber = _DspSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 1),
    _DspSapNumber_Type()
)
dspSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspSapNumber.setStatus("mandatory")
_DspSapRowStatus_Type = DspRowStatus
_DspSapRowStatus_Object = MibTableColumn
dspSapRowStatus = _DspSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 2),
    _DspSapRowStatus_Type()
)
dspSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapRowStatus.setStatus("mandatory")


class _DspSapType_Type(Integer32):
    """Custom type dspSapType based on Integer32"""
    defaultValue = 1

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


_DspSapType_Type.__name__ = "Integer32"
_DspSapType_Object = MibTableColumn
dspSapType = _DspSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 3),
    _DspSapType_Type()
)
dspSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapType.setStatus("mandatory")
_DspSapAlias_Type = Alias
_DspSapAlias_Object = MibTableColumn
dspSapAlias = _DspSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 4),
    _DspSapAlias_Type()
)
dspSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapAlias.setStatus("mandatory")
_DspSapCompanionAlias_Type = Alias
_DspSapCompanionAlias_Object = MibTableColumn
dspSapCompanionAlias = _DspSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 5),
    _DspSapCompanionAlias_Type()
)
dspSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapCompanionAlias.setStatus("mandatory")


class _DspSapSnalcRef_Type(Integer32):
    """Custom type dspSapSnalcRef based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DspSapSnalcRef_Type.__name__ = "Integer32"
_DspSapSnalcRef_Object = MibTableColumn
dspSapSnalcRef = _DspSapSnalcRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 6),
    _DspSapSnalcRef_Type()
)
dspSapSnalcRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapSnalcRef.setStatus("mandatory")


class _DspSapEbcdicAsciiMode_Type(Integer32):
    """Custom type dspSapEbcdicAsciiMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asciiMode", 2),
          ("encdicMode", 1))
    )


_DspSapEbcdicAsciiMode_Type.__name__ = "Integer32"
_DspSapEbcdicAsciiMode_Object = MibTableColumn
dspSapEbcdicAsciiMode = _DspSapEbcdicAsciiMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 7),
    _DspSapEbcdicAsciiMode_Type()
)
dspSapEbcdicAsciiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspSapEbcdicAsciiMode.setStatus("mandatory")


class _DspSapControl_Type(Integer32):
    """Custom type dspSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_DspSapControl_Type.__name__ = "Integer32"
_DspSapControl_Object = MibTableColumn
dspSapControl = _DspSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 20),
    _DspSapControl_Type()
)
dspSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dspSapControl.setStatus("mandatory")
_DspSapOperationalMode_Type = DspOperationalMode
_DspSapOperationalMode_Object = MibTableColumn
dspSapOperationalMode = _DspSapOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 1, 1, 30),
    _DspSapOperationalMode_Type()
)
dspSapOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspSapOperationalMode.setStatus("mandatory")
_DspCuTable_Object = MibTable
dspCuTable = _DspCuTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2)
)
if mibBuilder.loadTexts:
    dspCuTable.setStatus("mandatory")
_DspCuEntry_Object = MibTableRow
dspCuEntry = _DspCuEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1)
)
dspCuEntry.setIndexNames(
    (0, "CXDSP-MIB", "dspCuSapNumber"),
    (0, "CXDSP-MIB", "dspCuAddress"),
)
if mibBuilder.loadTexts:
    dspCuEntry.setStatus("mandatory")
_DspCuSapNumber_Type = SapIndex
_DspCuSapNumber_Object = MibTableColumn
dspCuSapNumber = _DspCuSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 1),
    _DspCuSapNumber_Type()
)
dspCuSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuSapNumber.setStatus("mandatory")
_DspCuAddress_Type = DspCuAddress
_DspCuAddress_Object = MibTableColumn
dspCuAddress = _DspCuAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 2),
    _DspCuAddress_Type()
)
dspCuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuAddress.setStatus("mandatory")
_DspCuRowStatus_Type = DspRowStatus
_DspCuRowStatus_Object = MibTableColumn
dspCuRowStatus = _DspCuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 3),
    _DspCuRowStatus_Type()
)
dspCuRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuRowStatus.setStatus("mandatory")


class _DspCuType_Type(Integer32):
    """Custom type dspCuType based on Integer32"""
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
          ("termInterfaceUnit", 1))
    )


_DspCuType_Type.__name__ = "Integer32"
_DspCuType_Object = MibTableColumn
dspCuType = _DspCuType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 4),
    _DspCuType_Type()
)
dspCuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuType.setStatus("mandatory")
_DspCuCallingX25Address_Type = X25Address
_DspCuCallingX25Address_Object = MibTableColumn
dspCuCallingX25Address = _DspCuCallingX25Address_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 5),
    _DspCuCallingX25Address_Type()
)
dspCuCallingX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuCallingX25Address.setStatus("mandatory")
_DspCuCalledX25Address_Type = X25Address
_DspCuCalledX25Address_Object = MibTableColumn
dspCuCalledX25Address = _DspCuCalledX25Address_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 6),
    _DspCuCalledX25Address_Type()
)
dspCuCalledX25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuCalledX25Address.setStatus("mandatory")


class _DspCuDSPCircuitType_Type(DspCircuitType):
    """Custom type dspCuDSPCircuitType based on DspCircuitType"""


_DspCuDSPCircuitType_Object = MibTableColumn
dspCuDSPCircuitType = _DspCuDSPCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 8),
    _DspCuDSPCircuitType_Type()
)
dspCuDSPCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuDSPCircuitType.setStatus("mandatory")


class _DspCuWindow_Type(Integer32):
    """Custom type dspCuWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DspCuWindow_Type.__name__ = "Integer32"
_DspCuWindow_Object = MibTableColumn
dspCuWindow = _DspCuWindow_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 9),
    _DspCuWindow_Type()
)
dspCuWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuWindow.setStatus("mandatory")


class _DspCuUserData_Type(DisplayString):
    """Custom type dspCuUserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DspCuUserData_Type.__name__ = "DisplayString"
_DspCuUserData_Object = MibTableColumn
dspCuUserData = _DspCuUserData_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 10),
    _DspCuUserData_Type()
)
dspCuUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuUserData.setStatus("mandatory")
_DspCuFacility_Type = OctetString
_DspCuFacility_Object = MibTableColumn
dspCuFacility = _DspCuFacility_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 11),
    _DspCuFacility_Type()
)
dspCuFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuFacility.setStatus("mandatory")


class _DspCuApplicationId_Type(Integer32):
    """Custom type dspCuApplicationId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspCuApplicationId_Type.__name__ = "Integer32"
_DspCuApplicationId_Object = MibTableColumn
dspCuApplicationId = _DspCuApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 12),
    _DspCuApplicationId_Type()
)
dspCuApplicationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuApplicationId.setStatus("mandatory")


class _DspCuReqMode_Type(Integer32):
    """Custom type dspCuReqMode based on Integer32"""
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
        *(("associateDeviceCrm", 4),
          ("fixedClassCrm", 1),
          ("nonSpecificClassCrm", 3),
          ("specificClassCrm", 2))
    )


_DspCuReqMode_Type.__name__ = "Integer32"
_DspCuReqMode_Object = MibTableColumn
dspCuReqMode = _DspCuReqMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 13),
    _DspCuReqMode_Type()
)
dspCuReqMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuReqMode.setStatus("mandatory")


class _DspCuPacketSize_Type(PacketSize):
    """Custom type dspCuPacketSize based on PacketSize"""


_DspCuPacketSize_Object = MibTableColumn
dspCuPacketSize = _DspCuPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 14),
    _DspCuPacketSize_Type()
)
dspCuPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuPacketSize.setStatus("mandatory")


class _DspCuThroughput_Type(ThruputClass):
    """Custom type dspCuThroughput based on ThruputClass"""


_DspCuThroughput_Object = MibTableColumn
dspCuThroughput = _DspCuThroughput_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 15),
    _DspCuThroughput_Type()
)
dspCuThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuThroughput.setStatus("mandatory")


class _DspCuPartner_Type(DspPartner):
    """Custom type dspCuPartner based on DspPartner"""


_DspCuPartner_Object = MibTableColumn
dspCuPartner = _DspCuPartner_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 16),
    _DspCuPartner_Type()
)
dspCuPartner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspCuPartner.setStatus("mandatory")


class _DspCuControl_Type(Integer32):
    """Custom type dspCuControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_DspCuControl_Type.__name__ = "Integer32"
_DspCuControl_Object = MibTableColumn
dspCuControl = _DspCuControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 25),
    _DspCuControl_Type()
)
dspCuControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dspCuControl.setStatus("mandatory")


class _DspCuState_Type(Integer32):
    """Custom type dspCuState based on Integer32"""
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
        *(("idle", 1),
          ("unknown", 5),
          ("x25-connected", 4),
          ("x25-connecting", 2),
          ("x25-wait-endtoend", 3))
    )


_DspCuState_Type.__name__ = "Integer32"
_DspCuState_Object = MibTableColumn
dspCuState = _DspCuState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 30),
    _DspCuState_Type()
)
dspCuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuState.setStatus("mandatory")
_DspCuOperationalMode_Type = DspOperationalMode
_DspCuOperationalMode_Object = MibTableColumn
dspCuOperationalMode = _DspCuOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 31),
    _DspCuOperationalMode_Type()
)
dspCuOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuOperationalMode.setStatus("mandatory")
_DspCuX25CallRequest_Type = Counter32
_DspCuX25CallRequest_Object = MibTableColumn
dspCuX25CallRequest = _DspCuX25CallRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 40),
    _DspCuX25CallRequest_Type()
)
dspCuX25CallRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuX25CallRequest.setStatus("mandatory")
_DspCuX25CallAccept_Type = Counter32
_DspCuX25CallAccept_Object = MibTableColumn
dspCuX25CallAccept = _DspCuX25CallAccept_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 41),
    _DspCuX25CallAccept_Type()
)
dspCuX25CallAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuX25CallAccept.setStatus("mandatory")
_DspCuClears_Type = Counter32
_DspCuClears_Object = MibTableColumn
dspCuClears = _DspCuClears_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 42),
    _DspCuClears_Type()
)
dspCuClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuClears.setStatus("mandatory")
_DspCuClearsInd_Type = Counter32
_DspCuClearsInd_Object = MibTableColumn
dspCuClearsInd = _DspCuClearsInd_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 43),
    _DspCuClearsInd_Type()
)
dspCuClearsInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuClearsInd.setStatus("mandatory")
_DspCuInvToClear_Type = Counter32
_DspCuInvToClear_Object = MibTableColumn
dspCuInvToClear = _DspCuInvToClear_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 2, 1, 44),
    _DspCuInvToClear_Type()
)
dspCuInvToClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspCuInvToClear.setStatus("mandatory")
_DspDevTable_Object = MibTable
dspDevTable = _DspDevTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3)
)
if mibBuilder.loadTexts:
    dspDevTable.setStatus("mandatory")
_DspDevEntry_Object = MibTableRow
dspDevEntry = _DspDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1)
)
dspDevEntry.setIndexNames(
    (0, "CXDSP-MIB", "dspDevSapNumber"),
    (0, "CXDSP-MIB", "dspDevCuAddress"),
    (0, "CXDSP-MIB", "dspDevAddress"),
)
if mibBuilder.loadTexts:
    dspDevEntry.setStatus("mandatory")
_DspDevSapNumber_Type = SapIndex
_DspDevSapNumber_Object = MibTableColumn
dspDevSapNumber = _DspDevSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 1),
    _DspDevSapNumber_Type()
)
dspDevSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevSapNumber.setStatus("mandatory")
_DspDevCuAddress_Type = DspCuAddress
_DspDevCuAddress_Object = MibTableColumn
dspDevCuAddress = _DspDevCuAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 2),
    _DspDevCuAddress_Type()
)
dspDevCuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCuAddress.setStatus("mandatory")
_DspDevAddress_Type = DspDevAddress
_DspDevAddress_Object = MibTableColumn
dspDevAddress = _DspDevAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 3),
    _DspDevAddress_Type()
)
dspDevAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevAddress.setStatus("mandatory")


class _DspDevRowStatus_Type(Integer32):
    """Custom type dspDevRowStatus based on Integer32"""
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


_DspDevRowStatus_Type.__name__ = "Integer32"
_DspDevRowStatus_Object = MibTableColumn
dspDevRowStatus = _DspDevRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 4),
    _DspDevRowStatus_Type()
)
dspDevRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevRowStatus.setStatus("mandatory")


class _DspDevUCN_Type(Integer32):
    """Custom type dspDevUCN based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DspDevUCN_Type.__name__ = "Integer32"
_DspDevUCN_Object = MibTableColumn
dspDevUCN = _DspDevUCN_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 5),
    _DspDevUCN_Type()
)
dspDevUCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevUCN.setStatus("mandatory")


class _DspDevRemoteCuAddress_Type(DspCuAddress):
    """Custom type dspDevRemoteCuAddress based on DspCuAddress"""
    defaultValue = 0


_DspDevRemoteCuAddress_Object = MibTableColumn
dspDevRemoteCuAddress = _DspDevRemoteCuAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 6),
    _DspDevRemoteCuAddress_Type()
)
dspDevRemoteCuAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevRemoteCuAddress.setStatus("mandatory")


class _DspDevRemoteDevAddress_Type(DspDevAddress):
    """Custom type dspDevRemoteDevAddress based on DspDevAddress"""
    defaultValue = 0


_DspDevRemoteDevAddress_Object = MibTableColumn
dspDevRemoteDevAddress = _DspDevRemoteDevAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 7),
    _DspDevRemoteDevAddress_Type()
)
dspDevRemoteDevAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevRemoteDevAddress.setStatus("mandatory")


class _DspDevFormatSize_Type(Integer32):
    """Custom type dspDevFormatSize based on Integer32"""
    defaultValue = 5

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
        *(("char1920", 3),
          ("char2560", 4),
          ("char3440", 5),
          ("char3564", 6),
          ("char480", 1),
          ("char960", 2),
          ("charReserved1", 7),
          ("charReserved2", 8))
    )


_DspDevFormatSize_Type.__name__ = "Integer32"
_DspDevFormatSize_Object = MibTableColumn
dspDevFormatSize = _DspDevFormatSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 8),
    _DspDevFormatSize_Type()
)
dspDevFormatSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevFormatSize.setStatus("mandatory")


class _DspDevAttPrnt_Type(Integer32):
    """Custom type dspDevAttPrnt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPrinterAttached", 1),
          ("printerAttached", 2))
    )


_DspDevAttPrnt_Type.__name__ = "Integer32"
_DspDevAttPrnt_Object = MibTableColumn
dspDevAttPrnt = _DspDevAttPrnt_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 9),
    _DspDevAttPrnt_Type()
)
dspDevAttPrnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevAttPrnt.setStatus("mandatory")


class _DspDevCharSet_Type(Integer32):
    """Custom type dspDevCharSet based on Integer32"""
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
        *(("aplCharSet", 2),
          ("aplTextCharSet", 4),
          ("noneCharSet", 1),
          ("textCharSet", 3))
    )


_DspDevCharSet_Type.__name__ = "Integer32"
_DspDevCharSet_Object = MibTableColumn
dspDevCharSet = _DspDevCharSet_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 10),
    _DspDevCharSet_Type()
)
dspDevCharSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevCharSet.setStatus("mandatory")


class _DspDevColour_Type(Integer32):
    """Custom type dspDevColour based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colourSuport", 1),
          ("noColourSuport", 2))
    )


_DspDevColour_Type.__name__ = "Integer32"
_DspDevColour_Object = MibTableColumn
dspDevColour = _DspDevColour_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 11),
    _DspDevColour_Type()
)
dspDevColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevColour.setStatus("mandatory")


class _DspDevTTextSupport_Type(Integer32):
    """Custom type dspDevTTextSupport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonTransparentText", 2),
          ("transparentText", 1))
    )


_DspDevTTextSupport_Type.__name__ = "Integer32"
_DspDevTTextSupport_Object = MibTableColumn
dspDevTTextSupport = _DspDevTTextSupport_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 12),
    _DspDevTTextSupport_Type()
)
dspDevTTextSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevTTextSupport.setStatus("mandatory")


class _DspDevDPmode_Type(Integer32):
    """Custom type dspDevDPmode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("display", 1),
          ("printer", 2))
    )


_DspDevDPmode_Type.__name__ = "Integer32"
_DspDevDPmode_Object = MibTableColumn
dspDevDPmode = _DspDevDPmode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 13),
    _DspDevDPmode_Type()
)
dspDevDPmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspDevDPmode.setStatus("mandatory")


class _DspDevControl_Type(Integer32):
    """Custom type dspDevControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_DspDevControl_Type.__name__ = "Integer32"
_DspDevControl_Object = MibTableColumn
dspDevControl = _DspDevControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 20),
    _DspDevControl_Type()
)
dspDevControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dspDevControl.setStatus("mandatory")
_DspDevOperationalMode_Type = DspOperationalMode
_DspDevOperationalMode_Object = MibTableColumn
dspDevOperationalMode = _DspDevOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 30),
    _DspDevOperationalMode_Type()
)
dspDevOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevOperationalMode.setStatus("mandatory")


class _DspDevState_Type(Integer32):
    """Custom type dspDevState based on Integer32"""
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
        *(("connected", 6),
          ("disconnecting", 7),
          ("idle", 1),
          ("wait-circuit-enabled", 4),
          ("wait-circuit-request", 3),
          ("wait-status", 5),
          ("x25-connected", 2))
    )


_DspDevState_Type.__name__ = "Integer32"
_DspDevState_Object = MibTableColumn
dspDevState = _DspDevState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 31),
    _DspDevState_Type()
)
dspDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevState.setStatus("mandatory")
_DspDevStatus_Type = Integer32
_DspDevStatus_Object = MibTableColumn
dspDevStatus = _DspDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 32),
    _DspDevStatus_Type()
)
dspDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevStatus.setStatus("mandatory")
_DspDevSense_Type = Integer32
_DspDevSense_Object = MibTableColumn
dspDevSense = _DspDevSense_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 33),
    _DspDevSense_Type()
)
dspDevSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevSense.setStatus("mandatory")
_DspDevCommand_Type = Counter32
_DspDevCommand_Object = MibTableColumn
dspDevCommand = _DspDevCommand_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 41),
    _DspDevCommand_Type()
)
dspDevCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCommand.setStatus("mandatory")
_DspDevResponse_Type = Counter32
_DspDevResponse_Object = MibTableColumn
dspDevResponse = _DspDevResponse_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 42),
    _DspDevResponse_Type()
)
dspDevResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevResponse.setStatus("mandatory")
_DspDevCmdRspUndel_Type = Counter32
_DspDevCmdRspUndel_Object = MibTableColumn
dspDevCmdRspUndel = _DspDevCmdRspUndel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 43),
    _DspDevCmdRspUndel_Type()
)
dspDevCmdRspUndel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCmdRspUndel.setStatus("mandatory")


class _DspDevCmdRspUndelReason_Type(Integer32):
    """Custom type dspDevCmdRspUndelReason based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("eot", 1),
          ("ff", 3),
          ("invalid", 8),
          ("nak", 5),
          ("reserved", 7),
          ("rvi", 2),
          ("timeout", 4),
          ("ur", 9),
          ("wack", 6))
    )


_DspDevCmdRspUndelReason_Type.__name__ = "Integer32"
_DspDevCmdRspUndelReason_Object = MibTableColumn
dspDevCmdRspUndelReason = _DspDevCmdRspUndelReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 44),
    _DspDevCmdRspUndelReason_Type()
)
dspDevCmdRspUndelReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCmdRspUndelReason.setStatus("mandatory")
_DspDevCmdRspAbort_Type = Counter32
_DspDevCmdRspAbort_Object = MibTableColumn
dspDevCmdRspAbort = _DspDevCmdRspAbort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 45),
    _DspDevCmdRspAbort_Type()
)
dspDevCmdRspAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCmdRspAbort.setStatus("mandatory")


class _DspDevCmdRspAbortReason_Type(Integer32):
    """Custom type dspDevCmdRspAbortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ff", 3),
          ("nak", 5),
          ("ste", 10),
          ("timeout", 4))
    )


_DspDevCmdRspAbortReason_Type.__name__ = "Integer32"
_DspDevCmdRspAbortReason_Object = MibTableColumn
dspDevCmdRspAbortReason = _DspDevCmdRspAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 46),
    _DspDevCmdRspAbortReason_Type()
)
dspDevCmdRspAbortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCmdRspAbortReason.setStatus("mandatory")
_DspDevStatStatus_Type = Counter32
_DspDevStatStatus_Object = MibTableColumn
dspDevStatStatus = _DspDevStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 47),
    _DspDevStatStatus_Type()
)
dspDevStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevStatStatus.setStatus("mandatory")
_DspDevAck_Type = Counter32
_DspDevAck_Object = MibTableColumn
dspDevAck = _DspDevAck_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 48),
    _DspDevAck_Type()
)
dspDevAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevAck.setStatus("mandatory")
_DspDevInvToClear_Type = Counter32
_DspDevInvToClear_Object = MibTableColumn
dspDevInvToClear = _DspDevInvToClear_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 49),
    _DspDevInvToClear_Type()
)
dspDevInvToClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevInvToClear.setStatus("mandatory")


class _DspDevInvClearReason_Type(Integer32):
    """Custom type dspDevInvClearReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              17,
              18,
              19,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("facility", 33),
          ("invDataFormat", 19),
          ("invDqFormat", 18),
          ("invStateTrans", 17),
          ("timeout", 32),
          ("unidentPkt", 16),
          ("userInitiated", 1))
    )


_DspDevInvClearReason_Type.__name__ = "Integer32"
_DspDevInvClearReason_Object = MibTableColumn
dspDevInvClearReason = _DspDevInvClearReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 50),
    _DspDevInvClearReason_Type()
)
dspDevInvClearReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevInvClearReason.setStatus("mandatory")
_DspDevReset_Type = Counter32
_DspDevReset_Object = MibTableColumn
dspDevReset = _DspDevReset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 51),
    _DspDevReset_Type()
)
dspDevReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevReset.setStatus("mandatory")


class _DspDevResetReason_Type(Integer32):
    """Custom type dspDevResetReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("invDataFormat", 19),
          ("invDqFormat", 18),
          ("seqErr", 17),
          ("unidentDqPkt", 16))
    )


_DspDevResetReason_Type.__name__ = "Integer32"
_DspDevResetReason_Object = MibTableColumn
dspDevResetReason = _DspDevResetReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 52),
    _DspDevResetReason_Type()
)
dspDevResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevResetReason.setStatus("mandatory")
_DspDevCircuitEnabled_Type = Counter32
_DspDevCircuitEnabled_Object = MibTableColumn
dspDevCircuitEnabled = _DspDevCircuitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 53),
    _DspDevCircuitEnabled_Type()
)
dspDevCircuitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCircuitEnabled.setStatus("mandatory")
_DspDevCircuitRequest_Type = Counter32
_DspDevCircuitRequest_Object = MibTableColumn
dspDevCircuitRequest = _DspDevCircuitRequest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 54),
    _DspDevCircuitRequest_Type()
)
dspDevCircuitRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCircuitRequest.setStatus("mandatory")
_DspDevCircuitDisconnect_Type = Counter32
_DspDevCircuitDisconnect_Object = MibTableColumn
dspDevCircuitDisconnect = _DspDevCircuitDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 57, 3, 1, 55),
    _DspDevCircuitDisconnect_Type()
)
dspDevCircuitDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspDevCircuitDisconnect.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXDSP-MIB",
    **{"X25Address": X25Address,
       "DspCuAddress": DspCuAddress,
       "DspDevAddress": DspDevAddress,
       "DspRowStatus": DspRowStatus,
       "DspCircuitType": DspCircuitType,
       "DspOperationalMode": DspOperationalMode,
       "DspPartner": DspPartner,
       "PacketSize": PacketSize,
       "ThruputClass": ThruputClass,
       "dspSapTable": dspSapTable,
       "dspSapEntry": dspSapEntry,
       "dspSapNumber": dspSapNumber,
       "dspSapRowStatus": dspSapRowStatus,
       "dspSapType": dspSapType,
       "dspSapAlias": dspSapAlias,
       "dspSapCompanionAlias": dspSapCompanionAlias,
       "dspSapSnalcRef": dspSapSnalcRef,
       "dspSapEbcdicAsciiMode": dspSapEbcdicAsciiMode,
       "dspSapControl": dspSapControl,
       "dspSapOperationalMode": dspSapOperationalMode,
       "dspCuTable": dspCuTable,
       "dspCuEntry": dspCuEntry,
       "dspCuSapNumber": dspCuSapNumber,
       "dspCuAddress": dspCuAddress,
       "dspCuRowStatus": dspCuRowStatus,
       "dspCuType": dspCuType,
       "dspCuCallingX25Address": dspCuCallingX25Address,
       "dspCuCalledX25Address": dspCuCalledX25Address,
       "dspCuDSPCircuitType": dspCuDSPCircuitType,
       "dspCuWindow": dspCuWindow,
       "dspCuUserData": dspCuUserData,
       "dspCuFacility": dspCuFacility,
       "dspCuApplicationId": dspCuApplicationId,
       "dspCuReqMode": dspCuReqMode,
       "dspCuPacketSize": dspCuPacketSize,
       "dspCuThroughput": dspCuThroughput,
       "dspCuPartner": dspCuPartner,
       "dspCuControl": dspCuControl,
       "dspCuState": dspCuState,
       "dspCuOperationalMode": dspCuOperationalMode,
       "dspCuX25CallRequest": dspCuX25CallRequest,
       "dspCuX25CallAccept": dspCuX25CallAccept,
       "dspCuClears": dspCuClears,
       "dspCuClearsInd": dspCuClearsInd,
       "dspCuInvToClear": dspCuInvToClear,
       "dspDevTable": dspDevTable,
       "dspDevEntry": dspDevEntry,
       "dspDevSapNumber": dspDevSapNumber,
       "dspDevCuAddress": dspDevCuAddress,
       "dspDevAddress": dspDevAddress,
       "dspDevRowStatus": dspDevRowStatus,
       "dspDevUCN": dspDevUCN,
       "dspDevRemoteCuAddress": dspDevRemoteCuAddress,
       "dspDevRemoteDevAddress": dspDevRemoteDevAddress,
       "dspDevFormatSize": dspDevFormatSize,
       "dspDevAttPrnt": dspDevAttPrnt,
       "dspDevCharSet": dspDevCharSet,
       "dspDevColour": dspDevColour,
       "dspDevTTextSupport": dspDevTTextSupport,
       "dspDevDPmode": dspDevDPmode,
       "dspDevControl": dspDevControl,
       "dspDevOperationalMode": dspDevOperationalMode,
       "dspDevState": dspDevState,
       "dspDevStatus": dspDevStatus,
       "dspDevSense": dspDevSense,
       "dspDevCommand": dspDevCommand,
       "dspDevResponse": dspDevResponse,
       "dspDevCmdRspUndel": dspDevCmdRspUndel,
       "dspDevCmdRspUndelReason": dspDevCmdRspUndelReason,
       "dspDevCmdRspAbort": dspDevCmdRspAbort,
       "dspDevCmdRspAbortReason": dspDevCmdRspAbortReason,
       "dspDevStatStatus": dspDevStatStatus,
       "dspDevAck": dspDevAck,
       "dspDevInvToClear": dspDevInvToClear,
       "dspDevInvClearReason": dspDevInvClearReason,
       "dspDevReset": dspDevReset,
       "dspDevResetReason": dspDevResetReason,
       "dspDevCircuitEnabled": dspDevCircuitEnabled,
       "dspDevCircuitRequest": dspDevCircuitRequest,
       "dspDevCircuitDisconnect": dspDevCircuitDisconnect}
)
