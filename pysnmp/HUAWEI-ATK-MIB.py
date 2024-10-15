# SNMP MIB module (HUAWEI-ATK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ATK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:49 2024
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

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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

hwATKComm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwATK_ObjectIdentity = ObjectIdentity
hwATK = _HwATK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10)
)
_HwAtkGlobalMibObjects_ObjectIdentity = ObjectIdentity
hwAtkGlobalMibObjects = _HwAtkGlobalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1)
)
_HwAtkIpSpoofingSw_Type = TruthValue
_HwAtkIpSpoofingSw_Object = MibScalar
hwAtkIpSpoofingSw = _HwAtkIpSpoofingSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 1),
    _HwAtkIpSpoofingSw_Type()
)
hwAtkIpSpoofingSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIpSpoofingSw.setStatus("current")
_HwAtkLandSw_Type = TruthValue
_HwAtkLandSw_Object = MibScalar
hwAtkLandSw = _HwAtkLandSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 2),
    _HwAtkLandSw_Type()
)
hwAtkLandSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkLandSw.setStatus("current")
_HwAtkSmurfSw_Type = TruthValue
_HwAtkSmurfSw_Object = MibScalar
hwAtkSmurfSw = _HwAtkSmurfSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 3),
    _HwAtkSmurfSw_Type()
)
hwAtkSmurfSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkSmurfSw.setStatus("current")
_HwAtkFraggleSw_Type = TruthValue
_HwAtkFraggleSw_Object = MibScalar
hwAtkFraggleSw = _HwAtkFraggleSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 4),
    _HwAtkFraggleSw_Type()
)
hwAtkFraggleSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkFraggleSw.setStatus("current")
_HwAtkWinNukeSw_Type = TruthValue
_HwAtkWinNukeSw_Object = MibScalar
hwAtkWinNukeSw = _HwAtkWinNukeSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 5),
    _HwAtkWinNukeSw_Type()
)
hwAtkWinNukeSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkWinNukeSw.setStatus("current")
_HwAtkIcmpRedirectSw_Type = TruthValue
_HwAtkIcmpRedirectSw_Object = MibScalar
hwAtkIcmpRedirectSw = _HwAtkIcmpRedirectSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 6),
    _HwAtkIcmpRedirectSw_Type()
)
hwAtkIcmpRedirectSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIcmpRedirectSw.setStatus("current")
_HwAtkIcmpUnReachSw_Type = TruthValue
_HwAtkIcmpUnReachSw_Object = MibScalar
hwAtkIcmpUnReachSw = _HwAtkIcmpUnReachSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 7),
    _HwAtkIcmpUnReachSw_Type()
)
hwAtkIcmpUnReachSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIcmpUnReachSw.setStatus("current")
_HwAtkSourceRouteSw_Type = TruthValue
_HwAtkSourceRouteSw_Object = MibScalar
hwAtkSourceRouteSw = _HwAtkSourceRouteSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 8),
    _HwAtkSourceRouteSw_Type()
)
hwAtkSourceRouteSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkSourceRouteSw.setStatus("current")


class _HwAtkRouteRecordSw_Type(TruthValue):
    """Custom type hwAtkRouteRecordSw based on TruthValue"""
    defaultValue = 0


_HwAtkRouteRecordSw_Object = MibScalar
hwAtkRouteRecordSw = _HwAtkRouteRecordSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 9),
    _HwAtkRouteRecordSw_Type()
)
hwAtkRouteRecordSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkRouteRecordSw.setStatus("current")


class _HwAtkTracertSw_Type(TruthValue):
    """Custom type hwAtkTracertSw based on TruthValue"""
    defaultValue = 0


_HwAtkTracertSw_Object = MibScalar
hwAtkTracertSw = _HwAtkTracertSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 10),
    _HwAtkTracertSw_Type()
)
hwAtkTracertSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkTracertSw.setStatus("current")


class _HwAtkTcpFlagSw_Type(TruthValue):
    """Custom type hwAtkTcpFlagSw based on TruthValue"""
    defaultValue = 0


_HwAtkTcpFlagSw_Object = MibScalar
hwAtkTcpFlagSw = _HwAtkTcpFlagSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 11),
    _HwAtkTcpFlagSw_Type()
)
hwAtkTcpFlagSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkTcpFlagSw.setStatus("current")


