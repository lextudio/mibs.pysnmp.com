# SNMP MIB module (CISCO-CONFIG-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONFIG-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:41 2024
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

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoConfigManMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43)
)
ciscoConfigManMIB.setRevisions(
        ("2007-04-27 00:00",
         "2006-08-17 00:00",
         "2004-06-18 00:00",
         "2002-06-07 00:00",
         "2002-03-12 00:00",
         "1995-11-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HistoryEventMedium(Integer32, TextualConvention):
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("commandSource", 2),
          ("erase", 1),
          ("local", 5),
          ("networkFtp", 8),
          ("networkRcp", 7),
          ("networkScp", 9),
          ("networkTftp", 6),
          ("running", 3),
          ("startup", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoConfigManMIBObjects_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBObjects = _CiscoConfigManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1)
)
_CcmHistory_ObjectIdentity = ObjectIdentity
ccmHistory = _CcmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1)
)
_CcmHistoryRunningLastChanged_Type = TimeTicks
_CcmHistoryRunningLastChanged_Object = MibScalar
ccmHistoryRunningLastChanged = _CcmHistoryRunningLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 1),
    _CcmHistoryRunningLastChanged_Type()
)
ccmHistoryRunningLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryRunningLastChanged.setStatus("current")
_CcmHistoryRunningLastSaved_Type = TimeTicks
_CcmHistoryRunningLastSaved_Object = MibScalar
ccmHistoryRunningLastSaved = _CcmHistoryRunningLastSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 2),
    _CcmHistoryRunningLastSaved_Type()
)
ccmHistoryRunningLastSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryRunningLastSaved.setStatus("current")
_CcmHistoryStartupLastChanged_Type = TimeTicks
_CcmHistoryStartupLastChanged_Object = MibScalar
ccmHistoryStartupLastChanged = _CcmHistoryStartupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 3),
    _CcmHistoryStartupLastChanged_Type()
)
ccmHistoryStartupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryStartupLastChanged.setStatus("current")


class _CcmHistoryMaxEventEntries_Type(Integer32):
    """Custom type ccmHistoryMaxEventEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CcmHistoryMaxEventEntries_Type.__name__ = "Integer32"
_CcmHistoryMaxEventEntries_Object = MibScalar
ccmHistoryMaxEventEntries = _CcmHistoryMaxEventEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 4),
    _CcmHistoryMaxEventEntries_Type()
)
ccmHistoryMaxEventEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryMaxEventEntries.setStatus("current")
_CcmHistoryEventEntriesBumped_Type = Counter32
_CcmHistoryEventEntriesBumped_Object = MibScalar
ccmHistoryEventEntriesBumped = _CcmHistoryEventEntriesBumped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 5),
    _CcmHistoryEventEntriesBumped_Type()
)
ccmHistoryEventEntriesBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventEntriesBumped.setStatus("current")
_CcmHistoryEventTable_Object = MibTable
ccmHistoryEventTable = _CcmHistoryEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ccmHistoryEventTable.setStatus("current")
_CcmHistoryEventEntry_Object = MibTableRow
ccmHistoryEventEntry = _CcmHistoryEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1)
)
ccmHistoryEventEntry.setIndexNames(
    (0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"),
)
if mibBuilder.loadTexts:
    ccmHistoryEventEntry.setStatus("current")


class _CcmHistoryEventIndex_Type(Integer32):
    """Custom type ccmHistoryEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcmHistoryEventIndex_Type.__name__ = "Integer32"
_CcmHistoryEventIndex_Object = MibTableColumn
ccmHistoryEventIndex = _CcmHistoryEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 1),
    _CcmHistoryEventIndex_Type()
)
ccmHistoryEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmHistoryEventIndex.setStatus("current")
_CcmHistoryEventTime_Type = TimeTicks
_CcmHistoryEventTime_Object = MibTableColumn
ccmHistoryEventTime = _CcmHistoryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 2),
    _CcmHistoryEventTime_Type()
)
ccmHistoryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventTime.setStatus("current")


