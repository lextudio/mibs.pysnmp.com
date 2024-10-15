# SNMP MIB module (ICF-ETWIST) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ICF-ETWIST
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:02 2024
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

(hubIntruderAddress,
 hubIntruderPort) = mibBuilder.importSymbols(
    "HP-ICF-GENERIC-RPTR",
    "hubIntruderAddress",
    "hubIntruderPort")

(advStack12,
 advStack24,
 advStack48,
 advStackU16,
 advStackU8,
 bridge1010,
 bridgeRemote,
 etherTwist12,
 etherTwist24S,
 etherTwist48,
 fiberOptic,
 hpicfEnetSMM,
 icfBridge,
 icfCommon,
 icfConfig,
 icfHub,
 repeaterAgent,
 thinLAN) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "advStack12",
    "advStack24",
    "advStack48",
    "advStackU16",
    "advStackU8",
    "bridge1010",
    "bridgeRemote",
    "etherTwist12",
    "etherTwist24S",
    "etherTwist48",
    "fiberOptic",
    "hpicfEnetSMM",
    "icfBridge",
    "icfCommon",
    "icfConfig",
    "icfHub",
    "repeaterAgent",
    "thinLAN")

(ifAdminStatus,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus")

(rptrAddrTrackLastSourceAddress,
 rptrPortAdminStatus) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrAddrTrackLastSourceAddress",
    "rptrPortAdminStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

icfEtwistMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 1)
)
icfEtwistMib.setRevisions(
        ("2000-11-03 22:20",
         "1996-09-06 02:58",
         "1994-02-25 00:00",
         "1993-07-09 00:00",
         "1992-04-16 00:00",
         "1991-04-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bridge1010TrapPrefix_ObjectIdentity = ObjectIdentity
bridge1010TrapPrefix = _Bridge1010TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1, 0)
)
_BridgeRemoteTrapPrefix_ObjectIdentity = ObjectIdentity
bridgeRemoteTrapPrefix = _BridgeRemoteTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2, 0)
)
_EtherTwist12TrapPrefix_ObjectIdentity = ObjectIdentity
etherTwist12TrapPrefix = _EtherTwist12TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1, 0)
)
_FiberOpticTrapPrefix_ObjectIdentity = ObjectIdentity
fiberOpticTrapPrefix = _FiberOpticTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0)
)
_EtherTwist48TrapPrefix_ObjectIdentity = ObjectIdentity
etherTwist48TrapPrefix = _EtherTwist48TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4, 0)
)
_ThinLANTrapPrefix_ObjectIdentity = ObjectIdentity
thinLANTrapPrefix = _ThinLANTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5, 0)
)
_EtherTwist24STrapPrefix_ObjectIdentity = ObjectIdentity
etherTwist24STrapPrefix = _EtherTwist24STrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0)
)
_AdvStack12TrapPrefix_ObjectIdentity = ObjectIdentity
advStack12TrapPrefix = _AdvStack12TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 7, 0)
)
_AdvStack24TrapPrefix_ObjectIdentity = ObjectIdentity
advStack24TrapPrefix = _AdvStack24TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 8, 0)
)
_AdvStack48TrapPrefix_ObjectIdentity = ObjectIdentity
advStack48TrapPrefix = _AdvStack48TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 9, 0)
)
_AdvStackU8TrapPrefix_ObjectIdentity = ObjectIdentity
advStackU8TrapPrefix = _AdvStackU8TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 11, 0)
)
_AdvStackU16TrapPrefix_ObjectIdentity = ObjectIdentity
advStackU16TrapPrefix = _AdvStackU16TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 12, 0)
)
_RepeaterAgentTrapPrefix_ObjectIdentity = ObjectIdentity
repeaterAgentTrapPrefix = _RepeaterAgentTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0)
)
_HpicfEnetSMMTrapPrefix_ObjectIdentity = ObjectIdentity
hpicfEnetSMMTrapPrefix = _HpicfEnetSMMTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0)
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
_Reset_Type = Integer32
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
    announceAddress.setStatus("obsolete")
_MapAddress_Type = MacAddress
_MapAddress_Object = MibScalar
mapAddress = _MapAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 3),
    _MapAddress_Type()
)
mapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mapAddress.setStatus("obsolete")
_MapState_Type = Integer32
_MapState_Object = MibScalar
mapState = _MapState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 4),
    _MapState_Type()
)
mapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapState.setStatus("obsolete")


class _MapPort_Type(Integer32):
    """Custom type mapPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MapPort_Type.__name__ = "Integer32"
_MapPort_Object = MibScalar
mapPort = _MapPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 6, 5),
    _MapPort_Type()
)
mapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapPort.setStatus("obsolete")
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
_LinkTest802MacAddress_Type = MacAddress
_LinkTest802MacAddress_Object = MibScalar
linkTest802MacAddress = _LinkTest802MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1, 1),
    _LinkTest802MacAddress_Type()
)
linkTest802MacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTest802MacAddress.setStatus("obsolete")
_LinkTestIpAddress_Type = IpAddress
_LinkTestIpAddress_Object = MibScalar
linkTestIpAddress = _LinkTestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 1, 2),
    _LinkTestIpAddress_Type()
)
linkTestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestIpAddress.setStatus("obsolete")


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
    linkTestIpxAddress.setStatus("obsolete")


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
    linkTestRepetitions.setStatus("obsolete")


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
    linkTestSuccess.setStatus("obsolete")
_LinkTestTimeout_Type = TimeTicks
_LinkTestTimeout_Object = MibScalar
linkTestTimeout = _LinkTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 8, 4),
    _LinkTestTimeout_Type()
)
linkTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkTestTimeout.setStatus("obsolete")
_Icf8023MacTable_Object = MibTable
icf8023MacTable = _Icf8023MacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 9)
)
if mibBuilder.loadTexts:
    icf8023MacTable.setStatus("obsolete")


class _Icf8023MacIndex_Type(Integer32):
    """Custom type icf8023MacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Icf8023MacIndex_Type.__name__ = "Integer32"
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
_IcfCommonAdmin_ObjectIdentity = ObjectIdentity
icfCommonAdmin = _IcfCommonAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11)
)
_IcfETwistConformance_ObjectIdentity = ObjectIdentity
icfETwistConformance = _IcfETwistConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2)
)
_IcfETCompliances_ObjectIdentity = ObjectIdentity
icfETCompliances = _IcfETCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1)
)
_IcfETGroups_ObjectIdentity = ObjectIdentity
icfETGroups = _IcfETGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2)
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
    hubAddressTable.setStatus("obsolete")


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
_HubBackupAddress_Type = MacAddress
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
_HubAddressMoveLogTable_Object = MibTable
hubAddressMoveLogTable = _HubAddressMoveLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11)
)
if mibBuilder.loadTexts:
    hubAddressMoveLogTable.setStatus("obsolete")
