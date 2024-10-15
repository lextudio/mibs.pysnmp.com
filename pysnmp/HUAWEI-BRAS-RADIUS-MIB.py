# SNMP MIB module (HUAWEI-BRAS-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:06 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 ModuleCompliance,
 ModuleIdentity,
 MibIdentifier,
 NotificationGroup,
 NotificationType,
 ObjectGroup,
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
    "ModuleCompliance",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationGroup",
    "NotificationType",
    "ObjectGroup",
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBRASRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRadiusGroupObject_ObjectIdentity = ObjectIdentity
hwRadiusGroupObject = _HwRadiusGroupObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1)
)
_HwRadiusGroupTable_Object = MibTable
hwRadiusGroupTable = _HwRadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hwRadiusGroupTable.setStatus("current")
_HwRadiusGroupEntry_Object = MibTableRow
hwRadiusGroupEntry = _HwRadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1)
)
hwRadiusGroupEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusGroupName"),
)
if mibBuilder.loadTexts:
    hwRadiusGroupEntry.setStatus("current")


class _HwRadiusGroupName_Type(OctetString):
    """Custom type hwRadiusGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRadiusGroupName_Type.__name__ = "OctetString"
_HwRadiusGroupName_Object = MibTableColumn
hwRadiusGroupName = _HwRadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 1),
    _HwRadiusGroupName_Type()
)
hwRadiusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusGroupName.setStatus("current")


class _HwRadiusServerKey_Type(OctetString):
    """Custom type hwRadiusServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwRadiusServerKey_Type.__name__ = "OctetString"
_HwRadiusServerKey_Object = MibTableColumn
hwRadiusServerKey = _HwRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 2),
    _HwRadiusServerKey_Type()
)
hwRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerKey.setStatus("current")


class _HwRadiusServerProtType_Type(Integer32):
    """Custom type hwRadiusServerProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("radiusPlus10", 2),
          ("radiusPlus11", 3))
    )


_HwRadiusServerProtType_Type.__name__ = "Integer32"
_HwRadiusServerProtType_Object = MibTableColumn
hwRadiusServerProtType = _HwRadiusServerProtType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 3),
    _HwRadiusServerProtType_Type()
)
hwRadiusServerProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerProtType.setStatus("current")


class _HwRadiusServerRetransmit_Type(Integer32):
    """Custom type hwRadiusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwRadiusServerRetransmit_Type.__name__ = "Integer32"
_HwRadiusServerRetransmit_Object = MibTableColumn
hwRadiusServerRetransmit = _HwRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 4),
    _HwRadiusServerRetransmit_Type()
)
hwRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerRetransmit.setStatus("current")


class _HwRadiusServerTimeout_Type(Integer32):
    """Custom type hwRadiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 25),
    )


_HwRadiusServerTimeout_Type.__name__ = "Integer32"
_HwRadiusServerTimeout_Object = MibTableColumn
hwRadiusServerTimeout = _HwRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 5),
    _HwRadiusServerTimeout_Type()
)
hwRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerTimeout.setStatus("current")


class _HwRadiusServerAttrTran_Type(TruthValue):
    """Custom type hwRadiusServerAttrTran based on TruthValue"""


_HwRadiusServerAttrTran_Object = MibTableColumn
hwRadiusServerAttrTran = _HwRadiusServerAttrTran_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 6),
    _HwRadiusServerAttrTran_Type()
)
hwRadiusServerAttrTran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerAttrTran.setStatus("current")


class _HwRadiusPacketUnit_Type(Integer32):
    """Custom type hwRadiusPacketUnit based on Integer32"""
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
        *(("byte", 1),
          ("gbyte", 4),
          ("kbyte", 2),
          ("mbyte", 3))
    )


_HwRadiusPacketUnit_Type.__name__ = "Integer32"
_HwRadiusPacketUnit_Object = MibTableColumn
hwRadiusPacketUnit = _HwRadiusPacketUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 7),
    _HwRadiusPacketUnit_Type()
)
hwRadiusPacketUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusPacketUnit.setStatus("current")


class _HwRadiusDomainInclude_Type(Integer32):
    """Custom type hwRadiusDomainInclude based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("includingDomain", 1),
          ("notIncludingDomain", 2),
          ("original", 3))
    )


_HwRadiusDomainInclude_Type.__name__ = "Integer32"
_HwRadiusDomainInclude_Object = MibTableColumn
hwRadiusDomainInclude = _HwRadiusDomainInclude_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 8),
    _HwRadiusDomainInclude_Type()
)
hwRadiusDomainInclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusDomainInclude.setStatus("current")


class _HwRadiusClassASCar_Type(TruthValue):
    """Custom type hwRadiusClassASCar based on TruthValue"""


_HwRadiusClassASCar_Object = MibTableColumn
hwRadiusClassASCar = _HwRadiusClassASCar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 9),
    _HwRadiusClassASCar_Type()
)
hwRadiusClassASCar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusClassASCar.setStatus("current")


class _HwRadiusAlgorithm_Type(Integer32):
    """Custom type hwRadiusAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterbackup", 1),
          ("shareloading", 2))
    )


_HwRadiusAlgorithm_Type.__name__ = "Integer32"
_HwRadiusAlgorithm_Object = MibTableColumn
hwRadiusAlgorithm = _HwRadiusAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 10),
    _HwRadiusAlgorithm_Type()
)
hwRadiusAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAlgorithm.setStatus("current")


class _HwRadiusServerNasPortFmt_Type(OctetString):
    """Custom type hwRadiusServerNasPortFmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwRadiusServerNasPortFmt_Type.__name__ = "OctetString"
_HwRadiusServerNasPortFmt_Object = MibTableColumn
hwRadiusServerNasPortFmt = _HwRadiusServerNasPortFmt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 11),
    _HwRadiusServerNasPortFmt_Type()
)
hwRadiusServerNasPortFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerNasPortFmt.setStatus("current")
_HwRadiusGroupRowStatus_Type = RowStatus
_HwRadiusGroupRowStatus_Object = MibTableColumn
hwRadiusGroupRowStatus = _HwRadiusGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 12),
    _HwRadiusGroupRowStatus_Type()
)
hwRadiusGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadiusGroupRowStatus.setStatus("current")


class _HwRadiusServerSourceInterface_Type(OctetString):
    """Custom type hwRadiusServerSourceInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwRadiusServerSourceInterface_Type.__name__ = "OctetString"
_HwRadiusServerSourceInterface_Object = MibTableColumn
hwRadiusServerSourceInterface = _HwRadiusServerSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 13),
    _HwRadiusServerSourceInterface_Type()
)
hwRadiusServerSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerSourceInterface.setStatus("current")
_HwRadiusServerNasIpAddress_Type = IpAddress
_HwRadiusServerNasIpAddress_Object = MibTableColumn
hwRadiusServerNasIpAddress = _HwRadiusServerNasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 14),
    _HwRadiusServerNasIpAddress_Type()
)
hwRadiusServerNasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerNasIpAddress.setStatus("current")


class _HwRadiusServerCallingStationId_Type(OctetString):
    """Custom type hwRadiusServerCallingStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwRadiusServerCallingStationId_Type.__name__ = "OctetString"
_HwRadiusServerCallingStationId_Object = MibTableColumn
hwRadiusServerCallingStationId = _HwRadiusServerCallingStationId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 15),
    _HwRadiusServerCallingStationId_Type()
)
hwRadiusServerCallingStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerCallingStationId.setStatus("current")


class _HwRadiusServerCallingStationIdDelimiter_Type(OctetString):
    """Custom type hwRadiusServerCallingStationIdDelimiter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwRadiusServerCallingStationIdDelimiter_Type.__name__ = "OctetString"
_HwRadiusServerCallingStationIdDelimiter_Object = MibTableColumn
hwRadiusServerCallingStationIdDelimiter = _HwRadiusServerCallingStationIdDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 16),
    _HwRadiusServerCallingStationIdDelimiter_Type()
)
hwRadiusServerCallingStationIdDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerCallingStationIdDelimiter.setStatus("current")


class _HwRadiusAttributeNoExistPolicy_Type(Integer32):
    """Custom type hwRadiusAttributeNoExistPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_HwRadiusAttributeNoExistPolicy_Type.__name__ = "Integer32"
_HwRadiusAttributeNoExistPolicy_Object = MibTableColumn
hwRadiusAttributeNoExistPolicy = _HwRadiusAttributeNoExistPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 17),
    _HwRadiusAttributeNoExistPolicy_Type()
)
hwRadiusAttributeNoExistPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAttributeNoExistPolicy.setStatus("current")


class _HwRadiusServerKeyType_Type(Integer32):
    """Custom type hwRadiusServerKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 0))
    )


_HwRadiusServerKeyType_Type.__name__ = "Integer32"
_HwRadiusServerKeyType_Object = MibTableColumn
hwRadiusServerKeyType = _HwRadiusServerKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 1, 1, 18),
    _HwRadiusServerKeyType_Type()
)
hwRadiusServerKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerKeyType.setStatus("current")
_HwRadiusServerTable_Object = MibTable
hwRadiusServerTable = _HwRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hwRadiusServerTable.setStatus("current")
_HwRadiusServerEntry_Object = MibTableRow
hwRadiusServerEntry = _HwRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1)
)
hwRadiusServerEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusGroupName"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerIndex"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerType"),
)
if mibBuilder.loadTexts:
    hwRadiusServerEntry.setStatus("current")


class _HwRadiusServerIndex_Type(Integer32):
    """Custom type hwRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwRadiusServerIndex_Type.__name__ = "Integer32"
_HwRadiusServerIndex_Object = MibTableColumn
hwRadiusServerIndex = _HwRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 1),
    _HwRadiusServerIndex_Type()
)
hwRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerIndex.setStatus("current")


