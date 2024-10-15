# SNMP MIB module (ACC-CALLINGNUMBER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-CALLINGNUMBER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:58 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccCallingNumber_ObjectIdentity = ObjectIdentity
accCallingNumber = _AccCallingNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67)
)
_AccCallingNumberTable_Object = MibTable
accCallingNumberTable = _AccCallingNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1)
)
if mibBuilder.loadTexts:
    accCallingNumberTable.setStatus("mandatory")
_AccCallingNumberEntry_Object = MibTableRow
accCallingNumberEntry = _AccCallingNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1)
)
accCallingNumberEntry.setIndexNames(
    (0, "ACC-CALLINGNUMBER", "accCallingNumberGroup"),
)
if mibBuilder.loadTexts:
    accCallingNumberEntry.setStatus("mandatory")


class _AccCallingNumberGroup_Type(Integer32):
    """Custom type accCallingNumberGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccCallingNumberGroup_Type.__name__ = "Integer32"
_AccCallingNumberGroup_Object = MibTableColumn
accCallingNumberGroup = _AccCallingNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 1),
    _AccCallingNumberGroup_Type()
)
accCallingNumberGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberGroup.setStatus("mandatory")


class _AccCallingNumberType_Type(Integer32):
    """Custom type accCallingNumberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              16,
              24,
              31)
        )
    )
    namedValues = NamedValues(
        *(("any", 31),
          ("audio", 16),
          ("cm56", 1),
          ("cm64", 2),
          ("data", 7),
          ("modem", 24),
          ("rdi", 4),
          ("udi", 3),
          ("voice", 8))
    )


_AccCallingNumberType_Type.__name__ = "Integer32"
_AccCallingNumberType_Object = MibTableColumn
accCallingNumberType = _AccCallingNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 2),
    _AccCallingNumberType_Type()
)
accCallingNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberType.setStatus("mandatory")
_AccCallingNumberDigits_Type = DisplayString
_AccCallingNumberDigits_Object = MibTableColumn
accCallingNumberDigits = _AccCallingNumberDigits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 3),
    _AccCallingNumberDigits_Type()
)
accCallingNumberDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberDigits.setStatus("mandatory")


class _AccCallingNumberAction_Type(Integer32):
    """Custom type accCallingNumberAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccCallingNumberAction_Type.__name__ = "Integer32"
_AccCallingNumberAction_Object = MibTableColumn
accCallingNumberAction = _AccCallingNumberAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 4),
    _AccCallingNumberAction_Type()
)
accCallingNumberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberAction.setStatus("mandatory")


class _AccCallingNumberStatus_Type(Integer32):
    """Custom type accCallingNumberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccCallingNumberStatus_Type.__name__ = "Integer32"
_AccCallingNumberStatus_Object = MibTableColumn
accCallingNumberStatus = _AccCallingNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 5),
    _AccCallingNumberStatus_Type()
)
accCallingNumberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberStatus.setStatus("mandatory")
_AccCallingNumberCallbackNumber_Type = DisplayString
_AccCallingNumberCallbackNumber_Object = MibTableColumn
accCallingNumberCallbackNumber = _AccCallingNumberCallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 6),
    _AccCallingNumberCallbackNumber_Type()
)
accCallingNumberCallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberCallbackNumber.setStatus("mandatory")


