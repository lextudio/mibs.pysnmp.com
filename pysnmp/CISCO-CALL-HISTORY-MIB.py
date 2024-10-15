# SNMP MIB module (CISCO-CALL-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-HISTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:46 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoCallHistoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27)
)
ciscoCallHistoryMib.setRevisions(
        ("1995-08-15 00:00",
         "1995-07-20 00:00",
         "1995-08-15 00:00",
         "1996-11-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCallHistoryMibObjects_ObjectIdentity = ObjectIdentity
ciscoCallHistoryMibObjects = _CiscoCallHistoryMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1)
)
_CiscoCallHistory_ObjectIdentity = ObjectIdentity
ciscoCallHistory = _CiscoCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1)
)


class _CiscoCallHistoryTableMaxLength_Type(Integer32):
    """Custom type ciscoCallHistoryTableMaxLength based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CiscoCallHistoryTableMaxLength_Type.__name__ = "Integer32"
_CiscoCallHistoryTableMaxLength_Object = MibScalar
ciscoCallHistoryTableMaxLength = _CiscoCallHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 1),
    _CiscoCallHistoryTableMaxLength_Type()
)
ciscoCallHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCallHistoryTableMaxLength.setStatus("current")


class _CiscoCallHistoryRetainTimer_Type(Integer32):
    """Custom type ciscoCallHistoryRetainTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CiscoCallHistoryRetainTimer_Type.__name__ = "Integer32"
_CiscoCallHistoryRetainTimer_Object = MibScalar
ciscoCallHistoryRetainTimer = _CiscoCallHistoryRetainTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 2),
    _CiscoCallHistoryRetainTimer_Type()
)
ciscoCallHistoryRetainTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoCallHistoryRetainTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciscoCallHistoryRetainTimer.setUnits("minutes")
_CiscoCallHistoryTable_Object = MibTable
ciscoCallHistoryTable = _CiscoCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCallHistoryTable.setStatus("current")
_CiscoCallHistoryEntry_Object = MibTableRow
ciscoCallHistoryEntry = _CiscoCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1)
)
ciscoCallHistoryEntry.setIndexNames(
    (0, "CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryStartTime"),
    (0, "CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    ciscoCallHistoryEntry.setStatus("current")
_CiscoCallHistoryStartTime_Type = TimeStamp
_CiscoCallHistoryStartTime_Object = MibTableColumn
ciscoCallHistoryStartTime = _CiscoCallHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 1),
    _CiscoCallHistoryStartTime_Type()
)
ciscoCallHistoryStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoCallHistoryStartTime.setStatus("current")


class _CiscoCallHistoryIndex_Type(Integer32):
    """Custom type ciscoCallHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoCallHistoryIndex_Type.__name__ = "Integer32"
_CiscoCallHistoryIndex_Object = MibTableColumn
ciscoCallHistoryIndex = _CiscoCallHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 2),
    _CiscoCallHistoryIndex_Type()
)
ciscoCallHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoCallHistoryIndex.setStatus("current")


class _CiscoCallHistoryCallingNumber_Type(OctetString):
    """Custom type ciscoCallHistoryCallingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoCallHistoryCallingNumber_Type.__name__ = "OctetString"
_CiscoCallHistoryCallingNumber_Object = MibTableColumn
ciscoCallHistoryCallingNumber = _CiscoCallHistoryCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 3),
    _CiscoCallHistoryCallingNumber_Type()
)
ciscoCallHistoryCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCallingNumber.setStatus("current")


class _CiscoCallHistoryCalledNumber_Type(OctetString):
    """Custom type ciscoCallHistoryCalledNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoCallHistoryCalledNumber_Type.__name__ = "OctetString"
_CiscoCallHistoryCalledNumber_Object = MibTableColumn
ciscoCallHistoryCalledNumber = _CiscoCallHistoryCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 4),
    _CiscoCallHistoryCalledNumber_Type()
)
ciscoCallHistoryCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCalledNumber.setStatus("current")
_CiscoCallHistoryInterfaceNumber_Type = InterfaceIndex
_CiscoCallHistoryInterfaceNumber_Object = MibTableColumn
ciscoCallHistoryInterfaceNumber = _CiscoCallHistoryInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 5),
    _CiscoCallHistoryInterfaceNumber_Type()
)
ciscoCallHistoryInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryInterfaceNumber.setStatus("current")


class _CiscoCallHistoryDestinationAddress_Type(OctetString):
    """Custom type ciscoCallHistoryDestinationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )


_CiscoCallHistoryDestinationAddress_Type.__name__ = "OctetString"
_CiscoCallHistoryDestinationAddress_Object = MibTableColumn
ciscoCallHistoryDestinationAddress = _CiscoCallHistoryDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 6),
    _CiscoCallHistoryDestinationAddress_Type()
)
ciscoCallHistoryDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryDestinationAddress.setStatus("current")
_CiscoCallHistoryDestinationHostName_Type = DisplayString
_CiscoCallHistoryDestinationHostName_Object = MibTableColumn
ciscoCallHistoryDestinationHostName = _CiscoCallHistoryDestinationHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 7),
    _CiscoCallHistoryDestinationHostName_Type()
)
ciscoCallHistoryDestinationHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryDestinationHostName.setStatus("current")


class _CiscoCallHistoryCallDisconnectCause_Type(Integer32):
    """Custom type ciscoCallHistoryCallDisconnectCause based on Integer32"""
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
        *(("callRejected", 5),
          ("interworkingError", 8),
          ("networkOutOfOrder", 4),
          ("noCircuitChannelAvailable", 7),
          ("normalDisconnectReceived", 3),
          ("normalDisconnectSent", 2),
          ("other", 1),
          ("userBusy", 6))
    )


_CiscoCallHistoryCallDisconnectCause_Type.__name__ = "Integer32"
_CiscoCallHistoryCallDisconnectCause_Object = MibTableColumn
ciscoCallHistoryCallDisconnectCause = _CiscoCallHistoryCallDisconnectCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 8),
    _CiscoCallHistoryCallDisconnectCause_Type()
)
ciscoCallHistoryCallDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCallDisconnectCause.setStatus("current")
_CiscoCallHistoryCallConnectionTime_Type = TimeStamp
_CiscoCallHistoryCallConnectionTime_Object = MibTableColumn
ciscoCallHistoryCallConnectionTime = _CiscoCallHistoryCallConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 9),
    _CiscoCallHistoryCallConnectionTime_Type()
)
ciscoCallHistoryCallConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCallConnectionTime.setStatus("current")
_CiscoCallHistoryCallDisconnectTime_Type = TimeStamp
_CiscoCallHistoryCallDisconnectTime_Object = MibTableColumn
ciscoCallHistoryCallDisconnectTime = _CiscoCallHistoryCallDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 10),
    _CiscoCallHistoryCallDisconnectTime_Type()
)
ciscoCallHistoryCallDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCallDisconnectTime.setStatus("current")
_CiscoCallHistoryDialReason_Type = DisplayString
_CiscoCallHistoryDialReason_Object = MibTableColumn
ciscoCallHistoryDialReason = _CiscoCallHistoryDialReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 11),
    _CiscoCallHistoryDialReason_Type()
)
ciscoCallHistoryDialReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryDialReason.setStatus("current")
_CiscoCallHistoryConnectTimeOfDay_Type = DisplayString
_CiscoCallHistoryConnectTimeOfDay_Object = MibTableColumn
ciscoCallHistoryConnectTimeOfDay = _CiscoCallHistoryConnectTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 12),
    _CiscoCallHistoryConnectTimeOfDay_Type()
)
ciscoCallHistoryConnectTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryConnectTimeOfDay.setStatus("current")
_CiscoCallHistoryDisconnectTimeOfDay_Type = DisplayString
_CiscoCallHistoryDisconnectTimeOfDay_Object = MibTableColumn
ciscoCallHistoryDisconnectTimeOfDay = _CiscoCallHistoryDisconnectTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 13),
    _CiscoCallHistoryDisconnectTimeOfDay_Type()
)
ciscoCallHistoryDisconnectTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryDisconnectTimeOfDay.setStatus("current")
_CiscoCallHistoryTransmitPackets_Type = Integer32
_CiscoCallHistoryTransmitPackets_Object = MibTableColumn
ciscoCallHistoryTransmitPackets = _CiscoCallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 14),
    _CiscoCallHistoryTransmitPackets_Type()
)
ciscoCallHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryTransmitPackets.setStatus("current")
_CiscoCallHistoryTransmitBytes_Type = Integer32
_CiscoCallHistoryTransmitBytes_Object = MibTableColumn
ciscoCallHistoryTransmitBytes = _CiscoCallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 15),
    _CiscoCallHistoryTransmitBytes_Type()
)
ciscoCallHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryTransmitBytes.setStatus("current")
_CiscoCallHistoryReceivePackets_Type = Integer32
_CiscoCallHistoryReceivePackets_Object = MibTableColumn
ciscoCallHistoryReceivePackets = _CiscoCallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 16),
    _CiscoCallHistoryReceivePackets_Type()
)
ciscoCallHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryReceivePackets.setStatus("current")
_CiscoCallHistoryReceiveBytes_Type = Integer32
_CiscoCallHistoryReceiveBytes_Object = MibTableColumn
ciscoCallHistoryReceiveBytes = _CiscoCallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 17),
    _CiscoCallHistoryReceiveBytes_Type()
)
ciscoCallHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryReceiveBytes.setStatus("current")


