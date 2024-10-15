# SNMP MIB module (HUAWEI-MUSA-MA5100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MUSA-MA5100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:51 2024
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

(musa,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "musa")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMa5100Mib_ObjectIdentity = ObjectIdentity
hwMa5100Mib = _HwMa5100Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5)
)
_HwMusaSysMib_ObjectIdentity = ObjectIdentity
hwMusaSysMib = _HwMusaSysMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1)
)
_HwMusaDevice_ObjectIdentity = ObjectIdentity
hwMusaDevice = _HwMusaDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1)
)
_HwMusaSysDate_Type = DisplayString
_HwMusaSysDate_Object = MibScalar
hwMusaSysDate = _HwMusaSysDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 9),
    _HwMusaSysDate_Type()
)
hwMusaSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSysDate.setStatus("mandatory")
_HwMusaSysTime_Type = DisplayString
_HwMusaSysTime_Object = MibScalar
hwMusaSysTime = _HwMusaSysTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 10),
    _HwMusaSysTime_Type()
)
hwMusaSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSysTime.setStatus("mandatory")
_HwMusaSysCpuRatio_Type = Integer32
_HwMusaSysCpuRatio_Object = MibScalar
hwMusaSysCpuRatio = _HwMusaSysCpuRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 11),
    _HwMusaSysCpuRatio_Type()
)
hwMusaSysCpuRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSysCpuRatio.setStatus("mandatory")
_HwMusaHostVersion_Type = DisplayString
_HwMusaHostVersion_Object = MibScalar
hwMusaHostVersion = _HwMusaHostVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 12),
    _HwMusaHostVersion_Type()
)
hwMusaHostVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaHostVersion.setStatus("mandatory")
_HwMusaResetSys_Type = Integer32
_HwMusaResetSys_Object = MibScalar
hwMusaResetSys = _HwMusaResetSys_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 13),
    _HwMusaResetSys_Type()
)
hwMusaResetSys.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaResetSys.setStatus("mandatory")
_HwMusaIpAddr_Type = IpAddress
_HwMusaIpAddr_Object = MibScalar
hwMusaIpAddr = _HwMusaIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 14),
    _HwMusaIpAddr_Type()
)
hwMusaIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaIpAddr.setStatus("mandatory")
_HwMusaIpMask_Type = IpAddress
_HwMusaIpMask_Object = MibScalar
hwMusaIpMask = _HwMusaIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 15),
    _HwMusaIpMask_Type()
)
hwMusaIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaIpMask.setStatus("mandatory")
_HwMusaGatewayIpAddr_Type = IpAddress
_HwMusaGatewayIpAddr_Object = MibScalar
hwMusaGatewayIpAddr = _HwMusaGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 16),
    _HwMusaGatewayIpAddr_Type()
)
hwMusaGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaGatewayIpAddr.setStatus("mandatory")
_HwMusaMacAddr_Type = DisplayString
_HwMusaMacAddr_Object = MibScalar
hwMusaMacAddr = _HwMusaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 17),
    _HwMusaMacAddr_Type()
)
hwMusaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaMacAddr.setStatus("mandatory")
_HwMusaIpAddrPermitTable_Object = MibTable
hwMusaIpAddrPermitTable = _HwMusaIpAddrPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hwMusaIpAddrPermitTable.setStatus("mandatory")
_HwMusaIpAddrPermitEntry_Object = MibTableRow
hwMusaIpAddrPermitEntry = _HwMusaIpAddrPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1)
)
hwMusaIpAddrPermitEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaIpPermitTableId"),
)
if mibBuilder.loadTexts:
    hwMusaIpAddrPermitEntry.setStatus("mandatory")
_HwMusaIpPermitTableId_Type = Integer32
_HwMusaIpPermitTableId_Object = MibTableColumn
hwMusaIpPermitTableId = _HwMusaIpPermitTableId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1, 1),
    _HwMusaIpPermitTableId_Type()
)
hwMusaIpPermitTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaIpPermitTableId.setStatus("mandatory")


class _HwMusaIpAddrPermitOper_Type(Integer32):
    """Custom type hwMusaIpAddrPermitOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1),
          ("modify", 2),
          ("query", 3))
    )


_HwMusaIpAddrPermitOper_Type.__name__ = "Integer32"
_HwMusaIpAddrPermitOper_Object = MibTableColumn
hwMusaIpAddrPermitOper = _HwMusaIpAddrPermitOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1, 2),
    _HwMusaIpAddrPermitOper_Type()
)
hwMusaIpAddrPermitOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaIpAddrPermitOper.setStatus("mandatory")
_HwMusaPermitBeginIp_Type = IpAddress
_HwMusaPermitBeginIp_Object = MibTableColumn
hwMusaPermitBeginIp = _HwMusaPermitBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1, 3),
    _HwMusaPermitBeginIp_Type()
)
hwMusaPermitBeginIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaPermitBeginIp.setStatus("mandatory")
_HwMusaPermitEndIp_Type = IpAddress
_HwMusaPermitEndIp_Object = MibTableColumn
hwMusaPermitEndIp = _HwMusaPermitEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1, 4),
    _HwMusaPermitEndIp_Type()
)
hwMusaPermitEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaPermitEndIp.setStatus("mandatory")
_HwMusaPermitIpMask_Type = IpAddress
_HwMusaPermitIpMask_Object = MibTableColumn
hwMusaPermitIpMask = _HwMusaPermitIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 18, 1, 5),
    _HwMusaPermitIpMask_Type()
)
hwMusaPermitIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaPermitIpMask.setStatus("mandatory")
_HwMusaIpAddrRejectTable_Object = MibTable
hwMusaIpAddrRejectTable = _HwMusaIpAddrRejectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hwMusaIpAddrRejectTable.setStatus("mandatory")
_HwMusaIpAddrRejectEntry_Object = MibTableRow
hwMusaIpAddrRejectEntry = _HwMusaIpAddrRejectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1)
)
hwMusaIpAddrRejectEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaIpRejectTableId"),
)
if mibBuilder.loadTexts:
    hwMusaIpAddrRejectEntry.setStatus("mandatory")
_HwMusaIpRejectTableId_Type = Integer32
_HwMusaIpRejectTableId_Object = MibTableColumn
hwMusaIpRejectTableId = _HwMusaIpRejectTableId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1, 1),
    _HwMusaIpRejectTableId_Type()
)
hwMusaIpRejectTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaIpRejectTableId.setStatus("mandatory")


class _HwMusaIpAddrRejectOper_Type(Integer32):
    """Custom type hwMusaIpAddrRejectOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1),
          ("modify", 2),
          ("query", 3))
    )


_HwMusaIpAddrRejectOper_Type.__name__ = "Integer32"
_HwMusaIpAddrRejectOper_Object = MibTableColumn
hwMusaIpAddrRejectOper = _HwMusaIpAddrRejectOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1, 2),
    _HwMusaIpAddrRejectOper_Type()
)
hwMusaIpAddrRejectOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaIpAddrRejectOper.setStatus("mandatory")
_HwMusaRejectBeginIp_Type = IpAddress
_HwMusaRejectBeginIp_Object = MibTableColumn
hwMusaRejectBeginIp = _HwMusaRejectBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1, 3),
    _HwMusaRejectBeginIp_Type()
)
hwMusaRejectBeginIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaRejectBeginIp.setStatus("mandatory")
_HwMusaRejectEndIp_Type = IpAddress
_HwMusaRejectEndIp_Object = MibTableColumn
hwMusaRejectEndIp = _HwMusaRejectEndIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1, 4),
    _HwMusaRejectEndIp_Type()
)
hwMusaRejectEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaRejectEndIp.setStatus("mandatory")
_HwMusaRejectIpMask_Type = IpAddress
_HwMusaRejectIpMask_Object = MibTableColumn
hwMusaRejectIpMask = _HwMusaRejectIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 19, 1, 5),
    _HwMusaRejectIpMask_Type()
)
hwMusaRejectIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaRejectIpMask.setStatus("mandatory")
_HwMusaAtmIpAddr_Type = IpAddress
_HwMusaAtmIpAddr_Object = MibScalar
hwMusaAtmIpAddr = _HwMusaAtmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 20),
    _HwMusaAtmIpAddr_Type()
)
hwMusaAtmIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAtmIpAddr.setStatus("mandatory")
_HwMusaAtmIpMask_Type = IpAddress
_HwMusaAtmIpMask_Object = MibScalar
hwMusaAtmIpMask = _HwMusaAtmIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 21),
    _HwMusaAtmIpMask_Type()
)
hwMusaAtmIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAtmIpMask.setStatus("mandatory")
_HwMusaMtu_Type = Integer32
_HwMusaMtu_Object = MibScalar
hwMusaMtu = _HwMusaMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 22),
    _HwMusaMtu_Type()
)
hwMusaMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaMtu.setStatus("mandatory")
_HwMusaOpticConvergentRate_Type = Integer32
_HwMusaOpticConvergentRate_Object = MibScalar
hwMusaOpticConvergentRate = _HwMusaOpticConvergentRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 23),
    _HwMusaOpticConvergentRate_Type()
)
hwMusaOpticConvergentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaOpticConvergentRate.setStatus("mandatory")


class _HwMusaCellbusID_Type(Integer32):
    """Custom type hwMusaCellbusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ma5100", 1),
          ("ma5103", 2))
    )


_HwMusaCellbusID_Type.__name__ = "Integer32"
_HwMusaCellbusID_Object = MibScalar
hwMusaCellbusID = _HwMusaCellbusID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 24),
    _HwMusaCellbusID_Type()
)
hwMusaCellbusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCellbusID.setStatus("mandatory")


class _HwMusaResetSlaveMMX_Type(Integer32):
    """Custom type hwMusaResetSlaveMMX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loaddata", 1),
          ("noloaddata", 2))
    )


_HwMusaResetSlaveMMX_Type.__name__ = "Integer32"
_HwMusaResetSlaveMMX_Object = MibScalar
hwMusaResetSlaveMMX = _HwMusaResetSlaveMMX_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 25),
    _HwMusaResetSlaveMMX_Type()
)
hwMusaResetSlaveMMX.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaResetSlaveMMX.setStatus("mandatory")
_HwMusaBiosVersion_Type = Integer32
_HwMusaBiosVersion_Object = MibScalar
hwMusaBiosVersion = _HwMusaBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 26),
    _HwMusaBiosVersion_Type()
)
hwMusaBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaBiosVersion.setStatus("mandatory")


class _HwMusaEthernetFirewall_Type(Integer32):
    """Custom type hwMusaEthernetFirewall based on Integer32"""
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


_HwMusaEthernetFirewall_Type.__name__ = "Integer32"
_HwMusaEthernetFirewall_Object = MibScalar
hwMusaEthernetFirewall = _HwMusaEthernetFirewall_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 1, 27),
    _HwMusaEthernetFirewall_Type()
)
hwMusaEthernetFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaEthernetFirewall.setStatus("mandatory")
_HwMusaNmsPvcConfTable_Object = MibTable
hwMusaNmsPvcConfTable = _HwMusaNmsPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hwMusaNmsPvcConfTable.setStatus("mandatory")
_HwMusaNmsPvcConfEntry_Object = MibTableRow
hwMusaNmsPvcConfEntry = _HwMusaNmsPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1)
)
hwMusaNmsPvcConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaNmsPvcIndex"),
)
if mibBuilder.loadTexts:
    hwMusaNmsPvcConfEntry.setStatus("mandatory")
_HwMusaNmsPvcIndex_Type = Integer32
_HwMusaNmsPvcIndex_Object = MibTableColumn
hwMusaNmsPvcIndex = _HwMusaNmsPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 1),
    _HwMusaNmsPvcIndex_Type()
)
hwMusaNmsPvcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaNmsPvcIndex.setStatus("mandatory")
_HwMusaNmsRelayVpi_Type = Integer32
_HwMusaNmsRelayVpi_Object = MibTableColumn
hwMusaNmsRelayVpi = _HwMusaNmsRelayVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 2),
    _HwMusaNmsRelayVpi_Type()
)
hwMusaNmsRelayVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsRelayVpi.setStatus("mandatory")
_HwMusaNmsRelayVci_Type = Integer32
_HwMusaNmsRelayVci_Object = MibTableColumn
hwMusaNmsRelayVci = _HwMusaNmsRelayVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 3),
    _HwMusaNmsRelayVci_Type()
)
hwMusaNmsRelayVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsRelayVci.setStatus("mandatory")
_HwMusaNmsIp_Type = IpAddress
_HwMusaNmsIp_Object = MibTableColumn
hwMusaNmsIp = _HwMusaNmsIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 4),
    _HwMusaNmsIp_Type()
)
hwMusaNmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsIp.setStatus("mandatory")


class _HwMusaNmsPvcOper_Type(Integer32):
    """Custom type hwMusaNmsPvcOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaNmsPvcOper_Type.__name__ = "Integer32"
_HwMusaNmsPvcOper_Object = MibTableColumn
hwMusaNmsPvcOper = _HwMusaNmsPvcOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 6),
    _HwMusaNmsPvcOper_Type()
)
hwMusaNmsPvcOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsPvcOper.setStatus("mandatory")
_HwMusaNmsRxTraffic_Type = Integer32
_HwMusaNmsRxTraffic_Object = MibTableColumn
hwMusaNmsRxTraffic = _HwMusaNmsRxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 8),
    _HwMusaNmsRxTraffic_Type()
)
hwMusaNmsRxTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsRxTraffic.setStatus("mandatory")
_HwMusaNmsTxTraffic_Type = Integer32
_HwMusaNmsTxTraffic_Object = MibTableColumn
hwMusaNmsTxTraffic = _HwMusaNmsTxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 9),
    _HwMusaNmsTxTraffic_Type()
)
hwMusaNmsTxTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsTxTraffic.setStatus("mandatory")
_HwMusaNmsSarVci_Type = Integer32
_HwMusaNmsSarVci_Object = MibTableColumn
hwMusaNmsSarVci = _HwMusaNmsSarVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 10),
    _HwMusaNmsSarVci_Type()
)
hwMusaNmsSarVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsSarVci.setStatus("mandatory")


class _HwMusaNmsLLCVC_Type(Integer32):
    """Custom type hwMusaNmsLLCVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_HwMusaNmsLLCVC_Type.__name__ = "Integer32"
_HwMusaNmsLLCVC_Object = MibTableColumn
hwMusaNmsLLCVC = _HwMusaNmsLLCVC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 11),
    _HwMusaNmsLLCVC_Type()
)
hwMusaNmsLLCVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsLLCVC.setStatus("mandatory")


