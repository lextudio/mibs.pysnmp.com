# SNMP MIB module (DMTF-DMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMTF-DMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:38 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

dmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1)
)
dmiMIB.setRevisions(
        ("1995-07-13 20:00",
         "1997-10-22 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DmiAccess(Integer32, TextualConvention):
    status = "current"
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
        *(("readOnly", 2),
          ("readWrite", 3),
          ("unknown", 1),
          ("unsupported", 5),
          ("writeOnly", 4))
    )



class DmiDate(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )



class DmiInteger64(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class DmiString(OctetString, TextualConvention):
    status = "current"


class DmiType(Integer32, TextualConvention):
    status = "current"
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
        *(("counter32", 2),
          ("counter64", 3),
          ("date", 9),
          ("displayString", 8),
          ("gauge32", 4),
          ("integer32", 5),
          ("integer64", 6),
          ("octetString", 7),
          ("unknown", 1))
    )



class DmiTDAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmiMIBObjects_ObjectIdentity = ObjectIdentity
dmiMIBObjects = _DmiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 1)
)
_DmiClasses_ObjectIdentity = ObjectIdentity
dmiClasses = _DmiClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1)
)
_DmiClassTable_Object = MibTable
dmiClassTable = _DmiClassTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dmiClassTable.setStatus("current")
_DmiClassEntry_Object = MibTableRow
dmiClassEntry = _DmiClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1)
)
dmiClassEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiClassIndex"),
)
if mibBuilder.loadTexts:
    dmiClassEntry.setStatus("current")
_DmiClassIndex_Type = Unsigned32
_DmiClassIndex_Object = MibTableColumn
dmiClassIndex = _DmiClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 1),
    _DmiClassIndex_Type()
)
dmiClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassIndex.setStatus("current")


class _DmiClassString_Type(DmiString):
    """Custom type dmiClassString based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiClassString_Type.__name__ = "DmiString"
_DmiClassString_Object = MibTableColumn
dmiClassString = _DmiClassString_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 2),
    _DmiClassString_Type()
)
dmiClassString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassString.setStatus("current")


class _DmiClassVersion_Type(Integer32):
    """Custom type dmiClassVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_DmiClassVersion_Type.__name__ = "Integer32"
_DmiClassVersion_Object = MibTableColumn
dmiClassVersion = _DmiClassVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 3),
    _DmiClassVersion_Type()
)
dmiClassVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassVersion.setStatus("current")


class _DmiClassName_Type(DmiString):
    """Custom type dmiClassName based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiClassName_Type.__name__ = "DmiString"
_DmiClassName_Object = MibTableColumn
dmiClassName = _DmiClassName_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 4),
    _DmiClassName_Type()
)
dmiClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassName.setStatus("current")
_DmiClassOID_Type = ObjectIdentifier
_DmiClassOID_Object = MibTableColumn
dmiClassOID = _DmiClassOID_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 5),
    _DmiClassOID_Type()
)
dmiClassOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassOID.setStatus("current")


class _DmiClassKeyCount_Type(Integer32):
    """Custom type dmiClassKeyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DmiClassKeyCount_Type.__name__ = "Integer32"
_DmiClassKeyCount_Object = MibTableColumn
dmiClassKeyCount = _DmiClassKeyCount_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 6),
    _DmiClassKeyCount_Type()
)
dmiClassKeyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassKeyCount.setStatus("current")


class _DmiClassDescrLength_Type(Integer32):
    """Custom type dmiClassDescrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmiClassDescrLength_Type.__name__ = "Integer32"
_DmiClassDescrLength_Object = MibTableColumn
dmiClassDescrLength = _DmiClassDescrLength_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 7),
    _DmiClassDescrLength_Type()
)
dmiClassDescrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassDescrLength.setStatus("current")
_DmiClassPragma_Type = DmiString
_DmiClassPragma_Object = MibTableColumn
dmiClassPragma = _DmiClassPragma_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 1, 1, 8),
    _DmiClassPragma_Type()
)
dmiClassPragma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiClassPragma.setStatus("current")
_DmiAttributeTable_Object = MibTable
dmiAttributeTable = _DmiAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dmiAttributeTable.setStatus("current")
_DmiAttributeEntry_Object = MibTableRow
dmiAttributeEntry = _DmiAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1)
)
dmiAttributeEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiClassIndex"),
    (0, "DMTF-DMI-MIB", "dmiAttrId"),
)
if mibBuilder.loadTexts:
    dmiAttributeEntry.setStatus("current")
_DmiAttrId_Type = Unsigned32
_DmiAttrId_Object = MibTableColumn
dmiAttrId = _DmiAttrId_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 1),
    _DmiAttrId_Type()
)
dmiAttrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrId.setStatus("current")


class _DmiAttrName_Type(DmiString):
    """Custom type dmiAttrName based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiAttrName_Type.__name__ = "DmiString"
