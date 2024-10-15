# SNMP MIB module (CROSSSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CROSSSTREAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:57 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ConnectionStatus(Integer32):
    """Custom type ConnectionStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("delete", 6),
          ("inactive", 2),
          ("underCreation", 3))
    )





class StreamDirection(Integer32):
    """Custom type StreamDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )





class StreamState(Integer32):
    """Custom type StreamState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class StreamType(Integer32):
    """Custom type StreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asi", 2),
          ("atm", 1),
          ("ethernet", 3))
    )





class StreamIndex(Integer32):
    """Custom type StreamIndex based on Integer32"""




class ProgIndex(Integer32):
    """Custom type ProgIndex based on Integer32"""




class PidIndex(Integer32):
    """Custom type PidIndex based on Integer32"""




class ConnectionIndex(Integer32):
    """Custom type ConnectionIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Artel_ObjectIdentity = ObjectIdentity
artel = _Artel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 1)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1)
)


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_DeviceSerialNum_Type = DisplayString
_DeviceSerialNum_Object = MibScalar
deviceSerialNum = _DeviceSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 2),
    _DeviceSerialNum_Type()
)
deviceSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNum.setStatus("mandatory")
_DeviceModelNum_Type = DisplayString
_DeviceModelNum_Object = MibScalar
deviceModelNum = _DeviceModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 3),
    _DeviceModelNum_Type()
)
deviceModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModelNum.setStatus("mandatory")
_DeviceFwVer_Type = DisplayString
_DeviceFwVer_Object = MibScalar
deviceFwVer = _DeviceFwVer_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 4),
    _DeviceFwVer_Type()
)
deviceFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFwVer.setStatus("mandatory")
_DeviceHwVer_Type = DisplayString
_DeviceHwVer_Object = MibScalar
deviceHwVer = _DeviceHwVer_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 5),
    _DeviceHwVer_Type()
)
deviceHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHwVer.setStatus("mandatory")


class _DeviceTime_Type(DisplayString):
    """Custom type deviceTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_DeviceTime_Type.__name__ = "DisplayString"
_DeviceTime_Object = MibScalar
deviceTime = _DeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 6),
    _DeviceTime_Type()
)
deviceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceTime.setStatus("mandatory")


class _DeviceUpTime_Type(DisplayString):
    """Custom type deviceUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_DeviceUpTime_Type.__name__ = "DisplayString"
_DeviceUpTime_Object = MibScalar
deviceUpTime = _DeviceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 7),
    _DeviceUpTime_Type()
)
deviceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUpTime.setStatus("mandatory")
_DeviceIpAddress_Type = IpAddress
_DeviceIpAddress_Object = MibScalar
deviceIpAddress = _DeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 8),
    _DeviceIpAddress_Type()
)
deviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIpAddress.setStatus("mandatory")
_DeviceIpNetmask_Type = IpAddress
_DeviceIpNetmask_Object = MibScalar
deviceIpNetmask = _DeviceIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 9),
    _DeviceIpNetmask_Type()
)
deviceIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIpNetmask.setStatus("mandatory")
_DeviceGwAddress_Type = IpAddress
_DeviceGwAddress_Object = MibScalar
deviceGwAddress = _DeviceGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 10),
    _DeviceGwAddress_Type()
)
deviceGwAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGwAddress.setStatus("mandatory")
_DeviceHostAddress_Type = IpAddress
_DeviceHostAddress_Object = MibScalar
deviceHostAddress = _DeviceHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 11),
    _DeviceHostAddress_Type()
)
deviceHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceHostAddress.setStatus("mandatory")
_DeviceReset_Type = Integer32
_DeviceReset_Object = MibScalar
deviceReset = _DeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 4962, 1, 1, 12),
    _DeviceReset_Type()
)
deviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceReset.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2)
)
_CrossStream_ObjectIdentity = ObjectIdentity
crossStream = _CrossStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1)
)
_CstrmControl_ObjectIdentity = ObjectIdentity
cstrmControl = _CstrmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1)
)
_VsarReset_Type = Integer32
_VsarReset_Object = MibScalar
vsarReset = _VsarReset_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 1),
    _VsarReset_Type()
)
vsarReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsarReset.setStatus("mandatory")
_VsarConfigTable_Object = MibTable
vsarConfigTable = _VsarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vsarConfigTable.setStatus("mandatory")
_VsarConfigEntry_Object = MibTableRow
vsarConfigEntry = _VsarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 2, 1)
)
vsarConfigEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "vsarConfigIndex"),
)
if mibBuilder.loadTexts:
    vsarConfigEntry.setStatus("mandatory")
_VsarConfigIndex_Type = Integer32
_VsarConfigIndex_Object = MibTableColumn
vsarConfigIndex = _VsarConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 2, 1, 1),
    _VsarConfigIndex_Type()
)
vsarConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsarConfigIndex.setStatus("mandatory")
_VsarConfigType_Type = Integer32
_VsarConfigType_Object = MibTableColumn
vsarConfigType = _VsarConfigType_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 2, 1, 2),
    _VsarConfigType_Type()
)
vsarConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsarConfigType.setStatus("mandatory")


class _VsarConfigAction_Type(Integer32):
    """Custom type vsarConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("load", 1),
          ("store", 2))
    )


