# SNMP MIB module (X-DDI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X-DDI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:36 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FddiMACLongAddressType(OctetString):
    """Custom type FddiMACLongAddressType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NorthernTelecom_ObjectIdentity = ObjectIdentity
northernTelecom = _NorthernTelecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562)
)
_NorthernTelecomProducts_ObjectIdentity = ObjectIdentity
northernTelecomProducts = _NorthernTelecomProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1)
)
_Concentrator_ObjectIdentity = ObjectIdentity
concentrator = _Concentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1, 1)
)
_Conc_ObjectIdentity = ObjectIdentity
conc = _Conc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1)
)


class _ConcMgmtType_Type(Integer32):
    """Custom type concMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("smux", 3),
          ("snmp", 2))
    )


_ConcMgmtType_Type.__name__ = "Integer32"
_ConcMgmtType_Object = MibScalar
concMgmtType = _ConcMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 1),
    _ConcMgmtType_Type()
)
concMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concMgmtType.setStatus("mandatory")
_ConcIpAddr_Type = IpAddress
_ConcIpAddr_Object = MibScalar
concIpAddr = _ConcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 2),
    _ConcIpAddr_Type()
)
concIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concIpAddr.setStatus("mandatory")
_ConcNetMask_Type = IpAddress
_ConcNetMask_Object = MibScalar
concNetMask = _ConcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 3),
    _ConcNetMask_Type()
)
concNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concNetMask.setStatus("mandatory")
_ConcBroadcast_Type = IpAddress
_ConcBroadcast_Object = MibScalar
concBroadcast = _ConcBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 4),
    _ConcBroadcast_Type()
)
concBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concBroadcast.setStatus("mandatory")
_ConcTrapReceiverTable_Object = MibTable
concTrapReceiverTable = _ConcTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    concTrapReceiverTable.setStatus("mandatory")
_ConcTrapReceiverEntry_Object = MibTableRow
concTrapReceiverEntry = _ConcTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1)
)
concTrapReceiverEntry.setIndexNames(
    (0, "X-DDI-MIB", "concTrapReceiverAddr"),
)
if mibBuilder.loadTexts:
    concTrapReceiverEntry.setStatus("mandatory")


class _ConcTrapReceiverType_Type(Integer32):
    """Custom type concTrapReceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_ConcTrapReceiverType_Type.__name__ = "Integer32"
_ConcTrapReceiverType_Object = MibTableColumn
concTrapReceiverType = _ConcTrapReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 1),
    _ConcTrapReceiverType_Type()
)
concTrapReceiverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concTrapReceiverType.setStatus("mandatory")
_ConcTrapReceiverAddr_Type = IpAddress
_ConcTrapReceiverAddr_Object = MibTableColumn
concTrapReceiverAddr = _ConcTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 2),
    _ConcTrapReceiverAddr_Type()
)
concTrapReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concTrapReceiverAddr.setStatus("mandatory")


class _ConcTrapReceiverComm_Type(DisplayString):
    """Custom type concTrapReceiverComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConcTrapReceiverComm_Type.__name__ = "DisplayString"
_ConcTrapReceiverComm_Object = MibTableColumn
concTrapReceiverComm = _ConcTrapReceiverComm_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 5, 1, 3),
    _ConcTrapReceiverComm_Type()
)
concTrapReceiverComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concTrapReceiverComm.setStatus("mandatory")
_ConcCommunityTable_Object = MibTable
concCommunityTable = _ConcCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    concCommunityTable.setStatus("mandatory")
_ConcCommunityEntry_Object = MibTableRow
concCommunityEntry = _ConcCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1)
)
concCommunityEntry.setIndexNames(
    (0, "X-DDI-MIB", "concCommunityAccess"),
)
if mibBuilder.loadTexts:
    concCommunityEntry.setStatus("mandatory")


class _ConcCommunityAccess_Type(Integer32):
    """Custom type concCommunityAccess based on Integer32"""
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
        *(("other", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("readWriteAll", 4))
    )


_ConcCommunityAccess_Type.__name__ = "Integer32"
_ConcCommunityAccess_Object = MibTableColumn
concCommunityAccess = _ConcCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1, 1),
    _ConcCommunityAccess_Type()
)
concCommunityAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concCommunityAccess.setStatus("mandatory")


