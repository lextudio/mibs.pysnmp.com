# SNMP MIB module (CTRON-SFPS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:19 2024
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

(sfpsAOProperties,
 sfpsAOPropertiesAPI,
 sfpsDiagEventLog,
 sfpsSystemGenerics) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsAOProperties",
    "sfpsAOPropertiesAPI",
    "sfpsDiagEventLog",
    "sfpsSystemGenerics")

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



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsGenericVersionTable_Object = MibTable
sfpsGenericVersionTable = _SfpsGenericVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sfpsGenericVersionTable.setStatus("mandatory")
_SfpsGenericVersionEntry_Object = MibTableRow
sfpsGenericVersionEntry = _SfpsGenericVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1)
)
sfpsGenericVersionEntry.setIndexNames(
    (0, "CTRON-SFPS-COMMON-MIB", "sfpsGenericVersionHash"),
)
if mibBuilder.loadTexts:
    sfpsGenericVersionEntry.setStatus("mandatory")
_SfpsGenericVersionHash_Type = Integer32
_SfpsGenericVersionHash_Object = MibTableColumn
sfpsGenericVersionHash = _SfpsGenericVersionHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 1),
    _SfpsGenericVersionHash_Type()
)
sfpsGenericVersionHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsGenericVersionHash.setStatus("mandatory")
_SfpsGenericVersionName_Type = DisplayString
_SfpsGenericVersionName_Object = MibTableColumn
sfpsGenericVersionName = _SfpsGenericVersionName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 2),
    _SfpsGenericVersionName_Type()
)
sfpsGenericVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsGenericVersionName.setStatus("mandatory")
_SfpsGenericVersionVersion_Type = DisplayString
_SfpsGenericVersionVersion_Object = MibTableColumn
sfpsGenericVersionVersion = _SfpsGenericVersionVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 3),
    _SfpsGenericVersionVersion_Type()
)
sfpsGenericVersionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsGenericVersionVersion.setStatus("mandatory")
_SfpsGenericVersionMIBRev_Type = DisplayString
_SfpsGenericVersionMIBRev_Object = MibTableColumn
sfpsGenericVersionMIBRev = _SfpsGenericVersionMIBRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 4),
    _SfpsGenericVersionMIBRev_Type()
)
sfpsGenericVersionMIBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsGenericVersionMIBRev.setStatus("mandatory")
_SfpsAOPropertiesTable_Object = MibTable
sfpsAOPropertiesTable = _SfpsAOPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsAOPropertiesTable.setStatus("mandatory")
_SfpsAOPropertiesEntry_Object = MibTableRow
sfpsAOPropertiesEntry = _SfpsAOPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1)
)
sfpsAOPropertiesEntry.setIndexNames(
    (0, "CTRON-SFPS-COMMON-MIB", "sfpsAOPropertiesTag"),
)
if mibBuilder.loadTexts:
    sfpsAOPropertiesEntry.setStatus("mandatory")
_SfpsAOPropertiesTag_Type = Integer32
_SfpsAOPropertiesTag_Object = MibTableColumn
sfpsAOPropertiesTag = _SfpsAOPropertiesTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 1),
    _SfpsAOPropertiesTag_Type()
)
sfpsAOPropertiesTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesTag.setStatus("mandatory")
_SfpsAOPropertiesTagDescriptor_Type = OctetString
_SfpsAOPropertiesTagDescriptor_Object = MibTableColumn
sfpsAOPropertiesTagDescriptor = _SfpsAOPropertiesTagDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 2),
    _SfpsAOPropertiesTagDescriptor_Type()
)
sfpsAOPropertiesTagDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesTagDescriptor.setStatus("mandatory")
_SfpsAOPropertiesPrettyType_Type = OctetString
_SfpsAOPropertiesPrettyType_Object = MibTableColumn
sfpsAOPropertiesPrettyType = _SfpsAOPropertiesPrettyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 3),
    _SfpsAOPropertiesPrettyType_Type()
)
sfpsAOPropertiesPrettyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesPrettyType.setStatus("mandatory")
_SfpsAOPropertiesNumBytes_Type = Integer32
_SfpsAOPropertiesNumBytes_Object = MibTableColumn
sfpsAOPropertiesNumBytes = _SfpsAOPropertiesNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 4),
    _SfpsAOPropertiesNumBytes_Type()
)
sfpsAOPropertiesNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesNumBytes.setStatus("mandatory")


