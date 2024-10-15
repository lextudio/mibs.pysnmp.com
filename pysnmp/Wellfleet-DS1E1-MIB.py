# SNMP MIB module (Wellfleet-DS1E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DS1E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:04 2024
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

(wfDs1E1Group,
 wfMcT1Group) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDs1E1Group",
    "wfMcT1Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDs1E1AnsiTable_Object = MibTable
wfDs1E1AnsiTable = _WfDs1E1AnsiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13)
)
if mibBuilder.loadTexts:
    wfDs1E1AnsiTable.setStatus("mandatory")
_WfDs1E1AnsiEntry_Object = MibTableRow
wfDs1E1AnsiEntry = _WfDs1E1AnsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1)
)
wfDs1E1AnsiEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1AnsiPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1AnsiEntry.setStatus("mandatory")
_WfDs1E1AnsiPortLineNumber_Type = Integer32
_WfDs1E1AnsiPortLineNumber_Object = MibTableColumn
wfDs1E1AnsiPortLineNumber = _WfDs1E1AnsiPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 1),
    _WfDs1E1AnsiPortLineNumber_Type()
)
wfDs1E1AnsiPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPortLineNumber.setStatus("mandatory")
_WfDs1E1AnsiCRCCounts_Type = Counter32
_WfDs1E1AnsiCRCCounts_Object = MibTableColumn
wfDs1E1AnsiCRCCounts = _WfDs1E1AnsiCRCCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 2),
    _WfDs1E1AnsiCRCCounts_Type()
)
wfDs1E1AnsiCRCCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiCRCCounts.setStatus("mandatory")
_WfDs1E1AnsiBPVCounts_Type = Counter32
_WfDs1E1AnsiBPVCounts_Object = MibTableColumn
wfDs1E1AnsiBPVCounts = _WfDs1E1AnsiBPVCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 3),
    _WfDs1E1AnsiBPVCounts_Type()
)
wfDs1E1AnsiBPVCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiBPVCounts.setStatus("mandatory")
_WfDs1E1AnsiOOFCounts_Type = Counter32
_WfDs1E1AnsiOOFCounts_Object = MibTableColumn
wfDs1E1AnsiOOFCounts = _WfDs1E1AnsiOOFCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 4),
    _WfDs1E1AnsiOOFCounts_Type()
)
wfDs1E1AnsiOOFCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiOOFCounts.setStatus("mandatory")
_WfDs1E1AnsiFECounts_Type = Counter32
_WfDs1E1AnsiFECounts_Object = MibTableColumn
wfDs1E1AnsiFECounts = _WfDs1E1AnsiFECounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 5),
    _WfDs1E1AnsiFECounts_Type()
)
wfDs1E1AnsiFECounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiFECounts.setStatus("mandatory")
_WfDs1E1AnsiESCounts_Type = Counter32
_WfDs1E1AnsiESCounts_Object = MibTableColumn
wfDs1E1AnsiESCounts = _WfDs1E1AnsiESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 6),
    _WfDs1E1AnsiESCounts_Type()
)
wfDs1E1AnsiESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiESCounts.setStatus("mandatory")
_WfDs1E1AnsiSESCounts_Type = Counter32
_WfDs1E1AnsiSESCounts_Object = MibTableColumn
wfDs1E1AnsiSESCounts = _WfDs1E1AnsiSESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 7),
    _WfDs1E1AnsiSESCounts_Type()
)
wfDs1E1AnsiSESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiSESCounts.setStatus("mandatory")
_WfDs1E1AnsiUASCounts_Type = Counter32
_WfDs1E1AnsiUASCounts_Object = MibTableColumn
wfDs1E1AnsiUASCounts = _WfDs1E1AnsiUASCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 8),
    _WfDs1E1AnsiUASCounts_Type()
)
wfDs1E1AnsiUASCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiUASCounts.setStatus("mandatory")
_WfDs1E1AnsiPRMR0Counts_Type = Counter32
_WfDs1E1AnsiPRMR0Counts_Object = MibTableColumn
wfDs1E1AnsiPRMR0Counts = _WfDs1E1AnsiPRMR0Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 9),
    _WfDs1E1AnsiPRMR0Counts_Type()
)
wfDs1E1AnsiPRMR0Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMR0Counts.setStatus("mandatory")
_WfDs1E1AnsiPRMR1Counts_Type = Counter32
_WfDs1E1AnsiPRMR1Counts_Object = MibTableColumn
wfDs1E1AnsiPRMR1Counts = _WfDs1E1AnsiPRMR1Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 10),
    _WfDs1E1AnsiPRMR1Counts_Type()
)
wfDs1E1AnsiPRMR1Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMR1Counts.setStatus("mandatory")
_WfDs1E1AnsiPRMR2Counts_Type = Counter32
_WfDs1E1AnsiPRMR2Counts_Object = MibTableColumn
wfDs1E1AnsiPRMR2Counts = _WfDs1E1AnsiPRMR2Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 11),
    _WfDs1E1AnsiPRMR2Counts_Type()
)
wfDs1E1AnsiPRMR2Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMR2Counts.setStatus("mandatory")
_WfDs1E1AnsiPRMR3Counts_Type = Counter32
_WfDs1E1AnsiPRMR3Counts_Object = MibTableColumn
wfDs1E1AnsiPRMR3Counts = _WfDs1E1AnsiPRMR3Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 12),
    _WfDs1E1AnsiPRMR3Counts_Type()
)
wfDs1E1AnsiPRMR3Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMR3Counts.setStatus("mandatory")
_WfDs1E1AnsiPRMESCounts_Type = Counter32
_WfDs1E1AnsiPRMESCounts_Object = MibTableColumn
wfDs1E1AnsiPRMESCounts = _WfDs1E1AnsiPRMESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 13),
    _WfDs1E1AnsiPRMESCounts_Type()
)
wfDs1E1AnsiPRMESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMESCounts.setStatus("mandatory")
_WfDs1E1AnsiPRMSESCounts_Type = Counter32
_WfDs1E1AnsiPRMSESCounts_Object = MibTableColumn
wfDs1E1AnsiPRMSESCounts = _WfDs1E1AnsiPRMSESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 14),
    _WfDs1E1AnsiPRMSESCounts_Type()
)
wfDs1E1AnsiPRMSESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMSESCounts.setStatus("mandatory")
_WfDs1E1AnsiPRMECounts_Type = Counter32
_WfDs1E1AnsiPRMECounts_Object = MibTableColumn
wfDs1E1AnsiPRMECounts = _WfDs1E1AnsiPRMECounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 13, 1, 15),
    _WfDs1E1AnsiPRMECounts_Type()
)
wfDs1E1AnsiPRMECounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1AnsiPRMECounts.setStatus("mandatory")
_WfDs1E1ModuleTable_Object = MibTable
wfDs1E1ModuleTable = _WfDs1E1ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1)
)
if mibBuilder.loadTexts:
    wfDs1E1ModuleTable.setStatus("mandatory")
_WfDs1E1ModuleEntry_Object = MibTableRow
wfDs1E1ModuleEntry = _WfDs1E1ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1)
)
wfDs1E1ModuleEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ModuleSlot"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ModuleModule"),
)
if mibBuilder.loadTexts:
    wfDs1E1ModuleEntry.setStatus("mandatory")


class _WfDs1E1ModuleDelete_Type(Integer32):
    """Custom type wfDs1E1ModuleDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1ModuleDelete_Type.__name__ = "Integer32"
_WfDs1E1ModuleDelete_Object = MibTableColumn
wfDs1E1ModuleDelete = _WfDs1E1ModuleDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 1),
    _WfDs1E1ModuleDelete_Type()
)
wfDs1E1ModuleDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ModuleDelete.setStatus("mandatory")
_WfDs1E1ModuleSlot_Type = Integer32
_WfDs1E1ModuleSlot_Object = MibTableColumn
wfDs1E1ModuleSlot = _WfDs1E1ModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 2),
    _WfDs1E1ModuleSlot_Type()
)
wfDs1E1ModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleSlot.setStatus("mandatory")
_WfDs1E1ModuleModule_Type = Integer32
_WfDs1E1ModuleModule_Object = MibTableColumn
wfDs1E1ModuleModule = _WfDs1E1ModuleModule_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 3),
    _WfDs1E1ModuleModule_Type()
)
wfDs1E1ModuleModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleModule.setStatus("mandatory")


class _WfDs1E1ModulePrimaryClock_Type(Integer32):
    """Custom type wfDs1E1ModulePrimaryClock based on Integer32"""
    defaultValue = 2

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
        *(("external", 1),
          ("internal", 4),
          ("loop1", 2),
          ("loop2", 3),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ModulePrimaryClock_Type.__name__ = "Integer32"
_WfDs1E1ModulePrimaryClock_Object = MibTableColumn
wfDs1E1ModulePrimaryClock = _WfDs1E1ModulePrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 4),
    _WfDs1E1ModulePrimaryClock_Type()
)
wfDs1E1ModulePrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ModulePrimaryClock.setStatus("mandatory")


class _WfDs1E1ModuleSecondaryClock_Type(Integer32):
    """Custom type wfDs1E1ModuleSecondaryClock based on Integer32"""
    defaultValue = 4

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
        *(("external", 1),
          ("internal", 4),
          ("loop1", 2),
          ("loop2", 3),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ModuleSecondaryClock_Type.__name__ = "Integer32"
_WfDs1E1ModuleSecondaryClock_Object = MibTableColumn
wfDs1E1ModuleSecondaryClock = _WfDs1E1ModuleSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 5),
    _WfDs1E1ModuleSecondaryClock_Type()
)
wfDs1E1ModuleSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ModuleSecondaryClock.setStatus("mandatory")


class _WfDs1E1ModuleCurrentClock_Type(Integer32):
    """Custom type wfDs1E1ModuleCurrentClock based on Integer32"""
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
        *(("external", 1),
          ("internal", 4),
          ("loop1", 2),
          ("loop2", 3),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ModuleCurrentClock_Type.__name__ = "Integer32"
_WfDs1E1ModuleCurrentClock_Object = MibTableColumn
wfDs1E1ModuleCurrentClock = _WfDs1E1ModuleCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 6),
    _WfDs1E1ModuleCurrentClock_Type()
)
wfDs1E1ModuleCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleCurrentClock.setStatus("mandatory")


class _WfDs1E1ModuleExtClockOperational_Type(Integer32):
    """Custom type wfDs1E1ModuleExtClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ModuleExtClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ModuleExtClockOperational_Object = MibTableColumn
wfDs1E1ModuleExtClockOperational = _WfDs1E1ModuleExtClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 7),
    _WfDs1E1ModuleExtClockOperational_Type()
)
wfDs1E1ModuleExtClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleExtClockOperational.setStatus("mandatory")


class _WfDs1E1ModuleLoop1ClockOperational_Type(Integer32):
    """Custom type wfDs1E1ModuleLoop1ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ModuleLoop1ClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ModuleLoop1ClockOperational_Object = MibTableColumn
wfDs1E1ModuleLoop1ClockOperational = _WfDs1E1ModuleLoop1ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 8),
    _WfDs1E1ModuleLoop1ClockOperational_Type()
)
wfDs1E1ModuleLoop1ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleLoop1ClockOperational.setStatus("mandatory")


class _WfDs1E1ModuleLoop2ClockOperational_Type(Integer32):
    """Custom type wfDs1E1ModuleLoop2ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ModuleLoop2ClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ModuleLoop2ClockOperational_Object = MibTableColumn
wfDs1E1ModuleLoop2ClockOperational = _WfDs1E1ModuleLoop2ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 9),
    _WfDs1E1ModuleLoop2ClockOperational_Type()
)
wfDs1E1ModuleLoop2ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleLoop2ClockOperational.setStatus("mandatory")


class _WfDs1E1ModuleLoop3ClockOperational_Type(Integer32):
    """Custom type wfDs1E1ModuleLoop3ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ModuleLoop3ClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ModuleLoop3ClockOperational_Object = MibTableColumn
wfDs1E1ModuleLoop3ClockOperational = _WfDs1E1ModuleLoop3ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 10),
    _WfDs1E1ModuleLoop3ClockOperational_Type()
)
wfDs1E1ModuleLoop3ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleLoop3ClockOperational.setStatus("mandatory")


class _WfDs1E1ModuleLoop4ClockOperational_Type(Integer32):
    """Custom type wfDs1E1ModuleLoop4ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ModuleLoop4ClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ModuleLoop4ClockOperational_Object = MibTableColumn
wfDs1E1ModuleLoop4ClockOperational = _WfDs1E1ModuleLoop4ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 11),
    _WfDs1E1ModuleLoop4ClockOperational_Type()
)
wfDs1E1ModuleLoop4ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleLoop4ClockOperational.setStatus("mandatory")


class _WfDs1E1ModuleCfgTxBufferUseCredits_Type(Integer32):
    """Custom type wfDs1E1ModuleCfgTxBufferUseCredits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WfDs1E1ModuleCfgTxBufferUseCredits_Type.__name__ = "Integer32"
_WfDs1E1ModuleCfgTxBufferUseCredits_Object = MibTableColumn
wfDs1E1ModuleCfgTxBufferUseCredits = _WfDs1E1ModuleCfgTxBufferUseCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 12),
    _WfDs1E1ModuleCfgTxBufferUseCredits_Type()
)
wfDs1E1ModuleCfgTxBufferUseCredits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ModuleCfgTxBufferUseCredits.setStatus("mandatory")


class _WfDs1E1ModuleCfgRxBufferUseCredits_Type(Integer32):
    """Custom type wfDs1E1ModuleCfgRxBufferUseCredits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WfDs1E1ModuleCfgRxBufferUseCredits_Type.__name__ = "Integer32"
_WfDs1E1ModuleCfgRxBufferUseCredits_Object = MibTableColumn
wfDs1E1ModuleCfgRxBufferUseCredits = _WfDs1E1ModuleCfgRxBufferUseCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 13),
    _WfDs1E1ModuleCfgRxBufferUseCredits_Type()
)
wfDs1E1ModuleCfgRxBufferUseCredits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ModuleCfgRxBufferUseCredits.setStatus("mandatory")
_WfDs1E1ModuleTxBufferUseCredits_Type = Integer32
_WfDs1E1ModuleTxBufferUseCredits_Object = MibTableColumn
wfDs1E1ModuleTxBufferUseCredits = _WfDs1E1ModuleTxBufferUseCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 14),
    _WfDs1E1ModuleTxBufferUseCredits_Type()
)
wfDs1E1ModuleTxBufferUseCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleTxBufferUseCredits.setStatus("mandatory")
_WfDs1E1ModuleRxBufferUseCredits_Type = Integer32
_WfDs1E1ModuleRxBufferUseCredits_Object = MibTableColumn
wfDs1E1ModuleRxBufferUseCredits = _WfDs1E1ModuleRxBufferUseCredits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 1, 1, 15),
    _WfDs1E1ModuleRxBufferUseCredits_Type()
)
wfDs1E1ModuleRxBufferUseCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ModuleRxBufferUseCredits.setStatus("mandatory")
_WfDs1E1PortMapTable_Object = MibTable
wfDs1E1PortMapTable = _WfDs1E1PortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2)
)
if mibBuilder.loadTexts:
    wfDs1E1PortMapTable.setStatus("mandatory")
_WfDs1E1PortMapEntry_Object = MibTableRow
wfDs1E1PortMapEntry = _WfDs1E1PortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1)
)
wfDs1E1PortMapEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1PortMapSlot"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1PortMapConnector"),
)
if mibBuilder.loadTexts:
    wfDs1E1PortMapEntry.setStatus("mandatory")


class _WfDs1E1PortMapDelete_Type(Integer32):
    """Custom type wfDs1E1PortMapDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1PortMapDelete_Type.__name__ = "Integer32"
_WfDs1E1PortMapDelete_Object = MibTableColumn
wfDs1E1PortMapDelete = _WfDs1E1PortMapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1, 1),
    _WfDs1E1PortMapDelete_Type()
)
wfDs1E1PortMapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortMapDelete.setStatus("mandatory")
_WfDs1E1PortMapSlot_Type = Integer32
_WfDs1E1PortMapSlot_Object = MibTableColumn
wfDs1E1PortMapSlot = _WfDs1E1PortMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1, 2),
    _WfDs1E1PortMapSlot_Type()
)
wfDs1E1PortMapSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortMapSlot.setStatus("mandatory")
_WfDs1E1PortMapConnector_Type = Integer32
_WfDs1E1PortMapConnector_Object = MibTableColumn
wfDs1E1PortMapConnector = _WfDs1E1PortMapConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1, 3),
    _WfDs1E1PortMapConnector_Type()
)
wfDs1E1PortMapConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortMapConnector.setStatus("mandatory")
_WfDs1E1PortMapLineNumber_Type = Integer32
_WfDs1E1PortMapLineNumber_Object = MibTableColumn
wfDs1E1PortMapLineNumber = _WfDs1E1PortMapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1, 4),
    _WfDs1E1PortMapLineNumber_Type()
)
wfDs1E1PortMapLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortMapLineNumber.setStatus("mandatory")
_WfDs1E1PortMapDslId_Type = Integer32
_WfDs1E1PortMapDslId_Object = MibTableColumn
wfDs1E1PortMapDslId = _WfDs1E1PortMapDslId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 2, 1, 5),
    _WfDs1E1PortMapDslId_Type()
)
wfDs1E1PortMapDslId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortMapDslId.setStatus("mandatory")
_WfDs1E1PortTable_Object = MibTable
wfDs1E1PortTable = _WfDs1E1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3)
)
if mibBuilder.loadTexts:
    wfDs1E1PortTable.setStatus("mandatory")
_WfDs1E1PortEntry_Object = MibTableRow
wfDs1E1PortEntry = _WfDs1E1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1)
)
wfDs1E1PortEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1PortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1PortEntry.setStatus("mandatory")


class _WfDs1E1PortDelete_Type(Integer32):
    """Custom type wfDs1E1PortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1PortDelete_Type.__name__ = "Integer32"
_WfDs1E1PortDelete_Object = MibTableColumn
wfDs1E1PortDelete = _WfDs1E1PortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 1),
    _WfDs1E1PortDelete_Type()
)
wfDs1E1PortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortDelete.setStatus("mandatory")


class _WfDs1E1PortDisable_Type(Integer32):
    """Custom type wfDs1E1PortDisable based on Integer32"""
    defaultValue = 1

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


_WfDs1E1PortDisable_Type.__name__ = "Integer32"
_WfDs1E1PortDisable_Object = MibTableColumn
wfDs1E1PortDisable = _WfDs1E1PortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 2),
    _WfDs1E1PortDisable_Type()
)
wfDs1E1PortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortDisable.setStatus("mandatory")


class _WfDs1E1PortState_Type(Integer32):
    """Custom type wfDs1E1PortState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              15,
              20)
        )
    )
    namedValues = NamedValues(
        *(("aisalarm", 3),
          ("bert", 11),
          ("init", 15),
          ("loopback", 10),
          ("notpresent", 20),
          ("redalarm", 4),
          ("up", 1),
          ("yelalarm", 2))
    )


_WfDs1E1PortState_Type.__name__ = "Integer32"
_WfDs1E1PortState_Object = MibTableColumn
wfDs1E1PortState = _WfDs1E1PortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 3),
    _WfDs1E1PortState_Type()
)
wfDs1E1PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortState.setStatus("mandatory")
_WfDs1E1PortLineNumber_Type = Integer32
_WfDs1E1PortLineNumber_Object = MibTableColumn
wfDs1E1PortLineNumber = _WfDs1E1PortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 4),
    _WfDs1E1PortLineNumber_Type()
)
wfDs1E1PortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortLineNumber.setStatus("mandatory")


class _WfDs1E1PortMtu_Type(Integer32):
    """Custom type wfDs1E1PortMtu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfDs1E1PortMtu_Type.__name__ = "Integer32"
_WfDs1E1PortMtu_Object = MibTableColumn
wfDs1E1PortMtu = _WfDs1E1PortMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 5),
    _WfDs1E1PortMtu_Type()
)
wfDs1E1PortMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortMtu.setStatus("mandatory")


class _WfDs1E1PortSignalLevel_Type(Integer32):
    """Custom type wfDs1E1PortSignalLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ds1-minus-15", 1),
          ("ds1-minus-7point5", 2),
          ("dsx1-plus-1point1", 6),
          ("dsx1-plus-1point5", 7),
          ("dsx1-plus-point5", 4),
          ("dsx1-plus-point8", 5),
          ("zero-point0", 3))
    )


_WfDs1E1PortSignalLevel_Type.__name__ = "Integer32"
_WfDs1E1PortSignalLevel_Object = MibTableColumn
wfDs1E1PortSignalLevel = _WfDs1E1PortSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 6),
    _WfDs1E1PortSignalLevel_Type()
)
wfDs1E1PortSignalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortSignalLevel.setStatus("mandatory")


class _WfDs1E1PortSetupAlarmThreshold_Type(Integer32):
    """Custom type wfDs1E1PortSetupAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_WfDs1E1PortSetupAlarmThreshold_Type.__name__ = "Integer32"
_WfDs1E1PortSetupAlarmThreshold_Object = MibTableColumn
wfDs1E1PortSetupAlarmThreshold = _WfDs1E1PortSetupAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 7),
    _WfDs1E1PortSetupAlarmThreshold_Type()
)
wfDs1E1PortSetupAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortSetupAlarmThreshold.setStatus("mandatory")


class _WfDs1E1PortClearAlarmThreshold_Type(Integer32):
    """Custom type wfDs1E1PortClearAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_WfDs1E1PortClearAlarmThreshold_Type.__name__ = "Integer32"
_WfDs1E1PortClearAlarmThreshold_Object = MibTableColumn
wfDs1E1PortClearAlarmThreshold = _WfDs1E1PortClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 8),
    _WfDs1E1PortClearAlarmThreshold_Type()
)
wfDs1E1PortClearAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortClearAlarmThreshold.setStatus("mandatory")


class _WfDs1E1PortFdlTargetHdlcAddress_Type(Integer32):
    """Custom type wfDs1E1PortFdlTargetHdlcAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("az", 1),
          ("by", 2))
    )


_WfDs1E1PortFdlTargetHdlcAddress_Type.__name__ = "Integer32"
_WfDs1E1PortFdlTargetHdlcAddress_Object = MibTableColumn
wfDs1E1PortFdlTargetHdlcAddress = _WfDs1E1PortFdlTargetHdlcAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 9),
    _WfDs1E1PortFdlTargetHdlcAddress_Type()
)
wfDs1E1PortFdlTargetHdlcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortFdlTargetHdlcAddress.setStatus("mandatory")


class _WfDs1E1PortAcceptLoopbackRequest_Type(Integer32):
    """Custom type wfDs1E1PortAcceptLoopbackRequest based on Integer32"""
    defaultValue = 1

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


_WfDs1E1PortAcceptLoopbackRequest_Type.__name__ = "Integer32"
_WfDs1E1PortAcceptLoopbackRequest_Object = MibTableColumn
wfDs1E1PortAcceptLoopbackRequest = _WfDs1E1PortAcceptLoopbackRequest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 10),
    _WfDs1E1PortAcceptLoopbackRequest_Type()
)
wfDs1E1PortAcceptLoopbackRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortAcceptLoopbackRequest.setStatus("mandatory")


class _WfDs1E1PortLoopbackState_Type(Integer32):
    """Custom type wfDs1E1PortLoopbackState based on Integer32"""
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
        *(("mgrreqlineloop", 3),
          ("mgrreqpayloadloop", 2),
          ("netreqlineloop", 5),
          ("netreqpayloadloop", 4),
          ("noloop", 1),
          ("otherloop", 6))
    )


_WfDs1E1PortLoopbackState_Type.__name__ = "Integer32"
_WfDs1E1PortLoopbackState_Object = MibTableColumn
wfDs1E1PortLoopbackState = _WfDs1E1PortLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 11),
    _WfDs1E1PortLoopbackState_Type()
)
wfDs1E1PortLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortLoopbackState.setStatus("mandatory")


class _WfDs1E1PortBertMode_Type(Integer32):
    """Custom type wfDs1E1PortBertMode based on Integer32"""
    defaultValue = 2

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


_WfDs1E1PortBertMode_Type.__name__ = "Integer32"
_WfDs1E1PortBertMode_Object = MibTableColumn
wfDs1E1PortBertMode = _WfDs1E1PortBertMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 12),
    _WfDs1E1PortBertMode_Type()
)
wfDs1E1PortBertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortBertMode.setStatus("mandatory")


class _WfDs1E1PortBertTestPattern_Type(Integer32):
    """Custom type wfDs1E1PortBertTestPattern based on Integer32"""
    defaultValue = 2

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
        *(("ones", 2),
          ("qrss", 3),
          ("two15", 4),
          ("two15-inv", 5),
          ("two20", 6),
          ("two23", 7),
          ("two23-inv", 8),
          ("zeros", 1))
    )


_WfDs1E1PortBertTestPattern_Type.__name__ = "Integer32"
_WfDs1E1PortBertTestPattern_Object = MibTableColumn
wfDs1E1PortBertTestPattern = _WfDs1E1PortBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 13),
    _WfDs1E1PortBertTestPattern_Type()
)
wfDs1E1PortBertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortBertTestPattern.setStatus("mandatory")


class _WfDs1E1PortBertSendAlarm_Type(Integer32):
    """Custom type wfDs1E1PortBertSendAlarm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ais-alarm", 1),
          ("disabled", 3),
          ("yellow-alarm", 2))
    )


_WfDs1E1PortBertSendAlarm_Type.__name__ = "Integer32"
_WfDs1E1PortBertSendAlarm_Object = MibTableColumn
wfDs1E1PortBertSendAlarm = _WfDs1E1PortBertSendAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 14),
    _WfDs1E1PortBertSendAlarm_Type()
)
wfDs1E1PortBertSendAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortBertSendAlarm.setStatus("mandatory")


class _WfDs1E1PortInternationalBit_Type(Integer32):
    """Custom type wfDs1E1PortInternationalBit based on Integer32"""
    defaultValue = 2

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


_WfDs1E1PortInternationalBit_Type.__name__ = "Integer32"
_WfDs1E1PortInternationalBit_Object = MibTableColumn
wfDs1E1PortInternationalBit = _WfDs1E1PortInternationalBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 15),
    _WfDs1E1PortInternationalBit_Type()
)
wfDs1E1PortInternationalBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortInternationalBit.setStatus("mandatory")


class _WfDs1E1PortLineApplication_Type(Integer32):
    """Custom type wfDs1E1PortLineApplication based on Integer32"""
    defaultValue = 1

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
        *(("frswpri", 4),
          ("mixed", 3),
          ("nonpri", 1),
          ("pri", 2))
    )


_WfDs1E1PortLineApplication_Type.__name__ = "Integer32"
_WfDs1E1PortLineApplication_Object = MibTableColumn
wfDs1E1PortLineApplication = _WfDs1E1PortLineApplication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 16),
    _WfDs1E1PortLineApplication_Type()
)
wfDs1E1PortLineApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortLineApplication.setStatus("mandatory")
_WfDs1E1PortLoggingEnableMask_Type = Integer32
_WfDs1E1PortLoggingEnableMask_Object = MibTableColumn
wfDs1E1PortLoggingEnableMask = _WfDs1E1PortLoggingEnableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 17),
    _WfDs1E1PortLoggingEnableMask_Type()
)
wfDs1E1PortLoggingEnableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortLoggingEnableMask.setStatus("mandatory")


class _WfDs1E1PortSendPrmCrAddressBit_Type(Integer32):
    """Custom type wfDs1E1PortSendPrmCrAddressBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prm-carrier", 2),
          ("prm-ci", 1))
    )


_WfDs1E1PortSendPrmCrAddressBit_Type.__name__ = "Integer32"
_WfDs1E1PortSendPrmCrAddressBit_Object = MibTableColumn
wfDs1E1PortSendPrmCrAddressBit = _WfDs1E1PortSendPrmCrAddressBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 18),
    _WfDs1E1PortSendPrmCrAddressBit_Type()
)
wfDs1E1PortSendPrmCrAddressBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortSendPrmCrAddressBit.setStatus("mandatory")


class _WfDs1E1PortAcceptPrmCrAddressBit_Type(Integer32):
    """Custom type wfDs1E1PortAcceptPrmCrAddressBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prm-carrier", 2),
          ("prm-ci", 1))
    )


_WfDs1E1PortAcceptPrmCrAddressBit_Type.__name__ = "Integer32"
_WfDs1E1PortAcceptPrmCrAddressBit_Object = MibTableColumn
wfDs1E1PortAcceptPrmCrAddressBit = _WfDs1E1PortAcceptPrmCrAddressBit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 19),
    _WfDs1E1PortAcceptPrmCrAddressBit_Type()
)
wfDs1E1PortAcceptPrmCrAddressBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortAcceptPrmCrAddressBit.setStatus("mandatory")


class _WfDs1E1PortLineImpedanceOption_Type(Integer32):
    """Custom type wfDs1E1PortLineImpedanceOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bnc-75-ohms", 2),
          ("rj45-120-ohms", 1))
    )


_WfDs1E1PortLineImpedanceOption_Type.__name__ = "Integer32"
_WfDs1E1PortLineImpedanceOption_Object = MibTableColumn
wfDs1E1PortLineImpedanceOption = _WfDs1E1PortLineImpedanceOption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 20),
    _WfDs1E1PortLineImpedanceOption_Type()
)
wfDs1E1PortLineImpedanceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortLineImpedanceOption.setStatus("mandatory")


class _WfDs1E1PortFdlLoopInterframeFill_Type(Integer32):
    """Custom type wfDs1E1PortFdlLoopInterframeFill based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop-retention", 2),
          ("mark", 1))
    )


_WfDs1E1PortFdlLoopInterframeFill_Type.__name__ = "Integer32"
_WfDs1E1PortFdlLoopInterframeFill_Object = MibTableColumn
wfDs1E1PortFdlLoopInterframeFill = _WfDs1E1PortFdlLoopInterframeFill_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 21),
    _WfDs1E1PortFdlLoopInterframeFill_Type()
)
wfDs1E1PortFdlLoopInterframeFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortFdlLoopInterframeFill.setStatus("mandatory")


class _WfDs1E1PortRelayCtrl_Type(Integer32):
    """Custom type wfDs1E1PortRelayCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("no-loop", 2))
    )


_WfDs1E1PortRelayCtrl_Type.__name__ = "Integer32"
_WfDs1E1PortRelayCtrl_Object = MibTableColumn
wfDs1E1PortRelayCtrl = _WfDs1E1PortRelayCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 22),
    _WfDs1E1PortRelayCtrl_Type()
)
wfDs1E1PortRelayCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortRelayCtrl.setStatus("mandatory")


class _WfDs1E1PortRelayStatus_Type(Integer32):
    """Custom type wfDs1E1PortRelayStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("noLoop", 2))
    )


_WfDs1E1PortRelayStatus_Type.__name__ = "Integer32"
_WfDs1E1PortRelayStatus_Object = MibTableColumn
wfDs1E1PortRelayStatus = _WfDs1E1PortRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 23),
    _WfDs1E1PortRelayStatus_Type()
)
wfDs1E1PortRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortRelayStatus.setStatus("mandatory")


class _WfDs1E1PortPrimaryClockSource_Type(Integer32):
    """Custom type wfDs1E1PortPrimaryClockSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs1E1PortPrimaryClockSource_Type.__name__ = "Integer32"
_WfDs1E1PortPrimaryClockSource_Object = MibTableColumn
wfDs1E1PortPrimaryClockSource = _WfDs1E1PortPrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 24),
    _WfDs1E1PortPrimaryClockSource_Type()
)
wfDs1E1PortPrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortPrimaryClockSource.setStatus("mandatory")


class _WfDs1E1PortSecondaryClockSource_Type(Integer32):
    """Custom type wfDs1E1PortSecondaryClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs1E1PortSecondaryClockSource_Type.__name__ = "Integer32"
_WfDs1E1PortSecondaryClockSource_Object = MibTableColumn
wfDs1E1PortSecondaryClockSource = _WfDs1E1PortSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 25),
    _WfDs1E1PortSecondaryClockSource_Type()
)
wfDs1E1PortSecondaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortSecondaryClockSource.setStatus("mandatory")


class _WfDs1E1PortCurrentClock_Type(Integer32):
    """Custom type wfDs1E1PortCurrentClock based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs1E1PortCurrentClock_Type.__name__ = "Integer32"
_WfDs1E1PortCurrentClock_Object = MibTableColumn
wfDs1E1PortCurrentClock = _WfDs1E1PortCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 26),
    _WfDs1E1PortCurrentClock_Type()
)
wfDs1E1PortCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortCurrentClock.setStatus("mandatory")


class _WfDs1E1PortExtClockOperational_Type(Integer32):
    """Custom type wfDs1E1PortExtClockOperational based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1PortExtClockOperational_Type.__name__ = "Integer32"
_WfDs1E1PortExtClockOperational_Object = MibTableColumn
wfDs1E1PortExtClockOperational = _WfDs1E1PortExtClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 27),
    _WfDs1E1PortExtClockOperational_Type()
)
wfDs1E1PortExtClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1PortExtClockOperational.setStatus("mandatory")


class _WfDs1E1PortTransmitWaveform_Type(Integer32):
    """Custom type wfDs1E1PortTransmitWaveform based on Integer32"""
    defaultValue = 5

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
        *(("long-haul-0point0", 1),
          ("long-haul-15point0", 3),
          ("long-haul-22point5", 4),
          ("long-haul-7point5", 2),
          ("short-haul-0to110", 5),
          ("short-haul-110to220", 6),
          ("short-haul-220to330", 7),
          ("short-haul-330to440", 8),
          ("short-haul-440to550", 9),
          ("short-haul-550to660", 10))
    )


_WfDs1E1PortTransmitWaveform_Type.__name__ = "Integer32"
_WfDs1E1PortTransmitWaveform_Object = MibTableColumn
wfDs1E1PortTransmitWaveform = _WfDs1E1PortTransmitWaveform_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 3, 1, 28),
    _WfDs1E1PortTransmitWaveform_Type()
)
wfDs1E1PortTransmitWaveform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1PortTransmitWaveform.setStatus("mandatory")
_WfDs1E1ConfigTable_Object = MibTable
wfDs1E1ConfigTable = _WfDs1E1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4)
)
if mibBuilder.loadTexts:
    wfDs1E1ConfigTable.setStatus("mandatory")
_WfDs1E1ConfigEntry_Object = MibTableRow
wfDs1E1ConfigEntry = _WfDs1E1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1)
)
wfDs1E1ConfigEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ConfigPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1ConfigEntry.setStatus("mandatory")


class _WfDs1E1ConfigDelete_Type(Integer32):
    """Custom type wfDs1E1ConfigDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1ConfigDelete_Type.__name__ = "Integer32"
