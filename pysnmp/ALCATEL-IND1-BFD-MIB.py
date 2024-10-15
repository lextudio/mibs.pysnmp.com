# SNMP MIB module (ALCATEL-IND1-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:43 2024
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

(softentIND1BFD,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1BFD")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1BfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1)
)
alcatelIND1BfdMIB.setRevisions(
        ("2010-05-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaBfdInterval(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class AlaBfdDiag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("administrativelyDown", 7),
          ("concatenatedPathDown", 6),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("forwardingPlaneReset", 4),
          ("neighborSignaledSessionDown", 3),
          ("noDiagnostic", 0),
          ("pathDown", 5),
          ("reverseConcatenatedPathDown", 8))
    )



class AlaBfdStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_AlaBfdObjects_ObjectIdentity = ObjectIdentity
alaBfdObjects = _AlaBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1)
)
if mibBuilder.loadTexts:
    alaBfdObjects.setStatus("current")
_AlaBfdGlobalObjects_ObjectIdentity = ObjectIdentity
alaBfdGlobalObjects = _AlaBfdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1)
)


class _AlaBfdGlobalVersionNumber_Type(Unsigned32):
    """Custom type alaBfdGlobalVersionNumber based on Unsigned32"""
    defaultValue = 1


_AlaBfdGlobalVersionNumber_Object = MibScalar
alaBfdGlobalVersionNumber = _AlaBfdGlobalVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 1),
    _AlaBfdGlobalVersionNumber_Type()
)
alaBfdGlobalVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdGlobalVersionNumber.setStatus("current")


class _AlaBfdGlobalAdminStatus_Type(AlaBfdStatus):
    """Custom type alaBfdGlobalAdminStatus based on AlaBfdStatus"""


_AlaBfdGlobalAdminStatus_Object = MibScalar
alaBfdGlobalAdminStatus = _AlaBfdGlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 2),
    _AlaBfdGlobalAdminStatus_Type()
)
alaBfdGlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalAdminStatus.setStatus("current")


class _AlaBfdGlobalTxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalTxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalTxInterval_Object = MibScalar
alaBfdGlobalTxInterval = _AlaBfdGlobalTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 3),
    _AlaBfdGlobalTxInterval_Type()
)
alaBfdGlobalTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalTxInterval.setStatus("current")


class _AlaBfdGlobalRxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalRxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalRxInterval_Object = MibScalar
alaBfdGlobalRxInterval = _AlaBfdGlobalRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 4),
    _AlaBfdGlobalRxInterval_Type()
)
alaBfdGlobalRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalRxInterval.setStatus("current")


class _AlaBfdGlobalDetectMult_Type(Integer32):
    """Custom type alaBfdGlobalDetectMult based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_AlaBfdGlobalDetectMult_Type.__name__ = "Integer32"
_AlaBfdGlobalDetectMult_Object = MibScalar
alaBfdGlobalDetectMult = _AlaBfdGlobalDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 5),
    _AlaBfdGlobalDetectMult_Type()
)
alaBfdGlobalDetectMult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalDetectMult.setStatus("current")


class _AlaBfdGlobalEchoRxInterval_Type(AlaBfdInterval):
    """Custom type alaBfdGlobalEchoRxInterval based on AlaBfdInterval"""
    defaultValue = 300


_AlaBfdGlobalEchoRxInterval_Object = MibScalar
alaBfdGlobalEchoRxInterval = _AlaBfdGlobalEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 6),
    _AlaBfdGlobalEchoRxInterval_Type()
)
alaBfdGlobalEchoRxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaBfdGlobalEchoRxInterval.setStatus("current")


class _AlaBfdGlobalProtocolApps_Type(Bits):
    """Custom type alaBfdGlobalProtocolApps based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("dvmrp", 6),
          ("isis", 4),
          ("ospf", 2),
          ("pim", 5),
          ("staticRtg", 1),
          ("vrrp", 0))
    )

