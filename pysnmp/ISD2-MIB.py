# SNMP MIB module (ISD2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISD2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:43 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

_Isd2_ObjectIdentity = ObjectIdentity
isd2 = _Isd2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 48)
)
_Isd2SigChan_ObjectIdentity = ObjectIdentity
isd2SigChan = _Isd2SigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 48, 1)
)
_Isd2SigChanTable_Object = MibTable
isd2SigChanTable = _Isd2SigChanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1)
)
if mibBuilder.loadTexts:
    isd2SigChanTable.setStatus("mandatory")
_Isd2SigChanEntry_Object = MibTableRow
isd2SigChanEntry = _Isd2SigChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1)
)
isd2SigChanEntry.setIndexNames(
    (0, "ISD2-MIB", "isd2SigChanIfIndex"),
)
if mibBuilder.loadTexts:
    isd2SigChanEntry.setStatus("mandatory")
_Isd2SigChanIfIndex_Type = Integer32
_Isd2SigChanIfIndex_Object = MibTableColumn
isd2SigChanIfIndex = _Isd2SigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 1),
    _Isd2SigChanIfIndex_Type()
)
isd2SigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanIfIndex.setStatus("mandatory")


class _Isd2SigChanL2State_Type(Integer32):
    """Custom type isd2SigChanL2State based on Integer32"""
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
        *(("assignAwaitTei", 2),
          ("awaitEstablishment", 5),
          ("awaitRelease", 6),
          ("establishAwaitTei", 3),
          ("multipleFrameEstablished", 7),
          ("teiAssigned", 4),
          ("teiUnassigned", 1),
          ("timerRecovery", 8))
    )


_Isd2SigChanL2State_Type.__name__ = "Integer32"
_Isd2SigChanL2State_Object = MibTableColumn
isd2SigChanL2State = _Isd2SigChanL2State_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 2),
    _Isd2SigChanL2State_Type()
)
isd2SigChanL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanL2State.setStatus("mandatory")
_Isd2SigChanCES_Type = Counter32
_Isd2SigChanCES_Object = MibTableColumn
isd2SigChanCES = _Isd2SigChanCES_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 3),
    _Isd2SigChanCES_Type()
)
isd2SigChanCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanCES.setStatus("mandatory")
_Isd2SigChanSAPI_Type = Counter32
_Isd2SigChanSAPI_Object = MibTableColumn
isd2SigChanSAPI = _Isd2SigChanSAPI_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 4),
    _Isd2SigChanSAPI_Type()
)
isd2SigChanSAPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanSAPI.setStatus("mandatory")
_Isd2SigChanCallCollisions_Type = Counter32
_Isd2SigChanCallCollisions_Object = MibTableColumn
isd2SigChanCallCollisions = _Isd2SigChanCallCollisions_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 5),
    _Isd2SigChanCallCollisions_Type()
)
isd2SigChanCallCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanCallCollisions.setStatus("mandatory")
_Isd2SigChanAddressCheckFails_Type = Counter32
_Isd2SigChanAddressCheckFails_Object = MibTableColumn
isd2SigChanAddressCheckFails = _Isd2SigChanAddressCheckFails_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 1, 1, 1, 6),
    _Isd2SigChanAddressCheckFails_Type()
)
isd2SigChanAddressCheckFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2SigChanAddressCheckFails.setStatus("mandatory")
_Isd2Dchan_ObjectIdentity = ObjectIdentity
isd2Dchan = _Isd2Dchan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 48, 2)
)
_Isd2DchanTable_Object = MibTable
isd2DchanTable = _Isd2DchanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1)
)
if mibBuilder.loadTexts:
    isd2DchanTable.setStatus("mandatory")
_Isd2DchanEntry_Object = MibTableRow
isd2DchanEntry = _Isd2DchanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1)
)
isd2DchanEntry.setIndexNames(
    (0, "ISD2-MIB", "isd2DchanIfIndex"),
)
if mibBuilder.loadTexts:
    isd2DchanEntry.setStatus("mandatory")
