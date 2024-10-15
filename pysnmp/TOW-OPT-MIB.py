# SNMP MIB module (TOW-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOW-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:41 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500TOWCfgTable_Object = MibTable
cdx6500TOWCfgTable = _Cdx6500TOWCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22)
)
if mibBuilder.loadTexts:
    cdx6500TOWCfgTable.setStatus("mandatory")
_Cdx6500TOWCfgEntry_Object = MibTableRow
cdx6500TOWCfgEntry = _Cdx6500TOWCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1)
)
cdx6500TOWCfgEntry.setIndexNames(
    (0, "TOW-OPT-MIB", "cdx6500TowCfgEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500TOWCfgEntry.setStatus("mandatory")


class _Cdx6500TowCfgEntryNum_Type(Integer32):
    """Custom type cdx6500TowCfgEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Cdx6500TowCfgEntryNum_Type.__name__ = "Integer32"
_Cdx6500TowCfgEntryNum_Object = MibTableColumn
cdx6500TowCfgEntryNum = _Cdx6500TowCfgEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 1),
    _Cdx6500TowCfgEntryNum_Type()
)
cdx6500TowCfgEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgEntryNum.setStatus("mandatory")


class _Cdx6500TowCfgEntryName_Type(DisplayString):
    """Custom type cdx6500TowCfgEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500TowCfgEntryName_Type.__name__ = "DisplayString"
_Cdx6500TowCfgEntryName_Object = MibTableColumn
cdx6500TowCfgEntryName = _Cdx6500TowCfgEntryName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 2),
    _Cdx6500TowCfgEntryName_Type()
)
cdx6500TowCfgEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgEntryName.setStatus("mandatory")