_WfDs1E1ConfigDelete_Object = MibTableColumn
wfDs1E1ConfigDelete = _WfDs1E1ConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 1),
    _WfDs1E1ConfigDelete_Type()
)
wfDs1E1ConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigDelete.setStatus("mandatory")
_WfDs1E1ConfigPortLineNumber_Type = Integer32
_WfDs1E1ConfigPortLineNumber_Object = MibTableColumn
wfDs1E1ConfigPortLineNumber = _WfDs1E1ConfigPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 2),
    _WfDs1E1ConfigPortLineNumber_Type()
)
wfDs1E1ConfigPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigPortLineNumber.setStatus("mandatory")
_WfDs1E1ConfigIfIndex_Type = Integer32
_WfDs1E1ConfigIfIndex_Object = MibTableColumn
wfDs1E1ConfigIfIndex = _WfDs1E1ConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 3),
    _WfDs1E1ConfigIfIndex_Type()
)
wfDs1E1ConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigIfIndex.setStatus("mandatory")
_WfDs1E1ConfigTimeElapsed_Type = Integer32
_WfDs1E1ConfigTimeElapsed_Object = MibTableColumn
wfDs1E1ConfigTimeElapsed = _WfDs1E1ConfigTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 4),
    _WfDs1E1ConfigTimeElapsed_Type()
)
wfDs1E1ConfigTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigTimeElapsed.setStatus("mandatory")
_WfDs1E1ConfigValidIntervals_Type = Integer32
_WfDs1E1ConfigValidIntervals_Object = MibTableColumn
wfDs1E1ConfigValidIntervals = _WfDs1E1ConfigValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 5),
    _WfDs1E1ConfigValidIntervals_Type()
)
wfDs1E1ConfigValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigValidIntervals.setStatus("mandatory")


class _WfDs1E1ConfigLineType_Type(Integer32):
    """Custom type wfDs1E1ConfigLineType based on Integer32"""
    defaultValue = 2

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
        *(("e1", 4),
          ("e1crc", 5),
          ("e1crcmf", 7),
          ("e1mf", 6),
          ("esf", 2),
          ("sf", 3),
          ("unframede1", 8),
          ("unframedt1", 1))
    )


_WfDs1E1ConfigLineType_Type.__name__ = "Integer32"
_WfDs1E1ConfigLineType_Object = MibTableColumn
wfDs1E1ConfigLineType = _WfDs1E1ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 6),
    _WfDs1E1ConfigLineType_Type()
)
wfDs1E1ConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigLineType.setStatus("mandatory")


class _WfDs1E1ConfigLineCoding_Type(Integer32):
    """Custom type wfDs1E1ConfigLineCoding based on Integer32"""
    defaultValue = 2

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
        *(("ami", 5),
          ("b8zs", 2),
          ("hdb3", 3),
          ("jbzs", 1),
          ("zbtsi", 4))
    )


_WfDs1E1ConfigLineCoding_Type.__name__ = "Integer32"
_WfDs1E1ConfigLineCoding_Object = MibTableColumn
wfDs1E1ConfigLineCoding = _WfDs1E1ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 7),
    _WfDs1E1ConfigLineCoding_Type()
)
wfDs1E1ConfigLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigLineCoding.setStatus("mandatory")


class _WfDs1E1ConfigSendCode_Type(Integer32):
    """Custom type wfDs1E1ConfigSendCode based on Integer32"""
    defaultValue = 1

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
        *(("send3in24pattern", 7),
          ("send511pattern", 6),
          ("sendlinecode", 2),
          ("sendnocode", 1),
          ("sendothertestpattern", 8),
          ("sendpayloadcode", 3),
          ("sendqrs", 5),
          ("sendresetcode", 4))
    )


_WfDs1E1ConfigSendCode_Type.__name__ = "Integer32"
_WfDs1E1ConfigSendCode_Object = MibTableColumn
wfDs1E1ConfigSendCode = _WfDs1E1ConfigSendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 8),
    _WfDs1E1ConfigSendCode_Type()
)
wfDs1E1ConfigSendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigSendCode.setStatus("mandatory")
_WfDs1E1ConfigCircuitIdentifier_Type = DisplayString
_WfDs1E1ConfigCircuitIdentifier_Object = MibTableColumn
wfDs1E1ConfigCircuitIdentifier = _WfDs1E1ConfigCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 9),
    _WfDs1E1ConfigCircuitIdentifier_Type()
)
wfDs1E1ConfigCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigCircuitIdentifier.setStatus("mandatory")


class _WfDs1E1ConfigLoopbackConfig_Type(Integer32):
    """Custom type wfDs1E1ConfigLoopbackConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("noloop", 1),
          ("payloadloop", 2))
    )


_WfDs1E1ConfigLoopbackConfig_Type.__name__ = "Integer32"
_WfDs1E1ConfigLoopbackConfig_Object = MibTableColumn
wfDs1E1ConfigLoopbackConfig = _WfDs1E1ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 10),
    _WfDs1E1ConfigLoopbackConfig_Type()
)
wfDs1E1ConfigLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigLoopbackConfig.setStatus("mandatory")


class _WfDs1E1ConfigLineStatus_Type(Integer32):
    """Custom type wfDs1E1ConfigLineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("loopbackstate", 128),
          ("lossofframe", 32),
          ("lossofsignal", 64),
          ("noalarm", 1),
          ("otherfailure", 4096),
          ("rcvais", 8),
          ("rcvfarendlof", 2),
          ("rcvfarendlomf", 512),
          ("rcvtestcode", 2048),
          ("t16ais", 256),
          ("xmtais", 16),
          ("xmtfarendlof", 4),
          ("xmtfarendlomf", 1024))
    )


_WfDs1E1ConfigLineStatus_Type.__name__ = "Integer32"
_WfDs1E1ConfigLineStatus_Object = MibTableColumn
wfDs1E1ConfigLineStatus = _WfDs1E1ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 11),
    _WfDs1E1ConfigLineStatus_Type()
)
wfDs1E1ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigLineStatus.setStatus("mandatory")


class _WfDs1E1ConfigSignalMode_Type(Integer32):
    """Custom type wfDs1E1ConfigSignalMode based on Integer32"""
    defaultValue = 1

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
        *(("bitoriented", 3),
          ("messageoriented", 4),
          ("none", 1),
          ("robbedbit", 2))
    )


_WfDs1E1ConfigSignalMode_Type.__name__ = "Integer32"
_WfDs1E1ConfigSignalMode_Object = MibTableColumn
wfDs1E1ConfigSignalMode = _WfDs1E1ConfigSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 12),
    _WfDs1E1ConfigSignalMode_Type()
)
wfDs1E1ConfigSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigSignalMode.setStatus("mandatory")


class _WfDs1E1ConfigTransmitClockSource_Type(Integer32):
    """Custom type wfDs1E1ConfigTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localtiming", 2),
          ("looptiming", 1),
          ("throughtiming", 3))
    )


_WfDs1E1ConfigTransmitClockSource_Type.__name__ = "Integer32"
_WfDs1E1ConfigTransmitClockSource_Object = MibTableColumn
wfDs1E1ConfigTransmitClockSource = _WfDs1E1ConfigTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 13),
    _WfDs1E1ConfigTransmitClockSource_Type()
)
wfDs1E1ConfigTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ConfigTransmitClockSource.setStatus("mandatory")


class _WfDs1E1ConfigFdl_Type(Integer32):
    """Custom type wfDs1E1ConfigFdl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ansi403", 2),
          ("att54016", 4),
          ("none", 8))
    )


_WfDs1E1ConfigFdl_Type.__name__ = "Integer32"
_WfDs1E1ConfigFdl_Object = MibTableColumn
wfDs1E1ConfigFdl = _WfDs1E1ConfigFdl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 4, 1, 14),
    _WfDs1E1ConfigFdl_Type()
)
wfDs1E1ConfigFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ConfigFdl.setStatus("mandatory")
_WfDs1E1ActionTable_Object = MibTable
wfDs1E1ActionTable = _WfDs1E1ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5)
)
if mibBuilder.loadTexts:
    wfDs1E1ActionTable.setStatus("mandatory")
_WfDs1E1ActionEntry_Object = MibTableRow
wfDs1E1ActionEntry = _WfDs1E1ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1)
)
wfDs1E1ActionEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ActionPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1ActionEntry.setStatus("mandatory")
_WfDs1E1ActionPortLineNumber_Type = Integer32
_WfDs1E1ActionPortLineNumber_Object = MibTableColumn
wfDs1E1ActionPortLineNumber = _WfDs1E1ActionPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 1),
    _WfDs1E1ActionPortLineNumber_Type()
)
wfDs1E1ActionPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ActionPortLineNumber.setStatus("mandatory")


class _WfDs1E1ActionBertReset_Type(Integer32):
    """Custom type wfDs1E1ActionBertReset based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 21),
          ("reset", 1))
    )


_WfDs1E1ActionBertReset_Type.__name__ = "Integer32"
_WfDs1E1ActionBertReset_Object = MibTableColumn
wfDs1E1ActionBertReset = _WfDs1E1ActionBertReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 2),
    _WfDs1E1ActionBertReset_Type()
)
wfDs1E1ActionBertReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionBertReset.setStatus("mandatory")


class _WfDs1E1ActionBertErrorInsert_Type(Integer32):
    """Custom type wfDs1E1ActionBertErrorInsert based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              21)
        )
    )
    namedValues = NamedValues(
        *(("disable", 4),
          ("errorpermillion", 3),
          ("errorperthousand", 2),
          ("noaction", 21),
          ("oneerror", 1))
    )


_WfDs1E1ActionBertErrorInsert_Type.__name__ = "Integer32"
_WfDs1E1ActionBertErrorInsert_Object = MibTableColumn
wfDs1E1ActionBertErrorInsert = _WfDs1E1ActionBertErrorInsert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 3),
    _WfDs1E1ActionBertErrorInsert_Type()
)
wfDs1E1ActionBertErrorInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionBertErrorInsert.setStatus("mandatory")


class _WfDs1E1ActionSendLoopCode_Type(Integer32):
    """Custom type wfDs1E1ActionSendLoopCode based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              21)
        )
    )
    namedValues = NamedValues(
        *(("loopdown", 2),
          ("loopup", 1),
          ("noaction", 21))
    )


_WfDs1E1ActionSendLoopCode_Type.__name__ = "Integer32"
_WfDs1E1ActionSendLoopCode_Object = MibTableColumn
wfDs1E1ActionSendLoopCode = _WfDs1E1ActionSendLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 4),
    _WfDs1E1ActionSendLoopCode_Type()
)
wfDs1E1ActionSendLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionSendLoopCode.setStatus("mandatory")


class _WfDs1E1ActionSendFdlLoopbackCode_Type(Integer32):
    """Custom type wfDs1E1ActionSendFdlLoopbackCode based on Integer32"""
    defaultValue = 21

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
              21)
        )
    )
    namedValues = NamedValues(
        *(("deactivateall", 7),
          ("deactivatell", 4),
          ("deactivatepl", 6),
          ("lineloopci", 1),
          ("lineloopia", 2),
          ("lineloopib", 3),
          ("noaction", 21),
          ("payloadloop", 5))
    )


_WfDs1E1ActionSendFdlLoopbackCode_Type.__name__ = "Integer32"
_WfDs1E1ActionSendFdlLoopbackCode_Object = MibTableColumn
wfDs1E1ActionSendFdlLoopbackCode = _WfDs1E1ActionSendFdlLoopbackCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 5),
    _WfDs1E1ActionSendFdlLoopbackCode_Type()
)
wfDs1E1ActionSendFdlLoopbackCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionSendFdlLoopbackCode.setStatus("mandatory")


class _WfDs1E1ActionSendLoopUpFractionalCode_Type(Integer32):
    """Custom type wfDs1E1ActionSendLoopUpFractionalCode based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            33
        )
    )
    namedValues = NamedValues(
        ("noaction", 33)
    )


_WfDs1E1ActionSendLoopUpFractionalCode_Type.__name__ = "Integer32"
_WfDs1E1ActionSendLoopUpFractionalCode_Object = MibTableColumn
wfDs1E1ActionSendLoopUpFractionalCode = _WfDs1E1ActionSendLoopUpFractionalCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 6),
    _WfDs1E1ActionSendLoopUpFractionalCode_Type()
)
wfDs1E1ActionSendLoopUpFractionalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionSendLoopUpFractionalCode.setStatus("mandatory")


class _WfDs1E1ActionSendLoopDownFractionalCode_Type(Integer32):
    """Custom type wfDs1E1ActionSendLoopDownFractionalCode based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            33
        )
    )
    namedValues = NamedValues(
        ("noaction", 33)
    )


_WfDs1E1ActionSendLoopDownFractionalCode_Type.__name__ = "Integer32"
_WfDs1E1ActionSendLoopDownFractionalCode_Object = MibTableColumn
wfDs1E1ActionSendLoopDownFractionalCode = _WfDs1E1ActionSendLoopDownFractionalCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 7),
    _WfDs1E1ActionSendLoopDownFractionalCode_Type()
)
wfDs1E1ActionSendLoopDownFractionalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionSendLoopDownFractionalCode.setStatus("mandatory")


class _WfDs1E1ActionClearFractionalLoopState_Type(Integer32):
    """Custom type wfDs1E1ActionClearFractionalLoopState based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            33
        )
    )
    namedValues = NamedValues(
        ("noaction", 33)
    )


_WfDs1E1ActionClearFractionalLoopState_Type.__name__ = "Integer32"
_WfDs1E1ActionClearFractionalLoopState_Object = MibTableColumn
wfDs1E1ActionClearFractionalLoopState = _WfDs1E1ActionClearFractionalLoopState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 8),
    _WfDs1E1ActionClearFractionalLoopState_Type()
)
wfDs1E1ActionClearFractionalLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearFractionalLoopState.setStatus("mandatory")


class _WfDs1E1ActionClearFdlStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearFdlStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearFdlStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearFdlStats_Object = MibTableColumn
wfDs1E1ActionClearFdlStats = _WfDs1E1ActionClearFdlStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 9),
    _WfDs1E1ActionClearFdlStats_Type()
)
wfDs1E1ActionClearFdlStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearFdlStats.setStatus("mandatory")


class _WfDs1E1ActionClearCurrentStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearCurrentStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearCurrentStats_Object = MibTableColumn
wfDs1E1ActionClearCurrentStats = _WfDs1E1ActionClearCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 10),
    _WfDs1E1ActionClearCurrentStats_Type()
)
wfDs1E1ActionClearCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearCurrentStats.setStatus("mandatory")


class _WfDs1E1ActionClearFarEndCurrentStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearFarEndCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearFarEndCurrentStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearFarEndCurrentStats_Object = MibTableColumn
wfDs1E1ActionClearFarEndCurrentStats = _WfDs1E1ActionClearFarEndCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 11),
    _WfDs1E1ActionClearFarEndCurrentStats_Type()
)
wfDs1E1ActionClearFarEndCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearFarEndCurrentStats.setStatus("mandatory")


class _WfDs1E1ActionClearDayCurrentStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearDayCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearDayCurrentStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearDayCurrentStats_Object = MibTableColumn
wfDs1E1ActionClearDayCurrentStats = _WfDs1E1ActionClearDayCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 12),
    _WfDs1E1ActionClearDayCurrentStats_Type()
)
wfDs1E1ActionClearDayCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearDayCurrentStats.setStatus("mandatory")


class _WfDs1E1ActionClearFarEndDayCurrentStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearFarEndDayCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearFarEndDayCurrentStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearFarEndDayCurrentStats_Object = MibTableColumn
wfDs1E1ActionClearFarEndDayCurrentStats = _WfDs1E1ActionClearFarEndDayCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 13),
    _WfDs1E1ActionClearFarEndDayCurrentStats_Type()
)
wfDs1E1ActionClearFarEndDayCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearFarEndDayCurrentStats.setStatus("mandatory")


class _WfDs1E1ActionClearIntervalStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearIntervalStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearIntervalStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearIntervalStats_Object = MibTableColumn
wfDs1E1ActionClearIntervalStats = _WfDs1E1ActionClearIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 14),
    _WfDs1E1ActionClearIntervalStats_Type()
)
wfDs1E1ActionClearIntervalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearIntervalStats.setStatus("mandatory")


class _WfDs1E1ActionClearFarEndIntervalStats_Type(Integer32):
    """Custom type wfDs1E1ActionClearFarEndIntervalStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs1E1ActionClearFarEndIntervalStats_Type.__name__ = "Integer32"
_WfDs1E1ActionClearFarEndIntervalStats_Object = MibTableColumn
wfDs1E1ActionClearFarEndIntervalStats = _WfDs1E1ActionClearFarEndIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 5, 1, 15),
    _WfDs1E1ActionClearFarEndIntervalStats_Type()
)
wfDs1E1ActionClearFarEndIntervalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ActionClearFarEndIntervalStats.setStatus("mandatory")
_WfLogicalLineTable_Object = MibTable
wfLogicalLineTable = _WfLogicalLineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6)
)
if mibBuilder.loadTexts:
    wfLogicalLineTable.setStatus("mandatory")
_WfLogicalLineEntry_Object = MibTableRow
wfLogicalLineEntry = _WfLogicalLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1)
)
wfLogicalLineEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfLogicalLinePortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfLogicalLineIndex"),
)
if mibBuilder.loadTexts:
    wfLogicalLineEntry.setStatus("mandatory")


class _WfLogicalLineDelete_Type(Integer32):
    """Custom type wfLogicalLineDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfLogicalLineDelete_Type.__name__ = "Integer32"
_WfLogicalLineDelete_Object = MibTableColumn
wfLogicalLineDelete = _WfLogicalLineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 1),
    _WfLogicalLineDelete_Type()
)
wfLogicalLineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineDelete.setStatus("mandatory")


class _WfLogicalLineDisable_Type(Integer32):
    """Custom type wfLogicalLineDisable based on Integer32"""
    defaultValue = 1

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


_WfLogicalLineDisable_Type.__name__ = "Integer32"
_WfLogicalLineDisable_Object = MibTableColumn
wfLogicalLineDisable = _WfLogicalLineDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 2),
    _WfLogicalLineDisable_Type()
)
wfLogicalLineDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineDisable.setStatus("mandatory")


class _WfLogicalLineState_Type(Integer32):
    """Custom type wfLogicalLineState based on Integer32"""
    defaultValue = 20

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
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("bert", 10),
          ("down", 2),
          ("hwfrac", 11),
          ("init", 3),
          ("linedead", 7),
          ("linedieing", 6),
          ("lineloopbofltest", 19),
          ("lmiwait", 4),
          ("loopback", 5),
          ("notpresent", 20),
          ("priWait", 12),
          ("remotedeaf", 9),
          ("remoteloop", 8),
          ("up", 1))
    )


_WfLogicalLineState_Type.__name__ = "Integer32"
_WfLogicalLineState_Object = MibTableColumn
wfLogicalLineState = _WfLogicalLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 3),
    _WfLogicalLineState_Type()
)
wfLogicalLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineState.setStatus("mandatory")
_WfLogicalLinePortLineNumber_Type = Integer32
_WfLogicalLinePortLineNumber_Object = MibTableColumn
wfLogicalLinePortLineNumber = _WfLogicalLinePortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 4),
    _WfLogicalLinePortLineNumber_Type()
)
wfLogicalLinePortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLinePortLineNumber.setStatus("mandatory")
_WfLogicalLineIndex_Type = Integer32
_WfLogicalLineIndex_Object = MibTableColumn
wfLogicalLineIndex = _WfLogicalLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 5),
    _WfLogicalLineIndex_Type()
)
wfLogicalLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineIndex.setStatus("mandatory")
_WfLogicalLineCct_Type = Integer32
_WfLogicalLineCct_Object = MibTableColumn
wfLogicalLineCct = _WfLogicalLineCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 6),
    _WfLogicalLineCct_Type()
)
wfLogicalLineCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineCct.setStatus("mandatory")
_WfLogicalLineLineNumber_Type = Integer32
_WfLogicalLineLineNumber_Object = MibTableColumn
wfLogicalLineLineNumber = _WfLogicalLineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 7),
    _WfLogicalLineLineNumber_Type()
)
wfLogicalLineLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineLineNumber.setStatus("mandatory")


class _WfLogicalLineBofl_Type(Integer32):
    """Custom type wfLogicalLineBofl based on Integer32"""
    defaultValue = 1

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


_WfLogicalLineBofl_Type.__name__ = "Integer32"
_WfLogicalLineBofl_Object = MibTableColumn
wfLogicalLineBofl = _WfLogicalLineBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 8),
    _WfLogicalLineBofl_Type()
)
wfLogicalLineBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBofl.setStatus("mandatory")


class _WfLogicalLineBoflTmo_Type(Integer32):
    """Custom type wfLogicalLineBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfLogicalLineBoflTmo_Type.__name__ = "Integer32"
_WfLogicalLineBoflTmo_Object = MibTableColumn
wfLogicalLineBoflTmo = _WfLogicalLineBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 9),
    _WfLogicalLineBoflTmo_Type()
)
wfLogicalLineBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBoflTmo.setStatus("mandatory")


class _WfLogicalLineFractionalLoopback_Type(Integer32):
    """Custom type wfLogicalLineFractionalLoopback based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineFractionalLoopback_Type.__name__ = "Integer32"
_WfLogicalLineFractionalLoopback_Object = MibTableColumn
wfLogicalLineFractionalLoopback = _WfLogicalLineFractionalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 10),
    _WfLogicalLineFractionalLoopback_Type()
)
wfLogicalLineFractionalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineFractionalLoopback.setStatus("mandatory")
_WfLogicalLineTimeSlotAssignment_Type = DisplayString
_WfLogicalLineTimeSlotAssignment_Object = MibTableColumn
wfLogicalLineTimeSlotAssignment = _WfLogicalLineTimeSlotAssignment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 11),
    _WfLogicalLineTimeSlotAssignment_Type()
)
wfLogicalLineTimeSlotAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTimeSlotAssignment.setStatus("mandatory")
_WfLogicalLineMtu_Type = Integer32
_WfLogicalLineMtu_Object = MibTableColumn
wfLogicalLineMtu = _WfLogicalLineMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 12),
    _WfLogicalLineMtu_Type()
)
wfLogicalLineMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineMtu.setStatus("mandatory")
_WfLogicalLineMadr_Type = OctetString
_WfLogicalLineMadr_Object = MibTableColumn
wfLogicalLineMadr = _WfLogicalLineMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 13),
    _WfLogicalLineMadr_Type()
)
wfLogicalLineMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineMadr.setStatus("mandatory")


class _WfLogicalLineWanProtocol_Type(Integer32):
    """Custom type wfLogicalLineWanProtocol based on Integer32"""
    defaultValue = 1

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("framerelay", 5),
          ("lapb", 10),
          ("passthru", 2),
          ("ppp", 3),
          ("sdlc", 11),
          ("smds", 4),
          ("standard", 1),
          ("sw", 8),
          ("switch", 7),
          ("x25", 6))
    )


_WfLogicalLineWanProtocol_Type.__name__ = "Integer32"
_WfLogicalLineWanProtocol_Object = MibTableColumn
wfLogicalLineWanProtocol = _WfLogicalLineWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 14),
    _WfLogicalLineWanProtocol_Type()
)
wfLogicalLineWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineWanProtocol.setStatus("mandatory")


class _WfLogicalLineHdlcService_Type(Integer32):
    """Custom type wfLogicalLineHdlcService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc1", 2),
          ("transparent", 1))
    )


_WfLogicalLineHdlcService_Type.__name__ = "Integer32"
_WfLogicalLineHdlcService_Object = MibTableColumn
wfLogicalLineHdlcService = _WfLogicalLineHdlcService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 15),
    _WfLogicalLineHdlcService_Type()
)
wfLogicalLineHdlcService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineHdlcService.setStatus("mandatory")


class _WfLogicalLineLocalHdlcAddress_Type(Integer32):
    """Custom type wfLogicalLineLocalHdlcAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 3),
          ("seven", 7))
    )


_WfLogicalLineLocalHdlcAddress_Type.__name__ = "Integer32"
_WfLogicalLineLocalHdlcAddress_Object = MibTableColumn
wfLogicalLineLocalHdlcAddress = _WfLogicalLineLocalHdlcAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 16),
    _WfLogicalLineLocalHdlcAddress_Type()
)
wfLogicalLineLocalHdlcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineLocalHdlcAddress.setStatus("mandatory")


class _WfLogicalLineRemoteHdlcAddress_Type(Integer32):
    """Custom type wfLogicalLineRemoteHdlcAddress based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 3),
          ("seven", 7))
    )


_WfLogicalLineRemoteHdlcAddress_Type.__name__ = "Integer32"
_WfLogicalLineRemoteHdlcAddress_Object = MibTableColumn
wfLogicalLineRemoteHdlcAddress = _WfLogicalLineRemoteHdlcAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 17),
    _WfLogicalLineRemoteHdlcAddress_Type()
)
wfLogicalLineRemoteHdlcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineRemoteHdlcAddress.setStatus("mandatory")


class _WfLogicalLineRateAdaption_Type(Integer32):
    """Custom type wfLogicalLineRateAdaption based on Integer32"""
    defaultValue = 3

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
        *(("adaption-19dot2k", 5),
          ("adaption-56klsb", 3),
          ("adaption-56kmsb", 2),
          ("adaption-64k", 1),
          ("adaption-9dot6k", 4))
    )


_WfLogicalLineRateAdaption_Type.__name__ = "Integer32"
_WfLogicalLineRateAdaption_Object = MibTableColumn
wfLogicalLineRateAdaption = _WfLogicalLineRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 18),
    _WfLogicalLineRateAdaption_Type()
)
wfLogicalLineRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineRateAdaption.setStatus("mandatory")


class _WfLogicalLineIFTF_Type(Integer32):
    """Custom type wfLogicalLineIFTF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flags", 1),
          ("idles", 2))
    )


_WfLogicalLineIFTF_Type.__name__ = "Integer32"
_WfLogicalLineIFTF_Object = MibTableColumn
wfLogicalLineIFTF = _WfLogicalLineIFTF_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 19),
    _WfLogicalLineIFTF_Type()
)
wfLogicalLineIFTF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineIFTF.setStatus("mandatory")


class _WfLogicalLineCRCSize_Type(Integer32):
    """Custom type wfLogicalLineCRCSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc-16", 2),
          ("crc-32", 1))
    )


_WfLogicalLineCRCSize_Type.__name__ = "Integer32"
_WfLogicalLineCRCSize_Object = MibTableColumn
wfLogicalLineCRCSize = _WfLogicalLineCRCSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 20),
    _WfLogicalLineCRCSize_Type()
)
wfLogicalLineCRCSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineCRCSize.setStatus("mandatory")
_WfLogicalLineRxOctets_Type = Counter32
_WfLogicalLineRxOctets_Object = MibTableColumn
wfLogicalLineRxOctets = _WfLogicalLineRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 21),
    _WfLogicalLineRxOctets_Type()
)
wfLogicalLineRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxOctets.setStatus("mandatory")
_WfLogicalLineRxFrames_Type = Counter32
_WfLogicalLineRxFrames_Object = MibTableColumn
wfLogicalLineRxFrames = _WfLogicalLineRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 22),
    _WfLogicalLineRxFrames_Type()
)
wfLogicalLineRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxFrames.setStatus("mandatory")
_WfLogicalLineTxOctets_Type = Counter32
_WfLogicalLineTxOctets_Object = MibTableColumn
wfLogicalLineTxOctets = _WfLogicalLineTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 23),
    _WfLogicalLineTxOctets_Type()
)
wfLogicalLineTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxOctets.setStatus("mandatory")
_WfLogicalLineTxFrames_Type = Counter32
_WfLogicalLineTxFrames_Object = MibTableColumn
wfLogicalLineTxFrames = _WfLogicalLineTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 24),
    _WfLogicalLineTxFrames_Type()
)
wfLogicalLineTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxFrames.setStatus("mandatory")
_WfLogicalLineRxErrors_Type = Counter32
_WfLogicalLineRxErrors_Object = MibTableColumn
wfLogicalLineRxErrors = _WfLogicalLineRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 25),
    _WfLogicalLineRxErrors_Type()
)
wfLogicalLineRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxErrors.setStatus("mandatory")
_WfLogicalLineTxErrors_Type = Counter32
_WfLogicalLineTxErrors_Object = MibTableColumn
wfLogicalLineTxErrors = _WfLogicalLineTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 26),
    _WfLogicalLineTxErrors_Type()
)
wfLogicalLineTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxErrors.setStatus("mandatory")
_WfLogicalLineLackRxResources_Type = Counter32
_WfLogicalLineLackRxResources_Object = MibTableColumn
wfLogicalLineLackRxResources = _WfLogicalLineLackRxResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 27),
    _WfLogicalLineLackRxResources_Type()
)
wfLogicalLineLackRxResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineLackRxResources.setStatus("mandatory")
_WfLogicalLineLackTxResources_Type = Counter32
_WfLogicalLineLackTxResources_Object = MibTableColumn
wfLogicalLineLackTxResources = _WfLogicalLineLackTxResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 28),
    _WfLogicalLineLackTxResources_Type()
)
wfLogicalLineLackTxResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineLackTxResources.setStatus("mandatory")
_WfLogicalLineTxUnderflows_Type = Counter32
_WfLogicalLineTxUnderflows_Object = MibTableColumn
wfLogicalLineTxUnderflows = _WfLogicalLineTxUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 29),
    _WfLogicalLineTxUnderflows_Type()
)
wfLogicalLineTxUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxUnderflows.setStatus("mandatory")
_WfLogicalLineRxOverflows_Type = Counter32
_WfLogicalLineRxOverflows_Object = MibTableColumn
wfLogicalLineRxOverflows = _WfLogicalLineRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 30),
    _WfLogicalLineRxOverflows_Type()
)
wfLogicalLineRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxOverflows.setStatus("mandatory")
_WfLogicalLineRxNullFrames_Type = Counter32
_WfLogicalLineRxNullFrames_Object = MibTableColumn
wfLogicalLineRxNullFrames = _WfLogicalLineRxNullFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 31),
    _WfLogicalLineRxNullFrames_Type()
)
wfLogicalLineRxNullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxNullFrames.setStatus("mandatory")
_WfLogicalLineRxShortFrames_Type = Counter32
_WfLogicalLineRxShortFrames_Object = MibTableColumn
wfLogicalLineRxShortFrames = _WfLogicalLineRxShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 32),
    _WfLogicalLineRxShortFrames_Type()
)
wfLogicalLineRxShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxShortFrames.setStatus("mandatory")
_WfLogicalLineRxLossSyncs_Type = Counter32
_WfLogicalLineRxLossSyncs_Object = MibTableColumn
wfLogicalLineRxLossSyncs = _WfLogicalLineRxLossSyncs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 33),
    _WfLogicalLineRxLossSyncs_Type()
)
wfLogicalLineRxLossSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxLossSyncs.setStatus("mandatory")
_WfLogicalLineRxCRCErrors_Type = Counter32
_WfLogicalLineRxCRCErrors_Object = MibTableColumn
wfLogicalLineRxCRCErrors = _WfLogicalLineRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 34),
    _WfLogicalLineRxCRCErrors_Type()
)
wfLogicalLineRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxCRCErrors.setStatus("mandatory")
_WfLogicalLineRxNonOctetBits_Type = Counter32
_WfLogicalLineRxNonOctetBits_Object = MibTableColumn
wfLogicalLineRxNonOctetBits = _WfLogicalLineRxNonOctetBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 35),
    _WfLogicalLineRxNonOctetBits_Type()
)
wfLogicalLineRxNonOctetBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxNonOctetBits.setStatus("mandatory")
_WfLogicalLineRxLongFrames_Type = Counter32
_WfLogicalLineRxLongFrames_Object = MibTableColumn
wfLogicalLineRxLongFrames = _WfLogicalLineRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 36),
    _WfLogicalLineRxLongFrames_Type()
)
wfLogicalLineRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxLongFrames.setStatus("mandatory")
_WfLogicalLineRxAbortFrames_Type = Counter32
_WfLogicalLineRxAbortFrames_Object = MibTableColumn
wfLogicalLineRxAbortFrames = _WfLogicalLineRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 37),
    _WfLogicalLineRxAbortFrames_Type()
)
wfLogicalLineRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxAbortFrames.setStatus("mandatory")
_WfLogicalLineRxDescOverflows_Type = Counter32
_WfLogicalLineRxDescOverflows_Object = MibTableColumn
wfLogicalLineRxDescOverflows = _WfLogicalLineRxDescOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 38),
    _WfLogicalLineRxDescOverflows_Type()
)
wfLogicalLineRxDescOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxDescOverflows.setStatus("mandatory")
_WfLogicalLineRxReplenMisses_Type = Counter32
_WfLogicalLineRxReplenMisses_Object = MibTableColumn
wfLogicalLineRxReplenMisses = _WfLogicalLineRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 39),
    _WfLogicalLineRxReplenMisses_Type()
)
wfLogicalLineRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxReplenMisses.setStatus("mandatory")
_WfLogicalLineRxIFCs_Type = Counter32
_WfLogicalLineRxIFCs_Object = MibTableColumn
wfLogicalLineRxIFCs = _WfLogicalLineRxIFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 40),
    _WfLogicalLineRxIFCs_Type()
)
wfLogicalLineRxIFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxIFCs.setStatus("mandatory")
_WfLogicalLineRxDropPackets_Type = Counter32
_WfLogicalLineRxDropPackets_Object = MibTableColumn
wfLogicalLineRxDropPackets = _WfLogicalLineRxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 41),
    _WfLogicalLineRxDropPackets_Type()
)
wfLogicalLineRxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxDropPackets.setStatus("mandatory")


class _WfLogicalLineCfgTxQueueLength_Type(Integer32):
    """Custom type wfLogicalLineCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WfLogicalLineCfgTxQueueLength_Type.__name__ = "Integer32"
_WfLogicalLineCfgTxQueueLength_Object = MibTableColumn
wfLogicalLineCfgTxQueueLength = _WfLogicalLineCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 42),
    _WfLogicalLineCfgTxQueueLength_Type()
)
wfLogicalLineCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineCfgTxQueueLength.setStatus("mandatory")