class _HwAtkPingOfDeathSw_Type(TruthValue):
    """Custom type hwAtkPingOfDeathSw based on TruthValue"""
    defaultValue = 0


_HwAtkPingOfDeathSw_Object = MibScalar
hwAtkPingOfDeathSw = _HwAtkPingOfDeathSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 12),
    _HwAtkPingOfDeathSw_Type()
)
hwAtkPingOfDeathSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkPingOfDeathSw.setStatus("current")


class _HwAtkTeardropSw_Type(TruthValue):
    """Custom type hwAtkTeardropSw based on TruthValue"""
    defaultValue = 0


_HwAtkTeardropSw_Object = MibScalar
hwAtkTeardropSw = _HwAtkTeardropSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 13),
    _HwAtkTeardropSw_Type()
)
hwAtkTeardropSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkTeardropSw.setStatus("current")


class _HwAtkFragFlagSw_Type(TruthValue):
    """Custom type hwAtkFragFlagSw based on TruthValue"""
    defaultValue = 0


_HwAtkFragFlagSw_Object = MibScalar
hwAtkFragFlagSw = _HwAtkFragFlagSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 14),
    _HwAtkFragFlagSw_Type()
)
hwAtkFragFlagSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkFragFlagSw.setStatus("current")


class _HwAtkIPSweepSw_Type(TruthValue):
    """Custom type hwAtkIPSweepSw based on TruthValue"""
    defaultValue = 0


_HwAtkIPSweepSw_Object = MibScalar
hwAtkIPSweepSw = _HwAtkIPSweepSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 15),
    _HwAtkIPSweepSw_Type()
)
hwAtkIPSweepSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIPSweepSw.setStatus("current")


class _HwAtkIpSweepSpeed_Type(Integer32):
    """Custom type hwAtkIpSweepSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwAtkIpSweepSpeed_Type.__name__ = "Integer32"
_HwAtkIpSweepSpeed_Object = MibScalar
hwAtkIpSweepSpeed = _HwAtkIpSweepSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 16),
    _HwAtkIpSweepSpeed_Type()
)
hwAtkIpSweepSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIpSweepSpeed.setStatus("current")


class _HwAtkIPSweepBlsTime_Type(Integer32):
    """Custom type hwAtkIPSweepBlsTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwAtkIPSweepBlsTime_Type.__name__ = "Integer32"
_HwAtkIPSweepBlsTime_Object = MibScalar
hwAtkIPSweepBlsTime = _HwAtkIPSweepBlsTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 17),
    _HwAtkIPSweepBlsTime_Type()
)
hwAtkIPSweepBlsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIPSweepBlsTime.setStatus("current")


class _HwAtkPortScanSw_Type(TruthValue):
    """Custom type hwAtkPortScanSw based on TruthValue"""
    defaultValue = 0


_HwAtkPortScanSw_Object = MibScalar
hwAtkPortScanSw = _HwAtkPortScanSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 18),
    _HwAtkPortScanSw_Type()
)
hwAtkPortScanSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkPortScanSw.setStatus("current")


class _HwAtkPortScanSpeed_Type(Integer32):
    """Custom type hwAtkPortScanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwAtkPortScanSpeed_Type.__name__ = "Integer32"
_HwAtkPortScanSpeed_Object = MibScalar
hwAtkPortScanSpeed = _HwAtkPortScanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 19),
    _HwAtkPortScanSpeed_Type()
)
hwAtkPortScanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkPortScanSpeed.setStatus("current")


class _HwAtkPortScanBlsTime_Type(Integer32):
    """Custom type hwAtkPortScanBlsTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwAtkPortScanBlsTime_Type.__name__ = "Integer32"
_HwAtkPortScanBlsTime_Object = MibScalar
hwAtkPortScanBlsTime = _HwAtkPortScanBlsTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 20),
    _HwAtkPortScanBlsTime_Type()
)
hwAtkPortScanBlsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkPortScanBlsTime.setStatus("current")


class _HwAtkLargeIcmpSw_Type(TruthValue):
    """Custom type hwAtkLargeIcmpSw based on TruthValue"""
    defaultValue = 0


_HwAtkLargeIcmpSw_Object = MibScalar
hwAtkLargeIcmpSw = _HwAtkLargeIcmpSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 21),
    _HwAtkLargeIcmpSw_Type()
)
hwAtkLargeIcmpSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkLargeIcmpSw.setStatus("current")


