# SNMP MIB module (INTEL-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:50 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 29)
)
_IsdnSigChan_ObjectIdentity = ObjectIdentity
isdnSigChan = _IsdnSigChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1)
)
_IsdnSigChanTable_Object = MibTable
isdnSigChanTable = _IsdnSigChanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1)
)
if mibBuilder.loadTexts:
    isdnSigChanTable.setStatus("mandatory")
_IsdnSigChanEntry_Object = MibTableRow
isdnSigChanEntry = _IsdnSigChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1)
)
isdnSigChanEntry.setIndexNames(
    (0, "INTEL-ISDN-MIB", "isdnSigChanIfIndex"),
)
if mibBuilder.loadTexts:
    isdnSigChanEntry.setStatus("mandatory")
_IsdnSigChanIfIndex_Type = Integer32
_IsdnSigChanIfIndex_Object = MibTableColumn
isdnSigChanIfIndex = _IsdnSigChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 1),
    _IsdnSigChanIfIndex_Type()
)
isdnSigChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanIfIndex.setStatus("mandatory")


class _IsdnSigChanL2State_Type(Integer32):
    """Custom type isdnSigChanL2State based on Integer32"""
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


_IsdnSigChanL2State_Type.__name__ = "Integer32"
_IsdnSigChanL2State_Object = MibTableColumn
isdnSigChanL2State = _IsdnSigChanL2State_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 2),
    _IsdnSigChanL2State_Type()
)
isdnSigChanL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanL2State.setStatus("mandatory")
_IsdnSigChanCES_Type = Counter32
_IsdnSigChanCES_Object = MibTableColumn
isdnSigChanCES = _IsdnSigChanCES_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 3),
    _IsdnSigChanCES_Type()
)
isdnSigChanCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanCES.setStatus("mandatory")
_IsdnSigChanSAPI_Type = Counter32
_IsdnSigChanSAPI_Object = MibTableColumn
isdnSigChanSAPI = _IsdnSigChanSAPI_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 4),
    _IsdnSigChanSAPI_Type()
)
isdnSigChanSAPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanSAPI.setStatus("mandatory")
_IsdnSigChanCallCollisions_Type = Counter32
_IsdnSigChanCallCollisions_Object = MibTableColumn
isdnSigChanCallCollisions = _IsdnSigChanCallCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 5),
    _IsdnSigChanCallCollisions_Type()
)
isdnSigChanCallCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanCallCollisions.setStatus("mandatory")
_IsdnSigChanAddressCheckFails_Type = Counter32
_IsdnSigChanAddressCheckFails_Object = MibTableColumn
isdnSigChanAddressCheckFails = _IsdnSigChanAddressCheckFails_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 1, 1, 1, 6),
    _IsdnSigChanAddressCheckFails_Type()
)
isdnSigChanAddressCheckFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnSigChanAddressCheckFails.setStatus("mandatory")
_IsdnDchan_ObjectIdentity = ObjectIdentity
isdnDchan = _IsdnDchan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2)
)
_IsdnDchanTable_Object = MibTable
isdnDchanTable = _IsdnDchanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1)
)
if mibBuilder.loadTexts:
    isdnDchanTable.setStatus("mandatory")
_IsdnDchanEntry_Object = MibTableRow
isdnDchanEntry = _IsdnDchanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1)
)
isdnDchanEntry.setIndexNames(
    (0, "INTEL-ISDN-MIB", "isdnDchanIfIndex"),
)
if mibBuilder.loadTexts:
    isdnDchanEntry.setStatus("mandatory")