class _ConcCommunityString_Type(DisplayString):
    """Custom type concCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConcCommunityString_Type.__name__ = "DisplayString"
_ConcCommunityString_Object = MibTableColumn
concCommunityString = _ConcCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 6, 1, 2),
    _ConcCommunityString_Type()
)
concCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concCommunityString.setStatus("mandatory")


class _ConcAttachType_Type(Integer32):
    """Custom type concAttachType based on Integer32"""
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
        *(("dualAttach", 2),
          ("nullAttach", 4),
          ("other", 1),
          ("singleAttach", 3))
    )


_ConcAttachType_Type.__name__ = "Integer32"
_ConcAttachType_Object = MibScalar
concAttachType = _ConcAttachType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 7),
    _ConcAttachType_Type()
)
concAttachType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concAttachType.setStatus("mandatory")


class _ConcTraffic_Type(Integer32):
    """Custom type concTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ConcTraffic_Type.__name__ = "Integer32"
_ConcTraffic_Object = MibScalar
concTraffic = _ConcTraffic_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 8),
    _ConcTraffic_Type()
)
concTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concTraffic.setStatus("mandatory")


class _ConcReset_Type(Integer32):
    """Custom type concReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_ConcReset_Type.__name__ = "Integer32"
_ConcReset_Object = MibScalar
concReset = _ConcReset_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 9),
    _ConcReset_Type()
)
concReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concReset.setStatus("mandatory")


class _ConcBaudRate_Type(Integer32):
    """Custom type concBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 38400),
    )


_ConcBaudRate_Type.__name__ = "Integer32"
_ConcBaudRate_Object = MibScalar
concBaudRate = _ConcBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 10),
    _ConcBaudRate_Type()
)
concBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concBaudRate.setStatus("mandatory")


class _ConcInsertMode_Type(Integer32):
    """Custom type concInsertMode based on Integer32"""
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
        *(("graceful", 4),
          ("other", 1),
          ("scheduled", 3),
          ("standard", 2))
    )


_ConcInsertMode_Type.__name__ = "Integer32"
_ConcInsertMode_Object = MibScalar
concInsertMode = _ConcInsertMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 11),
    _ConcInsertMode_Type()
)
concInsertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concInsertMode.setStatus("mandatory")
_ConcClearMacTime_Type = TimeTicks
_ConcClearMacTime_Object = MibScalar
concClearMacTime = _ConcClearMacTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 12),
    _ConcClearMacTime_Type()
)
concClearMacTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concClearMacTime.setStatus("mandatory")
_ConcClearPortTime_Type = TimeTicks
_ConcClearPortTime_Object = MibScalar
concClearPortTime = _ConcClearPortTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 13),
    _ConcClearPortTime_Type()
)
concClearPortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concClearPortTime.setStatus("mandatory")
_ConcFddiRingTable_Object = MibTable
concFddiRingTable = _ConcFddiRingTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    concFddiRingTable.setStatus("mandatory")
_ConcFddiRingEntry_Object = MibTableRow
concFddiRingEntry = _ConcFddiRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1)
)
concFddiRingEntry.setIndexNames(
    (0, "X-DDI-MIB", "concFddiRingSMTIndex"),
)
if mibBuilder.loadTexts:
    concFddiRingEntry.setStatus("mandatory")


class _ConcFddiRingSMTIndex_Type(Integer32):
    """Custom type concFddiRingSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcFddiRingSMTIndex_Type.__name__ = "Integer32"
_ConcFddiRingSMTIndex_Object = MibTableColumn
concFddiRingSMTIndex = _ConcFddiRingSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 1),
    _ConcFddiRingSMTIndex_Type()
)
concFddiRingSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concFddiRingSMTIndex.setStatus("mandatory")
_ConcFddiRingAddress_Type = FddiMACLongAddressType
_ConcFddiRingAddress_Object = MibTableColumn
concFddiRingAddress = _ConcFddiRingAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 2),
    _ConcFddiRingAddress_Type()
)
concFddiRingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concFddiRingAddress.setStatus("mandatory")
_ConcFddiRingNext_Type = FddiMACLongAddressType
_ConcFddiRingNext_Object = MibTableColumn
concFddiRingNext = _ConcFddiRingNext_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 1, 14, 1, 3),
    _ConcFddiRingNext_Type()
)
concFddiRingNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concFddiRingNext.setStatus("mandatory")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2)
)


class _ChassisType_Type(Integer32):
    """Custom type chassisType based on Integer32"""
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
        *(("other", 1),
          ("x-ddi-8f", 4),
          ("x-ddi-8u", 3),
          ("x-ddi-m", 5),
          ("x-ddi-s", 6),
          ("xxxxx", 2))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")


class _ChassisBkplType_Type(Integer32):
    """Custom type chassisBkplType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 2),
          ("fddiEthernet", 3),
          ("other", 1))
    )