class _SfpsAOPropertiesIsLimit_Type(Integer32):
    """Custom type sfpsAOPropertiesIsLimit based on Integer32"""
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


_SfpsAOPropertiesIsLimit_Type.__name__ = "Integer32"
_SfpsAOPropertiesIsLimit_Object = MibTableColumn
sfpsAOPropertiesIsLimit = _SfpsAOPropertiesIsLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 5),
    _SfpsAOPropertiesIsLimit_Type()
)
sfpsAOPropertiesIsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesIsLimit.setStatus("mandatory")


class _SfpsAOPropertiesIsMobile_Type(Integer32):
    """Custom type sfpsAOPropertiesIsMobile based on Integer32"""
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


_SfpsAOPropertiesIsMobile_Type.__name__ = "Integer32"
_SfpsAOPropertiesIsMobile_Object = MibTableColumn
sfpsAOPropertiesIsMobile = _SfpsAOPropertiesIsMobile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 6),
    _SfpsAOPropertiesIsMobile_Type()
)
sfpsAOPropertiesIsMobile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesIsMobile.setStatus("mandatory")


class _SfpsAOPropertiesIsSingle_Type(Integer32):
    """Custom type sfpsAOPropertiesIsSingle based on Integer32"""
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


_SfpsAOPropertiesIsSingle_Type.__name__ = "Integer32"
_SfpsAOPropertiesIsSingle_Object = MibTableColumn
sfpsAOPropertiesIsSingle = _SfpsAOPropertiesIsSingle_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 7),
    _SfpsAOPropertiesIsSingle_Type()
)
sfpsAOPropertiesIsSingle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesIsSingle.setStatus("mandatory")


class _SfpsAOPropertiesNoBlock_Type(Integer32):
    """Custom type sfpsAOPropertiesNoBlock based on Integer32"""
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


_SfpsAOPropertiesNoBlock_Type.__name__ = "Integer32"
_SfpsAOPropertiesNoBlock_Object = MibTableColumn
sfpsAOPropertiesNoBlock = _SfpsAOPropertiesNoBlock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 8),
    _SfpsAOPropertiesNoBlock_Type()
)
sfpsAOPropertiesNoBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesNoBlock.setStatus("mandatory")


class _SfpsAOPropertiesNoDelta_Type(Integer32):
    """Custom type sfpsAOPropertiesNoDelta based on Integer32"""
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