_DmiAttrName_Object = MibTableColumn
dmiAttrName = _DmiAttrName_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 2),
    _DmiAttrName_Type()
)
dmiAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrName.setStatus("current")
_DmiAttrAccess_Type = DmiAccess
_DmiAttrAccess_Object = MibTableColumn
dmiAttrAccess = _DmiAttrAccess_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 3),
    _DmiAttrAccess_Type()
)
dmiAttrAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrAccess.setStatus("current")
_DmiAttrType_Type = DmiType
_DmiAttrType_Object = MibTableColumn
dmiAttrType = _DmiAttrType_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 4),
    _DmiAttrType_Type()
)
dmiAttrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrType.setStatus("current")


class _DmiAttrMaxSize_Type(Integer32):
    """Custom type dmiAttrMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DmiAttrMaxSize_Type.__name__ = "Integer32"
_DmiAttrMaxSize_Object = MibTableColumn
dmiAttrMaxSize = _DmiAttrMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 5),
    _DmiAttrMaxSize_Type()
)
dmiAttrMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrMaxSize.setStatus("current")


class _DmiAttrEnumListCount_Type(Integer32):
    """Custom type dmiAttrEnumListCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DmiAttrEnumListCount_Type.__name__ = "Integer32"
_DmiAttrEnumListCount_Object = MibTableColumn
dmiAttrEnumListCount = _DmiAttrEnumListCount_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 6),
    _DmiAttrEnumListCount_Type()
)
dmiAttrEnumListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrEnumListCount.setStatus("current")


class _DmiAttrDescrLength_Type(Integer32):
    """Custom type dmiAttrDescrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmiAttrDescrLength_Type.__name__ = "Integer32"
_DmiAttrDescrLength_Object = MibTableColumn
dmiAttrDescrLength = _DmiAttrDescrLength_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 2, 1, 7),
    _DmiAttrDescrLength_Type()
)
dmiAttrDescrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiAttrDescrLength.setStatus("current")
_DmiKeyTable_Object = MibTable
dmiKeyTable = _DmiKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dmiKeyTable.setStatus("current")
_DmiKeyEntry_Object = MibTableRow
dmiKeyEntry = _DmiKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 3, 1)
)
dmiKeyEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiClassIndex"),
    (0, "DMTF-DMI-MIB", "dmiKeyIndex"),
)
if mibBuilder.loadTexts:
    dmiKeyEntry.setStatus("current")


class _DmiKeyIndex_Type(Integer32):
    """Custom type dmiKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DmiKeyIndex_Type.__name__ = "Integer32"
_DmiKeyIndex_Object = MibTableColumn
dmiKeyIndex = _DmiKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 3, 1, 1),
    _DmiKeyIndex_Type()
)
dmiKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiKeyIndex.setStatus("current")
_DmiKeyType_Type = DmiType
_DmiKeyType_Object = MibTableColumn
dmiKeyType = _DmiKeyType_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 3, 1, 2),
    _DmiKeyType_Type()
)
dmiKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiKeyType.setStatus("current")
_DmiKeyAttrId_Type = Unsigned32
_DmiKeyAttrId_Object = MibTableColumn
dmiKeyAttrId = _DmiKeyAttrId_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 3, 1, 3),
    _DmiKeyAttrId_Type()
)
dmiKeyAttrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiKeyAttrId.setStatus("current")
_DmiDescrTable_Object = MibTable
dmiDescrTable = _DmiDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dmiDescrTable.setStatus("current")
_DmiDescrEntry_Object = MibTableRow
dmiDescrEntry = _DmiDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 4, 1)
)
dmiDescrEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiClassIndex"),
    (0, "DMTF-DMI-MIB", "dmiAttrId"),
    (0, "DMTF-DMI-MIB", "dmiDescrIndex"),
)
if mibBuilder.loadTexts:
    dmiDescrEntry.setStatus("current")


