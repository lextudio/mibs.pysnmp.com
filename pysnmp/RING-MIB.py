# SNMP MIB module (RING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:17 2024
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

(coriolisMibs,
 ring) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "coriolisMibs",
    "ring")

(chassisElemReachStatus,
 chassisIpAddr) = mibBuilder.importSymbols(
    "DEVICE-MIB",
    "chassisElemReachStatus",
    "chassisIpAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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

ringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 4, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ActPhyRingCount_Type = Integer32
_ActPhyRingCount_Object = MibScalar
actPhyRingCount = _ActPhyRingCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 1),
    _ActPhyRingCount_Type()
)
actPhyRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actPhyRingCount.setStatus("current")
_ActPhyRingTable_Object = MibTable
actPhyRingTable = _ActPhyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 2)
)
if mibBuilder.loadTexts:
    actPhyRingTable.setStatus("current")
_ActPhyRingEntry_Object = MibTableRow
actPhyRingEntry = _ActPhyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 2, 1)
)
actPhyRingEntry.setIndexNames(
    (0, "RING-MIB", "phyRingSlotNo"),
    (0, "RING-MIB", "phyRingPortNo"),
)
if mibBuilder.loadTexts:
    actPhyRingEntry.setStatus("current")


class _PhyRingSlotNo_Type(Integer32):
    """Custom type phyRingSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_PhyRingSlotNo_Type.__name__ = "Integer32"
_PhyRingSlotNo_Object = MibTableColumn
phyRingSlotNo = _PhyRingSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 2, 1, 1),
    _PhyRingSlotNo_Type()
)
phyRingSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyRingSlotNo.setStatus("current")


class _PhyRingPortNo_Type(Integer32):
    """Custom type phyRingPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PhyRingPortNo_Type.__name__ = "Integer32"
_PhyRingPortNo_Object = MibTableColumn
phyRingPortNo = _PhyRingPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 2, 1, 2),
    _PhyRingPortNo_Type()
)
phyRingPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phyRingPortNo.setStatus("current")
_ActLogRingCount_Type = Integer32
_ActLogRingCount_Object = MibScalar
actLogRingCount = _ActLogRingCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 3),
    _ActLogRingCount_Type()
)
actLogRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actLogRingCount.setStatus("current")
_ActLogRingTable_Object = MibTable
actLogRingTable = _ActLogRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4)
)
if mibBuilder.loadTexts:
    actLogRingTable.setStatus("current")
_ActLogRingEntry_Object = MibTableRow
actLogRingEntry = _ActLogRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1)
)
actLogRingEntry.setIndexNames(
    (0, "RING-MIB", "phyRingSlotNo"),
    (0, "RING-MIB", "phyRingPortNo"),
    (0, "RING-MIB", "logRingVPortNo"),
)
if mibBuilder.loadTexts:
    actLogRingEntry.setStatus("current")
_LogRingVPortNo_Type = Integer32
_LogRingVPortNo_Object = MibTableColumn
logRingVPortNo = _LogRingVPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 1),
    _LogRingVPortNo_Type()
)
logRingVPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingVPortNo.setStatus("current")
_LogRingElemCount_Type = Integer32
_LogRingElemCount_Object = MibTableColumn
logRingElemCount = _LogRingElemCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 2),
    _LogRingElemCount_Type()
)
logRingElemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemCount.setStatus("current")


class _LogRingLambdaStatus_Type(Integer32):
    """Custom type logRingLambdaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cut", 2),
          ("noCut", 1),
          ("restored", 3))
    )


_LogRingLambdaStatus_Type.__name__ = "Integer32"
_LogRingLambdaStatus_Object = MibTableColumn
logRingLambdaStatus = _LogRingLambdaStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 3),
    _LogRingLambdaStatus_Type()
)
logRingLambdaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingLambdaStatus.setStatus("current")


class _LogRingProtoStatusTxt_Type(OctetString):
    """Custom type logRingProtoStatusTxt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_LogRingProtoStatusTxt_Type.__name__ = "OctetString"
_LogRingProtoStatusTxt_Object = MibTableColumn
logRingProtoStatusTxt = _LogRingProtoStatusTxt_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 5),
    _LogRingProtoStatusTxt_Type()
)
logRingProtoStatusTxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingProtoStatusTxt.setStatus("current")


class _LogRingProtoStatus_Type(Integer32):
    """Custom type logRingProtoStatus based on Integer32"""
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
        *(("clrAlarm", 6),
          ("clrError", 4),
          ("controlChanDn", 2),
          ("lowerLayerDn", 7),
          ("normal", 1),
          ("setAlarm", 5),
          ("setError", 3))
    )


_LogRingProtoStatus_Type.__name__ = "Integer32"
_LogRingProtoStatus_Object = MibTableColumn
logRingProtoStatus = _LogRingProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 6),
    _LogRingProtoStatus_Type()
)
logRingProtoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingProtoStatus.setStatus("current")


class _LogRingGneName_Type(OctetString):
    """Custom type logRingGneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LogRingGneName_Type.__name__ = "OctetString"
_LogRingGneName_Object = MibTableColumn
logRingGneName = _LogRingGneName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 7),
    _LogRingGneName_Type()
)
logRingGneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingGneName.setStatus("current")
_LogRingGneIpAddr_Type = IpAddress
_LogRingGneIpAddr_Object = MibTableColumn
logRingGneIpAddr = _LogRingGneIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 8),
    _LogRingGneIpAddr_Type()
)
logRingGneIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingGneIpAddr.setStatus("current")


class _LogRingGneRingSlot_Type(Integer32):
    """Custom type logRingGneRingSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LogRingGneRingSlot_Type.__name__ = "Integer32"
_LogRingGneRingSlot_Object = MibTableColumn
logRingGneRingSlot = _LogRingGneRingSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 9),
    _LogRingGneRingSlot_Type()
)
logRingGneRingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingGneRingSlot.setStatus("current")


