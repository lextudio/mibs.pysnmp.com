# SNMP MIB module (BIANCA-BRICK-BINARY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-BINARY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:21 2024
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
 enterprises,
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
    "enterprises",
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26)
)
_BinTable_Object = MibTable
binTable = _BinTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65)
)
if mibBuilder.loadTexts:
    binTable.setStatus("mandatory")
_BinEntry_Object = MibTableRow
binEntry = _BinEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65, 1)
)
binEntry.setIndexNames(
    (0, "BIANCA-BRICK-BINARY-MIB", "binEntIndex"),
)
if mibBuilder.loadTexts:
    binEntry.setStatus("mandatory")
_BinEntIndex_Type = Integer32
_BinEntIndex_Object = MibTableColumn
binEntIndex = _BinEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65, 1, 1),
    _BinEntIndex_Type()
)
binEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    binEntIndex.setStatus("mandatory")
_BinEntNextIndex_Type = Integer32
_BinEntNextIndex_Object = MibTableColumn
binEntNextIndex = _BinEntNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65, 1, 2),
    _BinEntNextIndex_Type()
)
binEntNextIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    binEntNextIndex.setStatus("mandatory")
_BinEntSetId_Type = Integer32
_BinEntSetId_Object = MibTableColumn
binEntSetId = _BinEntSetId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65, 1, 3),
    _BinEntSetId_Type()
)
binEntSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    binEntSetId.setStatus("mandatory")


class _BinEntData_Type(OctetString):
    """Custom type binEntData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BinEntData_Type.__name__ = "OctetString"
_BinEntData_Object = MibTableColumn
binEntData = _BinEntData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 65, 1, 4),
    _BinEntData_Type()
)
binEntData.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    binEntData.setStatus("mandatory")
_BinFileTable_Object = MibTable
binFileTable = _BinFileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66)
)
if mibBuilder.loadTexts:
    binFileTable.setStatus("mandatory")
_BinFileEntry_Object = MibTableRow
binFileEntry = _BinFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66, 1)
)
binFileEntry.setIndexNames(
    (0, "BIANCA-BRICK-BINARY-MIB", "binFileEntSetId"),
)
if mibBuilder.loadTexts:
    binFileEntry.setStatus("mandatory")
_BinFileEntName_Type = DisplayString
_BinFileEntName_Object = MibTableColumn
binFileEntName = _BinFileEntName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66, 1, 1),
    _BinFileEntName_Type()
)
binFileEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binFileEntName.setStatus("mandatory")
_BinFileEntSize_Type = Integer32
_BinFileEntSize_Object = MibTableColumn
binFileEntSize = _BinFileEntSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66, 1, 2),
    _BinFileEntSize_Type()
)
binFileEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binFileEntSize.setStatus("mandatory")


class _BinFileEntPublic_Type(Integer32):
    """Custom type binFileEntPublic based on Integer32"""
    defaultValue = 1

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


_BinFileEntPublic_Type.__name__ = "Integer32"
_BinFileEntPublic_Object = MibTableColumn
binFileEntPublic = _BinFileEntPublic_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66, 1, 3),
    _BinFileEntPublic_Type()
)
binFileEntPublic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binFileEntPublic.setStatus("mandatory")
_BinFileEntSetId_Type = Integer32
_BinFileEntSetId_Object = MibTableColumn
binFileEntSetId = _BinFileEntSetId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 66, 1, 17),
    _BinFileEntSetId_Type()
)
binFileEntSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binFileEntSetId.setStatus("mandatory")
_BinPublicTable_Object = MibTable
binPublicTable = _BinPublicTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67)
)
if mibBuilder.loadTexts:
    binPublicTable.setStatus("mandatory")
_BinPublicEntry_Object = MibTableRow
binPublicEntry = _BinPublicEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67, 1)
)
binPublicEntry.setIndexNames(
    (0, "BIANCA-BRICK-BINARY-MIB", "binPublicEntIndex"),
)
if mibBuilder.loadTexts:
    binPublicEntry.setStatus("mandatory")
_BinPublicEntIndex_Type = Integer32
_BinPublicEntIndex_Object = MibTableColumn
binPublicEntIndex = _BinPublicEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67, 1, 1),
    _BinPublicEntIndex_Type()
)
binPublicEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binPublicEntIndex.setStatus("mandatory")
_BinPublicEntNextIndex_Type = Integer32
_BinPublicEntNextIndex_Object = MibTableColumn
binPublicEntNextIndex = _BinPublicEntNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67, 1, 2),
    _BinPublicEntNextIndex_Type()
)
binPublicEntNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binPublicEntNextIndex.setStatus("mandatory")
_BinPublicEntSetId_Type = Integer32
_BinPublicEntSetId_Object = MibTableColumn
binPublicEntSetId = _BinPublicEntSetId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67, 1, 3),
    _BinPublicEntSetId_Type()
)
binPublicEntSetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binPublicEntSetId.setStatus("mandatory")


class _BinPublicEntData_Type(OctetString):
    """Custom type binPublicEntData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BinPublicEntData_Type.__name__ = "OctetString"
_BinPublicEntData_Object = MibTableColumn
binPublicEntData = _BinPublicEntData_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 67, 1, 4),
    _BinPublicEntData_Type()
)
binPublicEntData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    binPublicEntData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-BINARY-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "ipsec": ipsec,
       "binTable": binTable,
       "binEntry": binEntry,
       "binEntIndex": binEntIndex,
       "binEntNextIndex": binEntNextIndex,
       "binEntSetId": binEntSetId,
       "binEntData": binEntData,
       "binFileTable": binFileTable,
       "binFileEntry": binFileEntry,
       "binFileEntName": binFileEntName,
       "binFileEntSize": binFileEntSize,
       "binFileEntPublic": binFileEntPublic,
       "binFileEntSetId": binFileEntSetId,
       "binPublicTable": binPublicTable,
       "binPublicEntry": binPublicEntry,
       "binPublicEntIndex": binPublicEntIndex,
       "binPublicEntNextIndex": binPublicEntNextIndex,
       "binPublicEntSetId": binPublicEntSetId,
       "binPublicEntData": binPublicEntData}
)
