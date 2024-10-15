# SNMP MIB module (Fore-PLCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-PLCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:08 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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

forePlcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ForePlcpConfigTable_Object = MibTable
forePlcpConfigTable = _ForePlcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    forePlcpConfigTable.setStatus("current")
_ForePlcpConfigEntry_Object = MibTableRow
forePlcpConfigEntry = _ForePlcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1, 1)
)
forePlcpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    forePlcpConfigEntry.setStatus("current")


class _ForePlcpConfigFrameFormat_Type(Integer32):
    """Custom type forePlcpConfigFrameFormat based on Integer32"""
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
        *(("forePlcpFrameFormatDs1", 1),
          ("forePlcpFrameFormatDs3", 3),
          ("forePlcpFrameFormatE1", 2),
          ("forePlcpFrameFormatE3", 4))
    )


_ForePlcpConfigFrameFormat_Type.__name__ = "Integer32"
_ForePlcpConfigFrameFormat_Object = MibTableColumn
forePlcpConfigFrameFormat = _ForePlcpConfigFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 1, 1, 1),
    _ForePlcpConfigFrameFormat_Type()
)
forePlcpConfigFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forePlcpConfigFrameFormat.setStatus("current")
_ForePlcpTotalTable_Object = MibTable
forePlcpTotalTable = _ForePlcpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    forePlcpTotalTable.setStatus("current")
_ForePlcpTotalEntry_Object = MibTableRow
forePlcpTotalEntry = _ForePlcpTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1)
)
forePlcpTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    forePlcpTotalEntry.setStatus("current")
_ForePlcpTotalFerrCount_Type = Counter32
_ForePlcpTotalFerrCount_Object = MibTableColumn
forePlcpTotalFerrCount = _ForePlcpTotalFerrCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 1),
    _ForePlcpTotalFerrCount_Type()
)
forePlcpTotalFerrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpTotalFerrCount.setStatus("current")
_ForePlcpTotalLofSeconds_Type = Counter32
_ForePlcpTotalLofSeconds_Object = MibTableColumn
forePlcpTotalLofSeconds = _ForePlcpTotalLofSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 2),
    _ForePlcpTotalLofSeconds_Type()
)
forePlcpTotalLofSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpTotalLofSeconds.setStatus("current")
_ForePlcpTotalBip8Count_Type = Counter32
_ForePlcpTotalBip8Count_Object = MibTableColumn
forePlcpTotalBip8Count = _ForePlcpTotalBip8Count_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 3),
    _ForePlcpTotalBip8Count_Type()
)
forePlcpTotalBip8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpTotalBip8Count.setStatus("current")
_ForePlcpTotalFebeCount_Type = Counter32
_ForePlcpTotalFebeCount_Object = MibTableColumn
forePlcpTotalFebeCount = _ForePlcpTotalFebeCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 4),
    _ForePlcpTotalFebeCount_Type()
)
forePlcpTotalFebeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpTotalFebeCount.setStatus("current")
_ForePlcpTotalYellowAlarmSeconds_Type = Counter32
_ForePlcpTotalYellowAlarmSeconds_Object = MibTableColumn
forePlcpTotalYellowAlarmSeconds = _ForePlcpTotalYellowAlarmSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 2, 1, 5),
    _ForePlcpTotalYellowAlarmSeconds_Type()
)
forePlcpTotalYellowAlarmSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpTotalYellowAlarmSeconds.setStatus("current")
_ForePlcpCurrentTable_Object = MibTable
forePlcpCurrentTable = _ForePlcpCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3)
)
if mibBuilder.loadTexts:
    forePlcpCurrentTable.setStatus("current")