class _LogRingGneRingPort_Type(Integer32):
    """Custom type logRingGneRingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LogRingGneRingPort_Type.__name__ = "Integer32"
_LogRingGneRingPort_Object = MibTableColumn
logRingGneRingPort = _LogRingGneRingPort_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 10),
    _LogRingGneRingPort_Type()
)
logRingGneRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingGneRingPort.setStatus("current")
_LogRingGneRingVport_Type = Integer32
_LogRingGneRingVport_Object = MibTableColumn
logRingGneRingVport = _LogRingGneRingVport_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 11),
    _LogRingGneRingVport_Type()
)
logRingGneRingVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingGneRingVport.setStatus("current")


class _LogRingUpsNgbrName_Type(OctetString):
    """Custom type logRingUpsNgbrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_LogRingUpsNgbrName_Type.__name__ = "OctetString"
_LogRingUpsNgbrName_Object = MibTableColumn
logRingUpsNgbrName = _LogRingUpsNgbrName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 12),
    _LogRingUpsNgbrName_Type()
)
logRingUpsNgbrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingUpsNgbrName.setStatus("current")
_LogRingUpsNgbrIpAddr_Type = IpAddress
_LogRingUpsNgbrIpAddr_Object = MibTableColumn
logRingUpsNgbrIpAddr = _LogRingUpsNgbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 13),
    _LogRingUpsNgbrIpAddr_Type()
)
logRingUpsNgbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingUpsNgbrIpAddr.setStatus("current")


class _LogRingUpsNgbrRingSlot_Type(Integer32):
    """Custom type logRingUpsNgbrRingSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LogRingUpsNgbrRingSlot_Type.__name__ = "Integer32"
_LogRingUpsNgbrRingSlot_Object = MibTableColumn
logRingUpsNgbrRingSlot = _LogRingUpsNgbrRingSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 14),
    _LogRingUpsNgbrRingSlot_Type()
)
logRingUpsNgbrRingSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingUpsNgbrRingSlot.setStatus("current")


class _LogRingUpsNgbrRingPort_Type(Integer32):
    """Custom type logRingUpsNgbrRingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LogRingUpsNgbrRingPort_Type.__name__ = "Integer32"
_LogRingUpsNgbrRingPort_Object = MibTableColumn
logRingUpsNgbrRingPort = _LogRingUpsNgbrRingPort_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 15),
    _LogRingUpsNgbrRingPort_Type()
)
logRingUpsNgbrRingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingUpsNgbrRingPort.setStatus("current")
_LogRingUpsNgbrRingVport_Type = Integer32
_LogRingUpsNgbrRingVport_Object = MibTableColumn
logRingUpsNgbrRingVport = _LogRingUpsNgbrRingVport_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 16),
    _LogRingUpsNgbrRingVport_Type()
)
logRingUpsNgbrRingVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingUpsNgbrRingVport.setStatus("current")
_LogRingIsConfigured_Type = TruthValue
_LogRingIsConfigured_Object = MibTableColumn
logRingIsConfigured = _LogRingIsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 17),
    _LogRingIsConfigured_Type()
)
logRingIsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingIsConfigured.setStatus("current")


class _LogRingAttRingType_Type(Integer32):
    """Custom type logRingAttRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("protected", 3),
          ("working", 2))
    )


_LogRingAttRingType_Type.__name__ = "Integer32"
_LogRingAttRingType_Object = MibTableColumn
logRingAttRingType = _LogRingAttRingType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 18),
    _LogRingAttRingType_Type()
)
logRingAttRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingAttRingType.setStatus("current")
_LogRingCapacity_Type = Integer32
_LogRingCapacity_Object = MibTableColumn
logRingCapacity = _LogRingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 19),
    _LogRingCapacity_Type()
)
logRingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingCapacity.setStatus("current")
_LogRingCutLocationIp_Type = IpAddress
_LogRingCutLocationIp_Object = MibTableColumn
logRingCutLocationIp = _LogRingCutLocationIp_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 20),
    _LogRingCutLocationIp_Type()
)
logRingCutLocationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingCutLocationIp.setStatus("current")


class _LogRingCutLocationName_Type(OctetString):
    """Custom type logRingCutLocationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_LogRingCutLocationName_Type.__name__ = "OctetString"
_LogRingCutLocationName_Object = MibTableColumn
logRingCutLocationName = _LogRingCutLocationName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 21),
    _LogRingCutLocationName_Type()
)
logRingCutLocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingCutLocationName.setStatus("current")
_LogRingIsRingMaster_Type = TruthValue
_LogRingIsRingMaster_Object = MibTableColumn
logRingIsRingMaster = _LogRingIsRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 22),
    _LogRingIsRingMaster_Type()
)
logRingIsRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingIsRingMaster.setStatus("current")
_LogRingOtherSlot_Type = Integer32
_LogRingOtherSlot_Object = MibTableColumn
logRingOtherSlot = _LogRingOtherSlot_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 23),
    _LogRingOtherSlot_Type()
)
logRingOtherSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingOtherSlot.setStatus("current")
_LogRingOtherPort_Type = Integer32
_LogRingOtherPort_Object = MibTableColumn
logRingOtherPort = _LogRingOtherPort_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 24),
    _LogRingOtherPort_Type()
)
logRingOtherPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingOtherPort.setStatus("current")
_LogRingOtherVport_Type = Integer32
_LogRingOtherVport_Object = MibTableColumn
logRingOtherVport = _LogRingOtherVport_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 4, 1, 25),
    _LogRingOtherVport_Type()
)
logRingOtherVport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingOtherVport.setStatus("current")
_ActLogRingElemTable_Object = MibTable
actLogRingElemTable = _ActLogRingElemTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5)
)
if mibBuilder.loadTexts:
    actLogRingElemTable.setStatus("current")
