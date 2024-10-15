# SNMP MIB module (CTFPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTFPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:24 2024
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

(ctFPS,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFPS")

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

_FpsSystem_ObjectIdentity = ObjectIdentity
fpsSystem = _FpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1)
)
_FpsSystemSlotNum_Type = Integer32
_FpsSystemSlotNum_Object = MibScalar
fpsSystemSlotNum = _FpsSystemSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 1),
    _FpsSystemSlotNum_Type()
)
fpsSystemSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsSystemSlotNum.setStatus("mandatory")


class _FpsSystemMode_Type(Integer32):
    """Custom type fpsSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("switch", 2))
    )


_FpsSystemMode_Type.__name__ = "Integer32"
_FpsSystemMode_Object = MibScalar
fpsSystemMode = _FpsSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 2),
    _FpsSystemMode_Type()
)
fpsSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsSystemMode.setStatus("mandatory")
_FpsMaxPktRam_Type = Integer32
_FpsMaxPktRam_Object = MibScalar
fpsMaxPktRam = _FpsMaxPktRam_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 3),
    _FpsMaxPktRam_Type()
)
fpsMaxPktRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsMaxPktRam.setStatus("mandatory")
_FpsFreePktRam_Type = Gauge32
_FpsFreePktRam_Object = MibScalar
fpsFreePktRam = _FpsFreePktRam_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 4),
    _FpsFreePktRam_Type()
)
fpsFreePktRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsFreePktRam.setStatus("mandatory")
_FpsOperTime_Type = TimeTicks
_FpsOperTime_Object = MibScalar
fpsOperTime = _FpsOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 5),
    _FpsOperTime_Type()
)
fpsOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsOperTime.setStatus("mandatory")
_FpsInPkts_Type = Counter32
_FpsInPkts_Object = MibScalar
fpsInPkts = _FpsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 6),
    _FpsInPkts_Type()
)
fpsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsInPkts.setStatus("mandatory")
_FpsOutPkts_Type = Counter32
_FpsOutPkts_Object = MibScalar
fpsOutPkts = _FpsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 7),
    _FpsOutPkts_Type()
)
fpsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsOutPkts.setStatus("mandatory")
_FpsInOctets_Type = Counter32
_FpsInOctets_Object = MibScalar
fpsInOctets = _FpsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 8),
    _FpsInOctets_Type()
)
fpsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsInOctets.setStatus("mandatory")
_FpsOutOctets_Type = Counter32
_FpsOutOctets_Object = MibScalar
fpsOutOctets = _FpsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 1, 9),
    _FpsOutOctets_Type()
)
fpsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsOutOctets.setStatus("mandatory")
_FpsPort_ObjectIdentity = ObjectIdentity
fpsPort = _FpsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2)
)
_FpsActivePorts_Type = Integer32
_FpsActivePorts_Object = MibScalar
fpsActivePorts = _FpsActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 1),
    _FpsActivePorts_Type()
)
fpsActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsActivePorts.setStatus("mandatory")
_FpsMaxPortNum_Type = Integer32
_FpsMaxPortNum_Object = MibScalar
fpsMaxPortNum = _FpsMaxPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 2),
    _FpsMaxPortNum_Type()
)
fpsMaxPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsMaxPortNum.setStatus("mandatory")
_FpsPortTable_Object = MibTable
fpsPortTable = _FpsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3)
)
if mibBuilder.loadTexts:
    fpsPortTable.setStatus("mandatory")
_FpsPortEntry_Object = MibTableRow
fpsPortEntry = _FpsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1)
)
fpsPortEntry.setIndexNames(
    (0, "CTFPS-MIB", "fpsPortNum"),
)
if mibBuilder.loadTexts:
    fpsPortEntry.setStatus("mandatory")
_FpsPortNum_Type = Integer32
_FpsPortNum_Object = MibTableColumn
fpsPortNum = _FpsPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 1),
    _FpsPortNum_Type()
)
fpsPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortNum.setStatus("mandatory")
_FpsPortIfNum_Type = Integer32
_FpsPortIfNum_Object = MibTableColumn
fpsPortIfNum = _FpsPortIfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 2),
    _FpsPortIfNum_Type()
)
fpsPortIfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortIfNum.setStatus("mandatory")


class _FpsPortType_Type(Integer32):
    """Custom type fpsPortType based on Integer32"""
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
        *(("atm", 6),
          ("ether", 1),
          ("fddi", 4),
          ("host", 5),
          ("inb", 3),
          ("other", 8),
          ("tokenRing", 2),
          ("wan", 7))
    )


_FpsPortType_Type.__name__ = "Integer32"
_FpsPortType_Object = MibTableColumn
fpsPortType = _FpsPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 3),
    _FpsPortType_Type()
)
fpsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortType.setStatus("mandatory")
_FpsPortClusterNum_Type = Integer32
_FpsPortClusterNum_Object = MibTableColumn
fpsPortClusterNum = _FpsPortClusterNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 4),
    _FpsPortClusterNum_Type()
)
fpsPortClusterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortClusterNum.setStatus("mandatory")
_FpsPortTotalAvailQueDepth_Type = Integer32
_FpsPortTotalAvailQueDepth_Object = MibTableColumn
fpsPortTotalAvailQueDepth = _FpsPortTotalAvailQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 5),
    _FpsPortTotalAvailQueDepth_Type()
)
fpsPortTotalAvailQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortTotalAvailQueDepth.setStatus("mandatory")
_FpsPortMaxQueDepth_Type = Integer32
_FpsPortMaxQueDepth_Object = MibTableColumn
fpsPortMaxQueDepth = _FpsPortMaxQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 6),
    _FpsPortMaxQueDepth_Type()
)
fpsPortMaxQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortMaxQueDepth.setStatus("mandatory")
_FpsPortCurrentQueDepth_Type = Integer32
_FpsPortCurrentQueDepth_Object = MibTableColumn
fpsPortCurrentQueDepth = _FpsPortCurrentQueDepth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 7),
    _FpsPortCurrentQueDepth_Type()
)
fpsPortCurrentQueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortCurrentQueDepth.setStatus("mandatory")
_FpsPortBandwidthRequested_Type = Integer32
_FpsPortBandwidthRequested_Object = MibTableColumn
fpsPortBandwidthRequested = _FpsPortBandwidthRequested_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 8),
    _FpsPortBandwidthRequested_Type()
)
fpsPortBandwidthRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortBandwidthRequested.setStatus("mandatory")
_FpsPortBandwidthAllocated_Type = Integer32
_FpsPortBandwidthAllocated_Object = MibTableColumn
fpsPortBandwidthAllocated = _FpsPortBandwidthAllocated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 9),
    _FpsPortBandwidthAllocated_Type()
)
fpsPortBandwidthAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortBandwidthAllocated.setStatus("mandatory")


class _FpsPortXmitStatus_Type(Integer32):
    """Custom type fpsPortXmitStatus based on Integer32"""
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


_FpsPortXmitStatus_Type.__name__ = "Integer32"
_FpsPortXmitStatus_Object = MibTableColumn
fpsPortXmitStatus = _FpsPortXmitStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 10),
    _FpsPortXmitStatus_Type()
)
fpsPortXmitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortXmitStatus.setStatus("mandatory")


class _FpsPortFwdStatus_Type(Integer32):
    """Custom type fpsPortFwdStatus based on Integer32"""
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


_FpsPortFwdStatus_Type.__name__ = "Integer32"
_FpsPortFwdStatus_Object = MibTableColumn
fpsPortFwdStatus = _FpsPortFwdStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 11),
    _FpsPortFwdStatus_Type()
)
fpsPortFwdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortFwdStatus.setStatus("mandatory")


class _FpsPortLearningStatus_Type(Integer32):
    """Custom type fpsPortLearningStatus based on Integer32"""
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


_FpsPortLearningStatus_Type.__name__ = "Integer32"
_FpsPortLearningStatus_Object = MibTableColumn
fpsPortLearningStatus = _FpsPortLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 12),
    _FpsPortLearningStatus_Type()
)
fpsPortLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortLearningStatus.setStatus("mandatory")


class _FpsPortUnknownStatus_Type(Integer32):
    """Custom type fpsPortUnknownStatus based on Integer32"""
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


_FpsPortUnknownStatus_Type.__name__ = "Integer32"
_FpsPortUnknownStatus_Object = MibTableColumn
fpsPortUnknownStatus = _FpsPortUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 13),
    _FpsPortUnknownStatus_Type()
)
fpsPortUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortUnknownStatus.setStatus("mandatory")


class _FpsPortBroadcastStatus_Type(Integer32):
    """Custom type fpsPortBroadcastStatus based on Integer32"""
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


_FpsPortBroadcastStatus_Type.__name__ = "Integer32"
_FpsPortBroadcastStatus_Object = MibTableColumn
fpsPortBroadcastStatus = _FpsPortBroadcastStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 14),
    _FpsPortBroadcastStatus_Type()
)
fpsPortBroadcastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortBroadcastStatus.setStatus("mandatory")


class _FpsPortViolationStatus_Type(Integer32):
    """Custom type fpsPortViolationStatus based on Integer32"""
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


_FpsPortViolationStatus_Type.__name__ = "Integer32"
_FpsPortViolationStatus_Object = MibTableColumn
fpsPortViolationStatus = _FpsPortViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 15),
    _FpsPortViolationStatus_Type()
)
fpsPortViolationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortViolationStatus.setStatus("mandatory")


class _FpsPortCopyStatus_Type(Integer32):
    """Custom type fpsPortCopyStatus based on Integer32"""
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


_FpsPortCopyStatus_Type.__name__ = "Integer32"
_FpsPortCopyStatus_Object = MibTableColumn
fpsPortCopyStatus = _FpsPortCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 16),
    _FpsPortCopyStatus_Type()
)
fpsPortCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortCopyStatus.setStatus("mandatory")


class _FpsPortStatsStatus_Type(Integer32):
    """Custom type fpsPortStatsStatus based on Integer32"""
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


_FpsPortStatsStatus_Type.__name__ = "Integer32"
_FpsPortStatsStatus_Object = MibTableColumn
fpsPortStatsStatus = _FpsPortStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 17),
    _FpsPortStatsStatus_Type()
)
fpsPortStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortStatsStatus.setStatus("mandatory")


class _FpsPortSpecialPortsSMT_Type(Integer32):
    """Custom type fpsPortSpecialPortsSMT based on Integer32"""
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


_FpsPortSpecialPortsSMT_Type.__name__ = "Integer32"
_FpsPortSpecialPortsSMT_Object = MibTableColumn
fpsPortSpecialPortsSMT = _FpsPortSpecialPortsSMT_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 18),
    _FpsPortSpecialPortsSMT_Type()
)
fpsPortSpecialPortsSMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortSpecialPortsSMT.setStatus("mandatory")


class _FpsPortSpecialPortsHost_Type(Integer32):
    """Custom type fpsPortSpecialPortsHost based on Integer32"""
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


_FpsPortSpecialPortsHost_Type.__name__ = "Integer32"
_FpsPortSpecialPortsHost_Object = MibTableColumn
fpsPortSpecialPortsHost = _FpsPortSpecialPortsHost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 19),
    _FpsPortSpecialPortsHost_Type()
)
fpsPortSpecialPortsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortSpecialPortsHost.setStatus("mandatory")


class _FpsPortSpecialPortsError_Type(Integer32):
    """Custom type fpsPortSpecialPortsError based on Integer32"""
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


_FpsPortSpecialPortsError_Type.__name__ = "Integer32"
_FpsPortSpecialPortsError_Object = MibTableColumn
fpsPortSpecialPortsError = _FpsPortSpecialPortsError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 2, 3, 1, 20),
    _FpsPortSpecialPortsError_Type()
)
fpsPortSpecialPortsError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortSpecialPortsError.setStatus("mandatory")
_FpsCluster_ObjectIdentity = ObjectIdentity
fpsCluster = _FpsCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3)
)
_FpsActiveClusters_Type = Integer32
_FpsActiveClusters_Object = MibScalar
fpsActiveClusters = _FpsActiveClusters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 1),
    _FpsActiveClusters_Type()
)
fpsActiveClusters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsActiveClusters.setStatus("mandatory")
_FpsClusterTable_Object = MibTable
fpsClusterTable = _FpsClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fpsClusterTable.setStatus("mandatory")
_FpsClusterEntry_Object = MibTableRow
fpsClusterEntry = _FpsClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1)
)
fpsClusterEntry.setIndexNames(
    (0, "CTFPS-MIB", "fpsClusterNumber"),
)
if mibBuilder.loadTexts:
    fpsClusterEntry.setStatus("mandatory")
_FpsClusterNumber_Type = Integer32
_FpsClusterNumber_Object = MibTableColumn
fpsClusterNumber = _FpsClusterNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 1),
    _FpsClusterNumber_Type()
)
fpsClusterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsClusterNumber.setStatus("mandatory")


class _FpsClusterType_Type(Integer32):
    """Custom type fpsClusterType based on Integer32"""
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
        *(("atm", 6),
          ("ethernet", 1),
          ("fnb", 4),
          ("host", 5),
          ("inb", 3),
          ("token-ring", 2),
          ("wan", 7))
    )


_FpsClusterType_Type.__name__ = "Integer32"
_FpsClusterType_Object = MibTableColumn
fpsClusterType = _FpsClusterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 2),
    _FpsClusterType_Type()
)
fpsClusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsClusterType.setStatus("mandatory")


class _FpsClusterRoundRobin_Type(Integer32):
    """Custom type fpsClusterRoundRobin based on Integer32"""
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


_FpsClusterRoundRobin_Type.__name__ = "Integer32"
_FpsClusterRoundRobin_Object = MibTableColumn
fpsClusterRoundRobin = _FpsClusterRoundRobin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 3),
    _FpsClusterRoundRobin_Type()
)
fpsClusterRoundRobin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpsClusterRoundRobin.setStatus("mandatory")
_FpsPortsPerCluster_Type = Integer32
_FpsPortsPerCluster_Object = MibTableColumn
fpsPortsPerCluster = _FpsPortsPerCluster_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 3, 2, 1, 4),
    _FpsPortsPerCluster_Type()
)
fpsPortsPerCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpsPortsPerCluster.setStatus("mandatory")
_FpsDMAF_ObjectIdentity = ObjectIdentity
fpsDMAF = _FpsDMAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 4)
)
_DmafBandWidth3SecUtil_Type = Gauge32
_DmafBandWidth3SecUtil_Object = MibScalar
dmafBandWidth3SecUtil = _DmafBandWidth3SecUtil_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 4, 1),
    _DmafBandWidth3SecUtil_Type()
)
dmafBandWidth3SecUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmafBandWidth3SecUtil.setStatus("mandatory")
_FpsBAF_ObjectIdentity = ObjectIdentity
fpsBAF = _FpsBAF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5)
)
_BafEntryCount_Type = Integer32
_BafEntryCount_Object = MibScalar
bafEntryCount = _BafEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 1),
    _BafEntryCount_Type()
)
bafEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bafEntryCount.setStatus("mandatory")
_BafMaxEntry_Type = Integer32
_BafMaxEntry_Object = MibScalar
bafMaxEntry = _BafMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 2),
    _BafMaxEntry_Type()
)
bafMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bafMaxEntry.setStatus("mandatory")
_Baf3SecUtil_Type = Gauge32
_Baf3SecUtil_Object = MibScalar
baf3SecUtil = _Baf3SecUtil_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2, 5, 3),
    _Baf3SecUtil_Type()
)
baf3SecUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baf3SecUtil.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTFPS-MIB",
    **{"fpsSystem": fpsSystem,
       "fpsSystemSlotNum": fpsSystemSlotNum,
       "fpsSystemMode": fpsSystemMode,
       "fpsMaxPktRam": fpsMaxPktRam,
       "fpsFreePktRam": fpsFreePktRam,
       "fpsOperTime": fpsOperTime,
       "fpsInPkts": fpsInPkts,
       "fpsOutPkts": fpsOutPkts,
       "fpsInOctets": fpsInOctets,
       "fpsOutOctets": fpsOutOctets,
       "fpsPort": fpsPort,
       "fpsActivePorts": fpsActivePorts,
       "fpsMaxPortNum": fpsMaxPortNum,
       "fpsPortTable": fpsPortTable,
       "fpsPortEntry": fpsPortEntry,
       "fpsPortNum": fpsPortNum,
       "fpsPortIfNum": fpsPortIfNum,
       "fpsPortType": fpsPortType,
       "fpsPortClusterNum": fpsPortClusterNum,
       "fpsPortTotalAvailQueDepth": fpsPortTotalAvailQueDepth,
       "fpsPortMaxQueDepth": fpsPortMaxQueDepth,
       "fpsPortCurrentQueDepth": fpsPortCurrentQueDepth,
       "fpsPortBandwidthRequested": fpsPortBandwidthRequested,
       "fpsPortBandwidthAllocated": fpsPortBandwidthAllocated,
       "fpsPortXmitStatus": fpsPortXmitStatus,
       "fpsPortFwdStatus": fpsPortFwdStatus,
       "fpsPortLearningStatus": fpsPortLearningStatus,
       "fpsPortUnknownStatus": fpsPortUnknownStatus,
       "fpsPortBroadcastStatus": fpsPortBroadcastStatus,
       "fpsPortViolationStatus": fpsPortViolationStatus,
       "fpsPortCopyStatus": fpsPortCopyStatus,
       "fpsPortStatsStatus": fpsPortStatsStatus,
       "fpsPortSpecialPortsSMT": fpsPortSpecialPortsSMT,
       "fpsPortSpecialPortsHost": fpsPortSpecialPortsHost,
       "fpsPortSpecialPortsError": fpsPortSpecialPortsError,
       "fpsCluster": fpsCluster,
       "fpsActiveClusters": fpsActiveClusters,
       "fpsClusterTable": fpsClusterTable,
       "fpsClusterEntry": fpsClusterEntry,
       "fpsClusterNumber": fpsClusterNumber,
       "fpsClusterType": fpsClusterType,
       "fpsClusterRoundRobin": fpsClusterRoundRobin,
       "fpsPortsPerCluster": fpsPortsPerCluster,
       "fpsDMAF": fpsDMAF,
       "dmafBandWidth3SecUtil": dmafBandWidth3SecUtil,
       "fpsBAF": fpsBAF,
       "bafEntryCount": bafEntryCount,
       "bafMaxEntry": bafMaxEntry,
       "baf3SecUtil": baf3SecUtil}
)
