# SNMP MIB module (NNCGNI00X4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:26 2024
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

(nncExtPosition,) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtPosition")

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



class PositionIndex(Integer32):
    """Custom type PositionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class PositionCardType(Integer32):
    """Custom type PositionCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              46,
              108,
              109,
              110,
              111,
              120)
        )
    )
    namedValues = NamedValues(
        *(("ctlCard", 46),
          ("e1Card", 5),
          ("ethernetCard", 111),
          ("hubCard", 120),
          ("noCard", 1),
          ("t1Card", 6),
          ("v24Card", 109),
          ("v35Card", 110),
          ("x21Card", 108))
    )





class PositionModuleType(Integer32):
    """Custom type PositionModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("auiModule", 26),
          ("foirlModule", 28),
          ("hubModule", 29),
          ("noModule", 1),
          ("nullAUIModule", 27),
          ("thinModule", 24),
          ("tpModule", 25))
    )





class PositionCardId(Integer32):
    """Custom type PositionCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              10,
              12,
              24,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ctlCardId", 0),
          ("e1CoaxCardId", 12),
          ("e1TpCardId", 24),
          ("ethernetCardId", 1),
          ("hubCardId", 28),
          ("t1CsuCardId", 10),
          ("t1DsxCardId", 8),
          ("v24CardId", 4),
          ("v35CardId", 6),
          ("x21CardId", 2))
    )





class PositionModuleId(Integer32):
    """Custom type PositionModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auiModId", 0),
          ("foirlModId", 5),
          ("hubModId", 2),
          ("nullAUIModId", 6),
          ("thinModId", 1),
          ("tpModId", 4))
    )





class PositionVariantId(Integer32):
    """Custom type PositionVariantId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class RevisionNumber(Integer32):
    """Custom type RevisionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class PositionAdminStatus(Integer32):
    """Custom type PositionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busiedOut", 2),
          ("inUse", 1),
          ("reset", 3))
    )





class PositionOperStatus(Integer32):
    """Custom type PositionOperStatus based on Integer32"""
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
              9,
              12)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("fault-on-module", 3),
          ("module-dead", 4),
          ("module-type-mismatch", 6),
          ("ok", 2),
          ("sub-module-type-mismatch", 7),
          ("unknown-module-type", 5),
          ("wrong-firmware", 9),
          ("wrong-variant", 12))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NncExtPositionMaxPossible_Type(Integer32):
    """Custom type nncExtPositionMaxPossible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtPositionMaxPossible_Type.__name__ = "Integer32"
_NncExtPositionMaxPossible_Object = MibScalar
nncExtPositionMaxPossible = _NncExtPositionMaxPossible_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 1),
    _NncExtPositionMaxPossible_Type()
)
nncExtPositionMaxPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionMaxPossible.setStatus("mandatory")
_NncExtPositionTable_Object = MibTable
nncExtPositionTable = _NncExtPositionTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2)
)
if mibBuilder.loadTexts:
    nncExtPositionTable.setStatus("mandatory")
_NncExtPositionEntry_Object = MibTableRow
nncExtPositionEntry = _NncExtPositionEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1)
)
nncExtPositionEntry.setIndexNames(
    (0, "NNCGNI00X4-MIB", "nncExtPositionIndex"),
)
if mibBuilder.loadTexts:
    nncExtPositionEntry.setStatus("mandatory")
_NncExtPositionIndex_Type = PositionIndex
_NncExtPositionIndex_Object = MibTableColumn
nncExtPositionIndex = _NncExtPositionIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 1),
    _NncExtPositionIndex_Type()
)
nncExtPositionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionIndex.setStatus("mandatory")


class _NncExtPositionProgCard_Type(Integer32):
    """Custom type nncExtPositionProgCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              46,
              108,
              109,
              110,
              111,
              120)
        )
    )
    namedValues = NamedValues(
        *(("ctlCard", 46),
          ("e1Card", 5),
          ("ethernetCard", 111),
          ("hubCard", 120),
          ("noCard", 1),
          ("t1Card", 6),
          ("v24Card", 109),
          ("v35Card", 110),
          ("x21Card", 108))
    )


_NncExtPositionProgCard_Type.__name__ = "Integer32"
_NncExtPositionProgCard_Object = MibTableColumn
nncExtPositionProgCard = _NncExtPositionProgCard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 2),
    _NncExtPositionProgCard_Type()
)
nncExtPositionProgCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtPositionProgCard.setStatus("mandatory")