_ActLogRingElemEntry_Object = MibTableRow
actLogRingElemEntry = _ActLogRingElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1)
)
actLogRingElemEntry.setIndexNames(
    (0, "RING-MIB", "phyRingSlotNo"),
    (0, "RING-MIB", "phyRingPortNo"),
    (0, "RING-MIB", "logRingVPortNo"),
    (0, "RING-MIB", "logRingElemIndex"),
)
if mibBuilder.loadTexts:
    actLogRingElemEntry.setStatus("current")
_LogRingElemIndex_Type = Integer32
_LogRingElemIndex_Object = MibTableColumn
logRingElemIndex = _LogRingElemIndex_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 1),
    _LogRingElemIndex_Type()
)
logRingElemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemIndex.setStatus("current")


class _LogRingElemName_Type(OctetString):
    """Custom type logRingElemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_LogRingElemName_Type.__name__ = "OctetString"
_LogRingElemName_Object = MibTableColumn
logRingElemName = _LogRingElemName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 2),
    _LogRingElemName_Type()
)
logRingElemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemName.setStatus("current")


class _LogRingElemMACAddr_Type(OctetString):
    """Custom type logRingElemMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LogRingElemMACAddr_Type.__name__ = "OctetString"
_LogRingElemMACAddr_Object = MibTableColumn
logRingElemMACAddr = _LogRingElemMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 3),
    _LogRingElemMACAddr_Type()
)
logRingElemMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemMACAddr.setStatus("current")
_LogRingElemIpAddr_Type = IpAddress
_LogRingElemIpAddr_Object = MibTableColumn
logRingElemIpAddr = _LogRingElemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 4),
    _LogRingElemIpAddr_Type()
)
logRingElemIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemIpAddr.setStatus("current")


class _LogRingElemPortId_Type(OctetString):
    """Custom type logRingElemPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LogRingElemPortId_Type.__name__ = "OctetString"
_LogRingElemPortId_Object = MibTableColumn
logRingElemPortId = _LogRingElemPortId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 5),
    _LogRingElemPortId_Type()
)
logRingElemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemPortId.setStatus("current")


class _LogRingElemChassisId_Type(Integer32):
    """Custom type logRingElemChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              21)
        )
    )
    namedValues = NamedValues(
        *(("optiFlow1010", 21),
          ("optiFlow3000", 4),
          ("optiFlow3500", 3),
          ("optiFlow5000", 2),
          ("optiFlow5500", 1))
    )


_LogRingElemChassisId_Type.__name__ = "Integer32"
_LogRingElemChassisId_Object = MibTableColumn
logRingElemChassisId = _LogRingElemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 6),
    _LogRingElemChassisId_Type()
)
logRingElemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemChassisId.setStatus("current")


class _LogRingElemActiveMM_Type(Integer32):
    """Custom type logRingElemActiveMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_LogRingElemActiveMM_Type.__name__ = "Integer32"
_LogRingElemActiveMM_Object = MibTableColumn
logRingElemActiveMM = _LogRingElemActiveMM_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 7),
    _LogRingElemActiveMM_Type()
)
logRingElemActiveMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemActiveMM.setStatus("current")
_LogRingElemIsInNeTable_Type = TruthValue
_LogRingElemIsInNeTable_Object = MibTableColumn
logRingElemIsInNeTable = _LogRingElemIsInNeTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 8),
    _LogRingElemIsInNeTable_Type()
)
logRingElemIsInNeTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemIsInNeTable.setStatus("current")
_LogRingElemIsReachable_Type = TruthValue
_LogRingElemIsReachable_Object = MibTableColumn
logRingElemIsReachable = _LogRingElemIsReachable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 9),
    _LogRingElemIsReachable_Type()
)
logRingElemIsReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemIsReachable.setStatus("current")
_LogRingElemIsLambdaCutHere_Type = TruthValue
_LogRingElemIsLambdaCutHere_Object = MibTableColumn
logRingElemIsLambdaCutHere = _LogRingElemIsLambdaCutHere_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 10),
    _LogRingElemIsLambdaCutHere_Type()
)
logRingElemIsLambdaCutHere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemIsLambdaCutHere.setStatus("current")


class _LogRingElemChassisCharacter_Type(Integer32):
    """Custom type logRingElemChassisCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gne", 1),
          ("ne", 2),
          ("sne", 3))
    )


_LogRingElemChassisCharacter_Type.__name__ = "Integer32"
_LogRingElemChassisCharacter_Object = MibTableColumn
logRingElemChassisCharacter = _LogRingElemChassisCharacter_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 11),
    _LogRingElemChassisCharacter_Type()
)
logRingElemChassisCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemChassisCharacter.setStatus("current")


class _LogRingElemNodeId_Type(Integer32):
    """Custom type logRingElemNodeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_LogRingElemNodeId_Type.__name__ = "Integer32"
_LogRingElemNodeId_Object = MibTableColumn
logRingElemNodeId = _LogRingElemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 12),
    _LogRingElemNodeId_Type()
)
logRingElemNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemNodeId.setStatus("current")


class _LogRingElemRxSegCutSeverity_Type(Integer32):
    """Custom type logRingElemRxSegCutSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoss", 1),
          ("serviceAffecting", 3),
          ("sonetProtection", 2))
    )


_LogRingElemRxSegCutSeverity_Type.__name__ = "Integer32"
_LogRingElemRxSegCutSeverity_Object = MibTableColumn
logRingElemRxSegCutSeverity = _LogRingElemRxSegCutSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 5, 1, 13),
    _LogRingElemRxSegCutSeverity_Type()
)
logRingElemRxSegCutSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logRingElemRxSegCutSeverity.setStatus("current")
_CfgRingCount_Type = Integer32
_CfgRingCount_Object = MibScalar
cfgRingCount = _CfgRingCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 6),
    _CfgRingCount_Type()
)
cfgRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCount.setStatus("current")
_CfgRingTable_Object = MibTable
cfgRingTable = _CfgRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7)
)
if mibBuilder.loadTexts:
    cfgRingTable.setStatus("current")
