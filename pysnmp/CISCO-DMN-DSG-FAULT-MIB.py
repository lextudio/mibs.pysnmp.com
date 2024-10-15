# SNMP MIB module (CISCO-DMN-DSG-FAULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-FAULT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:23 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGFault = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17)
)
ciscoDSGFault.setRevisions(
        ("2010-08-30 11:00",
         "2010-03-22 05:00",
         "2010-02-12 12:00",
         "2010-01-08 12:00",
         "2009-12-20 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FaultSummary_ObjectIdentity = ObjectIdentity
faultSummary = _FaultSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1)
)


class _FaultSummaryNumActiveAlarms_Type(DisplayString):
    """Custom type faultSummaryNumActiveAlarms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FaultSummaryNumActiveAlarms_Type.__name__ = "DisplayString"
_FaultSummaryNumActiveAlarms_Object = MibScalar
faultSummaryNumActiveAlarms = _FaultSummaryNumActiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 1),
    _FaultSummaryNumActiveAlarms_Type()
)
faultSummaryNumActiveAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultSummaryNumActiveAlarms.setStatus("current")


class _FaultSummaryNumActiveWarnings_Type(DisplayString):
    """Custom type faultSummaryNumActiveWarnings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FaultSummaryNumActiveWarnings_Type.__name__ = "DisplayString"
_FaultSummaryNumActiveWarnings_Object = MibScalar
faultSummaryNumActiveWarnings = _FaultSummaryNumActiveWarnings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 2),
    _FaultSummaryNumActiveWarnings_Type()
)
faultSummaryNumActiveWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultSummaryNumActiveWarnings.setStatus("current")


class _FaultSummaryClearAlarms_Type(Integer32):
    """Custom type faultSummaryClearAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeonly", 1),
          ("yes", 2))
    )


_FaultSummaryClearAlarms_Type.__name__ = "Integer32"
_FaultSummaryClearAlarms_Object = MibScalar
faultSummaryClearAlarms = _FaultSummaryClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 3),
    _FaultSummaryClearAlarms_Type()
)
faultSummaryClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultSummaryClearAlarms.setStatus("current")


class _FaultSummaryClearWarnings_Type(Integer32):
    """Custom type faultSummaryClearWarnings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_FaultSummaryClearWarnings_Type.__name__ = "Integer32"
_FaultSummaryClearWarnings_Object = MibScalar
faultSummaryClearWarnings = _FaultSummaryClearWarnings_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 4),
    _FaultSummaryClearWarnings_Type()
)
faultSummaryClearWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultSummaryClearWarnings.setStatus("current")


class _FaultSummaryClearHistory_Type(Integer32):
    """Custom type faultSummaryClearHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("writeOnly", 1),
          ("yes", 2))
    )


_FaultSummaryClearHistory_Type.__name__ = "Integer32"
_FaultSummaryClearHistory_Object = MibScalar
faultSummaryClearHistory = _FaultSummaryClearHistory_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 1, 5),
    _FaultSummaryClearHistory_Type()
)
faultSummaryClearHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultSummaryClearHistory.setStatus("current")
_FaultAWTable_ObjectIdentity = ObjectIdentity
faultAWTable = _FaultAWTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2)
)
_AwFaultActiveListTable_Object = MibTable
awFaultActiveListTable = _AwFaultActiveListTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1)
)
if mibBuilder.loadTexts:
    awFaultActiveListTable.setStatus("current")
_AwFaultActiveListEntry_Object = MibTableRow
awFaultActiveListEntry = _AwFaultActiveListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1)
)
awFaultActiveListEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultActiveListPriority"),
)
if mibBuilder.loadTexts:
    awFaultActiveListEntry.setStatus("current")


class _AwFaultActiveListPriority_Type(Integer32):
    """Custom type awFaultActiveListPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AwFaultActiveListPriority_Type.__name__ = "Integer32"
_AwFaultActiveListPriority_Object = MibTableColumn
awFaultActiveListPriority = _AwFaultActiveListPriority_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 1),
    _AwFaultActiveListPriority_Type()
)
awFaultActiveListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awFaultActiveListPriority.setStatus("current")