_VsarConfigAction_Type.__name__ = "Integer32"
_VsarConfigAction_Object = MibTableColumn
vsarConfigAction = _VsarConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 1, 2, 1, 4),
    _VsarConfigAction_Type()
)
vsarConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsarConfigAction.setStatus("mandatory")
_CstrmInfo_ObjectIdentity = ObjectIdentity
cstrmInfo = _CstrmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2)
)
_UsedAtmStreamsNumber_Type = Integer32
_UsedAtmStreamsNumber_Object = MibScalar
usedAtmStreamsNumber = _UsedAtmStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 1),
    _UsedAtmStreamsNumber_Type()
)
usedAtmStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedAtmStreamsNumber.setStatus("mandatory")
_ActiveAtmStreamsNumber_Type = Integer32
_ActiveAtmStreamsNumber_Object = MibScalar
activeAtmStreamsNumber = _ActiveAtmStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 2),
    _ActiveAtmStreamsNumber_Type()
)
activeAtmStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAtmStreamsNumber.setStatus("mandatory")
_MaxAtmStreamsNumber_Type = Integer32
_MaxAtmStreamsNumber_Object = MibScalar
maxAtmStreamsNumber = _MaxAtmStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 3),
    _MaxAtmStreamsNumber_Type()
)
maxAtmStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAtmStreamsNumber.setStatus("mandatory")
_UsedAsiStreamsNumber_Type = Integer32
_UsedAsiStreamsNumber_Object = MibScalar
usedAsiStreamsNumber = _UsedAsiStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 4),
    _UsedAsiStreamsNumber_Type()
)
usedAsiStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedAsiStreamsNumber.setStatus("mandatory")
_ActiveAsiStreamsNumber_Type = Integer32
_ActiveAsiStreamsNumber_Object = MibScalar
activeAsiStreamsNumber = _ActiveAsiStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 5),
    _ActiveAsiStreamsNumber_Type()
)
activeAsiStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAsiStreamsNumber.setStatus("mandatory")
_MaxAsiStreamsNumber_Type = Integer32
_MaxAsiStreamsNumber_Object = MibScalar
maxAsiStreamsNumber = _MaxAsiStreamsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 6),
    _MaxAsiStreamsNumber_Type()
)
maxAsiStreamsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxAsiStreamsNumber.setStatus("mandatory")
_UsedProgsNumber_Type = Integer32
_UsedProgsNumber_Object = MibScalar
usedProgsNumber = _UsedProgsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 7),
    _UsedProgsNumber_Type()
)
usedProgsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedProgsNumber.setStatus("mandatory")
_ActiveProgsNumber_Type = Integer32
_ActiveProgsNumber_Object = MibScalar
activeProgsNumber = _ActiveProgsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 8),
    _ActiveProgsNumber_Type()
)
activeProgsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeProgsNumber.setStatus("mandatory")
_MaxProgsNumber_Type = Integer32
_MaxProgsNumber_Object = MibScalar
maxProgsNumber = _MaxProgsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 9),
    _MaxProgsNumber_Type()
)
maxProgsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxProgsNumber.setStatus("mandatory")
_UsedPidsNumber_Type = Integer32
_UsedPidsNumber_Object = MibScalar
usedPidsNumber = _UsedPidsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 10),
    _UsedPidsNumber_Type()
)
usedPidsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedPidsNumber.setStatus("mandatory")
_ActivePidsNumber_Type = Integer32
_ActivePidsNumber_Object = MibScalar
activePidsNumber = _ActivePidsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 11),
    _ActivePidsNumber_Type()
)
activePidsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activePidsNumber.setStatus("mandatory")
_MaxPidsNumber_Type = Integer32
_MaxPidsNumber_Object = MibScalar
maxPidsNumber = _MaxPidsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 12),
    _MaxPidsNumber_Type()
)
maxPidsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPidsNumber.setStatus("mandatory")
_UsedConnectionsNumber_Type = Integer32
_UsedConnectionsNumber_Object = MibScalar
usedConnectionsNumber = _UsedConnectionsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 13),
    _UsedConnectionsNumber_Type()
)
usedConnectionsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedConnectionsNumber.setStatus("mandatory")
_MaxConnectionsNumber_Type = Integer32
_MaxConnectionsNumber_Object = MibScalar
maxConnectionsNumber = _MaxConnectionsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 2, 14),
    _MaxConnectionsNumber_Type()
)
maxConnectionsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConnectionsNumber.setStatus("mandatory")
_CstrmEvents_ObjectIdentity = ObjectIdentity
cstrmEvents = _CstrmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3)
)
_CstrmDiags_ObjectIdentity = ObjectIdentity
cstrmDiags = _CstrmDiags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4)
)
_CstrmAirTemp_Type = Integer32
_CstrmAirTemp_Object = MibScalar
cstrmAirTemp = _CstrmAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 1),
    _CstrmAirTemp_Type()
)
cstrmAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrmAirTemp.setStatus("mandatory")
_CstrmCoreRegTemp_Type = Integer32
_CstrmCoreRegTemp_Object = MibScalar
cstrmCoreRegTemp = _CstrmCoreRegTemp_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 2),
    _CstrmCoreRegTemp_Type()
)
cstrmCoreRegTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrmCoreRegTemp.setStatus("mandatory")
_Cstrm3VRegTemp_Type = Integer32
_Cstrm3VRegTemp_Object = MibScalar
cstrm3VRegTemp = _Cstrm3VRegTemp_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 3),
    _Cstrm3VRegTemp_Type()
)
cstrm3VRegTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrm3VRegTemp.setStatus("mandatory")
_CstrmHotICTemp_Type = Integer32
_CstrmHotICTemp_Object = MibScalar
cstrmHotICTemp = _CstrmHotICTemp_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 4),
    _CstrmHotICTemp_Type()
)
cstrmHotICTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrmHotICTemp.setStatus("mandatory")
_Cstrm5VCoreVoltage_Type = Integer32
_Cstrm5VCoreVoltage_Object = MibScalar
cstrm5VCoreVoltage = _Cstrm5VCoreVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 5),
    _Cstrm5VCoreVoltage_Type()
)
cstrm5VCoreVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrm5VCoreVoltage.setStatus("mandatory")
_Cstrm3VCoreVoltage_Type = Integer32
_Cstrm3VCoreVoltage_Object = MibScalar
cstrm3VCoreVoltage = _Cstrm3VCoreVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 6),
    _Cstrm3VCoreVoltage_Type()
)
cstrm3VCoreVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrm3VCoreVoltage.setStatus("mandatory")
_Cstrm3VIOVoltage_Type = Integer32
_Cstrm3VIOVoltage_Object = MibScalar
cstrm3VIOVoltage = _Cstrm3VIOVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 4, 7),
    _Cstrm3VIOVoltage_Type()
)
cstrm3VIOVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrm3VIOVoltage.setStatus("mandatory")
_CstrmStreamGroup_ObjectIdentity = ObjectIdentity
cstrmStreamGroup = _CstrmStreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5)
)
_StreamNextIndex_Type = Integer32
_StreamNextIndex_Object = MibScalar
streamNextIndex = _StreamNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 1),
    _StreamNextIndex_Type()
)
streamNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamNextIndex.setStatus("mandatory")
_StreamTable_Object = MibTable
streamTable = _StreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    streamTable.setStatus("mandatory")
_StreamEntry_Object = MibTableRow
streamEntry = _StreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1)
)
streamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    streamEntry.setStatus("mandatory")
_StreamIndex_Type = Integer32
_StreamIndex_Object = MibTableColumn
streamIndex = _StreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 1),
    _StreamIndex_Type()
)
streamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    streamIndex.setStatus("mandatory")
_IngressState_Type = StreamState
_IngressState_Object = MibTableColumn
ingressState = _IngressState_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 2),
    _IngressState_Type()
)
ingressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressState.setStatus("mandatory")
_EgressState_Type = StreamState
_EgressState_Object = MibTableColumn
egressState = _EgressState_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 3),
    _EgressState_Type()
)
egressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressState.setStatus("mandatory")
_StreamType_Type = StreamType
_StreamType_Object = MibTableColumn
streamType = _StreamType_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 4),
    _StreamType_Type()
)
streamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamType.setStatus("mandatory")
_StreamName_Type = DisplayString
_StreamName_Object = MibTableColumn
streamName = _StreamName_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 5),
    _StreamName_Type()
)
streamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamName.setStatus("mandatory")
_StreamStatus_Type = ConnectionStatus
_StreamStatus_Object = MibTableColumn
streamStatus = _StreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 2, 1, 6),
    _StreamStatus_Type()
)
streamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    streamStatus.setStatus("mandatory")
_IngressStreamTable_Object = MibTable
ingressStreamTable = _IngressStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ingressStreamTable.setStatus("mandatory")
_IngressStreamEntry_Object = MibTableRow
ingressStreamEntry = _IngressStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 3, 1)
)
ingressStreamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    ingressStreamEntry.setStatus("mandatory")
_IngressStreamCellRate_Type = Integer32
_IngressStreamCellRate_Object = MibTableColumn
ingressStreamCellRate = _IngressStreamCellRate_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 3, 1, 1),
    _IngressStreamCellRate_Type()
)
ingressStreamCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressStreamCellRate.setStatus("mandatory")
_EgressStreamTable_Object = MibTable
egressStreamTable = _EgressStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    egressStreamTable.setStatus("mandatory")
_EgressStreamEntry_Object = MibTableRow
egressStreamEntry = _EgressStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1)
)
egressStreamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    egressStreamEntry.setStatus("mandatory")
_EgressStreamTsRate_Type = Integer32
_EgressStreamTsRate_Object = MibTableColumn
egressStreamTsRate = _EgressStreamTsRate_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1, 1),
    _EgressStreamTsRate_Type()
)
egressStreamTsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamTsRate.setStatus("mandatory")
_EgressStreamNumBufs_Type = Integer32
_EgressStreamNumBufs_Object = MibTableColumn
egressStreamNumBufs = _EgressStreamNumBufs_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1, 2),
    _EgressStreamNumBufs_Type()
)
egressStreamNumBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamNumBufs.setStatus("mandatory")
_EgressStreamBufThreshold_Type = Integer32
_EgressStreamBufThreshold_Object = MibTableColumn
egressStreamBufThreshold = _EgressStreamBufThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1, 3),
    _EgressStreamBufThreshold_Type()
)
egressStreamBufThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamBufThreshold.setStatus("mandatory")
_EgressStreamBufSize_Type = Integer32
_EgressStreamBufSize_Object = MibTableColumn
egressStreamBufSize = _EgressStreamBufSize_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1, 4),
    _EgressStreamBufSize_Type()
)
egressStreamBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamBufSize.setStatus("mandatory")