class _HwMusaNmsENCAP_Type(Integer32):
    """Custom type hwMusaNmsENCAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e1483B", 1),
          ("eipoa", 0))
    )


_HwMusaNmsENCAP_Type.__name__ = "Integer32"
_HwMusaNmsENCAP_Object = MibTableColumn
hwMusaNmsENCAP = _HwMusaNmsENCAP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 12),
    _HwMusaNmsENCAP_Type()
)
hwMusaNmsENCAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsENCAP.setStatus("mandatory")
_HwMusaNmsFrameId_Type = Integer32
_HwMusaNmsFrameId_Object = MibTableColumn
hwMusaNmsFrameId = _HwMusaNmsFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 14),
    _HwMusaNmsFrameId_Type()
)
hwMusaNmsFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsFrameId.setStatus("mandatory")
_HwMusaNmsSlotId_Type = Integer32
_HwMusaNmsSlotId_Object = MibTableColumn
hwMusaNmsSlotId = _HwMusaNmsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 15),
    _HwMusaNmsSlotId_Type()
)
hwMusaNmsSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsSlotId.setStatus("mandatory")
_HwMusaNmsPortVlanId_Type = Integer32
_HwMusaNmsPortVlanId_Object = MibTableColumn
hwMusaNmsPortVlanId = _HwMusaNmsPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 3, 1, 16),
    _HwMusaNmsPortVlanId_Type()
)
hwMusaNmsPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsPortVlanId.setStatus("mandatory")
_HwMusaNmsParaConfTable_Object = MibTable
hwMusaNmsParaConfTable = _HwMusaNmsParaConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5)
)
if mibBuilder.loadTexts:
    hwMusaNmsParaConfTable.setStatus("mandatory")
_HwMusaNmsParaConfEntry_Object = MibTableRow
hwMusaNmsParaConfEntry = _HwMusaNmsParaConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1)
)
hwMusaNmsParaConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaNmsID"),
)
if mibBuilder.loadTexts:
    hwMusaNmsParaConfEntry.setStatus("mandatory")


class _HwMusaNmsID_Type(Integer32):
    """Custom type hwMusaNmsID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMusaNmsID_Type.__name__ = "Integer32"
_HwMusaNmsID_Object = MibTableColumn
hwMusaNmsID = _HwMusaNmsID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 1),
    _HwMusaNmsID_Type()
)
hwMusaNmsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaNmsID.setStatus("mandatory")


class _HwMusaNmsOperState_Type(Integer32):
    """Custom type hwMusaNmsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("add", 0),
          ("deactive", 5),
          ("del", 1),
          ("modify", 2))
    )


_HwMusaNmsOperState_Type.__name__ = "Integer32"
_HwMusaNmsOperState_Object = MibTableColumn
hwMusaNmsOperState = _HwMusaNmsOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 2),
    _HwMusaNmsOperState_Type()
)
hwMusaNmsOperState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsOperState.setStatus("mandatory")
_HwMusaNmsName_Type = DisplayString
_HwMusaNmsName_Object = MibTableColumn
hwMusaNmsName = _HwMusaNmsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 3),
    _HwMusaNmsName_Type()
)
hwMusaNmsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsName.setStatus("mandatory")
_HwMusaNmsIpAddr_Type = IpAddress
_HwMusaNmsIpAddr_Object = MibTableColumn
hwMusaNmsIpAddr = _HwMusaNmsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 4),
    _HwMusaNmsIpAddr_Type()
)
hwMusaNmsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsIpAddr.setStatus("mandatory")
_HwMusaGetCommunity_Type = DisplayString
_HwMusaGetCommunity_Object = MibTableColumn
hwMusaGetCommunity = _HwMusaGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 5),
    _HwMusaGetCommunity_Type()
)
hwMusaGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaGetCommunity.setStatus("mandatory")
_HwMusaSetCommunity_Type = DisplayString
_HwMusaSetCommunity_Object = MibTableColumn
hwMusaSetCommunity = _HwMusaSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 6),
    _HwMusaSetCommunity_Type()
)
hwMusaSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSetCommunity.setStatus("mandatory")
_HwMusaTrapPort_Type = Integer32
_HwMusaTrapPort_Object = MibTableColumn
hwMusaTrapPort = _HwMusaTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 7),
    _HwMusaTrapPort_Type()
)
hwMusaTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaTrapPort.setStatus("mandatory")
_HwMusaGetSetPort_Type = Integer32
_HwMusaGetSetPort_Object = MibTableColumn
hwMusaGetSetPort = _HwMusaGetSetPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 8),
    _HwMusaGetSetPort_Type()
)
hwMusaGetSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaGetSetPort.setStatus("mandatory")


class _HwMusaNmsStatus_Type(Integer32):
    """Custom type hwMusaNmsStatus based on Integer32"""
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
        *(("active", 1),
          ("commfail", 3),
          ("deactive", 2),
          ("uninstall", 4))
    )


_HwMusaNmsStatus_Type.__name__ = "Integer32"
_HwMusaNmsStatus_Object = MibTableColumn
hwMusaNmsStatus = _HwMusaNmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 9),
    _HwMusaNmsStatus_Type()
)
hwMusaNmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaNmsStatus.setStatus("mandatory")


class _HwMusaNmsStyle_Type(Integer32):
    """Custom type hwMusaNmsStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bandin", 0),
          ("bandout", 1))
    )


_HwMusaNmsStyle_Type.__name__ = "Integer32"
_HwMusaNmsStyle_Object = MibTableColumn
hwMusaNmsStyle = _HwMusaNmsStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 5, 1, 10),
    _HwMusaNmsStyle_Type()
)
hwMusaNmsStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaNmsStyle.setStatus("mandatory")
_HwMusaSlotGroup_ObjectIdentity = ObjectIdentity
hwMusaSlotGroup = _HwMusaSlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6)
)
_HwMusaShelf_ObjectIdentity = ObjectIdentity
hwMusaShelf = _HwMusaShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1)
)
_HwMusaShelfNumber_Type = Integer32
_HwMusaShelfNumber_Object = MibScalar
hwMusaShelfNumber = _HwMusaShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 1),
    _HwMusaShelfNumber_Type()
)
hwMusaShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaShelfNumber.setStatus("mandatory")
_HwMusaShelfConfTable_Object = MibTable
hwMusaShelfConfTable = _HwMusaShelfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hwMusaShelfConfTable.setStatus("mandatory")
_HwMusaShelfConfEntry_Object = MibTableRow
hwMusaShelfConfEntry = _HwMusaShelfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2, 1)
)
hwMusaShelfConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaShelfIndex"),
)
if mibBuilder.loadTexts:
    hwMusaShelfConfEntry.setStatus("mandatory")
_HwMusaShelfIndex_Type = Integer32
_HwMusaShelfIndex_Object = MibTableColumn
hwMusaShelfIndex = _HwMusaShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2, 1, 1),
    _HwMusaShelfIndex_Type()
)
hwMusaShelfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaShelfIndex.setStatus("mandatory")


class _HwMusaShelfType_Type(Integer32):
    """Custom type hwMusaShelfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("other", 1))
    )


_HwMusaShelfType_Type.__name__ = "Integer32"
_HwMusaShelfType_Object = MibTableColumn
hwMusaShelfType = _HwMusaShelfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2, 1, 2),
    _HwMusaShelfType_Type()
)
hwMusaShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaShelfType.setStatus("mandatory")
_HwMusaShelfName_Type = DisplayString
_HwMusaShelfName_Object = MibTableColumn
hwMusaShelfName = _HwMusaShelfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2, 1, 3),
    _HwMusaShelfName_Type()
)
hwMusaShelfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaShelfName.setStatus("mandatory")


class _HwMusaFrameNumbers_Type(Integer32):
    """Custom type hwMusaFrameNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMusaFrameNumbers_Type.__name__ = "Integer32"
_HwMusaFrameNumbers_Object = MibTableColumn
hwMusaFrameNumbers = _HwMusaFrameNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 1, 2, 1, 4),
    _HwMusaFrameNumbers_Type()
)
hwMusaFrameNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameNumbers.setStatus("mandatory")
_HwMusaFrame_ObjectIdentity = ObjectIdentity
hwMusaFrame = _HwMusaFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2)
)
_HwMusaFrameNumber_Type = Integer32
_HwMusaFrameNumber_Object = MibScalar
hwMusaFrameNumber = _HwMusaFrameNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 1),
    _HwMusaFrameNumber_Type()
)
hwMusaFrameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameNumber.setStatus("mandatory")
_HwMusaFrameConfTable_Object = MibTable
hwMusaFrameConfTable = _HwMusaFrameConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwMusaFrameConfTable.setStatus("mandatory")
_HwMusaFrameConfEntry_Object = MibTableRow
hwMusaFrameConfEntry = _HwMusaFrameConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1)
)
hwMusaFrameConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaShelfIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
)
if mibBuilder.loadTexts:
    hwMusaFrameConfEntry.setStatus("mandatory")
_HwMusaFrameIndex_Type = Integer32
_HwMusaFrameIndex_Object = MibTableColumn
hwMusaFrameIndex = _HwMusaFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 1),
    _HwMusaFrameIndex_Type()
)
hwMusaFrameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaFrameIndex.setStatus("mandatory")


class _HwMusaFrameType_Type(Integer32):
    """Custom type hwMusaFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("other", 1))
    )


_HwMusaFrameType_Type.__name__ = "Integer32"
_HwMusaFrameType_Object = MibTableColumn
hwMusaFrameType = _HwMusaFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 2),
    _HwMusaFrameType_Type()
)
hwMusaFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameType.setStatus("mandatory")


class _HwMusaFrameName_Type(DisplayString):
    """Custom type hwMusaFrameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HwMusaFrameName_Type.__name__ = "DisplayString"
_HwMusaFrameName_Object = MibTableColumn
hwMusaFrameName = _HwMusaFrameName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 3),
    _HwMusaFrameName_Type()
)
hwMusaFrameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrameName.setStatus("mandatory")


class _HwMusaSlotNumbers_Type(Integer32):
    """Custom type hwMusaSlotNumbers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMusaSlotNumbers_Type.__name__ = "Integer32"
_HwMusaSlotNumbers_Object = MibTableColumn
hwMusaSlotNumbers = _HwMusaSlotNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 4),
    _HwMusaSlotNumbers_Type()
)
hwMusaSlotNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotNumbers.setStatus("mandatory")
_HwMusaFrameBandWidth_Type = Integer32
_HwMusaFrameBandWidth_Object = MibTableColumn
hwMusaFrameBandWidth = _HwMusaFrameBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 5),
    _HwMusaFrameBandWidth_Type()
)
hwMusaFrameBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameBandWidth.setStatus("mandatory")
_HwMusaFrameUsedBandWidth_Type = Integer32
_HwMusaFrameUsedBandWidth_Object = MibTableColumn
hwMusaFrameUsedBandWidth = _HwMusaFrameUsedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 2, 2, 1, 6),
    _HwMusaFrameUsedBandWidth_Type()
)
hwMusaFrameUsedBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrameUsedBandWidth.setStatus("mandatory")
_HwMusaSlot_ObjectIdentity = ObjectIdentity
hwMusaSlot = _HwMusaSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3)
)
_HwMusaSlotNumber_Type = Integer32
_HwMusaSlotNumber_Object = MibScalar
hwMusaSlotNumber = _HwMusaSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 1),
    _HwMusaSlotNumber_Type()
)
hwMusaSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotNumber.setStatus("mandatory")
_HwMusaSlotConfTable_Object = MibTable
hwMusaSlotConfTable = _HwMusaSlotConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    hwMusaSlotConfTable.setStatus("mandatory")
_HwMusaSlotConfEntry_Object = MibTableRow
hwMusaSlotConfEntry = _HwMusaSlotConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1)
)
hwMusaSlotConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaSlotConfEntry.setStatus("mandatory")


class _HwMusaSlotIndex_Type(Integer32):
    """Custom type hwMusaSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwMusaSlotIndex_Type.__name__ = "Integer32"
_HwMusaSlotIndex_Object = MibTableColumn
hwMusaSlotIndex = _HwMusaSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 1),
    _HwMusaSlotIndex_Type()
)
hwMusaSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaSlotIndex.setStatus("mandatory")


class _HwMusaSlotCardType_Type(Integer32):
    """Custom type hwMusaSlotCardType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              19,
              21,
              25)
        )
    )
    namedValues = NamedValues(
        *(("adl", 3),
          ("adlb", 10),
          ("adlc", 21),
          ("adld", 25),
          ("cesa", 6),
          ("cesb", 7),
          ("fra", 9),
          ("lan", 19),
          ("lana", 5),
          ("lanb", 4),
          ("mmx", 1),
          ("null", 0),
          ("pots", 16),
          ("sep", 13),
          ("smx", 2),
          ("smxa", 14),
          ("smxb", 15),
          ("spl", 8),
          ("splb", 12),
          ("splc", 18),
          ("unknown", 11))
    )


_HwMusaSlotCardType_Type.__name__ = "Integer32"
_HwMusaSlotCardType_Object = MibTableColumn
hwMusaSlotCardType = _HwMusaSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 2),
    _HwMusaSlotCardType_Type()
)
hwMusaSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotCardType.setStatus("mandatory")
_HwMusaSlotCardSerial_Type = Integer32
_HwMusaSlotCardSerial_Object = MibTableColumn
hwMusaSlotCardSerial = _HwMusaSlotCardSerial_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 3),
    _HwMusaSlotCardSerial_Type()
)
hwMusaSlotCardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotCardSerial.setStatus("mandatory")
_HwMusaSlotCardVersion_Type = DisplayString
_HwMusaSlotCardVersion_Object = MibTableColumn
hwMusaSlotCardVersion = _HwMusaSlotCardVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 4),
    _HwMusaSlotCardVersion_Type()
)
hwMusaSlotCardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotCardVersion.setStatus("mandatory")
_HwMusaSlotIpAddress_Type = IpAddress
_HwMusaSlotIpAddress_Object = MibTableColumn
hwMusaSlotIpAddress = _HwMusaSlotIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 5),
    _HwMusaSlotIpAddress_Type()
)
hwMusaSlotIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSlotIpAddress.setStatus("mandatory")


class _HwMusaSlotCardAdminStatus_Type(Integer32):
    """Custom type hwMusaSlotCardAdminStatus based on Integer32"""
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
              8,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("bakfault", 6),
          ("baknormal", 5),
          ("commfail", 13),
          ("commok", 12),
          ("config", 8),
          ("fault", 2),
          ("forbid", 7),
          ("mainfault", 4),
          ("mainnormal", 3),
          ("noinstall", 0),
          ("none", 11),
          ("normal", 1),
          ("online", 10))
    )


_HwMusaSlotCardAdminStatus_Type.__name__ = "Integer32"
_HwMusaSlotCardAdminStatus_Object = MibTableColumn
hwMusaSlotCardAdminStatus = _HwMusaSlotCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 6),
    _HwMusaSlotCardAdminStatus_Type()
)
hwMusaSlotCardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotCardAdminStatus.setStatus("mandatory")


class _HwMusaSlotCardOperStatus_Type(Integer32):
    """Custom type hwMusaSlotCardOperStatus based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("addaiusubboard", 8),
          ("del", 0),
          ("delaiusubboard", 9),
          ("delmmxsubboard", 7),
          ("inverse", 5),
          ("mmxswitchover", 6),
          ("nouse", 4),
          ("reset", 2),
          ("use", 3))
    )


