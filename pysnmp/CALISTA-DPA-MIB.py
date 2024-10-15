# SNMP MIB module (CALISTA-DPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CALISTA-DPA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:24 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Calista_ObjectIdentity = ObjectIdentity
calista = _Calista_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7505)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7505, 1)
)
_Dpa_ObjectIdentity = ObjectIdentity
dpa = _Dpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1)
)
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
_ImageVersion_Type = DisplayString
_ImageVersion_Object = MibScalar
imageVersion = _ImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 2),
    _ImageVersion_Type()
)
imageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageVersion.setStatus("mandatory")
_LoaderVersion_Type = DisplayString
_LoaderVersion_Object = MibScalar
loaderVersion = _LoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 3),
    _LoaderVersion_Type()
)
loaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loaderVersion.setStatus("mandatory")


class _IntegrationMode_Type(Integer32):
    """Custom type integrationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("simple", 2),
          ("unconfigured", 1))
    )


_IntegrationMode_Type.__name__ = "Integer32"
_IntegrationMode_Object = MibScalar
integrationMode = _IntegrationMode_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 4),
    _IntegrationMode_Type()
)
integrationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    integrationMode.setStatus("mandatory")
_PbxType_Type = DisplayString
_PbxType_Object = MibScalar
pbxType = _PbxType_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 5),
    _PbxType_Type()
)
pbxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxType.setStatus("mandatory")
_ReceivedCalls_Type = Counter32
_ReceivedCalls_Object = MibScalar
receivedCalls = _ReceivedCalls_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 6),
    _ReceivedCalls_Type()
)
receivedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    receivedCalls.setStatus("mandatory")
_OutgoingCallsMade_Type = Counter32
_OutgoingCallsMade_Object = MibScalar
outgoingCallsMade = _OutgoingCallsMade_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 7),
    _OutgoingCallsMade_Type()
)
outgoingCallsMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outgoingCallsMade.setStatus("mandatory")
_MwiCommandsReceived_Type = Counter32
_MwiCommandsReceived_Object = MibScalar
mwiCommandsReceived = _MwiCommandsReceived_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 8),
    _MwiCommandsReceived_Type()
)
mwiCommandsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiCommandsReceived.setStatus("mandatory")
_PbxQueuedMWICommands_Type = Counter32
_PbxQueuedMWICommands_Object = MibScalar
pbxQueuedMWICommands = _PbxQueuedMWICommands_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 9),
    _PbxQueuedMWICommands_Type()
)
pbxQueuedMWICommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxQueuedMWICommands.setStatus("mandatory")
_PbxCompletedMWICommands_Type = Counter32
_PbxCompletedMWICommands_Object = MibScalar
pbxCompletedMWICommands = _PbxCompletedMWICommands_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 10),
    _PbxCompletedMWICommands_Type()
)
pbxCompletedMWICommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxCompletedMWICommands.setStatus("mandatory")
_PbxMWIErrors_Type = Counter32
_PbxMWIErrors_Object = MibScalar
pbxMWIErrors = _PbxMWIErrors_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 11),
    _PbxMWIErrors_Type()
)
pbxMWIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pbxMWIErrors.setStatus("mandatory")
_CallManagerQueuedMWICommands_Type = Counter32
_CallManagerQueuedMWICommands_Object = MibScalar
callManagerQueuedMWICommands = _CallManagerQueuedMWICommands_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 12),
    _CallManagerQueuedMWICommands_Type()
)
callManagerQueuedMWICommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callManagerQueuedMWICommands.setStatus("mandatory")
_CallManagerCompletedMWICommands_Type = Counter32
_CallManagerCompletedMWICommands_Object = MibScalar
callManagerCompletedMWICommands = _CallManagerCompletedMWICommands_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 13),
    _CallManagerCompletedMWICommands_Type()
)
callManagerCompletedMWICommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callManagerCompletedMWICommands.setStatus("mandatory")
_CallManagerMWIErrors_Type = Counter32
_CallManagerMWIErrors_Object = MibScalar
callManagerMWIErrors = _CallManagerMWIErrors_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 14),
    _CallManagerMWIErrors_Type()
)
callManagerMWIErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callManagerMWIErrors.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1)
)
portEntry.setIndexNames(
    (0, "CALISTA-DPA-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("notInUse", 1),
          ("octel", 2),
          ("pbx", 3),
          ("virtual", 4))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 2),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("mandatory")


class _PortTelephonyLinkState_Type(Integer32):
    """Custom type portTelephonyLinkState based on Integer32"""
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
        *(("down", 2),
          ("notApplicable", 1),
          ("registering", 3),
          ("up", 4))
    )


_PortTelephonyLinkState_Type.__name__ = "Integer32"
_PortTelephonyLinkState_Object = MibTableColumn
portTelephonyLinkState = _PortTelephonyLinkState_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 3),
    _PortTelephonyLinkState_Type()
)
portTelephonyLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTelephonyLinkState.setStatus("mandatory")


class _PortCallManagerLinkState_Type(Integer32):
    """Custom type portCallManagerLinkState based on Integer32"""
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
        *(("down", 2),
          ("notApplicable", 1),
          ("registering", 3),
          ("up", 4))
    )


_PortCallManagerLinkState_Type.__name__ = "Integer32"
_PortCallManagerLinkState_Object = MibTableColumn
portCallManagerLinkState = _PortCallManagerLinkState_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 4),
    _PortCallManagerLinkState_Type()
)
portCallManagerLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCallManagerLinkState.setStatus("mandatory")


class _PortCallState_Type(Integer32):
    """Custom type portCallState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("callIn", 4),
          ("callOut", 5),
          ("hangingUp", 10),
          ("notApplicable", 2),
          ("offHook", 7),
          ("onCall", 6),
          ("onHook", 3),
          ("outCall", 9),
          ("transfer", 8),
          ("unknown", 1))
    )


