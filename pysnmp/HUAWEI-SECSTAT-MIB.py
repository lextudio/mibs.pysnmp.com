# SNMP MIB module (HUAWEI-SECSTAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SECSTAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:51 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSECSTATCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSECSTAT_ObjectIdentity = ObjectIdentity
hwSECSTAT = _HwSECSTAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11)
)
_HwSecStatCfgObjects_ObjectIdentity = ObjectIdentity
hwSecStatCfgObjects = _HwSecStatCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1)
)


class _HwSecStatGlobalStatEnable_Type(TruthValue):
    """Custom type hwSecStatGlobalStatEnable based on TruthValue"""


_HwSecStatGlobalStatEnable_Object = MibScalar
hwSecStatGlobalStatEnable = _HwSecStatGlobalStatEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 1),
    _HwSecStatGlobalStatEnable_Type()
)
hwSecStatGlobalStatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatGlobalStatEnable.setStatus("current")
_HwSecStatGlobalPktScale_ObjectIdentity = ObjectIdentity
hwSecStatGlobalPktScale = _HwSecStatGlobalPktScale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2)
)


class _HwSecStatTcpPktScale_Type(Integer32):
    """Custom type hwSecStatTcpPktScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSecStatTcpPktScale_Type.__name__ = "Integer32"
_HwSecStatTcpPktScale_Object = MibScalar
hwSecStatTcpPktScale = _HwSecStatTcpPktScale_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 1),
    _HwSecStatTcpPktScale_Type()
)
hwSecStatTcpPktScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatTcpPktScale.setStatus("current")


class _HwSecStatUdpPktScale_Type(Integer32):
    """Custom type hwSecStatUdpPktScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSecStatUdpPktScale_Type.__name__ = "Integer32"
_HwSecStatUdpPktScale_Object = MibScalar
hwSecStatUdpPktScale = _HwSecStatUdpPktScale_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 2),
    _HwSecStatUdpPktScale_Type()
)
hwSecStatUdpPktScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatUdpPktScale.setStatus("current")


class _HwSecStatIcmpPktScale_Type(Integer32):
    """Custom type hwSecStatIcmpPktScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSecStatIcmpPktScale_Type.__name__ = "Integer32"
_HwSecStatIcmpPktScale_Object = MibScalar
hwSecStatIcmpPktScale = _HwSecStatIcmpPktScale_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 3),
    _HwSecStatIcmpPktScale_Type()
)
hwSecStatIcmpPktScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatIcmpPktScale.setStatus("current")


class _HwSecStatAlteration_Type(Integer32):
    """Custom type hwSecStatAlteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_HwSecStatAlteration_Type.__name__ = "Integer32"
_HwSecStatAlteration_Object = MibScalar
hwSecStatAlteration = _HwSecStatAlteration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 4),
    _HwSecStatAlteration_Type()
)
hwSecStatAlteration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatAlteration.setStatus("current")


class _HwSecStatCalcTime_Type(Integer32):
    """Custom type hwSecStatCalcTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14400),
    )


_HwSecStatCalcTime_Type.__name__ = "Integer32"
_HwSecStatCalcTime_Object = MibScalar
hwSecStatCalcTime = _HwSecStatCalcTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 5),
    _HwSecStatCalcTime_Type()
)
hwSecStatCalcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatCalcTime.setStatus("current")


class _HwSecStatPktScaleSetDefault_Type(Integer32):
    """Custom type hwSecStatPktScaleSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatPktScaleSetDefault_Type.__name__ = "Integer32"
_HwSecStatPktScaleSetDefault_Object = MibScalar
hwSecStatPktScaleSetDefault = _HwSecStatPktScaleSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 2, 6),
    _HwSecStatPktScaleSetDefault_Type()
)
hwSecStatPktScaleSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatPktScaleSetDefault.setStatus("current")
_HwSecStatGlobalSessNum_ObjectIdentity = ObjectIdentity
hwSecStatGlobalSessNum = _HwSecStatGlobalSessNum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3)
)


class _HwSecStatTcpSessNumMax_Type(Integer32):
    """Custom type hwSecStatTcpSessNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatTcpSessNumMax_Type.__name__ = "Integer32"
_HwSecStatTcpSessNumMax_Object = MibScalar
hwSecStatTcpSessNumMax = _HwSecStatTcpSessNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 1),
    _HwSecStatTcpSessNumMax_Type()
)
hwSecStatTcpSessNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatTcpSessNumMax.setStatus("current")


class _HwSecStatTcpSessNumMin_Type(Integer32):
    """Custom type hwSecStatTcpSessNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatTcpSessNumMin_Type.__name__ = "Integer32"
_HwSecStatTcpSessNumMin_Object = MibScalar
hwSecStatTcpSessNumMin = _HwSecStatTcpSessNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 2),
    _HwSecStatTcpSessNumMin_Type()
)
hwSecStatTcpSessNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatTcpSessNumMin.setStatus("current")


class _HwSecStatUdpSessNumMax_Type(Integer32):
    """Custom type hwSecStatUdpSessNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatUdpSessNumMax_Type.__name__ = "Integer32"
_HwSecStatUdpSessNumMax_Object = MibScalar
hwSecStatUdpSessNumMax = _HwSecStatUdpSessNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 3),
    _HwSecStatUdpSessNumMax_Type()
)
hwSecStatUdpSessNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatUdpSessNumMax.setStatus("current")


class _HwSecStatUdpSessNumMin_Type(Integer32):
    """Custom type hwSecStatUdpSessNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatUdpSessNumMin_Type.__name__ = "Integer32"
_HwSecStatUdpSessNumMin_Object = MibScalar
hwSecStatUdpSessNumMin = _HwSecStatUdpSessNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 4),
    _HwSecStatUdpSessNumMin_Type()
)
hwSecStatUdpSessNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatUdpSessNumMin.setStatus("current")