class _EgressStreamJitter_Type(Integer32):
    """Custom type egressStreamJitter based on Integer32"""
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


_EgressStreamJitter_Type.__name__ = "Integer32"
_EgressStreamJitter_Object = MibTableColumn
egressStreamJitter = _EgressStreamJitter_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 4, 1, 5),
    _EgressStreamJitter_Type()
)
egressStreamJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamJitter.setStatus("mandatory")
_AtmStreamTable_Object = MibTable
atmStreamTable = _AtmStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    atmStreamTable.setStatus("mandatory")
_AtmStreamEntry_Object = MibTableRow
atmStreamEntry = _AtmStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 5, 1)
)
atmStreamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    atmStreamEntry.setStatus("mandatory")
_AtmStreamVpi_Type = Integer32
_AtmStreamVpi_Object = MibTableColumn
atmStreamVpi = _AtmStreamVpi_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 5, 1, 1),
    _AtmStreamVpi_Type()
)
atmStreamVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmStreamVpi.setStatus("mandatory")
_AtmStreamVci_Type = Integer32
_AtmStreamVci_Object = MibTableColumn
atmStreamVci = _AtmStreamVci_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 5, 1, 2),
    _AtmStreamVci_Type()
)
atmStreamVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmStreamVci.setStatus("mandatory")
_AsiStreamTable_Object = MibTable
asiStreamTable = _AsiStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    asiStreamTable.setStatus("mandatory")
_AsiStreamEntry_Object = MibTableRow
asiStreamEntry = _AsiStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 6, 1)
)
asiStreamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    asiStreamEntry.setStatus("mandatory")
_AsiStreamPort_Type = Integer32
_AsiStreamPort_Object = MibTableColumn
asiStreamPort = _AsiStreamPort_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 6, 1, 1),
    _AsiStreamPort_Type()
)
asiStreamPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asiStreamPort.setStatus("mandatory")
_AsiStreamChannel_Type = Integer32
_AsiStreamChannel_Object = MibTableColumn
asiStreamChannel = _AsiStreamChannel_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 6, 1, 2),
    _AsiStreamChannel_Type()
)
asiStreamChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asiStreamChannel.setStatus("mandatory")
_ProgNextTable_Object = MibTable
progNextTable = _ProgNextTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    progNextTable.setStatus("mandatory")
_ProgNextEntry_Object = MibTableRow
progNextEntry = _ProgNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 7, 1)
)
progNextEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
)
if mibBuilder.loadTexts:
    progNextEntry.setStatus("mandatory")