_ChassisBkplType_Type.__name__ = "Integer32"
_ChassisBkplType_Object = MibScalar
chassisBkplType = _ChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 2),
    _ChassisBkplType_Type()
)
chassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBkplType.setStatus("mandatory")


class _ChassisPs1Type_Type(Integer32):
    """Custom type chassisPs1Type based on Integer32"""
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
        *(("none", 2),
          ("other", 1),
          ("w200", 4),
          ("w50", 3),
          ("w600", 5),
          ("w80", 6))
    )


_ChassisPs1Type_Type.__name__ = "Integer32"
_ChassisPs1Type_Object = MibScalar
chassisPs1Type = _ChassisPs1Type_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 3),
    _ChassisPs1Type_Type()
)
chassisPs1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1Type.setStatus("mandatory")


class _ChassisPs1Status_Type(Integer32):
    """Custom type chassisPs1Status based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisPs1Status_Type.__name__ = "Integer32"
_ChassisPs1Status_Object = MibScalar
chassisPs1Status = _ChassisPs1Status_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 4),
    _ChassisPs1Status_Type()
)
chassisPs1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1Status.setStatus("mandatory")


class _ChassisPs1TestResult_Type(Integer32):
    """Custom type chassisPs1TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisPs1TestResult_Type.__name__ = "Integer32"
_ChassisPs1TestResult_Object = MibScalar
chassisPs1TestResult = _ChassisPs1TestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 5),
    _ChassisPs1TestResult_Type()
)
chassisPs1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1TestResult.setStatus("mandatory")


class _ChassisPs2Type_Type(Integer32):
    """Custom type chassisPs2Type based on Integer32"""
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
        *(("none", 2),
          ("other", 1),
          ("w200", 4),
          ("w50", 3),
          ("w600", 5),
          ("w80", 6))
    )


_ChassisPs2Type_Type.__name__ = "Integer32"
_ChassisPs2Type_Object = MibScalar
chassisPs2Type = _ChassisPs2Type_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 6),
    _ChassisPs2Type_Type()
)
chassisPs2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2Type.setStatus("mandatory")


class _ChassisPs2Status_Type(Integer32):
    """Custom type chassisPs2Status based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisPs2Status_Type.__name__ = "Integer32"
_ChassisPs2Status_Object = MibScalar
chassisPs2Status = _ChassisPs2Status_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 7),
    _ChassisPs2Status_Type()
)
chassisPs2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2Status.setStatus("mandatory")


class _ChassisPs2TestResult_Type(Integer32):
    """Custom type chassisPs2TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisPs2TestResult_Type.__name__ = "Integer32"
_ChassisPs2TestResult_Object = MibScalar
chassisPs2TestResult = _ChassisPs2TestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 8),
    _ChassisPs2TestResult_Type()
)
chassisPs2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2TestResult.setStatus("mandatory")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 9),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("mandatory")


class _ChassisFanTestResult_Type(Integer32):
    """Custom type chassisFanTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisFanTestResult_Type.__name__ = "Integer32"
_ChassisFanTestResult_Object = MibScalar
chassisFanTestResult = _ChassisFanTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 10),
    _ChassisFanTestResult_Type()
)
chassisFanTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanTestResult.setStatus("mandatory")


class _ChassisMinorAlarm_Type(Integer32):
    """Custom type chassisMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChassisMinorAlarm_Type.__name__ = "Integer32"
_ChassisMinorAlarm_Object = MibScalar
chassisMinorAlarm = _ChassisMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 11),
    _ChassisMinorAlarm_Type()
)
chassisMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMinorAlarm.setStatus("mandatory")