class _AwFaultActiveListTextID_Type(DisplayString):
    """Custom type awFaultActiveListTextID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultActiveListTextID_Type.__name__ = "DisplayString"
_AwFaultActiveListTextID_Object = MibTableColumn
awFaultActiveListTextID = _AwFaultActiveListTextID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 2),
    _AwFaultActiveListTextID_Type()
)
awFaultActiveListTextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultActiveListTextID.setStatus("current")


class _AwFaultActiveListName_Type(DisplayString):
    """Custom type awFaultActiveListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultActiveListName_Type.__name__ = "DisplayString"
_AwFaultActiveListName_Object = MibTableColumn
awFaultActiveListName = _AwFaultActiveListName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 3),
    _AwFaultActiveListName_Type()
)
awFaultActiveListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultActiveListName.setStatus("current")


class _AwFaultActiveListType_Type(Integer32):
    """Custom type awFaultActiveListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warning", 2))
    )


_AwFaultActiveListType_Type.__name__ = "Integer32"
_AwFaultActiveListType_Object = MibTableColumn
awFaultActiveListType = _AwFaultActiveListType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 4),
    _AwFaultActiveListType_Type()
)
awFaultActiveListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultActiveListType.setStatus("current")


class _AwFaultActiveListSetDateTime_Type(DisplayString):
    """Custom type awFaultActiveListSetDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultActiveListSetDateTime_Type.__name__ = "DisplayString"
_AwFaultActiveListSetDateTime_Object = MibTableColumn
awFaultActiveListSetDateTime = _AwFaultActiveListSetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 5),
    _AwFaultActiveListSetDateTime_Type()
)
awFaultActiveListSetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultActiveListSetDateTime.setStatus("current")


class _AwFaultActiveListDetails_Type(DisplayString):
    """Custom type awFaultActiveListDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AwFaultActiveListDetails_Type.__name__ = "DisplayString"
_AwFaultActiveListDetails_Object = MibTableColumn
awFaultActiveListDetails = _AwFaultActiveListDetails_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 1, 1, 6),
    _AwFaultActiveListDetails_Type()
)
awFaultActiveListDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultActiveListDetails.setStatus("current")
_AwFaultStatusTable_Object = MibTable
awFaultStatusTable = _AwFaultStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2)
)
if mibBuilder.loadTexts:
    awFaultStatusTable.setStatus("current")
_AwFaultStatusEntry_Object = MibTableRow
awFaultStatusEntry = _AwFaultStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1)
)
awFaultStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultStatusPriority"),
)
if mibBuilder.loadTexts:
    awFaultStatusEntry.setStatus("current")


class _AwFaultStatusPriority_Type(Integer32):
    """Custom type awFaultStatusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AwFaultStatusPriority_Type.__name__ = "Integer32"
_AwFaultStatusPriority_Object = MibTableColumn
awFaultStatusPriority = _AwFaultStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 1),
    _AwFaultStatusPriority_Type()
)
awFaultStatusPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awFaultStatusPriority.setStatus("current")


class _AwFaultStatusTextId_Type(DisplayString):
    """Custom type awFaultStatusTextId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultStatusTextId_Type.__name__ = "DisplayString"
_AwFaultStatusTextId_Object = MibTableColumn
awFaultStatusTextId = _AwFaultStatusTextId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 2),
    _AwFaultStatusTextId_Type()
)
awFaultStatusTextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusTextId.setStatus("current")


class _AwFaultStatusFaultNum_Type(DisplayString):
    """Custom type awFaultStatusFaultNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultStatusFaultNum_Type.__name__ = "DisplayString"
_AwFaultStatusFaultNum_Object = MibTableColumn
awFaultStatusFaultNum = _AwFaultStatusFaultNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 3),
    _AwFaultStatusFaultNum_Type()
)
awFaultStatusFaultNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusFaultNum.setStatus("current")


class _AwFaultStatusName_Type(DisplayString):
    """Custom type awFaultStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultStatusName_Type.__name__ = "DisplayString"
_AwFaultStatusName_Object = MibTableColumn
awFaultStatusName = _AwFaultStatusName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 4),
    _AwFaultStatusName_Type()
)
awFaultStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusName.setStatus("current")


class _AwFaultStatusType_Type(Integer32):
    """Custom type awFaultStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warning", 2))
    )