class _WfLogicalLineCfgRxQueueLength_Type(Integer32):
    """Custom type wfLogicalLineCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WfLogicalLineCfgRxQueueLength_Type.__name__ = "Integer32"
_WfLogicalLineCfgRxQueueLength_Object = MibTableColumn
wfLogicalLineCfgRxQueueLength = _WfLogicalLineCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 43),
    _WfLogicalLineCfgRxQueueLength_Type()
)
wfLogicalLineCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineCfgRxQueueLength.setStatus("mandatory")
_WfLogicalLineTxQueueLength_Type = Integer32
_WfLogicalLineTxQueueLength_Object = MibTableColumn
wfLogicalLineTxQueueLength = _WfLogicalLineTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 44),
    _WfLogicalLineTxQueueLength_Type()
)
wfLogicalLineTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxQueueLength.setStatus("mandatory")
_WfLogicalLineRxQueueLength_Type = Integer32
_WfLogicalLineRxQueueLength_Object = MibTableColumn
wfLogicalLineRxQueueLength = _WfLogicalLineRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 45),
    _WfLogicalLineRxQueueLength_Type()
)
wfLogicalLineRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxQueueLength.setStatus("mandatory")
_WfLogicalLineTxQueueEmpties_Type = Counter32
_WfLogicalLineTxQueueEmpties_Object = MibTableColumn
wfLogicalLineTxQueueEmpties = _WfLogicalLineTxQueueEmpties_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 46),
    _WfLogicalLineTxQueueEmpties_Type()
)
wfLogicalLineTxQueueEmpties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxQueueEmpties.setStatus("mandatory")
_WfLogicalLineRxIntProcs_Type = Counter32
_WfLogicalLineRxIntProcs_Object = MibTableColumn
wfLogicalLineRxIntProcs = _WfLogicalLineRxIntProcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 47),
    _WfLogicalLineRxIntProcs_Type()
)
wfLogicalLineRxIntProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxIntProcs.setStatus("mandatory")
_WfLogicalLineTxIntProcs_Type = Counter32
_WfLogicalLineTxIntProcs_Object = MibTableColumn
wfLogicalLineTxIntProcs = _WfLogicalLineTxIntProcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 48),
    _WfLogicalLineTxIntProcs_Type()
)
wfLogicalLineTxIntProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineTxIntProcs.setStatus("mandatory")
_WfLogicalLineRxPktCorruptions_Type = Counter32
_WfLogicalLineRxPktCorruptions_Object = MibTableColumn
wfLogicalLineRxPktCorruptions = _WfLogicalLineRxPktCorruptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 49),
    _WfLogicalLineRxPktCorruptions_Type()
)
wfLogicalLineRxPktCorruptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxPktCorruptions.setStatus("mandatory")


class _WfLogicalLineTurboBofl_Type(Integer32):
    """Custom type wfLogicalLineTurboBofl based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineTurboBofl_Type.__name__ = "Integer32"
_WfLogicalLineTurboBofl_Object = MibTableColumn
wfLogicalLineTurboBofl = _WfLogicalLineTurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 50),
    _WfLogicalLineTurboBofl_Type()
)
wfLogicalLineTurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineTurboBofl.setStatus("mandatory")


class _WfLogicalLineBoflNum_Type(Integer32):
    """Custom type wfLogicalLineBoflNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfLogicalLineBoflNum_Type.__name__ = "Integer32"
_WfLogicalLineBoflNum_Object = MibTableColumn
wfLogicalLineBoflNum = _WfLogicalLineBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 51),
    _WfLogicalLineBoflNum_Type()
)
wfLogicalLineBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBoflNum.setStatus("mandatory")


class _WfLogicalLineBoflLen_Type(Integer32):
    """Custom type wfLogicalLineBoflLen based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 4450),
    )


_WfLogicalLineBoflLen_Type.__name__ = "Integer32"
_WfLogicalLineBoflLen_Object = MibTableColumn
wfLogicalLineBoflLen = _WfLogicalLineBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 52),
    _WfLogicalLineBoflLen_Type()
)
wfLogicalLineBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBoflLen.setStatus("mandatory")
_WfLogicalLineOutQLen_Type = Gauge32
_WfLogicalLineOutQLen_Object = MibTableColumn
wfLogicalLineOutQLen = _WfLogicalLineOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 53),
    _WfLogicalLineOutQLen_Type()
)
wfLogicalLineOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineOutQLen.setStatus("mandatory")
_WfLogicalLineLastChange_Type = TimeTicks
_WfLogicalLineLastChange_Object = MibTableColumn
wfLogicalLineLastChange = _WfLogicalLineLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 54),
    _WfLogicalLineLastChange_Type()
)
wfLogicalLineLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineLastChange.setStatus("mandatory")


class _WfLogicalLineCfgMtu_Type(Integer32):
    """Custom type wfLogicalLineCfgMtu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfLogicalLineCfgMtu_Type.__name__ = "Integer32"
_WfLogicalLineCfgMtu_Object = MibTableColumn
wfLogicalLineCfgMtu = _WfLogicalLineCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 55),
    _WfLogicalLineCfgMtu_Type()
)
wfLogicalLineCfgMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineCfgMtu.setStatus("mandatory")


class _WfLogicalLineRemoteLpbkDetection_Type(Integer32):
    """Custom type wfLogicalLineRemoteLpbkDetection based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineRemoteLpbkDetection_Type.__name__ = "Integer32"
_WfLogicalLineRemoteLpbkDetection_Object = MibTableColumn
wfLogicalLineRemoteLpbkDetection = _WfLogicalLineRemoteLpbkDetection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 56),
    _WfLogicalLineRemoteLpbkDetection_Type()
)
wfLogicalLineRemoteLpbkDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineRemoteLpbkDetection.setStatus("mandatory")


class _WfLogicalLineLastState_Type(Integer32):
    """Custom type wfLogicalLineLastState based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("bert", 10),
          ("down", 2),
          ("hwfrac", 11),
          ("init", 3),
          ("linedead", 7),
          ("linedieing", 6),
          ("lmiwait", 4),
          ("loopback", 5),
          ("notpresent", 20),
          ("priWait", 12),
          ("remotedeaf", 9),
          ("remoteloop", 8),
          ("up", 1))
    )


_WfLogicalLineLastState_Type.__name__ = "Integer32"
_WfLogicalLineLastState_Object = MibTableColumn
wfLogicalLineLastState = _WfLogicalLineLastState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 57),
    _WfLogicalLineLastState_Type()
)
wfLogicalLineLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineLastState.setStatus("mandatory")
_WfLogicalLineRxIdles_Type = Counter32
_WfLogicalLineRxIdles_Object = MibTableColumn
wfLogicalLineRxIdles = _WfLogicalLineRxIdles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 58),
    _WfLogicalLineRxIdles_Type()
)
wfLogicalLineRxIdles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineRxIdles.setStatus("mandatory")


class _WfLogicalLineRole_Type(Integer32):
    """Custom type wfLogicalLineRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bchannel", 3),
          ("dchannel", 2),
          ("syncconnect", 1))
    )


_WfLogicalLineRole_Type.__name__ = "Integer32"
_WfLogicalLineRole_Object = MibTableColumn
wfLogicalLineRole = _WfLogicalLineRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 59),
    _WfLogicalLineRole_Type()
)
wfLogicalLineRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineRole.setStatus("mandatory")
_WfLogicalLineActiveCct_Type = Integer32
_WfLogicalLineActiveCct_Object = MibTableColumn
wfLogicalLineActiveCct = _WfLogicalLineActiveCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 60),
    _WfLogicalLineActiveCct_Type()
)
wfLogicalLineActiveCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineActiveCct.setStatus("mandatory")


class _WfLogicalLineActualRateAdaption_Type(Integer32):
    """Custom type wfLogicalLineActualRateAdaption based on Integer32"""
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
        *(("adaption19dot2k", 5),
          ("adaption56klsb", 3),
          ("adaption56kmsb", 2),
          ("adaption64k", 1),
          ("adaption9dot6k", 4))
    )


_WfLogicalLineActualRateAdaption_Type.__name__ = "Integer32"
_WfLogicalLineActualRateAdaption_Object = MibTableColumn
wfLogicalLineActualRateAdaption = _WfLogicalLineActualRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 61),
    _WfLogicalLineActualRateAdaption_Type()
)
wfLogicalLineActualRateAdaption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineActualRateAdaption.setStatus("mandatory")


class _WfLogicalLineBertMode_Type(Integer32):
    """Custom type wfLogicalLineBertMode based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineBertMode_Type.__name__ = "Integer32"
_WfLogicalLineBertMode_Object = MibTableColumn
wfLogicalLineBertMode = _WfLogicalLineBertMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 62),
    _WfLogicalLineBertMode_Type()
)
wfLogicalLineBertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBertMode.setStatus("mandatory")


class _WfLogicalLineBertTestPattern_Type(Integer32):
    """Custom type wfLogicalLineBertTestPattern based on Integer32"""
    defaultValue = 2

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
        *(("ones", 2),
          ("qrss", 3),
          ("two15", 4),
          ("two15-inv", 5),
          ("two20", 6),
          ("two23", 7),
          ("two23-inv", 8),
          ("zeros", 1))
    )


_WfLogicalLineBertTestPattern_Type.__name__ = "Integer32"
_WfLogicalLineBertTestPattern_Object = MibTableColumn
wfLogicalLineBertTestPattern = _WfLogicalLineBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 63),
    _WfLogicalLineBertTestPattern_Type()
)
wfLogicalLineBertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineBertTestPattern.setStatus("mandatory")


class _WfLogicalLineAcceptFracLoopCode_Type(Integer32):
    """Custom type wfLogicalLineAcceptFracLoopCode based on Integer32"""
    defaultValue = 1

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


_WfLogicalLineAcceptFracLoopCode_Type.__name__ = "Integer32"
_WfLogicalLineAcceptFracLoopCode_Object = MibTableColumn
wfLogicalLineAcceptFracLoopCode = _WfLogicalLineAcceptFracLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 64),
    _WfLogicalLineAcceptFracLoopCode_Type()
)
wfLogicalLineAcceptFracLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineAcceptFracLoopCode.setStatus("mandatory")


class _WfLogicalLineDS0AStatus_Type(Integer32):
    """Custom type wfLogicalLineDS0AStatus based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineDS0AStatus_Type.__name__ = "Integer32"
_WfLogicalLineDS0AStatus_Object = MibTableColumn
wfLogicalLineDS0AStatus = _WfLogicalLineDS0AStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 65),
    _WfLogicalLineDS0AStatus_Type()
)
wfLogicalLineDS0AStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfLogicalLineDS0AStatus.setStatus("mandatory")


class _WfLogicalLineNRZIEnable_Type(Integer32):
    """Custom type wfLogicalLineNRZIEnable based on Integer32"""
    defaultValue = 2

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


_WfLogicalLineNRZIEnable_Type.__name__ = "Integer32"
_WfLogicalLineNRZIEnable_Object = MibTableColumn
wfLogicalLineNRZIEnable = _WfLogicalLineNRZIEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 66),
    _WfLogicalLineNRZIEnable_Type()
)
wfLogicalLineNRZIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineNRZIEnable.setStatus("mandatory")


class _WfLogicalLineNRZIType_Type(Integer32):
    """Custom type wfLogicalLineNRZIType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mark", 2),
          ("space", 1))
    )


_WfLogicalLineNRZIType_Type.__name__ = "Integer32"
_WfLogicalLineNRZIType_Object = MibTableColumn
wfLogicalLineNRZIType = _WfLogicalLineNRZIType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 6, 1, 67),
    _WfLogicalLineNRZIType_Type()
)
wfLogicalLineNRZIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLogicalLineNRZIType.setStatus("mandatory")
_WfDs1E1FracTable_Object = MibTable
wfDs1E1FracTable = _WfDs1E1FracTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7)
)
if mibBuilder.loadTexts:
    wfDs1E1FracTable.setStatus("mandatory")
_WfDs1E1FracEntry_Object = MibTableRow
wfDs1E1FracEntry = _WfDs1E1FracEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1)
)
wfDs1E1FracEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FracPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FracNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FracEntry.setStatus("mandatory")


class _WfDs1E1FracDelete_Type(Integer32):
    """Custom type wfDs1E1FracDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1FracDelete_Type.__name__ = "Integer32"
_WfDs1E1FracDelete_Object = MibTableColumn
wfDs1E1FracDelete = _WfDs1E1FracDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1, 1),
    _WfDs1E1FracDelete_Type()
)
wfDs1E1FracDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FracDelete.setStatus("mandatory")
_WfDs1E1FracPortLineNumber_Type = Integer32
_WfDs1E1FracPortLineNumber_Object = MibTableColumn
wfDs1E1FracPortLineNumber = _WfDs1E1FracPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1, 2),
    _WfDs1E1FracPortLineNumber_Type()
)
wfDs1E1FracPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FracPortLineNumber.setStatus("mandatory")
_WfDs1E1FracNumber_Type = Integer32
_WfDs1E1FracNumber_Object = MibTableColumn
wfDs1E1FracNumber = _WfDs1E1FracNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1, 3),
    _WfDs1E1FracNumber_Type()
)
wfDs1E1FracNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FracNumber.setStatus("mandatory")
_WfDs1E1FracLogicalLineIndex_Type = Integer32
_WfDs1E1FracLogicalLineIndex_Object = MibTableColumn
wfDs1E1FracLogicalLineIndex = _WfDs1E1FracLogicalLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1, 4),
    _WfDs1E1FracLogicalLineIndex_Type()
)
wfDs1E1FracLogicalLineIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FracLogicalLineIndex.setStatus("mandatory")
_WfDs1E1FracActualLogicalLineIndex_Type = Integer32
_WfDs1E1FracActualLogicalLineIndex_Object = MibTableColumn
wfDs1E1FracActualLogicalLineIndex = _WfDs1E1FracActualLogicalLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 7, 1, 5),
    _WfDs1E1FracActualLogicalLineIndex_Type()
)
wfDs1E1FracActualLogicalLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FracActualLogicalLineIndex.setStatus("mandatory")
_WfDs1E1CurrentTable_Object = MibTable
wfDs1E1CurrentTable = _WfDs1E1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10)
)
if mibBuilder.loadTexts:
    wfDs1E1CurrentTable.setStatus("mandatory")
_WfDs1E1CurrentEntry_Object = MibTableRow
wfDs1E1CurrentEntry = _WfDs1E1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1)
)
wfDs1E1CurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1CurrentPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1CurrentEntry.setStatus("mandatory")
_WfDs1E1CurrentPortLineNumber_Type = Integer32
_WfDs1E1CurrentPortLineNumber_Object = MibTableColumn
wfDs1E1CurrentPortLineNumber = _WfDs1E1CurrentPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 1),
    _WfDs1E1CurrentPortLineNumber_Type()
)
wfDs1E1CurrentPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentPortLineNumber.setStatus("mandatory")
_WfDs1E1CurrentESs_Type = Gauge32
_WfDs1E1CurrentESs_Object = MibTableColumn
wfDs1E1CurrentESs = _WfDs1E1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 2),
    _WfDs1E1CurrentESs_Type()
)
wfDs1E1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentESs.setStatus("mandatory")
_WfDs1E1CurrentSESs_Type = Gauge32
_WfDs1E1CurrentSESs_Object = MibTableColumn
wfDs1E1CurrentSESs = _WfDs1E1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 3),
    _WfDs1E1CurrentSESs_Type()
)
wfDs1E1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentSESs.setStatus("mandatory")
_WfDs1E1CurrentSEFSs_Type = Gauge32
_WfDs1E1CurrentSEFSs_Object = MibTableColumn
wfDs1E1CurrentSEFSs = _WfDs1E1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 4),
    _WfDs1E1CurrentSEFSs_Type()
)
wfDs1E1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentSEFSs.setStatus("mandatory")
_WfDs1E1CurrentUASs_Type = Gauge32
_WfDs1E1CurrentUASs_Object = MibTableColumn
wfDs1E1CurrentUASs = _WfDs1E1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 5),
    _WfDs1E1CurrentUASs_Type()
)
wfDs1E1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentUASs.setStatus("mandatory")
_WfDs1E1CurrentCSSs_Type = Gauge32
_WfDs1E1CurrentCSSs_Object = MibTableColumn
wfDs1E1CurrentCSSs = _WfDs1E1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 6),
    _WfDs1E1CurrentCSSs_Type()
)
wfDs1E1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentCSSs.setStatus("mandatory")
_WfDs1E1CurrentPCVs_Type = Gauge32
_WfDs1E1CurrentPCVs_Object = MibTableColumn
wfDs1E1CurrentPCVs = _WfDs1E1CurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 7),
    _WfDs1E1CurrentPCVs_Type()
)
wfDs1E1CurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentPCVs.setStatus("mandatory")
_WfDs1E1CurrentLESs_Type = Gauge32
_WfDs1E1CurrentLESs_Object = MibTableColumn
wfDs1E1CurrentLESs = _WfDs1E1CurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 8),
    _WfDs1E1CurrentLESs_Type()
)
wfDs1E1CurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentLESs.setStatus("mandatory")
_WfDs1E1CurrentBESs_Type = Gauge32
_WfDs1E1CurrentBESs_Object = MibTableColumn
wfDs1E1CurrentBESs = _WfDs1E1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 9),
    _WfDs1E1CurrentBESs_Type()
)
wfDs1E1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentBESs.setStatus("mandatory")
_WfDs1E1CurrentDMs_Type = Gauge32
_WfDs1E1CurrentDMs_Object = MibTableColumn
wfDs1E1CurrentDMs = _WfDs1E1CurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 10),
    _WfDs1E1CurrentDMs_Type()
)
wfDs1E1CurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentDMs.setStatus("mandatory")
_WfDs1E1CurrentLCVs_Type = Gauge32
_WfDs1E1CurrentLCVs_Object = MibTableColumn
wfDs1E1CurrentLCVs = _WfDs1E1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 11),
    _WfDs1E1CurrentLCVs_Type()
)
wfDs1E1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentLCVs.setStatus("mandatory")
_WfDs1E1CurrentSASs_Type = Gauge32
_WfDs1E1CurrentSASs_Object = MibTableColumn
wfDs1E1CurrentSASs = _WfDs1E1CurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 12),
    _WfDs1E1CurrentSASs_Type()
)
wfDs1E1CurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentSASs.setStatus("mandatory")
_WfDs1E1CurrentAISSs_Type = Gauge32
_WfDs1E1CurrentAISSs_Object = MibTableColumn
wfDs1E1CurrentAISSs = _WfDs1E1CurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 13),
    _WfDs1E1CurrentAISSs_Type()
)
wfDs1E1CurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentAISSs.setStatus("mandatory")
_WfDs1E1CurrentFCs_Type = Gauge32
_WfDs1E1CurrentFCs_Object = MibTableColumn
wfDs1E1CurrentFCs = _WfDs1E1CurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 14),
    _WfDs1E1CurrentFCs_Type()
)
wfDs1E1CurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFCs.setStatus("mandatory")
_WfDs1E1CurrentTimeElapsed_Type = Integer32
_WfDs1E1CurrentTimeElapsed_Object = MibTableColumn
wfDs1E1CurrentTimeElapsed = _WfDs1E1CurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 15),
    _WfDs1E1CurrentTimeElapsed_Type()
)
wfDs1E1CurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentTimeElapsed.setStatus("mandatory")
_WfDs1E1CurrentValidIntervals_Type = Integer32
_WfDs1E1CurrentValidIntervals_Object = MibTableColumn
wfDs1E1CurrentValidIntervals = _WfDs1E1CurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 16),
    _WfDs1E1CurrentValidIntervals_Type()
)
wfDs1E1CurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentValidIntervals.setStatus("mandatory")


class _WfDs1E1CurrentValidFlag_Type(Integer32):
    """Custom type wfDs1E1CurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1CurrentValidFlag_Type.__name__ = "Integer32"
_WfDs1E1CurrentValidFlag_Object = MibTableColumn
wfDs1E1CurrentValidFlag = _WfDs1E1CurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 10, 1, 17),
    _WfDs1E1CurrentValidFlag_Type()
)
wfDs1E1CurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentValidFlag.setStatus("mandatory")
_WfDs1E1IntervalTable_Object = MibTable
wfDs1E1IntervalTable = _WfDs1E1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11)
)
if mibBuilder.loadTexts:
    wfDs1E1IntervalTable.setStatus("mandatory")
_WfDs1E1IntervalEntry_Object = MibTableRow
wfDs1E1IntervalEntry = _WfDs1E1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1)
)
wfDs1E1IntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1IntervalPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1IntervalEntry.setStatus("mandatory")
_WfDs1E1IntervalPortLineNumber_Type = Integer32
_WfDs1E1IntervalPortLineNumber_Object = MibTableColumn
wfDs1E1IntervalPortLineNumber = _WfDs1E1IntervalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 1),
    _WfDs1E1IntervalPortLineNumber_Type()
)
wfDs1E1IntervalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalPortLineNumber.setStatus("mandatory")
_WfDs1E1IntervalNumber_Type = Integer32
_WfDs1E1IntervalNumber_Object = MibTableColumn
wfDs1E1IntervalNumber = _WfDs1E1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 2),
    _WfDs1E1IntervalNumber_Type()
)
wfDs1E1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalNumber.setStatus("mandatory")
_WfDs1E1IntervalESs_Type = Gauge32
_WfDs1E1IntervalESs_Object = MibTableColumn
wfDs1E1IntervalESs = _WfDs1E1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 3),
    _WfDs1E1IntervalESs_Type()
)
wfDs1E1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalESs.setStatus("mandatory")
_WfDs1E1IntervalSESs_Type = Gauge32
_WfDs1E1IntervalSESs_Object = MibTableColumn
wfDs1E1IntervalSESs = _WfDs1E1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 4),
    _WfDs1E1IntervalSESs_Type()
)
wfDs1E1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalSESs.setStatus("mandatory")
_WfDs1E1IntervalSEFSs_Type = Gauge32
_WfDs1E1IntervalSEFSs_Object = MibTableColumn
wfDs1E1IntervalSEFSs = _WfDs1E1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 5),
    _WfDs1E1IntervalSEFSs_Type()
)
wfDs1E1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalSEFSs.setStatus("mandatory")
_WfDs1E1IntervalUASs_Type = Gauge32
_WfDs1E1IntervalUASs_Object = MibTableColumn
wfDs1E1IntervalUASs = _WfDs1E1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 6),
    _WfDs1E1IntervalUASs_Type()
)
wfDs1E1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalUASs.setStatus("mandatory")
_WfDs1E1IntervalCSSs_Type = Gauge32
_WfDs1E1IntervalCSSs_Object = MibTableColumn
wfDs1E1IntervalCSSs = _WfDs1E1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 7),
    _WfDs1E1IntervalCSSs_Type()
)
wfDs1E1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalCSSs.setStatus("mandatory")
_WfDs1E1IntervalPCVs_Type = Gauge32
_WfDs1E1IntervalPCVs_Object = MibTableColumn
wfDs1E1IntervalPCVs = _WfDs1E1IntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 8),
    _WfDs1E1IntervalPCVs_Type()
)
wfDs1E1IntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalPCVs.setStatus("mandatory")
_WfDs1E1IntervalLESs_Type = Gauge32
_WfDs1E1IntervalLESs_Object = MibTableColumn
wfDs1E1IntervalLESs = _WfDs1E1IntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 9),
    _WfDs1E1IntervalLESs_Type()
)
wfDs1E1IntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalLESs.setStatus("mandatory")
_WfDs1E1IntervalBESs_Type = Gauge32
_WfDs1E1IntervalBESs_Object = MibTableColumn
wfDs1E1IntervalBESs = _WfDs1E1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 10),
    _WfDs1E1IntervalBESs_Type()
)
wfDs1E1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalBESs.setStatus("mandatory")
_WfDs1E1IntervalDMs_Type = Gauge32
_WfDs1E1IntervalDMs_Object = MibTableColumn
wfDs1E1IntervalDMs = _WfDs1E1IntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 11),
    _WfDs1E1IntervalDMs_Type()
)
wfDs1E1IntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalDMs.setStatus("mandatory")
_WfDs1E1IntervalLCVs_Type = Gauge32
_WfDs1E1IntervalLCVs_Object = MibTableColumn
wfDs1E1IntervalLCVs = _WfDs1E1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 12),
    _WfDs1E1IntervalLCVs_Type()
)
wfDs1E1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalLCVs.setStatus("mandatory")
_WfDs1E1IntervalSASs_Type = Gauge32
_WfDs1E1IntervalSASs_Object = MibTableColumn
wfDs1E1IntervalSASs = _WfDs1E1IntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 13),
    _WfDs1E1IntervalSASs_Type()
)
wfDs1E1IntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalSASs.setStatus("mandatory")
_WfDs1E1IntervalAISSs_Type = Gauge32
_WfDs1E1IntervalAISSs_Object = MibTableColumn
wfDs1E1IntervalAISSs = _WfDs1E1IntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 14),
    _WfDs1E1IntervalAISSs_Type()
)
wfDs1E1IntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalAISSs.setStatus("mandatory")
_WfDs1E1IntervalFCs_Type = Gauge32
_WfDs1E1IntervalFCs_Object = MibTableColumn
wfDs1E1IntervalFCs = _WfDs1E1IntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 15),
    _WfDs1E1IntervalFCs_Type()
)
wfDs1E1IntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFCs.setStatus("mandatory")


class _WfDs1E1IntervalValidFlag_Type(Integer32):
    """Custom type wfDs1E1IntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1IntervalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1IntervalValidFlag_Object = MibTableColumn
wfDs1E1IntervalValidFlag = _WfDs1E1IntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 11, 1, 16),
    _WfDs1E1IntervalValidFlag_Type()
)
wfDs1E1IntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalValidFlag.setStatus("mandatory")
_WfDs1E1TotalTable_Object = MibTable
wfDs1E1TotalTable = _WfDs1E1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12)
)
if mibBuilder.loadTexts:
    wfDs1E1TotalTable.setStatus("mandatory")
_WfDs1E1TotalEntry_Object = MibTableRow
wfDs1E1TotalEntry = _WfDs1E1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1)
)
wfDs1E1TotalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1TotalPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1TotalEntry.setStatus("mandatory")
_WfDs1E1TotalPortLineNumber_Type = Integer32
_WfDs1E1TotalPortLineNumber_Object = MibTableColumn
wfDs1E1TotalPortLineNumber = _WfDs1E1TotalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 1),
    _WfDs1E1TotalPortLineNumber_Type()
)
wfDs1E1TotalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalPortLineNumber.setStatus("mandatory")
_WfDs1E1TotalESs_Type = Gauge32
_WfDs1E1TotalESs_Object = MibTableColumn
wfDs1E1TotalESs = _WfDs1E1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 2),
    _WfDs1E1TotalESs_Type()
)
wfDs1E1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalESs.setStatus("mandatory")
_WfDs1E1TotalSESs_Type = Gauge32
_WfDs1E1TotalSESs_Object = MibTableColumn
wfDs1E1TotalSESs = _WfDs1E1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 3),
    _WfDs1E1TotalSESs_Type()
)
wfDs1E1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalSESs.setStatus("mandatory")
_WfDs1E1TotalSEFSs_Type = Gauge32
_WfDs1E1TotalSEFSs_Object = MibTableColumn
wfDs1E1TotalSEFSs = _WfDs1E1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 4),
    _WfDs1E1TotalSEFSs_Type()
)
wfDs1E1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalSEFSs.setStatus("mandatory")
_WfDs1E1TotalUASs_Type = Gauge32
_WfDs1E1TotalUASs_Object = MibTableColumn
wfDs1E1TotalUASs = _WfDs1E1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 5),
    _WfDs1E1TotalUASs_Type()
)
wfDs1E1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalUASs.setStatus("mandatory")
_WfDs1E1TotalCSSs_Type = Gauge32
_WfDs1E1TotalCSSs_Object = MibTableColumn
wfDs1E1TotalCSSs = _WfDs1E1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 6),
    _WfDs1E1TotalCSSs_Type()
)
wfDs1E1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalCSSs.setStatus("mandatory")
_WfDs1E1TotalPCVs_Type = Gauge32
_WfDs1E1TotalPCVs_Object = MibTableColumn
wfDs1E1TotalPCVs = _WfDs1E1TotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 7),
    _WfDs1E1TotalPCVs_Type()
)
wfDs1E1TotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalPCVs.setStatus("mandatory")
_WfDs1E1TotalLESs_Type = Gauge32
_WfDs1E1TotalLESs_Object = MibTableColumn
wfDs1E1TotalLESs = _WfDs1E1TotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 8),
    _WfDs1E1TotalLESs_Type()
)
wfDs1E1TotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalLESs.setStatus("mandatory")
_WfDs1E1TotalBESs_Type = Gauge32
_WfDs1E1TotalBESs_Object = MibTableColumn
wfDs1E1TotalBESs = _WfDs1E1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 9),
    _WfDs1E1TotalBESs_Type()
)
wfDs1E1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalBESs.setStatus("mandatory")
_WfDs1E1TotalDMs_Type = Gauge32
_WfDs1E1TotalDMs_Object = MibTableColumn
wfDs1E1TotalDMs = _WfDs1E1TotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 10),
    _WfDs1E1TotalDMs_Type()
)
wfDs1E1TotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalDMs.setStatus("mandatory")
_WfDs1E1TotalLCVs_Type = Gauge32
_WfDs1E1TotalLCVs_Object = MibTableColumn
wfDs1E1TotalLCVs = _WfDs1E1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 11),
    _WfDs1E1TotalLCVs_Type()
)
wfDs1E1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalLCVs.setStatus("mandatory")
_WfDs1E1TotalSASs_Type = Gauge32
_WfDs1E1TotalSASs_Object = MibTableColumn
wfDs1E1TotalSASs = _WfDs1E1TotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 12),
    _WfDs1E1TotalSASs_Type()
)
wfDs1E1TotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalSASs.setStatus("mandatory")
_WfDs1E1TotalAISSs_Type = Gauge32
_WfDs1E1TotalAISSs_Object = MibTableColumn
wfDs1E1TotalAISSs = _WfDs1E1TotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 13),
    _WfDs1E1TotalAISSs_Type()
)
wfDs1E1TotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalAISSs.setStatus("mandatory")
_WfDs1E1TotalFCs_Type = Gauge32
_WfDs1E1TotalFCs_Object = MibTableColumn
wfDs1E1TotalFCs = _WfDs1E1TotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 14),
    _WfDs1E1TotalFCs_Type()
)
wfDs1E1TotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFCs.setStatus("mandatory")


class _WfDs1E1TotalValidFlag_Type(Integer32):
    """Custom type wfDs1E1TotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1TotalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1TotalValidFlag_Object = MibTableColumn
wfDs1E1TotalValidFlag = _WfDs1E1TotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 12, 1, 15),
    _WfDs1E1TotalValidFlag_Type()
)
wfDs1E1TotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalValidFlag.setStatus("mandatory")
_WfDs1E1BertStatsTable_Object = MibTable
wfDs1E1BertStatsTable = _WfDs1E1BertStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 14)
)
if mibBuilder.loadTexts:
    wfDs1E1BertStatsTable.setStatus("mandatory")
_WfDs1E1BertStatsEntry_Object = MibTableRow
wfDs1E1BertStatsEntry = _WfDs1E1BertStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 14, 1)
)
wfDs1E1BertStatsEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1BertStatsPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1BertStatsEntry.setStatus("mandatory")
_WfDs1E1BertStatsPortLineNumber_Type = Integer32
_WfDs1E1BertStatsPortLineNumber_Object = MibTableColumn
wfDs1E1BertStatsPortLineNumber = _WfDs1E1BertStatsPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 14, 1, 1),
    _WfDs1E1BertStatsPortLineNumber_Type()
)
wfDs1E1BertStatsPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1BertStatsPortLineNumber.setStatus("mandatory")
_WfDs1E1BertStatsBitErrors_Type = Counter32
_WfDs1E1BertStatsBitErrors_Object = MibTableColumn
wfDs1E1BertStatsBitErrors = _WfDs1E1BertStatsBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 14, 1, 2),
    _WfDs1E1BertStatsBitErrors_Type()
)
wfDs1E1BertStatsBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1BertStatsBitErrors.setStatus("mandatory")
_WfDs1E1BertStatsBits_Type = Counter32
_WfDs1E1BertStatsBits_Object = MibTableColumn
wfDs1E1BertStatsBits = _WfDs1E1BertStatsBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 14, 1, 3),
    _WfDs1E1BertStatsBits_Type()
)
wfDs1E1BertStatsBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1BertStatsBits.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsTable_Object = MibTable
wfDs1E1CurrentFramerStatsTable = _WfDs1E1CurrentFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15)
)
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsTable.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsEntry_Object = MibTableRow
wfDs1E1CurrentFramerStatsEntry = _WfDs1E1CurrentFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1)
)
wfDs1E1CurrentFramerStatsEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1CurrentFramerStatsPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsEntry.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsPortLineNumber_Type = Integer32
_WfDs1E1CurrentFramerStatsPortLineNumber_Object = MibTableColumn
wfDs1E1CurrentFramerStatsPortLineNumber = _WfDs1E1CurrentFramerStatsPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 1),
    _WfDs1E1CurrentFramerStatsPortLineNumber_Type()
)
wfDs1E1CurrentFramerStatsPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsPortLineNumber.setStatus("mandatory")


class _WfDs1E1CurrentFramerStatsMediaType_Type(Integer32):
    """Custom type wfDs1E1CurrentFramerStatsMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_WfDs1E1CurrentFramerStatsMediaType_Type.__name__ = "Integer32"