class _ChassisMajorAlarm_Type(Integer32):
    """Custom type chassisMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChassisMajorAlarm_Type.__name__ = "Integer32"
_ChassisMajorAlarm_Object = MibScalar
chassisMajorAlarm = _ChassisMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 12),
    _ChassisMajorAlarm_Type()
)
chassisMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMajorAlarm.setStatus("mandatory")


class _ChassisTempAlarm_Type(Integer32):
    """Custom type chassisTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChassisTempAlarm_Type.__name__ = "Integer32"
_ChassisTempAlarm_Object = MibScalar
chassisTempAlarm = _ChassisTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 13),
    _ChassisTempAlarm_Type()
)
chassisTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTempAlarm.setStatus("mandatory")


class _ChassisNumSlots_Type(Integer32):
    """Custom type chassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChassisNumSlots_Type.__name__ = "Integer32"
_ChassisNumSlots_Object = MibScalar
chassisNumSlots = _ChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 14),
    _ChassisNumSlots_Type()
)
chassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNumSlots.setStatus("mandatory")


class _ChassisSlotConfig_Type(Integer32):
    """Custom type chassisSlotConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisSlotConfig_Type.__name__ = "Integer32"
_ChassisSlotConfig_Object = MibScalar
chassisSlotConfig = _ChassisSlotConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 15),
    _ChassisSlotConfig_Type()
)
chassisSlotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotConfig.setStatus("mandatory")


class _ChassisModel_Type(DisplayString):
    """Custom type chassisModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChassisModel_Type.__name__ = "DisplayString"
_ChassisModel_Object = MibScalar
chassisModel = _ChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 2, 16),
    _ChassisModel_Type()
)
chassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModel.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("mandatory")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "X-DDI-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("mandatory")


class _ModuleIndex_Type(Integer32):
    """Custom type moduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModuleIndex_Type.__name__ = "Integer32"
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("mandatory")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
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
        *(("empty", 2),
          ("other", 1),
          ("x-ddi-8f", 4),
          ("x-ddi-8p-10baset-u-lc", 9),
          ("x-ddi-8p-f-lc", 8),
          ("x-ddi-8p-tr-u-lc", 10),
          ("x-ddi-8p-u-lc", 7),
          ("x-ddi-8u", 3),
          ("x-ddi-m", 5),
          ("x-ddi-mgt-lc", 6))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 2),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("mandatory")


class _ModuleSerialNumber_Type(Integer32):
    """Custom type moduleSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_ModuleSerialNumber_Type.__name__ = "Integer32"
_ModuleSerialNumber_Object = MibTableColumn
moduleSerialNumber = _ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 3),
    _ModuleSerialNumber_Type()
)
moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumber.setStatus("mandatory")


class _ModuleHwHiVersion_Type(Integer32):
    """Custom type moduleHwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleHwHiVersion_Type.__name__ = "Integer32"
_ModuleHwHiVersion_Object = MibTableColumn
moduleHwHiVersion = _ModuleHwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 4),
    _ModuleHwHiVersion_Type()
)
moduleHwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwHiVersion.setStatus("mandatory")


class _ModuleHwLoVersion_Type(Integer32):
    """Custom type moduleHwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleHwLoVersion_Type.__name__ = "Integer32"
_ModuleHwLoVersion_Object = MibTableColumn
moduleHwLoVersion = _ModuleHwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 5),
    _ModuleHwLoVersion_Type()
)
moduleHwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwLoVersion.setStatus("mandatory")


class _ModuleFwHiVersion_Type(Integer32):
    """Custom type moduleFwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleFwHiVersion_Type.__name__ = "Integer32"
_ModuleFwHiVersion_Object = MibTableColumn
moduleFwHiVersion = _ModuleFwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 6),
    _ModuleFwHiVersion_Type()
)
moduleFwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFwHiVersion.setStatus("mandatory")


class _ModuleFwLoVersion_Type(Integer32):
    """Custom type moduleFwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleFwLoVersion_Type.__name__ = "Integer32"
_ModuleFwLoVersion_Object = MibTableColumn
moduleFwLoVersion = _ModuleFwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 7),
    _ModuleFwLoVersion_Type()
)
moduleFwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFwLoVersion.setStatus("mandatory")


class _ModuleSwHiVersion_Type(Integer32):
    """Custom type moduleSwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleSwHiVersion_Type.__name__ = "Integer32"