_AwFaultStatusType_Type.__name__ = "Integer32"
_AwFaultStatusType_Object = MibTableColumn
awFaultStatusType = _AwFaultStatusType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 5),
    _AwFaultStatusType_Type()
)
awFaultStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusType.setStatus("current")


class _AwFaultStatusSeverity_Type(Integer32):
    """Custom type awFaultStatusSeverity based on Integer32"""
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
        *(("information", 4),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )


_AwFaultStatusSeverity_Type.__name__ = "Integer32"
_AwFaultStatusSeverity_Object = MibTableColumn
awFaultStatusSeverity = _AwFaultStatusSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 6),
    _AwFaultStatusSeverity_Type()
)
awFaultStatusSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusSeverity.setStatus("current")


class _AwFaultStatusLastDateTime_Type(DisplayString):
    """Custom type awFaultStatusLastDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultStatusLastDateTime_Type.__name__ = "DisplayString"
_AwFaultStatusLastDateTime_Object = MibTableColumn
awFaultStatusLastDateTime = _AwFaultStatusLastDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 7),
    _AwFaultStatusLastDateTime_Type()
)
awFaultStatusLastDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusLastDateTime.setStatus("current")


class _AwFaultStatusTrapState_Type(Integer32):
    """Custom type awFaultStatusTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_AwFaultStatusTrapState_Type.__name__ = "Integer32"
_AwFaultStatusTrapState_Object = MibTableColumn
awFaultStatusTrapState = _AwFaultStatusTrapState_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 8),
    _AwFaultStatusTrapState_Type()
)
awFaultStatusTrapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusTrapState.setStatus("current")


class _AwFaultStatusDetails_Type(DisplayString):
    """Custom type awFaultStatusDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AwFaultStatusDetails_Type.__name__ = "DisplayString"
_AwFaultStatusDetails_Object = MibTableColumn
awFaultStatusDetails = _AwFaultStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 9),
    _AwFaultStatusDetails_Type()
)
awFaultStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusDetails.setStatus("current")


class _AwFaultStatusRelay_Type(DisplayString):
    """Custom type awFaultStatusRelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultStatusRelay_Type.__name__ = "DisplayString"
_AwFaultStatusRelay_Object = MibTableColumn
awFaultStatusRelay = _AwFaultStatusRelay_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 2, 1, 10),
    _AwFaultStatusRelay_Type()
)
awFaultStatusRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultStatusRelay.setStatus("current")
_AwFaultSettingTable_Object = MibTable
awFaultSettingTable = _AwFaultSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3)
)
if mibBuilder.loadTexts:
    awFaultSettingTable.setStatus("current")
_AwFaultSettingEntry_Object = MibTableRow
awFaultSettingEntry = _AwFaultSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1)
)
awFaultSettingEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultSettingPriority"),
)
if mibBuilder.loadTexts:
    awFaultSettingEntry.setStatus("current")


class _AwFaultSettingPriority_Type(Integer32):
    """Custom type awFaultSettingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AwFaultSettingPriority_Type.__name__ = "Integer32"
_AwFaultSettingPriority_Object = MibTableColumn
awFaultSettingPriority = _AwFaultSettingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 1),
    _AwFaultSettingPriority_Type()
)
awFaultSettingPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awFaultSettingPriority.setStatus("current")


class _AwFaultSettingTextId_Type(DisplayString):
    """Custom type awFaultSettingTextId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultSettingTextId_Type.__name__ = "DisplayString"
_AwFaultSettingTextId_Object = MibTableColumn
awFaultSettingTextId = _AwFaultSettingTextId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 2),
    _AwFaultSettingTextId_Type()
)
awFaultSettingTextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultSettingTextId.setStatus("current")


class _AwFaultSettingType_Type(Integer32):
    """Custom type awFaultSettingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warning", 2))
    )


_AwFaultSettingType_Type.__name__ = "Integer32"
_AwFaultSettingType_Object = MibTableColumn
awFaultSettingType = _AwFaultSettingType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 3),
    _AwFaultSettingType_Type()
)
awFaultSettingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultSettingType.setStatus("current")


class _AwFaultSettingSeverity_Type(Integer32):
    """Custom type awFaultSettingSeverity based on Integer32"""
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
        *(("information", 4),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )


_AwFaultSettingSeverity_Type.__name__ = "Integer32"
_AwFaultSettingSeverity_Object = MibTableColumn
awFaultSettingSeverity = _AwFaultSettingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 4),
    _AwFaultSettingSeverity_Type()
)
awFaultSettingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultSettingSeverity.setStatus("current")


class _AwFaultSettingName_Type(DisplayString):
    """Custom type awFaultSettingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultSettingName_Type.__name__ = "DisplayString"
