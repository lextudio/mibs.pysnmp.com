# SNMP MIB module (Fore-Apsgroup-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Apsgroup-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:50 2024
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

(asx,
 atmSwitch) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx",
    "atmSwitch")

(hwPortBoard,
 hwPortModule,
 hwPortName,
 hwPortNumber) = mibBuilder.importSymbols(
    "Fore-Switch-MIB",
    "hwPortBoard",
    "hwPortModule",
    "hwPortName",
    "hwPortNumber")

(trapLogIndex,) = mibBuilder.importSymbols(
    "Fore-TrapLog-MIB",
    "trapLogIndex")

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

foreAps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApsPortGroup_ObjectIdentity = ObjectIdentity
apsPortGroup = _ApsPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1)
)
_ApsPortTable_Object = MibTable
apsPortTable = _ApsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    apsPortTable.setStatus("current")
_ApsPortEntry_Object = MibTableRow
apsPortEntry = _ApsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1)
)
apsPortEntry.setIndexNames(
    (0, "Fore-Apsgroup-MIB", "apsBoard"),
    (0, "Fore-Apsgroup-MIB", "apsModule"),
    (0, "Fore-Apsgroup-MIB", "apsPort"),
)
if mibBuilder.loadTexts:
    apsPortEntry.setStatus("current")
_ApsBoard_Type = Integer32
_ApsBoard_Object = MibTableColumn
apsBoard = _ApsBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 1),
    _ApsBoard_Type()
)
apsBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsBoard.setStatus("current")
_ApsModule_Type = Integer32
_ApsModule_Object = MibTableColumn
apsModule = _ApsModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 2),
    _ApsModule_Type()
)
apsModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsModule.setStatus("current")
_ApsPort_Type = Integer32
_ApsPort_Object = MibTableColumn
apsPort = _ApsPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 3),
    _ApsPort_Type()
)
apsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPort.setStatus("current")


class _ApsAdminMode_Type(Integer32):
    """Custom type apsAdminMode based on Integer32"""
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
        *(("protection", 2),
          ("unprotected", 3),
          ("working", 1))
    )


_ApsAdminMode_Type.__name__ = "Integer32"
_ApsAdminMode_Object = MibTableColumn
apsAdminMode = _ApsAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 4),
    _ApsAdminMode_Type()
)
apsAdminMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsAdminMode.setStatus("current")


class _ApsOperMode_Type(Integer32):
    """Custom type apsOperMode based on Integer32"""
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
        *(("active", 1),
          ("loopbackOff", 5),
          ("loopbackOn", 4),
          ("notApplicable", 3),
          ("standby", 2))
    )


_ApsOperMode_Type.__name__ = "Integer32"
_ApsOperMode_Object = MibTableColumn
apsOperMode = _ApsOperMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 5),
    _ApsOperMode_Type()
)
apsOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsOperMode.setStatus("current")
_ApsPortGroupName_Type = DisplayString
_ApsPortGroupName_Object = MibTableColumn
apsPortGroupName = _ApsPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 1, 1, 1, 6),
    _ApsPortGroupName_Type()
)
apsPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsPortGroupName.setStatus("current")
_ApsGroup_ObjectIdentity = ObjectIdentity
apsGroup = _ApsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2)
)
_ApsGroupTable_Object = MibTable
apsGroupTable = _ApsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    apsGroupTable.setStatus("current")
_ApsGroupEntry_Object = MibTableRow
apsGroupEntry = _ApsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1)
)
apsGroupEntry.setIndexNames(
    (0, "Fore-Apsgroup-MIB", "apsGroupName"),
)
if mibBuilder.loadTexts:
    apsGroupEntry.setStatus("current")
_ApsGroupName_Type = DisplayString
_ApsGroupName_Object = MibTableColumn
apsGroupName = _ApsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 1),
    _ApsGroupName_Type()
)
apsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsGroupName.setStatus("current")


