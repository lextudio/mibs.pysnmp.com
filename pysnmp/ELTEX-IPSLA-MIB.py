# SNMP MIB module (ELTEX-IPSLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-IPSLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:12 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltexIpSlaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexIpSlaOperationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("icmp-echo", 1),
          ("udp-jitter", 2))
    )



class EltexIpSlaOperationStatus(Integer32, TextualConvention):
    status = "current"
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



class EltexIpSlaStatsOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EltexIpSlaObjects_ObjectIdentity = ObjectIdentity
eltexIpSlaObjects = _EltexIpSlaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1)
)
_EltexIpSlaAppl_ObjectIdentity = ObjectIdentity
eltexIpSlaAppl = _EltexIpSlaAppl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 1)
)
_EltexIpSlaApplResponder_ObjectIdentity = ObjectIdentity
eltexIpSlaApplResponder = _EltexIpSlaApplResponder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 1, 13)
)


class _EltexIpSlaApplResponderUdpJitterPort_Type(Integer32):
    """Custom type eltexIpSlaApplResponderUdpJitterPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIpSlaApplResponderUdpJitterPort_Type.__name__ = "Integer32"
_EltexIpSlaApplResponderUdpJitterPort_Object = MibScalar
eltexIpSlaApplResponderUdpJitterPort = _EltexIpSlaApplResponderUdpJitterPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 1, 13, 1),
    _EltexIpSlaApplResponderUdpJitterPort_Type()
)
eltexIpSlaApplResponderUdpJitterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaApplResponderUdpJitterPort.setStatus("current")
_EltexIpSlaAdmin_ObjectIdentity = ObjectIdentity
eltexIpSlaAdmin = _EltexIpSlaAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2)
)
_EltexIpSlaAdminCtrlTable_Object = MibTable
eltexIpSlaAdminCtrlTable = _EltexIpSlaAdminCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlTable.setStatus("current")
_EltexIpSlaAdminCtrlEntry_Object = MibTableRow
eltexIpSlaAdminCtrlEntry = _EltexIpSlaAdminCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1)
)
eltexIpSlaAdminCtrlEntry.setIndexNames(
    (0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminCtrlIndex"),
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlEntry.setStatus("current")
_EltexIpSlaAdminCtrlIndex_Type = Integer32
_EltexIpSlaAdminCtrlIndex_Object = MibTableColumn
eltexIpSlaAdminCtrlIndex = _EltexIpSlaAdminCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 1),
    _EltexIpSlaAdminCtrlIndex_Type()
)
eltexIpSlaAdminCtrlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlIndex.setStatus("current")
_EltexIpSlaAdminCtrlType_Type = EltexIpSlaOperationType
_EltexIpSlaAdminCtrlType_Object = MibTableColumn
eltexIpSlaAdminCtrlType = _EltexIpSlaAdminCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 2),
    _EltexIpSlaAdminCtrlType_Type()
)
eltexIpSlaAdminCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlType.setStatus("current")
_EltexIpSlaAdminCtrlStatus_Type = EltexIpSlaOperationStatus
_EltexIpSlaAdminCtrlStatus_Object = MibTableColumn
eltexIpSlaAdminCtrlStatus = _EltexIpSlaAdminCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 3),
    _EltexIpSlaAdminCtrlStatus_Type()
)
eltexIpSlaAdminCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlStatus.setStatus("current")


class _EltexIpSlaAdminCtrlFrequency_Type(Integer32):
    """Custom type eltexIpSlaAdminCtrlFrequency based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_EltexIpSlaAdminCtrlFrequency_Type.__name__ = "Integer32"
_EltexIpSlaAdminCtrlFrequency_Object = MibTableColumn
eltexIpSlaAdminCtrlFrequency = _EltexIpSlaAdminCtrlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 4),
    _EltexIpSlaAdminCtrlFrequency_Type()
)
eltexIpSlaAdminCtrlFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlFrequency.setUnits("seconds")


class _EltexIpSlaAdminCtrlTag_Type(DisplayString):
    """Custom type eltexIpSlaAdminCtrlTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltexIpSlaAdminCtrlTag_Type.__name__ = "DisplayString"
_EltexIpSlaAdminCtrlTag_Object = MibTableColumn
eltexIpSlaAdminCtrlTag = _EltexIpSlaAdminCtrlTag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 5),
    _EltexIpSlaAdminCtrlTag_Type()
)
eltexIpSlaAdminCtrlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlTag.setStatus("current")


class _EltexIpSlaAdminCtrlOwner_Type(DisplayString):
    """Custom type eltexIpSlaAdminCtrlOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltexIpSlaAdminCtrlOwner_Type.__name__ = "DisplayString"
_EltexIpSlaAdminCtrlOwner_Object = MibTableColumn
eltexIpSlaAdminCtrlOwner = _EltexIpSlaAdminCtrlOwner_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 6),
    _EltexIpSlaAdminCtrlOwner_Type()
)
eltexIpSlaAdminCtrlOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlOwner.setStatus("current")
_EltexIpSlaAdminCtrlRowStatus_Type = RowStatus
_EltexIpSlaAdminCtrlRowStatus_Object = MibTableColumn
eltexIpSlaAdminCtrlRowStatus = _EltexIpSlaAdminCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 1, 1, 7),
    _EltexIpSlaAdminCtrlRowStatus_Type()
)
eltexIpSlaAdminCtrlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminCtrlRowStatus.setStatus("current")
_EltexIpSlaAdminIcmpEchoTable_Object = MibTable
eltexIpSlaAdminIcmpEchoTable = _EltexIpSlaAdminIcmpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoTable.setStatus("current")
_EltexIpSlaAdminIcmpEchoEntry_Object = MibTableRow
eltexIpSlaAdminIcmpEchoEntry = _EltexIpSlaAdminIcmpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1)
)
eltexIpSlaAdminIcmpEchoEntry.setIndexNames(
    (0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminIcmpEchoIndex"),
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoEntry.setStatus("current")
_EltexIpSlaAdminIcmpEchoIndex_Type = Integer32
_EltexIpSlaAdminIcmpEchoIndex_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoIndex = _EltexIpSlaAdminIcmpEchoIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 1),
    _EltexIpSlaAdminIcmpEchoIndex_Type()
)
eltexIpSlaAdminIcmpEchoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoIndex.setStatus("current")
_EltexIpSlaAdminIcmpEchoTargetAddress_Type = IpAddress
_EltexIpSlaAdminIcmpEchoTargetAddress_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoTargetAddress = _EltexIpSlaAdminIcmpEchoTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 2),
    _EltexIpSlaAdminIcmpEchoTargetAddress_Type()
)
eltexIpSlaAdminIcmpEchoTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoTargetAddress.setStatus("current")
_EltexIpSlaAdminIcmpEchoSourceAddress_Type = IpAddress
_EltexIpSlaAdminIcmpEchoSourceAddress_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoSourceAddress = _EltexIpSlaAdminIcmpEchoSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 3),
    _EltexIpSlaAdminIcmpEchoSourceAddress_Type()
)
eltexIpSlaAdminIcmpEchoSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoSourceAddress.setStatus("current")
_EltexIpSlaAdminIcmpEchoSourceInterface_Type = InterfaceIndexOrZero
_EltexIpSlaAdminIcmpEchoSourceInterface_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoSourceInterface = _EltexIpSlaAdminIcmpEchoSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 4),
    _EltexIpSlaAdminIcmpEchoSourceInterface_Type()
)
eltexIpSlaAdminIcmpEchoSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoSourceInterface.setStatus("current")