_SfpsAOPropertiesNoDelta_Type.__name__ = "Integer32"
_SfpsAOPropertiesNoDelta_Object = MibTableColumn
sfpsAOPropertiesNoDelta = _SfpsAOPropertiesNoDelta_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 9),
    _SfpsAOPropertiesNoDelta_Type()
)
sfpsAOPropertiesNoDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesNoDelta.setStatus("mandatory")
_SfpsAOPropertiesAPITag_Type = Integer32
_SfpsAOPropertiesAPITag_Object = MibScalar
sfpsAOPropertiesAPITag = _SfpsAOPropertiesAPITag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 1),
    _SfpsAOPropertiesAPITag_Type()
)
sfpsAOPropertiesAPITag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPITag.setStatus("mandatory")
_SfpsAOPropertiesAPITagString_Type = Integer32
_SfpsAOPropertiesAPITagString_Object = MibScalar
sfpsAOPropertiesAPITagString = _SfpsAOPropertiesAPITagString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 2),
    _SfpsAOPropertiesAPITagString_Type()
)
sfpsAOPropertiesAPITagString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPITagString.setStatus("mandatory")
_SfpsAOPropertiesAPIPrettyType_Type = Integer32
_SfpsAOPropertiesAPIPrettyType_Object = MibScalar
sfpsAOPropertiesAPIPrettyType = _SfpsAOPropertiesAPIPrettyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 3),
    _SfpsAOPropertiesAPIPrettyType_Type()
)
sfpsAOPropertiesAPIPrettyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPIPrettyType.setStatus("mandatory")
_SfpsAOPropertiesAPINumBytes_Type = Integer32
_SfpsAOPropertiesAPINumBytes_Object = MibScalar
sfpsAOPropertiesAPINumBytes = _SfpsAOPropertiesAPINumBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 4),
    _SfpsAOPropertiesAPINumBytes_Type()
)
sfpsAOPropertiesAPINumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPINumBytes.setStatus("mandatory")


class _SfpsAOPropertiesAPIIsLimit_Type(Integer32):
    """Custom type sfpsAOPropertiesAPIIsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSet", 1),
          ("true", 3))
    )


_SfpsAOPropertiesAPIIsLimit_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPIIsLimit_Object = MibScalar
sfpsAOPropertiesAPIIsLimit = _SfpsAOPropertiesAPIIsLimit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 5),
    _SfpsAOPropertiesAPIIsLimit_Type()
)
sfpsAOPropertiesAPIIsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPIIsLimit.setStatus("mandatory")


class _SfpsAOPropertiesAPIIsMobile_Type(Integer32):
    """Custom type sfpsAOPropertiesAPIIsMobile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSet", 1),
          ("true", 3))
    )


_SfpsAOPropertiesAPIIsMobile_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPIIsMobile_Object = MibScalar
sfpsAOPropertiesAPIIsMobile = _SfpsAOPropertiesAPIIsMobile_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 6),
    _SfpsAOPropertiesAPIIsMobile_Type()
)
sfpsAOPropertiesAPIIsMobile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPIIsMobile.setStatus("mandatory")


class _SfpsAOPropertiesAPIIsSingle_Type(Integer32):
    """Custom type sfpsAOPropertiesAPIIsSingle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSet", 1),
          ("true", 3))
    )


_SfpsAOPropertiesAPIIsSingle_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPIIsSingle_Object = MibScalar
sfpsAOPropertiesAPIIsSingle = _SfpsAOPropertiesAPIIsSingle_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 7),
    _SfpsAOPropertiesAPIIsSingle_Type()
)
sfpsAOPropertiesAPIIsSingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPIIsSingle.setStatus("mandatory")


class _SfpsAOPropertiesAPINoBlock_Type(Integer32):
    """Custom type sfpsAOPropertiesAPINoBlock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSet", 1),
          ("true", 3))
    )


_SfpsAOPropertiesAPINoBlock_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPINoBlock_Object = MibScalar
sfpsAOPropertiesAPINoBlock = _SfpsAOPropertiesAPINoBlock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 8),
    _SfpsAOPropertiesAPINoBlock_Type()
)
sfpsAOPropertiesAPINoBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPINoBlock.setStatus("mandatory")


class _SfpsAOPropertiesAPINoDelta_Type(Integer32):
    """Custom type sfpsAOPropertiesAPINoDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSet", 1),
          ("true", 3))
    )


_SfpsAOPropertiesAPINoDelta_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPINoDelta_Object = MibScalar
sfpsAOPropertiesAPINoDelta = _SfpsAOPropertiesAPINoDelta_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 9),
    _SfpsAOPropertiesAPINoDelta_Type()
)
sfpsAOPropertiesAPINoDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPINoDelta.setStatus("mandatory")


class _SfpsAOPropertiesAPIAction_Type(Integer32):
    """Custom type sfpsAOPropertiesAPIAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readProperties", 1),
          ("setProperties", 2))
    )