_IsdnDchanIfIndex_Type = Integer32
_IsdnDchanIfIndex_Object = MibTableColumn
isdnDchanIfIndex = _IsdnDchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 1),
    _IsdnDchanIfIndex_Type()
)
isdnDchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanIfIndex.setStatus("mandatory")
_IsdnDchanRxShort_Type = Counter32
_IsdnDchanRxShort_Object = MibTableColumn
isdnDchanRxShort = _IsdnDchanRxShort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 2),
    _IsdnDchanRxShort_Type()
)
isdnDchanRxShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxShort.setStatus("mandatory")
_IsdnDchanRxLong_Type = Counter32
_IsdnDchanRxLong_Object = MibTableColumn
isdnDchanRxLong = _IsdnDchanRxLong_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 3),
    _IsdnDchanRxLong_Type()
)
isdnDchanRxLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxLong.setStatus("mandatory")
_IsdnDchanRxCRCerror_Type = Counter32
_IsdnDchanRxCRCerror_Object = MibTableColumn
isdnDchanRxCRCerror = _IsdnDchanRxCRCerror_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 4),
    _IsdnDchanRxCRCerror_Type()
)
isdnDchanRxCRCerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxCRCerror.setStatus("mandatory")
_IsdnDchanRxResidual_Type = Counter32
_IsdnDchanRxResidual_Object = MibTableColumn
isdnDchanRxResidual = _IsdnDchanRxResidual_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 5),
    _IsdnDchanRxResidual_Type()
)
isdnDchanRxResidual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxResidual.setStatus("mandatory")
_IsdnDchanRxAborts_Type = Counter32
_IsdnDchanRxAborts_Object = MibTableColumn
isdnDchanRxAborts = _IsdnDchanRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 6),
    _IsdnDchanRxAborts_Type()
)
isdnDchanRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxAborts.setStatus("mandatory")
_IsdnDchanRxOverrun_Type = Counter32
_IsdnDchanRxOverrun_Object = MibTableColumn
isdnDchanRxOverrun = _IsdnDchanRxOverrun_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 7),
    _IsdnDchanRxOverrun_Type()
)
isdnDchanRxOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxOverrun.setStatus("mandatory")
_IsdnDchanRxLostSync_Type = Counter32
_IsdnDchanRxLostSync_Object = MibTableColumn
isdnDchanRxLostSync = _IsdnDchanRxLostSync_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 8),
    _IsdnDchanRxLostSync_Type()
)
isdnDchanRxLostSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxLostSync.setStatus("mandatory")
_IsdnDchanRxBufferLack_Type = Counter32
_IsdnDchanRxBufferLack_Object = MibTableColumn
isdnDchanRxBufferLack = _IsdnDchanRxBufferLack_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 9),
    _IsdnDchanRxBufferLack_Type()
)
isdnDchanRxBufferLack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxBufferLack.setStatus("mandatory")
_IsdnDchanRxApplnotready_Type = Counter32
_IsdnDchanRxApplnotready_Object = MibTableColumn
isdnDchanRxApplnotready = _IsdnDchanRxApplnotready_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 10),
    _IsdnDchanRxApplnotready_Type()
)
isdnDchanRxApplnotready.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxApplnotready.setStatus("mandatory")
_IsdnDchanRxUnknownProto_Type = Counter32
_IsdnDchanRxUnknownProto_Object = MibTableColumn
isdnDchanRxUnknownProto = _IsdnDchanRxUnknownProto_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 11),
    _IsdnDchanRxUnknownProto_Type()
)
isdnDchanRxUnknownProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanRxUnknownProto.setStatus("mandatory")
_IsdnDchanTxDiscardedProto_Type = Counter32
_IsdnDchanTxDiscardedProto_Object = MibTableColumn
isdnDchanTxDiscardedProto = _IsdnDchanTxDiscardedProto_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 12),
    _IsdnDchanTxDiscardedProto_Type()
)
isdnDchanTxDiscardedProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanTxDiscardedProto.setStatus("mandatory")
_IsdnDchanTxDiscardedData_Type = Counter32
_IsdnDchanTxDiscardedData_Object = MibTableColumn
isdnDchanTxDiscardedData = _IsdnDchanTxDiscardedData_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 13),
    _IsdnDchanTxDiscardedData_Type()
)
isdnDchanTxDiscardedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanTxDiscardedData.setStatus("mandatory")
_IsdnDchanTxUnderrun_Type = Counter32
_IsdnDchanTxUnderrun_Object = MibTableColumn
isdnDchanTxUnderrun = _IsdnDchanTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 14),
    _IsdnDchanTxUnderrun_Type()
)
isdnDchanTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanTxUnderrun.setStatus("mandatory")
_IsdnDchanTxCollision_Type = Counter32
_IsdnDchanTxCollision_Object = MibTableColumn
isdnDchanTxCollision = _IsdnDchanTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 2, 1, 1, 15),
    _IsdnDchanTxCollision_Type()
)
isdnDchanTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnDchanTxCollision.setStatus("mandatory")
_IsdnPhys_ObjectIdentity = ObjectIdentity
isdnPhys = _IsdnPhys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3)
)
_IsdnPhysTable_Object = MibTable
isdnPhysTable = _IsdnPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3, 1)
)
if mibBuilder.loadTexts:
    isdnPhysTable.setStatus("mandatory")
_IsdnPhysEntry_Object = MibTableRow
isdnPhysEntry = _IsdnPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3, 1, 1)
)
isdnPhysEntry.setIndexNames(
    (0, "INTEL-ISDN-MIB", "isdnPhysIfIndex"),
)
if mibBuilder.loadTexts:
    isdnPhysEntry.setStatus("mandatory")