class _HwRadiusServerType_Type(Integer32):
    """Custom type hwRadiusServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acct", 2),
          ("auth", 1))
    )


_HwRadiusServerType_Type.__name__ = "Integer32"
_HwRadiusServerType_Object = MibTableColumn
hwRadiusServerType = _HwRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 2),
    _HwRadiusServerType_Type()
)
hwRadiusServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerType.setStatus("current")


class _HwRadiusServerVRF_Type(OctetString):
    """Custom type hwRadiusServerVRF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusServerVRF_Type.__name__ = "OctetString"
_HwRadiusServerVRF_Object = MibTableColumn
hwRadiusServerVRF = _HwRadiusServerVRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 3),
    _HwRadiusServerVRF_Type()
)
hwRadiusServerVRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerVRF.setStatus("current")
_HwRadiusServerIP_Type = IpAddress
_HwRadiusServerIP_Object = MibTableColumn
hwRadiusServerIP = _HwRadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 4),
    _HwRadiusServerIP_Type()
)
hwRadiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerIP.setStatus("current")


class _HwRadiusServerPort_Type(Integer32):
    """Custom type hwRadiusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRadiusServerPort_Type.__name__ = "Integer32"
_HwRadiusServerPort_Object = MibTableColumn
hwRadiusServerPort = _HwRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 5),
    _HwRadiusServerPort_Type()
)
hwRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerPort.setStatus("current")


class _HwRadiusServerWeight_Type(Integer32):
    """Custom type hwRadiusServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwRadiusServerWeight_Type.__name__ = "Integer32"
_HwRadiusServerWeight_Object = MibTableColumn
hwRadiusServerWeight = _HwRadiusServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 6),
    _HwRadiusServerWeight_Type()
)
hwRadiusServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerWeight.setStatus("current")


class _HwRadiusServerSecretKey_Type(OctetString):
    """Custom type hwRadiusServerSecretKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwRadiusServerSecretKey_Type.__name__ = "OctetString"
_HwRadiusServerSecretKey_Object = MibTableColumn
hwRadiusServerSecretKey = _HwRadiusServerSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 7),
    _HwRadiusServerSecretKey_Type()
)
hwRadiusServerSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerSecretKey.setStatus("current")
_HwRadiusServerRowStatus_Type = RowStatus
_HwRadiusServerRowStatus_Object = MibTableColumn
hwRadiusServerRowStatus = _HwRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 8),
    _HwRadiusServerRowStatus_Type()
)
hwRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadiusServerRowStatus.setStatus("current")


class _HwRadiusServerPktSendNumber_Type(Integer32):
    """Custom type hwRadiusServerPktSendNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRadiusServerPktSendNumber_Type.__name__ = "Integer32"
_HwRadiusServerPktSendNumber_Object = MibTableColumn
hwRadiusServerPktSendNumber = _HwRadiusServerPktSendNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 9),
    _HwRadiusServerPktSendNumber_Type()
)
hwRadiusServerPktSendNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerPktSendNumber.setStatus("current")


class _HwRadiusServerPktSendInterval_Type(Integer32):
    """Custom type hwRadiusServerPktSendInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRadiusServerPktSendInterval_Type.__name__ = "Integer32"
_HwRadiusServerPktSendInterval_Object = MibTableColumn
hwRadiusServerPktSendInterval = _HwRadiusServerPktSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 10),
    _HwRadiusServerPktSendInterval_Type()
)
hwRadiusServerPktSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerPktSendInterval.setStatus("current")


class _HwRadiusServerSourceInterfaceEachServer_Type(OctetString):
    """Custom type hwRadiusServerSourceInterfaceEachServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_HwRadiusServerSourceInterfaceEachServer_Type.__name__ = "OctetString"
_HwRadiusServerSourceInterfaceEachServer_Object = MibTableColumn
hwRadiusServerSourceInterfaceEachServer = _HwRadiusServerSourceInterfaceEachServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 11),
    _HwRadiusServerSourceInterfaceEachServer_Type()
)
hwRadiusServerSourceInterfaceEachServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerSourceInterfaceEachServer.setStatus("current")


class _HwRadiusServerResponses_Type(Unsigned32):
    """Custom type hwRadiusServerResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusServerResponses_Type.__name__ = "Unsigned32"
_HwRadiusServerResponses_Object = MibTableColumn
hwRadiusServerResponses = _HwRadiusServerResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 12),
    _HwRadiusServerResponses_Type()
)
hwRadiusServerResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerResponses.setStatus("current")


class _HwRadiusServerSecretKeyType_Type(Integer32):
    """Custom type hwRadiusServerSecretKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 0))
    )


_HwRadiusServerSecretKeyType_Type.__name__ = "Integer32"
_HwRadiusServerSecretKeyType_Object = MibTableColumn
hwRadiusServerSecretKeyType = _HwRadiusServerSecretKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 13),
    _HwRadiusServerSecretKeyType_Type()
)
hwRadiusServerSecretKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusServerSecretKeyType.setStatus("current")


class _HwRadiusServerDeadCount_Type(Integer32):
    """Custom type hwRadiusServerDeadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwRadiusServerDeadCount_Type.__name__ = "Integer32"
_HwRadiusServerDeadCount_Object = MibTableColumn
hwRadiusServerDeadCount = _HwRadiusServerDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 14),
    _HwRadiusServerDeadCount_Type()
)
hwRadiusServerDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerDeadCount.setStatus("current")


class _HwRadiusServerDeadTime_Type(Integer32):
    """Custom type hwRadiusServerDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwRadiusServerDeadTime_Type.__name__ = "Integer32"
_HwRadiusServerDeadTime_Object = MibTableColumn
hwRadiusServerDeadTime = _HwRadiusServerDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 15),
    _HwRadiusServerDeadTime_Type()
)
hwRadiusServerDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerDeadTime.setStatus("current")


class _HwRadiusServerDeadInterval_Type(Integer32):
    """Custom type hwRadiusServerDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRadiusServerDeadInterval_Type.__name__ = "Integer32"
_HwRadiusServerDeadInterval_Object = MibTableColumn
hwRadiusServerDeadInterval = _HwRadiusServerDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 2, 1, 16),
    _HwRadiusServerDeadInterval_Type()
)
hwRadiusServerDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusServerDeadInterval.setStatus("current")
_HwRadiusClientTable_Object = MibTable
hwRadiusClientTable = _HwRadiusClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3)
)
if mibBuilder.loadTexts:
    hwRadiusClientTable.setStatus("current")
_HwRadiusClientEntry_Object = MibTableRow
hwRadiusClientEntry = _HwRadiusClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1)
)
hwRadiusClientEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientIP"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientVrf"),
)
if mibBuilder.loadTexts:
    hwRadiusClientEntry.setStatus("current")
_HwRadiusClientIP_Type = IpAddress
_HwRadiusClientIP_Object = MibTableColumn
hwRadiusClientIP = _HwRadiusClientIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 1),
    _HwRadiusClientIP_Type()
)
hwRadiusClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusClientIP.setStatus("current")


class _HwRadiusClientVrf_Type(OctetString):
    """Custom type hwRadiusClientVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusClientVrf_Type.__name__ = "OctetString"
_HwRadiusClientVrf_Object = MibTableColumn
hwRadiusClientVrf = _HwRadiusClientVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 2),
    _HwRadiusClientVrf_Type()
)
hwRadiusClientVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusClientVrf.setStatus("current")


class _HwRadiusClientKey_Type(OctetString):
    """Custom type hwRadiusClientKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwRadiusClientKey_Type.__name__ = "OctetString"
_HwRadiusClientKey_Object = MibTableColumn
hwRadiusClientKey = _HwRadiusClientKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 3),
    _HwRadiusClientKey_Type()
)
hwRadiusClientKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusClientKey.setStatus("current")


class _HwRadiusClientGroupName_Type(OctetString):
    """Custom type hwRadiusClientGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRadiusClientGroupName_Type.__name__ = "OctetString"
_HwRadiusClientGroupName_Object = MibTableColumn
hwRadiusClientGroupName = _HwRadiusClientGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 4),
    _HwRadiusClientGroupName_Type()
)
hwRadiusClientGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusClientGroupName.setStatus("current")
_HwRadiusClientRowStatus_Type = RowStatus
_HwRadiusClientRowStatus_Object = MibTableColumn
hwRadiusClientRowStatus = _HwRadiusClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 5),
    _HwRadiusClientRowStatus_Type()
)
hwRadiusClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRadiusClientRowStatus.setStatus("current")


class _HwRadiusClientKeyType_Type(Integer32):
    """Custom type hwRadiusClientKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 0))
    )


_HwRadiusClientKeyType_Type.__name__ = "Integer32"
_HwRadiusClientKeyType_Object = MibTableColumn
hwRadiusClientKeyType = _HwRadiusClientKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 3, 1, 6),
    _HwRadiusClientKeyType_Type()
)
hwRadiusClientKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusClientKeyType.setStatus("current")
_HwRadiusAuthorServerTable_Object = MibTable
hwRadiusAuthorServerTable = _HwRadiusAuthorServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4)
)
if mibBuilder.loadTexts:
    hwRadiusAuthorServerTable.setStatus("current")
_HwRadiusAuthorServerEntry_Object = MibTableRow
hwRadiusAuthorServerEntry = _HwRadiusAuthorServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1)
)
hwRadiusAuthorServerEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerIP"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerVrf"),
)
if mibBuilder.loadTexts:
    hwRadiusAuthorServerEntry.setStatus("current")
_HwRadiusAuthorServerIP_Type = IpAddress
_HwRadiusAuthorServerIP_Object = MibTableColumn
hwRadiusAuthorServerIP = _HwRadiusAuthorServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 1),
    _HwRadiusAuthorServerIP_Type()
)
hwRadiusAuthorServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerIP.setStatus("current")


class _HwRadiusAuthorServerVrf_Type(OctetString):
    """Custom type hwRadiusAuthorServerVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusAuthorServerVrf_Type.__name__ = "OctetString"