class _DmiDescrIndex_Type(Integer32):
    """Custom type dmiDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DmiDescrIndex_Type.__name__ = "Integer32"
_DmiDescrIndex_Object = MibTableColumn
dmiDescrIndex = _DmiDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 4, 1, 1),
    _DmiDescrIndex_Type()
)
dmiDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiDescrIndex.setStatus("current")
_DmiDescrText_Type = DmiString
_DmiDescrText_Object = MibTableColumn
dmiDescrText = _DmiDescrText_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 4, 1, 2),
    _DmiDescrText_Type()
)
dmiDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiDescrText.setStatus("current")
_DmiEnumTable_Object = MibTable
dmiEnumTable = _DmiEnumTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dmiEnumTable.setStatus("current")
_DmiEnumEntry_Object = MibTableRow
dmiEnumEntry = _DmiEnumEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 5, 1)
)
dmiEnumEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiClassIndex"),
    (0, "DMTF-DMI-MIB", "dmiAttrId"),
    (0, "DMTF-DMI-MIB", "dmiEnumId"),
)
if mibBuilder.loadTexts:
    dmiEnumEntry.setStatus("current")
_DmiEnumId_Type = Unsigned32
_DmiEnumId_Object = MibTableColumn
dmiEnumId = _DmiEnumId_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 5, 1, 1),
    _DmiEnumId_Type()
)
dmiEnumId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiEnumId.setStatus("current")
_DmiEnumValue_Type = Integer32
_DmiEnumValue_Object = MibTableColumn
dmiEnumValue = _DmiEnumValue_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 5, 1, 2),
    _DmiEnumValue_Type()
)
dmiEnumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiEnumValue.setStatus("current")


class _DmiEnumString_Type(DmiString):
    """Custom type dmiEnumString based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiEnumString_Type.__name__ = "DmiString"
_DmiEnumString_Object = MibTableColumn
dmiEnumString = _DmiEnumString_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 1, 5, 1, 3),
    _DmiEnumString_Type()
)
dmiEnumString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiEnumString.setStatus("current")
_DmiComponents_ObjectIdentity = ObjectIdentity
dmiComponents = _DmiComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2)
)
_DmiComponentTable_Object = MibTable
dmiComponentTable = _DmiComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dmiComponentTable.setStatus("current")
_DmiComponentEntry_Object = MibTableRow
dmiComponentEntry = _DmiComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1)
)
dmiComponentEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiCompId"),
)
if mibBuilder.loadTexts:
    dmiComponentEntry.setStatus("current")
_DmiCompId_Type = Unsigned32
_DmiCompId_Object = MibTableColumn
dmiCompId = _DmiCompId_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1, 1),
    _DmiCompId_Type()
)
dmiCompId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompId.setStatus("current")


class _DmiCompName_Type(DmiString):
    """Custom type dmiCompName based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiCompName_Type.__name__ = "DmiString"
_DmiCompName_Object = MibTableColumn
dmiCompName = _DmiCompName_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1, 2),
    _DmiCompName_Type()
)
dmiCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompName.setStatus("current")


class _DmiCompDescrLength_Type(Integer32):
    """Custom type dmiCompDescrLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DmiCompDescrLength_Type.__name__ = "Integer32"
_DmiCompDescrLength_Object = MibTableColumn
dmiCompDescrLength = _DmiCompDescrLength_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1, 3),
    _DmiCompDescrLength_Type()
)
dmiCompDescrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompDescrLength.setStatus("current")


class _DmiCompGroupCount_Type(Integer32):
    """Custom type dmiCompGroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DmiCompGroupCount_Type.__name__ = "Integer32"
_DmiCompGroupCount_Object = MibTableColumn
dmiCompGroupCount = _DmiCompGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1, 4),
    _DmiCompGroupCount_Type()
)
dmiCompGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompGroupCount.setStatus("current")


class _DmiCompPragma_Type(DmiString):
    """Custom type dmiCompPragma based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiCompPragma_Type.__name__ = "DmiString"