class _HwSecStatGlobalSessSetDefault_Type(Integer32):
    """Custom type hwSecStatGlobalSessSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatGlobalSessSetDefault_Type.__name__ = "Integer32"
_HwSecStatGlobalSessSetDefault_Object = MibScalar
hwSecStatGlobalSessSetDefault = _HwSecStatGlobalSessSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 5),
    _HwSecStatGlobalSessSetDefault_Type()
)
hwSecStatGlobalSessSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatGlobalSessSetDefault.setStatus("current")


class _HwSecStatIcmpSessNumMax_Type(Integer32):
    """Custom type hwSecStatIcmpSessNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatIcmpSessNumMax_Type.__name__ = "Integer32"
_HwSecStatIcmpSessNumMax_Object = MibScalar
hwSecStatIcmpSessNumMax = _HwSecStatIcmpSessNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 6),
    _HwSecStatIcmpSessNumMax_Type()
)
hwSecStatIcmpSessNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatIcmpSessNumMax.setStatus("current")


class _HwSecStatIcmpSessNumMin_Type(Integer32):
    """Custom type hwSecStatIcmpSessNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatIcmpSessNumMin_Type.__name__ = "Integer32"
_HwSecStatIcmpSessNumMin_Object = MibScalar
hwSecStatIcmpSessNumMin = _HwSecStatIcmpSessNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 7),
    _HwSecStatIcmpSessNumMin_Type()
)
hwSecStatIcmpSessNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatIcmpSessNumMin.setStatus("current")


class _HwSecStatTcpProxySessNumMax_Type(Integer32):
    """Custom type hwSecStatTcpProxySessNumMax based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatTcpProxySessNumMax_Type.__name__ = "Integer32"
_HwSecStatTcpProxySessNumMax_Object = MibScalar
hwSecStatTcpProxySessNumMax = _HwSecStatTcpProxySessNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 8),
    _HwSecStatTcpProxySessNumMax_Type()
)
hwSecStatTcpProxySessNumMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatTcpProxySessNumMax.setStatus("current")


class _HwSecStatTcpProxySessNumMin_Type(Integer32):
    """Custom type hwSecStatTcpProxySessNumMin based on Integer32"""
    defaultValue = 500000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500000),
    )


