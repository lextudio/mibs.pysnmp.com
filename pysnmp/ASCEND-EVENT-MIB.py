# SNMP MIB module (ASCEND-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:56 2024
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

(eventGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "eventGroup")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EventMaximumNumberOfEvents_Type = Integer32
_EventMaximumNumberOfEvents_Object = MibScalar
eventMaximumNumberOfEvents = _EventMaximumNumberOfEvents_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 1),
    _EventMaximumNumberOfEvents_Type()
)
eventMaximumNumberOfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventMaximumNumberOfEvents.setStatus("mandatory")
_EventOldestEventIdNumber_Type = Integer32
_EventOldestEventIdNumber_Object = MibScalar
eventOldestEventIdNumber = _EventOldestEventIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 2),
    _EventOldestEventIdNumber_Type()
)
eventOldestEventIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOldestEventIdNumber.setStatus("mandatory")
_EventLatestEventIdNumber_Type = Integer32
_EventLatestEventIdNumber_Object = MibScalar
eventLatestEventIdNumber = _EventLatestEventIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 3),
    _EventLatestEventIdNumber_Type()
)
eventLatestEventIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLatestEventIdNumber.setStatus("mandatory")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1)
)
eventEntry.setIndexNames(
    (0, "ASCEND-EVENT-MIB", "eventIdNumber"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")
_EventIdNumber_Type = Integer32
_EventIdNumber_Object = MibTableColumn
eventIdNumber = _EventIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 1),
    _EventIdNumber_Type()
)
eventIdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIdNumber.setStatus("mandatory")
_EventTimeStamp_Type = Integer32
_EventTimeStamp_Object = MibTableColumn
eventTimeStamp = _EventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 2),
    _EventTimeStamp_Type()
)
eventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTimeStamp.setStatus("mandatory")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
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
        *(("baudRateChanged", 6),
          ("callAnswered", 2),
          ("callCleared", 3),
          ("callOriginated", 1),
          ("nameChanged", 5),
          ("serviceChanged", 4))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("mandatory")
_EventCallReferenceNum_Type = Integer32
_EventCallReferenceNum_Object = MibTableColumn
eventCallReferenceNum = _EventCallReferenceNum_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 4),
    _EventCallReferenceNum_Type()
)
eventCallReferenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCallReferenceNum.setStatus("mandatory")
_EventDataRate_Type = Integer32
_EventDataRate_Object = MibTableColumn
eventDataRate = _EventDataRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 5),
    _EventDataRate_Type()
)
eventDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDataRate.setStatus("mandatory")
_EventSlotNumber_Type = Integer32
_EventSlotNumber_Object = MibTableColumn
eventSlotNumber = _EventSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 6),
    _EventSlotNumber_Type()
)
eventSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSlotNumber.setStatus("mandatory")
_EventSlotLineNumber_Type = Integer32
_EventSlotLineNumber_Object = MibTableColumn
eventSlotLineNumber = _EventSlotLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 7),
    _EventSlotLineNumber_Type()
)
eventSlotLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSlotLineNumber.setStatus("mandatory")
_EventSlotChannelNumber_Type = Integer32
_EventSlotChannelNumber_Object = MibTableColumn
eventSlotChannelNumber = _EventSlotChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 8),
    _EventSlotChannelNumber_Type()
)
eventSlotChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSlotChannelNumber.setStatus("mandatory")
_EventModemSlotNumber_Type = Integer32
_EventModemSlotNumber_Object = MibTableColumn
eventModemSlotNumber = _EventModemSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 9),
    _EventModemSlotNumber_Type()
)
eventModemSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventModemSlotNumber.setStatus("mandatory")
_EventModemOnSlot_Type = Integer32
_EventModemOnSlot_Object = MibTableColumn
eventModemOnSlot = _EventModemOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 10),
    _EventModemOnSlot_Type()
)
eventModemOnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventModemOnSlot.setStatus("mandatory")