_Isd2DchanIfIndex_Type = Integer32
_Isd2DchanIfIndex_Object = MibTableColumn
isd2DchanIfIndex = _Isd2DchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 1),
    _Isd2DchanIfIndex_Type()
)
isd2DchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanIfIndex.setStatus("mandatory")
_Isd2DchanRxShort_Type = Counter32
_Isd2DchanRxShort_Object = MibTableColumn
isd2DchanRxShort = _Isd2DchanRxShort_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 2),
    _Isd2DchanRxShort_Type()
)
isd2DchanRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxShort.setStatus("mandatory")
_Isd2DchanRxLong_Type = Counter32
_Isd2DchanRxLong_Object = MibTableColumn
isd2DchanRxLong = _Isd2DchanRxLong_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 3),
    _Isd2DchanRxLong_Type()
)
isd2DchanRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxLong.setStatus("mandatory")
_Isd2DchanRxCRCerror_Type = Counter32
_Isd2DchanRxCRCerror_Object = MibTableColumn
isd2DchanRxCRCerror = _Isd2DchanRxCRCerror_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 4),
    _Isd2DchanRxCRCerror_Type()
)
isd2DchanRxCRCerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxCRCerror.setStatus("mandatory")
_Isd2DchanRxResidual_Type = Counter32
_Isd2DchanRxResidual_Object = MibTableColumn
isd2DchanRxResidual = _Isd2DchanRxResidual_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 5),
    _Isd2DchanRxResidual_Type()
)
isd2DchanRxResidual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxResidual.setStatus("mandatory")
_Isd2DchanRxAborts_Type = Counter32
_Isd2DchanRxAborts_Object = MibTableColumn
isd2DchanRxAborts = _Isd2DchanRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 6),
    _Isd2DchanRxAborts_Type()
)
isd2DchanRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxAborts.setStatus("mandatory")
_Isd2DchanRxOverrun_Type = Counter32
_Isd2DchanRxOverrun_Object = MibTableColumn
isd2DchanRxOverrun = _Isd2DchanRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 7),
    _Isd2DchanRxOverrun_Type()
)
isd2DchanRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxOverrun.setStatus("mandatory")
_Isd2DchanRxLostSync_Type = Counter32
_Isd2DchanRxLostSync_Object = MibTableColumn
isd2DchanRxLostSync = _Isd2DchanRxLostSync_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 8),
    _Isd2DchanRxLostSync_Type()
)
isd2DchanRxLostSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxLostSync.setStatus("mandatory")
_Isd2DchanRxBufferLack_Type = Counter32
_Isd2DchanRxBufferLack_Object = MibTableColumn
isd2DchanRxBufferLack = _Isd2DchanRxBufferLack_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 9),
    _Isd2DchanRxBufferLack_Type()
)
isd2DchanRxBufferLack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxBufferLack.setStatus("mandatory")
_Isd2DchanRxApplnotready_Type = Counter32
_Isd2DchanRxApplnotready_Object = MibTableColumn
isd2DchanRxApplnotready = _Isd2DchanRxApplnotready_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 10),
    _Isd2DchanRxApplnotready_Type()
)
isd2DchanRxApplnotready.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxApplnotready.setStatus("mandatory")
_Isd2DchanRxUnknownProto_Type = Counter32
_Isd2DchanRxUnknownProto_Object = MibTableColumn
isd2DchanRxUnknownProto = _Isd2DchanRxUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 11),
    _Isd2DchanRxUnknownProto_Type()
)
isd2DchanRxUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanRxUnknownProto.setStatus("mandatory")
_Isd2DchanTxDiscardedProto_Type = Counter32
_Isd2DchanTxDiscardedProto_Object = MibTableColumn
isd2DchanTxDiscardedProto = _Isd2DchanTxDiscardedProto_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 12),
    _Isd2DchanTxDiscardedProto_Type()
)
isd2DchanTxDiscardedProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanTxDiscardedProto.setStatus("mandatory")
_Isd2DchanTxDiscardedData_Type = Counter32
_Isd2DchanTxDiscardedData_Object = MibTableColumn
isd2DchanTxDiscardedData = _Isd2DchanTxDiscardedData_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 13),
    _Isd2DchanTxDiscardedData_Type()
)
isd2DchanTxDiscardedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanTxDiscardedData.setStatus("mandatory")
_Isd2DchanTxUnderrun_Type = Counter32
_Isd2DchanTxUnderrun_Object = MibTableColumn
isd2DchanTxUnderrun = _Isd2DchanTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 14),
    _Isd2DchanTxUnderrun_Type()
)
isd2DchanTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanTxUnderrun.setStatus("mandatory")
_Isd2DchanTxCollision_Type = Counter32
_Isd2DchanTxCollision_Object = MibTableColumn
isd2DchanTxCollision = _Isd2DchanTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 2, 1, 1, 15),
    _Isd2DchanTxCollision_Type()
)
isd2DchanTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2DchanTxCollision.setStatus("mandatory")
_Isd2Phys_ObjectIdentity = ObjectIdentity
isd2Phys = _Isd2Phys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 48, 3)
)
_Isd2PhysTable_Object = MibTable
isd2PhysTable = _Isd2PhysTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 3, 1)
)
if mibBuilder.loadTexts:
    isd2PhysTable.setStatus("mandatory")