_DmiCompPragma_Object = MibTableColumn
dmiCompPragma = _DmiCompPragma_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 1, 1, 5),
    _DmiCompPragma_Type()
)
dmiCompPragma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompPragma.setStatus("current")
_DmiCompDescrTable_Object = MibTable
dmiCompDescrTable = _DmiCompDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dmiCompDescrTable.setStatus("current")
_DmiCompDescrEntry_Object = MibTableRow
dmiCompDescrEntry = _DmiCompDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 2, 1)
)
dmiCompDescrEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiCompId"),
    (0, "DMTF-DMI-MIB", "dmiCompDescrIndex"),
)
if mibBuilder.loadTexts:
    dmiCompDescrEntry.setStatus("current")


class _DmiCompDescrIndex_Type(Integer32):
    """Custom type dmiCompDescrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DmiCompDescrIndex_Type.__name__ = "Integer32"
_DmiCompDescrIndex_Object = MibTableColumn
dmiCompDescrIndex = _DmiCompDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 2, 1, 1),
    _DmiCompDescrIndex_Type()
)
dmiCompDescrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompDescrIndex.setStatus("current")
_DmiCompDescrText_Type = DmiString
_DmiCompDescrText_Object = MibTableColumn
dmiCompDescrText = _DmiCompDescrText_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 2, 1, 2),
    _DmiCompDescrText_Type()
)
dmiCompDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiCompDescrText.setStatus("current")
_DmiGroupTable_Object = MibTable
dmiGroupTable = _DmiGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dmiGroupTable.setStatus("current")
_DmiGroupEntry_Object = MibTableRow
dmiGroupEntry = _DmiGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3, 1)
)
dmiGroupEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiCompId"),
    (0, "DMTF-DMI-MIB", "dmiGroupId"),
)
if mibBuilder.loadTexts:
    dmiGroupEntry.setStatus("current")
_DmiGroupId_Type = Unsigned32
_DmiGroupId_Object = MibTableColumn
dmiGroupId = _DmiGroupId_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3, 1, 1),
    _DmiGroupId_Type()
)
dmiGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiGroupId.setStatus("current")


class _DmiGroupClassString_Type(DmiString):
    """Custom type dmiGroupClassString based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DmiGroupClassString_Type.__name__ = "DmiString"
_DmiGroupClassString_Object = MibTableColumn
dmiGroupClassString = _DmiGroupClassString_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3, 1, 2),
    _DmiGroupClassString_Type()
)
dmiGroupClassString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiGroupClassString.setStatus("current")


class _DmiGroupVersion_Type(Integer32):
    """Custom type dmiGroupVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_DmiGroupVersion_Type.__name__ = "Integer32"
_DmiGroupVersion_Object = MibTableColumn
dmiGroupVersion = _DmiGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3, 1, 3),
    _DmiGroupVersion_Type()
)
dmiGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiGroupVersion.setStatus("current")
_DmiGroupClassIndex_Type = Unsigned32
_DmiGroupClassIndex_Object = MibTableColumn
dmiGroupClassIndex = _DmiGroupClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 3, 1, 4),
    _DmiGroupClassIndex_Type()
)
dmiGroupClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiGroupClassIndex.setStatus("current")
_DmiLanguageTable_Object = MibTable
dmiLanguageTable = _DmiLanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dmiLanguageTable.setStatus("current")
_DmiLanguageEntry_Object = MibTableRow
dmiLanguageEntry = _DmiLanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 4, 1)
)
dmiLanguageEntry.setIndexNames(
    (0, "DMTF-DMI-MIB", "dmiCompId"),
    (1, "DMTF-DMI-MIB", "dmiLanguage"),
)
if mibBuilder.loadTexts:
    dmiLanguageEntry.setStatus("current")


class _DmiLanguage_Type(DmiString):
    """Custom type dmiLanguage based on DmiString"""
    subtypeSpec = DmiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(14, 14),
    )


_DmiLanguage_Type.__name__ = "DmiString"
_DmiLanguage_Object = MibTableColumn
dmiLanguage = _DmiLanguage_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 2, 4, 1, 1),
    _DmiLanguage_Type()
)
dmiLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiLanguage.setStatus("current")
_DmiMappingAgent_ObjectIdentity = ObjectIdentity
dmiMappingAgent = _DmiMappingAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 3)
)


class _DmiMappingLevel_Type(Integer32):
    """Custom type dmiMappingLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DmiMappingLevel_Type.__name__ = "Integer32"