_ModuleSwHiVersion_Object = MibTableColumn
moduleSwHiVersion = _ModuleSwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 8),
    _ModuleSwHiVersion_Type()
)
moduleSwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwHiVersion.setStatus("mandatory")


class _ModuleSwLoVersion_Type(Integer32):
    """Custom type moduleSwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleSwLoVersion_Type.__name__ = "Integer32"
_ModuleSwLoVersion_Object = MibTableColumn
moduleSwLoVersion = _ModuleSwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 9),
    _ModuleSwLoVersion_Type()
)
moduleSwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwLoVersion.setStatus("mandatory")


class _ModuleStatus_Type(Integer32):
    """Custom type moduleStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ModuleStatus_Type.__name__ = "Integer32"
_ModuleStatus_Object = MibTableColumn
moduleStatus = _ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 10),
    _ModuleStatus_Type()
)
moduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatus.setStatus("mandatory")


class _ModuleTestResult_Type(Integer32):
    """Custom type moduleTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleTestResult_Type.__name__ = "Integer32"
_ModuleTestResult_Object = MibTableColumn
moduleTestResult = _ModuleTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 11),
    _ModuleTestResult_Type()
)
moduleTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTestResult.setStatus("mandatory")


class _ModuleReset_Type(Integer32):
    """Custom type moduleReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_ModuleReset_Type.__name__ = "Integer32"
_ModuleReset_Object = MibTableColumn
moduleReset = _ModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 12),
    _ModuleReset_Type()
)
moduleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleReset.setStatus("mandatory")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 13),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleName.setStatus("mandatory")


class _ModuleNumPorts_Type(Integer32):
    """Custom type moduleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleNumPorts_Type.__name__ = "Integer32"
_ModuleNumPorts_Object = MibTableColumn
moduleNumPorts = _ModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 14),
    _ModuleNumPorts_Type()
)
moduleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumPorts.setStatus("mandatory")


class _ModulePortStatus_Type(OctetString):
    """Custom type modulePortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModulePortStatus_Type.__name__ = "OctetString"
_ModulePortStatus_Object = MibTableColumn
modulePortStatus = _ModulePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 15),
    _ModulePortStatus_Type()
)
modulePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePortStatus.setStatus("mandatory")


class _ModuleSubType_Type(Integer32):
    """Custom type moduleSubType based on Integer32"""
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
        *(("empty", 2),
          ("other", 1),
          ("x-ddi-1mac", 3),
          ("x-ddi-2mac", 4),
          ("x-ddi-3mac", 5))
    )


_ModuleSubType_Type.__name__ = "Integer32"
_ModuleSubType_Object = MibTableColumn
moduleSubType = _ModuleSubType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 16),
    _ModuleSubType_Type()
)
moduleSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSubType.setStatus("mandatory")


class _ModuleModel_Type(DisplayString):
    """Custom type moduleModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ModuleModel_Type.__name__ = "DisplayString"
_ModuleModel_Object = MibTableColumn
moduleModel = _ModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 3, 1, 1, 17),
    _ModuleModel_Type()
)
moduleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleModel.setStatus("mandatory")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "X-DDI-MIB", "portModuleIndex"),
    (0, "X-DDI-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")


class _PortModuleIndex_Type(Integer32):
    """Custom type portModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortModuleIndex_Type.__name__ = "Integer32"
_PortModuleIndex_Object = MibTableColumn
portModuleIndex = _PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 1),
    _PortModuleIndex_Type()
)
portModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleIndex.setStatus("mandatory")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortFddiIndex_Type(Integer32):
    """Custom type portFddiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4080),
    )


_PortFddiIndex_Type.__name__ = "Integer32"
_PortFddiIndex_Object = MibTableColumn
portFddiIndex = _PortFddiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 3),
    _PortFddiIndex_Type()
)
portFddiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFddiIndex.setStatus("mandatory")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 4),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("fiber", 3),
          ("mlt3", 5),
          ("other", 1),
          ("sddi", 6),
          ("tp-pmd", 4),
          ("x-ddi", 2))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 5),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortStatus_Type(Integer32):
    """Custom type portStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_PortStatus_Type.__name__ = "Integer32"