_ForePlcpCurrentEntry_Object = MibTableRow
forePlcpCurrentEntry = _ForePlcpCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1)
)
forePlcpCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    forePlcpCurrentEntry.setStatus("current")
_ForePlcpCurrentFerrCount_Type = Counter32
_ForePlcpCurrentFerrCount_Object = MibTableColumn
forePlcpCurrentFerrCount = _ForePlcpCurrentFerrCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 1),
    _ForePlcpCurrentFerrCount_Type()
)
forePlcpCurrentFerrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentFerrCount.setStatus("current")
_ForePlcpCurrentBip8Count_Type = Counter32
_ForePlcpCurrentBip8Count_Object = MibTableColumn
forePlcpCurrentBip8Count = _ForePlcpCurrentBip8Count_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 2),
    _ForePlcpCurrentBip8Count_Type()
)
forePlcpCurrentBip8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentBip8Count.setStatus("current")
_ForePlcpCurrentFebeCount_Type = Counter32
_ForePlcpCurrentFebeCount_Object = MibTableColumn
forePlcpCurrentFebeCount = _ForePlcpCurrentFebeCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 3),
    _ForePlcpCurrentFebeCount_Type()
)
forePlcpCurrentFebeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentFebeCount.setStatus("current")
_ForePlcpCurrentErrSeconds_Type = Counter32
_ForePlcpCurrentErrSeconds_Object = MibTableColumn
forePlcpCurrentErrSeconds = _ForePlcpCurrentErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 4),
    _ForePlcpCurrentErrSeconds_Type()
)
forePlcpCurrentErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentErrSeconds.setStatus("current")
_ForePlcpCurrentSevErrSeconds_Type = Counter32
_ForePlcpCurrentSevErrSeconds_Object = MibTableColumn
forePlcpCurrentSevErrSeconds = _ForePlcpCurrentSevErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 5),
    _ForePlcpCurrentSevErrSeconds_Type()
)
forePlcpCurrentSevErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentSevErrSeconds.setStatus("current")
_ForePlcpCurrentUnavailSeconds_Type = Counter32
_ForePlcpCurrentUnavailSeconds_Object = MibTableColumn
forePlcpCurrentUnavailSeconds = _ForePlcpCurrentUnavailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 3, 1, 6),
    _ForePlcpCurrentUnavailSeconds_Type()
)
forePlcpCurrentUnavailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpCurrentUnavailSeconds.setStatus("current")
_ForePlcpIntervalTable_Object = MibTable
forePlcpIntervalTable = _ForePlcpIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    forePlcpIntervalTable.setStatus("current")
_ForePlcpIntervalEntry_Object = MibTableRow
forePlcpIntervalEntry = _ForePlcpIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1)
)
forePlcpIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Fore-PLCP-MIB", "forePlcpInterval"),
)
if mibBuilder.loadTexts:
    forePlcpIntervalEntry.setStatus("current")
_ForePlcpInterval_Type = Integer32
_ForePlcpInterval_Object = MibTableColumn
forePlcpInterval = _ForePlcpInterval_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 1),
    _ForePlcpInterval_Type()
)
forePlcpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpInterval.setStatus("current")
_ForePlcpIntervalFerrCount_Type = Counter32
_ForePlcpIntervalFerrCount_Object = MibTableColumn
forePlcpIntervalFerrCount = _ForePlcpIntervalFerrCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 2),
    _ForePlcpIntervalFerrCount_Type()
)
forePlcpIntervalFerrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalFerrCount.setStatus("current")
_ForePlcpIntervalBip8Count_Type = Counter32
_ForePlcpIntervalBip8Count_Object = MibTableColumn
forePlcpIntervalBip8Count = _ForePlcpIntervalBip8Count_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 3),
    _ForePlcpIntervalBip8Count_Type()
)
forePlcpIntervalBip8Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalBip8Count.setStatus("current")
_ForePlcpIntervalFebeCount_Type = Counter32
_ForePlcpIntervalFebeCount_Object = MibTableColumn
forePlcpIntervalFebeCount = _ForePlcpIntervalFebeCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 4),
    _ForePlcpIntervalFebeCount_Type()
)
forePlcpIntervalFebeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalFebeCount.setStatus("current")
_ForePlcpIntervalErrSeconds_Type = Counter32
_ForePlcpIntervalErrSeconds_Object = MibTableColumn
forePlcpIntervalErrSeconds = _ForePlcpIntervalErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 5),
    _ForePlcpIntervalErrSeconds_Type()
)
forePlcpIntervalErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalErrSeconds.setStatus("current")
_ForePlcpIntervalSevErrSeconds_Type = Counter32
_ForePlcpIntervalSevErrSeconds_Object = MibTableColumn
forePlcpIntervalSevErrSeconds = _ForePlcpIntervalSevErrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 6),
    _ForePlcpIntervalSevErrSeconds_Type()
)
forePlcpIntervalSevErrSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalSevErrSeconds.setStatus("current")
_ForePlcpIntervalUnavailSeconds_Type = Counter32
_ForePlcpIntervalUnavailSeconds_Object = MibTableColumn
forePlcpIntervalUnavailSeconds = _ForePlcpIntervalUnavailSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 4, 1, 7),
    _ForePlcpIntervalUnavailSeconds_Type()
)
forePlcpIntervalUnavailSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forePlcpIntervalUnavailSeconds.setStatus("current")