_HwRadiusAuthorServerVrf_Object = MibTableColumn
hwRadiusAuthorServerVrf = _HwRadiusAuthorServerVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 2),
    _HwRadiusAuthorServerVrf_Type()
)
hwRadiusAuthorServerVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerVrf.setStatus("current")


class _HwRadiusAuthorServerKey_Type(OctetString):
    """Custom type hwRadiusAuthorServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwRadiusAuthorServerKey_Type.__name__ = "OctetString"
_HwRadiusAuthorServerKey_Object = MibTableColumn
hwRadiusAuthorServerKey = _HwRadiusAuthorServerKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 3),
    _HwRadiusAuthorServerKey_Type()
)
hwRadiusAuthorServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerKey.setStatus("current")


class _HwRadiusAuthorServerGroupName_Type(OctetString):
    """Custom type hwRadiusAuthorServerGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwRadiusAuthorServerGroupName_Type.__name__ = "OctetString"
_HwRadiusAuthorServerGroupName_Object = MibTableColumn
hwRadiusAuthorServerGroupName = _HwRadiusAuthorServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 4),
    _HwRadiusAuthorServerGroupName_Type()
)
hwRadiusAuthorServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerGroupName.setStatus("current")
_HwRadiusAuthorServerRowStatus_Type = RowStatus
_HwRadiusAuthorServerRowStatus_Object = MibTableColumn
hwRadiusAuthorServerRowStatus = _HwRadiusAuthorServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 5),
    _HwRadiusAuthorServerRowStatus_Type()
)
hwRadiusAuthorServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerRowStatus.setStatus("current")


class _HwRadiusAuthorServerKeyType_Type(Integer32):
    """Custom type hwRadiusAuthorServerKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 1),
          ("simple", 0))
    )


_HwRadiusAuthorServerKeyType_Type.__name__ = "Integer32"
_HwRadiusAuthorServerKeyType_Object = MibTableColumn
hwRadiusAuthorServerKeyType = _HwRadiusAuthorServerKeyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 4, 1, 6),
    _HwRadiusAuthorServerKeyType_Type()
)
hwRadiusAuthorServerKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusAuthorServerKeyType.setStatus("current")
_HwRadiusSetting_ObjectIdentity = ObjectIdentity
hwRadiusSetting = _HwRadiusSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5)
)
_HwRadiusSettingEntry_ObjectIdentity = ObjectIdentity
hwRadiusSettingEntry = _HwRadiusSettingEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1)
)
_HwEnableSourcePortsExtended_Type = EnabledStatus
_HwEnableSourcePortsExtended_Object = MibScalar
hwEnableSourcePortsExtended = _HwEnableSourcePortsExtended_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 1),
    _HwEnableSourcePortsExtended_Type()
)
hwEnableSourcePortsExtended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnableSourcePortsExtended.setStatus("current")


class _HwSourcePortsExtendedStartPort_Type(Integer32):
    """Custom type hwSourcePortsExtendedStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 55535),
    )


_HwSourcePortsExtendedStartPort_Type.__name__ = "Integer32"
_HwSourcePortsExtendedStartPort_Object = MibScalar
hwSourcePortsExtendedStartPort = _HwSourcePortsExtendedStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 2),
    _HwSourcePortsExtendedStartPort_Type()
)
hwSourcePortsExtendedStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSourcePortsExtendedStartPort.setStatus("current")


class _HwSourcePortsExtendedPortNum_Type(Integer32):
    """Custom type hwSourcePortsExtendedPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_HwSourcePortsExtendedPortNum_Type.__name__ = "Integer32"
_HwSourcePortsExtendedPortNum_Object = MibScalar
hwSourcePortsExtendedPortNum = _HwSourcePortsExtendedPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 3),
    _HwSourcePortsExtendedPortNum_Type()
)
hwSourcePortsExtendedPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSourcePortsExtendedPortNum.setStatus("current")


class _HwRadiusResetStatAll_Type(Integer32):
    """Custom type hwRadiusResetStatAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwRadiusResetStatAll_Type.__name__ = "Integer32"
_HwRadiusResetStatAll_Object = MibScalar
hwRadiusResetStatAll = _HwRadiusResetStatAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 4),
    _HwRadiusResetStatAll_Type()
)
hwRadiusResetStatAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusResetStatAll.setStatus("current")


class _HwResetRadiusAttrCount_Type(Integer32):
    """Custom type hwResetRadiusAttrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwResetRadiusAttrCount_Type.__name__ = "Integer32"
_HwResetRadiusAttrCount_Object = MibScalar
hwResetRadiusAttrCount = _HwResetRadiusAttrCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 5),
    _HwResetRadiusAttrCount_Type()
)
hwResetRadiusAttrCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwResetRadiusAttrCount.setStatus("current")


class _HwRadiusTotalDeadCount_Type(Integer32):
    """Custom type hwRadiusTotalDeadCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_HwRadiusTotalDeadCount_Type.__name__ = "Integer32"
_HwRadiusTotalDeadCount_Object = MibScalar
hwRadiusTotalDeadCount = _HwRadiusTotalDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 6),
    _HwRadiusTotalDeadCount_Type()
)
hwRadiusTotalDeadCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusTotalDeadCount.setStatus("current")


class _HwRadiusTotalDeadTime_Type(Integer32):
    """Custom type hwRadiusTotalDeadTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwRadiusTotalDeadTime_Type.__name__ = "Integer32"
_HwRadiusTotalDeadTime_Object = MibScalar
hwRadiusTotalDeadTime = _HwRadiusTotalDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 7),
    _HwRadiusTotalDeadTime_Type()
)
hwRadiusTotalDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusTotalDeadTime.setStatus("current")


class _HwRadiusTotalDeadInterval_Type(Integer32):
    """Custom type hwRadiusTotalDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRadiusTotalDeadInterval_Type.__name__ = "Integer32"
_HwRadiusTotalDeadInterval_Object = MibScalar
hwRadiusTotalDeadInterval = _HwRadiusTotalDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 5, 1, 8),
    _HwRadiusTotalDeadInterval_Type()
)
hwRadiusTotalDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRadiusTotalDeadInterval.setStatus("current")
_HwRadiusStatAuthenIpv4Table_Object = MibTable
hwRadiusStatAuthenIpv4Table = _HwRadiusStatAuthenIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6)
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Table.setStatus("current")
_HwRadiusStatAuthenIpv4Entry_Object = MibTableRow
hwRadiusStatAuthenIpv4Entry = _HwRadiusStatAuthenIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1)
)
hwRadiusStatAuthenIpv4Entry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthenIpv4ServerIP"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthenIpv4Vrf"),
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Entry.setStatus("current")
_HwRadiusStatAuthenIpv4ServerIP_Type = IpAddress
_HwRadiusStatAuthenIpv4ServerIP_Object = MibTableColumn
hwRadiusStatAuthenIpv4ServerIP = _HwRadiusStatAuthenIpv4ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 1),
    _HwRadiusStatAuthenIpv4ServerIP_Type()
)
hwRadiusStatAuthenIpv4ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4ServerIP.setStatus("current")


