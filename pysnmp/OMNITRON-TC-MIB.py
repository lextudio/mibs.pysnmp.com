# SNMP MIB module (OMNITRON-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNITRON-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:43 2024
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

ostOmnitronTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 11)
)
ostOmnitronTcMib.setRevisions(
        ("2015-05-13 12:00",
         "2015-01-21 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OstAccessibiltyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )



class OstClassOfService(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class OstClockFreq(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class OstCosL2cpDstAddr(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )



class OstCosNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstCosNameStringOrNone(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )



class OstCosTrustType(Integer32, TextualConvention):
    status = "current"
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
        *(("cosGreenYellow", 5),
          ("cosTrust", 1),
          ("cosUseClass", 3),
          ("cosUsePri", 2),
          ("cosUsePriClass", 4))
    )



class OstEgressSchedulingProfileIndexType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class OstEgressQueueIndexType(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class OstElpsProtectType(Integer32, TextualConvention):
    status = "current"
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
        *(("e1plus1BiAps", 3),
          ("e1plus1UniAps", 2),
          ("e1plus1UniNoAps", 1),
          ("e1to1", 4),
          ("notAvailable", 5))
    )



class OstElpsRequestStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6,
              7,
              9,
              11,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 1),
          ("exercise", 4),
          ("forcedSwitch", 13),
          ("lockoutProtection", 15),
          ("manualSwitch", 7),
          ("manualSwitchWorking", 6),
          ("noRequest", 0),
          ("notAvailable", 16),
          ("revertRequest", 2),
          ("signalDegrade", 9),
          ("signalFailProtection", 14),
          ("signalFailWorking", 11),
          ("waitToRestore", 5))
    )



class OstElpsSignalStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalSignal", 1),
          ("notAvailable", 2),
          ("nullSignal", 0))
    )



class OstErpsLinkState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("na", 0),
          ("up", 1))
    )



class OstErpsPortState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 2),
          ("forward", 1),
          ("na", 0))
    )



class OstErpsPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rp0", 1),
          ("rp1", 2))
    )



class OstErpsRingStates(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("clear", 14),
          ("forcedSwtich", 13),
          ("localClearSignalFail", 10),
          ("localSignalFail", 11),
          ("manualSwitch", 7),
          ("noRequest", 0),
          ("rapsForcedSwitch", 12),
          ("rapsManualSwitch", 8),
          ("rapsNr", 1),
          ("rapsNrRb", 2),
          ("rapsSignalFail", 9),
          ("wtbExpires", 4),
          ("wtbRunning", 3),
          ("wtrExpires", 6),
          ("wtrRunning", 5))
    )



class OstErpsRingStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("forcedSwitch", 5),
          ("idle", 2),
          ("initializing", 1),
          ("manualSwitch", 4),
          ("pending", 6),
          ("protection", 3))
    )



class OstErrorString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class OstEvcNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstEvcNameStringOrNone(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )



class OstFileNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstFingerprintString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class OstFloatValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class OstFrameCount64(Counter64, TextualConvention):
    status = "current"
    displayHint = "d"


class OstFrameSizeList(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class OstIndexIntegerNextFree(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



class OstIpPriorityList(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class OstIpv6Addr(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:2x:2x:2x:2x:2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class OstIpAddr(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )



class OstMhfCreation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ostMHFdefault", 1),
          ("ostMHFexplicit", 2))
    )



class OstMipdMethodOfCreation(Integer32, TextualConvention):
    status = "current"
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
        *(("ostExplicit", 1),
          ("ostExplicitImplicitMa", 4),
          ("ostImplicitMa", 2),
          ("ostImplicitMde", 3))
    )



class OstModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("normal", 1),
          ("sp", 3))
    )



class OstModuleSingleIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 9999),
    )



class OstPcpPriorityList(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )



class OstPortClockType(Integer32, TextualConvention):
    status = "current"
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
        *(("adaptiveAcqu", 2),
          ("adaptiveIdle", 1),
          ("adaptiveTrk1", 3),
          ("adaptiveTrk2", 4),
          ("coax", 6),
          ("holdOver", 5),
          ("internal", 7),
          ("line", 8))
    )



class OstPortList(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"


class OstPortNumber(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )



class OstPortSingleIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10101, 999999),
    )



class OstPriority(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class OstProbeNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstProfileNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class OstTestResultType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("oversubscribe", 3),
          ("pass", 1))
    )



class OstTestStatusType(Integer32, TextualConvention):
    status = "current"
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
        *(("testCompleted", 4),
          ("testInProcess", 2),
          ("testInitializing", 5),
          ("testNotStarted", 1),
          ("testStopped", 3))
    )



class OstUnsigned64(Counter64, TextualConvention):
    status = "current"
    displayHint = "d"


class OstUserNameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class OstVlanId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class OstVlanIdList(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 110),
    )



# MIB Managed Objects in the order of their OIDs

_Omnitron_ObjectIdentity = ObjectIdentity
omnitron = _Omnitron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342)
)
_IcAgent_ObjectIdentity = ObjectIdentity
icAgent = _IcAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNITRON-TC-MIB",
    **{"OstAccessibiltyType": OstAccessibiltyType,
       "OstClassOfService": OstClassOfService,
       "OstClockFreq": OstClockFreq,
       "OstCosL2cpDstAddr": OstCosL2cpDstAddr,
       "OstCosNameString": OstCosNameString,
       "OstCosNameStringOrNone": OstCosNameStringOrNone,
       "OstCosTrustType": OstCosTrustType,
       "OstEgressSchedulingProfileIndexType": OstEgressSchedulingProfileIndexType,
       "OstEgressQueueIndexType": OstEgressQueueIndexType,
       "OstElpsProtectType": OstElpsProtectType,
       "OstElpsRequestStates": OstElpsRequestStates,
       "OstElpsSignalStates": OstElpsSignalStates,
       "OstErpsLinkState": OstErpsLinkState,
       "OstErpsPortState": OstErpsPortState,
       "OstErpsPortType": OstErpsPortType,
       "OstErpsRingStates": OstErpsRingStates,
       "OstErpsRingStatus": OstErpsRingStatus,
       "OstErrorString": OstErrorString,
       "OstEvcNameString": OstEvcNameString,
       "OstEvcNameStringOrNone": OstEvcNameStringOrNone,
       "OstFileNameString": OstFileNameString,
       "OstFingerprintString": OstFingerprintString,
       "OstFloatValue": OstFloatValue,
       "OstFrameCount64": OstFrameCount64,
       "OstFrameSizeList": OstFrameSizeList,
       "OstIndexIntegerNextFree": OstIndexIntegerNextFree,
       "OstIpPriorityList": OstIpPriorityList,
       "OstIpv6Addr": OstIpv6Addr,
       "OstIpAddr": OstIpAddr,
       "OstMhfCreation": OstMhfCreation,
       "OstMipdMethodOfCreation": OstMipdMethodOfCreation,
       "OstModeType": OstModeType,
       "OstModuleSingleIndex": OstModuleSingleIndex,
       "OstPcpPriorityList": OstPcpPriorityList,
       "OstPortClockType": OstPortClockType,
       "OstPortList": OstPortList,
       "OstPortNumber": OstPortNumber,
       "OstPortSingleIndex": OstPortSingleIndex,
       "OstPriority": OstPriority,
       "OstProbeNameString": OstProbeNameString,
       "OstProfileNameString": OstProfileNameString,
       "OstTestResultType": OstTestResultType,
       "OstTestStatusType": OstTestStatusType,
       "OstUnsigned64": OstUnsigned64,
       "OstUserNameString": OstUserNameString,
       "OstVlanId": OstVlanId,
       "OstVlanIdList": OstVlanIdList,
       "omnitron": omnitron,
       "icAgent": icAgent,
       "ostOmnitronTcMib": ostOmnitronTcMib}
)