class _EventCurrentService_Type(Integer32):
    """Custom type eventCurrentService based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("atm", 20),
          ("combinet", 7),
          ("dchannelX25", 17),
          ("dtpt", 18),
          ("euraw", 9),
          ("euui", 10),
          ("frameRelay", 8),
          ("hdlcNrm", 21),
          ("ipFax", 19),
          ("mp", 15),
          ("mpp", 5),
          ("netToNet", 25),
          ("none", 1),
          ("other", 2),
          ("ppp", 3),
          ("rawTcp", 13),
          ("slip", 4),
          ("telnet", 11),
          ("telnetBinary", 12),
          ("terminalServer", 14),
          ("virtualConnect", 16),
          ("visa2", 23),
          ("voip", 22),
          ("x25", 6))
    )


_EventCurrentService_Type.__name__ = "Integer32"
_EventCurrentService_Object = MibTableColumn
eventCurrentService = _EventCurrentService_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 11),
    _EventCurrentService_Type()
)
eventCurrentService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCurrentService.setStatus("mandatory")
_EventUserName_Type = DisplayString
_EventUserName_Object = MibTableColumn
eventUserName = _EventUserName_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 12),
    _EventUserName_Type()
)
eventUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventUserName.setStatus("mandatory")
_EventUserIPAddress_Type = IpAddress
_EventUserIPAddress_Object = MibTableColumn
eventUserIPAddress = _EventUserIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 13),
    _EventUserIPAddress_Type()
)
eventUserIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventUserIPAddress.setStatus("mandatory")
_EventUserSubnetMask_Type = IpAddress
_EventUserSubnetMask_Object = MibTableColumn
eventUserSubnetMask = _EventUserSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 14),
    _EventUserSubnetMask_Type()
)
eventUserSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventUserSubnetMask.setStatus("mandatory")


class _EventDisconnectReason_Type(Integer32):
    """Custom type eventDisconnectReason based on Integer32"""
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
              35,
              36,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              90,
              100,
              101,
              102,
              103,
              105,
              106,
              115,
              120,
              150,
              151,
              152,
              160,
              170,
              171,
              180,
              181,
              185,
              190,
              195,
              201,
              210,
              220,
              230,
              240,
              241,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              260,
              261,
              262,
              300,
              350,
              370,
              400,
              420,
              425,
              450,
              500,
              501,
              502,
              503,
              504,
              505,
              506,
              507,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              801,
              802,
              803,
              806,
              816,
              817,
              818,
              819,
              821,
              822,
              827,
              828,
              829,
              830,
              831,
              834,
              838,
              841,
              842,
              843,
              844,
              845,
              847,
              850,
              852,
              854,
              858,
              863,
              865,
              866,
              869,
              881,
              882,
              888,
              896,
              897,
              898,
              899,
              900,
              901,
              902,
              903,
              911,
              927)
        )
    )
    namedValues = NamedValues(
        *(("backupCleared", 241),
          ("biDirectionalAuthFailed", 450),
          ("callbackDialoutFailed", 400),
          ("clidAuthFailed", 4),
          ("clidAuthRequestCallback", 6),
          ("clidAuthServTimeout", 5),
          ("disconnected", 3),
          ("dnisDenied", 370),
          ("dropUtilization", 36),
          ("filterProfileNotFound", 425),
          ("h323DropReasonCoderDenied", 516),
          ("h323DropReasonDestBusy", 502),
          ("h323DropReasonDestUnreachable", 503),
          ("h323DropReasonFegwCauseCode", 514),
          ("h323DropReasonGatewayResources", 506),
          ("h323DropReasonGwNotRegistered", 508),
          ("h323DropReasonHostDrop", 517),
          ("h323DropReasonInvalidDnis", 510),
          ("h323DropReasonInvalidPin", 509),
          ("h323DropReasonMaxPinAttempts", 515),
          ("h323DropReasonNoBandwidth", 507),
          ("h323DropReasonNoLanAnswer", 511),
          ("h323DropReasonNoLanDisconnect", 513),
          ("h323DropReasonNormal", 501),
          ("h323DropReasonNull", 500),
          ("h323DropReasonReject", 504),
          ("h323DropReasonStateMachine", 512),
          ("h323DropReasonWanFailure", 505),
          ("invalidProtocol", 120),
          ("ipfaxBadDecode", 260),
          ("ipfaxCallCleared", 250),
          ("ipfaxDecodeError", 261),
          ("ipfaxIncomingError", 252),
          ("ipfaxLowMemory", 251),
          ("ipfaxNoModemAvail", 254),
          ("ipfaxNoServer", 262),
          ("ipfaxNoSession", 257),
          ("ipfaxOpenError", 255),
          ("ipfaxOutgoingError", 253),
          ("ipfaxParsePhonestr", 258),
          ("ipfaxTcpWrite", 256),
          ("localAdmin", 151),
          ("localSnmp", 152),
          ("lowMemory", 201),
          ("lqmTerminated", 240),
          ("maxCallDurationReached", 195),
          ("mpMasterCardDied", 350),
          ("mpNullMessageTimeout", 35),
          ("noModemAvailable", 9),
          ("noModemForcedDisconnect", 18),
          ("noModemLossCarrier", 11),
          ("noModemMissingOK", 15),
          ("noModemNoCarrier", 10),
          ("noModemOpenFailed", 13),
          ("noModemOpenFailedDiag", 14),
          ("noModemPumpDead", 17),
          ("noModemResultCodes", 12),
          ("noModemStuckMsgQueue", 16),
          ("noPortAvailable", 90),
          ("notApplicable", 1),
          ("pppAuthTimeout", 170),
          ("pppCHAPAuthFail", 43),
          ("pppCbcpRequired", 220),
          ("pppCloseEvent", 46),
          ("pppCloseMpAddChanFail", 49),
          ("pppCloseNoNcpsOpened", 47),
          ("pppCloseUnknownMpBundle", 48),
          ("pppIffReleased", 171),
          ("pppLcpNegotiateFail", 41),
          ("pppLcpTimeout", 40),
          ("pppPAPAuthFail", 42),
          ("pppRcvTerminate", 45),
          ("pppRemoteAuthFail", 44),
          ("preT310Timeout", 7),
          ("privateRouteTableNotFound", 420),
          ("q850AccessInfoDiscarded", 843),
          ("q850BearCapNotAvail", 858),
          ("q850CallRejected", 821),
          ("q850CapNotImplemented", 865),
          ("q850ChanDoesNotExist", 882),
          ("q850ChanNotImplemented", 866),
          ("q850ChannelUnacceptable", 806),
          ("q850DestOutOfOrder", 827),
          ("q850FacilityNotImplement", 869),
          ("q850FacilityNotSubscribed", 850),
          ("q850FacilityRejected", 829),
          ("q850IncomingCallBarred", 854),
          ("q850IncompatibleDest", 888),
          ("q850InterworkingUnspec", 927),
          ("q850InvalidCallRef", 881),
          ("q850InvalidElemContents", 900),
          ("q850InvalidNumberFormat", 828),
          ("q850MandatoryIeLenErr", 903),
          ("q850MandatoryIeMissing", 896),
          ("q850NetworkCongestion", 842),
          ("q850NetworkOutOfOrder", 838),
          ("q850NoCircuitAvailable", 834),
          ("q850NoRoute", 802),
          ("q850NoRouteToDest", 803),
          ("q850NoUserResponding", 818),
          ("q850NonexistentIe", 899),
          ("q850NonexistentMsg", 897),
          ("q850NormalClearing", 816),
          ("q850NumberChanged", 822),
          ("q850OutgoingCallBarred", 852),
          ("q850PreEmpted", 845),
          ("q850ProtocolError", 911),
          ("q850ReqChannelNotAvail", 844),
          ("q850ResourceNotAvail", 847),
          ("q850RespToStatEnq", 830),
          ("q850ServiceNotAvail", 863),
          ("q850TemporaryFailure", 841),
          ("q850TimerExpiry", 902),
          ("q850UnassignedNumber", 801),
          ("q850UnspecifiedCause", 831),
          ("q850UserAlertNoAnswer", 819),
          ("q850UserBusy", 817),
          ("q850WrongMessage", 898),
          ("q850WrongMsgForStat", 901),
          ("remoteEndHungUp", 185),
          ("requestByRadiusClient", 150),
          ("resourceQuiesced", 190),
          ("sessCallback", 102),
          ("sessDtptSourceCleared", 115),
          ("sessFailSecurity", 101),
          ("sessOutgoingInvalid", 103),
          ("sessTimeOut", 100),
          ("sessTimeoutEncaps", 105),
          ("sessTimeoutMp", 106),
          ("slotCardDied", 210),
          ("systemCallClearRequest", 181),
          ("tsClosedVirtualConnect", 29),
          ("tsControlC", 27),
          ("tsDestroyed", 28),
          ("tsErrorResource", 33),
          ("tsExitErrBadPort", 54),
          ("tsExitErrClosed", 63),
          ("tsExitErrConnRefused", 61),
          ("tsExitErrHostAdminUnreach", 67),
          ("tsExitErrHostName", 53),
          ("tsExitErrHostReset", 60),
          ("tsExitErrHostUnreach", 65),
          ("tsExitErrInvalidIP", 52),
          ("tsExitErrNetAdminUnreach", 66),
          ("tsExitErrNetUnreach", 64),
          ("tsExitErrPortUnreach", 68),
          ("tsExitErrResource", 51),
          ("tsExitErrTimedOut", 62),
          ("tsExitErrTooMany", 50),
          ("tsExitRlogin", 31),
          ("tsExitTcp", 24),
          ("tsExitTelnet", 22),
          ("tsIdleTimeout", 21),
          ("tsNoIPAddr", 23),
          ("tsPassWordFail", 25),
          ("tsRawTCPDisable", 26),
          ("tsRloginBadOption", 32),
          ("tsUserExit", 20),
          ("tsVirtualConnectDestroyed", 30),
          ("unknown", 2),
          ("userCallClearRequest", 180),
          ("v110Timeout", 160),
          ("vrouterDeleted", 230),
          ("x25Termsrv", 300))
    )


_EventDisconnectReason_Type.__name__ = "Integer32"
_EventDisconnectReason_Object = MibTableColumn
eventDisconnectReason = _EventDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 15),
    _EventDisconnectReason_Type()
)
eventDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDisconnectReason.setStatus("mandatory")


class _EventConnectProgress_Type(Integer32):
    """Custom type eventConnectProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              10,
              11,
              30,
              31,
              32,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              50,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              80,
              81,
              82,
              83,
              84,
              85,
              90,
              91,
              92,
              93,
              94,
              100,
              101,
              102,
              120,
              121,
              200,
              201,
              202,
              203,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              400,
              401,
              402,
              403,
              404)
        )
    )
    namedValues = NamedValues(
        *(("prAtNcpOpened", 81),
          ("prAuthOpened", 203),
          ("prBACPOpened", 83),
          ("prBACPOpening", 82),
          ("prBNCPOpened", 68),
          ("prCBCPOpened", 85),
          ("prCBCPOpening", 84),
          ("prCCPOpened", 66),
          ("prCallUp", 10),
          ("prClidAuthFailed", 101),
          ("prClidAuthTimeout", 102),
          ("prClidCallBackReq", 100),
          ("prDialSrvcBlocked", 11),
          ("prFRLinkActive", 121),
          ("prFRLinkInactive", 120),
          ("prH323CallConnected", 312),
          ("prH323DetectingDnisFromWan", 302),
          ("prH323DetectingPinFromWan", 301),
          ("prH323DialingOutToWan", 310),
          ("prH323DisconnectingRtp", 314),
          ("prH323FaxDisconnected", 316),
          ("prH323HairpinDialingOutToWan", 308),
          ("prH323NewIncomingCallFromWan", 300),
          ("prH323PlayingBusyPromptToWan", 313),
          ("prH323PlayingErrPromptToWan", 307),
          ("prH323ReceivedAcfFromGatekeeper", 304),
          ("prH323ReceivedH225SetupFromLan", 309),
          ("prH323RtpDisconnected", 315),
          ("prH323SendingArqToGatekeeper", 303),
          ("prH323WaitingH225AlertingFromLan", 305),
          ("prH323WaitingH225ProceedingFromLan", 306),
          ("prH323WanAnsweredAndRtpNotUpYet", 311),
          ("prIPNCPOpened", 67),
          ("prIPXNCPOpened", 80),
          ("prLCPOpened", 65),
          ("prLCPStateAckRecd", 76),
          ("prLCPStateAckSent", 77),
          ("prLCPStateClosed", 71),
          ("prLCPStateClosing", 73),
          ("prLCPStateInitial", 69),
          ("prLCPStateReqSent", 75),
          ("prLCPStateStarting", 70),
          ("prLCPStateStopped", 72),
          ("prLCPStateStopping", 74),
          ("prLanSessionUp", 60),
          ("prModemOutdialCallUp", 50),
          ("prModemUp", 30),
          ("prModemWaitCodes", 32),
          ("prModemWaitDCD", 31),
          ("prNotApplicable", 1),
          ("prNotConnected", 7),
          ("prOpeningAuth", 201),
          ("prOpeningBNCP", 64),
          ("prOpeningCCP", 62),
          ("prOpeningIPNCP", 63),
          ("prOpeningLCP", 61),
          ("prRawTcpConnect", 43),
          ("prRawTcpStarting", 41),
          ("prRloginConnect", 46),
          ("prRloginStarting", 45),
          ("prSkippingAuth", 202),
          ("prSs7VoipCedDetected", 404),
          ("prSs7VoipChangeParameter", 400),
          ("prSs7VoipRtpClosed", 402),
          ("prSs7VoipRtpOpened", 401),
          ("prSs7VoipTerminateRtp", 403),
          ("prStartingAuth", 200),
          ("prTelnetConnect", 44),
          ("prTelnetStarting", 42),
          ("prTermSrvStarted", 40),
          ("prTermSrvStartedThruCR", 47),
          ("prUnknown", 2),
          ("prV110StateCarrier", 92),
          ("prV110StateClosed", 94),
          ("prV110StateOpened", 91),
          ("prV110StateReset", 93),
          ("prV110Up", 90))
    )