class _HwRadiusStatAuthenIpv4Vrf_Type(OctetString):
    """Custom type hwRadiusStatAuthenIpv4Vrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusStatAuthenIpv4Vrf_Type.__name__ = "OctetString"
_HwRadiusStatAuthenIpv4Vrf_Object = MibTableColumn
hwRadiusStatAuthenIpv4Vrf = _HwRadiusStatAuthenIpv4Vrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 2),
    _HwRadiusStatAuthenIpv4Vrf_Type()
)
hwRadiusStatAuthenIpv4Vrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Vrf.setStatus("current")


class _HwRadiusStatAuthenIpv4Requests_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Requests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Requests_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Requests_Object = MibTableColumn
hwRadiusStatAuthenIpv4Requests = _HwRadiusStatAuthenIpv4Requests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 3),
    _HwRadiusStatAuthenIpv4Requests_Type()
)
hwRadiusStatAuthenIpv4Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Requests.setStatus("current")


class _HwRadiusStatAuthenIpv4Accepts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Accepts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Accepts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Accepts_Object = MibTableColumn
hwRadiusStatAuthenIpv4Accepts = _HwRadiusStatAuthenIpv4Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 4),
    _HwRadiusStatAuthenIpv4Accepts_Type()
)
hwRadiusStatAuthenIpv4Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Accepts.setStatus("current")


class _HwRadiusStatAuthenIpv4Rejects_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Rejects based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Rejects_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Rejects_Object = MibTableColumn
hwRadiusStatAuthenIpv4Rejects = _HwRadiusStatAuthenIpv4Rejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 5),
    _HwRadiusStatAuthenIpv4Rejects_Type()
)
hwRadiusStatAuthenIpv4Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Rejects.setStatus("current")


class _HwRadiusStatAuthenIpv4Retransmissions_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Retransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Retransmissions_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Retransmissions_Object = MibTableColumn
hwRadiusStatAuthenIpv4Retransmissions = _HwRadiusStatAuthenIpv4Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 6),
    _HwRadiusStatAuthenIpv4Retransmissions_Type()
)
hwRadiusStatAuthenIpv4Retransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Retransmissions.setStatus("current")


class _HwRadiusStatAuthenIpv4Challenges_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Challenges based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Challenges_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Challenges_Object = MibTableColumn
hwRadiusStatAuthenIpv4Challenges = _HwRadiusStatAuthenIpv4Challenges_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 7),
    _HwRadiusStatAuthenIpv4Challenges_Type()
)
hwRadiusStatAuthenIpv4Challenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Challenges.setStatus("current")


class _HwRadiusStatAuthenIpv4MalformedResponses_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4MalformedResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4MalformedResponses_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4MalformedResponses_Object = MibTableColumn
hwRadiusStatAuthenIpv4MalformedResponses = _HwRadiusStatAuthenIpv4MalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 8),
    _HwRadiusStatAuthenIpv4MalformedResponses_Type()
)
hwRadiusStatAuthenIpv4MalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4MalformedResponses.setStatus("current")


class _HwRadiusStatAuthenIpv4BadAuthenticators_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4BadAuthenticators based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4BadAuthenticators_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4BadAuthenticators_Object = MibTableColumn
hwRadiusStatAuthenIpv4BadAuthenticators = _HwRadiusStatAuthenIpv4BadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 9),
    _HwRadiusStatAuthenIpv4BadAuthenticators_Type()
)
hwRadiusStatAuthenIpv4BadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4BadAuthenticators.setStatus("current")


class _HwRadiusStatAuthenIpv4PendingRequests_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4PendingRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4PendingRequests_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4PendingRequests_Object = MibTableColumn
hwRadiusStatAuthenIpv4PendingRequests = _HwRadiusStatAuthenIpv4PendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 10),
    _HwRadiusStatAuthenIpv4PendingRequests_Type()
)
hwRadiusStatAuthenIpv4PendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4PendingRequests.setStatus("current")


class _HwRadiusStatAuthenIpv4Timeouts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4Timeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4Timeouts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4Timeouts_Object = MibTableColumn
hwRadiusStatAuthenIpv4Timeouts = _HwRadiusStatAuthenIpv4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 11),
    _HwRadiusStatAuthenIpv4Timeouts_Type()
)
hwRadiusStatAuthenIpv4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4Timeouts.setStatus("current")


class _HwRadiusStatAuthenIpv4UnknownTypes_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4UnknownTypes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4UnknownTypes_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4UnknownTypes_Object = MibTableColumn
hwRadiusStatAuthenIpv4UnknownTypes = _HwRadiusStatAuthenIpv4UnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 12),
    _HwRadiusStatAuthenIpv4UnknownTypes_Type()
)
hwRadiusStatAuthenIpv4UnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4UnknownTypes.setStatus("current")


class _HwRadiusStatAuthenIpv4DroppedPackets_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv4DroppedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv4DroppedPackets_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv4DroppedPackets_Object = MibTableColumn
hwRadiusStatAuthenIpv4DroppedPackets = _HwRadiusStatAuthenIpv4DroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 6, 1, 13),
    _HwRadiusStatAuthenIpv4DroppedPackets_Type()
)
hwRadiusStatAuthenIpv4DroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv4DroppedPackets.setStatus("current")
_HwRadiusStatAcctIpv4Table_Object = MibTable
hwRadiusStatAcctIpv4Table = _HwRadiusStatAcctIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7)
)
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Table.setStatus("current")
_HwRadiusStatAcctIpv4Entry_Object = MibTableRow
hwRadiusStatAcctIpv4Entry = _HwRadiusStatAcctIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1)
)
hwRadiusStatAcctIpv4Entry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAcctIpv4ServerIP"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAcctIpv4Vrf"),
)
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Entry.setStatus("current")
_HwRadiusStatAcctIpv4ServerIP_Type = IpAddress
_HwRadiusStatAcctIpv4ServerIP_Object = MibTableColumn
hwRadiusStatAcctIpv4ServerIP = _HwRadiusStatAcctIpv4ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 1),
    _HwRadiusStatAcctIpv4ServerIP_Type()
)
hwRadiusStatAcctIpv4ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4ServerIP.setStatus("current")


class _HwRadiusStatAcctIpv4Vrf_Type(OctetString):
    """Custom type hwRadiusStatAcctIpv4Vrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusStatAcctIpv4Vrf_Type.__name__ = "OctetString"
_HwRadiusStatAcctIpv4Vrf_Object = MibTableColumn
hwRadiusStatAcctIpv4Vrf = _HwRadiusStatAcctIpv4Vrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 2),
    _HwRadiusStatAcctIpv4Vrf_Type()
)
hwRadiusStatAcctIpv4Vrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Vrf.setStatus("current")


class _HwRadiusStatAcctIpv4Requests_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4Requests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4Requests_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4Requests_Object = MibTableColumn
hwRadiusStatAcctIpv4Requests = _HwRadiusStatAcctIpv4Requests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 3),
    _HwRadiusStatAcctIpv4Requests_Type()
)
hwRadiusStatAcctIpv4Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Requests.setStatus("current")


class _HwRadiusStatAcctIpv4Responses_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4Responses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4Responses_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4Responses_Object = MibTableColumn
hwRadiusStatAcctIpv4Responses = _HwRadiusStatAcctIpv4Responses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 4),
    _HwRadiusStatAcctIpv4Responses_Type()
)
hwRadiusStatAcctIpv4Responses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Responses.setStatus("current")


class _HwRadiusStatAcctIpv4Retransmissions_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4Retransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4Retransmissions_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4Retransmissions_Object = MibTableColumn
hwRadiusStatAcctIpv4Retransmissions = _HwRadiusStatAcctIpv4Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 5),
    _HwRadiusStatAcctIpv4Retransmissions_Type()
)
hwRadiusStatAcctIpv4Retransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Retransmissions.setStatus("current")


class _HwRadiusStatAcctIpv4MalformedResponses_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4MalformedResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4MalformedResponses_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4MalformedResponses_Object = MibTableColumn
hwRadiusStatAcctIpv4MalformedResponses = _HwRadiusStatAcctIpv4MalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 6),
    _HwRadiusStatAcctIpv4MalformedResponses_Type()
)
hwRadiusStatAcctIpv4MalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4MalformedResponses.setStatus("current")


class _HwRadiusStatAcctIpv4BadAuthenticators_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4BadAuthenticators based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4BadAuthenticators_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4BadAuthenticators_Object = MibTableColumn
hwRadiusStatAcctIpv4BadAuthenticators = _HwRadiusStatAcctIpv4BadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 7),
    _HwRadiusStatAcctIpv4BadAuthenticators_Type()
)
hwRadiusStatAcctIpv4BadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4BadAuthenticators.setStatus("current")


class _HwRadiusStatAcctIpv4PendingRequests_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4PendingRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4PendingRequests_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4PendingRequests_Object = MibTableColumn
hwRadiusStatAcctIpv4PendingRequests = _HwRadiusStatAcctIpv4PendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 8),
    _HwRadiusStatAcctIpv4PendingRequests_Type()
)
hwRadiusStatAcctIpv4PendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4PendingRequests.setStatus("current")


class _HwRadiusStatAcctIpv4Timeouts_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4Timeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4Timeouts_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4Timeouts_Object = MibTableColumn
hwRadiusStatAcctIpv4Timeouts = _HwRadiusStatAcctIpv4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 9),
    _HwRadiusStatAcctIpv4Timeouts_Type()
)
hwRadiusStatAcctIpv4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4Timeouts.setStatus("current")


class _HwRadiusStatAcctIpv4UnknownTypes_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4UnknownTypes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4UnknownTypes_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4UnknownTypes_Object = MibTableColumn
hwRadiusStatAcctIpv4UnknownTypes = _HwRadiusStatAcctIpv4UnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 10),
    _HwRadiusStatAcctIpv4UnknownTypes_Type()
)
hwRadiusStatAcctIpv4UnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4UnknownTypes.setStatus("current")


class _HwRadiusStatAcctIpv4DroppedPackets_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv4DroppedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv4DroppedPackets_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv4DroppedPackets_Object = MibTableColumn
hwRadiusStatAcctIpv4DroppedPackets = _HwRadiusStatAcctIpv4DroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 7, 1, 11),
    _HwRadiusStatAcctIpv4DroppedPackets_Type()
)
hwRadiusStatAcctIpv4DroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv4DroppedPackets.setStatus("current")
_HwRadiusStatAuthorIpv4Table_Object = MibTable
hwRadiusStatAuthorIpv4Table = _HwRadiusStatAuthorIpv4Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8)
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Table.setStatus("current")
_HwRadiusStatAuthorIpv4Entry_Object = MibTableRow
hwRadiusStatAuthorIpv4Entry = _HwRadiusStatAuthorIpv4Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1)
)
hwRadiusStatAuthorIpv4Entry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthorIpv4ServerType"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthorIpv4ServerIP"),
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthorIpv4Vrf"),
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Entry.setStatus("current")


class _HwRadiusStatAuthorIpv4ServerType_Type(Integer32):
    """Custom type hwRadiusStatAuthorIpv4ServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_HwRadiusStatAuthorIpv4ServerType_Type.__name__ = "Integer32"
_HwRadiusStatAuthorIpv4ServerType_Object = MibTableColumn
hwRadiusStatAuthorIpv4ServerType = _HwRadiusStatAuthorIpv4ServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 1),
    _HwRadiusStatAuthorIpv4ServerType_Type()
)
hwRadiusStatAuthorIpv4ServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4ServerType.setStatus("current")
_HwRadiusStatAuthorIpv4ServerIP_Type = IpAddress
_HwRadiusStatAuthorIpv4ServerIP_Object = MibTableColumn
hwRadiusStatAuthorIpv4ServerIP = _HwRadiusStatAuthorIpv4ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 2),
    _HwRadiusStatAuthorIpv4ServerIP_Type()
)
hwRadiusStatAuthorIpv4ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4ServerIP.setStatus("current")


class _HwRadiusStatAuthorIpv4Vrf_Type(OctetString):
    """Custom type hwRadiusStatAuthorIpv4Vrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRadiusStatAuthorIpv4Vrf_Type.__name__ = "OctetString"
_HwRadiusStatAuthorIpv4Vrf_Object = MibTableColumn
hwRadiusStatAuthorIpv4Vrf = _HwRadiusStatAuthorIpv4Vrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 3),
    _HwRadiusStatAuthorIpv4Vrf_Type()
)
hwRadiusStatAuthorIpv4Vrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Vrf.setStatus("current")


class _HwRadiusStatAuthorIpv4Requests_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4Requests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4Requests_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4Requests_Object = MibTableColumn
hwRadiusStatAuthorIpv4Requests = _HwRadiusStatAuthorIpv4Requests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 4),
    _HwRadiusStatAuthorIpv4Requests_Type()
)
hwRadiusStatAuthorIpv4Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Requests.setStatus("current")