_WfDs1E1CurrentFramerStatsMediaType_Object = MibTableColumn
wfDs1E1CurrentFramerStatsMediaType = _WfDs1E1CurrentFramerStatsMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 2),
    _WfDs1E1CurrentFramerStatsMediaType_Type()
)
wfDs1E1CurrentFramerStatsMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsMediaType.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsBpvCounts_Type = Gauge32
_WfDs1E1CurrentFramerStatsBpvCounts_Object = MibTableColumn
wfDs1E1CurrentFramerStatsBpvCounts = _WfDs1E1CurrentFramerStatsBpvCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 3),
    _WfDs1E1CurrentFramerStatsBpvCounts_Type()
)
wfDs1E1CurrentFramerStatsBpvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsBpvCounts.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsCrc4Counts_Type = Gauge32
_WfDs1E1CurrentFramerStatsCrc4Counts_Object = MibTableColumn
wfDs1E1CurrentFramerStatsCrc4Counts = _WfDs1E1CurrentFramerStatsCrc4Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 4),
    _WfDs1E1CurrentFramerStatsCrc4Counts_Type()
)
wfDs1E1CurrentFramerStatsCrc4Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsCrc4Counts.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsFebeCounts_Type = Gauge32
_WfDs1E1CurrentFramerStatsFebeCounts_Object = MibTableColumn
wfDs1E1CurrentFramerStatsFebeCounts = _WfDs1E1CurrentFramerStatsFebeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 5),
    _WfDs1E1CurrentFramerStatsFebeCounts_Type()
)
wfDs1E1CurrentFramerStatsFebeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsFebeCounts.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsOofCounts_Type = Gauge32
_WfDs1E1CurrentFramerStatsOofCounts_Object = MibTableColumn
wfDs1E1CurrentFramerStatsOofCounts = _WfDs1E1CurrentFramerStatsOofCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 6),
    _WfDs1E1CurrentFramerStatsOofCounts_Type()
)
wfDs1E1CurrentFramerStatsOofCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsOofCounts.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsFeCounts_Type = Gauge32
_WfDs1E1CurrentFramerStatsFeCounts_Object = MibTableColumn
wfDs1E1CurrentFramerStatsFeCounts = _WfDs1E1CurrentFramerStatsFeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 7),
    _WfDs1E1CurrentFramerStatsFeCounts_Type()
)
wfDs1E1CurrentFramerStatsFeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsFeCounts.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsLossFrameFailures_Type = Gauge32
_WfDs1E1CurrentFramerStatsLossFrameFailures_Object = MibTableColumn
wfDs1E1CurrentFramerStatsLossFrameFailures = _WfDs1E1CurrentFramerStatsLossFrameFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 8),
    _WfDs1E1CurrentFramerStatsLossFrameFailures_Type()
)
wfDs1E1CurrentFramerStatsLossFrameFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsLossFrameFailures.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsLossSignalFailures_Type = Gauge32
_WfDs1E1CurrentFramerStatsLossSignalFailures_Object = MibTableColumn
wfDs1E1CurrentFramerStatsLossSignalFailures = _WfDs1E1CurrentFramerStatsLossSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 9),
    _WfDs1E1CurrentFramerStatsLossSignalFailures_Type()
)
wfDs1E1CurrentFramerStatsLossSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsLossSignalFailures.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsAlarmIndicationFailures_Type = Gauge32
_WfDs1E1CurrentFramerStatsAlarmIndicationFailures_Object = MibTableColumn
wfDs1E1CurrentFramerStatsAlarmIndicationFailures = _WfDs1E1CurrentFramerStatsAlarmIndicationFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 10),
    _WfDs1E1CurrentFramerStatsAlarmIndicationFailures_Type()
)
wfDs1E1CurrentFramerStatsAlarmIndicationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsAlarmIndicationFailures.setStatus("mandatory")
_WfDs1E1CurrentFramerStatsRemoteAlarmFailures_Type = Gauge32
_WfDs1E1CurrentFramerStatsRemoteAlarmFailures_Object = MibTableColumn
wfDs1E1CurrentFramerStatsRemoteAlarmFailures = _WfDs1E1CurrentFramerStatsRemoteAlarmFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 15, 1, 11),
    _WfDs1E1CurrentFramerStatsRemoteAlarmFailures_Type()
)
wfDs1E1CurrentFramerStatsRemoteAlarmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1CurrentFramerStatsRemoteAlarmFailures.setStatus("mandatory")
_WfDs1E1TotalFramerStatsTable_Object = MibTable
wfDs1E1TotalFramerStatsTable = _WfDs1E1TotalFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16)
)
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsTable.setStatus("mandatory")
_WfDs1E1TotalFramerStatsEntry_Object = MibTableRow
wfDs1E1TotalFramerStatsEntry = _WfDs1E1TotalFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1)
)
wfDs1E1TotalFramerStatsEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1TotalFramerStatsPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsEntry.setStatus("mandatory")
_WfDs1E1TotalFramerStatsPortLineNumber_Type = Integer32
_WfDs1E1TotalFramerStatsPortLineNumber_Object = MibTableColumn
wfDs1E1TotalFramerStatsPortLineNumber = _WfDs1E1TotalFramerStatsPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 1),
    _WfDs1E1TotalFramerStatsPortLineNumber_Type()
)
wfDs1E1TotalFramerStatsPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsPortLineNumber.setStatus("mandatory")


class _WfDs1E1TotalFramerStatsMediaType_Type(Integer32):
    """Custom type wfDs1E1TotalFramerStatsMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_WfDs1E1TotalFramerStatsMediaType_Type.__name__ = "Integer32"
_WfDs1E1TotalFramerStatsMediaType_Object = MibTableColumn
wfDs1E1TotalFramerStatsMediaType = _WfDs1E1TotalFramerStatsMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 2),
    _WfDs1E1TotalFramerStatsMediaType_Type()
)
wfDs1E1TotalFramerStatsMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsMediaType.setStatus("mandatory")
_WfDs1E1TotalFramerStatsValidIntervals_Type = Gauge32
_WfDs1E1TotalFramerStatsValidIntervals_Object = MibTableColumn
wfDs1E1TotalFramerStatsValidIntervals = _WfDs1E1TotalFramerStatsValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 3),
    _WfDs1E1TotalFramerStatsValidIntervals_Type()
)
wfDs1E1TotalFramerStatsValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsValidIntervals.setStatus("mandatory")
_WfDs1E1TotalFramerStatsBpvCounts_Type = Gauge32
_WfDs1E1TotalFramerStatsBpvCounts_Object = MibTableColumn
wfDs1E1TotalFramerStatsBpvCounts = _WfDs1E1TotalFramerStatsBpvCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 4),
    _WfDs1E1TotalFramerStatsBpvCounts_Type()
)
wfDs1E1TotalFramerStatsBpvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsBpvCounts.setStatus("mandatory")
_WfDs1E1TotalFramerStatsCrc4Counts_Type = Gauge32
_WfDs1E1TotalFramerStatsCrc4Counts_Object = MibTableColumn
wfDs1E1TotalFramerStatsCrc4Counts = _WfDs1E1TotalFramerStatsCrc4Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 5),
    _WfDs1E1TotalFramerStatsCrc4Counts_Type()
)
wfDs1E1TotalFramerStatsCrc4Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsCrc4Counts.setStatus("mandatory")
_WfDs1E1TotalFramerStatsFebeCounts_Type = Gauge32
_WfDs1E1TotalFramerStatsFebeCounts_Object = MibTableColumn
wfDs1E1TotalFramerStatsFebeCounts = _WfDs1E1TotalFramerStatsFebeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 6),
    _WfDs1E1TotalFramerStatsFebeCounts_Type()
)
wfDs1E1TotalFramerStatsFebeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsFebeCounts.setStatus("mandatory")
_WfDs1E1TotalFramerStatsOofCounts_Type = Gauge32
_WfDs1E1TotalFramerStatsOofCounts_Object = MibTableColumn
wfDs1E1TotalFramerStatsOofCounts = _WfDs1E1TotalFramerStatsOofCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 7),
    _WfDs1E1TotalFramerStatsOofCounts_Type()
)
wfDs1E1TotalFramerStatsOofCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsOofCounts.setStatus("mandatory")
_WfDs1E1TotalFramerStatsFeCounts_Type = Gauge32
_WfDs1E1TotalFramerStatsFeCounts_Object = MibTableColumn
wfDs1E1TotalFramerStatsFeCounts = _WfDs1E1TotalFramerStatsFeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 8),
    _WfDs1E1TotalFramerStatsFeCounts_Type()
)
wfDs1E1TotalFramerStatsFeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsFeCounts.setStatus("mandatory")
_WfDs1E1TotalFramerStatsLossFrameFailures_Type = Gauge32
_WfDs1E1TotalFramerStatsLossFrameFailures_Object = MibTableColumn
wfDs1E1TotalFramerStatsLossFrameFailures = _WfDs1E1TotalFramerStatsLossFrameFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 9),
    _WfDs1E1TotalFramerStatsLossFrameFailures_Type()
)
wfDs1E1TotalFramerStatsLossFrameFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsLossFrameFailures.setStatus("mandatory")
_WfDs1E1TotalFramerStatsLossSignalFailures_Type = Gauge32
_WfDs1E1TotalFramerStatsLossSignalFailures_Object = MibTableColumn
wfDs1E1TotalFramerStatsLossSignalFailures = _WfDs1E1TotalFramerStatsLossSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 10),
    _WfDs1E1TotalFramerStatsLossSignalFailures_Type()
)
wfDs1E1TotalFramerStatsLossSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsLossSignalFailures.setStatus("mandatory")
_WfDs1E1TotalFramerStatsAlarmIndicationFailures_Type = Gauge32
_WfDs1E1TotalFramerStatsAlarmIndicationFailures_Object = MibTableColumn
wfDs1E1TotalFramerStatsAlarmIndicationFailures = _WfDs1E1TotalFramerStatsAlarmIndicationFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 11),
    _WfDs1E1TotalFramerStatsAlarmIndicationFailures_Type()
)
wfDs1E1TotalFramerStatsAlarmIndicationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsAlarmIndicationFailures.setStatus("mandatory")
_WfDs1E1TotalFramerStatsRemoteAlarmFailures_Type = Gauge32
_WfDs1E1TotalFramerStatsRemoteAlarmFailures_Object = MibTableColumn
wfDs1E1TotalFramerStatsRemoteAlarmFailures = _WfDs1E1TotalFramerStatsRemoteAlarmFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 16, 1, 12),
    _WfDs1E1TotalFramerStatsRemoteAlarmFailures_Type()
)
wfDs1E1TotalFramerStatsRemoteAlarmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1TotalFramerStatsRemoteAlarmFailures.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsTable_Object = MibTable
wfDs1E1IntervalFramerStatsTable = _WfDs1E1IntervalFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17)
)
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsTable.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsEntry_Object = MibTableRow
wfDs1E1IntervalFramerStatsEntry = _WfDs1E1IntervalFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1)
)
wfDs1E1IntervalFramerStatsEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1IntervalFramerStatsPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1IntervalFramerStatsIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsEntry.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsPortLineNumber_Type = Integer32
_WfDs1E1IntervalFramerStatsPortLineNumber_Object = MibTableColumn
wfDs1E1IntervalFramerStatsPortLineNumber = _WfDs1E1IntervalFramerStatsPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 1),
    _WfDs1E1IntervalFramerStatsPortLineNumber_Type()
)
wfDs1E1IntervalFramerStatsPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsPortLineNumber.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsIntervalNumber_Type = Integer32
_WfDs1E1IntervalFramerStatsIntervalNumber_Object = MibTableColumn
wfDs1E1IntervalFramerStatsIntervalNumber = _WfDs1E1IntervalFramerStatsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 2),
    _WfDs1E1IntervalFramerStatsIntervalNumber_Type()
)
wfDs1E1IntervalFramerStatsIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsIntervalNumber.setStatus("mandatory")


class _WfDs1E1IntervalFramerStatsMediaType_Type(Integer32):
    """Custom type wfDs1E1IntervalFramerStatsMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_WfDs1E1IntervalFramerStatsMediaType_Type.__name__ = "Integer32"
_WfDs1E1IntervalFramerStatsMediaType_Object = MibTableColumn
wfDs1E1IntervalFramerStatsMediaType = _WfDs1E1IntervalFramerStatsMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 3),
    _WfDs1E1IntervalFramerStatsMediaType_Type()
)
wfDs1E1IntervalFramerStatsMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsMediaType.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsBpvCounts_Type = Gauge32
_WfDs1E1IntervalFramerStatsBpvCounts_Object = MibTableColumn
wfDs1E1IntervalFramerStatsBpvCounts = _WfDs1E1IntervalFramerStatsBpvCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 4),
    _WfDs1E1IntervalFramerStatsBpvCounts_Type()
)
wfDs1E1IntervalFramerStatsBpvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsBpvCounts.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsCrc4Counts_Type = Gauge32
_WfDs1E1IntervalFramerStatsCrc4Counts_Object = MibTableColumn
wfDs1E1IntervalFramerStatsCrc4Counts = _WfDs1E1IntervalFramerStatsCrc4Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 5),
    _WfDs1E1IntervalFramerStatsCrc4Counts_Type()
)
wfDs1E1IntervalFramerStatsCrc4Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsCrc4Counts.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsFebeCounts_Type = Gauge32
_WfDs1E1IntervalFramerStatsFebeCounts_Object = MibTableColumn
wfDs1E1IntervalFramerStatsFebeCounts = _WfDs1E1IntervalFramerStatsFebeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 6),
    _WfDs1E1IntervalFramerStatsFebeCounts_Type()
)
wfDs1E1IntervalFramerStatsFebeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsFebeCounts.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsOofCounts_Type = Gauge32
_WfDs1E1IntervalFramerStatsOofCounts_Object = MibTableColumn
wfDs1E1IntervalFramerStatsOofCounts = _WfDs1E1IntervalFramerStatsOofCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 7),
    _WfDs1E1IntervalFramerStatsOofCounts_Type()
)
wfDs1E1IntervalFramerStatsOofCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsOofCounts.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsFeCounts_Type = Gauge32
_WfDs1E1IntervalFramerStatsFeCounts_Object = MibTableColumn
wfDs1E1IntervalFramerStatsFeCounts = _WfDs1E1IntervalFramerStatsFeCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 8),
    _WfDs1E1IntervalFramerStatsFeCounts_Type()
)
wfDs1E1IntervalFramerStatsFeCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsFeCounts.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsLossFrameFailures_Type = Gauge32
_WfDs1E1IntervalFramerStatsLossFrameFailures_Object = MibTableColumn
wfDs1E1IntervalFramerStatsLossFrameFailures = _WfDs1E1IntervalFramerStatsLossFrameFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 9),
    _WfDs1E1IntervalFramerStatsLossFrameFailures_Type()
)
wfDs1E1IntervalFramerStatsLossFrameFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsLossFrameFailures.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsLossSignalFailures_Type = Gauge32
_WfDs1E1IntervalFramerStatsLossSignalFailures_Object = MibTableColumn
wfDs1E1IntervalFramerStatsLossSignalFailures = _WfDs1E1IntervalFramerStatsLossSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 10),
    _WfDs1E1IntervalFramerStatsLossSignalFailures_Type()
)
wfDs1E1IntervalFramerStatsLossSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsLossSignalFailures.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsAlarmIndicationFailures_Type = Gauge32
_WfDs1E1IntervalFramerStatsAlarmIndicationFailures_Object = MibTableColumn
wfDs1E1IntervalFramerStatsAlarmIndicationFailures = _WfDs1E1IntervalFramerStatsAlarmIndicationFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 11),
    _WfDs1E1IntervalFramerStatsAlarmIndicationFailures_Type()
)
wfDs1E1IntervalFramerStatsAlarmIndicationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsAlarmIndicationFailures.setStatus("mandatory")
_WfDs1E1IntervalFramerStatsRemoteAlarmFailures_Type = Gauge32
_WfDs1E1IntervalFramerStatsRemoteAlarmFailures_Object = MibTableColumn
wfDs1E1IntervalFramerStatsRemoteAlarmFailures = _WfDs1E1IntervalFramerStatsRemoteAlarmFailures_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 17, 1, 12),
    _WfDs1E1IntervalFramerStatsRemoteAlarmFailures_Type()
)
wfDs1E1IntervalFramerStatsRemoteAlarmFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1IntervalFramerStatsRemoteAlarmFailures.setStatus("mandatory")
_WfDs1E1ClockTable_Object = MibTable
wfDs1E1ClockTable = _WfDs1E1ClockTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18)
)
if mibBuilder.loadTexts:
    wfDs1E1ClockTable.setStatus("mandatory")
_WfDs1E1ClockEntry_Object = MibTableRow
wfDs1E1ClockEntry = _WfDs1E1ClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1)
)
wfDs1E1ClockEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ClockPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1ClockEntry.setStatus("mandatory")


class _WfDs1E1ClockDelete_Type(Integer32):
    """Custom type wfDs1E1ClockDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1ClockDelete_Type.__name__ = "Integer32"
_WfDs1E1ClockDelete_Object = MibTableColumn
wfDs1E1ClockDelete = _WfDs1E1ClockDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 1),
    _WfDs1E1ClockDelete_Type()
)
wfDs1E1ClockDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ClockDelete.setStatus("mandatory")
_WfDs1E1ClockPortLineNumber_Type = Integer32
_WfDs1E1ClockPortLineNumber_Object = MibTableColumn
wfDs1E1ClockPortLineNumber = _WfDs1E1ClockPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 2),
    _WfDs1E1ClockPortLineNumber_Type()
)
wfDs1E1ClockPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ClockPortLineNumber.setStatus("mandatory")


class _WfDs1E1ClockPrimaryClock_Type(Integer32):
    """Custom type wfDs1E1ClockPrimaryClock based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("loop1", 3),
          ("loop2", 4),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ClockPrimaryClock_Type.__name__ = "Integer32"
_WfDs1E1ClockPrimaryClock_Object = MibTableColumn
wfDs1E1ClockPrimaryClock = _WfDs1E1ClockPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 3),
    _WfDs1E1ClockPrimaryClock_Type()
)
wfDs1E1ClockPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ClockPrimaryClock.setStatus("mandatory")


class _WfDs1E1ClockSecondaryClock_Type(Integer32):
    """Custom type wfDs1E1ClockSecondaryClock based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("loop1", 3),
          ("loop2", 4),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ClockSecondaryClock_Type.__name__ = "Integer32"
_WfDs1E1ClockSecondaryClock_Object = MibTableColumn
wfDs1E1ClockSecondaryClock = _WfDs1E1ClockSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 4),
    _WfDs1E1ClockSecondaryClock_Type()
)
wfDs1E1ClockSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ClockSecondaryClock.setStatus("mandatory")


class _WfDs1E1ClockCurrentClock_Type(Integer32):
    """Custom type wfDs1E1ClockCurrentClock based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("loop1", 3),
          ("loop2", 4),
          ("loop3", 5),
          ("loop4", 6))
    )


_WfDs1E1ClockCurrentClock_Type.__name__ = "Integer32"
_WfDs1E1ClockCurrentClock_Object = MibTableColumn
wfDs1E1ClockCurrentClock = _WfDs1E1ClockCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 5),
    _WfDs1E1ClockCurrentClock_Type()
)
wfDs1E1ClockCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ClockCurrentClock.setStatus("mandatory")


class _WfDs1E1ClockLoopClockOperational_Type(Integer32):
    """Custom type wfDs1E1ClockLoopClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ClockLoopClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ClockLoopClockOperational_Object = MibTableColumn
wfDs1E1ClockLoopClockOperational = _WfDs1E1ClockLoopClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 6),
    _WfDs1E1ClockLoopClockOperational_Type()
)
wfDs1E1ClockLoopClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ClockLoopClockOperational.setStatus("mandatory")


class _WfDs1E1ClockExtClockOperational_Type(Integer32):
    """Custom type wfDs1E1ClockExtClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs1E1ClockExtClockOperational_Type.__name__ = "Integer32"
_WfDs1E1ClockExtClockOperational_Object = MibTableColumn
wfDs1E1ClockExtClockOperational = _WfDs1E1ClockExtClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 18, 1, 7),
    _WfDs1E1ClockExtClockOperational_Type()
)
wfDs1E1ClockExtClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ClockExtClockOperational.setStatus("mandatory")
_WfDs1E1LineQueStatTable_Object = MibTable
wfDs1E1LineQueStatTable = _WfDs1E1LineQueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20)
)
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatTable.setStatus("mandatory")
_WfDs1E1LineQueStatEntry_Object = MibTableRow
wfDs1E1LineQueStatEntry = _WfDs1E1LineQueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1)
)
wfDs1E1LineQueStatEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineQueStatPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineQueStatLineIndex"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineQueStatQueueIndex"),
)
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatEntry.setStatus("mandatory")
_WfDs1E1LineQueStatPortLineNumber_Type = Integer32
_WfDs1E1LineQueStatPortLineNumber_Object = MibTableColumn
wfDs1E1LineQueStatPortLineNumber = _WfDs1E1LineQueStatPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 1),
    _WfDs1E1LineQueStatPortLineNumber_Type()
)
wfDs1E1LineQueStatPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatPortLineNumber.setStatus("mandatory")
_WfDs1E1LineQueStatLineIndex_Type = Integer32
_WfDs1E1LineQueStatLineIndex_Object = MibTableColumn
wfDs1E1LineQueStatLineIndex = _WfDs1E1LineQueStatLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 2),
    _WfDs1E1LineQueStatLineIndex_Type()
)
wfDs1E1LineQueStatLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatLineIndex.setStatus("mandatory")
_WfDs1E1LineQueStatQueueIndex_Type = Integer32
_WfDs1E1LineQueStatQueueIndex_Object = MibTableColumn
wfDs1E1LineQueStatQueueIndex = _WfDs1E1LineQueStatQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 3),
    _WfDs1E1LineQueStatQueueIndex_Type()
)
wfDs1E1LineQueStatQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatQueueIndex.setStatus("mandatory")
_WfDs1E1LineQueStatTxOctets_Type = Counter32
_WfDs1E1LineQueStatTxOctets_Object = MibTableColumn
wfDs1E1LineQueStatTxOctets = _WfDs1E1LineQueStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 4),
    _WfDs1E1LineQueStatTxOctets_Type()
)
wfDs1E1LineQueStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatTxOctets.setStatus("mandatory")
_WfDs1E1LineQueStatTxPackets_Type = Counter32
_WfDs1E1LineQueStatTxPackets_Object = MibTableColumn
wfDs1E1LineQueStatTxPackets = _WfDs1E1LineQueStatTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 5),
    _WfDs1E1LineQueStatTxPackets_Type()
)
wfDs1E1LineQueStatTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatTxPackets.setStatus("mandatory")
_WfDs1E1LineQueStatTxDrops_Type = Counter32
_WfDs1E1LineQueStatTxDrops_Object = MibTableColumn
wfDs1E1LineQueStatTxDrops = _WfDs1E1LineQueStatTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 20, 1, 6),
    _WfDs1E1LineQueStatTxDrops_Type()
)
wfDs1E1LineQueStatTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineQueStatTxDrops.setStatus("mandatory")
_WfDs1E1LineCfgTable_Object = MibTable
wfDs1E1LineCfgTable = _WfDs1E1LineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21)
)
if mibBuilder.loadTexts:
    wfDs1E1LineCfgTable.setStatus("mandatory")
_WfDs1E1LineCfgEntry_Object = MibTableRow
wfDs1E1LineCfgEntry = _WfDs1E1LineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1)
)
wfDs1E1LineCfgEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineCfgPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineCfgIndex"),
)
if mibBuilder.loadTexts:
    wfDs1E1LineCfgEntry.setStatus("mandatory")


class _WfDs1E1LineCfgDelete_Type(Integer32):
    """Custom type wfDs1E1LineCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1LineCfgDelete_Type.__name__ = "Integer32"
_WfDs1E1LineCfgDelete_Object = MibTableColumn
wfDs1E1LineCfgDelete = _WfDs1E1LineCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 1),
    _WfDs1E1LineCfgDelete_Type()
)
wfDs1E1LineCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgDelete.setStatus("mandatory")


class _WfDs1E1LineCfgDisable_Type(Integer32):
    """Custom type wfDs1E1LineCfgDisable based on Integer32"""
    defaultValue = 1

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


_WfDs1E1LineCfgDisable_Type.__name__ = "Integer32"
_WfDs1E1LineCfgDisable_Object = MibTableColumn
wfDs1E1LineCfgDisable = _WfDs1E1LineCfgDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 2),
    _WfDs1E1LineCfgDisable_Type()
)
wfDs1E1LineCfgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgDisable.setStatus("mandatory")


class _WfDs1E1LineCfgState_Type(Integer32):
    """Custom type wfDs1E1LineCfgState based on Integer32"""
    defaultValue = 20

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
              20)
        )
    )
    namedValues = NamedValues(
        *(("bert", 10),
          ("down", 2),
          ("hwfrac", 11),
          ("init", 3),
          ("linedead", 7),
          ("linedieing", 6),
          ("lmiwait", 4),
          ("loopback", 5),
          ("notpresent", 20),
          ("priWait", 12),
          ("queMisCfg", 14),
          ("quePkgWait", 13),
          ("remotedeaf", 9),
          ("remoteloop", 8),
          ("up", 1))
    )


_WfDs1E1LineCfgState_Type.__name__ = "Integer32"
_WfDs1E1LineCfgState_Object = MibTableColumn
wfDs1E1LineCfgState = _WfDs1E1LineCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 3),
    _WfDs1E1LineCfgState_Type()
)
wfDs1E1LineCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgState.setStatus("mandatory")
_WfDs1E1LineLastChange_Type = TimeTicks
_WfDs1E1LineLastChange_Object = MibTableColumn
wfDs1E1LineLastChange = _WfDs1E1LineLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 4),
    _WfDs1E1LineLastChange_Type()
)
wfDs1E1LineLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineLastChange.setStatus("mandatory")
_WfDs1E1LineCfgPortLineNumber_Type = Integer32
_WfDs1E1LineCfgPortLineNumber_Object = MibTableColumn
wfDs1E1LineCfgPortLineNumber = _WfDs1E1LineCfgPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 5),
    _WfDs1E1LineCfgPortLineNumber_Type()
)
wfDs1E1LineCfgPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgPortLineNumber.setStatus("mandatory")
_WfDs1E1LineCfgIndex_Type = Integer32
_WfDs1E1LineCfgIndex_Object = MibTableColumn
wfDs1E1LineCfgIndex = _WfDs1E1LineCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 6),
    _WfDs1E1LineCfgIndex_Type()
)
wfDs1E1LineCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgIndex.setStatus("mandatory")
_WfDs1E1LineCfgIfIndex_Type = Integer32
_WfDs1E1LineCfgIfIndex_Object = MibTableColumn
wfDs1E1LineCfgIfIndex = _WfDs1E1LineCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 7),
    _WfDs1E1LineCfgIfIndex_Type()
)
wfDs1E1LineCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgIfIndex.setStatus("mandatory")
_WfDs1E1LineCfgCct_Type = Integer32
_WfDs1E1LineCfgCct_Object = MibTableColumn
wfDs1E1LineCfgCct = _WfDs1E1LineCfgCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 8),
    _WfDs1E1LineCfgCct_Type()
)
wfDs1E1LineCfgCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgCct.setStatus("mandatory")
_WfDs1E1LineCfgLineNumber_Type = Integer32
_WfDs1E1LineCfgLineNumber_Object = MibTableColumn
wfDs1E1LineCfgLineNumber = _WfDs1E1LineCfgLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 9),
    _WfDs1E1LineCfgLineNumber_Type()
)
wfDs1E1LineCfgLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgLineNumber.setStatus("mandatory")


class _WfDs1E1LineCfgQosServicePkg_Type(Integer32):
    """Custom type wfDs1E1LineCfgQosServicePkg based on Integer32"""
    defaultValue = 0


_WfDs1E1LineCfgQosServicePkg_Object = MibTableColumn
wfDs1E1LineCfgQosServicePkg = _WfDs1E1LineCfgQosServicePkg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 10),
    _WfDs1E1LineCfgQosServicePkg_Type()
)
wfDs1E1LineCfgQosServicePkg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgQosServicePkg.setStatus("mandatory")
_WfDs1E1LineCfgTimeSlotAssign_Type = Integer32
_WfDs1E1LineCfgTimeSlotAssign_Object = MibTableColumn
wfDs1E1LineCfgTimeSlotAssign = _WfDs1E1LineCfgTimeSlotAssign_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 11),
    _WfDs1E1LineCfgTimeSlotAssign_Type()
)
wfDs1E1LineCfgTimeSlotAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgTimeSlotAssign.setStatus("mandatory")
_WfDs1E1LineCfgActualTimeSlotAssign_Type = DisplayString
_WfDs1E1LineCfgActualTimeSlotAssign_Object = MibTableColumn
wfDs1E1LineCfgActualTimeSlotAssign = _WfDs1E1LineCfgActualTimeSlotAssign_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 12),
    _WfDs1E1LineCfgActualTimeSlotAssign_Type()
)
wfDs1E1LineCfgActualTimeSlotAssign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgActualTimeSlotAssign.setStatus("mandatory")


class _WfDs1E1LineCfgWanProtocol_Type(Integer32):
    """Custom type wfDs1E1LineCfgWanProtocol based on Integer32"""
    defaultValue = 3

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("atm", 9),
          ("framerelay", 5),
          ("lapb", 10),
          ("passthru", 2),
          ("ppp", 3),
          ("sdlc", 11),
          ("smds", 4),
          ("standard", 1),
          ("sw", 8),
          ("switch", 7),
          ("x25", 6))
    )


_WfDs1E1LineCfgWanProtocol_Type.__name__ = "Integer32"
_WfDs1E1LineCfgWanProtocol_Object = MibTableColumn
wfDs1E1LineCfgWanProtocol = _WfDs1E1LineCfgWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 13),
    _WfDs1E1LineCfgWanProtocol_Type()
)
wfDs1E1LineCfgWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgWanProtocol.setStatus("mandatory")


class _WfDs1E1LineCfgRateAdaption_Type(Integer32):
    """Custom type wfDs1E1LineCfgRateAdaption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaption56klsb", 3),
          ("adaption64k", 1))
    )


_WfDs1E1LineCfgRateAdaption_Type.__name__ = "Integer32"
_WfDs1E1LineCfgRateAdaption_Object = MibTableColumn
wfDs1E1LineCfgRateAdaption = _WfDs1E1LineCfgRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 14),
    _WfDs1E1LineCfgRateAdaption_Type()
)
wfDs1E1LineCfgRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgRateAdaption.setStatus("mandatory")


class _WfDs1E1LineCfgIFTF_Type(Integer32):
    """Custom type wfDs1E1LineCfgIFTF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flags", 1),
          ("idles", 2))
    )


_WfDs1E1LineCfgIFTF_Type.__name__ = "Integer32"
_WfDs1E1LineCfgIFTF_Object = MibTableColumn
wfDs1E1LineCfgIFTF = _WfDs1E1LineCfgIFTF_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 15),
    _WfDs1E1LineCfgIFTF_Type()
)
wfDs1E1LineCfgIFTF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgIFTF.setStatus("mandatory")


class _WfDs1E1LineCfgCRCSize_Type(Integer32):
    """Custom type wfDs1E1LineCfgCRCSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 2),
          ("crc32", 1))
    )


_WfDs1E1LineCfgCRCSize_Type.__name__ = "Integer32"
_WfDs1E1LineCfgCRCSize_Object = MibTableColumn
wfDs1E1LineCfgCRCSize = _WfDs1E1LineCfgCRCSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 16),
    _WfDs1E1LineCfgCRCSize_Type()
)
wfDs1E1LineCfgCRCSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgCRCSize.setStatus("mandatory")


class _WfDs1E1LineCfgMtu_Type(Integer32):
    """Custom type wfDs1E1LineCfgMtu based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfDs1E1LineCfgMtu_Type.__name__ = "Integer32"
_WfDs1E1LineCfgMtu_Object = MibTableColumn
wfDs1E1LineCfgMtu = _WfDs1E1LineCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 17),
    _WfDs1E1LineCfgMtu_Type()
)
wfDs1E1LineCfgMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgMtu.setStatus("mandatory")


class _WfDs1E1LineCfgBertMode_Type(Integer32):
    """Custom type wfDs1E1LineCfgBertMode based on Integer32"""
    defaultValue = 2

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


_WfDs1E1LineCfgBertMode_Type.__name__ = "Integer32"
_WfDs1E1LineCfgBertMode_Object = MibTableColumn
wfDs1E1LineCfgBertMode = _WfDs1E1LineCfgBertMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 18),
    _WfDs1E1LineCfgBertMode_Type()
)
wfDs1E1LineCfgBertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgBertMode.setStatus("mandatory")


class _WfDs1E1LineCfgBertTestPattern_Type(Integer32):
    """Custom type wfDs1E1LineCfgBertTestPattern based on Integer32"""
    defaultValue = 2

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
        *(("ones", 2),
          ("qrss", 3),
          ("two15", 4),
          ("two15-inv", 5),
          ("two20", 6),
          ("two23", 7),
          ("two23-inv", 8),
          ("zeros", 1))
    )


_WfDs1E1LineCfgBertTestPattern_Type.__name__ = "Integer32"
_WfDs1E1LineCfgBertTestPattern_Object = MibTableColumn
wfDs1E1LineCfgBertTestPattern = _WfDs1E1LineCfgBertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 19),
    _WfDs1E1LineCfgBertTestPattern_Type()
)
wfDs1E1LineCfgBertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgBertTestPattern.setStatus("mandatory")


class _WfDs1E1LineCfgFractionalLoopback_Type(Integer32):
    """Custom type wfDs1E1LineCfgFractionalLoopback based on Integer32"""
    defaultValue = 2

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


_WfDs1E1LineCfgFractionalLoopback_Type.__name__ = "Integer32"
_WfDs1E1LineCfgFractionalLoopback_Object = MibTableColumn
wfDs1E1LineCfgFractionalLoopback = _WfDs1E1LineCfgFractionalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 20),
    _WfDs1E1LineCfgFractionalLoopback_Type()
)
wfDs1E1LineCfgFractionalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgFractionalLoopback.setStatus("mandatory")


class _WfDs1E1LineCfgAcceptFracLoopCode_Type(Integer32):
    """Custom type wfDs1E1LineCfgAcceptFracLoopCode based on Integer32"""
    defaultValue = 1

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


_WfDs1E1LineCfgAcceptFracLoopCode_Type.__name__ = "Integer32"
_WfDs1E1LineCfgAcceptFracLoopCode_Object = MibTableColumn
wfDs1E1LineCfgAcceptFracLoopCode = _WfDs1E1LineCfgAcceptFracLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 21),
    _WfDs1E1LineCfgAcceptFracLoopCode_Type()
)
wfDs1E1LineCfgAcceptFracLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgAcceptFracLoopCode.setStatus("mandatory")


class _WfDs1E1LineCfgManagerMethod_Type(Integer32):
    """Custom type wfDs1E1LineCfgManagerMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1", 2),
          ("timeslots", 1))
    )


_WfDs1E1LineCfgManagerMethod_Type.__name__ = "Integer32"
_WfDs1E1LineCfgManagerMethod_Object = MibTableColumn
wfDs1E1LineCfgManagerMethod = _WfDs1E1LineCfgManagerMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 21, 1, 22),
    _WfDs1E1LineCfgManagerMethod_Type()
)
wfDs1E1LineCfgManagerMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1LineCfgManagerMethod.setStatus("mandatory")
_WfDs1E1LineStatTable_Object = MibTable
wfDs1E1LineStatTable = _WfDs1E1LineStatTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22)
)
if mibBuilder.loadTexts:
    wfDs1E1LineStatTable.setStatus("mandatory")
_WfDs1E1LineStatEntry_Object = MibTableRow
wfDs1E1LineStatEntry = _WfDs1E1LineStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1)
)
wfDs1E1LineStatEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineStatPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1LineStatIndex"),
)
if mibBuilder.loadTexts:
    wfDs1E1LineStatEntry.setStatus("mandatory")
