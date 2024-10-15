# SNMP MIB module (HP-ICF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:01 2024
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

(rptrAddrTrackLastSourceAddress,
 rptrPortAdminStatus) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrAddrTrackLastSourceAddress",
    "rptrPortAdminStatus")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class TAddress(OctetString):
    """Custom type TAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpSystem_ObjectIdentity = ObjectIdentity
hpSystem = _HpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1)
)
_Bridge1010_ObjectIdentity = ObjectIdentity
bridge1010 = _Bridge1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1)
)
_BridgeRemote_ObjectIdentity = ObjectIdentity
bridgeRemote = _BridgeRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2)
)
_Eswitch_ObjectIdentity = ObjectIdentity
eswitch = _Eswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 3)
)
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2)
)
_IcfRouterER_ObjectIdentity = ObjectIdentity
icfRouterER = _IcfRouterER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 1)
)
_IcfRouterTR_ObjectIdentity = ObjectIdentity
icfRouterTR = _IcfRouterTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 2)
)
_IcfRouterSR_ObjectIdentity = ObjectIdentity
icfRouterSR = _IcfRouterSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 3)
)
_IcfRouterFR_ObjectIdentity = ObjectIdentity
icfRouterFR = _IcfRouterFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 4)
)
_IcfRouterLR_ObjectIdentity = ObjectIdentity
icfRouterLR = _IcfRouterLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 5)
)
_IcfRouterBR_ObjectIdentity = ObjectIdentity
icfRouterBR = _IcfRouterBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 6)
)
_IcfRouterPR_ObjectIdentity = ObjectIdentity
icfRouterPR = _IcfRouterPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 7)
)
_IcfRouter650_ObjectIdentity = ObjectIdentity
icfRouter650 = _IcfRouter650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8)
)
_IcfRouter650Engine_ObjectIdentity = ObjectIdentity
icfRouter650Engine = _IcfRouter650Engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 2)
)
_IcfRouter650Port4E_ObjectIdentity = ObjectIdentity
icfRouter650Port4E = _IcfRouter650Port4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 3)
)
_IcfRouter650Port4S_ObjectIdentity = ObjectIdentity
icfRouter650Port4S = _IcfRouter650Port4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 4)
)
_IcfRouter650Port4T_ObjectIdentity = ObjectIdentity
icfRouter650Port4T = _IcfRouter650Port4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 5)
)
_IcfRouter230_ObjectIdentity = ObjectIdentity
icfRouter230 = _IcfRouter230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 9)
)
_IcfRouter250_ObjectIdentity = ObjectIdentity
icfRouter250 = _IcfRouter250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 10)
)
_IcfRouter255_ObjectIdentity = ObjectIdentity
icfRouter255 = _IcfRouter255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 11)
)
_IcfRouter210_ObjectIdentity = ObjectIdentity
icfRouter210 = _IcfRouter210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 12)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5)
)
_EtherTwist12_ObjectIdentity = ObjectIdentity
etherTwist12 = _EtherTwist12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1)
)
_FiberOptic_ObjectIdentity = ObjectIdentity
fiberOptic = _FiberOptic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3)
)
_EtherTwist48_ObjectIdentity = ObjectIdentity
etherTwist48 = _EtherTwist48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4)
)
_ThinLAN_ObjectIdentity = ObjectIdentity
thinLAN = _ThinLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5)
)
_EtherTwist24S_ObjectIdentity = ObjectIdentity
etherTwist24S = _EtherTwist24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6)
)
_AdvStack12_ObjectIdentity = ObjectIdentity
advStack12 = _AdvStack12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 7)
)
_AdvStack24_ObjectIdentity = ObjectIdentity
advStack24 = _AdvStack24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 8)
)
_AdvStack48_ObjectIdentity = ObjectIdentity
advStack48 = _AdvStack48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 9)
)
_AdvStackVg15_ObjectIdentity = ObjectIdentity
advStackVg15 = _AdvStackVg15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 10)
)
_AdvStackU8_ObjectIdentity = ObjectIdentity
advStackU8 = _AdvStackU8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 11)
)
_AdvStackU16_ObjectIdentity = ObjectIdentity
advStackU16 = _AdvStackU16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8)
)
_RepeaterAgent_ObjectIdentity = ObjectIdentity
repeaterAgent = _RepeaterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1)
)
_ChassisAgents_ObjectIdentity = ObjectIdentity
chassisAgents = _ChassisAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2)
)
_IcfVgAgent_ObjectIdentity = ObjectIdentity
icfVgAgent = _IcfVgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 1)
)
_IcfEnetAgent_ObjectIdentity = ObjectIdentity
icfEnetAgent = _IcfEnetAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 2)
)
_IcfSensors_ObjectIdentity = ObjectIdentity
icfSensors = _IcfSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3)
)
_IcfPowerSupplySensor_ObjectIdentity = ObjectIdentity
icfPowerSupplySensor = _IcfPowerSupplySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 1)
)
_IcfFanSensor_ObjectIdentity = ObjectIdentity
icfFanSensor = _IcfFanSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 2)
)
_IcfTemperatureSensor_ObjectIdentity = ObjectIdentity
icfTemperatureSensor = _IcfTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 3)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_IcfCommon_ObjectIdentity = ObjectIdentity
icfCommon = _IcfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1)
)


class _LastSetError_Type(Integer32):
    """Custom type lastSetError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("adrsAlreadyPresent", 107),
          ("cantDeletePermAdrs", 109),
          ("disallowedLAPBAdrsPair", 106),
          ("disallowedRemoteDevice", 105),
          ("disallowedSTPPortState", 102),
          ("downloadInProgress", 111),
          ("incompleteSetlet", 103),
          ("inconsistentValues", 110),
          ("invalidEventObject", 104),
          ("resourceLimitExceeded", 101),
          ("staticSectionFull", 108),
          ("unexpectedError", 100))
    )


_LastSetError_Type.__name__ = "Integer32"
_LastSetError_Object = MibScalar
lastSetError = _LastSetError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 1),
    _LastSetError_Type()
)
lastSetError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSetError.setStatus("obsolete")


class _Password_Type(OctetString):
    """Custom type password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Password_Type.__name__ = "OctetString"
_Password_Object = MibScalar
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 2),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("obsolete")


class _Reset_Type(Integer32):
    """Custom type reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold", 2),
          ("warm", 1))
    )


_Reset_Type.__name__ = "Integer32"
_Reset_Object = MibScalar
reset = _Reset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 3),
    _Reset_Type()
)
reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset.setStatus("obsolete")
_SelfTest_Type = Integer32
_SelfTest_Object = MibScalar
selfTest = _SelfTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 4),
    _SelfTest_Type()
)
selfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    selfTest.setStatus("obsolete")
_Semaphore_Type = IpAddress
_Semaphore_Object = MibScalar
semaphore = _Semaphore_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 5),
    _Semaphore_Type()
)
semaphore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    semaphore.setStatus("obsolete")
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6)
)
_PollResponse_Type = Integer32
_PollResponse_Object = MibScalar
pollResponse = _PollResponse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 1),
    _PollResponse_Type()
)
pollResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollResponse.setStatus("obsolete")
_AnnounceAddress_Type = MacAddress
_AnnounceAddress_Object = MibScalar
announceAddress = _AnnounceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 2),
    _AnnounceAddress_Type()
)
announceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announceAddress.setStatus("deprecated")


class _MapAddress_Type(OctetString):
    """Custom type mapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MapAddress_Type.__name__ = "OctetString"
_MapAddress_Object = MibScalar
mapAddress = _MapAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 3),
    _MapAddress_Type()
)
mapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapAddress.setStatus("deprecated")
_MapState_Type = Integer32
_MapState_Object = MibScalar
mapState = _MapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 4),
    _MapState_Type()
)
mapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapState.setStatus("deprecated")


class _MapPort_Type(Integer32):
    """Custom type mapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MapPort_Type.__name__ = "Integer32"
_MapPort_Object = MibScalar
mapPort = _MapPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 5),
    _MapPort_Type()
)
mapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapPort.setStatus("deprecated")
_IpSubnetMask_Type = IpAddress
_IpSubnetMask_Object = MibScalar
ipSubnetMask = _IpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 6),
    _IpSubnetMask_Type()
)
ipSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSubnetMask.setStatus("obsolete")
_IcfEvent_ObjectIdentity = ObjectIdentity
icfEvent = _IcfEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7)
)
_EventNotificationNode_ObjectIdentity = ObjectIdentity
eventNotificationNode = _EventNotificationNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 1)
)
_EvtIpNotify_Type = IpAddress
_EvtIpNotify_Object = MibScalar
evtIpNotify = _EvtIpNotify_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 1, 1),
    _EvtIpNotify_Type()
)
evtIpNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtIpNotify.setStatus("obsolete")


class _EvtIpxNotify_Type(OctetString):
    """Custom type evtIpxNotify based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_EvtIpxNotify_Type.__name__ = "OctetString"
_EvtIpxNotify_Object = MibScalar
evtIpxNotify = _EvtIpxNotify_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 1, 2),
    _EvtIpxNotify_Type()
)
evtIpxNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtIpxNotify.setStatus("obsolete")
_EvtTable_Object = MibTable
evtTable = _EvtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 2)
)
if mibBuilder.loadTexts:
    evtTable.setStatus("obsolete")


class _EvtIndex_Type(Integer32):
    """Custom type evtIndex based on Integer32"""
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
        *(("addressMovedEvent", 7),
          ("backupLinkEvent", 5),
          ("coldStartEvent", 2),
          ("intrusionEvent", 6),
          ("newAddressEvent", 8),
          ("rptrHealthEvent", 9),
          ("rptrResetEvent", 10),
          ("spanTreeOrLinkBeatEvent", 3),
          ("temperatureOrSegmentationEvent", 4),
          ("warmStartEvent", 1))
    )


_EvtIndex_Type.__name__ = "Integer32"
_EvtIndex_Object = MibTableColumn
evtIndex = _EvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 2, 1),
    _EvtIndex_Type()
)
evtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtIndex.setStatus("obsolete")
_EvtArm_Type = Integer32
_EvtArm_Object = MibTableColumn
evtArm = _EvtArm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 2, 2),
    _EvtArm_Type()
)
evtArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evtArm.setStatus("obsolete")
_EvtTimeSinceOccurrence_Type = TimeTicks
_EvtTimeSinceOccurrence_Object = MibTableColumn
evtTimeSinceOccurrence = _EvtTimeSinceOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 2, 3),
    _EvtTimeSinceOccurrence_Type()
)
evtTimeSinceOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evtTimeSinceOccurrence.setStatus("obsolete")
_EvtThresholdTable_Object = MibTable
evtThresholdTable = _EvtThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3)
)
if mibBuilder.loadTexts:
    evtThresholdTable.setStatus("obsolete")


class _EvthIndex_Type(Integer32):
    """Custom type evthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EvthIndex_Type.__name__ = "Integer32"
_EvthIndex_Object = MibTableColumn
evthIndex = _EvthIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 1),
    _EvthIndex_Type()
)
evthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evthIndex.setStatus("obsolete")
_EvthArm_Type = Integer32
_EvthArm_Object = MibTableColumn
evthArm = _EvthArm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 2),
    _EvthArm_Type()
)
evthArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evthArm.setStatus("obsolete")
_EvthObject_Type = ObjectIdentifier
_EvthObject_Object = MibTableColumn
evthObject = _EvthObject_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 3),
    _EvthObject_Type()
)
evthObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evthObject.setStatus("obsolete")
_EvthThreshold_Type = Integer32
_EvthThreshold_Object = MibTableColumn
evthThreshold = _EvthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 4),
    _EvthThreshold_Type()
)
evthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evthThreshold.setStatus("obsolete")
_EvthHysteresis_Type = Integer32
_EvthHysteresis_Object = MibTableColumn
evthHysteresis = _EvthHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 5),
    _EvthHysteresis_Type()
)
evthHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evthHysteresis.setStatus("obsolete")
_EvthTimeInterval_Type = TimeTicks
_EvthTimeInterval_Object = MibTableColumn
evthTimeInterval = _EvthTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 6),
    _EvthTimeInterval_Type()
)
evthTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evthTimeInterval.setStatus("obsolete")
_EvthTimeSinceOccurrence_Type = TimeTicks
_EvthTimeSinceOccurrence_Object = MibTableColumn
evthTimeSinceOccurrence = _EvthTimeSinceOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 7, 3, 7),
    _EvthTimeSinceOccurrence_Type()
)
evthTimeSinceOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evthTimeSinceOccurrence.setStatus("obsolete")
_LinkTest_ObjectIdentity = ObjectIdentity
linkTest = _LinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8)
)
_LinkTestAddress_ObjectIdentity = ObjectIdentity
linkTestAddress = _LinkTestAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1)
)


class _LinkTest802MacAddress_Type(OctetString):
    """Custom type linkTest802MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LinkTest802MacAddress_Type.__name__ = "OctetString"
_LinkTest802MacAddress_Object = MibScalar
linkTest802MacAddress = _LinkTest802MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1, 1),
    _LinkTest802MacAddress_Type()
)
linkTest802MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTest802MacAddress.setStatus("deprecated")
_LinkTestIpAddress_Type = IpAddress
_LinkTestIpAddress_Object = MibScalar
linkTestIpAddress = _LinkTestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1, 2),
    _LinkTestIpAddress_Type()
)
linkTestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestIpAddress.setStatus("deprecated")


class _LinkTestIpxAddress_Type(OctetString):
    """Custom type linkTestIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_LinkTestIpxAddress_Type.__name__ = "OctetString"
_LinkTestIpxAddress_Object = MibScalar
linkTestIpxAddress = _LinkTestIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1, 3),
    _LinkTestIpxAddress_Type()
)
linkTestIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestIpxAddress.setStatus("deprecated")


class _LinkTestRepetitions_Type(Integer32):
    """Custom type linkTestRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LinkTestRepetitions_Type.__name__ = "Integer32"
_LinkTestRepetitions_Object = MibScalar
linkTestRepetitions = _LinkTestRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 2),
    _LinkTestRepetitions_Type()
)
linkTestRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestRepetitions.setStatus("deprecated")


class _LinkTestSuccess_Type(Integer32):
    """Custom type linkTestSuccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LinkTestSuccess_Type.__name__ = "Integer32"
_LinkTestSuccess_Object = MibScalar
linkTestSuccess = _LinkTestSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 3),
    _LinkTestSuccess_Type()
)
linkTestSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkTestSuccess.setStatus("deprecated")
_LinkTestTimeout_Type = TimeTicks
_LinkTestTimeout_Object = MibScalar
linkTestTimeout = _LinkTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 4),
    _LinkTestTimeout_Type()
)
linkTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestTimeout.setStatus("deprecated")
_Icf8023MacTable_Object = MibTable
icf8023MacTable = _Icf8023MacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9)
)
if mibBuilder.loadTexts:
    icf8023MacTable.setStatus("obsolete")
_Icf8023MacIndex_Type = Integer32
_Icf8023MacIndex_Object = MibTableColumn
icf8023MacIndex = _Icf8023MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 1),
    _Icf8023MacIndex_Type()
)
icf8023MacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacIndex.setStatus("obsolete")
_Icf8023MacInBroadcastPkts_Type = Counter32
_Icf8023MacInBroadcastPkts_Object = MibTableColumn
icf8023MacInBroadcastPkts = _Icf8023MacInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 2),
    _Icf8023MacInBroadcastPkts_Type()
)
icf8023MacInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacInBroadcastPkts.setStatus("obsolete")
_Icf8023MacOutBroadcastPkts_Type = Counter32
_Icf8023MacOutBroadcastPkts_Object = MibTableColumn
icf8023MacOutBroadcastPkts = _Icf8023MacOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 3),
    _Icf8023MacOutBroadcastPkts_Type()
)
icf8023MacOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacOutBroadcastPkts.setStatus("obsolete")
_Icf8023MacInMulticastPkts_Type = Counter32
_Icf8023MacInMulticastPkts_Object = MibTableColumn
icf8023MacInMulticastPkts = _Icf8023MacInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 4),
    _Icf8023MacInMulticastPkts_Type()
)
icf8023MacInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacInMulticastPkts.setStatus("obsolete")
_Icf8023MacOutMulticastPkts_Type = Counter32
_Icf8023MacOutMulticastPkts_Object = MibTableColumn
icf8023MacOutMulticastPkts = _Icf8023MacOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 5),
    _Icf8023MacOutMulticastPkts_Type()
)
icf8023MacOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacOutMulticastPkts.setStatus("obsolete")
_Icf8023MacRunts_Type = Counter32
_Icf8023MacRunts_Object = MibTableColumn
icf8023MacRunts = _Icf8023MacRunts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 6),
    _Icf8023MacRunts_Type()
)
icf8023MacRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacRunts.setStatus("obsolete")
_Icf8023MacGiants_Type = Counter32
_Icf8023MacGiants_Object = MibTableColumn
icf8023MacGiants = _Icf8023MacGiants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 7),
    _Icf8023MacGiants_Type()
)
icf8023MacGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacGiants.setStatus("obsolete")
_Icf8023MacMissedPktErrors_Type = Counter32
_Icf8023MacMissedPktErrors_Object = MibTableColumn
icf8023MacMissedPktErrors = _Icf8023MacMissedPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 8),
    _Icf8023MacMissedPktErrors_Type()
)
icf8023MacMissedPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacMissedPktErrors.setStatus("obsolete")
_Icf8023MacExcessDeferrals_Type = Counter32
_Icf8023MacExcessDeferrals_Object = MibTableColumn
icf8023MacExcessDeferrals = _Icf8023MacExcessDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 9),
    _Icf8023MacExcessDeferrals_Type()
)
icf8023MacExcessDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacExcessDeferrals.setStatus("obsolete")
_Icf8023MacTotalMediaErrors_Type = Counter32
_Icf8023MacTotalMediaErrors_Object = MibTableColumn
icf8023MacTotalMediaErrors = _Icf8023MacTotalMediaErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 10),
    _Icf8023MacTotalMediaErrors_Type()
)
icf8023MacTotalMediaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacTotalMediaErrors.setStatus("obsolete")
_Icf8023MacSpuriousIntrs_Type = Counter32
_Icf8023MacSpuriousIntrs_Object = MibTableColumn
icf8023MacSpuriousIntrs = _Icf8023MacSpuriousIntrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9, 11),
    _Icf8023MacSpuriousIntrs_Type()
)
icf8023MacSpuriousIntrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icf8023MacSpuriousIntrs.setStatus("obsolete")
_IcfDownload_ObjectIdentity = ObjectIdentity
icfDownload = _IcfDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 10)
)
_IcfDownloadAddress_ObjectIdentity = ObjectIdentity
icfDownloadAddress = _IcfDownloadAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 10, 1)
)
_IcfDownloadIpAddress_Type = IpAddress
_IcfDownloadIpAddress_Object = MibScalar
icfDownloadIpAddress = _IcfDownloadIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 10, 1, 1),
    _IcfDownloadIpAddress_Type()
)
icfDownloadIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfDownloadIpAddress.setStatus("obsolete")


class _IcfDownloadIpxAddress_Type(OctetString):
    """Custom type icfDownloadIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IcfDownloadIpxAddress_Type.__name__ = "OctetString"
_IcfDownloadIpxAddress_Object = MibScalar
icfDownloadIpxAddress = _IcfDownloadIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 10, 1, 2),
    _IcfDownloadIpxAddress_Type()
)
icfDownloadIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfDownloadIpxAddress.setStatus("obsolete")


class _IcfDownloadFilename_Type(DisplayString):
    """Custom type icfDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IcfDownloadFilename_Type.__name__ = "DisplayString"
_IcfDownloadFilename_Object = MibScalar
icfDownloadFilename = _IcfDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 10, 2),
    _IcfDownloadFilename_Type()
)
icfDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfDownloadFilename.setStatus("obsolete")
_IcfHub_ObjectIdentity = ObjectIdentity
icfHub = _IcfHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2)
)
_HubThinlanFault_Type = Integer32
_HubThinlanFault_Object = MibScalar
hubThinlanFault = _HubThinlanFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 1),
    _HubThinlanFault_Type()
)
hubThinlanFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubThinlanFault.setStatus("obsolete")
_HubGlobal_ObjectIdentity = ObjectIdentity
hubGlobal = _HubGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2)
)
_HubGlobalErrors_Type = Counter32
_HubGlobalErrors_Object = MibScalar
hubGlobalErrors = _HubGlobalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 1),
    _HubGlobalErrors_Type()
)
hubGlobalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalErrors.setStatus("obsolete")
_HubGlobalCollisions_Type = Counter32
_HubGlobalCollisions_Object = MibScalar
hubGlobalCollisions = _HubGlobalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 2),
    _HubGlobalCollisions_Type()
)
hubGlobalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalCollisions.setStatus("obsolete")
_HubGlobalPktFragments_Type = Counter32
_HubGlobalPktFragments_Object = MibScalar
hubGlobalPktFragments = _HubGlobalPktFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 3),
    _HubGlobalPktFragments_Type()
)
hubGlobalPktFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalPktFragments.setStatus("obsolete")
_HubGlobalRunts_Type = Counter32
_HubGlobalRunts_Object = MibScalar
hubGlobalRunts = _HubGlobalRunts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 4),
    _HubGlobalRunts_Type()
)
hubGlobalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalRunts.setStatus("obsolete")
_HubGlobalGiants_Type = Counter32
_HubGlobalGiants_Object = MibScalar
hubGlobalGiants = _HubGlobalGiants_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 5),
    _HubGlobalGiants_Type()
)
hubGlobalGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalGiants.setStatus("obsolete")
_HubGlobalCrcErrors_Type = Counter32
_HubGlobalCrcErrors_Object = MibScalar
hubGlobalCrcErrors = _HubGlobalCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 6),
    _HubGlobalCrcErrors_Type()
)
hubGlobalCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalCrcErrors.setStatus("obsolete")
_HubGlobalAlignmentErrors_Type = Counter32
_HubGlobalAlignmentErrors_Object = MibScalar
hubGlobalAlignmentErrors = _HubGlobalAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 7),
    _HubGlobalAlignmentErrors_Type()
)
hubGlobalAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalAlignmentErrors.setStatus("obsolete")
_HubGlobalInOctets_Type = Counter32
_HubGlobalInOctets_Object = MibScalar
hubGlobalInOctets = _HubGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 8),
    _HubGlobalInOctets_Type()
)
hubGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalInOctets.setStatus("obsolete")
_HubGlobalInUcastPkts_Type = Counter32
_HubGlobalInUcastPkts_Object = MibScalar
hubGlobalInUcastPkts = _HubGlobalInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 9),
    _HubGlobalInUcastPkts_Type()
)
hubGlobalInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalInUcastPkts.setStatus("obsolete")
_HubGlobalInNUcastPkts_Type = Counter32
_HubGlobalInNUcastPkts_Object = MibScalar
hubGlobalInNUcastPkts = _HubGlobalInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 10),
    _HubGlobalInNUcastPkts_Type()
)
hubGlobalInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalInNUcastPkts.setStatus("obsolete")
_HubGlobalInBroadcastPkts_Type = Counter32
_HubGlobalInBroadcastPkts_Object = MibScalar
hubGlobalInBroadcastPkts = _HubGlobalInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 2, 11),
    _HubGlobalInBroadcastPkts_Type()
)
hubGlobalInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGlobalInBroadcastPkts.setStatus("obsolete")
_HubPortTable_Object = MibTable
hubPortTable = _HubPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3)
)
if mibBuilder.loadTexts:
    hubPortTable.setStatus("obsolete")