class _EltexIpSlaAdminIcmpEchoTimeOut_Type(Integer32):
    """Custom type eltexIpSlaAdminIcmpEchoTimeOut based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_EltexIpSlaAdminIcmpEchoTimeOut_Type.__name__ = "Integer32"
_EltexIpSlaAdminIcmpEchoTimeOut_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoTimeOut = _EltexIpSlaAdminIcmpEchoTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 5),
    _EltexIpSlaAdminIcmpEchoTimeOut_Type()
)
eltexIpSlaAdminIcmpEchoTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoTimeOut.setUnits("milliseconds")


class _EltexIpSlaAdminIcmpEchoReqDataSize_Type(Integer32):
    """Custom type eltexIpSlaAdminIcmpEchoReqDataSize based on Integer32"""
    defaultValue = 56

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1432),
    )


_EltexIpSlaAdminIcmpEchoReqDataSize_Type.__name__ = "Integer32"
_EltexIpSlaAdminIcmpEchoReqDataSize_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoReqDataSize = _EltexIpSlaAdminIcmpEchoReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 6),
    _EltexIpSlaAdminIcmpEchoReqDataSize_Type()
)
eltexIpSlaAdminIcmpEchoReqDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoReqDataSize.setStatus("current")


class _EltexIpSlaAdminIcmpEchoTOS_Type(Integer32):
    """Custom type eltexIpSlaAdminIcmpEchoTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexIpSlaAdminIcmpEchoTOS_Type.__name__ = "Integer32"
_EltexIpSlaAdminIcmpEchoTOS_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoTOS = _EltexIpSlaAdminIcmpEchoTOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 7),
    _EltexIpSlaAdminIcmpEchoTOS_Type()
)
eltexIpSlaAdminIcmpEchoTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoTOS.setStatus("current")
_EltexIpSlaAdminIcmpEchoRowStatus_Type = RowStatus
_EltexIpSlaAdminIcmpEchoRowStatus_Object = MibTableColumn
eltexIpSlaAdminIcmpEchoRowStatus = _EltexIpSlaAdminIcmpEchoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 2, 1, 8),
    _EltexIpSlaAdminIcmpEchoRowStatus_Type()
)
eltexIpSlaAdminIcmpEchoRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminIcmpEchoRowStatus.setStatus("current")
_EltexIpSlaAdminUdpJitterTable_Object = MibTable
eltexIpSlaAdminUdpJitterTable = _EltexIpSlaAdminUdpJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTable.setStatus("current")
_EltexIpSlaAdminUdpJitterEntry_Object = MibTableRow
eltexIpSlaAdminUdpJitterEntry = _EltexIpSlaAdminUdpJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1)
)
eltexIpSlaAdminUdpJitterEntry.setIndexNames(
    (0, "ELTEX-IPSLA-MIB", "eltexIpSlaAdminUdpJitterIndex"),
)
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterEntry.setStatus("current")
_EltexIpSlaAdminUdpJitterIndex_Type = Integer32
_EltexIpSlaAdminUdpJitterIndex_Object = MibTableColumn
eltexIpSlaAdminUdpJitterIndex = _EltexIpSlaAdminUdpJitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 1),
    _EltexIpSlaAdminUdpJitterIndex_Type()
)
eltexIpSlaAdminUdpJitterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterIndex.setStatus("current")
_EltexIpSlaAdminUdpJitterTargetAddress_Type = IpAddress
_EltexIpSlaAdminUdpJitterTargetAddress_Object = MibTableColumn
eltexIpSlaAdminUdpJitterTargetAddress = _EltexIpSlaAdminUdpJitterTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 2),
    _EltexIpSlaAdminUdpJitterTargetAddress_Type()
)
eltexIpSlaAdminUdpJitterTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTargetAddress.setStatus("current")


class _EltexIpSlaAdminUdpJitterTargetPort_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIpSlaAdminUdpJitterTargetPort_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterTargetPort_Object = MibTableColumn
eltexIpSlaAdminUdpJitterTargetPort = _EltexIpSlaAdminUdpJitterTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 3),
    _EltexIpSlaAdminUdpJitterTargetPort_Type()
)
eltexIpSlaAdminUdpJitterTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTargetPort.setStatus("current")
_EltexIpSlaAdminUdpJitterSourceAddress_Type = IpAddress
_EltexIpSlaAdminUdpJitterSourceAddress_Object = MibTableColumn
eltexIpSlaAdminUdpJitterSourceAddress = _EltexIpSlaAdminUdpJitterSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 4),
    _EltexIpSlaAdminUdpJitterSourceAddress_Type()
)
eltexIpSlaAdminUdpJitterSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterSourceAddress.setStatus("current")


class _EltexIpSlaAdminUdpJitterSourcePort_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltexIpSlaAdminUdpJitterSourcePort_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterSourcePort_Object = MibTableColumn
eltexIpSlaAdminUdpJitterSourcePort = _EltexIpSlaAdminUdpJitterSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 5),
    _EltexIpSlaAdminUdpJitterSourcePort_Type()
)
eltexIpSlaAdminUdpJitterSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterSourcePort.setStatus("current")


class _EltexIpSlaAdminUdpJitterSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type eltexIpSlaAdminUdpJitterSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_EltexIpSlaAdminUdpJitterSourceInterface_Object = MibTableColumn
eltexIpSlaAdminUdpJitterSourceInterface = _EltexIpSlaAdminUdpJitterSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 6),
    _EltexIpSlaAdminUdpJitterSourceInterface_Type()
)
eltexIpSlaAdminUdpJitterSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterSourceInterface.setStatus("current")


class _EltexIpSlaAdminUdpJitterInterval_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterInterval based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_EltexIpSlaAdminUdpJitterInterval_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterInterval_Object = MibTableColumn
eltexIpSlaAdminUdpJitterInterval = _EltexIpSlaAdminUdpJitterInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 7),
    _EltexIpSlaAdminUdpJitterInterval_Type()
)
eltexIpSlaAdminUdpJitterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterInterval.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterInterval.setUnits("milliseconds")


