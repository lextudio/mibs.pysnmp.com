# SNMP MIB module (SHIVA-MLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-MLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:42 2024
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

(messageLog,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "messageLog")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MLogEntryCount_Type = Integer32
_MLogEntryCount_Object = MibScalar
mLogEntryCount = _MLogEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 1),
    _MLogEntryCount_Type()
)
mLogEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogEntryCount.setStatus("deprecated")


class _MLogNewMessageTrapEnable_Type(Integer32):
    """Custom type mLogNewMessageTrapEnable based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("crit", 4),
          ("debug", 9),
          ("disabled", 1),
          ("emerg", 2),
          ("err", 5),
          ("info", 8),
          ("notice", 7),
          ("warning", 6))
    )


_MLogNewMessageTrapEnable_Type.__name__ = "Integer32"
_MLogNewMessageTrapEnable_Object = MibScalar
mLogNewMessageTrapEnable = _MLogNewMessageTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 2),
    _MLogNewMessageTrapEnable_Type()
)
mLogNewMessageTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mLogNewMessageTrapEnable.setStatus("deprecated")
_MLogBuffer_Object = MibTable
mLogBuffer = _MLogBuffer_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mLogBuffer.setStatus("deprecated")
_MLogMessage_Object = MibTableRow
mLogMessage = _MLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1)
)
mLogMessage.setIndexNames(
    (0, "SHIVA-MLOG-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    mLogMessage.setStatus("deprecated")
_MLogTimeStamp_Type = TimeTicks
_MLogTimeStamp_Object = MibTableColumn
mLogTimeStamp = _MLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 1),
    _MLogTimeStamp_Type()
)
mLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogTimeStamp.setStatus("deprecated")


class _MLogPriority_Type(Integer32):
    """Custom type mLogPriority based on Integer32"""
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
        *(("alert", 3),
          ("crit", 4),
          ("debug", 9),
          ("emerg", 2),
          ("err", 5),
          ("info", 8),
          ("not-possible", 1),
          ("notice", 7),
          ("warning", 6))
    )


_MLogPriority_Type.__name__ = "Integer32"
_MLogPriority_Object = MibTableColumn
mLogPriority = _MLogPriority_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 2),
    _MLogPriority_Type()
)
mLogPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogPriority.setStatus("deprecated")
_MLogMessageText_Type = DisplayString
_MLogMessageText_Object = MibTableColumn
mLogMessageText = _MLogMessageText_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 3),
    _MLogMessageText_Type()
)
mLogMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogMessageText.setStatus("deprecated")
_MLogTimeOfDay_Type = Integer32
_MLogTimeOfDay_Object = MibTableColumn
mLogTimeOfDay = _MLogTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4),
    _MLogTimeOfDay_Type()
)
mLogTimeOfDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mLogTimeOfDay.setStatus("deprecated")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 166, 1, 1, 3, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-MLOG-MIB",
    **{"mLogEntryCount": mLogEntryCount,
       "mLogNewMessageTrapEnable": mLogNewMessageTrapEnable,
       "mLogBuffer": mLogBuffer,
       "mLogMessage": mLogMessage,
       "mLogTimeStamp": mLogTimeStamp,
       "mLogPriority": mLogPriority,
       "mLogMessageText": mLogMessageText,
       "mLogTimeOfDay": mLogTimeOfDay,
       "pysmiFakeCol1": pysmiFakeCol1}
)