class _HubPortIndex_Type(Integer32):
    """Custom type hubPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubPortIndex_Type.__name__ = "Integer32"
_HubPortIndex_Object = MibTableColumn
hubPortIndex = _HubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 1),
    _HubPortIndex_Type()
)
hubPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortIndex.setStatus("obsolete")
_HubPortPktFragments_Type = Counter32
_HubPortPktFragments_Object = MibTableColumn
hubPortPktFragments = _HubPortPktFragments_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 2),
    _HubPortPktFragments_Type()
)
hubPortPktFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortPktFragments.setStatus("obsolete")
_HubPortCollisions_Type = Counter32
_HubPortCollisions_Object = MibTableColumn
hubPortCollisions = _HubPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 3),
    _HubPortCollisions_Type()
)
hubPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortCollisions.setStatus("obsolete")
_HubPortSegmentation_Type = Integer32
_HubPortSegmentation_Object = MibTableColumn
hubPortSegmentation = _HubPortSegmentation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 4),
    _HubPortSegmentation_Type()
)
hubPortSegmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortSegmentation.setStatus("obsolete")
_HubPortLinkBeatStatus_Type = Integer32
_HubPortLinkBeatStatus_Object = MibTableColumn
hubPortLinkBeatStatus = _HubPortLinkBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 5),
    _HubPortLinkBeatStatus_Type()
)
hubPortLinkBeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortLinkBeatStatus.setStatus("obsolete")
_HubPortLinkBeatEnable_Type = Integer32
_HubPortLinkBeatEnable_Object = MibTableColumn
hubPortLinkBeatEnable = _HubPortLinkBeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 6),
    _HubPortLinkBeatEnable_Type()
)
hubPortLinkBeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubPortLinkBeatEnable.setStatus("obsolete")
_HubPortMacAddress_Type = MacAddress
_HubPortMacAddress_Object = MibTableColumn
hubPortMacAddress = _HubPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 7),
    _HubPortMacAddress_Type()
)
hubPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortMacAddress.setStatus("obsolete")
_HubPortAddressState_Type = Integer32
_HubPortAddressState_Object = MibTableColumn
hubPortAddressState = _HubPortAddressState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 8),
    _HubPortAddressState_Type()
)
hubPortAddressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubPortAddressState.setStatus("obsolete")
_HubPortPolarityReversed_Type = Integer32
_HubPortPolarityReversed_Object = MibTableColumn
hubPortPolarityReversed = _HubPortPolarityReversed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 9),
    _HubPortPolarityReversed_Type()
)
hubPortPolarityReversed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortPolarityReversed.setStatus("obsolete")


class _HubPortLateEventDisable_Type(Integer32):
    """Custom type hubPortLateEventDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HubPortLateEventDisable_Type.__name__ = "Integer32"
_HubPortLateEventDisable_Object = MibTableColumn
hubPortLateEventDisable = _HubPortLateEventDisable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 3, 10),
    _HubPortLateEventDisable_Type()
)
hubPortLateEventDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortLateEventDisable.setStatus("obsolete")
_HubBitmaps_ObjectIdentity = ObjectIdentity
hubBitmaps = _HubBitmaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 4)
)


class _HubPortsOperStatus_Type(OctetString):
    """Custom type hubPortsOperStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HubPortsOperStatus_Type.__name__ = "OctetString"
_HubPortsOperStatus_Object = MibScalar
hubPortsOperStatus = _HubPortsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 4, 1),
    _HubPortsOperStatus_Type()
)
hubPortsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubPortsOperStatus.setStatus("obsolete")
_HubAddressTableMaxAge_Type = TimeTicks
_HubAddressTableMaxAge_Object = MibScalar
hubAddressTableMaxAge = _HubAddressTableMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 5),
    _HubAddressTableMaxAge_Type()
)
hubAddressTableMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAddressTableMaxAge.setStatus("obsolete")
_HubAddressTable_Object = MibTable
hubAddressTable = _HubAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 6)
)
if mibBuilder.loadTexts:
    hubAddressTable.setStatus("deprecated")


class _HubAddressIndex_Type(Integer32):
    """Custom type hubAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_HubAddressIndex_Type.__name__ = "Integer32"
_HubAddressIndex_Object = MibTableColumn
hubAddressIndex = _HubAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 6, 1),
    _HubAddressIndex_Type()
)
hubAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddressIndex.setStatus("obsolete")


class _HubAddressChunk_Type(OctetString):
    """Custom type hubAddressChunk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(408, 408),
    )


_HubAddressChunk_Type.__name__ = "OctetString"
_HubAddressChunk_Object = MibTableColumn
hubAddressChunk = _HubAddressChunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 6, 2),
    _HubAddressChunk_Type()
)
hubAddressChunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddressChunk.setStatus("obsolete")
_HubNumBkpLinks_Type = Integer32
_HubNumBkpLinks_Object = MibScalar
hubNumBkpLinks = _HubNumBkpLinks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 7),
    _HubNumBkpLinks_Type()
)
hubNumBkpLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubNumBkpLinks.setStatus("obsolete")
_HubBkpLinkTable_Object = MibTable
hubBkpLinkTable = _HubBkpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8)
)
if mibBuilder.loadTexts:
    hubBkpLinkTable.setStatus("obsolete")
_HubBkpLinkIndex_Type = Integer32
_HubBkpLinkIndex_Object = MibTableColumn
hubBkpLinkIndex = _HubBkpLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 1),
    _HubBkpLinkIndex_Type()
)
hubBkpLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubBkpLinkIndex.setStatus("obsolete")


class _HubBackupPort_Type(Integer32):
    """Custom type hubBackupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubBackupPort_Type.__name__ = "Integer32"
_HubBackupPort_Object = MibTableColumn
hubBackupPort = _HubBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 2),
    _HubBackupPort_Type()
)
hubBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubBackupPort.setStatus("obsolete")


class _HubPrimaryPort_Type(Integer32):
    """Custom type hubPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubPrimaryPort_Type.__name__ = "Integer32"
_HubPrimaryPort_Object = MibTableColumn
hubPrimaryPort = _HubPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 3),
    _HubPrimaryPort_Type()
)
hubPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubPrimaryPort.setStatus("obsolete")


class _HubBackupAddress_Type(OctetString):
    """Custom type hubBackupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubBackupAddress_Type.__name__ = "OctetString"
_HubBackupAddress_Object = MibTableColumn
hubBackupAddress = _HubBackupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 4),
    _HubBackupAddress_Type()
)
hubBackupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubBackupAddress.setStatus("obsolete")
_HubBackupTestTime_Type = TimeTicks
_HubBackupTestTime_Object = MibTableColumn
hubBackupTestTime = _HubBackupTestTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 5),
    _HubBackupTestTime_Type()
)
hubBackupTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubBackupTestTime.setStatus("obsolete")


class _HubBackupConsecutiveFails_Type(Integer32):
    """Custom type hubBackupConsecutiveFails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HubBackupConsecutiveFails_Type.__name__ = "Integer32"
_HubBackupConsecutiveFails_Object = MibTableColumn
hubBackupConsecutiveFails = _HubBackupConsecutiveFails_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 8, 6),
    _HubBackupConsecutiveFails_Type()
)
hubBackupConsecutiveFails.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubBackupConsecutiveFails.setStatus("obsolete")
_HubSqeEnabled_Type = Integer32
_HubSqeEnabled_Object = MibScalar
hubSqeEnabled = _HubSqeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 9),
    _HubSqeEnabled_Type()
)
hubSqeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSqeEnabled.setStatus("obsolete")
_HubSecurity_ObjectIdentity = ObjectIdentity
hubSecurity = _HubSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10)
)
_HubSecurePortTable_Object = MibTable
hubSecurePortTable = _HubSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1)
)
if mibBuilder.loadTexts:
    hubSecurePortTable.setStatus("mandatory")
_HubSecurePortEntry_Object = MibTableRow
hubSecurePortEntry = _HubSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1)
)
hubSecurePortEntry.setIndexNames(
    (0, "HP-ICF", "hubSecPtGroupIndex"),
    (0, "HP-ICF", "hubSecPtPortIndex"),
)
if mibBuilder.loadTexts:
    hubSecurePortEntry.setStatus("mandatory")


class _HubSecPtGroupIndex_Type(Integer32):
    """Custom type hubSecPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubSecPtGroupIndex_Type.__name__ = "Integer32"
_HubSecPtGroupIndex_Object = MibTableColumn
hubSecPtGroupIndex = _HubSecPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 1),
    _HubSecPtGroupIndex_Type()
)
hubSecPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtGroupIndex.setStatus("mandatory")


class _HubSecPtPortIndex_Type(Integer32):
    """Custom type hubSecPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubSecPtPortIndex_Type.__name__ = "Integer32"
_HubSecPtPortIndex_Object = MibTableColumn
hubSecPtPortIndex = _HubSecPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 2),
    _HubSecPtPortIndex_Type()
)
hubSecPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtPortIndex.setStatus("mandatory")


class _HubSecPtSecurityAddress_Type(OctetString):
    """Custom type hubSecPtSecurityAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubSecPtSecurityAddress_Type.__name__ = "OctetString"
_HubSecPtSecurityAddress_Object = MibTableColumn
hubSecPtSecurityAddress = _HubSecPtSecurityAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 3),
    _HubSecPtSecurityAddress_Type()
)
hubSecPtSecurityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtSecurityAddress.setStatus("mandatory")


class _HubSecPtAuthorizedAddress_Type(OctetString):
    """Custom type hubSecPtAuthorizedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubSecPtAuthorizedAddress_Type.__name__ = "OctetString"
_HubSecPtAuthorizedAddress_Object = MibTableColumn
hubSecPtAuthorizedAddress = _HubSecPtAuthorizedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 4),
    _HubSecPtAuthorizedAddress_Type()
)
hubSecPtAuthorizedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtAuthorizedAddress.setStatus("mandatory")


class _HubSecPtPreventEavesdrop_Type(Integer32):
    """Custom type hubSecPtPreventEavesdrop based on Integer32"""
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


_HubSecPtPreventEavesdrop_Type.__name__ = "Integer32"
_HubSecPtPreventEavesdrop_Object = MibTableColumn
hubSecPtPreventEavesdrop = _HubSecPtPreventEavesdrop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 5),
    _HubSecPtPreventEavesdrop_Type()
)
hubSecPtPreventEavesdrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtPreventEavesdrop.setStatus("mandatory")


class _HubSecPtAlarmEnable_Type(Integer32):
    """Custom type hubSecPtAlarmEnable based on Integer32"""
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


_HubSecPtAlarmEnable_Type.__name__ = "Integer32"
_HubSecPtAlarmEnable_Object = MibTableColumn
hubSecPtAlarmEnable = _HubSecPtAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 6),
    _HubSecPtAlarmEnable_Type()
)
hubSecPtAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtAlarmEnable.setStatus("mandatory")


class _HubSecPtIntrusionFlag_Type(Integer32):
    """Custom type hubSecPtIntrusionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusion", 1),
          ("noIntrusion", 2))
    )


_HubSecPtIntrusionFlag_Type.__name__ = "Integer32"
_HubSecPtIntrusionFlag_Object = MibTableColumn
hubSecPtIntrusionFlag = _HubSecPtIntrusionFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 7),
    _HubSecPtIntrusionFlag_Type()
)
hubSecPtIntrusionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtIntrusionFlag.setStatus("mandatory")
_HubIntruderLogTable_Object = MibTable
hubIntruderLogTable = _HubIntruderLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hubIntruderLogTable.setStatus("mandatory")
_HubIntruderLogEntry_Object = MibTableRow
hubIntruderLogEntry = _HubIntruderLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1)
)
hubIntruderLogEntry.setIndexNames(
    (0, "HP-ICF", "hubIntruderIndex"),
)
if mibBuilder.loadTexts:
    hubIntruderLogEntry.setStatus("mandatory")


class _HubIntruderIndex_Type(Integer32):
    """Custom type hubIntruderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HubIntruderIndex_Type.__name__ = "Integer32"
_HubIntruderIndex_Object = MibTableColumn
hubIntruderIndex = _HubIntruderIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 1),
    _HubIntruderIndex_Type()
)
hubIntruderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderIndex.setStatus("mandatory")


class _HubIntruderGroup_Type(Integer32):
    """Custom type hubIntruderGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubIntruderGroup_Type.__name__ = "Integer32"
_HubIntruderGroup_Object = MibTableColumn
hubIntruderGroup = _HubIntruderGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 2),
    _HubIntruderGroup_Type()
)
hubIntruderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderGroup.setStatus("mandatory")


class _HubIntruderPort_Type(Integer32):
    """Custom type hubIntruderPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubIntruderPort_Type.__name__ = "Integer32"
_HubIntruderPort_Object = MibTableColumn
hubIntruderPort = _HubIntruderPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 3),
    _HubIntruderPort_Type()
)
hubIntruderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderPort.setStatus("mandatory")


class _HubIntruderAddress_Type(OctetString):
    """Custom type hubIntruderAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubIntruderAddress_Type.__name__ = "OctetString"
_HubIntruderAddress_Object = MibTableColumn
hubIntruderAddress = _HubIntruderAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 4),
    _HubIntruderAddress_Type()
)
hubIntruderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderAddress.setStatus("mandatory")
_HubIntruderTime_Type = TimeTicks
_HubIntruderTime_Object = MibTableColumn
hubIntruderTime = _HubIntruderTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 5),
    _HubIntruderTime_Type()
)
hubIntruderTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderTime.setStatus("mandatory")
_HubAddressMoveLogTable_Object = MibTable
hubAddressMoveLogTable = _HubAddressMoveLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11)
)
if mibBuilder.loadTexts:
    hubAddressMoveLogTable.setStatus("mandatory")
_HubAddressMoveLogEntry_Object = MibTableRow
hubAddressMoveLogEntry = _HubAddressMoveLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1)
)
hubAddressMoveLogEntry.setIndexNames(
    (0, "HP-ICF", "hubAddrMoveIndex"),
)
if mibBuilder.loadTexts:
    hubAddressMoveLogEntry.setStatus("mandatory")


class _HubAddrMoveIndex_Type(Integer32):
    """Custom type hubAddrMoveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HubAddrMoveIndex_Type.__name__ = "Integer32"
_HubAddrMoveIndex_Object = MibTableColumn
hubAddrMoveIndex = _HubAddrMoveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 1),
    _HubAddrMoveIndex_Type()
)
hubAddrMoveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveIndex.setStatus("mandatory")


class _HubAddrMoveAddress_Type(OctetString):
    """Custom type hubAddrMoveAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HubAddrMoveAddress_Type.__name__ = "OctetString"
_HubAddrMoveAddress_Object = MibTableColumn
hubAddrMoveAddress = _HubAddrMoveAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 2),
    _HubAddrMoveAddress_Type()
)
hubAddrMoveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveAddress.setStatus("mandatory")


class _HubAddrMoveOldGroup_Type(Integer32):
    """Custom type hubAddrMoveOldGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubAddrMoveOldGroup_Type.__name__ = "Integer32"
_HubAddrMoveOldGroup_Object = MibTableColumn
hubAddrMoveOldGroup = _HubAddrMoveOldGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 3),
    _HubAddrMoveOldGroup_Type()
)
hubAddrMoveOldGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveOldGroup.setStatus("mandatory")


class _HubAddrMoveOldPort_Type(Integer32):
    """Custom type hubAddrMoveOldPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubAddrMoveOldPort_Type.__name__ = "Integer32"
_HubAddrMoveOldPort_Object = MibTableColumn
hubAddrMoveOldPort = _HubAddrMoveOldPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 4),
    _HubAddrMoveOldPort_Type()
)
hubAddrMoveOldPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveOldPort.setStatus("mandatory")


class _HubAddrMoveNewGroup_Type(Integer32):
    """Custom type hubAddrMoveNewGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubAddrMoveNewGroup_Type.__name__ = "Integer32"
_HubAddrMoveNewGroup_Object = MibTableColumn
hubAddrMoveNewGroup = _HubAddrMoveNewGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 5),
    _HubAddrMoveNewGroup_Type()
)
hubAddrMoveNewGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveNewGroup.setStatus("mandatory")


class _HubAddrMoveNewPort_Type(Integer32):
    """Custom type hubAddrMoveNewPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_HubAddrMoveNewPort_Type.__name__ = "Integer32"
_HubAddrMoveNewPort_Object = MibTableColumn
hubAddrMoveNewPort = _HubAddrMoveNewPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 6),
    _HubAddrMoveNewPort_Type()
)
hubAddrMoveNewPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveNewPort.setStatus("mandatory")


class _HubLateEventMonitor_Type(Integer32):
    """Custom type hubLateEventMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onAll", 3),
          ("onSingle", 2))
    )


_HubLateEventMonitor_Type.__name__ = "Integer32"
_HubLateEventMonitor_Object = MibScalar
hubLateEventMonitor = _HubLateEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 12),
    _HubLateEventMonitor_Type()
)
hubLateEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubLateEventMonitor.setStatus("mandatory")
_IcfBridge_ObjectIdentity = ObjectIdentity
icfBridge = _IcfBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3)
)
_OperationalState_Type = Integer32
_OperationalState_Object = MibScalar
operationalState = _OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 1),
    _OperationalState_Type()
)
operationalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operationalState.setStatus("obsolete")
_ForwardDbMaxAge_Type = TimeTicks
_ForwardDbMaxAge_Object = MibScalar
forwardDbMaxAge = _ForwardDbMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 2),
    _ForwardDbMaxAge_Type()
)
forwardDbMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forwardDbMaxAge.setStatus("obsolete")
_AddressTable_Object = MibTable
addressTable = _AddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 3)
)
if mibBuilder.loadTexts:
    addressTable.setStatus("obsolete")
_AddressIndex_Type = Integer32
_AddressIndex_Object = MibTableColumn
addressIndex = _AddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 3, 1),
    _AddressIndex_Type()
)
addressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addressIndex.setStatus("obsolete")


class _AddressChunk_Type(OctetString):
    """Custom type addressChunk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(410, 410),
    )


_AddressChunk_Type.__name__ = "OctetString"
_AddressChunk_Object = MibTableColumn
addressChunk = _AddressChunk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 3, 2),
    _AddressChunk_Type()
)
addressChunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    addressChunk.setStatus("obsolete")
_BrgPortTable_Object = MibTable
brgPortTable = _BrgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4)
)
if mibBuilder.loadTexts:
    brgPortTable.setStatus("obsolete")
_BrgPortIndex_Type = Integer32
_BrgPortIndex_Object = MibTableColumn
brgPortIndex = _BrgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4, 1),
    _BrgPortIndex_Type()
)
brgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPortIndex.setStatus("obsolete")
_BrgPortCacheHits_Type = Counter32
_BrgPortCacheHits_Object = MibTableColumn
brgPortCacheHits = _BrgPortCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4, 2),
    _BrgPortCacheHits_Type()
)
brgPortCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPortCacheHits.setStatus("obsolete")
_BrgPortCacheMisses_Type = Counter32
_BrgPortCacheMisses_Object = MibTableColumn
brgPortCacheMisses = _BrgPortCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4, 3),
    _BrgPortCacheMisses_Type()
)
brgPortCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPortCacheMisses.setStatus("obsolete")
_BrgPortForwardedPkts_Type = Counter32
_BrgPortForwardedPkts_Object = MibTableColumn
brgPortForwardedPkts = _BrgPortForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4, 4),
    _BrgPortForwardedPkts_Type()
)
brgPortForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPortForwardedPkts.setStatus("obsolete")
_BrgPortFilteredPkts_Type = Counter32
_BrgPortFilteredPkts_Object = MibTableColumn
brgPortFilteredPkts = _BrgPortFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 4, 5),
    _BrgPortFilteredPkts_Type()
)
brgPortFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brgPortFilteredPkts.setStatus("obsolete")
_WildcardTable_Object = MibTable
wildcardTable = _WildcardTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5)
)
if mibBuilder.loadTexts:
    wildcardTable.setStatus("obsolete")
_WildcardIndex_Type = Integer32
_WildcardIndex_Object = MibTableColumn
wildcardIndex = _WildcardIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 1),
    _WildcardIndex_Type()
)
wildcardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wildcardIndex.setStatus("obsolete")


class _WildcardFilter_Type(OctetString):
    """Custom type wildcardFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WildcardFilter_Type.__name__ = "OctetString"
_WildcardFilter_Object = MibTableColumn
wildcardFilter = _WildcardFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 2),
    _WildcardFilter_Type()
)
wildcardFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wildcardFilter.setStatus("obsolete")


class _WildcardMask_Type(OctetString):
    """Custom type wildcardMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WildcardMask_Type.__name__ = "OctetString"
_WildcardMask_Object = MibTableColumn
wildcardMask = _WildcardMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 3),
    _WildcardMask_Type()
)
wildcardMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wildcardMask.setStatus("obsolete")
_WildcardOffset_Type = Integer32
_WildcardOffset_Object = MibTableColumn
wildcardOffset = _WildcardOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 4),
    _WildcardOffset_Type()
)
wildcardOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wildcardOffset.setStatus("obsolete")
_WildcardUserOffset_Type = Integer32
_WildcardUserOffset_Object = MibTableColumn
wildcardUserOffset = _WildcardUserOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 5),
    _WildcardUserOffset_Type()
)
wildcardUserOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wildcardUserOffset.setStatus("obsolete")
_WildcardArm_Type = Integer32
_WildcardArm_Object = MibTableColumn
wildcardArm = _WildcardArm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 5, 6),
    _WildcardArm_Type()
)
wildcardArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wildcardArm.setStatus("obsolete")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6)
)


class _StpBridgeId_Type(OctetString):
    """Custom type stpBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StpBridgeId_Type.__name__ = "OctetString"
_StpBridgeId_Object = MibScalar
stpBridgeId = _StpBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 1),
    _StpBridgeId_Type()
)
stpBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpBridgeId.setStatus("obsolete")
_StpTopoChangeTime_Type = TimeTicks
_StpTopoChangeTime_Object = MibScalar
stpTopoChangeTime = _StpTopoChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 2),
    _StpTopoChangeTime_Type()
)
stpTopoChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopoChangeTime.setStatus("obsolete")
_StpTopoNumChanges_Type = Counter32
_StpTopoNumChanges_Object = MibScalar
stpTopoNumChanges = _StpTopoNumChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 3),
    _StpTopoNumChanges_Type()
)
stpTopoNumChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopoNumChanges.setStatus("obsolete")
_StpTopoChange_Type = Integer32
_StpTopoChange_Object = MibScalar
stpTopoChange = _StpTopoChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 4),
    _StpTopoChange_Type()
)
stpTopoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpTopoChange.setStatus("obsolete")


class _StpDesignatedRoot_Type(OctetString):
    """Custom type stpDesignatedRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_StpDesignatedRoot_Type.__name__ = "OctetString"
_StpDesignatedRoot_Object = MibScalar
stpDesignatedRoot = _StpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 5),
    _StpDesignatedRoot_Type()
)
stpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpDesignatedRoot.setStatus("obsolete")