class _EltexIpSlaAdminUdpJitterNumPackets_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterNumPackets based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EltexIpSlaAdminUdpJitterNumPackets_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterNumPackets_Object = MibTableColumn
eltexIpSlaAdminUdpJitterNumPackets = _EltexIpSlaAdminUdpJitterNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 8),
    _EltexIpSlaAdminUdpJitterNumPackets_Type()
)
eltexIpSlaAdminUdpJitterNumPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterNumPackets.setStatus("current")


class _EltexIpSlaAdminUdpJitterTimeOut_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterTimeOut based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_EltexIpSlaAdminUdpJitterTimeOut_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterTimeOut_Object = MibTableColumn
eltexIpSlaAdminUdpJitterTimeOut = _EltexIpSlaAdminUdpJitterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 9),
    _EltexIpSlaAdminUdpJitterTimeOut_Type()
)
eltexIpSlaAdminUdpJitterTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTimeOut.setUnits("milliseconds")


class _EltexIpSlaAdminUdpJitterReqDataSize_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterReqDataSize based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1432),
    )


_EltexIpSlaAdminUdpJitterReqDataSize_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterReqDataSize_Object = MibTableColumn
eltexIpSlaAdminUdpJitterReqDataSize = _EltexIpSlaAdminUdpJitterReqDataSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 10),
    _EltexIpSlaAdminUdpJitterReqDataSize_Type()
)
eltexIpSlaAdminUdpJitterReqDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterReqDataSize.setStatus("current")