_CfgRingEntry_Object = MibTableRow
cfgRingEntry = _CfgRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1)
)
cfgRingEntry.setIndexNames(
    (0, "RING-MIB", "phyRingSlotNo"),
    (0, "RING-MIB", "phyRingPortNo"),
    (0, "RING-MIB", "logRingVPortNo"),
)
if mibBuilder.loadTexts:
    cfgRingEntry.setStatus("current")


class _CfgRingRowStatus_Type(Integer32):
    """Custom type cfgRingRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("delete", 6),
          ("out-of-service", 2))
    )


_CfgRingRowStatus_Type.__name__ = "Integer32"
_CfgRingRowStatus_Object = MibTableColumn
cfgRingRowStatus = _CfgRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 1),
    _CfgRingRowStatus_Type()
)
cfgRingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingRowStatus.setStatus("current")


class _CfgRingAdminCost_Type(Integer32):
    """Custom type cfgRingAdminCost based on Integer32"""
    defaultValue = 100


_CfgRingAdminCost_Object = MibTableColumn
cfgRingAdminCost = _CfgRingAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 2),
    _CfgRingAdminCost_Type()
)
cfgRingAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingAdminCost.setStatus("current")


class _CfgRingName_Type(DisplayString):
    """Custom type cfgRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CfgRingName_Type.__name__ = "DisplayString"
_CfgRingName_Object = MibTableColumn
cfgRingName = _CfgRingName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 3),
    _CfgRingName_Type()
)
cfgRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingName.setStatus("current")


class _CfgRingMeshFactor_Type(Integer32):
    """Custom type cfgRingMeshFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CfgRingMeshFactor_Type.__name__ = "Integer32"
_CfgRingMeshFactor_Object = MibTableColumn
cfgRingMeshFactor = _CfgRingMeshFactor_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 4),
    _CfgRingMeshFactor_Type()
)
cfgRingMeshFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingMeshFactor.setStatus("current")


class _CfgRingEirOverSub_Type(Integer32):
    """Custom type cfgRingEirOverSub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65000),
    )


_CfgRingEirOverSub_Type.__name__ = "Integer32"
_CfgRingEirOverSub_Object = MibTableColumn
cfgRingEirOverSub = _CfgRingEirOverSub_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 5),
    _CfgRingEirOverSub_Type()
)
cfgRingEirOverSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingEirOverSub.setStatus("current")


class _CfgRingProtectMode_Type(Integer32):
    """Custom type cfgRingProtectMode based on Integer32"""
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
        *(("blsr", 3),
          ("flex", 4),
          ("none", 1),
          ("upsr", 2))
    )


_CfgRingProtectMode_Type.__name__ = "Integer32"
_CfgRingProtectMode_Object = MibTableColumn
cfgRingProtectMode = _CfgRingProtectMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 6),
    _CfgRingProtectMode_Type()
)
cfgRingProtectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingProtectMode.setStatus("current")


class _CfgRingExceptNes_Type(DisplayString):
    """Custom type cfgRingExceptNes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 496),
    )


_CfgRingExceptNes_Type.__name__ = "DisplayString"
_CfgRingExceptNes_Object = MibTableColumn
cfgRingExceptNes = _CfgRingExceptNes_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 7),
    _CfgRingExceptNes_Type()
)
cfgRingExceptNes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingExceptNes.setStatus("current")


class _CfgRingNeTopo_Type(DisplayString):
    """Custom type cfgRingNeTopo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 496),
    )


_CfgRingNeTopo_Type.__name__ = "DisplayString"
_CfgRingNeTopo_Object = MibTableColumn
cfgRingNeTopo = _CfgRingNeTopo_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 8),
    _CfgRingNeTopo_Type()
)
cfgRingNeTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingNeTopo.setStatus("current")


class _CfgRingIpMode_Type(Integer32):
    """Custom type cfgRingIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gneSupplied", 1),
          ("takenFromNe", 2))
    )


_CfgRingIpMode_Type.__name__ = "Integer32"
_CfgRingIpMode_Object = MibTableColumn
cfgRingIpMode = _CfgRingIpMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 9),
    _CfgRingIpMode_Type()
)
cfgRingIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingIpMode.setStatus("current")


class _CfgRingFrameMode_Type(Integer32):
    """Custom type cfgRingFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("axson", 1),
          ("axsonNBOS", 3),
          ("pos", 2))
    )


_CfgRingFrameMode_Type.__name__ = "Integer32"
_CfgRingFrameMode_Object = MibTableColumn
cfgRingFrameMode = _CfgRingFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 10),
    _CfgRingFrameMode_Type()
)
cfgRingFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingFrameMode.setStatus("current")


class _CfgRingOperStatus_Type(Integer32):
    """Custom type cfgRingOperStatus based on Integer32"""
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


_CfgRingOperStatus_Type.__name__ = "Integer32"
_CfgRingOperStatus_Object = MibTableColumn
cfgRingOperStatus = _CfgRingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 13),
    _CfgRingOperStatus_Type()
)
cfgRingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingOperStatus.setStatus("current")
_CfgRingCurNumTdmCkts_Type = Integer32
_CfgRingCurNumTdmCkts_Object = MibTableColumn
cfgRingCurNumTdmCkts = _CfgRingCurNumTdmCkts_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 14),
    _CfgRingCurNumTdmCkts_Type()
)
cfgRingCurNumTdmCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurNumTdmCkts.setStatus("current")
_CfgRingCurNumFreeChans_Type = Integer32
_CfgRingCurNumFreeChans_Object = MibTableColumn
cfgRingCurNumFreeChans = _CfgRingCurNumFreeChans_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 15),
    _CfgRingCurNumFreeChans_Type()
)
cfgRingCurNumFreeChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurNumFreeChans.setStatus("current")