class _HwAtkIcmpLength_Type(Integer32):
    """Custom type hwAtkIcmpLength based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 65535),
    )


_HwAtkIcmpLength_Type.__name__ = "Integer32"
_HwAtkIcmpLength_Object = MibScalar
hwAtkIcmpLength = _HwAtkIcmpLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 22),
    _HwAtkIcmpLength_Type()
)
hwAtkIcmpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIcmpLength.setStatus("current")


class _HwAtkSynFloodSw_Type(TruthValue):
    """Custom type hwAtkSynFloodSw based on TruthValue"""


_HwAtkSynFloodSw_Object = MibScalar
hwAtkSynFloodSw = _HwAtkSynFloodSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 23),
    _HwAtkSynFloodSw_Type()
)
hwAtkSynFloodSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkSynFloodSw.setStatus("current")


class _HwAtkUdpFloodSw_Type(TruthValue):
    """Custom type hwAtkUdpFloodSw based on TruthValue"""


_HwAtkUdpFloodSw_Object = MibScalar
hwAtkUdpFloodSw = _HwAtkUdpFloodSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 24),
    _HwAtkUdpFloodSw_Type()
)
hwAtkUdpFloodSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkUdpFloodSw.setStatus("current")


class _HwAtkIcmpFloodSw_Type(TruthValue):
    """Custom type hwAtkIcmpFloodSw based on TruthValue"""


_HwAtkIcmpFloodSw_Object = MibScalar
hwAtkIcmpFloodSw = _HwAtkIcmpFloodSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 1, 25),
    _HwAtkIcmpFloodSw_Type()
)
hwAtkIcmpFloodSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAtkIcmpFloodSw.setStatus("current")
_HwAtkIPMibObjects_ObjectIdentity = ObjectIdentity
hwAtkIPMibObjects = _HwAtkIPMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2)
)
_HwAtkSynFloodIPTable_Object = MibTable
hwAtkSynFloodIPTable = _HwAtkSynFloodIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwAtkSynFloodIPTable.setStatus("current")
_HwAtkSynFloodIPEntry_Object = MibTableRow
hwAtkSynFloodIPEntry = _HwAtkSynFloodIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1)
)
hwAtkSynFloodIPEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-MIB", "hwAtkSynFloodIP"),
)
if mibBuilder.loadTexts:
    hwAtkSynFloodIPEntry.setStatus("current")
_HwAtkSynFloodIP_Type = IpAddress
_HwAtkSynFloodIP_Object = MibTableColumn
hwAtkSynFloodIP = _HwAtkSynFloodIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 1),
    _HwAtkSynFloodIP_Type()
)
hwAtkSynFloodIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkSynFloodIP.setStatus("current")


class _HwAtkIPSynFloodSynSpeed_Type(Integer32):
    """Custom type hwAtkIPSynFloodSynSpeed based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkIPSynFloodSynSpeed_Type.__name__ = "Integer32"
_HwAtkIPSynFloodSynSpeed_Object = MibTableColumn
hwAtkIPSynFloodSynSpeed = _HwAtkIPSynFloodSynSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 2),
    _HwAtkIPSynFloodSynSpeed_Type()
)
hwAtkIPSynFloodSynSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPSynFloodSynSpeed.setStatus("current")


class _HwAtkIPSynFloodHalfMax_Type(Integer32):
    """Custom type hwAtkIPSynFloodHalfMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwAtkIPSynFloodHalfMax_Type.__name__ = "Integer32"
_HwAtkIPSynFloodHalfMax_Object = MibTableColumn
hwAtkIPSynFloodHalfMax = _HwAtkIPSynFloodHalfMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 3),
    _HwAtkIPSynFloodHalfMax_Type()
)
hwAtkIPSynFloodHalfMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPSynFloodHalfMax.setStatus("current")


class _HwAtkIPSynFloodHalfAge_Type(Integer32):
    """Custom type hwAtkIPSynFloodHalfAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAtkIPSynFloodHalfAge_Type.__name__ = "Integer32"
_HwAtkIPSynFloodHalfAge_Object = MibTableColumn
hwAtkIPSynFloodHalfAge = _HwAtkIPSynFloodHalfAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 4),
    _HwAtkIPSynFloodHalfAge_Type()
)
hwAtkIPSynFloodHalfAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPSynFloodHalfAge.setStatus("current")


