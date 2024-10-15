# SNMP MIB module (SCA-MPLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-MPLINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:54 2024
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



class OffOn(Integer32):
    """Custom type OffOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mplk_ObjectIdentity = ObjectIdentity
mplk = _Mplk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 24)
)
_Service_ObjectIdentity = ObjectIdentity
service = _Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 24, 1)
)
_ServiceTable_Object = MibTable
serviceTable = _ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1)
)
if mibBuilder.loadTexts:
    serviceTable.setStatus("mandatory")
_ServiceEntry_Object = MibTableRow
serviceEntry = _ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1)
)
serviceEntry.setIndexNames(
    (0, "SCA-MPLINK-MIB", "serviceNumber1"),
)
if mibBuilder.loadTexts:
    serviceEntry.setStatus("mandatory")
_ServiceNumber1_Type = Integer32
_ServiceNumber1_Object = MibTableColumn
serviceNumber1 = _ServiceNumber1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 1),
    _ServiceNumber1_Type()
)
serviceNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceNumber1.setStatus("mandatory")


class _ServiceName_Type(DisplayString):
    """Custom type serviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ServiceName_Type.__name__ = "DisplayString"
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 2),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("mandatory")


class _ServiceType_Type(Integer32):
    """Custom type serviceType based on Integer32"""
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
        *(("aod", 2),
          ("internal", 5),
          ("lan", 6),
          ("pod", 3),
          ("pool", 4),
          ("static", 1))
    )


_ServiceType_Type.__name__ = "Integer32"
_ServiceType_Object = MibTableColumn
serviceType = _ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 3),
    _ServiceType_Type()
)
serviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceType.setStatus("mandatory")
_Slot_Type = Integer32
_Slot_Object = MibTableColumn
slot = _Slot_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 4),
    _Slot_Type()
)
slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slot.setStatus("mandatory")
_Plug_Type = Integer32
_Plug_Object = MibTableColumn
plug = _Plug_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 5),
    _Plug_Type()
)
plug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plug.setStatus("mandatory")


class _ServiceState_Type(Integer32):
    """Custom type serviceState based on Integer32"""
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
        *(("down", 3),
          ("noProvider", 2),
          ("outOfService", 1),
          ("timeCut", 4),
          ("up", 5))
    )


_ServiceState_Type.__name__ = "Integer32"
_ServiceState_Object = MibTableColumn
serviceState = _ServiceState_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 6),
    _ServiceState_Type()
)
serviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceState.setStatus("mandatory")
_BytesSent_Type = Counter32
_BytesSent_Object = MibTableColumn
bytesSent = _BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 7),
    _BytesSent_Type()
)
bytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesSent.setStatus("mandatory")
_BytesReceived_Type = Counter32
_BytesReceived_Object = MibTableColumn
bytesReceived = _BytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 8),
    _BytesReceived_Type()
)
bytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesReceived.setStatus("mandatory")
_PacketsSent_Type = Counter32
_PacketsSent_Object = MibTableColumn
packetsSent = _PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 9),
    _PacketsSent_Type()
)
packetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsSent.setStatus("mandatory")
_PacketsReceived_Type = Counter32
_PacketsReceived_Object = MibTableColumn
packetsReceived = _PacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 10),
    _PacketsReceived_Type()
)
packetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsReceived.setStatus("mandatory")
_MaxPacketSize_Type = Integer32
_MaxPacketSize_Object = MibTableColumn
maxPacketSize = _MaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 1, 1, 1, 11),
    _MaxPacketSize_Type()
)
maxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPacketSize.setStatus("mandatory")
_LanSpecific_ObjectIdentity = ObjectIdentity
lanSpecific = _LanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 24, 2)
)
_LanTable_Object = MibTable
lanTable = _LanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1)
)
if mibBuilder.loadTexts:
    lanTable.setStatus("mandatory")
_LanEntry_Object = MibTableRow
lanEntry = _LanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1)
)
lanEntry.setIndexNames(
    (0, "SCA-MPLINK-MIB", "serviceNumber2"),
)
if mibBuilder.loadTexts:
    lanEntry.setStatus("mandatory")