class _HwRadiusStatAuthorIpv4Accepts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4Accepts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4Accepts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4Accepts_Object = MibTableColumn
hwRadiusStatAuthorIpv4Accepts = _HwRadiusStatAuthorIpv4Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 5),
    _HwRadiusStatAuthorIpv4Accepts_Type()
)
hwRadiusStatAuthorIpv4Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Accepts.setStatus("current")


class _HwRadiusStatAuthorIpv4Rejects_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4Rejects based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4Rejects_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4Rejects_Object = MibTableColumn
hwRadiusStatAuthorIpv4Rejects = _HwRadiusStatAuthorIpv4Rejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 6),
    _HwRadiusStatAuthorIpv4Rejects_Type()
)
hwRadiusStatAuthorIpv4Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Rejects.setStatus("current")


class _HwRadiusStatAuthorIpv4BadAuthenticators_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4BadAuthenticators based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4BadAuthenticators_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4BadAuthenticators_Object = MibTableColumn
hwRadiusStatAuthorIpv4BadAuthenticators = _HwRadiusStatAuthorIpv4BadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 7),
    _HwRadiusStatAuthorIpv4BadAuthenticators_Type()
)
hwRadiusStatAuthorIpv4BadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4BadAuthenticators.setStatus("current")


class _HwRadiusStatAuthorIpv4Retransmissions_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4Retransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4Retransmissions_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4Retransmissions_Object = MibTableColumn
hwRadiusStatAuthorIpv4Retransmissions = _HwRadiusStatAuthorIpv4Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 8),
    _HwRadiusStatAuthorIpv4Retransmissions_Type()
)
hwRadiusStatAuthorIpv4Retransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Retransmissions.setStatus("current")


class _HwRadiusStatAuthorIpv4MalformedResponses_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4MalformedResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4MalformedResponses_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4MalformedResponses_Object = MibTableColumn
hwRadiusStatAuthorIpv4MalformedResponses = _HwRadiusStatAuthorIpv4MalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 9),
    _HwRadiusStatAuthorIpv4MalformedResponses_Type()
)
hwRadiusStatAuthorIpv4MalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4MalformedResponses.setStatus("current")


class _HwRadiusStatAuthorIpv4Timeouts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4Timeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4Timeouts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4Timeouts_Object = MibTableColumn
hwRadiusStatAuthorIpv4Timeouts = _HwRadiusStatAuthorIpv4Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 10),
    _HwRadiusStatAuthorIpv4Timeouts_Type()
)
hwRadiusStatAuthorIpv4Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4Timeouts.setStatus("current")


class _HwRadiusStatAuthorIpv4UnknownTypes_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4UnknownTypes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4UnknownTypes_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4UnknownTypes_Object = MibTableColumn
hwRadiusStatAuthorIpv4UnknownTypes = _HwRadiusStatAuthorIpv4UnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 11),
    _HwRadiusStatAuthorIpv4UnknownTypes_Type()
)
hwRadiusStatAuthorIpv4UnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4UnknownTypes.setStatus("current")


class _HwRadiusStatAuthorIpv4DroppedPackets_Type(Unsigned32):
    """Custom type hwRadiusStatAuthorIpv4DroppedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthorIpv4DroppedPackets_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthorIpv4DroppedPackets_Object = MibTableColumn
hwRadiusStatAuthorIpv4DroppedPackets = _HwRadiusStatAuthorIpv4DroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 8, 1, 12),
    _HwRadiusStatAuthorIpv4DroppedPackets_Type()
)
hwRadiusStatAuthorIpv4DroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthorIpv4DroppedPackets.setStatus("current")
_HwRadiusStatAuthenIpv6Table_Object = MibTable
hwRadiusStatAuthenIpv6Table = _HwRadiusStatAuthenIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9)
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Table.setStatus("current")
_HwRadiusStatAuthenIpv6Entry_Object = MibTableRow
hwRadiusStatAuthenIpv6Entry = _HwRadiusStatAuthenIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1)
)
hwRadiusStatAuthenIpv6Entry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAuthenIpv6ServerIP"),
)
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Entry.setStatus("current")
_HwRadiusStatAuthenIpv6ServerIP_Type = Ipv6Address
_HwRadiusStatAuthenIpv6ServerIP_Object = MibTableColumn
hwRadiusStatAuthenIpv6ServerIP = _HwRadiusStatAuthenIpv6ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 1),
    _HwRadiusStatAuthenIpv6ServerIP_Type()
)
hwRadiusStatAuthenIpv6ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6ServerIP.setStatus("current")


class _HwRadiusStatAuthenIpv6Requests_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Requests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Requests_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Requests_Object = MibTableColumn
hwRadiusStatAuthenIpv6Requests = _HwRadiusStatAuthenIpv6Requests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 3),
    _HwRadiusStatAuthenIpv6Requests_Type()
)
hwRadiusStatAuthenIpv6Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Requests.setStatus("current")


class _HwRadiusStatAuthenIpv6Accepts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Accepts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Accepts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Accepts_Object = MibTableColumn
hwRadiusStatAuthenIpv6Accepts = _HwRadiusStatAuthenIpv6Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 4),
    _HwRadiusStatAuthenIpv6Accepts_Type()
)
hwRadiusStatAuthenIpv6Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Accepts.setStatus("current")


class _HwRadiusStatAuthenIpv6Rejects_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Rejects based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Rejects_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Rejects_Object = MibTableColumn
hwRadiusStatAuthenIpv6Rejects = _HwRadiusStatAuthenIpv6Rejects_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 5),
    _HwRadiusStatAuthenIpv6Rejects_Type()
)
hwRadiusStatAuthenIpv6Rejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Rejects.setStatus("current")


class _HwRadiusStatAuthenIpv6Retransmissions_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Retransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Retransmissions_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Retransmissions_Object = MibTableColumn
hwRadiusStatAuthenIpv6Retransmissions = _HwRadiusStatAuthenIpv6Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 6),
    _HwRadiusStatAuthenIpv6Retransmissions_Type()
)
hwRadiusStatAuthenIpv6Retransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Retransmissions.setStatus("current")


class _HwRadiusStatAuthenIpv6Challenges_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Challenges based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Challenges_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Challenges_Object = MibTableColumn
hwRadiusStatAuthenIpv6Challenges = _HwRadiusStatAuthenIpv6Challenges_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 7),
    _HwRadiusStatAuthenIpv6Challenges_Type()
)
hwRadiusStatAuthenIpv6Challenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Challenges.setStatus("current")


class _HwRadiusStatAuthenIpv6MalformedResponses_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6MalformedResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6MalformedResponses_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6MalformedResponses_Object = MibTableColumn
hwRadiusStatAuthenIpv6MalformedResponses = _HwRadiusStatAuthenIpv6MalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 8),
    _HwRadiusStatAuthenIpv6MalformedResponses_Type()
)
hwRadiusStatAuthenIpv6MalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6MalformedResponses.setStatus("current")


class _HwRadiusStatAuthenIpv6BadAuthenticators_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6BadAuthenticators based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6BadAuthenticators_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6BadAuthenticators_Object = MibTableColumn
hwRadiusStatAuthenIpv6BadAuthenticators = _HwRadiusStatAuthenIpv6BadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 9),
    _HwRadiusStatAuthenIpv6BadAuthenticators_Type()
)
hwRadiusStatAuthenIpv6BadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6BadAuthenticators.setStatus("current")


class _HwRadiusStatAuthenIpv6PendingRequests_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6PendingRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6PendingRequests_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6PendingRequests_Object = MibTableColumn
hwRadiusStatAuthenIpv6PendingRequests = _HwRadiusStatAuthenIpv6PendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 10),
    _HwRadiusStatAuthenIpv6PendingRequests_Type()
)
hwRadiusStatAuthenIpv6PendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6PendingRequests.setStatus("current")


class _HwRadiusStatAuthenIpv6Timeouts_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6Timeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6Timeouts_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6Timeouts_Object = MibTableColumn
hwRadiusStatAuthenIpv6Timeouts = _HwRadiusStatAuthenIpv6Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 11),
    _HwRadiusStatAuthenIpv6Timeouts_Type()
)
hwRadiusStatAuthenIpv6Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6Timeouts.setStatus("current")


class _HwRadiusStatAuthenIpv6UnknownTypes_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6UnknownTypes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6UnknownTypes_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6UnknownTypes_Object = MibTableColumn
hwRadiusStatAuthenIpv6UnknownTypes = _HwRadiusStatAuthenIpv6UnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 12),
    _HwRadiusStatAuthenIpv6UnknownTypes_Type()
)
hwRadiusStatAuthenIpv6UnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6UnknownTypes.setStatus("current")


class _HwRadiusStatAuthenIpv6DroppedPackets_Type(Unsigned32):
    """Custom type hwRadiusStatAuthenIpv6DroppedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAuthenIpv6DroppedPackets_Type.__name__ = "Unsigned32"
_HwRadiusStatAuthenIpv6DroppedPackets_Object = MibTableColumn
hwRadiusStatAuthenIpv6DroppedPackets = _HwRadiusStatAuthenIpv6DroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 9, 1, 13),
    _HwRadiusStatAuthenIpv6DroppedPackets_Type()
)
hwRadiusStatAuthenIpv6DroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAuthenIpv6DroppedPackets.setStatus("current")
_HwRadiusStatAcctIpv6Table_Object = MibTable
hwRadiusStatAcctIpv6Table = _HwRadiusStatAcctIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10)
)
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Table.setStatus("current")
_HwRadiusStatAcctIpv6Entry_Object = MibTableRow
hwRadiusStatAcctIpv6Entry = _HwRadiusStatAcctIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1)
)
hwRadiusStatAcctIpv6Entry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwRadiusStatAcctIpv6ServerIP"),
)
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Entry.setStatus("current")
_HwRadiusStatAcctIpv6ServerIP_Type = Ipv6Address
_HwRadiusStatAcctIpv6ServerIP_Object = MibTableColumn
hwRadiusStatAcctIpv6ServerIP = _HwRadiusStatAcctIpv6ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 1),
    _HwRadiusStatAcctIpv6ServerIP_Type()
)
hwRadiusStatAcctIpv6ServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6ServerIP.setStatus("current")