_HwSecStatTcpProxySessNumMin_Type.__name__ = "Integer32"
_HwSecStatTcpProxySessNumMin_Object = MibScalar
hwSecStatTcpProxySessNumMin = _HwSecStatTcpProxySessNumMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 1, 3, 9),
    _HwSecStatTcpProxySessNumMin_Type()
)
hwSecStatTcpProxySessNumMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatTcpProxySessNumMin.setStatus("current")
_HwSecStatMonitorObjects_ObjectIdentity = ObjectIdentity
hwSecStatMonitorObjects = _HwSecStatMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2)
)
_HwSecStatMonitorGlobalSessFlow_ObjectIdentity = ObjectIdentity
hwSecStatMonitorGlobalSessFlow = _HwSecStatMonitorGlobalSessFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1)
)
_HwSecStatMonTotalBootConnNum_Type = Counter64
_HwSecStatMonTotalBootConnNum_Object = MibScalar
hwSecStatMonTotalBootConnNum = _HwSecStatMonTotalBootConnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 1),
    _HwSecStatMonTotalBootConnNum_Type()
)
hwSecStatMonTotalBootConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonTotalBootConnNum.setStatus("current")
_HwSecStatMonPeakSessSpeed_Type = Counter64
_HwSecStatMonPeakSessSpeed_Object = MibScalar
hwSecStatMonPeakSessSpeed = _HwSecStatMonPeakSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 2),
    _HwSecStatMonPeakSessSpeed_Type()
)
hwSecStatMonPeakSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPeakSessSpeed.setStatus("current")
_HwSecStatMonCurSessSpeed_Type = Counter64
_HwSecStatMonCurSessSpeed_Object = MibScalar
hwSecStatMonCurSessSpeed = _HwSecStatMonCurSessSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 3),
    _HwSecStatMonCurSessSpeed_Type()
)
hwSecStatMonCurSessSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonCurSessSpeed.setStatus("current")
_HwSecStatMonTotalSess_Type = Counter64
_HwSecStatMonTotalSess_Object = MibScalar
hwSecStatMonTotalSess = _HwSecStatMonTotalSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 4),
    _HwSecStatMonTotalSess_Type()
)
hwSecStatMonTotalSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonTotalSess.setStatus("current")
_HwSecStatMonHalfConn_Type = Counter64
_HwSecStatMonHalfConn_Object = MibScalar
hwSecStatMonHalfConn = _HwSecStatMonHalfConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 5),
    _HwSecStatMonHalfConn_Type()
)
hwSecStatMonHalfConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonHalfConn.setStatus("current")
_HwSecStatMonTcpSess_Type = Counter64
_HwSecStatMonTcpSess_Object = MibScalar
hwSecStatMonTcpSess = _HwSecStatMonTcpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 6),
    _HwSecStatMonTcpSess_Type()
)
hwSecStatMonTcpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonTcpSess.setStatus("current")
_HwSecStatMonUdpSess_Type = Counter64
_HwSecStatMonUdpSess_Object = MibScalar
hwSecStatMonUdpSess = _HwSecStatMonUdpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 7),
    _HwSecStatMonUdpSess_Type()
)
hwSecStatMonUdpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonUdpSess.setStatus("current")
_HwSecStatMonIcmpSess_Type = Counter64
_HwSecStatMonIcmpSess_Object = MibScalar
hwSecStatMonIcmpSess = _HwSecStatMonIcmpSess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 8),
    _HwSecStatMonIcmpSess_Type()
)
hwSecStatMonIcmpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonIcmpSess.setStatus("current")
_HwSecStatMonSvrMapTblNum_Type = Counter64
_HwSecStatMonSvrMapTblNum_Object = MibScalar
hwSecStatMonSvrMapTblNum = _HwSecStatMonSvrMapTblNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 9),
    _HwSecStatMonSvrMapTblNum_Type()
)
hwSecStatMonSvrMapTblNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonSvrMapTblNum.setStatus("current")
_HwSecStatFragTblNum_Type = Counter64
_HwSecStatFragTblNum_Object = MibScalar
hwSecStatFragTblNum = _HwSecStatFragTblNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 10),
    _HwSecStatFragTblNum_Type()
)
hwSecStatFragTblNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatFragTblNum.setStatus("current")
_HwSecStatMonRcvIcmpPkts_Type = Counter64
_HwSecStatMonRcvIcmpPkts_Object = MibScalar
hwSecStatMonRcvIcmpPkts = _HwSecStatMonRcvIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 11),
    _HwSecStatMonRcvIcmpPkts_Type()
)
hwSecStatMonRcvIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvIcmpPkts.setStatus("current")
_HwSecStatMonRcvIcmpOcts_Type = Counter64
_HwSecStatMonRcvIcmpOcts_Object = MibScalar
hwSecStatMonRcvIcmpOcts = _HwSecStatMonRcvIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 12),
    _HwSecStatMonRcvIcmpOcts_Type()
)
hwSecStatMonRcvIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvIcmpOcts.setStatus("current")
_HwSecStatMonRcvTcpPkts_Type = Counter64
_HwSecStatMonRcvTcpPkts_Object = MibScalar
hwSecStatMonRcvTcpPkts = _HwSecStatMonRcvTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 13),
    _HwSecStatMonRcvTcpPkts_Type()
)
hwSecStatMonRcvTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvTcpPkts.setStatus("current")
_HwSecStatMonRcvTcpOcts_Type = Counter64
_HwSecStatMonRcvTcpOcts_Object = MibScalar
hwSecStatMonRcvTcpOcts = _HwSecStatMonRcvTcpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 14),
    _HwSecStatMonRcvTcpOcts_Type()
)
hwSecStatMonRcvTcpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvTcpOcts.setStatus("current")
_HwSecStatMonRcvUdpPkts_Type = Counter64
_HwSecStatMonRcvUdpPkts_Object = MibScalar
hwSecStatMonRcvUdpPkts = _HwSecStatMonRcvUdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 15),
    _HwSecStatMonRcvUdpPkts_Type()
)
hwSecStatMonRcvUdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvUdpPkts.setStatus("current")
_HwSecStatMonRcvUdpOcts_Type = Counter64
_HwSecStatMonRcvUdpOcts_Object = MibScalar
hwSecStatMonRcvUdpOcts = _HwSecStatMonRcvUdpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 16),
    _HwSecStatMonRcvUdpOcts_Type()
)
hwSecStatMonRcvUdpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvUdpOcts.setStatus("current")
_HwSecStatMonRcvEtcPkts_Type = Counter64
_HwSecStatMonRcvEtcPkts_Object = MibScalar
hwSecStatMonRcvEtcPkts = _HwSecStatMonRcvEtcPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 17),
    _HwSecStatMonRcvEtcPkts_Type()
)
hwSecStatMonRcvEtcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvEtcPkts.setStatus("current")
_HwSecStatMonRcvEtcOcts_Type = Counter64
_HwSecStatMonRcvEtcOcts_Object = MibScalar
hwSecStatMonRcvEtcOcts = _HwSecStatMonRcvEtcOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 18),
    _HwSecStatMonRcvEtcOcts_Type()
)
hwSecStatMonRcvEtcOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvEtcOcts.setStatus("current")
_HwSecStatMonPassIcmpPkts_Type = Counter64
_HwSecStatMonPassIcmpPkts_Object = MibScalar
hwSecStatMonPassIcmpPkts = _HwSecStatMonPassIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 19),
    _HwSecStatMonPassIcmpPkts_Type()
)
hwSecStatMonPassIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassIcmpPkts.setStatus("current")
_HwSecStatMonPassIcmpOcts_Type = Counter64
_HwSecStatMonPassIcmpOcts_Object = MibScalar
hwSecStatMonPassIcmpOcts = _HwSecStatMonPassIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 20),
    _HwSecStatMonPassIcmpOcts_Type()
)
hwSecStatMonPassIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassIcmpOcts.setStatus("current")
_HwSecStatMonPassTcpPkts_Type = Counter64
_HwSecStatMonPassTcpPkts_Object = MibScalar
hwSecStatMonPassTcpPkts = _HwSecStatMonPassTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 21),
    _HwSecStatMonPassTcpPkts_Type()
)
hwSecStatMonPassTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassTcpPkts.setStatus("current")
_HwSecStatMonPassTcpOcts_Type = Counter64
_HwSecStatMonPassTcpOcts_Object = MibScalar
hwSecStatMonPassTcpOcts = _HwSecStatMonPassTcpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 22),
    _HwSecStatMonPassTcpOcts_Type()
)
hwSecStatMonPassTcpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassTcpOcts.setStatus("current")
_HwSecStatMonPassUdpPkts_Type = Counter64
_HwSecStatMonPassUdpPkts_Object = MibScalar
hwSecStatMonPassUdpPkts = _HwSecStatMonPassUdpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 23),
    _HwSecStatMonPassUdpPkts_Type()
)
hwSecStatMonPassUdpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassUdpPkts.setStatus("current")
_HwSecStatMonPassUdpOcts_Type = Counter64
_HwSecStatMonPassUdpOcts_Object = MibScalar
hwSecStatMonPassUdpOcts = _HwSecStatMonPassUdpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 24),
    _HwSecStatMonPassUdpOcts_Type()
)
hwSecStatMonPassUdpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassUdpOcts.setStatus("current")
_HwSecStatMonPassEtcPkts_Type = Counter64
_HwSecStatMonPassEtcPkts_Object = MibScalar
hwSecStatMonPassEtcPkts = _HwSecStatMonPassEtcPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 25),
    _HwSecStatMonPassEtcPkts_Type()
)
hwSecStatMonPassEtcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassEtcPkts.setStatus("current")
_HwSecStatMonPassEtcOcts_Type = Counter64
_HwSecStatMonPassEtcOcts_Object = MibScalar
hwSecStatMonPassEtcOcts = _HwSecStatMonPassEtcOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 26),
    _HwSecStatMonPassEtcOcts_Type()
)
hwSecStatMonPassEtcOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonPassEtcOcts.setStatus("current")
_HwSecStatMonSynPkts_Type = Counter64
_HwSecStatMonSynPkts_Object = MibScalar
hwSecStatMonSynPkts = _HwSecStatMonSynPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 27),
    _HwSecStatMonSynPkts_Type()
)
hwSecStatMonSynPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonSynPkts.setStatus("current")
_HwSecStatMonFinPkts_Type = Counter64
_HwSecStatMonFinPkts_Object = MibScalar
hwSecStatMonFinPkts = _HwSecStatMonFinPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 28),
    _HwSecStatMonFinPkts_Type()
)
hwSecStatMonFinPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonFinPkts.setStatus("current")
_HwSecStatMonSynAckPkts_Type = Counter64
_HwSecStatMonSynAckPkts_Object = MibScalar
hwSecStatMonSynAckPkts = _HwSecStatMonSynAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 29),
    _HwSecStatMonSynAckPkts_Type()
)
hwSecStatMonSynAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonSynAckPkts.setStatus("current")
_HwSecStatMonRstPkts_Type = Counter64
_HwSecStatMonRstPkts_Object = MibScalar
hwSecStatMonRstPkts = _HwSecStatMonRstPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 30),
    _HwSecStatMonRstPkts_Type()
)
hwSecStatMonRstPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRstPkts.setStatus("current")
_HwSecStatMonRcvFragPkts_Type = Counter64
_HwSecStatMonRcvFragPkts_Object = MibScalar
hwSecStatMonRcvFragPkts = _HwSecStatMonRcvFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 31),
    _HwSecStatMonRcvFragPkts_Type()
)
hwSecStatMonRcvFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvFragPkts.setStatus("current")
_HwSecStatMonRcvFragOcts_Type = Counter64
_HwSecStatMonRcvFragOcts_Object = MibScalar
hwSecStatMonRcvFragOcts = _HwSecStatMonRcvFragOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 32),
    _HwSecStatMonRcvFragOcts_Type()
)
hwSecStatMonRcvFragOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvFragOcts.setStatus("current")
_HwSecStatMonAllPkts_Type = Counter64
_HwSecStatMonAllPkts_Object = MibScalar
hwSecStatMonAllPkts = _HwSecStatMonAllPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 33),
    _HwSecStatMonAllPkts_Type()
)
hwSecStatMonAllPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonAllPkts.setStatus("current")
_HwSecStatMonAllOcts_Type = Counter64
_HwSecStatMonAllOcts_Object = MibScalar
hwSecStatMonAllOcts = _HwSecStatMonAllOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 34),
    _HwSecStatMonAllOcts_Type()
)
hwSecStatMonAllOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonAllOcts.setStatus("current")