_SfpsAOPropertiesAPIAction_Type.__name__ = "Integer32"
_SfpsAOPropertiesAPIAction_Object = MibScalar
sfpsAOPropertiesAPIAction = _SfpsAOPropertiesAPIAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 10),
    _SfpsAOPropertiesAPIAction_Type()
)
sfpsAOPropertiesAPIAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAOPropertiesAPIAction.setStatus("mandatory")
_SfpsDiagLogConfigTable_Object = MibTable
sfpsDiagLogConfigTable = _SfpsDiagLogConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsDiagLogConfigTable.setStatus("mandatory")
_SfpsDiagLogConfigEntry_Object = MibTableRow
sfpsDiagLogConfigEntry = _SfpsDiagLogConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1)
)
sfpsDiagLogConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-COMMON-MIB", "sfpsDiagLogConfigInstance"),
)
if mibBuilder.loadTexts:
    sfpsDiagLogConfigEntry.setStatus("mandatory")
_SfpsDiagLogConfigInstance_Type = Integer32
_SfpsDiagLogConfigInstance_Object = MibTableColumn
sfpsDiagLogConfigInstance = _SfpsDiagLogConfigInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 1),
    _SfpsDiagLogConfigInstance_Type()
)
sfpsDiagLogConfigInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigInstance.setStatus("mandatory")