_HubAddressMoveLogEntry_Object = MibTableRow
hubAddressMoveLogEntry = _HubAddressMoveLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1)
)
hubAddressMoveLogEntry.setIndexNames(
    (0, "ICF-ETWIST", "hubAddrMoveIndex"),
)
if mibBuilder.loadTexts:
    hubAddressMoveLogEntry.setStatus("obsolete")


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
    hubAddrMoveIndex.setStatus("obsolete")
_HubAddrMoveAddress_Type = MacAddress
_HubAddrMoveAddress_Object = MibTableColumn
hubAddrMoveAddress = _HubAddrMoveAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 11, 1, 2),
    _HubAddrMoveAddress_Type()
)
hubAddrMoveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAddrMoveAddress.setStatus("obsolete")


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
    hubAddrMoveOldGroup.setStatus("obsolete")


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
    hubAddrMoveOldPort.setStatus("obsolete")


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
    hubAddrMoveNewGroup.setStatus("obsolete")


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
    hubAddrMoveNewPort.setStatus("obsolete")


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
    hubLateEventMonitor.setStatus("obsolete")
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
        ValueRangeConstraint(0, 2147483647),
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
_IcfConfigIfTable_Object = MibTable
icfConfigIfTable = _IcfConfigIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1)
)
if mibBuilder.loadTexts:
    icfConfigIfTable.setStatus("obsolete")
_IcfConfigIfEntry_Object = MibTableRow
icfConfigIfEntry = _IcfConfigIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1)
)
icfConfigIfEntry.setIndexNames(
    (0, "ICF-ETWIST", "icfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    icfConfigIfEntry.setStatus("obsolete")
_IcfConfigIfIndex_Type = Integer32
_IcfConfigIfIndex_Object = MibTableColumn
icfConfigIfIndex = _IcfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 1),
    _IcfConfigIfIndex_Type()
)
icfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icfConfigIfIndex.setStatus("obsolete")
_IcfConfigIfIpAddress_Type = IpAddress
_IcfConfigIfIpAddress_Object = MibTableColumn
icfConfigIfIpAddress = _IcfConfigIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 2),
    _IcfConfigIfIpAddress_Type()
)
icfConfigIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfIpAddress.setStatus("obsolete")
_IcfConfigIfNetMask_Type = IpAddress
_IcfConfigIfNetMask_Object = MibTableColumn
icfConfigIfNetMask = _IcfConfigIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 3),
    _IcfConfigIfNetMask_Type()
)
icfConfigIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfNetMask.setStatus("obsolete")
_IcfConfigIfDefaultGate_Type = IpAddress
_IcfConfigIfDefaultGate_Object = MibTableColumn
icfConfigIfDefaultGate = _IcfConfigIfDefaultGate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5, 1, 1, 4),
    _IcfConfigIfDefaultGate_Type()
)
icfConfigIfDefaultGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    icfConfigIfDefaultGate.setStatus("obsolete")


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
    icfConfigIpTTL.setStatus("obsolete")


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
    icfConfigBootpEnable.setStatus("obsolete")

# Managed Objects groups

icfCommonBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 1)
)
icfCommonBasicGroup.setObjects(
      *(("ICF-ETWIST", "lastSetError"),
        ("ICF-ETWIST", "reset"),
        ("ICF-ETWIST", "selfTest"),
        ("ICF-ETWIST", "semaphore"),
        ("ICF-ETWIST", "pollResponse"),
        ("ICF-ETWIST", "evtIndex"),
        ("ICF-ETWIST", "evtArm"),
        ("ICF-ETWIST", "evtTimeSinceOccurrence"),
        ("ICF-ETWIST", "evthIndex"),
        ("ICF-ETWIST", "evthArm"),
        ("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"),
        ("ICF-ETWIST", "evthTimeSinceOccurrence"))
)
if mibBuilder.loadTexts:
    icfCommonBasicGroup.setStatus("obsolete")

icfCommonIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 2)
)
icfCommonIpGroup.setObjects(
      *(("ICF-ETWIST", "ipSubnetMask"),
        ("ICF-ETWIST", "evtIpNotify"))
)
if mibBuilder.loadTexts:
    icfCommonIpGroup.setStatus("obsolete")

icfCommonIpxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 3)
)
icfCommonIpxGroup.setObjects(
    ("ICF-ETWIST", "evtIpxNotify")
)
if mibBuilder.loadTexts:
    icfCommonIpxGroup.setStatus("obsolete")

icfEncryptedPasswordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 4)
)
icfEncryptedPasswordGroup.setObjects(
    ("ICF-ETWIST", "password")
)
if mibBuilder.loadTexts:
    icfEncryptedPasswordGroup.setStatus("obsolete")

icfMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 5)
)
icfMappingGroup.setObjects(
      *(("ICF-ETWIST", "announceAddress"),
        ("ICF-ETWIST", "mapAddress"),
        ("ICF-ETWIST", "mapState"),
        ("ICF-ETWIST", "mapPort"),
        ("ICF-ETWIST", "linkTest802MacAddress"),
        ("ICF-ETWIST", "linkTestRepetitions"),
        ("ICF-ETWIST", "linkTestSuccess"),
        ("ICF-ETWIST", "linkTestTimeout"))
)
if mibBuilder.loadTexts:
    icfMappingGroup.setStatus("obsolete")

icfIpMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 6)
)
icfIpMappingGroup.setObjects(
    ("ICF-ETWIST", "linkTestIpAddress")
)
if mibBuilder.loadTexts:
    icfIpMappingGroup.setStatus("obsolete")

icfIpxMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 7)
)
icfIpxMappingGroup.setObjects(
    ("ICF-ETWIST", "linkTestIpxAddress")
)
if mibBuilder.loadTexts:
    icfIpxMappingGroup.setStatus("obsolete")

icfSlaveMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 8)
)
icfSlaveMappingGroup.setObjects(
      *(("ICF-ETWIST", "mapAddress"),
        ("ICF-ETWIST", "mapState"),
        ("ICF-ETWIST", "mapPort"))
)
if mibBuilder.loadTexts:
    icfSlaveMappingGroup.setStatus("obsolete")

icf8023MacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 9)
)
icf8023MacGroup.setObjects(
      *(("ICF-ETWIST", "icf8023MacIndex"),
        ("ICF-ETWIST", "icf8023MacInBroadcastPkts"),
        ("ICF-ETWIST", "icf8023MacOutBroadcastPkts"),
        ("ICF-ETWIST", "icf8023MacInMulticastPkts"),
        ("ICF-ETWIST", "icf8023MacOutMulticastPkts"),
        ("ICF-ETWIST", "icf8023MacRunts"),
        ("ICF-ETWIST", "icf8023MacGiants"),
        ("ICF-ETWIST", "icf8023MacMissedPktErrors"),
        ("ICF-ETWIST", "icf8023MacExcessDeferrals"),
        ("ICF-ETWIST", "icf8023MacTotalMediaErrors"),
        ("ICF-ETWIST", "icf8023MacSpuriousIntrs"))
)
if mibBuilder.loadTexts:
    icf8023MacGroup.setStatus("obsolete")

icf8023MacSlaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 10)
)
icf8023MacSlaveGroup.setObjects(
      *(("ICF-ETWIST", "icf8023MacIndex"),
        ("ICF-ETWIST", "icf8023MacRunts"),
        ("ICF-ETWIST", "icf8023MacGiants"),
        ("ICF-ETWIST", "icf8023MacMissedPktErrors"),
        ("ICF-ETWIST", "icf8023MacExcessDeferrals"),
        ("ICF-ETWIST", "icf8023MacTotalMediaErrors"),
        ("ICF-ETWIST", "icf8023MacSpuriousIntrs"))
)
if mibBuilder.loadTexts:
    icf8023MacSlaveGroup.setStatus("obsolete")

icfDownloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 11)
)
icfDownloadGroup.setObjects(
      *(("ICF-ETWIST", "icfDownloadIpAddress"),
        ("ICF-ETWIST", "icfDownloadIpxAddress"),
        ("ICF-ETWIST", "icfDownloadFilename"))
)
if mibBuilder.loadTexts:
    icfDownloadGroup.setStatus("obsolete")

hubBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 12)
)
hubBasicGroup.setObjects(
      *(("ICF-ETWIST", "hubThinlanFault"),
        ("ICF-ETWIST", "hubGlobalErrors"),
        ("ICF-ETWIST", "hubGlobalCollisions"),
        ("ICF-ETWIST", "hubGlobalPktFragments"),
        ("ICF-ETWIST", "hubGlobalRunts"),
        ("ICF-ETWIST", "hubGlobalGiants"),
        ("ICF-ETWIST", "hubGlobalCrcErrors"),
        ("ICF-ETWIST", "hubGlobalAlignmentErrors"),
        ("ICF-ETWIST", "hubGlobalInOctets"),
        ("ICF-ETWIST", "hubGlobalInUcastPkts"),
        ("ICF-ETWIST", "hubGlobalInNUcastPkts"),
        ("ICF-ETWIST", "hubGlobalInBroadcastPkts"),
        ("ICF-ETWIST", "hubPortPktFragments"),
        ("ICF-ETWIST", "hubPortCollisions"),
        ("ICF-ETWIST", "hubPortSegmentation"),
        ("ICF-ETWIST", "hubPortLinkBeatStatus"),
        ("ICF-ETWIST", "hubPortsOperStatus"))
)
if mibBuilder.loadTexts:
    hubBasicGroup.setStatus("obsolete")

hubBasicSlaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 13)
)
hubBasicSlaveGroup.setObjects(
      *(("ICF-ETWIST", "hubThinlanFault"),
        ("ICF-ETWIST", "hubGlobalErrors"),
        ("ICF-ETWIST", "hubGlobalCollisions"),
        ("ICF-ETWIST", "hubGlobalPktFragments"),
        ("ICF-ETWIST", "hubGlobalRunts"),
        ("ICF-ETWIST", "hubGlobalGiants"),
        ("ICF-ETWIST", "hubGlobalCrcErrors"),
        ("ICF-ETWIST", "hubGlobalAlignmentErrors"),
        ("ICF-ETWIST", "hubGlobalInOctets"),
        ("ICF-ETWIST", "hubPortPktFragments"),
        ("ICF-ETWIST", "hubPortCollisions"),
        ("ICF-ETWIST", "hubPortSegmentation"),
        ("ICF-ETWIST", "hubPortLinkBeatStatus"),
        ("ICF-ETWIST", "hubPortsOperStatus"))
)
if mibBuilder.loadTexts:
    hubBasicSlaveGroup.setStatus("obsolete")

hubMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 14)
)
hubMappingGroup.setObjects(
      *(("ICF-ETWIST", "hubPortIndex"),
        ("ICF-ETWIST", "hubPortMacAddress"),
        ("ICF-ETWIST", "hubPortAddressState"))
)
if mibBuilder.loadTexts:
    hubMappingGroup.setStatus("obsolete")

hubLinkBeatControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 15)
)
hubLinkBeatControlGroup.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatEnable")
)
if mibBuilder.loadTexts:
    hubLinkBeatControlGroup.setStatus("obsolete")

hubBasicEnhancementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 16)
)
hubBasicEnhancementsGroup.setObjects(
    ("ICF-ETWIST", "hubSqeEnabled")
)
if mibBuilder.loadTexts:
    hubBasicEnhancementsGroup.setStatus("obsolete")

hubBasicAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 17)
)
hubBasicAddrTableGroup.setObjects(
    ("ICF-ETWIST", "hubAddressTableMaxAge")
)
if mibBuilder.loadTexts:
    hubBasicAddrTableGroup.setStatus("obsolete")

hubReadableAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 18)
)
hubReadableAddrTableGroup.setObjects(
      *(("ICF-ETWIST", "hubAddressIndex"),
        ("ICF-ETWIST", "hubAddressChunk"))
)
if mibBuilder.loadTexts:
    hubReadableAddrTableGroup.setStatus("obsolete")

hubBackupLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 19)
)
hubBackupLinkGroup.setObjects(
      *(("ICF-ETWIST", "hubNumBkpLinks"),
        ("ICF-ETWIST", "hubBkpLinkIndex"),
        ("ICF-ETWIST", "hubBackupPort"),
        ("ICF-ETWIST", "hubPrimaryPort"),
        ("ICF-ETWIST", "hubBackupAddress"),
        ("ICF-ETWIST", "hubBackupTestTime"),
        ("ICF-ETWIST", "hubBackupConsecutiveFails"))
)
if mibBuilder.loadTexts:
    hubBackupLinkGroup.setStatus("obsolete")

hubNewEnhancementsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 20)
)
hubNewEnhancementsGroup.setObjects(
    ("ICF-ETWIST", "hubPortPolarityReversed")
)
if mibBuilder.loadTexts:
    hubNewEnhancementsGroup.setStatus("obsolete")

hubAddressMoveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 21)
)
hubAddressMoveGroup.setObjects(
      *(("ICF-ETWIST", "hubAddrMoveIndex"),
        ("ICF-ETWIST", "hubAddrMoveAddress"),
        ("ICF-ETWIST", "hubAddrMoveOldGroup"),
        ("ICF-ETWIST", "hubAddrMoveOldPort"),
        ("ICF-ETWIST", "hubAddrMoveNewGroup"),
        ("ICF-ETWIST", "hubAddrMoveNewPort"))
)
if mibBuilder.loadTexts:
    hubAddressMoveGroup.setStatus("obsolete")

hubLateEventMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 22)
)
hubLateEventMonitorGroup.setObjects(
      *(("ICF-ETWIST", "hubPortLateEventDisable"),
        ("ICF-ETWIST", "hubLateEventMonitor"))
)
if mibBuilder.loadTexts:
    hubLateEventMonitorGroup.setStatus("obsolete")

icfBridgeBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 23)
)
icfBridgeBasicGroup.setObjects(
      *(("ICF-ETWIST", "operationalState"),
        ("ICF-ETWIST", "forwardDbMaxAge"),
        ("ICF-ETWIST", "addressIndex"),
        ("ICF-ETWIST", "addressChunk"),
        ("ICF-ETWIST", "brgPortIndex"),
        ("ICF-ETWIST", "brgPortCacheHits"),
        ("ICF-ETWIST", "brgPortCacheMisses"),
        ("ICF-ETWIST", "brgPortForwardedPkts"),
        ("ICF-ETWIST", "brgPortFilteredPkts"),
        ("ICF-ETWIST", "wildcardIndex"),
        ("ICF-ETWIST", "wildcardFilter"),
        ("ICF-ETWIST", "wildcardMask"),
        ("ICF-ETWIST", "wildcardOffset"),
        ("ICF-ETWIST", "wildcardUserOffset"),
        ("ICF-ETWIST", "wildcardArm"))
)
if mibBuilder.loadTexts:
    icfBridgeBasicGroup.setStatus("obsolete")

icfBridgeSpanningTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 24)
)
icfBridgeSpanningTreeGroup.setObjects(
      *(("ICF-ETWIST", "stpBridgeId"),
        ("ICF-ETWIST", "stpTopoChangeTime"),
        ("ICF-ETWIST", "stpTopoNumChanges"),
        ("ICF-ETWIST", "stpTopoChange"),
        ("ICF-ETWIST", "stpDesignatedRoot"),
        ("ICF-ETWIST", "stpRootCost"),
        ("ICF-ETWIST", "stpRootPort"),
        ("ICF-ETWIST", "stpCurrentMaxAge"),
        ("ICF-ETWIST", "stpCurrentHelloTime"),
        ("ICF-ETWIST", "stpCurrentForwardDelay"),
        ("ICF-ETWIST", "stpMaxAge"),
        ("ICF-ETWIST", "stpHelloTime"),
        ("ICF-ETWIST", "stpForwardDelay"),
        ("ICF-ETWIST", "stpPriority"),
        ("ICF-ETWIST", "stpPortIndex"),
        ("ICF-ETWIST", "stpPortState"),
        ("ICF-ETWIST", "stpPortId"),
        ("ICF-ETWIST", "stpPortPathCost"),
        ("ICF-ETWIST", "stpPortRootId"),
        ("ICF-ETWIST", "stpPortDesignatedCost"),
        ("ICF-ETWIST", "stpPortDesignatedBridge"),
        ("ICF-ETWIST", "stpPortDesignatedPort"),
        ("ICF-ETWIST", "stpPortPriority"))
)
if mibBuilder.loadTexts:
    icfBridgeSpanningTreeGroup.setStatus("obsolete")

icfRemoteBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 25)
)
icfRemoteBridgeGroup.setObjects(
      *(("ICF-ETWIST", "hdlcErrorIndex"),
        ("ICF-ETWIST", "hdlcErrorIndications"),
        ("ICF-ETWIST", "hdlcT1Timeouts"),
        ("ICF-ETWIST", "hdlcMissedPackets"),
        ("ICF-ETWIST", "hdlcRcvOverruns"),
        ("ICF-ETWIST", "hdlcXmtUnderruns"),
        ("ICF-ETWIST", "hdlcProviderLostPrimitives"),
        ("ICF-ETWIST", "hdlcRuntFrameReceives"),
        ("ICF-ETWIST", "hdlcGiantFrameReceives"),
        ("ICF-ETWIST", "hdlcBadFrameReceives"),
        ("ICF-ETWIST", "hdlcRejectFrameReceives"),
        ("ICF-ETWIST", "hdlcRejectFrameSends"),
        ("ICF-ETWIST", "hdlcFrameRejectFrameRecs"),
        ("ICF-ETWIST", "hdlcLocalIndex"),
        ("ICF-ETWIST", "hdlcLocalResetRequests"),
        ("ICF-ETWIST", "hdlcLocalResetConfirms"),
        ("ICF-ETWIST", "hdlcLocalConnectRequests"),
        ("ICF-ETWIST", "hdlcLocalConnectConfirms"),
        ("ICF-ETWIST", "hdlcLocalDisconnectRequests"),
        ("ICF-ETWIST", "hdlcLocalDisconnectConfirms"),
        ("ICF-ETWIST", "hdlcLocalState"),
        ("ICF-ETWIST", "hdlcLocalAddress"),
        ("ICF-ETWIST", "hdlcLocalPhase"),
        ("ICF-ETWIST", "hdlcRemoteIndex"),
        ("ICF-ETWIST", "hdlcRemoteResetRequests"),
        ("ICF-ETWIST", "hdlcRemoteResetConfirms"),
        ("ICF-ETWIST", "hdlcRemoteConnectRequests"),
        ("ICF-ETWIST", "hdlcRemoteConnectConfirms"),
        ("ICF-ETWIST", "hdlcRemoteDisconnectRequests"),
        ("ICF-ETWIST", "hdlcRemoteState"),
        ("ICF-ETWIST", "hdlcRemoteAddress"),
        ("ICF-ETWIST", "hdlcRemoteXidCommands"),
        ("ICF-ETWIST", "hdlcRemoteXidResponses"),
        ("ICF-ETWIST", "hdlcRemoteTestCommands"),
        ("ICF-ETWIST", "hdlcRemoteTestResponses"),
        ("ICF-ETWIST", "hdlcRemoteNodeId"),
        ("ICF-ETWIST", "x25Index"),
        ("ICF-ETWIST", "x25T1Timer"),
        ("ICF-ETWIST", "x25N2Count"),
        ("ICF-ETWIST", "x25T3Timer"))
)
if mibBuilder.loadTexts:
    icfRemoteBridgeGroup.setStatus("obsolete")

icfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 2, 26)
)
icfConfigGroup.setObjects(
      *(("ICF-ETWIST", "icfConfigIfIndex"),
        ("ICF-ETWIST", "icfConfigIfIpAddress"),
        ("ICF-ETWIST", "icfConfigIfNetMask"),
        ("ICF-ETWIST", "icfConfigIfDefaultGate"),
        ("ICF-ETWIST", "icfConfigIpTTL"),
        ("ICF-ETWIST", "icfConfigBootpEnable"))
)
if mibBuilder.loadTexts:
    icfConfigGroup.setStatus("obsolete")


# Notification objects

thresholdTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1, 0, 0)
)
thresholdTrap1010.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrap1010.setStatus(
        "obsolete"
    )

stpTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1, 0, 3)
)
stpTrap1010.setObjects(
    ("ICF-ETWIST", "stpPortState")
)
if mibBuilder.loadTexts:
    stpTrap1010.setStatus(
        "obsolete"
    )

temperatureTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1, 0, 4)
)
if mibBuilder.loadTexts:
    temperatureTrap1010.setStatus(
        "obsolete"
    )

thresholdTrapRem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2, 0, 0)
)
thresholdTrapRem.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapRem.setStatus(
        "obsolete"
    )

stpTrapRem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2, 0, 3)
)
stpTrapRem.setObjects(
    ("ICF-ETWIST", "stpPortState")
)
if mibBuilder.loadTexts:
    stpTrapRem.setStatus(
        "obsolete"
    )

temperatureTrapRem = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    temperatureTrapRem.setStatus(
        "obsolete"
    )

thresholdTrapET12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1, 0, 0)
)
thresholdTrapET12.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapET12.setStatus(
        "obsolete"
    )

linkBeatTrapET12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1, 0, 3)
)
linkBeatTrapET12.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapET12.setStatus(
        "obsolete"
    )