_HwMusaSlotCardOperStatus_Type.__name__ = "Integer32"
_HwMusaSlotCardOperStatus_Object = MibTableColumn
hwMusaSlotCardOperStatus = _HwMusaSlotCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 7),
    _HwMusaSlotCardOperStatus_Type()
)
hwMusaSlotCardOperStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaSlotCardOperStatus.setStatus("mandatory")
_HwMusaSlotDescript_Type = DisplayString
_HwMusaSlotDescript_Object = MibTableColumn
hwMusaSlotDescript = _HwMusaSlotDescript_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 8),
    _HwMusaSlotDescript_Type()
)
hwMusaSlotDescript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotDescript.setStatus("mandatory")


class _HwMusaBoardCellLossPriority_Type(Integer32):
    """Custom type hwMusaBoardCellLossPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_HwMusaBoardCellLossPriority_Type.__name__ = "Integer32"
_HwMusaBoardCellLossPriority_Object = MibTableColumn
hwMusaBoardCellLossPriority = _HwMusaBoardCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 9),
    _HwMusaBoardCellLossPriority_Type()
)
hwMusaBoardCellLossPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaBoardCellLossPriority.setStatus("mandatory")


class _HwMusaBoardMaxBandwidth_Type(Integer32):
    """Custom type hwMusaBoardMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b-155M", 0),
          ("b-20M", 2),
          ("b-4M", 3),
          ("b-80M", 1))
    )


_HwMusaBoardMaxBandwidth_Type.__name__ = "Integer32"
_HwMusaBoardMaxBandwidth_Object = MibTableColumn
hwMusaBoardMaxBandwidth = _HwMusaBoardMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 10),
    _HwMusaBoardMaxBandwidth_Type()
)
hwMusaBoardMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaBoardMaxBandwidth.setStatus("mandatory")
_HwMusaCpuOccupyRate_Type = Integer32
_HwMusaCpuOccupyRate_Object = MibTableColumn
hwMusaCpuOccupyRate = _HwMusaCpuOccupyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 11),
    _HwMusaCpuOccupyRate_Type()
)
hwMusaCpuOccupyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCpuOccupyRate.setStatus("mandatory")
_HwMusaQueryMemory_Type = DisplayString
_HwMusaQueryMemory_Object = MibTableColumn
hwMusaQueryMemory = _HwMusaQueryMemory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 12),
    _HwMusaQueryMemory_Type()
)
hwMusaQueryMemory.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaQueryMemory.setStatus("mandatory")


class _HwMusaLoadProtocol_Type(Integer32):
    """Custom type hwMusaLoadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("tftp", 0)
    )


_HwMusaLoadProtocol_Type.__name__ = "Integer32"
_HwMusaLoadProtocol_Object = MibTableColumn
hwMusaLoadProtocol = _HwMusaLoadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 13),
    _HwMusaLoadProtocol_Type()
)
hwMusaLoadProtocol.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaLoadProtocol.setStatus("mandatory")


class _HwMusaLoadContent_Type(Integer32):
    """Custom type hwMusaLoadContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("data", 8),
          ("fpga", 7),
          ("program", 6))
    )


_HwMusaLoadContent_Type.__name__ = "Integer32"
_HwMusaLoadContent_Object = MibTableColumn
hwMusaLoadContent = _HwMusaLoadContent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 14),
    _HwMusaLoadContent_Type()
)
hwMusaLoadContent.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaLoadContent.setStatus("mandatory")
_HwMusaLoadTftpServerIp_Type = IpAddress
_HwMusaLoadTftpServerIp_Object = MibTableColumn
hwMusaLoadTftpServerIp = _HwMusaLoadTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 15),
    _HwMusaLoadTftpServerIp_Type()
)
hwMusaLoadTftpServerIp.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaLoadTftpServerIp.setStatus("mandatory")
_HwMusaLoadFileName_Type = DisplayString
_HwMusaLoadFileName_Object = MibTableColumn
hwMusaLoadFileName = _HwMusaLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 16),
    _HwMusaLoadFileName_Type()
)
hwMusaLoadFileName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaLoadFileName.setStatus("mandatory")


class _HwMusaLoadOperType_Type(Integer32):
    """Custom type hwMusaLoadOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clearflash", 4),
          ("downback", 2),
          ("load", 0),
          ("rollback", 3),
          ("upback", 1))
    )


_HwMusaLoadOperType_Type.__name__ = "Integer32"
_HwMusaLoadOperType_Object = MibTableColumn
hwMusaLoadOperType = _HwMusaLoadOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 17),
    _HwMusaLoadOperType_Type()
)
hwMusaLoadOperType.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaLoadOperType.setStatus("mandatory")
_HwMusaSlotUpBandWidth_Type = Integer32
_HwMusaSlotUpBandWidth_Object = MibTableColumn
hwMusaSlotUpBandWidth = _HwMusaSlotUpBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 18),
    _HwMusaSlotUpBandWidth_Type()
)
hwMusaSlotUpBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSlotUpBandWidth.setStatus("mandatory")
_HwMusaSlotDownBandWidth_Type = Integer32
_HwMusaSlotDownBandWidth_Object = MibTableColumn
hwMusaSlotDownBandWidth = _HwMusaSlotDownBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 19),
    _HwMusaSlotDownBandWidth_Type()
)
hwMusaSlotDownBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSlotDownBandWidth.setStatus("mandatory")
_HwMusaSlotUsedUpBandWidth_Type = Integer32
_HwMusaSlotUsedUpBandWidth_Object = MibTableColumn
hwMusaSlotUsedUpBandWidth = _HwMusaSlotUsedUpBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 20),
    _HwMusaSlotUsedUpBandWidth_Type()
)
hwMusaSlotUsedUpBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotUsedUpBandWidth.setStatus("mandatory")
_HwMusaSlotUsedDownBandWidth_Type = Integer32
_HwMusaSlotUsedDownBandWidth_Object = MibTableColumn
hwMusaSlotUsedDownBandWidth = _HwMusaSlotUsedDownBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 21),
    _HwMusaSlotUsedDownBandWidth_Type()
)
hwMusaSlotUsedDownBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotUsedDownBandWidth.setStatus("mandatory")
_HwMusaSlotUpPracticalBandWidth_Type = Integer32
_HwMusaSlotUpPracticalBandWidth_Object = MibTableColumn
hwMusaSlotUpPracticalBandWidth = _HwMusaSlotUpPracticalBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 22),
    _HwMusaSlotUpPracticalBandWidth_Type()
)
hwMusaSlotUpPracticalBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotUpPracticalBandWidth.setStatus("mandatory")
_HwMusaSlotDownPracticalBandWidth_Type = Integer32
_HwMusaSlotDownPracticalBandWidth_Object = MibTableColumn
hwMusaSlotDownPracticalBandWidth = _HwMusaSlotDownPracticalBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 6, 3, 2, 1, 23),
    _HwMusaSlotDownPracticalBandWidth_Type()
)
hwMusaSlotDownPracticalBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaSlotDownPracticalBandWidth.setStatus("mandatory")
_HwMusaOamGroup_ObjectIdentity = ObjectIdentity
hwMusaOamGroup = _HwMusaOamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7)
)
_HwMusaOimPhyTable_Object = MibTable
hwMusaOimPhyTable = _HwMusaOimPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwMusaOimPhyTable.setStatus("mandatory")
_HwMusaOimPhyEntry_Object = MibTableRow
hwMusaOimPhyEntry = _HwMusaOimPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1)
)
hwMusaOimPhyEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwOIMPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaOimPhyEntry.setStatus("mandatory")
_HwOIMPortIndex_Type = Integer32
_HwOIMPortIndex_Object = MibTableColumn
hwOIMPortIndex = _HwOIMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 1),
    _HwOIMPortIndex_Type()
)
hwOIMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOIMPortIndex.setStatus("mandatory")


class _HwMusaSetSrcLoop_Type(Integer32):
    """Custom type hwMusaSetSrcLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("notloop", 0))
    )


_HwMusaSetSrcLoop_Type.__name__ = "Integer32"
_HwMusaSetSrcLoop_Object = MibTableColumn
hwMusaSetSrcLoop = _HwMusaSetSrcLoop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 2),
    _HwMusaSetSrcLoop_Type()
)
hwMusaSetSrcLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSetSrcLoop.setStatus("mandatory")


class _HwMusaSetLineLoop_Type(Integer32):
    """Custom type hwMusaSetLineLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("notloop", 0))
    )


_HwMusaSetLineLoop_Type.__name__ = "Integer32"
_HwMusaSetLineLoop_Object = MibTableColumn
hwMusaSetLineLoop = _HwMusaSetLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 3),
    _HwMusaSetLineLoop_Type()
)
hwMusaSetLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSetLineLoop.setStatus("mandatory")


class _HwMusaSetUtopiaLoop_Type(Integer32):
    """Custom type hwMusaSetUtopiaLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("notloop", 0))
    )


_HwMusaSetUtopiaLoop_Type.__name__ = "Integer32"
_HwMusaSetUtopiaLoop_Object = MibTableColumn
hwMusaSetUtopiaLoop = _HwMusaSetUtopiaLoop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 4),
    _HwMusaSetUtopiaLoop_Type()
)
hwMusaSetUtopiaLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSetUtopiaLoop.setStatus("mandatory")


class _HwMusaInsertLOF_Type(Integer32):
    """Custom type hwMusaInsertLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notinsert", 0))
    )


_HwMusaInsertLOF_Type.__name__ = "Integer32"
_HwMusaInsertLOF_Object = MibTableColumn
hwMusaInsertLOF = _HwMusaInsertLOF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 5),
    _HwMusaInsertLOF_Type()
)
hwMusaInsertLOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaInsertLOF.setStatus("mandatory")


class _HwMusaInsertLOS_Type(Integer32):
    """Custom type hwMusaInsertLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notinsert", 0))
    )


_HwMusaInsertLOS_Type.__name__ = "Integer32"
_HwMusaInsertLOS_Object = MibTableColumn
hwMusaInsertLOS = _HwMusaInsertLOS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 6),
    _HwMusaInsertLOS_Type()
)
hwMusaInsertLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaInsertLOS.setStatus("mandatory")
_HwMusaInsertBIP1_Type = Integer32
_HwMusaInsertBIP1_Object = MibTableColumn
hwMusaInsertBIP1 = _HwMusaInsertBIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 7),
    _HwMusaInsertBIP1_Type()
)
hwMusaInsertBIP1.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaInsertBIP1.setStatus("mandatory")
_HwMusaInsertBIP2_Type = Integer32
_HwMusaInsertBIP2_Object = MibTableColumn
hwMusaInsertBIP2 = _HwMusaInsertBIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 8),
    _HwMusaInsertBIP2_Type()
)
hwMusaInsertBIP2.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaInsertBIP2.setStatus("mandatory")
_HwMusaInsertBIP3_Type = Integer32
_HwMusaInsertBIP3_Object = MibTableColumn
hwMusaInsertBIP3 = _HwMusaInsertBIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 9),
    _HwMusaInsertBIP3_Type()
)
hwMusaInsertBIP3.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaInsertBIP3.setStatus("mandatory")


class _HwMusaInsertLAIS_Type(Integer32):
    """Custom type hwMusaInsertLAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notinsert", 0))
    )


_HwMusaInsertLAIS_Type.__name__ = "Integer32"
_HwMusaInsertLAIS_Object = MibTableColumn
hwMusaInsertLAIS = _HwMusaInsertLAIS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 10),
    _HwMusaInsertLAIS_Type()
)
hwMusaInsertLAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaInsertLAIS.setStatus("mandatory")


class _HwMusaInsertPAIS_Type(Integer32):
    """Custom type hwMusaInsertPAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notinsert", 0))
    )


_HwMusaInsertPAIS_Type.__name__ = "Integer32"
_HwMusaInsertPAIS_Object = MibTableColumn
hwMusaInsertPAIS = _HwMusaInsertPAIS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 11),
    _HwMusaInsertPAIS_Type()
)
hwMusaInsertPAIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaInsertPAIS.setStatus("mandatory")


