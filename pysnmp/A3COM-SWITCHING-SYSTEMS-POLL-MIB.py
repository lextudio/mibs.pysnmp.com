# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-POLL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-POLL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:51 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComPoll_ObjectIdentity = ObjectIdentity
a3ComPoll = _A3ComPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22)
)
_A3ComPollTable_Object = MibTable
a3ComPollTable = _A3ComPollTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1)
)
if mibBuilder.loadTexts:
    a3ComPollTable.setStatus("mandatory")
_A3ComPollEntry_Object = MibTableRow
a3ComPollEntry = _A3ComPollEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1)
)
a3ComPollEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollIndex"),
)
if mibBuilder.loadTexts:
    a3ComPollEntry.setStatus("mandatory")


class _A3ComPollIndex_Type(Integer32):
    """Custom type a3ComPollIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComPollIndex_Type.__name__ = "Integer32"
_A3ComPollIndex_Object = MibTableColumn
a3ComPollIndex = _A3ComPollIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 1),
    _A3ComPollIndex_Type()
)
a3ComPollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollIndex.setStatus("mandatory")


class _A3ComPollAddress_Type(DisplayString):
    """Custom type a3ComPollAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3ComPollAddress_Type.__name__ = "DisplayString"
_A3ComPollAddress_Object = MibTableColumn
a3ComPollAddress = _A3ComPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 2),
    _A3ComPollAddress_Type()
)
a3ComPollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollAddress.setStatus("mandatory")


class _A3ComPollAddressType_Type(Integer32):
    """Custom type a3ComPollAddressType based on Integer32"""
    defaultValue = 1

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
        *(("appletalk", 6),
          ("ip", 2),
          ("ipdotted", 3),
          ("ipname", 4),
          ("ipx", 5),
          ("unknown", 1))
    )


_A3ComPollAddressType_Type.__name__ = "Integer32"
_A3ComPollAddressType_Object = MibTableColumn
a3ComPollAddressType = _A3ComPollAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 3),
    _A3ComPollAddressType_Type()
)
a3ComPollAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollAddressType.setStatus("mandatory")


class _A3ComPollCount_Type(Integer32):
    """Custom type a3ComPollCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_A3ComPollCount_Type.__name__ = "Integer32"
_A3ComPollCount_Object = MibTableColumn
a3ComPollCount = _A3ComPollCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 4),
    _A3ComPollCount_Type()
)
a3ComPollCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollCount.setStatus("mandatory")


class _A3ComPollAttempts_Type(Integer32):
    """Custom type a3ComPollAttempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_A3ComPollAttempts_Type.__name__ = "Integer32"
_A3ComPollAttempts_Object = MibTableColumn
a3ComPollAttempts = _A3ComPollAttempts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 5),
    _A3ComPollAttempts_Type()
)
a3ComPollAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollAttempts.setStatus("mandatory")


class _A3ComPollRate_Type(Integer32):
    """Custom type a3ComPollRate based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5400),
    )


_A3ComPollRate_Type.__name__ = "Integer32"
_A3ComPollRate_Object = MibTableColumn
a3ComPollRate = _A3ComPollRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 6),
    _A3ComPollRate_Type()
)
a3ComPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollRate.setStatus("mandatory")


class _A3ComPollResponseTimeOut_Type(Integer32):
    """Custom type a3ComPollResponseTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_A3ComPollResponseTimeOut_Type.__name__ = "Integer32"
_A3ComPollResponseTimeOut_Object = MibTableColumn
a3ComPollResponseTimeOut = _A3ComPollResponseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 7),
    _A3ComPollResponseTimeOut_Type()
)
a3ComPollResponseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollResponseTimeOut.setStatus("mandatory")


