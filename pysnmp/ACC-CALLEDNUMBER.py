# SNMP MIB module (ACC-CALLEDNUMBER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-CALLEDNUMBER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:57 2024
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

_AccCalledNumber_ObjectIdentity = ObjectIdentity
accCalledNumber = _AccCalledNumber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66)
)
_AccCalledNumberTable_Object = MibTable
accCalledNumberTable = _AccCalledNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1)
)
if mibBuilder.loadTexts:
    accCalledNumberTable.setStatus("mandatory")
_AccCalledNumberEntry_Object = MibTableRow
accCalledNumberEntry = _AccCalledNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1)
)
accCalledNumberEntry.setIndexNames(
    (0, "ACC-CALLEDNUMBER", "accCalledNumberGroup"),
)
if mibBuilder.loadTexts:
    accCalledNumberEntry.setStatus("mandatory")


class _AccCalledNumberGroup_Type(Integer32):
    """Custom type accCalledNumberGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccCalledNumberGroup_Type.__name__ = "Integer32"
_AccCalledNumberGroup_Object = MibTableColumn
accCalledNumberGroup = _AccCalledNumberGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 1),
    _AccCalledNumberGroup_Type()
)
accCalledNumberGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCalledNumberGroup.setStatus("mandatory")


class _AccCalledNumberType_Type(Integer32):
    """Custom type accCalledNumberType based on Integer32"""
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


_AccCalledNumberType_Type.__name__ = "Integer32"
_AccCalledNumberType_Object = MibTableColumn
accCalledNumberType = _AccCalledNumberType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 2),
    _AccCalledNumberType_Type()
)
accCalledNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCalledNumberType.setStatus("mandatory")
_AccCalledNumberDigits_Type = DisplayString
_AccCalledNumberDigits_Object = MibTableColumn
accCalledNumberDigits = _AccCalledNumberDigits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 3),
    _AccCalledNumberDigits_Type()
)
accCalledNumberDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCalledNumberDigits.setStatus("mandatory")
_AccCalledNumberServProfile_Type = DisplayString
_AccCalledNumberServProfile_Object = MibTableColumn
accCalledNumberServProfile = _AccCalledNumberServProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 4),
    _AccCalledNumberServProfile_Type()
)
accCalledNumberServProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberServProfile.setStatus("mandatory")


class _AccCalledNumberStatus_Type(Integer32):
    """Custom type accCalledNumberStatus based on Integer32"""
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


_AccCalledNumberStatus_Type.__name__ = "Integer32"
_AccCalledNumberStatus_Object = MibTableColumn
accCalledNumberStatus = _AccCalledNumberStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 5),
    _AccCalledNumberStatus_Type()
)
accCalledNumberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberStatus.setStatus("mandatory")


class _AccCalledNumberAction_Type(Integer32):
    """Custom type accCalledNumberAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2),
          ("switch", 3))
    )


_AccCalledNumberAction_Type.__name__ = "Integer32"
_AccCalledNumberAction_Object = MibTableColumn
accCalledNumberAction = _AccCalledNumberAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 7),
    _AccCalledNumberAction_Type()
)
accCalledNumberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberAction.setStatus("mandatory")
_AccCalledNumberEgressInfc_Type = Integer32
_AccCalledNumberEgressInfc_Object = MibTableColumn
accCalledNumberEgressInfc = _AccCalledNumberEgressInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 8),
    _AccCalledNumberEgressInfc_Type()
)
accCalledNumberEgressInfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberEgressInfc.setStatus("mandatory")


class _AccCalledNumberEgressType_Type(Integer32):
    """Custom type accCalledNumberEgressType based on Integer32"""
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


_AccCalledNumberEgressType_Type.__name__ = "Integer32"
_AccCalledNumberEgressType_Object = MibTableColumn
accCalledNumberEgressType = _AccCalledNumberEgressType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 9),
    _AccCalledNumberEgressType_Type()
)
accCalledNumberEgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberEgressType.setStatus("mandatory")
_AccCalledNumberEgressNumber_Type = OctetString
_AccCalledNumberEgressNumber_Object = MibTableColumn
accCalledNumberEgressNumber = _AccCalledNumberEgressNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 66, 1, 1, 10),
    _AccCalledNumberEgressNumber_Type()
)
accCalledNumberEgressNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCalledNumberEgressNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-CALLEDNUMBER",
    **{"accCalledNumber": accCalledNumber,
       "accCalledNumberTable": accCalledNumberTable,
       "accCalledNumberEntry": accCalledNumberEntry,
       "accCalledNumberGroup": accCalledNumberGroup,
       "accCalledNumberType": accCalledNumberType,
       "accCalledNumberDigits": accCalledNumberDigits,
       "accCalledNumberServProfile": accCalledNumberServProfile,
       "accCalledNumberStatus": accCalledNumberStatus,
       "accCalledNumberAction": accCalledNumberAction,
       "accCalledNumberEgressInfc": accCalledNumberEgressInfc,
       "accCalledNumberEgressType": accCalledNumberEgressType,
       "accCalledNumberEgressNumber": accCalledNumberEgressNumber}
)