class _StpRootCost_Type(Integer32):
    """Custom type stpRootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_StpRootCost_Type.__name__ = "Integer32"
_StpRootCost_Object = MibScalar
stpRootCost = _StpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 6),
    _StpRootCost_Type()
)
stpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootCost.setStatus("obsolete")


class _StpRootPort_Type(Integer32):
    """Custom type stpRootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpRootPort_Type.__name__ = "Integer32"
_StpRootPort_Object = MibScalar
stpRootPort = _StpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 7),
    _StpRootPort_Type()
)
stpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRootPort.setStatus("obsolete")


class _StpCurrentMaxAge_Type(Integer32):
    """Custom type stpCurrentMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpCurrentMaxAge_Type.__name__ = "Integer32"
_StpCurrentMaxAge_Object = MibScalar
stpCurrentMaxAge = _StpCurrentMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 8),
    _StpCurrentMaxAge_Type()
)
stpCurrentMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpCurrentMaxAge.setStatus("obsolete")


class _StpCurrentHelloTime_Type(Integer32):
    """Custom type stpCurrentHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpCurrentHelloTime_Type.__name__ = "Integer32"
_StpCurrentHelloTime_Object = MibScalar
stpCurrentHelloTime = _StpCurrentHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 9),
    _StpCurrentHelloTime_Type()
)
stpCurrentHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpCurrentHelloTime.setStatus("obsolete")


class _StpCurrentForwardDelay_Type(Integer32):
    """Custom type stpCurrentForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_StpCurrentForwardDelay_Type.__name__ = "Integer32"
_StpCurrentForwardDelay_Object = MibScalar
stpCurrentForwardDelay = _StpCurrentForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 10),
    _StpCurrentForwardDelay_Type()
)
stpCurrentForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpCurrentForwardDelay.setStatus("obsolete")


class _StpMaxAge_Type(Integer32):
    """Custom type stpMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpMaxAge_Type.__name__ = "Integer32"
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 11),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("obsolete")


class _StpHelloTime_Type(Integer32):
    """Custom type stpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpHelloTime_Type.__name__ = "Integer32"
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 12),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("obsolete")


class _StpForwardDelay_Type(Integer32):
    """Custom type stpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpForwardDelay_Type.__name__ = "Integer32"
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 13),
    _StpForwardDelay_Type()
)
stpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpForwardDelay.setStatus("obsolete")
_StpPriority_Type = Integer32
_StpPriority_Object = MibScalar
stpPriority = _StpPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 14),
    _StpPriority_Type()
)
stpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPriority.setStatus("obsolete")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("obsolete")
_StpPortIndex_Type = Integer32
_StpPortIndex_Object = MibTableColumn
stpPortIndex = _StpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 1),
    _StpPortIndex_Type()
)
stpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortIndex.setStatus("obsolete")
_StpPortState_Type = Integer32
_StpPortState_Object = MibTableColumn
stpPortState = _StpPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 2),
    _StpPortState_Type()
)
stpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortState.setStatus("obsolete")
_StpPortId_Type = Integer32
_StpPortId_Object = MibTableColumn
stpPortId = _StpPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 3),
    _StpPortId_Type()
)
stpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortId.setStatus("obsolete")


class _StpPortPathCost_Type(Integer32):
    """Custom type stpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPortPathCost_Type.__name__ = "Integer32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 4),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("obsolete")


class _StpPortRootId_Type(OctetString):
    """Custom type stpPortRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StpPortRootId_Type.__name__ = "OctetString"
_StpPortRootId_Object = MibTableColumn
stpPortRootId = _StpPortRootId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 5),
    _StpPortRootId_Type()
)
stpPortRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortRootId.setStatus("obsolete")


class _StpPortDesignatedCost_Type(Integer32):
    """Custom type stpPortDesignatedCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpPortDesignatedCost_Type.__name__ = "Integer32"
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 6),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("obsolete")


class _StpPortDesignatedBridge_Type(OctetString):
    """Custom type stpPortDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StpPortDesignatedBridge_Type.__name__ = "OctetString"
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 7),
    _StpPortDesignatedBridge_Type()
)
stpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridge.setStatus("obsolete")


class _StpPortDesignatedPort_Type(Integer32):
    """Custom type stpPortDesignatedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StpPortDesignatedPort_Type.__name__ = "Integer32"
_StpPortDesignatedPort_Object = MibTableColumn
stpPortDesignatedPort = _StpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 8),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("obsolete")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 6, 15, 9),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("obsolete")
_HdlcErrorTable_Object = MibTable
hdlcErrorTable = _HdlcErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7)
)
if mibBuilder.loadTexts:
    hdlcErrorTable.setStatus("obsolete")
_HdlcErrorIndex_Type = Integer32
_HdlcErrorIndex_Object = MibTableColumn
hdlcErrorIndex = _HdlcErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 1),
    _HdlcErrorIndex_Type()
)
hdlcErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcErrorIndex.setStatus("obsolete")
_HdlcErrorIndications_Type = Counter32
_HdlcErrorIndications_Object = MibTableColumn
hdlcErrorIndications = _HdlcErrorIndications_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 2),
    _HdlcErrorIndications_Type()
)
hdlcErrorIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcErrorIndications.setStatus("obsolete")
_HdlcT1Timeouts_Type = Counter32
_HdlcT1Timeouts_Object = MibTableColumn
hdlcT1Timeouts = _HdlcT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 3),
    _HdlcT1Timeouts_Type()
)
hdlcT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcT1Timeouts.setStatus("obsolete")
_HdlcMissedPackets_Type = Counter32
_HdlcMissedPackets_Object = MibTableColumn
hdlcMissedPackets = _HdlcMissedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 4),
    _HdlcMissedPackets_Type()
)
hdlcMissedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcMissedPackets.setStatus("obsolete")
_HdlcRcvOverruns_Type = Counter32
_HdlcRcvOverruns_Object = MibTableColumn
hdlcRcvOverruns = _HdlcRcvOverruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 5),
    _HdlcRcvOverruns_Type()
)
hdlcRcvOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRcvOverruns.setStatus("obsolete")
_HdlcXmtUnderruns_Type = Counter32
_HdlcXmtUnderruns_Object = MibTableColumn
hdlcXmtUnderruns = _HdlcXmtUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 6),
    _HdlcXmtUnderruns_Type()
)
hdlcXmtUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcXmtUnderruns.setStatus("obsolete")
_HdlcProviderLostPrimitives_Type = Counter32
_HdlcProviderLostPrimitives_Object = MibTableColumn
hdlcProviderLostPrimitives = _HdlcProviderLostPrimitives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 7),
    _HdlcProviderLostPrimitives_Type()
)
hdlcProviderLostPrimitives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcProviderLostPrimitives.setStatus("obsolete")
_HdlcRuntFrameReceives_Type = Counter32
_HdlcRuntFrameReceives_Object = MibTableColumn
hdlcRuntFrameReceives = _HdlcRuntFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 8),
    _HdlcRuntFrameReceives_Type()
)
hdlcRuntFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRuntFrameReceives.setStatus("obsolete")
_HdlcGiantFrameReceives_Type = Counter32
_HdlcGiantFrameReceives_Object = MibTableColumn
hdlcGiantFrameReceives = _HdlcGiantFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 9),
    _HdlcGiantFrameReceives_Type()
)
hdlcGiantFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcGiantFrameReceives.setStatus("obsolete")
_HdlcBadFrameReceives_Type = Counter32
_HdlcBadFrameReceives_Object = MibTableColumn
hdlcBadFrameReceives = _HdlcBadFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 10),
    _HdlcBadFrameReceives_Type()
)
hdlcBadFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcBadFrameReceives.setStatus("obsolete")
_HdlcRejectFrameReceives_Type = Counter32
_HdlcRejectFrameReceives_Object = MibTableColumn
hdlcRejectFrameReceives = _HdlcRejectFrameReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 11),
    _HdlcRejectFrameReceives_Type()
)
hdlcRejectFrameReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRejectFrameReceives.setStatus("obsolete")
_HdlcRejectFrameSends_Type = Counter32
_HdlcRejectFrameSends_Object = MibTableColumn
hdlcRejectFrameSends = _HdlcRejectFrameSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 12),
    _HdlcRejectFrameSends_Type()
)
hdlcRejectFrameSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRejectFrameSends.setStatus("obsolete")
_HdlcFrameRejectFrameRecs_Type = Counter32
_HdlcFrameRejectFrameRecs_Object = MibTableColumn
hdlcFrameRejectFrameRecs = _HdlcFrameRejectFrameRecs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 7, 13),
    _HdlcFrameRejectFrameRecs_Type()
)
hdlcFrameRejectFrameRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcFrameRejectFrameRecs.setStatus("obsolete")
_HdlcLocalTable_Object = MibTable
hdlcLocalTable = _HdlcLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8)
)
if mibBuilder.loadTexts:
    hdlcLocalTable.setStatus("obsolete")
_HdlcLocalIndex_Type = Integer32
_HdlcLocalIndex_Object = MibTableColumn
hdlcLocalIndex = _HdlcLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 1),
    _HdlcLocalIndex_Type()
)
hdlcLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalIndex.setStatus("obsolete")
_HdlcLocalResetRequests_Type = Counter32
_HdlcLocalResetRequests_Object = MibTableColumn
hdlcLocalResetRequests = _HdlcLocalResetRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 2),
    _HdlcLocalResetRequests_Type()
)
hdlcLocalResetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalResetRequests.setStatus("obsolete")
_HdlcLocalResetConfirms_Type = Counter32
_HdlcLocalResetConfirms_Object = MibTableColumn
hdlcLocalResetConfirms = _HdlcLocalResetConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 3),
    _HdlcLocalResetConfirms_Type()
)
hdlcLocalResetConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalResetConfirms.setStatus("obsolete")
_HdlcLocalConnectRequests_Type = Counter32
_HdlcLocalConnectRequests_Object = MibTableColumn
hdlcLocalConnectRequests = _HdlcLocalConnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 4),
    _HdlcLocalConnectRequests_Type()
)
hdlcLocalConnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalConnectRequests.setStatus("obsolete")
_HdlcLocalConnectConfirms_Type = Counter32
_HdlcLocalConnectConfirms_Object = MibTableColumn
hdlcLocalConnectConfirms = _HdlcLocalConnectConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 5),
    _HdlcLocalConnectConfirms_Type()
)
hdlcLocalConnectConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalConnectConfirms.setStatus("obsolete")
_HdlcLocalDisconnectRequests_Type = Counter32
_HdlcLocalDisconnectRequests_Object = MibTableColumn
hdlcLocalDisconnectRequests = _HdlcLocalDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 6),
    _HdlcLocalDisconnectRequests_Type()
)
hdlcLocalDisconnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalDisconnectRequests.setStatus("obsolete")
_HdlcLocalDisconnectConfirms_Type = Counter32
_HdlcLocalDisconnectConfirms_Object = MibTableColumn
hdlcLocalDisconnectConfirms = _HdlcLocalDisconnectConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 7),
    _HdlcLocalDisconnectConfirms_Type()
)
hdlcLocalDisconnectConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalDisconnectConfirms.setStatus("obsolete")
_HdlcLocalState_Type = Integer32
_HdlcLocalState_Object = MibTableColumn
hdlcLocalState = _HdlcLocalState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 8),
    _HdlcLocalState_Type()
)
hdlcLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalState.setStatus("obsolete")


class _HdlcLocalAddress_Type(Integer32):
    """Custom type hdlcLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlcDCEAddress", 3),
          ("hdlcDTEAddress", 1))
    )


_HdlcLocalAddress_Type.__name__ = "Integer32"
_HdlcLocalAddress_Object = MibTableColumn
hdlcLocalAddress = _HdlcLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 9),
    _HdlcLocalAddress_Type()
)
hdlcLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcLocalAddress.setStatus("obsolete")
_HdlcLocalPhase_Type = Integer32
_HdlcLocalPhase_Object = MibTableColumn
hdlcLocalPhase = _HdlcLocalPhase_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 8, 10),
    _HdlcLocalPhase_Type()
)
hdlcLocalPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcLocalPhase.setStatus("obsolete")
_HdlcRemoteTable_Object = MibTable
hdlcRemoteTable = _HdlcRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9)
)
if mibBuilder.loadTexts:
    hdlcRemoteTable.setStatus("obsolete")
_HdlcRemoteIndex_Type = Integer32
_HdlcRemoteIndex_Object = MibTableColumn
hdlcRemoteIndex = _HdlcRemoteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 1),
    _HdlcRemoteIndex_Type()
)
hdlcRemoteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteIndex.setStatus("obsolete")
_HdlcRemoteResetRequests_Type = Counter32
_HdlcRemoteResetRequests_Object = MibTableColumn
hdlcRemoteResetRequests = _HdlcRemoteResetRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 2),
    _HdlcRemoteResetRequests_Type()
)
hdlcRemoteResetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteResetRequests.setStatus("obsolete")
_HdlcRemoteResetConfirms_Type = Counter32
_HdlcRemoteResetConfirms_Object = MibTableColumn
hdlcRemoteResetConfirms = _HdlcRemoteResetConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 3),
    _HdlcRemoteResetConfirms_Type()
)
hdlcRemoteResetConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteResetConfirms.setStatus("obsolete")
_HdlcRemoteConnectRequests_Type = Counter32
_HdlcRemoteConnectRequests_Object = MibTableColumn
hdlcRemoteConnectRequests = _HdlcRemoteConnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 4),
    _HdlcRemoteConnectRequests_Type()
)
hdlcRemoteConnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteConnectRequests.setStatus("obsolete")
_HdlcRemoteConnectConfirms_Type = Counter32
_HdlcRemoteConnectConfirms_Object = MibTableColumn
hdlcRemoteConnectConfirms = _HdlcRemoteConnectConfirms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 5),
    _HdlcRemoteConnectConfirms_Type()
)
hdlcRemoteConnectConfirms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteConnectConfirms.setStatus("obsolete")
_HdlcRemoteDisconnectRequests_Type = Counter32
_HdlcRemoteDisconnectRequests_Object = MibTableColumn
hdlcRemoteDisconnectRequests = _HdlcRemoteDisconnectRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 6),
    _HdlcRemoteDisconnectRequests_Type()
)
hdlcRemoteDisconnectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteDisconnectRequests.setStatus("obsolete")
_HdlcRemoteState_Type = Integer32
_HdlcRemoteState_Object = MibTableColumn
hdlcRemoteState = _HdlcRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 7),
    _HdlcRemoteState_Type()
)
hdlcRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteState.setStatus("obsolete")


class _HdlcRemoteAddress_Type(Integer32):
    """Custom type hdlcRemoteAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlcDCEAddress", 3),
          ("hdlcDTEAddress", 1))
    )


_HdlcRemoteAddress_Type.__name__ = "Integer32"
_HdlcRemoteAddress_Object = MibTableColumn
hdlcRemoteAddress = _HdlcRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 8),
    _HdlcRemoteAddress_Type()
)
hdlcRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcRemoteAddress.setStatus("obsolete")
_HdlcRemoteXidCommands_Type = Counter32
_HdlcRemoteXidCommands_Object = MibTableColumn
hdlcRemoteXidCommands = _HdlcRemoteXidCommands_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 9),
    _HdlcRemoteXidCommands_Type()
)
hdlcRemoteXidCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteXidCommands.setStatus("obsolete")
_HdlcRemoteXidResponses_Type = Counter32
_HdlcRemoteXidResponses_Object = MibTableColumn
hdlcRemoteXidResponses = _HdlcRemoteXidResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 10),
    _HdlcRemoteXidResponses_Type()
)
hdlcRemoteXidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteXidResponses.setStatus("obsolete")
_HdlcRemoteTestCommands_Type = Counter32
_HdlcRemoteTestCommands_Object = MibTableColumn
hdlcRemoteTestCommands = _HdlcRemoteTestCommands_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 11),
    _HdlcRemoteTestCommands_Type()
)
hdlcRemoteTestCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteTestCommands.setStatus("obsolete")
_HdlcRemoteTestResponses_Type = Counter32
_HdlcRemoteTestResponses_Object = MibTableColumn
hdlcRemoteTestResponses = _HdlcRemoteTestResponses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 12),
    _HdlcRemoteTestResponses_Type()
)
hdlcRemoteTestResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdlcRemoteTestResponses.setStatus("obsolete")
_HdlcRemoteNodeId_Type = Integer32
_HdlcRemoteNodeId_Object = MibTableColumn
hdlcRemoteNodeId = _HdlcRemoteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 9, 13),
    _HdlcRemoteNodeId_Type()
)
hdlcRemoteNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdlcRemoteNodeId.setStatus("obsolete")
_X25Table_Object = MibTable
x25Table = _X25Table_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 10)
)
if mibBuilder.loadTexts:
    x25Table.setStatus("obsolete")
_X25Index_Type = Integer32
_X25Index_Object = MibTableColumn
x25Index = _X25Index_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 10, 1),
    _X25Index_Type()
)
x25Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Index.setStatus("obsolete")
_X25T1Timer_Type = TimeTicks
_X25T1Timer_Object = MibTableColumn
x25T1Timer = _X25T1Timer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 10, 2),
    _X25T1Timer_Type()
)
x25T1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25T1Timer.setStatus("obsolete")


class _X25N2Count_Type(Integer32):
    """Custom type x25N2Count based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_X25N2Count_Type.__name__ = "Integer32"
_X25N2Count_Object = MibTableColumn
x25N2Count = _X25N2Count_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 10, 3),
    _X25N2Count_Type()
)
x25N2Count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25N2Count.setStatus("obsolete")
_X25T3Timer_Type = TimeTicks
_X25T3Timer_Object = MibTableColumn
x25T3Timer = _X25T3Timer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 10, 4),
    _X25T3Timer_Type()
)
x25T3Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25T3Timer.setStatus("obsolete")
_IcfSecurity_ObjectIdentity = ObjectIdentity
icfSecurity = _IcfSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4)
)


class _IcfSecurPassword_Type(DisplayString):
    """Custom type icfSecurPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IcfSecurPassword_Type.__name__ = "DisplayString"
_IcfSecurPassword_Object = MibScalar
icfSecurPassword = _IcfSecurPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 1),
    _IcfSecurPassword_Type()
)
icfSecurPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurPassword.setStatus("mandatory")


class _IcfSecurAuthAnyMgr_Type(Integer32):
    """Custom type icfSecurAuthAnyMgr based on Integer32"""
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


_IcfSecurAuthAnyMgr_Type.__name__ = "Integer32"
_IcfSecurAuthAnyMgr_Object = MibScalar
icfSecurAuthAnyMgr = _IcfSecurAuthAnyMgr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 2),
    _IcfSecurAuthAnyMgr_Type()
)
icfSecurAuthAnyMgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurAuthAnyMgr.setStatus("mandatory")
_IcfSecurAuthMgrTable_Object = MibTable
icfSecurAuthMgrTable = _IcfSecurAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3)
)
if mibBuilder.loadTexts:
    icfSecurAuthMgrTable.setStatus("mandatory")
_IcfSecurAuthMgrEntry_Object = MibTableRow
icfSecurAuthMgrEntry = _IcfSecurAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1)
)
icfSecurAuthMgrEntry.setIndexNames(
    (0, "HP-ICF", "icfAuthMgrIndex"),
)
if mibBuilder.loadTexts:
    icfSecurAuthMgrEntry.setStatus("mandatory")


class _IcfAuthMgrIndex_Type(Integer32):
    """Custom type icfAuthMgrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IcfAuthMgrIndex_Type.__name__ = "Integer32"
_IcfAuthMgrIndex_Object = MibTableColumn
icfAuthMgrIndex = _IcfAuthMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 1),
    _IcfAuthMgrIndex_Type()
)
icfAuthMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfAuthMgrIndex.setStatus("mandatory")
_IcfAuthMgrIpAddress_Type = IpAddress
_IcfAuthMgrIpAddress_Object = MibTableColumn
icfAuthMgrIpAddress = _IcfAuthMgrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 2),
    _IcfAuthMgrIpAddress_Type()
)
icfAuthMgrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrIpAddress.setStatus("mandatory")


class _IcfAuthMgrIpxAddress_Type(OctetString):
    """Custom type icfAuthMgrIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IcfAuthMgrIpxAddress_Type.__name__ = "OctetString"
_IcfAuthMgrIpxAddress_Object = MibTableColumn
icfAuthMgrIpxAddress = _IcfAuthMgrIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 3),
    _IcfAuthMgrIpxAddress_Type()
)
icfAuthMgrIpxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrIpxAddress.setStatus("mandatory")


class _IcfAuthMgrRcvTraps_Type(Integer32):
    """Custom type icfAuthMgrRcvTraps based on Integer32"""
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


_IcfAuthMgrRcvTraps_Type.__name__ = "Integer32"
_IcfAuthMgrRcvTraps_Object = MibTableColumn
icfAuthMgrRcvTraps = _IcfAuthMgrRcvTraps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 3, 1, 4),
    _IcfAuthMgrRcvTraps_Type()
)
icfAuthMgrRcvTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfAuthMgrRcvTraps.setStatus("mandatory")
_IcfSecurIntruder_ObjectIdentity = ObjectIdentity
icfSecurIntruder = _IcfSecurIntruder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4)
)


class _IcfSecurIntruderFlag_Type(Integer32):
    """Custom type icfSecurIntruderFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IcfSecurIntruderFlag_Type.__name__ = "Integer32"
_IcfSecurIntruderFlag_Object = MibScalar
icfSecurIntruderFlag = _IcfSecurIntruderFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 1),
    _IcfSecurIntruderFlag_Type()
)
icfSecurIntruderFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfSecurIntruderFlag.setStatus("mandatory")
_IcfSecurIntruderIpAddress_Type = IpAddress
_IcfSecurIntruderIpAddress_Object = MibScalar
icfSecurIntruderIpAddress = _IcfSecurIntruderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 2),
    _IcfSecurIntruderIpAddress_Type()
)
icfSecurIntruderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderIpAddress.setStatus("mandatory")