_Isd2PhysEntry_Object = MibTableRow
isd2PhysEntry = _Isd2PhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1)
)
isd2PhysEntry.setIndexNames(
    (0, "ISD2-MIB", "isd2PhysIfIndex"),
)
if mibBuilder.loadTexts:
    isd2PhysEntry.setStatus("mandatory")
_Isd2PhysIfIndex_Type = Integer32
_Isd2PhysIfIndex_Object = MibTableColumn
isd2PhysIfIndex = _Isd2PhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 1),
    _Isd2PhysIfIndex_Type()
)
isd2PhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2PhysIfIndex.setStatus("mandatory")


class _Isd2PhysL1State_Type(Integer32):
    """Custom type isd2PhysL1State based on Integer32"""
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
              100,
              101,
              102,
              103,
              104,
              105,
              106)
        )
    )
    namedValues = NamedValues(
        *(("activated", 7),
          ("awaitingSignal", 4),
          ("deactivated", 3),
          ("fault1", 102),
          ("fault2", 103),
          ("fault3", 104),
          ("fault4", 105),
          ("identifyingInput", 5),
          ("inactive", 1),
          ("lossOfPower", 100),
          ("lostFraming", 8),
          ("operational", 101),
          ("powerOn", 106),
          ("sensing", 2),
          ("synchronized", 6))
    )


_Isd2PhysL1State_Type.__name__ = "Integer32"
_Isd2PhysL1State_Object = MibTableColumn
isd2PhysL1State = _Isd2PhysL1State_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 2),
    _Isd2PhysL1State_Type()
)
isd2PhysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2PhysL1State.setStatus("mandatory")


class _Isd2PhysL1Alarm_Type(Integer32):
    """Custom type isd2PhysL1Alarm based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("alarmIndicationSignal", 4),
          ("crce0", 10),
          ("crce1", 11),
          ("ebit0", 12),
          ("ebit1", 13),
          ("lossOfSignal", 2),
          ("ncrc4", 9),
          ("noBasicFrameAlignment", 7),
          ("noCableInserted", 1),
          ("noMultiFrameAlignment", 6),
          ("noSyncPattern", 8),
          ("remoteAlarmIndication", 5),
          ("txCableNotConnected", 3))
    )


_Isd2PhysL1Alarm_Type.__name__ = "Integer32"
_Isd2PhysL1Alarm_Object = MibTableColumn
isd2PhysL1Alarm = _Isd2PhysL1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 3, 1, 1, 3),
    _Isd2PhysL1Alarm_Type()
)
isd2PhysL1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2PhysL1Alarm.setStatus("mandatory")
_Isd2CallCtrl_ObjectIdentity = ObjectIdentity
isd2CallCtrl = _Isd2CallCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 48, 4)
)
_Isd2CallCtrlTable_Object = MibTable
isd2CallCtrlTable = _Isd2CallCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1)
)
if mibBuilder.loadTexts:
    isd2CallCtrlTable.setStatus("mandatory")
_Isd2CallCtrlEntry_Object = MibTableRow
isd2CallCtrlEntry = _Isd2CallCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1)
)
isd2CallCtrlEntry.setIndexNames(
    (0, "ISD2-MIB", "isd2CallCtrlSigchanIfIndex"),
)
if mibBuilder.loadTexts:
    isd2CallCtrlEntry.setStatus("mandatory")
_Isd2CallCtrlSigchanIfIndex_Type = Integer32
_Isd2CallCtrlSigchanIfIndex_Object = MibTableColumn
isd2CallCtrlSigchanIfIndex = _Isd2CallCtrlSigchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 1),
    _Isd2CallCtrlSigchanIfIndex_Type()
)
isd2CallCtrlSigchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlSigchanIfIndex.setStatus("mandatory")
_Isd2CallCtrlBchanIfIndex_Type = Integer32
_Isd2CallCtrlBchanIfIndex_Object = MibTableColumn
isd2CallCtrlBchanIfIndex = _Isd2CallCtrlBchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 2),
    _Isd2CallCtrlBchanIfIndex_Type()
)
isd2CallCtrlBchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlBchanIfIndex.setStatus("mandatory")


class _Isd2CallCtrlLocalNumber_Type(OctetString):
    """Custom type isd2CallCtrlLocalNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_Isd2CallCtrlLocalNumber_Type.__name__ = "OctetString"