class _CfgRingNeAdminCost_Type(DisplayString):
    """Custom type cfgRingNeAdminCost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 720),
    )


_CfgRingNeAdminCost_Type.__name__ = "DisplayString"
_CfgRingNeAdminCost_Object = MibTableColumn
cfgRingNeAdminCost = _CfgRingNeAdminCost_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 16),
    _CfgRingNeAdminCost_Type()
)
cfgRingNeAdminCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingNeAdminCost.setStatus("current")
_CfgRingCurNumDataCkts_Type = Integer32
_CfgRingCurNumDataCkts_Object = MibTableColumn
cfgRingCurNumDataCkts = _CfgRingCurNumDataCkts_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 17),
    _CfgRingCurNumDataCkts_Type()
)
cfgRingCurNumDataCkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurNumDataCkts.setStatus("current")
_CfgRingCurAllocTdmBwKbits_Type = Integer32
_CfgRingCurAllocTdmBwKbits_Object = MibTableColumn
cfgRingCurAllocTdmBwKbits = _CfgRingCurAllocTdmBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 18),
    _CfgRingCurAllocTdmBwKbits_Type()
)
cfgRingCurAllocTdmBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurAllocTdmBwKbits.setStatus("current")
_CfgRingCurAllocCirBwKbits_Type = Integer32
_CfgRingCurAllocCirBwKbits_Object = MibTableColumn
cfgRingCurAllocCirBwKbits = _CfgRingCurAllocCirBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 19),
    _CfgRingCurAllocCirBwKbits_Type()
)
cfgRingCurAllocCirBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurAllocCirBwKbits.setStatus("current")
_CfgRingCurAllocEirBwKbits_Type = Integer32
_CfgRingCurAllocEirBwKbits_Object = MibTableColumn
cfgRingCurAllocEirBwKbits = _CfgRingCurAllocEirBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 20),
    _CfgRingCurAllocEirBwKbits_Type()
)
cfgRingCurAllocEirBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurAllocEirBwKbits.setStatus("current")
_CfgRingCurAvailBwKbits_Type = Integer32
_CfgRingCurAvailBwKbits_Object = MibTableColumn
cfgRingCurAvailBwKbits = _CfgRingCurAvailBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 21),
    _CfgRingCurAvailBwKbits_Type()
)
cfgRingCurAvailBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurAvailBwKbits.setStatus("current")


class _CfgRingTdmAvgUtilPercent_Type(Integer32):
    """Custom type cfgRingTdmAvgUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTdmAvgUtilPercent_Type.__name__ = "Integer32"
_CfgRingTdmAvgUtilPercent_Object = MibTableColumn
cfgRingTdmAvgUtilPercent = _CfgRingTdmAvgUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 22),
    _CfgRingTdmAvgUtilPercent_Type()
)
cfgRingTdmAvgUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmAvgUtilPercent.setStatus("current")


class _CfgRingTdmLastUtilPercent_Type(Integer32):
    """Custom type cfgRingTdmLastUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTdmLastUtilPercent_Type.__name__ = "Integer32"
_CfgRingTdmLastUtilPercent_Object = MibTableColumn
cfgRingTdmLastUtilPercent = _CfgRingTdmLastUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 23),
    _CfgRingTdmLastUtilPercent_Type()
)
cfgRingTdmLastUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmLastUtilPercent.setStatus("current")


class _CfgRingTdmMaxUtilPercent_Type(Integer32):
    """Custom type cfgRingTdmMaxUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTdmMaxUtilPercent_Type.__name__ = "Integer32"
_CfgRingTdmMaxUtilPercent_Object = MibTableColumn
cfgRingTdmMaxUtilPercent = _CfgRingTdmMaxUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 24),
    _CfgRingTdmMaxUtilPercent_Type()
)
cfgRingTdmMaxUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmMaxUtilPercent.setStatus("current")


class _CfgRingDataAvgUtilPercent_Type(Integer32):
    """Custom type cfgRingDataAvgUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingDataAvgUtilPercent_Type.__name__ = "Integer32"
_CfgRingDataAvgUtilPercent_Object = MibTableColumn
cfgRingDataAvgUtilPercent = _CfgRingDataAvgUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 25),
    _CfgRingDataAvgUtilPercent_Type()
)
cfgRingDataAvgUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataAvgUtilPercent.setStatus("current")


class _CfgRingDataLastUtilPercent_Type(Integer32):
    """Custom type cfgRingDataLastUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingDataLastUtilPercent_Type.__name__ = "Integer32"
_CfgRingDataLastUtilPercent_Object = MibTableColumn
cfgRingDataLastUtilPercent = _CfgRingDataLastUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 26),
    _CfgRingDataLastUtilPercent_Type()
)
cfgRingDataLastUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataLastUtilPercent.setStatus("current")


class _CfgRingDataMaxUtilPercent_Type(Integer32):
    """Custom type cfgRingDataMaxUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingDataMaxUtilPercent_Type.__name__ = "Integer32"
_CfgRingDataMaxUtilPercent_Object = MibTableColumn
cfgRingDataMaxUtilPercent = _CfgRingDataMaxUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 27),
    _CfgRingDataMaxUtilPercent_Type()
)
cfgRingDataMaxUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataMaxUtilPercent.setStatus("current")


class _CfgRingTotalAvgUtilPercent_Type(Integer32):
    """Custom type cfgRingTotalAvgUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTotalAvgUtilPercent_Type.__name__ = "Integer32"
_CfgRingTotalAvgUtilPercent_Object = MibTableColumn
cfgRingTotalAvgUtilPercent = _CfgRingTotalAvgUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 28),
    _CfgRingTotalAvgUtilPercent_Type()
)
cfgRingTotalAvgUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTotalAvgUtilPercent.setStatus("current")