class _CcmHistoryEventCommandSource_Type(Integer32):
    """Custom type ccmHistoryEventCommandSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commandLine", 1),
          ("snmp", 2))
    )


_CcmHistoryEventCommandSource_Type.__name__ = "Integer32"
_CcmHistoryEventCommandSource_Object = MibTableColumn
ccmHistoryEventCommandSource = _CcmHistoryEventCommandSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 3),
    _CcmHistoryEventCommandSource_Type()
)
ccmHistoryEventCommandSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventCommandSource.setStatus("current")
_CcmHistoryEventConfigSource_Type = HistoryEventMedium
_CcmHistoryEventConfigSource_Object = MibTableColumn
ccmHistoryEventConfigSource = _CcmHistoryEventConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 4),
    _CcmHistoryEventConfigSource_Type()
)
ccmHistoryEventConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventConfigSource.setStatus("current")
_CcmHistoryEventConfigDestination_Type = HistoryEventMedium
_CcmHistoryEventConfigDestination_Object = MibTableColumn
ccmHistoryEventConfigDestination = _CcmHistoryEventConfigDestination_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 5),
    _CcmHistoryEventConfigDestination_Type()
)
ccmHistoryEventConfigDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventConfigDestination.setStatus("current")


class _CcmHistoryEventTerminalType_Type(Integer32):
    """Custom type ccmHistoryEventTerminalType based on Integer32"""
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
        *(("auxiliary", 6),
          ("console", 3),
          ("notApplicable", 1),
          ("terminal", 4),
          ("unknown", 2),
          ("virtual", 5))
    )


_CcmHistoryEventTerminalType_Type.__name__ = "Integer32"
_CcmHistoryEventTerminalType_Object = MibTableColumn
ccmHistoryEventTerminalType = _CcmHistoryEventTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 6),
    _CcmHistoryEventTerminalType_Type()
)
ccmHistoryEventTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventTerminalType.setStatus("current")


class _CcmHistoryEventTerminalNumber_Type(Integer32):
    """Custom type ccmHistoryEventTerminalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CcmHistoryEventTerminalNumber_Type.__name__ = "Integer32"
_CcmHistoryEventTerminalNumber_Object = MibTableColumn
ccmHistoryEventTerminalNumber = _CcmHistoryEventTerminalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 7),
    _CcmHistoryEventTerminalNumber_Type()
)
ccmHistoryEventTerminalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventTerminalNumber.setStatus("current")


class _CcmHistoryEventTerminalUser_Type(DisplayString):
    """Custom type ccmHistoryEventTerminalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmHistoryEventTerminalUser_Type.__name__ = "DisplayString"
_CcmHistoryEventTerminalUser_Object = MibTableColumn
ccmHistoryEventTerminalUser = _CcmHistoryEventTerminalUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 8),
    _CcmHistoryEventTerminalUser_Type()
)
ccmHistoryEventTerminalUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventTerminalUser.setStatus("current")


class _CcmHistoryEventTerminalLocation_Type(DisplayString):
    """Custom type ccmHistoryEventTerminalLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmHistoryEventTerminalLocation_Type.__name__ = "DisplayString"
_CcmHistoryEventTerminalLocation_Object = MibTableColumn
ccmHistoryEventTerminalLocation = _CcmHistoryEventTerminalLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 9),
    _CcmHistoryEventTerminalLocation_Type()
)
ccmHistoryEventTerminalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventTerminalLocation.setStatus("current")
_CcmHistoryEventCommandSourceAddress_Type = IpAddress
_CcmHistoryEventCommandSourceAddress_Object = MibTableColumn
ccmHistoryEventCommandSourceAddress = _CcmHistoryEventCommandSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 10),
    _CcmHistoryEventCommandSourceAddress_Type()
)
ccmHistoryEventCommandSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventCommandSourceAddress.setStatus("deprecated")


class _CcmHistoryEventVirtualHostName_Type(DisplayString):
    """Custom type ccmHistoryEventVirtualHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmHistoryEventVirtualHostName_Type.__name__ = "DisplayString"
_CcmHistoryEventVirtualHostName_Object = MibTableColumn
ccmHistoryEventVirtualHostName = _CcmHistoryEventVirtualHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 11),
    _CcmHistoryEventVirtualHostName_Type()
)
ccmHistoryEventVirtualHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventVirtualHostName.setStatus("current")
_CcmHistoryEventServerAddress_Type = IpAddress
_CcmHistoryEventServerAddress_Object = MibTableColumn
ccmHistoryEventServerAddress = _CcmHistoryEventServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 12),
    _CcmHistoryEventServerAddress_Type()
)
ccmHistoryEventServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventServerAddress.setStatus("deprecated")


class _CcmHistoryEventFile_Type(DisplayString):
    """Custom type ccmHistoryEventFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmHistoryEventFile_Type.__name__ = "DisplayString"