class _HwMusaInsertLRDI_Type(Integer32):
    """Custom type hwMusaInsertLRDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notinsert", 0))
    )


_HwMusaInsertLRDI_Type.__name__ = "Integer32"
_HwMusaInsertLRDI_Object = MibTableColumn
hwMusaInsertLRDI = _HwMusaInsertLRDI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 1, 1, 12),
    _HwMusaInsertLRDI_Type()
)
hwMusaInsertLRDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaInsertLRDI.setStatus("mandatory")
_HwMusaOimOpticTable_Object = MibTable
hwMusaOimOpticTable = _HwMusaOimOpticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hwMusaOimOpticTable.setStatus("mandatory")
_HwMusaOimOpticEntry_Object = MibTableRow
hwMusaOimOpticEntry = _HwMusaOimOpticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1)
)
hwMusaOimOpticEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwOIMPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaOimOpticEntry.setStatus("mandatory")
_HwMusaQueryCurBIP1_Type = Counter32
_HwMusaQueryCurBIP1_Object = MibTableColumn
hwMusaQueryCurBIP1 = _HwMusaQueryCurBIP1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 1),
    _HwMusaQueryCurBIP1_Type()
)
hwMusaQueryCurBIP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurBIP1.setStatus("mandatory")
_HwMusaQueryCurBIP2_Type = Counter32
_HwMusaQueryCurBIP2_Object = MibTableColumn
hwMusaQueryCurBIP2 = _HwMusaQueryCurBIP2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 2),
    _HwMusaQueryCurBIP2_Type()
)
hwMusaQueryCurBIP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurBIP2.setStatus("mandatory")
_HwMusaQueryCurBIP3_Type = Counter32
_HwMusaQueryCurBIP3_Object = MibTableColumn
hwMusaQueryCurBIP3 = _HwMusaQueryCurBIP3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 3),
    _HwMusaQueryCurBIP3_Type()
)
hwMusaQueryCurBIP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurBIP3.setStatus("mandatory")
_HwMusaQueryCurLFEBE_Type = Counter32
_HwMusaQueryCurLFEBE_Object = MibTableColumn
hwMusaQueryCurLFEBE = _HwMusaQueryCurLFEBE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 4),
    _HwMusaQueryCurLFEBE_Type()
)
hwMusaQueryCurLFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurLFEBE.setStatus("mandatory")
_HwMusaQueryCurPFEBE_Type = Counter32
_HwMusaQueryCurPFEBE_Object = MibTableColumn
hwMusaQueryCurPFEBE = _HwMusaQueryCurPFEBE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 5),
    _HwMusaQueryCurPFEBE_Type()
)
hwMusaQueryCurPFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurPFEBE.setStatus("mandatory")
_HwMusaQueryCurSendCellNum_Type = Counter32
_HwMusaQueryCurSendCellNum_Object = MibTableColumn
hwMusaQueryCurSendCellNum = _HwMusaQueryCurSendCellNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 6),
    _HwMusaQueryCurSendCellNum_Type()
)
hwMusaQueryCurSendCellNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurSendCellNum.setStatus("mandatory")
_HwMusaQueryCurReceiveCellNum_Type = Counter32
_HwMusaQueryCurReceiveCellNum_Object = MibTableColumn
hwMusaQueryCurReceiveCellNum = _HwMusaQueryCurReceiveCellNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 7),
    _HwMusaQueryCurReceiveCellNum_Type()
)
hwMusaQueryCurReceiveCellNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurReceiveCellNum.setStatus("mandatory")
_HwMusaQueryCurCorrectHECNum_Type = Counter32
_HwMusaQueryCurCorrectHECNum_Object = MibTableColumn
hwMusaQueryCurCorrectHECNum = _HwMusaQueryCurCorrectHECNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 8),
    _HwMusaQueryCurCorrectHECNum_Type()
)
hwMusaQueryCurCorrectHECNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurCorrectHECNum.setStatus("mandatory")
_HwMusaQueryCurNonCorrectHECNum_Type = Counter32
_HwMusaQueryCurNonCorrectHECNum_Object = MibTableColumn
hwMusaQueryCurNonCorrectHECNum = _HwMusaQueryCurNonCorrectHECNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 9),
    _HwMusaQueryCurNonCorrectHECNum_Type()
)
hwMusaQueryCurNonCorrectHECNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurNonCorrectHECNum.setStatus("mandatory")
_HwMusaQueryCurLOCDNum_Type = Counter32
_HwMusaQueryCurLOCDNum_Object = MibTableColumn
hwMusaQueryCurLOCDNum = _HwMusaQueryCurLOCDNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 10),
    _HwMusaQueryCurLOCDNum_Type()
)
hwMusaQueryCurLOCDNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurLOCDNum.setStatus("mandatory")
_HwMusaQueryCurUnmatchCellNum_Type = Counter32
_HwMusaQueryCurUnmatchCellNum_Object = MibTableColumn
hwMusaQueryCurUnmatchCellNum = _HwMusaQueryCurUnmatchCellNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 11),
    _HwMusaQueryCurUnmatchCellNum_Type()
)
hwMusaQueryCurUnmatchCellNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurUnmatchCellNum.setStatus("mandatory")
_HwMusaQueryCurOOFNum_Type = Counter32
_HwMusaQueryCurOOFNum_Object = MibTableColumn
hwMusaQueryCurOOFNum = _HwMusaQueryCurOOFNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 12),
    _HwMusaQueryCurOOFNum_Type()
)
hwMusaQueryCurOOFNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaQueryCurOOFNum.setStatus("mandatory")
_HwMusaClearAllAlarmStat_Type = Integer32
_HwMusaClearAllAlarmStat_Object = MibTableColumn
hwMusaClearAllAlarmStat = _HwMusaClearAllAlarmStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 13),
    _HwMusaClearAllAlarmStat_Type()
)
hwMusaClearAllAlarmStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaClearAllAlarmStat.setStatus("mandatory")
_HwMusaClearOIMErrEventStat_Type = Integer32
_HwMusaClearOIMErrEventStat_Object = MibTableColumn
hwMusaClearOIMErrEventStat = _HwMusaClearOIMErrEventStat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 7, 2, 1, 14),
    _HwMusaClearOIMErrEventStat_Type()
)
hwMusaClearOIMErrEventStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaClearOIMErrEventStat.setStatus("mandatory")
_HwMusaWarningCtrlTable_Object = MibTable
hwMusaWarningCtrlTable = _HwMusaWarningCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hwMusaWarningCtrlTable.setStatus("mandatory")
_HwMusaWarningCtrlEntry_Object = MibTableRow
hwMusaWarningCtrlEntry = _HwMusaWarningCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1)
)
hwMusaWarningCtrlEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaWarningID"),
)
if mibBuilder.loadTexts:
    hwMusaWarningCtrlEntry.setStatus("mandatory")
_HwMusaWarningID_Type = Counter32
_HwMusaWarningID_Object = MibTableColumn
hwMusaWarningID = _HwMusaWarningID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 1),
    _HwMusaWarningID_Type()
)
hwMusaWarningID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaWarningID.setStatus("mandatory")


class _HwMusaWarningLevel_Type(Integer32):
    """Custom type hwMusaWarningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 4),
          ("fatal", 3),
          ("normal", 1),
          ("notify", 0),
          ("serious", 2))
    )


_HwMusaWarningLevel_Type.__name__ = "Integer32"
_HwMusaWarningLevel_Object = MibTableColumn
hwMusaWarningLevel = _HwMusaWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 2),
    _HwMusaWarningLevel_Type()
)
hwMusaWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarningLevel.setStatus("mandatory")


class _HwMusaWarningNmsCtrl_Type(Integer32):
    """Custom type hwMusaWarningNmsCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwMusaWarningNmsCtrl_Type.__name__ = "Integer32"
_HwMusaWarningNmsCtrl_Object = MibTableColumn
hwMusaWarningNmsCtrl = _HwMusaWarningNmsCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 3),
    _HwMusaWarningNmsCtrl_Type()
)
hwMusaWarningNmsCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarningNmsCtrl.setStatus("mandatory")


class _HwMusaWarningTerminalCtrl_Type(Integer32):
    """Custom type hwMusaWarningTerminalCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwMusaWarningTerminalCtrl_Type.__name__ = "Integer32"
_HwMusaWarningTerminalCtrl_Object = MibTableColumn
hwMusaWarningTerminalCtrl = _HwMusaWarningTerminalCtrl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 4),
    _HwMusaWarningTerminalCtrl_Type()
)
hwMusaWarningTerminalCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarningTerminalCtrl.setStatus("mandatory")


class _HwMusaWarningIsCount_Type(Integer32):
    """Custom type hwMusaWarningIsCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwMusaWarningIsCount_Type.__name__ = "Integer32"
_HwMusaWarningIsCount_Object = MibTableColumn
hwMusaWarningIsCount = _HwMusaWarningIsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 5),
    _HwMusaWarningIsCount_Type()
)
hwMusaWarningIsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarningIsCount.setStatus("mandatory")
_HwMusaWarn15MinThreshold_Type = Integer32
_HwMusaWarn15MinThreshold_Object = MibTableColumn
hwMusaWarn15MinThreshold = _HwMusaWarn15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 6),
    _HwMusaWarn15MinThreshold_Type()
)
hwMusaWarn15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarn15MinThreshold.setStatus("mandatory")
_HwMusaWarn24HourThreshold_Type = Integer32
_HwMusaWarn24HourThreshold_Object = MibTableColumn
hwMusaWarn24HourThreshold = _HwMusaWarn24HourThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 7),
    _HwMusaWarn24HourThreshold_Type()
)
hwMusaWarn24HourThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaWarn24HourThreshold.setStatus("mandatory")


class _HwMusaWarningDesc_Type(DisplayString):
    """Custom type hwMusaWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMusaWarningDesc_Type.__name__ = "DisplayString"
_HwMusaWarningDesc_Object = MibTableColumn
hwMusaWarningDesc = _HwMusaWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 8),
    _HwMusaWarningDesc_Type()
)
hwMusaWarningDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaWarningDesc.setStatus("mandatory")


class _HwMusaWarningEngDesc_Type(DisplayString):
    """Custom type hwMusaWarningEngDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwMusaWarningEngDesc_Type.__name__ = "DisplayString"
_HwMusaWarningEngDesc_Object = MibTableColumn
hwMusaWarningEngDesc = _HwMusaWarningEngDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 9, 1, 9),
    _HwMusaWarningEngDesc_Type()
)
hwMusaWarningEngDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaWarningEngDesc.setStatus("mandatory")
_HwMusaSysRouteTable_Object = MibTable
hwMusaSysRouteTable = _HwMusaSysRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hwMusaSysRouteTable.setStatus("mandatory")
_HwMusaSysRouteEntry_Object = MibTableRow
hwMusaSysRouteEntry = _HwMusaSysRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1)
)
hwMusaSysRouteEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSysRouteIndex"),
)
if mibBuilder.loadTexts:
    hwMusaSysRouteEntry.setStatus("mandatory")
_HwMusaSysRouteIndex_Type = Integer32
_HwMusaSysRouteIndex_Object = MibTableColumn
hwMusaSysRouteIndex = _HwMusaSysRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1, 1),
    _HwMusaSysRouteIndex_Type()
)
hwMusaSysRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaSysRouteIndex.setStatus("mandatory")
_HwMusaDstIp_Type = IpAddress
_HwMusaDstIp_Object = MibTableColumn
hwMusaDstIp = _HwMusaDstIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1, 2),
    _HwMusaDstIp_Type()
)
hwMusaDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDstIp.setStatus("mandatory")
_HwMusaDstIpMask_Type = IpAddress
_HwMusaDstIpMask_Object = MibTableColumn
hwMusaDstIpMask = _HwMusaDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1, 3),
    _HwMusaDstIpMask_Type()
)
hwMusaDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDstIpMask.setStatus("mandatory")
_HwMusaGateIp_Type = IpAddress
_HwMusaGateIp_Object = MibTableColumn
hwMusaGateIp = _HwMusaGateIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1, 4),
    _HwMusaGateIp_Type()
)
hwMusaGateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaGateIp.setStatus("mandatory")


class _HwMusaSysRouteOper_Type(Integer32):
    """Custom type hwMusaSysRouteOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaSysRouteOper_Type.__name__ = "Integer32"
_HwMusaSysRouteOper_Object = MibTableColumn
hwMusaSysRouteOper = _HwMusaSysRouteOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 10, 1, 5),
    _HwMusaSysRouteOper_Type()
)
hwMusaSysRouteOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSysRouteOper.setStatus("mandatory")
_HwMusaLoadRateTable_Object = MibTable
hwMusaLoadRateTable = _HwMusaLoadRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hwMusaLoadRateTable.setStatus("mandatory")
_HwMusaLoadRateEntry_Object = MibTableRow
hwMusaLoadRateEntry = _HwMusaLoadRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 11, 1)
)
hwMusaLoadRateEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaLoadRateEntry.setStatus("mandatory")


class _HwMusaLoadRate_Type(Integer32):
    """Custom type hwMusaLoadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMusaLoadRate_Type.__name__ = "Integer32"
_HwMusaLoadRate_Object = MibTableColumn
hwMusaLoadRate = _HwMusaLoadRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 11, 1, 1),
    _HwMusaLoadRate_Type()
)
hwMusaLoadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaLoadRate.setStatus("mandatory")


class _HwMusaLoadType_Type(Integer32):
    """Custom type hwMusaLoadType based on Integer32"""
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
        *(("backData", 1),
          ("data", 8),
          ("dumpData", 2),
          ("fpga", 7),
          ("loadData", 3),
          ("loadFpga", 5),
          ("loadProc", 4),
          ("noOper", 0),
          ("program", 6))
    )


_HwMusaLoadType_Type.__name__ = "Integer32"
_HwMusaLoadType_Object = MibTableColumn
hwMusaLoadType = _HwMusaLoadType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 11, 1, 2),
    _HwMusaLoadType_Type()
)
hwMusaLoadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaLoadType.setStatus("mandatory")
_HwMusaTrafficTable_Object = MibTable
hwMusaTrafficTable = _HwMusaTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hwMusaTrafficTable.setStatus("mandatory")
_HwMusaTrafficEntry_Object = MibTableRow
hwMusaTrafficEntry = _HwMusaTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1)
)
hwMusaTrafficEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaTrafficIndex"),
)
if mibBuilder.loadTexts:
    hwMusaTrafficEntry.setStatus("mandatory")


class _HwMusaTrafficIndex_Type(Integer32):
    """Custom type hwMusaTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_HwMusaTrafficIndex_Type.__name__ = "Integer32"
_HwMusaTrafficIndex_Object = MibTableColumn
hwMusaTrafficIndex = _HwMusaTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 1),
    _HwMusaTrafficIndex_Type()
)
hwMusaTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaTrafficIndex.setStatus("mandatory")


class _HwMusaTrafficType_Type(Integer32):
    """Custom type hwMusaTrafficType based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("clpnotaggingmcr", 7),
          ("clpnotaggingnoscr", 2),
          ("clpnotaggingscr", 5),
          ("clpnotaggingscrcdvt", 13),
          ("clptaggingnoscr", 3),
          ("clptaggingscr", 6),
          ("clptaggingscrcdvt", 14),
          ("clptransparentnoscr", 8),
          ("clptransparentscr", 9),
          ("noclpnoscr", 1),
          ("noclpnoscrcdvt", 11),
          ("noclpscr", 4),
          ("noclpscrcdvt", 12),
          ("noclptaggingnoscr", 10))
    )


_HwMusaTrafficType_Type.__name__ = "Integer32"
_HwMusaTrafficType_Object = MibTableColumn
hwMusaTrafficType = _HwMusaTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 2),
    _HwMusaTrafficType_Type()
)
hwMusaTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaTrafficType.setStatus("mandatory")


class _HwMusaServiceClass_Type(Integer32):
    """Custom type hwMusaServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("nrtVBR", 4),
          ("rtVBR", 3),
          ("ubr", 6))
    )


_HwMusaServiceClass_Type.__name__ = "Integer32"
_HwMusaServiceClass_Object = MibTableColumn
hwMusaServiceClass = _HwMusaServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 3),
    _HwMusaServiceClass_Type()
)
hwMusaServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaServiceClass.setStatus("mandatory")
_HwMusaRefCount_Type = Integer32
_HwMusaRefCount_Object = MibTableColumn
hwMusaRefCount = _HwMusaRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 4),
    _HwMusaRefCount_Type()
)
hwMusaRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaRefCount.setStatus("mandatory")


class _HwMusaRecordState_Type(Integer32):
    """Custom type hwMusaRecordState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("module", 2))
    )


_HwMusaRecordState_Type.__name__ = "Integer32"
_HwMusaRecordState_Object = MibTableColumn
hwMusaRecordState = _HwMusaRecordState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 5),
    _HwMusaRecordState_Type()
)
hwMusaRecordState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaRecordState.setStatus("mandatory")
_HwMusaClp01pcr_Type = Integer32
_HwMusaClp01pcr_Object = MibTableColumn
hwMusaClp01pcr = _HwMusaClp01pcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 6),
    _HwMusaClp01pcr_Type()
)
hwMusaClp01pcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaClp01pcr.setStatus("mandatory")
_HwMusaClp0pcr_Type = Integer32
_HwMusaClp0pcr_Object = MibTableColumn
hwMusaClp0pcr = _HwMusaClp0pcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 7),
    _HwMusaClp0pcr_Type()
)
hwMusaClp0pcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaClp0pcr.setStatus("mandatory")
_HwMusaClp01scr_Type = Integer32
_HwMusaClp01scr_Object = MibTableColumn
hwMusaClp01scr = _HwMusaClp01scr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 8),
    _HwMusaClp01scr_Type()
)
hwMusaClp01scr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaClp01scr.setStatus("mandatory")
_HwMusaClp0scr_Type = Integer32
_HwMusaClp0scr_Object = MibTableColumn
hwMusaClp0scr = _HwMusaClp0scr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 9),
    _HwMusaClp0scr_Type()
)
hwMusaClp0scr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaClp0scr.setStatus("mandatory")
_HwMusaMbs_Type = Integer32
_HwMusaMbs_Object = MibTableColumn
hwMusaMbs = _HwMusaMbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 10),
    _HwMusaMbs_Type()
)
hwMusaMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaMbs.setStatus("mandatory")
_HwMusaMcr_Type = Integer32
_HwMusaMcr_Object = MibTableColumn
hwMusaMcr = _HwMusaMcr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 11),
    _HwMusaMcr_Type()
)
hwMusaMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaMcr.setStatus("mandatory")
_HwMusaCDVT_Type = Integer32
_HwMusaCDVT_Object = MibTableColumn
hwMusaCDVT = _HwMusaCDVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 12),
    _HwMusaCDVT_Type()
)
hwMusaCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaCDVT.setStatus("mandatory")


class _HwMusaOperat_Type(Integer32):
    """Custom type hwMusaOperat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaOperat_Type.__name__ = "Integer32"