_PortCallState_Type.__name__ = "Integer32"
_PortCallState_Object = MibTableColumn
portCallState = _PortCallState_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 5),
    _PortCallState_Type()
)
portCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCallState.setStatus("mandatory")
_PortDeviceName_Type = DisplayString
_PortDeviceName_Object = MibTableColumn
portDeviceName = _PortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 6),
    _PortDeviceName_Type()
)
portDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDeviceName.setStatus("mandatory")


class _PortCodecInUse_Type(Integer32):
    """Custom type portCodecInUse based on Integer32"""
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
        *(("g711ALaw", 2),
          ("g711MuLaw", 3),
          ("g723dot1", 4),
          ("g729a", 5),
          ("none", 1))
    )


_PortCodecInUse_Type.__name__ = "Integer32"
_PortCodecInUse_Object = MibTableColumn
portCodecInUse = _PortCodecInUse_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 7),
    _PortCodecInUse_Type()
)
portCodecInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCodecInUse.setStatus("mandatory")
_PortErrors_Type = Integer32
_PortErrors_Object = MibTableColumn
portErrors = _PortErrors_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 8),
    _PortErrors_Type()
)
portErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrors.setStatus("mandatory")
_PortDacLevel_Type = Integer32
_PortDacLevel_Object = MibTableColumn
portDacLevel = _PortDacLevel_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 15, 1, 9),
    _PortDacLevel_Type()
)
portDacLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDacLevel.setStatus("mandatory")
_CallManagerConnectionTable_Object = MibTable
callManagerConnectionTable = _CallManagerConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16)
)
if mibBuilder.loadTexts:
    callManagerConnectionTable.setStatus("mandatory")
_CallManagerConnectionEntry_Object = MibTableRow
callManagerConnectionEntry = _CallManagerConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1)
)
callManagerConnectionEntry.setIndexNames(
    (0, "CALISTA-DPA-MIB", "portIndex"),
    (0, "CALISTA-DPA-MIB", "cmConnectionIndex"),
)
if mibBuilder.loadTexts:
    callManagerConnectionEntry.setStatus("mandatory")