_ProgNextIndex_Type = Integer32
_ProgNextIndex_Object = MibTableColumn
progNextIndex = _ProgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 7, 1, 1),
    _ProgNextIndex_Type()
)
progNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    progNextIndex.setStatus("mandatory")
_ProgTable_Object = MibTable
progTable = _ProgTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    progTable.setStatus("mandatory")
_ProgEntry_Object = MibTableRow
progEntry = _ProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1)
)
progEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
    (0, "CROSSSTREAM-MIB", "progIndex"),
)
if mibBuilder.loadTexts:
    progEntry.setStatus("mandatory")
_ProgIndex_Type = Integer32
_ProgIndex_Object = MibTableColumn
progIndex = _ProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 1),
    _ProgIndex_Type()
)
progIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    progIndex.setStatus("mandatory")
_ProgNumber_Type = Integer32
_ProgNumber_Object = MibTableColumn
progNumber = _ProgNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 2),
    _ProgNumber_Type()
)
progNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progNumber.setStatus("mandatory")


class _ProgName_Type(DisplayString):
    """Custom type progName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ProgName_Type.__name__ = "DisplayString"
_ProgName_Object = MibTableColumn
progName = _ProgName_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 3),
    _ProgName_Type()
)
progName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progName.setStatus("mandatory")
_ProgTsRate_Type = Integer32
_ProgTsRate_Object = MibTableColumn
progTsRate = _ProgTsRate_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 4),
    _ProgTsRate_Type()
)
progTsRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progTsRate.setStatus("mandatory")
_ProgTsLen_Type = Integer32
_ProgTsLen_Object = MibTableColumn
progTsLen = _ProgTsLen_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 5),
    _ProgTsLen_Type()
)
progTsLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progTsLen.setStatus("mandatory")
_ProgStatus_Type = ConnectionStatus
_ProgStatus_Object = MibTableColumn
progStatus = _ProgStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 8, 1, 6),
    _ProgStatus_Type()
)
progStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    progStatus.setStatus("mandatory")
_PidNextTable_Object = MibTable
pidNextTable = _PidNextTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    pidNextTable.setStatus("mandatory")
_PidNextEntry_Object = MibTableRow
pidNextEntry = _PidNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 9, 1)
)
pidNextEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
    (0, "CROSSSTREAM-MIB", "progIndex"),
)
if mibBuilder.loadTexts:
    pidNextEntry.setStatus("mandatory")
_PidNextIndex_Type = Integer32
_PidNextIndex_Object = MibTableColumn
pidNextIndex = _PidNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 9, 1, 1),
    _PidNextIndex_Type()
)
pidNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidNextIndex.setStatus("mandatory")
_PidTable_Object = MibTable
pidTable = _PidTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    pidTable.setStatus("mandatory")
_PidEntry_Object = MibTableRow
pidEntry = _PidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1)
)
pidEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "streamIndex"),
    (0, "CROSSSTREAM-MIB", "progIndex"),
    (0, "CROSSSTREAM-MIB", "pidIndex"),
)
if mibBuilder.loadTexts:
    pidEntry.setStatus("mandatory")
_PidIndex_Type = Integer32
_PidIndex_Object = MibTableColumn
pidIndex = _PidIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1, 1),
    _PidIndex_Type()
)
pidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pidIndex.setStatus("mandatory")
_PidNumber_Type = Integer32
_PidNumber_Object = MibTableColumn
pidNumber = _PidNumber_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1, 2),
    _PidNumber_Type()
)
pidNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidNumber.setStatus("mandatory")
_PidTableID_Type = Integer32
_PidTableID_Object = MibTableColumn
pidTableID = _PidTableID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1, 3),
    _PidTableID_Type()
)
pidTableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidTableID.setStatus("mandatory")
_PidRate_Type = Integer32
_PidRate_Object = MibTableColumn
pidRate = _PidRate_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1, 4),
    _PidRate_Type()
)
pidRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidRate.setStatus("mandatory")
_PidStatus_Type = ConnectionStatus
_PidStatus_Object = MibTableColumn
pidStatus = _PidStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 10, 1, 5),
    _PidStatus_Type()
)
pidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pidStatus.setStatus("mandatory")
_CstrmConnNextIndex_Type = Integer32
_CstrmConnNextIndex_Object = MibScalar
cstrmConnNextIndex = _CstrmConnNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 11),
    _CstrmConnNextIndex_Type()
)
cstrmConnNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrmConnNextIndex.setStatus("mandatory")
_CstrmConnTable_Object = MibTable
cstrmConnTable = _CstrmConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    cstrmConnTable.setStatus("mandatory")
_CstrmConnEntry_Object = MibTableRow
cstrmConnEntry = _CstrmConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1)
)
cstrmConnEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "cstrmConnIndex"),
)
if mibBuilder.loadTexts:
    cstrmConnEntry.setStatus("mandatory")
_CstrmConnIndex_Type = Integer32
_CstrmConnIndex_Object = MibTableColumn
cstrmConnIndex = _CstrmConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 1),
    _CstrmConnIndex_Type()
)
cstrmConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstrmConnIndex.setStatus("mandatory")
_IngressStreamIndexVal_Type = Integer32
_IngressStreamIndexVal_Object = MibTableColumn
ingressStreamIndexVal = _IngressStreamIndexVal_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 2),
    _IngressStreamIndexVal_Type()
)
ingressStreamIndexVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressStreamIndexVal.setStatus("mandatory")
_EgressStreamIndexVal_Type = Integer32
_EgressStreamIndexVal_Object = MibTableColumn
egressStreamIndexVal = _EgressStreamIndexVal_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 3),
    _EgressStreamIndexVal_Type()
)
egressStreamIndexVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressStreamIndexVal.setStatus("mandatory")
_IngressProgIndex_Type = Integer32
_IngressProgIndex_Object = MibTableColumn
ingressProgIndex = _IngressProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 4),
    _IngressProgIndex_Type()
)
ingressProgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressProgIndex.setStatus("mandatory")
_IngressPidIndex_Type = Integer32
_IngressPidIndex_Object = MibTableColumn
ingressPidIndex = _IngressPidIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 5),
    _IngressPidIndex_Type()
)
ingressPidIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressPidIndex.setStatus("mandatory")
_EgressProgNum_Type = Integer32
_EgressProgNum_Object = MibTableColumn
egressProgNum = _EgressProgNum_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 6),
    _EgressProgNum_Type()
)
egressProgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressProgNum.setStatus("mandatory")
_EgressPidNum_Type = Integer32
_EgressPidNum_Object = MibTableColumn
egressPidNum = _EgressPidNum_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 7),
    _EgressPidNum_Type()
)
egressPidNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressPidNum.setStatus("mandatory")


class _PcrAdjust_Type(Integer32):
    """Custom type pcrAdjust based on Integer32"""
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


_PcrAdjust_Type.__name__ = "Integer32"
_PcrAdjust_Object = MibTableColumn
pcrAdjust = _PcrAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 8),
    _PcrAdjust_Type()
)
pcrAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcrAdjust.setStatus("mandatory")
_CstrmConnStatus_Type = ConnectionStatus
_CstrmConnStatus_Object = MibTableColumn
cstrmConnStatus = _CstrmConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 12, 1, 9),
    _CstrmConnStatus_Type()
)
cstrmConnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cstrmConnStatus.setStatus("mandatory")
_ConnectionStreamTable_Object = MibTable
connectionStreamTable = _ConnectionStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 13)
)
if mibBuilder.loadTexts:
    connectionStreamTable.setStatus("mandatory")
_ConnectionStreamEntry_Object = MibTableRow
connectionStreamEntry = _ConnectionStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 13, 1)
)
connectionStreamEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "StreamDirection"),
    (0, "CROSSSTREAM-MIB", "StreamIndex"),
    (0, "CROSSSTREAM-MIB", "ConnectionIndex"),
)
if mibBuilder.loadTexts:
    connectionStreamEntry.setStatus("mandatory")
_ConnectionStreamIndex_Type = Integer32
_ConnectionStreamIndex_Object = MibTableColumn
connectionStreamIndex = _ConnectionStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 13, 1, 1),
    _ConnectionStreamIndex_Type()
)
connectionStreamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionStreamIndex.setStatus("mandatory")
_ConnectionProgTable_Object = MibTable
connectionProgTable = _ConnectionProgTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 14)
)
if mibBuilder.loadTexts:
    connectionProgTable.setStatus("mandatory")
_ConnectionProgEntry_Object = MibTableRow
connectionProgEntry = _ConnectionProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 14, 1)
)
connectionProgEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "StreamDirection"),
    (0, "CROSSSTREAM-MIB", "StreamIndex"),
    (0, "CROSSSTREAM-MIB", "ProgIndex"),
    (0, "CROSSSTREAM-MIB", "ConnectionIndex"),
)
if mibBuilder.loadTexts:
    connectionProgEntry.setStatus("mandatory")
_ConnectionProgIndex_Type = Integer32
_ConnectionProgIndex_Object = MibTableColumn
connectionProgIndex = _ConnectionProgIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 14, 1, 1),
    _ConnectionProgIndex_Type()
)
connectionProgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionProgIndex.setStatus("mandatory")
_ConnectionPidTable_Object = MibTable
connectionPidTable = _ConnectionPidTable_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 15)
)
if mibBuilder.loadTexts:
    connectionPidTable.setStatus("mandatory")
_ConnectionPidEntry_Object = MibTableRow
connectionPidEntry = _ConnectionPidEntry_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 15, 1)
)
connectionPidEntry.setIndexNames(
    (0, "CROSSSTREAM-MIB", "StreamDirection"),
    (0, "CROSSSTREAM-MIB", "StreamIndex"),
    (0, "CROSSSTREAM-MIB", "ProgIndex"),
    (0, "CROSSSTREAM-MIB", "PidIndex"),
    (0, "CROSSSTREAM-MIB", "ConnectionIndex"),
)
if mibBuilder.loadTexts:
    connectionPidEntry.setStatus("mandatory")
_ConnectionPidIndex_Type = Integer32
_ConnectionPidIndex_Object = MibTableColumn
connectionPidIndex = _ConnectionPidIndex_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 5, 15, 1, 1),
    _ConnectionPidIndex_Type()
)
connectionPidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionPidIndex.setStatus("mandatory")
_CstrmStreamPrivate_ObjectIdentity = ObjectIdentity
cstrmStreamPrivate = _CstrmStreamPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6)
)
_CstrmATMPhyTrapID_Type = Integer32
_CstrmATMPhyTrapID_Object = MibScalar
cstrmATMPhyTrapID = _CstrmATMPhyTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 1),
    _CstrmATMPhyTrapID_Type()
)
cstrmATMPhyTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmATMPhyTrapID.setStatus("mandatory")
_CstrmATMPhyTrapStatus_Type = Integer32
_CstrmATMPhyTrapStatus_Object = MibScalar
cstrmATMPhyTrapStatus = _CstrmATMPhyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 1, 1),
    _CstrmATMPhyTrapStatus_Type()
)
cstrmATMPhyTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmATMPhyTrapStatus.setStatus("mandatory")
_CstrmOAMVCTrapID_Type = Integer32
_CstrmOAMVCTrapID_Object = MibScalar
cstrmOAMVCTrapID = _CstrmOAMVCTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 2),
    _CstrmOAMVCTrapID_Type()
)
cstrmOAMVCTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmOAMVCTrapID.setStatus("mandatory")
_CstrmOAMVCTrapStatus_Type = Integer32
_CstrmOAMVCTrapStatus_Object = MibScalar
cstrmOAMVCTrapStatus = _CstrmOAMVCTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 2, 1),
    _CstrmOAMVCTrapStatus_Type()
)
cstrmOAMVCTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmOAMVCTrapStatus.setStatus("mandatory")
_CstrmOAMVPTrapID_Type = Integer32
_CstrmOAMVPTrapID_Object = MibScalar
cstrmOAMVPTrapID = _CstrmOAMVPTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 3),
    _CstrmOAMVPTrapID_Type()
)
cstrmOAMVPTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmOAMVPTrapID.setStatus("mandatory")
_CstrmOAMVPTrapStatus_Type = Integer32
_CstrmOAMVPTrapStatus_Object = MibScalar
cstrmOAMVPTrapStatus = _CstrmOAMVPTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 3, 1),
    _CstrmOAMVPTrapStatus_Type()
)
cstrmOAMVPTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmOAMVPTrapStatus.setStatus("mandatory")
_CstrmSONETTrapID_Type = Integer32
_CstrmSONETTrapID_Object = MibScalar
cstrmSONETTrapID = _CstrmSONETTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 4),
    _CstrmSONETTrapID_Type()
)
cstrmSONETTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmSONETTrapID.setStatus("mandatory")
_CstrmSONETTrapStatus_Type = Integer32
_CstrmSONETTrapStatus_Object = MibScalar
cstrmSONETTrapStatus = _CstrmSONETTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 4, 1),
    _CstrmSONETTrapStatus_Type()
)
cstrmSONETTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmSONETTrapStatus.setStatus("mandatory")
_CstrmActDeActTrapID_Type = Integer32
_CstrmActDeActTrapID_Object = MibScalar
cstrmActDeActTrapID = _CstrmActDeActTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 5),
    _CstrmActDeActTrapID_Type()
)
cstrmActDeActTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmActDeActTrapID.setStatus("mandatory")
_CstrmActDeActTrapStatus_Type = Integer32
_CstrmActDeActTrapStatus_Object = MibScalar
cstrmActDeActTrapStatus = _CstrmActDeActTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 5, 1),
    _CstrmActDeActTrapStatus_Type()
)
cstrmActDeActTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmActDeActTrapStatus.setStatus("mandatory")
_CstrmIngressPidsChangedTrapID_Type = Integer32
_CstrmIngressPidsChangedTrapID_Object = MibScalar
cstrmIngressPidsChangedTrapID = _CstrmIngressPidsChangedTrapID_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 6),
    _CstrmIngressPidsChangedTrapID_Type()
)
cstrmIngressPidsChangedTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmIngressPidsChangedTrapID.setStatus("mandatory")
_CstrmIngressPidsChangedTrapStatus_Type = Integer32
_CstrmIngressPidsChangedTrapStatus_Object = MibScalar
cstrmIngressPidsChangedTrapStatus = _CstrmIngressPidsChangedTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 6, 6, 1),
    _CstrmIngressPidsChangedTrapStatus_Type()
)
cstrmIngressPidsChangedTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstrmIngressPidsChangedTrapStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cstrmOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 1)
)
cstrmOverTemp.setObjects(
      *(("CROSSSTREAM-MIB", "cstrmAirTemp"),
        ("CROSSSTREAM-MIB", "cstrmCoreRegTemp"),
        ("CROSSSTREAM-MIB", "cstrm3VRegTemp"),
        ("CROSSSTREAM-MIB", "cstrmHotICTemp"))
)
if mibBuilder.loadTexts:
    cstrmOverTemp.setStatus(
        ""
    )

cstrmCoolFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    cstrmCoolFail.setStatus(
        ""
    )

cstrmPowerMonitor = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 3)
)
cstrmPowerMonitor.setObjects(
      *(("CROSSSTREAM-MIB", "cstrm5VCoreVoltage"),
        ("CROSSSTREAM-MIB", "cstrm3VCoreVoltage"),
        ("CROSSSTREAM-MIB", "cstrm3VIOVoltage"))
)
if mibBuilder.loadTexts:
    cstrmPowerMonitor.setStatus(
        ""
    )

cstrmATMPhyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 4)
)
cstrmATMPhyTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmATMPhyTrapID"),
        ("CROSSSTREAM-MIB", "cstrmATMPhyTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmATMPhyTrap.setStatus(
        ""
    )

cstrmOAMVPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 5)
)
cstrmOAMVPTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmOAMVPTrapID"),
        ("CROSSSTREAM-MIB", "atmStreamVpi"),
        ("CROSSSTREAM-MIB", "cstrmOAMVPTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmOAMVPTrap.setStatus(
        ""
    )

cstrmOAMVCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 6)
)
cstrmOAMVCTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmOAMVCTrapID"),
        ("CROSSSTREAM-MIB", "atmStreamVpi"),
        ("CROSSSTREAM-MIB", "atmStreamVci"),
        ("CROSSSTREAM-MIB", "cstrmOAMVCTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmOAMVCTrap.setStatus(
        ""
    )

cstrmSONETTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 7)
)
cstrmSONETTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmSONETTrapID"),
        ("CROSSSTREAM-MIB", "cstrmSONETTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmSONETTrap.setStatus(
        ""
    )

cstrmActDeActTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 8)
)
cstrmActDeActTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmActDeActTrapID"),
        ("CROSSSTREAM-MIB", "cstrmActDeActTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmActDeActTrap.setStatus(
        ""
    )

cstrmIngressPidsChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4962, 2, 1, 3, 0, 9)
)
cstrmIngressPidsChangedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CROSSSTREAM-MIB", "cstrmIngressPidsChangedTrapID"),
        ("CROSSSTREAM-MIB", "cstrmIngressPidsChangedTrapStatus"))
)
if mibBuilder.loadTexts:
    cstrmIngressPidsChangedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CROSSSTREAM-MIB",
    **{"ConnectionStatus": ConnectionStatus,
       "StreamDirection": StreamDirection,
       "StreamState": StreamState,
       "StreamType": StreamType,
       "StreamIndex": StreamIndex,
       "ProgIndex": ProgIndex,
       "PidIndex": PidIndex,
       "ConnectionIndex": ConnectionIndex,
       "artel": artel,
       "common": common,
       "device": device,
       "deviceName": deviceName,
       "deviceSerialNum": deviceSerialNum,
       "deviceModelNum": deviceModelNum,
       "deviceFwVer": deviceFwVer,
       "deviceHwVer": deviceHwVer,
       "deviceTime": deviceTime,
       "deviceUpTime": deviceUpTime,
       "deviceIpAddress": deviceIpAddress,
       "deviceIpNetmask": deviceIpNetmask,
       "deviceGwAddress": deviceGwAddress,
       "deviceHostAddress": deviceHostAddress,
       "deviceReset": deviceReset,
       "products": products,
       "crossStream": crossStream,
       "cstrmControl": cstrmControl,
       "vsarReset": vsarReset,
       "vsarConfigTable": vsarConfigTable,
       "vsarConfigEntry": vsarConfigEntry,
       "vsarConfigIndex": vsarConfigIndex,
       "vsarConfigType": vsarConfigType,
       "vsarConfigAction": vsarConfigAction,
       "cstrmInfo": cstrmInfo,
       "usedAtmStreamsNumber": usedAtmStreamsNumber,
       "activeAtmStreamsNumber": activeAtmStreamsNumber,
       "maxAtmStreamsNumber": maxAtmStreamsNumber,
       "usedAsiStreamsNumber": usedAsiStreamsNumber,
       "activeAsiStreamsNumber": activeAsiStreamsNumber,
       "maxAsiStreamsNumber": maxAsiStreamsNumber,
       "usedProgsNumber": usedProgsNumber,
       "activeProgsNumber": activeProgsNumber,
       "maxProgsNumber": maxProgsNumber,
       "usedPidsNumber": usedPidsNumber,
       "activePidsNumber": activePidsNumber,
       "maxPidsNumber": maxPidsNumber,
       "usedConnectionsNumber": usedConnectionsNumber,
       "maxConnectionsNumber": maxConnectionsNumber,
       "cstrmEvents": cstrmEvents,
       "cstrmOverTemp": cstrmOverTemp,
       "cstrmCoolFail": cstrmCoolFail,
       "cstrmPowerMonitor": cstrmPowerMonitor,
       "cstrmATMPhyTrap": cstrmATMPhyTrap,
       "cstrmOAMVPTrap": cstrmOAMVPTrap,
       "cstrmOAMVCTrap": cstrmOAMVCTrap,
       "cstrmSONETTrap": cstrmSONETTrap,
       "cstrmActDeActTrap": cstrmActDeActTrap,
       "cstrmIngressPidsChangedTrap": cstrmIngressPidsChangedTrap,
       "cstrmDiags": cstrmDiags,
       "cstrmAirTemp": cstrmAirTemp,
       "cstrmCoreRegTemp": cstrmCoreRegTemp,
       "cstrm3VRegTemp": cstrm3VRegTemp,
       "cstrmHotICTemp": cstrmHotICTemp,
       "cstrm5VCoreVoltage": cstrm5VCoreVoltage,
       "cstrm3VCoreVoltage": cstrm3VCoreVoltage,
       "cstrm3VIOVoltage": cstrm3VIOVoltage,
       "cstrmStreamGroup": cstrmStreamGroup,
       "streamNextIndex": streamNextIndex,
       "streamTable": streamTable,
       "streamEntry": streamEntry,
       "streamIndex": streamIndex,
       "ingressState": ingressState,
       "egressState": egressState,
       "streamType": streamType,
       "streamName": streamName,
       "streamStatus": streamStatus,
       "ingressStreamTable": ingressStreamTable,
       "ingressStreamEntry": ingressStreamEntry,
       "ingressStreamCellRate": ingressStreamCellRate,
       "egressStreamTable": egressStreamTable,
       "egressStreamEntry": egressStreamEntry,
       "egressStreamTsRate": egressStreamTsRate,
       "egressStreamNumBufs": egressStreamNumBufs,
       "egressStreamBufThreshold": egressStreamBufThreshold,
       "egressStreamBufSize": egressStreamBufSize,
       "egressStreamJitter": egressStreamJitter,
       "atmStreamTable": atmStreamTable,
       "atmStreamEntry": atmStreamEntry,
       "atmStreamVpi": atmStreamVpi,
       "atmStreamVci": atmStreamVci,
       "asiStreamTable": asiStreamTable,
       "asiStreamEntry": asiStreamEntry,
       "asiStreamPort": asiStreamPort,
       "asiStreamChannel": asiStreamChannel,
       "progNextTable": progNextTable,
       "progNextEntry": progNextEntry,
       "progNextIndex": progNextIndex,
       "progTable": progTable,
       "progEntry": progEntry,
       "progIndex": progIndex,
       "progNumber": progNumber,
       "progName": progName,
       "progTsRate": progTsRate,
       "progTsLen": progTsLen,
       "progStatus": progStatus,
       "pidNextTable": pidNextTable,
       "pidNextEntry": pidNextEntry,
       "pidNextIndex": pidNextIndex,
       "pidTable": pidTable,
       "pidEntry": pidEntry,
       "pidIndex": pidIndex,
       "pidNumber": pidNumber,
       "pidTableID": pidTableID,
       "pidRate": pidRate,
       "pidStatus": pidStatus,
       "cstrmConnNextIndex": cstrmConnNextIndex,
       "cstrmConnTable": cstrmConnTable,
       "cstrmConnEntry": cstrmConnEntry,
       "cstrmConnIndex": cstrmConnIndex,
       "ingressStreamIndexVal": ingressStreamIndexVal,
       "egressStreamIndexVal": egressStreamIndexVal,
       "ingressProgIndex": ingressProgIndex,
       "ingressPidIndex": ingressPidIndex,
       "egressProgNum": egressProgNum,
       "egressPidNum": egressPidNum,
       "pcrAdjust": pcrAdjust,
       "cstrmConnStatus": cstrmConnStatus,
       "connectionStreamTable": connectionStreamTable,
       "connectionStreamEntry": connectionStreamEntry,
       "connectionStreamIndex": connectionStreamIndex,
       "connectionProgTable": connectionProgTable,
       "connectionProgEntry": connectionProgEntry,
       "connectionProgIndex": connectionProgIndex,
       "connectionPidTable": connectionPidTable,
       "connectionPidEntry": connectionPidEntry,
       "connectionPidIndex": connectionPidIndex,
       "cstrmStreamPrivate": cstrmStreamPrivate,
       "cstrmATMPhyTrapID": cstrmATMPhyTrapID,
       "cstrmATMPhyTrapStatus": cstrmATMPhyTrapStatus,
       "cstrmOAMVCTrapID": cstrmOAMVCTrapID,
       "cstrmOAMVCTrapStatus": cstrmOAMVCTrapStatus,
       "cstrmOAMVPTrapID": cstrmOAMVPTrapID,
       "cstrmOAMVPTrapStatus": cstrmOAMVPTrapStatus,
       "cstrmSONETTrapID": cstrmSONETTrapID,
       "cstrmSONETTrapStatus": cstrmSONETTrapStatus,
       "cstrmActDeActTrapID": cstrmActDeActTrapID,
       "cstrmActDeActTrapStatus": cstrmActDeActTrapStatus,
       "cstrmIngressPidsChangedTrapID": cstrmIngressPidsChangedTrapID,
       "cstrmIngressPidsChangedTrapStatus": cstrmIngressPidsChangedTrapStatus}
)