_IsdnPhysIfIndex_Type = Integer32
_IsdnPhysIfIndex_Object = MibTableColumn
isdnPhysIfIndex = _IsdnPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3, 1, 1, 1),
    _IsdnPhysIfIndex_Type()
)
isdnPhysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPhysIfIndex.setStatus("mandatory")


class _IsdnPhysL1State_Type(Integer32):
    """Custom type isdnPhysL1State based on Integer32"""
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
              106,
              107,
              108)
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
          ("incomingCall", 107),
          ("lossOfPower", 100),
          ("lostFraming", 8),
          ("operational", 101),
          ("powerOn", 106),
          ("sensing", 2),
          ("synchronized", 6),
          ("testing", 108))
    )


_IsdnPhysL1State_Type.__name__ = "Integer32"
_IsdnPhysL1State_Object = MibTableColumn
isdnPhysL1State = _IsdnPhysL1State_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3, 1, 1, 2),
    _IsdnPhysL1State_Type()
)
isdnPhysL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPhysL1State.setStatus("mandatory")


class _IsdnPhysL1Alarm_Type(Integer32):
    """Custom type isdnPhysL1Alarm based on Integer32"""
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


_IsdnPhysL1Alarm_Type.__name__ = "Integer32"
_IsdnPhysL1Alarm_Object = MibTableColumn
isdnPhysL1Alarm = _IsdnPhysL1Alarm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 3, 1, 1, 3),
    _IsdnPhysL1Alarm_Type()
)
isdnPhysL1Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnPhysL1Alarm.setStatus("mandatory")
_IsdnCallCtrl_ObjectIdentity = ObjectIdentity
isdnCallCtrl = _IsdnCallCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4)
)
_IsdnCallCtrlTable_Object = MibTable
isdnCallCtrlTable = _IsdnCallCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1)
)
if mibBuilder.loadTexts:
    isdnCallCtrlTable.setStatus("mandatory")
_IsdnCallCtrlEntry_Object = MibTableRow
isdnCallCtrlEntry = _IsdnCallCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1)
)
isdnCallCtrlEntry.setIndexNames(
    (0, "INTEL-ISDN-MIB", "isdnCallCtrlSigchanIfIndex"),
)
if mibBuilder.loadTexts:
    isdnCallCtrlEntry.setStatus("mandatory")
_IsdnCallCtrlSigchanIfIndex_Type = Integer32
_IsdnCallCtrlSigchanIfIndex_Object = MibTableColumn
isdnCallCtrlSigchanIfIndex = _IsdnCallCtrlSigchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 1),
    _IsdnCallCtrlSigchanIfIndex_Type()
)
isdnCallCtrlSigchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlSigchanIfIndex.setStatus("mandatory")
_IsdnCallCtrlBchanIfIndex_Type = Integer32
_IsdnCallCtrlBchanIfIndex_Object = MibTableColumn
isdnCallCtrlBchanIfIndex = _IsdnCallCtrlBchanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 2),
    _IsdnCallCtrlBchanIfIndex_Type()
)
isdnCallCtrlBchanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlBchanIfIndex.setStatus("mandatory")


class _IsdnCallCtrlLocalNumber_Type(OctetString):
    """Custom type isdnCallCtrlLocalNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_IsdnCallCtrlLocalNumber_Type.__name__ = "OctetString"
_IsdnCallCtrlLocalNumber_Object = MibTableColumn
isdnCallCtrlLocalNumber = _IsdnCallCtrlLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 3),
    _IsdnCallCtrlLocalNumber_Type()
)
isdnCallCtrlLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlLocalNumber.setStatus("mandatory")


class _IsdnCallCtrlLocalSubaddr_Type(OctetString):
    """Custom type isdnCallCtrlLocalSubaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_IsdnCallCtrlLocalSubaddr_Type.__name__ = "OctetString"
_IsdnCallCtrlLocalSubaddr_Object = MibTableColumn
isdnCallCtrlLocalSubaddr = _IsdnCallCtrlLocalSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 4),
    _IsdnCallCtrlLocalSubaddr_Type()
)
isdnCallCtrlLocalSubaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlLocalSubaddr.setStatus("mandatory")