_AlaBfdGlobalProtocolApps_Type.__name__ = "Bits"
_AlaBfdGlobalProtocolApps_Object = MibScalar
alaBfdGlobalProtocolApps = _AlaBfdGlobalProtocolApps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 1, 7),
    _AlaBfdGlobalProtocolApps_Type()
)
alaBfdGlobalProtocolApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdGlobalProtocolApps.setStatus("current")
_AlaBfdIntfTable_Object = MibTable
alaBfdIntfTable = _AlaBfdIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaBfdIntfTable.setStatus("current")
_AlaBfdIntfEntry_Object = MibTableRow
alaBfdIntfEntry = _AlaBfdIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1)
)
alaBfdIntfEntry.setIndexNames(
    (0, "ALCATEL-IND1-BFD-MIB", "alaBfdIntfIndex"),
)
if mibBuilder.loadTexts:
    alaBfdIntfEntry.setStatus("current")
_AlaBfdIntfIndex_Type = InterfaceIndex
_AlaBfdIntfIndex_Object = MibTableColumn
alaBfdIntfIndex = _AlaBfdIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 1),
    _AlaBfdIntfIndex_Type()
)
alaBfdIntfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBfdIntfIndex.setStatus("current")
_AlaBfdIntfAddrType_Type = InetAddressType
_AlaBfdIntfAddrType_Object = MibTableColumn
alaBfdIntfAddrType = _AlaBfdIntfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 2),
    _AlaBfdIntfAddrType_Type()
)
alaBfdIntfAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAddrType.setStatus("current")
_AlaBfdIntfAddr_Type = InetAddress
_AlaBfdIntfAddr_Object = MibTableColumn
alaBfdIntfAddr = _AlaBfdIntfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 3),
    _AlaBfdIntfAddr_Type()
)
alaBfdIntfAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAddr.setStatus("current")


class _AlaBfdIntfAdminStatus_Type(AlaBfdStatus):
    """Custom type alaBfdIntfAdminStatus based on AlaBfdStatus"""


_AlaBfdIntfAdminStatus_Object = MibTableColumn
alaBfdIntfAdminStatus = _AlaBfdIntfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 4),
    _AlaBfdIntfAdminStatus_Type()
)
alaBfdIntfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAdminStatus.setStatus("current")
_AlaBfdIntfDesiredMinTxInterval_Type = AlaBfdInterval
_AlaBfdIntfDesiredMinTxInterval_Object = MibTableColumn
alaBfdIntfDesiredMinTxInterval = _AlaBfdIntfDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 5),
    _AlaBfdIntfDesiredMinTxInterval_Type()
)
alaBfdIntfDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfDesiredMinTxInterval.setStatus("current")
_AlaBfdIntfReqMinRxInterval_Type = AlaBfdInterval
_AlaBfdIntfReqMinRxInterval_Object = MibTableColumn
alaBfdIntfReqMinRxInterval = _AlaBfdIntfReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 6),
    _AlaBfdIntfReqMinRxInterval_Type()
)
alaBfdIntfReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfReqMinRxInterval.setStatus("current")
_AlaBfdIntfReqMinEchoRxInterval_Type = AlaBfdInterval
_AlaBfdIntfReqMinEchoRxInterval_Object = MibTableColumn
alaBfdIntfReqMinEchoRxInterval = _AlaBfdIntfReqMinEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 7),
    _AlaBfdIntfReqMinEchoRxInterval_Type()
)
alaBfdIntfReqMinEchoRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfReqMinEchoRxInterval.setStatus("current")