class _EltexIpSlaAdminUdpJitterTOS_Type(Integer32):
    """Custom type eltexIpSlaAdminUdpJitterTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexIpSlaAdminUdpJitterTOS_Type.__name__ = "Integer32"
_EltexIpSlaAdminUdpJitterTOS_Object = MibTableColumn
eltexIpSlaAdminUdpJitterTOS = _EltexIpSlaAdminUdpJitterTOS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 11),
    _EltexIpSlaAdminUdpJitterTOS_Type()
)
eltexIpSlaAdminUdpJitterTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterTOS.setStatus("current")
_EltexIpSlaAdminUdpJitterRowStatus_Type = RowStatus
_EltexIpSlaAdminUdpJitterRowStatus_Object = MibTableColumn
eltexIpSlaAdminUdpJitterRowStatus = _EltexIpSlaAdminUdpJitterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 2, 3, 1, 12),
    _EltexIpSlaAdminUdpJitterRowStatus_Type()
)
eltexIpSlaAdminUdpJitterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaAdminUdpJitterRowStatus.setStatus("current")
_EltexIpSlaStats_ObjectIdentity = ObjectIdentity
eltexIpSlaStats = _EltexIpSlaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3)
)
_EltexIpSlaStatsIcmpEchoTable_Object = MibTable
eltexIpSlaStatsIcmpEchoTable = _EltexIpSlaStatsIcmpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoTable.setStatus("current")
_EltexIpSlaStatsIcmpEchoEntry_Object = MibTableRow
eltexIpSlaStatsIcmpEchoEntry = _EltexIpSlaStatsIcmpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1)
)
eltexIpSlaStatsIcmpEchoEntry.setIndexNames(
    (0, "ELTEX-IPSLA-MIB", "eltexIpSlaStatsIcmpEchoIndex"),
)
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoEntry.setStatus("current")
_EltexIpSlaStatsIcmpEchoIndex_Type = Integer32
_EltexIpSlaStatsIcmpEchoIndex_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoIndex = _EltexIpSlaStatsIcmpEchoIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 1),
    _EltexIpSlaStatsIcmpEchoIndex_Type()
)
eltexIpSlaStatsIcmpEchoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoIndex.setStatus("current")
_EltexIpSlaStatsIcmpEchoLastStatus_Type = EltexIpSlaStatsOperStatus
_EltexIpSlaStatsIcmpEchoLastStatus_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoLastStatus = _EltexIpSlaStatsIcmpEchoLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 2),
    _EltexIpSlaStatsIcmpEchoLastStatus_Type()
)
eltexIpSlaStatsIcmpEchoLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoLastStatus.setStatus("current")
_EltexIpSlaStatsIcmpEchoLastLatency_Type = Integer32
_EltexIpSlaStatsIcmpEchoLastLatency_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoLastLatency = _EltexIpSlaStatsIcmpEchoLastLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 3),
    _EltexIpSlaStatsIcmpEchoLastLatency_Type()
)
eltexIpSlaStatsIcmpEchoLastLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoLastLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoLastLatency.setUnits("milliseconds")
_EltexIpSlaStatsIcmpEchoMinLatency_Type = Integer32
_EltexIpSlaStatsIcmpEchoMinLatency_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoMinLatency = _EltexIpSlaStatsIcmpEchoMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 4),
    _EltexIpSlaStatsIcmpEchoMinLatency_Type()
)
eltexIpSlaStatsIcmpEchoMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoMinLatency.setUnits("milliseconds")
_EltexIpSlaStatsIcmpEchoAvgLatency_Type = Integer32
_EltexIpSlaStatsIcmpEchoAvgLatency_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoAvgLatency = _EltexIpSlaStatsIcmpEchoAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 5),
    _EltexIpSlaStatsIcmpEchoAvgLatency_Type()
)
eltexIpSlaStatsIcmpEchoAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoAvgLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoAvgLatency.setUnits("milliseconds")
_EltexIpSlaStatsIcmpEchoMaxLatency_Type = Integer32
_EltexIpSlaStatsIcmpEchoMaxLatency_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoMaxLatency = _EltexIpSlaStatsIcmpEchoMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 6),
    _EltexIpSlaStatsIcmpEchoMaxLatency_Type()
)
eltexIpSlaStatsIcmpEchoMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoMaxLatency.setUnits("milliseconds")
_EltexIpSlaStatsIcmpEchoOperationsCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoOperationsCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoOperationsCtr = _EltexIpSlaStatsIcmpEchoOperationsCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 7),
    _EltexIpSlaStatsIcmpEchoOperationsCtr_Type()
)
eltexIpSlaStatsIcmpEchoOperationsCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoOperationsCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoSuccessesCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoSuccessesCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoSuccessesCtr = _EltexIpSlaStatsIcmpEchoSuccessesCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 8),
    _EltexIpSlaStatsIcmpEchoSuccessesCtr_Type()
)
eltexIpSlaStatsIcmpEchoSuccessesCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoSuccessesCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoFailuresCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoFailuresCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoFailuresCtr = _EltexIpSlaStatsIcmpEchoFailuresCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 9),
    _EltexIpSlaStatsIcmpEchoFailuresCtr_Type()
)
eltexIpSlaStatsIcmpEchoFailuresCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoFailuresCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoTimeoutCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoTimeoutCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoTimeoutCtr = _EltexIpSlaStatsIcmpEchoTimeoutCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 10),
    _EltexIpSlaStatsIcmpEchoTimeoutCtr_Type()
)
eltexIpSlaStatsIcmpEchoTimeoutCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoTimeoutCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoUnreachNetCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachNetCtr = _EltexIpSlaStatsIcmpEchoUnreachNetCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 11),
    _EltexIpSlaStatsIcmpEchoUnreachNetCtr_Type()
)
eltexIpSlaStatsIcmpEchoUnreachNetCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoUnreachNetCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoUnreachHostCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachHostCtr = _EltexIpSlaStatsIcmpEchoUnreachHostCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 12),
    _EltexIpSlaStatsIcmpEchoUnreachHostCtr_Type()
)
eltexIpSlaStatsIcmpEchoUnreachHostCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoUnreachHostCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoUnreachProtCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoUnreachProtCtr = _EltexIpSlaStatsIcmpEchoUnreachProtCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 13),
    _EltexIpSlaStatsIcmpEchoUnreachProtCtr_Type()
)
eltexIpSlaStatsIcmpEchoUnreachProtCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoUnreachProtCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoExTimeTransCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoExTimeTransCtr = _EltexIpSlaStatsIcmpEchoExTimeTransCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 14),
    _EltexIpSlaStatsIcmpEchoExTimeTransCtr_Type()
)
eltexIpSlaStatsIcmpEchoExTimeTransCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoExTimeTransCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoExTimeReassCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoExTimeReassCtr = _EltexIpSlaStatsIcmpEchoExTimeReassCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 15),
    _EltexIpSlaStatsIcmpEchoExTimeReassCtr_Type()
)
eltexIpSlaStatsIcmpEchoExTimeReassCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoExTimeReassCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoUnableSendCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoUnableSendCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoUnableSendCtr = _EltexIpSlaStatsIcmpEchoUnableSendCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 16),
    _EltexIpSlaStatsIcmpEchoUnableSendCtr_Type()
)
eltexIpSlaStatsIcmpEchoUnableSendCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoUnableSendCtr.setStatus("current")
_EltexIpSlaStatsIcmpEchoBadReplyCtr_Type = Counter32
_EltexIpSlaStatsIcmpEchoBadReplyCtr_Object = MibTableColumn
eltexIpSlaStatsIcmpEchoBadReplyCtr = _EltexIpSlaStatsIcmpEchoBadReplyCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 2, 1, 17),
    _EltexIpSlaStatsIcmpEchoBadReplyCtr_Type()
)
eltexIpSlaStatsIcmpEchoBadReplyCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsIcmpEchoBadReplyCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterTable_Object = MibTable
eltexIpSlaStatsUdpJitterTable = _EltexIpSlaStatsUdpJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterTable.setStatus("current")
_EltexIpSlaStatsUdpJitterEntry_Object = MibTableRow
eltexIpSlaStatsUdpJitterEntry = _EltexIpSlaStatsUdpJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1)
)
eltexIpSlaStatsUdpJitterEntry.setIndexNames(
    (0, "ELTEX-IPSLA-MIB", "eltexIpSlaStatsUdpJitterIndex"),
)
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterEntry.setStatus("current")
_EltexIpSlaStatsUdpJitterIndex_Type = Integer32
_EltexIpSlaStatsUdpJitterIndex_Object = MibTableColumn
eltexIpSlaStatsUdpJitterIndex = _EltexIpSlaStatsUdpJitterIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 1),
    _EltexIpSlaStatsUdpJitterIndex_Type()
)
eltexIpSlaStatsUdpJitterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterIndex.setStatus("current")
_EltexIpSlaStatsUdpJitterLastStatus_Type = EltexIpSlaStatsOperStatus
_EltexIpSlaStatsUdpJitterLastStatus_Object = MibTableColumn
eltexIpSlaStatsUdpJitterLastStatus = _EltexIpSlaStatsUdpJitterLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 2),
    _EltexIpSlaStatsUdpJitterLastStatus_Type()
)
eltexIpSlaStatsUdpJitterLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterLastStatus.setStatus("current")
_EltexIpSlaStatsUdpJitterLastLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterLastLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterLastLatency = _EltexIpSlaStatsUdpJitterLastLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 3),
    _EltexIpSlaStatsUdpJitterLastLatency_Type()
)
eltexIpSlaStatsUdpJitterLastLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterLastLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterLastLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterNumLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumLatency = _EltexIpSlaStatsUdpJitterNumLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 4),
    _EltexIpSlaStatsUdpJitterNumLatency_Type()
)
eltexIpSlaStatsUdpJitterNumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterSumLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterSumLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumLatency = _EltexIpSlaStatsUdpJitterSumLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 5),
    _EltexIpSlaStatsUdpJitterSumLatency_Type()
)
eltexIpSlaStatsUdpJitterSumLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMinLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMinLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinLatency = _EltexIpSlaStatsUdpJitterMinLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 6),
    _EltexIpSlaStatsUdpJitterMinLatency_Type()
)
eltexIpSlaStatsUdpJitterMinLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgLatency = _EltexIpSlaStatsUdpJitterAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 7),
    _EltexIpSlaStatsUdpJitterAvgLatency_Type()
)
eltexIpSlaStatsUdpJitterAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxLatency = _EltexIpSlaStatsUdpJitterMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 8),
    _EltexIpSlaStatsUdpJitterMaxLatency_Type()
)
eltexIpSlaStatsUdpJitterMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumSDLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterNumSDLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumSDLatency = _EltexIpSlaStatsUdpJitterNumSDLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 9),
    _EltexIpSlaStatsUdpJitterNumSDLatency_Type()
)
eltexIpSlaStatsUdpJitterNumSDLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumSDLatency.setStatus("current")
_EltexIpSlaStatsUdpJitterSumSDLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterSumSDLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumSDLatency = _EltexIpSlaStatsUdpJitterSumSDLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 10),
    _EltexIpSlaStatsUdpJitterSumSDLatency_Type()
)
eltexIpSlaStatsUdpJitterSumSDLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumSDLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumSDLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMinSDLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMinSDLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinSDLatency = _EltexIpSlaStatsUdpJitterMinSDLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 11),
    _EltexIpSlaStatsUdpJitterMinSDLatency_Type()
)
eltexIpSlaStatsUdpJitterMinSDLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgSDLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgSDLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDLatency = _EltexIpSlaStatsUdpJitterAvgSDLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 12),
    _EltexIpSlaStatsUdpJitterAvgSDLatency_Type()
)
eltexIpSlaStatsUdpJitterAvgSDLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxSDLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxSDLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDLatency = _EltexIpSlaStatsUdpJitterMaxSDLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 13),
    _EltexIpSlaStatsUdpJitterMaxSDLatency_Type()
)
eltexIpSlaStatsUdpJitterMaxSDLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumDSLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterNumDSLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumDSLatency = _EltexIpSlaStatsUdpJitterNumDSLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 14),
    _EltexIpSlaStatsUdpJitterNumDSLatency_Type()
)
eltexIpSlaStatsUdpJitterNumDSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumDSLatency.setStatus("current")
_EltexIpSlaStatsUdpJitterSumDSLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterSumDSLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumDSLatency = _EltexIpSlaStatsUdpJitterSumDSLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 15),
    _EltexIpSlaStatsUdpJitterSumDSLatency_Type()
)
eltexIpSlaStatsUdpJitterSumDSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMinDSLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMinDSLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinDSLatency = _EltexIpSlaStatsUdpJitterMinDSLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 16),
    _EltexIpSlaStatsUdpJitterMinDSLatency_Type()
)
eltexIpSlaStatsUdpJitterMinDSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgDSLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgDSLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSLatency = _EltexIpSlaStatsUdpJitterAvgDSLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 17),
    _EltexIpSlaStatsUdpJitterAvgDSLatency_Type()
)
eltexIpSlaStatsUdpJitterAvgDSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxDSLatency_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxDSLatency_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSLatency = _EltexIpSlaStatsUdpJitterMaxDSLatency_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 18),
    _EltexIpSlaStatsUdpJitterMaxDSLatency_Type()
)
eltexIpSlaStatsUdpJitterMaxDSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSLatency.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSLatency.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumSDPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterNumSDPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumSDPosJitter = _EltexIpSlaStatsUdpJitterNumSDPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 19),
    _EltexIpSlaStatsUdpJitterNumSDPosJitter_Type()
)
eltexIpSlaStatsUdpJitterNumSDPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumSDPosJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterSumSDPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterSumSDPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumSDPosJitter = _EltexIpSlaStatsUdpJitterSumSDPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 20),
    _EltexIpSlaStatsUdpJitterSumSDPosJitter_Type()
)
eltexIpSlaStatsUdpJitterSumSDPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumSDPosJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterMinSDPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMinSDPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinSDPosJitter = _EltexIpSlaStatsUdpJitterMinSDPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 21),
    _EltexIpSlaStatsUdpJitterMinSDPosJitter_Type()
)
eltexIpSlaStatsUdpJitterMinSDPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgSDPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDPosJitter = _EltexIpSlaStatsUdpJitterAvgSDPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 22),
    _EltexIpSlaStatsUdpJitterAvgSDPosJitter_Type()
)
eltexIpSlaStatsUdpJitterAvgSDPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxSDPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDPosJitter = _EltexIpSlaStatsUdpJitterMaxSDPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 23),
    _EltexIpSlaStatsUdpJitterMaxSDPosJitter_Type()
)
eltexIpSlaStatsUdpJitterMaxSDPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumDSPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterNumDSPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumDSPosJitter = _EltexIpSlaStatsUdpJitterNumDSPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 24),
    _EltexIpSlaStatsUdpJitterNumDSPosJitter_Type()
)
eltexIpSlaStatsUdpJitterNumDSPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumDSPosJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterSumDSPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterSumDSPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumDSPosJitter = _EltexIpSlaStatsUdpJitterSumDSPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 25),
    _EltexIpSlaStatsUdpJitterSumDSPosJitter_Type()
)
eltexIpSlaStatsUdpJitterSumDSPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMinDSPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMinDSPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinDSPosJitter = _EltexIpSlaStatsUdpJitterMinDSPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 26),
    _EltexIpSlaStatsUdpJitterMinDSPosJitter_Type()
)
eltexIpSlaStatsUdpJitterMinDSPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgDSPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSPosJitter = _EltexIpSlaStatsUdpJitterAvgDSPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 27),
    _EltexIpSlaStatsUdpJitterAvgDSPosJitter_Type()
)
eltexIpSlaStatsUdpJitterAvgDSPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxDSPosJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSPosJitter = _EltexIpSlaStatsUdpJitterMaxDSPosJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 28),
    _EltexIpSlaStatsUdpJitterMaxDSPosJitter_Type()
)
eltexIpSlaStatsUdpJitterMaxDSPosJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSPosJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSPosJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumSDNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterNumSDNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumSDNegJitter = _EltexIpSlaStatsUdpJitterNumSDNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 29),
    _EltexIpSlaStatsUdpJitterNumSDNegJitter_Type()
)
eltexIpSlaStatsUdpJitterNumSDNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumSDNegJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterSumSDNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterSumSDNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumSDNegJitter = _EltexIpSlaStatsUdpJitterSumSDNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 30),
    _EltexIpSlaStatsUdpJitterSumSDNegJitter_Type()
)
eltexIpSlaStatsUdpJitterSumSDNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumSDNegJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterMinSDNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMinSDNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinSDNegJitter = _EltexIpSlaStatsUdpJitterMinSDNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 31),
    _EltexIpSlaStatsUdpJitterMinSDNegJitter_Type()
)
eltexIpSlaStatsUdpJitterMinSDNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinSDNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgSDNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgSDNegJitter = _EltexIpSlaStatsUdpJitterAvgSDNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 32),
    _EltexIpSlaStatsUdpJitterAvgSDNegJitter_Type()
)
eltexIpSlaStatsUdpJitterAvgSDNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgSDNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxSDNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxSDNegJitter = _EltexIpSlaStatsUdpJitterMaxSDNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 33),
    _EltexIpSlaStatsUdpJitterMaxSDNegJitter_Type()
)
eltexIpSlaStatsUdpJitterMaxSDNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxSDNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterNumDSNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterNumDSNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterNumDSNegJitter = _EltexIpSlaStatsUdpJitterNumDSNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 34),
    _EltexIpSlaStatsUdpJitterNumDSNegJitter_Type()
)
eltexIpSlaStatsUdpJitterNumDSNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterNumDSNegJitter.setStatus("current")
_EltexIpSlaStatsUdpJitterSumDSNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterSumDSNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSumDSNegJitter = _EltexIpSlaStatsUdpJitterSumDSNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 35),
    _EltexIpSlaStatsUdpJitterSumDSNegJitter_Type()
)
eltexIpSlaStatsUdpJitterSumDSNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSumDSNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMinDSNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMinDSNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMinDSNegJitter = _EltexIpSlaStatsUdpJitterMinDSNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 36),
    _EltexIpSlaStatsUdpJitterMinDSNegJitter_Type()
)
eltexIpSlaStatsUdpJitterMinDSNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMinDSNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterAvgDSNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterAvgDSNegJitter = _EltexIpSlaStatsUdpJitterAvgDSNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 37),
    _EltexIpSlaStatsUdpJitterAvgDSNegJitter_Type()
)
eltexIpSlaStatsUdpJitterAvgDSNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterAvgDSNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Type = Integer32
_EltexIpSlaStatsUdpJitterMaxDSNegJitter_Object = MibTableColumn
eltexIpSlaStatsUdpJitterMaxDSNegJitter = _EltexIpSlaStatsUdpJitterMaxDSNegJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 38),
    _EltexIpSlaStatsUdpJitterMaxDSNegJitter_Type()
)
eltexIpSlaStatsUdpJitterMaxDSNegJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSNegJitter.setStatus("current")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterMaxDSNegJitter.setUnits("milliseconds")
_EltexIpSlaStatsUdpJitterOperationsCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterOperationsCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterOperationsCtr = _EltexIpSlaStatsUdpJitterOperationsCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 39),
    _EltexIpSlaStatsUdpJitterOperationsCtr_Type()
)
eltexIpSlaStatsUdpJitterOperationsCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterOperationsCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterSuccessesCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterSuccessesCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterSuccessesCtr = _EltexIpSlaStatsUdpJitterSuccessesCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 40),
    _EltexIpSlaStatsUdpJitterSuccessesCtr_Type()
)
eltexIpSlaStatsUdpJitterSuccessesCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterSuccessesCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterFailuresCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterFailuresCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterFailuresCtr = _EltexIpSlaStatsUdpJitterFailuresCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 41),
    _EltexIpSlaStatsUdpJitterFailuresCtr_Type()
)
eltexIpSlaStatsUdpJitterFailuresCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterFailuresCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterTimeoutCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterTimeoutCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterTimeoutCtr = _EltexIpSlaStatsUdpJitterTimeoutCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 42),
    _EltexIpSlaStatsUdpJitterTimeoutCtr_Type()
)
eltexIpSlaStatsUdpJitterTimeoutCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterTimeoutCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterUnreachNetCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterUnreachNetCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterUnreachNetCtr = _EltexIpSlaStatsUdpJitterUnreachNetCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 43),
    _EltexIpSlaStatsUdpJitterUnreachNetCtr_Type()
)
eltexIpSlaStatsUdpJitterUnreachNetCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterUnreachNetCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterUnreachHostCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterUnreachHostCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterUnreachHostCtr = _EltexIpSlaStatsUdpJitterUnreachHostCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 44),
    _EltexIpSlaStatsUdpJitterUnreachHostCtr_Type()
)
eltexIpSlaStatsUdpJitterUnreachHostCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterUnreachHostCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterUnreachPortCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterUnreachPortCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterUnreachPortCtr = _EltexIpSlaStatsUdpJitterUnreachPortCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 45),
    _EltexIpSlaStatsUdpJitterUnreachPortCtr_Type()
)
eltexIpSlaStatsUdpJitterUnreachPortCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterUnreachPortCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterUnreachProtCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterUnreachProtCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterUnreachProtCtr = _EltexIpSlaStatsUdpJitterUnreachProtCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 46),
    _EltexIpSlaStatsUdpJitterUnreachProtCtr_Type()
)
eltexIpSlaStatsUdpJitterUnreachProtCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterUnreachProtCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterExTimeTransCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterExTimeTransCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterExTimeTransCtr = _EltexIpSlaStatsUdpJitterExTimeTransCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 47),
    _EltexIpSlaStatsUdpJitterExTimeTransCtr_Type()
)
eltexIpSlaStatsUdpJitterExTimeTransCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterExTimeTransCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterExTimeReassCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterExTimeReassCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterExTimeReassCtr = _EltexIpSlaStatsUdpJitterExTimeReassCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 48),
    _EltexIpSlaStatsUdpJitterExTimeReassCtr_Type()
)
eltexIpSlaStatsUdpJitterExTimeReassCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterExTimeReassCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterUnableSendCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterUnableSendCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterUnableSendCtr = _EltexIpSlaStatsUdpJitterUnableSendCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 49),
    _EltexIpSlaStatsUdpJitterUnableSendCtr_Type()
)
eltexIpSlaStatsUdpJitterUnableSendCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterUnableSendCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterBadReplyCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterBadReplyCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterBadReplyCtr = _EltexIpSlaStatsUdpJitterBadReplyCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 50),
    _EltexIpSlaStatsUdpJitterBadReplyCtr_Type()
)
eltexIpSlaStatsUdpJitterBadReplyCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterBadReplyCtr.setStatus("current")
_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Type = Counter32
_EltexIpSlaStatsUdpJitterPacketsOOSCtr_Object = MibTableColumn
eltexIpSlaStatsUdpJitterPacketsOOSCtr = _EltexIpSlaStatsUdpJitterPacketsOOSCtr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 3, 3, 1, 51),
    _EltexIpSlaStatsUdpJitterPacketsOOSCtr_Type()
)
eltexIpSlaStatsUdpJitterPacketsOOSCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexIpSlaStatsUdpJitterPacketsOOSCtr.setStatus("current")
_EltexIpSlaSchedule_ObjectIdentity = ObjectIdentity
eltexIpSlaSchedule = _EltexIpSlaSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 4)
)
_EltexIpSlaScheduleStartTrigger_Type = Integer32
_EltexIpSlaScheduleStartTrigger_Object = MibScalar
eltexIpSlaScheduleStartTrigger = _EltexIpSlaScheduleStartTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 4, 1),
    _EltexIpSlaScheduleStartTrigger_Type()
)
eltexIpSlaScheduleStartTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaScheduleStartTrigger.setStatus("current")
_EltexIpSlaScheduleStopTrigger_Type = Integer32
_EltexIpSlaScheduleStopTrigger_Object = MibScalar
eltexIpSlaScheduleStopTrigger = _EltexIpSlaScheduleStopTrigger_Object(
    (1, 3, 6, 1, 4, 1, 35265, 32, 1, 4, 2),
    _EltexIpSlaScheduleStopTrigger_Type()
)
eltexIpSlaScheduleStopTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexIpSlaScheduleStopTrigger.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-IPSLA-MIB",
    **{"EltexIpSlaOperationType": EltexIpSlaOperationType,
       "EltexIpSlaOperationStatus": EltexIpSlaOperationStatus,
       "EltexIpSlaStatsOperStatus": EltexIpSlaStatsOperStatus,
       "eltexIpSlaMIB": eltexIpSlaMIB,
       "eltexIpSlaObjects": eltexIpSlaObjects,
       "eltexIpSlaAppl": eltexIpSlaAppl,
       "eltexIpSlaApplResponder": eltexIpSlaApplResponder,
       "eltexIpSlaApplResponderUdpJitterPort": eltexIpSlaApplResponderUdpJitterPort,
       "eltexIpSlaAdmin": eltexIpSlaAdmin,
       "eltexIpSlaAdminCtrlTable": eltexIpSlaAdminCtrlTable,
       "eltexIpSlaAdminCtrlEntry": eltexIpSlaAdminCtrlEntry,
       "eltexIpSlaAdminCtrlIndex": eltexIpSlaAdminCtrlIndex,
       "eltexIpSlaAdminCtrlType": eltexIpSlaAdminCtrlType,
       "eltexIpSlaAdminCtrlStatus": eltexIpSlaAdminCtrlStatus,
       "eltexIpSlaAdminCtrlFrequency": eltexIpSlaAdminCtrlFrequency,
       "eltexIpSlaAdminCtrlTag": eltexIpSlaAdminCtrlTag,
       "eltexIpSlaAdminCtrlOwner": eltexIpSlaAdminCtrlOwner,
       "eltexIpSlaAdminCtrlRowStatus": eltexIpSlaAdminCtrlRowStatus,
       "eltexIpSlaAdminIcmpEchoTable": eltexIpSlaAdminIcmpEchoTable,
       "eltexIpSlaAdminIcmpEchoEntry": eltexIpSlaAdminIcmpEchoEntry,
       "eltexIpSlaAdminIcmpEchoIndex": eltexIpSlaAdminIcmpEchoIndex,
       "eltexIpSlaAdminIcmpEchoTargetAddress": eltexIpSlaAdminIcmpEchoTargetAddress,
       "eltexIpSlaAdminIcmpEchoSourceAddress": eltexIpSlaAdminIcmpEchoSourceAddress,
       "eltexIpSlaAdminIcmpEchoSourceInterface": eltexIpSlaAdminIcmpEchoSourceInterface,
       "eltexIpSlaAdminIcmpEchoTimeOut": eltexIpSlaAdminIcmpEchoTimeOut,
       "eltexIpSlaAdminIcmpEchoReqDataSize": eltexIpSlaAdminIcmpEchoReqDataSize,
       "eltexIpSlaAdminIcmpEchoTOS": eltexIpSlaAdminIcmpEchoTOS,
       "eltexIpSlaAdminIcmpEchoRowStatus": eltexIpSlaAdminIcmpEchoRowStatus,
       "eltexIpSlaAdminUdpJitterTable": eltexIpSlaAdminUdpJitterTable,
       "eltexIpSlaAdminUdpJitterEntry": eltexIpSlaAdminUdpJitterEntry,
       "eltexIpSlaAdminUdpJitterIndex": eltexIpSlaAdminUdpJitterIndex,
       "eltexIpSlaAdminUdpJitterTargetAddress": eltexIpSlaAdminUdpJitterTargetAddress,
       "eltexIpSlaAdminUdpJitterTargetPort": eltexIpSlaAdminUdpJitterTargetPort,
       "eltexIpSlaAdminUdpJitterSourceAddress": eltexIpSlaAdminUdpJitterSourceAddress,
       "eltexIpSlaAdminUdpJitterSourcePort": eltexIpSlaAdminUdpJitterSourcePort,
       "eltexIpSlaAdminUdpJitterSourceInterface": eltexIpSlaAdminUdpJitterSourceInterface,
       "eltexIpSlaAdminUdpJitterInterval": eltexIpSlaAdminUdpJitterInterval,
       "eltexIpSlaAdminUdpJitterNumPackets": eltexIpSlaAdminUdpJitterNumPackets,
       "eltexIpSlaAdminUdpJitterTimeOut": eltexIpSlaAdminUdpJitterTimeOut,
       "eltexIpSlaAdminUdpJitterReqDataSize": eltexIpSlaAdminUdpJitterReqDataSize,
       "eltexIpSlaAdminUdpJitterTOS": eltexIpSlaAdminUdpJitterTOS,
       "eltexIpSlaAdminUdpJitterRowStatus": eltexIpSlaAdminUdpJitterRowStatus,
       "eltexIpSlaStats": eltexIpSlaStats,
       "eltexIpSlaStatsIcmpEchoTable": eltexIpSlaStatsIcmpEchoTable,
       "eltexIpSlaStatsIcmpEchoEntry": eltexIpSlaStatsIcmpEchoEntry,
       "eltexIpSlaStatsIcmpEchoIndex": eltexIpSlaStatsIcmpEchoIndex,
       "eltexIpSlaStatsIcmpEchoLastStatus": eltexIpSlaStatsIcmpEchoLastStatus,
       "eltexIpSlaStatsIcmpEchoLastLatency": eltexIpSlaStatsIcmpEchoLastLatency,
       "eltexIpSlaStatsIcmpEchoMinLatency": eltexIpSlaStatsIcmpEchoMinLatency,
       "eltexIpSlaStatsIcmpEchoAvgLatency": eltexIpSlaStatsIcmpEchoAvgLatency,
       "eltexIpSlaStatsIcmpEchoMaxLatency": eltexIpSlaStatsIcmpEchoMaxLatency,
       "eltexIpSlaStatsIcmpEchoOperationsCtr": eltexIpSlaStatsIcmpEchoOperationsCtr,
       "eltexIpSlaStatsIcmpEchoSuccessesCtr": eltexIpSlaStatsIcmpEchoSuccessesCtr,
       "eltexIpSlaStatsIcmpEchoFailuresCtr": eltexIpSlaStatsIcmpEchoFailuresCtr,
       "eltexIpSlaStatsIcmpEchoTimeoutCtr": eltexIpSlaStatsIcmpEchoTimeoutCtr,
       "eltexIpSlaStatsIcmpEchoUnreachNetCtr": eltexIpSlaStatsIcmpEchoUnreachNetCtr,
       "eltexIpSlaStatsIcmpEchoUnreachHostCtr": eltexIpSlaStatsIcmpEchoUnreachHostCtr,
       "eltexIpSlaStatsIcmpEchoUnreachProtCtr": eltexIpSlaStatsIcmpEchoUnreachProtCtr,
       "eltexIpSlaStatsIcmpEchoExTimeTransCtr": eltexIpSlaStatsIcmpEchoExTimeTransCtr,
       "eltexIpSlaStatsIcmpEchoExTimeReassCtr": eltexIpSlaStatsIcmpEchoExTimeReassCtr,
       "eltexIpSlaStatsIcmpEchoUnableSendCtr": eltexIpSlaStatsIcmpEchoUnableSendCtr,
       "eltexIpSlaStatsIcmpEchoBadReplyCtr": eltexIpSlaStatsIcmpEchoBadReplyCtr,
       "eltexIpSlaStatsUdpJitterTable": eltexIpSlaStatsUdpJitterTable,
       "eltexIpSlaStatsUdpJitterEntry": eltexIpSlaStatsUdpJitterEntry,
       "eltexIpSlaStatsUdpJitterIndex": eltexIpSlaStatsUdpJitterIndex,
       "eltexIpSlaStatsUdpJitterLastStatus": eltexIpSlaStatsUdpJitterLastStatus,
       "eltexIpSlaStatsUdpJitterLastLatency": eltexIpSlaStatsUdpJitterLastLatency,
       "eltexIpSlaStatsUdpJitterNumLatency": eltexIpSlaStatsUdpJitterNumLatency,
       "eltexIpSlaStatsUdpJitterSumLatency": eltexIpSlaStatsUdpJitterSumLatency,
       "eltexIpSlaStatsUdpJitterMinLatency": eltexIpSlaStatsUdpJitterMinLatency,
       "eltexIpSlaStatsUdpJitterAvgLatency": eltexIpSlaStatsUdpJitterAvgLatency,
       "eltexIpSlaStatsUdpJitterMaxLatency": eltexIpSlaStatsUdpJitterMaxLatency,
       "eltexIpSlaStatsUdpJitterNumSDLatency": eltexIpSlaStatsUdpJitterNumSDLatency,
       "eltexIpSlaStatsUdpJitterSumSDLatency": eltexIpSlaStatsUdpJitterSumSDLatency,
       "eltexIpSlaStatsUdpJitterMinSDLatency": eltexIpSlaStatsUdpJitterMinSDLatency,
       "eltexIpSlaStatsUdpJitterAvgSDLatency": eltexIpSlaStatsUdpJitterAvgSDLatency,
       "eltexIpSlaStatsUdpJitterMaxSDLatency": eltexIpSlaStatsUdpJitterMaxSDLatency,
       "eltexIpSlaStatsUdpJitterNumDSLatency": eltexIpSlaStatsUdpJitterNumDSLatency,
       "eltexIpSlaStatsUdpJitterSumDSLatency": eltexIpSlaStatsUdpJitterSumDSLatency,
       "eltexIpSlaStatsUdpJitterMinDSLatency": eltexIpSlaStatsUdpJitterMinDSLatency,
       "eltexIpSlaStatsUdpJitterAvgDSLatency": eltexIpSlaStatsUdpJitterAvgDSLatency,
       "eltexIpSlaStatsUdpJitterMaxDSLatency": eltexIpSlaStatsUdpJitterMaxDSLatency,
       "eltexIpSlaStatsUdpJitterNumSDPosJitter": eltexIpSlaStatsUdpJitterNumSDPosJitter,
       "eltexIpSlaStatsUdpJitterSumSDPosJitter": eltexIpSlaStatsUdpJitterSumSDPosJitter,
       "eltexIpSlaStatsUdpJitterMinSDPosJitter": eltexIpSlaStatsUdpJitterMinSDPosJitter,
       "eltexIpSlaStatsUdpJitterAvgSDPosJitter": eltexIpSlaStatsUdpJitterAvgSDPosJitter,
       "eltexIpSlaStatsUdpJitterMaxSDPosJitter": eltexIpSlaStatsUdpJitterMaxSDPosJitter,
       "eltexIpSlaStatsUdpJitterNumDSPosJitter": eltexIpSlaStatsUdpJitterNumDSPosJitter,
       "eltexIpSlaStatsUdpJitterSumDSPosJitter": eltexIpSlaStatsUdpJitterSumDSPosJitter,
       "eltexIpSlaStatsUdpJitterMinDSPosJitter": eltexIpSlaStatsUdpJitterMinDSPosJitter,
       "eltexIpSlaStatsUdpJitterAvgDSPosJitter": eltexIpSlaStatsUdpJitterAvgDSPosJitter,
       "eltexIpSlaStatsUdpJitterMaxDSPosJitter": eltexIpSlaStatsUdpJitterMaxDSPosJitter,
       "eltexIpSlaStatsUdpJitterNumSDNegJitter": eltexIpSlaStatsUdpJitterNumSDNegJitter,
       "eltexIpSlaStatsUdpJitterSumSDNegJitter": eltexIpSlaStatsUdpJitterSumSDNegJitter,
       "eltexIpSlaStatsUdpJitterMinSDNegJitter": eltexIpSlaStatsUdpJitterMinSDNegJitter,
       "eltexIpSlaStatsUdpJitterAvgSDNegJitter": eltexIpSlaStatsUdpJitterAvgSDNegJitter,
       "eltexIpSlaStatsUdpJitterMaxSDNegJitter": eltexIpSlaStatsUdpJitterMaxSDNegJitter,
       "eltexIpSlaStatsUdpJitterNumDSNegJitter": eltexIpSlaStatsUdpJitterNumDSNegJitter,
       "eltexIpSlaStatsUdpJitterSumDSNegJitter": eltexIpSlaStatsUdpJitterSumDSNegJitter,
       "eltexIpSlaStatsUdpJitterMinDSNegJitter": eltexIpSlaStatsUdpJitterMinDSNegJitter,
       "eltexIpSlaStatsUdpJitterAvgDSNegJitter": eltexIpSlaStatsUdpJitterAvgDSNegJitter,
       "eltexIpSlaStatsUdpJitterMaxDSNegJitter": eltexIpSlaStatsUdpJitterMaxDSNegJitter,
       "eltexIpSlaStatsUdpJitterOperationsCtr": eltexIpSlaStatsUdpJitterOperationsCtr,
       "eltexIpSlaStatsUdpJitterSuccessesCtr": eltexIpSlaStatsUdpJitterSuccessesCtr,
       "eltexIpSlaStatsUdpJitterFailuresCtr": eltexIpSlaStatsUdpJitterFailuresCtr,
       "eltexIpSlaStatsUdpJitterTimeoutCtr": eltexIpSlaStatsUdpJitterTimeoutCtr,
       "eltexIpSlaStatsUdpJitterUnreachNetCtr": eltexIpSlaStatsUdpJitterUnreachNetCtr,
       "eltexIpSlaStatsUdpJitterUnreachHostCtr": eltexIpSlaStatsUdpJitterUnreachHostCtr,
       "eltexIpSlaStatsUdpJitterUnreachPortCtr": eltexIpSlaStatsUdpJitterUnreachPortCtr,
       "eltexIpSlaStatsUdpJitterUnreachProtCtr": eltexIpSlaStatsUdpJitterUnreachProtCtr,
       "eltexIpSlaStatsUdpJitterExTimeTransCtr": eltexIpSlaStatsUdpJitterExTimeTransCtr,
       "eltexIpSlaStatsUdpJitterExTimeReassCtr": eltexIpSlaStatsUdpJitterExTimeReassCtr,
       "eltexIpSlaStatsUdpJitterUnableSendCtr": eltexIpSlaStatsUdpJitterUnableSendCtr,
       "eltexIpSlaStatsUdpJitterBadReplyCtr": eltexIpSlaStatsUdpJitterBadReplyCtr,
       "eltexIpSlaStatsUdpJitterPacketsOOSCtr": eltexIpSlaStatsUdpJitterPacketsOOSCtr,
       "eltexIpSlaSchedule": eltexIpSlaSchedule,
       "eltexIpSlaScheduleStartTrigger": eltexIpSlaScheduleStartTrigger,
       "eltexIpSlaScheduleStopTrigger": eltexIpSlaScheduleStopTrigger}
)