class _IsdnCallCtrlRemoteNumber_Type(OctetString):
    """Custom type isdnCallCtrlRemoteNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_IsdnCallCtrlRemoteNumber_Type.__name__ = "OctetString"
_IsdnCallCtrlRemoteNumber_Object = MibTableColumn
isdnCallCtrlRemoteNumber = _IsdnCallCtrlRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 5),
    _IsdnCallCtrlRemoteNumber_Type()
)
isdnCallCtrlRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlRemoteNumber.setStatus("mandatory")


class _IsdnCallCtrlRemoteSubaddr_Type(OctetString):
    """Custom type isdnCallCtrlRemoteSubaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_IsdnCallCtrlRemoteSubaddr_Type.__name__ = "OctetString"
_IsdnCallCtrlRemoteSubaddr_Object = MibTableColumn
isdnCallCtrlRemoteSubaddr = _IsdnCallCtrlRemoteSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 6),
    _IsdnCallCtrlRemoteSubaddr_Type()
)
isdnCallCtrlRemoteSubaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlRemoteSubaddr.setStatus("mandatory")


class _IsdnCallCtrlL3State_Type(Integer32):
    """Custom type isdnCallCtrlL3State based on Integer32"""
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


_IsdnCallCtrlL3State_Type.__name__ = "Integer32"
_IsdnCallCtrlL3State_Object = MibTableColumn
isdnCallCtrlL3State = _IsdnCallCtrlL3State_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 7),
    _IsdnCallCtrlL3State_Type()
)
isdnCallCtrlL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlL3State.setStatus("mandatory")
_IsdnCallCtrlCallRef_Type = Integer32
_IsdnCallCtrlCallRef_Object = MibTableColumn
isdnCallCtrlCallRef = _IsdnCallCtrlCallRef_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 8),
    _IsdnCallCtrlCallRef_Type()
)
isdnCallCtrlCallRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlCallRef.setStatus("mandatory")
_IsdnCallCtrlChannelNum_Type = Integer32
_IsdnCallCtrlChannelNum_Object = MibTableColumn
isdnCallCtrlChannelNum = _IsdnCallCtrlChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 9),
    _IsdnCallCtrlChannelNum_Type()
)
isdnCallCtrlChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlChannelNum.setStatus("mandatory")
_IsdnCallCtrlOutCallsConnected_Type = Counter32
_IsdnCallCtrlOutCallsConnected_Object = MibTableColumn
isdnCallCtrlOutCallsConnected = _IsdnCallCtrlOutCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 10),
    _IsdnCallCtrlOutCallsConnected_Type()
)
isdnCallCtrlOutCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlOutCallsConnected.setStatus("mandatory")
_IsdnCallCtrlOutCallsFailed_Type = Counter32
_IsdnCallCtrlOutCallsFailed_Object = MibTableColumn
isdnCallCtrlOutCallsFailed = _IsdnCallCtrlOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 11),
    _IsdnCallCtrlOutCallsFailed_Type()
)
isdnCallCtrlOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlOutCallsFailed.setStatus("mandatory")
_IsdnCallCtrlInCallsConnected_Type = Counter32
_IsdnCallCtrlInCallsConnected_Object = MibTableColumn
isdnCallCtrlInCallsConnected = _IsdnCallCtrlInCallsConnected_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 12),
    _IsdnCallCtrlInCallsConnected_Type()
)
isdnCallCtrlInCallsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlInCallsConnected.setStatus("mandatory")
_IsdnCallCtrlInCallsRefused_Type = Counter32
_IsdnCallCtrlInCallsRefused_Object = MibTableColumn
isdnCallCtrlInCallsRefused = _IsdnCallCtrlInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 13),
    _IsdnCallCtrlInCallsRefused_Type()
)
isdnCallCtrlInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlInCallsRefused.setStatus("mandatory")
_IsdnCallCtrlCallCollisions_Type = Counter32
_IsdnCallCtrlCallCollisions_Object = MibTableColumn
isdnCallCtrlCallCollisions = _IsdnCallCtrlCallCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 14),
    _IsdnCallCtrlCallCollisions_Type()
)
isdnCallCtrlCallCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlCallCollisions.setStatus("mandatory")
_IsdnCallCtrlCauseCode_Type = Integer32
_IsdnCallCtrlCauseCode_Object = MibTableColumn
isdnCallCtrlCauseCode = _IsdnCallCtrlCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 15),
    _IsdnCallCtrlCauseCode_Type()
)
isdnCallCtrlCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlCauseCode.setStatus("mandatory")
_IsdnCallCtrlLocationCode_Type = Integer32
_IsdnCallCtrlLocationCode_Object = MibTableColumn
isdnCallCtrlLocationCode = _IsdnCallCtrlLocationCode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 16),
    _IsdnCallCtrlLocationCode_Type()
)
isdnCallCtrlLocationCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlLocationCode.setStatus("mandatory")