class _HwSecStatClearGlobalSessFlowInfo_Type(Integer32):
    """Custom type hwSecStatClearGlobalSessFlowInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearGlobalSessFlowInfo_Type.__name__ = "Integer32"
_HwSecStatClearGlobalSessFlowInfo_Object = MibScalar
hwSecStatClearGlobalSessFlowInfo = _HwSecStatClearGlobalSessFlowInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 1, 35),
    _HwSecStatClearGlobalSessFlowInfo_Type()
)
hwSecStatClearGlobalSessFlowInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearGlobalSessFlowInfo.setStatus("current")
_HwSecStatMonitorGlobalAppInfo_ObjectIdentity = ObjectIdentity
hwSecStatMonitorGlobalAppInfo = _HwSecStatMonitorGlobalAppInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2)
)
_HwSecStatMonFtpSessions_Type = Counter64
_HwSecStatMonFtpSessions_Object = MibScalar
hwSecStatMonFtpSessions = _HwSecStatMonFtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 1),
    _HwSecStatMonFtpSessions_Type()
)
hwSecStatMonFtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonFtpSessions.setStatus("current")
_HwSecStatMonRcvFtpPkts_Type = Counter64
_HwSecStatMonRcvFtpPkts_Object = MibScalar
hwSecStatMonRcvFtpPkts = _HwSecStatMonRcvFtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 2),
    _HwSecStatMonRcvFtpPkts_Type()
)
hwSecStatMonRcvFtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvFtpPkts.setStatus("current")
_HwSecStatMonRcvFtpOcts_Type = Counter64
_HwSecStatMonRcvFtpOcts_Object = MibScalar
hwSecStatMonRcvFtpOcts = _HwSecStatMonRcvFtpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 3),
    _HwSecStatMonRcvFtpOcts_Type()
)
hwSecStatMonRcvFtpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvFtpOcts.setStatus("current")
_HwSecStatMonSmtpSessions_Type = Counter64
_HwSecStatMonSmtpSessions_Object = MibScalar
hwSecStatMonSmtpSessions = _HwSecStatMonSmtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 4),
    _HwSecStatMonSmtpSessions_Type()
)
hwSecStatMonSmtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonSmtpSessions.setStatus("current")
_HwSecStatMonRcvSmtpPkts_Type = Counter64
_HwSecStatMonRcvSmtpPkts_Object = MibScalar
hwSecStatMonRcvSmtpPkts = _HwSecStatMonRcvSmtpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 5),
    _HwSecStatMonRcvSmtpPkts_Type()
)
hwSecStatMonRcvSmtpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvSmtpPkts.setStatus("current")
_HwSecStatMonRcvSmtpOcts_Type = Counter64
_HwSecStatMonRcvSmtpOcts_Object = MibScalar
hwSecStatMonRcvSmtpOcts = _HwSecStatMonRcvSmtpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 6),
    _HwSecStatMonRcvSmtpOcts_Type()
)
hwSecStatMonRcvSmtpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvSmtpOcts.setStatus("current")
_HwSecStatMonHttpSessions_Type = Counter64
_HwSecStatMonHttpSessions_Object = MibScalar
hwSecStatMonHttpSessions = _HwSecStatMonHttpSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 7),
    _HwSecStatMonHttpSessions_Type()
)
hwSecStatMonHttpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonHttpSessions.setStatus("current")
_HwSecStatMonRcvHttpPkts_Type = Counter64
_HwSecStatMonRcvHttpPkts_Object = MibScalar
hwSecStatMonRcvHttpPkts = _HwSecStatMonRcvHttpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 8),
    _HwSecStatMonRcvHttpPkts_Type()
)
hwSecStatMonRcvHttpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvHttpPkts.setStatus("current")
_HwSecStatMonRcvHttpOcts_Type = Counter64
_HwSecStatMonRcvHttpOcts_Object = MibScalar
hwSecStatMonRcvHttpOcts = _HwSecStatMonRcvHttpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 9),
    _HwSecStatMonRcvHttpOcts_Type()
)
hwSecStatMonRcvHttpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvHttpOcts.setStatus("current")
_HwSecStatMonH323Sessions_Type = Counter64
_HwSecStatMonH323Sessions_Object = MibScalar
hwSecStatMonH323Sessions = _HwSecStatMonH323Sessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 10),
    _HwSecStatMonH323Sessions_Type()
)
hwSecStatMonH323Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonH323Sessions.setStatus("current")
_HwSecStatMonRcvH323Pkts_Type = Counter64
_HwSecStatMonRcvH323Pkts_Object = MibScalar
hwSecStatMonRcvH323Pkts = _HwSecStatMonRcvH323Pkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 11),
    _HwSecStatMonRcvH323Pkts_Type()
)
hwSecStatMonRcvH323Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvH323Pkts.setStatus("current")
_HwSecStatMonRcvH323Octs_Type = Counter64
_HwSecStatMonRcvH323Octs_Object = MibScalar
hwSecStatMonRcvH323Octs = _HwSecStatMonRcvH323Octs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 12),
    _HwSecStatMonRcvH323Octs_Type()
)
hwSecStatMonRcvH323Octs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvH323Octs.setStatus("current")
_HwSecStatMonRtspSessions_Type = Counter64
_HwSecStatMonRtspSessions_Object = MibScalar
hwSecStatMonRtspSessions = _HwSecStatMonRtspSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 13),
    _HwSecStatMonRtspSessions_Type()
)
hwSecStatMonRtspSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRtspSessions.setStatus("current")
_HwSecStatMonRcvRtspPkts_Type = Counter64
_HwSecStatMonRcvRtspPkts_Object = MibScalar
hwSecStatMonRcvRtspPkts = _HwSecStatMonRcvRtspPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 14),
    _HwSecStatMonRcvRtspPkts_Type()
)
hwSecStatMonRcvRtspPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvRtspPkts.setStatus("current")
_HwSecStatMonRcvRtspOcts_Type = Counter64
_HwSecStatMonRcvRtspOcts_Object = MibScalar
hwSecStatMonRcvRtspOcts = _HwSecStatMonRcvRtspOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 15),
    _HwSecStatMonRcvRtspOcts_Type()
)
hwSecStatMonRcvRtspOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonRcvRtspOcts.setStatus("current")
_HwSecStatMonJavaAtckNum_Type = Counter64
_HwSecStatMonJavaAtckNum_Object = MibScalar
hwSecStatMonJavaAtckNum = _HwSecStatMonJavaAtckNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 16),
    _HwSecStatMonJavaAtckNum_Type()
)
hwSecStatMonJavaAtckNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatMonJavaAtckNum.setStatus("current")


class _HwSecStatClearGlobalAppInfo_Type(Integer32):
    """Custom type hwSecStatClearGlobalAppInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearGlobalAppInfo_Type.__name__ = "Integer32"