class _IcfSecurIntruderIpxAddress_Type(OctetString):
    """Custom type icfSecurIntruderIpxAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_IcfSecurIntruderIpxAddress_Type.__name__ = "OctetString"
_IcfSecurIntruderIpxAddress_Object = MibScalar
icfSecurIntruderIpxAddress = _IcfSecurIntruderIpxAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 3),
    _IcfSecurIntruderIpxAddress_Type()
)
icfSecurIntruderIpxAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderIpxAddress.setStatus("mandatory")
_IcfSecurIntruderTime_Type = TimeTicks
_IcfSecurIntruderTime_Object = MibScalar
icfSecurIntruderTime = _IcfSecurIntruderTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4, 4, 4),
    _IcfSecurIntruderTime_Type()
)
icfSecurIntruderTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfSecurIntruderTime.setStatus("mandatory")
_IcfConfig_ObjectIdentity = ObjectIdentity
icfConfig = _IcfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5)
)
_IcfConfigIfTable_Object = MibTable
icfConfigIfTable = _IcfConfigIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1)
)
if mibBuilder.loadTexts:
    icfConfigIfTable.setStatus("mandatory")
_IcfConfigIfEntry_Object = MibTableRow
icfConfigIfEntry = _IcfConfigIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1)
)
icfConfigIfEntry.setIndexNames(
    (0, "HP-ICF", "icfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    icfConfigIfEntry.setStatus("mandatory")
_IcfConfigIfIndex_Type = Integer32
_IcfConfigIfIndex_Object = MibTableColumn
icfConfigIfIndex = _IcfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 1),
    _IcfConfigIfIndex_Type()
)
icfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfConfigIfIndex.setStatus("mandatory")
_IcfConfigIfIpAddress_Type = IpAddress
_IcfConfigIfIpAddress_Object = MibTableColumn
icfConfigIfIpAddress = _IcfConfigIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 2),
    _IcfConfigIfIpAddress_Type()
)
icfConfigIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfIpAddress.setStatus("mandatory")
_IcfConfigIfNetMask_Type = IpAddress
_IcfConfigIfNetMask_Object = MibTableColumn
icfConfigIfNetMask = _IcfConfigIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 3),
    _IcfConfigIfNetMask_Type()
)
icfConfigIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfNetMask.setStatus("mandatory")
_IcfConfigIfDefaultGate_Type = IpAddress
_IcfConfigIfDefaultGate_Object = MibTableColumn
icfConfigIfDefaultGate = _IcfConfigIfDefaultGate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 4),
    _IcfConfigIfDefaultGate_Type()
)
icfConfigIfDefaultGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfDefaultGate.setStatus("mandatory")


class _IcfConfigIpTTL_Type(Integer32):
    """Custom type icfConfigIpTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IcfConfigIpTTL_Type.__name__ = "Integer32"
_IcfConfigIpTTL_Object = MibScalar
icfConfigIpTTL = _IcfConfigIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 2),
    _IcfConfigIpTTL_Type()
)
icfConfigIpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIpTTL.setStatus("mandatory")


class _IcfConfigBootpEnable_Type(Integer32):
    """Custom type icfConfigBootpEnable based on Integer32"""
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


_IcfConfigBootpEnable_Type.__name__ = "Integer32"
_IcfConfigBootpEnable_Object = MibScalar
icfConfigBootpEnable = _IcfConfigBootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 3),
    _IcfConfigBootpEnable_Type()
)
icfConfigBootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigBootpEnable.setStatus("mandatory")
_IcfDot12Draft_ObjectIdentity = ObjectIdentity
icfDot12Draft = _IcfDot12Draft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8)
)
_IcfVgRepeater_ObjectIdentity = ObjectIdentity
icfVgRepeater = _IcfVgRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1)
)
_IcfVgBasic_ObjectIdentity = ObjectIdentity
icfVgBasic = _IcfVgBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1)
)
_IcfVgBasicRptr_ObjectIdentity = ObjectIdentity
icfVgBasicRptr = _IcfVgBasicRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1)
)
_IcfVgMACAddress_Type = MacAddress
_IcfVgMACAddress_Object = MibScalar
icfVgMACAddress = _IcfVgMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 1),
    _IcfVgMACAddress_Type()
)
icfVgMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgMACAddress.setStatus("mandatory")


class _IcfVgCurrentFramingType_Type(Integer32):
    """Custom type icfVgCurrentFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_IcfVgCurrentFramingType_Type.__name__ = "Integer32"
_IcfVgCurrentFramingType_Object = MibScalar
icfVgCurrentFramingType = _IcfVgCurrentFramingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 2),
    _IcfVgCurrentFramingType_Type()
)
icfVgCurrentFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgCurrentFramingType.setStatus("mandatory")


class _IcfVgDesiredFramingType_Type(Integer32):
    """Custom type icfVgDesiredFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2))
    )


_IcfVgDesiredFramingType_Type.__name__ = "Integer32"
_IcfVgDesiredFramingType_Object = MibScalar
icfVgDesiredFramingType = _IcfVgDesiredFramingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 3),
    _IcfVgDesiredFramingType_Type()
)
icfVgDesiredFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgDesiredFramingType.setStatus("mandatory")


class _IcfVgFramingCapability_Type(Integer32):
    """Custom type icfVgFramingCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frameType88023", 1),
          ("frameType88025", 2),
          ("frameTypeEither", 3))
    )


_IcfVgFramingCapability_Type.__name__ = "Integer32"
_IcfVgFramingCapability_Object = MibScalar
icfVgFramingCapability = _IcfVgFramingCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 4),
    _IcfVgFramingCapability_Type()
)
icfVgFramingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgFramingCapability.setStatus("mandatory")


class _IcfVgTrainingVersion_Type(Integer32):
    """Custom type icfVgTrainingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IcfVgTrainingVersion_Type.__name__ = "Integer32"
_IcfVgTrainingVersion_Object = MibScalar
icfVgTrainingVersion = _IcfVgTrainingVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 5),
    _IcfVgTrainingVersion_Type()
)
icfVgTrainingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgTrainingVersion.setStatus("mandatory")


class _IcfVgRepeaterGroupCapacity_Type(Integer32):
    """Custom type icfVgRepeaterGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgRepeaterGroupCapacity_Type.__name__ = "Integer32"
_IcfVgRepeaterGroupCapacity_Object = MibScalar
icfVgRepeaterGroupCapacity = _IcfVgRepeaterGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 6),
    _IcfVgRepeaterGroupCapacity_Type()
)
icfVgRepeaterGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterGroupCapacity.setStatus("mandatory")


class _IcfVgRepeaterHealthState_Type(Integer32):
    """Custom type icfVgRepeaterHealthState based on Integer32"""
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
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_IcfVgRepeaterHealthState_Type.__name__ = "Integer32"
_IcfVgRepeaterHealthState_Object = MibScalar
icfVgRepeaterHealthState = _IcfVgRepeaterHealthState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 7),
    _IcfVgRepeaterHealthState_Type()
)
icfVgRepeaterHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterHealthState.setStatus("mandatory")


class _IcfVgRepeaterHealthText_Type(DisplayString):
    """Custom type icfVgRepeaterHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcfVgRepeaterHealthText_Type.__name__ = "DisplayString"
_IcfVgRepeaterHealthText_Object = MibScalar
icfVgRepeaterHealthText = _IcfVgRepeaterHealthText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 8),
    _IcfVgRepeaterHealthText_Type()
)
icfVgRepeaterHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgRepeaterHealthText.setStatus("mandatory")


class _IcfVgRepeaterReset_Type(Integer32):
    """Custom type icfVgRepeaterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_IcfVgRepeaterReset_Type.__name__ = "Integer32"
_IcfVgRepeaterReset_Object = MibScalar
icfVgRepeaterReset = _IcfVgRepeaterReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 9),
    _IcfVgRepeaterReset_Type()
)
icfVgRepeaterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgRepeaterReset.setStatus("mandatory")


class _IcfVgRepeaterNonDisruptTest_Type(Integer32):
    """Custom type icfVgRepeaterNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_IcfVgRepeaterNonDisruptTest_Type.__name__ = "Integer32"
_IcfVgRepeaterNonDisruptTest_Object = MibScalar
icfVgRepeaterNonDisruptTest = _IcfVgRepeaterNonDisruptTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 1, 10),
    _IcfVgRepeaterNonDisruptTest_Type()
)
icfVgRepeaterNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgRepeaterNonDisruptTest.setStatus("mandatory")
_IcfVgBasicGroup_ObjectIdentity = ObjectIdentity
icfVgBasicGroup = _IcfVgBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2)
)
_IcfVgBasicGroupTable_Object = MibTable
icfVgBasicGroupTable = _IcfVgBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    icfVgBasicGroupTable.setStatus("mandatory")
_IcfVgBasicGroupEntry_Object = MibTableRow
icfVgBasicGroupEntry = _IcfVgBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1)
)
icfVgBasicGroupEntry.setIndexNames(
    (0, "HP-ICF", "icfVgGroupIndex"),
)
if mibBuilder.loadTexts:
    icfVgBasicGroupEntry.setStatus("mandatory")


class _IcfVgGroupIndex_Type(Integer32):
    """Custom type icfVgGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgGroupIndex_Type.__name__ = "Integer32"
_IcfVgGroupIndex_Object = MibTableColumn
icfVgGroupIndex = _IcfVgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 1),
    _IcfVgGroupIndex_Type()
)
icfVgGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgGroupIndex.setStatus("mandatory")


class _IcfVgGroupDescr_Type(DisplayString):
    """Custom type icfVgGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcfVgGroupDescr_Type.__name__ = "DisplayString"
_IcfVgGroupDescr_Object = MibTableColumn
icfVgGroupDescr = _IcfVgGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 2),
    _IcfVgGroupDescr_Type()
)
icfVgGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupDescr.setStatus("mandatory")
_IcfVgGroupObjectID_Type = ObjectIdentifier
_IcfVgGroupObjectID_Object = MibTableColumn
icfVgGroupObjectID = _IcfVgGroupObjectID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 3),
    _IcfVgGroupObjectID_Type()
)
icfVgGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupObjectID.setStatus("mandatory")


class _IcfVgGroupOperStatus_Type(Integer32):
    """Custom type icfVgGroupOperStatus based on Integer32"""
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
        *(("malfunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("underTest", 5))
    )


_IcfVgGroupOperStatus_Type.__name__ = "Integer32"
_IcfVgGroupOperStatus_Object = MibTableColumn
icfVgGroupOperStatus = _IcfVgGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 4),
    _IcfVgGroupOperStatus_Type()
)
icfVgGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupOperStatus.setStatus("mandatory")
_IcfVgGroupLastOperStatusChange_Type = TimeStamp
_IcfVgGroupLastOperStatusChange_Object = MibTableColumn
icfVgGroupLastOperStatusChange = _IcfVgGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 5),
    _IcfVgGroupLastOperStatusChange_Type()
)
icfVgGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupLastOperStatusChange.setStatus("mandatory")


class _IcfVgGroupPortCapacity_Type(Integer32):
    """Custom type icfVgGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgGroupPortCapacity_Type.__name__ = "Integer32"
_IcfVgGroupPortCapacity_Object = MibTableColumn
icfVgGroupPortCapacity = _IcfVgGroupPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 6),
    _IcfVgGroupPortCapacity_Type()
)
icfVgGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgGroupPortCapacity.setStatus("mandatory")


class _IcfVgGroupCablesBundled_Type(Integer32):
    """Custom type icfVgGroupCablesBundled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCablesBundled", 2),
          ("someCablesBundled", 1))
    )


_IcfVgGroupCablesBundled_Type.__name__ = "Integer32"
_IcfVgGroupCablesBundled_Object = MibTableColumn
icfVgGroupCablesBundled = _IcfVgGroupCablesBundled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 2, 1, 1, 7),
    _IcfVgGroupCablesBundled_Type()
)
icfVgGroupCablesBundled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgGroupCablesBundled.setStatus("mandatory")
_IcfVgBasicPort_ObjectIdentity = ObjectIdentity
icfVgBasicPort = _IcfVgBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3)
)
_IcfVgBasicPortTable_Object = MibTable
icfVgBasicPortTable = _IcfVgBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgBasicPortTable.setStatus("mandatory")
_IcfVgBasicPortEntry_Object = MibTableRow
icfVgBasicPortEntry = _IcfVgBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1)
)
icfVgBasicPortEntry.setIndexNames(
    (0, "HP-ICF", "icfVgPortGroupIndex"),
    (0, "HP-ICF", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgBasicPortEntry.setStatus("mandatory")


class _IcfVgPortGroupIndex_Type(Integer32):
    """Custom type icfVgPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgPortGroupIndex_Type.__name__ = "Integer32"
_IcfVgPortGroupIndex_Object = MibTableColumn
icfVgPortGroupIndex = _IcfVgPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 1),
    _IcfVgPortGroupIndex_Type()
)
icfVgPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgPortGroupIndex.setStatus("mandatory")


class _IcfVgPortIndex_Type(Integer32):
    """Custom type icfVgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_IcfVgPortIndex_Type.__name__ = "Integer32"
_IcfVgPortIndex_Object = MibTableColumn
icfVgPortIndex = _IcfVgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 2),
    _IcfVgPortIndex_Type()
)
icfVgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icfVgPortIndex.setStatus("mandatory")


class _IcfVgPortType_Type(Integer32):
    """Custom type icfVgPortType based on Integer32"""
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
        *(("cascadeExternal", 1),
          ("cascadeInternal", 2),
          ("localExternal", 3),
          ("localInternal", 4))
    )


_IcfVgPortType_Type.__name__ = "Integer32"
_IcfVgPortType_Object = MibTableColumn
icfVgPortType = _IcfVgPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 3),
    _IcfVgPortType_Type()
)
icfVgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortType.setStatus("mandatory")


class _IcfVgPortAdminStatus_Type(Integer32):
    """Custom type icfVgPortAdminStatus based on Integer32"""
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


_IcfVgPortAdminStatus_Type.__name__ = "Integer32"
_IcfVgPortAdminStatus_Object = MibTableColumn
icfVgPortAdminStatus = _IcfVgPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 4),
    _IcfVgPortAdminStatus_Type()
)
icfVgPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortAdminStatus.setStatus("mandatory")


class _IcfVgPortStatus_Type(Integer32):
    """Custom type icfVgPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("training", 3))
    )


_IcfVgPortStatus_Type.__name__ = "Integer32"
_IcfVgPortStatus_Object = MibTableColumn
icfVgPortStatus = _IcfVgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 5),
    _IcfVgPortStatus_Type()
)
icfVgPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortStatus.setStatus("mandatory")


class _IcfVgPortSupportedPromiscMode_Type(Integer32):
    """Custom type icfVgPortSupportedPromiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("promiscModeOnly", 3),
          ("singleModeOnly", 1),
          ("singleOrPromiscMode", 2))
    )


_IcfVgPortSupportedPromiscMode_Type.__name__ = "Integer32"
_IcfVgPortSupportedPromiscMode_Object = MibTableColumn
icfVgPortSupportedPromiscMode = _IcfVgPortSupportedPromiscMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 6),
    _IcfVgPortSupportedPromiscMode_Type()
)
icfVgPortSupportedPromiscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortSupportedPromiscMode.setStatus("mandatory")


class _IcfVgPortSupportedCascadeMode_Type(Integer32):
    """Custom type icfVgPortSupportedCascadeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascadePort", 3),
          ("endNodesOnly", 1),
          ("endNodesOrRepeaters", 2))
    )


_IcfVgPortSupportedCascadeMode_Type.__name__ = "Integer32"
_IcfVgPortSupportedCascadeMode_Object = MibTableColumn
icfVgPortSupportedCascadeMode = _IcfVgPortSupportedCascadeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 7),
    _IcfVgPortSupportedCascadeMode_Type()
)
icfVgPortSupportedCascadeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortSupportedCascadeMode.setStatus("mandatory")


class _IcfVgPortAllowedTrainType_Type(Integer32):
    """Custom type icfVgPortAllowedTrainType based on Integer32"""
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
        *(("allowAnything", 4),
          ("allowEndNodesOnly", 1),
          ("allowEndNodesOrRepeaters", 3),
          ("allowPromiscuousEndNodes", 2))
    )


_IcfVgPortAllowedTrainType_Type.__name__ = "Integer32"
_IcfVgPortAllowedTrainType_Object = MibTableColumn
icfVgPortAllowedTrainType = _IcfVgPortAllowedTrainType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 8),
    _IcfVgPortAllowedTrainType_Type()
)
icfVgPortAllowedTrainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortAllowedTrainType.setStatus("mandatory")


class _IcfVgPortLastTrainConfig_Type(OctetString):
    """Custom type icfVgPortLastTrainConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IcfVgPortLastTrainConfig_Type.__name__ = "OctetString"
_IcfVgPortLastTrainConfig_Object = MibTableColumn
icfVgPortLastTrainConfig = _IcfVgPortLastTrainConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 9),
    _IcfVgPortLastTrainConfig_Type()
)
icfVgPortLastTrainConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortLastTrainConfig.setStatus("mandatory")


class _IcfVgPortTrainingResult_Type(OctetString):
    """Custom type icfVgPortTrainingResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IcfVgPortTrainingResult_Type.__name__ = "OctetString"
_IcfVgPortTrainingResult_Object = MibTableColumn
icfVgPortTrainingResult = _IcfVgPortTrainingResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 10),
    _IcfVgPortTrainingResult_Type()
)
icfVgPortTrainingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortTrainingResult.setStatus("mandatory")
_IcfVgPortPriorityEnable_Type = TruthValue
_IcfVgPortPriorityEnable_Object = MibTableColumn
icfVgPortPriorityEnable = _IcfVgPortPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 11),
    _IcfVgPortPriorityEnable_Type()
)
icfVgPortPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfVgPortPriorityEnable.setStatus("mandatory")


class _IcfVgPortMediaType_Type(Integer32):
    """Custom type icfVgPortMediaType based on Integer32"""
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
        *(("fibre", 6),
          ("other", 1),
          ("pmdMissing", 3),
          ("stp2", 5),
          ("unknown", 2),
          ("utp4", 4))
    )


_IcfVgPortMediaType_Type.__name__ = "Integer32"
_IcfVgPortMediaType_Object = MibTableColumn
icfVgPortMediaType = _IcfVgPortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 1, 3, 1, 1, 12),
    _IcfVgPortMediaType_Type()
)
icfVgPortMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortMediaType.setStatus("mandatory")
_IcfVgMonitor_ObjectIdentity = ObjectIdentity
icfVgMonitor = _IcfVgMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2)
)
_IcfVgMonRptr_ObjectIdentity = ObjectIdentity
icfVgMonRptr = _IcfVgMonRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 1)
)
_IcfVgMonGroup_ObjectIdentity = ObjectIdentity
icfVgMonGroup = _IcfVgMonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 2)
)
_IcfVgMonPort_ObjectIdentity = ObjectIdentity
icfVgMonPort = _IcfVgMonPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3)
)
_IcfVgMonPortTable_Object = MibTable
icfVgMonPortTable = _IcfVgMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgMonPortTable.setStatus("mandatory")
_IcfVgMonPortEntry_Object = MibTableRow
icfVgMonPortEntry = _IcfVgMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1)
)
icfVgMonPortEntry.setIndexNames(
    (0, "HP-ICF", "icfVgPortGroupIndex"),
    (0, "HP-ICF", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgMonPortEntry.setStatus("mandatory")
_IcfVgPortReadableFrames_Type = Counter32
_IcfVgPortReadableFrames_Object = MibTableColumn
icfVgPortReadableFrames = _IcfVgPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 1),
    _IcfVgPortReadableFrames_Type()
)
icfVgPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortReadableFrames.setStatus("mandatory")
_IcfVgPortReadableOctets_Type = Counter32
_IcfVgPortReadableOctets_Object = MibTableColumn
icfVgPortReadableOctets = _IcfVgPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 2),
    _IcfVgPortReadableOctets_Type()
)
icfVgPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortReadableOctets.setStatus("mandatory")
_IcfVgPortUnreadableOctets_Type = Counter32
_IcfVgPortUnreadableOctets_Object = MibTableColumn
icfVgPortUnreadableOctets = _IcfVgPortUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 3),
    _IcfVgPortUnreadableOctets_Type()
)
icfVgPortUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortUnreadableOctets.setStatus("mandatory")
_IcfVgPortHighPriorityFrames_Type = Counter32
_IcfVgPortHighPriorityFrames_Object = MibTableColumn
icfVgPortHighPriorityFrames = _IcfVgPortHighPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 4),
    _IcfVgPortHighPriorityFrames_Type()
)
icfVgPortHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHighPriorityFrames.setStatus("mandatory")
_IcfVgPortHighPriorityOctets_Type = Counter32
_IcfVgPortHighPriorityOctets_Object = MibTableColumn
icfVgPortHighPriorityOctets = _IcfVgPortHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 5),
    _IcfVgPortHighPriorityOctets_Type()
)
icfVgPortHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortHighPriorityOctets.setStatus("mandatory")
_IcfVgPortBroadcastFrames_Type = Counter32
_IcfVgPortBroadcastFrames_Object = MibTableColumn
icfVgPortBroadcastFrames = _IcfVgPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 6),
    _IcfVgPortBroadcastFrames_Type()
)
icfVgPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortBroadcastFrames.setStatus("mandatory")
_IcfVgPortMulticastFrames_Type = Counter32
_IcfVgPortMulticastFrames_Object = MibTableColumn
icfVgPortMulticastFrames = _IcfVgPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 7),
    _IcfVgPortMulticastFrames_Type()
)
icfVgPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortMulticastFrames.setStatus("mandatory")
_IcfVgPortIPMFrames_Type = Counter32
_IcfVgPortIPMFrames_Object = MibTableColumn
icfVgPortIPMFrames = _IcfVgPortIPMFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 8),
    _IcfVgPortIPMFrames_Type()
)
icfVgPortIPMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortIPMFrames.setStatus("mandatory")
_IcfVgPortDataErrorFrames_Type = Counter32
_IcfVgPortDataErrorFrames_Object = MibTableColumn
icfVgPortDataErrorFrames = _IcfVgPortDataErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 9),
    _IcfVgPortDataErrorFrames_Type()
)
icfVgPortDataErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortDataErrorFrames.setStatus("mandatory")
_IcfVgPortPriorityPromotions_Type = Counter32
_IcfVgPortPriorityPromotions_Object = MibTableColumn
icfVgPortPriorityPromotions = _IcfVgPortPriorityPromotions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 2, 3, 1, 1, 10),
    _IcfVgPortPriorityPromotions_Type()
)
icfVgPortPriorityPromotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgPortPriorityPromotions.setStatus("mandatory")
_IcfVgAddrTrack_ObjectIdentity = ObjectIdentity
icfVgAddrTrack = _IcfVgAddrTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3)
)
_IcfVgAddrTrackRptr_ObjectIdentity = ObjectIdentity
icfVgAddrTrackRptr = _IcfVgAddrTrackRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 1)
)
_IcfVgAddrTrackGroup_ObjectIdentity = ObjectIdentity
icfVgAddrTrackGroup = _IcfVgAddrTrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 2)
)
_IcfVgAddrTrackPort_ObjectIdentity = ObjectIdentity
icfVgAddrTrackPort = _IcfVgAddrTrackPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3)
)
_IcfVgAddrTrackTable_Object = MibTable
icfVgAddrTrackTable = _IcfVgAddrTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    icfVgAddrTrackTable.setStatus("mandatory")
_IcfVgAddrTrackEntry_Object = MibTableRow
icfVgAddrTrackEntry = _IcfVgAddrTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1)
)
icfVgAddrTrackEntry.setIndexNames(
    (0, "HP-ICF", "icfVgPortGroupIndex"),
    (0, "HP-ICF", "icfVgPortIndex"),
)
if mibBuilder.loadTexts:
    icfVgAddrTrackEntry.setStatus("mandatory")


class _IcfVgAddrLastTrainedAddress_Type(OctetString):
    """Custom type icfVgAddrLastTrainedAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_IcfVgAddrLastTrainedAddress_Type.__name__ = "OctetString"