class _HwAtkIPSynFloodProxy_Type(Integer32):
    """Custom type hwAtkIPSynFloodProxy based on Integer32"""
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
        *(("auto", 1),
          ("off", 3),
          ("on", 2))
    )


_HwAtkIPSynFloodProxy_Type.__name__ = "Integer32"
_HwAtkIPSynFloodProxy_Object = MibTableColumn
hwAtkIPSynFloodProxy = _HwAtkIPSynFloodProxy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 5),
    _HwAtkIPSynFloodProxy_Type()
)
hwAtkIPSynFloodProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPSynFloodProxy.setStatus("current")
_HwAtkIPSynFloodStatus_Type = RowStatus
_HwAtkIPSynFloodStatus_Object = MibTableColumn
hwAtkIPSynFloodStatus = _HwAtkIPSynFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 1, 1, 6),
    _HwAtkIPSynFloodStatus_Type()
)
hwAtkIPSynFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPSynFloodStatus.setStatus("current")
_HwAtkUdpFloodIPTable_Object = MibTable
hwAtkUdpFloodIPTable = _HwAtkUdpFloodIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwAtkUdpFloodIPTable.setStatus("current")
_HwAtkUdpFloodIPEntry_Object = MibTableRow
hwAtkUdpFloodIPEntry = _HwAtkUdpFloodIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 2, 1)
)
hwAtkUdpFloodIPEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-MIB", "hwAtkUdpFloodIP"),
)
if mibBuilder.loadTexts:
    hwAtkUdpFloodIPEntry.setStatus("current")
_HwAtkUdpFloodIP_Type = IpAddress
_HwAtkUdpFloodIP_Object = MibTableColumn
hwAtkUdpFloodIP = _HwAtkUdpFloodIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 2, 1, 1),
    _HwAtkUdpFloodIP_Type()
)
hwAtkUdpFloodIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkUdpFloodIP.setStatus("current")


class _HwAtkIPUdpFloodSpeed_Type(Integer32):
    """Custom type hwAtkIPUdpFloodSpeed based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkIPUdpFloodSpeed_Type.__name__ = "Integer32"
_HwAtkIPUdpFloodSpeed_Object = MibTableColumn
hwAtkIPUdpFloodSpeed = _HwAtkIPUdpFloodSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 2, 1, 2),
    _HwAtkIPUdpFloodSpeed_Type()
)
hwAtkIPUdpFloodSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPUdpFloodSpeed.setStatus("current")
_HwAtkIPUdpFloodStatus_Type = RowStatus
_HwAtkIPUdpFloodStatus_Object = MibTableColumn
hwAtkIPUdpFloodStatus = _HwAtkIPUdpFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 2, 1, 3),
    _HwAtkIPUdpFloodStatus_Type()
)
hwAtkIPUdpFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPUdpFloodStatus.setStatus("current")
_HwAtkIcmpFloodIPTable_Object = MibTable
hwAtkIcmpFloodIPTable = _HwAtkIcmpFloodIPTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwAtkIcmpFloodIPTable.setStatus("current")
_HwAtkIcmpFloodIPEntry_Object = MibTableRow
hwAtkIcmpFloodIPEntry = _HwAtkIcmpFloodIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 3, 1)
)
hwAtkIcmpFloodIPEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-MIB", "hwAtkIcmpFloodIP"),
)
if mibBuilder.loadTexts:
    hwAtkIcmpFloodIPEntry.setStatus("current")
_HwAtkIcmpFloodIP_Type = IpAddress
_HwAtkIcmpFloodIP_Object = MibTableColumn
hwAtkIcmpFloodIP = _HwAtkIcmpFloodIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 3, 1, 1),
    _HwAtkIcmpFloodIP_Type()
)
hwAtkIcmpFloodIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkIcmpFloodIP.setStatus("current")


class _HwAtkIPIcmpFloodSpeed_Type(Integer32):
    """Custom type hwAtkIPIcmpFloodSpeed based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkIPIcmpFloodSpeed_Type.__name__ = "Integer32"