_AwFaultSettingName_Object = MibTableColumn
awFaultSettingName = _AwFaultSettingName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 5),
    _AwFaultSettingName_Type()
)
awFaultSettingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultSettingName.setStatus("current")


class _AwFaultSettingEnable_Type(Integer32):
    """Custom type awFaultSettingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("no", 1),
          ("yes", 2))
    )


_AwFaultSettingEnable_Type.__name__ = "Integer32"
_AwFaultSettingEnable_Object = MibTableColumn
awFaultSettingEnable = _AwFaultSettingEnable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 6),
    _AwFaultSettingEnable_Type()
)
awFaultSettingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awFaultSettingEnable.setStatus("current")


class _AwFaultSettingRelay_Type(Integer32):
    """Custom type awFaultSettingRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("no", 1),
          ("yes", 2))
    )


_AwFaultSettingRelay_Type.__name__ = "Integer32"
_AwFaultSettingRelay_Object = MibTableColumn
awFaultSettingRelay = _AwFaultSettingRelay_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 7),
    _AwFaultSettingRelay_Type()
)
awFaultSettingRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awFaultSettingRelay.setStatus("current")


class _AwFaultSettingTrap_Type(Integer32):
    """Custom type awFaultSettingTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("no", 1),
          ("yes", 2))
    )


_AwFaultSettingTrap_Type.__name__ = "Integer32"
_AwFaultSettingTrap_Object = MibTableColumn
awFaultSettingTrap = _AwFaultSettingTrap_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 3, 1, 8),
    _AwFaultSettingTrap_Type()
)
awFaultSettingTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    awFaultSettingTrap.setStatus("current")
_AwFaultHistoryTable_Object = MibTable
awFaultHistoryTable = _AwFaultHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5)
)
if mibBuilder.loadTexts:
    awFaultHistoryTable.setStatus("current")
_AwFaultHistoryEntry_Object = MibTableRow
awFaultHistoryEntry = _AwFaultHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1)
)
awFaultHistoryEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-FAULT-MIB", "awFaultHistorySequence"),
)
if mibBuilder.loadTexts:
    awFaultHistoryEntry.setStatus("current")
_AwFaultHistorySequence_Type = Counter32
_AwFaultHistorySequence_Object = MibTableColumn
awFaultHistorySequence = _AwFaultHistorySequence_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 1),
    _AwFaultHistorySequence_Type()
)
awFaultHistorySequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awFaultHistorySequence.setStatus("current")


class _AwFaultHistoryName_Type(DisplayString):
    """Custom type awFaultHistoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultHistoryName_Type.__name__ = "DisplayString"
_AwFaultHistoryName_Object = MibTableColumn
awFaultHistoryName = _AwFaultHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 2),
    _AwFaultHistoryName_Type()
)
awFaultHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistoryName.setStatus("current")


class _AwFaultHistoryType_Type(Integer32):
    """Custom type awFaultHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warning", 2))
    )


_AwFaultHistoryType_Type.__name__ = "Integer32"
_AwFaultHistoryType_Object = MibTableColumn
awFaultHistoryType = _AwFaultHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 3),
    _AwFaultHistoryType_Type()
)
awFaultHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistoryType.setStatus("current")


class _AwFaultHistorySetDateTime_Type(DisplayString):
    """Custom type awFaultHistorySetDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultHistorySetDateTime_Type.__name__ = "DisplayString"
_AwFaultHistorySetDateTime_Object = MibTableColumn
awFaultHistorySetDateTime = _AwFaultHistorySetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 4),
    _AwFaultHistorySetDateTime_Type()
)
awFaultHistorySetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistorySetDateTime.setStatus("current")