class _CfgRingTotalLastUtilPercent_Type(Integer32):
    """Custom type cfgRingTotalLastUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTotalLastUtilPercent_Type.__name__ = "Integer32"
_CfgRingTotalLastUtilPercent_Object = MibTableColumn
cfgRingTotalLastUtilPercent = _CfgRingTotalLastUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 29),
    _CfgRingTotalLastUtilPercent_Type()
)
cfgRingTotalLastUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTotalLastUtilPercent.setStatus("current")


class _CfgRingTotalMaxUtilPercent_Type(Integer32):
    """Custom type cfgRingTotalMaxUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTotalMaxUtilPercent_Type.__name__ = "Integer32"
_CfgRingTotalMaxUtilPercent_Object = MibTableColumn
cfgRingTotalMaxUtilPercent = _CfgRingTotalMaxUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 30),
    _CfgRingTotalMaxUtilPercent_Type()
)
cfgRingTotalMaxUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTotalMaxUtilPercent.setStatus("current")
_CfgRingTdmTrafficKbits_Type = Counter64
_CfgRingTdmTrafficKbits_Object = MibTableColumn
cfgRingTdmTrafficKbits = _CfgRingTdmTrafficKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 31),
    _CfgRingTdmTrafficKbits_Type()
)
cfgRingTdmTrafficKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmTrafficKbits.setStatus("current")
_CfgRingTdmLastTrafficKbits_Type = Counter64
_CfgRingTdmLastTrafficKbits_Object = MibTableColumn
cfgRingTdmLastTrafficKbits = _CfgRingTdmLastTrafficKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 32),
    _CfgRingTdmLastTrafficKbits_Type()
)
cfgRingTdmLastTrafficKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmLastTrafficKbits.setStatus("current")
_CfgRingDataTrafficKbits_Type = Counter64
_CfgRingDataTrafficKbits_Object = MibTableColumn
cfgRingDataTrafficKbits = _CfgRingDataTrafficKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 33),
    _CfgRingDataTrafficKbits_Type()
)
cfgRingDataTrafficKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataTrafficKbits.setStatus("current")
_CfgRingDataLastTrafficKbits_Type = Counter64
_CfgRingDataLastTrafficKbits_Object = MibTableColumn
cfgRingDataLastTrafficKbits = _CfgRingDataLastTrafficKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 34),
    _CfgRingDataLastTrafficKbits_Type()
)
cfgRingDataLastTrafficKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataLastTrafficKbits.setStatus("current")
_CfgRingDataNumPkts_Type = Counter64
_CfgRingDataNumPkts_Object = MibTableColumn
cfgRingDataNumPkts = _CfgRingDataNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 35),
    _CfgRingDataNumPkts_Type()
)
cfgRingDataNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataNumPkts.setStatus("current")
_CfgRingDataLastNumPkts_Type = Counter64
_CfgRingDataLastNumPkts_Object = MibTableColumn
cfgRingDataLastNumPkts = _CfgRingDataLastNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 36),
    _CfgRingDataLastNumPkts_Type()
)
cfgRingDataLastNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataLastNumPkts.setStatus("current")
_CfgRingStatsCollElapsedTime_Type = TimeTicks
_CfgRingStatsCollElapsedTime_Object = MibTableColumn
cfgRingStatsCollElapsedTime = _CfgRingStatsCollElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 37),
    _CfgRingStatsCollElapsedTime_Type()
)
cfgRingStatsCollElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingStatsCollElapsedTime.setStatus("current")
_CfgRingStatsPeriodTime_Type = TimeTicks
_CfgRingStatsPeriodTime_Object = MibTableColumn
cfgRingStatsPeriodTime = _CfgRingStatsPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 38),
    _CfgRingStatsPeriodTime_Type()
)
cfgRingStatsPeriodTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingStatsPeriodTime.setStatus("current")
_CfgRingTimeSinceLastOperStatusChange_Type = TimeTicks
_CfgRingTimeSinceLastOperStatusChange_Object = MibTableColumn
cfgRingTimeSinceLastOperStatusChange = _CfgRingTimeSinceLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 39),
    _CfgRingTimeSinceLastOperStatusChange_Type()
)
cfgRingTimeSinceLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTimeSinceLastOperStatusChange.setStatus("current")


class _CfgRingTdmMinUtilPercent_Type(Integer32):
    """Custom type cfgRingTdmMinUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingTdmMinUtilPercent_Type.__name__ = "Integer32"
_CfgRingTdmMinUtilPercent_Object = MibTableColumn
cfgRingTdmMinUtilPercent = _CfgRingTdmMinUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 40),
    _CfgRingTdmMinUtilPercent_Type()
)
cfgRingTdmMinUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTdmMinUtilPercent.setStatus("current")


class _CfgRingDataMinUtilPercent_Type(Integer32):
    """Custom type cfgRingDataMinUtilPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CfgRingDataMinUtilPercent_Type.__name__ = "Integer32"
_CfgRingDataMinUtilPercent_Object = MibTableColumn
cfgRingDataMinUtilPercent = _CfgRingDataMinUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 41),
    _CfgRingDataMinUtilPercent_Type()
)
cfgRingDataMinUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingDataMinUtilPercent.setStatus("current")
_CfgRingTotalMinUtilPercent_Type = Integer32
_CfgRingTotalMinUtilPercent_Object = MibTableColumn
cfgRingTotalMinUtilPercent = _CfgRingTotalMinUtilPercent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 42),
    _CfgRingTotalMinUtilPercent_Type()
)
cfgRingTotalMinUtilPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingTotalMinUtilPercent.setStatus("current")