class _ApsGroupStateCommand_Type(Integer32):
    """Custom type apsGroupStateCommand based on Integer32"""
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
        *(("clear", 1),
          ("forceSwitchToProtection", 4),
          ("forceSwitchToWorking", 3),
          ("lockout", 2),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 5))
    )


_ApsGroupStateCommand_Type.__name__ = "Integer32"
_ApsGroupStateCommand_Object = MibTableColumn
apsGroupStateCommand = _ApsGroupStateCommand_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 2),
    _ApsGroupStateCommand_Type()
)
apsGroupStateCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsGroupStateCommand.setStatus("current")


class _ApsGroupLastCommand_Type(Integer32):
    """Custom type apsGroupLastCommand based on Integer32"""
    defaultValue = 9

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
        *(("clear", 1),
          ("forceSwitchToProtection", 4),
          ("forceSwitchToWorking", 3),
          ("lockout", 2),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 5),
          ("noRequest", 9),
          ("suspendProtection", 8),
          ("suspendWorking", 7))
    )


_ApsGroupLastCommand_Type.__name__ = "Integer32"
_ApsGroupLastCommand_Object = MibTableColumn
apsGroupLastCommand = _ApsGroupLastCommand_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 3),
    _ApsGroupLastCommand_Type()
)
apsGroupLastCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsGroupLastCommand.setStatus("current")


class _ApsWorkingLineState_Type(Integer32):
    """Custom type apsWorkingLineState based on Integer32"""
    defaultValue = 3

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
        *(("none", 3),
          ("notAvailable", 4),
          ("signalDegrade", 2),
          ("signalFailure", 1))
    )


_ApsWorkingLineState_Type.__name__ = "Integer32"
_ApsWorkingLineState_Object = MibTableColumn
apsWorkingLineState = _ApsWorkingLineState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 4),
    _ApsWorkingLineState_Type()
)
apsWorkingLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsWorkingLineState.setStatus("current")


class _ApsProtectionLineState_Type(Integer32):
    """Custom type apsProtectionLineState based on Integer32"""
    defaultValue = 3

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
        *(("none", 3),
          ("notAvailable", 4),
          ("signalDegrade", 2),
          ("signalFailure", 1))
    )


_ApsProtectionLineState_Type.__name__ = "Integer32"
_ApsProtectionLineState_Object = MibTableColumn
apsProtectionLineState = _ApsProtectionLineState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 5),
    _ApsProtectionLineState_Type()
)
apsProtectionLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsProtectionLineState.setStatus("current")


class _ApsGroupMode_Type(Integer32):
    """Custom type apsGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bi-directional", 2),
          ("uni-directional", 1))
    )


_ApsGroupMode_Type.__name__ = "Integer32"
_ApsGroupMode_Object = MibTableColumn
apsGroupMode = _ApsGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 6),
    _ApsGroupMode_Type()
)
apsGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsGroupMode.setStatus("current")


class _ApsRxK1K2_Type(Integer32):
    """Custom type apsRxK1K2 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 9),
          ("exercise", 6),
          ("forceSwitch", 2),
          ("lockout", 1),
          ("manualSwitch", 3),
          ("noRequest", 10),
          ("none", 11),
          ("notAvailable", 12),
          ("reverseRequest", 8),
          ("signalDegrade", 5),
          ("signalFailure", 4),
          ("waitToRestore", 7))
    )


_ApsRxK1K2_Type.__name__ = "Integer32"
_ApsRxK1K2_Object = MibTableColumn
apsRxK1K2 = _ApsRxK1K2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 7),
    _ApsRxK1K2_Type()
)
apsRxK1K2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsRxK1K2.setStatus("current")