_HwSecStatClearGlobalAppInfo_Object = MibScalar
hwSecStatClearGlobalAppInfo = _HwSecStatClearGlobalAppInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 2, 17),
    _HwSecStatClearGlobalAppInfo_Type()
)
hwSecStatClearGlobalAppInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearGlobalAppInfo.setStatus("current")
_HwSecStatMonitorGlobalDrop_ObjectIdentity = ObjectIdentity
hwSecStatMonitorGlobalDrop = _HwSecStatMonitorGlobalDrop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3)
)
_HwSecStatNoSessTblPkts_Type = Counter64
_HwSecStatNoSessTblPkts_Object = MibScalar
hwSecStatNoSessTblPkts = _HwSecStatNoSessTblPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 1),
    _HwSecStatNoSessTblPkts_Type()
)
hwSecStatNoSessTblPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatNoSessTblPkts.setStatus("current")
_HwSecStatNoSessTblOcts_Type = Counter64
_HwSecStatNoSessTblOcts_Object = MibScalar
hwSecStatNoSessTblOcts = _HwSecStatNoSessTblOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 2),
    _HwSecStatNoSessTblOcts_Type()
)
hwSecStatNoSessTblOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatNoSessTblOcts.setStatus("current")
_HwSecStatSeqErrPkts_Type = Counter64
_HwSecStatSeqErrPkts_Object = MibScalar
hwSecStatSeqErrPkts = _HwSecStatSeqErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 3),
    _HwSecStatSeqErrPkts_Type()
)
hwSecStatSeqErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatSeqErrPkts.setStatus("current")
_HwSecStatSeqErrOcts_Type = Counter64
_HwSecStatSeqErrOcts_Object = MibScalar
hwSecStatSeqErrOcts = _HwSecStatSeqErrOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 4),
    _HwSecStatSeqErrOcts_Type()
)
hwSecStatSeqErrOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatSeqErrOcts.setStatus("current")
_HwSecStatAclDenyNonIcmpPkts_Type = Counter64
_HwSecStatAclDenyNonIcmpPkts_Object = MibScalar
hwSecStatAclDenyNonIcmpPkts = _HwSecStatAclDenyNonIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 5),
    _HwSecStatAclDenyNonIcmpPkts_Type()
)
hwSecStatAclDenyNonIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAclDenyNonIcmpPkts.setStatus("current")
_HwSecStatAclDenyNonIcmpOcts_Type = Counter64
_HwSecStatAclDenyNonIcmpOcts_Object = MibScalar
hwSecStatAclDenyNonIcmpOcts = _HwSecStatAclDenyNonIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 6),
    _HwSecStatAclDenyNonIcmpOcts_Type()
)
hwSecStatAclDenyNonIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAclDenyNonIcmpOcts.setStatus("current")
_HwSecStatAclDenyIcmpPkts_Type = Counter64
_HwSecStatAclDenyIcmpPkts_Object = MibScalar
hwSecStatAclDenyIcmpPkts = _HwSecStatAclDenyIcmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 7),
    _HwSecStatAclDenyIcmpPkts_Type()
)
hwSecStatAclDenyIcmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAclDenyIcmpPkts.setStatus("current")
_HwSecStatAclDenyIcmpOcts_Type = Counter64
_HwSecStatAclDenyIcmpOcts_Object = MibScalar
hwSecStatAclDenyIcmpOcts = _HwSecStatAclDenyIcmpOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 8),
    _HwSecStatAclDenyIcmpOcts_Type()
)
hwSecStatAclDenyIcmpOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAclDenyIcmpOcts.setStatus("current")
_HwSecStatBlsDenyPkts_Type = Counter64
_HwSecStatBlsDenyPkts_Object = MibScalar
hwSecStatBlsDenyPkts = _HwSecStatBlsDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 9),
    _HwSecStatBlsDenyPkts_Type()
)
hwSecStatBlsDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatBlsDenyPkts.setStatus("current")
_HwSecStatBlsDenyOcts_Type = Counter64
_HwSecStatBlsDenyOcts_Object = MibScalar
hwSecStatBlsDenyOcts = _HwSecStatBlsDenyOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 10),
    _HwSecStatBlsDenyOcts_Type()
)
hwSecStatBlsDenyOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatBlsDenyOcts.setStatus("current")
_HwSecStatIcmpFloodDropPkts_Type = Counter64
_HwSecStatIcmpFloodDropPkts_Object = MibScalar
hwSecStatIcmpFloodDropPkts = _HwSecStatIcmpFloodDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 11),
    _HwSecStatIcmpFloodDropPkts_Type()
)
hwSecStatIcmpFloodDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIcmpFloodDropPkts.setStatus("current")
_HwSecStatIcmpFloodDropOcts_Type = Counter64
_HwSecStatIcmpFloodDropOcts_Object = MibScalar
hwSecStatIcmpFloodDropOcts = _HwSecStatIcmpFloodDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 12),
    _HwSecStatIcmpFloodDropOcts_Type()
)
hwSecStatIcmpFloodDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIcmpFloodDropOcts.setStatus("current")
_HwSecStatUdpFloodDropPkts_Type = Counter64
_HwSecStatUdpFloodDropPkts_Object = MibScalar
hwSecStatUdpFloodDropPkts = _HwSecStatUdpFloodDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 13),
    _HwSecStatUdpFloodDropPkts_Type()
)
hwSecStatUdpFloodDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatUdpFloodDropPkts.setStatus("current")
_HwSecStatUdpFloodDropOcts_Type = Counter64
_HwSecStatUdpFloodDropOcts_Object = MibScalar
hwSecStatUdpFloodDropOcts = _HwSecStatUdpFloodDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 14),
    _HwSecStatUdpFloodDropOcts_Type()
)
hwSecStatUdpFloodDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatUdpFloodDropOcts.setStatus("current")
_HwSecStatAlgDropPkts_Type = Counter64
_HwSecStatAlgDropPkts_Object = MibScalar
hwSecStatAlgDropPkts = _HwSecStatAlgDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 15),
    _HwSecStatAlgDropPkts_Type()
)
hwSecStatAlgDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAlgDropPkts.setStatus("current")
_HwSecStatAlgDropOcts_Type = Counter64
_HwSecStatAlgDropOcts_Object = MibScalar
hwSecStatAlgDropOcts = _HwSecStatAlgDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 16),
    _HwSecStatAlgDropOcts_Type()
)
hwSecStatAlgDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatAlgDropOcts.setStatus("current")
_HwSecStatIPVerErrDropPkts_Type = Counter64
_HwSecStatIPVerErrDropPkts_Object = MibScalar
hwSecStatIPVerErrDropPkts = _HwSecStatIPVerErrDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 17),
    _HwSecStatIPVerErrDropPkts_Type()
)
hwSecStatIPVerErrDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPVerErrDropPkts.setStatus("current")
_HwSecStatIpCrcDropPkts_Type = Counter64
_HwSecStatIpCrcDropPkts_Object = MibScalar
hwSecStatIpCrcDropPkts = _HwSecStatIpCrcDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 18),
    _HwSecStatIpCrcDropPkts_Type()
)
hwSecStatIpCrcDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIpCrcDropPkts.setStatus("current")
_HwSecStatIpTTLDropPkts_Type = Counter64
_HwSecStatIpTTLDropPkts_Object = MibScalar
hwSecStatIpTTLDropPkts = _HwSecStatIpTTLDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 19),
    _HwSecStatIpTTLDropPkts_Type()
)
hwSecStatIpTTLDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIpTTLDropPkts.setStatus("current")
_HwSecStatProtoErrDropPkts_Type = Counter64
_HwSecStatProtoErrDropPkts_Object = MibScalar
hwSecStatProtoErrDropPkts = _HwSecStatProtoErrDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 20),
    _HwSecStatProtoErrDropPkts_Type()
)
hwSecStatProtoErrDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatProtoErrDropPkts.setStatus("current")