class _CiscoCallHistoryRecordedUnits_Type(Integer32):
    """Custom type ciscoCallHistoryRecordedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CiscoCallHistoryRecordedUnits_Type.__name__ = "Integer32"
_CiscoCallHistoryRecordedUnits_Object = MibTableColumn
ciscoCallHistoryRecordedUnits = _CiscoCallHistoryRecordedUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 18),
    _CiscoCallHistoryRecordedUnits_Type()
)
ciscoCallHistoryRecordedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryRecordedUnits.setStatus("current")
_CiscoCallHistoryCurrency_Type = DisplayString
_CiscoCallHistoryCurrency_Object = MibTableColumn
ciscoCallHistoryCurrency = _CiscoCallHistoryCurrency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 19),
    _CiscoCallHistoryCurrency_Type()
)
ciscoCallHistoryCurrency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCurrency.setStatus("current")


class _CiscoCallHistoryCurrencyAmount_Type(Integer32):
    """Custom type ciscoCallHistoryCurrencyAmount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CiscoCallHistoryCurrencyAmount_Type.__name__ = "Integer32"
_CiscoCallHistoryCurrencyAmount_Object = MibTableColumn
ciscoCallHistoryCurrencyAmount = _CiscoCallHistoryCurrencyAmount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 20),
    _CiscoCallHistoryCurrencyAmount_Type()
)
ciscoCallHistoryCurrencyAmount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryCurrencyAmount.setStatus("current")