class _HwRadiusStatAcctIpv6Requests_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6Requests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6Requests_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6Requests_Object = MibTableColumn
hwRadiusStatAcctIpv6Requests = _HwRadiusStatAcctIpv6Requests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 3),
    _HwRadiusStatAcctIpv6Requests_Type()
)
hwRadiusStatAcctIpv6Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Requests.setStatus("current")


class _HwRadiusStatAcctIpv6Responses_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6Responses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6Responses_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6Responses_Object = MibTableColumn
hwRadiusStatAcctIpv6Responses = _HwRadiusStatAcctIpv6Responses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 4),
    _HwRadiusStatAcctIpv6Responses_Type()
)
hwRadiusStatAcctIpv6Responses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Responses.setStatus("current")


class _HwRadiusStatAcctIpv6Retransmissions_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6Retransmissions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6Retransmissions_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6Retransmissions_Object = MibTableColumn
hwRadiusStatAcctIpv6Retransmissions = _HwRadiusStatAcctIpv6Retransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 5),
    _HwRadiusStatAcctIpv6Retransmissions_Type()
)
hwRadiusStatAcctIpv6Retransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Retransmissions.setStatus("current")


class _HwRadiusStatAcctIpv6MalformedResponses_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6MalformedResponses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6MalformedResponses_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6MalformedResponses_Object = MibTableColumn
hwRadiusStatAcctIpv6MalformedResponses = _HwRadiusStatAcctIpv6MalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 6),
    _HwRadiusStatAcctIpv6MalformedResponses_Type()
)
hwRadiusStatAcctIpv6MalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6MalformedResponses.setStatus("current")


class _HwRadiusStatAcctIpv6BadAuthenticators_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6BadAuthenticators based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6BadAuthenticators_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6BadAuthenticators_Object = MibTableColumn
hwRadiusStatAcctIpv6BadAuthenticators = _HwRadiusStatAcctIpv6BadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 7),
    _HwRadiusStatAcctIpv6BadAuthenticators_Type()
)
hwRadiusStatAcctIpv6BadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6BadAuthenticators.setStatus("current")


class _HwRadiusStatAcctIpv6PendingRequests_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6PendingRequests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6PendingRequests_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6PendingRequests_Object = MibTableColumn
hwRadiusStatAcctIpv6PendingRequests = _HwRadiusStatAcctIpv6PendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 8),
    _HwRadiusStatAcctIpv6PendingRequests_Type()
)
hwRadiusStatAcctIpv6PendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6PendingRequests.setStatus("current")


class _HwRadiusStatAcctIpv6Timeouts_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6Timeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6Timeouts_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6Timeouts_Object = MibTableColumn
hwRadiusStatAcctIpv6Timeouts = _HwRadiusStatAcctIpv6Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 9),
    _HwRadiusStatAcctIpv6Timeouts_Type()
)
hwRadiusStatAcctIpv6Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6Timeouts.setStatus("current")


class _HwRadiusStatAcctIpv6UnknownTypes_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6UnknownTypes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6UnknownTypes_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6UnknownTypes_Object = MibTableColumn
hwRadiusStatAcctIpv6UnknownTypes = _HwRadiusStatAcctIpv6UnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 10),
    _HwRadiusStatAcctIpv6UnknownTypes_Type()
)
hwRadiusStatAcctIpv6UnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6UnknownTypes.setStatus("current")


class _HwRadiusStatAcctIpv6DroppedPackets_Type(Unsigned32):
    """Custom type hwRadiusStatAcctIpv6DroppedPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwRadiusStatAcctIpv6DroppedPackets_Type.__name__ = "Unsigned32"
_HwRadiusStatAcctIpv6DroppedPackets_Object = MibTableColumn
hwRadiusStatAcctIpv6DroppedPackets = _HwRadiusStatAcctIpv6DroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 10, 1, 11),
    _HwRadiusStatAcctIpv6DroppedPackets_Type()
)
hwRadiusStatAcctIpv6DroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadiusStatAcctIpv6DroppedPackets.setStatus("current")
_HwRadiusAttrCountTable_Object = MibTable
hwRadiusAttrCountTable = _HwRadiusAttrCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11)
)
if mibBuilder.loadTexts:
    hwRadiusAttrCountTable.setStatus("current")
_HwRadiusAttrCountEntry_Object = MibTableRow
hwRadiusAttrCountEntry = _HwRadiusAttrCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1)
)
hwRadiusAttrCountEntry.setIndexNames(
    (0, "HUAWEI-BRAS-RADIUS-MIB", "hwAttributeName"),
)
if mibBuilder.loadTexts:
    hwRadiusAttrCountEntry.setStatus("current")


class _HwAttributeName_Type(DisplayString):
    """Custom type hwAttributeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwAttributeName_Type.__name__ = "DisplayString"
_HwAttributeName_Object = MibTableColumn
hwAttributeName = _HwAttributeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 1),
    _HwAttributeName_Type()
)
hwAttributeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAttributeName.setStatus("current")


class _HwAuthRequestPacketNum_Type(Integer32):
    """Custom type hwAuthRequestPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAuthRequestPacketNum_Type.__name__ = "Integer32"
_HwAuthRequestPacketNum_Object = MibTableColumn
hwAuthRequestPacketNum = _HwAuthRequestPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 2),
    _HwAuthRequestPacketNum_Type()
)
hwAuthRequestPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthRequestPacketNum.setStatus("current")


class _HwAuthAcceptPacketNum_Type(Integer32):
    """Custom type hwAuthAcceptPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAuthAcceptPacketNum_Type.__name__ = "Integer32"
_HwAuthAcceptPacketNum_Object = MibTableColumn
hwAuthAcceptPacketNum = _HwAuthAcceptPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 3),
    _HwAuthAcceptPacketNum_Type()
)
hwAuthAcceptPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthAcceptPacketNum.setStatus("current")


class _HwAuthRejectPacketNum_Type(Integer32):
    """Custom type hwAuthRejectPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAuthRejectPacketNum_Type.__name__ = "Integer32"
_HwAuthRejectPacketNum_Object = MibTableColumn
hwAuthRejectPacketNum = _HwAuthRejectPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 4),
    _HwAuthRejectPacketNum_Type()
)
hwAuthRejectPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAuthRejectPacketNum.setStatus("current")


class _HwAcctRequestPacketNum_Type(Integer32):
    """Custom type hwAcctRequestPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAcctRequestPacketNum_Type.__name__ = "Integer32"
_HwAcctRequestPacketNum_Object = MibTableColumn
hwAcctRequestPacketNum = _HwAcctRequestPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 5),
    _HwAcctRequestPacketNum_Type()
)
hwAcctRequestPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcctRequestPacketNum.setStatus("current")


class _HwAcctResponsePacketNum_Type(Integer32):
    """Custom type hwAcctResponsePacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwAcctResponsePacketNum_Type.__name__ = "Integer32"
_HwAcctResponsePacketNum_Object = MibTableColumn
hwAcctResponsePacketNum = _HwAcctResponsePacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 6),
    _HwAcctResponsePacketNum_Type()
)
hwAcctResponsePacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcctResponsePacketNum.setStatus("current")


class _HwCOARequestPacketNum_Type(Integer32):
    """Custom type hwCOARequestPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwCOARequestPacketNum_Type.__name__ = "Integer32"
_HwCOARequestPacketNum_Object = MibTableColumn
hwCOARequestPacketNum = _HwCOARequestPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 7),
    _HwCOARequestPacketNum_Type()
)
hwCOARequestPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCOARequestPacketNum.setStatus("current")


class _HwCOAAcknowledgePacketNum_Type(Integer32):
    """Custom type hwCOAAcknowledgePacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwCOAAcknowledgePacketNum_Type.__name__ = "Integer32"
_HwCOAAcknowledgePacketNum_Object = MibTableColumn
hwCOAAcknowledgePacketNum = _HwCOAAcknowledgePacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 8),
    _HwCOAAcknowledgePacketNum_Type()
)
hwCOAAcknowledgePacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCOAAcknowledgePacketNum.setStatus("current")


class _HwDMRequestPacketNum_Type(Integer32):
    """Custom type hwDMRequestPacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwDMRequestPacketNum_Type.__name__ = "Integer32"
_HwDMRequestPacketNum_Object = MibTableColumn
hwDMRequestPacketNum = _HwDMRequestPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 9),
    _HwDMRequestPacketNum_Type()
)
hwDMRequestPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDMRequestPacketNum.setStatus("current")


class _HwDMAcknowledgePacketNum_Type(Integer32):
    """Custom type hwDMAcknowledgePacketNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwDMAcknowledgePacketNum_Type.__name__ = "Integer32"
_HwDMAcknowledgePacketNum_Object = MibTableColumn
hwDMAcknowledgePacketNum = _HwDMAcknowledgePacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 1, 11, 1, 10),
    _HwDMAcknowledgePacketNum_Type()
)
hwDMAcknowledgePacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDMAcknowledgePacketNum.setStatus("current")
_HwRadiusMIBTrap_ObjectIdentity = ObjectIdentity
hwRadiusMIBTrap = _HwRadiusMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2)
)
_HwRadiusTrapObject_ObjectIdentity = ObjectIdentity
hwRadiusTrapObject = _HwRadiusTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 1)
)
_HwStateChangeServerIp_Type = IpAddress
_HwStateChangeServerIp_Object = MibScalar
hwStateChangeServerIp = _HwStateChangeServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 1, 1),
    _HwStateChangeServerIp_Type()
)
hwStateChangeServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStateChangeServerIp.setStatus("current")


class _HwStateChangeServerVrf_Type(OctetString):
    """Custom type hwStateChangeServerVrf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwStateChangeServerVrf_Type.__name__ = "OctetString"