class _ApsRxChannel_Type(Integer32):
    """Custom type apsRxChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("protection", 2),
          ("working", 1))
    )


_ApsRxChannel_Type.__name__ = "Integer32"
_ApsRxChannel_Object = MibTableColumn
apsRxChannel = _ApsRxChannel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 8),
    _ApsRxChannel_Type()
)
apsRxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsRxChannel.setStatus("current")


class _ApsTxK1K2_Type(Integer32):
    """Custom type apsTxK1K2 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 9),
          ("exercise", 6),
          ("forceSwitch", 2),
          ("lockout", 1),
          ("manualSwitch", 3),
          ("noRequest", 10),
          ("none", 11),
          ("notAvailable", 12),
          ("reverseRequest", 8),
          ("signalDegrade", 5),
          ("signalFailure", 4),
          ("waitToRestore", 7))
    )


_ApsTxK1K2_Type.__name__ = "Integer32"
_ApsTxK1K2_Object = MibTableColumn
apsTxK1K2 = _ApsTxK1K2_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 9),
    _ApsTxK1K2_Type()
)
apsTxK1K2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTxK1K2.setStatus("current")


class _ApsTxChannel_Type(Integer32):
    """Custom type apsTxChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("protection", 2),
          ("working", 1))
    )


_ApsTxChannel_Type.__name__ = "Integer32"
_ApsTxChannel_Object = MibTableColumn
apsTxChannel = _ApsTxChannel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 10),
    _ApsTxChannel_Type()
)
apsTxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTxChannel.setStatus("current")


class _ApsRevertMode_Type(Integer32):
    """Custom type apsRevertMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ApsRevertMode_Type.__name__ = "Integer32"
_ApsRevertMode_Object = MibTableColumn
apsRevertMode = _ApsRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 11),
    _ApsRevertMode_Type()
)
apsRevertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsRevertMode.setStatus("current")


class _ApsRevertTimer_Type(Integer32):
    """Custom type apsRevertTimer based on Integer32"""
    defaultValue = 5


_ApsRevertTimer_Object = MibTableColumn
apsRevertTimer = _ApsRevertTimer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 16, 2, 1, 1, 12),
    _ApsRevertTimer_Type()
)
apsRevertTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsRevertTimer.setStatus("current")

# Managed Objects groups


# Notification objects

apsSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 0, 2017)
)
apsSwitchOver.setObjects(
      *(("Fore-Switch-MIB", "hwPortName"),
        ("Fore-Switch-MIB", "hwPortBoard"),
        ("Fore-Switch-MIB", "hwPortModule"),
        ("Fore-Switch-MIB", "hwPortNumber"),
        ("Fore-TrapLog-MIB", "trapLogIndex"))
)
if mibBuilder.loadTexts:
    apsSwitchOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Apsgroup-MIB",
    **{"apsSwitchOver": apsSwitchOver,
       "foreAps": foreAps,
       "apsPortGroup": apsPortGroup,
       "apsPortTable": apsPortTable,
       "apsPortEntry": apsPortEntry,
       "apsBoard": apsBoard,
       "apsModule": apsModule,
       "apsPort": apsPort,
       "apsAdminMode": apsAdminMode,
       "apsOperMode": apsOperMode,
       "apsPortGroupName": apsPortGroupName,
       "apsGroup": apsGroup,
       "apsGroupTable": apsGroupTable,
       "apsGroupEntry": apsGroupEntry,
       "apsGroupName": apsGroupName,
       "apsGroupStateCommand": apsGroupStateCommand,
       "apsGroupLastCommand": apsGroupLastCommand,
       "apsWorkingLineState": apsWorkingLineState,
       "apsProtectionLineState": apsProtectionLineState,
       "apsGroupMode": apsGroupMode,
       "apsRxK1K2": apsRxK1K2,
       "apsRxChannel": apsRxChannel,
       "apsTxK1K2": apsTxK1K2,
       "apsTxChannel": apsTxChannel,
       "apsRevertMode": apsRevertMode,
       "apsRevertTimer": apsRevertTimer}
)