_ServiceNumber2_Type = Integer32
_ServiceNumber2_Object = MibTableColumn
serviceNumber2 = _ServiceNumber2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 1),
    _ServiceNumber2_Type()
)
serviceNumber2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceNumber2.setStatus("mandatory")


class _OwnSNPAAddress_Type(OctetString):
    """Custom type ownSNPAAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_OwnSNPAAddress_Type.__name__ = "OctetString"
_OwnSNPAAddress_Object = MibTableColumn
ownSNPAAddress = _OwnSNPAAddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 2),
    _OwnSNPAAddress_Type()
)
ownSNPAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ownSNPAAddress.setStatus("mandatory")
_ScaNetSubnet_Type = Integer32
_ScaNetSubnet_Object = MibTableColumn
scaNetSubnet = _ScaNetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 3),
    _ScaNetSubnet_Type()
)
scaNetSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scaNetSubnet.setStatus("mandatory")


class _IncomingAccessMask1_Type(OctetString):
    """Custom type incomingAccessMask1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IncomingAccessMask1_Type.__name__ = "OctetString"
_IncomingAccessMask1_Object = MibTableColumn
incomingAccessMask1 = _IncomingAccessMask1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 4),
    _IncomingAccessMask1_Type()
)
incomingAccessMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incomingAccessMask1.setStatus("mandatory")


class _OutgoingAccessMask1_Type(OctetString):
    """Custom type outgoingAccessMask1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OutgoingAccessMask1_Type.__name__ = "OctetString"
_OutgoingAccessMask1_Object = MibTableColumn
outgoingAccessMask1 = _OutgoingAccessMask1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 2, 1, 1, 5),
    _OutgoingAccessMask1_Type()
)
outgoingAccessMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outgoingAccessMask1.setStatus("mandatory")
_WanSpecific_ObjectIdentity = ObjectIdentity
wanSpecific = _WanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 24, 3)
)
_WanTable_Object = MibTable
wanTable = _WanTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1)
)
if mibBuilder.loadTexts:
    wanTable.setStatus("mandatory")
_WanEntry_Object = MibTableRow
wanEntry = _WanEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1)
)
wanEntry.setIndexNames(
    (0, "SCA-MPLINK-MIB", "serviceNumber3"),
)
if mibBuilder.loadTexts:
    wanEntry.setStatus("mandatory")
_ServiceNumber3_Type = Integer32
_ServiceNumber3_Object = MibTableColumn
serviceNumber3 = _ServiceNumber3_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 1),
    _ServiceNumber3_Type()
)
serviceNumber3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceNumber3.setStatus("mandatory")
_Provider_Type = Integer32
_Provider_Object = MibTableColumn
provider = _Provider_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 2),
    _Provider_Type()
)
provider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    provider.setStatus("mandatory")
_QueueActualValue_Type = Integer32
_QueueActualValue_Object = MibTableColumn
queueActualValue = _QueueActualValue_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 3),
    _QueueActualValue_Type()
)
queueActualValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueActualValue.setStatus("mandatory")
_QueueHighWaterTideMark_Type = Integer32
_QueueHighWaterTideMark_Object = MibTableColumn
queueHighWaterTideMark = _QueueHighWaterTideMark_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 4),
    _QueueHighWaterTideMark_Type()
)
queueHighWaterTideMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueHighWaterTideMark.setStatus("mandatory")
_QueueRejectThreshold1_Type = Integer32
_QueueRejectThreshold1_Object = MibTableColumn
queueRejectThreshold1 = _QueueRejectThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 5),
    _QueueRejectThreshold1_Type()
)
queueRejectThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueRejectThreshold1.setStatus("mandatory")
_DataCompressionSwitch1_Type = OffOn
_DataCompressionSwitch1_Object = MibTableColumn
dataCompressionSwitch1 = _DataCompressionSwitch1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 6),
    _DataCompressionSwitch1_Type()
)
dataCompressionSwitch1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataCompressionSwitch1.setStatus("mandatory")
_DataCompressionState_Type = OffOn
_DataCompressionState_Object = MibTableColumn
dataCompressionState = _DataCompressionState_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 7),
    _DataCompressionState_Type()
)
dataCompressionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCompressionState.setStatus("mandatory")
_AcceptIncomingCalls1_Type = OffOn
_AcceptIncomingCalls1_Object = MibTableColumn
acceptIncomingCalls1 = _AcceptIncomingCalls1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 8),
    _AcceptIncomingCalls1_Type()
)
acceptIncomingCalls1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptIncomingCalls1.setStatus("mandatory")
_PermitOutgoingCalls1_Type = OffOn
_PermitOutgoingCalls1_Object = MibTableColumn
permitOutgoingCalls1 = _PermitOutgoingCalls1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 9),
    _PermitOutgoingCalls1_Type()
)
permitOutgoingCalls1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permitOutgoingCalls1.setStatus("mandatory")
_AcceptReverseCharge1_Type = OffOn
_AcceptReverseCharge1_Object = MibTableColumn
acceptReverseCharge1 = _AcceptReverseCharge1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 10),
    _AcceptReverseCharge1_Type()
)
acceptReverseCharge1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptReverseCharge1.setStatus("mandatory")
_ProposeReverseCharge1_Type = OffOn
_ProposeReverseCharge1_Object = MibTableColumn
proposeReverseCharge1 = _ProposeReverseCharge1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 11),
    _ProposeReverseCharge1_Type()
)
proposeReverseCharge1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proposeReverseCharge1.setStatus("mandatory")
_PermitTimeCut1_Type = OffOn
_PermitTimeCut1_Object = MibTableColumn
permitTimeCut1 = _PermitTimeCut1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 12),
    _PermitTimeCut1_Type()
)
permitTimeCut1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permitTimeCut1.setStatus("mandatory")
_BackupOnly_Type = OffOn
_BackupOnly_Object = MibTableColumn
backupOnly = _BackupOnly_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 13),
    _BackupOnly_Type()
)
backupOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupOnly.setStatus("mandatory")


class _ActualCallState_Type(Integer32):
    """Custom type actualCallState based on Integer32"""
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
        *(("connecting", 6),
          ("disconnecting", 5),
          ("down", 4),
          ("error", 3),
          ("noProvider", 2),
          ("outOfService", 1),
          ("up", 7))
    )


_ActualCallState_Type.__name__ = "Integer32"
_ActualCallState_Object = MibTableColumn
actualCallState = _ActualCallState_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 14),
    _ActualCallState_Type()
)
actualCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualCallState.setStatus("mandatory")


class _ActualCallDirection_Type(Integer32):
    """Custom type actualCallDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inc", 1),
          ("outg", 2))
    )