class _NncExtPositionProgModule_Type(Integer32):
    """Custom type nncExtPositionProgModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("auiModule", 26),
          ("foirlModule", 28),
          ("hubModule", 29),
          ("noModule", 1),
          ("nullAUIModule", 27),
          ("thinModule", 24),
          ("tpModule", 25))
    )


_NncExtPositionProgModule_Type.__name__ = "Integer32"
_NncExtPositionProgModule_Object = MibTableColumn
nncExtPositionProgModule = _NncExtPositionProgModule_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 3),
    _NncExtPositionProgModule_Type()
)
nncExtPositionProgModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtPositionProgModule.setStatus("mandatory")


class _NncExtPositionCurrentCard_Type(Integer32):
    """Custom type nncExtPositionCurrentCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              46,
              108,
              109,
              110,
              111,
              120)
        )
    )
    namedValues = NamedValues(
        *(("ctlCard", 46),
          ("e1Card", 5),
          ("ethernetCard", 111),
          ("hubCard", 120),
          ("noCard", 1),
          ("t1Card", 6),
          ("v24Card", 109),
          ("v35Card", 110),
          ("x21Card", 108))
    )


_NncExtPositionCurrentCard_Type.__name__ = "Integer32"
_NncExtPositionCurrentCard_Object = MibTableColumn
nncExtPositionCurrentCard = _NncExtPositionCurrentCard_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 4),
    _NncExtPositionCurrentCard_Type()
)
nncExtPositionCurrentCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionCurrentCard.setStatus("mandatory")


class _NncExtPositionCurrentModule_Type(Integer32):
    """Custom type nncExtPositionCurrentModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("auiModule", 26),
          ("foirlModule", 28),
          ("hubModule", 29),
          ("noModule", 1),
          ("nullAUIModule", 27),
          ("thinModule", 24),
          ("tpModule", 25))
    )


_NncExtPositionCurrentModule_Type.__name__ = "Integer32"
_NncExtPositionCurrentModule_Object = MibTableColumn
nncExtPositionCurrentModule = _NncExtPositionCurrentModule_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 5),
    _NncExtPositionCurrentModule_Type()
)
nncExtPositionCurrentModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionCurrentModule.setStatus("mandatory")


class _NncExtPositionOperStatus_Type(Integer32):
    """Custom type nncExtPositionOperStatus based on Integer32"""
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
              9,
              12)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("fault-on-module", 3),
          ("module-dead", 4),
          ("module-type-mismatch", 6),
          ("ok", 2),
          ("sub-module-type-mismatch", 7),
          ("unknown-module-type", 5),
          ("wrong-firmware", 9),
          ("wrong-variant", 12))
    )


_NncExtPositionOperStatus_Type.__name__ = "Integer32"
_NncExtPositionOperStatus_Object = MibTableColumn
nncExtPositionOperStatus = _NncExtPositionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 6),
    _NncExtPositionOperStatus_Type()
)
nncExtPositionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionOperStatus.setStatus("mandatory")


class _NncExtPositionAdminStatus_Type(Integer32):
    """Custom type nncExtPositionAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busiedOut", 2),
          ("inUse", 1),
          ("reset", 3))
    )


_NncExtPositionAdminStatus_Type.__name__ = "Integer32"
_NncExtPositionAdminStatus_Object = MibTableColumn
nncExtPositionAdminStatus = _NncExtPositionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 7),
    _NncExtPositionAdminStatus_Type()
)
nncExtPositionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtPositionAdminStatus.setStatus("mandatory")


class _NncExtPositionCardId_Type(Integer32):
    """Custom type nncExtPositionCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              10,
              12,
              24,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ctlCardId", 0),
          ("e1CoaxCardId", 12),
          ("e1TpCardId", 24),
          ("ethernetCardId", 1),
          ("hubCardId", 28),
          ("t1CsuCardId", 10),
          ("t1DsxCardId", 8),
          ("v24CardId", 4),
          ("v35CardId", 6),
          ("x21CardId", 2))
    )


_NncExtPositionCardId_Type.__name__ = "Integer32"
_NncExtPositionCardId_Object = MibTableColumn
nncExtPositionCardId = _NncExtPositionCardId_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 8),
    _NncExtPositionCardId_Type()
)
nncExtPositionCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionCardId.setStatus("mandatory")


class _NncExtPositionModuleId_Type(Integer32):
    """Custom type nncExtPositionModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auiModId", 0),
          ("foirlModId", 5),
          ("hubModId", 2),
          ("nullAUIModId", 6),
          ("thinModId", 1),
          ("tpModId", 4))
    )