class _Cdx6500TowCfgInt1StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt1StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt1StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt1StartTime_Object = MibTableColumn
cdx6500TowCfgInt1StartTime = _Cdx6500TowCfgInt1StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 3),
    _Cdx6500TowCfgInt1StartTime_Type()
)
cdx6500TowCfgInt1StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt1StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt1Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt1Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt1Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt1Duration_Object = MibTableColumn
cdx6500TowCfgInt1Duration = _Cdx6500TowCfgInt1Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 4),
    _Cdx6500TowCfgInt1Duration_Type()
)
cdx6500TowCfgInt1Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt1Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt1StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt1StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt1StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt1StartDays_Object = MibTableColumn
cdx6500TowCfgInt1StartDays = _Cdx6500TowCfgInt1StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 5),
    _Cdx6500TowCfgInt1StartDays_Type()
)
cdx6500TowCfgInt1StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt1StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt2StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt2StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt2StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt2StartTime_Object = MibTableColumn
cdx6500TowCfgInt2StartTime = _Cdx6500TowCfgInt2StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 6),
    _Cdx6500TowCfgInt2StartTime_Type()
)
cdx6500TowCfgInt2StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt2StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt2Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt2Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt2Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt2Duration_Object = MibTableColumn
cdx6500TowCfgInt2Duration = _Cdx6500TowCfgInt2Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 7),
    _Cdx6500TowCfgInt2Duration_Type()
)
cdx6500TowCfgInt2Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt2Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt2StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt2StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt2StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt2StartDays_Object = MibTableColumn
cdx6500TowCfgInt2StartDays = _Cdx6500TowCfgInt2StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 8),
    _Cdx6500TowCfgInt2StartDays_Type()
)
cdx6500TowCfgInt2StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt2StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt3StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt3StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt3StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt3StartTime_Object = MibTableColumn
cdx6500TowCfgInt3StartTime = _Cdx6500TowCfgInt3StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 9),
    _Cdx6500TowCfgInt3StartTime_Type()
)
cdx6500TowCfgInt3StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt3StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt3Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt3Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt3Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt3Duration_Object = MibTableColumn
cdx6500TowCfgInt3Duration = _Cdx6500TowCfgInt3Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 10),
    _Cdx6500TowCfgInt3Duration_Type()
)
cdx6500TowCfgInt3Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt3Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt3StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt3StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt3StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt3StartDays_Object = MibTableColumn
cdx6500TowCfgInt3StartDays = _Cdx6500TowCfgInt3StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 11),
    _Cdx6500TowCfgInt3StartDays_Type()
)
cdx6500TowCfgInt3StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt3StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt4StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt4StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt4StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt4StartTime_Object = MibTableColumn
cdx6500TowCfgInt4StartTime = _Cdx6500TowCfgInt4StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 12),
    _Cdx6500TowCfgInt4StartTime_Type()
)
cdx6500TowCfgInt4StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt4StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt4Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt4Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt4Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt4Duration_Object = MibTableColumn
cdx6500TowCfgInt4Duration = _Cdx6500TowCfgInt4Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 13),
    _Cdx6500TowCfgInt4Duration_Type()
)
cdx6500TowCfgInt4Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt4Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt4StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt4StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt4StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt4StartDays_Object = MibTableColumn
cdx6500TowCfgInt4StartDays = _Cdx6500TowCfgInt4StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 14),
    _Cdx6500TowCfgInt4StartDays_Type()
)
cdx6500TowCfgInt4StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt4StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt5StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt5StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt5StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt5StartTime_Object = MibTableColumn
cdx6500TowCfgInt5StartTime = _Cdx6500TowCfgInt5StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 15),
    _Cdx6500TowCfgInt5StartTime_Type()
)
cdx6500TowCfgInt5StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt5StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt5Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt5Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt5Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt5Duration_Object = MibTableColumn
cdx6500TowCfgInt5Duration = _Cdx6500TowCfgInt5Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 16),
    _Cdx6500TowCfgInt5Duration_Type()
)
cdx6500TowCfgInt5Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt5Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt5StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt5StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt5StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt5StartDays_Object = MibTableColumn
cdx6500TowCfgInt5StartDays = _Cdx6500TowCfgInt5StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 17),
    _Cdx6500TowCfgInt5StartDays_Type()
)
cdx6500TowCfgInt5StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt5StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt6StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt6StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt6StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt6StartTime_Object = MibTableColumn
cdx6500TowCfgInt6StartTime = _Cdx6500TowCfgInt6StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 18),
    _Cdx6500TowCfgInt6StartTime_Type()
)
cdx6500TowCfgInt6StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt6StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt6Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt6Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt6Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt6Duration_Object = MibTableColumn
cdx6500TowCfgInt6Duration = _Cdx6500TowCfgInt6Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 19),
    _Cdx6500TowCfgInt6Duration_Type()
)
cdx6500TowCfgInt6Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt6Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt6StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt6StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt6StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt6StartDays_Object = MibTableColumn
cdx6500TowCfgInt6StartDays = _Cdx6500TowCfgInt6StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 20),
    _Cdx6500TowCfgInt6StartDays_Type()
)
cdx6500TowCfgInt6StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt6StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt7StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt7StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt7StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt7StartTime_Object = MibTableColumn
cdx6500TowCfgInt7StartTime = _Cdx6500TowCfgInt7StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 21),
    _Cdx6500TowCfgInt7StartTime_Type()
)
cdx6500TowCfgInt7StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt7StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt7Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt7Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt7Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt7Duration_Object = MibTableColumn
cdx6500TowCfgInt7Duration = _Cdx6500TowCfgInt7Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 22),
    _Cdx6500TowCfgInt7Duration_Type()
)
cdx6500TowCfgInt7Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt7Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt7StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt7StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt7StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt7StartDays_Object = MibTableColumn
cdx6500TowCfgInt7StartDays = _Cdx6500TowCfgInt7StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 23),
    _Cdx6500TowCfgInt7StartDays_Type()
)
cdx6500TowCfgInt7StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt7StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt8StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt8StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt8StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt8StartTime_Object = MibTableColumn
cdx6500TowCfgInt8StartTime = _Cdx6500TowCfgInt8StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 24),
    _Cdx6500TowCfgInt8StartTime_Type()
)
cdx6500TowCfgInt8StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt8StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt8Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt8Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt8Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt8Duration_Object = MibTableColumn
cdx6500TowCfgInt8Duration = _Cdx6500TowCfgInt8Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 25),
    _Cdx6500TowCfgInt8Duration_Type()
)
cdx6500TowCfgInt8Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt8Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt8StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt8StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt8StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt8StartDays_Object = MibTableColumn
cdx6500TowCfgInt8StartDays = _Cdx6500TowCfgInt8StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 26),
    _Cdx6500TowCfgInt8StartDays_Type()
)
cdx6500TowCfgInt8StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt8StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt9StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt9StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt9StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt9StartTime_Object = MibTableColumn
cdx6500TowCfgInt9StartTime = _Cdx6500TowCfgInt9StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 27),
    _Cdx6500TowCfgInt9StartTime_Type()
)
cdx6500TowCfgInt9StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt9StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt9Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt9Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt9Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt9Duration_Object = MibTableColumn
cdx6500TowCfgInt9Duration = _Cdx6500TowCfgInt9Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 28),
    _Cdx6500TowCfgInt9Duration_Type()
)
cdx6500TowCfgInt9Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt9Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt9StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt9StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt9StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt9StartDays_Object = MibTableColumn
cdx6500TowCfgInt9StartDays = _Cdx6500TowCfgInt9StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 29),
    _Cdx6500TowCfgInt9StartDays_Type()
)
cdx6500TowCfgInt9StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt9StartDays.setStatus("mandatory")