_HwStateChangeServerVrf_Object = MibScalar
hwStateChangeServerVrf = _HwStateChangeServerVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 1, 2),
    _HwStateChangeServerVrf_Type()
)
hwStateChangeServerVrf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStateChangeServerVrf.setStatus("current")
_HwRadiusTrapsDefine_ObjectIdentity = ObjectIdentity
hwRadiusTrapsDefine = _HwRadiusTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2)
)
_HwRadiusServerTraps_ObjectIdentity = ObjectIdentity
hwRadiusServerTraps = _HwRadiusServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2, 1)
)
_HwRadiusConformance_ObjectIdentity = ObjectIdentity
hwRadiusConformance = _HwRadiusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3)
)
_HwRadiusCompliances_ObjectIdentity = ObjectIdentity
hwRadiusCompliances = _HwRadiusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 1)
)
_HwRadiusGroups_ObjectIdentity = ObjectIdentity
hwRadiusGroups = _HwRadiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2)
)

# Managed Objects groups

hwRadiusGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 1)
)
hwRadiusGroupGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusGroupName"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerKey"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerProtType"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerRetransmit"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerTimeout"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerAttrTran"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusPacketUnit"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusDomainInclude"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClassASCar"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAlgorithm"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerNasPortFmt"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusGroupRowStatus"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerSourceInterface"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerNasIpAddress"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerCallingStationId"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerCallingStationIdDelimiter"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAttributeNoExistPolicy"))
)
if mibBuilder.loadTexts:
    hwRadiusGroupGroup.setStatus("current")

hwRadiusServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 2)
)
hwRadiusServerGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerIndex"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerType"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerVRF"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerIP"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerPort"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerWeight"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerSecretKey"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerRowStatus"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerPktSendNumber"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerPktSendInterval"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerSourceInterfaceEachServer"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerResponses"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerSecretKeyType"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerDeadCount"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerDeadTime"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusServerDeadInterval"))
)
if mibBuilder.loadTexts:
    hwRadiusServerGroup.setStatus("current")

hwRadiusClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 3)
)
hwRadiusClientGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientIP"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientVrf"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientKey"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientGroupName"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusClientRowStatus"))
)
if mibBuilder.loadTexts:
    hwRadiusClientGroup.setStatus("current")

hwRadiusAuthorServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 4)
)
hwRadiusAuthorServerGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerIP"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerVrf"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerKey"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerGroupName"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthorServerRowStatus"))
)
if mibBuilder.loadTexts:
    hwRadiusAuthorServerGroup.setStatus("current")

hwRadiusSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 5)
)
hwRadiusSettingGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwEnableSourcePortsExtended"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwSourcePortsExtendedStartPort"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwSourcePortsExtendedPortNum"))
)
if mibBuilder.loadTexts:
    hwRadiusSettingGroup.setStatus("current")

hwRadiusTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 6)
)
hwRadiusTrapObjectGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerIp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerVrf"))
)
if mibBuilder.loadTexts:
    hwRadiusTrapObjectGroup.setStatus("current")


# Notification objects

hwRadiusAuthServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2, 1, 1)
)
hwRadiusAuthServerUp.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerIp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerVrf"))
)
if mibBuilder.loadTexts:
    hwRadiusAuthServerUp.setStatus(
        "current"
    )

hwRadiusAuthServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2, 1, 2)
)
hwRadiusAuthServerDown.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerIp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerVrf"))
)
if mibBuilder.loadTexts:
    hwRadiusAuthServerDown.setStatus(
        "current"
    )

hwRadiusAcctServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2, 1, 3)
)
hwRadiusAcctServerUp.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerIp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerVrf"))
)
if mibBuilder.loadTexts:
    hwRadiusAcctServerUp.setStatus(
        "current"
    )

hwRadiusAcctServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 2, 2, 1, 4)
)
hwRadiusAcctServerDown.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerIp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwStateChangeServerVrf"))
)
if mibBuilder.loadTexts:
    hwRadiusAcctServerDown.setStatus(
        "current"
    )


# Notifications groups

hwRadiusTrapsDefineGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 2, 7)
)
hwRadiusTrapsDefineGroup.setObjects(
      *(("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthServerUp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAuthServerDown"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAcctServerUp"),
        ("HUAWEI-BRAS-RADIUS-MIB", "hwRadiusAcctServerDown"))
)
if mibBuilder.loadTexts:
    hwRadiusTrapsDefineGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwRadiusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwRadiusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-RADIUS-MIB",
    **{"hwBRASRadius": hwBRASRadius,
       "hwRadiusGroupObject": hwRadiusGroupObject,
       "hwRadiusGroupTable": hwRadiusGroupTable,
       "hwRadiusGroupEntry": hwRadiusGroupEntry,
       "hwRadiusGroupName": hwRadiusGroupName,
       "hwRadiusServerKey": hwRadiusServerKey,
       "hwRadiusServerProtType": hwRadiusServerProtType,
       "hwRadiusServerRetransmit": hwRadiusServerRetransmit,
       "hwRadiusServerTimeout": hwRadiusServerTimeout,
       "hwRadiusServerAttrTran": hwRadiusServerAttrTran,
       "hwRadiusPacketUnit": hwRadiusPacketUnit,
       "hwRadiusDomainInclude": hwRadiusDomainInclude,
       "hwRadiusClassASCar": hwRadiusClassASCar,
       "hwRadiusAlgorithm": hwRadiusAlgorithm,
       "hwRadiusServerNasPortFmt": hwRadiusServerNasPortFmt,
       "hwRadiusGroupRowStatus": hwRadiusGroupRowStatus,
       "hwRadiusServerSourceInterface": hwRadiusServerSourceInterface,
       "hwRadiusServerNasIpAddress": hwRadiusServerNasIpAddress,
       "hwRadiusServerCallingStationId": hwRadiusServerCallingStationId,
       "hwRadiusServerCallingStationIdDelimiter": hwRadiusServerCallingStationIdDelimiter,
       "hwRadiusAttributeNoExistPolicy": hwRadiusAttributeNoExistPolicy,
       "hwRadiusServerKeyType": hwRadiusServerKeyType,
       "hwRadiusServerTable": hwRadiusServerTable,
       "hwRadiusServerEntry": hwRadiusServerEntry,
       "hwRadiusServerIndex": hwRadiusServerIndex,
       "hwRadiusServerType": hwRadiusServerType,
       "hwRadiusServerVRF": hwRadiusServerVRF,
       "hwRadiusServerIP": hwRadiusServerIP,
       "hwRadiusServerPort": hwRadiusServerPort,
       "hwRadiusServerWeight": hwRadiusServerWeight,
       "hwRadiusServerSecretKey": hwRadiusServerSecretKey,
       "hwRadiusServerRowStatus": hwRadiusServerRowStatus,
       "hwRadiusServerPktSendNumber": hwRadiusServerPktSendNumber,
       "hwRadiusServerPktSendInterval": hwRadiusServerPktSendInterval,
       "hwRadiusServerSourceInterfaceEachServer": hwRadiusServerSourceInterfaceEachServer,
       "hwRadiusServerResponses": hwRadiusServerResponses,
       "hwRadiusServerSecretKeyType": hwRadiusServerSecretKeyType,
       "hwRadiusServerDeadCount": hwRadiusServerDeadCount,
       "hwRadiusServerDeadTime": hwRadiusServerDeadTime,
       "hwRadiusServerDeadInterval": hwRadiusServerDeadInterval,
       "hwRadiusClientTable": hwRadiusClientTable,
       "hwRadiusClientEntry": hwRadiusClientEntry,
       "hwRadiusClientIP": hwRadiusClientIP,
       "hwRadiusClientVrf": hwRadiusClientVrf,
       "hwRadiusClientKey": hwRadiusClientKey,
       "hwRadiusClientGroupName": hwRadiusClientGroupName,
       "hwRadiusClientRowStatus": hwRadiusClientRowStatus,
       "hwRadiusClientKeyType": hwRadiusClientKeyType,
       "hwRadiusAuthorServerTable": hwRadiusAuthorServerTable,
       "hwRadiusAuthorServerEntry": hwRadiusAuthorServerEntry,
       "hwRadiusAuthorServerIP": hwRadiusAuthorServerIP,
       "hwRadiusAuthorServerVrf": hwRadiusAuthorServerVrf,
       "hwRadiusAuthorServerKey": hwRadiusAuthorServerKey,
       "hwRadiusAuthorServerGroupName": hwRadiusAuthorServerGroupName,
       "hwRadiusAuthorServerRowStatus": hwRadiusAuthorServerRowStatus,
       "hwRadiusAuthorServerKeyType": hwRadiusAuthorServerKeyType,
       "hwRadiusSetting": hwRadiusSetting,
       "hwRadiusSettingEntry": hwRadiusSettingEntry,
       "hwEnableSourcePortsExtended": hwEnableSourcePortsExtended,
       "hwSourcePortsExtendedStartPort": hwSourcePortsExtendedStartPort,
       "hwSourcePortsExtendedPortNum": hwSourcePortsExtendedPortNum,
       "hwRadiusResetStatAll": hwRadiusResetStatAll,
       "hwResetRadiusAttrCount": hwResetRadiusAttrCount,
       "hwRadiusTotalDeadCount": hwRadiusTotalDeadCount,
       "hwRadiusTotalDeadTime": hwRadiusTotalDeadTime,
       "hwRadiusTotalDeadInterval": hwRadiusTotalDeadInterval,
       "hwRadiusStatAuthenIpv4Table": hwRadiusStatAuthenIpv4Table,
       "hwRadiusStatAuthenIpv4Entry": hwRadiusStatAuthenIpv4Entry,
       "hwRadiusStatAuthenIpv4ServerIP": hwRadiusStatAuthenIpv4ServerIP,
       "hwRadiusStatAuthenIpv4Vrf": hwRadiusStatAuthenIpv4Vrf,
       "hwRadiusStatAuthenIpv4Requests": hwRadiusStatAuthenIpv4Requests,
       "hwRadiusStatAuthenIpv4Accepts": hwRadiusStatAuthenIpv4Accepts,
       "hwRadiusStatAuthenIpv4Rejects": hwRadiusStatAuthenIpv4Rejects,
       "hwRadiusStatAuthenIpv4Retransmissions": hwRadiusStatAuthenIpv4Retransmissions,
       "hwRadiusStatAuthenIpv4Challenges": hwRadiusStatAuthenIpv4Challenges,
       "hwRadiusStatAuthenIpv4MalformedResponses": hwRadiusStatAuthenIpv4MalformedResponses,
       "hwRadiusStatAuthenIpv4BadAuthenticators": hwRadiusStatAuthenIpv4BadAuthenticators,
       "hwRadiusStatAuthenIpv4PendingRequests": hwRadiusStatAuthenIpv4PendingRequests,
       "hwRadiusStatAuthenIpv4Timeouts": hwRadiusStatAuthenIpv4Timeouts,
       "hwRadiusStatAuthenIpv4UnknownTypes": hwRadiusStatAuthenIpv4UnknownTypes,
       "hwRadiusStatAuthenIpv4DroppedPackets": hwRadiusStatAuthenIpv4DroppedPackets,
       "hwRadiusStatAcctIpv4Table": hwRadiusStatAcctIpv4Table,
       "hwRadiusStatAcctIpv4Entry": hwRadiusStatAcctIpv4Entry,
       "hwRadiusStatAcctIpv4ServerIP": hwRadiusStatAcctIpv4ServerIP,
       "hwRadiusStatAcctIpv4Vrf": hwRadiusStatAcctIpv4Vrf,
       "hwRadiusStatAcctIpv4Requests": hwRadiusStatAcctIpv4Requests,
       "hwRadiusStatAcctIpv4Responses": hwRadiusStatAcctIpv4Responses,
       "hwRadiusStatAcctIpv4Retransmissions": hwRadiusStatAcctIpv4Retransmissions,
       "hwRadiusStatAcctIpv4MalformedResponses": hwRadiusStatAcctIpv4MalformedResponses,
       "hwRadiusStatAcctIpv4BadAuthenticators": hwRadiusStatAcctIpv4BadAuthenticators,
       "hwRadiusStatAcctIpv4PendingRequests": hwRadiusStatAcctIpv4PendingRequests,
       "hwRadiusStatAcctIpv4Timeouts": hwRadiusStatAcctIpv4Timeouts,
       "hwRadiusStatAcctIpv4UnknownTypes": hwRadiusStatAcctIpv4UnknownTypes,
       "hwRadiusStatAcctIpv4DroppedPackets": hwRadiusStatAcctIpv4DroppedPackets,
       "hwRadiusStatAuthorIpv4Table": hwRadiusStatAuthorIpv4Table,
       "hwRadiusStatAuthorIpv4Entry": hwRadiusStatAuthorIpv4Entry,
       "hwRadiusStatAuthorIpv4ServerType": hwRadiusStatAuthorIpv4ServerType,
       "hwRadiusStatAuthorIpv4ServerIP": hwRadiusStatAuthorIpv4ServerIP,
       "hwRadiusStatAuthorIpv4Vrf": hwRadiusStatAuthorIpv4Vrf,
       "hwRadiusStatAuthorIpv4Requests": hwRadiusStatAuthorIpv4Requests,
       "hwRadiusStatAuthorIpv4Accepts": hwRadiusStatAuthorIpv4Accepts,
       "hwRadiusStatAuthorIpv4Rejects": hwRadiusStatAuthorIpv4Rejects,
       "hwRadiusStatAuthorIpv4BadAuthenticators": hwRadiusStatAuthorIpv4BadAuthenticators,
       "hwRadiusStatAuthorIpv4Retransmissions": hwRadiusStatAuthorIpv4Retransmissions,
       "hwRadiusStatAuthorIpv4MalformedResponses": hwRadiusStatAuthorIpv4MalformedResponses,
       "hwRadiusStatAuthorIpv4Timeouts": hwRadiusStatAuthorIpv4Timeouts,
       "hwRadiusStatAuthorIpv4UnknownTypes": hwRadiusStatAuthorIpv4UnknownTypes,
       "hwRadiusStatAuthorIpv4DroppedPackets": hwRadiusStatAuthorIpv4DroppedPackets,
       "hwRadiusStatAuthenIpv6Table": hwRadiusStatAuthenIpv6Table,
       "hwRadiusStatAuthenIpv6Entry": hwRadiusStatAuthenIpv6Entry,
       "hwRadiusStatAuthenIpv6ServerIP": hwRadiusStatAuthenIpv6ServerIP,
       "hwRadiusStatAuthenIpv6Requests": hwRadiusStatAuthenIpv6Requests,
       "hwRadiusStatAuthenIpv6Accepts": hwRadiusStatAuthenIpv6Accepts,
       "hwRadiusStatAuthenIpv6Rejects": hwRadiusStatAuthenIpv6Rejects,
       "hwRadiusStatAuthenIpv6Retransmissions": hwRadiusStatAuthenIpv6Retransmissions,
       "hwRadiusStatAuthenIpv6Challenges": hwRadiusStatAuthenIpv6Challenges,
       "hwRadiusStatAuthenIpv6MalformedResponses": hwRadiusStatAuthenIpv6MalformedResponses,
       "hwRadiusStatAuthenIpv6BadAuthenticators": hwRadiusStatAuthenIpv6BadAuthenticators,
       "hwRadiusStatAuthenIpv6PendingRequests": hwRadiusStatAuthenIpv6PendingRequests,
       "hwRadiusStatAuthenIpv6Timeouts": hwRadiusStatAuthenIpv6Timeouts,
       "hwRadiusStatAuthenIpv6UnknownTypes": hwRadiusStatAuthenIpv6UnknownTypes,
       "hwRadiusStatAuthenIpv6DroppedPackets": hwRadiusStatAuthenIpv6DroppedPackets,
       "hwRadiusStatAcctIpv6Table": hwRadiusStatAcctIpv6Table,
       "hwRadiusStatAcctIpv6Entry": hwRadiusStatAcctIpv6Entry,
       "hwRadiusStatAcctIpv6ServerIP": hwRadiusStatAcctIpv6ServerIP,
       "hwRadiusStatAcctIpv6Requests": hwRadiusStatAcctIpv6Requests,
       "hwRadiusStatAcctIpv6Responses": hwRadiusStatAcctIpv6Responses,
       "hwRadiusStatAcctIpv6Retransmissions": hwRadiusStatAcctIpv6Retransmissions,
       "hwRadiusStatAcctIpv6MalformedResponses": hwRadiusStatAcctIpv6MalformedResponses,
       "hwRadiusStatAcctIpv6BadAuthenticators": hwRadiusStatAcctIpv6BadAuthenticators,
       "hwRadiusStatAcctIpv6PendingRequests": hwRadiusStatAcctIpv6PendingRequests,
       "hwRadiusStatAcctIpv6Timeouts": hwRadiusStatAcctIpv6Timeouts,
       "hwRadiusStatAcctIpv6UnknownTypes": hwRadiusStatAcctIpv6UnknownTypes,
       "hwRadiusStatAcctIpv6DroppedPackets": hwRadiusStatAcctIpv6DroppedPackets,
       "hwRadiusAttrCountTable": hwRadiusAttrCountTable,
       "hwRadiusAttrCountEntry": hwRadiusAttrCountEntry,
       "hwAttributeName": hwAttributeName,
       "hwAuthRequestPacketNum": hwAuthRequestPacketNum,
       "hwAuthAcceptPacketNum": hwAuthAcceptPacketNum,
       "hwAuthRejectPacketNum": hwAuthRejectPacketNum,
       "hwAcctRequestPacketNum": hwAcctRequestPacketNum,
       "hwAcctResponsePacketNum": hwAcctResponsePacketNum,
       "hwCOARequestPacketNum": hwCOARequestPacketNum,
       "hwCOAAcknowledgePacketNum": hwCOAAcknowledgePacketNum,
       "hwDMRequestPacketNum": hwDMRequestPacketNum,
       "hwDMAcknowledgePacketNum": hwDMAcknowledgePacketNum,
       "hwRadiusMIBTrap": hwRadiusMIBTrap,
       "hwRadiusTrapObject": hwRadiusTrapObject,
       "hwStateChangeServerIp": hwStateChangeServerIp,
       "hwStateChangeServerVrf": hwStateChangeServerVrf,
       "hwRadiusTrapsDefine": hwRadiusTrapsDefine,
       "hwRadiusServerTraps": hwRadiusServerTraps,
       "hwRadiusAuthServerUp": hwRadiusAuthServerUp,
       "hwRadiusAuthServerDown": hwRadiusAuthServerDown,
       "hwRadiusAcctServerUp": hwRadiusAcctServerUp,
       "hwRadiusAcctServerDown": hwRadiusAcctServerDown,
       "hwRadiusConformance": hwRadiusConformance,
       "hwRadiusCompliances": hwRadiusCompliances,
       "hwRadiusCompliance": hwRadiusCompliance,
       "hwRadiusGroups": hwRadiusGroups,
       "hwRadiusGroupGroup": hwRadiusGroupGroup,
       "hwRadiusServerGroup": hwRadiusServerGroup,
       "hwRadiusClientGroup": hwRadiusClientGroup,
       "hwRadiusAuthorServerGroup": hwRadiusAuthorServerGroup,
       "hwRadiusSettingGroup": hwRadiusSettingGroup,
       "hwRadiusTrapObjectGroup": hwRadiusTrapObjectGroup,
       "hwRadiusTrapsDefineGroup": hwRadiusTrapsDefineGroup}
)