class _AlaBfdIntfDetectMult_Type(Integer32):
    """Custom type alaBfdIntfDetectMult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_AlaBfdIntfDetectMult_Type.__name__ = "Integer32"
_AlaBfdIntfDetectMult_Object = MibTableColumn
alaBfdIntfDetectMult = _AlaBfdIntfDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 8),
    _AlaBfdIntfDetectMult_Type()
)
alaBfdIntfDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfDetectMult.setStatus("current")


class _AlaBfdIntfAuthPresFlag_Type(TruthValue):
    """Custom type alaBfdIntfAuthPresFlag based on TruthValue"""


_AlaBfdIntfAuthPresFlag_Object = MibTableColumn
alaBfdIntfAuthPresFlag = _AlaBfdIntfAuthPresFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 9),
    _AlaBfdIntfAuthPresFlag_Type()
)
alaBfdIntfAuthPresFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAuthPresFlag.setStatus("current")


class _AlaBfdIntfAuthenticationType_Type(Integer32):
    """Custom type alaBfdIntfAuthenticationType based on Integer32"""
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
        *(("keyedMD5", 3),
          ("keyedSHA1", 5),
          ("meticulousKeyedMD5", 4),
          ("meticulousKeyedSHA1", 6),
          ("none", 1),
          ("simplePassword", 2))
    )


_AlaBfdIntfAuthenticationType_Type.__name__ = "Integer32"
_AlaBfdIntfAuthenticationType_Object = MibTableColumn
alaBfdIntfAuthenticationType = _AlaBfdIntfAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 10),
    _AlaBfdIntfAuthenticationType_Type()
)
alaBfdIntfAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfAuthenticationType.setStatus("current")
_AlaBfdIntfIfName_Type = SnmpAdminString
_AlaBfdIntfIfName_Object = MibTableColumn
alaBfdIntfIfName = _AlaBfdIntfIfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 11),
    _AlaBfdIntfIfName_Type()
)
alaBfdIntfIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfIfName.setStatus("current")


class _AlaBfdIntfOperStatus_Type(Integer32):
    """Custom type alaBfdIntfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaBfdIntfOperStatus_Type.__name__ = "Integer32"
_AlaBfdIntfOperStatus_Object = MibTableColumn
alaBfdIntfOperStatus = _AlaBfdIntfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 12),
    _AlaBfdIntfOperStatus_Type()
)
alaBfdIntfOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfOperStatus.setStatus("current")
_AlaBfdIntfRowStatus_Type = RowStatus
_AlaBfdIntfRowStatus_Object = MibTableColumn
alaBfdIntfRowStatus = _AlaBfdIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 2, 1, 13),
    _AlaBfdIntfRowStatus_Type()
)
alaBfdIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaBfdIntfRowStatus.setStatus("current")
_AlaBfdSessTable_Object = MibTable
alaBfdSessTable = _AlaBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaBfdSessTable.setStatus("current")
_AlaBfdSessEntry_Object = MibTableRow
alaBfdSessEntry = _AlaBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1)
)
alaBfdSessEntry.setIndexNames(
    (0, "ALCATEL-IND1-BFD-MIB", "alaBfdSessDiscriminator"),
)
if mibBuilder.loadTexts:
    alaBfdSessEntry.setStatus("current")


class _AlaBfdSessDiscriminator_Type(Unsigned32):
    """Custom type alaBfdSessDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AlaBfdSessDiscriminator_Type.__name__ = "Unsigned32"
_AlaBfdSessDiscriminator_Object = MibTableColumn
alaBfdSessDiscriminator = _AlaBfdSessDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 1),
    _AlaBfdSessDiscriminator_Type()
)
alaBfdSessDiscriminator.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaBfdSessDiscriminator.setStatus("current")
_AlaBfdSessNeighborAddrType_Type = InetAddressType
_AlaBfdSessNeighborAddrType_Object = MibTableColumn
alaBfdSessNeighborAddrType = _AlaBfdSessNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 2),
    _AlaBfdSessNeighborAddrType_Type()
)
alaBfdSessNeighborAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNeighborAddrType.setStatus("current")
_AlaBfdSessNeighborAddr_Type = InetAddress
_AlaBfdSessNeighborAddr_Object = MibTableColumn
alaBfdSessNeighborAddr = _AlaBfdSessNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 3),
    _AlaBfdSessNeighborAddr_Type()
)
alaBfdSessNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNeighborAddr.setStatus("current")


class _AlaBfdSessSessionType_Type(Bits):
    """Custom type alaBfdSessSessionType based on Bits"""
    namedValues = NamedValues(
        *(("asynchronous", 0),
          ("demand", 2),
          ("echo", 1))
    )

_AlaBfdSessSessionType_Type.__name__ = "Bits"
_AlaBfdSessSessionType_Object = MibTableColumn
alaBfdSessSessionType = _AlaBfdSessSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 4),
    _AlaBfdSessSessionType_Type()
)
alaBfdSessSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessSessionType.setStatus("current")


class _AlaBfdSessRemoteDiscr_Type(Unsigned32):
    """Custom type alaBfdSessRemoteDiscr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlaBfdSessRemoteDiscr_Type.__name__ = "Unsigned32"