_DmiMappingLevel_Object = MibScalar
dmiMappingLevel = _DmiMappingLevel_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 1, 3, 1),
    _DmiMappingLevel_Type()
)
dmiMappingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dmiMappingLevel.setStatus("current")
_DmiNotifications_ObjectIdentity = ObjectIdentity
dmiNotifications = _DmiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 2)
)
_DmiIndications_ObjectIdentity = ObjectIdentity
dmiIndications = _DmiIndications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0)
)
_DmiEventVars_ObjectIdentity = ObjectIdentity
dmiEventVars = _DmiEventVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1)
)
_DmiEventType_Type = Integer32
_DmiEventType_Object = MibScalar
dmiEventType = _DmiEventType_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 1),
    _DmiEventType_Type()
)
dmiEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventType.setStatus("current")


class _DmiEventSeverity_Type(Integer32):
    """Custom type dmiEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("critical", 16),
          ("information", 2),
          ("monitor", 1),
          ("nonCritical", 8),
          ("nonRecoverable", 32),
          ("ok", 4))
    )


_DmiEventSeverity_Type.__name__ = "Integer32"
_DmiEventSeverity_Object = MibScalar
dmiEventSeverity = _DmiEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 2),
    _DmiEventSeverity_Type()
)
dmiEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventSeverity.setStatus("current")
_DmiEventStateKey_Type = Integer32
_DmiEventStateKey_Object = MibScalar
dmiEventStateKey = _DmiEventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 4),
    _DmiEventStateKey_Type()
)
dmiEventStateKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventStateKey.setStatus("current")
_DmiEventAssociatedGroup_Type = DmiString
_DmiEventAssociatedGroup_Object = MibScalar
dmiEventAssociatedGroup = _DmiEventAssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 5),
    _DmiEventAssociatedGroup_Type()
)
dmiEventAssociatedGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventAssociatedGroup.setStatus("current")
_DmiEventSystem_Type = Integer32
_DmiEventSystem_Object = MibScalar
dmiEventSystem = _DmiEventSystem_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 6),
    _DmiEventSystem_Type()
)
dmiEventSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventSystem.setStatus("current")
_DmiEventSubSystem_Type = Integer32
_DmiEventSubSystem_Object = MibScalar
dmiEventSubSystem = _DmiEventSubSystem_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 7),
    _DmiEventSubSystem_Type()
)
dmiEventSubSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventSubSystem.setStatus("current")
_DmiEventSolution_Type = Integer32
_DmiEventSolution_Object = MibScalar
dmiEventSolution = _DmiEventSolution_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 8),
    _DmiEventSolution_Type()
)
dmiEventSolution.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventSolution.setStatus("current")
_DmiEventVendorMsg_Type = DmiString
_DmiEventVendorMsg_Object = MibScalar
dmiEventVendorMsg = _DmiEventVendorMsg_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 10),
    _DmiEventVendorMsg_Type()
)
dmiEventVendorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventVendorMsg.setStatus("current")
_DmiEventVendorData_Type = OctetString
_DmiEventVendorData_Object = MibScalar
dmiEventVendorData = _DmiEventVendorData_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 11),
    _DmiEventVendorData_Type()
)
dmiEventVendorData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventVendorData.setStatus("current")
_DmiEventDateTime_Type = DmiDate
_DmiEventDateTime_Object = MibScalar
dmiEventDateTime = _DmiEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 12),
    _DmiEventDateTime_Type()
)
dmiEventDateTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventDateTime.setStatus("current")
_DmiEventClassString_Type = DmiString
_DmiEventClassString_Object = MibScalar
dmiEventClassString = _DmiEventClassString_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 13),
    _DmiEventClassString_Type()
)
dmiEventClassString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventClassString.setStatus("current")
_DmiEventSource_Type = DmiTDAddress
_DmiEventSource_Object = MibScalar
dmiEventSource = _DmiEventSource_Object(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 1, 14),
    _DmiEventSource_Type()
)
dmiEventSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dmiEventSource.setStatus("current")
_DmiMIBConformance_ObjectIdentity = ObjectIdentity
dmiMIBConformance = _DmiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 3)
)
_DmiMIBCompliances_ObjectIdentity = ObjectIdentity
dmiMIBCompliances = _DmiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 1)
)
_DmiMIBGroups_ObjectIdentity = ObjectIdentity
dmiMIBGroups = _DmiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 2)
)
_DmiNotificationGroups_ObjectIdentity = ObjectIdentity
dmiNotificationGroups = _DmiNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 3)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)

# Managed Objects groups

dmiClassesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 2, 1)
)
dmiClassesGroup.setObjects(
      *(("DMTF-DMI-MIB", "dmiClassIndex"),
        ("DMTF-DMI-MIB", "dmiClassString"),
        ("DMTF-DMI-MIB", "dmiClassVersion"),
        ("DMTF-DMI-MIB", "dmiClassName"),
        ("DMTF-DMI-MIB", "dmiClassOID"),
        ("DMTF-DMI-MIB", "dmiClassKeyCount"),
        ("DMTF-DMI-MIB", "dmiClassDescrLength"),
        ("DMTF-DMI-MIB", "dmiClassPragma"),
        ("DMTF-DMI-MIB", "dmiAttrId"),
        ("DMTF-DMI-MIB", "dmiAttrName"),
        ("DMTF-DMI-MIB", "dmiAttrAccess"),
        ("DMTF-DMI-MIB", "dmiAttrType"),
        ("DMTF-DMI-MIB", "dmiAttrMaxSize"),
        ("DMTF-DMI-MIB", "dmiAttrEnumListCount"),
        ("DMTF-DMI-MIB", "dmiAttrDescrLength"),
        ("DMTF-DMI-MIB", "dmiKeyIndex"),
        ("DMTF-DMI-MIB", "dmiKeyType"),
        ("DMTF-DMI-MIB", "dmiKeyAttrId"),
        ("DMTF-DMI-MIB", "dmiDescrIndex"),
        ("DMTF-DMI-MIB", "dmiDescrText"),
        ("DMTF-DMI-MIB", "dmiEnumId"),
        ("DMTF-DMI-MIB", "dmiEnumValue"),
        ("DMTF-DMI-MIB", "dmiEnumString"))
)
if mibBuilder.loadTexts:
    dmiClassesGroup.setStatus("current")

dmiComponentsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 2, 2)
)
dmiComponentsGroup.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiCompName"),
        ("DMTF-DMI-MIB", "dmiCompDescrLength"),
        ("DMTF-DMI-MIB", "dmiCompGroupCount"),
        ("DMTF-DMI-MIB", "dmiCompPragma"),
        ("DMTF-DMI-MIB", "dmiCompDescrIndex"),
        ("DMTF-DMI-MIB", "dmiCompDescrText"),
        ("DMTF-DMI-MIB", "dmiGroupId"),
        ("DMTF-DMI-MIB", "dmiGroupClassString"),
        ("DMTF-DMI-MIB", "dmiGroupVersion"),
        ("DMTF-DMI-MIB", "dmiGroupClassId"),
        ("DMTF-DMI-MIB", "dmiLanguage"))
)
if mibBuilder.loadTexts:
    dmiComponentsGroup.setStatus("current")

dmiNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 2, 3)
)
dmiNotificationObjectGroup.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiCompName"),
        ("DMTF-DMI-MIB", "dmiGroupId"),
        ("DMTF-DMI-MIB", "dmiGroupClassString"),
        ("DMTF-DMI-MIB", "dmiLanguage"))
)
if mibBuilder.loadTexts:
    dmiNotificationObjectGroup.setStatus("current")

dmiMappingAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 2, 4)
)
dmiMappingAgentGroup.setObjects(
    ("DMTF-DMI-MIB", "dmiMappingLevel")
)
if mibBuilder.loadTexts:
    dmiMappingAgentGroup.setStatus("current")


# Notification objects

dmiEventIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 1)
)
dmiEventIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventClassString"),
        ("DMTF-DMI-MIB", "dmiEventType"),
        ("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("DMTF-DMI-MIB", "dmiEventSystem"),
        ("DMTF-DMI-MIB", "dmiEventSubSystem"))
)
if mibBuilder.loadTexts:
    dmiEventIndication.setStatus(
        "current"
    )

dmiComponentAddedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 2)
)
dmiComponentAddedIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiCompName"))
)
if mibBuilder.loadTexts:
    dmiComponentAddedIndication.setStatus(
        "current"
    )

dmiComponentDeletedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 3)
)
dmiComponentDeletedIndication.setObjects(
    ("DMTF-DMI-MIB", "dmiCompId")
)
if mibBuilder.loadTexts:
    dmiComponentDeletedIndication.setStatus(
        "current"
    )

dmiLanguageAddedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 4)
)
dmiLanguageAddedIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiLanguage"))
)
if mibBuilder.loadTexts:
    dmiLanguageAddedIndication.setStatus(
        "current"
    )

dmiLanguageDeletedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 5)
)
dmiLanguageDeletedIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiLanguage"))
)
if mibBuilder.loadTexts:
    dmiLanguageDeletedIndication.setStatus(
        "current"
    )

dmiGroupAddedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 6)
)
dmiGroupAddedIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiGroupId"),
        ("DMTF-DMI-MIB", "dmiGroupClassString"))
)
if mibBuilder.loadTexts:
    dmiGroupAddedIndication.setStatus(
        "current"
    )

dmiGroupDeletedIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 1, 2, 0, 7)
)
dmiGroupDeletedIndication.setObjects(
      *(("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiGroupId"))
)
if mibBuilder.loadTexts:
    dmiGroupDeletedIndication.setStatus(
        "current"
    )


# Notifications groups

dmiNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 3, 1)
)
dmiNotificationsGroup.setObjects(
      *(("DMTF-DMI-MIB", "dmiComponentAddedIndication"),
        ("DMTF-DMI-MIB", "dmiComponentDeletedIndication"),
        ("DMTF-DMI-MIB", "dmiLanguageAddedIndication"),
        ("DMTF-DMI-MIB", "dmiLanguageDeletedIndication"),
        ("DMTF-DMI-MIB", "dmiGroupAddedIndication"),
        ("DMTF-DMI-MIB", "dmiGroupDeletedIndication"))
)
if mibBuilder.loadTexts:
    dmiNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dmiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dmiMIBCompliance.setStatus(
        "current"
    )

dmiNotificationsOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 412, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    dmiNotificationsOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMTF-DMI-MIB",
    **{"DmiAccess": DmiAccess,
       "DmiDate": DmiDate,
       "DmiInteger64": DmiInteger64,
       "DmiString": DmiString,
       "DmiType": DmiType,
       "DmiTDAddress": DmiTDAddress,
       "dmtf": dmtf,
       "dmiMIB": dmiMIB,
       "dmiMIBObjects": dmiMIBObjects,
       "dmiClasses": dmiClasses,
       "dmiClassTable": dmiClassTable,
       "dmiClassEntry": dmiClassEntry,
       "dmiClassIndex": dmiClassIndex,
       "dmiClassString": dmiClassString,
       "dmiClassVersion": dmiClassVersion,
       "dmiClassName": dmiClassName,
       "dmiClassOID": dmiClassOID,
       "dmiClassKeyCount": dmiClassKeyCount,
       "dmiClassDescrLength": dmiClassDescrLength,
       "dmiClassPragma": dmiClassPragma,
       "dmiAttributeTable": dmiAttributeTable,
       "dmiAttributeEntry": dmiAttributeEntry,
       "dmiAttrId": dmiAttrId,
       "dmiAttrName": dmiAttrName,
       "dmiAttrAccess": dmiAttrAccess,
       "dmiAttrType": dmiAttrType,
       "dmiAttrMaxSize": dmiAttrMaxSize,
       "dmiAttrEnumListCount": dmiAttrEnumListCount,
       "dmiAttrDescrLength": dmiAttrDescrLength,
       "dmiKeyTable": dmiKeyTable,
       "dmiKeyEntry": dmiKeyEntry,
       "dmiKeyIndex": dmiKeyIndex,
       "dmiKeyType": dmiKeyType,
       "dmiKeyAttrId": dmiKeyAttrId,
       "dmiDescrTable": dmiDescrTable,
       "dmiDescrEntry": dmiDescrEntry,
       "dmiDescrIndex": dmiDescrIndex,
       "dmiDescrText": dmiDescrText,
       "dmiEnumTable": dmiEnumTable,
       "dmiEnumEntry": dmiEnumEntry,
       "dmiEnumId": dmiEnumId,
       "dmiEnumValue": dmiEnumValue,
       "dmiEnumString": dmiEnumString,
       "dmiComponents": dmiComponents,
       "dmiComponentTable": dmiComponentTable,
       "dmiComponentEntry": dmiComponentEntry,
       "dmiCompId": dmiCompId,
       "dmiCompName": dmiCompName,
       "dmiCompDescrLength": dmiCompDescrLength,
       "dmiCompGroupCount": dmiCompGroupCount,
       "dmiCompPragma": dmiCompPragma,
       "dmiCompDescrTable": dmiCompDescrTable,
       "dmiCompDescrEntry": dmiCompDescrEntry,
       "dmiCompDescrIndex": dmiCompDescrIndex,
       "dmiCompDescrText": dmiCompDescrText,
       "dmiGroupTable": dmiGroupTable,
       "dmiGroupEntry": dmiGroupEntry,
       "dmiGroupId": dmiGroupId,
       "dmiGroupClassString": dmiGroupClassString,
       "dmiGroupVersion": dmiGroupVersion,
       "dmiGroupClassIndex": dmiGroupClassIndex,
       "dmiLanguageTable": dmiLanguageTable,
       "dmiLanguageEntry": dmiLanguageEntry,
       "dmiLanguage": dmiLanguage,
       "dmiMappingAgent": dmiMappingAgent,
       "dmiMappingLevel": dmiMappingLevel,
       "dmiNotifications": dmiNotifications,
       "dmiIndications": dmiIndications,
       "dmiEventIndication": dmiEventIndication,
       "dmiComponentAddedIndication": dmiComponentAddedIndication,
       "dmiComponentDeletedIndication": dmiComponentDeletedIndication,
       "dmiLanguageAddedIndication": dmiLanguageAddedIndication,
       "dmiLanguageDeletedIndication": dmiLanguageDeletedIndication,
       "dmiGroupAddedIndication": dmiGroupAddedIndication,
       "dmiGroupDeletedIndication": dmiGroupDeletedIndication,
       "dmiEventVars": dmiEventVars,
       "dmiEventType": dmiEventType,
       "dmiEventSeverity": dmiEventSeverity,
       "dmiEventStateKey": dmiEventStateKey,
       "dmiEventAssociatedGroup": dmiEventAssociatedGroup,
       "dmiEventSystem": dmiEventSystem,
       "dmiEventSubSystem": dmiEventSubSystem,
       "dmiEventSolution": dmiEventSolution,
       "dmiEventVendorMsg": dmiEventVendorMsg,
       "dmiEventVendorData": dmiEventVendorData,
       "dmiEventDateTime": dmiEventDateTime,
       "dmiEventClassString": dmiEventClassString,
       "dmiEventSource": dmiEventSource,
       "dmiMIBConformance": dmiMIBConformance,
       "dmiMIBCompliances": dmiMIBCompliances,
       "dmiMIBCompliance": dmiMIBCompliance,
       "dmiNotificationsOnlyCompliance": dmiNotificationsOnlyCompliance,
       "dmiMIBGroups": dmiMIBGroups,
       "dmiClassesGroup": dmiClassesGroup,
       "dmiComponentsGroup": dmiComponentsGroup,
       "dmiNotificationObjectGroup": dmiNotificationObjectGroup,
       "dmiMappingAgentGroup": dmiMappingAgentGroup,
       "dmiNotificationGroups": dmiNotificationGroups,
       "dmiNotificationsGroup": dmiNotificationsGroup,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfDynOids": dmtfDynOids}
)