class _CiscoCallHistoryMultiplier_Type(Integer32):
    """Custom type ciscoCallHistoryMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hundred", 5),
          ("one", 3),
          ("oneHundreth", 1),
          ("oneTenth", 2),
          ("oneThousandth", 0),
          ("ten", 4),
          ("thousand", 6))
    )


_CiscoCallHistoryMultiplier_Type.__name__ = "Integer32"
_CiscoCallHistoryMultiplier_Object = MibTableColumn
ciscoCallHistoryMultiplier = _CiscoCallHistoryMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 1, 1, 3, 1, 21),
    _CiscoCallHistoryMultiplier_Type()
)
ciscoCallHistoryMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoCallHistoryMultiplier.setStatus("current")
_CiscoCallHistoryMibConformance_ObjectIdentity = ObjectIdentity
ciscoCallHistoryMibConformance = _CiscoCallHistoryMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2)
)
_CiscoCallHistoryMibCompliances_ObjectIdentity = ObjectIdentity
ciscoCallHistoryMibCompliances = _CiscoCallHistoryMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 1)
)
_CiscoCallHistoryMibGroups_ObjectIdentity = ObjectIdentity
ciscoCallHistoryMibGroups = _CiscoCallHistoryMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 2)
)

# Managed Objects groups

ciscoCallHistoryMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 2, 1)
)
ciscoCallHistoryMibGroup.setObjects(
      *(("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallingNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCalledNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryInterfaceNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationAddress"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationHostName"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectCause"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallConnectionTime"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectTime"))
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibGroup.setStatus("obsolete")

ciscoCallHistoryMibGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 2, 2)
)
ciscoCallHistoryMibGroupRev1.setObjects(
      *(("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallingNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCalledNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryInterfaceNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationAddress"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationHostName"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectCause"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallConnectionTime"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectTime"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDialReason"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryConnectTimeOfDay"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDisconnectTimeOfDay"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryTransmitPackets"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryTransmitBytes"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryReceivePackets"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryReceiveBytes"))
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibGroupRev1.setStatus("obsolete")

ciscoCallHistoryMibGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 2, 3)
)
ciscoCallHistoryMibGroupRev2.setObjects(
      *(("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallingNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCalledNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryInterfaceNumber"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationAddress"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDestinationHostName"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectCause"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallConnectionTime"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCallDisconnectTime"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDialReason"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryConnectTimeOfDay"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryDisconnectTimeOfDay"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryTransmitPackets"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryTransmitBytes"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryReceivePackets"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryReceiveBytes"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryRecordedUnits"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCurrency"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryCurrencyAmount"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryMultiplier"))
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibGroupRev2.setStatus("current")

ciscoCallHistoryMibGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 2, 4)
)
ciscoCallHistoryMibGlobalsGroup.setObjects(
      *(("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryTableMaxLength"),
        ("CISCO-CALL-HISTORY-MIB", "ciscoCallHistoryRetainTimer"))
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibGlobalsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCallHistoryMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibCompliance.setStatus(
        "obsolete"
    )

ciscoCallHistoryMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibComplianceRev1.setStatus(
        "obsolete"
    )

ciscoCallHistoryMibComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibComplianceV11R01.setStatus(
        "obsolete"
    )

ciscoCallHistoryMibComplianceV11R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 27, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCallHistoryMibComplianceV11R02.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-HISTORY-MIB",
    **{"ciscoCallHistoryMib": ciscoCallHistoryMib,
       "ciscoCallHistoryMibObjects": ciscoCallHistoryMibObjects,
       "ciscoCallHistory": ciscoCallHistory,
       "ciscoCallHistoryTableMaxLength": ciscoCallHistoryTableMaxLength,
       "ciscoCallHistoryRetainTimer": ciscoCallHistoryRetainTimer,
       "ciscoCallHistoryTable": ciscoCallHistoryTable,
       "ciscoCallHistoryEntry": ciscoCallHistoryEntry,
       "ciscoCallHistoryStartTime": ciscoCallHistoryStartTime,
       "ciscoCallHistoryIndex": ciscoCallHistoryIndex,
       "ciscoCallHistoryCallingNumber": ciscoCallHistoryCallingNumber,
       "ciscoCallHistoryCalledNumber": ciscoCallHistoryCalledNumber,
       "ciscoCallHistoryInterfaceNumber": ciscoCallHistoryInterfaceNumber,
       "ciscoCallHistoryDestinationAddress": ciscoCallHistoryDestinationAddress,
       "ciscoCallHistoryDestinationHostName": ciscoCallHistoryDestinationHostName,
       "ciscoCallHistoryCallDisconnectCause": ciscoCallHistoryCallDisconnectCause,
       "ciscoCallHistoryCallConnectionTime": ciscoCallHistoryCallConnectionTime,
       "ciscoCallHistoryCallDisconnectTime": ciscoCallHistoryCallDisconnectTime,
       "ciscoCallHistoryDialReason": ciscoCallHistoryDialReason,
       "ciscoCallHistoryConnectTimeOfDay": ciscoCallHistoryConnectTimeOfDay,
       "ciscoCallHistoryDisconnectTimeOfDay": ciscoCallHistoryDisconnectTimeOfDay,
       "ciscoCallHistoryTransmitPackets": ciscoCallHistoryTransmitPackets,
       "ciscoCallHistoryTransmitBytes": ciscoCallHistoryTransmitBytes,
       "ciscoCallHistoryReceivePackets": ciscoCallHistoryReceivePackets,
       "ciscoCallHistoryReceiveBytes": ciscoCallHistoryReceiveBytes,
       "ciscoCallHistoryRecordedUnits": ciscoCallHistoryRecordedUnits,
       "ciscoCallHistoryCurrency": ciscoCallHistoryCurrency,
       "ciscoCallHistoryCurrencyAmount": ciscoCallHistoryCurrencyAmount,
       "ciscoCallHistoryMultiplier": ciscoCallHistoryMultiplier,
       "ciscoCallHistoryMibConformance": ciscoCallHistoryMibConformance,
       "ciscoCallHistoryMibCompliances": ciscoCallHistoryMibCompliances,
       "ciscoCallHistoryMibCompliance": ciscoCallHistoryMibCompliance,
       "ciscoCallHistoryMibComplianceRev1": ciscoCallHistoryMibComplianceRev1,
       "ciscoCallHistoryMibComplianceV11R01": ciscoCallHistoryMibComplianceV11R01,
       "ciscoCallHistoryMibComplianceV11R02": ciscoCallHistoryMibComplianceV11R02,
       "ciscoCallHistoryMibGroups": ciscoCallHistoryMibGroups,
       "ciscoCallHistoryMibGroup": ciscoCallHistoryMibGroup,
       "ciscoCallHistoryMibGroupRev1": ciscoCallHistoryMibGroupRev1,
       "ciscoCallHistoryMibGroupRev2": ciscoCallHistoryMibGroupRev2,
       "ciscoCallHistoryMibGlobalsGroup": ciscoCallHistoryMibGlobalsGroup}
)
