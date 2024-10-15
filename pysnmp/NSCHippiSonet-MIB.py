# SNMP MIB module (NSCHippiSonet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NSCHippiSonet-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:30 2024
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

(nscHippiSonet,) = mibBuilder.importSymbols(
    "NSC-MIB",
    "nscHippiSonet")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NscHippiSonetEngineStatus_Type = DisplayString
_NscHippiSonetEngineStatus_Object = MibScalar
nscHippiSonetEngineStatus = _NscHippiSonetEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 1),
    _NscHippiSonetEngineStatus_Type()
)
nscHippiSonetEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetEngineStatus.setStatus("mandatory")
_NscHippiSonetRegisters_ObjectIdentity = ObjectIdentity
nscHippiSonetRegisters = _NscHippiSonetRegisters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2)
)
_NscHippiSonetUnframer_ObjectIdentity = ObjectIdentity
nscHippiSonetUnframer = _NscHippiSonetUnframer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 1)
)
_NscHippiSonetUnframerStatus_Type = DisplayString
_NscHippiSonetUnframerStatus_Object = MibScalar
nscHippiSonetUnframerStatus = _NscHippiSonetUnframerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 1, 1),
    _NscHippiSonetUnframerStatus_Type()
)
nscHippiSonetUnframerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetUnframerStatus.setStatus("mandatory")
_NscHippiSonetUnframerOHdma_Type = DisplayString
_NscHippiSonetUnframerOHdma_Object = MibScalar
nscHippiSonetUnframerOHdma = _NscHippiSonetUnframerOHdma_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 1, 2),
    _NscHippiSonetUnframerOHdma_Type()
)
nscHippiSonetUnframerOHdma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetUnframerOHdma.setStatus("mandatory")
_NscHippiSonetFramer_ObjectIdentity = ObjectIdentity
nscHippiSonetFramer = _NscHippiSonetFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2)
)
_NscHippiSonetFramerStatus_Type = DisplayString
_NscHippiSonetFramerStatus_Object = MibScalar
nscHippiSonetFramerStatus = _NscHippiSonetFramerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2, 1),
    _NscHippiSonetFramerStatus_Type()
)
nscHippiSonetFramerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetFramerStatus.setStatus("mandatory")
_NscHippiSonetFramerAdaptID_Type = DisplayString
_NscHippiSonetFramerAdaptID_Object = MibScalar
nscHippiSonetFramerAdaptID = _NscHippiSonetFramerAdaptID_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2, 2),
    _NscHippiSonetFramerAdaptID_Type()
)
nscHippiSonetFramerAdaptID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetFramerAdaptID.setStatus("mandatory")
_NscHippiSonetFramerInput_Type = DisplayString
_NscHippiSonetFramerInput_Object = MibScalar
nscHippiSonetFramerInput = _NscHippiSonetFramerInput_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2, 3),
    _NscHippiSonetFramerInput_Type()
)
nscHippiSonetFramerInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetFramerInput.setStatus("mandatory")
_NscHippiSonetFramerData_Type = DisplayString
_NscHippiSonetFramerData_Object = MibScalar
nscHippiSonetFramerData = _NscHippiSonetFramerData_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2, 4),
    _NscHippiSonetFramerData_Type()
)
nscHippiSonetFramerData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetFramerData.setStatus("mandatory")
_NscHippiSonetFramerIField_Type = DisplayString
_NscHippiSonetFramerIField_Object = MibScalar
nscHippiSonetFramerIField = _NscHippiSonetFramerIField_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 2, 5),
    _NscHippiSonetFramerIField_Type()
)
nscHippiSonetFramerIField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetFramerIField.setStatus("mandatory")
_NscHippiSonetMegaFifo_ObjectIdentity = ObjectIdentity
nscHippiSonetMegaFifo = _NscHippiSonetMegaFifo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 3)
)
_NscHippiSonetMFcontrol_Type = DisplayString
_NscHippiSonetMFcontrol_Object = MibScalar
nscHippiSonetMFcontrol = _NscHippiSonetMFcontrol_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 3, 1),
    _NscHippiSonetMFcontrol_Type()
)
nscHippiSonetMFcontrol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMFcontrol.setStatus("mandatory")
_NscHippiSonetMFstatus_Type = DisplayString
_NscHippiSonetMFstatus_Object = MibScalar
nscHippiSonetMFstatus = _NscHippiSonetMFstatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 3, 2),
    _NscHippiSonetMFstatus_Type()
)
nscHippiSonetMFstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMFstatus.setStatus("mandatory")
_NscHippiSonetMFtimeout_Type = DisplayString
_NscHippiSonetMFtimeout_Object = MibScalar
nscHippiSonetMFtimeout = _NscHippiSonetMFtimeout_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 3, 3),
    _NscHippiSonetMFtimeout_Type()
)
nscHippiSonetMFtimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMFtimeout.setStatus("mandatory")
_NscHippiSonetMFConnectStatus_Type = DisplayString
_NscHippiSonetMFConnectStatus_Object = MibScalar
nscHippiSonetMFConnectStatus = _NscHippiSonetMFConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 2, 3, 4),
    _NscHippiSonetMFConnectStatus_Type()
)
nscHippiSonetMFConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMFConnectStatus.setStatus("mandatory")
_NscHippiSonetMonitor_ObjectIdentity = ObjectIdentity
nscHippiSonetMonitor = _NscHippiSonetMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3)
)
_NscHippiSonetMonClock_Type = Integer32
_NscHippiSonetMonClock_Object = MibScalar
nscHippiSonetMonClock = _NscHippiSonetMonClock_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 1),
    _NscHippiSonetMonClock_Type()
)
nscHippiSonetMonClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonClock.setStatus("mandatory")
_NscHippiSonetMonMFFlowControl_Type = Integer32
_NscHippiSonetMonMFFlowControl_Object = MibScalar
nscHippiSonetMonMFFlowControl = _NscHippiSonetMonMFFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 2),
    _NscHippiSonetMonMFFlowControl_Type()
)
nscHippiSonetMonMFFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonMFFlowControl.setStatus("mandatory")
_NscHippiSonetMonDLFlowControl_Type = Integer32
_NscHippiSonetMonDLFlowControl_Object = MibScalar
nscHippiSonetMonDLFlowControl = _NscHippiSonetMonDLFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 3),
    _NscHippiSonetMonDLFlowControl_Type()
)
nscHippiSonetMonDLFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDLFlowControl.setStatus("mandatory")
_NscHippiSonetMonBIPErrors_Type = Integer32
_NscHippiSonetMonBIPErrors_Object = MibScalar
nscHippiSonetMonBIPErrors = _NscHippiSonetMonBIPErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 4),
    _NscHippiSonetMonBIPErrors_Type()
)
nscHippiSonetMonBIPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonBIPErrors.setStatus("mandatory")
_NscHippiSonetMonSrcBusy_Type = Integer32
_NscHippiSonetMonSrcBusy_Object = MibScalar
nscHippiSonetMonSrcBusy = _NscHippiSonetMonSrcBusy_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 5),
    _NscHippiSonetMonSrcBusy_Type()
)
nscHippiSonetMonSrcBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcBusy.setStatus("mandatory")
_NscHippiSonetMonSrcSOC_Type = Integer32
_NscHippiSonetMonSrcSOC_Object = MibScalar
nscHippiSonetMonSrcSOC = _NscHippiSonetMonSrcSOC_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 6),
    _NscHippiSonetMonSrcSOC_Type()
)
nscHippiSonetMonSrcSOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcSOC.setStatus("mandatory")
_NscHippiSonetMonSrcEOC_Type = Integer32
_NscHippiSonetMonSrcEOC_Object = MibScalar
nscHippiSonetMonSrcEOC = _NscHippiSonetMonSrcEOC_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 7),
    _NscHippiSonetMonSrcEOC_Type()
)
nscHippiSonetMonSrcEOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcEOC.setStatus("mandatory")
_NscHippiSonetMonDstConnectDuration_Type = Integer32
_NscHippiSonetMonDstConnectDuration_Object = MibScalar
nscHippiSonetMonDstConnectDuration = _NscHippiSonetMonDstConnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 8),
    _NscHippiSonetMonDstConnectDuration_Type()
)
nscHippiSonetMonDstConnectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstConnectDuration.setStatus("mandatory")
_NscHippiSonetMonSrcConnectDuration_Type = Integer32
_NscHippiSonetMonSrcConnectDuration_Object = MibScalar
nscHippiSonetMonSrcConnectDuration = _NscHippiSonetMonSrcConnectDuration_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 9),
    _NscHippiSonetMonSrcConnectDuration_Type()
)
nscHippiSonetMonSrcConnectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcConnectDuration.setStatus("mandatory")
_NscHippiSonetMonDstConnectReject_Type = Integer32
_NscHippiSonetMonDstConnectReject_Object = MibScalar
nscHippiSonetMonDstConnectReject = _NscHippiSonetMonDstConnectReject_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 10),
    _NscHippiSonetMonDstConnectReject_Type()
)
nscHippiSonetMonDstConnectReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstConnectReject.setStatus("mandatory")
_NscHippiSonetMonSrcConnectFail_Type = Integer32
_NscHippiSonetMonSrcConnectFail_Object = MibScalar
nscHippiSonetMonSrcConnectFail = _NscHippiSonetMonSrcConnectFail_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 11),
    _NscHippiSonetMonSrcConnectFail_Type()
)
nscHippiSonetMonSrcConnectFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcConnectFail.setStatus("mandatory")
_NscHippiSonetMonLOF_Type = Integer32
_NscHippiSonetMonLOF_Object = MibScalar
nscHippiSonetMonLOF = _NscHippiSonetMonLOF_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 12),
    _NscHippiSonetMonLOF_Type()
)
nscHippiSonetMonLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonLOF.setStatus("mandatory")
_NscHippiSonetMonLOS_Type = Integer32
_NscHippiSonetMonLOS_Object = MibScalar
nscHippiSonetMonLOS = _NscHippiSonetMonLOS_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 13),
    _NscHippiSonetMonLOS_Type()
)
nscHippiSonetMonLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonLOS.setStatus("mandatory")
_NscHippiSonetMonDstBursts_Type = Integer32
_NscHippiSonetMonDstBursts_Object = MibScalar
nscHippiSonetMonDstBursts = _NscHippiSonetMonDstBursts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 14),
    _NscHippiSonetMonDstBursts_Type()
)
nscHippiSonetMonDstBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstBursts.setStatus("mandatory")
_NscHippiSonetMonDstPackets_Type = Integer32
_NscHippiSonetMonDstPackets_Object = MibScalar
nscHippiSonetMonDstPackets = _NscHippiSonetMonDstPackets_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 15),
    _NscHippiSonetMonDstPackets_Type()
)
nscHippiSonetMonDstPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstPackets.setStatus("mandatory")
_NscHippiSonetMonDstSync_Type = Integer32
_NscHippiSonetMonDstSync_Object = MibScalar
nscHippiSonetMonDstSync = _NscHippiSonetMonDstSync_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 16),
    _NscHippiSonetMonDstSync_Type()
)
nscHippiSonetMonDstSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstSync.setStatus("mandatory")
_NscHippiSonetMonDstLLRC_Type = Integer32
_NscHippiSonetMonDstLLRC_Object = MibScalar
nscHippiSonetMonDstLLRC = _NscHippiSonetMonDstLLRC_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 17),
    _NscHippiSonetMonDstLLRC_Type()
)
nscHippiSonetMonDstLLRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstLLRC.setStatus("mandatory")
_NscHippiSonetMonDstPE_Type = Integer32
_NscHippiSonetMonDstPE_Object = MibScalar
nscHippiSonetMonDstPE = _NscHippiSonetMonDstPE_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 18),
    _NscHippiSonetMonDstPE_Type()
)
nscHippiSonetMonDstPE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstPE.setStatus("mandatory")
_NscHippiSonetMonDstConnect_Type = Integer32
_NscHippiSonetMonDstConnect_Object = MibScalar
nscHippiSonetMonDstConnect = _NscHippiSonetMonDstConnect_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 19),
    _NscHippiSonetMonDstConnect_Type()
)
nscHippiSonetMonDstConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstConnect.setStatus("mandatory")
_NscHippiSonetMonSrcConnect_Type = Integer32
_NscHippiSonetMonSrcConnect_Object = MibScalar
nscHippiSonetMonSrcConnect = _NscHippiSonetMonSrcConnect_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 20),
    _NscHippiSonetMonSrcConnect_Type()
)
nscHippiSonetMonSrcConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcConnect.setStatus("mandatory")
_NscHippiSonetMonSrcPackets_Type = Integer32
_NscHippiSonetMonSrcPackets_Object = MibScalar
nscHippiSonetMonSrcPackets = _NscHippiSonetMonSrcPackets_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 21),
    _NscHippiSonetMonSrcPackets_Type()
)
nscHippiSonetMonSrcPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcPackets.setStatus("mandatory")
_NscHippiSonetMonSrcBursts_Type = Integer32
_NscHippiSonetMonSrcBursts_Object = MibScalar
nscHippiSonetMonSrcBursts = _NscHippiSonetMonSrcBursts_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 22),
    _NscHippiSonetMonSrcBursts_Type()
)
nscHippiSonetMonSrcBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcBursts.setStatus("mandatory")
_NscHippiSonetMonSrcForceErrors_Type = Integer32
_NscHippiSonetMonSrcForceErrors_Object = MibScalar
nscHippiSonetMonSrcForceErrors = _NscHippiSonetMonSrcForceErrors_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 23),
    _NscHippiSonetMonSrcForceErrors_Type()
)
nscHippiSonetMonSrcForceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcForceErrors.setStatus("mandatory")
_NscHippiSonetMonSrcCRC_Type = Integer32
_NscHippiSonetMonSrcCRC_Object = MibScalar
nscHippiSonetMonSrcCRC = _NscHippiSonetMonSrcCRC_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 24),
    _NscHippiSonetMonSrcCRC_Type()
)
nscHippiSonetMonSrcCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcCRC.setStatus("mandatory")
_NscHippiSonetMonDstWords_Type = Integer32
_NscHippiSonetMonDstWords_Object = MibScalar
nscHippiSonetMonDstWords = _NscHippiSonetMonDstWords_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 25),
    _NscHippiSonetMonDstWords_Type()
)
nscHippiSonetMonDstWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonDstWords.setStatus("mandatory")
_NscHippiSonetMonSrcWords_Type = Integer32
_NscHippiSonetMonSrcWords_Object = MibScalar
nscHippiSonetMonSrcWords = _NscHippiSonetMonSrcWords_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 3, 26),
    _NscHippiSonetMonSrcWords_Type()
)
nscHippiSonetMonSrcWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetMonSrcWords.setStatus("mandatory")
_NscHippiSonetAtoD_ObjectIdentity = ObjectIdentity
nscHippiSonetAtoD = _NscHippiSonetAtoD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4)
)
_NscHippiSonetADRecvOpticalPower_Type = Integer32
_NscHippiSonetADRecvOpticalPower_Object = MibScalar
nscHippiSonetADRecvOpticalPower = _NscHippiSonetADRecvOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4, 1),
    _NscHippiSonetADRecvOpticalPower_Type()
)
nscHippiSonetADRecvOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetADRecvOpticalPower.setStatus("mandatory")
_NscHippiSonetADLaserBias_Type = Integer32
_NscHippiSonetADLaserBias_Object = MibScalar
nscHippiSonetADLaserBias = _NscHippiSonetADLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4, 2),
    _NscHippiSonetADLaserBias_Type()
)
nscHippiSonetADLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetADLaserBias.setStatus("mandatory")
_NscHippiSonetADLaserBackface_Type = Integer32
_NscHippiSonetADLaserBackface_Object = MibScalar
nscHippiSonetADLaserBackface = _NscHippiSonetADLaserBackface_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4, 3),
    _NscHippiSonetADLaserBackface_Type()
)
nscHippiSonetADLaserBackface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetADLaserBackface.setStatus("mandatory")
_NscHippiSonetADInternalTemp_Type = Integer32
_NscHippiSonetADInternalTemp_Object = MibScalar
nscHippiSonetADInternalTemp = _NscHippiSonetADInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4, 4),
    _NscHippiSonetADInternalTemp_Type()
)
nscHippiSonetADInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetADInternalTemp.setStatus("mandatory")
_NscHippiSonetADExhaustTemp_Type = Integer32
_NscHippiSonetADExhaustTemp_Object = MibScalar
nscHippiSonetADExhaustTemp = _NscHippiSonetADExhaustTemp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 4, 5),
    _NscHippiSonetADExhaustTemp_Type()
)
nscHippiSonetADExhaustTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetADExhaustTemp.setStatus("mandatory")
_NscHippiSonetSourceIField_Type = DisplayString
_NscHippiSonetSourceIField_Object = MibScalar
nscHippiSonetSourceIField = _NscHippiSonetSourceIField_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 5),
    _NscHippiSonetSourceIField_Type()
)
nscHippiSonetSourceIField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetSourceIField.setStatus("mandatory")
_NscHippiSonetProfile_ObjectIdentity = ObjectIdentity
nscHippiSonetProfile = _NscHippiSonetProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6)
)
_NscHippiSonetOpticalRcvOffset_Type = DisplayString
_NscHippiSonetOpticalRcvOffset_Object = MibScalar
nscHippiSonetOpticalRcvOffset = _NscHippiSonetOpticalRcvOffset_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 1),
    _NscHippiSonetOpticalRcvOffset_Type()
)
nscHippiSonetOpticalRcvOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetOpticalRcvOffset.setStatus("mandatory")
_NscHippiSonetOpticalRcvSlope_Type = DisplayString
_NscHippiSonetOpticalRcvSlope_Object = MibScalar
nscHippiSonetOpticalRcvSlope = _NscHippiSonetOpticalRcvSlope_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 2),
    _NscHippiSonetOpticalRcvSlope_Type()
)
nscHippiSonetOpticalRcvSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetOpticalRcvSlope.setStatus("mandatory")
_NscHippiSonetBiasCurrent_Type = Integer32
_NscHippiSonetBiasCurrent_Object = MibScalar
nscHippiSonetBiasCurrent = _NscHippiSonetBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 3),
    _NscHippiSonetBiasCurrent_Type()
)
nscHippiSonetBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetBiasCurrent.setStatus("mandatory")
_NscHippiSonetBiasTemp_Type = Integer32
_NscHippiSonetBiasTemp_Object = MibScalar
nscHippiSonetBiasTemp = _NscHippiSonetBiasTemp_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 4),
    _NscHippiSonetBiasTemp_Type()
)
nscHippiSonetBiasTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetBiasTemp.setStatus("mandatory")
_NscHippiSonetBackfaceVoltage_Type = DisplayString
_NscHippiSonetBackfaceVoltage_Object = MibScalar
nscHippiSonetBackfaceVoltage = _NscHippiSonetBackfaceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 5),
    _NscHippiSonetBackfaceVoltage_Type()
)
nscHippiSonetBackfaceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nscHippiSonetBackfaceVoltage.setStatus("mandatory")
_NscHippiSonetIField_Type = Integer32
_NscHippiSonetIField_Object = MibScalar
nscHippiSonetIField = _NscHippiSonetIField_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 6),
    _NscHippiSonetIField_Type()
)
nscHippiSonetIField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiSonetIField.setStatus("mandatory")