_AlaBfdSessRemoteDiscr_Object = MibTableColumn
alaBfdSessRemoteDiscr = _AlaBfdSessRemoteDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 5),
    _AlaBfdSessRemoteDiscr_Type()
)
alaBfdSessRemoteDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessRemoteDiscr.setStatus("current")
_AlaBfdSessUdpPort_Type = InetPortNumber
_AlaBfdSessUdpPort_Object = MibTableColumn
alaBfdSessUdpPort = _AlaBfdSessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 6),
    _AlaBfdSessUdpPort_Type()
)
alaBfdSessUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessUdpPort.setStatus("current")


class _AlaBfdSessState_Type(Integer32):
    """Custom type alaBfdSessState based on Integer32"""
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
        *(("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4))
    )


_AlaBfdSessState_Type.__name__ = "Integer32"
_AlaBfdSessState_Object = MibTableColumn
alaBfdSessState = _AlaBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 7),
    _AlaBfdSessState_Type()
)
alaBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessState.setStatus("current")
_AlaBfdSessDiag_Type = AlaBfdDiag
_AlaBfdSessDiag_Object = MibTableColumn
alaBfdSessDiag = _AlaBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 8),
    _AlaBfdSessDiag_Type()
)
alaBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessDiag.setStatus("current")


class _AlaBfdSessOperMode_Type(Integer32):
    """Custom type alaBfdSessOperMode based on Integer32"""
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
        *(("asyncModeWEchoFunction", 1),
          ("asynchModeWOEchoFunction", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4),
          ("echoOnly", 5))
    )


_AlaBfdSessOperMode_Type.__name__ = "Integer32"
_AlaBfdSessOperMode_Object = MibTableColumn
alaBfdSessOperMode = _AlaBfdSessOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 10),
    _AlaBfdSessOperMode_Type()
)
alaBfdSessOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessOperMode.setStatus("current")
_AlaBfdSessControlPlanIndepFlag_Type = TruthValue
_AlaBfdSessControlPlanIndepFlag_Object = MibTableColumn
alaBfdSessControlPlanIndepFlag = _AlaBfdSessControlPlanIndepFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 11),
    _AlaBfdSessControlPlanIndepFlag_Type()
)
alaBfdSessControlPlanIndepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessControlPlanIndepFlag.setStatus("current")
_AlaBfdSessIfIndex_Type = InterfaceIndexOrZero
_AlaBfdSessIfIndex_Object = MibTableColumn
alaBfdSessIfIndex = _AlaBfdSessIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 12),
    _AlaBfdSessIfIndex_Type()
)
alaBfdSessIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessIfIndex.setStatus("current")
_AlaBfdSessNegotiatedTxInterval_Type = AlaBfdInterval
_AlaBfdSessNegotiatedTxInterval_Object = MibTableColumn
alaBfdSessNegotiatedTxInterval = _AlaBfdSessNegotiatedTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 13),
    _AlaBfdSessNegotiatedTxInterval_Type()
)
alaBfdSessNegotiatedTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNegotiatedTxInterval.setStatus("current")
_AlaBfdSessNegotiatedRxInterval_Type = AlaBfdInterval
_AlaBfdSessNegotiatedRxInterval_Object = MibTableColumn
alaBfdSessNegotiatedRxInterval = _AlaBfdSessNegotiatedRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 14),
    _AlaBfdSessNegotiatedRxInterval_Type()
)
alaBfdSessNegotiatedRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessNegotiatedRxInterval.setStatus("current")
_AlaBfdSessEchoRxInterval_Type = AlaBfdInterval
_AlaBfdSessEchoRxInterval_Object = MibTableColumn
alaBfdSessEchoRxInterval = _AlaBfdSessEchoRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 15),
    _AlaBfdSessEchoRxInterval_Type()
)
alaBfdSessEchoRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessEchoRxInterval.setStatus("current")