_Isd2CallCtrlLocalNumber_Object = MibTableColumn
isd2CallCtrlLocalNumber = _Isd2CallCtrlLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 3),
    _Isd2CallCtrlLocalNumber_Type()
)
isd2CallCtrlLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlLocalNumber.setStatus("mandatory")


class _Isd2CallCtrlLocalSubaddr_Type(OctetString):
    """Custom type isd2CallCtrlLocalSubaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Isd2CallCtrlLocalSubaddr_Type.__name__ = "OctetString"
_Isd2CallCtrlLocalSubaddr_Object = MibTableColumn
isd2CallCtrlLocalSubaddr = _Isd2CallCtrlLocalSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 4),
    _Isd2CallCtrlLocalSubaddr_Type()
)
isd2CallCtrlLocalSubaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlLocalSubaddr.setStatus("mandatory")


class _Isd2CallCtrlRemoteNumber_Type(OctetString):
    """Custom type isd2CallCtrlRemoteNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_Isd2CallCtrlRemoteNumber_Type.__name__ = "OctetString"
_Isd2CallCtrlRemoteNumber_Object = MibTableColumn
isd2CallCtrlRemoteNumber = _Isd2CallCtrlRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 5),
    _Isd2CallCtrlRemoteNumber_Type()
)
isd2CallCtrlRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlRemoteNumber.setStatus("mandatory")


class _Isd2CallCtrlRemoteSubaddr_Type(OctetString):
    """Custom type isd2CallCtrlRemoteSubaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Isd2CallCtrlRemoteSubaddr_Type.__name__ = "OctetString"
_Isd2CallCtrlRemoteSubaddr_Object = MibTableColumn
isd2CallCtrlRemoteSubaddr = _Isd2CallCtrlRemoteSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 6),
    _Isd2CallCtrlRemoteSubaddr_Type()
)
isd2CallCtrlRemoteSubaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlRemoteSubaddr.setStatus("mandatory")


class _Isd2CallCtrlL3State_Type(Integer32):
    """Custom type isd2CallCtrlL3State based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47)
        )
    )
    namedValues = NamedValues(
        *(("asaiTr1State", 28),
          ("broadcastState", 47),
          ("callActive", 10),
          ("callDelivered", 4),
          ("callInit", 1),
          ("callPassive", 14),
          ("callPresent", 6),
          ("callReceived", 7),
          ("cancelRequest", 21),
          ("connectRequest", 8),
          ("deactivateRequested", 37),
          ("deactivated", 35),
          ("disconnectInd", 12),
          ("disconnectRequest", 11),
          ("establishWait", 27),
          ("idleState", 26),
          ("inCallProc", 9),
          ("ni1HoldActiveU10", 46),
          ("ni1HoldActiveU3", 44),
          ("ni1HoldActiveU4", 45),
          ("ni1HoldReqU10", 40),
          ("ni1HoldReqU3", 38),
          ("ni1HoldReqU4", 39),
          ("ni1RetrieveU10", 43),
          ("ni1RetrieveU3", 41),
          ("ni1RetrieveU4", 42),
          ("outCallProc", 3),
          ("overlapReceive", 25),
          ("overlapSending", 2),
          ("passiveAwaitingConf", 13),
          ("reactivateRequested", 36),
          ("registerRequest", 20),
          ("releaseRequest", 19),
          ("resumeRequest", 17),
          ("suspendRequest", 15),
          ("u10AwaitingDisc", 33),
          ("u10CallOnHold", 34),
          ("u10ConferenceRequest", 31),
          ("u10HoldRequest", 29),
          ("u10ReconnectRequest", 32),
          ("u10TransferRequest", 30),
          ("undef16", 16),
          ("undef18", 18),
          ("undef22", 22),
          ("undef23", 23),
          ("undef24", 24),
          ("undef5", 5))
    )