_CcmHistoryEventFile_Object = MibTableColumn
ccmHistoryEventFile = _CcmHistoryEventFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 13),
    _CcmHistoryEventFile_Type()
)
ccmHistoryEventFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventFile.setStatus("current")


class _CcmHistoryEventRcpUser_Type(DisplayString):
    """Custom type ccmHistoryEventRcpUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CcmHistoryEventRcpUser_Type.__name__ = "DisplayString"
_CcmHistoryEventRcpUser_Object = MibTableColumn
ccmHistoryEventRcpUser = _CcmHistoryEventRcpUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 14),
    _CcmHistoryEventRcpUser_Type()
)
ccmHistoryEventRcpUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventRcpUser.setStatus("current")
_CcmHistoryCLICmdEntriesBumped_Type = Counter32
_CcmHistoryCLICmdEntriesBumped_Object = MibTableColumn
ccmHistoryCLICmdEntriesBumped = _CcmHistoryCLICmdEntriesBumped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 15),
    _CcmHistoryCLICmdEntriesBumped_Type()
)
ccmHistoryCLICmdEntriesBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryCLICmdEntriesBumped.setStatus("current")
_CcmHistoryEventCommandSourceAddrType_Type = InetAddressType
_CcmHistoryEventCommandSourceAddrType_Object = MibTableColumn
ccmHistoryEventCommandSourceAddrType = _CcmHistoryEventCommandSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 16),
    _CcmHistoryEventCommandSourceAddrType_Type()
)
ccmHistoryEventCommandSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventCommandSourceAddrType.setStatus("current")
_CcmHistoryEventCommandSourceAddrRev1_Type = InetAddress
_CcmHistoryEventCommandSourceAddrRev1_Object = MibTableColumn
ccmHistoryEventCommandSourceAddrRev1 = _CcmHistoryEventCommandSourceAddrRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 17),
    _CcmHistoryEventCommandSourceAddrRev1_Type()
)
ccmHistoryEventCommandSourceAddrRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventCommandSourceAddrRev1.setStatus("current")
_CcmHistoryEventServerAddrType_Type = InetAddressType
_CcmHistoryEventServerAddrType_Object = MibTableColumn
ccmHistoryEventServerAddrType = _CcmHistoryEventServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 18),
    _CcmHistoryEventServerAddrType_Type()
)
ccmHistoryEventServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventServerAddrType.setStatus("current")
_CcmHistoryEventServerAddrRev1_Type = InetAddress
_CcmHistoryEventServerAddrRev1_Object = MibTableColumn
ccmHistoryEventServerAddrRev1 = _CcmHistoryEventServerAddrRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 1, 6, 1, 19),
    _CcmHistoryEventServerAddrRev1_Type()
)
ccmHistoryEventServerAddrRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmHistoryEventServerAddrRev1.setStatus("current")
_CcmCLIHistory_ObjectIdentity = ObjectIdentity
ccmCLIHistory = _CcmCLIHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2)
)


class _CcmCLIHistoryMaxCmdEntries_Type(Unsigned32):
    """Custom type ccmCLIHistoryMaxCmdEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CcmCLIHistoryMaxCmdEntries_Type.__name__ = "Unsigned32"
_CcmCLIHistoryMaxCmdEntries_Object = MibScalar
ccmCLIHistoryMaxCmdEntries = _CcmCLIHistoryMaxCmdEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 1),
    _CcmCLIHistoryMaxCmdEntries_Type()
)
ccmCLIHistoryMaxCmdEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCLIHistoryMaxCmdEntries.setStatus("current")
_CcmCLIHistoryCmdEntries_Type = Gauge32
_CcmCLIHistoryCmdEntries_Object = MibScalar
ccmCLIHistoryCmdEntries = _CcmCLIHistoryCmdEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 2),
    _CcmCLIHistoryCmdEntries_Type()
)
ccmCLIHistoryCmdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCLIHistoryCmdEntries.setStatus("current")
_CcmCLIHistoryCmdEntriesAllowed_Type = Unsigned32
_CcmCLIHistoryCmdEntriesAllowed_Object = MibScalar
ccmCLIHistoryCmdEntriesAllowed = _CcmCLIHistoryCmdEntriesAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 3),
    _CcmCLIHistoryCmdEntriesAllowed_Type()
)
ccmCLIHistoryCmdEntriesAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCLIHistoryCmdEntriesAllowed.setStatus("current")
_CcmCLIHistoryCommandTable_Object = MibTable
ccmCLIHistoryCommandTable = _CcmCLIHistoryCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ccmCLIHistoryCommandTable.setStatus("current")
_CcmCLIHistoryCommandEntry_Object = MibTableRow
ccmCLIHistoryCommandEntry = _CcmCLIHistoryCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1)
)
ccmCLIHistoryCommandEntry.setIndexNames(
    (0, "CISCO-CONFIG-MAN-MIB", "ccmHistoryEventIndex"),
    (0, "CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommandIndex"),
)
if mibBuilder.loadTexts:
    ccmCLIHistoryCommandEntry.setStatus("current")


