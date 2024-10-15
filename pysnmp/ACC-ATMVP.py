# SNMP MIB module (ACC-ATMVP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ATMVP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:52 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accSysInfo,
 accTrapLogSeqNum) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accSysInfo",
    "accTrapLogSeqNum")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccAtmVp_ObjectIdentity = ObjectIdentity
accAtmVp = _AccAtmVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73)
)
_AccVpTable_Object = MibTable
accVpTable = _AccVpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1)
)
if mibBuilder.loadTexts:
    accVpTable.setStatus("mandatory")
_AccVpEntry_Object = MibTableRow
accVpEntry = _AccVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1)
)
accVpEntry.setIndexNames(
    (0, "ACC-ATMVP", "oVirtualPortName"),
)
if mibBuilder.loadTexts:
    accVpEntry.setStatus("mandatory")
_OVirtualPortName_Type = IfIndex
_OVirtualPortName_Object = MibTableColumn
oVirtualPortName = _OVirtualPortName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 1),
    _OVirtualPortName_Type()
)
oVirtualPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortName.setStatus("mandatory")


class _OVirtualPortAdminState_Type(Integer32):
    """Custom type oVirtualPortAdminState based on Integer32"""
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


_OVirtualPortAdminState_Type.__name__ = "Integer32"
_OVirtualPortAdminState_Object = MibTableColumn
oVirtualPortAdminState = _OVirtualPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 2),
    _OVirtualPortAdminState_Type()
)
oVirtualPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortAdminState.setStatus("mandatory")


class _OVirtualPortOperState_Type(Integer32):
    """Custom type oVirtualPortOperState based on Integer32"""
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


_OVirtualPortOperState_Type.__name__ = "Integer32"
_OVirtualPortOperState_Object = MibTableColumn
oVirtualPortOperState = _OVirtualPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 3),
    _OVirtualPortOperState_Type()
)
oVirtualPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortOperState.setStatus("mandatory")


class _OVirtualPortProtocol_Type(Integer32):
    """Custom type oVirtualPortProtocol based on Integer32"""
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
        *(("cip", 4),
          ("frf5", 6),
          ("lane", 2),
          ("none", 1),
          ("ppp", 5),
          ("rfc1483", 3))
    )


_OVirtualPortProtocol_Type.__name__ = "Integer32"
_OVirtualPortProtocol_Object = MibTableColumn
oVirtualPortProtocol = _OVirtualPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 4),
    _OVirtualPortProtocol_Type()
)
oVirtualPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortProtocol.setStatus("mandatory")