_WfDs1E1LineStatPortLineNumber_Type = Integer32
_WfDs1E1LineStatPortLineNumber_Object = MibTableColumn
wfDs1E1LineStatPortLineNumber = _WfDs1E1LineStatPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 1),
    _WfDs1E1LineStatPortLineNumber_Type()
)
wfDs1E1LineStatPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatPortLineNumber.setStatus("mandatory")
_WfDs1E1LineStatIndex_Type = Integer32
_WfDs1E1LineStatIndex_Object = MibTableColumn
wfDs1E1LineStatIndex = _WfDs1E1LineStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 2),
    _WfDs1E1LineStatIndex_Type()
)
wfDs1E1LineStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatIndex.setStatus("mandatory")
_WfDs1E1LineStatRxOctets_Type = Counter32
_WfDs1E1LineStatRxOctets_Object = MibTableColumn
wfDs1E1LineStatRxOctets = _WfDs1E1LineStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 3),
    _WfDs1E1LineStatRxOctets_Type()
)
wfDs1E1LineStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxOctets.setStatus("mandatory")
_WfDs1E1LineStatTxOctets_Type = Counter32
_WfDs1E1LineStatTxOctets_Object = MibTableColumn
wfDs1E1LineStatTxOctets = _WfDs1E1LineStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 4),
    _WfDs1E1LineStatTxOctets_Type()
)
wfDs1E1LineStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatTxOctets.setStatus("mandatory")
_WfDs1E1LineStatRxFrames_Type = Counter32
_WfDs1E1LineStatRxFrames_Object = MibTableColumn
wfDs1E1LineStatRxFrames = _WfDs1E1LineStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 5),
    _WfDs1E1LineStatRxFrames_Type()
)
wfDs1E1LineStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxFrames.setStatus("mandatory")
_WfDs1E1LineStatTxFrames_Type = Counter32
_WfDs1E1LineStatTxFrames_Object = MibTableColumn
wfDs1E1LineStatTxFrames = _WfDs1E1LineStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 6),
    _WfDs1E1LineStatTxFrames_Type()
)
wfDs1E1LineStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatTxFrames.setStatus("mandatory")
_WfDs1E1LineStatRxErrors_Type = Counter32
_WfDs1E1LineStatRxErrors_Object = MibTableColumn
wfDs1E1LineStatRxErrors = _WfDs1E1LineStatRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 7),
    _WfDs1E1LineStatRxErrors_Type()
)
wfDs1E1LineStatRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxErrors.setStatus("mandatory")
_WfDs1E1LineStatTxErrors_Type = Counter32
_WfDs1E1LineStatTxErrors_Object = MibTableColumn
wfDs1E1LineStatTxErrors = _WfDs1E1LineStatTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 8),
    _WfDs1E1LineStatTxErrors_Type()
)
wfDs1E1LineStatTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatTxErrors.setStatus("mandatory")
_WfDs1E1LineStatRxDropPackets_Type = Counter32
_WfDs1E1LineStatRxDropPackets_Object = MibTableColumn
wfDs1E1LineStatRxDropPackets = _WfDs1E1LineStatRxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 9),
    _WfDs1E1LineStatRxDropPackets_Type()
)
wfDs1E1LineStatRxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxDropPackets.setStatus("mandatory")
_WfDs1E1LineStatTxDropPackets_Type = Counter32
_WfDs1E1LineStatTxDropPackets_Object = MibTableColumn
wfDs1E1LineStatTxDropPackets = _WfDs1E1LineStatTxDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 10),
    _WfDs1E1LineStatTxDropPackets_Type()
)
wfDs1E1LineStatTxDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatTxDropPackets.setStatus("mandatory")
_WfDs1E1LineStatTxUnderflows_Type = Counter32
_WfDs1E1LineStatTxUnderflows_Object = MibTableColumn
wfDs1E1LineStatTxUnderflows = _WfDs1E1LineStatTxUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 11),
    _WfDs1E1LineStatTxUnderflows_Type()
)
wfDs1E1LineStatTxUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatTxUnderflows.setStatus("mandatory")
_WfDs1E1LineStatRxOverflows_Type = Counter32
_WfDs1E1LineStatRxOverflows_Object = MibTableColumn
wfDs1E1LineStatRxOverflows = _WfDs1E1LineStatRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 12),
    _WfDs1E1LineStatRxOverflows_Type()
)
wfDs1E1LineStatRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxOverflows.setStatus("mandatory")
_WfDs1E1LineStatRxShortFrames_Type = Counter32
_WfDs1E1LineStatRxShortFrames_Object = MibTableColumn
wfDs1E1LineStatRxShortFrames = _WfDs1E1LineStatRxShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 13),
    _WfDs1E1LineStatRxShortFrames_Type()
)
wfDs1E1LineStatRxShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxShortFrames.setStatus("mandatory")
_WfDs1E1LineStatRxCRCErrors_Type = Counter32
_WfDs1E1LineStatRxCRCErrors_Object = MibTableColumn
wfDs1E1LineStatRxCRCErrors = _WfDs1E1LineStatRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 14),
    _WfDs1E1LineStatRxCRCErrors_Type()
)
wfDs1E1LineStatRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxCRCErrors.setStatus("mandatory")
_WfDs1E1LineStatRxNonOctetBits_Type = Counter32
_WfDs1E1LineStatRxNonOctetBits_Object = MibTableColumn
wfDs1E1LineStatRxNonOctetBits = _WfDs1E1LineStatRxNonOctetBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 15),
    _WfDs1E1LineStatRxNonOctetBits_Type()
)
wfDs1E1LineStatRxNonOctetBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxNonOctetBits.setStatus("mandatory")
_WfDs1E1LineStatRxLongFrames_Type = Counter32
_WfDs1E1LineStatRxLongFrames_Object = MibTableColumn
wfDs1E1LineStatRxLongFrames = _WfDs1E1LineStatRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 16),
    _WfDs1E1LineStatRxLongFrames_Type()
)
wfDs1E1LineStatRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxLongFrames.setStatus("mandatory")
_WfDs1E1LineStatRxAbortFrames_Type = Counter32
_WfDs1E1LineStatRxAbortFrames_Object = MibTableColumn
wfDs1E1LineStatRxAbortFrames = _WfDs1E1LineStatRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 22, 1, 17),
    _WfDs1E1LineStatRxAbortFrames_Type()
)
wfDs1E1LineStatRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1LineStatRxAbortFrames.setStatus("mandatory")
_WfDs1E1DayCurrentTable_Object = MibTable
wfDs1E1DayCurrentTable = _WfDs1E1DayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24)
)
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentTable.setStatus("mandatory")
_WfDs1E1DayCurrentEntry_Object = MibTableRow
wfDs1E1DayCurrentEntry = _WfDs1E1DayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1)
)
wfDs1E1DayCurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1DayCurrentPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentEntry.setStatus("mandatory")
_WfDs1E1DayCurrentPortLineNumber_Type = Integer32
_WfDs1E1DayCurrentPortLineNumber_Object = MibTableColumn
wfDs1E1DayCurrentPortLineNumber = _WfDs1E1DayCurrentPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 1),
    _WfDs1E1DayCurrentPortLineNumber_Type()
)
wfDs1E1DayCurrentPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentPortLineNumber.setStatus("mandatory")
_WfDs1E1DayCurrentESs_Type = Gauge32
_WfDs1E1DayCurrentESs_Object = MibTableColumn
wfDs1E1DayCurrentESs = _WfDs1E1DayCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 2),
    _WfDs1E1DayCurrentESs_Type()
)
wfDs1E1DayCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentESs.setStatus("mandatory")
_WfDs1E1DayCurrentSESs_Type = Gauge32
_WfDs1E1DayCurrentSESs_Object = MibTableColumn
wfDs1E1DayCurrentSESs = _WfDs1E1DayCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 3),
    _WfDs1E1DayCurrentSESs_Type()
)
wfDs1E1DayCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentSESs.setStatus("mandatory")
_WfDs1E1DayCurrentSEFSs_Type = Gauge32
_WfDs1E1DayCurrentSEFSs_Object = MibTableColumn
wfDs1E1DayCurrentSEFSs = _WfDs1E1DayCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 4),
    _WfDs1E1DayCurrentSEFSs_Type()
)
wfDs1E1DayCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentSEFSs.setStatus("mandatory")
_WfDs1E1DayCurrentUASs_Type = Gauge32
_WfDs1E1DayCurrentUASs_Object = MibTableColumn
wfDs1E1DayCurrentUASs = _WfDs1E1DayCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 5),
    _WfDs1E1DayCurrentUASs_Type()
)
wfDs1E1DayCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentUASs.setStatus("mandatory")
_WfDs1E1DayCurrentCSSs_Type = Gauge32
_WfDs1E1DayCurrentCSSs_Object = MibTableColumn
wfDs1E1DayCurrentCSSs = _WfDs1E1DayCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 6),
    _WfDs1E1DayCurrentCSSs_Type()
)
wfDs1E1DayCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentCSSs.setStatus("mandatory")
_WfDs1E1DayCurrentPCVs_Type = Gauge32
_WfDs1E1DayCurrentPCVs_Object = MibTableColumn
wfDs1E1DayCurrentPCVs = _WfDs1E1DayCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 7),
    _WfDs1E1DayCurrentPCVs_Type()
)
wfDs1E1DayCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentPCVs.setStatus("mandatory")
_WfDs1E1DayCurrentLESs_Type = Gauge32
_WfDs1E1DayCurrentLESs_Object = MibTableColumn
wfDs1E1DayCurrentLESs = _WfDs1E1DayCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 8),
    _WfDs1E1DayCurrentLESs_Type()
)
wfDs1E1DayCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentLESs.setStatus("mandatory")
_WfDs1E1DayCurrentBESs_Type = Gauge32
_WfDs1E1DayCurrentBESs_Object = MibTableColumn
wfDs1E1DayCurrentBESs = _WfDs1E1DayCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 9),
    _WfDs1E1DayCurrentBESs_Type()
)
wfDs1E1DayCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentBESs.setStatus("mandatory")
_WfDs1E1DayCurrentDMs_Type = Gauge32
_WfDs1E1DayCurrentDMs_Object = MibTableColumn
wfDs1E1DayCurrentDMs = _WfDs1E1DayCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 10),
    _WfDs1E1DayCurrentDMs_Type()
)
wfDs1E1DayCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentDMs.setStatus("mandatory")
_WfDs1E1DayCurrentLCVs_Type = Gauge32
_WfDs1E1DayCurrentLCVs_Object = MibTableColumn
wfDs1E1DayCurrentLCVs = _WfDs1E1DayCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 11),
    _WfDs1E1DayCurrentLCVs_Type()
)
wfDs1E1DayCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentLCVs.setStatus("mandatory")
_WfDs1E1DayCurrentSASs_Type = Gauge32
_WfDs1E1DayCurrentSASs_Object = MibTableColumn
wfDs1E1DayCurrentSASs = _WfDs1E1DayCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 12),
    _WfDs1E1DayCurrentSASs_Type()
)
wfDs1E1DayCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentSASs.setStatus("mandatory")
_WfDs1E1DayCurrentAISSs_Type = Gauge32
_WfDs1E1DayCurrentAISSs_Object = MibTableColumn
wfDs1E1DayCurrentAISSs = _WfDs1E1DayCurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 13),
    _WfDs1E1DayCurrentAISSs_Type()
)
wfDs1E1DayCurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentAISSs.setStatus("mandatory")
_WfDs1E1DayCurrentFCs_Type = Gauge32
_WfDs1E1DayCurrentFCs_Object = MibTableColumn
wfDs1E1DayCurrentFCs = _WfDs1E1DayCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 14),
    _WfDs1E1DayCurrentFCs_Type()
)
wfDs1E1DayCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentFCs.setStatus("mandatory")
_WfDs1E1DayCurrentTimeElapsed_Type = Integer32
_WfDs1E1DayCurrentTimeElapsed_Object = MibTableColumn
wfDs1E1DayCurrentTimeElapsed = _WfDs1E1DayCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 15),
    _WfDs1E1DayCurrentTimeElapsed_Type()
)
wfDs1E1DayCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentTimeElapsed.setStatus("mandatory")
_WfDs1E1DayCurrentValidIntervals_Type = Integer32
_WfDs1E1DayCurrentValidIntervals_Object = MibTableColumn
wfDs1E1DayCurrentValidIntervals = _WfDs1E1DayCurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 16),
    _WfDs1E1DayCurrentValidIntervals_Type()
)
wfDs1E1DayCurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentValidIntervals.setStatus("mandatory")


class _WfDs1E1DayCurrentValidFlag_Type(Integer32):
    """Custom type wfDs1E1DayCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1DayCurrentValidFlag_Type.__name__ = "Integer32"
_WfDs1E1DayCurrentValidFlag_Object = MibTableColumn
wfDs1E1DayCurrentValidFlag = _WfDs1E1DayCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 24, 1, 17),
    _WfDs1E1DayCurrentValidFlag_Type()
)
wfDs1E1DayCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayCurrentValidFlag.setStatus("mandatory")
_WfDs1E1DayIntervalTable_Object = MibTable
wfDs1E1DayIntervalTable = _WfDs1E1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25)
)
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalTable.setStatus("mandatory")
_WfDs1E1DayIntervalEntry_Object = MibTableRow
wfDs1E1DayIntervalEntry = _WfDs1E1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1)
)
wfDs1E1DayIntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1DayIntervalPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalEntry.setStatus("mandatory")
_WfDs1E1DayIntervalPortLineNumber_Type = Integer32
_WfDs1E1DayIntervalPortLineNumber_Object = MibTableColumn
wfDs1E1DayIntervalPortLineNumber = _WfDs1E1DayIntervalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 1),
    _WfDs1E1DayIntervalPortLineNumber_Type()
)
wfDs1E1DayIntervalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalPortLineNumber.setStatus("mandatory")
_WfDs1E1DayIntervalNumber_Type = Integer32
_WfDs1E1DayIntervalNumber_Object = MibTableColumn
wfDs1E1DayIntervalNumber = _WfDs1E1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 2),
    _WfDs1E1DayIntervalNumber_Type()
)
wfDs1E1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalNumber.setStatus("mandatory")
_WfDs1E1DayIntervalESs_Type = Gauge32
_WfDs1E1DayIntervalESs_Object = MibTableColumn
wfDs1E1DayIntervalESs = _WfDs1E1DayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 3),
    _WfDs1E1DayIntervalESs_Type()
)
wfDs1E1DayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalESs.setStatus("mandatory")
_WfDs1E1DayIntervalSESs_Type = Gauge32
_WfDs1E1DayIntervalSESs_Object = MibTableColumn
wfDs1E1DayIntervalSESs = _WfDs1E1DayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 4),
    _WfDs1E1DayIntervalSESs_Type()
)
wfDs1E1DayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalSESs.setStatus("mandatory")
_WfDs1E1DayIntervalSEFSs_Type = Gauge32
_WfDs1E1DayIntervalSEFSs_Object = MibTableColumn
wfDs1E1DayIntervalSEFSs = _WfDs1E1DayIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 5),
    _WfDs1E1DayIntervalSEFSs_Type()
)
wfDs1E1DayIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalSEFSs.setStatus("mandatory")
_WfDs1E1DayIntervalUASs_Type = Gauge32
_WfDs1E1DayIntervalUASs_Object = MibTableColumn
wfDs1E1DayIntervalUASs = _WfDs1E1DayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 6),
    _WfDs1E1DayIntervalUASs_Type()
)
wfDs1E1DayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalUASs.setStatus("mandatory")
_WfDs1E1DayIntervalCSSs_Type = Gauge32
_WfDs1E1DayIntervalCSSs_Object = MibTableColumn
wfDs1E1DayIntervalCSSs = _WfDs1E1DayIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 7),
    _WfDs1E1DayIntervalCSSs_Type()
)
wfDs1E1DayIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalCSSs.setStatus("mandatory")
_WfDs1E1DayIntervalPCVs_Type = Gauge32
_WfDs1E1DayIntervalPCVs_Object = MibTableColumn
wfDs1E1DayIntervalPCVs = _WfDs1E1DayIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 8),
    _WfDs1E1DayIntervalPCVs_Type()
)
wfDs1E1DayIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalPCVs.setStatus("mandatory")
_WfDs1E1DayIntervalLESs_Type = Gauge32
_WfDs1E1DayIntervalLESs_Object = MibTableColumn
wfDs1E1DayIntervalLESs = _WfDs1E1DayIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 9),
    _WfDs1E1DayIntervalLESs_Type()
)
wfDs1E1DayIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalLESs.setStatus("mandatory")
_WfDs1E1DayIntervalBESs_Type = Gauge32
_WfDs1E1DayIntervalBESs_Object = MibTableColumn
wfDs1E1DayIntervalBESs = _WfDs1E1DayIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 10),
    _WfDs1E1DayIntervalBESs_Type()
)
wfDs1E1DayIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalBESs.setStatus("mandatory")
_WfDs1E1DayIntervalDMs_Type = Gauge32
_WfDs1E1DayIntervalDMs_Object = MibTableColumn
wfDs1E1DayIntervalDMs = _WfDs1E1DayIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 11),
    _WfDs1E1DayIntervalDMs_Type()
)
wfDs1E1DayIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalDMs.setStatus("mandatory")
_WfDs1E1DayIntervalLCVs_Type = Gauge32
_WfDs1E1DayIntervalLCVs_Object = MibTableColumn
wfDs1E1DayIntervalLCVs = _WfDs1E1DayIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 12),
    _WfDs1E1DayIntervalLCVs_Type()
)
wfDs1E1DayIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalLCVs.setStatus("mandatory")
_WfDs1E1DayIntervalSASs_Type = Gauge32
_WfDs1E1DayIntervalSASs_Object = MibTableColumn
wfDs1E1DayIntervalSASs = _WfDs1E1DayIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 13),
    _WfDs1E1DayIntervalSASs_Type()
)
wfDs1E1DayIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalSASs.setStatus("mandatory")
_WfDs1E1DayIntervalAISSs_Type = Gauge32
_WfDs1E1DayIntervalAISSs_Object = MibTableColumn
wfDs1E1DayIntervalAISSs = _WfDs1E1DayIntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 14),
    _WfDs1E1DayIntervalAISSs_Type()
)
wfDs1E1DayIntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalAISSs.setStatus("mandatory")
_WfDs1E1DayIntervalFCs_Type = Gauge32
_WfDs1E1DayIntervalFCs_Object = MibTableColumn
wfDs1E1DayIntervalFCs = _WfDs1E1DayIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 15),
    _WfDs1E1DayIntervalFCs_Type()
)
wfDs1E1DayIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalFCs.setStatus("mandatory")


class _WfDs1E1DayIntervalValidFlag_Type(Integer32):
    """Custom type wfDs1E1DayIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1DayIntervalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1DayIntervalValidFlag_Object = MibTableColumn
wfDs1E1DayIntervalValidFlag = _WfDs1E1DayIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 25, 1, 16),
    _WfDs1E1DayIntervalValidFlag_Type()
)
wfDs1E1DayIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayIntervalValidFlag.setStatus("mandatory")
_WfDs1E1DayTotalTable_Object = MibTable
wfDs1E1DayTotalTable = _WfDs1E1DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26)
)
if mibBuilder.loadTexts:
    wfDs1E1DayTotalTable.setStatus("mandatory")
_WfDs1E1DayTotalEntry_Object = MibTableRow
wfDs1E1DayTotalEntry = _WfDs1E1DayTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1)
)
wfDs1E1DayTotalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1DayTotalPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1DayTotalEntry.setStatus("mandatory")
_WfDs1E1DayTotalPortLineNumber_Type = Integer32
_WfDs1E1DayTotalPortLineNumber_Object = MibTableColumn
wfDs1E1DayTotalPortLineNumber = _WfDs1E1DayTotalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 1),
    _WfDs1E1DayTotalPortLineNumber_Type()
)
wfDs1E1DayTotalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalPortLineNumber.setStatus("mandatory")
_WfDs1E1DayTotalESs_Type = Gauge32
_WfDs1E1DayTotalESs_Object = MibTableColumn
wfDs1E1DayTotalESs = _WfDs1E1DayTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 2),
    _WfDs1E1DayTotalESs_Type()
)
wfDs1E1DayTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalESs.setStatus("mandatory")
_WfDs1E1DayTotalSESs_Type = Gauge32
_WfDs1E1DayTotalSESs_Object = MibTableColumn
wfDs1E1DayTotalSESs = _WfDs1E1DayTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 3),
    _WfDs1E1DayTotalSESs_Type()
)
wfDs1E1DayTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalSESs.setStatus("mandatory")
_WfDs1E1DayTotalSEFSs_Type = Gauge32
_WfDs1E1DayTotalSEFSs_Object = MibTableColumn
wfDs1E1DayTotalSEFSs = _WfDs1E1DayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 4),
    _WfDs1E1DayTotalSEFSs_Type()
)
wfDs1E1DayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalSEFSs.setStatus("mandatory")
_WfDs1E1DayTotalUASs_Type = Gauge32
_WfDs1E1DayTotalUASs_Object = MibTableColumn
wfDs1E1DayTotalUASs = _WfDs1E1DayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 5),
    _WfDs1E1DayTotalUASs_Type()
)
wfDs1E1DayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalUASs.setStatus("mandatory")
_WfDs1E1DayTotalCSSs_Type = Gauge32
_WfDs1E1DayTotalCSSs_Object = MibTableColumn
wfDs1E1DayTotalCSSs = _WfDs1E1DayTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 6),
    _WfDs1E1DayTotalCSSs_Type()
)
wfDs1E1DayTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalCSSs.setStatus("mandatory")
_WfDs1E1DayTotalPCVs_Type = Gauge32
_WfDs1E1DayTotalPCVs_Object = MibTableColumn
wfDs1E1DayTotalPCVs = _WfDs1E1DayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 7),
    _WfDs1E1DayTotalPCVs_Type()
)
wfDs1E1DayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalPCVs.setStatus("mandatory")
_WfDs1E1DayTotalLESs_Type = Gauge32
_WfDs1E1DayTotalLESs_Object = MibTableColumn
wfDs1E1DayTotalLESs = _WfDs1E1DayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 8),
    _WfDs1E1DayTotalLESs_Type()
)
wfDs1E1DayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalLESs.setStatus("mandatory")
_WfDs1E1DayTotalBESs_Type = Gauge32
_WfDs1E1DayTotalBESs_Object = MibTableColumn
wfDs1E1DayTotalBESs = _WfDs1E1DayTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 9),
    _WfDs1E1DayTotalBESs_Type()
)
wfDs1E1DayTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalBESs.setStatus("mandatory")
_WfDs1E1DayTotalDMs_Type = Gauge32
_WfDs1E1DayTotalDMs_Object = MibTableColumn
wfDs1E1DayTotalDMs = _WfDs1E1DayTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 10),
    _WfDs1E1DayTotalDMs_Type()
)
wfDs1E1DayTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalDMs.setStatus("mandatory")
_WfDs1E1DayTotalLCVs_Type = Gauge32
_WfDs1E1DayTotalLCVs_Object = MibTableColumn
wfDs1E1DayTotalLCVs = _WfDs1E1DayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 11),
    _WfDs1E1DayTotalLCVs_Type()
)
wfDs1E1DayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalLCVs.setStatus("mandatory")
_WfDs1E1DayTotalSASs_Type = Gauge32
_WfDs1E1DayTotalSASs_Object = MibTableColumn
wfDs1E1DayTotalSASs = _WfDs1E1DayTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 12),
    _WfDs1E1DayTotalSASs_Type()
)
wfDs1E1DayTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalSASs.setStatus("mandatory")
_WfDs1E1DayTotalAISSs_Type = Gauge32
_WfDs1E1DayTotalAISSs_Object = MibTableColumn
wfDs1E1DayTotalAISSs = _WfDs1E1DayTotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 13),
    _WfDs1E1DayTotalAISSs_Type()
)
wfDs1E1DayTotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalAISSs.setStatus("mandatory")
_WfDs1E1DayTotalFCs_Type = Gauge32
_WfDs1E1DayTotalFCs_Object = MibTableColumn
wfDs1E1DayTotalFCs = _WfDs1E1DayTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 14),
    _WfDs1E1DayTotalFCs_Type()
)
wfDs1E1DayTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalFCs.setStatus("mandatory")