class _AccCallingNumberCallbackDelay_Type(Integer32):
    """Custom type accCallingNumberCallbackDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccCallingNumberCallbackDelay_Type.__name__ = "Integer32"
_AccCallingNumberCallbackDelay_Object = MibTableColumn
accCallingNumberCallbackDelay = _AccCallingNumberCallbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 7),
    _AccCallingNumberCallbackDelay_Type()
)
accCallingNumberCallbackDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberCallbackDelay.setStatus("mandatory")
_AccCallingNumberDialoutUserName_Type = DisplayString
_AccCallingNumberDialoutUserName_Object = MibTableColumn
accCallingNumberDialoutUserName = _AccCallingNumberDialoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 8),
    _AccCallingNumberDialoutUserName_Type()
)
accCallingNumberDialoutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberDialoutUserName.setStatus("mandatory")
_AccCallingNumberDialoutPassword_Type = DisplayString
_AccCallingNumberDialoutPassword_Object = MibTableColumn
accCallingNumberDialoutPassword = _AccCallingNumberDialoutPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 9),
    _AccCallingNumberDialoutPassword_Type()
)
accCallingNumberDialoutPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberDialoutPassword.setStatus("mandatory")
_AccCallingNumberDialoutAuthMode_Type = DisplayString
_AccCallingNumberDialoutAuthMode_Object = MibTableColumn
accCallingNumberDialoutAuthMode = _AccCallingNumberDialoutAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 10),
    _AccCallingNumberDialoutAuthMode_Type()
)
accCallingNumberDialoutAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberDialoutAuthMode.setStatus("mandatory")
_AccCallingNumberEgressInfc_Type = Integer32
_AccCallingNumberEgressInfc_Object = MibTableColumn
accCallingNumberEgressInfc = _AccCallingNumberEgressInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 11),
    _AccCallingNumberEgressInfc_Type()
)
accCallingNumberEgressInfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberEgressInfc.setStatus("mandatory")


class _AccCallingNumberEgressType_Type(Integer32):
    """Custom type accCallingNumberEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              16,
              24,
              31)
        )
    )
    namedValues = NamedValues(
        *(("any", 31),
          ("audio", 16),
          ("cm56", 2),
          ("cm64", 1),
          ("data", 7),
          ("modem", 24),
          ("rdi", 4),
          ("udi", 3),
          ("v-110", 5),
          ("voice", 8))
    )


_AccCallingNumberEgressType_Type.__name__ = "Integer32"
_AccCallingNumberEgressType_Object = MibTableColumn
accCallingNumberEgressType = _AccCallingNumberEgressType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 12),
    _AccCallingNumberEgressType_Type()
)
accCallingNumberEgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberEgressType.setStatus("mandatory")
_AccCallingNumberEgressNumber_Type = OctetString
_AccCallingNumberEgressNumber_Object = MibTableColumn
accCallingNumberEgressNumber = _AccCallingNumberEgressNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 1, 1, 13),
    _AccCallingNumberEgressNumber_Type()
)
accCallingNumberEgressNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberEgressNumber.setStatus("mandatory")
_AccCallingNumberScreeningTable_Object = MibTable
accCallingNumberScreeningTable = _AccCallingNumberScreeningTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2)
)
if mibBuilder.loadTexts:
    accCallingNumberScreeningTable.setStatus("mandatory")
_AccCallingNumberScreeningEntry_Object = MibTableRow
accCallingNumberScreeningEntry = _AccCallingNumberScreeningEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1)
)
accCallingNumberScreeningEntry.setIndexNames(
    (0, "ACC-CALLINGNUMBER", "accCallingNumberScreeningGroup"),
)
if mibBuilder.loadTexts:
    accCallingNumberScreeningEntry.setStatus("mandatory")


class _AccCallingNumberScreeningGroup_Type(Integer32):
    """Custom type accCallingNumberScreeningGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccCallingNumberScreeningGroup_Type.__name__ = "Integer32"
_AccCallingNumberScreeningGroup_Object = MibTableColumn
accCallingNumberScreeningGroup = _AccCallingNumberScreeningGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 1),
    _AccCallingNumberScreeningGroup_Type()
)
accCallingNumberScreeningGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningGroup.setStatus("mandatory")


class _AccCallingNumberScreeningIndex_Type(Integer32):
    """Custom type accCallingNumberScreeningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccCallingNumberScreeningIndex_Type.__name__ = "Integer32"
_AccCallingNumberScreeningIndex_Object = MibTableColumn
accCallingNumberScreeningIndex = _AccCallingNumberScreeningIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 2),
    _AccCallingNumberScreeningIndex_Type()
)
accCallingNumberScreeningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningIndex.setStatus("mandatory")