class _OVirtualPortQueueMode_Type(Integer32):
    """Custom type oVirtualPortQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("express", 1)
    )


_OVirtualPortQueueMode_Type.__name__ = "Integer32"
_OVirtualPortQueueMode_Object = MibTableColumn
oVirtualPortQueueMode = _OVirtualPortQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 5),
    _OVirtualPortQueueMode_Type()
)
oVirtualPortQueueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortQueueMode.setStatus("mandatory")
_OVirtualPortCongestion_Type = Integer32
_OVirtualPortCongestion_Object = MibTableColumn
oVirtualPortCongestion = _OVirtualPortCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 6),
    _OVirtualPortCongestion_Type()
)
oVirtualPortCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortCongestion.setStatus("mandatory")
_OVirtualPortPhysicalPort_Type = Integer32
_OVirtualPortPhysicalPort_Object = MibTableColumn
oVirtualPortPhysicalPort = _OVirtualPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 1, 1, 7),
    _OVirtualPortPhysicalPort_Type()
)
oVirtualPortPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVirtualPortPhysicalPort.setStatus("mandatory")
_AccAtmVpScalarGrp_ObjectIdentity = ObjectIdentity
accAtmVpScalarGrp = _AccAtmVpScalarGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2)
)
_OVirtualPortCount1483Br_Type = Integer32
_OVirtualPortCount1483Br_Object = MibScalar
oVirtualPortCount1483Br = _OVirtualPortCount1483Br_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 1),
    _OVirtualPortCount1483Br_Type()
)
oVirtualPortCount1483Br.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCount1483Br.setStatus("mandatory")
_OVirtualPortCountCIP_Type = Integer32
_OVirtualPortCountCIP_Object = MibScalar
oVirtualPortCountCIP = _OVirtualPortCountCIP_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 2),
    _OVirtualPortCountCIP_Type()
)
oVirtualPortCountCIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountCIP.setStatus("mandatory")
_OVirtualPortCountTunnel_Type = Integer32
_OVirtualPortCountTunnel_Object = MibScalar
oVirtualPortCountTunnel = _OVirtualPortCountTunnel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 3),
    _OVirtualPortCountTunnel_Type()
)
oVirtualPortCountTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountTunnel.setStatus("mandatory")
_OVirtualPortCountFrf_Type = Integer32
_OVirtualPortCountFrf_Object = MibScalar
oVirtualPortCountFrf = _OVirtualPortCountFrf_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 4),
    _OVirtualPortCountFrf_Type()
)
oVirtualPortCountFrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountFrf.setStatus("mandatory")
_OVirtualPortCountPpp_Type = Integer32
_OVirtualPortCountPpp_Object = MibScalar
oVirtualPortCountPpp = _OVirtualPortCountPpp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 6),
    _OVirtualPortCountPpp_Type()
)
oVirtualPortCountPpp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountPpp.setStatus("mandatory")
_OVirtualPortCountVFR_Type = Integer32
_OVirtualPortCountVFR_Object = MibScalar
oVirtualPortCountVFR = _OVirtualPortCountVFR_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 7),
    _OVirtualPortCountVFR_Type()
)
oVirtualPortCountVFR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountVFR.setStatus("mandatory")
_OVirtualPortCountXOT_Type = Integer32
_OVirtualPortCountXOT_Object = MibScalar
oVirtualPortCountXOT = _OVirtualPortCountXOT_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 2, 8),
    _OVirtualPortCountXOT_Type()
)
oVirtualPortCountXOT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVirtualPortCountXOT.setStatus("mandatory")
_AccAtmVpStatsGrp_ObjectIdentity = ObjectIdentity
accAtmVpStatsGrp = _AccAtmVpStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3)
)
_AccVpStatTable_Object = MibTable
accVpStatTable = _AccVpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1)
)
if mibBuilder.loadTexts:
    accVpStatTable.setStatus("mandatory")
_AccVpStatEntry_Object = MibTableRow
accVpStatEntry = _AccVpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1)
)
accVpStatEntry.setIndexNames(
    (0, "ACC-ATMVP", "oVpStatName"),
)
if mibBuilder.loadTexts:
    accVpStatEntry.setStatus("mandatory")
_OVpStatName_Type = IfIndex
_OVpStatName_Object = MibTableColumn
oVpStatName = _OVpStatName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 1),
    _OVpStatName_Type()
)
oVpStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatName.setStatus("mandatory")
_OVpStatInPackets_Type = Counter32
_OVpStatInPackets_Object = MibTableColumn
oVpStatInPackets = _OVpStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 2),
    _OVpStatInPackets_Type()
)
oVpStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatInPackets.setStatus("mandatory")
_OVpStatOutPackets_Type = Counter32
_OVpStatOutPackets_Object = MibTableColumn
oVpStatOutPackets = _OVpStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 3),
    _OVpStatOutPackets_Type()
)
oVpStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatOutPackets.setStatus("mandatory")
_OVpStatInOctets_Type = Counter32
_OVpStatInOctets_Object = MibTableColumn
oVpStatInOctets = _OVpStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 4),
    _OVpStatInOctets_Type()
)
oVpStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatInOctets.setStatus("mandatory")
_OVpStatOutOctets_Type = Counter32
_OVpStatOutOctets_Object = MibTableColumn
oVpStatOutOctets = _OVpStatOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 5),
    _OVpStatOutOctets_Type()
)
oVpStatOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatOutOctets.setStatus("mandatory")
_OVpStatInDiscards_Type = Counter32
_OVpStatInDiscards_Object = MibTableColumn
oVpStatInDiscards = _OVpStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 6),
    _OVpStatInDiscards_Type()
)
oVpStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatInDiscards.setStatus("mandatory")
_OVpStatOutDiscards_Type = Counter32
_OVpStatOutDiscards_Object = MibTableColumn
oVpStatOutDiscards = _OVpStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 7),
    _OVpStatOutDiscards_Type()
)
oVpStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatOutDiscards.setStatus("mandatory")
_OVpStatNumChangeds_Type = Counter32
_OVpStatNumChangeds_Object = MibTableColumn
oVpStatNumChangeds = _OVpStatNumChangeds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 8),
    _OVpStatNumChangeds_Type()
)
oVpStatNumChangeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatNumChangeds.setStatus("mandatory")
_OVpStatInErrs_Type = Counter32
_OVpStatInErrs_Object = MibTableColumn
oVpStatInErrs = _OVpStatInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 9),
    _OVpStatInErrs_Type()
)
oVpStatInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatInErrs.setStatus("mandatory")
_OVpStatOutErrs_Type = Counter32
_OVpStatOutErrs_Object = MibTableColumn
oVpStatOutErrs = _OVpStatOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 3, 1, 1, 10),
    _OVpStatOutErrs_Type()
)
oVpStatOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpStatOutErrs.setStatus("mandatory")
_AccAtmVpFrfGrp_ObjectIdentity = ObjectIdentity
accAtmVpFrfGrp = _AccAtmVpFrfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4)
)
_VpAtmFrfTable_Object = MibTable
vpAtmFrfTable = _VpAtmFrfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1)
)
if mibBuilder.loadTexts:
    vpAtmFrfTable.setStatus("mandatory")
_VpAtmFrfEntry_Object = MibTableRow
vpAtmFrfEntry = _VpAtmFrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1)
)
vpAtmFrfEntry.setIndexNames(
    (0, "ACC-ATMVP", "oVpAtmFrfName"),
)
if mibBuilder.loadTexts:
    vpAtmFrfEntry.setStatus("mandatory")
_OVpAtmFrfName_Type = IfIndex
_OVpAtmFrfName_Object = MibTableColumn
oVpAtmFrfName = _OVpAtmFrfName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 1),
    _OVpAtmFrfName_Type()
)
oVpAtmFrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpAtmFrfName.setStatus("mandatory")
_OVpAtmFrfRetryTimer_Type = Integer32
_OVpAtmFrfRetryTimer_Object = MibTableColumn
oVpAtmFrfRetryTimer = _OVpAtmFrfRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 2),
    _OVpAtmFrfRetryTimer_Type()
)
oVpAtmFrfRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfRetryTimer.setStatus("mandatory")
_OVpAtmFrfRetryCount_Type = Integer32
_OVpAtmFrfRetryCount_Object = MibTableColumn
oVpAtmFrfRetryCount = _OVpAtmFrfRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 3),
    _OVpAtmFrfRetryCount_Type()
)
oVpAtmFrfRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfRetryCount.setStatus("mandatory")
_OVpAtmFrfDlciLimit_Type = Integer32
_OVpAtmFrfDlciLimit_Object = MibTableColumn
oVpAtmFrfDlciLimit = _OVpAtmFrfDlciLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 4),
    _OVpAtmFrfDlciLimit_Type()
)
oVpAtmFrfDlciLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfDlciLimit.setStatus("mandatory")
_OVpAtmFrfAddrLength_Type = Integer32
_OVpAtmFrfAddrLength_Object = MibTableColumn
oVpAtmFrfAddrLength = _OVpAtmFrfAddrLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 5),
    _OVpAtmFrfAddrLength_Type()
)
oVpAtmFrfAddrLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfAddrLength.setStatus("mandatory")
_OVpAtmFrfPvcDlciStart_Type = Integer32
_OVpAtmFrfPvcDlciStart_Object = MibTableColumn
oVpAtmFrfPvcDlciStart = _OVpAtmFrfPvcDlciStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 6),
    _OVpAtmFrfPvcDlciStart_Type()
)
oVpAtmFrfPvcDlciStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfPvcDlciStart.setStatus("mandatory")
_OVpAtmFrfPvcDlciEnd_Type = Integer32
_OVpAtmFrfPvcDlciEnd_Object = MibTableColumn
oVpAtmFrfPvcDlciEnd = _OVpAtmFrfPvcDlciEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 7),
    _OVpAtmFrfPvcDlciEnd_Type()
)
oVpAtmFrfPvcDlciEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfPvcDlciEnd.setStatus("mandatory")
_OVpAtmFrfPvcVpi_Type = Integer32
_OVpAtmFrfPvcVpi_Object = MibTableColumn
oVpAtmFrfPvcVpi = _OVpAtmFrfPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 8),
    _OVpAtmFrfPvcVpi_Type()
)
oVpAtmFrfPvcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfPvcVpi.setStatus("mandatory")
_OVpAtmFrfPvcVci_Type = Integer32
_OVpAtmFrfPvcVci_Object = MibTableColumn
oVpAtmFrfPvcVci = _OVpAtmFrfPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 9),
    _OVpAtmFrfPvcVci_Type()
)
oVpAtmFrfPvcVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfPvcVci.setStatus("mandatory")
_OVpAtmFrfCongTimeOut_Type = Integer32
_OVpAtmFrfCongTimeOut_Object = MibTableColumn
oVpAtmFrfCongTimeOut = _OVpAtmFrfCongTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 10),
    _OVpAtmFrfCongTimeOut_Type()
)
oVpAtmFrfCongTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfCongTimeOut.setStatus("mandatory")
_OVpAtmFrfCellLossPrioIn_Type = Integer32
_OVpAtmFrfCellLossPrioIn_Object = MibTableColumn
oVpAtmFrfCellLossPrioIn = _OVpAtmFrfCellLossPrioIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 11),
    _OVpAtmFrfCellLossPrioIn_Type()
)
oVpAtmFrfCellLossPrioIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfCellLossPrioIn.setStatus("mandatory")
_OVpAtmFrfCellLossPrioOut_Type = Integer32
_OVpAtmFrfCellLossPrioOut_Object = MibTableColumn
oVpAtmFrfCellLossPrioOut = _OVpAtmFrfCellLossPrioOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 12),
    _OVpAtmFrfCellLossPrioOut_Type()
)
oVpAtmFrfCellLossPrioOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfCellLossPrioOut.setStatus("mandatory")
_OVpAtmFrfClpMode_Type = Integer32
_OVpAtmFrfClpMode_Object = MibTableColumn
oVpAtmFrfClpMode = _OVpAtmFrfClpMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 4, 1, 1, 13),
    _OVpAtmFrfClpMode_Type()
)
oVpAtmFrfClpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmFrfClpMode.setStatus("mandatory")
_AccAtmVpPppGrp_ObjectIdentity = ObjectIdentity
accAtmVpPppGrp = _AccAtmVpPppGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5)
)
_VpAtmPppTable_Object = MibTable
vpAtmPppTable = _VpAtmPppTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1)
)
if mibBuilder.loadTexts:
    vpAtmPppTable.setStatus("mandatory")
_VpAtmPppEntry_Object = MibTableRow
vpAtmPppEntry = _VpAtmPppEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1)
)
vpAtmPppEntry.setIndexNames(
    (0, "ACC-ATMVP", "oVpAtmPppName"),
)
if mibBuilder.loadTexts:
    vpAtmPppEntry.setStatus("mandatory")
_OVpAtmPppName_Type = IfIndex
_OVpAtmPppName_Object = MibTableColumn
oVpAtmPppName = _OVpAtmPppName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 1),
    _OVpAtmPppName_Type()
)
oVpAtmPppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpAtmPppName.setStatus("mandatory")
_OVpAtmPppRetryTimer_Type = Integer32
_OVpAtmPppRetryTimer_Object = MibTableColumn
oVpAtmPppRetryTimer = _OVpAtmPppRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 2),
    _OVpAtmPppRetryTimer_Type()
)
oVpAtmPppRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppRetryTimer.setStatus("mandatory")
_OVpAtmPppRetryCount_Type = Integer32
_OVpAtmPppRetryCount_Object = MibTableColumn
oVpAtmPppRetryCount = _OVpAtmPppRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 3),
    _OVpAtmPppRetryCount_Type()
)
oVpAtmPppRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppRetryCount.setStatus("mandatory")
_OVpAtmPppVpi_Type = Integer32
_OVpAtmPppVpi_Object = MibTableColumn
oVpAtmPppVpi = _OVpAtmPppVpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 4),
    _OVpAtmPppVpi_Type()
)
oVpAtmPppVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppVpi.setStatus("mandatory")
_OVpAtmPppVci_Type = Integer32
_OVpAtmPppVci_Object = MibTableColumn
oVpAtmPppVci = _OVpAtmPppVci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 5),
    _OVpAtmPppVci_Type()
)
oVpAtmPppVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppVci.setStatus("mandatory")
_OVpAtmPppCongTimeOut_Type = Integer32
_OVpAtmPppCongTimeOut_Object = MibTableColumn
oVpAtmPppCongTimeOut = _OVpAtmPppCongTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 6),
    _OVpAtmPppCongTimeOut_Type()
)
oVpAtmPppCongTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppCongTimeOut.setStatus("mandatory")
_OVpAtmPppMuxType_Type = Integer32
_OVpAtmPppMuxType_Object = MibTableColumn
oVpAtmPppMuxType = _OVpAtmPppMuxType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 5, 1, 1, 7),
    _OVpAtmPppMuxType_Type()
)
oVpAtmPppMuxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmPppMuxType.setStatus("mandatory")
_AccAtmVp1483Grp_ObjectIdentity = ObjectIdentity
accAtmVp1483Grp = _AccAtmVp1483Grp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6)
)
_VpAtm1483Table_Object = MibTable
vpAtm1483Table = _VpAtm1483Table_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1)
)
if mibBuilder.loadTexts:
    vpAtm1483Table.setStatus("mandatory")
_VpAtm1483Entry_Object = MibTableRow
vpAtm1483Entry = _VpAtm1483Entry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1)
)
vpAtm1483Entry.setIndexNames(
    (0, "ACC-ATMVP", "oVpAtm1483Name"),
)
if mibBuilder.loadTexts:
    vpAtm1483Entry.setStatus("mandatory")
_OVpAtm1483Name_Type = IfIndex
_OVpAtm1483Name_Object = MibTableColumn
oVpAtm1483Name = _OVpAtm1483Name_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 1),
    _OVpAtm1483Name_Type()
)
oVpAtm1483Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpAtm1483Name.setStatus("mandatory")
_OVpAtm1483RetryTimer_Type = Integer32
_OVpAtm1483RetryTimer_Object = MibTableColumn
oVpAtm1483RetryTimer = _OVpAtm1483RetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 2),
    _OVpAtm1483RetryTimer_Type()
)
oVpAtm1483RetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483RetryTimer.setStatus("mandatory")
_OVpAtm1483RetryCount_Type = Integer32
_OVpAtm1483RetryCount_Object = MibTableColumn
oVpAtm1483RetryCount = _OVpAtm1483RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 3),
    _OVpAtm1483RetryCount_Type()
)
oVpAtm1483RetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483RetryCount.setStatus("mandatory")
_OVpAtm1483Vpi_Type = Integer32
_OVpAtm1483Vpi_Object = MibTableColumn
oVpAtm1483Vpi = _OVpAtm1483Vpi_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 4),
    _OVpAtm1483Vpi_Type()
)
oVpAtm1483Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483Vpi.setStatus("mandatory")
_OVpAtm1483Vci_Type = Integer32
_OVpAtm1483Vci_Object = MibTableColumn
oVpAtm1483Vci = _OVpAtm1483Vci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 5),
    _OVpAtm1483Vci_Type()
)
oVpAtm1483Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483Vci.setStatus("mandatory")
_OVpAtm1483CongTimeOut_Type = Integer32
_OVpAtm1483CongTimeOut_Object = MibTableColumn
oVpAtm1483CongTimeOut = _OVpAtm1483CongTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 6),
    _OVpAtm1483CongTimeOut_Type()
)
oVpAtm1483CongTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483CongTimeOut.setStatus("mandatory")
_OVpAtm1483MuxType_Type = Integer32
_OVpAtm1483MuxType_Object = MibTableColumn
oVpAtm1483MuxType = _OVpAtm1483MuxType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 6, 1, 1, 7),
    _OVpAtm1483MuxType_Type()
)
oVpAtm1483MuxType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtm1483MuxType.setStatus("mandatory")
_AccAtmVpCipGrp_ObjectIdentity = ObjectIdentity
accAtmVpCipGrp = _AccAtmVpCipGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7)
)
_VpAtmCipTable_Object = MibTable
vpAtmCipTable = _VpAtmCipTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1)
)
if mibBuilder.loadTexts:
    vpAtmCipTable.setStatus("mandatory")
_VpAtmCipEntry_Object = MibTableRow
vpAtmCipEntry = _VpAtmCipEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1)
)
vpAtmCipEntry.setIndexNames(
    (0, "ACC-ATMVP", "oVpAtmCipName"),
)
if mibBuilder.loadTexts:
    vpAtmCipEntry.setStatus("mandatory")
_OVpAtmCipName_Type = IfIndex
_OVpAtmCipName_Object = MibTableColumn
oVpAtmCipName = _OVpAtmCipName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 1),
    _OVpAtmCipName_Type()
)
oVpAtmCipName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oVpAtmCipName.setStatus("mandatory")
_OVpAtmCipRetryTimer_Type = Integer32
_OVpAtmCipRetryTimer_Object = MibTableColumn
oVpAtmCipRetryTimer = _OVpAtmCipRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 2),
    _OVpAtmCipRetryTimer_Type()
)
oVpAtmCipRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipRetryTimer.setStatus("mandatory")
_OVpAtmCipRetryCount_Type = Integer32
_OVpAtmCipRetryCount_Object = MibTableColumn
oVpAtmCipRetryCount = _OVpAtmCipRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 3),
    _OVpAtmCipRetryCount_Type()
)
oVpAtmCipRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipRetryCount.setStatus("mandatory")
_OVpAtmCipMode_Type = Integer32
_OVpAtmCipMode_Object = MibTableColumn
oVpAtmCipMode = _OVpAtmCipMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 4),
    _OVpAtmCipMode_Type()
)
oVpAtmCipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipMode.setStatus("mandatory")
_OVpAtmCipAging_Type = Integer32
_OVpAtmCipAging_Object = MibTableColumn
oVpAtmCipAging = _OVpAtmCipAging_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 5),
    _OVpAtmCipAging_Type()
)
oVpAtmCipAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipAging.setStatus("mandatory")
_OVpAtmCipAddrType_Type = Integer32
_OVpAtmCipAddrType_Object = MibTableColumn
oVpAtmCipAddrType = _OVpAtmCipAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 6),
    _OVpAtmCipAddrType_Type()
)
oVpAtmCipAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipAddrType.setStatus("mandatory")
_OVpAtmCipLocalAddress_Type = DisplayString
_OVpAtmCipLocalAddress_Object = MibTableColumn
oVpAtmCipLocalAddress = _OVpAtmCipLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 7),
    _OVpAtmCipLocalAddress_Type()
)
oVpAtmCipLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipLocalAddress.setStatus("mandatory")
_OVpAtmCipServerAddress_Type = DisplayString
_OVpAtmCipServerAddress_Object = MibTableColumn
oVpAtmCipServerAddress = _OVpAtmCipServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 8),
    _OVpAtmCipServerAddress_Type()
)
oVpAtmCipServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipServerAddress.setStatus("mandatory")
_OVpAtmCipServerVccType_Type = Integer32
_OVpAtmCipServerVccType_Object = MibTableColumn
oVpAtmCipServerVccType = _OVpAtmCipServerVccType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 9),
    _OVpAtmCipServerVccType_Type()
)
oVpAtmCipServerVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipServerVccType.setStatus("mandatory")
_OVpAtmCipMtu_Type = Integer32
_OVpAtmCipMtu_Object = MibTableColumn
oVpAtmCipMtu = _OVpAtmCipMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 10),
    _OVpAtmCipMtu_Type()
)
oVpAtmCipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipMtu.setStatus("mandatory")
_OVpAtmCipPcr_Type = Integer32
_OVpAtmCipPcr_Object = MibTableColumn
oVpAtmCipPcr = _OVpAtmCipPcr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 73, 7, 1, 1, 11),
    _OVpAtmCipPcr_Type()
)
oVpAtmCipPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oVpAtmCipPcr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ATMVP",
    **{"accAtmVp": accAtmVp,
       "accVpTable": accVpTable,
       "accVpEntry": accVpEntry,
       "oVirtualPortName": oVirtualPortName,
       "oVirtualPortAdminState": oVirtualPortAdminState,
       "oVirtualPortOperState": oVirtualPortOperState,
       "oVirtualPortProtocol": oVirtualPortProtocol,
       "oVirtualPortQueueMode": oVirtualPortQueueMode,
       "oVirtualPortCongestion": oVirtualPortCongestion,
       "oVirtualPortPhysicalPort": oVirtualPortPhysicalPort,
       "accAtmVpScalarGrp": accAtmVpScalarGrp,
       "oVirtualPortCount1483Br": oVirtualPortCount1483Br,
       "oVirtualPortCountCIP": oVirtualPortCountCIP,
       "oVirtualPortCountTunnel": oVirtualPortCountTunnel,
       "oVirtualPortCountFrf": oVirtualPortCountFrf,
       "oVirtualPortCountPpp": oVirtualPortCountPpp,
       "oVirtualPortCountVFR": oVirtualPortCountVFR,
       "oVirtualPortCountXOT": oVirtualPortCountXOT,
       "accAtmVpStatsGrp": accAtmVpStatsGrp,
       "accVpStatTable": accVpStatTable,
       "accVpStatEntry": accVpStatEntry,
       "oVpStatName": oVpStatName,
       "oVpStatInPackets": oVpStatInPackets,
       "oVpStatOutPackets": oVpStatOutPackets,
       "oVpStatInOctets": oVpStatInOctets,
       "oVpStatOutOctets": oVpStatOutOctets,
       "oVpStatInDiscards": oVpStatInDiscards,
       "oVpStatOutDiscards": oVpStatOutDiscards,
       "oVpStatNumChangeds": oVpStatNumChangeds,
       "oVpStatInErrs": oVpStatInErrs,
       "oVpStatOutErrs": oVpStatOutErrs,
       "accAtmVpFrfGrp": accAtmVpFrfGrp,
       "vpAtmFrfTable": vpAtmFrfTable,
       "vpAtmFrfEntry": vpAtmFrfEntry,
       "oVpAtmFrfName": oVpAtmFrfName,
       "oVpAtmFrfRetryTimer": oVpAtmFrfRetryTimer,
       "oVpAtmFrfRetryCount": oVpAtmFrfRetryCount,
       "oVpAtmFrfDlciLimit": oVpAtmFrfDlciLimit,
       "oVpAtmFrfAddrLength": oVpAtmFrfAddrLength,
       "oVpAtmFrfPvcDlciStart": oVpAtmFrfPvcDlciStart,
       "oVpAtmFrfPvcDlciEnd": oVpAtmFrfPvcDlciEnd,
       "oVpAtmFrfPvcVpi": oVpAtmFrfPvcVpi,
       "oVpAtmFrfPvcVci": oVpAtmFrfPvcVci,
       "oVpAtmFrfCongTimeOut": oVpAtmFrfCongTimeOut,
       "oVpAtmFrfCellLossPrioIn": oVpAtmFrfCellLossPrioIn,
       "oVpAtmFrfCellLossPrioOut": oVpAtmFrfCellLossPrioOut,
       "oVpAtmFrfClpMode": oVpAtmFrfClpMode,
       "accAtmVpPppGrp": accAtmVpPppGrp,
       "vpAtmPppTable": vpAtmPppTable,
       "vpAtmPppEntry": vpAtmPppEntry,
       "oVpAtmPppName": oVpAtmPppName,
       "oVpAtmPppRetryTimer": oVpAtmPppRetryTimer,
       "oVpAtmPppRetryCount": oVpAtmPppRetryCount,
       "oVpAtmPppVpi": oVpAtmPppVpi,
       "oVpAtmPppVci": oVpAtmPppVci,
       "oVpAtmPppCongTimeOut": oVpAtmPppCongTimeOut,
       "oVpAtmPppMuxType": oVpAtmPppMuxType,
       "accAtmVp1483Grp": accAtmVp1483Grp,
       "vpAtm1483Table": vpAtm1483Table,
       "vpAtm1483Entry": vpAtm1483Entry,
       "oVpAtm1483Name": oVpAtm1483Name,
       "oVpAtm1483RetryTimer": oVpAtm1483RetryTimer,
       "oVpAtm1483RetryCount": oVpAtm1483RetryCount,
       "oVpAtm1483Vpi": oVpAtm1483Vpi,
       "oVpAtm1483Vci": oVpAtm1483Vci,
       "oVpAtm1483CongTimeOut": oVpAtm1483CongTimeOut,
       "oVpAtm1483MuxType": oVpAtm1483MuxType,
       "accAtmVpCipGrp": accAtmVpCipGrp,
       "vpAtmCipTable": vpAtmCipTable,
       "vpAtmCipEntry": vpAtmCipEntry,
       "oVpAtmCipName": oVpAtmCipName,
       "oVpAtmCipRetryTimer": oVpAtmCipRetryTimer,
       "oVpAtmCipRetryCount": oVpAtmCipRetryCount,
       "oVpAtmCipMode": oVpAtmCipMode,
       "oVpAtmCipAging": oVpAtmCipAging,
       "oVpAtmCipAddrType": oVpAtmCipAddrType,
       "oVpAtmCipLocalAddress": oVpAtmCipLocalAddress,
       "oVpAtmCipServerAddress": oVpAtmCipServerAddress,
       "oVpAtmCipServerVccType": oVpAtmCipServerVccType,
       "oVpAtmCipMtu": oVpAtmCipMtu,
       "oVpAtmCipPcr": oVpAtmCipPcr}
)