_IcfVgAddrLastTrainedAddress_Object = MibTableColumn
icfVgAddrLastTrainedAddress = _IcfVgAddrLastTrainedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 1),
    _IcfVgAddrLastTrainedAddress_Type()
)
icfVgAddrLastTrainedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgAddrLastTrainedAddress.setStatus("mandatory")
_IcfVgAddrTrainedAddrChanges_Type = Counter32
_IcfVgAddrTrainedAddrChanges_Object = MibTableColumn
icfVgAddrTrainedAddrChanges = _IcfVgAddrTrainedAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1, 3, 3, 1, 1, 2),
    _IcfVgAddrTrainedAddrChanges_Type()
)
icfVgAddrTrainedAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfVgAddrTrainedAddrChanges.setStatus("mandatory")
_HpicfAdmin_ObjectIdentity = ObjectIdentity
hpicfAdmin = _HpicfAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10)
)
_HpicfDomains_ObjectIdentity = ObjectIdentity
hpicfDomains = _HpicfDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 1)
)
_HpicfLLCDomain_ObjectIdentity = ObjectIdentity
hpicfLLCDomain = _HpicfLLCDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 1, 1)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)
_HpicfCommon_ObjectIdentity = ObjectIdentity
hpicfCommon = _HpicfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1)
)
_HpicfChain_ObjectIdentity = ObjectIdentity
hpicfChain = _HpicfChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1)
)


class _HpicfChainMaxMembers_Type(Integer32):
    """Custom type hpicfChainMaxMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChainMaxMembers_Type.__name__ = "Integer32"
_HpicfChainMaxMembers_Object = MibScalar
hpicfChainMaxMembers = _HpicfChainMaxMembers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 1),
    _HpicfChainMaxMembers_Type()
)
hpicfChainMaxMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainMaxMembers.setStatus("mandatory")


class _HpicfChainCurMembers_Type(Integer32):
    """Custom type hpicfChainCurMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChainCurMembers_Type.__name__ = "Integer32"
_HpicfChainCurMembers_Object = MibScalar
hpicfChainCurMembers = _HpicfChainCurMembers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 2),
    _HpicfChainCurMembers_Type()
)
hpicfChainCurMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainCurMembers.setStatus("mandatory")
_HpicfChainLastChange_Type = TimeStamp
_HpicfChainLastChange_Object = MibScalar
hpicfChainLastChange = _HpicfChainLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 3),
    _HpicfChainLastChange_Type()
)
hpicfChainLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainLastChange.setStatus("mandatory")
_HpicfChainChanges_Type = Counter32
_HpicfChainChanges_Object = MibScalar
hpicfChainChanges = _HpicfChainChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 4),
    _HpicfChainChanges_Type()
)
hpicfChainChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainChanges.setStatus("mandatory")
_HpicfChainTable_Object = MibTable
hpicfChainTable = _HpicfChainTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfChainTable.setStatus("mandatory")
_HpicfChainEntry_Object = MibTableRow
hpicfChainEntry = _HpicfChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1)
)
hpicfChainEntry.setIndexNames(
    (0, "HP-ICF", "hpicfChainId"),
)
if mibBuilder.loadTexts:
    hpicfChainEntry.setStatus("mandatory")


class _HpicfChainId_Type(OctetString):
    """Custom type hpicfChainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChainId_Type.__name__ = "OctetString"
_HpicfChainId_Object = MibTableColumn
hpicfChainId = _HpicfChainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 1),
    _HpicfChainId_Type()
)
hpicfChainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainId.setStatus("mandatory")
_HpicfChainObjectId_Type = ObjectIdentifier
_HpicfChainObjectId_Object = MibTableColumn
hpicfChainObjectId = _HpicfChainObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 2),
    _HpicfChainObjectId_Type()
)
hpicfChainObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainObjectId.setStatus("mandatory")
_HpicfChainTimestamp_Type = TimeStamp
_HpicfChainTimestamp_Object = MibTableColumn
hpicfChainTimestamp = _HpicfChainTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 3),
    _HpicfChainTimestamp_Type()
)
hpicfChainTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainTimestamp.setStatus("mandatory")
_HpicfChainHasAgent_Type = TruthValue
_HpicfChainHasAgent_Object = MibTableColumn
hpicfChainHasAgent = _HpicfChainHasAgent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 4),
    _HpicfChainHasAgent_Type()
)
hpicfChainHasAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainHasAgent.setStatus("mandatory")
_HpicfChainThisBox_Type = TruthValue
_HpicfChainThisBox_Object = MibTableColumn
hpicfChainThisBox = _HpicfChainThisBox_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 5),
    _HpicfChainThisBox_Type()
)
hpicfChainThisBox.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainThisBox.setStatus("mandatory")


class _HpicfChainLocation_Type(Integer32):
    """Custom type hpicfChainLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfChainLocation_Type.__name__ = "Integer32"
_HpicfChainLocation_Object = MibTableColumn
hpicfChainLocation = _HpicfChainLocation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 5, 1, 6),
    _HpicfChainLocation_Type()
)
hpicfChainLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfChainLocation.setStatus("mandatory")
_HpicfChainViewTable_Object = MibTable
hpicfChainViewTable = _HpicfChainViewTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfChainViewTable.setStatus("mandatory")
_HpicfChainViewEntry_Object = MibTableRow
hpicfChainViewEntry = _HpicfChainViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1)
)
hpicfChainViewEntry.setIndexNames(
    (0, "HP-ICF", "hpicfChainViewId"),
)
if mibBuilder.loadTexts:
    hpicfChainViewEntry.setStatus("mandatory")


class _HpicfChainViewId_Type(OctetString):
    """Custom type hpicfChainViewId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChainViewId_Type.__name__ = "OctetString"
_HpicfChainViewId_Object = MibTableColumn
hpicfChainViewId = _HpicfChainViewId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1, 1),
    _HpicfChainViewId_Type()
)
hpicfChainViewId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainViewId.setStatus("mandatory")


class _HpicfChainViewName_Type(DisplayString):
    """Custom type hpicfChainViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpicfChainViewName_Type.__name__ = "DisplayString"
_HpicfChainViewName_Object = MibTableColumn
hpicfChainViewName = _HpicfChainViewName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1, 6, 1, 2),
    _HpicfChainViewName_Type()
)
hpicfChainViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChainViewName.setStatus("mandatory")
_HpicfChassis_ObjectIdentity = ObjectIdentity
hpicfChassis = _HpicfChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2)
)


class _HpicfChassisId_Type(OctetString):
    """Custom type hpicfChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpicfChassisId_Type.__name__ = "OctetString"
_HpicfChassisId_Object = MibScalar
hpicfChassisId = _HpicfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 1),
    _HpicfChassisId_Type()
)
hpicfChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChassisId.setStatus("mandatory")


class _HpicfChassisNumSlots_Type(Integer32):
    """Custom type hpicfChassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HpicfChassisNumSlots_Type.__name__ = "Integer32"
_HpicfChassisNumSlots_Object = MibScalar
hpicfChassisNumSlots = _HpicfChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 2),
    _HpicfChassisNumSlots_Type()
)
hpicfChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChassisNumSlots.setStatus("mandatory")
_HpicfSlotTable_Object = MibTable
hpicfSlotTable = _HpicfSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfSlotTable.setStatus("mandatory")
_HpicfSlotEntry_Object = MibTableRow
hpicfSlotEntry = _HpicfSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1)
)
hpicfSlotEntry.setIndexNames(
    (0, "HP-ICF", "hpicfSlotIndex"),
)
if mibBuilder.loadTexts:
    hpicfSlotEntry.setStatus("mandatory")


class _HpicfSlotIndex_Type(Integer32):
    """Custom type hpicfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotIndex_Type.__name__ = "Integer32"
_HpicfSlotIndex_Object = MibTableColumn
hpicfSlotIndex = _HpicfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 1),
    _HpicfSlotIndex_Type()
)
hpicfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotIndex.setStatus("mandatory")
_HpicfSlotObjectId_Type = ObjectIdentifier
_HpicfSlotObjectId_Object = MibTableColumn
hpicfSlotObjectId = _HpicfSlotObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 2),
    _HpicfSlotObjectId_Type()
)
hpicfSlotObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotObjectId.setStatus("mandatory")
_HpicfSlotLastChange_Type = TimeStamp
_HpicfSlotLastChange_Object = MibTableColumn
hpicfSlotLastChange = _HpicfSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 3),
    _HpicfSlotLastChange_Type()
)
hpicfSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotLastChange.setStatus("mandatory")


class _HpicfSlotDescr_Type(DisplayString):
    """Custom type hpicfSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfSlotDescr_Type.__name__ = "DisplayString"
_HpicfSlotDescr_Object = MibTableColumn
hpicfSlotDescr = _HpicfSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 3, 1, 4),
    _HpicfSlotDescr_Type()
)
hpicfSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotDescr.setStatus("mandatory")
_HpicfEntityTable_Object = MibTable
hpicfEntityTable = _HpicfEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfEntityTable.setStatus("mandatory")
_HpicfEntityEntry_Object = MibTableRow
hpicfEntityEntry = _HpicfEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1)
)
hpicfEntityEntry.setIndexNames(
    (0, "HP-ICF", "hpicfEntityIndex"),
)
if mibBuilder.loadTexts:
    hpicfEntityEntry.setStatus("mandatory")


class _HpicfEntityIndex_Type(Integer32):
    """Custom type hpicfEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfEntityIndex_Type.__name__ = "Integer32"
_HpicfEntityIndex_Object = MibTableColumn
hpicfEntityIndex = _HpicfEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 1),
    _HpicfEntityIndex_Type()
)
hpicfEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityIndex.setStatus("mandatory")


class _HpicfEntityFunction_Type(Integer32):
    """Custom type hpicfEntityFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpicfEntityFunction_Type.__name__ = "Integer32"
_HpicfEntityFunction_Object = MibTableColumn
hpicfEntityFunction = _HpicfEntityFunction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 2),
    _HpicfEntityFunction_Type()
)
hpicfEntityFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityFunction.setStatus("mandatory")
_HpicfEntityObjectId_Type = ObjectIdentifier
_HpicfEntityObjectId_Object = MibTableColumn
hpicfEntityObjectId = _HpicfEntityObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 3),
    _HpicfEntityObjectId_Type()
)
hpicfEntityObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityObjectId.setStatus("mandatory")


class _HpicfEntityDescr_Type(DisplayString):
    """Custom type hpicfEntityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfEntityDescr_Type.__name__ = "DisplayString"
_HpicfEntityDescr_Object = MibTableColumn
hpicfEntityDescr = _HpicfEntityDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 4),
    _HpicfEntityDescr_Type()
)
hpicfEntityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityDescr.setStatus("mandatory")
_HpicfEntityTimestamp_Type = TimeStamp
_HpicfEntityTimestamp_Object = MibTableColumn
hpicfEntityTimestamp = _HpicfEntityTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 4, 1, 5),
    _HpicfEntityTimestamp_Type()
)
hpicfEntityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfEntityTimestamp.setStatus("mandatory")
_HpicfSlotMapTable_Object = MibTable
hpicfSlotMapTable = _HpicfSlotMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfSlotMapTable.setStatus("mandatory")
_HpicfSlotMapEntry_Object = MibTableRow
hpicfSlotMapEntry = _HpicfSlotMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1)
)
hpicfSlotMapEntry.setIndexNames(
    (0, "HP-ICF", "hpicfSlotMapSlot"),
    (0, "HP-ICF", "hpicfSlotMapEntity"),
)
if mibBuilder.loadTexts:
    hpicfSlotMapEntry.setStatus("mandatory")


class _HpicfSlotMapSlot_Type(Integer32):
    """Custom type hpicfSlotMapSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotMapSlot_Type.__name__ = "Integer32"
_HpicfSlotMapSlot_Object = MibTableColumn
hpicfSlotMapSlot = _HpicfSlotMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 1),
    _HpicfSlotMapSlot_Type()
)
hpicfSlotMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotMapSlot.setStatus("mandatory")


class _HpicfSlotMapEntity_Type(Integer32):
    """Custom type hpicfSlotMapEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfSlotMapEntity_Type.__name__ = "Integer32"
_HpicfSlotMapEntity_Object = MibTableColumn
hpicfSlotMapEntity = _HpicfSlotMapEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 5, 1, 2),
    _HpicfSlotMapEntity_Type()
)
hpicfSlotMapEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSlotMapEntity.setStatus("mandatory")
_HpicfSensorTable_Object = MibTable
hpicfSensorTable = _HpicfSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfSensorTable.setStatus("mandatory")
_HpicfSensorEntry_Object = MibTableRow
hpicfSensorEntry = _HpicfSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1)
)
hpicfSensorEntry.setIndexNames(
    (0, "HP-ICF", "hpicfSensorIndex"),
)
if mibBuilder.loadTexts:
    hpicfSensorEntry.setStatus("mandatory")
_HpicfSensorIndex_Type = Integer32
_HpicfSensorIndex_Object = MibTableColumn
hpicfSensorIndex = _HpicfSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 1),
    _HpicfSensorIndex_Type()
)
hpicfSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorIndex.setStatus("mandatory")
_HpicfSensorObjectId_Type = ObjectIdentifier
_HpicfSensorObjectId_Object = MibTableColumn
hpicfSensorObjectId = _HpicfSensorObjectId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 2),
    _HpicfSensorObjectId_Type()
)
hpicfSensorObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorObjectId.setStatus("mandatory")
_HpicfSensorNumber_Type = Integer32
_HpicfSensorNumber_Object = MibTableColumn
hpicfSensorNumber = _HpicfSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 3),
    _HpicfSensorNumber_Type()
)
hpicfSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorNumber.setStatus("mandatory")


class _HpicfSensorStatus_Type(Integer32):
    """Custom type hpicfSensorStatus based on Integer32"""
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
        *(("bad", 2),
          ("good", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_HpicfSensorStatus_Type.__name__ = "Integer32"
_HpicfSensorStatus_Object = MibTableColumn
hpicfSensorStatus = _HpicfSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 4),
    _HpicfSensorStatus_Type()
)
hpicfSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorStatus.setStatus("mandatory")
_HpicfSensorWarnings_Type = Counter32
_HpicfSensorWarnings_Object = MibTableColumn
hpicfSensorWarnings = _HpicfSensorWarnings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 5),
    _HpicfSensorWarnings_Type()
)
hpicfSensorWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorWarnings.setStatus("mandatory")
_HpicfSensorFailures_Type = Counter32
_HpicfSensorFailures_Object = MibTableColumn
hpicfSensorFailures = _HpicfSensorFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 6),
    _HpicfSensorFailures_Type()
)
hpicfSensorFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorFailures.setStatus("mandatory")
_HpicfSensorDescr_Type = DisplayString
_HpicfSensorDescr_Object = MibTableColumn
hpicfSensorDescr = _HpicfSensorDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 6, 1, 7),
    _HpicfSensorDescr_Type()
)
hpicfSensorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSensorDescr.setStatus("mandatory")
_HpicfChassisAddrTable_Object = MibTable
hpicfChassisAddrTable = _HpicfChassisAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfChassisAddrTable.setStatus("mandatory")
_HpicfChassisAddrEntry_Object = MibTableRow
hpicfChassisAddrEntry = _HpicfChassisAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1)
)
hpicfChassisAddrEntry.setIndexNames(
    (0, "HP-ICF", "hpicfChasAddrType"),
    (0, "HP-ICF", "hpicfChasAddrAddress"),
)
if mibBuilder.loadTexts:
    hpicfChassisAddrEntry.setStatus("mandatory")


class _HpicfChasAddrType_Type(Integer32):
    """Custom type hpicfChasAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipAddr", 1),
          ("ipxAddr", 2),
          ("macAddr", 3))
    )


_HpicfChasAddrType_Type.__name__ = "Integer32"
_HpicfChasAddrType_Object = MibTableColumn
hpicfChasAddrType = _HpicfChasAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 1),
    _HpicfChasAddrType_Type()
)
hpicfChasAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfChasAddrType.setStatus("mandatory")


class _HpicfChasAddrAddress_Type(OctetString):
    """Custom type hpicfChasAddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_HpicfChasAddrAddress_Type.__name__ = "OctetString"
_HpicfChasAddrAddress_Object = MibTableColumn
hpicfChasAddrAddress = _HpicfChasAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 2),
    _HpicfChasAddrAddress_Type()
)
hpicfChasAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfChasAddrAddress.setStatus("mandatory")


class _HpicfChasAddrEntity_Type(Integer32):
    """Custom type hpicfChasAddrEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfChasAddrEntity_Type.__name__ = "Integer32"
_HpicfChasAddrEntity_Object = MibTableColumn
hpicfChasAddrEntity = _HpicfChasAddrEntity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2, 7, 1, 3),
    _HpicfChasAddrEntity_Type()
)
hpicfChasAddrEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfChasAddrEntity.setStatus("mandatory")
_HpicfDownload_ObjectIdentity = ObjectIdentity
hpicfDownload = _HpicfDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3)
)
_HpicfDownloadTable_Object = MibTable
hpicfDownloadTable = _HpicfDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfDownloadTable.setStatus("mandatory")
_HpicfDownloadEntry_Object = MibTableRow
hpicfDownloadEntry = _HpicfDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1)
)
hpicfDownloadEntry.setIndexNames(
    (0, "HP-ICF", "hpicfDownloadIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadEntry.setStatus("mandatory")


class _HpicfDownloadIndex_Type(Integer32):
    """Custom type hpicfDownloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dlInstance", 1)
    )


_HpicfDownloadIndex_Type.__name__ = "Integer32"
_HpicfDownloadIndex_Object = MibTableColumn
hpicfDownloadIndex = _HpicfDownloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 1),
    _HpicfDownloadIndex_Type()
)
hpicfDownloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadIndex.setStatus("mandatory")
_HpicfDownloadOwnerAddress_Type = TAddress
_HpicfDownloadOwnerAddress_Object = MibTableColumn
hpicfDownloadOwnerAddress = _HpicfDownloadOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 2),
    _HpicfDownloadOwnerAddress_Type()
)
hpicfDownloadOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadOwnerAddress.setStatus("mandatory")
_HpicfDownloadOwnerDomain_Type = ObjectIdentifier
_HpicfDownloadOwnerDomain_Object = MibTableColumn
hpicfDownloadOwnerDomain = _HpicfDownloadOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 3),
    _HpicfDownloadOwnerDomain_Type()
)
hpicfDownloadOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadOwnerDomain.setStatus("mandatory")
_HpicfDownloadTAddress_Type = TAddress
_HpicfDownloadTAddress_Object = MibTableColumn
hpicfDownloadTAddress = _HpicfDownloadTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 4),
    _HpicfDownloadTAddress_Type()
)
hpicfDownloadTAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTAddress.setStatus("mandatory")
_HpicfDownloadTDomain_Type = ObjectIdentifier
_HpicfDownloadTDomain_Object = MibTableColumn
hpicfDownloadTDomain = _HpicfDownloadTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 5),
    _HpicfDownloadTDomain_Type()
)
hpicfDownloadTDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadTDomain.setStatus("mandatory")


class _HpicfDownloadFilename_Type(DisplayString):
    """Custom type hpicfDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDownloadFilename_Type.__name__ = "DisplayString"
_HpicfDownloadFilename_Object = MibTableColumn
hpicfDownloadFilename = _HpicfDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 6),
    _HpicfDownloadFilename_Type()
)
hpicfDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadFilename.setStatus("mandatory")


class _HpicfDownloadResetType_Type(Integer32):
    """Custom type hpicfDownloadResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 3),
          ("noReset", 1),
          ("warmReset", 2))
    )


_HpicfDownloadResetType_Type.__name__ = "Integer32"
_HpicfDownloadResetType_Object = MibTableColumn
hpicfDownloadResetType = _HpicfDownloadResetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 7),
    _HpicfDownloadResetType_Type()
)
hpicfDownloadResetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadResetType.setStatus("mandatory")


class _HpicfDownloadErrorStatus_Type(Integer32):
    """Custom type hpicfDownloadErrorStatus based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 14),
          ("accessViolation", 2),
          ("cannotDowngrade", 21),
          ("cannotUpgrade", 20),
          ("corruptFile", 9),
          ("diskFull", 3),
          ("erasingEeprom", 17),
          ("fileExists", 6),
          ("fileNotFound", 1),
          ("hardwareError", 12),
          ("idle", 16),
          ("illegalOperation", 4),
          ("inProgress", 15),
          ("incompleteFirmware", 18),
          ("noServer", 10),
          ("noSuchUser", 7),
          ("notDefined", 8),
          ("requirePowerCycle", 19),
          ("success", 13),
          ("tftpTimeout", 11),
          ("unknownTID", 5))
    )


_HpicfDownloadErrorStatus_Type.__name__ = "Integer32"
_HpicfDownloadErrorStatus_Object = MibTableColumn
hpicfDownloadErrorStatus = _HpicfDownloadErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 8),
    _HpicfDownloadErrorStatus_Type()
)
hpicfDownloadErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadErrorStatus.setStatus("mandatory")


class _HpicfDownloadErrorText_Type(DisplayString):
    """Custom type hpicfDownloadErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDownloadErrorText_Type.__name__ = "DisplayString"
_HpicfDownloadErrorText_Object = MibTableColumn
hpicfDownloadErrorText = _HpicfDownloadErrorText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 9),
    _HpicfDownloadErrorText_Type()
)
hpicfDownloadErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadErrorText.setStatus("mandatory")
_HpicfDownloadStatus_Type = RowStatus
_HpicfDownloadStatus_Object = MibTableColumn
hpicfDownloadStatus = _HpicfDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 1, 1, 10),
    _HpicfDownloadStatus_Type()
)
hpicfDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDownloadStatus.setStatus("mandatory")
_HpicfDownloadLogMaxSize_Type = Integer32
_HpicfDownloadLogMaxSize_Object = MibScalar
hpicfDownloadLogMaxSize = _HpicfDownloadLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 2),
    _HpicfDownloadLogMaxSize_Type()
)
hpicfDownloadLogMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadLogMaxSize.setStatus("mandatory")
_HpicfDownloadLogSize_Type = Gauge32
_HpicfDownloadLogSize_Object = MibScalar
hpicfDownloadLogSize = _HpicfDownloadLogSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 3),
    _HpicfDownloadLogSize_Type()
)
hpicfDownloadLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDownloadLogSize.setStatus("mandatory")
_HpicfDownloadLogTable_Object = MibTable
hpicfDownloadLogTable = _HpicfDownloadLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hpicfDownloadLogTable.setStatus("mandatory")
_HpicfDownloadLogEntry_Object = MibTableRow
hpicfDownloadLogEntry = _HpicfDownloadLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1)
)
hpicfDownloadLogEntry.setIndexNames(
    (0, "HP-ICF", "hpicfDlLogIndex"),
)
if mibBuilder.loadTexts:
    hpicfDownloadLogEntry.setStatus("mandatory")
_HpicfDlLogIndex_Type = Integer32
_HpicfDlLogIndex_Object = MibTableColumn
hpicfDlLogIndex = _HpicfDlLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 1),
    _HpicfDlLogIndex_Type()
)
hpicfDlLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogIndex.setStatus("mandatory")
_HpicfDlLogOwnerAddress_Type = TAddress
_HpicfDlLogOwnerAddress_Object = MibTableColumn
hpicfDlLogOwnerAddress = _HpicfDlLogOwnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 2),
    _HpicfDlLogOwnerAddress_Type()
)
hpicfDlLogOwnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogOwnerAddress.setStatus("mandatory")
_HpicfDlLogOwnerDomain_Type = ObjectIdentifier
_HpicfDlLogOwnerDomain_Object = MibTableColumn
hpicfDlLogOwnerDomain = _HpicfDlLogOwnerDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 3),
    _HpicfDlLogOwnerDomain_Type()
)
hpicfDlLogOwnerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogOwnerDomain.setStatus("mandatory")
_HpicfDlLogTAddress_Type = TAddress
_HpicfDlLogTAddress_Object = MibTableColumn
hpicfDlLogTAddress = _HpicfDlLogTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 4),
    _HpicfDlLogTAddress_Type()
)
hpicfDlLogTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogTAddress.setStatus("mandatory")
_HpicfDlLogTDomain_Type = ObjectIdentifier
_HpicfDlLogTDomain_Object = MibTableColumn
hpicfDlLogTDomain = _HpicfDlLogTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 5),
    _HpicfDlLogTDomain_Type()
)
hpicfDlLogTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogTDomain.setStatus("mandatory")


class _HpicfDlLogFilename_Type(DisplayString):
    """Custom type hpicfDlLogFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpicfDlLogFilename_Type.__name__ = "DisplayString"