_NncExtPositionModuleId_Type.__name__ = "Integer32"
_NncExtPositionModuleId_Object = MibTableColumn
nncExtPositionModuleId = _NncExtPositionModuleId_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 9),
    _NncExtPositionModuleId_Type()
)
nncExtPositionModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionModuleId.setStatus("mandatory")
_NncExtPositionVariantId_Type = PositionVariantId
_NncExtPositionVariantId_Object = MibTableColumn
nncExtPositionVariantId = _NncExtPositionVariantId_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 10),
    _NncExtPositionVariantId_Type()
)
nncExtPositionVariantId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionVariantId.setStatus("mandatory")
_NncExtPositionHardwareRevision_Type = RevisionNumber
_NncExtPositionHardwareRevision_Object = MibTableColumn
nncExtPositionHardwareRevision = _NncExtPositionHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 11),
    _NncExtPositionHardwareRevision_Type()
)
nncExtPositionHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionHardwareRevision.setStatus("mandatory")
_NncExtPositionFirmwareRevision_Type = RevisionNumber
_NncExtPositionFirmwareRevision_Object = MibTableColumn
nncExtPositionFirmwareRevision = _NncExtPositionFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 12),
    _NncExtPositionFirmwareRevision_Type()
)
nncExtPositionFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionFirmwareRevision.setStatus("mandatory")


class _NncExtPositionUIName_Type(DisplayString):
    """Custom type nncExtPositionUIName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_NncExtPositionUIName_Type.__name__ = "DisplayString"
_NncExtPositionUIName_Object = MibTableColumn
nncExtPositionUIName = _NncExtPositionUIName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 13),
    _NncExtPositionUIName_Type()
)
nncExtPositionUIName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionUIName.setStatus("mandatory")


class _NncExtPositionName_Type(DisplayString):
    """Custom type nncExtPositionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NncExtPositionName_Type.__name__ = "DisplayString"
_NncExtPositionName_Object = MibTableColumn
nncExtPositionName = _NncExtPositionName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 2, 1, 14),
    _NncExtPositionName_Type()
)
nncExtPositionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtPositionName.setStatus("mandatory")


class _NncExtPositionBackplaneIdAndRev_Type(Integer32):
    """Custom type nncExtPositionBackplaneIdAndRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtPositionBackplaneIdAndRev_Type.__name__ = "Integer32"
_NncExtPositionBackplaneIdAndRev_Object = MibScalar
nncExtPositionBackplaneIdAndRev = _NncExtPositionBackplaneIdAndRev_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 3),
    _NncExtPositionBackplaneIdAndRev_Type()
)
nncExtPositionBackplaneIdAndRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionBackplaneIdAndRev.setStatus("mandatory")


class _NncExtPositionDisplayIdAndRev_Type(Integer32):
    """Custom type nncExtPositionDisplayIdAndRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtPositionDisplayIdAndRev_Type.__name__ = "Integer32"
_NncExtPositionDisplayIdAndRev_Object = MibScalar
nncExtPositionDisplayIdAndRev = _NncExtPositionDisplayIdAndRev_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 8, 4),
    _NncExtPositionDisplayIdAndRev_Type()
)
nncExtPositionDisplayIdAndRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtPositionDisplayIdAndRev.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X4-MIB",
    **{"PositionIndex": PositionIndex,
       "PositionCardType": PositionCardType,
       "PositionModuleType": PositionModuleType,
       "PositionCardId": PositionCardId,
       "PositionModuleId": PositionModuleId,
       "PositionVariantId": PositionVariantId,
       "RevisionNumber": RevisionNumber,
       "PositionAdminStatus": PositionAdminStatus,
       "PositionOperStatus": PositionOperStatus,
       "nncExtPositionMaxPossible": nncExtPositionMaxPossible,
       "nncExtPositionTable": nncExtPositionTable,
       "nncExtPositionEntry": nncExtPositionEntry,
       "nncExtPositionIndex": nncExtPositionIndex,
       "nncExtPositionProgCard": nncExtPositionProgCard,
       "nncExtPositionProgModule": nncExtPositionProgModule,
       "nncExtPositionCurrentCard": nncExtPositionCurrentCard,
       "nncExtPositionCurrentModule": nncExtPositionCurrentModule,
       "nncExtPositionOperStatus": nncExtPositionOperStatus,
       "nncExtPositionAdminStatus": nncExtPositionAdminStatus,
       "nncExtPositionCardId": nncExtPositionCardId,
       "nncExtPositionModuleId": nncExtPositionModuleId,
       "nncExtPositionVariantId": nncExtPositionVariantId,
       "nncExtPositionHardwareRevision": nncExtPositionHardwareRevision,
       "nncExtPositionFirmwareRevision": nncExtPositionFirmwareRevision,
       "nncExtPositionUIName": nncExtPositionUIName,
       "nncExtPositionName": nncExtPositionName,
       "nncExtPositionBackplaneIdAndRev": nncExtPositionBackplaneIdAndRev,
       "nncExtPositionDisplayIdAndRev": nncExtPositionDisplayIdAndRev}
)