class _CcmCLIHistoryCommandIndex_Type(Unsigned32):
    """Custom type ccmCLIHistoryCommandIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcmCLIHistoryCommandIndex_Type.__name__ = "Unsigned32"
_CcmCLIHistoryCommandIndex_Object = MibTableColumn
ccmCLIHistoryCommandIndex = _CcmCLIHistoryCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 1),
    _CcmCLIHistoryCommandIndex_Type()
)
ccmCLIHistoryCommandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCLIHistoryCommandIndex.setStatus("current")
_CcmCLIHistoryCommand_Type = DisplayString
_CcmCLIHistoryCommand_Object = MibTableColumn
ccmCLIHistoryCommand = _CcmCLIHistoryCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 2, 4, 1, 2),
    _CcmCLIHistoryCommand_Type()
)
ccmCLIHistoryCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCLIHistoryCommand.setStatus("current")
_CcmCLICfg_ObjectIdentity = ObjectIdentity
ccmCLICfg = _CcmCLICfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3)
)


class _CcmCLICfgRunConfNotifEnable_Type(TruthValue):
    """Custom type ccmCLICfgRunConfNotifEnable based on TruthValue"""


_CcmCLICfgRunConfNotifEnable_Object = MibScalar
ccmCLICfgRunConfNotifEnable = _CcmCLICfgRunConfNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 3, 1),
    _CcmCLICfgRunConfNotifEnable_Type()
)
ccmCLICfgRunConfNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCLICfgRunConfNotifEnable.setStatus("current")
_CcmCTIDObjects_ObjectIdentity = ObjectIdentity
ccmCTIDObjects = _CcmCTIDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4)
)
_CcmCTID_Type = Unsigned64
_CcmCTID_Object = MibScalar
ccmCTID = _CcmCTID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 1),
    _CcmCTID_Type()
)
ccmCTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTID.setStatus("current")
_CcmCTIDLastChangeTime_Type = DateAndTime
_CcmCTIDLastChangeTime_Object = MibScalar
ccmCTIDLastChangeTime = _CcmCTIDLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 2),
    _CcmCTIDLastChangeTime_Type()
)
ccmCTIDLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDLastChangeTime.setStatus("current")
_CcmCTIDWhoChanged_Type = SnmpAdminString
_CcmCTIDWhoChanged_Object = MibScalar
ccmCTIDWhoChanged = _CcmCTIDWhoChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 3),
    _CcmCTIDWhoChanged_Type()
)
ccmCTIDWhoChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCTIDWhoChanged.setStatus("current")


class _CcmCTIDRolledOverNotifEnable_Type(TruthValue):
    """Custom type ccmCTIDRolledOverNotifEnable based on TruthValue"""


_CcmCTIDRolledOverNotifEnable_Object = MibScalar
ccmCTIDRolledOverNotifEnable = _CcmCTIDRolledOverNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 1, 4, 4),
    _CcmCTIDRolledOverNotifEnable_Type()
)
ccmCTIDRolledOverNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCTIDRolledOverNotifEnable.setStatus("current")
_CiscoConfigManMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBNotificationPrefix = _CiscoConfigManMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 2)
)
_CiscoConfigManMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBNotifications = _CiscoConfigManMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0)
)
_CiscoConfigManMIBConformance_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBConformance = _CiscoConfigManMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3)
)
_CiscoConfigManMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBCompliances = _CiscoConfigManMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1)
)
_CiscoConfigManMIBGroups_ObjectIdentity = ObjectIdentity
ciscoConfigManMIBGroups = _CiscoConfigManMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2)
)

# Managed Objects groups

ciscoConfigManHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 1)
)
ciscoConfigManHistoryGroup.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"))
)
if mibBuilder.loadTexts:
    ciscoConfigManHistoryGroup.setStatus("deprecated")

ciscoConfigManHistoryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 2)
)
ciscoConfigManHistoryGroupRev1.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddress"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddress"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"))
)
if mibBuilder.loadTexts:
    ciscoConfigManHistoryGroupRev1.setStatus("deprecated")

ciscoConfigManCLIHistCmdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 4)
)
ciscoConfigManCLIHistCmdGroup.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryMaxCmdEntries"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntries"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCmdEntriesAllowed"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCLIHistoryCommand"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCLICfgRunConfNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoConfigManCLIHistCmdGroup.setStatus("current")

ciscoConfigManHistoryGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 5)
)
ciscoConfigManHistoryGroupRev2.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastSaved"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryStartupLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryMaxEventEntries"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventEntriesBumped"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTime"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalNumber"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalUser"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalLocation"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventVirtualHostName"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventFile"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventRcpUser"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryCLICmdEntriesBumped"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrType"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSourceAddrRev1"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrType"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventServerAddrRev1"))
)
if mibBuilder.loadTexts:
    ciscoConfigManHistoryGroupRev2.setStatus("current")

ciscoConfigManCTIDObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 7)
)
ciscoConfigManCTIDObjectGroup.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmCTID"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCTIDLastChangeTime"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCTIDWhoChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOverNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoConfigManCTIDObjectGroup.setStatus("current")


# Notification objects

ciscoConfigManEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 1)
)
ciscoConfigManEvent.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventCommandSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigSource"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventConfigDestination"))
)
if mibBuilder.loadTexts:
    ciscoConfigManEvent.setStatus(
        "current"
    )

ccmCLIRunningConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 2)
)
ccmCLIRunningConfigChanged.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ccmHistoryRunningLastChanged"),
        ("CISCO-CONFIG-MAN-MIB", "ccmHistoryEventTerminalType"))
)
if mibBuilder.loadTexts:
    ccmCLIRunningConfigChanged.setStatus(
        "current"
    )

ccmCTIDRolledOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 2, 0, 3)
)
if mibBuilder.loadTexts:
    ccmCTIDRolledOver.setStatus(
        "current"
    )


# Notifications groups

ciscoConfigManHistNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 3)
)
ciscoConfigManHistNotifyGroup.setObjects(
      *(("CISCO-CONFIG-MAN-MIB", "ciscoConfigManEvent"),
        ("CISCO-CONFIG-MAN-MIB", "ccmCLIRunningConfigChanged"))
)
if mibBuilder.loadTexts:
    ciscoConfigManHistNotifyGroup.setStatus(
        "current"
    )

ciscoConfigManCTIDNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 2, 6)
)
ciscoConfigManCTIDNotifyGroup.setObjects(
    ("CISCO-CONFIG-MAN-MIB", "ccmCTIDRolledOver")
)
if mibBuilder.loadTexts:
    ciscoConfigManCTIDNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoConfigManMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoConfigManMIBCompliance.setStatus(
        "deprecated"
    )

ciscoConfigManMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoConfigManMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoConfigManMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoConfigManMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoConfigManMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 43, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoConfigManMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONFIG-MAN-MIB",
    **{"HistoryEventMedium": HistoryEventMedium,
       "ciscoConfigManMIB": ciscoConfigManMIB,
       "ciscoConfigManMIBObjects": ciscoConfigManMIBObjects,
       "ccmHistory": ccmHistory,
       "ccmHistoryRunningLastChanged": ccmHistoryRunningLastChanged,
       "ccmHistoryRunningLastSaved": ccmHistoryRunningLastSaved,
       "ccmHistoryStartupLastChanged": ccmHistoryStartupLastChanged,
       "ccmHistoryMaxEventEntries": ccmHistoryMaxEventEntries,
       "ccmHistoryEventEntriesBumped": ccmHistoryEventEntriesBumped,
       "ccmHistoryEventTable": ccmHistoryEventTable,
       "ccmHistoryEventEntry": ccmHistoryEventEntry,
       "ccmHistoryEventIndex": ccmHistoryEventIndex,
       "ccmHistoryEventTime": ccmHistoryEventTime,
       "ccmHistoryEventCommandSource": ccmHistoryEventCommandSource,
       "ccmHistoryEventConfigSource": ccmHistoryEventConfigSource,
       "ccmHistoryEventConfigDestination": ccmHistoryEventConfigDestination,
       "ccmHistoryEventTerminalType": ccmHistoryEventTerminalType,
       "ccmHistoryEventTerminalNumber": ccmHistoryEventTerminalNumber,
       "ccmHistoryEventTerminalUser": ccmHistoryEventTerminalUser,
       "ccmHistoryEventTerminalLocation": ccmHistoryEventTerminalLocation,
       "ccmHistoryEventCommandSourceAddress": ccmHistoryEventCommandSourceAddress,
       "ccmHistoryEventVirtualHostName": ccmHistoryEventVirtualHostName,
       "ccmHistoryEventServerAddress": ccmHistoryEventServerAddress,
       "ccmHistoryEventFile": ccmHistoryEventFile,
       "ccmHistoryEventRcpUser": ccmHistoryEventRcpUser,
       "ccmHistoryCLICmdEntriesBumped": ccmHistoryCLICmdEntriesBumped,
       "ccmHistoryEventCommandSourceAddrType": ccmHistoryEventCommandSourceAddrType,
       "ccmHistoryEventCommandSourceAddrRev1": ccmHistoryEventCommandSourceAddrRev1,
       "ccmHistoryEventServerAddrType": ccmHistoryEventServerAddrType,
       "ccmHistoryEventServerAddrRev1": ccmHistoryEventServerAddrRev1,
       "ccmCLIHistory": ccmCLIHistory,
       "ccmCLIHistoryMaxCmdEntries": ccmCLIHistoryMaxCmdEntries,
       "ccmCLIHistoryCmdEntries": ccmCLIHistoryCmdEntries,
       "ccmCLIHistoryCmdEntriesAllowed": ccmCLIHistoryCmdEntriesAllowed,
       "ccmCLIHistoryCommandTable": ccmCLIHistoryCommandTable,
       "ccmCLIHistoryCommandEntry": ccmCLIHistoryCommandEntry,
       "ccmCLIHistoryCommandIndex": ccmCLIHistoryCommandIndex,
       "ccmCLIHistoryCommand": ccmCLIHistoryCommand,
       "ccmCLICfg": ccmCLICfg,
       "ccmCLICfgRunConfNotifEnable": ccmCLICfgRunConfNotifEnable,
       "ccmCTIDObjects": ccmCTIDObjects,
       "ccmCTID": ccmCTID,
       "ccmCTIDLastChangeTime": ccmCTIDLastChangeTime,
       "ccmCTIDWhoChanged": ccmCTIDWhoChanged,
       "ccmCTIDRolledOverNotifEnable": ccmCTIDRolledOverNotifEnable,
       "ciscoConfigManMIBNotificationPrefix": ciscoConfigManMIBNotificationPrefix,
       "ciscoConfigManMIBNotifications": ciscoConfigManMIBNotifications,
       "ciscoConfigManEvent": ciscoConfigManEvent,
       "ccmCLIRunningConfigChanged": ccmCLIRunningConfigChanged,
       "ccmCTIDRolledOver": ccmCTIDRolledOver,
       "ciscoConfigManMIBConformance": ciscoConfigManMIBConformance,
       "ciscoConfigManMIBCompliances": ciscoConfigManMIBCompliances,
       "ciscoConfigManMIBCompliance": ciscoConfigManMIBCompliance,
       "ciscoConfigManMIBComplianceRev2": ciscoConfigManMIBComplianceRev2,
       "ciscoConfigManMIBComplianceRev3": ciscoConfigManMIBComplianceRev3,
       "ciscoConfigManMIBComplianceRev4": ciscoConfigManMIBComplianceRev4,
       "ciscoConfigManMIBGroups": ciscoConfigManMIBGroups,
       "ciscoConfigManHistoryGroup": ciscoConfigManHistoryGroup,
       "ciscoConfigManHistoryGroupRev1": ciscoConfigManHistoryGroupRev1,
       "ciscoConfigManHistNotifyGroup": ciscoConfigManHistNotifyGroup,
       "ciscoConfigManCLIHistCmdGroup": ciscoConfigManCLIHistCmdGroup,
       "ciscoConfigManHistoryGroupRev2": ciscoConfigManHistoryGroupRev2,
       "ciscoConfigManCTIDNotifyGroup": ciscoConfigManCTIDNotifyGroup,
       "ciscoConfigManCTIDObjectGroup": ciscoConfigManCTIDObjectGroup}
)