_HpicfDlLogFilename_Object = MibTableColumn
hpicfDlLogFilename = _HpicfDlLogFilename_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 6),
    _HpicfDlLogFilename_Type()
)
hpicfDlLogFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogFilename.setStatus("mandatory")


class _HpicfDlLogResetType_Type(Integer32):
    """Custom type hpicfDlLogResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 3),
          ("noReset", 1),
          ("warmReset", 2))
    )


_HpicfDlLogResetType_Type.__name__ = "Integer32"
_HpicfDlLogResetType_Object = MibTableColumn
hpicfDlLogResetType = _HpicfDlLogResetType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 7),
    _HpicfDlLogResetType_Type()
)
hpicfDlLogResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogResetType.setStatus("mandatory")


class _HpicfDlLogErrorStatus_Type(Integer32):
    """Custom type hpicfDlLogErrorStatus based on Integer32"""
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
        *(("aborted", 14),
          ("accessViolation", 2),
          ("corruptFile", 9),
          ("diskFull", 3),
          ("fileExists", 6),
          ("fileNotFound", 1),
          ("hardwareError", 12),
          ("illegalOperation", 4),
          ("noServer", 10),
          ("noSuchUser", 7),
          ("notDefined", 8),
          ("success", 13),
          ("tftpTimeout", 11),
          ("unknownTID", 5))
    )


_HpicfDlLogErrorStatus_Type.__name__ = "Integer32"
_HpicfDlLogErrorStatus_Object = MibTableColumn
hpicfDlLogErrorStatus = _HpicfDlLogErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 8),
    _HpicfDlLogErrorStatus_Type()
)
hpicfDlLogErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogErrorStatus.setStatus("mandatory")


class _HpicfDlLogErrorText_Type(DisplayString):
    """Custom type hpicfDlLogErrorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDlLogErrorText_Type.__name__ = "DisplayString"
_HpicfDlLogErrorText_Object = MibTableColumn
hpicfDlLogErrorText = _HpicfDlLogErrorText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3, 4, 1, 9),
    _HpicfDlLogErrorText_Type()
)
hpicfDlLogErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDlLogErrorText.setStatus("mandatory")
_HpicfBasic_ObjectIdentity = ObjectIdentity
hpicfBasic = _HpicfBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4)
)


class _HpicfReset_Type(Integer32):
    """Custom type hpicfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factoryReset", 3),
          ("noReset", 1),
          ("normalReset", 2))
    )


_HpicfReset_Type.__name__ = "Integer32"
_HpicfReset_Object = MibScalar
hpicfReset = _HpicfReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 1),
    _HpicfReset_Type()
)
hpicfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReset.setStatus("mandatory")


class _HpicfSelfTest_Type(Integer32):
    """Custom type hpicfSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stExecute", 2),
          ("stSuccess", 1))
    )


_HpicfSelfTest_Type.__name__ = "Integer32"
_HpicfSelfTest_Object = MibScalar
hpicfSelfTest = _HpicfSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 2),
    _HpicfSelfTest_Type()
)
hpicfSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSelfTest.setStatus("mandatory")
_HpicfRepeater_ObjectIdentity = ObjectIdentity
hpicfRepeater = _HpicfRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2)
)
_HpRptrBasic_ObjectIdentity = ObjectIdentity
hpRptrBasic = _HpRptrBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1)
)
_HpRptrBasicGlobal_ObjectIdentity = ObjectIdentity
hpRptrBasicGlobal = _HpRptrBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1)
)


class _HpRptrEntityName_Type(DisplayString):
    """Custom type hpRptrEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpRptrEntityName_Type.__name__ = "DisplayString"
_HpRptrEntityName_Object = MibScalar
hpRptrEntityName = _HpRptrEntityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 1),
    _HpRptrEntityName_Type()
)
hpRptrEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrEntityName.setStatus("mandatory")
_HpRptrThinlanFault_Type = TruthValue
_HpRptrThinlanFault_Object = MibScalar
hpRptrThinlanFault = _HpRptrThinlanFault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 2),
    _HpRptrThinlanFault_Type()
)
hpRptrThinlanFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrThinlanFault.setStatus("mandatory")
_HpRptrSqeEnabled_Type = TruthValue
_HpRptrSqeEnabled_Object = MibScalar
hpRptrSqeEnabled = _HpRptrSqeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 3),
    _HpRptrSqeEnabled_Type()
)
hpRptrSqeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrSqeEnabled.setStatus("mandatory")
_HpRptrRobustHealing_Type = TruthValue
_HpRptrRobustHealing_Object = MibScalar
hpRptrRobustHealing = _HpRptrRobustHealing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 1, 4),
    _HpRptrRobustHealing_Type()
)
hpRptrRobustHealing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrRobustHealing.setStatus("mandatory")
_HpRptrBasicGroup_ObjectIdentity = ObjectIdentity
hpRptrBasicGroup = _HpRptrBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2)
)
_HpRptrBasicGroupTable_Object = MibTable
hpRptrBasicGroupTable = _HpRptrBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpRptrBasicGroupTable.setStatus("mandatory")
_HpRptrBasicGroupEntry_Object = MibTableRow
hpRptrBasicGroupEntry = _HpRptrBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1)
)
hpRptrBasicGroupEntry.setIndexNames(
    (0, "HP-ICF", "hpRptrGrpGroupIndex"),
)
if mibBuilder.loadTexts:
    hpRptrBasicGroupEntry.setStatus("mandatory")


class _HpRptrGrpGroupIndex_Type(Integer32):
    """Custom type hpRptrGrpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpRptrGrpGroupIndex_Type.__name__ = "Integer32"
_HpRptrGrpGroupIndex_Object = MibTableColumn
hpRptrGrpGroupIndex = _HpRptrGrpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 1),
    _HpRptrGrpGroupIndex_Type()
)
hpRptrGrpGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpGroupIndex.setStatus("mandatory")


class _HpRptrGrpPortsAdminStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsAdminStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsAdminStatus_Object = MibTableColumn
hpRptrGrpPortsAdminStatus = _HpRptrGrpPortsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 2),
    _HpRptrGrpPortsAdminStatus_Type()
)
hpRptrGrpPortsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsAdminStatus.setStatus("mandatory")


class _HpRptrGrpPortsSegStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsSegStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsSegStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsSegStatus_Object = MibTableColumn
hpRptrGrpPortsSegStatus = _HpRptrGrpPortsSegStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 3),
    _HpRptrGrpPortsSegStatus_Type()
)
hpRptrGrpPortsSegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsSegStatus.setStatus("mandatory")


class _HpRptrGrpPortsMediaAvailable_Type(OctetString):
    """Custom type hpRptrGrpPortsMediaAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsMediaAvailable_Type.__name__ = "OctetString"
_HpRptrGrpPortsMediaAvailable_Object = MibTableColumn
hpRptrGrpPortsMediaAvailable = _HpRptrGrpPortsMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 4),
    _HpRptrGrpPortsMediaAvailable_Type()
)
hpRptrGrpPortsMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsMediaAvailable.setStatus("mandatory")


class _HpRptrGrpPortsLinkbeatEnabled_Type(OctetString):
    """Custom type hpRptrGrpPortsLinkbeatEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsLinkbeatEnabled_Type.__name__ = "OctetString"
_HpRptrGrpPortsLinkbeatEnabled_Object = MibTableColumn
hpRptrGrpPortsLinkbeatEnabled = _HpRptrGrpPortsLinkbeatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 5),
    _HpRptrGrpPortsLinkbeatEnabled_Type()
)
hpRptrGrpPortsLinkbeatEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsLinkbeatEnabled.setStatus("mandatory")


class _HpRptrGrpPortsOperStatus_Type(OctetString):
    """Custom type hpRptrGrpPortsOperStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpRptrGrpPortsOperStatus_Type.__name__ = "OctetString"
_HpRptrGrpPortsOperStatus_Object = MibTableColumn
hpRptrGrpPortsOperStatus = _HpRptrGrpPortsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 2, 1, 1, 6),
    _HpRptrGrpPortsOperStatus_Type()
)
hpRptrGrpPortsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrGrpPortsOperStatus.setStatus("mandatory")
_HpRptrBasicPort_ObjectIdentity = ObjectIdentity
hpRptrBasicPort = _HpRptrBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3)
)
_HpRptrBasicPtTable_Object = MibTable
hpRptrBasicPtTable = _HpRptrBasicPtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpRptrBasicPtTable.setStatus("mandatory")
_HpRptrBasicPtEntry_Object = MibTableRow
hpRptrBasicPtEntry = _HpRptrBasicPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1)
)
hpRptrBasicPtEntry.setIndexNames(
    (0, "HP-ICF", "hpRptrPtGroupIndex"),
    (0, "HP-ICF", "hpRptrPtPortIndex"),
)
if mibBuilder.loadTexts:
    hpRptrBasicPtEntry.setStatus("mandatory")


class _HpRptrPtGroupIndex_Type(Integer32):
    """Custom type hpRptrPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpRptrPtGroupIndex_Type.__name__ = "Integer32"
_HpRptrPtGroupIndex_Object = MibTableColumn
hpRptrPtGroupIndex = _HpRptrPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 1),
    _HpRptrPtGroupIndex_Type()
)
hpRptrPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtGroupIndex.setStatus("mandatory")


class _HpRptrPtPortIndex_Type(Integer32):
    """Custom type hpRptrPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpRptrPtPortIndex_Type.__name__ = "Integer32"
_HpRptrPtPortIndex_Object = MibTableColumn
hpRptrPtPortIndex = _HpRptrPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 2),
    _HpRptrPtPortIndex_Type()
)
hpRptrPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtPortIndex.setStatus("mandatory")
_HpRptrPtLinkbeatEnable_Type = TruthValue
_HpRptrPtLinkbeatEnable_Object = MibTableColumn
hpRptrPtLinkbeatEnable = _HpRptrPtLinkbeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 3),
    _HpRptrPtLinkbeatEnable_Type()
)
hpRptrPtLinkbeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpRptrPtLinkbeatEnable.setStatus("mandatory")
_HpRptrPtPolarityReversed_Type = TruthValue
_HpRptrPtPolarityReversed_Object = MibTableColumn
hpRptrPtPolarityReversed = _HpRptrPtPolarityReversed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 1, 3, 1, 1, 4),
    _HpRptrPtPolarityReversed_Type()
)
hpRptrPtPolarityReversed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrPtPolarityReversed.setStatus("mandatory")
_HpRptrMonitor_ObjectIdentity = ObjectIdentity
hpRptrMonitor = _HpRptrMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2)
)
_HpRptrMonitorGlobal_ObjectIdentity = ObjectIdentity
hpRptrMonitorGlobal = _HpRptrMonitorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1)
)
_HpRptrMonCounters_ObjectIdentity = ObjectIdentity
hpRptrMonCounters = _HpRptrMonCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1)
)
_HpRptrMonGlobalFrames_Type = Counter32
_HpRptrMonGlobalFrames_Object = MibScalar
hpRptrMonGlobalFrames = _HpRptrMonGlobalFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 1),
    _HpRptrMonGlobalFrames_Type()
)
hpRptrMonGlobalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFrames.setStatus("mandatory")
_HpRptrMonGlobalOctets_Type = Counter32
_HpRptrMonGlobalOctets_Object = MibScalar
hpRptrMonGlobalOctets = _HpRptrMonGlobalOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 2),
    _HpRptrMonGlobalOctets_Type()
)
hpRptrMonGlobalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalOctets.setStatus("mandatory")
_HpRptrMonGlobalFCSErrors_Type = Counter32
_HpRptrMonGlobalFCSErrors_Object = MibScalar
hpRptrMonGlobalFCSErrors = _HpRptrMonGlobalFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 3),
    _HpRptrMonGlobalFCSErrors_Type()
)
hpRptrMonGlobalFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFCSErrors.setStatus("mandatory")
_HpRptrMonGlobalAlignmentErrors_Type = Counter32
_HpRptrMonGlobalAlignmentErrors_Object = MibScalar
hpRptrMonGlobalAlignmentErrors = _HpRptrMonGlobalAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 4),
    _HpRptrMonGlobalAlignmentErrors_Type()
)
hpRptrMonGlobalAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalAlignmentErrors.setStatus("mandatory")
_HpRptrMonGlobalFrameTooLongs_Type = Counter32
_HpRptrMonGlobalFrameTooLongs_Object = MibScalar
hpRptrMonGlobalFrameTooLongs = _HpRptrMonGlobalFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 5),
    _HpRptrMonGlobalFrameTooLongs_Type()
)
hpRptrMonGlobalFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalFrameTooLongs.setStatus("mandatory")
_HpRptrMonGlobalShortEvents_Type = Counter32
_HpRptrMonGlobalShortEvents_Object = MibScalar
hpRptrMonGlobalShortEvents = _HpRptrMonGlobalShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 6),
    _HpRptrMonGlobalShortEvents_Type()
)
hpRptrMonGlobalShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalShortEvents.setStatus("mandatory")
_HpRptrMonGlobalRunts_Type = Counter32
_HpRptrMonGlobalRunts_Object = MibScalar
hpRptrMonGlobalRunts = _HpRptrMonGlobalRunts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 7),
    _HpRptrMonGlobalRunts_Type()
)
hpRptrMonGlobalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalRunts.setStatus("mandatory")
_HpRptrMonGlobalCollisions_Type = Counter32
_HpRptrMonGlobalCollisions_Object = MibScalar
hpRptrMonGlobalCollisions = _HpRptrMonGlobalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 8),
    _HpRptrMonGlobalCollisions_Type()
)
hpRptrMonGlobalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalCollisions.setStatus("mandatory")
_HpRptrMonGlobalLateEvents_Type = Counter32
_HpRptrMonGlobalLateEvents_Object = MibScalar
hpRptrMonGlobalLateEvents = _HpRptrMonGlobalLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 9),
    _HpRptrMonGlobalLateEvents_Type()
)
hpRptrMonGlobalLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalLateEvents.setStatus("mandatory")
_HpRptrMonGlobalVeryLongEvents_Type = Counter32
_HpRptrMonGlobalVeryLongEvents_Object = MibScalar
hpRptrMonGlobalVeryLongEvents = _HpRptrMonGlobalVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 10),
    _HpRptrMonGlobalVeryLongEvents_Type()
)
hpRptrMonGlobalVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalVeryLongEvents.setStatus("mandatory")
_HpRptrMonGlobalDataRateMismatches_Type = Counter32
_HpRptrMonGlobalDataRateMismatches_Object = MibScalar
hpRptrMonGlobalDataRateMismatches = _HpRptrMonGlobalDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 11),
    _HpRptrMonGlobalDataRateMismatches_Type()
)
hpRptrMonGlobalDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalDataRateMismatches.setStatus("mandatory")
_HpRptrMonGlobalAutoPartitions_Type = Counter32
_HpRptrMonGlobalAutoPartitions_Object = MibScalar
hpRptrMonGlobalAutoPartitions = _HpRptrMonGlobalAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 12),
    _HpRptrMonGlobalAutoPartitions_Type()
)
hpRptrMonGlobalAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalAutoPartitions.setStatus("mandatory")
_HpRptrMonGlobalErrors_Type = Counter32
_HpRptrMonGlobalErrors_Object = MibScalar
hpRptrMonGlobalErrors = _HpRptrMonGlobalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 13),
    _HpRptrMonGlobalErrors_Type()
)
hpRptrMonGlobalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalErrors.setStatus("mandatory")
_HpRptrMonGlobalUcastPackets_Type = Counter32
_HpRptrMonGlobalUcastPackets_Object = MibScalar
hpRptrMonGlobalUcastPackets = _HpRptrMonGlobalUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 14),
    _HpRptrMonGlobalUcastPackets_Type()
)
hpRptrMonGlobalUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalUcastPackets.setStatus("mandatory")
_HpRptrMonGlobalBcastPackets_Type = Counter32
_HpRptrMonGlobalBcastPackets_Object = MibScalar
hpRptrMonGlobalBcastPackets = _HpRptrMonGlobalBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 15),
    _HpRptrMonGlobalBcastPackets_Type()
)
hpRptrMonGlobalBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalBcastPackets.setStatus("mandatory")
_HpRptrMonGlobalMcastPackets_Type = Counter32
_HpRptrMonGlobalMcastPackets_Object = MibScalar
hpRptrMonGlobalMcastPackets = _HpRptrMonGlobalMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 1, 1, 16),
    _HpRptrMonGlobalMcastPackets_Type()
)
hpRptrMonGlobalMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonGlobalMcastPackets.setStatus("mandatory")
_HpRptrMonitorGroup_ObjectIdentity = ObjectIdentity
hpRptrMonitorGroup = _HpRptrMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 2)
)
_HpRptrMonitorPort_ObjectIdentity = ObjectIdentity
hpRptrMonitorPort = _HpRptrMonitorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3)
)
_HpRptrMonPtTable_Object = MibTable
hpRptrMonPtTable = _HpRptrMonPtTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpRptrMonPtTable.setStatus("mandatory")
_HpRptrMonPtEntry_Object = MibTableRow
hpRptrMonPtEntry = _HpRptrMonPtEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1)
)
hpRptrMonPtEntry.setIndexNames(
    (0, "HP-ICF", "hpRptrMonPtGroupIndex"),
    (0, "HP-ICF", "hpRptrMonPtPortIndex"),
)
if mibBuilder.loadTexts:
    hpRptrMonPtEntry.setStatus("mandatory")


class _HpRptrMonPtGroupIndex_Type(Integer32):
    """Custom type hpRptrMonPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpRptrMonPtGroupIndex_Type.__name__ = "Integer32"
_HpRptrMonPtGroupIndex_Object = MibTableColumn
hpRptrMonPtGroupIndex = _HpRptrMonPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 1),
    _HpRptrMonPtGroupIndex_Type()
)
hpRptrMonPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtGroupIndex.setStatus("mandatory")


class _HpRptrMonPtPortIndex_Type(Integer32):
    """Custom type hpRptrMonPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpRptrMonPtPortIndex_Type.__name__ = "Integer32"
_HpRptrMonPtPortIndex_Object = MibTableColumn
hpRptrMonPtPortIndex = _HpRptrMonPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 2),
    _HpRptrMonPtPortIndex_Type()
)
hpRptrMonPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtPortIndex.setStatus("mandatory")
_HpRptrMonPtUcastPackets_Type = Counter32
_HpRptrMonPtUcastPackets_Object = MibTableColumn
hpRptrMonPtUcastPackets = _HpRptrMonPtUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 3),
    _HpRptrMonPtUcastPackets_Type()
)
hpRptrMonPtUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtUcastPackets.setStatus("mandatory")
_HpRptrMonPtBcastPackets_Type = Counter32
_HpRptrMonPtBcastPackets_Object = MibTableColumn
hpRptrMonPtBcastPackets = _HpRptrMonPtBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 4),
    _HpRptrMonPtBcastPackets_Type()
)
hpRptrMonPtBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtBcastPackets.setStatus("mandatory")
_HpRptrMonPtMcastPackets_Type = Counter32
_HpRptrMonPtMcastPackets_Object = MibTableColumn
hpRptrMonPtMcastPackets = _HpRptrMonPtMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 2, 3, 1, 1, 5),
    _HpRptrMonPtMcastPackets_Type()
)
hpRptrMonPtMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpRptrMonPtMcastPackets.setStatus("mandatory")
_HpRptrAddrTrack_ObjectIdentity = ObjectIdentity
hpRptrAddrTrack = _HpRptrAddrTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 3)
)
_HpRptrAddrTrkGlobal_ObjectIdentity = ObjectIdentity
hpRptrAddrTrkGlobal = _HpRptrAddrTrkGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 3, 1)
)
_HpRptrAddrTrkGroup_ObjectIdentity = ObjectIdentity
hpRptrAddrTrkGroup = _HpRptrAddrTrkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 3, 2)
)
_HpRptrAddrTrkPort_ObjectIdentity = ObjectIdentity
hpRptrAddrTrkPort = _HpRptrAddrTrkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2, 3, 3)
)
_HpicfVg_ObjectIdentity = ObjectIdentity
hpicfVg = _HpicfVg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3)
)
_HpVgBasic_ObjectIdentity = ObjectIdentity
hpVgBasic = _HpVgBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1)
)
_HpVgBasicGlobal_ObjectIdentity = ObjectIdentity
hpVgBasicGlobal = _HpVgBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1)
)


class _HpVgEntityName_Type(DisplayString):
    """Custom type hpVgEntityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_HpVgEntityName_Type.__name__ = "DisplayString"
_HpVgEntityName_Object = MibScalar
hpVgEntityName = _HpVgEntityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 1, 1),
    _HpVgEntityName_Type()
)
hpVgEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgEntityName.setStatus("mandatory")
_HpVgBasicGroup_ObjectIdentity = ObjectIdentity
hpVgBasicGroup = _HpVgBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2)
)
_HpVgBasicGroupTable_Object = MibTable
hpVgBasicGroupTable = _HpVgBasicGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpVgBasicGroupTable.setStatus("mandatory")
_HpVgBasicGroupEntry_Object = MibTableRow
hpVgBasicGroupEntry = _HpVgBasicGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1)
)
hpVgBasicGroupEntry.setIndexNames(
    (0, "HP-ICF", "hpVgGrpGroupIndex"),
)
if mibBuilder.loadTexts:
    hpVgBasicGroupEntry.setStatus("mandatory")


class _HpVgGrpGroupIndex_Type(Integer32):
    """Custom type hpVgGrpGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgGrpGroupIndex_Type.__name__ = "Integer32"
_HpVgGrpGroupIndex_Object = MibTableColumn
hpVgGrpGroupIndex = _HpVgGrpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 1),
    _HpVgGrpGroupIndex_Type()
)
hpVgGrpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgGrpGroupIndex.setStatus("mandatory")


class _HpVgGrpPortsAdminStatus_Type(OctetString):
    """Custom type hpVgGrpPortsAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsAdminStatus_Type.__name__ = "OctetString"
_HpVgGrpPortsAdminStatus_Object = MibTableColumn
hpVgGrpPortsAdminStatus = _HpVgGrpPortsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 2),
    _HpVgGrpPortsAdminStatus_Type()
)
hpVgGrpPortsAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsAdminStatus.setStatus("mandatory")