class _AccCallingNumberScreeningType_Type(Integer32):
    """Custom type accCallingNumberScreeningType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              16,
              24,
              31)
        )
    )
    namedValues = NamedValues(
        *(("any", 31),
          ("audio", 16),
          ("cm56", 1),
          ("cm64", 2),
          ("data", 7),
          ("modem", 24),
          ("rdi", 4),
          ("udi", 3),
          ("voice", 8))
    )


_AccCallingNumberScreeningType_Type.__name__ = "Integer32"
_AccCallingNumberScreeningType_Object = MibTableColumn
accCallingNumberScreeningType = _AccCallingNumberScreeningType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 3),
    _AccCallingNumberScreeningType_Type()
)
accCallingNumberScreeningType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningType.setStatus("mandatory")
_AccCallingNumberScreeningDigits_Type = DisplayString
_AccCallingNumberScreeningDigits_Object = MibTableColumn
accCallingNumberScreeningDigits = _AccCallingNumberScreeningDigits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 4),
    _AccCallingNumberScreeningDigits_Type()
)
accCallingNumberScreeningDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningDigits.setStatus("mandatory")


class _AccCallingNumberScreeningAction_Type(Integer32):
    """Custom type accCallingNumberScreeningAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccCallingNumberScreeningAction_Type.__name__ = "Integer32"
_AccCallingNumberScreeningAction_Object = MibTableColumn
accCallingNumberScreeningAction = _AccCallingNumberScreeningAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 5),
    _AccCallingNumberScreeningAction_Type()
)
accCallingNumberScreeningAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningAction.setStatus("mandatory")


class _AccCallingNumberScreeningSource_Type(Integer32):
    """Custom type accCallingNumberScreeningSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dod", 2),
          ("nvm", 1))
    )


_AccCallingNumberScreeningSource_Type.__name__ = "Integer32"
_AccCallingNumberScreeningSource_Object = MibTableColumn
accCallingNumberScreeningSource = _AccCallingNumberScreeningSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 6),
    _AccCallingNumberScreeningSource_Type()
)
accCallingNumberScreeningSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberScreeningSource.setStatus("mandatory")
_AccCallingNumberScreeningEgressInfc_Type = Integer32
_AccCallingNumberScreeningEgressInfc_Object = MibTableColumn
accCallingNumberScreeningEgressInfc = _AccCallingNumberScreeningEgressInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 7),
    _AccCallingNumberScreeningEgressInfc_Type()
)
accCallingNumberScreeningEgressInfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberScreeningEgressInfc.setStatus("mandatory")


class _AccCallingNumberScreeningEgressType_Type(Integer32):
    """Custom type accCallingNumberScreeningEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              16,
              24,
              31)
        )
    )
    namedValues = NamedValues(
        *(("any", 31),
          ("audio", 16),
          ("cm56", 2),
          ("cm64", 1),
          ("data", 7),
          ("modem", 24),
          ("rdi", 4),
          ("udi", 3),
          ("v-110", 5),
          ("voice", 8))
    )


_AccCallingNumberScreeningEgressType_Type.__name__ = "Integer32"
_AccCallingNumberScreeningEgressType_Object = MibTableColumn
accCallingNumberScreeningEgressType = _AccCallingNumberScreeningEgressType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 8),
    _AccCallingNumberScreeningEgressType_Type()
)
accCallingNumberScreeningEgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberScreeningEgressType.setStatus("mandatory")
_AccCallingNumberScreeningEgressNumber_Type = OctetString
_AccCallingNumberScreeningEgressNumber_Object = MibTableColumn
accCallingNumberScreeningEgressNumber = _AccCallingNumberScreeningEgressNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 2, 1, 9),
    _AccCallingNumberScreeningEgressNumber_Type()
)
accCallingNumberScreeningEgressNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberScreeningEgressNumber.setStatus("mandatory")
_AccCallingNumberDefaultTable_Object = MibTable
accCallingNumberDefaultTable = _AccCallingNumberDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 3)
)
if mibBuilder.loadTexts:
    accCallingNumberDefaultTable.setStatus("mandatory")