class _Cdx6500TowCfgInt10StartTime_Type(DisplayString):
    """Custom type cdx6500TowCfgInt10StartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Cdx6500TowCfgInt10StartTime_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt10StartTime_Object = MibTableColumn
cdx6500TowCfgInt10StartTime = _Cdx6500TowCfgInt10StartTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 30),
    _Cdx6500TowCfgInt10StartTime_Type()
)
cdx6500TowCfgInt10StartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt10StartTime.setStatus("mandatory")


class _Cdx6500TowCfgInt10Duration_Type(DisplayString):
    """Custom type cdx6500TowCfgInt10Duration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cdx6500TowCfgInt10Duration_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt10Duration_Object = MibTableColumn
cdx6500TowCfgInt10Duration = _Cdx6500TowCfgInt10Duration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 31),
    _Cdx6500TowCfgInt10Duration_Type()
)
cdx6500TowCfgInt10Duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt10Duration.setStatus("mandatory")


class _Cdx6500TowCfgInt10StartDays_Type(DisplayString):
    """Custom type cdx6500TowCfgInt10StartDays based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_Cdx6500TowCfgInt10StartDays_Type.__name__ = "DisplayString"
_Cdx6500TowCfgInt10StartDays_Object = MibTableColumn
cdx6500TowCfgInt10StartDays = _Cdx6500TowCfgInt10StartDays_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 22, 1, 32),
    _Cdx6500TowCfgInt10StartDays_Type()
)
cdx6500TowCfgInt10StartDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500TowCfgInt10StartDays.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOW-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500TOWCfgTable": cdx6500TOWCfgTable,
       "cdx6500TOWCfgEntry": cdx6500TOWCfgEntry,
       "cdx6500TowCfgEntryNum": cdx6500TowCfgEntryNum,
       "cdx6500TowCfgEntryName": cdx6500TowCfgEntryName,
       "cdx6500TowCfgInt1StartTime": cdx6500TowCfgInt1StartTime,
       "cdx6500TowCfgInt1Duration": cdx6500TowCfgInt1Duration,
       "cdx6500TowCfgInt1StartDays": cdx6500TowCfgInt1StartDays,
       "cdx6500TowCfgInt2StartTime": cdx6500TowCfgInt2StartTime,
       "cdx6500TowCfgInt2Duration": cdx6500TowCfgInt2Duration,
       "cdx6500TowCfgInt2StartDays": cdx6500TowCfgInt2StartDays,
       "cdx6500TowCfgInt3StartTime": cdx6500TowCfgInt3StartTime,
       "cdx6500TowCfgInt3Duration": cdx6500TowCfgInt3Duration,
       "cdx6500TowCfgInt3StartDays": cdx6500TowCfgInt3StartDays,
       "cdx6500TowCfgInt4StartTime": cdx6500TowCfgInt4StartTime,
       "cdx6500TowCfgInt4Duration": cdx6500TowCfgInt4Duration,
       "cdx6500TowCfgInt4StartDays": cdx6500TowCfgInt4StartDays,
       "cdx6500TowCfgInt5StartTime": cdx6500TowCfgInt5StartTime,
       "cdx6500TowCfgInt5Duration": cdx6500TowCfgInt5Duration,
       "cdx6500TowCfgInt5StartDays": cdx6500TowCfgInt5StartDays,
       "cdx6500TowCfgInt6StartTime": cdx6500TowCfgInt6StartTime,
       "cdx6500TowCfgInt6Duration": cdx6500TowCfgInt6Duration,
       "cdx6500TowCfgInt6StartDays": cdx6500TowCfgInt6StartDays,
       "cdx6500TowCfgInt7StartTime": cdx6500TowCfgInt7StartTime,
       "cdx6500TowCfgInt7Duration": cdx6500TowCfgInt7Duration,
       "cdx6500TowCfgInt7StartDays": cdx6500TowCfgInt7StartDays,
       "cdx6500TowCfgInt8StartTime": cdx6500TowCfgInt8StartTime,
       "cdx6500TowCfgInt8Duration": cdx6500TowCfgInt8Duration,
       "cdx6500TowCfgInt8StartDays": cdx6500TowCfgInt8StartDays,
       "cdx6500TowCfgInt9StartTime": cdx6500TowCfgInt9StartTime,
       "cdx6500TowCfgInt9Duration": cdx6500TowCfgInt9Duration,
       "cdx6500TowCfgInt9StartDays": cdx6500TowCfgInt9StartDays,
       "cdx6500TowCfgInt10StartTime": cdx6500TowCfgInt10StartTime,
       "cdx6500TowCfgInt10Duration": cdx6500TowCfgInt10Duration,
       "cdx6500TowCfgInt10StartDays": cdx6500TowCfgInt10StartDays}
)