class _AwFaultHistoryResetDateTime_Type(DisplayString):
    """Custom type awFaultHistoryResetDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AwFaultHistoryResetDateTime_Type.__name__ = "DisplayString"
_AwFaultHistoryResetDateTime_Object = MibTableColumn
awFaultHistoryResetDateTime = _AwFaultHistoryResetDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 5),
    _AwFaultHistoryResetDateTime_Type()
)
awFaultHistoryResetDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistoryResetDateTime.setStatus("current")


class _AwFaultHistoryState_Type(Integer32):
    """Custom type awFaultHistoryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("clearByReset", 3),
          ("set", 2))
    )


_AwFaultHistoryState_Type.__name__ = "Integer32"
_AwFaultHistoryState_Object = MibTableColumn
awFaultHistoryState = _AwFaultHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 6),
    _AwFaultHistoryState_Type()
)
awFaultHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistoryState.setStatus("current")


class _AwFaultHistoryDetails_Type(DisplayString):
    """Custom type awFaultHistoryDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AwFaultHistoryDetails_Type.__name__ = "DisplayString"
_AwFaultHistoryDetails_Object = MibTableColumn
awFaultHistoryDetails = _AwFaultHistoryDetails_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 17, 2, 5, 1, 7),
    _AwFaultHistoryDetails_Type()
)
awFaultHistoryDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awFaultHistoryDetails.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-FAULT-MIB",
    **{"ciscoDSGFault": ciscoDSGFault,
       "faultSummary": faultSummary,
       "faultSummaryNumActiveAlarms": faultSummaryNumActiveAlarms,
       "faultSummaryNumActiveWarnings": faultSummaryNumActiveWarnings,
       "faultSummaryClearAlarms": faultSummaryClearAlarms,
       "faultSummaryClearWarnings": faultSummaryClearWarnings,
       "faultSummaryClearHistory": faultSummaryClearHistory,
       "faultAWTable": faultAWTable,
       "awFaultActiveListTable": awFaultActiveListTable,
       "awFaultActiveListEntry": awFaultActiveListEntry,
       "awFaultActiveListPriority": awFaultActiveListPriority,
       "awFaultActiveListTextID": awFaultActiveListTextID,
       "awFaultActiveListName": awFaultActiveListName,
       "awFaultActiveListType": awFaultActiveListType,
       "awFaultActiveListSetDateTime": awFaultActiveListSetDateTime,
       "awFaultActiveListDetails": awFaultActiveListDetails,
       "awFaultStatusTable": awFaultStatusTable,
       "awFaultStatusEntry": awFaultStatusEntry,
       "awFaultStatusPriority": awFaultStatusPriority,
       "awFaultStatusTextId": awFaultStatusTextId,
       "awFaultStatusFaultNum": awFaultStatusFaultNum,
       "awFaultStatusName": awFaultStatusName,
       "awFaultStatusType": awFaultStatusType,
       "awFaultStatusSeverity": awFaultStatusSeverity,
       "awFaultStatusLastDateTime": awFaultStatusLastDateTime,
       "awFaultStatusTrapState": awFaultStatusTrapState,
       "awFaultStatusDetails": awFaultStatusDetails,
       "awFaultStatusRelay": awFaultStatusRelay,
       "awFaultSettingTable": awFaultSettingTable,
       "awFaultSettingEntry": awFaultSettingEntry,
       "awFaultSettingPriority": awFaultSettingPriority,
       "awFaultSettingTextId": awFaultSettingTextId,
       "awFaultSettingType": awFaultSettingType,
       "awFaultSettingSeverity": awFaultSettingSeverity,
       "awFaultSettingName": awFaultSettingName,
       "awFaultSettingEnable": awFaultSettingEnable,
       "awFaultSettingRelay": awFaultSettingRelay,
       "awFaultSettingTrap": awFaultSettingTrap,
       "awFaultHistoryTable": awFaultHistoryTable,
       "awFaultHistoryEntry": awFaultHistoryEntry,
       "awFaultHistorySequence": awFaultHistorySequence,
       "awFaultHistoryName": awFaultHistoryName,
       "awFaultHistoryType": awFaultHistoryType,
       "awFaultHistorySetDateTime": awFaultHistorySetDateTime,
       "awFaultHistoryResetDateTime": awFaultHistoryResetDateTime,
       "awFaultHistoryState": awFaultHistoryState,
       "awFaultHistoryDetails": awFaultHistoryDetails}
)