class _A3ComPollPacketSize_Type(Integer32):
    """Custom type a3ComPollPacketSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_A3ComPollPacketSize_Type.__name__ = "Integer32"
_A3ComPollPacketSize_Object = MibTableColumn
a3ComPollPacketSize = _A3ComPollPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 8),
    _A3ComPollPacketSize_Type()
)
a3ComPollPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollPacketSize.setStatus("mandatory")


class _A3ComPollSourceAddress_Type(DisplayString):
    """Custom type a3ComPollSourceAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_A3ComPollSourceAddress_Type.__name__ = "DisplayString"
_A3ComPollSourceAddress_Object = MibTableColumn
a3ComPollSourceAddress = _A3ComPollSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 9),
    _A3ComPollSourceAddress_Type()
)
a3ComPollSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollSourceAddress.setStatus("mandatory")
_A3ComPollMinRoundTripTime_Type = Integer32
_A3ComPollMinRoundTripTime_Object = MibTableColumn
a3ComPollMinRoundTripTime = _A3ComPollMinRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 10),
    _A3ComPollMinRoundTripTime_Type()
)
a3ComPollMinRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollMinRoundTripTime.setStatus("mandatory")
_A3ComPollAvgRoundTripTime_Type = Integer32
_A3ComPollAvgRoundTripTime_Object = MibTableColumn
a3ComPollAvgRoundTripTime = _A3ComPollAvgRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 11),
    _A3ComPollAvgRoundTripTime_Type()
)
a3ComPollAvgRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollAvgRoundTripTime.setStatus("mandatory")
_A3ComPollMaxRoundTripTime_Type = Integer32
_A3ComPollMaxRoundTripTime_Object = MibTableColumn
a3ComPollMaxRoundTripTime = _A3ComPollMaxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 12),
    _A3ComPollMaxRoundTripTime_Type()
)
a3ComPollMaxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollMaxRoundTripTime.setStatus("mandatory")
_A3ComPollFramesSent_Type = Integer32
_A3ComPollFramesSent_Object = MibTableColumn
a3ComPollFramesSent = _A3ComPollFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 13),
    _A3ComPollFramesSent_Type()
)
a3ComPollFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollFramesSent.setStatus("mandatory")
_A3ComPollFramesReceived_Type = Integer32
_A3ComPollFramesReceived_Object = MibTableColumn
a3ComPollFramesReceived = _A3ComPollFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 14),
    _A3ComPollFramesReceived_Type()
)
a3ComPollFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollFramesReceived.setStatus("mandatory")


class _A3ComPollInformation_Type(DisplayString):
    """Custom type a3ComPollInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_A3ComPollInformation_Type.__name__ = "DisplayString"
_A3ComPollInformation_Object = MibTableColumn
a3ComPollInformation = _A3ComPollInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 15),
    _A3ComPollInformation_Type()
)
a3ComPollInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollInformation.setStatus("mandatory")
_A3ComPollOwner_Type = DisplayString
_A3ComPollOwner_Object = MibTableColumn
a3ComPollOwner = _A3ComPollOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 16),
    _A3ComPollOwner_Type()
)
a3ComPollOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollOwner.setStatus("mandatory")


class _A3ComPollReport_Type(Integer32):
    """Custom type a3ComPollReport based on Integer32"""
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
        *(("badArgument", 3),
          ("busy", 2),
          ("hostAlive", 6),
          ("hostNotResponding", 8),
          ("hostUnreachable", 7),
          ("idle", 1),
          ("nameLookupFailed", 5),
          ("noResource", 4))
    )


_A3ComPollReport_Type.__name__ = "Integer32"
_A3ComPollReport_Object = MibTableColumn
a3ComPollReport = _A3ComPollReport_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 17),
    _A3ComPollReport_Type()
)
a3ComPollReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollReport.setStatus("mandatory")


class _A3ComPollAction_Type(Integer32):
    """Custom type a3ComPollAction based on Integer32"""
    defaultValue = 1

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
        *(("activate", 2),
          ("deactivate", 3),
          ("destroy", 5),
          ("noop", 1),
          ("reset", 4))
    )


_A3ComPollAction_Type.__name__ = "Integer32"
_A3ComPollAction_Object = MibTableColumn
a3ComPollAction = _A3ComPollAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 1, 1, 18),
    _A3ComPollAction_Type()
)
a3ComPollAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollAction.setStatus("mandatory")
_A3ComPollNextFreeIndex_Type = Integer32
_A3ComPollNextFreeIndex_Object = MibScalar
a3ComPollNextFreeIndex = _A3ComPollNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 2),
    _A3ComPollNextFreeIndex_Type()
)
a3ComPollNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollNextFreeIndex.setStatus("mandatory")


class _A3ComPollTableInformation_Type(DisplayString):
    """Custom type a3ComPollTableInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_A3ComPollTableInformation_Type.__name__ = "DisplayString"