class _CfgRingAttUpsrSwitchCmd_Type(Integer32):
    """Custom type cfgRingAttUpsrSwitchCmd based on Integer32"""
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
        *(("axsonUpsrScClear", 1),
          ("axsonUpsrScForcedSwToProtection", 3),
          ("axsonUpsrScForcedSwToWorking", 4),
          ("axsonUpsrScLockoutOfProtection", 2),
          ("axsonUpsrScManualSwToProtection", 5),
          ("axsonUpsrScManualSwToWorking", 6))
    )


_CfgRingAttUpsrSwitchCmd_Type.__name__ = "Integer32"
_CfgRingAttUpsrSwitchCmd_Object = MibTableColumn
cfgRingAttUpsrSwitchCmd = _CfgRingAttUpsrSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 43),
    _CfgRingAttUpsrSwitchCmd_Type()
)
cfgRingAttUpsrSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingAttUpsrSwitchCmd.setStatus("current")
_CfgRingIsRevertiveModeEnabled_Type = TruthValue
_CfgRingIsRevertiveModeEnabled_Object = MibTableColumn
cfgRingIsRevertiveModeEnabled = _CfgRingIsRevertiveModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 44),
    _CfgRingIsRevertiveModeEnabled_Type()
)
cfgRingIsRevertiveModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingIsRevertiveModeEnabled.setStatus("current")