_ActualCallDirection_Type.__name__ = "Integer32"
_ActualCallDirection_Object = MibTableColumn
actualCallDirection = _ActualCallDirection_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 15),
    _ActualCallDirection_Type()
)
actualCallDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualCallDirection.setStatus("mandatory")
_ActualCallDuration_Type = Integer32
_ActualCallDuration_Object = MibTableColumn
actualCallDuration = _ActualCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 16),
    _ActualCallDuration_Type()
)
actualCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualCallDuration.setStatus("mandatory")
_MinCallDuration1_Type = Integer32
_MinCallDuration1_Object = MibTableColumn
minCallDuration1 = _MinCallDuration1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 17),
    _MinCallDuration1_Type()
)
minCallDuration1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minCallDuration1.setStatus("mandatory")
_IdleTime1_Type = Integer32
_IdleTime1_Object = MibTableColumn
idleTime1 = _IdleTime1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 18),
    _IdleTime1_Type()
)
idleTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleTime1.setStatus("mandatory")
_ActualTimer_Type = Integer32
_ActualTimer_Object = MibTableColumn
actualTimer = _ActualTimer_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 19),
    _ActualTimer_Type()
)
actualTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualTimer.setStatus("mandatory")
_ReserveTime1_Type = Integer32
_ReserveTime1_Object = MibTableColumn
reserveTime1 = _ReserveTime1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 20),
    _ReserveTime1_Type()
)
reserveTime1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reserveTime1.setStatus("mandatory")
_OwnUserDataAddress1_Type = Integer32
_OwnUserDataAddress1_Object = MibTableColumn
ownUserDataAddress1 = _OwnUserDataAddress1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 21),
    _OwnUserDataAddress1_Type()
)
ownUserDataAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ownUserDataAddress1.setStatus("mandatory")