_PortStatus_Object = MibTableColumn
portStatus = _PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 6),
    _PortStatus_Type()
)
portStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatus.setStatus("mandatory")


class _PortFddiSmtIndex_Type(Integer32):
    """Custom type portFddiSmtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortFddiSmtIndex_Type.__name__ = "Integer32"
_PortFddiSmtIndex_Object = MibTableColumn
portFddiSmtIndex = _PortFddiSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 1, 1, 4, 1, 1, 7),
    _PortFddiSmtIndex_Type()
)
portFddiSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFddiSmtIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X-DDI-MIB",
    **{"FddiMACLongAddressType": FddiMACLongAddressType,
       "northernTelecom": northernTelecom,
       "northernTelecomProducts": northernTelecomProducts,
       "concentrator": concentrator,
       "conc": conc,
       "concMgmtType": concMgmtType,
       "concIpAddr": concIpAddr,
       "concNetMask": concNetMask,
       "concBroadcast": concBroadcast,
       "concTrapReceiverTable": concTrapReceiverTable,
       "concTrapReceiverEntry": concTrapReceiverEntry,
       "concTrapReceiverType": concTrapReceiverType,
       "concTrapReceiverAddr": concTrapReceiverAddr,
       "concTrapReceiverComm": concTrapReceiverComm,
       "concCommunityTable": concCommunityTable,
       "concCommunityEntry": concCommunityEntry,
       "concCommunityAccess": concCommunityAccess,
       "concCommunityString": concCommunityString,
       "concAttachType": concAttachType,
       "concTraffic": concTraffic,
       "concReset": concReset,
       "concBaudRate": concBaudRate,
       "concInsertMode": concInsertMode,
       "concClearMacTime": concClearMacTime,
       "concClearPortTime": concClearPortTime,
       "concFddiRingTable": concFddiRingTable,
       "concFddiRingEntry": concFddiRingEntry,
       "concFddiRingSMTIndex": concFddiRingSMTIndex,
       "concFddiRingAddress": concFddiRingAddress,
       "concFddiRingNext": concFddiRingNext,
       "chassis": chassis,
       "chassisType": chassisType,
       "chassisBkplType": chassisBkplType,
       "chassisPs1Type": chassisPs1Type,
       "chassisPs1Status": chassisPs1Status,
       "chassisPs1TestResult": chassisPs1TestResult,
       "chassisPs2Type": chassisPs2Type,
       "chassisPs2Status": chassisPs2Status,
       "chassisPs2TestResult": chassisPs2TestResult,
       "chassisFanStatus": chassisFanStatus,
       "chassisFanTestResult": chassisFanTestResult,
       "chassisMinorAlarm": chassisMinorAlarm,
       "chassisMajorAlarm": chassisMajorAlarm,
       "chassisTempAlarm": chassisTempAlarm,
       "chassisNumSlots": chassisNumSlots,
       "chassisSlotConfig": chassisSlotConfig,
       "chassisModel": chassisModel,
       "module": module,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleType": moduleType,
       "moduleSerialNumber": moduleSerialNumber,
       "moduleHwHiVersion": moduleHwHiVersion,
       "moduleHwLoVersion": moduleHwLoVersion,
       "moduleFwHiVersion": moduleFwHiVersion,
       "moduleFwLoVersion": moduleFwLoVersion,
       "moduleSwHiVersion": moduleSwHiVersion,
       "moduleSwLoVersion": moduleSwLoVersion,
       "moduleStatus": moduleStatus,
       "moduleTestResult": moduleTestResult,
       "moduleReset": moduleReset,
       "moduleName": moduleName,
       "moduleNumPorts": moduleNumPorts,
       "modulePortStatus": modulePortStatus,
       "moduleSubType": moduleSubType,
       "moduleModel": moduleModel,
       "port": port,
       "portTable": portTable,
       "portEntry": portEntry,
       "portModuleIndex": portModuleIndex,
       "portIndex": portIndex,
       "portFddiIndex": portFddiIndex,
       "portName": portName,
       "portType": portType,
       "portStatus": portStatus,
       "portFddiSmtIndex": portFddiSmtIndex}
)