_HwAtkIPIcmpFloodSpeed_Object = MibTableColumn
hwAtkIPIcmpFloodSpeed = _HwAtkIPIcmpFloodSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 3, 1, 2),
    _HwAtkIPIcmpFloodSpeed_Type()
)
hwAtkIPIcmpFloodSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPIcmpFloodSpeed.setStatus("current")
_HwAtkIPIcmpFloodStatus_Type = RowStatus
_HwAtkIPIcmpFloodStatus_Object = MibTableColumn
hwAtkIPIcmpFloodStatus = _HwAtkIPIcmpFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 2, 3, 1, 3),
    _HwAtkIPIcmpFloodStatus_Type()
)
hwAtkIPIcmpFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkIPIcmpFloodStatus.setStatus("current")
_HwAtkCommConformance_ObjectIdentity = ObjectIdentity
hwAtkCommConformance = _HwAtkCommConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3)
)
_HwAtkCommCompliance_ObjectIdentity = ObjectIdentity
hwAtkCommCompliance = _HwAtkCommCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 1)
)
_HwAtkCommMibGroups_ObjectIdentity = ObjectIdentity
hwAtkCommMibGroups = _HwAtkCommMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 2)
)

# Managed Objects groups

hwAtkGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 2, 1)
)
hwAtkGlobalCfgGroup.setObjects(
      *(("HUAWEI-ATK-MIB", "hwAtkIpSpoofingSw"),
        ("HUAWEI-ATK-MIB", "hwAtkLandSw"),
        ("HUAWEI-ATK-MIB", "hwAtkSmurfSw"),
        ("HUAWEI-ATK-MIB", "hwAtkFraggleSw"),
        ("HUAWEI-ATK-MIB", "hwAtkWinNukeSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIcmpRedirectSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIcmpUnReachSw"),
        ("HUAWEI-ATK-MIB", "hwAtkSourceRouteSw"),
        ("HUAWEI-ATK-MIB", "hwAtkRouteRecordSw"),
        ("HUAWEI-ATK-MIB", "hwAtkTracertSw"),
        ("HUAWEI-ATK-MIB", "hwAtkTcpFlagSw"),
        ("HUAWEI-ATK-MIB", "hwAtkPingOfDeathSw"),
        ("HUAWEI-ATK-MIB", "hwAtkTeardropSw"),
        ("HUAWEI-ATK-MIB", "hwAtkFragFlagSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSweepSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIpSweepSpeed"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSweepBlsTime"),
        ("HUAWEI-ATK-MIB", "hwAtkPortScanSw"),
        ("HUAWEI-ATK-MIB", "hwAtkPortScanSpeed"),
        ("HUAWEI-ATK-MIB", "hwAtkPortScanBlsTime"),
        ("HUAWEI-ATK-MIB", "hwAtkLargeIcmpSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIcmpLength"),
        ("HUAWEI-ATK-MIB", "hwAtkSynFloodSw"),
        ("HUAWEI-ATK-MIB", "hwAtkUdpFloodSw"),
        ("HUAWEI-ATK-MIB", "hwAtkIcmpFloodSw"))
)
if mibBuilder.loadTexts:
    hwAtkGlobalCfgGroup.setStatus("current")

hwAtkCommSynFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 2, 2)
)
hwAtkCommSynFloodGroup.setObjects(
      *(("HUAWEI-ATK-MIB", "hwAtkIPSynFloodSynSpeed"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSynFloodHalfMax"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSynFloodHalfAge"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSynFloodProxy"),
        ("HUAWEI-ATK-MIB", "hwAtkIPSynFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkCommSynFloodGroup.setStatus("current")

hwAtkCommUdpFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 2, 3)
)
hwAtkCommUdpFloodGroup.setObjects(
      *(("HUAWEI-ATK-MIB", "hwAtkIPUdpFloodSpeed"),
        ("HUAWEI-ATK-MIB", "hwAtkIPUdpFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkCommUdpFloodGroup.setStatus("current")

hwAtkCommIcmpFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 1, 3, 2, 4)
)
hwAtkCommIcmpFloodGroup.setObjects(
      *(("HUAWEI-ATK-MIB", "hwAtkIPIcmpFloodSpeed"),
        ("HUAWEI-ATK-MIB", "hwAtkIPIcmpFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkCommIcmpFloodGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ATK-MIB",
    **{"hwATK": hwATK,
       "hwATKComm": hwATKComm,
       "hwAtkGlobalMibObjects": hwAtkGlobalMibObjects,
       "hwAtkIpSpoofingSw": hwAtkIpSpoofingSw,
       "hwAtkLandSw": hwAtkLandSw,
       "hwAtkSmurfSw": hwAtkSmurfSw,
       "hwAtkFraggleSw": hwAtkFraggleSw,
       "hwAtkWinNukeSw": hwAtkWinNukeSw,
       "hwAtkIcmpRedirectSw": hwAtkIcmpRedirectSw,
       "hwAtkIcmpUnReachSw": hwAtkIcmpUnReachSw,
       "hwAtkSourceRouteSw": hwAtkSourceRouteSw,
       "hwAtkRouteRecordSw": hwAtkRouteRecordSw,
       "hwAtkTracertSw": hwAtkTracertSw,
       "hwAtkTcpFlagSw": hwAtkTcpFlagSw,
       "hwAtkPingOfDeathSw": hwAtkPingOfDeathSw,
       "hwAtkTeardropSw": hwAtkTeardropSw,
       "hwAtkFragFlagSw": hwAtkFragFlagSw,
       "hwAtkIPSweepSw": hwAtkIPSweepSw,
       "hwAtkIpSweepSpeed": hwAtkIpSweepSpeed,
       "hwAtkIPSweepBlsTime": hwAtkIPSweepBlsTime,
       "hwAtkPortScanSw": hwAtkPortScanSw,
       "hwAtkPortScanSpeed": hwAtkPortScanSpeed,
       "hwAtkPortScanBlsTime": hwAtkPortScanBlsTime,
       "hwAtkLargeIcmpSw": hwAtkLargeIcmpSw,
       "hwAtkIcmpLength": hwAtkIcmpLength,
       "hwAtkSynFloodSw": hwAtkSynFloodSw,
       "hwAtkUdpFloodSw": hwAtkUdpFloodSw,
       "hwAtkIcmpFloodSw": hwAtkIcmpFloodSw,
       "hwAtkIPMibObjects": hwAtkIPMibObjects,
       "hwAtkSynFloodIPTable": hwAtkSynFloodIPTable,
       "hwAtkSynFloodIPEntry": hwAtkSynFloodIPEntry,
       "hwAtkSynFloodIP": hwAtkSynFloodIP,
       "hwAtkIPSynFloodSynSpeed": hwAtkIPSynFloodSynSpeed,
       "hwAtkIPSynFloodHalfMax": hwAtkIPSynFloodHalfMax,
       "hwAtkIPSynFloodHalfAge": hwAtkIPSynFloodHalfAge,
       "hwAtkIPSynFloodProxy": hwAtkIPSynFloodProxy,
       "hwAtkIPSynFloodStatus": hwAtkIPSynFloodStatus,
       "hwAtkUdpFloodIPTable": hwAtkUdpFloodIPTable,
       "hwAtkUdpFloodIPEntry": hwAtkUdpFloodIPEntry,
       "hwAtkUdpFloodIP": hwAtkUdpFloodIP,
       "hwAtkIPUdpFloodSpeed": hwAtkIPUdpFloodSpeed,
       "hwAtkIPUdpFloodStatus": hwAtkIPUdpFloodStatus,
       "hwAtkIcmpFloodIPTable": hwAtkIcmpFloodIPTable,
       "hwAtkIcmpFloodIPEntry": hwAtkIcmpFloodIPEntry,
       "hwAtkIcmpFloodIP": hwAtkIcmpFloodIP,
       "hwAtkIPIcmpFloodSpeed": hwAtkIPIcmpFloodSpeed,
       "hwAtkIPIcmpFloodStatus": hwAtkIPIcmpFloodStatus,
       "hwAtkCommConformance": hwAtkCommConformance,
       "hwAtkCommCompliance": hwAtkCommCompliance,
       "hwAtkCommMibGroups": hwAtkCommMibGroups,
       "hwAtkGlobalCfgGroup": hwAtkGlobalCfgGroup,
       "hwAtkCommSynFloodGroup": hwAtkCommSynFloodGroup,
       "hwAtkCommUdpFloodGroup": hwAtkCommUdpFloodGroup,
       "hwAtkCommIcmpFloodGroup": hwAtkCommIcmpFloodGroup}
)