class _WfDs1E1DayTotalValidFlag_Type(Integer32):
    """Custom type wfDs1E1DayTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1DayTotalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1DayTotalValidFlag_Object = MibTableColumn
wfDs1E1DayTotalValidFlag = _WfDs1E1DayTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 26, 1, 15),
    _WfDs1E1DayTotalValidFlag_Type()
)
wfDs1E1DayTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayTotalValidFlag.setStatus("mandatory")
_WfDs1E1FarEndCurrentTable_Object = MibTable
wfDs1E1FarEndCurrentTable = _WfDs1E1FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentTable.setStatus("mandatory")
_WfDs1E1FarEndCurrentEntry_Object = MibTableRow
wfDs1E1FarEndCurrentEntry = _WfDs1E1FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1)
)
wfDs1E1FarEndCurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndCurrentPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentEntry.setStatus("mandatory")
_WfDs1E1FarEndCurrentPortLineNumber_Type = Integer32
_WfDs1E1FarEndCurrentPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndCurrentPortLineNumber = _WfDs1E1FarEndCurrentPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 1),
    _WfDs1E1FarEndCurrentPortLineNumber_Type()
)
wfDs1E1FarEndCurrentPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndCurrentESs_Type = Gauge32
_WfDs1E1FarEndCurrentESs_Object = MibTableColumn
wfDs1E1FarEndCurrentESs = _WfDs1E1FarEndCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 2),
    _WfDs1E1FarEndCurrentESs_Type()
)
wfDs1E1FarEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentESs.setStatus("mandatory")
_WfDs1E1FarEndCurrentSESs_Type = Gauge32
_WfDs1E1FarEndCurrentSESs_Object = MibTableColumn
wfDs1E1FarEndCurrentSESs = _WfDs1E1FarEndCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 3),
    _WfDs1E1FarEndCurrentSESs_Type()
)
wfDs1E1FarEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentSESs.setStatus("mandatory")
_WfDs1E1FarEndCurrentSEFSs_Type = Gauge32
_WfDs1E1FarEndCurrentSEFSs_Object = MibTableColumn
wfDs1E1FarEndCurrentSEFSs = _WfDs1E1FarEndCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 4),
    _WfDs1E1FarEndCurrentSEFSs_Type()
)
wfDs1E1FarEndCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentSEFSs.setStatus("mandatory")
_WfDs1E1FarEndCurrentUASs_Type = Gauge32
_WfDs1E1FarEndCurrentUASs_Object = MibTableColumn
wfDs1E1FarEndCurrentUASs = _WfDs1E1FarEndCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 5),
    _WfDs1E1FarEndCurrentUASs_Type()
)
wfDs1E1FarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentUASs.setStatus("mandatory")
_WfDs1E1FarEndCurrentCSSs_Type = Gauge32
_WfDs1E1FarEndCurrentCSSs_Object = MibTableColumn
wfDs1E1FarEndCurrentCSSs = _WfDs1E1FarEndCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 6),
    _WfDs1E1FarEndCurrentCSSs_Type()
)
wfDs1E1FarEndCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentCSSs.setStatus("mandatory")
_WfDs1E1FarEndCurrentPCVs_Type = Gauge32
_WfDs1E1FarEndCurrentPCVs_Object = MibTableColumn
wfDs1E1FarEndCurrentPCVs = _WfDs1E1FarEndCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 7),
    _WfDs1E1FarEndCurrentPCVs_Type()
)
wfDs1E1FarEndCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentPCVs.setStatus("mandatory")
_WfDs1E1FarEndCurrentLESs_Type = Gauge32
_WfDs1E1FarEndCurrentLESs_Object = MibTableColumn
wfDs1E1FarEndCurrentLESs = _WfDs1E1FarEndCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 8),
    _WfDs1E1FarEndCurrentLESs_Type()
)
wfDs1E1FarEndCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentLESs.setStatus("mandatory")
_WfDs1E1FarEndCurrentBESs_Type = Gauge32
_WfDs1E1FarEndCurrentBESs_Object = MibTableColumn
wfDs1E1FarEndCurrentBESs = _WfDs1E1FarEndCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 9),
    _WfDs1E1FarEndCurrentBESs_Type()
)
wfDs1E1FarEndCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentBESs.setStatus("mandatory")
_WfDs1E1FarEndCurrentDMs_Type = Gauge32
_WfDs1E1FarEndCurrentDMs_Object = MibTableColumn
wfDs1E1FarEndCurrentDMs = _WfDs1E1FarEndCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 10),
    _WfDs1E1FarEndCurrentDMs_Type()
)
wfDs1E1FarEndCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentDMs.setStatus("mandatory")
_WfDs1E1FarEndCurrentLCVs_Type = Gauge32
_WfDs1E1FarEndCurrentLCVs_Object = MibTableColumn
wfDs1E1FarEndCurrentLCVs = _WfDs1E1FarEndCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 11),
    _WfDs1E1FarEndCurrentLCVs_Type()
)
wfDs1E1FarEndCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentLCVs.setStatus("mandatory")
_WfDs1E1FarEndCurrentSASs_Type = Gauge32
_WfDs1E1FarEndCurrentSASs_Object = MibTableColumn
wfDs1E1FarEndCurrentSASs = _WfDs1E1FarEndCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 12),
    _WfDs1E1FarEndCurrentSASs_Type()
)
wfDs1E1FarEndCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentSASs.setStatus("mandatory")
_WfDs1E1FarEndCurrentAISSs_Type = Gauge32
_WfDs1E1FarEndCurrentAISSs_Object = MibTableColumn
wfDs1E1FarEndCurrentAISSs = _WfDs1E1FarEndCurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 13),
    _WfDs1E1FarEndCurrentAISSs_Type()
)
wfDs1E1FarEndCurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentAISSs.setStatus("mandatory")
_WfDs1E1FarEndCurrentFCs_Type = Gauge32
_WfDs1E1FarEndCurrentFCs_Object = MibTableColumn
wfDs1E1FarEndCurrentFCs = _WfDs1E1FarEndCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 14),
    _WfDs1E1FarEndCurrentFCs_Type()
)
wfDs1E1FarEndCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentFCs.setStatus("mandatory")
_WfDs1E1FarEndCurrentTimeElapsed_Type = Integer32
_WfDs1E1FarEndCurrentTimeElapsed_Object = MibTableColumn
wfDs1E1FarEndCurrentTimeElapsed = _WfDs1E1FarEndCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 15),
    _WfDs1E1FarEndCurrentTimeElapsed_Type()
)
wfDs1E1FarEndCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentTimeElapsed.setStatus("mandatory")
_WfDs1E1FarEndCurrentValidIntervals_Type = Integer32
_WfDs1E1FarEndCurrentValidIntervals_Object = MibTableColumn
wfDs1E1FarEndCurrentValidIntervals = _WfDs1E1FarEndCurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 16),
    _WfDs1E1FarEndCurrentValidIntervals_Type()
)
wfDs1E1FarEndCurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentValidIntervals.setStatus("mandatory")


class _WfDs1E1FarEndCurrentValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndCurrentValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndCurrentValidFlag_Object = MibTableColumn
wfDs1E1FarEndCurrentValidFlag = _WfDs1E1FarEndCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 27, 1, 17),
    _WfDs1E1FarEndCurrentValidFlag_Type()
)
wfDs1E1FarEndCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndCurrentValidFlag.setStatus("mandatory")
_WfDs1E1FarEndIntervalTable_Object = MibTable
wfDs1E1FarEndIntervalTable = _WfDs1E1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalTable.setStatus("mandatory")
_WfDs1E1FarEndIntervalEntry_Object = MibTableRow
wfDs1E1FarEndIntervalEntry = _WfDs1E1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1)
)
wfDs1E1FarEndIntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndIntervalPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalEntry.setStatus("mandatory")
_WfDs1E1FarEndIntervalPortLineNumber_Type = Integer32
_WfDs1E1FarEndIntervalPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndIntervalPortLineNumber = _WfDs1E1FarEndIntervalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 1),
    _WfDs1E1FarEndIntervalPortLineNumber_Type()
)
wfDs1E1FarEndIntervalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndIntervalNumber_Type = Integer32
_WfDs1E1FarEndIntervalNumber_Object = MibTableColumn
wfDs1E1FarEndIntervalNumber = _WfDs1E1FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 2),
    _WfDs1E1FarEndIntervalNumber_Type()
)
wfDs1E1FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalNumber.setStatus("mandatory")
_WfDs1E1FarEndIntervalESs_Type = Gauge32
_WfDs1E1FarEndIntervalESs_Object = MibTableColumn
wfDs1E1FarEndIntervalESs = _WfDs1E1FarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 3),
    _WfDs1E1FarEndIntervalESs_Type()
)
wfDs1E1FarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalESs.setStatus("mandatory")
_WfDs1E1FarEndIntervalSESs_Type = Gauge32
_WfDs1E1FarEndIntervalSESs_Object = MibTableColumn
wfDs1E1FarEndIntervalSESs = _WfDs1E1FarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 4),
    _WfDs1E1FarEndIntervalSESs_Type()
)
wfDs1E1FarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalSESs.setStatus("mandatory")
_WfDs1E1FarEndIntervalSEFSs_Type = Gauge32
_WfDs1E1FarEndIntervalSEFSs_Object = MibTableColumn
wfDs1E1FarEndIntervalSEFSs = _WfDs1E1FarEndIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 5),
    _WfDs1E1FarEndIntervalSEFSs_Type()
)
wfDs1E1FarEndIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalSEFSs.setStatus("mandatory")
_WfDs1E1FarEndIntervalUASs_Type = Gauge32
_WfDs1E1FarEndIntervalUASs_Object = MibTableColumn
wfDs1E1FarEndIntervalUASs = _WfDs1E1FarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 6),
    _WfDs1E1FarEndIntervalUASs_Type()
)
wfDs1E1FarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalUASs.setStatus("mandatory")
_WfDs1E1FarEndIntervalCSSs_Type = Gauge32
_WfDs1E1FarEndIntervalCSSs_Object = MibTableColumn
wfDs1E1FarEndIntervalCSSs = _WfDs1E1FarEndIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 7),
    _WfDs1E1FarEndIntervalCSSs_Type()
)
wfDs1E1FarEndIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalCSSs.setStatus("mandatory")
_WfDs1E1FarEndIntervalPCVs_Type = Gauge32
_WfDs1E1FarEndIntervalPCVs_Object = MibTableColumn
wfDs1E1FarEndIntervalPCVs = _WfDs1E1FarEndIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 8),
    _WfDs1E1FarEndIntervalPCVs_Type()
)
wfDs1E1FarEndIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalPCVs.setStatus("mandatory")
_WfDs1E1FarEndIntervalLESs_Type = Gauge32
_WfDs1E1FarEndIntervalLESs_Object = MibTableColumn
wfDs1E1FarEndIntervalLESs = _WfDs1E1FarEndIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 9),
    _WfDs1E1FarEndIntervalLESs_Type()
)
wfDs1E1FarEndIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalLESs.setStatus("mandatory")
_WfDs1E1FarEndIntervalBESs_Type = Gauge32
_WfDs1E1FarEndIntervalBESs_Object = MibTableColumn
wfDs1E1FarEndIntervalBESs = _WfDs1E1FarEndIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 10),
    _WfDs1E1FarEndIntervalBESs_Type()
)
wfDs1E1FarEndIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalBESs.setStatus("mandatory")
_WfDs1E1FarEndIntervalDMs_Type = Gauge32
_WfDs1E1FarEndIntervalDMs_Object = MibTableColumn
wfDs1E1FarEndIntervalDMs = _WfDs1E1FarEndIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 11),
    _WfDs1E1FarEndIntervalDMs_Type()
)
wfDs1E1FarEndIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalDMs.setStatus("mandatory")
_WfDs1E1FarEndIntervalLCVs_Type = Gauge32
_WfDs1E1FarEndIntervalLCVs_Object = MibTableColumn
wfDs1E1FarEndIntervalLCVs = _WfDs1E1FarEndIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 12),
    _WfDs1E1FarEndIntervalLCVs_Type()
)
wfDs1E1FarEndIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalLCVs.setStatus("mandatory")
_WfDs1E1FarEndIntervalSASs_Type = Gauge32
_WfDs1E1FarEndIntervalSASs_Object = MibTableColumn
wfDs1E1FarEndIntervalSASs = _WfDs1E1FarEndIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 13),
    _WfDs1E1FarEndIntervalSASs_Type()
)
wfDs1E1FarEndIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalSASs.setStatus("mandatory")
_WfDs1E1FarEndIntervalAISSs_Type = Gauge32
_WfDs1E1FarEndIntervalAISSs_Object = MibTableColumn
wfDs1E1FarEndIntervalAISSs = _WfDs1E1FarEndIntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 14),
    _WfDs1E1FarEndIntervalAISSs_Type()
)
wfDs1E1FarEndIntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalAISSs.setStatus("mandatory")
_WfDs1E1FarEndIntervalFCs_Type = Gauge32
_WfDs1E1FarEndIntervalFCs_Object = MibTableColumn
wfDs1E1FarEndIntervalFCs = _WfDs1E1FarEndIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 15),
    _WfDs1E1FarEndIntervalFCs_Type()
)
wfDs1E1FarEndIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalFCs.setStatus("mandatory")


class _WfDs1E1FarEndIntervalValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndIntervalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndIntervalValidFlag_Object = MibTableColumn
wfDs1E1FarEndIntervalValidFlag = _WfDs1E1FarEndIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 28, 1, 16),
    _WfDs1E1FarEndIntervalValidFlag_Type()
)
wfDs1E1FarEndIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndIntervalValidFlag.setStatus("mandatory")
_WfDs1E1FarEndTotalTable_Object = MibTable
wfDs1E1FarEndTotalTable = _WfDs1E1FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalTable.setStatus("mandatory")
_WfDs1E1FarEndTotalEntry_Object = MibTableRow
wfDs1E1FarEndTotalEntry = _WfDs1E1FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1)
)
wfDs1E1FarEndTotalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndTotalPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalEntry.setStatus("mandatory")
_WfDs1E1FarEndTotalPortLineNumber_Type = Integer32
_WfDs1E1FarEndTotalPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndTotalPortLineNumber = _WfDs1E1FarEndTotalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 1),
    _WfDs1E1FarEndTotalPortLineNumber_Type()
)
wfDs1E1FarEndTotalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndTotalESs_Type = Gauge32
_WfDs1E1FarEndTotalESs_Object = MibTableColumn
wfDs1E1FarEndTotalESs = _WfDs1E1FarEndTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 2),
    _WfDs1E1FarEndTotalESs_Type()
)
wfDs1E1FarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalESs.setStatus("mandatory")
_WfDs1E1FarEndTotalSESs_Type = Gauge32
_WfDs1E1FarEndTotalSESs_Object = MibTableColumn
wfDs1E1FarEndTotalSESs = _WfDs1E1FarEndTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 3),
    _WfDs1E1FarEndTotalSESs_Type()
)
wfDs1E1FarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalSESs.setStatus("mandatory")
_WfDs1E1FarEndTotalSEFSs_Type = Gauge32
_WfDs1E1FarEndTotalSEFSs_Object = MibTableColumn
wfDs1E1FarEndTotalSEFSs = _WfDs1E1FarEndTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 4),
    _WfDs1E1FarEndTotalSEFSs_Type()
)
wfDs1E1FarEndTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalSEFSs.setStatus("mandatory")
_WfDs1E1FarEndTotalUASs_Type = Gauge32
_WfDs1E1FarEndTotalUASs_Object = MibTableColumn
wfDs1E1FarEndTotalUASs = _WfDs1E1FarEndTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 5),
    _WfDs1E1FarEndTotalUASs_Type()
)
wfDs1E1FarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalUASs.setStatus("mandatory")
_WfDs1E1FarEndTotalCSSs_Type = Gauge32
_WfDs1E1FarEndTotalCSSs_Object = MibTableColumn
wfDs1E1FarEndTotalCSSs = _WfDs1E1FarEndTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 6),
    _WfDs1E1FarEndTotalCSSs_Type()
)
wfDs1E1FarEndTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalCSSs.setStatus("mandatory")
_WfDs1E1FarEndTotalPCVs_Type = Gauge32
_WfDs1E1FarEndTotalPCVs_Object = MibTableColumn
wfDs1E1FarEndTotalPCVs = _WfDs1E1FarEndTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 7),
    _WfDs1E1FarEndTotalPCVs_Type()
)
wfDs1E1FarEndTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalPCVs.setStatus("mandatory")
_WfDs1E1FarEndTotalLESs_Type = Gauge32
_WfDs1E1FarEndTotalLESs_Object = MibTableColumn
wfDs1E1FarEndTotalLESs = _WfDs1E1FarEndTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 8),
    _WfDs1E1FarEndTotalLESs_Type()
)
wfDs1E1FarEndTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalLESs.setStatus("mandatory")
_WfDs1E1FarEndTotalBESs_Type = Gauge32
_WfDs1E1FarEndTotalBESs_Object = MibTableColumn
wfDs1E1FarEndTotalBESs = _WfDs1E1FarEndTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 9),
    _WfDs1E1FarEndTotalBESs_Type()
)
wfDs1E1FarEndTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalBESs.setStatus("mandatory")
_WfDs1E1FarEndTotalDMs_Type = Gauge32
_WfDs1E1FarEndTotalDMs_Object = MibTableColumn
wfDs1E1FarEndTotalDMs = _WfDs1E1FarEndTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 10),
    _WfDs1E1FarEndTotalDMs_Type()
)
wfDs1E1FarEndTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalDMs.setStatus("mandatory")
_WfDs1E1FarEndTotalLCVs_Type = Gauge32
_WfDs1E1FarEndTotalLCVs_Object = MibTableColumn
wfDs1E1FarEndTotalLCVs = _WfDs1E1FarEndTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 11),
    _WfDs1E1FarEndTotalLCVs_Type()
)
wfDs1E1FarEndTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalLCVs.setStatus("mandatory")
_WfDs1E1FarEndTotalSASs_Type = Gauge32
_WfDs1E1FarEndTotalSASs_Object = MibTableColumn
wfDs1E1FarEndTotalSASs = _WfDs1E1FarEndTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 12),
    _WfDs1E1FarEndTotalSASs_Type()
)
wfDs1E1FarEndTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalSASs.setStatus("mandatory")
_WfDs1E1FarEndTotalAISSs_Type = Gauge32
_WfDs1E1FarEndTotalAISSs_Object = MibTableColumn
wfDs1E1FarEndTotalAISSs = _WfDs1E1FarEndTotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 13),
    _WfDs1E1FarEndTotalAISSs_Type()
)
wfDs1E1FarEndTotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalAISSs.setStatus("mandatory")
_WfDs1E1FarEndTotalFCs_Type = Gauge32
_WfDs1E1FarEndTotalFCs_Object = MibTableColumn
wfDs1E1FarEndTotalFCs = _WfDs1E1FarEndTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 14),
    _WfDs1E1FarEndTotalFCs_Type()
)
wfDs1E1FarEndTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalFCs.setStatus("mandatory")


class _WfDs1E1FarEndTotalValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndTotalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndTotalValidFlag_Object = MibTableColumn
wfDs1E1FarEndTotalValidFlag = _WfDs1E1FarEndTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 29, 1, 15),
    _WfDs1E1FarEndTotalValidFlag_Type()
)
wfDs1E1FarEndTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndTotalValidFlag.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentTable_Object = MibTable
wfDs1E1FarEndDayCurrentTable = _WfDs1E1FarEndDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentTable.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentEntry_Object = MibTableRow
wfDs1E1FarEndDayCurrentEntry = _WfDs1E1FarEndDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1)
)
wfDs1E1FarEndDayCurrentEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndDayCurrentPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentEntry.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentPortLineNumber_Type = Integer32
_WfDs1E1FarEndDayCurrentPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndDayCurrentPortLineNumber = _WfDs1E1FarEndDayCurrentPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 1),
    _WfDs1E1FarEndDayCurrentPortLineNumber_Type()
)
wfDs1E1FarEndDayCurrentPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentESs_Type = Gauge32
_WfDs1E1FarEndDayCurrentESs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentESs = _WfDs1E1FarEndDayCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 2),
    _WfDs1E1FarEndDayCurrentESs_Type()
)
wfDs1E1FarEndDayCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentESs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentSESs_Type = Gauge32
_WfDs1E1FarEndDayCurrentSESs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentSESs = _WfDs1E1FarEndDayCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 3),
    _WfDs1E1FarEndDayCurrentSESs_Type()
)
wfDs1E1FarEndDayCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentSESs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentSEFSs_Type = Gauge32
_WfDs1E1FarEndDayCurrentSEFSs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentSEFSs = _WfDs1E1FarEndDayCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 4),
    _WfDs1E1FarEndDayCurrentSEFSs_Type()
)
wfDs1E1FarEndDayCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentSEFSs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentUASs_Type = Gauge32
_WfDs1E1FarEndDayCurrentUASs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentUASs = _WfDs1E1FarEndDayCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 5),
    _WfDs1E1FarEndDayCurrentUASs_Type()
)
wfDs1E1FarEndDayCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentUASs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentCSSs_Type = Gauge32
_WfDs1E1FarEndDayCurrentCSSs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentCSSs = _WfDs1E1FarEndDayCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 6),
    _WfDs1E1FarEndDayCurrentCSSs_Type()
)
wfDs1E1FarEndDayCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentCSSs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentPCVs_Type = Gauge32
_WfDs1E1FarEndDayCurrentPCVs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentPCVs = _WfDs1E1FarEndDayCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 7),
    _WfDs1E1FarEndDayCurrentPCVs_Type()
)
wfDs1E1FarEndDayCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentPCVs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentLESs_Type = Gauge32
_WfDs1E1FarEndDayCurrentLESs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentLESs = _WfDs1E1FarEndDayCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 8),
    _WfDs1E1FarEndDayCurrentLESs_Type()
)
wfDs1E1FarEndDayCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentLESs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentBESs_Type = Gauge32
_WfDs1E1FarEndDayCurrentBESs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentBESs = _WfDs1E1FarEndDayCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 9),
    _WfDs1E1FarEndDayCurrentBESs_Type()
)
wfDs1E1FarEndDayCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentBESs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentDMs_Type = Gauge32
_WfDs1E1FarEndDayCurrentDMs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentDMs = _WfDs1E1FarEndDayCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 10),
    _WfDs1E1FarEndDayCurrentDMs_Type()
)
wfDs1E1FarEndDayCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentDMs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentLCVs_Type = Gauge32
_WfDs1E1FarEndDayCurrentLCVs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentLCVs = _WfDs1E1FarEndDayCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 11),
    _WfDs1E1FarEndDayCurrentLCVs_Type()
)
wfDs1E1FarEndDayCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentLCVs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentSASs_Type = Gauge32
_WfDs1E1FarEndDayCurrentSASs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentSASs = _WfDs1E1FarEndDayCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 12),
    _WfDs1E1FarEndDayCurrentSASs_Type()
)
wfDs1E1FarEndDayCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentSASs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentAISSs_Type = Gauge32
_WfDs1E1FarEndDayCurrentAISSs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentAISSs = _WfDs1E1FarEndDayCurrentAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 13),
    _WfDs1E1FarEndDayCurrentAISSs_Type()
)
wfDs1E1FarEndDayCurrentAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentAISSs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentFCs_Type = Gauge32
_WfDs1E1FarEndDayCurrentFCs_Object = MibTableColumn
wfDs1E1FarEndDayCurrentFCs = _WfDs1E1FarEndDayCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 14),
    _WfDs1E1FarEndDayCurrentFCs_Type()
)
wfDs1E1FarEndDayCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentFCs.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentTimeElapsed_Type = Integer32
_WfDs1E1FarEndDayCurrentTimeElapsed_Object = MibTableColumn
wfDs1E1FarEndDayCurrentTimeElapsed = _WfDs1E1FarEndDayCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 15),
    _WfDs1E1FarEndDayCurrentTimeElapsed_Type()
)
wfDs1E1FarEndDayCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentTimeElapsed.setStatus("mandatory")
_WfDs1E1FarEndDayCurrentValidIntervals_Type = Integer32
_WfDs1E1FarEndDayCurrentValidIntervals_Object = MibTableColumn
wfDs1E1FarEndDayCurrentValidIntervals = _WfDs1E1FarEndDayCurrentValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 16),
    _WfDs1E1FarEndDayCurrentValidIntervals_Type()
)
wfDs1E1FarEndDayCurrentValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentValidIntervals.setStatus("mandatory")


class _WfDs1E1FarEndDayCurrentValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndDayCurrentValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndDayCurrentValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndDayCurrentValidFlag_Object = MibTableColumn
wfDs1E1FarEndDayCurrentValidFlag = _WfDs1E1FarEndDayCurrentValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 30, 1, 17),
    _WfDs1E1FarEndDayCurrentValidFlag_Type()
)
wfDs1E1FarEndDayCurrentValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayCurrentValidFlag.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalTable_Object = MibTable
wfDs1E1FarEndDayIntervalTable = _WfDs1E1FarEndDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalTable.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalEntry_Object = MibTableRow
wfDs1E1FarEndDayIntervalEntry = _WfDs1E1FarEndDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1)
)
wfDs1E1FarEndDayIntervalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndDayIntervalPortLineNumber"),
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalEntry.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalPortLineNumber_Type = Integer32
_WfDs1E1FarEndDayIntervalPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndDayIntervalPortLineNumber = _WfDs1E1FarEndDayIntervalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 1),
    _WfDs1E1FarEndDayIntervalPortLineNumber_Type()
)
wfDs1E1FarEndDayIntervalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalNumber_Type = Integer32
_WfDs1E1FarEndDayIntervalNumber_Object = MibTableColumn
wfDs1E1FarEndDayIntervalNumber = _WfDs1E1FarEndDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 2),
    _WfDs1E1FarEndDayIntervalNumber_Type()
)
wfDs1E1FarEndDayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalNumber.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalESs_Type = Gauge32
_WfDs1E1FarEndDayIntervalESs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalESs = _WfDs1E1FarEndDayIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 3),
    _WfDs1E1FarEndDayIntervalESs_Type()
)
wfDs1E1FarEndDayIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalESs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalSESs_Type = Gauge32
_WfDs1E1FarEndDayIntervalSESs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalSESs = _WfDs1E1FarEndDayIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 4),
    _WfDs1E1FarEndDayIntervalSESs_Type()
)
wfDs1E1FarEndDayIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalSESs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalSEFSs_Type = Gauge32
_WfDs1E1FarEndDayIntervalSEFSs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalSEFSs = _WfDs1E1FarEndDayIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 5),
    _WfDs1E1FarEndDayIntervalSEFSs_Type()
)
wfDs1E1FarEndDayIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalSEFSs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalUASs_Type = Gauge32
_WfDs1E1FarEndDayIntervalUASs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalUASs = _WfDs1E1FarEndDayIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 6),
    _WfDs1E1FarEndDayIntervalUASs_Type()
)
wfDs1E1FarEndDayIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalUASs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalCSSs_Type = Gauge32
_WfDs1E1FarEndDayIntervalCSSs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalCSSs = _WfDs1E1FarEndDayIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 7),
    _WfDs1E1FarEndDayIntervalCSSs_Type()
)
wfDs1E1FarEndDayIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalCSSs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalPCVs_Type = Gauge32
_WfDs1E1FarEndDayIntervalPCVs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalPCVs = _WfDs1E1FarEndDayIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 8),
    _WfDs1E1FarEndDayIntervalPCVs_Type()
)
wfDs1E1FarEndDayIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalPCVs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalLESs_Type = Gauge32
_WfDs1E1FarEndDayIntervalLESs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalLESs = _WfDs1E1FarEndDayIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 9),
    _WfDs1E1FarEndDayIntervalLESs_Type()
)
wfDs1E1FarEndDayIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalLESs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalBESs_Type = Gauge32
_WfDs1E1FarEndDayIntervalBESs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalBESs = _WfDs1E1FarEndDayIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 10),
    _WfDs1E1FarEndDayIntervalBESs_Type()
)
wfDs1E1FarEndDayIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalBESs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalDMs_Type = Gauge32
_WfDs1E1FarEndDayIntervalDMs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalDMs = _WfDs1E1FarEndDayIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 11),
    _WfDs1E1FarEndDayIntervalDMs_Type()
)
wfDs1E1FarEndDayIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalDMs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalLCVs_Type = Gauge32
_WfDs1E1FarEndDayIntervalLCVs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalLCVs = _WfDs1E1FarEndDayIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 12),
    _WfDs1E1FarEndDayIntervalLCVs_Type()
)
wfDs1E1FarEndDayIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalLCVs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalSASs_Type = Gauge32
_WfDs1E1FarEndDayIntervalSASs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalSASs = _WfDs1E1FarEndDayIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 13),
    _WfDs1E1FarEndDayIntervalSASs_Type()
)
wfDs1E1FarEndDayIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalSASs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalAISSs_Type = Gauge32
_WfDs1E1FarEndDayIntervalAISSs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalAISSs = _WfDs1E1FarEndDayIntervalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 14),
    _WfDs1E1FarEndDayIntervalAISSs_Type()
)
wfDs1E1FarEndDayIntervalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalAISSs.setStatus("mandatory")
_WfDs1E1FarEndDayIntervalFCs_Type = Gauge32
_WfDs1E1FarEndDayIntervalFCs_Object = MibTableColumn
wfDs1E1FarEndDayIntervalFCs = _WfDs1E1FarEndDayIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 15),
    _WfDs1E1FarEndDayIntervalFCs_Type()
)
wfDs1E1FarEndDayIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalFCs.setStatus("mandatory")


class _WfDs1E1FarEndDayIntervalValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndDayIntervalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndDayIntervalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndDayIntervalValidFlag_Object = MibTableColumn
wfDs1E1FarEndDayIntervalValidFlag = _WfDs1E1FarEndDayIntervalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 31, 1, 16),
    _WfDs1E1FarEndDayIntervalValidFlag_Type()
)
wfDs1E1FarEndDayIntervalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayIntervalValidFlag.setStatus("mandatory")
_WfDs1E1FarEndDayTotalTable_Object = MibTable
wfDs1E1FarEndDayTotalTable = _WfDs1E1FarEndDayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalTable.setStatus("mandatory")
_WfDs1E1FarEndDayTotalEntry_Object = MibTableRow
wfDs1E1FarEndDayTotalEntry = _WfDs1E1FarEndDayTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1)
)
wfDs1E1FarEndDayTotalEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndDayTotalPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalEntry.setStatus("mandatory")
_WfDs1E1FarEndDayTotalPortLineNumber_Type = Integer32
_WfDs1E1FarEndDayTotalPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndDayTotalPortLineNumber = _WfDs1E1FarEndDayTotalPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 1),
    _WfDs1E1FarEndDayTotalPortLineNumber_Type()
)
wfDs1E1FarEndDayTotalPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalPortLineNumber.setStatus("mandatory")
_WfDs1E1FarEndDayTotalESs_Type = Gauge32
_WfDs1E1FarEndDayTotalESs_Object = MibTableColumn
wfDs1E1FarEndDayTotalESs = _WfDs1E1FarEndDayTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 2),
    _WfDs1E1FarEndDayTotalESs_Type()
)
wfDs1E1FarEndDayTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalESs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalSESs_Type = Gauge32
_WfDs1E1FarEndDayTotalSESs_Object = MibTableColumn
wfDs1E1FarEndDayTotalSESs = _WfDs1E1FarEndDayTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 3),
    _WfDs1E1FarEndDayTotalSESs_Type()
)
wfDs1E1FarEndDayTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalSESs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalSEFSs_Type = Gauge32
_WfDs1E1FarEndDayTotalSEFSs_Object = MibTableColumn
wfDs1E1FarEndDayTotalSEFSs = _WfDs1E1FarEndDayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 4),
    _WfDs1E1FarEndDayTotalSEFSs_Type()
)
wfDs1E1FarEndDayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalSEFSs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalUASs_Type = Gauge32
_WfDs1E1FarEndDayTotalUASs_Object = MibTableColumn
wfDs1E1FarEndDayTotalUASs = _WfDs1E1FarEndDayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 5),
    _WfDs1E1FarEndDayTotalUASs_Type()
)
wfDs1E1FarEndDayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalUASs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalCSSs_Type = Gauge32
_WfDs1E1FarEndDayTotalCSSs_Object = MibTableColumn
wfDs1E1FarEndDayTotalCSSs = _WfDs1E1FarEndDayTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 6),
    _WfDs1E1FarEndDayTotalCSSs_Type()
)
wfDs1E1FarEndDayTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalCSSs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalPCVs_Type = Gauge32
_WfDs1E1FarEndDayTotalPCVs_Object = MibTableColumn
wfDs1E1FarEndDayTotalPCVs = _WfDs1E1FarEndDayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 7),
    _WfDs1E1FarEndDayTotalPCVs_Type()
)
wfDs1E1FarEndDayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalPCVs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalLESs_Type = Gauge32
_WfDs1E1FarEndDayTotalLESs_Object = MibTableColumn
wfDs1E1FarEndDayTotalLESs = _WfDs1E1FarEndDayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 8),
    _WfDs1E1FarEndDayTotalLESs_Type()
)
wfDs1E1FarEndDayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalLESs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalBESs_Type = Gauge32
_WfDs1E1FarEndDayTotalBESs_Object = MibTableColumn
wfDs1E1FarEndDayTotalBESs = _WfDs1E1FarEndDayTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 9),
    _WfDs1E1FarEndDayTotalBESs_Type()
)
wfDs1E1FarEndDayTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalBESs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalDMs_Type = Gauge32
_WfDs1E1FarEndDayTotalDMs_Object = MibTableColumn
wfDs1E1FarEndDayTotalDMs = _WfDs1E1FarEndDayTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 10),
    _WfDs1E1FarEndDayTotalDMs_Type()
)
wfDs1E1FarEndDayTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalDMs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalLCVs_Type = Gauge32
_WfDs1E1FarEndDayTotalLCVs_Object = MibTableColumn
wfDs1E1FarEndDayTotalLCVs = _WfDs1E1FarEndDayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 11),
    _WfDs1E1FarEndDayTotalLCVs_Type()
)
wfDs1E1FarEndDayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalLCVs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalSASs_Type = Gauge32
_WfDs1E1FarEndDayTotalSASs_Object = MibTableColumn
wfDs1E1FarEndDayTotalSASs = _WfDs1E1FarEndDayTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 12),
    _WfDs1E1FarEndDayTotalSASs_Type()
)
wfDs1E1FarEndDayTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalSASs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalAISSs_Type = Gauge32
_WfDs1E1FarEndDayTotalAISSs_Object = MibTableColumn
wfDs1E1FarEndDayTotalAISSs = _WfDs1E1FarEndDayTotalAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 13),
    _WfDs1E1FarEndDayTotalAISSs_Type()
)
wfDs1E1FarEndDayTotalAISSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalAISSs.setStatus("mandatory")
_WfDs1E1FarEndDayTotalFCs_Type = Gauge32
_WfDs1E1FarEndDayTotalFCs_Object = MibTableColumn
wfDs1E1FarEndDayTotalFCs = _WfDs1E1FarEndDayTotalFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 14),
    _WfDs1E1FarEndDayTotalFCs_Type()
)
wfDs1E1FarEndDayTotalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalFCs.setStatus("mandatory")


class _WfDs1E1FarEndDayTotalValidFlag_Type(Integer32):
    """Custom type wfDs1E1FarEndDayTotalValidFlag based on Integer32"""
    defaultValue = 1

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


_WfDs1E1FarEndDayTotalValidFlag_Type.__name__ = "Integer32"
_WfDs1E1FarEndDayTotalValidFlag_Object = MibTableColumn
wfDs1E1FarEndDayTotalValidFlag = _WfDs1E1FarEndDayTotalValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 32, 1, 15),
    _WfDs1E1FarEndDayTotalValidFlag_Type()
)
wfDs1E1FarEndDayTotalValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayTotalValidFlag.setStatus("mandatory")
_WfDs1E1ThrAlrtTable_Object = MibTable
wfDs1E1ThrAlrtTable = _WfDs1E1ThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33)
)
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtTable.setStatus("mandatory")
_WfDs1E1ThrAlrtEntry_Object = MibTableRow
wfDs1E1ThrAlrtEntry = _WfDs1E1ThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1)
)
wfDs1E1ThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1ThrAlrtPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtEntry.setStatus("mandatory")


class _WfDs1E1ThrAlrtDelete_Type(Integer32):
    """Custom type wfDs1E1ThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1ThrAlrtDelete_Type.__name__ = "Integer32"
_WfDs1E1ThrAlrtDelete_Object = MibTableColumn
wfDs1E1ThrAlrtDelete = _WfDs1E1ThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 1),
    _WfDs1E1ThrAlrtDelete_Type()
)
wfDs1E1ThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtDelete.setStatus("mandatory")
_WfDs1E1ThrAlrtPortLineNumber_Type = Integer32
_WfDs1E1ThrAlrtPortLineNumber_Object = MibTableColumn
wfDs1E1ThrAlrtPortLineNumber = _WfDs1E1ThrAlrtPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 2),
    _WfDs1E1ThrAlrtPortLineNumber_Type()
)
wfDs1E1ThrAlrtPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtPortLineNumber.setStatus("mandatory")


class _WfDs1E1ThrAlrtESs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtESs based on Gauge32"""
    defaultValue = 65


_WfDs1E1ThrAlrtESs_Object = MibTableColumn
wfDs1E1ThrAlrtESs = _WfDs1E1ThrAlrtESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 3),
    _WfDs1E1ThrAlrtESs_Type()
)
wfDs1E1ThrAlrtESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtESs.setStatus("mandatory")


class _WfDs1E1ThrAlrtSESs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtSESs based on Gauge32"""
    defaultValue = 10


_WfDs1E1ThrAlrtSESs_Object = MibTableColumn
wfDs1E1ThrAlrtSESs = _WfDs1E1ThrAlrtSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 4),
    _WfDs1E1ThrAlrtSESs_Type()
)
wfDs1E1ThrAlrtSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtSESs.setStatus("mandatory")


class _WfDs1E1ThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1ThrAlrtSEFSs_Object = MibTableColumn
wfDs1E1ThrAlrtSEFSs = _WfDs1E1ThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 5),
    _WfDs1E1ThrAlrtSEFSs_Type()
)
wfDs1E1ThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtSEFSs.setStatus("mandatory")


class _WfDs1E1ThrAlrtUASs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDs1E1ThrAlrtUASs_Object = MibTableColumn
wfDs1E1ThrAlrtUASs = _WfDs1E1ThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 6),
    _WfDs1E1ThrAlrtUASs_Type()
)
wfDs1E1ThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtUASs.setStatus("mandatory")


class _WfDs1E1ThrAlrtCSSs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtCSSs based on Gauge32"""
    defaultValue = 1


_WfDs1E1ThrAlrtCSSs_Object = MibTableColumn
wfDs1E1ThrAlrtCSSs = _WfDs1E1ThrAlrtCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 7),
    _WfDs1E1ThrAlrtCSSs_Type()
)
wfDs1E1ThrAlrtCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtCSSs.setStatus("mandatory")


class _WfDs1E1ThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtPCVs based on Gauge32"""
    defaultValue = 13296


_WfDs1E1ThrAlrtPCVs_Object = MibTableColumn
wfDs1E1ThrAlrtPCVs = _WfDs1E1ThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 8),
    _WfDs1E1ThrAlrtPCVs_Type()
)
wfDs1E1ThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtPCVs.setStatus("mandatory")


class _WfDs1E1ThrAlrtLESs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtLESs based on Gauge32"""
    defaultValue = 65


_WfDs1E1ThrAlrtLESs_Object = MibTableColumn
wfDs1E1ThrAlrtLESs = _WfDs1E1ThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 9),
    _WfDs1E1ThrAlrtLESs_Type()
)
wfDs1E1ThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtLESs.setStatus("mandatory")


class _WfDs1E1ThrAlrtBESs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtBESs based on Gauge32"""
    defaultValue = 0


_WfDs1E1ThrAlrtBESs_Object = MibTableColumn
wfDs1E1ThrAlrtBESs = _WfDs1E1ThrAlrtBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 10),
    _WfDs1E1ThrAlrtBESs_Type()
)
wfDs1E1ThrAlrtBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtBESs.setStatus("mandatory")


class _WfDs1E1ThrAlrtDMs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtDMs based on Gauge32"""
    defaultValue = 0


_WfDs1E1ThrAlrtDMs_Object = MibTableColumn
wfDs1E1ThrAlrtDMs = _WfDs1E1ThrAlrtDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 11),
    _WfDs1E1ThrAlrtDMs_Type()
)
wfDs1E1ThrAlrtDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtDMs.setStatus("mandatory")


class _WfDs1E1ThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtLCVs based on Gauge32"""
    defaultValue = 13340


_WfDs1E1ThrAlrtLCVs_Object = MibTableColumn
wfDs1E1ThrAlrtLCVs = _WfDs1E1ThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 12),
    _WfDs1E1ThrAlrtLCVs_Type()
)
wfDs1E1ThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtLCVs.setStatus("mandatory")


class _WfDs1E1ThrAlrtSASs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtSASs based on Gauge32"""
    defaultValue = 2


_WfDs1E1ThrAlrtSASs_Object = MibTableColumn
wfDs1E1ThrAlrtSASs = _WfDs1E1ThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 13),
    _WfDs1E1ThrAlrtSASs_Type()
)
wfDs1E1ThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtSASs.setStatus("mandatory")


class _WfDs1E1ThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1ThrAlrtAISSs_Object = MibTableColumn
wfDs1E1ThrAlrtAISSs = _WfDs1E1ThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 14),
    _WfDs1E1ThrAlrtAISSs_Type()
)
wfDs1E1ThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtAISSs.setStatus("mandatory")


class _WfDs1E1ThrAlrtFCs_Type(Gauge32):
    """Custom type wfDs1E1ThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDs1E1ThrAlrtFCs_Object = MibTableColumn
wfDs1E1ThrAlrtFCs = _WfDs1E1ThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 33, 1, 15),
    _WfDs1E1ThrAlrtFCs_Type()
)
wfDs1E1ThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1ThrAlrtFCs.setStatus("mandatory")
_WfDs1E1DayThrAlrtTable_Object = MibTable
wfDs1E1DayThrAlrtTable = _WfDs1E1DayThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34)
)
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtTable.setStatus("mandatory")
_WfDs1E1DayThrAlrtEntry_Object = MibTableRow
wfDs1E1DayThrAlrtEntry = _WfDs1E1DayThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1)
)
wfDs1E1DayThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1DayThrAlrtPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtEntry.setStatus("mandatory")


class _WfDs1E1DayThrAlrtDelete_Type(Integer32):
    """Custom type wfDs1E1DayThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1DayThrAlrtDelete_Type.__name__ = "Integer32"
_WfDs1E1DayThrAlrtDelete_Object = MibTableColumn
wfDs1E1DayThrAlrtDelete = _WfDs1E1DayThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 1),
    _WfDs1E1DayThrAlrtDelete_Type()
)
wfDs1E1DayThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtDelete.setStatus("mandatory")
_WfDs1E1DayThrAlrtPortLineNumber_Type = Integer32
_WfDs1E1DayThrAlrtPortLineNumber_Object = MibTableColumn
wfDs1E1DayThrAlrtPortLineNumber = _WfDs1E1DayThrAlrtPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 2),
    _WfDs1E1DayThrAlrtPortLineNumber_Type()
)
wfDs1E1DayThrAlrtPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtPortLineNumber.setStatus("mandatory")


class _WfDs1E1DayThrAlrtESs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtESs based on Gauge32"""
    defaultValue = 648


_WfDs1E1DayThrAlrtESs_Object = MibTableColumn
wfDs1E1DayThrAlrtESs = _WfDs1E1DayThrAlrtESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 3),
    _WfDs1E1DayThrAlrtESs_Type()
)
wfDs1E1DayThrAlrtESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtESs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtSESs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtSESs based on Gauge32"""
    defaultValue = 100


_WfDs1E1DayThrAlrtSESs_Object = MibTableColumn
wfDs1E1DayThrAlrtSESs = _WfDs1E1DayThrAlrtSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 4),
    _WfDs1E1DayThrAlrtSESs_Type()
)
wfDs1E1DayThrAlrtSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtSESs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1DayThrAlrtSEFSs_Object = MibTableColumn
wfDs1E1DayThrAlrtSEFSs = _WfDs1E1DayThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 5),
    _WfDs1E1DayThrAlrtSEFSs_Type()
)
wfDs1E1DayThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtSEFSs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtUASs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDs1E1DayThrAlrtUASs_Object = MibTableColumn
wfDs1E1DayThrAlrtUASs = _WfDs1E1DayThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 6),
    _WfDs1E1DayThrAlrtUASs_Type()
)
wfDs1E1DayThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtUASs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtCSSs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtCSSs based on Gauge32"""
    defaultValue = 4