_EventConnectProgress_Type.__name__ = "Integer32"
_EventConnectProgress_Object = MibTableColumn
eventConnectProgress = _EventConnectProgress_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 16),
    _EventConnectProgress_Type()
)
eventConnectProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventConnectProgress.setStatus("mandatory")
_EventCallCharge_Type = Integer32
_EventCallCharge_Object = MibTableColumn
eventCallCharge = _EventCallCharge_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 17),
    _EventCallCharge_Type()
)
eventCallCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCallCharge.setStatus("mandatory")
_EventCalledPartyID_Type = DisplayString
_EventCalledPartyID_Object = MibTableColumn
eventCalledPartyID = _EventCalledPartyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 18),
    _EventCalledPartyID_Type()
)
eventCalledPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCalledPartyID.setStatus("mandatory")
_EventCallingPartyID_Type = DisplayString
_EventCallingPartyID_Object = MibTableColumn
eventCallingPartyID = _EventCallingPartyID_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 19),
    _EventCallingPartyID_Type()
)
eventCallingPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCallingPartyID.setStatus("mandatory")
_EventInOctets_Type = Integer32
_EventInOctets_Object = MibTableColumn
eventInOctets = _EventInOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 20),
    _EventInOctets_Type()
)
eventInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInOctets.setStatus("mandatory")
_EventOutOctets_Type = Integer32
_EventOutOctets_Object = MibTableColumn
eventOutOctets = _EventOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 21),
    _EventOutOctets_Type()
)
eventOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOutOctets.setStatus("mandatory")
_EventMultiLinkID_Type = Integer32
_EventMultiLinkID_Object = MibTableColumn
eventMultiLinkID = _EventMultiLinkID_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 22),
    _EventMultiLinkID_Type()
)
eventMultiLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventMultiLinkID.setStatus("mandatory")
_EventXmitRate_Type = Integer32
_EventXmitRate_Object = MibTableColumn
eventXmitRate = _EventXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 23),
    _EventXmitRate_Type()
)
eventXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventXmitRate.setStatus("mandatory")
_EventTrunkGroup_Type = Integer32
_EventTrunkGroup_Object = MibTableColumn
eventTrunkGroup = _EventTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 4, 1, 24),
    _EventTrunkGroup_Type()
)
eventTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTrunkGroup.setStatus("mandatory")
_EventCurrentActiveCalls_Type = Integer32
_EventCurrentActiveCalls_Object = MibScalar
eventCurrentActiveCalls = _EventCurrentActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 5),
    _EventCurrentActiveCalls_Type()
)
eventCurrentActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCurrentActiveCalls.setStatus("mandatory")
_EventCurrentActiveSessions_Type = Integer32
_EventCurrentActiveSessions_Object = MibScalar
eventCurrentActiveSessions = _EventCurrentActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 6),
    _EventCurrentActiveSessions_Type()
)
eventCurrentActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCurrentActiveSessions.setStatus("mandatory")
_EventTotalCalls_Type = Counter32
_EventTotalCalls_Object = MibScalar
eventTotalCalls = _EventTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 7),
    _EventTotalCalls_Type()
)
eventTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalCalls.setStatus("mandatory")
_EventTotalSessions_Type = Counter32
_EventTotalSessions_Object = MibScalar
eventTotalSessions = _EventTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 8),
    _EventTotalSessions_Type()
)
eventTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalSessions.setStatus("mandatory")
_EventTotalCallsAnswered_Type = Counter32
_EventTotalCallsAnswered_Object = MibScalar
eventTotalCallsAnswered = _EventTotalCallsAnswered_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 9),
    _EventTotalCallsAnswered_Type()
)
eventTotalCallsAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalCallsAnswered.setStatus("mandatory")
_EventTotalCallsOriginated_Type = Counter32
_EventTotalCallsOriginated_Object = MibScalar
eventTotalCallsOriginated = _EventTotalCallsOriginated_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 10),
    _EventTotalCallsOriginated_Type()
)
eventTotalCallsOriginated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalCallsOriginated.setStatus("mandatory")
_EventTotalCallsCleared_Type = Counter32
_EventTotalCallsCleared_Object = MibScalar
eventTotalCallsCleared = _EventTotalCallsCleared_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 11),
    _EventTotalCallsCleared_Type()
)
eventTotalCallsCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalCallsCleared.setStatus("mandatory")
_EventTotalBaudRateChanges_Type = Counter32
_EventTotalBaudRateChanges_Object = MibScalar
eventTotalBaudRateChanges = _EventTotalBaudRateChanges_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 12),
    _EventTotalBaudRateChanges_Type()
)
eventTotalBaudRateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalBaudRateChanges.setStatus("mandatory")
_EventTotalServiceChanges_Type = Counter32
_EventTotalServiceChanges_Object = MibScalar
eventTotalServiceChanges = _EventTotalServiceChanges_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 13),
    _EventTotalServiceChanges_Type()
)
eventTotalServiceChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalServiceChanges.setStatus("mandatory")
_EventTotalNameChanges_Type = Counter32
_EventTotalNameChanges_Object = MibScalar
eventTotalNameChanges = _EventTotalNameChanges_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 14),
    _EventTotalNameChanges_Type()
)
eventTotalNameChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalNameChanges.setStatus("mandatory")
_EventTotalNoModems_Type = Counter32
_EventTotalNoModems_Object = MibScalar
eventTotalNoModems = _EventTotalNoModems_Object(
    (1, 3, 6, 1, 4, 1, 529, 10, 15),
    _EventTotalNoModems_Type()
)
eventTotalNoModems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTotalNoModems.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-EVENT-MIB",
    **{"DisplayString": DisplayString,
       "eventMaximumNumberOfEvents": eventMaximumNumberOfEvents,
       "eventOldestEventIdNumber": eventOldestEventIdNumber,
       "eventLatestEventIdNumber": eventLatestEventIdNumber,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIdNumber": eventIdNumber,
       "eventTimeStamp": eventTimeStamp,
       "eventType": eventType,
       "eventCallReferenceNum": eventCallReferenceNum,
       "eventDataRate": eventDataRate,
       "eventSlotNumber": eventSlotNumber,
       "eventSlotLineNumber": eventSlotLineNumber,
       "eventSlotChannelNumber": eventSlotChannelNumber,
       "eventModemSlotNumber": eventModemSlotNumber,
       "eventModemOnSlot": eventModemOnSlot,
       "eventCurrentService": eventCurrentService,
       "eventUserName": eventUserName,
       "eventUserIPAddress": eventUserIPAddress,
       "eventUserSubnetMask": eventUserSubnetMask,
       "eventDisconnectReason": eventDisconnectReason,
       "eventConnectProgress": eventConnectProgress,
       "eventCallCharge": eventCallCharge,
       "eventCalledPartyID": eventCalledPartyID,
       "eventCallingPartyID": eventCallingPartyID,
       "eventInOctets": eventInOctets,
       "eventOutOctets": eventOutOctets,
       "eventMultiLinkID": eventMultiLinkID,
       "eventXmitRate": eventXmitRate,
       "eventTrunkGroup": eventTrunkGroup,
       "eventCurrentActiveCalls": eventCurrentActiveCalls,
       "eventCurrentActiveSessions": eventCurrentActiveSessions,
       "eventTotalCalls": eventTotalCalls,
       "eventTotalSessions": eventTotalSessions,
       "eventTotalCallsAnswered": eventTotalCallsAnswered,
       "eventTotalCallsOriginated": eventTotalCallsOriginated,
       "eventTotalCallsCleared": eventTotalCallsCleared,
       "eventTotalBaudRateChanges": eventTotalBaudRateChanges,
       "eventTotalServiceChanges": eventTotalServiceChanges,
       "eventTotalNameChanges": eventTotalNameChanges,
       "eventTotalNoModems": eventTotalNoModems}
)