class _RemoteSNPAaddress_Type(OctetString):
    """Custom type remoteSNPAaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_RemoteSNPAaddress_Type.__name__ = "OctetString"
_RemoteSNPAaddress_Object = MibTableColumn
remoteSNPAaddress = _RemoteSNPAaddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 22),
    _RemoteSNPAaddress_Type()
)
remoteSNPAaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteSNPAaddress.setStatus("mandatory")
_RemoteUserDataAddress_Type = Integer32
_RemoteUserDataAddress_Object = MibTableColumn
remoteUserDataAddress = _RemoteUserDataAddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 23),
    _RemoteUserDataAddress_Type()
)
remoteUserDataAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteUserDataAddress.setStatus("mandatory")
_CallsPlaced1_Type = Counter32
_CallsPlaced1_Object = MibTableColumn
callsPlaced1 = _CallsPlaced1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 24),
    _CallsPlaced1_Type()
)
callsPlaced1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callsPlaced1.setStatus("mandatory")
_CallsFailed1_Type = Counter32
_CallsFailed1_Object = MibTableColumn
callsFailed1 = _CallsFailed1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 25),
    _CallsFailed1_Type()
)
callsFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callsFailed1.setStatus("mandatory")
_ActualErrorRetries_Type = Counter32
_ActualErrorRetries_Object = MibTableColumn
actualErrorRetries = _ActualErrorRetries_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 26),
    _ActualErrorRetries_Type()
)
actualErrorRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualErrorRetries.setStatus("mandatory")
_MaxErrorRetries1_Type = Integer32
_MaxErrorRetries1_Object = MibTableColumn
maxErrorRetries1 = _MaxErrorRetries1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 27),
    _MaxErrorRetries1_Type()
)
maxErrorRetries1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxErrorRetries1.setStatus("mandatory")
_ErrorRetryInterval1_Type = Integer32
_ErrorRetryInterval1_Object = MibTableColumn
errorRetryInterval1 = _ErrorRetryInterval1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 28),
    _ErrorRetryInterval1_Type()
)
errorRetryInterval1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorRetryInterval1.setStatus("mandatory")
_MaxCallSetupTime1_Type = Integer32
_MaxCallSetupTime1_Object = MibTableColumn
maxCallSetupTime1 = _MaxCallSetupTime1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 29),
    _MaxCallSetupTime1_Type()
)
maxCallSetupTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxCallSetupTime1.setStatus("mandatory")
_MostRecentFailure1_Type = TimeTicks
_MostRecentFailure1_Object = MibTableColumn
mostRecentFailure1 = _MostRecentFailure1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 30),
    _MostRecentFailure1_Type()
)
mostRecentFailure1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mostRecentFailure1.setStatus("mandatory")
_BackupForLink_Type = Integer32
_BackupForLink_Object = MibTableColumn
backupForLink = _BackupForLink_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 31),
    _BackupForLink_Type()
)
backupForLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupForLink.setStatus("mandatory")
_PoolIndex_Type = Integer32
_PoolIndex_Object = MibTableColumn
poolIndex = _PoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 32),
    _PoolIndex_Type()
)
poolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poolIndex.setStatus("mandatory")


class _IncomingAccessMask2_Type(OctetString):
    """Custom type incomingAccessMask2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IncomingAccessMask2_Type.__name__ = "OctetString"
_IncomingAccessMask2_Object = MibTableColumn
incomingAccessMask2 = _IncomingAccessMask2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 33),
    _IncomingAccessMask2_Type()
)
incomingAccessMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incomingAccessMask2.setStatus("mandatory")