class _SfpsDiagLogConfigStatus_Type(Integer32):
    """Custom type sfpsDiagLogConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsDiagLogConfigStatus_Type.__name__ = "Integer32"
_SfpsDiagLogConfigStatus_Object = MibTableColumn
sfpsDiagLogConfigStatus = _SfpsDiagLogConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 2),
    _SfpsDiagLogConfigStatus_Type()
)
sfpsDiagLogConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigStatus.setStatus("mandatory")
_SfpsDiagLogConfigIndex_Type = Integer32
_SfpsDiagLogConfigIndex_Object = MibTableColumn
sfpsDiagLogConfigIndex = _SfpsDiagLogConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 3),
    _SfpsDiagLogConfigIndex_Type()
)
sfpsDiagLogConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigIndex.setStatus("mandatory")
_SfpsDiagLogConfigStart_Type = Integer32
_SfpsDiagLogConfigStart_Object = MibTableColumn
sfpsDiagLogConfigStart = _SfpsDiagLogConfigStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 4),
    _SfpsDiagLogConfigStart_Type()
)
sfpsDiagLogConfigStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigStart.setStatus("mandatory")
_SfpsDiagLogConfigStop_Type = Integer32
_SfpsDiagLogConfigStop_Object = MibTableColumn
sfpsDiagLogConfigStop = _SfpsDiagLogConfigStop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 5),
    _SfpsDiagLogConfigStop_Type()
)
sfpsDiagLogConfigStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigStop.setStatus("mandatory")
_SfpsDiagLogConfigLogIndex_Type = Integer32
_SfpsDiagLogConfigLogIndex_Object = MibTableColumn
sfpsDiagLogConfigLogIndex = _SfpsDiagLogConfigLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 6),
    _SfpsDiagLogConfigLogIndex_Type()
)
sfpsDiagLogConfigLogIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigLogIndex.setStatus("mandatory")
_SfpsDiagLogConfigFilterMatch_Type = Integer32
_SfpsDiagLogConfigFilterMatch_Object = MibTableColumn
sfpsDiagLogConfigFilterMatch = _SfpsDiagLogConfigFilterMatch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 7),
    _SfpsDiagLogConfigFilterMatch_Type()
)
sfpsDiagLogConfigFilterMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigFilterMatch.setStatus("mandatory")
_SfpsDiagLogConfigFilterStart_Type = Integer32
_SfpsDiagLogConfigFilterStart_Object = MibTableColumn
sfpsDiagLogConfigFilterStart = _SfpsDiagLogConfigFilterStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 8),
    _SfpsDiagLogConfigFilterStart_Type()
)
sfpsDiagLogConfigFilterStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigFilterStart.setStatus("mandatory")
_SfpsDiagLogConfigFilterStop_Type = Integer32
_SfpsDiagLogConfigFilterStop_Object = MibTableColumn
sfpsDiagLogConfigFilterStop = _SfpsDiagLogConfigFilterStop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 9),
    _SfpsDiagLogConfigFilterStop_Type()
)
sfpsDiagLogConfigFilterStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigFilterStop.setStatus("mandatory")


class _SfpsDiagLogAccessPortControl_Type(HexInteger):
    """Custom type sfpsDiagLogAccessPortControl based on HexInteger"""
    defaultValue = 0


_SfpsDiagLogAccessPortControl_Object = MibTableColumn
sfpsDiagLogAccessPortControl = _SfpsDiagLogAccessPortControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 10),
    _SfpsDiagLogAccessPortControl_Type()
)
sfpsDiagLogAccessPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogAccessPortControl.setStatus("mandatory")


class _SfpsDiagLogCallIdleTime_Type(Integer32):
    """Custom type sfpsDiagLogCallIdleTime based on Integer32"""
    defaultValue = 60


_SfpsDiagLogCallIdleTime_Object = MibTableColumn
sfpsDiagLogCallIdleTime = _SfpsDiagLogCallIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 11),
    _SfpsDiagLogCallIdleTime_Type()
)
sfpsDiagLogCallIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogCallIdleTime.setStatus("mandatory")


class _SfpsDiagLogFilterAddTimer_Type(Integer32):
    """Custom type sfpsDiagLogFilterAddTimer based on Integer32"""
    defaultValue = 900


_SfpsDiagLogFilterAddTimer_Object = MibTableColumn
sfpsDiagLogFilterAddTimer = _SfpsDiagLogFilterAddTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 12),
    _SfpsDiagLogFilterAddTimer_Type()
)
sfpsDiagLogFilterAddTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogFilterAddTimer.setStatus("mandatory")
_SfpsDiagLogRedirectorWakeup_Type = Integer32
_SfpsDiagLogRedirectorWakeup_Object = MibTableColumn
sfpsDiagLogRedirectorWakeup = _SfpsDiagLogRedirectorWakeup_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 13),
    _SfpsDiagLogRedirectorWakeup_Type()
)
sfpsDiagLogRedirectorWakeup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogRedirectorWakeup.setStatus("mandatory")


class _SfpsDiagLogRedirectorNumPackets_Type(Integer32):
    """Custom type sfpsDiagLogRedirectorNumPackets based on Integer32"""
    defaultValue = 64


_SfpsDiagLogRedirectorNumPackets_Object = MibTableColumn
sfpsDiagLogRedirectorNumPackets = _SfpsDiagLogRedirectorNumPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 14),
    _SfpsDiagLogRedirectorNumPackets_Type()
)
sfpsDiagLogRedirectorNumPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogRedirectorNumPackets.setStatus("mandatory")


class _SfpsDiagLogEndSystemTimeout_Type(Integer32):
    """Custom type sfpsDiagLogEndSystemTimeout based on Integer32"""
    defaultValue = 600


_SfpsDiagLogEndSystemTimeout_Object = MibTableColumn
sfpsDiagLogEndSystemTimeout = _SfpsDiagLogEndSystemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 15),
    _SfpsDiagLogEndSystemTimeout_Type()
)
sfpsDiagLogEndSystemTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogEndSystemTimeout.setStatus("mandatory")


class _SfpsDiagLogSwitchIdleInterval_Type(Integer32):
    """Custom type sfpsDiagLogSwitchIdleInterval based on Integer32"""
    defaultValue = 30


_SfpsDiagLogSwitchIdleInterval_Object = MibTableColumn
sfpsDiagLogSwitchIdleInterval = _SfpsDiagLogSwitchIdleInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 16),
    _SfpsDiagLogSwitchIdleInterval_Type()
)
sfpsDiagLogSwitchIdleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogSwitchIdleInterval.setStatus("mandatory")
_SfpsDiagLogInlnFltrAgeTime_Type = Integer32
_SfpsDiagLogInlnFltrAgeTime_Object = MibTableColumn
sfpsDiagLogInlnFltrAgeTime = _SfpsDiagLogInlnFltrAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 17),
    _SfpsDiagLogInlnFltrAgeTime_Type()
)
sfpsDiagLogInlnFltrAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogInlnFltrAgeTime.setStatus("mandatory")
_SfpsDiagLogConfigDebug9_Type = Integer32
_SfpsDiagLogConfigDebug9_Object = MibTableColumn
sfpsDiagLogConfigDebug9 = _SfpsDiagLogConfigDebug9_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 18),
    _SfpsDiagLogConfigDebug9_Type()
)
sfpsDiagLogConfigDebug9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigDebug9.setStatus("mandatory")
_SfpsDiagLogSignalThrottle_Type = Integer32
_SfpsDiagLogSignalThrottle_Object = MibTableColumn
sfpsDiagLogSignalThrottle = _SfpsDiagLogSignalThrottle_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 19),
    _SfpsDiagLogSignalThrottle_Type()
)
sfpsDiagLogSignalThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogSignalThrottle.setStatus("mandatory")


class _SfpsDiagLogConfigOther_Type(Integer32):
    """Custom type sfpsDiagLogConfigOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("integer", 2),
          ("string", 1))
    )