_Isd2CallCtrlL3State_Type.__name__ = "Integer32"
_Isd2CallCtrlL3State_Object = MibTableColumn
isd2CallCtrlL3State = _Isd2CallCtrlL3State_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 7),
    _Isd2CallCtrlL3State_Type()
)
isd2CallCtrlL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlL3State.setStatus("mandatory")
_Isd2CallCtrlCallRef_Type = Integer32
_Isd2CallCtrlCallRef_Object = MibTableColumn
isd2CallCtrlCallRef = _Isd2CallCtrlCallRef_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 8),
    _Isd2CallCtrlCallRef_Type()
)
isd2CallCtrlCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlCallRef.setStatus("mandatory")
_Isd2CallCtrlChannelNum_Type = Integer32
_Isd2CallCtrlChannelNum_Object = MibTableColumn
isd2CallCtrlChannelNum = _Isd2CallCtrlChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 9),
    _Isd2CallCtrlChannelNum_Type()
)
isd2CallCtrlChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlChannelNum.setStatus("mandatory")
_Isd2CallCtrlOutCallsConnected_Type = Counter32
_Isd2CallCtrlOutCallsConnected_Object = MibTableColumn
isd2CallCtrlOutCallsConnected = _Isd2CallCtrlOutCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 10),
    _Isd2CallCtrlOutCallsConnected_Type()
)
isd2CallCtrlOutCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlOutCallsConnected.setStatus("mandatory")
_Isd2CallCtrlOutCallsFailed_Type = Counter32
_Isd2CallCtrlOutCallsFailed_Object = MibTableColumn
isd2CallCtrlOutCallsFailed = _Isd2CallCtrlOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 11),
    _Isd2CallCtrlOutCallsFailed_Type()
)
isd2CallCtrlOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlOutCallsFailed.setStatus("mandatory")
_Isd2CallCtrlInCallsConnected_Type = Counter32
_Isd2CallCtrlInCallsConnected_Object = MibTableColumn
isd2CallCtrlInCallsConnected = _Isd2CallCtrlInCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 12),
    _Isd2CallCtrlInCallsConnected_Type()
)
isd2CallCtrlInCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlInCallsConnected.setStatus("mandatory")
_Isd2CallCtrlInCallsRefused_Type = Counter32
_Isd2CallCtrlInCallsRefused_Object = MibTableColumn
isd2CallCtrlInCallsRefused = _Isd2CallCtrlInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 13),
    _Isd2CallCtrlInCallsRefused_Type()
)
isd2CallCtrlInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlInCallsRefused.setStatus("mandatory")
_Isd2CallCtrlCallCollisions_Type = Counter32
_Isd2CallCtrlCallCollisions_Object = MibTableColumn
isd2CallCtrlCallCollisions = _Isd2CallCtrlCallCollisions_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 14),
    _Isd2CallCtrlCallCollisions_Type()
)
isd2CallCtrlCallCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlCallCollisions.setStatus("mandatory")
_Isd2CallCtrlCauseCode_Type = Integer32
_Isd2CallCtrlCauseCode_Object = MibTableColumn
isd2CallCtrlCauseCode = _Isd2CallCtrlCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 15),
    _Isd2CallCtrlCauseCode_Type()
)
isd2CallCtrlCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlCauseCode.setStatus("mandatory")
_Isd2CallCtrlLocationCode_Type = Integer32
_Isd2CallCtrlLocationCode_Object = MibTableColumn
isd2CallCtrlLocationCode = _Isd2CallCtrlLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 16),
    _Isd2CallCtrlLocationCode_Type()
)
isd2CallCtrlLocationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlLocationCode.setStatus("mandatory")