segmentationTrapET12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1, 0, 4)
)
segmentationTrapET12.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapET12.setStatus(
        "obsolete"
    )

backupLinkTrapET12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1, 0, 5)
)
backupLinkTrapET12.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapET12.setStatus(
        "obsolete"
    )

thresholdTrapFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0, 0)
)
thresholdTrapFiber.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapFiber.setStatus(
        "obsolete"
    )

linkBeatTrapFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0, 3)
)
linkBeatTrapFiber.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapFiber.setStatus(
        "obsolete"
    )

segmentationTrapFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0, 4)
)
segmentationTrapFiber.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapFiber.setStatus(
        "obsolete"
    )

backupLinkTrapFiber = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3, 0, 5)
)
backupLinkTrapFiber.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapFiber.setStatus(
        "obsolete"
    )

thresholdTrapET48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4, 0, 0)
)
thresholdTrapET48.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapET48.setStatus(
        "obsolete"
    )

linkBeatTrapET48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4, 0, 3)
)
linkBeatTrapET48.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapET48.setStatus(
        "obsolete"
    )

segmentationTrapET48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4, 0, 4)
)
segmentationTrapET48.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapET48.setStatus(
        "obsolete"
    )

backupLinkTrapET48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4, 0, 5)
)
backupLinkTrapET48.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapET48.setStatus(
        "obsolete"
    )

thresholdTrapTLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5, 0, 0)
)
thresholdTrapTLAN.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapTLAN.setStatus(
        "obsolete"
    )

linkBeatTrapTLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5, 0, 3)
)
linkBeatTrapTLAN.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapTLAN.setStatus(
        "obsolete"
    )

segmentationTrapTLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5, 0, 4)
)
segmentationTrapTLAN.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapTLAN.setStatus(
        "obsolete"
    )

backupLinkTrapTLAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5, 0, 5)
)
backupLinkTrapTLAN.setObjects(
    ("IF-MIB", "ifAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapTLAN.setStatus(
        "obsolete"
    )

thresholdTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 0)
)
thresholdTrapET24S.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapET24S.setStatus(
        "obsolete"
    )

linkBeatTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 3)
)
linkBeatTrapET24S.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapET24S.setStatus(
        "obsolete"
    )

segmentationTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 4)
)
segmentationTrapET24S.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapET24S.setStatus(
        "obsolete"
    )

backupLinkTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 5)
)
backupLinkTrapET24S.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapET24S.setStatus(
        "obsolete"
    )

intrusionTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 6)
)
intrusionTrapET24S.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"))
)
if mibBuilder.loadTexts:
    intrusionTrapET24S.setStatus(
        "obsolete"
    )

addressMovedTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 7)
)
addressMovedTrapET24S.setObjects(
      *(("ICF-ETWIST", "hubAddrMoveAddress"),
        ("ICF-ETWIST", "hubAddrMoveOldGroup"),
        ("ICF-ETWIST", "hubAddrMoveOldPort"),
        ("ICF-ETWIST", "hubAddrMoveNewGroup"),
        ("ICF-ETWIST", "hubAddrMoveNewPort"))
)
if mibBuilder.loadTexts:
    addressMovedTrapET24S.setStatus(
        "obsolete"
    )

newAddressTrapET24S = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6, 0, 8)
)
newAddressTrapET24S.setObjects(
    ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress")
)
if mibBuilder.loadTexts:
    newAddressTrapET24S.setStatus(
        "obsolete"
    )

thresholdTrapAS12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 7, 0, 0)
)
thresholdTrapAS12.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapAS12.setStatus(
        "obsolete"
    )

thresholdTrapAS24 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 8, 0, 0)
)
thresholdTrapAS24.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapAS24.setStatus(
        "obsolete"
    )

thresholdTrapAS48 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 9, 0, 0)
)
thresholdTrapAS48.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapAS48.setStatus(
        "obsolete"
    )

thresholdTrapASU8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 11, 0, 0)
)
thresholdTrapASU8.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapASU8.setStatus(
        "obsolete"
    )

thresholdTrapASU16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 12, 0, 0)
)
thresholdTrapASU16.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapASU16.setStatus(
        "obsolete"
    )

thresholdTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 0)
)
thresholdTrapASEN.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapASEN.setStatus(
        "obsolete"
    )

linkBeatTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 3)
)
linkBeatTrapASEN.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapASEN.setStatus(
        "obsolete"
    )

segmentationTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 4)
)
segmentationTrapASEN.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapASEN.setStatus(
        "obsolete"
    )

backupLinkTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 5)
)
backupLinkTrapASEN.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapASEN.setStatus(
        "obsolete"
    )

intrusionTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 6)
)
intrusionTrapASEN.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"))
)
if mibBuilder.loadTexts:
    intrusionTrapASEN.setStatus(
        "obsolete"
    )

addressMovedTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 7)
)
addressMovedTrapASEN.setObjects(
      *(("ICF-ETWIST", "hubAddrMoveAddress"),
        ("ICF-ETWIST", "hubAddrMoveOldGroup"),
        ("ICF-ETWIST", "hubAddrMoveOldPort"),
        ("ICF-ETWIST", "hubAddrMoveNewGroup"),
        ("ICF-ETWIST", "hubAddrMoveNewPort"))
)
if mibBuilder.loadTexts:
    addressMovedTrapASEN.setStatus(
        "obsolete"
    )

newAddressTrapASEN = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1, 0, 8)
)
newAddressTrapASEN.setObjects(
    ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress")
)
if mibBuilder.loadTexts:
    newAddressTrapASEN.setStatus(
        "obsolete"
    )

thresholdTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 0)
)
thresholdTrapSMM.setObjects(
      *(("ICF-ETWIST", "evthObject"),
        ("ICF-ETWIST", "evthThreshold"),
        ("ICF-ETWIST", "evthHysteresis"),
        ("ICF-ETWIST", "evthTimeInterval"))
)
if mibBuilder.loadTexts:
    thresholdTrapSMM.setStatus(
        "obsolete"
    )

linkBeatTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 3)
)
linkBeatTrapSMM.setObjects(
    ("ICF-ETWIST", "hubPortLinkBeatStatus")
)
if mibBuilder.loadTexts:
    linkBeatTrapSMM.setStatus(
        "obsolete"
    )

segmentationTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 4)
)
segmentationTrapSMM.setObjects(
    ("ICF-ETWIST", "hubPortSegmentation")
)
if mibBuilder.loadTexts:
    segmentationTrapSMM.setStatus(
        "obsolete"
    )

backupLinkTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 5)
)
backupLinkTrapSMM.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortAdminStatus")
)
if mibBuilder.loadTexts:
    backupLinkTrapSMM.setStatus(
        "obsolete"
    )

intrusionTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 6)
)
intrusionTrapSMM.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"))
)
if mibBuilder.loadTexts:
    intrusionTrapSMM.setStatus(
        "obsolete"
    )

addressMovedTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 7)
)
addressMovedTrapSMM.setObjects(
      *(("ICF-ETWIST", "hubAddrMoveAddress"),
        ("ICF-ETWIST", "hubAddrMoveOldGroup"),
        ("ICF-ETWIST", "hubAddrMoveOldPort"),
        ("ICF-ETWIST", "hubAddrMoveNewGroup"),
        ("ICF-ETWIST", "hubAddrMoveNewPort"))
)
if mibBuilder.loadTexts:
    addressMovedTrapSMM.setStatus(
        "obsolete"
    )

newAddressTrapSMM = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4, 0, 8)
)
newAddressTrapSMM.setObjects(
    ("SNMP-REPEATER-MIB", "rptrAddrTrackLastSourceAddress")
)
if mibBuilder.loadTexts:
    newAddressTrapSMM.setStatus(
        "obsolete"
    )


# Notifications groups


# Agent capabilities


# Module compliance

icfETwistHubCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    icfETwistHubCompliance.setStatus(
        "obsolete"
    )

icfETwistBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    icfETwistBridgeCompliance.setStatus(
        "obsolete"
    )

icfETwistHubDCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    icfETwistHubDCompliance.setStatus(
        "obsolete"
    )

icfETwistBridgeDCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 4)
)
if mibBuilder.loadTexts:
    icfETwistBridgeDCompliance.setStatus(
        "obsolete"
    )

icfETwistHub24SCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 5)
)
if mibBuilder.loadTexts:
    icfETwistHub24SCompliance.setStatus(
        "obsolete"
    )

icfAdvStkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 6)
)
if mibBuilder.loadTexts:
    icfAdvStkCompliance.setStatus(
        "obsolete"
    )

icfAdvStkSlaveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 7)
)
if mibBuilder.loadTexts:
    icfAdvStkSlaveCompliance.setStatus(
        "obsolete"
    )

icfAdvStkVGCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 8)
)
if mibBuilder.loadTexts:
    icfAdvStkVGCompliance.setStatus(
        "obsolete"
    )

icfAdvStkVGSlaveCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1, 11, 2, 1, 9)
)
if mibBuilder.loadTexts:
    icfAdvStkVGSlaveCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICF-ETWIST",
    **{"bridge1010TrapPrefix": bridge1010TrapPrefix,
       "thresholdTrap1010": thresholdTrap1010,
       "stpTrap1010": stpTrap1010,
       "temperatureTrap1010": temperatureTrap1010,
       "bridgeRemoteTrapPrefix": bridgeRemoteTrapPrefix,
       "thresholdTrapRem": thresholdTrapRem,
       "stpTrapRem": stpTrapRem,
       "temperatureTrapRem": temperatureTrapRem,
       "etherTwist12TrapPrefix": etherTwist12TrapPrefix,
       "thresholdTrapET12": thresholdTrapET12,
       "linkBeatTrapET12": linkBeatTrapET12,
       "segmentationTrapET12": segmentationTrapET12,
       "backupLinkTrapET12": backupLinkTrapET12,
       "fiberOpticTrapPrefix": fiberOpticTrapPrefix,
       "thresholdTrapFiber": thresholdTrapFiber,
       "linkBeatTrapFiber": linkBeatTrapFiber,
       "segmentationTrapFiber": segmentationTrapFiber,
       "backupLinkTrapFiber": backupLinkTrapFiber,
       "etherTwist48TrapPrefix": etherTwist48TrapPrefix,
       "thresholdTrapET48": thresholdTrapET48,
       "linkBeatTrapET48": linkBeatTrapET48,
       "segmentationTrapET48": segmentationTrapET48,
       "backupLinkTrapET48": backupLinkTrapET48,
       "thinLANTrapPrefix": thinLANTrapPrefix,
       "thresholdTrapTLAN": thresholdTrapTLAN,
       "linkBeatTrapTLAN": linkBeatTrapTLAN,
       "segmentationTrapTLAN": segmentationTrapTLAN,
       "backupLinkTrapTLAN": backupLinkTrapTLAN,
       "etherTwist24STrapPrefix": etherTwist24STrapPrefix,
       "thresholdTrapET24S": thresholdTrapET24S,
       "linkBeatTrapET24S": linkBeatTrapET24S,
       "segmentationTrapET24S": segmentationTrapET24S,
       "backupLinkTrapET24S": backupLinkTrapET24S,
       "intrusionTrapET24S": intrusionTrapET24S,
       "addressMovedTrapET24S": addressMovedTrapET24S,
       "newAddressTrapET24S": newAddressTrapET24S,
       "advStack12TrapPrefix": advStack12TrapPrefix,
       "thresholdTrapAS12": thresholdTrapAS12,
       "advStack24TrapPrefix": advStack24TrapPrefix,
       "thresholdTrapAS24": thresholdTrapAS24,
       "advStack48TrapPrefix": advStack48TrapPrefix,
       "thresholdTrapAS48": thresholdTrapAS48,
       "advStackU8TrapPrefix": advStackU8TrapPrefix,
       "thresholdTrapASU8": thresholdTrapASU8,
       "advStackU16TrapPrefix": advStackU16TrapPrefix,
       "thresholdTrapASU16": thresholdTrapASU16,
       "repeaterAgentTrapPrefix": repeaterAgentTrapPrefix,
       "thresholdTrapASEN": thresholdTrapASEN,
       "linkBeatTrapASEN": linkBeatTrapASEN,
       "segmentationTrapASEN": segmentationTrapASEN,
       "backupLinkTrapASEN": backupLinkTrapASEN,
       "intrusionTrapASEN": intrusionTrapASEN,
       "addressMovedTrapASEN": addressMovedTrapASEN,
       "newAddressTrapASEN": newAddressTrapASEN,
       "hpicfEnetSMMTrapPrefix": hpicfEnetSMMTrapPrefix,
       "thresholdTrapSMM": thresholdTrapSMM,
       "linkBeatTrapSMM": linkBeatTrapSMM,
       "segmentationTrapSMM": segmentationTrapSMM,
       "backupLinkTrapSMM": backupLinkTrapSMM,
       "intrusionTrapSMM": intrusionTrapSMM,
       "addressMovedTrapSMM": addressMovedTrapSMM,
       "newAddressTrapSMM": newAddressTrapSMM,
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
       "icfCommonAdmin": icfCommonAdmin,
       "icfEtwistMib": icfEtwistMib,
       "icfETwistConformance": icfETwistConformance,
       "icfETCompliances": icfETCompliances,
       "icfETwistHubCompliance": icfETwistHubCompliance,
       "icfETwistBridgeCompliance": icfETwistBridgeCompliance,
       "icfETwistHubDCompliance": icfETwistHubDCompliance,
       "icfETwistBridgeDCompliance": icfETwistBridgeDCompliance,
       "icfETwistHub24SCompliance": icfETwistHub24SCompliance,
       "icfAdvStkCompliance": icfAdvStkCompliance,
       "icfAdvStkSlaveCompliance": icfAdvStkSlaveCompliance,
       "icfAdvStkVGCompliance": icfAdvStkVGCompliance,
       "icfAdvStkVGSlaveCompliance": icfAdvStkVGSlaveCompliance,
       "icfETGroups": icfETGroups,
       "icfCommonBasicGroup": icfCommonBasicGroup,
       "icfCommonIpGroup": icfCommonIpGroup,
       "icfCommonIpxGroup": icfCommonIpxGroup,
       "icfEncryptedPasswordGroup": icfEncryptedPasswordGroup,
       "icfMappingGroup": icfMappingGroup,
       "icfIpMappingGroup": icfIpMappingGroup,
       "icfIpxMappingGroup": icfIpxMappingGroup,
       "icfSlaveMappingGroup": icfSlaveMappingGroup,
       "icf8023MacGroup": icf8023MacGroup,
       "icf8023MacSlaveGroup": icf8023MacSlaveGroup,
       "icfDownloadGroup": icfDownloadGroup,
       "hubBasicGroup": hubBasicGroup,
       "hubBasicSlaveGroup": hubBasicSlaveGroup,
       "hubMappingGroup": hubMappingGroup,
       "hubLinkBeatControlGroup": hubLinkBeatControlGroup,
       "hubBasicEnhancementsGroup": hubBasicEnhancementsGroup,
       "hubBasicAddrTableGroup": hubBasicAddrTableGroup,
       "hubReadableAddrTableGroup": hubReadableAddrTableGroup,
       "hubBackupLinkGroup": hubBackupLinkGroup,
       "hubNewEnhancementsGroup": hubNewEnhancementsGroup,
       "hubAddressMoveGroup": hubAddressMoveGroup,
       "hubLateEventMonitorGroup": hubLateEventMonitorGroup,
       "icfBridgeBasicGroup": icfBridgeBasicGroup,
       "icfBridgeSpanningTreeGroup": icfBridgeSpanningTreeGroup,
       "icfRemoteBridgeGroup": icfRemoteBridgeGroup,
       "icfConfigGroup": icfConfigGroup,
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
       "hubAddressMoveLogTable": hubAddressMoveLogTable,
       "hubAddressMoveLogEntry": hubAddressMoveLogEntry,
       "hubAddrMoveIndex": hubAddrMoveIndex,
       "hubAddrMoveAddress": hubAddrMoveAddress,
       "hubAddrMoveOldGroup": hubAddrMoveOldGroup,
       "hubAddrMoveOldPort": hubAddrMoveOldPort,
       "hubAddrMoveNewGroup": hubAddrMoveNewGroup,
       "hubAddrMoveNewPort": hubAddrMoveNewPort,
       "hubLateEventMonitor": hubLateEventMonitor,
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
       "icfConfigIfTable": icfConfigIfTable,
       "icfConfigIfEntry": icfConfigIfEntry,
       "icfConfigIfIndex": icfConfigIfIndex,
       "icfConfigIfIpAddress": icfConfigIfIpAddress,
       "icfConfigIfNetMask": icfConfigIfNetMask,
       "icfConfigIfDefaultGate": icfConfigIfDefaultGate,
       "icfConfigIpTTL": icfConfigIpTTL,
       "icfConfigBootpEnable": icfConfigBootpEnable}
)