class _AlaBfdSessProtocolApps_Type(Bits):
    """Custom type alaBfdSessProtocolApps based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("dvmrp", 6),
          ("isis", 4),
          ("ospf", 2),
          ("pim", 5),
          ("staticRtg", 1),
          ("vrrp", 0))
    )

_AlaBfdSessProtocolApps_Type.__name__ = "Bits"
_AlaBfdSessProtocolApps_Object = MibTableColumn
alaBfdSessProtocolApps = _AlaBfdSessProtocolApps_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 3, 1, 16),
    _AlaBfdSessProtocolApps_Type()
)
alaBfdSessProtocolApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessProtocolApps.setStatus("current")
_AlaBfdSessPerfTable_Object = MibTable
alaBfdSessPerfTable = _AlaBfdSessPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaBfdSessPerfTable.setStatus("current")
_AlaBfdSessPerfEntry_Object = MibTableRow
alaBfdSessPerfEntry = _AlaBfdSessPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaBfdSessPerfEntry.setStatus("current")
_AlaBfdSessPerfPktIn_Type = Counter64
_AlaBfdSessPerfPktIn_Object = MibTableColumn
alaBfdSessPerfPktIn = _AlaBfdSessPerfPktIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 1),
    _AlaBfdSessPerfPktIn_Type()
)
alaBfdSessPerfPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfPktIn.setStatus("current")
_AlaBfdSessPerfPktOut_Type = Counter64
_AlaBfdSessPerfPktOut_Object = MibTableColumn
alaBfdSessPerfPktOut = _AlaBfdSessPerfPktOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 2),
    _AlaBfdSessPerfPktOut_Type()
)
alaBfdSessPerfPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfPktOut.setStatus("current")
_AlaBfdSessPerfEchoOut_Type = Counter64
_AlaBfdSessPerfEchoOut_Object = MibTableColumn
alaBfdSessPerfEchoOut = _AlaBfdSessPerfEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 3),
    _AlaBfdSessPerfEchoOut_Type()
)
alaBfdSessPerfEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfEchoOut.setStatus("current")
_AlaBfdSessPerfEchoIn_Type = Counter64
_AlaBfdSessPerfEchoIn_Object = MibTableColumn
alaBfdSessPerfEchoIn = _AlaBfdSessPerfEchoIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 4),
    _AlaBfdSessPerfEchoIn_Type()
)
alaBfdSessPerfEchoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfEchoIn.setStatus("current")
_AlaBfdSessPerfUpTime_Type = TimeTicks
_AlaBfdSessPerfUpTime_Object = MibTableColumn
alaBfdSessPerfUpTime = _AlaBfdSessPerfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 5),
    _AlaBfdSessPerfUpTime_Type()
)
alaBfdSessPerfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfUpTime.setStatus("current")
_AlaBfdSessPerfLastSessDownTime_Type = TimeTicks
_AlaBfdSessPerfLastSessDownTime_Object = MibTableColumn
alaBfdSessPerfLastSessDownTime = _AlaBfdSessPerfLastSessDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 6),
    _AlaBfdSessPerfLastSessDownTime_Type()
)
alaBfdSessPerfLastSessDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfLastSessDownTime.setStatus("current")
_AlaBfdSessPerfLastCommLostDiag_Type = AlaBfdDiag
_AlaBfdSessPerfLastCommLostDiag_Object = MibTableColumn
alaBfdSessPerfLastCommLostDiag = _AlaBfdSessPerfLastCommLostDiag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 7),
    _AlaBfdSessPerfLastCommLostDiag_Type()
)
alaBfdSessPerfLastCommLostDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfLastCommLostDiag.setStatus("current")
_AlaBfdSessPerfSessUpCount_Type = Counter64
_AlaBfdSessPerfSessUpCount_Object = MibTableColumn
alaBfdSessPerfSessUpCount = _AlaBfdSessPerfSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 8),
    _AlaBfdSessPerfSessUpCount_Type()
)
alaBfdSessPerfSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfSessUpCount.setStatus("current")
_AlaBfdSessPerfDiscTime_Type = TimeTicks
_AlaBfdSessPerfDiscTime_Object = MibTableColumn
alaBfdSessPerfDiscTime = _AlaBfdSessPerfDiscTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 1, 4, 1, 9),
    _AlaBfdSessPerfDiscTime_Type()
)
alaBfdSessPerfDiscTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaBfdSessPerfDiscTime.setStatus("current")
_AlcatelIND1BfdMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBConformance = _AlcatelIND1BfdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1BfdMIBConformance.setStatus("current")
_AlcatelIND1BfdMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBGroups = _AlcatelIND1BfdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1)
)
_AlcatelIND1BfdMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1BfdMIBCompliances = _AlcatelIND1BfdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 2)
)
alaBfdSessEntry.registerAugmentions(
    ("ALCATEL-IND1-BFD-MIB",
     "alaBfdSessPerfEntry")
)
alaBfdSessPerfEntry.setIndexNames(*alaBfdSessEntry.getIndexNames())

# Managed Objects groups

alaBfdBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 1)
)
alaBfdBasicGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalVersionNumber"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalAdminStatus"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalDetectMult"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalEchoRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdGlobalProtocolApps"))
)
if mibBuilder.loadTexts:
    alaBfdBasicGroup.setStatus("current")

alaBfdIntfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 2)
)
alaBfdIntfCfgGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddr"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAddrType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAdminStatus"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDesiredMinTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfReqMinEchoRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfDetectMult"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthPresFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfAuthenticationType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfIfName"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfOperStatus"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdIntfRowStatus"))
)
if mibBuilder.loadTexts:
    alaBfdIntfCfgGroup.setStatus("current")

alaBfdSessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 3)
)
alaBfdSessGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddrType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNeighborAddr"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessSessionType"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessRemoteDiscr"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessUdpPort"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessState"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessDiag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessOperMode"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessControlPlanIndepFlag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessIfIndex"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedTxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessNegotiatedRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessEchoRxInterval"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessProtocolApps"))
)
if mibBuilder.loadTexts:
    alaBfdSessGroup.setStatus("current")

alaBfdSessPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 1, 4)
)
alaBfdSessPerfGroup.setObjects(
      *(("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktIn"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfPktOut"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEchoOut"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfEchoIn"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfUpTime"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastSessDownTime"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfLastCommLostDiag"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfSessUpCount"),
        ("ALCATEL-IND1-BFD-MIB", "alaBfdSessPerfDiscTime"))
)
if mibBuilder.loadTexts:
    alaBfdSessPerfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1BfdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 45, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1BfdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-BFD-MIB",
    **{"AlaBfdInterval": AlaBfdInterval,
       "AlaBfdDiag": AlaBfdDiag,
       "AlaBfdStatus": AlaBfdStatus,
       "alcatelIND1BfdMIB": alcatelIND1BfdMIB,
       "alaBfdObjects": alaBfdObjects,
       "alaBfdGlobalObjects": alaBfdGlobalObjects,
       "alaBfdGlobalVersionNumber": alaBfdGlobalVersionNumber,
       "alaBfdGlobalAdminStatus": alaBfdGlobalAdminStatus,
       "alaBfdGlobalTxInterval": alaBfdGlobalTxInterval,
       "alaBfdGlobalRxInterval": alaBfdGlobalRxInterval,
       "alaBfdGlobalDetectMult": alaBfdGlobalDetectMult,
       "alaBfdGlobalEchoRxInterval": alaBfdGlobalEchoRxInterval,
       "alaBfdGlobalProtocolApps": alaBfdGlobalProtocolApps,
       "alaBfdIntfTable": alaBfdIntfTable,
       "alaBfdIntfEntry": alaBfdIntfEntry,
       "alaBfdIntfIndex": alaBfdIntfIndex,
       "alaBfdIntfAddrType": alaBfdIntfAddrType,
       "alaBfdIntfAddr": alaBfdIntfAddr,
       "alaBfdIntfAdminStatus": alaBfdIntfAdminStatus,
       "alaBfdIntfDesiredMinTxInterval": alaBfdIntfDesiredMinTxInterval,
       "alaBfdIntfReqMinRxInterval": alaBfdIntfReqMinRxInterval,
       "alaBfdIntfReqMinEchoRxInterval": alaBfdIntfReqMinEchoRxInterval,
       "alaBfdIntfDetectMult": alaBfdIntfDetectMult,
       "alaBfdIntfAuthPresFlag": alaBfdIntfAuthPresFlag,
       "alaBfdIntfAuthenticationType": alaBfdIntfAuthenticationType,
       "alaBfdIntfIfName": alaBfdIntfIfName,
       "alaBfdIntfOperStatus": alaBfdIntfOperStatus,
       "alaBfdIntfRowStatus": alaBfdIntfRowStatus,
       "alaBfdSessTable": alaBfdSessTable,
       "alaBfdSessEntry": alaBfdSessEntry,
       "alaBfdSessDiscriminator": alaBfdSessDiscriminator,
       "alaBfdSessNeighborAddrType": alaBfdSessNeighborAddrType,
       "alaBfdSessNeighborAddr": alaBfdSessNeighborAddr,
       "alaBfdSessSessionType": alaBfdSessSessionType,
       "alaBfdSessRemoteDiscr": alaBfdSessRemoteDiscr,
       "alaBfdSessUdpPort": alaBfdSessUdpPort,
       "alaBfdSessState": alaBfdSessState,
       "alaBfdSessDiag": alaBfdSessDiag,
       "alaBfdSessOperMode": alaBfdSessOperMode,
       "alaBfdSessControlPlanIndepFlag": alaBfdSessControlPlanIndepFlag,
       "alaBfdSessIfIndex": alaBfdSessIfIndex,
       "alaBfdSessNegotiatedTxInterval": alaBfdSessNegotiatedTxInterval,
       "alaBfdSessNegotiatedRxInterval": alaBfdSessNegotiatedRxInterval,
       "alaBfdSessEchoRxInterval": alaBfdSessEchoRxInterval,
       "alaBfdSessProtocolApps": alaBfdSessProtocolApps,
       "alaBfdSessPerfTable": alaBfdSessPerfTable,
       "alaBfdSessPerfEntry": alaBfdSessPerfEntry,
       "alaBfdSessPerfPktIn": alaBfdSessPerfPktIn,
       "alaBfdSessPerfPktOut": alaBfdSessPerfPktOut,
       "alaBfdSessPerfEchoOut": alaBfdSessPerfEchoOut,
       "alaBfdSessPerfEchoIn": alaBfdSessPerfEchoIn,
       "alaBfdSessPerfUpTime": alaBfdSessPerfUpTime,
       "alaBfdSessPerfLastSessDownTime": alaBfdSessPerfLastSessDownTime,
       "alaBfdSessPerfLastCommLostDiag": alaBfdSessPerfLastCommLostDiag,
       "alaBfdSessPerfSessUpCount": alaBfdSessPerfSessUpCount,
       "alaBfdSessPerfDiscTime": alaBfdSessPerfDiscTime,
       "alcatelIND1BfdMIBConformance": alcatelIND1BfdMIBConformance,
       "alcatelIND1BfdMIBGroups": alcatelIND1BfdMIBGroups,
       "alaBfdBasicGroup": alaBfdBasicGroup,
       "alaBfdIntfCfgGroup": alaBfdIntfCfgGroup,
       "alaBfdSessGroup": alaBfdSessGroup,
       "alaBfdSessPerfGroup": alaBfdSessPerfGroup,
       "alcatelIND1BfdMIBCompliances": alcatelIND1BfdMIBCompliances,
       "alcatelIND1BfdMIBCompliance": alcatelIND1BfdMIBCompliance}
)