class _NscHippiSonetBootPort_Type(Integer32):
    """Custom type nscHippiSonetBootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NscHippiSonetBootPort_Type.__name__ = "Integer32"
_NscHippiSonetBootPort_Object = MibScalar
nscHippiSonetBootPort = _NscHippiSonetBootPort_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 7),
    _NscHippiSonetBootPort_Type()
)
nscHippiSonetBootPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiSonetBootPort.setStatus("mandatory")
_NscHippiSonetPortSpeed_Type = Integer32
_NscHippiSonetPortSpeed_Object = MibScalar
nscHippiSonetPortSpeed = _NscHippiSonetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 8),
    _NscHippiSonetPortSpeed_Type()
)
nscHippiSonetPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiSonetPortSpeed.setStatus("mandatory")


class _NscHippiSonetThreshold_Type(Integer32):
    """Custom type nscHippiSonetThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NscHippiSonetThreshold_Type.__name__ = "Integer32"
_NscHippiSonetThreshold_Object = MibScalar
nscHippiSonetThreshold = _NscHippiSonetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 9),
    _NscHippiSonetThreshold_Type()
)
nscHippiSonetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiSonetThreshold.setStatus("mandatory")


class _NscHippiTimeout_Type(Integer32):
    """Custom type nscHippiTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_NscHippiTimeout_Type.__name__ = "Integer32"
_NscHippiTimeout_Object = MibScalar
nscHippiTimeout = _NscHippiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 10),
    _NscHippiTimeout_Type()
)
nscHippiTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiTimeout.setStatus("mandatory")
_NscHippiSonetDipSwitch_Type = Integer32
_NscHippiSonetDipSwitch_Object = MibScalar
nscHippiSonetDipSwitch = _NscHippiSonetDipSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10, 2, 1, 5, 6, 11),
    _NscHippiSonetDipSwitch_Type()
)
nscHippiSonetDipSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nscHippiSonetDipSwitch.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCHippiSonet-MIB",
    **{"nscHippiSonetEngineStatus": nscHippiSonetEngineStatus,
       "nscHippiSonetRegisters": nscHippiSonetRegisters,
       "nscHippiSonetUnframer": nscHippiSonetUnframer,
       "nscHippiSonetUnframerStatus": nscHippiSonetUnframerStatus,
       "nscHippiSonetUnframerOHdma": nscHippiSonetUnframerOHdma,
       "nscHippiSonetFramer": nscHippiSonetFramer,
       "nscHippiSonetFramerStatus": nscHippiSonetFramerStatus,
       "nscHippiSonetFramerAdaptID": nscHippiSonetFramerAdaptID,
       "nscHippiSonetFramerInput": nscHippiSonetFramerInput,
       "nscHippiSonetFramerData": nscHippiSonetFramerData,
       "nscHippiSonetFramerIField": nscHippiSonetFramerIField,
       "nscHippiSonetMegaFifo": nscHippiSonetMegaFifo,
       "nscHippiSonetMFcontrol": nscHippiSonetMFcontrol,
       "nscHippiSonetMFstatus": nscHippiSonetMFstatus,
       "nscHippiSonetMFtimeout": nscHippiSonetMFtimeout,
       "nscHippiSonetMFConnectStatus": nscHippiSonetMFConnectStatus,
       "nscHippiSonetMonitor": nscHippiSonetMonitor,
       "nscHippiSonetMonClock": nscHippiSonetMonClock,
       "nscHippiSonetMonMFFlowControl": nscHippiSonetMonMFFlowControl,
       "nscHippiSonetMonDLFlowControl": nscHippiSonetMonDLFlowControl,
       "nscHippiSonetMonBIPErrors": nscHippiSonetMonBIPErrors,
       "nscHippiSonetMonSrcBusy": nscHippiSonetMonSrcBusy,
       "nscHippiSonetMonSrcSOC": nscHippiSonetMonSrcSOC,
       "nscHippiSonetMonSrcEOC": nscHippiSonetMonSrcEOC,
       "nscHippiSonetMonDstConnectDuration": nscHippiSonetMonDstConnectDuration,
       "nscHippiSonetMonSrcConnectDuration": nscHippiSonetMonSrcConnectDuration,
       "nscHippiSonetMonDstConnectReject": nscHippiSonetMonDstConnectReject,
       "nscHippiSonetMonSrcConnectFail": nscHippiSonetMonSrcConnectFail,
       "nscHippiSonetMonLOF": nscHippiSonetMonLOF,
       "nscHippiSonetMonLOS": nscHippiSonetMonLOS,
       "nscHippiSonetMonDstBursts": nscHippiSonetMonDstBursts,
       "nscHippiSonetMonDstPackets": nscHippiSonetMonDstPackets,
       "nscHippiSonetMonDstSync": nscHippiSonetMonDstSync,
       "nscHippiSonetMonDstLLRC": nscHippiSonetMonDstLLRC,
       "nscHippiSonetMonDstPE": nscHippiSonetMonDstPE,
       "nscHippiSonetMonDstConnect": nscHippiSonetMonDstConnect,
       "nscHippiSonetMonSrcConnect": nscHippiSonetMonSrcConnect,
       "nscHippiSonetMonSrcPackets": nscHippiSonetMonSrcPackets,
       "nscHippiSonetMonSrcBursts": nscHippiSonetMonSrcBursts,
       "nscHippiSonetMonSrcForceErrors": nscHippiSonetMonSrcForceErrors,
       "nscHippiSonetMonSrcCRC": nscHippiSonetMonSrcCRC,
       "nscHippiSonetMonDstWords": nscHippiSonetMonDstWords,
       "nscHippiSonetMonSrcWords": nscHippiSonetMonSrcWords,
       "nscHippiSonetAtoD": nscHippiSonetAtoD,
       "nscHippiSonetADRecvOpticalPower": nscHippiSonetADRecvOpticalPower,
       "nscHippiSonetADLaserBias": nscHippiSonetADLaserBias,
       "nscHippiSonetADLaserBackface": nscHippiSonetADLaserBackface,
       "nscHippiSonetADInternalTemp": nscHippiSonetADInternalTemp,
       "nscHippiSonetADExhaustTemp": nscHippiSonetADExhaustTemp,
       "nscHippiSonetSourceIField": nscHippiSonetSourceIField,
       "nscHippiSonetProfile": nscHippiSonetProfile,
       "nscHippiSonetOpticalRcvOffset": nscHippiSonetOpticalRcvOffset,
       "nscHippiSonetOpticalRcvSlope": nscHippiSonetOpticalRcvSlope,
       "nscHippiSonetBiasCurrent": nscHippiSonetBiasCurrent,
       "nscHippiSonetBiasTemp": nscHippiSonetBiasTemp,
       "nscHippiSonetBackfaceVoltage": nscHippiSonetBackfaceVoltage,
       "nscHippiSonetIField": nscHippiSonetIField,
       "nscHippiSonetBootPort": nscHippiSonetBootPort,
       "nscHippiSonetPortSpeed": nscHippiSonetPortSpeed,
       "nscHippiSonetThreshold": nscHippiSonetThreshold,
       "nscHippiTimeout": nscHippiTimeout,
       "nscHippiSonetDipSwitch": nscHippiSonetDipSwitch}
)