_WfDs1E1DayThrAlrtCSSs_Object = MibTableColumn
wfDs1E1DayThrAlrtCSSs = _WfDs1E1DayThrAlrtCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 7),
    _WfDs1E1DayThrAlrtCSSs_Type()
)
wfDs1E1DayThrAlrtCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtCSSs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtPCVs based on Gauge32"""
    defaultValue = 132960


_WfDs1E1DayThrAlrtPCVs_Object = MibTableColumn
wfDs1E1DayThrAlrtPCVs = _WfDs1E1DayThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 8),
    _WfDs1E1DayThrAlrtPCVs_Type()
)
wfDs1E1DayThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtPCVs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtLESs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtLESs based on Gauge32"""
    defaultValue = 648


_WfDs1E1DayThrAlrtLESs_Object = MibTableColumn
wfDs1E1DayThrAlrtLESs = _WfDs1E1DayThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 9),
    _WfDs1E1DayThrAlrtLESs_Type()
)
wfDs1E1DayThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtLESs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtBESs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtBESs based on Gauge32"""
    defaultValue = 0


_WfDs1E1DayThrAlrtBESs_Object = MibTableColumn
wfDs1E1DayThrAlrtBESs = _WfDs1E1DayThrAlrtBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 10),
    _WfDs1E1DayThrAlrtBESs_Type()
)
wfDs1E1DayThrAlrtBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtBESs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtDMs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtDMs based on Gauge32"""
    defaultValue = 0


_WfDs1E1DayThrAlrtDMs_Object = MibTableColumn
wfDs1E1DayThrAlrtDMs = _WfDs1E1DayThrAlrtDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 11),
    _WfDs1E1DayThrAlrtDMs_Type()
)
wfDs1E1DayThrAlrtDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtDMs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtLCVs based on Gauge32"""
    defaultValue = 133400


_WfDs1E1DayThrAlrtLCVs_Object = MibTableColumn
wfDs1E1DayThrAlrtLCVs = _WfDs1E1DayThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 12),
    _WfDs1E1DayThrAlrtLCVs_Type()
)
wfDs1E1DayThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtLCVs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtSASs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtSASs based on Gauge32"""
    defaultValue = 17


_WfDs1E1DayThrAlrtSASs_Object = MibTableColumn
wfDs1E1DayThrAlrtSASs = _WfDs1E1DayThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 13),
    _WfDs1E1DayThrAlrtSASs_Type()
)
wfDs1E1DayThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtSASs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1DayThrAlrtAISSs_Object = MibTableColumn
wfDs1E1DayThrAlrtAISSs = _WfDs1E1DayThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 14),
    _WfDs1E1DayThrAlrtAISSs_Type()
)
wfDs1E1DayThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtAISSs.setStatus("mandatory")


class _WfDs1E1DayThrAlrtFCs_Type(Gauge32):
    """Custom type wfDs1E1DayThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDs1E1DayThrAlrtFCs_Object = MibTableColumn
wfDs1E1DayThrAlrtFCs = _WfDs1E1DayThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 34, 1, 15),
    _WfDs1E1DayThrAlrtFCs_Type()
)
wfDs1E1DayThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1DayThrAlrtFCs.setStatus("mandatory")
_WfDs1E1FarEndThrAlrtTable_Object = MibTable
wfDs1E1FarEndThrAlrtTable = _WfDs1E1FarEndThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtTable.setStatus("mandatory")
_WfDs1E1FarEndThrAlrtEntry_Object = MibTableRow
wfDs1E1FarEndThrAlrtEntry = _WfDs1E1FarEndThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1)
)
wfDs1E1FarEndThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndThrAlrtPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtEntry.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtDelete_Type(Integer32):
    """Custom type wfDs1E1FarEndThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1FarEndThrAlrtDelete_Type.__name__ = "Integer32"
_WfDs1E1FarEndThrAlrtDelete_Object = MibTableColumn
wfDs1E1FarEndThrAlrtDelete = _WfDs1E1FarEndThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 1),
    _WfDs1E1FarEndThrAlrtDelete_Type()
)
wfDs1E1FarEndThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtDelete.setStatus("mandatory")
_WfDs1E1FarEndThrAlrtPortLineNumber_Type = Integer32
_WfDs1E1FarEndThrAlrtPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndThrAlrtPortLineNumber = _WfDs1E1FarEndThrAlrtPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 2),
    _WfDs1E1FarEndThrAlrtPortLineNumber_Type()
)
wfDs1E1FarEndThrAlrtPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtPortLineNumber.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtESs based on Gauge32"""
    defaultValue = 65


_WfDs1E1FarEndThrAlrtESs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtESs = _WfDs1E1FarEndThrAlrtESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 3),
    _WfDs1E1FarEndThrAlrtESs_Type()
)
wfDs1E1FarEndThrAlrtESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtESs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtSESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtSESs based on Gauge32"""
    defaultValue = 10


_WfDs1E1FarEndThrAlrtSESs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtSESs = _WfDs1E1FarEndThrAlrtSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 4),
    _WfDs1E1FarEndThrAlrtSESs_Type()
)
wfDs1E1FarEndThrAlrtSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtSESs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndThrAlrtSEFSs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtSEFSs = _WfDs1E1FarEndThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 5),
    _WfDs1E1FarEndThrAlrtSEFSs_Type()
)
wfDs1E1FarEndThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtSEFSs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtUASs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDs1E1FarEndThrAlrtUASs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtUASs = _WfDs1E1FarEndThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 6),
    _WfDs1E1FarEndThrAlrtUASs_Type()
)
wfDs1E1FarEndThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtUASs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtCSSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtCSSs based on Gauge32"""
    defaultValue = 1


_WfDs1E1FarEndThrAlrtCSSs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtCSSs = _WfDs1E1FarEndThrAlrtCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 7),
    _WfDs1E1FarEndThrAlrtCSSs_Type()
)
wfDs1E1FarEndThrAlrtCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtCSSs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtPCVs based on Gauge32"""
    defaultValue = 13296


_WfDs1E1FarEndThrAlrtPCVs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtPCVs = _WfDs1E1FarEndThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 8),
    _WfDs1E1FarEndThrAlrtPCVs_Type()
)
wfDs1E1FarEndThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtPCVs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtLESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtLESs based on Gauge32"""
    defaultValue = 65


_WfDs1E1FarEndThrAlrtLESs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtLESs = _WfDs1E1FarEndThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 9),
    _WfDs1E1FarEndThrAlrtLESs_Type()
)
wfDs1E1FarEndThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtLESs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtBESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtBESs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndThrAlrtBESs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtBESs = _WfDs1E1FarEndThrAlrtBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 10),
    _WfDs1E1FarEndThrAlrtBESs_Type()
)
wfDs1E1FarEndThrAlrtBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtBESs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtDMs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtDMs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndThrAlrtDMs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtDMs = _WfDs1E1FarEndThrAlrtDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 11),
    _WfDs1E1FarEndThrAlrtDMs_Type()
)
wfDs1E1FarEndThrAlrtDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtDMs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtLCVs based on Gauge32"""
    defaultValue = 13340


_WfDs1E1FarEndThrAlrtLCVs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtLCVs = _WfDs1E1FarEndThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 12),
    _WfDs1E1FarEndThrAlrtLCVs_Type()
)
wfDs1E1FarEndThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtLCVs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtSASs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtSASs based on Gauge32"""
    defaultValue = 2


_WfDs1E1FarEndThrAlrtSASs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtSASs = _WfDs1E1FarEndThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 13),
    _WfDs1E1FarEndThrAlrtSASs_Type()
)
wfDs1E1FarEndThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtSASs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndThrAlrtAISSs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtAISSs = _WfDs1E1FarEndThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 14),
    _WfDs1E1FarEndThrAlrtAISSs_Type()
)
wfDs1E1FarEndThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtAISSs.setStatus("mandatory")


class _WfDs1E1FarEndThrAlrtFCs_Type(Gauge32):
    """Custom type wfDs1E1FarEndThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndThrAlrtFCs_Object = MibTableColumn
wfDs1E1FarEndThrAlrtFCs = _WfDs1E1FarEndThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 35, 1, 15),
    _WfDs1E1FarEndThrAlrtFCs_Type()
)
wfDs1E1FarEndThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndThrAlrtFCs.setStatus("mandatory")
_WfDs1E1FarEndDayThrAlrtTable_Object = MibTable
wfDs1E1FarEndDayThrAlrtTable = _WfDs1E1FarEndDayThrAlrtTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36)
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtTable.setStatus("mandatory")
_WfDs1E1FarEndDayThrAlrtEntry_Object = MibTableRow
wfDs1E1FarEndDayThrAlrtEntry = _WfDs1E1FarEndDayThrAlrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1)
)
wfDs1E1FarEndDayThrAlrtEntry.setIndexNames(
    (0, "Wellfleet-DS1E1-MIB", "wfDs1E1FarEndDayThrAlrtPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtEntry.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtDelete_Type(Integer32):
    """Custom type wfDs1E1FarEndDayThrAlrtDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs1E1FarEndDayThrAlrtDelete_Type.__name__ = "Integer32"
_WfDs1E1FarEndDayThrAlrtDelete_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtDelete = _WfDs1E1FarEndDayThrAlrtDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 1),
    _WfDs1E1FarEndDayThrAlrtDelete_Type()
)
wfDs1E1FarEndDayThrAlrtDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtDelete.setStatus("mandatory")
_WfDs1E1FarEndDayThrAlrtPortLineNumber_Type = Integer32
_WfDs1E1FarEndDayThrAlrtPortLineNumber_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtPortLineNumber = _WfDs1E1FarEndDayThrAlrtPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 2),
    _WfDs1E1FarEndDayThrAlrtPortLineNumber_Type()
)
wfDs1E1FarEndDayThrAlrtPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtPortLineNumber.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtESs based on Gauge32"""
    defaultValue = 648


_WfDs1E1FarEndDayThrAlrtESs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtESs = _WfDs1E1FarEndDayThrAlrtESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 3),
    _WfDs1E1FarEndDayThrAlrtESs_Type()
)
wfDs1E1FarEndDayThrAlrtESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtESs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtSESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtSESs based on Gauge32"""
    defaultValue = 100


_WfDs1E1FarEndDayThrAlrtSESs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtSESs = _WfDs1E1FarEndDayThrAlrtSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 4),
    _WfDs1E1FarEndDayThrAlrtSESs_Type()
)
wfDs1E1FarEndDayThrAlrtSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtSESs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtSEFSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtSEFSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndDayThrAlrtSEFSs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtSEFSs = _WfDs1E1FarEndDayThrAlrtSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 5),
    _WfDs1E1FarEndDayThrAlrtSEFSs_Type()
)
wfDs1E1FarEndDayThrAlrtSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtSEFSs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtUASs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtUASs based on Gauge32"""
    defaultValue = 10


_WfDs1E1FarEndDayThrAlrtUASs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtUASs = _WfDs1E1FarEndDayThrAlrtUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 6),
    _WfDs1E1FarEndDayThrAlrtUASs_Type()
)
wfDs1E1FarEndDayThrAlrtUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtUASs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtCSSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtCSSs based on Gauge32"""
    defaultValue = 4


_WfDs1E1FarEndDayThrAlrtCSSs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtCSSs = _WfDs1E1FarEndDayThrAlrtCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 7),
    _WfDs1E1FarEndDayThrAlrtCSSs_Type()
)
wfDs1E1FarEndDayThrAlrtCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtCSSs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtPCVs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtPCVs based on Gauge32"""
    defaultValue = 132960


_WfDs1E1FarEndDayThrAlrtPCVs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtPCVs = _WfDs1E1FarEndDayThrAlrtPCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 8),
    _WfDs1E1FarEndDayThrAlrtPCVs_Type()
)
wfDs1E1FarEndDayThrAlrtPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtPCVs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtLESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtLESs based on Gauge32"""
    defaultValue = 648


_WfDs1E1FarEndDayThrAlrtLESs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtLESs = _WfDs1E1FarEndDayThrAlrtLESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 9),
    _WfDs1E1FarEndDayThrAlrtLESs_Type()
)
wfDs1E1FarEndDayThrAlrtLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtLESs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtBESs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtBESs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndDayThrAlrtBESs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtBESs = _WfDs1E1FarEndDayThrAlrtBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 10),
    _WfDs1E1FarEndDayThrAlrtBESs_Type()
)
wfDs1E1FarEndDayThrAlrtBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtBESs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtDMs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtDMs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndDayThrAlrtDMs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtDMs = _WfDs1E1FarEndDayThrAlrtDMs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 11),
    _WfDs1E1FarEndDayThrAlrtDMs_Type()
)
wfDs1E1FarEndDayThrAlrtDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtDMs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtLCVs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtLCVs based on Gauge32"""
    defaultValue = 133400