_AccCallingNumberDefaultEntry_Object = MibTableRow
accCallingNumberDefaultEntry = _AccCallingNumberDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 3, 1)
)
accCallingNumberDefaultEntry.setIndexNames(
    (0, "ACC-CALLINGNUMBER", "accCallingNumberDefaultGroup"),
)
if mibBuilder.loadTexts:
    accCallingNumberDefaultEntry.setStatus("mandatory")


class _AccCallingNumberDefaultGroup_Type(Integer32):
    """Custom type accCallingNumberDefaultGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccCallingNumberDefaultGroup_Type.__name__ = "Integer32"
_AccCallingNumberDefaultGroup_Object = MibTableColumn
accCallingNumberDefaultGroup = _AccCallingNumberDefaultGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 3, 1, 1),
    _AccCallingNumberDefaultGroup_Type()
)
accCallingNumberDefaultGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCallingNumberDefaultGroup.setStatus("mandatory")


class _AccCallingNumberDefaultAction_Type(Integer32):
    """Custom type accCallingNumberDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccCallingNumberDefaultAction_Type.__name__ = "Integer32"
_AccCallingNumberDefaultAction_Object = MibTableColumn
accCallingNumberDefaultAction = _AccCallingNumberDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 67, 3, 1, 2),
    _AccCallingNumberDefaultAction_Type()
)
accCallingNumberDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCallingNumberDefaultAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-CALLINGNUMBER",
    **{"accCallingNumber": accCallingNumber,
       "accCallingNumberTable": accCallingNumberTable,
       "accCallingNumberEntry": accCallingNumberEntry,
       "accCallingNumberGroup": accCallingNumberGroup,
       "accCallingNumberType": accCallingNumberType,
       "accCallingNumberDigits": accCallingNumberDigits,
       "accCallingNumberAction": accCallingNumberAction,
       "accCallingNumberStatus": accCallingNumberStatus,
       "accCallingNumberCallbackNumber": accCallingNumberCallbackNumber,
       "accCallingNumberCallbackDelay": accCallingNumberCallbackDelay,
       "accCallingNumberDialoutUserName": accCallingNumberDialoutUserName,
       "accCallingNumberDialoutPassword": accCallingNumberDialoutPassword,
       "accCallingNumberDialoutAuthMode": accCallingNumberDialoutAuthMode,
       "accCallingNumberEgressInfc": accCallingNumberEgressInfc,
       "accCallingNumberEgressType": accCallingNumberEgressType,
       "accCallingNumberEgressNumber": accCallingNumberEgressNumber,
       "accCallingNumberScreeningTable": accCallingNumberScreeningTable,
       "accCallingNumberScreeningEntry": accCallingNumberScreeningEntry,
       "accCallingNumberScreeningGroup": accCallingNumberScreeningGroup,
       "accCallingNumberScreeningIndex": accCallingNumberScreeningIndex,
       "accCallingNumberScreeningType": accCallingNumberScreeningType,
       "accCallingNumberScreeningDigits": accCallingNumberScreeningDigits,
       "accCallingNumberScreeningAction": accCallingNumberScreeningAction,
       "accCallingNumberScreeningSource": accCallingNumberScreeningSource,
       "accCallingNumberScreeningEgressInfc": accCallingNumberScreeningEgressInfc,
       "accCallingNumberScreeningEgressType": accCallingNumberScreeningEgressType,
       "accCallingNumberScreeningEgressNumber": accCallingNumberScreeningEgressNumber,
       "accCallingNumberDefaultTable": accCallingNumberDefaultTable,
       "accCallingNumberDefaultEntry": accCallingNumberDefaultEntry,
       "accCallingNumberDefaultGroup": accCallingNumberDefaultGroup,
       "accCallingNumberDefaultAction": accCallingNumberDefaultAction}
)