_HwMusaOperat_Object = MibTableColumn
hwMusaOperat = _HwMusaOperat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 13),
    _HwMusaOperat_Type()
)
hwMusaOperat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaOperat.setStatus("mandatory")
_HwMusaNextTrafficIndex_Type = Integer32
_HwMusaNextTrafficIndex_Object = MibTableColumn
hwMusaNextTrafficIndex = _HwMusaNextTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 13, 1, 14),
    _HwMusaNextTrafficIndex_Type()
)
hwMusaNextTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaNextTrafficIndex.setStatus("mandatory")
_HwMusaCampusPvcConfTable_Object = MibTable
hwMusaCampusPvcConfTable = _HwMusaCampusPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15)
)
if mibBuilder.loadTexts:
    hwMusaCampusPvcConfTable.setStatus("mandatory")
_HwMusaCampusPvcConfEntry_Object = MibTableRow
hwMusaCampusPvcConfEntry = _HwMusaCampusPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1)
)
hwMusaCampusPvcConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaVlanId"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaVlanIciIndex"),
)
if mibBuilder.loadTexts:
    hwMusaCampusPvcConfEntry.setStatus("mandatory")


class _HwMusaVlanId_Type(Integer32):
    """Custom type hwMusaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HwMusaVlanId_Type.__name__ = "Integer32"
_HwMusaVlanId_Object = MibTableColumn
hwMusaVlanId = _HwMusaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 1),
    _HwMusaVlanId_Type()
)
hwMusaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaVlanId.setStatus("mandatory")
_HwMusaVlanIciIndex_Type = Integer32
_HwMusaVlanIciIndex_Object = MibTableColumn
hwMusaVlanIciIndex = _HwMusaVlanIciIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 2),
    _HwMusaVlanIciIndex_Type()
)
hwMusaVlanIciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaVlanIciIndex.setStatus("mandatory")
_HwMusaAdlPortCount_Type = Integer32
_HwMusaAdlPortCount_Object = MibTableColumn
hwMusaAdlPortCount = _HwMusaAdlPortCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 3),
    _HwMusaAdlPortCount_Type()
)
hwMusaAdlPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaAdlPortCount.setStatus("mandatory")


class _HwMusaAdlFrameId_Type(Integer32):
    """Custom type hwMusaAdlFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_HwMusaAdlFrameId_Type.__name__ = "Integer32"
_HwMusaAdlFrameId_Object = MibTableColumn
hwMusaAdlFrameId = _HwMusaAdlFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 4),
    _HwMusaAdlFrameId_Type()
)
hwMusaAdlFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlFrameId.setStatus("mandatory")


class _HwMusaAdlSlotId_Type(Integer32):
    """Custom type hwMusaAdlSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwMusaAdlSlotId_Type.__name__ = "Integer32"
_HwMusaAdlSlotId_Object = MibTableColumn
hwMusaAdlSlotId = _HwMusaAdlSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 5),
    _HwMusaAdlSlotId_Type()
)
hwMusaAdlSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlSlotId.setStatus("mandatory")


class _HwMusaAdlPortId_Type(Integer32):
    """Custom type hwMusaAdlPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwMusaAdlPortId_Type.__name__ = "Integer32"
_HwMusaAdlPortId_Object = MibTableColumn
hwMusaAdlPortId = _HwMusaAdlPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 6),
    _HwMusaAdlPortId_Type()
)
hwMusaAdlPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlPortId.setStatus("mandatory")


class _HwMusaAdlVpi_Type(Integer32):
    """Custom type hwMusaAdlVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwMusaAdlVpi_Type.__name__ = "Integer32"
_HwMusaAdlVpi_Object = MibTableColumn
hwMusaAdlVpi = _HwMusaAdlVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 7),
    _HwMusaAdlVpi_Type()
)
hwMusaAdlVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaAdlVpi.setStatus("mandatory")


class _HwMusaAdlVci_Type(Integer32):
    """Custom type hwMusaAdlVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 127),
    )


_HwMusaAdlVci_Type.__name__ = "Integer32"
_HwMusaAdlVci_Object = MibTableColumn
hwMusaAdlVci = _HwMusaAdlVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 8),
    _HwMusaAdlVci_Type()
)
hwMusaAdlVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaAdlVci.setStatus("mandatory")
_HwMusaToLanTrafficId_Type = Integer32
_HwMusaToLanTrafficId_Object = MibTableColumn
hwMusaToLanTrafficId = _HwMusaToLanTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 9),
    _HwMusaToLanTrafficId_Type()
)
hwMusaToLanTrafficId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaToLanTrafficId.setStatus("mandatory")
_HwMusaFromLanTrafficId_Type = Integer32
_HwMusaFromLanTrafficId_Object = MibTableColumn
hwMusaFromLanTrafficId = _HwMusaFromLanTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 10),
    _HwMusaFromLanTrafficId_Type()
)
hwMusaFromLanTrafficId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFromLanTrafficId.setStatus("mandatory")


class _HwMusaAdlPortOperat_Type(Integer32):
    """Custom type hwMusaAdlPortOperat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaAdlPortOperat_Type.__name__ = "Integer32"
_HwMusaAdlPortOperat_Object = MibTableColumn
hwMusaAdlPortOperat = _HwMusaAdlPortOperat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 15, 1, 11),
    _HwMusaAdlPortOperat_Type()
)
hwMusaAdlPortOperat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAdlPortOperat.setStatus("mandatory")
_HwMusaOpticBandwidthTable_Object = MibTable
hwMusaOpticBandwidthTable = _HwMusaOpticBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17)
)
if mibBuilder.loadTexts:
    hwMusaOpticBandwidthTable.setStatus("mandatory")
_HwMusaOpticBandwidthEntry_Object = MibTableRow
hwMusaOpticBandwidthEntry = _HwMusaOpticBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1)
)
hwMusaOpticBandwidthEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwOIMPortIndex"),
)
if mibBuilder.loadTexts:
    hwMusaOpticBandwidthEntry.setStatus("mandatory")
_HwMusaUpOpticMainBandWidth_Type = Integer32
_HwMusaUpOpticMainBandWidth_Object = MibTableColumn
hwMusaUpOpticMainBandWidth = _HwMusaUpOpticMainBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 1),
    _HwMusaUpOpticMainBandWidth_Type()
)
hwMusaUpOpticMainBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaUpOpticMainBandWidth.setStatus("mandatory")
_HwMusaDnOpticMainBandWidth_Type = Integer32
_HwMusaDnOpticMainBandWidth_Object = MibTableColumn
hwMusaDnOpticMainBandWidth = _HwMusaDnOpticMainBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 2),
    _HwMusaDnOpticMainBandWidth_Type()
)
hwMusaDnOpticMainBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDnOpticMainBandWidth.setStatus("mandatory")
_HwMusaCurUsedUpBandWidth_Type = Integer32
_HwMusaCurUsedUpBandWidth_Object = MibTableColumn
hwMusaCurUsedUpBandWidth = _HwMusaCurUsedUpBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 3),
    _HwMusaCurUsedUpBandWidth_Type()
)
hwMusaCurUsedUpBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCurUsedUpBandWidth.setStatus("mandatory")
_HwMusaCurUsedDownBandWidth_Type = Integer32
_HwMusaCurUsedDownBandWidth_Object = MibTableColumn
hwMusaCurUsedDownBandWidth = _HwMusaCurUsedDownBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 4),
    _HwMusaCurUsedDownBandWidth_Type()
)
hwMusaCurUsedDownBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCurUsedDownBandWidth.setStatus("mandatory")
_HwMusaUpReservedBandWidth_Type = Integer32
_HwMusaUpReservedBandWidth_Object = MibTableColumn
hwMusaUpReservedBandWidth = _HwMusaUpReservedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 5),
    _HwMusaUpReservedBandWidth_Type()
)
hwMusaUpReservedBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaUpReservedBandWidth.setStatus("mandatory")
_HwMusaDownReservedBandWidth_Type = Integer32
_HwMusaDownReservedBandWidth_Object = MibTableColumn
hwMusaDownReservedBandWidth = _HwMusaDownReservedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 6),
    _HwMusaDownReservedBandWidth_Type()
)
hwMusaDownReservedBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDownReservedBandWidth.setStatus("mandatory")
_HwMusaUpPracticalBandWidth_Type = Integer32
_HwMusaUpPracticalBandWidth_Object = MibTableColumn
hwMusaUpPracticalBandWidth = _HwMusaUpPracticalBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 7),
    _HwMusaUpPracticalBandWidth_Type()
)
hwMusaUpPracticalBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaUpPracticalBandWidth.setStatus("mandatory")
_HwMusaDownPracticalBandWidth_Type = Integer32
_HwMusaDownPracticalBandWidth_Object = MibTableColumn
hwMusaDownPracticalBandWidth = _HwMusaDownPracticalBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 17, 1, 8),
    _HwMusaDownPracticalBandWidth_Type()
)
hwMusaDownPracticalBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDownPracticalBandWidth.setStatus("mandatory")
_HwMusaTrafficCbrPcrTable_Object = MibTable
hwMusaTrafficCbrPcrTable = _HwMusaTrafficCbrPcrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 18)
)
if mibBuilder.loadTexts:
    hwMusaTrafficCbrPcrTable.setStatus("mandatory")
_HwMusaTrafficCbrPcrEntry_Object = MibTableRow
hwMusaTrafficCbrPcrEntry = _HwMusaTrafficCbrPcrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 18, 1)
)
hwMusaTrafficCbrPcrEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaCbrPcrIndex"),
)
if mibBuilder.loadTexts:
    hwMusaTrafficCbrPcrEntry.setStatus("mandatory")
_HwMusaCbrPcrIndex_Type = Integer32
_HwMusaCbrPcrIndex_Object = MibTableColumn
hwMusaCbrPcrIndex = _HwMusaCbrPcrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 18, 1, 1),
    _HwMusaCbrPcrIndex_Type()
)
hwMusaCbrPcrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaCbrPcrIndex.setStatus("mandatory")
_HwMusaCbrPcrValue_Type = Integer32
_HwMusaCbrPcrValue_Object = MibTableColumn
hwMusaCbrPcrValue = _HwMusaCbrPcrValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 18, 1, 2),
    _HwMusaCbrPcrValue_Type()
)
hwMusaCbrPcrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaCbrPcrValue.setStatus("mandatory")
_HwMusaCbrPcrRefCount_Type = Integer32
_HwMusaCbrPcrRefCount_Object = MibTableColumn
hwMusaCbrPcrRefCount = _HwMusaCbrPcrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 18, 1, 3),
    _HwMusaCbrPcrRefCount_Type()
)
hwMusaCbrPcrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCbrPcrRefCount.setStatus("mandatory")
_HwMusaTrafficRtvbrScrTable_Object = MibTable
hwMusaTrafficRtvbrScrTable = _HwMusaTrafficRtvbrScrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 19)
)
if mibBuilder.loadTexts:
    hwMusaTrafficRtvbrScrTable.setStatus("mandatory")
_HwMusaTrafficRtvbrScrEntry_Object = MibTableRow
hwMusaTrafficRtvbrScrEntry = _HwMusaTrafficRtvbrScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 19, 1)
)
hwMusaTrafficRtvbrScrEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaRtvbrScrIndex"),
)
if mibBuilder.loadTexts:
    hwMusaTrafficRtvbrScrEntry.setStatus("mandatory")
_HwMusaRtvbrScrIndex_Type = Integer32
_HwMusaRtvbrScrIndex_Object = MibTableColumn
hwMusaRtvbrScrIndex = _HwMusaRtvbrScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 19, 1, 1),
    _HwMusaRtvbrScrIndex_Type()
)
hwMusaRtvbrScrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaRtvbrScrIndex.setStatus("mandatory")
_HwMusaRtvbrScrValue_Type = Integer32
_HwMusaRtvbrScrValue_Object = MibTableColumn
hwMusaRtvbrScrValue = _HwMusaRtvbrScrValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 19, 1, 2),
    _HwMusaRtvbrScrValue_Type()
)
hwMusaRtvbrScrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaRtvbrScrValue.setStatus("mandatory")
_HwMusaRtvbrScrRefCount_Type = Integer32
_HwMusaRtvbrScrRefCount_Object = MibTableColumn
hwMusaRtvbrScrRefCount = _HwMusaRtvbrScrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 19, 1, 3),
    _HwMusaRtvbrScrRefCount_Type()
)
hwMusaRtvbrScrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaRtvbrScrRefCount.setStatus("mandatory")
_HwMusaPvcTrafficStatisTable_Object = MibTable
hwMusaPvcTrafficStatisTable = _HwMusaPvcTrafficStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21)
)
if mibBuilder.loadTexts:
    hwMusaPvcTrafficStatisTable.setStatus("mandatory")
_HwMusaPvcTrafficStatisEntry_Object = MibTableRow
hwMusaPvcTrafficStatisEntry = _HwMusaPvcTrafficStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21, 1)
)
hwMusaPvcTrafficStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSPvcIndex"),
)
if mibBuilder.loadTexts:
    hwMusaPvcTrafficStatisEntry.setStatus("mandatory")
_HwMusaUpStreamTrafficRx_Type = Counter32
_HwMusaUpStreamTrafficRx_Object = MibTableColumn
hwMusaUpStreamTrafficRx = _HwMusaUpStreamTrafficRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21, 1, 1),
    _HwMusaUpStreamTrafficRx_Type()
)
hwMusaUpStreamTrafficRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaUpStreamTrafficRx.setStatus("mandatory")
_HwMusaUpStreamTrafficTx_Type = Counter32
_HwMusaUpStreamTrafficTx_Object = MibTableColumn
hwMusaUpStreamTrafficTx = _HwMusaUpStreamTrafficTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21, 1, 2),
    _HwMusaUpStreamTrafficTx_Type()
)
hwMusaUpStreamTrafficTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaUpStreamTrafficTx.setStatus("mandatory")
_HwMusaDownStreamTrafficRx_Type = Counter32
_HwMusaDownStreamTrafficRx_Object = MibTableColumn
hwMusaDownStreamTrafficRx = _HwMusaDownStreamTrafficRx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21, 1, 3),
    _HwMusaDownStreamTrafficRx_Type()
)
hwMusaDownStreamTrafficRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaDownStreamTrafficRx.setStatus("mandatory")
_HwMusaDownStreamTrafficTx_Type = Counter32
_HwMusaDownStreamTrafficTx_Object = MibTableColumn
hwMusaDownStreamTrafficTx = _HwMusaDownStreamTrafficTx_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 21, 1, 4),
    _HwMusaDownStreamTrafficTx_Type()
)
hwMusaDownStreamTrafficTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaDownStreamTrafficTx.setStatus("mandatory")
_HwMusaAllPvcConfTable_Object = MibTable
hwMusaAllPvcConfTable = _HwMusaAllPvcConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22)
)
if mibBuilder.loadTexts:
    hwMusaAllPvcConfTable.setStatus("mandatory")
_HwMusaAllPvcConfEntry_Object = MibTableRow
hwMusaAllPvcConfEntry = _HwMusaAllPvcConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1)
)
hwMusaAllPvcConfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaTypeOfPvcPvp"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaCidIndex"),
)
if mibBuilder.loadTexts:
    hwMusaAllPvcConfEntry.setStatus("mandatory")
_HwMusaCidIndex_Type = Counter32
_HwMusaCidIndex_Object = MibTableColumn
hwMusaCidIndex = _HwMusaCidIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 1),
    _HwMusaCidIndex_Type()
)
hwMusaCidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaCidIndex.setStatus("mandatory")
_HwMusaSrcFrameId_Type = Integer32
_HwMusaSrcFrameId_Object = MibTableColumn
hwMusaSrcFrameId = _HwMusaSrcFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 2),
    _HwMusaSrcFrameId_Type()
)
hwMusaSrcFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrameId.setStatus("mandatory")
_HwMuasSrcSlotId_Type = Integer32
_HwMuasSrcSlotId_Object = MibTableColumn
hwMuasSrcSlotId = _HwMuasSrcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 3),
    _HwMuasSrcSlotId_Type()
)
hwMuasSrcSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMuasSrcSlotId.setStatus("mandatory")
_HwMusaSrcPortVlanVccId_Type = Integer32
_HwMusaSrcPortVlanVccId_Object = MibTableColumn
hwMusaSrcPortVlanVccId = _HwMusaSrcPortVlanVccId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 4),
    _HwMusaSrcPortVlanVccId_Type()
)
hwMusaSrcPortVlanVccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcPortVlanVccId.setStatus("mandatory")
_HwMusaSrcOnuId_Type = Integer32
_HwMusaSrcOnuId_Object = MibTableColumn
hwMusaSrcOnuId = _HwMusaSrcOnuId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 5),
    _HwMusaSrcOnuId_Type()
)
hwMusaSrcOnuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcOnuId.setStatus("mandatory")
_HwMusaSrcBoardVpi_Type = Integer32
_HwMusaSrcBoardVpi_Object = MibTableColumn
hwMusaSrcBoardVpi = _HwMusaSrcBoardVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 6),
    _HwMusaSrcBoardVpi_Type()
)
hwMusaSrcBoardVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcBoardVpi.setStatus("mandatory")
_HwMusaSrcBoardVci_Type = Integer32
_HwMusaSrcBoardVci_Object = MibTableColumn
hwMusaSrcBoardVci = _HwMusaSrcBoardVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 7),
    _HwMusaSrcBoardVci_Type()
)
hwMusaSrcBoardVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcBoardVci.setStatus("mandatory")


class _HwMusaSrcPortType_Type(Integer32):
    """Custom type hwMusaSrcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdt", 1),
          ("udt", 2),
          ("uni", 0))
    )


