# SNMP MIB module (Fore-SSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-SSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:14 2024
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

(syncStatusMsgGroup,) = mibBuilder.importSymbols(
    "Fore-Switch-MIB",
    "syncStatusMsgGroup")

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

sysStatusMsgModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 4)
)


# Types definitions



class SyncStatusMsgType(Integer32):
    """Custom type SyncStatusMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12,
              13,
              15,
              16,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("dus", 16),
          ("invalid", 100),
          ("none", 101),
          ("prc", 2),
          ("prs", 1),
          ("res", 15),
          ("sec", 11),
          ("smc", 12),
          ("ssub", 9),
          ("st2", 4),
          ("st3", 10),
          ("st3e", 8),
          ("st4", 13),
          ("stu", 3),
          ("tncssua", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SyncStatusMsgTable_Object = MibTable
syncStatusMsgTable = _SyncStatusMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    syncStatusMsgTable.setStatus("current")
_SyncStatusMsgEntry_Object = MibTableRow
syncStatusMsgEntry = _SyncStatusMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1)
)
syncStatusMsgEntry.setIndexNames(
    (1, "Fore-SSM-MIB", "syncStatusMsgInterface"),
)
if mibBuilder.loadTexts:
    syncStatusMsgEntry.setStatus("current")


class _SyncStatusMsgInterface_Type(DisplayString):
    """Custom type syncStatusMsgInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SyncStatusMsgInterface_Type.__name__ = "DisplayString"
_SyncStatusMsgInterface_Object = MibTableColumn
syncStatusMsgInterface = _SyncStatusMsgInterface_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 1),
    _SyncStatusMsgInterface_Type()
)
syncStatusMsgInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syncStatusMsgInterface.setStatus("current")
_SyncStatusMsgRxMessage_Type = SyncStatusMsgType
_SyncStatusMsgRxMessage_Object = MibTableColumn
syncStatusMsgRxMessage = _SyncStatusMsgRxMessage_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 2),
    _SyncStatusMsgRxMessage_Type()
)
syncStatusMsgRxMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatusMsgRxMessage.setStatus("current")
_SyncStatusMsgTxMessage_Type = SyncStatusMsgType
_SyncStatusMsgTxMessage_Object = MibTableColumn
syncStatusMsgTxMessage = _SyncStatusMsgTxMessage_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 3),
    _SyncStatusMsgTxMessage_Type()
)
syncStatusMsgTxMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatusMsgTxMessage.setStatus("current")
_SyncStatusMsgForceRxSsm_Type = SyncStatusMsgType
_SyncStatusMsgForceRxSsm_Object = MibTableColumn
syncStatusMsgForceRxSsm = _SyncStatusMsgForceRxSsm_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 4),
    _SyncStatusMsgForceRxSsm_Type()
)
syncStatusMsgForceRxSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncStatusMsgForceRxSsm.setStatus("current")


class _SyncStatusMsgForceDus_Type(Integer32):
    """Custom type syncStatusMsgForceDus based on Integer32"""
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


_SyncStatusMsgForceDus_Type.__name__ = "Integer32"
_SyncStatusMsgForceDus_Object = MibTableColumn
syncStatusMsgForceDus = _SyncStatusMsgForceDus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 5),
    _SyncStatusMsgForceDus_Type()
)
syncStatusMsgForceDus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncStatusMsgForceDus.setStatus("current")
_SyncStatusMsgPrevRxMessage_Type = SyncStatusMsgType
_SyncStatusMsgPrevRxMessage_Object = MibTableColumn
syncStatusMsgPrevRxMessage = _SyncStatusMsgPrevRxMessage_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 1, 1, 6),
    _SyncStatusMsgPrevRxMessage_Type()
)
syncStatusMsgPrevRxMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syncStatusMsgPrevRxMessage.setStatus("current")


class _SyncStatusMsgAutomaticRefSwitching_Type(Integer32):
    """Custom type syncStatusMsgAutomaticRefSwitching based on Integer32"""
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


_SyncStatusMsgAutomaticRefSwitching_Type.__name__ = "Integer32"
_SyncStatusMsgAutomaticRefSwitching_Object = MibScalar
syncStatusMsgAutomaticRefSwitching = _SyncStatusMsgAutomaticRefSwitching_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 2),
    _SyncStatusMsgAutomaticRefSwitching_Type()
)
syncStatusMsgAutomaticRefSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncStatusMsgAutomaticRefSwitching.setStatus("current")


class _SyncStatusMsgSdhOption_Type(Integer32):
    """Custom type syncStatusMsgSdhOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optionI", 1),
          ("optionII", 2))
    )


_SyncStatusMsgSdhOption_Type.__name__ = "Integer32"
_SyncStatusMsgSdhOption_Object = MibScalar
syncStatusMsgSdhOption = _SyncStatusMsgSdhOption_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 3),
    _SyncStatusMsgSdhOption_Type()
)
syncStatusMsgSdhOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncStatusMsgSdhOption.setStatus("current")

# Managed Objects groups


# Notification objects

syncStatusMsgChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 1, 21, 0, 1)
)
syncStatusMsgChanged.setObjects(
      *(("Fore-SSM-MIB", "syncStatusMsgPrevRxMessage"),
        ("Fore-SSM-MIB", "syncStatusMsgRxMessage"))
)
if mibBuilder.loadTexts:
    syncStatusMsgChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-SSM-MIB",
    **{"SyncStatusMsgType": SyncStatusMsgType,
       "syncStatusMsgChanged": syncStatusMsgChanged,
       "syncStatusMsgTable": syncStatusMsgTable,
       "syncStatusMsgEntry": syncStatusMsgEntry,
       "syncStatusMsgInterface": syncStatusMsgInterface,
       "syncStatusMsgRxMessage": syncStatusMsgRxMessage,
       "syncStatusMsgTxMessage": syncStatusMsgTxMessage,
       "syncStatusMsgForceRxSsm": syncStatusMsgForceRxSsm,
       "syncStatusMsgForceDus": syncStatusMsgForceDus,
       "syncStatusMsgPrevRxMessage": syncStatusMsgPrevRxMessage,
       "syncStatusMsgAutomaticRefSwitching": syncStatusMsgAutomaticRefSwitching,
       "syncStatusMsgSdhOption": syncStatusMsgSdhOption,
       "sysStatusMsgModule": sysStatusMsgModule}
)