class _Isd2CallCtrlCauseText_Type(OctetString):
    """Custom type isd2CallCtrlCauseText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_Isd2CallCtrlCauseText_Type.__name__ = "OctetString"
_Isd2CallCtrlCauseText_Object = MibTableColumn
isd2CallCtrlCauseText = _Isd2CallCtrlCauseText_Object(
    (1, 3, 6, 1, 4, 1, 208, 48, 4, 1, 1, 17),
    _Isd2CallCtrlCauseText_Type()
)
isd2CallCtrlCauseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isd2CallCtrlCauseText.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISD2-MIB",
    **{"isd2": isd2,
       "isd2SigChan": isd2SigChan,
       "isd2SigChanTable": isd2SigChanTable,
       "isd2SigChanEntry": isd2SigChanEntry,
       "isd2SigChanIfIndex": isd2SigChanIfIndex,
       "isd2SigChanL2State": isd2SigChanL2State,
       "isd2SigChanCES": isd2SigChanCES,
       "isd2SigChanSAPI": isd2SigChanSAPI,
       "isd2SigChanCallCollisions": isd2SigChanCallCollisions,
       "isd2SigChanAddressCheckFails": isd2SigChanAddressCheckFails,
       "isd2Dchan": isd2Dchan,
       "isd2DchanTable": isd2DchanTable,
       "isd2DchanEntry": isd2DchanEntry,
       "isd2DchanIfIndex": isd2DchanIfIndex,
       "isd2DchanRxShort": isd2DchanRxShort,
       "isd2DchanRxLong": isd2DchanRxLong,
       "isd2DchanRxCRCerror": isd2DchanRxCRCerror,
       "isd2DchanRxResidual": isd2DchanRxResidual,
       "isd2DchanRxAborts": isd2DchanRxAborts,
       "isd2DchanRxOverrun": isd2DchanRxOverrun,
       "isd2DchanRxLostSync": isd2DchanRxLostSync,
       "isd2DchanRxBufferLack": isd2DchanRxBufferLack,
       "isd2DchanRxApplnotready": isd2DchanRxApplnotready,
       "isd2DchanRxUnknownProto": isd2DchanRxUnknownProto,
       "isd2DchanTxDiscardedProto": isd2DchanTxDiscardedProto,
       "isd2DchanTxDiscardedData": isd2DchanTxDiscardedData,
       "isd2DchanTxUnderrun": isd2DchanTxUnderrun,
       "isd2DchanTxCollision": isd2DchanTxCollision,
       "isd2Phys": isd2Phys,
       "isd2PhysTable": isd2PhysTable,
       "isd2PhysEntry": isd2PhysEntry,
       "isd2PhysIfIndex": isd2PhysIfIndex,
       "isd2PhysL1State": isd2PhysL1State,
       "isd2PhysL1Alarm": isd2PhysL1Alarm,
       "isd2CallCtrl": isd2CallCtrl,
       "isd2CallCtrlTable": isd2CallCtrlTable,
       "isd2CallCtrlEntry": isd2CallCtrlEntry,
       "isd2CallCtrlSigchanIfIndex": isd2CallCtrlSigchanIfIndex,
       "isd2CallCtrlBchanIfIndex": isd2CallCtrlBchanIfIndex,
       "isd2CallCtrlLocalNumber": isd2CallCtrlLocalNumber,
       "isd2CallCtrlLocalSubaddr": isd2CallCtrlLocalSubaddr,
       "isd2CallCtrlRemoteNumber": isd2CallCtrlRemoteNumber,
       "isd2CallCtrlRemoteSubaddr": isd2CallCtrlRemoteSubaddr,
       "isd2CallCtrlL3State": isd2CallCtrlL3State,
       "isd2CallCtrlCallRef": isd2CallCtrlCallRef,
       "isd2CallCtrlChannelNum": isd2CallCtrlChannelNum,
       "isd2CallCtrlOutCallsConnected": isd2CallCtrlOutCallsConnected,
       "isd2CallCtrlOutCallsFailed": isd2CallCtrlOutCallsFailed,
       "isd2CallCtrlInCallsConnected": isd2CallCtrlInCallsConnected,
       "isd2CallCtrlInCallsRefused": isd2CallCtrlInCallsRefused,
       "isd2CallCtrlCallCollisions": isd2CallCtrlCallCollisions,
       "isd2CallCtrlCauseCode": isd2CallCtrlCauseCode,
       "isd2CallCtrlLocationCode": isd2CallCtrlLocationCode,
       "isd2CallCtrlCauseText": isd2CallCtrlCauseText}
)