_HwMusaSrcPortType_Type.__name__ = "Integer32"
_HwMusaSrcPortType_Object = MibTableColumn
hwMusaSrcPortType = _HwMusaSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 8),
    _HwMusaSrcPortType_Type()
)
hwMusaSrcPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcPortType.setStatus("mandatory")
_HwMusaSrcCescChannelId_Type = Integer32
_HwMusaSrcCescChannelId_Object = MibTableColumn
hwMusaSrcCescChannelId = _HwMusaSrcCescChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 9),
    _HwMusaSrcCescChannelId_Type()
)
hwMusaSrcCescChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcCescChannelId.setStatus("mandatory")
_HwMusaSrcCescChannelBitmap_Type = Integer32
_HwMusaSrcCescChannelBitmap_Object = MibTableColumn
hwMusaSrcCescChannelBitmap = _HwMusaSrcCescChannelBitmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 10),
    _HwMusaSrcCescChannelBitmap_Type()
)
hwMusaSrcCescChannelBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcCescChannelBitmap.setStatus("mandatory")


class _HwMusaSrcCescFillDegree_Type(Integer32):
    """Custom type hwMusaSrcCescFillDegree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 47),
    )


_HwMusaSrcCescFillDegree_Type.__name__ = "Integer32"
_HwMusaSrcCescFillDegree_Object = MibTableColumn
hwMusaSrcCescFillDegree = _HwMusaSrcCescFillDegree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 11),
    _HwMusaSrcCescFillDegree_Type()
)
hwMusaSrcCescFillDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcCescFillDegree.setStatus("mandatory")


class _HwMusaSrcFrcDlciType_Type(Integer32):
    """Custom type hwMusaSrcFrcDlciType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwMusaSrcFrcDlciType_Type.__name__ = "Integer32"
_HwMusaSrcFrcDlciType_Object = MibTableColumn
hwMusaSrcFrcDlciType = _HwMusaSrcFrcDlciType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 12),
    _HwMusaSrcFrcDlciType_Type()
)
hwMusaSrcFrcDlciType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrcDlciType.setStatus("mandatory")


class _HwMusaSrcFrcIwfType_Type(Integer32):
    """Custom type hwMusaSrcFrcIwfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("network11", 0),
          ("networkN1", 3),
          ("service", 1))
    )


_HwMusaSrcFrcIwfType_Type.__name__ = "Integer32"
_HwMusaSrcFrcIwfType_Object = MibTableColumn
hwMusaSrcFrcIwfType = _HwMusaSrcFrcIwfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 13),
    _HwMusaSrcFrcIwfType_Type()
)
hwMusaSrcFrcIwfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrcIwfType.setStatus("mandatory")


class _HwMusaSrcFrcActiveStatus_Type(Integer32):
    """Custom type hwMusaSrcFrcActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_HwMusaSrcFrcActiveStatus_Type.__name__ = "Integer32"
_HwMusaSrcFrcActiveStatus_Object = MibTableColumn
hwMusaSrcFrcActiveStatus = _HwMusaSrcFrcActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 14),
    _HwMusaSrcFrcActiveStatus_Type()
)
hwMusaSrcFrcActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrcActiveStatus.setStatus("mandatory")
_HwMusaSrcFrcFreeBandwidth_Type = Integer32
_HwMusaSrcFrcFreeBandwidth_Object = MibTableColumn
hwMusaSrcFrcFreeBandwidth = _HwMusaSrcFrcFreeBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 15),
    _HwMusaSrcFrcFreeBandwidth_Type()
)
hwMusaSrcFrcFreeBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcFrcFreeBandwidth.setStatus("mandatory")
_HwMusaSrcApcConnectAttribute_Type = Integer32
_HwMusaSrcApcConnectAttribute_Object = MibTableColumn
hwMusaSrcApcConnectAttribute = _HwMusaSrcApcConnectAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 16),
    _HwMusaSrcApcConnectAttribute_Type()
)
hwMusaSrcApcConnectAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcApcConnectAttribute.setStatus("mandatory")
_HwMusaSrcCescV35N_Type = Integer32
_HwMusaSrcCescV35N_Object = MibTableColumn
hwMusaSrcCescV35N = _HwMusaSrcCescV35N_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 17),
    _HwMusaSrcCescV35N_Type()
)
hwMusaSrcCescV35N.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcCescV35N.setStatus("mandatory")
_HwMusaDestFrameId_Type = Integer32
_HwMusaDestFrameId_Object = MibTableColumn
hwMusaDestFrameId = _HwMusaDestFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 20),
    _HwMusaDestFrameId_Type()
)
hwMusaDestFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrameId.setStatus("mandatory")
_HwMusaDestSlotId_Type = Integer32
_HwMusaDestSlotId_Object = MibTableColumn
hwMusaDestSlotId = _HwMusaDestSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 21),
    _HwMusaDestSlotId_Type()
)
hwMusaDestSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestSlotId.setStatus("mandatory")
_HwMusaDestPortVlanVccId_Type = Integer32
_HwMusaDestPortVlanVccId_Object = MibTableColumn
hwMusaDestPortVlanVccId = _HwMusaDestPortVlanVccId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 22),
    _HwMusaDestPortVlanVccId_Type()
)
hwMusaDestPortVlanVccId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestPortVlanVccId.setStatus("mandatory")
_HwMusaDestOnuId_Type = Integer32
_HwMusaDestOnuId_Object = MibTableColumn
hwMusaDestOnuId = _HwMusaDestOnuId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 23),
    _HwMusaDestOnuId_Type()
)
hwMusaDestOnuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestOnuId.setStatus("mandatory")
_HwMusaDestBoardVpi_Type = Integer32
_HwMusaDestBoardVpi_Object = MibTableColumn
hwMusaDestBoardVpi = _HwMusaDestBoardVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 24),
    _HwMusaDestBoardVpi_Type()
)
hwMusaDestBoardVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestBoardVpi.setStatus("mandatory")
_HwMusaDestBoardVci_Type = Integer32
_HwMusaDestBoardVci_Object = MibTableColumn
hwMusaDestBoardVci = _HwMusaDestBoardVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 25),
    _HwMusaDestBoardVci_Type()
)
hwMusaDestBoardVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestBoardVci.setStatus("mandatory")


class _HwMusaDestPortType_Type(Integer32):
    """Custom type hwMusaDestPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdt", 1),
          ("udt", 2),
          ("uni", 0))
    )


_HwMusaDestPortType_Type.__name__ = "Integer32"
_HwMusaDestPortType_Object = MibTableColumn
hwMusaDestPortType = _HwMusaDestPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 26),
    _HwMusaDestPortType_Type()
)
hwMusaDestPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestPortType.setStatus("mandatory")
_HwMusaDestCescChannelId_Type = Integer32
_HwMusaDestCescChannelId_Object = MibTableColumn
hwMusaDestCescChannelId = _HwMusaDestCescChannelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 27),
    _HwMusaDestCescChannelId_Type()
)
hwMusaDestCescChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestCescChannelId.setStatus("mandatory")
_HwMusaDestCescChannelBitmap_Type = Integer32
_HwMusaDestCescChannelBitmap_Object = MibTableColumn
hwMusaDestCescChannelBitmap = _HwMusaDestCescChannelBitmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 28),
    _HwMusaDestCescChannelBitmap_Type()
)
hwMusaDestCescChannelBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestCescChannelBitmap.setStatus("mandatory")


class _HwMusaDestCescFillDegree_Type(Integer32):
    """Custom type hwMusaDestCescFillDegree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 47),
    )


_HwMusaDestCescFillDegree_Type.__name__ = "Integer32"
_HwMusaDestCescFillDegree_Object = MibTableColumn
hwMusaDestCescFillDegree = _HwMusaDestCescFillDegree_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 29),
    _HwMusaDestCescFillDegree_Type()
)
hwMusaDestCescFillDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestCescFillDegree.setStatus("mandatory")


class _HwMusaDestFrcDlciType_Type(Integer32):
    """Custom type hwMusaDestFrcDlciType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwMusaDestFrcDlciType_Type.__name__ = "Integer32"
_HwMusaDestFrcDlciType_Object = MibTableColumn
hwMusaDestFrcDlciType = _HwMusaDestFrcDlciType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 30),
    _HwMusaDestFrcDlciType_Type()
)
hwMusaDestFrcDlciType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrcDlciType.setStatus("mandatory")


class _HwMusaDestFrcIwfType_Type(Integer32):
    """Custom type hwMusaDestFrcIwfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("network11", 0),
          ("networkN1", 3),
          ("service", 1))
    )


_HwMusaDestFrcIwfType_Type.__name__ = "Integer32"
_HwMusaDestFrcIwfType_Object = MibTableColumn
hwMusaDestFrcIwfType = _HwMusaDestFrcIwfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 31),
    _HwMusaDestFrcIwfType_Type()
)
hwMusaDestFrcIwfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrcIwfType.setStatus("mandatory")


class _HwMusaDestFrcActiveStatus_Type(Integer32):
    """Custom type hwMusaDestFrcActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_HwMusaDestFrcActiveStatus_Type.__name__ = "Integer32"
_HwMusaDestFrcActiveStatus_Object = MibTableColumn
hwMusaDestFrcActiveStatus = _HwMusaDestFrcActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 32),
    _HwMusaDestFrcActiveStatus_Type()
)
hwMusaDestFrcActiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrcActiveStatus.setStatus("mandatory")
_HwMusaDestFrcFreeBandwidth_Type = Integer32
_HwMusaDestFrcFreeBandwidth_Object = MibTableColumn
hwMusaDestFrcFreeBandwidth = _HwMusaDestFrcFreeBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 33),
    _HwMusaDestFrcFreeBandwidth_Type()
)
hwMusaDestFrcFreeBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestFrcFreeBandwidth.setStatus("mandatory")
_HwMusaDestApcConnectAttribute_Type = Integer32
_HwMusaDestApcConnectAttribute_Object = MibTableColumn
hwMusaDestApcConnectAttribute = _HwMusaDestApcConnectAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 34),
    _HwMusaDestApcConnectAttribute_Type()
)
hwMusaDestApcConnectAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestApcConnectAttribute.setStatus("mandatory")
_HwMusaDestCescV35N_Type = Integer32
_HwMusaDestCescV35N_Object = MibTableColumn
hwMusaDestCescV35N = _HwMusaDestCescV35N_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 35),
    _HwMusaDestCescV35N_Type()
)
hwMusaDestCescV35N.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestCescV35N.setStatus("mandatory")
_HwMusaSrcToDestTraffic_Type = Integer32
_HwMusaSrcToDestTraffic_Object = MibTableColumn
hwMusaSrcToDestTraffic = _HwMusaSrcToDestTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 38),
    _HwMusaSrcToDestTraffic_Type()
)
hwMusaSrcToDestTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaSrcToDestTraffic.setStatus("mandatory")
_HwMusaDestToSrcTraffic_Type = Integer32
_HwMusaDestToSrcTraffic_Object = MibTableColumn
hwMusaDestToSrcTraffic = _HwMusaDestToSrcTraffic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 39),
    _HwMusaDestToSrcTraffic_Type()
)
hwMusaDestToSrcTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaDestToSrcTraffic.setStatus("mandatory")


class _HwMusaAllPvcOperater_Type(Integer32):
    """Custom type hwMusaAllPvcOperater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaAllPvcOperater_Type.__name__ = "Integer32"
_HwMusaAllPvcOperater_Object = MibTableColumn
hwMusaAllPvcOperater = _HwMusaAllPvcOperater_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 40),
    _HwMusaAllPvcOperater_Type()
)
hwMusaAllPvcOperater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaAllPvcOperater.setStatus("mandatory")