class _HpVgGrpPortsTrained_Type(OctetString):
    """Custom type hpVgGrpPortsTrained based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsTrained_Type.__name__ = "OctetString"
_HpVgGrpPortsTrained_Object = MibTableColumn
hpVgGrpPortsTrained = _HpVgGrpPortsTrained_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 3),
    _HpVgGrpPortsTrained_Type()
)
hpVgGrpPortsTrained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsTrained.setStatus("mandatory")


class _HpVgGrpPortsInTraining_Type(OctetString):
    """Custom type hpVgGrpPortsInTraining based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsInTraining_Type.__name__ = "OctetString"
_HpVgGrpPortsInTraining_Object = MibTableColumn
hpVgGrpPortsInTraining = _HpVgGrpPortsInTraining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 4),
    _HpVgGrpPortsInTraining_Type()
)
hpVgGrpPortsInTraining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsInTraining.setStatus("mandatory")


class _HpVgGrpPortsCascaded_Type(OctetString):
    """Custom type hpVgGrpPortsCascaded based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsCascaded_Type.__name__ = "OctetString"
_HpVgGrpPortsCascaded_Object = MibTableColumn
hpVgGrpPortsCascaded = _HpVgGrpPortsCascaded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 5),
    _HpVgGrpPortsCascaded_Type()
)
hpVgGrpPortsCascaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsCascaded.setStatus("mandatory")


class _HpVgGrpPortsPromiscuous_Type(OctetString):
    """Custom type hpVgGrpPortsPromiscuous based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpVgGrpPortsPromiscuous_Type.__name__ = "OctetString"
_HpVgGrpPortsPromiscuous_Object = MibTableColumn
hpVgGrpPortsPromiscuous = _HpVgGrpPortsPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 2, 1, 1, 6),
    _HpVgGrpPortsPromiscuous_Type()
)
hpVgGrpPortsPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgGrpPortsPromiscuous.setStatus("mandatory")
_HpVgBasicPort_ObjectIdentity = ObjectIdentity
hpVgBasicPort = _HpVgBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3)
)
_HpVgBasicPortTable_Object = MibTable
hpVgBasicPortTable = _HpVgBasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpVgBasicPortTable.setStatus("mandatory")
_HpVgBasicPortEntry_Object = MibTableRow
hpVgBasicPortEntry = _HpVgBasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1)
)
hpVgBasicPortEntry.setIndexNames(
    (0, "HP-ICF", "hpVgPortGroupIndex"),
    (0, "HP-ICF", "hpVgPortIndex"),
)
if mibBuilder.loadTexts:
    hpVgBasicPortEntry.setStatus("mandatory")


class _HpVgPortGroupIndex_Type(Integer32):
    """Custom type hpVgPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgPortGroupIndex_Type.__name__ = "Integer32"
_HpVgPortGroupIndex_Object = MibTableColumn
hpVgPortGroupIndex = _HpVgPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 1),
    _HpVgPortGroupIndex_Type()
)
hpVgPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgPortGroupIndex.setStatus("mandatory")


class _HpVgPortIndex_Type(Integer32):
    """Custom type hpVgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpVgPortIndex_Type.__name__ = "Integer32"
_HpVgPortIndex_Object = MibTableColumn
hpVgPortIndex = _HpVgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 2),
    _HpVgPortIndex_Type()
)
hpVgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpVgPortIndex.setStatus("mandatory")
_HpVgPortPolarityReversed_Type = TruthValue
_HpVgPortPolarityReversed_Object = MibTableColumn
hpVgPortPolarityReversed = _HpVgPortPolarityReversed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 3),
    _HpVgPortPolarityReversed_Type()
)
hpVgPortPolarityReversed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgPortPolarityReversed.setStatus("mandatory")
_HpVgPortWireSkewError_Type = TruthValue
_HpVgPortWireSkewError_Object = MibTableColumn
hpVgPortWireSkewError = _HpVgPortWireSkewError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 1, 3, 1, 1, 4),
    _HpVgPortWireSkewError_Type()
)
hpVgPortWireSkewError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgPortWireSkewError.setStatus("mandatory")
_HpVgMonitor_ObjectIdentity = ObjectIdentity
hpVgMonitor = _HpVgMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2)
)
_HpVgMonitorGlobal_ObjectIdentity = ObjectIdentity
hpVgMonitorGlobal = _HpVgMonitorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1)
)
_HpVgMonCounters_ObjectIdentity = ObjectIdentity
hpVgMonCounters = _HpVgMonCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1)
)
_HpVgMonGlbReadableFrames_Type = Counter32
_HpVgMonGlbReadableFrames_Object = MibScalar
hpVgMonGlbReadableFrames = _HpVgMonGlbReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 1),
    _HpVgMonGlbReadableFrames_Type()
)
hpVgMonGlbReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbReadableFrames.setStatus("mandatory")
_HpVgMonGlbReadableOctets_Type = Counter32
_HpVgMonGlbReadableOctets_Object = MibScalar
hpVgMonGlbReadableOctets = _HpVgMonGlbReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 2),
    _HpVgMonGlbReadableOctets_Type()
)
hpVgMonGlbReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbReadableOctets.setStatus("mandatory")
_HpVgMonGlbUnreadableOctets_Type = Counter32
_HpVgMonGlbUnreadableOctets_Object = MibScalar
hpVgMonGlbUnreadableOctets = _HpVgMonGlbUnreadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 3),
    _HpVgMonGlbUnreadableOctets_Type()
)
hpVgMonGlbUnreadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbUnreadableOctets.setStatus("mandatory")
_HpVgMonGlbHighPriorityFrames_Type = Counter32
_HpVgMonGlbHighPriorityFrames_Object = MibScalar
hpVgMonGlbHighPriorityFrames = _HpVgMonGlbHighPriorityFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 4),
    _HpVgMonGlbHighPriorityFrames_Type()
)
hpVgMonGlbHighPriorityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHighPriorityFrames.setStatus("mandatory")
_HpVgMonGlbHighPriorityOctets_Type = Counter32
_HpVgMonGlbHighPriorityOctets_Object = MibScalar
hpVgMonGlbHighPriorityOctets = _HpVgMonGlbHighPriorityOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 5),
    _HpVgMonGlbHighPriorityOctets_Type()
)
hpVgMonGlbHighPriorityOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbHighPriorityOctets.setStatus("mandatory")
_HpVgMonGlbBroadcastFrames_Type = Counter32
_HpVgMonGlbBroadcastFrames_Object = MibScalar
hpVgMonGlbBroadcastFrames = _HpVgMonGlbBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 6),
    _HpVgMonGlbBroadcastFrames_Type()
)
hpVgMonGlbBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbBroadcastFrames.setStatus("mandatory")
_HpVgMonGlbMulticastFrames_Type = Counter32
_HpVgMonGlbMulticastFrames_Object = MibScalar
hpVgMonGlbMulticastFrames = _HpVgMonGlbMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 7),
    _HpVgMonGlbMulticastFrames_Type()
)
hpVgMonGlbMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbMulticastFrames.setStatus("mandatory")
_HpVgMonGlbIPMFrames_Type = Counter32
_HpVgMonGlbIPMFrames_Object = MibScalar
hpVgMonGlbIPMFrames = _HpVgMonGlbIPMFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 8),
    _HpVgMonGlbIPMFrames_Type()
)
hpVgMonGlbIPMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbIPMFrames.setStatus("mandatory")
_HpVgMonGlbDataErrorFrames_Type = Counter32
_HpVgMonGlbDataErrorFrames_Object = MibScalar
hpVgMonGlbDataErrorFrames = _HpVgMonGlbDataErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 9),
    _HpVgMonGlbDataErrorFrames_Type()
)
hpVgMonGlbDataErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbDataErrorFrames.setStatus("mandatory")
_HpVgMonGlbPriorityPromotions_Type = Counter32
_HpVgMonGlbPriorityPromotions_Object = MibScalar
hpVgMonGlbPriorityPromotions = _HpVgMonGlbPriorityPromotions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 1, 1, 10),
    _HpVgMonGlbPriorityPromotions_Type()
)
hpVgMonGlbPriorityPromotions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpVgMonGlbPriorityPromotions.setStatus("mandatory")
_HpVgMonitorGroup_ObjectIdentity = ObjectIdentity
hpVgMonitorGroup = _HpVgMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 2)
)
_HpVgMonitorPort_ObjectIdentity = ObjectIdentity
hpVgMonitorPort = _HpVgMonitorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3, 2, 3)
)
_HpicfGenericRepeater_ObjectIdentity = ObjectIdentity
hpicfGenericRepeater = _HpicfGenericRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4)
)
_HpGRpBasic_ObjectIdentity = ObjectIdentity
hpGRpBasic = _HpGRpBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1)
)
_HpGRpBasicGlobal_ObjectIdentity = ObjectIdentity
hpGRpBasicGlobal = _HpGRpBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1)
)


class _HpGRpSelfHealEnable_Type(Integer32):
    """Custom type hpGRpSelfHealEnable based on Integer32"""
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


_HpGRpSelfHealEnable_Type.__name__ = "Integer32"
_HpGRpSelfHealEnable_Object = MibScalar
hpGRpSelfHealEnable = _HpGRpSelfHealEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 1),
    _HpGRpSelfHealEnable_Type()
)
hpGRpSelfHealEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpSelfHealEnable.setStatus("mandatory")
_HpGRpBasicGroup_ObjectIdentity = ObjectIdentity
hpGRpBasicGroup = _HpGRpBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 2)
)
_HpGRpBasicPort_ObjectIdentity = ObjectIdentity
hpGRpBasicPort = _HpGRpBasicPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 3)
)
_HpGRpMonitor_ObjectIdentity = ObjectIdentity
hpGRpMonitor = _HpGRpMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2)
)
_HpGRpAddrTrack_ObjectIdentity = ObjectIdentity
hpGRpAddrTrack = _HpGRpAddrTrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3)
)
_HpicfNotifications_ObjectIdentity = ObjectIdentity
hpicfNotifications = _HpicfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12)
)
_HpicfCommonTraps_ObjectIdentity = ObjectIdentity
hpicfCommonTraps = _HpicfCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1)
)
_Hpicf8023RptrTraps_ObjectIdentity = ObjectIdentity
hpicf8023RptrTraps = _Hpicf8023RptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2)
)
_HpicfVgRptrTraps_ObjectIdentity = ObjectIdentity
hpicfVgRptrTraps = _HpicfVgRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3)
)
_HpicfGenRptrTraps_ObjectIdentity = ObjectIdentity
hpicfGenRptrTraps = _HpicfGenRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 4)
)

# Managed Objects groups


# Notification objects

thresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 0, 0)
)
thresholdTrap.setObjects(
      *(("HP-ICF", "evthObject"),
        ("HP-ICF", "evthThreshold"),
        ("HP-ICF", "evthHysteresis"),
        ("HP-ICF", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrap.setStatus(
        ""
    )

linkBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 3)
)
linkBeatTrap.setObjects(
    ("HP-ICF", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrap.setStatus(
        ""
    )

segmentationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 4)
)
segmentationTrap.setObjects(
    ("HP-ICF", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrap.setStatus(
        ""
    )

backupLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 5)
)
backupLinkTrap.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrap.setStatus(
        ""
    )

intrusionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 6)
)
intrusionTrap.setObjects(
      *(("HP-ICF", "hubIntruderAddress"),
        ("HP-ICF", "hubIntruderPort"))
)
if mibBuilder.loadTexts:
    intrusionTrap.setStatus(
        ""
    )

addressMovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 7)
)
addressMovedTrap.setObjects(
      *(("HP-ICF", "hubAddrMoveAddress"),
        ("HP-ICF", "hubAddrMoveOldGroup"),
        ("HP-ICF", "hubAddrMoveOldPort"),
        ("HP-ICF", "hubAddrMoveNewGroup"),
        ("HP-ICF", "hubAddrMoveNewPort"))
)
if mibBuilder.loadTexts:
    addressMovedTrap.setStatus(
        ""
    )

newAddressTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 0, 8)
)
newAddressTrap.setObjects(
    ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress")
)
if mibBuilder.loadTexts:
    newAddressTrap.setStatus(
        ""
    )

stpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 0, 3)
)
stpTrap.setObjects(
    ("HP-ICF", "stpPortState")
)
if mibBuilder.loadTexts:
    stpTrap.setStatus(
        ""
    )

temperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3, 0, 4)
)
if mibBuilder.loadTexts:
    temperatureTrap.setStatus(
        ""
    )

hpicfChainAddition = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 1)
)
hpicfChainAddition.setObjects(
    ("HP-ICF", "hpicfChainId")
)
if mibBuilder.loadTexts:
    hpicfChainAddition.setStatus(
        ""
    )

hpicfChainRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 2)
)
hpicfChainRemoval.setObjects(
    ("HP-ICF", "hpicfChainId")
)
if mibBuilder.loadTexts:
    hpicfChainRemoval.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF",
    **{"MacAddress": MacAddress,
       "TimeStamp": TimeStamp,
       "TruthValue": TruthValue,
       "RowStatus": RowStatus,
       "TAddress": TAddress,
       "hp": hp,
       "nm": nm,
       "hpSystem": hpSystem,
       "netElement": netElement,
       "bridge": bridge,
       "bridge1010": bridge1010,
       "bridgeRemote": bridgeRemote,
       "eswitch": eswitch,
       "router": router,
       "icfRouterER": icfRouterER,
       "icfRouterTR": icfRouterTR,
       "icfRouterSR": icfRouterSR,
       "icfRouterFR": icfRouterFR,
       "icfRouterLR": icfRouterLR,
       "icfRouterBR": icfRouterBR,
       "icfRouterPR": icfRouterPR,
       "icfRouter650": icfRouter650,
       "icfRouter650Engine": icfRouter650Engine,
       "icfRouter650Port4E": icfRouter650Port4E,
       "icfRouter650Port4S": icfRouter650Port4S,
       "icfRouter650Port4T": icfRouter650Port4T,
       "icfRouter230": icfRouter230,
       "icfRouter250": icfRouter250,
       "icfRouter255": icfRouter255,
       "icfRouter210": icfRouter210,
       "hub": hub,
       "etherTwist12": etherTwist12,
       "fiberOptic": fiberOptic,
       "etherTwist48": etherTwist48,
       "thinLAN": thinLAN,
       "etherTwist24S": etherTwist24S,
       "advStack12": advStack12,
       "advStack24": advStack24,
       "advStack48": advStack48,
       "advStackVg15": advStackVg15,
       "advStackU8": advStackU8,
       "advStackU16": advStackU16,
       "chassis": chassis,
       "repeaterAgent": repeaterAgent,
       "chassisAgents": chassisAgents,
       "icfVgAgent": icfVgAgent,
       "icfEnetAgent": icfEnetAgent,
       "icfSensors": icfSensors,
       "icfPowerSupplySensor": icfPowerSupplySensor,
       "icfFanSensor": icfFanSensor,
       "icfTemperatureSensor": icfTemperatureSensor,
       "icf": icf,
       "icfCommon": icfCommon,
       "thresholdTrap": thresholdTrap,
       "lastSetError": lastSetError,
       "password": password,
       "reset": reset,
       "selfTest": selfTest,
       "semaphore": semaphore,
       "discovery": discovery,
       "pollResponse": pollResponse,
       "announceAddress": announceAddress,
       "mapAddress": mapAddress,
       "mapState": mapState,
       "mapPort": mapPort,
       "ipSubnetMask": ipSubnetMask,
       "icfEvent": icfEvent,
       "eventNotificationNode": eventNotificationNode,
       "evtIpNotify": evtIpNotify,
       "evtIpxNotify": evtIpxNotify,
       "evtTable": evtTable,
       "evtIndex": evtIndex,
       "evtArm": evtArm,
       "evtTimeSinceOccurrence": evtTimeSinceOccurrence,
       "evtThresholdTable": evtThresholdTable,
       "evthIndex": evthIndex,
       "evthArm": evthArm,
       "evthObject": evthObject,
       "evthThreshold": evthThreshold,
       "evthHysteresis": evthHysteresis,
       "evthTimeInterval": evthTimeInterval,
       "evthTimeSinceOccurrence": evthTimeSinceOccurrence,
       "linkTest": linkTest,
       "linkTestAddress": linkTestAddress,
       "linkTest802MacAddress": linkTest802MacAddress,
       "linkTestIpAddress": linkTestIpAddress,
       "linkTestIpxAddress": linkTestIpxAddress,
       "linkTestRepetitions": linkTestRepetitions,
       "linkTestSuccess": linkTestSuccess,
       "linkTestTimeout": linkTestTimeout,
       "icf8023MacTable": icf8023MacTable,
       "icf8023MacIndex": icf8023MacIndex,
       "icf8023MacInBroadcastPkts": icf8023MacInBroadcastPkts,
       "icf8023MacOutBroadcastPkts": icf8023MacOutBroadcastPkts,
       "icf8023MacInMulticastPkts": icf8023MacInMulticastPkts,
       "icf8023MacOutMulticastPkts": icf8023MacOutMulticastPkts,
       "icf8023MacRunts": icf8023MacRunts,
       "icf8023MacGiants": icf8023MacGiants,
       "icf8023MacMissedPktErrors": icf8023MacMissedPktErrors,
       "icf8023MacExcessDeferrals": icf8023MacExcessDeferrals,
       "icf8023MacTotalMediaErrors": icf8023MacTotalMediaErrors,
       "icf8023MacSpuriousIntrs": icf8023MacSpuriousIntrs,
       "icfDownload": icfDownload,
       "icfDownloadAddress": icfDownloadAddress,
       "icfDownloadIpAddress": icfDownloadIpAddress,
       "icfDownloadIpxAddress": icfDownloadIpxAddress,
       "icfDownloadFilename": icfDownloadFilename,
       "icfHub": icfHub,
       "linkBeatTrap": linkBeatTrap,
       "segmentationTrap": segmentationTrap,
       "backupLinkTrap": backupLinkTrap,
       "intrusionTrap": intrusionTrap,
       "addressMovedTrap": addressMovedTrap,
       "newAddressTrap": newAddressTrap,
       "hubThinlanFault": hubThinlanFault,
       "hubGlobal": hubGlobal,
       "hubGlobalErrors": hubGlobalErrors,
       "hubGlobalCollisions": hubGlobalCollisions,
       "hubGlobalPktFragments": hubGlobalPktFragments,
       "hubGlobalRunts": hubGlobalRunts,
       "hubGlobalGiants": hubGlobalGiants,
       "hubGlobalCrcErrors": hubGlobalCrcErrors,
       "hubGlobalAlignmentErrors": hubGlobalAlignmentErrors,
       "hubGlobalInOctets": hubGlobalInOctets,
       "hubGlobalInUcastPkts": hubGlobalInUcastPkts,
       "hubGlobalInNUcastPkts": hubGlobalInNUcastPkts,
       "hubGlobalInBroadcastPkts": hubGlobalInBroadcastPkts,
       "hubPortTable": hubPortTable,
       "hubPortIndex": hubPortIndex,
       "hubPortPktFragments": hubPortPktFragments,
       "hubPortCollisions": hubPortCollisions,
       "hubPortSegmentation": hubPortSegmentation,
       "hubPortLinkBeatStatus": hubPortLinkBeatStatus,
       "hubPortLinkBeatEnable": hubPortLinkBeatEnable,
       "hubPortMacAddress": hubPortMacAddress,
       "hubPortAddressState": hubPortAddressState,
       "hubPortPolarityReversed": hubPortPolarityReversed,
       "hubPortLateEventDisable": hubPortLateEventDisable,
       "hubBitmaps": hubBitmaps,
       "hubPortsOperStatus": hubPortsOperStatus,
       "hubAddressTableMaxAge": hubAddressTableMaxAge,
       "hubAddressTable": hubAddressTable,
       "hubAddressIndex": hubAddressIndex,
       "hubAddressChunk": hubAddressChunk,
       "hubNumBkpLinks": hubNumBkpLinks,
       "hubBkpLinkTable": hubBkpLinkTable,
       "hubBkpLinkIndex": hubBkpLinkIndex,
       "hubBackupPort": hubBackupPort,
       "hubPrimaryPort": hubPrimaryPort,
       "hubBackupAddress": hubBackupAddress,
       "hubBackupTestTime": hubBackupTestTime,
       "hubBackupConsecutiveFails": hubBackupConsecutiveFails,
       "hubSqeEnabled": hubSqeEnabled,
       "hubSecurity": hubSecurity,
       "hubSecurePortTable": hubSecurePortTable,
       "hubSecurePortEntry": hubSecurePortEntry,
       "hubSecPtGroupIndex": hubSecPtGroupIndex,
       "hubSecPtPortIndex": hubSecPtPortIndex,
       "hubSecPtSecurityAddress": hubSecPtSecurityAddress,
       "hubSecPtAuthorizedAddress": hubSecPtAuthorizedAddress,
       "hubSecPtPreventEavesdrop": hubSecPtPreventEavesdrop,
       "hubSecPtAlarmEnable": hubSecPtAlarmEnable,
       "hubSecPtIntrusionFlag": hubSecPtIntrusionFlag,
       "hubIntruderLogTable": hubIntruderLogTable,
       "hubIntruderLogEntry": hubIntruderLogEntry,
       "hubIntruderIndex": hubIntruderIndex,
       "hubIntruderGroup": hubIntruderGroup,
       "hubIntruderPort": hubIntruderPort,
       "hubIntruderAddress": hubIntruderAddress,
       "hubIntruderTime": hubIntruderTime,
       "hubAddressMoveLogTable": hubAddressMoveLogTable,
       "hubAddressMoveLogEntry": hubAddressMoveLogEntry,
       "hubAddrMoveIndex": hubAddrMoveIndex,
       "hubAddrMoveAddress": hubAddrMoveAddress,
       "hubAddrMoveOldGroup": hubAddrMoveOldGroup,
       "hubAddrMoveOldPort": hubAddrMoveOldPort,
       "hubAddrMoveNewGroup": hubAddrMoveNewGroup,
       "hubAddrMoveNewPort": hubAddrMoveNewPort,
       "hubLateEventMonitor": hubLateEventMonitor,
       "icfBridge": icfBridge,
       "stpTrap": stpTrap,
       "temperatureTrap": temperatureTrap,
       "operationalState": operationalState,
       "forwardDbMaxAge": forwardDbMaxAge,
       "addressTable": addressTable,
       "addressIndex": addressIndex,
       "addressChunk": addressChunk,
       "brgPortTable": brgPortTable,
       "brgPortIndex": brgPortIndex,
       "brgPortCacheHits": brgPortCacheHits,
       "brgPortCacheMisses": brgPortCacheMisses,
       "brgPortForwardedPkts": brgPortForwardedPkts,
       "brgPortFilteredPkts": brgPortFilteredPkts,
       "wildcardTable": wildcardTable,
       "wildcardIndex": wildcardIndex,
       "wildcardFilter": wildcardFilter,
       "wildcardMask": wildcardMask,
       "wildcardOffset": wildcardOffset,
       "wildcardUserOffset": wildcardUserOffset,
       "wildcardArm": wildcardArm,
       "stp": stp,
       "stpBridgeId": stpBridgeId,
       "stpTopoChangeTime": stpTopoChangeTime,
       "stpTopoNumChanges": stpTopoNumChanges,
       "stpTopoChange": stpTopoChange,
       "stpDesignatedRoot": stpDesignatedRoot,
       "stpRootCost": stpRootCost,
       "stpRootPort": stpRootPort,
       "stpCurrentMaxAge": stpCurrentMaxAge,
       "stpCurrentHelloTime": stpCurrentHelloTime,
       "stpCurrentForwardDelay": stpCurrentForwardDelay,
       "stpMaxAge": stpMaxAge,
       "stpHelloTime": stpHelloTime,
       "stpForwardDelay": stpForwardDelay,
       "stpPriority": stpPriority,
       "stpPortTable": stpPortTable,
       "stpPortIndex": stpPortIndex,
       "stpPortState": stpPortState,
       "stpPortId": stpPortId,
       "stpPortPathCost": stpPortPathCost,
       "stpPortRootId": stpPortRootId,
       "stpPortDesignatedCost": stpPortDesignatedCost,
       "stpPortDesignatedBridge": stpPortDesignatedBridge,
       "stpPortDesignatedPort": stpPortDesignatedPort,
       "stpPortPriority": stpPortPriority,
       "hdlcErrorTable": hdlcErrorTable,
       "hdlcErrorIndex": hdlcErrorIndex,
       "hdlcErrorIndications": hdlcErrorIndications,
       "hdlcT1Timeouts": hdlcT1Timeouts,
       "hdlcMissedPackets": hdlcMissedPackets,
       "hdlcRcvOverruns": hdlcRcvOverruns,
       "hdlcXmtUnderruns": hdlcXmtUnderruns,
       "hdlcProviderLostPrimitives": hdlcProviderLostPrimitives,
       "hdlcRuntFrameReceives": hdlcRuntFrameReceives,
       "hdlcGiantFrameReceives": hdlcGiantFrameReceives,
       "hdlcBadFrameReceives": hdlcBadFrameReceives,
       "hdlcRejectFrameReceives": hdlcRejectFrameReceives,
       "hdlcRejectFrameSends": hdlcRejectFrameSends,
       "hdlcFrameRejectFrameRecs": hdlcFrameRejectFrameRecs,
       "hdlcLocalTable": hdlcLocalTable,
       "hdlcLocalIndex": hdlcLocalIndex,
       "hdlcLocalResetRequests": hdlcLocalResetRequests,
       "hdlcLocalResetConfirms": hdlcLocalResetConfirms,
       "hdlcLocalConnectRequests": hdlcLocalConnectRequests,
       "hdlcLocalConnectConfirms": hdlcLocalConnectConfirms,
       "hdlcLocalDisconnectRequests": hdlcLocalDisconnectRequests,
       "hdlcLocalDisconnectConfirms": hdlcLocalDisconnectConfirms,
       "hdlcLocalState": hdlcLocalState,
       "hdlcLocalAddress": hdlcLocalAddress,
       "hdlcLocalPhase": hdlcLocalPhase,
       "hdlcRemoteTable": hdlcRemoteTable,
       "hdlcRemoteIndex": hdlcRemoteIndex,
       "hdlcRemoteResetRequests": hdlcRemoteResetRequests,
       "hdlcRemoteResetConfirms": hdlcRemoteResetConfirms,
       "hdlcRemoteConnectRequests": hdlcRemoteConnectRequests,
       "hdlcRemoteConnectConfirms": hdlcRemoteConnectConfirms,
       "hdlcRemoteDisconnectRequests": hdlcRemoteDisconnectRequests,
       "hdlcRemoteState": hdlcRemoteState,
       "hdlcRemoteAddress": hdlcRemoteAddress,
       "hdlcRemoteXidCommands": hdlcRemoteXidCommands,
       "hdlcRemoteXidResponses": hdlcRemoteXidResponses,
       "hdlcRemoteTestCommands": hdlcRemoteTestCommands,
       "hdlcRemoteTestResponses": hdlcRemoteTestResponses,
       "hdlcRemoteNodeId": hdlcRemoteNodeId,
       "x25Table": x25Table,
       "x25Index": x25Index,
       "x25T1Timer": x25T1Timer,
       "x25N2Count": x25N2Count,
       "x25T3Timer": x25T3Timer,
       "icfSecurity": icfSecurity,
       "icfSecurPassword": icfSecurPassword,
       "icfSecurAuthAnyMgr": icfSecurAuthAnyMgr,
       "icfSecurAuthMgrTable": icfSecurAuthMgrTable,
       "icfSecurAuthMgrEntry": icfSecurAuthMgrEntry,
       "icfAuthMgrIndex": icfAuthMgrIndex,
       "icfAuthMgrIpAddress": icfAuthMgrIpAddress,
       "icfAuthMgrIpxAddress": icfAuthMgrIpxAddress,
       "icfAuthMgrRcvTraps": icfAuthMgrRcvTraps,
       "icfSecurIntruder": icfSecurIntruder,
       "icfSecurIntruderFlag": icfSecurIntruderFlag,
       "icfSecurIntruderIpAddress": icfSecurIntruderIpAddress,
       "icfSecurIntruderIpxAddress": icfSecurIntruderIpxAddress,
       "icfSecurIntruderTime": icfSecurIntruderTime,
       "icfConfig": icfConfig,
       "icfConfigIfTable": icfConfigIfTable,
       "icfConfigIfEntry": icfConfigIfEntry,
       "icfConfigIfIndex": icfConfigIfIndex,
       "icfConfigIfIpAddress": icfConfigIfIpAddress,
       "icfConfigIfNetMask": icfConfigIfNetMask,
       "icfConfigIfDefaultGate": icfConfigIfDefaultGate,
       "icfConfigIpTTL": icfConfigIpTTL,
       "icfConfigBootpEnable": icfConfigBootpEnable,
       "icfDot12Draft": icfDot12Draft,
       "icfVgRepeater": icfVgRepeater,
       "icfVgBasic": icfVgBasic,
       "icfVgBasicRptr": icfVgBasicRptr,
       "icfVgMACAddress": icfVgMACAddress,
       "icfVgCurrentFramingType": icfVgCurrentFramingType,
       "icfVgDesiredFramingType": icfVgDesiredFramingType,
       "icfVgFramingCapability": icfVgFramingCapability,
       "icfVgTrainingVersion": icfVgTrainingVersion,
       "icfVgRepeaterGroupCapacity": icfVgRepeaterGroupCapacity,
       "icfVgRepeaterHealthState": icfVgRepeaterHealthState,
       "icfVgRepeaterHealthText": icfVgRepeaterHealthText,
       "icfVgRepeaterReset": icfVgRepeaterReset,
       "icfVgRepeaterNonDisruptTest": icfVgRepeaterNonDisruptTest,
       "icfVgBasicGroup": icfVgBasicGroup,
       "icfVgBasicGroupTable": icfVgBasicGroupTable,
       "icfVgBasicGroupEntry": icfVgBasicGroupEntry,
       "icfVgGroupIndex": icfVgGroupIndex,
       "icfVgGroupDescr": icfVgGroupDescr,
       "icfVgGroupObjectID": icfVgGroupObjectID,
       "icfVgGroupOperStatus": icfVgGroupOperStatus,
       "icfVgGroupLastOperStatusChange": icfVgGroupLastOperStatusChange,
       "icfVgGroupPortCapacity": icfVgGroupPortCapacity,
       "icfVgGroupCablesBundled": icfVgGroupCablesBundled,
       "icfVgBasicPort": icfVgBasicPort,
       "icfVgBasicPortTable": icfVgBasicPortTable,
       "icfVgBasicPortEntry": icfVgBasicPortEntry,
       "icfVgPortGroupIndex": icfVgPortGroupIndex,
       "icfVgPortIndex": icfVgPortIndex,
       "icfVgPortType": icfVgPortType,
       "icfVgPortAdminStatus": icfVgPortAdminStatus,
       "icfVgPortStatus": icfVgPortStatus,
       "icfVgPortSupportedPromiscMode": icfVgPortSupportedPromiscMode,
       "icfVgPortSupportedCascadeMode": icfVgPortSupportedCascadeMode,
       "icfVgPortAllowedTrainType": icfVgPortAllowedTrainType,
       "icfVgPortLastTrainConfig": icfVgPortLastTrainConfig,
       "icfVgPortTrainingResult": icfVgPortTrainingResult,
       "icfVgPortPriorityEnable": icfVgPortPriorityEnable,
       "icfVgPortMediaType": icfVgPortMediaType,
       "icfVgMonitor": icfVgMonitor,
       "icfVgMonRptr": icfVgMonRptr,
       "icfVgMonGroup": icfVgMonGroup,
       "icfVgMonPort": icfVgMonPort,
       "icfVgMonPortTable": icfVgMonPortTable,
       "icfVgMonPortEntry": icfVgMonPortEntry,
       "icfVgPortReadableFrames": icfVgPortReadableFrames,
       "icfVgPortReadableOctets": icfVgPortReadableOctets,
       "icfVgPortUnreadableOctets": icfVgPortUnreadableOctets,
       "icfVgPortHighPriorityFrames": icfVgPortHighPriorityFrames,
       "icfVgPortHighPriorityOctets": icfVgPortHighPriorityOctets,
       "icfVgPortBroadcastFrames": icfVgPortBroadcastFrames,
       "icfVgPortMulticastFrames": icfVgPortMulticastFrames,
       "icfVgPortIPMFrames": icfVgPortIPMFrames,
       "icfVgPortDataErrorFrames": icfVgPortDataErrorFrames,
       "icfVgPortPriorityPromotions": icfVgPortPriorityPromotions,
       "icfVgAddrTrack": icfVgAddrTrack,
       "icfVgAddrTrackRptr": icfVgAddrTrackRptr,
       "icfVgAddrTrackGroup": icfVgAddrTrackGroup,
       "icfVgAddrTrackPort": icfVgAddrTrackPort,
       "icfVgAddrTrackTable": icfVgAddrTrackTable,
       "icfVgAddrTrackEntry": icfVgAddrTrackEntry,
       "icfVgAddrLastTrainedAddress": icfVgAddrLastTrainedAddress,
       "icfVgAddrTrainedAddrChanges": icfVgAddrTrainedAddrChanges,
       "hpicfAdmin": hpicfAdmin,
       "hpicfDomains": hpicfDomains,
       "hpicfLLCDomain": hpicfLLCDomain,
       "hpicfObjects": hpicfObjects,
       "hpicfCommon": hpicfCommon,
       "hpicfChain": hpicfChain,
       "hpicfChainMaxMembers": hpicfChainMaxMembers,
       "hpicfChainCurMembers": hpicfChainCurMembers,
       "hpicfChainLastChange": hpicfChainLastChange,
       "hpicfChainChanges": hpicfChainChanges,
       "hpicfChainTable": hpicfChainTable,
       "hpicfChainEntry": hpicfChainEntry,
       "hpicfChainId": hpicfChainId,
       "hpicfChainObjectId": hpicfChainObjectId,
       "hpicfChainTimestamp": hpicfChainTimestamp,
       "hpicfChainHasAgent": hpicfChainHasAgent,
       "hpicfChainThisBox": hpicfChainThisBox,
       "hpicfChainLocation": hpicfChainLocation,
       "hpicfChainViewTable": hpicfChainViewTable,
       "hpicfChainViewEntry": hpicfChainViewEntry,
       "hpicfChainViewId": hpicfChainViewId,
       "hpicfChainViewName": hpicfChainViewName,
       "hpicfChassis": hpicfChassis,
       "hpicfChassisId": hpicfChassisId,
       "hpicfChassisNumSlots": hpicfChassisNumSlots,
       "hpicfSlotTable": hpicfSlotTable,
       "hpicfSlotEntry": hpicfSlotEntry,
       "hpicfSlotIndex": hpicfSlotIndex,
       "hpicfSlotObjectId": hpicfSlotObjectId,
       "hpicfSlotLastChange": hpicfSlotLastChange,
       "hpicfSlotDescr": hpicfSlotDescr,
       "hpicfEntityTable": hpicfEntityTable,
       "hpicfEntityEntry": hpicfEntityEntry,
       "hpicfEntityIndex": hpicfEntityIndex,
       "hpicfEntityFunction": hpicfEntityFunction,
       "hpicfEntityObjectId": hpicfEntityObjectId,
       "hpicfEntityDescr": hpicfEntityDescr,
       "hpicfEntityTimestamp": hpicfEntityTimestamp,
       "hpicfSlotMapTable": hpicfSlotMapTable,
       "hpicfSlotMapEntry": hpicfSlotMapEntry,
       "hpicfSlotMapSlot": hpicfSlotMapSlot,
       "hpicfSlotMapEntity": hpicfSlotMapEntity,
       "hpicfSensorTable": hpicfSensorTable,
       "hpicfSensorEntry": hpicfSensorEntry,
       "hpicfSensorIndex": hpicfSensorIndex,
       "hpicfSensorObjectId": hpicfSensorObjectId,
       "hpicfSensorNumber": hpicfSensorNumber,
       "hpicfSensorStatus": hpicfSensorStatus,
       "hpicfSensorWarnings": hpicfSensorWarnings,
       "hpicfSensorFailures": hpicfSensorFailures,
       "hpicfSensorDescr": hpicfSensorDescr,
       "hpicfChassisAddrTable": hpicfChassisAddrTable,
       "hpicfChassisAddrEntry": hpicfChassisAddrEntry,
       "hpicfChasAddrType": hpicfChasAddrType,
       "hpicfChasAddrAddress": hpicfChasAddrAddress,
       "hpicfChasAddrEntity": hpicfChasAddrEntity,
       "hpicfDownload": hpicfDownload,
       "hpicfDownloadTable": hpicfDownloadTable,
       "hpicfDownloadEntry": hpicfDownloadEntry,
       "hpicfDownloadIndex": hpicfDownloadIndex,
       "hpicfDownloadOwnerAddress": hpicfDownloadOwnerAddress,
       "hpicfDownloadOwnerDomain": hpicfDownloadOwnerDomain,
       "hpicfDownloadTAddress": hpicfDownloadTAddress,
       "hpicfDownloadTDomain": hpicfDownloadTDomain,
       "hpicfDownloadFilename": hpicfDownloadFilename,
       "hpicfDownloadResetType": hpicfDownloadResetType,
       "hpicfDownloadErrorStatus": hpicfDownloadErrorStatus,
       "hpicfDownloadErrorText": hpicfDownloadErrorText,
       "hpicfDownloadStatus": hpicfDownloadStatus,
       "hpicfDownloadLogMaxSize": hpicfDownloadLogMaxSize,
       "hpicfDownloadLogSize": hpicfDownloadLogSize,
       "hpicfDownloadLogTable": hpicfDownloadLogTable,
       "hpicfDownloadLogEntry": hpicfDownloadLogEntry,
       "hpicfDlLogIndex": hpicfDlLogIndex,
       "hpicfDlLogOwnerAddress": hpicfDlLogOwnerAddress,
       "hpicfDlLogOwnerDomain": hpicfDlLogOwnerDomain,
       "hpicfDlLogTAddress": hpicfDlLogTAddress,
       "hpicfDlLogTDomain": hpicfDlLogTDomain,
       "hpicfDlLogFilename": hpicfDlLogFilename,
       "hpicfDlLogResetType": hpicfDlLogResetType,
       "hpicfDlLogErrorStatus": hpicfDlLogErrorStatus,
       "hpicfDlLogErrorText": hpicfDlLogErrorText,
       "hpicfBasic": hpicfBasic,
       "hpicfReset": hpicfReset,
       "hpicfSelfTest": hpicfSelfTest,
       "hpicfRepeater": hpicfRepeater,
       "hpRptrBasic": hpRptrBasic,
       "hpRptrBasicGlobal": hpRptrBasicGlobal,
       "hpRptrEntityName": hpRptrEntityName,
       "hpRptrThinlanFault": hpRptrThinlanFault,
       "hpRptrSqeEnabled": hpRptrSqeEnabled,
       "hpRptrRobustHealing": hpRptrRobustHealing,
       "hpRptrBasicGroup": hpRptrBasicGroup,
       "hpRptrBasicGroupTable": hpRptrBasicGroupTable,
       "hpRptrBasicGroupEntry": hpRptrBasicGroupEntry,
       "hpRptrGrpGroupIndex": hpRptrGrpGroupIndex,
       "hpRptrGrpPortsAdminStatus": hpRptrGrpPortsAdminStatus,
       "hpRptrGrpPortsSegStatus": hpRptrGrpPortsSegStatus,
       "hpRptrGrpPortsMediaAvailable": hpRptrGrpPortsMediaAvailable,
       "hpRptrGrpPortsLinkbeatEnabled": hpRptrGrpPortsLinkbeatEnabled,
       "hpRptrGrpPortsOperStatus": hpRptrGrpPortsOperStatus,
       "hpRptrBasicPort": hpRptrBasicPort,
       "hpRptrBasicPtTable": hpRptrBasicPtTable,
       "hpRptrBasicPtEntry": hpRptrBasicPtEntry,
       "hpRptrPtGroupIndex": hpRptrPtGroupIndex,
       "hpRptrPtPortIndex": hpRptrPtPortIndex,
       "hpRptrPtLinkbeatEnable": hpRptrPtLinkbeatEnable,
       "hpRptrPtPolarityReversed": hpRptrPtPolarityReversed,
       "hpRptrMonitor": hpRptrMonitor,
       "hpRptrMonitorGlobal": hpRptrMonitorGlobal,
       "hpRptrMonCounters": hpRptrMonCounters,
       "hpRptrMonGlobalFrames": hpRptrMonGlobalFrames,
       "hpRptrMonGlobalOctets": hpRptrMonGlobalOctets,
       "hpRptrMonGlobalFCSErrors": hpRptrMonGlobalFCSErrors,
       "hpRptrMonGlobalAlignmentErrors": hpRptrMonGlobalAlignmentErrors,
       "hpRptrMonGlobalFrameTooLongs": hpRptrMonGlobalFrameTooLongs,
       "hpRptrMonGlobalShortEvents": hpRptrMonGlobalShortEvents,
       "hpRptrMonGlobalRunts": hpRptrMonGlobalRunts,
       "hpRptrMonGlobalCollisions": hpRptrMonGlobalCollisions,
       "hpRptrMonGlobalLateEvents": hpRptrMonGlobalLateEvents,
       "hpRptrMonGlobalVeryLongEvents": hpRptrMonGlobalVeryLongEvents,
       "hpRptrMonGlobalDataRateMismatches": hpRptrMonGlobalDataRateMismatches,
       "hpRptrMonGlobalAutoPartitions": hpRptrMonGlobalAutoPartitions,
       "hpRptrMonGlobalErrors": hpRptrMonGlobalErrors,
       "hpRptrMonGlobalUcastPackets": hpRptrMonGlobalUcastPackets,
       "hpRptrMonGlobalBcastPackets": hpRptrMonGlobalBcastPackets,
       "hpRptrMonGlobalMcastPackets": hpRptrMonGlobalMcastPackets,
       "hpRptrMonitorGroup": hpRptrMonitorGroup,
       "hpRptrMonitorPort": hpRptrMonitorPort,
       "hpRptrMonPtTable": hpRptrMonPtTable,
       "hpRptrMonPtEntry": hpRptrMonPtEntry,
       "hpRptrMonPtGroupIndex": hpRptrMonPtGroupIndex,
       "hpRptrMonPtPortIndex": hpRptrMonPtPortIndex,
       "hpRptrMonPtUcastPackets": hpRptrMonPtUcastPackets,
       "hpRptrMonPtBcastPackets": hpRptrMonPtBcastPackets,
       "hpRptrMonPtMcastPackets": hpRptrMonPtMcastPackets,
       "hpRptrAddrTrack": hpRptrAddrTrack,
       "hpRptrAddrTrkGlobal": hpRptrAddrTrkGlobal,
       "hpRptrAddrTrkGroup": hpRptrAddrTrkGroup,
       "hpRptrAddrTrkPort": hpRptrAddrTrkPort,
       "hpicfVg": hpicfVg,
       "hpVgBasic": hpVgBasic,
       "hpVgBasicGlobal": hpVgBasicGlobal,
       "hpVgEntityName": hpVgEntityName,
       "hpVgBasicGroup": hpVgBasicGroup,
       "hpVgBasicGroupTable": hpVgBasicGroupTable,
       "hpVgBasicGroupEntry": hpVgBasicGroupEntry,
       "hpVgGrpGroupIndex": hpVgGrpGroupIndex,
       "hpVgGrpPortsAdminStatus": hpVgGrpPortsAdminStatus,
       "hpVgGrpPortsTrained": hpVgGrpPortsTrained,
       "hpVgGrpPortsInTraining": hpVgGrpPortsInTraining,
       "hpVgGrpPortsCascaded": hpVgGrpPortsCascaded,
       "hpVgGrpPortsPromiscuous": hpVgGrpPortsPromiscuous,
       "hpVgBasicPort": hpVgBasicPort,
       "hpVgBasicPortTable": hpVgBasicPortTable,
       "hpVgBasicPortEntry": hpVgBasicPortEntry,
       "hpVgPortGroupIndex": hpVgPortGroupIndex,
       "hpVgPortIndex": hpVgPortIndex,
       "hpVgPortPolarityReversed": hpVgPortPolarityReversed,
       "hpVgPortWireSkewError": hpVgPortWireSkewError,
       "hpVgMonitor": hpVgMonitor,
       "hpVgMonitorGlobal": hpVgMonitorGlobal,
       "hpVgMonCounters": hpVgMonCounters,
       "hpVgMonGlbReadableFrames": hpVgMonGlbReadableFrames,
       "hpVgMonGlbReadableOctets": hpVgMonGlbReadableOctets,
       "hpVgMonGlbUnreadableOctets": hpVgMonGlbUnreadableOctets,
       "hpVgMonGlbHighPriorityFrames": hpVgMonGlbHighPriorityFrames,
       "hpVgMonGlbHighPriorityOctets": hpVgMonGlbHighPriorityOctets,
       "hpVgMonGlbBroadcastFrames": hpVgMonGlbBroadcastFrames,
       "hpVgMonGlbMulticastFrames": hpVgMonGlbMulticastFrames,
       "hpVgMonGlbIPMFrames": hpVgMonGlbIPMFrames,
       "hpVgMonGlbDataErrorFrames": hpVgMonGlbDataErrorFrames,
       "hpVgMonGlbPriorityPromotions": hpVgMonGlbPriorityPromotions,
       "hpVgMonitorGroup": hpVgMonitorGroup,
       "hpVgMonitorPort": hpVgMonitorPort,
       "hpicfGenericRepeater": hpicfGenericRepeater,
       "hpGRpBasic": hpGRpBasic,
       "hpGRpBasicGlobal": hpGRpBasicGlobal,
       "hpGRpSelfHealEnable": hpGRpSelfHealEnable,
       "hpGRpBasicGroup": hpGRpBasicGroup,
       "hpGRpBasicPort": hpGRpBasicPort,
       "hpGRpMonitor": hpGRpMonitor,
       "hpGRpAddrTrack": hpGRpAddrTrack,
       "hpicfNotifications": hpicfNotifications,
       "hpicfCommonTraps": hpicfCommonTraps,
       "hpicfChainAddition": hpicfChainAddition,
       "hpicfChainRemoval": hpicfChainRemoval,
       "hpicf8023RptrTraps": hpicf8023RptrTraps,
       "hpicfVgRptrTraps": hpicfVgRptrTraps,
       "hpicfGenRptrTraps": hpicfGenRptrTraps}
)