# Managed Objects groups


# Notification objects

forePlcpYellowDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 1)
)
forePlcpYellowDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    forePlcpYellowDetected.setStatus(
        "current"
    )

forePlcpYellowCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 2)
)
forePlcpYellowCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    forePlcpYellowCleared.setStatus(
        "current"
    )

forePlcpLOFDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 3)
)
forePlcpLOFDetected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    forePlcpLOFDetected.setStatus(
        "current"
    )

forePlcpLOFCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 13, 0, 4)
)
forePlcpLOFCleared.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    forePlcpLOFCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-PLCP-MIB",
    **{"forePlcpMib": forePlcpMib,
       "forePlcpYellowDetected": forePlcpYellowDetected,
       "forePlcpYellowCleared": forePlcpYellowCleared,
       "forePlcpLOFDetected": forePlcpLOFDetected,
       "forePlcpLOFCleared": forePlcpLOFCleared,
       "forePlcpConfigTable": forePlcpConfigTable,
       "forePlcpConfigEntry": forePlcpConfigEntry,
       "forePlcpConfigFrameFormat": forePlcpConfigFrameFormat,
       "forePlcpTotalTable": forePlcpTotalTable,
       "forePlcpTotalEntry": forePlcpTotalEntry,
       "forePlcpTotalFerrCount": forePlcpTotalFerrCount,
       "forePlcpTotalLofSeconds": forePlcpTotalLofSeconds,
       "forePlcpTotalBip8Count": forePlcpTotalBip8Count,
       "forePlcpTotalFebeCount": forePlcpTotalFebeCount,
       "forePlcpTotalYellowAlarmSeconds": forePlcpTotalYellowAlarmSeconds,
       "forePlcpCurrentTable": forePlcpCurrentTable,
       "forePlcpCurrentEntry": forePlcpCurrentEntry,
       "forePlcpCurrentFerrCount": forePlcpCurrentFerrCount,
       "forePlcpCurrentBip8Count": forePlcpCurrentBip8Count,
       "forePlcpCurrentFebeCount": forePlcpCurrentFebeCount,
       "forePlcpCurrentErrSeconds": forePlcpCurrentErrSeconds,
       "forePlcpCurrentSevErrSeconds": forePlcpCurrentSevErrSeconds,
       "forePlcpCurrentUnavailSeconds": forePlcpCurrentUnavailSeconds,
       "forePlcpIntervalTable": forePlcpIntervalTable,
       "forePlcpIntervalEntry": forePlcpIntervalEntry,
       "forePlcpInterval": forePlcpInterval,
       "forePlcpIntervalFerrCount": forePlcpIntervalFerrCount,
       "forePlcpIntervalBip8Count": forePlcpIntervalBip8Count,
       "forePlcpIntervalFebeCount": forePlcpIntervalFebeCount,
       "forePlcpIntervalErrSeconds": forePlcpIntervalErrSeconds,
       "forePlcpIntervalSevErrSeconds": forePlcpIntervalSevErrSeconds,
       "forePlcpIntervalUnavailSeconds": forePlcpIntervalUnavailSeconds}
)