class _HwMusaTypeOfPvcPvp_Type(Integer32):
    """Custom type hwMusaTypeOfPvcPvp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 0),
          ("pvp", 1))
    )


_HwMusaTypeOfPvcPvp_Type.__name__ = "Integer32"
_HwMusaTypeOfPvcPvp_Object = MibTableColumn
hwMusaTypeOfPvcPvp = _HwMusaTypeOfPvcPvp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 41),
    _HwMusaTypeOfPvcPvp_Type()
)
hwMusaTypeOfPvcPvp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaTypeOfPvcPvp.setStatus("mandatory")


class _HwMusaPvcPvpState_Type(Integer32):
    """Custom type hwMusaPvcPvpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("invalid", 2),
          ("normal", 1))
    )


_HwMusaPvcPvpState_Type.__name__ = "Integer32"
_HwMusaPvcPvpState_Object = MibTableColumn
hwMusaPvcPvpState = _HwMusaPvcPvpState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 22, 1, 42),
    _HwMusaPvcPvpState_Type()
)
hwMusaPvcPvpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPvcPvpState.setStatus("mandatory")
_HwMusaPvcCidTable_Object = MibTable
hwMusaPvcCidTable = _HwMusaPvcCidTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 23)
)
if mibBuilder.loadTexts:
    hwMusaPvcCidTable.setStatus("mandatory")
_HwMusaPvcCidEntry_Object = MibTableRow
hwMusaPvcCidEntry = _HwMusaPvcCidEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 23, 1)
)
hwMusaPvcCidEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSrcPortVlanVccId"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSrcOnuId"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSrcBoardVpi"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSrcBoardVci"),
)
if mibBuilder.loadTexts:
    hwMusaPvcCidEntry.setStatus("mandatory")
_HwMusaPvcCid_Type = Counter32
_HwMusaPvcCid_Object = MibTableColumn
hwMusaPvcCid = _HwMusaPvcCid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 23, 1, 1),
    _HwMusaPvcCid_Type()
)
hwMusaPvcCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaPvcCid.setStatus("mandatory")
_HwMusaPatchOperateTable_Object = MibTable
hwMusaPatchOperateTable = _HwMusaPatchOperateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24)
)
if mibBuilder.loadTexts:
    hwMusaPatchOperateTable.setStatus("mandatory")
_HwMusaPatchOperateEntry_Object = MibTableRow
hwMusaPatchOperateEntry = _HwMusaPatchOperateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1)
)
hwMusaPatchOperateEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaPatchIdIndex"),
)
if mibBuilder.loadTexts:
    hwMusaPatchOperateEntry.setStatus("mandatory")
_HwMusaPatchIdIndex_Type = Integer32
_HwMusaPatchIdIndex_Object = MibTableColumn
hwMusaPatchIdIndex = _HwMusaPatchIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1, 1),
    _HwMusaPatchIdIndex_Type()
)
hwMusaPatchIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaPatchIdIndex.setStatus("mandatory")


class _HwMusaPatchLoadProtocol_Type(Integer32):
    """Custom type hwMusaPatchLoadProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tftp", 1)
    )


_HwMusaPatchLoadProtocol_Type.__name__ = "Integer32"
_HwMusaPatchLoadProtocol_Object = MibTableColumn
hwMusaPatchLoadProtocol = _HwMusaPatchLoadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1, 2),
    _HwMusaPatchLoadProtocol_Type()
)
hwMusaPatchLoadProtocol.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaPatchLoadProtocol.setStatus("mandatory")
_HwMusaPatchLoadFilename_Type = DisplayString
_HwMusaPatchLoadFilename_Object = MibTableColumn
hwMusaPatchLoadFilename = _HwMusaPatchLoadFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1, 3),
    _HwMusaPatchLoadFilename_Type()
)
hwMusaPatchLoadFilename.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaPatchLoadFilename.setStatus("mandatory")
_HwMusaPatchLoadSerIp_Type = IpAddress
_HwMusaPatchLoadSerIp_Object = MibTableColumn
hwMusaPatchLoadSerIp = _HwMusaPatchLoadSerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1, 4),
    _HwMusaPatchLoadSerIp_Type()
)
hwMusaPatchLoadSerIp.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaPatchLoadSerIp.setStatus("mandatory")


class _HwMusaPatchOper_Type(Integer32):
    """Custom type hwMusaPatchOper based on Integer32"""
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
        *(("activate", 1),
          ("deactivate", 2),
          ("load", 3),
          ("remove", 4),
          ("run", 5))
    )


_HwMusaPatchOper_Type.__name__ = "Integer32"
_HwMusaPatchOper_Object = MibTableColumn
hwMusaPatchOper = _HwMusaPatchOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 24, 1, 5),
    _HwMusaPatchOper_Type()
)
hwMusaPatchOper.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaPatchOper.setStatus("mandatory")
_HwMusaPatchTable_Object = MibTable
hwMusaPatchTable = _HwMusaPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25)
)
if mibBuilder.loadTexts:
    hwMusaPatchTable.setStatus("mandatory")
_HwMusaPatchEntry_Object = MibTableRow
hwMusaPatchEntry = _HwMusaPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1)
)
hwMusaPatchEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaPatchIdIndex"),
)
if mibBuilder.loadTexts:
    hwMusaPatchEntry.setStatus("mandatory")
_HwMusaPatchShowIdIndex_Type = Integer32
_HwMusaPatchShowIdIndex_Object = MibTableColumn
hwMusaPatchShowIdIndex = _HwMusaPatchShowIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 1),
    _HwMusaPatchShowIdIndex_Type()
)
hwMusaPatchShowIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaPatchShowIdIndex.setStatus("mandatory")
_HwMusaPatchCRC_Type = Integer32
_HwMusaPatchCRC_Object = MibTableColumn
hwMusaPatchCRC = _HwMusaPatchCRC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 2),
    _HwMusaPatchCRC_Type()
)
hwMusaPatchCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchCRC.setStatus("mandatory")


class _HwMusaPatchType_Type(Integer32):
    """Custom type hwMusaPatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("c-Commonpatch", 1),
          ("t-Temporarypatch", 2))
    )


_HwMusaPatchType_Type.__name__ = "Integer32"
_HwMusaPatchType_Object = MibTableColumn
hwMusaPatchType = _HwMusaPatchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 3),
    _HwMusaPatchType_Type()
)
hwMusaPatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchType.setStatus("mandatory")