class _HwSecStatClearGlobalDropInfo_Type(Integer32):
    """Custom type hwSecStatClearGlobalDropInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearGlobalDropInfo_Type.__name__ = "Integer32"
_HwSecStatClearGlobalDropInfo_Object = MibScalar
hwSecStatClearGlobalDropInfo = _HwSecStatClearGlobalDropInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 2, 3, 21),
    _HwSecStatClearGlobalDropInfo_Type()
)
hwSecStatClearGlobalDropInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearGlobalDropInfo.setStatus("current")
_HwSecStatConformance_ObjectIdentity = ObjectIdentity
hwSecStatConformance = _HwSecStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 3)
)
_HwSecStatCompliance_ObjectIdentity = ObjectIdentity
hwSecStatCompliance = _HwSecStatCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 3, 1)
)
_HwSecStatMibGroups_ObjectIdentity = ObjectIdentity
hwSecStatMibGroups = _HwSecStatMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 3, 2)
)

# Managed Objects groups

hwSecStatGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 3, 2, 1)
)
hwSecStatGlobalCfgGroup.setObjects(
      *(("HUAWEI-SECSTAT-MIB", "hwSecStatTcpPktScale"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatUdpPktScale"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIcmpPktScale"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAlteration"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatCalcTime"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatTcpSessNumMax"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatTcpSessNumMin"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatUdpSessNumMax"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatGlobalSessSetDefault"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIcmpSessNumMax"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIcmpSessNumMin"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatTcpProxySessNumMax"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatTcpProxySessNumMin"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatPktScaleSetDefault"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatUdpSessNumMin"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatGlobalStatEnable"))
)
if mibBuilder.loadTexts:
    hwSecStatGlobalCfgGroup.setStatus("current")

hwSecStatGlobalMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 1, 3, 2, 2)
)
hwSecStatGlobalMonitorGroup.setObjects(
      *(("HUAWEI-SECSTAT-MIB", "hwSecStatMonTotalSess"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonHalfConn"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvIcmpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvIcmpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvTcpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvTcpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvUdpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvUdpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvEtcPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvEtcOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassIcmpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassIcmpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassTcpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassTcpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassUdpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassUdpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassEtcPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPassEtcOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonSynPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonFinPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonSynAckPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRstPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvFragPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvFragOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonFtpSessions"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvFtpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvFtpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonSmtpSessions"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvSmtpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvSmtpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonHttpSessions"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvHttpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvHttpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonH323Sessions"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvH323Pkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvH323Octs"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRtspSessions"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvRtspPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonRcvRtspOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonJavaAtckNum"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatNoSessTblPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatNoSessTblOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatSeqErrPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatSeqErrOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIcmpFloodDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIcmpFloodDropOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatUdpFloodDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatUdpFloodDropOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAlgDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAlgDropOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIPVerErrDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIpCrcDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatIpTTLDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonCurSessSpeed"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonPeakSessSpeed"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonTotalBootConnNum"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatProtoErrDropPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAclDenyNonIcmpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAclDenyNonIcmpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAclDenyIcmpPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatAclDenyIcmpOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatBlsDenyPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatClearGlobalDropInfo"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatClearGlobalAppInfo"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatClearGlobalSessFlowInfo"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatBlsDenyOcts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonTcpSess"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonUdpSess"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonIcmpSess"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonSvrMapTblNum"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatFragTblNum"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonAllPkts"),
        ("HUAWEI-SECSTAT-MIB", "hwSecStatMonAllOcts"))
)
if mibBuilder.loadTexts:
    hwSecStatGlobalMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECSTAT-MIB",
    **{"hwSECSTAT": hwSECSTAT,
       "hwSECSTATCommon": hwSECSTATCommon,
       "hwSecStatCfgObjects": hwSecStatCfgObjects,
       "hwSecStatGlobalStatEnable": hwSecStatGlobalStatEnable,
       "hwSecStatGlobalPktScale": hwSecStatGlobalPktScale,
       "hwSecStatTcpPktScale": hwSecStatTcpPktScale,
       "hwSecStatUdpPktScale": hwSecStatUdpPktScale,
       "hwSecStatIcmpPktScale": hwSecStatIcmpPktScale,
       "hwSecStatAlteration": hwSecStatAlteration,
       "hwSecStatCalcTime": hwSecStatCalcTime,
       "hwSecStatPktScaleSetDefault": hwSecStatPktScaleSetDefault,
       "hwSecStatGlobalSessNum": hwSecStatGlobalSessNum,
       "hwSecStatTcpSessNumMax": hwSecStatTcpSessNumMax,
       "hwSecStatTcpSessNumMin": hwSecStatTcpSessNumMin,
       "hwSecStatUdpSessNumMax": hwSecStatUdpSessNumMax,
       "hwSecStatUdpSessNumMin": hwSecStatUdpSessNumMin,
       "hwSecStatGlobalSessSetDefault": hwSecStatGlobalSessSetDefault,
       "hwSecStatIcmpSessNumMax": hwSecStatIcmpSessNumMax,
       "hwSecStatIcmpSessNumMin": hwSecStatIcmpSessNumMin,
       "hwSecStatTcpProxySessNumMax": hwSecStatTcpProxySessNumMax,
       "hwSecStatTcpProxySessNumMin": hwSecStatTcpProxySessNumMin,
       "hwSecStatMonitorObjects": hwSecStatMonitorObjects,
       "hwSecStatMonitorGlobalSessFlow": hwSecStatMonitorGlobalSessFlow,
       "hwSecStatMonTotalBootConnNum": hwSecStatMonTotalBootConnNum,
       "hwSecStatMonPeakSessSpeed": hwSecStatMonPeakSessSpeed,
       "hwSecStatMonCurSessSpeed": hwSecStatMonCurSessSpeed,
       "hwSecStatMonTotalSess": hwSecStatMonTotalSess,
       "hwSecStatMonHalfConn": hwSecStatMonHalfConn,
       "hwSecStatMonTcpSess": hwSecStatMonTcpSess,
       "hwSecStatMonUdpSess": hwSecStatMonUdpSess,
       "hwSecStatMonIcmpSess": hwSecStatMonIcmpSess,
       "hwSecStatMonSvrMapTblNum": hwSecStatMonSvrMapTblNum,
       "hwSecStatFragTblNum": hwSecStatFragTblNum,
       "hwSecStatMonRcvIcmpPkts": hwSecStatMonRcvIcmpPkts,
       "hwSecStatMonRcvIcmpOcts": hwSecStatMonRcvIcmpOcts,
       "hwSecStatMonRcvTcpPkts": hwSecStatMonRcvTcpPkts,
       "hwSecStatMonRcvTcpOcts": hwSecStatMonRcvTcpOcts,
       "hwSecStatMonRcvUdpPkts": hwSecStatMonRcvUdpPkts,
       "hwSecStatMonRcvUdpOcts": hwSecStatMonRcvUdpOcts,
       "hwSecStatMonRcvEtcPkts": hwSecStatMonRcvEtcPkts,
       "hwSecStatMonRcvEtcOcts": hwSecStatMonRcvEtcOcts,
       "hwSecStatMonPassIcmpPkts": hwSecStatMonPassIcmpPkts,
       "hwSecStatMonPassIcmpOcts": hwSecStatMonPassIcmpOcts,
       "hwSecStatMonPassTcpPkts": hwSecStatMonPassTcpPkts,
       "hwSecStatMonPassTcpOcts": hwSecStatMonPassTcpOcts,
       "hwSecStatMonPassUdpPkts": hwSecStatMonPassUdpPkts,
       "hwSecStatMonPassUdpOcts": hwSecStatMonPassUdpOcts,
       "hwSecStatMonPassEtcPkts": hwSecStatMonPassEtcPkts,
       "hwSecStatMonPassEtcOcts": hwSecStatMonPassEtcOcts,
       "hwSecStatMonSynPkts": hwSecStatMonSynPkts,
       "hwSecStatMonFinPkts": hwSecStatMonFinPkts,
       "hwSecStatMonSynAckPkts": hwSecStatMonSynAckPkts,
       "hwSecStatMonRstPkts": hwSecStatMonRstPkts,
       "hwSecStatMonRcvFragPkts": hwSecStatMonRcvFragPkts,
       "hwSecStatMonRcvFragOcts": hwSecStatMonRcvFragOcts,
       "hwSecStatMonAllPkts": hwSecStatMonAllPkts,
       "hwSecStatMonAllOcts": hwSecStatMonAllOcts,
       "hwSecStatClearGlobalSessFlowInfo": hwSecStatClearGlobalSessFlowInfo,
       "hwSecStatMonitorGlobalAppInfo": hwSecStatMonitorGlobalAppInfo,
       "hwSecStatMonFtpSessions": hwSecStatMonFtpSessions,
       "hwSecStatMonRcvFtpPkts": hwSecStatMonRcvFtpPkts,
       "hwSecStatMonRcvFtpOcts": hwSecStatMonRcvFtpOcts,
       "hwSecStatMonSmtpSessions": hwSecStatMonSmtpSessions,
       "hwSecStatMonRcvSmtpPkts": hwSecStatMonRcvSmtpPkts,
       "hwSecStatMonRcvSmtpOcts": hwSecStatMonRcvSmtpOcts,
       "hwSecStatMonHttpSessions": hwSecStatMonHttpSessions,
       "hwSecStatMonRcvHttpPkts": hwSecStatMonRcvHttpPkts,
       "hwSecStatMonRcvHttpOcts": hwSecStatMonRcvHttpOcts,
       "hwSecStatMonH323Sessions": hwSecStatMonH323Sessions,
       "hwSecStatMonRcvH323Pkts": hwSecStatMonRcvH323Pkts,
       "hwSecStatMonRcvH323Octs": hwSecStatMonRcvH323Octs,
       "hwSecStatMonRtspSessions": hwSecStatMonRtspSessions,
       "hwSecStatMonRcvRtspPkts": hwSecStatMonRcvRtspPkts,
       "hwSecStatMonRcvRtspOcts": hwSecStatMonRcvRtspOcts,
       "hwSecStatMonJavaAtckNum": hwSecStatMonJavaAtckNum,
       "hwSecStatClearGlobalAppInfo": hwSecStatClearGlobalAppInfo,
       "hwSecStatMonitorGlobalDrop": hwSecStatMonitorGlobalDrop,
       "hwSecStatNoSessTblPkts": hwSecStatNoSessTblPkts,
       "hwSecStatNoSessTblOcts": hwSecStatNoSessTblOcts,
       "hwSecStatSeqErrPkts": hwSecStatSeqErrPkts,
       "hwSecStatSeqErrOcts": hwSecStatSeqErrOcts,
       "hwSecStatAclDenyNonIcmpPkts": hwSecStatAclDenyNonIcmpPkts,
       "hwSecStatAclDenyNonIcmpOcts": hwSecStatAclDenyNonIcmpOcts,
       "hwSecStatAclDenyIcmpPkts": hwSecStatAclDenyIcmpPkts,
       "hwSecStatAclDenyIcmpOcts": hwSecStatAclDenyIcmpOcts,
       "hwSecStatBlsDenyPkts": hwSecStatBlsDenyPkts,
       "hwSecStatBlsDenyOcts": hwSecStatBlsDenyOcts,
       "hwSecStatIcmpFloodDropPkts": hwSecStatIcmpFloodDropPkts,
       "hwSecStatIcmpFloodDropOcts": hwSecStatIcmpFloodDropOcts,
       "hwSecStatUdpFloodDropPkts": hwSecStatUdpFloodDropPkts,
       "hwSecStatUdpFloodDropOcts": hwSecStatUdpFloodDropOcts,
       "hwSecStatAlgDropPkts": hwSecStatAlgDropPkts,
       "hwSecStatAlgDropOcts": hwSecStatAlgDropOcts,
       "hwSecStatIPVerErrDropPkts": hwSecStatIPVerErrDropPkts,
       "hwSecStatIpCrcDropPkts": hwSecStatIpCrcDropPkts,
       "hwSecStatIpTTLDropPkts": hwSecStatIpTTLDropPkts,
       "hwSecStatProtoErrDropPkts": hwSecStatProtoErrDropPkts,
       "hwSecStatClearGlobalDropInfo": hwSecStatClearGlobalDropInfo,
       "hwSecStatConformance": hwSecStatConformance,
       "hwSecStatCompliance": hwSecStatCompliance,
       "hwSecStatMibGroups": hwSecStatMibGroups,
       "hwSecStatGlobalCfgGroup": hwSecStatGlobalCfgGroup,
       "hwSecStatGlobalMonitorGroup": hwSecStatGlobalMonitorGroup}
)