_A3ComPollTableInformation_Object = MibScalar
a3ComPollTableInformation = _A3ComPollTableInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 3),
    _A3ComPollTableInformation_Type()
)
a3ComPollTableInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPollTableInformation.setStatus("mandatory")


class _A3ComPollTableActionAll_Type(Integer32):
    """Custom type a3ComPollTableActionAll based on Integer32"""
    defaultValue = 1

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
        *(("activate", 2),
          ("deactivate", 3),
          ("destroy", 5),
          ("noop", 1),
          ("reset", 4))
    )


_A3ComPollTableActionAll_Type.__name__ = "Integer32"
_A3ComPollTableActionAll_Object = MibScalar
a3ComPollTableActionAll = _A3ComPollTableActionAll_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 22, 4),
    _A3ComPollTableActionAll_Type()
)
a3ComPollTableActionAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPollTableActionAll.setStatus("mandatory")

# Managed Objects groups


# Notification objects

a3ComPollResponseReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 61)
)
a3ComPollResponseReceived.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAddress"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAddressType"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAttempts"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollRate"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollFramesSent"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollFramesReceived"))
)
if mibBuilder.loadTexts:
    a3ComPollResponseReceived.setStatus(
        ""
    )

a3ComPollResponseNotReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 62)
)
a3ComPollResponseNotReceived.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAddress"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAddressType"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollAttempts"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollRate"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollFramesSent"),
        ("A3COM-SWITCHING-SYSTEMS-POLL-MIB", "a3ComPollFramesReceived"))
)
if mibBuilder.loadTexts:
    a3ComPollResponseNotReceived.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-POLL-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComPollResponseReceived": a3ComPollResponseReceived,
       "a3ComPollResponseNotReceived": a3ComPollResponseNotReceived,
       "a3ComPoll": a3ComPoll,
       "a3ComPollTable": a3ComPollTable,
       "a3ComPollEntry": a3ComPollEntry,
       "a3ComPollIndex": a3ComPollIndex,
       "a3ComPollAddress": a3ComPollAddress,
       "a3ComPollAddressType": a3ComPollAddressType,
       "a3ComPollCount": a3ComPollCount,
       "a3ComPollAttempts": a3ComPollAttempts,
       "a3ComPollRate": a3ComPollRate,
       "a3ComPollResponseTimeOut": a3ComPollResponseTimeOut,
       "a3ComPollPacketSize": a3ComPollPacketSize,
       "a3ComPollSourceAddress": a3ComPollSourceAddress,
       "a3ComPollMinRoundTripTime": a3ComPollMinRoundTripTime,
       "a3ComPollAvgRoundTripTime": a3ComPollAvgRoundTripTime,
       "a3ComPollMaxRoundTripTime": a3ComPollMaxRoundTripTime,
       "a3ComPollFramesSent": a3ComPollFramesSent,
       "a3ComPollFramesReceived": a3ComPollFramesReceived,
       "a3ComPollInformation": a3ComPollInformation,
       "a3ComPollOwner": a3ComPollOwner,
       "a3ComPollReport": a3ComPollReport,
       "a3ComPollAction": a3ComPollAction,
       "a3ComPollNextFreeIndex": a3ComPollNextFreeIndex,
       "a3ComPollTableInformation": a3ComPollTableInformation,
       "a3ComPollTableActionAll": a3ComPollTableActionAll}
)
