# SNMP MIB module (RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(stratacom,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "stratacom")

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

_Rtm_ObjectIdentity = ObjectIdentity
rtm = _Rtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120)
)
_TrapsConfig_ObjectIdentity = ObjectIdentity
trapsConfig = _TrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 120, 1)
)
_TrapConfigTable_Object = MibTable
trapConfigTable = _TrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1)
)
if mibBuilder.loadTexts:
    trapConfigTable.setStatus("mandatory")
_TrapConfigEntry_Object = MibTableRow
trapConfigEntry = _TrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1)
)
trapConfigEntry.setIndexNames(
    (0, "RTM-MIB", "managerIPaddress"),
)
if mibBuilder.loadTexts:
    trapConfigEntry.setStatus("mandatory")
_ManagerIPaddress_Type = IpAddress
_ManagerIPaddress_Object = MibTableColumn
managerIPaddress = _ManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1),
    _ManagerIPaddress_Type()
)
managerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIPaddress.setStatus("mandatory")
_ManagerPortNumber_Type = Integer32
_ManagerPortNumber_Object = MibTableColumn
managerPortNumber = _ManagerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2),
    _ManagerPortNumber_Type()
)
managerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerPortNumber.setStatus("mandatory")


class _ManagerRowStatus_Type(Integer32):
    """Custom type managerRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addRow", 1),
          ("delRow", 2))
    )


_ManagerRowStatus_Type.__name__ = "Integer32"
_ManagerRowStatus_Object = MibTableColumn
managerRowStatus = _ManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3),
    _ManagerRowStatus_Type()
)
managerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerRowStatus.setStatus("mandatory")


class _ReadingTrapsFlag_Type(Integer32):
    """Custom type readingTrapsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_ReadingTrapsFlag_Type.__name__ = "Integer32"
_ReadingTrapsFlag_Object = MibTableColumn
readingTrapsFlag = _ReadingTrapsFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4),
    _ReadingTrapsFlag_Type()
)
readingTrapsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readingTrapsFlag.setStatus("mandatory")
_NextTrapSeqNum_Type = Integer32
_NextTrapSeqNum_Object = MibTableColumn
nextTrapSeqNum = _NextTrapSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5),
    _NextTrapSeqNum_Type()
)
nextTrapSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextTrapSeqNum.setStatus("mandatory")


class _ManagerNumOfValidEntries_Type(Integer32):
    """Custom type managerNumOfValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ManagerNumOfValidEntries_Type.__name__ = "Integer32"
_ManagerNumOfValidEntries_Object = MibScalar
managerNumOfValidEntries = _ManagerNumOfValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 2),
    _ManagerNumOfValidEntries_Type()
)
managerNumOfValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managerNumOfValidEntries.setStatus("mandatory")
_LastSequenceNumber_Type = Integer32
_LastSequenceNumber_Object = MibScalar
lastSequenceNumber = _LastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 3),
    _LastSequenceNumber_Type()
)
lastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSequenceNumber.setStatus("mandatory")
_TrapUploadTable_Object = MibTable
trapUploadTable = _TrapUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4)
)
if mibBuilder.loadTexts:
    trapUploadTable.setStatus("mandatory")
_TrapUploadEntry_Object = MibTableRow
trapUploadEntry = _TrapUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1)
)
trapUploadEntry.setIndexNames(
    (0, "RTM-MIB", "trapManagerIPaddress"),
)
if mibBuilder.loadTexts:
    trapUploadEntry.setStatus("mandatory")
_TrapManagerIPaddress_Type = IpAddress
_TrapManagerIPaddress_Object = MibTableColumn
trapManagerIPaddress = _TrapManagerIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1),
    _TrapManagerIPaddress_Type()
)
trapManagerIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapManagerIPaddress.setStatus("mandatory")
_TrapSequenceNum_Type = Integer32
_TrapSequenceNum_Object = MibTableColumn
trapSequenceNum = _TrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2),
    _TrapSequenceNum_Type()
)
trapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNum.setStatus("mandatory")
_TrapPduString_Type = DisplayString
_TrapPduString_Object = MibTableColumn
trapPduString = _TrapPduString_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3),
    _TrapPduString_Type()
)
trapPduString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPduString.setStatus("mandatory")


class _EndOfQueueFlag_Type(Integer32):
    """Custom type endOfQueueFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_EndOfQueueFlag_Type.__name__ = "Integer32"
_EndOfQueueFlag_Object = MibTableColumn
endOfQueueFlag = _EndOfQueueFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4),
    _EndOfQueueFlag_Type()
)
endOfQueueFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfQueueFlag.setStatus("mandatory")
_RecoverTrapTable_Object = MibTable
recoverTrapTable = _RecoverTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 5)
)
if mibBuilder.loadTexts:
    recoverTrapTable.setStatus("mandatory")
_RecoverTrapEntry_Object = MibTableRow
recoverTrapEntry = _RecoverTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1)
)
recoverTrapEntry.setIndexNames(
    (0, "RTM-MIB", "recoverTrapSequenceNum"),
)
if mibBuilder.loadTexts:
    recoverTrapEntry.setStatus("mandatory")


class _RecoverTrapSequenceNum_Type(Integer32):
    """Custom type recoverTrapSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RecoverTrapSequenceNum_Type.__name__ = "Integer32"
_RecoverTrapSequenceNum_Object = MibTableColumn
recoverTrapSequenceNum = _RecoverTrapSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 1),
    _RecoverTrapSequenceNum_Type()
)
recoverTrapSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recoverTrapSequenceNum.setStatus("mandatory")


class _RecoverTrapPduString_Type(OctetString):
    """Custom type recoverTrapPduString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RecoverTrapPduString_Type.__name__ = "OctetString"
_RecoverTrapPduString_Object = MibTableColumn
recoverTrapPduString = _RecoverTrapPduString_Object(
    (1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 2),
    _RecoverTrapPduString_Type()
)
recoverTrapPduString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recoverTrapPduString.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTM-MIB",
    **{"rtm": rtm,
       "trapsConfig": trapsConfig,
       "trapConfigTable": trapConfigTable,
       "trapConfigEntry": trapConfigEntry,
       "managerIPaddress": managerIPaddress,
       "managerPortNumber": managerPortNumber,
       "managerRowStatus": managerRowStatus,
       "readingTrapsFlag": readingTrapsFlag,
       "nextTrapSeqNum": nextTrapSeqNum,
       "managerNumOfValidEntries": managerNumOfValidEntries,
       "lastSequenceNumber": lastSequenceNumber,
       "trapUploadTable": trapUploadTable,
       "trapUploadEntry": trapUploadEntry,
       "trapManagerIPaddress": trapManagerIPaddress,
       "trapSequenceNum": trapSequenceNum,
       "trapPduString": trapPduString,
       "endOfQueueFlag": endOfQueueFlag,
       "recoverTrapTable": recoverTrapTable,
       "recoverTrapEntry": recoverTrapEntry,
       "recoverTrapSequenceNum": recoverTrapSequenceNum,
       "recoverTrapPduString": recoverTrapPduString}
)
