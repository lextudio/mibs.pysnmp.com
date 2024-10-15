# SNMP MIB module (SHIVA-COMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-COMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:15 2024
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

(tCommunity,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "tCommunity")

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



class _TCommunityTrapHostType_Type(Integer32):
    """Custom type tCommunityTrapHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("unconfigured", 1))
    )


_TCommunityTrapHostType_Type.__name__ = "Integer32"
_TCommunityTrapHostType_Object = MibScalar
tCommunityTrapHostType = _TCommunityTrapHostType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 1),
    _TCommunityTrapHostType_Type()
)
tCommunityTrapHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapHostType.setStatus("mandatory")
_TCommunityTrapHostAddress_Type = OctetString
_TCommunityTrapHostAddress_Object = MibScalar
tCommunityTrapHostAddress = _TCommunityTrapHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 2),
    _TCommunityTrapHostAddress_Type()
)
tCommunityTrapHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapHostAddress.setStatus("mandatory")


class _TCommunitySetHostType_Type(Integer32):
    """Custom type tCommunitySetHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ddprange", 6),
          ("ip", 2),
          ("ipx", 3),
          ("netbios", 4),
          ("unconfigured", 1))
    )


_TCommunitySetHostType_Type.__name__ = "Integer32"
_TCommunitySetHostType_Object = MibScalar
tCommunitySetHostType = _TCommunitySetHostType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 3),
    _TCommunitySetHostType_Type()
)
tCommunitySetHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunitySetHostType.setStatus("mandatory")
_TCommunitySetHostAddress_Type = OctetString
_TCommunitySetHostAddress_Object = MibScalar
tCommunitySetHostAddress = _TCommunitySetHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 4),
    _TCommunitySetHostAddress_Type()
)
tCommunitySetHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunitySetHostAddress.setStatus("mandatory")
_TCommunityTable_Object = MibTable
tCommunityTable = _TCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5)
)
if mibBuilder.loadTexts:
    tCommunityTable.setStatus("mandatory")
_TCommunityEntry_Object = MibTableRow
tCommunityEntry = _TCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1)
)
tCommunityEntry.setIndexNames(
    (0, "SHIVA-COMM-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    tCommunityEntry.setStatus("mandatory")
_TCommunityName_Type = DisplayString
_TCommunityName_Object = MibTableColumn
tCommunityName = _TCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 1),
    _TCommunityName_Type()
)
tCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityName.setStatus("mandatory")


class _TCommunityAccess_Type(Integer32):
    """Custom type tCommunityAccess based on Integer32"""
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
        *(("clear-statistics", 3),
          ("configure", 4),
          ("no-access", 1),
          ("read-only-access", 2))
    )


_TCommunityAccess_Type.__name__ = "Integer32"
_TCommunityAccess_Object = MibTableColumn
tCommunityAccess = _TCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 2),
    _TCommunityAccess_Type()
)
tCommunityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityAccess.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 5, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_TCommunityTrapTable_Object = MibTable
tCommunityTrapTable = _TCommunityTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 6)
)
if mibBuilder.loadTexts:
    tCommunityTrapTable.setStatus("mandatory")
_TCommunityTrapEntry_Object = MibTableRow
tCommunityTrapEntry = _TCommunityTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1)
)
tCommunityTrapEntry.setIndexNames(
    (0, "SHIVA-COMM-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    tCommunityTrapEntry.setStatus("mandatory")
_TCommunityTrapEntryHostAddress_Type = OctetString
_TCommunityTrapEntryHostAddress_Object = MibTableColumn
tCommunityTrapEntryHostAddress = _TCommunityTrapEntryHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1, 1),
    _TCommunityTrapEntryHostAddress_Type()
)
tCommunityTrapEntryHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapEntryHostAddress.setStatus("mandatory")


class _TCommunityTrapEntryHostType_Type(Integer32):
    """Custom type tCommunityTrapEntryHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("unconfigured", 1))
    )


_TCommunityTrapEntryHostType_Type.__name__ = "Integer32"
_TCommunityTrapEntryHostType_Object = MibTableColumn
tCommunityTrapEntryHostType = _TCommunityTrapEntryHostType_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1, 2),
    _TCommunityTrapEntryHostType_Type()
)
tCommunityTrapEntryHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tCommunityTrapEntryHostType.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 4, 6, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-COMM-MIB",
    **{"tCommunityTrapHostType": tCommunityTrapHostType,
       "tCommunityTrapHostAddress": tCommunityTrapHostAddress,
       "tCommunitySetHostType": tCommunitySetHostType,
       "tCommunitySetHostAddress": tCommunitySetHostAddress,
       "tCommunityTable": tCommunityTable,
       "tCommunityEntry": tCommunityEntry,
       "tCommunityName": tCommunityName,
       "tCommunityAccess": tCommunityAccess,
       "pysmiFakeCol1": pysmiFakeCol1,
       "tCommunityTrapTable": tCommunityTrapTable,
       "tCommunityTrapEntry": tCommunityTrapEntry,
       "tCommunityTrapEntryHostAddress": tCommunityTrapEntryHostAddress,
       "tCommunityTrapEntryHostType": tCommunityTrapEntryHostType,
       "pysmiFakeCol2": pysmiFakeCol2}
)