class _CfgRingWaitToRestorePeriod_Type(Integer32):
    """Custom type cfgRingWaitToRestorePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_CfgRingWaitToRestorePeriod_Type.__name__ = "Integer32"
_CfgRingWaitToRestorePeriod_Object = MibTableColumn
cfgRingWaitToRestorePeriod = _CfgRingWaitToRestorePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 45),
    _CfgRingWaitToRestorePeriod_Type()
)
cfgRingWaitToRestorePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgRingWaitToRestorePeriod.setStatus("current")
_CfgRingCurTdmAvailBwKbits_Type = Integer32
_CfgRingCurTdmAvailBwKbits_Object = MibTableColumn
cfgRingCurTdmAvailBwKbits = _CfgRingCurTdmAvailBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 46),
    _CfgRingCurTdmAvailBwKbits_Type()
)
cfgRingCurTdmAvailBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurTdmAvailBwKbits.setStatus("current")
_CfgRingCurDataAvailBwKbits_Type = Integer32
_CfgRingCurDataAvailBwKbits_Object = MibTableColumn
cfgRingCurDataAvailBwKbits = _CfgRingCurDataAvailBwKbits_Object(
    (1, 3, 6, 1, 4, 1, 5812, 4, 7, 1, 47),
    _CfgRingCurDataAvailBwKbits_Type()
)
cfgRingCurDataAvailBwKbits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgRingCurDataAvailBwKbits.setStatus("current")

# Managed Objects groups


# Notification objects

ringOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 3)
)
ringOperStatusChange.setObjects(
      *(("RING-MIB", "cfgRingName"),
        ("RING-MIB", "cfgRingOperStatus"))
)
if mibBuilder.loadTexts:
    ringOperStatusChange.setStatus(
        ""
    )

neReachabilityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 4)
)
neReachabilityChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("DEVICE-MIB", "chassisIpAddr"),
        ("DEVICE-MIB", "chassisElemReachStatus"))
)
if mibBuilder.loadTexts:
    neReachabilityChange.setStatus(
        ""
    )

lambdaStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 5)
)
lambdaStatusChange.setObjects(
      *(("RING-MIB", "cfgRingName"),
        ("RING-MIB", "logRingLambdaStatus"),
        ("RING-MIB", "logRingCutLocationIp"),
        ("RING-MIB", "logRingCutLocationName"))
)
if mibBuilder.loadTexts:
    lambdaStatusChange.setStatus(
        ""
    )

ringProtoErrorStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 6)
)
ringProtoErrorStatusChange.setObjects(
      *(("RING-MIB", "cfgRingName"),
        ("RING-MIB", "logRingProtoStatusTxt"),
        ("RING-MIB", "logRingProtoStatus"))
)
if mibBuilder.loadTexts:
    ringProtoErrorStatusChange.setStatus(
        ""
    )

ringProtoWarnStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 7)
)
ringProtoWarnStatusChange.setObjects(
      *(("RING-MIB", "cfgRingName"),
        ("RING-MIB", "logRingProtoStatusTxt"),
        ("RING-MIB", "logRingProtoStatus"))
)
if mibBuilder.loadTexts:
    ringProtoWarnStatusChange.setStatus(
        ""
    )

ringTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 56)
)
ringTopoChange.setObjects(
    ("RING-MIB", "cfgRingName")
)
if mibBuilder.loadTexts:
    ringTopoChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RING-MIB",
    **{"ringOperStatusChange": ringOperStatusChange,
       "neReachabilityChange": neReachabilityChange,
       "lambdaStatusChange": lambdaStatusChange,
       "ringProtoErrorStatusChange": ringProtoErrorStatusChange,
       "ringProtoWarnStatusChange": ringProtoWarnStatusChange,
       "ringTopoChange": ringTopoChange,
       "actPhyRingCount": actPhyRingCount,
       "actPhyRingTable": actPhyRingTable,
       "actPhyRingEntry": actPhyRingEntry,
       "phyRingSlotNo": phyRingSlotNo,
       "phyRingPortNo": phyRingPortNo,
       "actLogRingCount": actLogRingCount,
       "actLogRingTable": actLogRingTable,
       "actLogRingEntry": actLogRingEntry,
       "logRingVPortNo": logRingVPortNo,
       "logRingElemCount": logRingElemCount,
       "logRingLambdaStatus": logRingLambdaStatus,
       "logRingProtoStatusTxt": logRingProtoStatusTxt,
       "logRingProtoStatus": logRingProtoStatus,
       "logRingGneName": logRingGneName,
       "logRingGneIpAddr": logRingGneIpAddr,
       "logRingGneRingSlot": logRingGneRingSlot,
       "logRingGneRingPort": logRingGneRingPort,
       "logRingGneRingVport": logRingGneRingVport,
       "logRingUpsNgbrName": logRingUpsNgbrName,
       "logRingUpsNgbrIpAddr": logRingUpsNgbrIpAddr,
       "logRingUpsNgbrRingSlot": logRingUpsNgbrRingSlot,
       "logRingUpsNgbrRingPort": logRingUpsNgbrRingPort,
       "logRingUpsNgbrRingVport": logRingUpsNgbrRingVport,
       "logRingIsConfigured": logRingIsConfigured,
       "logRingAttRingType": logRingAttRingType,
       "logRingCapacity": logRingCapacity,
       "logRingCutLocationIp": logRingCutLocationIp,
       "logRingCutLocationName": logRingCutLocationName,
       "logRingIsRingMaster": logRingIsRingMaster,
       "logRingOtherSlot": logRingOtherSlot,
       "logRingOtherPort": logRingOtherPort,
       "logRingOtherVport": logRingOtherVport,
       "actLogRingElemTable": actLogRingElemTable,
       "actLogRingElemEntry": actLogRingElemEntry,
       "logRingElemIndex": logRingElemIndex,
       "logRingElemName": logRingElemName,
       "logRingElemMACAddr": logRingElemMACAddr,
       "logRingElemIpAddr": logRingElemIpAddr,
       "logRingElemPortId": logRingElemPortId,
       "logRingElemChassisId": logRingElemChassisId,
       "logRingElemActiveMM": logRingElemActiveMM,
       "logRingElemIsInNeTable": logRingElemIsInNeTable,
       "logRingElemIsReachable": logRingElemIsReachable,
       "logRingElemIsLambdaCutHere": logRingElemIsLambdaCutHere,
       "logRingElemChassisCharacter": logRingElemChassisCharacter,
       "logRingElemNodeId": logRingElemNodeId,
       "logRingElemRxSegCutSeverity": logRingElemRxSegCutSeverity,
       "cfgRingCount": cfgRingCount,
       "cfgRingTable": cfgRingTable,
       "cfgRingEntry": cfgRingEntry,
       "cfgRingRowStatus": cfgRingRowStatus,
       "cfgRingAdminCost": cfgRingAdminCost,
       "cfgRingName": cfgRingName,
       "cfgRingMeshFactor": cfgRingMeshFactor,
       "cfgRingEirOverSub": cfgRingEirOverSub,
       "cfgRingProtectMode": cfgRingProtectMode,
       "cfgRingExceptNes": cfgRingExceptNes,
       "cfgRingNeTopo": cfgRingNeTopo,
       "cfgRingIpMode": cfgRingIpMode,
       "cfgRingFrameMode": cfgRingFrameMode,
       "cfgRingOperStatus": cfgRingOperStatus,
       "cfgRingCurNumTdmCkts": cfgRingCurNumTdmCkts,
       "cfgRingCurNumFreeChans": cfgRingCurNumFreeChans,
       "cfgRingNeAdminCost": cfgRingNeAdminCost,
       "cfgRingCurNumDataCkts": cfgRingCurNumDataCkts,
       "cfgRingCurAllocTdmBwKbits": cfgRingCurAllocTdmBwKbits,
       "cfgRingCurAllocCirBwKbits": cfgRingCurAllocCirBwKbits,
       "cfgRingCurAllocEirBwKbits": cfgRingCurAllocEirBwKbits,
       "cfgRingCurAvailBwKbits": cfgRingCurAvailBwKbits,
       "cfgRingTdmAvgUtilPercent": cfgRingTdmAvgUtilPercent,
       "cfgRingTdmLastUtilPercent": cfgRingTdmLastUtilPercent,
       "cfgRingTdmMaxUtilPercent": cfgRingTdmMaxUtilPercent,
       "cfgRingDataAvgUtilPercent": cfgRingDataAvgUtilPercent,
       "cfgRingDataLastUtilPercent": cfgRingDataLastUtilPercent,
       "cfgRingDataMaxUtilPercent": cfgRingDataMaxUtilPercent,
       "cfgRingTotalAvgUtilPercent": cfgRingTotalAvgUtilPercent,
       "cfgRingTotalLastUtilPercent": cfgRingTotalLastUtilPercent,
       "cfgRingTotalMaxUtilPercent": cfgRingTotalMaxUtilPercent,
       "cfgRingTdmTrafficKbits": cfgRingTdmTrafficKbits,
       "cfgRingTdmLastTrafficKbits": cfgRingTdmLastTrafficKbits,
       "cfgRingDataTrafficKbits": cfgRingDataTrafficKbits,
       "cfgRingDataLastTrafficKbits": cfgRingDataLastTrafficKbits,
       "cfgRingDataNumPkts": cfgRingDataNumPkts,
       "cfgRingDataLastNumPkts": cfgRingDataLastNumPkts,
       "cfgRingStatsCollElapsedTime": cfgRingStatsCollElapsedTime,
       "cfgRingStatsPeriodTime": cfgRingStatsPeriodTime,
       "cfgRingTimeSinceLastOperStatusChange": cfgRingTimeSinceLastOperStatusChange,
       "cfgRingTdmMinUtilPercent": cfgRingTdmMinUtilPercent,
       "cfgRingDataMinUtilPercent": cfgRingDataMinUtilPercent,
       "cfgRingTotalMinUtilPercent": cfgRingTotalMinUtilPercent,
       "cfgRingAttUpsrSwitchCmd": cfgRingAttUpsrSwitchCmd,
       "cfgRingIsRevertiveModeEnabled": cfgRingIsRevertiveModeEnabled,
       "cfgRingWaitToRestorePeriod": cfgRingWaitToRestorePeriod,
       "cfgRingCurTdmAvailBwKbits": cfgRingCurTdmAvailBwKbits,
       "cfgRingCurDataAvailBwKbits": cfgRingCurDataAvailBwKbits,
       "ringMIB": ringMIB}
)