_CmConnectionPortIndex_Type = Integer32
_CmConnectionPortIndex_Object = MibTableColumn
cmConnectionPortIndex = _CmConnectionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 1),
    _CmConnectionPortIndex_Type()
)
cmConnectionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionPortIndex.setStatus("mandatory")
_CmConnectionIndex_Type = Integer32
_CmConnectionIndex_Object = MibTableColumn
cmConnectionIndex = _CmConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 2),
    _CmConnectionIndex_Type()
)
cmConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionIndex.setStatus("mandatory")
_CmConnectionCallManagerName_Type = DisplayString
_CmConnectionCallManagerName_Object = MibTableColumn
cmConnectionCallManagerName = _CmConnectionCallManagerName_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 3),
    _CmConnectionCallManagerName_Type()
)
cmConnectionCallManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionCallManagerName.setStatus("mandatory")
_CmConnectionIpAddress_Type = IpAddress
_CmConnectionIpAddress_Object = MibTableColumn
cmConnectionIpAddress = _CmConnectionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 4),
    _CmConnectionIpAddress_Type()
)
cmConnectionIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionIpAddress.setStatus("mandatory")


class _CmConnectionIpPort_Type(Integer32):
    """Custom type cmConnectionIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmConnectionIpPort_Type.__name__ = "Integer32"
_CmConnectionIpPort_Object = MibTableColumn
cmConnectionIpPort = _CmConnectionIpPort_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 5),
    _CmConnectionIpPort_Type()
)
cmConnectionIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionIpPort.setStatus("mandatory")


class _CmConnectionState_Type(Integer32):
    """Custom type cmConnectionState based on Integer32"""
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
        *(("active", 5),
          ("connectPending", 4),
          ("connecting", 2),
          ("idle", 1),
          ("retryBackOff", 3),
          ("standby", 6))
    )


_CmConnectionState_Type.__name__ = "Integer32"
_CmConnectionState_Object = MibTableColumn
cmConnectionState = _CmConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 7505, 1, 1, 16, 1, 6),
    _CmConnectionState_Type()
)
cmConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmConnectionState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALISTA-DPA-MIB",
    **{"DisplayString": DisplayString,
       "calista": calista,
       "products": products,
       "dpa": dpa,
       "serialNumber": serialNumber,
       "imageVersion": imageVersion,
       "loaderVersion": loaderVersion,
       "integrationMode": integrationMode,
       "pbxType": pbxType,
       "receivedCalls": receivedCalls,
       "outgoingCallsMade": outgoingCallsMade,
       "mwiCommandsReceived": mwiCommandsReceived,
       "pbxQueuedMWICommands": pbxQueuedMWICommands,
       "pbxCompletedMWICommands": pbxCompletedMWICommands,
       "pbxMWIErrors": pbxMWIErrors,
       "callManagerQueuedMWICommands": callManagerQueuedMWICommands,
       "callManagerCompletedMWICommands": callManagerCompletedMWICommands,
       "callManagerMWIErrors": callManagerMWIErrors,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portType": portType,
       "portTelephonyLinkState": portTelephonyLinkState,
       "portCallManagerLinkState": portCallManagerLinkState,
       "portCallState": portCallState,
       "portDeviceName": portDeviceName,
       "portCodecInUse": portCodecInUse,
       "portErrors": portErrors,
       "portDacLevel": portDacLevel,
       "callManagerConnectionTable": callManagerConnectionTable,
       "callManagerConnectionEntry": callManagerConnectionEntry,
       "cmConnectionPortIndex": cmConnectionPortIndex,
       "cmConnectionIndex": cmConnectionIndex,
       "cmConnectionCallManagerName": cmConnectionCallManagerName,
       "cmConnectionIpAddress": cmConnectionIpAddress,
       "cmConnectionIpPort": cmConnectionIpPort,
       "cmConnectionState": cmConnectionState}
)