class _OutgoingAccessMask2_Type(OctetString):
    """Custom type outgoingAccessMask2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OutgoingAccessMask2_Type.__name__ = "OctetString"
_OutgoingAccessMask2_Object = MibTableColumn
outgoingAccessMask2 = _OutgoingAccessMask2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 34),
    _OutgoingAccessMask2_Type()
)
outgoingAccessMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outgoingAccessMask2.setStatus("mandatory")


class _TimecutAccessMask1_Type(OctetString):
    """Custom type timecutAccessMask1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TimecutAccessMask1_Type.__name__ = "OctetString"
_TimecutAccessMask1_Object = MibTableColumn
timecutAccessMask1 = _TimecutAccessMask1_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 1, 1, 35),
    _TimecutAccessMask1_Type()
)
timecutAccessMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timecutAccessMask1.setStatus("mandatory")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("mandatory")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1)
)
poolEntry.setIndexNames(
    (0, "SCA-MPLINK-MIB", "serviceNumber4"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("mandatory")
_ServiceNumber4_Type = Integer32
_ServiceNumber4_Object = MibTableColumn
serviceNumber4 = _ServiceNumber4_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 1),
    _ServiceNumber4_Type()
)
serviceNumber4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceNumber4.setStatus("mandatory")


class _PoolName_Type(DisplayString):
    """Custom type poolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_PoolName_Type.__name__ = "DisplayString"
_PoolName_Object = MibTableColumn
poolName = _PoolName_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 2),
    _PoolName_Type()
)
poolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolName.setStatus("mandatory")
_QueueRejectThreshold2_Type = Integer32
_QueueRejectThreshold2_Object = MibTableColumn
queueRejectThreshold2 = _QueueRejectThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 3),
    _QueueRejectThreshold2_Type()
)
queueRejectThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueRejectThreshold2.setStatus("mandatory")
_DataCompressionSwitch2_Type = OffOn
_DataCompressionSwitch2_Object = MibTableColumn
dataCompressionSwitch2 = _DataCompressionSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 4),
    _DataCompressionSwitch2_Type()
)
dataCompressionSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataCompressionSwitch2.setStatus("mandatory")
_AcceptIncomingCalls2_Type = OffOn
_AcceptIncomingCalls2_Object = MibTableColumn
acceptIncomingCalls2 = _AcceptIncomingCalls2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 5),
    _AcceptIncomingCalls2_Type()
)
acceptIncomingCalls2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptIncomingCalls2.setStatus("mandatory")
_PermitOutgoingCalls2_Type = OffOn
_PermitOutgoingCalls2_Object = MibTableColumn
permitOutgoingCalls2 = _PermitOutgoingCalls2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 6),
    _PermitOutgoingCalls2_Type()
)
permitOutgoingCalls2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permitOutgoingCalls2.setStatus("mandatory")
_AcceptReverseCharge2_Type = OffOn
_AcceptReverseCharge2_Object = MibTableColumn
acceptReverseCharge2 = _AcceptReverseCharge2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 7),
    _AcceptReverseCharge2_Type()
)
acceptReverseCharge2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acceptReverseCharge2.setStatus("mandatory")
_ProposeReverseCharge2_Type = OffOn
_ProposeReverseCharge2_Object = MibTableColumn
proposeReverseCharge2 = _ProposeReverseCharge2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 8),
    _ProposeReverseCharge2_Type()
)
proposeReverseCharge2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proposeReverseCharge2.setStatus("mandatory")
_PermitTimeCut2_Type = OffOn
_PermitTimeCut2_Object = MibTableColumn
permitTimeCut2 = _PermitTimeCut2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 9),
    _PermitTimeCut2_Type()
)
permitTimeCut2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permitTimeCut2.setStatus("mandatory")
_MinCallDuration2_Type = Integer32
_MinCallDuration2_Object = MibTableColumn
minCallDuration2 = _MinCallDuration2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 10),
    _MinCallDuration2_Type()
)
minCallDuration2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minCallDuration2.setStatus("mandatory")
_IdleTime2_Type = Integer32
_IdleTime2_Object = MibTableColumn
idleTime2 = _IdleTime2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 11),
    _IdleTime2_Type()
)
idleTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleTime2.setStatus("mandatory")
_ReserveTime2_Type = Integer32
_ReserveTime2_Object = MibTableColumn
reserveTime2 = _ReserveTime2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 12),
    _ReserveTime2_Type()
)
reserveTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reserveTime2.setStatus("mandatory")
_OwnUserDataAddress2_Type = Integer32
_OwnUserDataAddress2_Object = MibTableColumn
ownUserDataAddress2 = _OwnUserDataAddress2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 13),
    _OwnUserDataAddress2_Type()
)
ownUserDataAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ownUserDataAddress2.setStatus("mandatory")
_CallsPlaced2_Type = Counter32
_CallsPlaced2_Object = MibTableColumn
callsPlaced2 = _CallsPlaced2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 14),
    _CallsPlaced2_Type()
)
callsPlaced2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callsPlaced2.setStatus("mandatory")
_CallsFailed2_Type = Counter32
_CallsFailed2_Object = MibTableColumn
callsFailed2 = _CallsFailed2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 15),
    _CallsFailed2_Type()
)
callsFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callsFailed2.setStatus("mandatory")
_MaxErrorRetries2_Type = Integer32
_MaxErrorRetries2_Object = MibTableColumn
maxErrorRetries2 = _MaxErrorRetries2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 16),
    _MaxErrorRetries2_Type()
)
maxErrorRetries2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxErrorRetries2.setStatus("mandatory")
_ErrorRetryInterval2_Type = Integer32
_ErrorRetryInterval2_Object = MibTableColumn
errorRetryInterval2 = _ErrorRetryInterval2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 17),
    _ErrorRetryInterval2_Type()
)
errorRetryInterval2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorRetryInterval2.setStatus("mandatory")
_MaxCallSetupTime2_Type = Integer32
_MaxCallSetupTime2_Object = MibTableColumn
maxCallSetupTime2 = _MaxCallSetupTime2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 18),
    _MaxCallSetupTime2_Type()
)
maxCallSetupTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxCallSetupTime2.setStatus("mandatory")
_MostRecentFailure2_Type = TimeTicks
_MostRecentFailure2_Object = MibTableColumn
mostRecentFailure2 = _MostRecentFailure2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 19),
    _MostRecentFailure2_Type()
)
mostRecentFailure2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mostRecentFailure2.setStatus("mandatory")
_PoolSize_Type = Integer32
_PoolSize_Object = MibTableColumn
poolSize = _PoolSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 20),
    _PoolSize_Type()
)
poolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSize.setStatus("mandatory")
_FreeLinks_Type = Integer32
_FreeLinks_Object = MibTableColumn
freeLinks = _FreeLinks_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 21),
    _FreeLinks_Type()
)
freeLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeLinks.setStatus("mandatory")
_IncomingAccessMask3_Type = OctetString
_IncomingAccessMask3_Object = MibTableColumn
incomingAccessMask3 = _IncomingAccessMask3_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 22),
    _IncomingAccessMask3_Type()
)
incomingAccessMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    incomingAccessMask3.setStatus("mandatory")


class _OutgoingAccessMask3_Type(OctetString):
    """Custom type outgoingAccessMask3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_OutgoingAccessMask3_Type.__name__ = "OctetString"