_WfDs1E1FarEndDayThrAlrtLCVs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtLCVs = _WfDs1E1FarEndDayThrAlrtLCVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 12),
    _WfDs1E1FarEndDayThrAlrtLCVs_Type()
)
wfDs1E1FarEndDayThrAlrtLCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtLCVs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtSASs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtSASs based on Gauge32"""
    defaultValue = 17


_WfDs1E1FarEndDayThrAlrtSASs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtSASs = _WfDs1E1FarEndDayThrAlrtSASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 13),
    _WfDs1E1FarEndDayThrAlrtSASs_Type()
)
wfDs1E1FarEndDayThrAlrtSASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtSASs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtAISSs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtAISSs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndDayThrAlrtAISSs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtAISSs = _WfDs1E1FarEndDayThrAlrtAISSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 14),
    _WfDs1E1FarEndDayThrAlrtAISSs_Type()
)
wfDs1E1FarEndDayThrAlrtAISSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtAISSs.setStatus("mandatory")


class _WfDs1E1FarEndDayThrAlrtFCs_Type(Gauge32):
    """Custom type wfDs1E1FarEndDayThrAlrtFCs based on Gauge32"""
    defaultValue = 0


_WfDs1E1FarEndDayThrAlrtFCs_Object = MibTableColumn
wfDs1E1FarEndDayThrAlrtFCs = _WfDs1E1FarEndDayThrAlrtFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 9, 36, 1, 15),
    _WfDs1E1FarEndDayThrAlrtFCs_Type()
)
wfDs1E1FarEndDayThrAlrtFCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs1E1FarEndDayThrAlrtFCs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DS1E1-MIB",
    **{"wfDs1E1AnsiTable": wfDs1E1AnsiTable,
       "wfDs1E1AnsiEntry": wfDs1E1AnsiEntry,
       "wfDs1E1AnsiPortLineNumber": wfDs1E1AnsiPortLineNumber,
       "wfDs1E1AnsiCRCCounts": wfDs1E1AnsiCRCCounts,
       "wfDs1E1AnsiBPVCounts": wfDs1E1AnsiBPVCounts,
       "wfDs1E1AnsiOOFCounts": wfDs1E1AnsiOOFCounts,
       "wfDs1E1AnsiFECounts": wfDs1E1AnsiFECounts,
       "wfDs1E1AnsiESCounts": wfDs1E1AnsiESCounts,
       "wfDs1E1AnsiSESCounts": wfDs1E1AnsiSESCounts,
       "wfDs1E1AnsiUASCounts": wfDs1E1AnsiUASCounts,
       "wfDs1E1AnsiPRMR0Counts": wfDs1E1AnsiPRMR0Counts,
       "wfDs1E1AnsiPRMR1Counts": wfDs1E1AnsiPRMR1Counts,
       "wfDs1E1AnsiPRMR2Counts": wfDs1E1AnsiPRMR2Counts,
       "wfDs1E1AnsiPRMR3Counts": wfDs1E1AnsiPRMR3Counts,
       "wfDs1E1AnsiPRMESCounts": wfDs1E1AnsiPRMESCounts,
       "wfDs1E1AnsiPRMSESCounts": wfDs1E1AnsiPRMSESCounts,
       "wfDs1E1AnsiPRMECounts": wfDs1E1AnsiPRMECounts,
       "wfDs1E1ModuleTable": wfDs1E1ModuleTable,
       "wfDs1E1ModuleEntry": wfDs1E1ModuleEntry,
       "wfDs1E1ModuleDelete": wfDs1E1ModuleDelete,
       "wfDs1E1ModuleSlot": wfDs1E1ModuleSlot,
       "wfDs1E1ModuleModule": wfDs1E1ModuleModule,
       "wfDs1E1ModulePrimaryClock": wfDs1E1ModulePrimaryClock,
       "wfDs1E1ModuleSecondaryClock": wfDs1E1ModuleSecondaryClock,
       "wfDs1E1ModuleCurrentClock": wfDs1E1ModuleCurrentClock,
       "wfDs1E1ModuleExtClockOperational": wfDs1E1ModuleExtClockOperational,
       "wfDs1E1ModuleLoop1ClockOperational": wfDs1E1ModuleLoop1ClockOperational,
       "wfDs1E1ModuleLoop2ClockOperational": wfDs1E1ModuleLoop2ClockOperational,
       "wfDs1E1ModuleLoop3ClockOperational": wfDs1E1ModuleLoop3ClockOperational,
       "wfDs1E1ModuleLoop4ClockOperational": wfDs1E1ModuleLoop4ClockOperational,
       "wfDs1E1ModuleCfgTxBufferUseCredits": wfDs1E1ModuleCfgTxBufferUseCredits,
       "wfDs1E1ModuleCfgRxBufferUseCredits": wfDs1E1ModuleCfgRxBufferUseCredits,
       "wfDs1E1ModuleTxBufferUseCredits": wfDs1E1ModuleTxBufferUseCredits,
       "wfDs1E1ModuleRxBufferUseCredits": wfDs1E1ModuleRxBufferUseCredits,
       "wfDs1E1PortMapTable": wfDs1E1PortMapTable,
       "wfDs1E1PortMapEntry": wfDs1E1PortMapEntry,
       "wfDs1E1PortMapDelete": wfDs1E1PortMapDelete,
       "wfDs1E1PortMapSlot": wfDs1E1PortMapSlot,
       "wfDs1E1PortMapConnector": wfDs1E1PortMapConnector,
       "wfDs1E1PortMapLineNumber": wfDs1E1PortMapLineNumber,
       "wfDs1E1PortMapDslId": wfDs1E1PortMapDslId,
       "wfDs1E1PortTable": wfDs1E1PortTable,
       "wfDs1E1PortEntry": wfDs1E1PortEntry,
       "wfDs1E1PortDelete": wfDs1E1PortDelete,
       "wfDs1E1PortDisable": wfDs1E1PortDisable,
       "wfDs1E1PortState": wfDs1E1PortState,
       "wfDs1E1PortLineNumber": wfDs1E1PortLineNumber,
       "wfDs1E1PortMtu": wfDs1E1PortMtu,
       "wfDs1E1PortSignalLevel": wfDs1E1PortSignalLevel,
       "wfDs1E1PortSetupAlarmThreshold": wfDs1E1PortSetupAlarmThreshold,
       "wfDs1E1PortClearAlarmThreshold": wfDs1E1PortClearAlarmThreshold,
       "wfDs1E1PortFdlTargetHdlcAddress": wfDs1E1PortFdlTargetHdlcAddress,
       "wfDs1E1PortAcceptLoopbackRequest": wfDs1E1PortAcceptLoopbackRequest,
       "wfDs1E1PortLoopbackState": wfDs1E1PortLoopbackState,
       "wfDs1E1PortBertMode": wfDs1E1PortBertMode,
       "wfDs1E1PortBertTestPattern": wfDs1E1PortBertTestPattern,
       "wfDs1E1PortBertSendAlarm": wfDs1E1PortBertSendAlarm,
       "wfDs1E1PortInternationalBit": wfDs1E1PortInternationalBit,
       "wfDs1E1PortLineApplication": wfDs1E1PortLineApplication,
       "wfDs1E1PortLoggingEnableMask": wfDs1E1PortLoggingEnableMask,
       "wfDs1E1PortSendPrmCrAddressBit": wfDs1E1PortSendPrmCrAddressBit,
       "wfDs1E1PortAcceptPrmCrAddressBit": wfDs1E1PortAcceptPrmCrAddressBit,
       "wfDs1E1PortLineImpedanceOption": wfDs1E1PortLineImpedanceOption,
       "wfDs1E1PortFdlLoopInterframeFill": wfDs1E1PortFdlLoopInterframeFill,
       "wfDs1E1PortRelayCtrl": wfDs1E1PortRelayCtrl,
       "wfDs1E1PortRelayStatus": wfDs1E1PortRelayStatus,
       "wfDs1E1PortPrimaryClockSource": wfDs1E1PortPrimaryClockSource,
       "wfDs1E1PortSecondaryClockSource": wfDs1E1PortSecondaryClockSource,
       "wfDs1E1PortCurrentClock": wfDs1E1PortCurrentClock,
       "wfDs1E1PortExtClockOperational": wfDs1E1PortExtClockOperational,
       "wfDs1E1PortTransmitWaveform": wfDs1E1PortTransmitWaveform,
       "wfDs1E1ConfigTable": wfDs1E1ConfigTable,
       "wfDs1E1ConfigEntry": wfDs1E1ConfigEntry,
       "wfDs1E1ConfigDelete": wfDs1E1ConfigDelete,
       "wfDs1E1ConfigPortLineNumber": wfDs1E1ConfigPortLineNumber,
       "wfDs1E1ConfigIfIndex": wfDs1E1ConfigIfIndex,
       "wfDs1E1ConfigTimeElapsed": wfDs1E1ConfigTimeElapsed,
       "wfDs1E1ConfigValidIntervals": wfDs1E1ConfigValidIntervals,
       "wfDs1E1ConfigLineType": wfDs1E1ConfigLineType,
       "wfDs1E1ConfigLineCoding": wfDs1E1ConfigLineCoding,
       "wfDs1E1ConfigSendCode": wfDs1E1ConfigSendCode,
       "wfDs1E1ConfigCircuitIdentifier": wfDs1E1ConfigCircuitIdentifier,
       "wfDs1E1ConfigLoopbackConfig": wfDs1E1ConfigLoopbackConfig,
       "wfDs1E1ConfigLineStatus": wfDs1E1ConfigLineStatus,
       "wfDs1E1ConfigSignalMode": wfDs1E1ConfigSignalMode,
       "wfDs1E1ConfigTransmitClockSource": wfDs1E1ConfigTransmitClockSource,
       "wfDs1E1ConfigFdl": wfDs1E1ConfigFdl,
       "wfDs1E1ActionTable": wfDs1E1ActionTable,
       "wfDs1E1ActionEntry": wfDs1E1ActionEntry,
       "wfDs1E1ActionPortLineNumber": wfDs1E1ActionPortLineNumber,
       "wfDs1E1ActionBertReset": wfDs1E1ActionBertReset,
       "wfDs1E1ActionBertErrorInsert": wfDs1E1ActionBertErrorInsert,
       "wfDs1E1ActionSendLoopCode": wfDs1E1ActionSendLoopCode,
       "wfDs1E1ActionSendFdlLoopbackCode": wfDs1E1ActionSendFdlLoopbackCode,
       "wfDs1E1ActionSendLoopUpFractionalCode": wfDs1E1ActionSendLoopUpFractionalCode,
       "wfDs1E1ActionSendLoopDownFractionalCode": wfDs1E1ActionSendLoopDownFractionalCode,
       "wfDs1E1ActionClearFractionalLoopState": wfDs1E1ActionClearFractionalLoopState,
       "wfDs1E1ActionClearFdlStats": wfDs1E1ActionClearFdlStats,
       "wfDs1E1ActionClearCurrentStats": wfDs1E1ActionClearCurrentStats,
       "wfDs1E1ActionClearFarEndCurrentStats": wfDs1E1ActionClearFarEndCurrentStats,
       "wfDs1E1ActionClearDayCurrentStats": wfDs1E1ActionClearDayCurrentStats,
       "wfDs1E1ActionClearFarEndDayCurrentStats": wfDs1E1ActionClearFarEndDayCurrentStats,
       "wfDs1E1ActionClearIntervalStats": wfDs1E1ActionClearIntervalStats,
       "wfDs1E1ActionClearFarEndIntervalStats": wfDs1E1ActionClearFarEndIntervalStats,
       "wfLogicalLineTable": wfLogicalLineTable,
       "wfLogicalLineEntry": wfLogicalLineEntry,
       "wfLogicalLineDelete": wfLogicalLineDelete,
       "wfLogicalLineDisable": wfLogicalLineDisable,
       "wfLogicalLineState": wfLogicalLineState,
       "wfLogicalLinePortLineNumber": wfLogicalLinePortLineNumber,
       "wfLogicalLineIndex": wfLogicalLineIndex,
       "wfLogicalLineCct": wfLogicalLineCct,
       "wfLogicalLineLineNumber": wfLogicalLineLineNumber,
       "wfLogicalLineBofl": wfLogicalLineBofl,
       "wfLogicalLineBoflTmo": wfLogicalLineBoflTmo,
       "wfLogicalLineFractionalLoopback": wfLogicalLineFractionalLoopback,
       "wfLogicalLineTimeSlotAssignment": wfLogicalLineTimeSlotAssignment,
       "wfLogicalLineMtu": wfLogicalLineMtu,
       "wfLogicalLineMadr": wfLogicalLineMadr,
       "wfLogicalLineWanProtocol": wfLogicalLineWanProtocol,
       "wfLogicalLineHdlcService": wfLogicalLineHdlcService,
       "wfLogicalLineLocalHdlcAddress": wfLogicalLineLocalHdlcAddress,
       "wfLogicalLineRemoteHdlcAddress": wfLogicalLineRemoteHdlcAddress,
       "wfLogicalLineRateAdaption": wfLogicalLineRateAdaption,
       "wfLogicalLineIFTF": wfLogicalLineIFTF,
       "wfLogicalLineCRCSize": wfLogicalLineCRCSize,
       "wfLogicalLineRxOctets": wfLogicalLineRxOctets,
       "wfLogicalLineRxFrames": wfLogicalLineRxFrames,
       "wfLogicalLineTxOctets": wfLogicalLineTxOctets,
       "wfLogicalLineTxFrames": wfLogicalLineTxFrames,
       "wfLogicalLineRxErrors": wfLogicalLineRxErrors,
       "wfLogicalLineTxErrors": wfLogicalLineTxErrors,
       "wfLogicalLineLackRxResources": wfLogicalLineLackRxResources,
       "wfLogicalLineLackTxResources": wfLogicalLineLackTxResources,
       "wfLogicalLineTxUnderflows": wfLogicalLineTxUnderflows,
       "wfLogicalLineRxOverflows": wfLogicalLineRxOverflows,
       "wfLogicalLineRxNullFrames": wfLogicalLineRxNullFrames,
       "wfLogicalLineRxShortFrames": wfLogicalLineRxShortFrames,
       "wfLogicalLineRxLossSyncs": wfLogicalLineRxLossSyncs,
       "wfLogicalLineRxCRCErrors": wfLogicalLineRxCRCErrors,
       "wfLogicalLineRxNonOctetBits": wfLogicalLineRxNonOctetBits,
       "wfLogicalLineRxLongFrames": wfLogicalLineRxLongFrames,
       "wfLogicalLineRxAbortFrames": wfLogicalLineRxAbortFrames,
       "wfLogicalLineRxDescOverflows": wfLogicalLineRxDescOverflows,
       "wfLogicalLineRxReplenMisses": wfLogicalLineRxReplenMisses,
       "wfLogicalLineRxIFCs": wfLogicalLineRxIFCs,
       "wfLogicalLineRxDropPackets": wfLogicalLineRxDropPackets,
       "wfLogicalLineCfgTxQueueLength": wfLogicalLineCfgTxQueueLength,
       "wfLogicalLineCfgRxQueueLength": wfLogicalLineCfgRxQueueLength,
       "wfLogicalLineTxQueueLength": wfLogicalLineTxQueueLength,
       "wfLogicalLineRxQueueLength": wfLogicalLineRxQueueLength,
       "wfLogicalLineTxQueueEmpties": wfLogicalLineTxQueueEmpties,
       "wfLogicalLineRxIntProcs": wfLogicalLineRxIntProcs,
       "wfLogicalLineTxIntProcs": wfLogicalLineTxIntProcs,
       "wfLogicalLineRxPktCorruptions": wfLogicalLineRxPktCorruptions,
       "wfLogicalLineTurboBofl": wfLogicalLineTurboBofl,
       "wfLogicalLineBoflNum": wfLogicalLineBoflNum,
       "wfLogicalLineBoflLen": wfLogicalLineBoflLen,
       "wfLogicalLineOutQLen": wfLogicalLineOutQLen,
       "wfLogicalLineLastChange": wfLogicalLineLastChange,
       "wfLogicalLineCfgMtu": wfLogicalLineCfgMtu,
       "wfLogicalLineRemoteLpbkDetection": wfLogicalLineRemoteLpbkDetection,
       "wfLogicalLineLastState": wfLogicalLineLastState,
       "wfLogicalLineRxIdles": wfLogicalLineRxIdles,
       "wfLogicalLineRole": wfLogicalLineRole,
       "wfLogicalLineActiveCct": wfLogicalLineActiveCct,
       "wfLogicalLineActualRateAdaption": wfLogicalLineActualRateAdaption,
       "wfLogicalLineBertMode": wfLogicalLineBertMode,
       "wfLogicalLineBertTestPattern": wfLogicalLineBertTestPattern,
       "wfLogicalLineAcceptFracLoopCode": wfLogicalLineAcceptFracLoopCode,
       "wfLogicalLineDS0AStatus": wfLogicalLineDS0AStatus,
       "wfLogicalLineNRZIEnable": wfLogicalLineNRZIEnable,
       "wfLogicalLineNRZIType": wfLogicalLineNRZIType,
       "wfDs1E1FracTable": wfDs1E1FracTable,
       "wfDs1E1FracEntry": wfDs1E1FracEntry,
       "wfDs1E1FracDelete": wfDs1E1FracDelete,
       "wfDs1E1FracPortLineNumber": wfDs1E1FracPortLineNumber,
       "wfDs1E1FracNumber": wfDs1E1FracNumber,
       "wfDs1E1FracLogicalLineIndex": wfDs1E1FracLogicalLineIndex,
       "wfDs1E1FracActualLogicalLineIndex": wfDs1E1FracActualLogicalLineIndex,
       "wfDs1E1CurrentTable": wfDs1E1CurrentTable,
       "wfDs1E1CurrentEntry": wfDs1E1CurrentEntry,
       "wfDs1E1CurrentPortLineNumber": wfDs1E1CurrentPortLineNumber,
       "wfDs1E1CurrentESs": wfDs1E1CurrentESs,
       "wfDs1E1CurrentSESs": wfDs1E1CurrentSESs,
       "wfDs1E1CurrentSEFSs": wfDs1E1CurrentSEFSs,
       "wfDs1E1CurrentUASs": wfDs1E1CurrentUASs,
       "wfDs1E1CurrentCSSs": wfDs1E1CurrentCSSs,
       "wfDs1E1CurrentPCVs": wfDs1E1CurrentPCVs,
       "wfDs1E1CurrentLESs": wfDs1E1CurrentLESs,
       "wfDs1E1CurrentBESs": wfDs1E1CurrentBESs,
       "wfDs1E1CurrentDMs": wfDs1E1CurrentDMs,
       "wfDs1E1CurrentLCVs": wfDs1E1CurrentLCVs,
       "wfDs1E1CurrentSASs": wfDs1E1CurrentSASs,
       "wfDs1E1CurrentAISSs": wfDs1E1CurrentAISSs,
       "wfDs1E1CurrentFCs": wfDs1E1CurrentFCs,
       "wfDs1E1CurrentTimeElapsed": wfDs1E1CurrentTimeElapsed,
       "wfDs1E1CurrentValidIntervals": wfDs1E1CurrentValidIntervals,
       "wfDs1E1CurrentValidFlag": wfDs1E1CurrentValidFlag,
       "wfDs1E1IntervalTable": wfDs1E1IntervalTable,
       "wfDs1E1IntervalEntry": wfDs1E1IntervalEntry,
       "wfDs1E1IntervalPortLineNumber": wfDs1E1IntervalPortLineNumber,
       "wfDs1E1IntervalNumber": wfDs1E1IntervalNumber,
       "wfDs1E1IntervalESs": wfDs1E1IntervalESs,
       "wfDs1E1IntervalSESs": wfDs1E1IntervalSESs,
       "wfDs1E1IntervalSEFSs": wfDs1E1IntervalSEFSs,
       "wfDs1E1IntervalUASs": wfDs1E1IntervalUASs,
       "wfDs1E1IntervalCSSs": wfDs1E1IntervalCSSs,
       "wfDs1E1IntervalPCVs": wfDs1E1IntervalPCVs,
       "wfDs1E1IntervalLESs": wfDs1E1IntervalLESs,
       "wfDs1E1IntervalBESs": wfDs1E1IntervalBESs,
       "wfDs1E1IntervalDMs": wfDs1E1IntervalDMs,
       "wfDs1E1IntervalLCVs": wfDs1E1IntervalLCVs,
       "wfDs1E1IntervalSASs": wfDs1E1IntervalSASs,
       "wfDs1E1IntervalAISSs": wfDs1E1IntervalAISSs,
       "wfDs1E1IntervalFCs": wfDs1E1IntervalFCs,
       "wfDs1E1IntervalValidFlag": wfDs1E1IntervalValidFlag,
       "wfDs1E1TotalTable": wfDs1E1TotalTable,
       "wfDs1E1TotalEntry": wfDs1E1TotalEntry,
       "wfDs1E1TotalPortLineNumber": wfDs1E1TotalPortLineNumber,
       "wfDs1E1TotalESs": wfDs1E1TotalESs,
       "wfDs1E1TotalSESs": wfDs1E1TotalSESs,
       "wfDs1E1TotalSEFSs": wfDs1E1TotalSEFSs,
       "wfDs1E1TotalUASs": wfDs1E1TotalUASs,
       "wfDs1E1TotalCSSs": wfDs1E1TotalCSSs,
       "wfDs1E1TotalPCVs": wfDs1E1TotalPCVs,
       "wfDs1E1TotalLESs": wfDs1E1TotalLESs,
       "wfDs1E1TotalBESs": wfDs1E1TotalBESs,
       "wfDs1E1TotalDMs": wfDs1E1TotalDMs,
       "wfDs1E1TotalLCVs": wfDs1E1TotalLCVs,
       "wfDs1E1TotalSASs": wfDs1E1TotalSASs,
       "wfDs1E1TotalAISSs": wfDs1E1TotalAISSs,
       "wfDs1E1TotalFCs": wfDs1E1TotalFCs,
       "wfDs1E1TotalValidFlag": wfDs1E1TotalValidFlag,
       "wfDs1E1BertStatsTable": wfDs1E1BertStatsTable,
       "wfDs1E1BertStatsEntry": wfDs1E1BertStatsEntry,
       "wfDs1E1BertStatsPortLineNumber": wfDs1E1BertStatsPortLineNumber,
       "wfDs1E1BertStatsBitErrors": wfDs1E1BertStatsBitErrors,
       "wfDs1E1BertStatsBits": wfDs1E1BertStatsBits,
       "wfDs1E1CurrentFramerStatsTable": wfDs1E1CurrentFramerStatsTable,
       "wfDs1E1CurrentFramerStatsEntry": wfDs1E1CurrentFramerStatsEntry,
       "wfDs1E1CurrentFramerStatsPortLineNumber": wfDs1E1CurrentFramerStatsPortLineNumber,
       "wfDs1E1CurrentFramerStatsMediaType": wfDs1E1CurrentFramerStatsMediaType,
       "wfDs1E1CurrentFramerStatsBpvCounts": wfDs1E1CurrentFramerStatsBpvCounts,
       "wfDs1E1CurrentFramerStatsCrc4Counts": wfDs1E1CurrentFramerStatsCrc4Counts,
       "wfDs1E1CurrentFramerStatsFebeCounts": wfDs1E1CurrentFramerStatsFebeCounts,
       "wfDs1E1CurrentFramerStatsOofCounts": wfDs1E1CurrentFramerStatsOofCounts,
       "wfDs1E1CurrentFramerStatsFeCounts": wfDs1E1CurrentFramerStatsFeCounts,
       "wfDs1E1CurrentFramerStatsLossFrameFailures": wfDs1E1CurrentFramerStatsLossFrameFailures,
       "wfDs1E1CurrentFramerStatsLossSignalFailures": wfDs1E1CurrentFramerStatsLossSignalFailures,
       "wfDs1E1CurrentFramerStatsAlarmIndicationFailures": wfDs1E1CurrentFramerStatsAlarmIndicationFailures,
       "wfDs1E1CurrentFramerStatsRemoteAlarmFailures": wfDs1E1CurrentFramerStatsRemoteAlarmFailures,
       "wfDs1E1TotalFramerStatsTable": wfDs1E1TotalFramerStatsTable,
       "wfDs1E1TotalFramerStatsEntry": wfDs1E1TotalFramerStatsEntry,
       "wfDs1E1TotalFramerStatsPortLineNumber": wfDs1E1TotalFramerStatsPortLineNumber,
       "wfDs1E1TotalFramerStatsMediaType": wfDs1E1TotalFramerStatsMediaType,
       "wfDs1E1TotalFramerStatsValidIntervals": wfDs1E1TotalFramerStatsValidIntervals,
       "wfDs1E1TotalFramerStatsBpvCounts": wfDs1E1TotalFramerStatsBpvCounts,
       "wfDs1E1TotalFramerStatsCrc4Counts": wfDs1E1TotalFramerStatsCrc4Counts,
       "wfDs1E1TotalFramerStatsFebeCounts": wfDs1E1TotalFramerStatsFebeCounts,
       "wfDs1E1TotalFramerStatsOofCounts": wfDs1E1TotalFramerStatsOofCounts,
       "wfDs1E1TotalFramerStatsFeCounts": wfDs1E1TotalFramerStatsFeCounts,
       "wfDs1E1TotalFramerStatsLossFrameFailures": wfDs1E1TotalFramerStatsLossFrameFailures,
       "wfDs1E1TotalFramerStatsLossSignalFailures": wfDs1E1TotalFramerStatsLossSignalFailures,
       "wfDs1E1TotalFramerStatsAlarmIndicationFailures": wfDs1E1TotalFramerStatsAlarmIndicationFailures,
       "wfDs1E1TotalFramerStatsRemoteAlarmFailures": wfDs1E1TotalFramerStatsRemoteAlarmFailures,
       "wfDs1E1IntervalFramerStatsTable": wfDs1E1IntervalFramerStatsTable,
       "wfDs1E1IntervalFramerStatsEntry": wfDs1E1IntervalFramerStatsEntry,
       "wfDs1E1IntervalFramerStatsPortLineNumber": wfDs1E1IntervalFramerStatsPortLineNumber,
       "wfDs1E1IntervalFramerStatsIntervalNumber": wfDs1E1IntervalFramerStatsIntervalNumber,
       "wfDs1E1IntervalFramerStatsMediaType": wfDs1E1IntervalFramerStatsMediaType,
       "wfDs1E1IntervalFramerStatsBpvCounts": wfDs1E1IntervalFramerStatsBpvCounts,
       "wfDs1E1IntervalFramerStatsCrc4Counts": wfDs1E1IntervalFramerStatsCrc4Counts,
       "wfDs1E1IntervalFramerStatsFebeCounts": wfDs1E1IntervalFramerStatsFebeCounts,
       "wfDs1E1IntervalFramerStatsOofCounts": wfDs1E1IntervalFramerStatsOofCounts,
       "wfDs1E1IntervalFramerStatsFeCounts": wfDs1E1IntervalFramerStatsFeCounts,
       "wfDs1E1IntervalFramerStatsLossFrameFailures": wfDs1E1IntervalFramerStatsLossFrameFailures,
       "wfDs1E1IntervalFramerStatsLossSignalFailures": wfDs1E1IntervalFramerStatsLossSignalFailures,
       "wfDs1E1IntervalFramerStatsAlarmIndicationFailures": wfDs1E1IntervalFramerStatsAlarmIndicationFailures,
       "wfDs1E1IntervalFramerStatsRemoteAlarmFailures": wfDs1E1IntervalFramerStatsRemoteAlarmFailures,
       "wfDs1E1ClockTable": wfDs1E1ClockTable,
       "wfDs1E1ClockEntry": wfDs1E1ClockEntry,
       "wfDs1E1ClockDelete": wfDs1E1ClockDelete,
       "wfDs1E1ClockPortLineNumber": wfDs1E1ClockPortLineNumber,
       "wfDs1E1ClockPrimaryClock": wfDs1E1ClockPrimaryClock,
       "wfDs1E1ClockSecondaryClock": wfDs1E1ClockSecondaryClock,
       "wfDs1E1ClockCurrentClock": wfDs1E1ClockCurrentClock,
       "wfDs1E1ClockLoopClockOperational": wfDs1E1ClockLoopClockOperational,
       "wfDs1E1ClockExtClockOperational": wfDs1E1ClockExtClockOperational,
       "wfDs1E1LineQueStatTable": wfDs1E1LineQueStatTable,
       "wfDs1E1LineQueStatEntry": wfDs1E1LineQueStatEntry,
       "wfDs1E1LineQueStatPortLineNumber": wfDs1E1LineQueStatPortLineNumber,
       "wfDs1E1LineQueStatLineIndex": wfDs1E1LineQueStatLineIndex,
       "wfDs1E1LineQueStatQueueIndex": wfDs1E1LineQueStatQueueIndex,
       "wfDs1E1LineQueStatTxOctets": wfDs1E1LineQueStatTxOctets,
       "wfDs1E1LineQueStatTxPackets": wfDs1E1LineQueStatTxPackets,
       "wfDs1E1LineQueStatTxDrops": wfDs1E1LineQueStatTxDrops,
       "wfDs1E1LineCfgTable": wfDs1E1LineCfgTable,
       "wfDs1E1LineCfgEntry": wfDs1E1LineCfgEntry,
       "wfDs1E1LineCfgDelete": wfDs1E1LineCfgDelete,
       "wfDs1E1LineCfgDisable": wfDs1E1LineCfgDisable,
       "wfDs1E1LineCfgState": wfDs1E1LineCfgState,
       "wfDs1E1LineLastChange": wfDs1E1LineLastChange,
       "wfDs1E1LineCfgPortLineNumber": wfDs1E1LineCfgPortLineNumber,
       "wfDs1E1LineCfgIndex": wfDs1E1LineCfgIndex,
       "wfDs1E1LineCfgIfIndex": wfDs1E1LineCfgIfIndex,
       "wfDs1E1LineCfgCct": wfDs1E1LineCfgCct,
       "wfDs1E1LineCfgLineNumber": wfDs1E1LineCfgLineNumber,
       "wfDs1E1LineCfgQosServicePkg": wfDs1E1LineCfgQosServicePkg,
       "wfDs1E1LineCfgTimeSlotAssign": wfDs1E1LineCfgTimeSlotAssign,
       "wfDs1E1LineCfgActualTimeSlotAssign": wfDs1E1LineCfgActualTimeSlotAssign,
       "wfDs1E1LineCfgWanProtocol": wfDs1E1LineCfgWanProtocol,
       "wfDs1E1LineCfgRateAdaption": wfDs1E1LineCfgRateAdaption,
       "wfDs1E1LineCfgIFTF": wfDs1E1LineCfgIFTF,
       "wfDs1E1LineCfgCRCSize": wfDs1E1LineCfgCRCSize,
       "wfDs1E1LineCfgMtu": wfDs1E1LineCfgMtu,
       "wfDs1E1LineCfgBertMode": wfDs1E1LineCfgBertMode,
       "wfDs1E1LineCfgBertTestPattern": wfDs1E1LineCfgBertTestPattern,
       "wfDs1E1LineCfgFractionalLoopback": wfDs1E1LineCfgFractionalLoopback,
       "wfDs1E1LineCfgAcceptFracLoopCode": wfDs1E1LineCfgAcceptFracLoopCode,
       "wfDs1E1LineCfgManagerMethod": wfDs1E1LineCfgManagerMethod,
       "wfDs1E1LineStatTable": wfDs1E1LineStatTable,
       "wfDs1E1LineStatEntry": wfDs1E1LineStatEntry,
       "wfDs1E1LineStatPortLineNumber": wfDs1E1LineStatPortLineNumber,
       "wfDs1E1LineStatIndex": wfDs1E1LineStatIndex,
       "wfDs1E1LineStatRxOctets": wfDs1E1LineStatRxOctets,
       "wfDs1E1LineStatTxOctets": wfDs1E1LineStatTxOctets,
       "wfDs1E1LineStatRxFrames": wfDs1E1LineStatRxFrames,
       "wfDs1E1LineStatTxFrames": wfDs1E1LineStatTxFrames,
       "wfDs1E1LineStatRxErrors": wfDs1E1LineStatRxErrors,
       "wfDs1E1LineStatTxErrors": wfDs1E1LineStatTxErrors,
       "wfDs1E1LineStatRxDropPackets": wfDs1E1LineStatRxDropPackets,
       "wfDs1E1LineStatTxDropPackets": wfDs1E1LineStatTxDropPackets,
       "wfDs1E1LineStatTxUnderflows": wfDs1E1LineStatTxUnderflows,
       "wfDs1E1LineStatRxOverflows": wfDs1E1LineStatRxOverflows,
       "wfDs1E1LineStatRxShortFrames": wfDs1E1LineStatRxShortFrames,
       "wfDs1E1LineStatRxCRCErrors": wfDs1E1LineStatRxCRCErrors,
       "wfDs1E1LineStatRxNonOctetBits": wfDs1E1LineStatRxNonOctetBits,
       "wfDs1E1LineStatRxLongFrames": wfDs1E1LineStatRxLongFrames,
       "wfDs1E1LineStatRxAbortFrames": wfDs1E1LineStatRxAbortFrames,
       "wfDs1E1DayCurrentTable": wfDs1E1DayCurrentTable,
       "wfDs1E1DayCurrentEntry": wfDs1E1DayCurrentEntry,
       "wfDs1E1DayCurrentPortLineNumber": wfDs1E1DayCurrentPortLineNumber,
       "wfDs1E1DayCurrentESs": wfDs1E1DayCurrentESs,
       "wfDs1E1DayCurrentSESs": wfDs1E1DayCurrentSESs,
       "wfDs1E1DayCurrentSEFSs": wfDs1E1DayCurrentSEFSs,
       "wfDs1E1DayCurrentUASs": wfDs1E1DayCurrentUASs,
       "wfDs1E1DayCurrentCSSs": wfDs1E1DayCurrentCSSs,
       "wfDs1E1DayCurrentPCVs": wfDs1E1DayCurrentPCVs,
       "wfDs1E1DayCurrentLESs": wfDs1E1DayCurrentLESs,
       "wfDs1E1DayCurrentBESs": wfDs1E1DayCurrentBESs,
       "wfDs1E1DayCurrentDMs": wfDs1E1DayCurrentDMs,
       "wfDs1E1DayCurrentLCVs": wfDs1E1DayCurrentLCVs,
       "wfDs1E1DayCurrentSASs": wfDs1E1DayCurrentSASs,
       "wfDs1E1DayCurrentAISSs": wfDs1E1DayCurrentAISSs,
       "wfDs1E1DayCurrentFCs": wfDs1E1DayCurrentFCs,
       "wfDs1E1DayCurrentTimeElapsed": wfDs1E1DayCurrentTimeElapsed,
       "wfDs1E1DayCurrentValidIntervals": wfDs1E1DayCurrentValidIntervals,
       "wfDs1E1DayCurrentValidFlag": wfDs1E1DayCurrentValidFlag,
       "wfDs1E1DayIntervalTable": wfDs1E1DayIntervalTable,
       "wfDs1E1DayIntervalEntry": wfDs1E1DayIntervalEntry,
       "wfDs1E1DayIntervalPortLineNumber": wfDs1E1DayIntervalPortLineNumber,
       "wfDs1E1DayIntervalNumber": wfDs1E1DayIntervalNumber,
       "wfDs1E1DayIntervalESs": wfDs1E1DayIntervalESs,
       "wfDs1E1DayIntervalSESs": wfDs1E1DayIntervalSESs,
       "wfDs1E1DayIntervalSEFSs": wfDs1E1DayIntervalSEFSs,
       "wfDs1E1DayIntervalUASs": wfDs1E1DayIntervalUASs,
       "wfDs1E1DayIntervalCSSs": wfDs1E1DayIntervalCSSs,
       "wfDs1E1DayIntervalPCVs": wfDs1E1DayIntervalPCVs,
       "wfDs1E1DayIntervalLESs": wfDs1E1DayIntervalLESs,
       "wfDs1E1DayIntervalBESs": wfDs1E1DayIntervalBESs,
       "wfDs1E1DayIntervalDMs": wfDs1E1DayIntervalDMs,
       "wfDs1E1DayIntervalLCVs": wfDs1E1DayIntervalLCVs,
       "wfDs1E1DayIntervalSASs": wfDs1E1DayIntervalSASs,
       "wfDs1E1DayIntervalAISSs": wfDs1E1DayIntervalAISSs,
       "wfDs1E1DayIntervalFCs": wfDs1E1DayIntervalFCs,
       "wfDs1E1DayIntervalValidFlag": wfDs1E1DayIntervalValidFlag,
       "wfDs1E1DayTotalTable": wfDs1E1DayTotalTable,
       "wfDs1E1DayTotalEntry": wfDs1E1DayTotalEntry,
       "wfDs1E1DayTotalPortLineNumber": wfDs1E1DayTotalPortLineNumber,
       "wfDs1E1DayTotalESs": wfDs1E1DayTotalESs,
       "wfDs1E1DayTotalSESs": wfDs1E1DayTotalSESs,
       "wfDs1E1DayTotalSEFSs": wfDs1E1DayTotalSEFSs,
       "wfDs1E1DayTotalUASs": wfDs1E1DayTotalUASs,
       "wfDs1E1DayTotalCSSs": wfDs1E1DayTotalCSSs,
       "wfDs1E1DayTotalPCVs": wfDs1E1DayTotalPCVs,
       "wfDs1E1DayTotalLESs": wfDs1E1DayTotalLESs,
       "wfDs1E1DayTotalBESs": wfDs1E1DayTotalBESs,
       "wfDs1E1DayTotalDMs": wfDs1E1DayTotalDMs,
       "wfDs1E1DayTotalLCVs": wfDs1E1DayTotalLCVs,
       "wfDs1E1DayTotalSASs": wfDs1E1DayTotalSASs,
       "wfDs1E1DayTotalAISSs": wfDs1E1DayTotalAISSs,
       "wfDs1E1DayTotalFCs": wfDs1E1DayTotalFCs,
       "wfDs1E1DayTotalValidFlag": wfDs1E1DayTotalValidFlag,
       "wfDs1E1FarEndCurrentTable": wfDs1E1FarEndCurrentTable,
       "wfDs1E1FarEndCurrentEntry": wfDs1E1FarEndCurrentEntry,
       "wfDs1E1FarEndCurrentPortLineNumber": wfDs1E1FarEndCurrentPortLineNumber,
       "wfDs1E1FarEndCurrentESs": wfDs1E1FarEndCurrentESs,
       "wfDs1E1FarEndCurrentSESs": wfDs1E1FarEndCurrentSESs,
       "wfDs1E1FarEndCurrentSEFSs": wfDs1E1FarEndCurrentSEFSs,
       "wfDs1E1FarEndCurrentUASs": wfDs1E1FarEndCurrentUASs,
       "wfDs1E1FarEndCurrentCSSs": wfDs1E1FarEndCurrentCSSs,
       "wfDs1E1FarEndCurrentPCVs": wfDs1E1FarEndCurrentPCVs,
       "wfDs1E1FarEndCurrentLESs": wfDs1E1FarEndCurrentLESs,
       "wfDs1E1FarEndCurrentBESs": wfDs1E1FarEndCurrentBESs,
       "wfDs1E1FarEndCurrentDMs": wfDs1E1FarEndCurrentDMs,
       "wfDs1E1FarEndCurrentLCVs": wfDs1E1FarEndCurrentLCVs,
       "wfDs1E1FarEndCurrentSASs": wfDs1E1FarEndCurrentSASs,
       "wfDs1E1FarEndCurrentAISSs": wfDs1E1FarEndCurrentAISSs,
       "wfDs1E1FarEndCurrentFCs": wfDs1E1FarEndCurrentFCs,
       "wfDs1E1FarEndCurrentTimeElapsed": wfDs1E1FarEndCurrentTimeElapsed,
       "wfDs1E1FarEndCurrentValidIntervals": wfDs1E1FarEndCurrentValidIntervals,
       "wfDs1E1FarEndCurrentValidFlag": wfDs1E1FarEndCurrentValidFlag,
       "wfDs1E1FarEndIntervalTable": wfDs1E1FarEndIntervalTable,
       "wfDs1E1FarEndIntervalEntry": wfDs1E1FarEndIntervalEntry,
       "wfDs1E1FarEndIntervalPortLineNumber": wfDs1E1FarEndIntervalPortLineNumber,
       "wfDs1E1FarEndIntervalNumber": wfDs1E1FarEndIntervalNumber,
       "wfDs1E1FarEndIntervalESs": wfDs1E1FarEndIntervalESs,
       "wfDs1E1FarEndIntervalSESs": wfDs1E1FarEndIntervalSESs,
       "wfDs1E1FarEndIntervalSEFSs": wfDs1E1FarEndIntervalSEFSs,
       "wfDs1E1FarEndIntervalUASs": wfDs1E1FarEndIntervalUASs,
       "wfDs1E1FarEndIntervalCSSs": wfDs1E1FarEndIntervalCSSs,
       "wfDs1E1FarEndIntervalPCVs": wfDs1E1FarEndIntervalPCVs,
       "wfDs1E1FarEndIntervalLESs": wfDs1E1FarEndIntervalLESs,
       "wfDs1E1FarEndIntervalBESs": wfDs1E1FarEndIntervalBESs,
       "wfDs1E1FarEndIntervalDMs": wfDs1E1FarEndIntervalDMs,
       "wfDs1E1FarEndIntervalLCVs": wfDs1E1FarEndIntervalLCVs,
       "wfDs1E1FarEndIntervalSASs": wfDs1E1FarEndIntervalSASs,
       "wfDs1E1FarEndIntervalAISSs": wfDs1E1FarEndIntervalAISSs,
       "wfDs1E1FarEndIntervalFCs": wfDs1E1FarEndIntervalFCs,
       "wfDs1E1FarEndIntervalValidFlag": wfDs1E1FarEndIntervalValidFlag,
       "wfDs1E1FarEndTotalTable": wfDs1E1FarEndTotalTable,
       "wfDs1E1FarEndTotalEntry": wfDs1E1FarEndTotalEntry,
       "wfDs1E1FarEndTotalPortLineNumber": wfDs1E1FarEndTotalPortLineNumber,
       "wfDs1E1FarEndTotalESs": wfDs1E1FarEndTotalESs,
       "wfDs1E1FarEndTotalSESs": wfDs1E1FarEndTotalSESs,
       "wfDs1E1FarEndTotalSEFSs": wfDs1E1FarEndTotalSEFSs,
       "wfDs1E1FarEndTotalUASs": wfDs1E1FarEndTotalUASs,
       "wfDs1E1FarEndTotalCSSs": wfDs1E1FarEndTotalCSSs,
       "wfDs1E1FarEndTotalPCVs": wfDs1E1FarEndTotalPCVs,
       "wfDs1E1FarEndTotalLESs": wfDs1E1FarEndTotalLESs,
       "wfDs1E1FarEndTotalBESs": wfDs1E1FarEndTotalBESs,
       "wfDs1E1FarEndTotalDMs": wfDs1E1FarEndTotalDMs,
       "wfDs1E1FarEndTotalLCVs": wfDs1E1FarEndTotalLCVs,
       "wfDs1E1FarEndTotalSASs": wfDs1E1FarEndTotalSASs,
       "wfDs1E1FarEndTotalAISSs": wfDs1E1FarEndTotalAISSs,
       "wfDs1E1FarEndTotalFCs": wfDs1E1FarEndTotalFCs,
       "wfDs1E1FarEndTotalValidFlag": wfDs1E1FarEndTotalValidFlag,
       "wfDs1E1FarEndDayCurrentTable": wfDs1E1FarEndDayCurrentTable,
       "wfDs1E1FarEndDayCurrentEntry": wfDs1E1FarEndDayCurrentEntry,
       "wfDs1E1FarEndDayCurrentPortLineNumber": wfDs1E1FarEndDayCurrentPortLineNumber,
       "wfDs1E1FarEndDayCurrentESs": wfDs1E1FarEndDayCurrentESs,
       "wfDs1E1FarEndDayCurrentSESs": wfDs1E1FarEndDayCurrentSESs,
       "wfDs1E1FarEndDayCurrentSEFSs": wfDs1E1FarEndDayCurrentSEFSs,
       "wfDs1E1FarEndDayCurrentUASs": wfDs1E1FarEndDayCurrentUASs,
       "wfDs1E1FarEndDayCurrentCSSs": wfDs1E1FarEndDayCurrentCSSs,
       "wfDs1E1FarEndDayCurrentPCVs": wfDs1E1FarEndDayCurrentPCVs,
       "wfDs1E1FarEndDayCurrentLESs": wfDs1E1FarEndDayCurrentLESs,
       "wfDs1E1FarEndDayCurrentBESs": wfDs1E1FarEndDayCurrentBESs,
       "wfDs1E1FarEndDayCurrentDMs": wfDs1E1FarEndDayCurrentDMs,
       "wfDs1E1FarEndDayCurrentLCVs": wfDs1E1FarEndDayCurrentLCVs,
       "wfDs1E1FarEndDayCurrentSASs": wfDs1E1FarEndDayCurrentSASs,
       "wfDs1E1FarEndDayCurrentAISSs": wfDs1E1FarEndDayCurrentAISSs,
       "wfDs1E1FarEndDayCurrentFCs": wfDs1E1FarEndDayCurrentFCs,
       "wfDs1E1FarEndDayCurrentTimeElapsed": wfDs1E1FarEndDayCurrentTimeElapsed,
       "wfDs1E1FarEndDayCurrentValidIntervals": wfDs1E1FarEndDayCurrentValidIntervals,
       "wfDs1E1FarEndDayCurrentValidFlag": wfDs1E1FarEndDayCurrentValidFlag,
       "wfDs1E1FarEndDayIntervalTable": wfDs1E1FarEndDayIntervalTable,
       "wfDs1E1FarEndDayIntervalEntry": wfDs1E1FarEndDayIntervalEntry,
       "wfDs1E1FarEndDayIntervalPortLineNumber": wfDs1E1FarEndDayIntervalPortLineNumber,
       "wfDs1E1FarEndDayIntervalNumber": wfDs1E1FarEndDayIntervalNumber,
       "wfDs1E1FarEndDayIntervalESs": wfDs1E1FarEndDayIntervalESs,
       "wfDs1E1FarEndDayIntervalSESs": wfDs1E1FarEndDayIntervalSESs,
       "wfDs1E1FarEndDayIntervalSEFSs": wfDs1E1FarEndDayIntervalSEFSs,
       "wfDs1E1FarEndDayIntervalUASs": wfDs1E1FarEndDayIntervalUASs,
       "wfDs1E1FarEndDayIntervalCSSs": wfDs1E1FarEndDayIntervalCSSs,
       "wfDs1E1FarEndDayIntervalPCVs": wfDs1E1FarEndDayIntervalPCVs,
       "wfDs1E1FarEndDayIntervalLESs": wfDs1E1FarEndDayIntervalLESs,
       "wfDs1E1FarEndDayIntervalBESs": wfDs1E1FarEndDayIntervalBESs,
       "wfDs1E1FarEndDayIntervalDMs": wfDs1E1FarEndDayIntervalDMs,
       "wfDs1E1FarEndDayIntervalLCVs": wfDs1E1FarEndDayIntervalLCVs,
       "wfDs1E1FarEndDayIntervalSASs": wfDs1E1FarEndDayIntervalSASs,
       "wfDs1E1FarEndDayIntervalAISSs": wfDs1E1FarEndDayIntervalAISSs,
       "wfDs1E1FarEndDayIntervalFCs": wfDs1E1FarEndDayIntervalFCs,
       "wfDs1E1FarEndDayIntervalValidFlag": wfDs1E1FarEndDayIntervalValidFlag,
       "wfDs1E1FarEndDayTotalTable": wfDs1E1FarEndDayTotalTable,
       "wfDs1E1FarEndDayTotalEntry": wfDs1E1FarEndDayTotalEntry,
       "wfDs1E1FarEndDayTotalPortLineNumber": wfDs1E1FarEndDayTotalPortLineNumber,
       "wfDs1E1FarEndDayTotalESs": wfDs1E1FarEndDayTotalESs,
       "wfDs1E1FarEndDayTotalSESs": wfDs1E1FarEndDayTotalSESs,
       "wfDs1E1FarEndDayTotalSEFSs": wfDs1E1FarEndDayTotalSEFSs,
       "wfDs1E1FarEndDayTotalUASs": wfDs1E1FarEndDayTotalUASs,
       "wfDs1E1FarEndDayTotalCSSs": wfDs1E1FarEndDayTotalCSSs,
       "wfDs1E1FarEndDayTotalPCVs": wfDs1E1FarEndDayTotalPCVs,
       "wfDs1E1FarEndDayTotalLESs": wfDs1E1FarEndDayTotalLESs,
       "wfDs1E1FarEndDayTotalBESs": wfDs1E1FarEndDayTotalBESs,
       "wfDs1E1FarEndDayTotalDMs": wfDs1E1FarEndDayTotalDMs,
       "wfDs1E1FarEndDayTotalLCVs": wfDs1E1FarEndDayTotalLCVs,
       "wfDs1E1FarEndDayTotalSASs": wfDs1E1FarEndDayTotalSASs,
       "wfDs1E1FarEndDayTotalAISSs": wfDs1E1FarEndDayTotalAISSs,
       "wfDs1E1FarEndDayTotalFCs": wfDs1E1FarEndDayTotalFCs,
       "wfDs1E1FarEndDayTotalValidFlag": wfDs1E1FarEndDayTotalValidFlag,
       "wfDs1E1ThrAlrtTable": wfDs1E1ThrAlrtTable,
       "wfDs1E1ThrAlrtEntry": wfDs1E1ThrAlrtEntry,
       "wfDs1E1ThrAlrtDelete": wfDs1E1ThrAlrtDelete,
       "wfDs1E1ThrAlrtPortLineNumber": wfDs1E1ThrAlrtPortLineNumber,
       "wfDs1E1ThrAlrtESs": wfDs1E1ThrAlrtESs,
       "wfDs1E1ThrAlrtSESs": wfDs1E1ThrAlrtSESs,
       "wfDs1E1ThrAlrtSEFSs": wfDs1E1ThrAlrtSEFSs,
       "wfDs1E1ThrAlrtUASs": wfDs1E1ThrAlrtUASs,
       "wfDs1E1ThrAlrtCSSs": wfDs1E1ThrAlrtCSSs,
       "wfDs1E1ThrAlrtPCVs": wfDs1E1ThrAlrtPCVs,
       "wfDs1E1ThrAlrtLESs": wfDs1E1ThrAlrtLESs,
       "wfDs1E1ThrAlrtBESs": wfDs1E1ThrAlrtBESs,
       "wfDs1E1ThrAlrtDMs": wfDs1E1ThrAlrtDMs,
       "wfDs1E1ThrAlrtLCVs": wfDs1E1ThrAlrtLCVs,
       "wfDs1E1ThrAlrtSASs": wfDs1E1ThrAlrtSASs,
       "wfDs1E1ThrAlrtAISSs": wfDs1E1ThrAlrtAISSs,
       "wfDs1E1ThrAlrtFCs": wfDs1E1ThrAlrtFCs,
       "wfDs1E1DayThrAlrtTable": wfDs1E1DayThrAlrtTable,
       "wfDs1E1DayThrAlrtEntry": wfDs1E1DayThrAlrtEntry,
       "wfDs1E1DayThrAlrtDelete": wfDs1E1DayThrAlrtDelete,
       "wfDs1E1DayThrAlrtPortLineNumber": wfDs1E1DayThrAlrtPortLineNumber,
       "wfDs1E1DayThrAlrtESs": wfDs1E1DayThrAlrtESs,
       "wfDs1E1DayThrAlrtSESs": wfDs1E1DayThrAlrtSESs,
       "wfDs1E1DayThrAlrtSEFSs": wfDs1E1DayThrAlrtSEFSs,
       "wfDs1E1DayThrAlrtUASs": wfDs1E1DayThrAlrtUASs,
       "wfDs1E1DayThrAlrtCSSs": wfDs1E1DayThrAlrtCSSs,
       "wfDs1E1DayThrAlrtPCVs": wfDs1E1DayThrAlrtPCVs,
       "wfDs1E1DayThrAlrtLESs": wfDs1E1DayThrAlrtLESs,
       "wfDs1E1DayThrAlrtBESs": wfDs1E1DayThrAlrtBESs,
       "wfDs1E1DayThrAlrtDMs": wfDs1E1DayThrAlrtDMs,
       "wfDs1E1DayThrAlrtLCVs": wfDs1E1DayThrAlrtLCVs,
       "wfDs1E1DayThrAlrtSASs": wfDs1E1DayThrAlrtSASs,
       "wfDs1E1DayThrAlrtAISSs": wfDs1E1DayThrAlrtAISSs,
       "wfDs1E1DayThrAlrtFCs": wfDs1E1DayThrAlrtFCs,
       "wfDs1E1FarEndThrAlrtTable": wfDs1E1FarEndThrAlrtTable,
       "wfDs1E1FarEndThrAlrtEntry": wfDs1E1FarEndThrAlrtEntry,
       "wfDs1E1FarEndThrAlrtDelete": wfDs1E1FarEndThrAlrtDelete,
       "wfDs1E1FarEndThrAlrtPortLineNumber": wfDs1E1FarEndThrAlrtPortLineNumber,
       "wfDs1E1FarEndThrAlrtESs": wfDs1E1FarEndThrAlrtESs,
       "wfDs1E1FarEndThrAlrtSESs": wfDs1E1FarEndThrAlrtSESs,
       "wfDs1E1FarEndThrAlrtSEFSs": wfDs1E1FarEndThrAlrtSEFSs,
       "wfDs1E1FarEndThrAlrtUASs": wfDs1E1FarEndThrAlrtUASs,
       "wfDs1E1FarEndThrAlrtCSSs": wfDs1E1FarEndThrAlrtCSSs,
       "wfDs1E1FarEndThrAlrtPCVs": wfDs1E1FarEndThrAlrtPCVs,
       "wfDs1E1FarEndThrAlrtLESs": wfDs1E1FarEndThrAlrtLESs,
       "wfDs1E1FarEndThrAlrtBESs": wfDs1E1FarEndThrAlrtBESs,
       "wfDs1E1FarEndThrAlrtDMs": wfDs1E1FarEndThrAlrtDMs,
       "wfDs1E1FarEndThrAlrtLCVs": wfDs1E1FarEndThrAlrtLCVs,
       "wfDs1E1FarEndThrAlrtSASs": wfDs1E1FarEndThrAlrtSASs,
       "wfDs1E1FarEndThrAlrtAISSs": wfDs1E1FarEndThrAlrtAISSs,
       "wfDs1E1FarEndThrAlrtFCs": wfDs1E1FarEndThrAlrtFCs,
       "wfDs1E1FarEndDayThrAlrtTable": wfDs1E1FarEndDayThrAlrtTable,
       "wfDs1E1FarEndDayThrAlrtEntry": wfDs1E1FarEndDayThrAlrtEntry,
       "wfDs1E1FarEndDayThrAlrtDelete": wfDs1E1FarEndDayThrAlrtDelete,
       "wfDs1E1FarEndDayThrAlrtPortLineNumber": wfDs1E1FarEndDayThrAlrtPortLineNumber,
       "wfDs1E1FarEndDayThrAlrtESs": wfDs1E1FarEndDayThrAlrtESs,
       "wfDs1E1FarEndDayThrAlrtSESs": wfDs1E1FarEndDayThrAlrtSESs,
       "wfDs1E1FarEndDayThrAlrtSEFSs": wfDs1E1FarEndDayThrAlrtSEFSs,
       "wfDs1E1FarEndDayThrAlrtUASs": wfDs1E1FarEndDayThrAlrtUASs,
       "wfDs1E1FarEndDayThrAlrtCSSs": wfDs1E1FarEndDayThrAlrtCSSs,
       "wfDs1E1FarEndDayThrAlrtPCVs": wfDs1E1FarEndDayThrAlrtPCVs,
       "wfDs1E1FarEndDayThrAlrtLESs": wfDs1E1FarEndDayThrAlrtLESs,
       "wfDs1E1FarEndDayThrAlrtBESs": wfDs1E1FarEndDayThrAlrtBESs,
       "wfDs1E1FarEndDayThrAlrtDMs": wfDs1E1FarEndDayThrAlrtDMs,
       "wfDs1E1FarEndDayThrAlrtLCVs": wfDs1E1FarEndDayThrAlrtLCVs,
       "wfDs1E1FarEndDayThrAlrtSASs": wfDs1E1FarEndDayThrAlrtSASs,
       "wfDs1E1FarEndDayThrAlrtAISSs": wfDs1E1FarEndDayThrAlrtAISSs,
       "wfDs1E1FarEndDayThrAlrtFCs": wfDs1E1FarEndDayThrAlrtFCs}
)