class _IsdnCallCtrlCauseText_Type(OctetString):
    """Custom type isdnCallCtrlCauseText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_IsdnCallCtrlCauseText_Type.__name__ = "OctetString"
_IsdnCallCtrlCauseText_Object = MibTableColumn
isdnCallCtrlCauseText = _IsdnCallCtrlCauseText_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 29, 4, 1, 1, 17),
    _IsdnCallCtrlCauseText_Type()
)
isdnCallCtrlCauseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnCallCtrlCauseText.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-ISDN-MIB",
    **{"isdn": isdn,
       "isdnSigChan": isdnSigChan,
       "isdnSigChanTable": isdnSigChanTable,
       "isdnSigChanEntry": isdnSigChanEntry,
       "isdnSigChanIfIndex": isdnSigChanIfIndex,
       "isdnSigChanL2State": isdnSigChanL2State,
       "isdnSigChanCES": isdnSigChanCES,
       "isdnSigChanSAPI": isdnSigChanSAPI,
       "isdnSigChanCallCollisions": isdnSigChanCallCollisions,
       "isdnSigChanAddressCheckFails": isdnSigChanAddressCheckFails,
       "isdnDchan": isdnDchan,
       "isdnDchanTable": isdnDchanTable,
       "isdnDchanEntry": isdnDchanEntry,
       "isdnDchanIfIndex": isdnDchanIfIndex,
       "isdnDchanRxShort": isdnDchanRxShort,
       "isdnDchanRxLong": isdnDchanRxLong,
       "isdnDchanRxCRCerror": isdnDchanRxCRCerror,
       "isdnDchanRxResidual": isdnDchanRxResidual,
       "isdnDchanRxAborts": isdnDchanRxAborts,
       "isdnDchanRxOverrun": isdnDchanRxOverrun,
       "isdnDchanRxLostSync": isdnDchanRxLostSync,
       "isdnDchanRxBufferLack": isdnDchanRxBufferLack,
       "isdnDchanRxApplnotready": isdnDchanRxApplnotready,
       "isdnDchanRxUnknownProto": isdnDchanRxUnknownProto,
       "isdnDchanTxDiscardedProto": isdnDchanTxDiscardedProto,
       "isdnDchanTxDiscardedData": isdnDchanTxDiscardedData,
       "isdnDchanTxUnderrun": isdnDchanTxUnderrun,
       "isdnDchanTxCollision": isdnDchanTxCollision,
       "isdnPhys": isdnPhys,
       "isdnPhysTable": isdnPhysTable,
       "isdnPhysEntry": isdnPhysEntry,
       "isdnPhysIfIndex": isdnPhysIfIndex,
       "isdnPhysL1State": isdnPhysL1State,
       "isdnPhysL1Alarm": isdnPhysL1Alarm,
       "isdnCallCtrl": isdnCallCtrl,
       "isdnCallCtrlTable": isdnCallCtrlTable,
       "isdnCallCtrlEntry": isdnCallCtrlEntry,
       "isdnCallCtrlSigchanIfIndex": isdnCallCtrlSigchanIfIndex,
       "isdnCallCtrlBchanIfIndex": isdnCallCtrlBchanIfIndex,
       "isdnCallCtrlLocalNumber": isdnCallCtrlLocalNumber,
       "isdnCallCtrlLocalSubaddr": isdnCallCtrlLocalSubaddr,
       "isdnCallCtrlRemoteNumber": isdnCallCtrlRemoteNumber,
       "isdnCallCtrlRemoteSubaddr": isdnCallCtrlRemoteSubaddr,
       "isdnCallCtrlL3State": isdnCallCtrlL3State,
       "isdnCallCtrlCallRef": isdnCallCtrlCallRef,
       "isdnCallCtrlChannelNum": isdnCallCtrlChannelNum,
       "isdnCallCtrlOutCallsConnected": isdnCallCtrlOutCallsConnected,
       "isdnCallCtrlOutCallsFailed": isdnCallCtrlOutCallsFailed,
       "isdnCallCtrlInCallsConnected": isdnCallCtrlInCallsConnected,
       "isdnCallCtrlInCallsRefused": isdnCallCtrlInCallsRefused,
       "isdnCallCtrlCallCollisions": isdnCallCtrlCallCollisions,
       "isdnCallCtrlCauseCode": isdnCallCtrlCauseCode,
       "isdnCallCtrlLocationCode": isdnCallCtrlLocationCode,
       "isdnCallCtrlCauseText": isdnCallCtrlCauseText}
)