class _HwMusaPatchState_Type(Integer32):
    """Custom type hwMusaPatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("deactivate", 3),
          ("run", 1))
    )


_HwMusaPatchState_Type.__name__ = "Integer32"
_HwMusaPatchState_Object = MibTableColumn
hwMusaPatchState = _HwMusaPatchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 4),
    _HwMusaPatchState_Type()
)
hwMusaPatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchState.setStatus("mandatory")
_HwMusaPatchCodeAddress_Type = Integer32
_HwMusaPatchCodeAddress_Object = MibTableColumn
hwMusaPatchCodeAddress = _HwMusaPatchCodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 5),
    _HwMusaPatchCodeAddress_Type()
)
hwMusaPatchCodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchCodeAddress.setStatus("mandatory")
_HwMusaPatchCodeLength_Type = Integer32
_HwMusaPatchCodeLength_Object = MibTableColumn
hwMusaPatchCodeLength = _HwMusaPatchCodeLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 6),
    _HwMusaPatchCodeLength_Type()
)
hwMusaPatchCodeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchCodeLength.setStatus("mandatory")
_HwMusaPatchDataAddress_Type = Integer32
_HwMusaPatchDataAddress_Object = MibTableColumn
hwMusaPatchDataAddress = _HwMusaPatchDataAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 7),
    _HwMusaPatchDataAddress_Type()
)
hwMusaPatchDataAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchDataAddress.setStatus("mandatory")
_HwMusaPatchDataLength_Type = Integer32
_HwMusaPatchDataLength_Object = MibTableColumn
hwMusaPatchDataLength = _HwMusaPatchDataLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 8),
    _HwMusaPatchDataLength_Type()
)
hwMusaPatchDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchDataLength.setStatus("mandatory")
_HwMusaPatchFunctionNumber_Type = Integer32
_HwMusaPatchFunctionNumber_Object = MibTableColumn
hwMusaPatchFunctionNumber = _HwMusaPatchFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 1, 25, 1, 9),
    _HwMusaPatchFunctionNumber_Type()
)
hwMusaPatchFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaPatchFunctionNumber.setStatus("mandatory")
_HwMusaEndOfMib_ObjectIdentity = ObjectIdentity
hwMusaEndOfMib = _HwMusaEndOfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 100)
)
_HwMa5100EndOfMib_Type = Integer32
_HwMa5100EndOfMib_Object = MibScalar
hwMa5100EndOfMib = _HwMa5100EndOfMib_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 100, 1),
    _HwMa5100EndOfMib_Type()
)
hwMa5100EndOfMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMa5100EndOfMib.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MUSA-MA5100-MIB",
    **{"DisplayString": DisplayString,
       "hwMa5100Mib": hwMa5100Mib,
       "hwMusaSysMib": hwMusaSysMib,
       "hwMusaDevice": hwMusaDevice,
       "hwMusaSysDate": hwMusaSysDate,
       "hwMusaSysTime": hwMusaSysTime,
       "hwMusaSysCpuRatio": hwMusaSysCpuRatio,
       "hwMusaHostVersion": hwMusaHostVersion,
       "hwMusaResetSys": hwMusaResetSys,
       "hwMusaIpAddr": hwMusaIpAddr,
       "hwMusaIpMask": hwMusaIpMask,
       "hwMusaGatewayIpAddr": hwMusaGatewayIpAddr,
       "hwMusaMacAddr": hwMusaMacAddr,
       "hwMusaIpAddrPermitTable": hwMusaIpAddrPermitTable,
       "hwMusaIpAddrPermitEntry": hwMusaIpAddrPermitEntry,
       "hwMusaIpPermitTableId": hwMusaIpPermitTableId,
       "hwMusaIpAddrPermitOper": hwMusaIpAddrPermitOper,
       "hwMusaPermitBeginIp": hwMusaPermitBeginIp,
       "hwMusaPermitEndIp": hwMusaPermitEndIp,
       "hwMusaPermitIpMask": hwMusaPermitIpMask,
       "hwMusaIpAddrRejectTable": hwMusaIpAddrRejectTable,
       "hwMusaIpAddrRejectEntry": hwMusaIpAddrRejectEntry,
       "hwMusaIpRejectTableId": hwMusaIpRejectTableId,
       "hwMusaIpAddrRejectOper": hwMusaIpAddrRejectOper,
       "hwMusaRejectBeginIp": hwMusaRejectBeginIp,
       "hwMusaRejectEndIp": hwMusaRejectEndIp,
       "hwMusaRejectIpMask": hwMusaRejectIpMask,
       "hwMusaAtmIpAddr": hwMusaAtmIpAddr,
       "hwMusaAtmIpMask": hwMusaAtmIpMask,
       "hwMusaMtu": hwMusaMtu,
       "hwMusaOpticConvergentRate": hwMusaOpticConvergentRate,
       "hwMusaCellbusID": hwMusaCellbusID,
       "hwMusaResetSlaveMMX": hwMusaResetSlaveMMX,
       "hwMusaBiosVersion": hwMusaBiosVersion,
       "hwMusaEthernetFirewall": hwMusaEthernetFirewall,
       "hwMusaNmsPvcConfTable": hwMusaNmsPvcConfTable,
       "hwMusaNmsPvcConfEntry": hwMusaNmsPvcConfEntry,
       "hwMusaNmsPvcIndex": hwMusaNmsPvcIndex,
       "hwMusaNmsRelayVpi": hwMusaNmsRelayVpi,
       "hwMusaNmsRelayVci": hwMusaNmsRelayVci,
       "hwMusaNmsIp": hwMusaNmsIp,
       "hwMusaNmsPvcOper": hwMusaNmsPvcOper,
       "hwMusaNmsRxTraffic": hwMusaNmsRxTraffic,
       "hwMusaNmsTxTraffic": hwMusaNmsTxTraffic,
       "hwMusaNmsSarVci": hwMusaNmsSarVci,
       "hwMusaNmsLLCVC": hwMusaNmsLLCVC,
       "hwMusaNmsENCAP": hwMusaNmsENCAP,
       "hwMusaNmsFrameId": hwMusaNmsFrameId,
       "hwMusaNmsSlotId": hwMusaNmsSlotId,
       "hwMusaNmsPortVlanId": hwMusaNmsPortVlanId,
       "hwMusaNmsParaConfTable": hwMusaNmsParaConfTable,
       "hwMusaNmsParaConfEntry": hwMusaNmsParaConfEntry,
       "hwMusaNmsID": hwMusaNmsID,
       "hwMusaNmsOperState": hwMusaNmsOperState,
       "hwMusaNmsName": hwMusaNmsName,
       "hwMusaNmsIpAddr": hwMusaNmsIpAddr,
       "hwMusaGetCommunity": hwMusaGetCommunity,
       "hwMusaSetCommunity": hwMusaSetCommunity,
       "hwMusaTrapPort": hwMusaTrapPort,
       "hwMusaGetSetPort": hwMusaGetSetPort,
       "hwMusaNmsStatus": hwMusaNmsStatus,
       "hwMusaNmsStyle": hwMusaNmsStyle,
       "hwMusaSlotGroup": hwMusaSlotGroup,
       "hwMusaShelf": hwMusaShelf,
       "hwMusaShelfNumber": hwMusaShelfNumber,
       "hwMusaShelfConfTable": hwMusaShelfConfTable,
       "hwMusaShelfConfEntry": hwMusaShelfConfEntry,
       "hwMusaShelfIndex": hwMusaShelfIndex,
       "hwMusaShelfType": hwMusaShelfType,
       "hwMusaShelfName": hwMusaShelfName,
       "hwMusaFrameNumbers": hwMusaFrameNumbers,
       "hwMusaFrame": hwMusaFrame,
       "hwMusaFrameNumber": hwMusaFrameNumber,
       "hwMusaFrameConfTable": hwMusaFrameConfTable,
       "hwMusaFrameConfEntry": hwMusaFrameConfEntry,
       "hwMusaFrameIndex": hwMusaFrameIndex,
       "hwMusaFrameType": hwMusaFrameType,
       "hwMusaFrameName": hwMusaFrameName,
       "hwMusaSlotNumbers": hwMusaSlotNumbers,
       "hwMusaFrameBandWidth": hwMusaFrameBandWidth,
       "hwMusaFrameUsedBandWidth": hwMusaFrameUsedBandWidth,
       "hwMusaSlot": hwMusaSlot,
       "hwMusaSlotNumber": hwMusaSlotNumber,
       "hwMusaSlotConfTable": hwMusaSlotConfTable,
       "hwMusaSlotConfEntry": hwMusaSlotConfEntry,
       "hwMusaSlotIndex": hwMusaSlotIndex,
       "hwMusaSlotCardType": hwMusaSlotCardType,
       "hwMusaSlotCardSerial": hwMusaSlotCardSerial,
       "hwMusaSlotCardVersion": hwMusaSlotCardVersion,
       "hwMusaSlotIpAddress": hwMusaSlotIpAddress,
       "hwMusaSlotCardAdminStatus": hwMusaSlotCardAdminStatus,
       "hwMusaSlotCardOperStatus": hwMusaSlotCardOperStatus,
       "hwMusaSlotDescript": hwMusaSlotDescript,
       "hwMusaBoardCellLossPriority": hwMusaBoardCellLossPriority,
       "hwMusaBoardMaxBandwidth": hwMusaBoardMaxBandwidth,
       "hwMusaCpuOccupyRate": hwMusaCpuOccupyRate,
       "hwMusaQueryMemory": hwMusaQueryMemory,
       "hwMusaLoadProtocol": hwMusaLoadProtocol,
       "hwMusaLoadContent": hwMusaLoadContent,
       "hwMusaLoadTftpServerIp": hwMusaLoadTftpServerIp,
       "hwMusaLoadFileName": hwMusaLoadFileName,
       "hwMusaLoadOperType": hwMusaLoadOperType,
       "hwMusaSlotUpBandWidth": hwMusaSlotUpBandWidth,
       "hwMusaSlotDownBandWidth": hwMusaSlotDownBandWidth,
       "hwMusaSlotUsedUpBandWidth": hwMusaSlotUsedUpBandWidth,
       "hwMusaSlotUsedDownBandWidth": hwMusaSlotUsedDownBandWidth,
       "hwMusaSlotUpPracticalBandWidth": hwMusaSlotUpPracticalBandWidth,
       "hwMusaSlotDownPracticalBandWidth": hwMusaSlotDownPracticalBandWidth,
       "hwMusaOamGroup": hwMusaOamGroup,
       "hwMusaOimPhyTable": hwMusaOimPhyTable,
       "hwMusaOimPhyEntry": hwMusaOimPhyEntry,
       "hwOIMPortIndex": hwOIMPortIndex,
       "hwMusaSetSrcLoop": hwMusaSetSrcLoop,
       "hwMusaSetLineLoop": hwMusaSetLineLoop,
       "hwMusaSetUtopiaLoop": hwMusaSetUtopiaLoop,
       "hwMusaInsertLOF": hwMusaInsertLOF,
       "hwMusaInsertLOS": hwMusaInsertLOS,
       "hwMusaInsertBIP1": hwMusaInsertBIP1,
       "hwMusaInsertBIP2": hwMusaInsertBIP2,
       "hwMusaInsertBIP3": hwMusaInsertBIP3,
       "hwMusaInsertLAIS": hwMusaInsertLAIS,
       "hwMusaInsertPAIS": hwMusaInsertPAIS,
       "hwMusaInsertLRDI": hwMusaInsertLRDI,
       "hwMusaOimOpticTable": hwMusaOimOpticTable,
       "hwMusaOimOpticEntry": hwMusaOimOpticEntry,
       "hwMusaQueryCurBIP1": hwMusaQueryCurBIP1,
       "hwMusaQueryCurBIP2": hwMusaQueryCurBIP2,
       "hwMusaQueryCurBIP3": hwMusaQueryCurBIP3,
       "hwMusaQueryCurLFEBE": hwMusaQueryCurLFEBE,
       "hwMusaQueryCurPFEBE": hwMusaQueryCurPFEBE,
       "hwMusaQueryCurSendCellNum": hwMusaQueryCurSendCellNum,
       "hwMusaQueryCurReceiveCellNum": hwMusaQueryCurReceiveCellNum,
       "hwMusaQueryCurCorrectHECNum": hwMusaQueryCurCorrectHECNum,
       "hwMusaQueryCurNonCorrectHECNum": hwMusaQueryCurNonCorrectHECNum,
       "hwMusaQueryCurLOCDNum": hwMusaQueryCurLOCDNum,
       "hwMusaQueryCurUnmatchCellNum": hwMusaQueryCurUnmatchCellNum,
       "hwMusaQueryCurOOFNum": hwMusaQueryCurOOFNum,
       "hwMusaClearAllAlarmStat": hwMusaClearAllAlarmStat,
       "hwMusaClearOIMErrEventStat": hwMusaClearOIMErrEventStat,
       "hwMusaWarningCtrlTable": hwMusaWarningCtrlTable,
       "hwMusaWarningCtrlEntry": hwMusaWarningCtrlEntry,
       "hwMusaWarningID": hwMusaWarningID,
       "hwMusaWarningLevel": hwMusaWarningLevel,
       "hwMusaWarningNmsCtrl": hwMusaWarningNmsCtrl,
       "hwMusaWarningTerminalCtrl": hwMusaWarningTerminalCtrl,
       "hwMusaWarningIsCount": hwMusaWarningIsCount,
       "hwMusaWarn15MinThreshold": hwMusaWarn15MinThreshold,
       "hwMusaWarn24HourThreshold": hwMusaWarn24HourThreshold,
       "hwMusaWarningDesc": hwMusaWarningDesc,
       "hwMusaWarningEngDesc": hwMusaWarningEngDesc,
       "hwMusaSysRouteTable": hwMusaSysRouteTable,
       "hwMusaSysRouteEntry": hwMusaSysRouteEntry,
       "hwMusaSysRouteIndex": hwMusaSysRouteIndex,
       "hwMusaDstIp": hwMusaDstIp,
       "hwMusaDstIpMask": hwMusaDstIpMask,
       "hwMusaGateIp": hwMusaGateIp,
       "hwMusaSysRouteOper": hwMusaSysRouteOper,
       "hwMusaLoadRateTable": hwMusaLoadRateTable,
       "hwMusaLoadRateEntry": hwMusaLoadRateEntry,
       "hwMusaLoadRate": hwMusaLoadRate,
       "hwMusaLoadType": hwMusaLoadType,
       "hwMusaTrafficTable": hwMusaTrafficTable,
       "hwMusaTrafficEntry": hwMusaTrafficEntry,
       "hwMusaTrafficIndex": hwMusaTrafficIndex,
       "hwMusaTrafficType": hwMusaTrafficType,
       "hwMusaServiceClass": hwMusaServiceClass,
       "hwMusaRefCount": hwMusaRefCount,
       "hwMusaRecordState": hwMusaRecordState,
       "hwMusaClp01pcr": hwMusaClp01pcr,
       "hwMusaClp0pcr": hwMusaClp0pcr,
       "hwMusaClp01scr": hwMusaClp01scr,
       "hwMusaClp0scr": hwMusaClp0scr,
       "hwMusaMbs": hwMusaMbs,
       "hwMusaMcr": hwMusaMcr,
       "hwMusaCDVT": hwMusaCDVT,
       "hwMusaOperat": hwMusaOperat,
       "hwMusaNextTrafficIndex": hwMusaNextTrafficIndex,
       "hwMusaCampusPvcConfTable": hwMusaCampusPvcConfTable,
       "hwMusaCampusPvcConfEntry": hwMusaCampusPvcConfEntry,
       "hwMusaVlanId": hwMusaVlanId,
       "hwMusaVlanIciIndex": hwMusaVlanIciIndex,
       "hwMusaAdlPortCount": hwMusaAdlPortCount,
       "hwMusaAdlFrameId": hwMusaAdlFrameId,
       "hwMusaAdlSlotId": hwMusaAdlSlotId,
       "hwMusaAdlPortId": hwMusaAdlPortId,
       "hwMusaAdlVpi": hwMusaAdlVpi,
       "hwMusaAdlVci": hwMusaAdlVci,
       "hwMusaToLanTrafficId": hwMusaToLanTrafficId,
       "hwMusaFromLanTrafficId": hwMusaFromLanTrafficId,
       "hwMusaAdlPortOperat": hwMusaAdlPortOperat,
       "hwMusaOpticBandwidthTable": hwMusaOpticBandwidthTable,
       "hwMusaOpticBandwidthEntry": hwMusaOpticBandwidthEntry,
       "hwMusaUpOpticMainBandWidth": hwMusaUpOpticMainBandWidth,
       "hwMusaDnOpticMainBandWidth": hwMusaDnOpticMainBandWidth,
       "hwMusaCurUsedUpBandWidth": hwMusaCurUsedUpBandWidth,
       "hwMusaCurUsedDownBandWidth": hwMusaCurUsedDownBandWidth,
       "hwMusaUpReservedBandWidth": hwMusaUpReservedBandWidth,
       "hwMusaDownReservedBandWidth": hwMusaDownReservedBandWidth,
       "hwMusaUpPracticalBandWidth": hwMusaUpPracticalBandWidth,
       "hwMusaDownPracticalBandWidth": hwMusaDownPracticalBandWidth,
       "hwMusaTrafficCbrPcrTable": hwMusaTrafficCbrPcrTable,
       "hwMusaTrafficCbrPcrEntry": hwMusaTrafficCbrPcrEntry,
       "hwMusaCbrPcrIndex": hwMusaCbrPcrIndex,
       "hwMusaCbrPcrValue": hwMusaCbrPcrValue,
       "hwMusaCbrPcrRefCount": hwMusaCbrPcrRefCount,
       "hwMusaTrafficRtvbrScrTable": hwMusaTrafficRtvbrScrTable,
       "hwMusaTrafficRtvbrScrEntry": hwMusaTrafficRtvbrScrEntry,
       "hwMusaRtvbrScrIndex": hwMusaRtvbrScrIndex,
       "hwMusaRtvbrScrValue": hwMusaRtvbrScrValue,
       "hwMusaRtvbrScrRefCount": hwMusaRtvbrScrRefCount,
       "hwMusaPvcTrafficStatisTable": hwMusaPvcTrafficStatisTable,
       "hwMusaPvcTrafficStatisEntry": hwMusaPvcTrafficStatisEntry,
       "hwMusaUpStreamTrafficRx": hwMusaUpStreamTrafficRx,
       "hwMusaUpStreamTrafficTx": hwMusaUpStreamTrafficTx,
       "hwMusaDownStreamTrafficRx": hwMusaDownStreamTrafficRx,
       "hwMusaDownStreamTrafficTx": hwMusaDownStreamTrafficTx,
       "hwMusaAllPvcConfTable": hwMusaAllPvcConfTable,
       "hwMusaAllPvcConfEntry": hwMusaAllPvcConfEntry,
       "hwMusaCidIndex": hwMusaCidIndex,
       "hwMusaSrcFrameId": hwMusaSrcFrameId,
       "hwMuasSrcSlotId": hwMuasSrcSlotId,
       "hwMusaSrcPortVlanVccId": hwMusaSrcPortVlanVccId,
       "hwMusaSrcOnuId": hwMusaSrcOnuId,
       "hwMusaSrcBoardVpi": hwMusaSrcBoardVpi,
       "hwMusaSrcBoardVci": hwMusaSrcBoardVci,
       "hwMusaSrcPortType": hwMusaSrcPortType,
       "hwMusaSrcCescChannelId": hwMusaSrcCescChannelId,
       "hwMusaSrcCescChannelBitmap": hwMusaSrcCescChannelBitmap,
       "hwMusaSrcCescFillDegree": hwMusaSrcCescFillDegree,
       "hwMusaSrcFrcDlciType": hwMusaSrcFrcDlciType,
       "hwMusaSrcFrcIwfType": hwMusaSrcFrcIwfType,
       "hwMusaSrcFrcActiveStatus": hwMusaSrcFrcActiveStatus,
       "hwMusaSrcFrcFreeBandwidth": hwMusaSrcFrcFreeBandwidth,
       "hwMusaSrcApcConnectAttribute": hwMusaSrcApcConnectAttribute,
       "hwMusaSrcCescV35N": hwMusaSrcCescV35N,
       "hwMusaDestFrameId": hwMusaDestFrameId,
       "hwMusaDestSlotId": hwMusaDestSlotId,
       "hwMusaDestPortVlanVccId": hwMusaDestPortVlanVccId,
       "hwMusaDestOnuId": hwMusaDestOnuId,
       "hwMusaDestBoardVpi": hwMusaDestBoardVpi,
       "hwMusaDestBoardVci": hwMusaDestBoardVci,
       "hwMusaDestPortType": hwMusaDestPortType,
       "hwMusaDestCescChannelId": hwMusaDestCescChannelId,
       "hwMusaDestCescChannelBitmap": hwMusaDestCescChannelBitmap,
       "hwMusaDestCescFillDegree": hwMusaDestCescFillDegree,
       "hwMusaDestFrcDlciType": hwMusaDestFrcDlciType,
       "hwMusaDestFrcIwfType": hwMusaDestFrcIwfType,
       "hwMusaDestFrcActiveStatus": hwMusaDestFrcActiveStatus,
       "hwMusaDestFrcFreeBandwidth": hwMusaDestFrcFreeBandwidth,
       "hwMusaDestApcConnectAttribute": hwMusaDestApcConnectAttribute,
       "hwMusaDestCescV35N": hwMusaDestCescV35N,
       "hwMusaSrcToDestTraffic": hwMusaSrcToDestTraffic,
       "hwMusaDestToSrcTraffic": hwMusaDestToSrcTraffic,
       "hwMusaAllPvcOperater": hwMusaAllPvcOperater,
       "hwMusaTypeOfPvcPvp": hwMusaTypeOfPvcPvp,
       "hwMusaPvcPvpState": hwMusaPvcPvpState,
       "hwMusaPvcCidTable": hwMusaPvcCidTable,
       "hwMusaPvcCidEntry": hwMusaPvcCidEntry,
       "hwMusaPvcCid": hwMusaPvcCid,
       "hwMusaPatchOperateTable": hwMusaPatchOperateTable,
       "hwMusaPatchOperateEntry": hwMusaPatchOperateEntry,
       "hwMusaPatchIdIndex": hwMusaPatchIdIndex,
       "hwMusaPatchLoadProtocol": hwMusaPatchLoadProtocol,
       "hwMusaPatchLoadFilename": hwMusaPatchLoadFilename,
       "hwMusaPatchLoadSerIp": hwMusaPatchLoadSerIp,
       "hwMusaPatchOper": hwMusaPatchOper,
       "hwMusaPatchTable": hwMusaPatchTable,
       "hwMusaPatchEntry": hwMusaPatchEntry,
       "hwMusaPatchShowIdIndex": hwMusaPatchShowIdIndex,
       "hwMusaPatchCRC": hwMusaPatchCRC,
       "hwMusaPatchType": hwMusaPatchType,
       "hwMusaPatchState": hwMusaPatchState,
       "hwMusaPatchCodeAddress": hwMusaPatchCodeAddress,
       "hwMusaPatchCodeLength": hwMusaPatchCodeLength,
       "hwMusaPatchDataAddress": hwMusaPatchDataAddress,
       "hwMusaPatchDataLength": hwMusaPatchDataLength,
       "hwMusaPatchFunctionNumber": hwMusaPatchFunctionNumber,
       "hwMusaEndOfMib": hwMusaEndOfMib,
       "hwMa5100EndOfMib": hwMa5100EndOfMib}
)