_OutgoingAccessMask3_Object = MibTableColumn
outgoingAccessMask3 = _OutgoingAccessMask3_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 23),
    _OutgoingAccessMask3_Type()
)
outgoingAccessMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outgoingAccessMask3.setStatus("mandatory")


class _TimecutAccessMask2_Type(OctetString):
    """Custom type timecutAccessMask2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_TimecutAccessMask2_Type.__name__ = "OctetString"
_TimecutAccessMask2_Object = MibTableColumn
timecutAccessMask2 = _TimecutAccessMask2_Object(
    (1, 3, 6, 1, 4, 1, 208, 24, 3, 2, 1, 24),
    _TimecutAccessMask2_Type()
)
timecutAccessMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timecutAccessMask2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-MPLINK-MIB",
    **{"OffOn": OffOn,
       "mplk": mplk,
       "service": service,
       "serviceTable": serviceTable,
       "serviceEntry": serviceEntry,
       "serviceNumber1": serviceNumber1,
       "serviceName": serviceName,
       "serviceType": serviceType,
       "slot": slot,
       "plug": plug,
       "serviceState": serviceState,
       "bytesSent": bytesSent,
       "bytesReceived": bytesReceived,
       "packetsSent": packetsSent,
       "packetsReceived": packetsReceived,
       "maxPacketSize": maxPacketSize,
       "lanSpecific": lanSpecific,
       "lanTable": lanTable,
       "lanEntry": lanEntry,
       "serviceNumber2": serviceNumber2,
       "ownSNPAAddress": ownSNPAAddress,
       "scaNetSubnet": scaNetSubnet,
       "incomingAccessMask1": incomingAccessMask1,
       "outgoingAccessMask1": outgoingAccessMask1,
       "wanSpecific": wanSpecific,
       "wanTable": wanTable,
       "wanEntry": wanEntry,
       "serviceNumber3": serviceNumber3,
       "provider": provider,
       "queueActualValue": queueActualValue,
       "queueHighWaterTideMark": queueHighWaterTideMark,
       "queueRejectThreshold1": queueRejectThreshold1,
       "dataCompressionSwitch1": dataCompressionSwitch1,
       "dataCompressionState": dataCompressionState,
       "acceptIncomingCalls1": acceptIncomingCalls1,
       "permitOutgoingCalls1": permitOutgoingCalls1,
       "acceptReverseCharge1": acceptReverseCharge1,
       "proposeReverseCharge1": proposeReverseCharge1,
       "permitTimeCut1": permitTimeCut1,
       "backupOnly": backupOnly,
       "actualCallState": actualCallState,
       "actualCallDirection": actualCallDirection,
       "actualCallDuration": actualCallDuration,
       "minCallDuration1": minCallDuration1,
       "idleTime1": idleTime1,
       "actualTimer": actualTimer,
       "reserveTime1": reserveTime1,
       "ownUserDataAddress1": ownUserDataAddress1,
       "remoteSNPAaddress": remoteSNPAaddress,
       "remoteUserDataAddress": remoteUserDataAddress,
       "callsPlaced1": callsPlaced1,
       "callsFailed1": callsFailed1,
       "actualErrorRetries": actualErrorRetries,
       "maxErrorRetries1": maxErrorRetries1,
       "errorRetryInterval1": errorRetryInterval1,
       "maxCallSetupTime1": maxCallSetupTime1,
       "mostRecentFailure1": mostRecentFailure1,
       "backupForLink": backupForLink,
       "poolIndex": poolIndex,
       "incomingAccessMask2": incomingAccessMask2,
       "outgoingAccessMask2": outgoingAccessMask2,
       "timecutAccessMask1": timecutAccessMask1,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "serviceNumber4": serviceNumber4,
       "poolName": poolName,
       "queueRejectThreshold2": queueRejectThreshold2,
       "dataCompressionSwitch2": dataCompressionSwitch2,
       "acceptIncomingCalls2": acceptIncomingCalls2,
       "permitOutgoingCalls2": permitOutgoingCalls2,
       "acceptReverseCharge2": acceptReverseCharge2,
       "proposeReverseCharge2": proposeReverseCharge2,
       "permitTimeCut2": permitTimeCut2,
       "minCallDuration2": minCallDuration2,
       "idleTime2": idleTime2,
       "reserveTime2": reserveTime2,
       "ownUserDataAddress2": ownUserDataAddress2,
       "callsPlaced2": callsPlaced2,
       "callsFailed2": callsFailed2,
       "maxErrorRetries2": maxErrorRetries2,
       "errorRetryInterval2": errorRetryInterval2,
       "maxCallSetupTime2": maxCallSetupTime2,
       "mostRecentFailure2": mostRecentFailure2,
       "poolSize": poolSize,
       "freeLinks": freeLinks,
       "incomingAccessMask3": incomingAccessMask3,
       "outgoingAccessMask3": outgoingAccessMask3,
       "timecutAccessMask2": timecutAccessMask2}
)