_SfpsDiagLogConfigOther_Type.__name__ = "Integer32"
_SfpsDiagLogConfigOther_Object = MibTableColumn
sfpsDiagLogConfigOther = _SfpsDiagLogConfigOther_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 20),
    _SfpsDiagLogConfigOther_Type()
)
sfpsDiagLogConfigOther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigOther.setStatus("mandatory")
_SfpsDiagLogConfigSoftReset_Type = Integer32
_SfpsDiagLogConfigSoftReset_Object = MibTableColumn
sfpsDiagLogConfigSoftReset = _SfpsDiagLogConfigSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 21),
    _SfpsDiagLogConfigSoftReset_Type()
)
sfpsDiagLogConfigSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigSoftReset.setStatus("mandatory")
_SfpsDiagLogConfigSFPSVlan_Type = Integer32
_SfpsDiagLogConfigSFPSVlan_Object = MibTableColumn
sfpsDiagLogConfigSFPSVlan = _SfpsDiagLogConfigSFPSVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 22),
    _SfpsDiagLogConfigSFPSVlan_Type()
)
sfpsDiagLogConfigSFPSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDiagLogConfigSFPSVlan.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-COMMON-MIB",
    **{"HexInteger": HexInteger,
       "sfpsGenericVersionTable": sfpsGenericVersionTable,
       "sfpsGenericVersionEntry": sfpsGenericVersionEntry,
       "sfpsGenericVersionHash": sfpsGenericVersionHash,
       "sfpsGenericVersionName": sfpsGenericVersionName,
       "sfpsGenericVersionVersion": sfpsGenericVersionVersion,
       "sfpsGenericVersionMIBRev": sfpsGenericVersionMIBRev,
       "sfpsAOPropertiesTable": sfpsAOPropertiesTable,
       "sfpsAOPropertiesEntry": sfpsAOPropertiesEntry,
       "sfpsAOPropertiesTag": sfpsAOPropertiesTag,
       "sfpsAOPropertiesTagDescriptor": sfpsAOPropertiesTagDescriptor,
       "sfpsAOPropertiesPrettyType": sfpsAOPropertiesPrettyType,
       "sfpsAOPropertiesNumBytes": sfpsAOPropertiesNumBytes,
       "sfpsAOPropertiesIsLimit": sfpsAOPropertiesIsLimit,
       "sfpsAOPropertiesIsMobile": sfpsAOPropertiesIsMobile,
       "sfpsAOPropertiesIsSingle": sfpsAOPropertiesIsSingle,
       "sfpsAOPropertiesNoBlock": sfpsAOPropertiesNoBlock,
       "sfpsAOPropertiesNoDelta": sfpsAOPropertiesNoDelta,
       "sfpsAOPropertiesAPITag": sfpsAOPropertiesAPITag,
       "sfpsAOPropertiesAPITagString": sfpsAOPropertiesAPITagString,
       "sfpsAOPropertiesAPIPrettyType": sfpsAOPropertiesAPIPrettyType,
       "sfpsAOPropertiesAPINumBytes": sfpsAOPropertiesAPINumBytes,
       "sfpsAOPropertiesAPIIsLimit": sfpsAOPropertiesAPIIsLimit,
       "sfpsAOPropertiesAPIIsMobile": sfpsAOPropertiesAPIIsMobile,
       "sfpsAOPropertiesAPIIsSingle": sfpsAOPropertiesAPIIsSingle,
       "sfpsAOPropertiesAPINoBlock": sfpsAOPropertiesAPINoBlock,
       "sfpsAOPropertiesAPINoDelta": sfpsAOPropertiesAPINoDelta,
       "sfpsAOPropertiesAPIAction": sfpsAOPropertiesAPIAction,
       "sfpsDiagLogConfigTable": sfpsDiagLogConfigTable,
       "sfpsDiagLogConfigEntry": sfpsDiagLogConfigEntry,
       "sfpsDiagLogConfigInstance": sfpsDiagLogConfigInstance,
       "sfpsDiagLogConfigStatus": sfpsDiagLogConfigStatus,
       "sfpsDiagLogConfigIndex": sfpsDiagLogConfigIndex,
       "sfpsDiagLogConfigStart": sfpsDiagLogConfigStart,
       "sfpsDiagLogConfigStop": sfpsDiagLogConfigStop,
       "sfpsDiagLogConfigLogIndex": sfpsDiagLogConfigLogIndex,
       "sfpsDiagLogConfigFilterMatch": sfpsDiagLogConfigFilterMatch,
       "sfpsDiagLogConfigFilterStart": sfpsDiagLogConfigFilterStart,
       "sfpsDiagLogConfigFilterStop": sfpsDiagLogConfigFilterStop,
       "sfpsDiagLogAccessPortControl": sfpsDiagLogAccessPortControl,
       "sfpsDiagLogCallIdleTime": sfpsDiagLogCallIdleTime,
       "sfpsDiagLogFilterAddTimer": sfpsDiagLogFilterAddTimer,
       "sfpsDiagLogRedirectorWakeup": sfpsDiagLogRedirectorWakeup,
       "sfpsDiagLogRedirectorNumPackets": sfpsDiagLogRedirectorNumPackets,
       "sfpsDiagLogEndSystemTimeout": sfpsDiagLogEndSystemTimeout,
       "sfpsDiagLogSwitchIdleInterval": sfpsDiagLogSwitchIdleInterval,
       "sfpsDiagLogInlnFltrAgeTime": sfpsDiagLogInlnFltrAgeTime,
       "sfpsDiagLogConfigDebug9": sfpsDiagLogConfigDebug9,
       "sfpsDiagLogSignalThrottle": sfpsDiagLogSignalThrottle,
       "sfpsDiagLogConfigOther": sfpsDiagLogConfigOther,
       "sfpsDiagLogConfigSoftReset": sfpsDiagLogConfigSoftReset,
       "sfpsDiagLogConfigSFPSVlan": sfpsDiagLogConfigSFPSVlan}
)
