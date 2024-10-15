# SNMP MIB module (CT-PIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-PIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:19 2024
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

(ctPIC,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPIC")

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

_Pic_ObjectIdentity = ObjectIdentity
pic = _Pic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1)
)
_CtPicNumberEntries_Type = Gauge32
_CtPicNumberEntries_Object = MibScalar
ctPicNumberEntries = _CtPicNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 1),
    _CtPicNumberEntries_Type()
)
ctPicNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicNumberEntries.setStatus("mandatory")
_CtPicTable_Object = MibTable
ctPicTable = _CtPicTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    ctPicTable.setStatus("mandatory")
_CtPicEntry_Object = MibTableRow
ctPicEntry = _CtPicEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1)
)
ctPicEntry.setIndexNames(
    (0, "CT-PIC-MIB", "ctPicSlot"),
    (0, "CT-PIC-MIB", "ctPicIndex"),
)
if mibBuilder.loadTexts:
    ctPicEntry.setStatus("mandatory")
_CtPicSlot_Type = Integer32
_CtPicSlot_Object = MibTableColumn
ctPicSlot = _CtPicSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 1),
    _CtPicSlot_Type()
)
ctPicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicSlot.setStatus("mandatory")
_CtPicIndex_Type = Integer32
_CtPicIndex_Object = MibTableColumn
ctPicIndex = _CtPicIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 2),
    _CtPicIndex_Type()
)
ctPicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicIndex.setStatus("mandatory")
_CtPicLocation_Type = ObjectIdentifier
_CtPicLocation_Object = MibTableColumn
ctPicLocation = _CtPicLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 3),
    _CtPicLocation_Type()
)
ctPicLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicLocation.setStatus("mandatory")


class _CtPicStatus_Type(Integer32):
    """Custom type ctPicStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("checkSum", 4),
          ("error", 5),
          ("limited", 6),
          ("notPresent", 3),
          ("other", 1),
          ("present", 2))
    )


_CtPicStatus_Type.__name__ = "Integer32"
_CtPicStatus_Object = MibTableColumn
ctPicStatus = _CtPicStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 4),
    _CtPicStatus_Type()
)
ctPicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicStatus.setStatus("mandatory")


class _CtPicVersion_Type(DisplayString):
    """Custom type ctPicVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicVersion_Type.__name__ = "DisplayString"
_CtPicVersion_Object = MibTableColumn
ctPicVersion = _CtPicVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 5),
    _CtPicVersion_Type()
)
ctPicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicVersion.setStatus("mandatory")
_CtPicModuleType_Type = ObjectIdentifier
_CtPicModuleType_Object = MibTableColumn
ctPicModuleType = _CtPicModuleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 6),
    _CtPicModuleType_Type()
)
ctPicModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicModuleType.setStatus("mandatory")


class _CtPicMfgPN_Type(DisplayString):
    """Custom type ctPicMfgPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_CtPicMfgPN_Type.__name__ = "DisplayString"
_CtPicMfgPN_Object = MibTableColumn
ctPicMfgPN = _CtPicMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 7),
    _CtPicMfgPN_Type()
)
ctPicMfgPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgPN.setStatus("mandatory")


class _CtPicMfgSN_Type(DisplayString):
    """Custom type ctPicMfgSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicMfgSN_Type.__name__ = "DisplayString"
_CtPicMfgSN_Object = MibTableColumn
ctPicMfgSN = _CtPicMfgSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 8),
    _CtPicMfgSN_Type()
)
ctPicMfgSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgSN.setStatus("mandatory")


class _CtPicMfgPartNumb_Type(DisplayString):
    """Custom type ctPicMfgPartNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CtPicMfgPartNumb_Type.__name__ = "DisplayString"
_CtPicMfgPartNumb_Object = MibTableColumn
ctPicMfgPartNumb = _CtPicMfgPartNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 9),
    _CtPicMfgPartNumb_Type()
)
ctPicMfgPartNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgPartNumb.setStatus("mandatory")


class _CtPicMfgSerialNumb_Type(DisplayString):
    """Custom type ctPicMfgSerialNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtPicMfgSerialNumb_Type.__name__ = "DisplayString"
_CtPicMfgSerialNumb_Object = MibTableColumn
ctPicMfgSerialNumb = _CtPicMfgSerialNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 10),
    _CtPicMfgSerialNumb_Type()
)
ctPicMfgSerialNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgSerialNumb.setStatus("mandatory")


class _CtPicMfgReworkLocation_Type(DisplayString):
    """Custom type ctPicMfgReworkLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicMfgReworkLocation_Type.__name__ = "DisplayString"
_CtPicMfgReworkLocation_Object = MibTableColumn
ctPicMfgReworkLocation = _CtPicMfgReworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 11),
    _CtPicMfgReworkLocation_Type()
)
ctPicMfgReworkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgReworkLocation.setStatus("mandatory")


class _CtPicMfgMfgLocation_Type(DisplayString):
    """Custom type ctPicMfgMfgLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicMfgMfgLocation_Type.__name__ = "DisplayString"
_CtPicMfgMfgLocation_Object = MibTableColumn
ctPicMfgMfgLocation = _CtPicMfgMfgLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 12),
    _CtPicMfgMfgLocation_Type()
)
ctPicMfgMfgLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgMfgLocation.setStatus("mandatory")


class _CtPicMfgDateCode_Type(DisplayString):
    """Custom type ctPicMfgDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicMfgDateCode_Type.__name__ = "DisplayString"
_CtPicMfgDateCode_Object = MibTableColumn
ctPicMfgDateCode = _CtPicMfgDateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 13),
    _CtPicMfgDateCode_Type()
)
ctPicMfgDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgDateCode.setStatus("mandatory")


class _CtPicMfgRevisionCode_Type(DisplayString):
    """Custom type ctPicMfgRevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicMfgRevisionCode_Type.__name__ = "DisplayString"
_CtPicMfgRevisionCode_Object = MibTableColumn
ctPicMfgRevisionCode = _CtPicMfgRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 14),
    _CtPicMfgRevisionCode_Type()
)
ctPicMfgRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfgRevisionCode.setStatus("mandatory")


class _CtPicTLPN_Type(DisplayString):
    """Custom type ctPicTLPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_CtPicTLPN_Type.__name__ = "DisplayString"
_CtPicTLPN_Object = MibTableColumn
ctPicTLPN = _CtPicTLPN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 15),
    _CtPicTLPN_Type()
)
ctPicTLPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLPN.setStatus("mandatory")


class _CtPicTLSN_Type(DisplayString):
    """Custom type ctPicTLSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicTLSN_Type.__name__ = "DisplayString"
_CtPicTLSN_Object = MibTableColumn
ctPicTLSN = _CtPicTLSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 16),
    _CtPicTLSN_Type()
)
ctPicTLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLSN.setStatus("mandatory")


class _CtPicTLPartNumb_Type(DisplayString):
    """Custom type ctPicTLPartNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_CtPicTLPartNumb_Type.__name__ = "DisplayString"
_CtPicTLPartNumb_Object = MibTableColumn
ctPicTLPartNumb = _CtPicTLPartNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 17),
    _CtPicTLPartNumb_Type()
)
ctPicTLPartNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLPartNumb.setStatus("mandatory")


class _CtPicTLSerialNumb_Type(DisplayString):
    """Custom type ctPicTLSerialNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtPicTLSerialNumb_Type.__name__ = "DisplayString"
_CtPicTLSerialNumb_Object = MibTableColumn
ctPicTLSerialNumb = _CtPicTLSerialNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 18),
    _CtPicTLSerialNumb_Type()
)
ctPicTLSerialNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLSerialNumb.setStatus("mandatory")


class _CtPicTLReworkLocation_Type(DisplayString):
    """Custom type ctPicTLReworkLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicTLReworkLocation_Type.__name__ = "DisplayString"
_CtPicTLReworkLocation_Object = MibTableColumn
ctPicTLReworkLocation = _CtPicTLReworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 19),
    _CtPicTLReworkLocation_Type()
)
ctPicTLReworkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLReworkLocation.setStatus("mandatory")


class _CtPicTLMfgLocation_Type(DisplayString):
    """Custom type ctPicTLMfgLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicTLMfgLocation_Type.__name__ = "DisplayString"
_CtPicTLMfgLocation_Object = MibTableColumn
ctPicTLMfgLocation = _CtPicTLMfgLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 20),
    _CtPicTLMfgLocation_Type()
)
ctPicTLMfgLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLMfgLocation.setStatus("mandatory")


class _CtPicTLDateCode_Type(DisplayString):
    """Custom type ctPicTLDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicTLDateCode_Type.__name__ = "DisplayString"
_CtPicTLDateCode_Object = MibTableColumn
ctPicTLDateCode = _CtPicTLDateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 21),
    _CtPicTLDateCode_Type()
)
ctPicTLDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLDateCode.setStatus("mandatory")


class _CtPicTLRevisionCode_Type(DisplayString):
    """Custom type ctPicTLRevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicTLRevisionCode_Type.__name__ = "DisplayString"
_CtPicTLRevisionCode_Object = MibTableColumn
ctPicTLRevisionCode = _CtPicTLRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 22),
    _CtPicTLRevisionCode_Type()
)
ctPicTLRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTLRevisionCode.setStatus("mandatory")


class _CtPicPcbRevision_Type(DisplayString):
    """Custom type ctPicPcbRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CtPicPcbRevision_Type.__name__ = "DisplayString"
_CtPicPcbRevision_Object = MibTableColumn
ctPicPcbRevision = _CtPicPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 23),
    _CtPicPcbRevision_Type()
)
ctPicPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicPcbRevision.setStatus("mandatory")


class _CtPicMacAddr_Type(OctetString):
    """Custom type ctPicMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CtPicMacAddr_Type.__name__ = "OctetString"
_CtPicMacAddr_Object = MibTableColumn
ctPicMacAddr = _CtPicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 24),
    _CtPicMacAddr_Type()
)
ctPicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMacAddr.setStatus("mandatory")
_CtPicNumbRsvdAddrs_Type = Integer32
_CtPicNumbRsvdAddrs_Object = MibTableColumn
ctPicNumbRsvdAddrs = _CtPicNumbRsvdAddrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 25),
    _CtPicNumbRsvdAddrs_Type()
)
ctPicNumbRsvdAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicNumbRsvdAddrs.setStatus("mandatory")


class _CtPicBoardRevision_Type(DisplayString):
    """Custom type ctPicBoardRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicBoardRevision_Type.__name__ = "DisplayString"
_CtPicBoardRevision_Object = MibTableColumn
ctPicBoardRevision = _CtPicBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 26),
    _CtPicBoardRevision_Type()
)
ctPicBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicBoardRevision.setStatus("mandatory")


class _CtPicModuleTypeString_Type(DisplayString):
    """Custom type ctPicModuleTypeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CtPicModuleTypeString_Type.__name__ = "DisplayString"
_CtPicModuleTypeString_Object = MibTableColumn
ctPicModuleTypeString = _CtPicModuleTypeString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 27),
    _CtPicModuleTypeString_Type()
)
ctPicModuleTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicModuleTypeString.setStatus("mandatory")


class _CtPicDCDCconverterType_Type(DisplayString):
    """Custom type ctPicDCDCconverterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicDCDCconverterType_Type.__name__ = "DisplayString"
_CtPicDCDCconverterType_Object = MibTableColumn
ctPicDCDCconverterType = _CtPicDCDCconverterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 28),
    _CtPicDCDCconverterType_Type()
)
ctPicDCDCconverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDCDCconverterType.setStatus("mandatory")


class _CtPicDCDCconvInputPower_Type(DisplayString):
    """Custom type ctPicDCDCconvInputPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CtPicDCDCconvInputPower_Type.__name__ = "DisplayString"
_CtPicDCDCconvInputPower_Object = MibTableColumn
ctPicDCDCconvInputPower = _CtPicDCDCconvInputPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 29),
    _CtPicDCDCconvInputPower_Type()
)
ctPicDCDCconvInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDCDCconvInputPower.setStatus("mandatory")


class _CtPicSMB1promVersion_Type(DisplayString):
    """Custom type ctPicSMB1promVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CtPicSMB1promVersion_Type.__name__ = "DisplayString"
_CtPicSMB1promVersion_Object = MibTableColumn
ctPicSMB1promVersion = _CtPicSMB1promVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 30),
    _CtPicSMB1promVersion_Type()
)
ctPicSMB1promVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicSMB1promVersion.setStatus("mandatory")


class _CtPicAtmMacAddr_Type(OctetString):
    """Custom type ctPicAtmMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CtPicAtmMacAddr_Type.__name__ = "OctetString"
_CtPicAtmMacAddr_Object = MibTableColumn
ctPicAtmMacAddr = _CtPicAtmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 31),
    _CtPicAtmMacAddr_Type()
)
ctPicAtmMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPicAtmMacAddr.setStatus("mandatory")


class _CtPicOEMVendorId_Type(Integer32):
    """Custom type ctPicOEMVendorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cPQ", 4),
          ("cabletron", 1),
          ("dEC", 3),
          ("enTeraSys", 6),
          ("nEC", 2),
          ("newbridge", 5))
    )


_CtPicOEMVendorId_Type.__name__ = "Integer32"
_CtPicOEMVendorId_Object = MibTableColumn
ctPicOEMVendorId = _CtPicOEMVendorId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 32),
    _CtPicOEMVendorId_Type()
)
ctPicOEMVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicOEMVendorId.setStatus("mandatory")


class _CtPicOEMVendorName_Type(DisplayString):
    """Custom type ctPicOEMVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_CtPicOEMVendorName_Type.__name__ = "DisplayString"
_CtPicOEMVendorName_Object = MibTableColumn
ctPicOEMVendorName = _CtPicOEMVendorName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 33),
    _CtPicOEMVendorName_Type()
)
ctPicOEMVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicOEMVendorName.setStatus("mandatory")


class _CtPicMfg97SN_Type(DisplayString):
    """Custom type ctPicMfg97SN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicMfg97SN_Type.__name__ = "DisplayString"
_CtPicMfg97SN_Object = MibTableColumn
ctPicMfg97SN = _CtPicMfg97SN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 34),
    _CtPicMfg97SN_Type()
)
ctPicMfg97SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfg97SN.setStatus("mandatory")


class _CtPicMfg97DateCode_Type(DisplayString):
    """Custom type ctPicMfg97DateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtPicMfg97DateCode_Type.__name__ = "DisplayString"
_CtPicMfg97DateCode_Object = MibTableColumn
ctPicMfg97DateCode = _CtPicMfg97DateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 35),
    _CtPicMfg97DateCode_Type()
)
ctPicMfg97DateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfg97DateCode.setStatus("mandatory")


class _CtPicMfg97RevisionCode_Type(DisplayString):
    """Custom type ctPicMfg97RevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicMfg97RevisionCode_Type.__name__ = "DisplayString"
_CtPicMfg97RevisionCode_Object = MibTableColumn
ctPicMfg97RevisionCode = _CtPicMfg97RevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 36),
    _CtPicMfg97RevisionCode_Type()
)
ctPicMfg97RevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicMfg97RevisionCode.setStatus("mandatory")


class _CtPicTL97SN_Type(DisplayString):
    """Custom type ctPicTL97SN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicTL97SN_Type.__name__ = "DisplayString"
_CtPicTL97SN_Object = MibTableColumn
ctPicTL97SN = _CtPicTL97SN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 37),
    _CtPicTL97SN_Type()
)
ctPicTL97SN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTL97SN.setStatus("mandatory")


class _CtPicTL97DateCode_Type(DisplayString):
    """Custom type ctPicTL97DateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtPicTL97DateCode_Type.__name__ = "DisplayString"
_CtPicTL97DateCode_Object = MibTableColumn
ctPicTL97DateCode = _CtPicTL97DateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 38),
    _CtPicTL97DateCode_Type()
)
ctPicTL97DateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTL97DateCode.setStatus("mandatory")


class _CtPicTL97RevisionCode_Type(DisplayString):
    """Custom type ctPicTL97RevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CtPicTL97RevisionCode_Type.__name__ = "DisplayString"
_CtPicTL97RevisionCode_Object = MibTableColumn
ctPicTL97RevisionCode = _CtPicTL97RevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 39),
    _CtPicTL97RevisionCode_Type()
)
ctPicTL97RevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicTL97RevisionCode.setStatus("mandatory")


class _CtPicOEMTLSN_Type(DisplayString):
    """Custom type ctPicOEMTLSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CtPicOEMTLSN_Type.__name__ = "DisplayString"
_CtPicOEMTLSN_Object = MibTableColumn
ctPicOEMTLSN = _CtPicOEMTLSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 40),
    _CtPicOEMTLSN_Type()
)
ctPicOEMTLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicOEMTLSN.setStatus("mandatory")
_CtPicECOTable_Object = MibTable
ctPicECOTable = _CtPicECOTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3)
)
if mibBuilder.loadTexts:
    ctPicECOTable.setStatus("mandatory")
_CtPicECOEntry_Object = MibTableRow
ctPicECOEntry = _CtPicECOEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1)
)
ctPicECOEntry.setIndexNames(
    (0, "CT-PIC-MIB", "ctPicECOSlot"),
    (0, "CT-PIC-MIB", "ctPicECOIndex"),
    (0, "CT-PIC-MIB", "ctPicECOID"),
)
if mibBuilder.loadTexts:
    ctPicECOEntry.setStatus("mandatory")
_CtPicECOSlot_Type = Integer32
_CtPicECOSlot_Object = MibTableColumn
ctPicECOSlot = _CtPicECOSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 1),
    _CtPicECOSlot_Type()
)
ctPicECOSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicECOSlot.setStatus("mandatory")
_CtPicECOIndex_Type = Integer32
_CtPicECOIndex_Object = MibTableColumn
ctPicECOIndex = _CtPicECOIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 2),
    _CtPicECOIndex_Type()
)
ctPicECOIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicECOIndex.setStatus("mandatory")
_CtPicECOID_Type = Integer32
_CtPicECOID_Object = MibTableColumn
ctPicECOID = _CtPicECOID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 3),
    _CtPicECOID_Type()
)
ctPicECOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicECOID.setStatus("mandatory")


class _CtPicECONumber_Type(DisplayString):
    """Custom type ctPicECONumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtPicECONumber_Type.__name__ = "DisplayString"
_CtPicECONumber_Object = MibTableColumn
ctPicECONumber = _CtPicECONumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 4),
    _CtPicECONumber_Type()
)
ctPicECONumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicECONumber.setStatus("mandatory")
_CtPicLocationID_ObjectIdentity = ObjectIdentity
ctPicLocationID = _CtPicLocationID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4)
)
_CtPicLocationModule_ObjectIdentity = ObjectIdentity
ctPicLocationModule = _CtPicLocationModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 1)
)
_CtPicBrim_ObjectIdentity = ObjectIdentity
ctPicBrim = _CtPicBrim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 2)
)
_CtPicChassis_ObjectIdentity = ObjectIdentity
ctPicChassis = _CtPicChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 3)
)
_CtPicDaughter_ObjectIdentity = ObjectIdentity
ctPicDaughter = _CtPicDaughter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 4)
)
_CtPicBackPlane_ObjectIdentity = ObjectIdentity
ctPicBackPlane = _CtPicBackPlane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 5)
)
_CtPicDiagTable_Object = MibTable
ctPicDiagTable = _CtPicDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5)
)
if mibBuilder.loadTexts:
    ctPicDiagTable.setStatus("mandatory")
_CtPicDiagEntry_Object = MibTableRow
ctPicDiagEntry = _CtPicDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1)
)
ctPicDiagEntry.setIndexNames(
    (0, "CT-PIC-MIB", "ctPicDiagSlot"),
    (0, "CT-PIC-MIB", "ctPicDiagIndex"),
    (0, "CT-PIC-MIB", "ctPicDiagID"),
)
if mibBuilder.loadTexts:
    ctPicDiagEntry.setStatus("mandatory")
_CtPicDiagSlot_Type = Integer32
_CtPicDiagSlot_Object = MibTableColumn
ctPicDiagSlot = _CtPicDiagSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 1),
    _CtPicDiagSlot_Type()
)
ctPicDiagSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDiagSlot.setStatus("mandatory")
_CtPicDiagIndex_Type = Integer32
_CtPicDiagIndex_Object = MibTableColumn
ctPicDiagIndex = _CtPicDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 2),
    _CtPicDiagIndex_Type()
)
ctPicDiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDiagIndex.setStatus("mandatory")


class _CtPicDiagID_Type(Integer32):
    """Custom type ctPicDiagID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CtPicDiagID_Type.__name__ = "Integer32"
_CtPicDiagID_Object = MibTableColumn
ctPicDiagID = _CtPicDiagID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 3),
    _CtPicDiagID_Type()
)
ctPicDiagID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDiagID.setStatus("mandatory")


class _CtPicDiagResults_Type(DisplayString):
    """Custom type ctPicDiagResults based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_CtPicDiagResults_Type.__name__ = "DisplayString"
_CtPicDiagResults_Object = MibTableColumn
ctPicDiagResults = _CtPicDiagResults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 4),
    _CtPicDiagResults_Type()
)
ctPicDiagResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicDiagResults.setStatus("mandatory")
_CtPicControlTable_Object = MibTable
ctPicControlTable = _CtPicControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8)
)
if mibBuilder.loadTexts:
    ctPicControlTable.setStatus("mandatory")
_CtPicControlEntry_Object = MibTableRow
ctPicControlEntry = _CtPicControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8, 1)
)
ctPicControlEntry.setIndexNames(
    (0, "CT-PIC-MIB", "ctPicSlot"),
    (0, "CT-PIC-MIB", "ctPicIndex"),
)
if mibBuilder.loadTexts:
    ctPicControlEntry.setStatus("mandatory")


class _CtPicRefresh_Type(Integer32):
    """Custom type ctPicRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reFresh", 1)
    )


_CtPicRefresh_Type.__name__ = "Integer32"
_CtPicRefresh_Object = MibTableColumn
ctPicRefresh = _CtPicRefresh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8, 1, 1),
    _CtPicRefresh_Type()
)
ctPicRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPicRefresh.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-PIC-MIB",
    **{"pic": pic,
       "ctPicNumberEntries": ctPicNumberEntries,
       "ctPicTable": ctPicTable,
       "ctPicEntry": ctPicEntry,
       "ctPicSlot": ctPicSlot,
       "ctPicIndex": ctPicIndex,
       "ctPicLocation": ctPicLocation,
       "ctPicStatus": ctPicStatus,
       "ctPicVersion": ctPicVersion,
       "ctPicModuleType": ctPicModuleType,
       "ctPicMfgPN": ctPicMfgPN,
       "ctPicMfgSN": ctPicMfgSN,
       "ctPicMfgPartNumb": ctPicMfgPartNumb,
       "ctPicMfgSerialNumb": ctPicMfgSerialNumb,
       "ctPicMfgReworkLocation": ctPicMfgReworkLocation,
       "ctPicMfgMfgLocation": ctPicMfgMfgLocation,
       "ctPicMfgDateCode": ctPicMfgDateCode,
       "ctPicMfgRevisionCode": ctPicMfgRevisionCode,
       "ctPicTLPN": ctPicTLPN,
       "ctPicTLSN": ctPicTLSN,
       "ctPicTLPartNumb": ctPicTLPartNumb,
       "ctPicTLSerialNumb": ctPicTLSerialNumb,
       "ctPicTLReworkLocation": ctPicTLReworkLocation,
       "ctPicTLMfgLocation": ctPicTLMfgLocation,
       "ctPicTLDateCode": ctPicTLDateCode,
       "ctPicTLRevisionCode": ctPicTLRevisionCode,
       "ctPicPcbRevision": ctPicPcbRevision,
       "ctPicMacAddr": ctPicMacAddr,
       "ctPicNumbRsvdAddrs": ctPicNumbRsvdAddrs,
       "ctPicBoardRevision": ctPicBoardRevision,
       "ctPicModuleTypeString": ctPicModuleTypeString,
       "ctPicDCDCconverterType": ctPicDCDCconverterType,
       "ctPicDCDCconvInputPower": ctPicDCDCconvInputPower,
       "ctPicSMB1promVersion": ctPicSMB1promVersion,
       "ctPicAtmMacAddr": ctPicAtmMacAddr,
       "ctPicOEMVendorId": ctPicOEMVendorId,
       "ctPicOEMVendorName": ctPicOEMVendorName,
       "ctPicMfg97SN": ctPicMfg97SN,
       "ctPicMfg97DateCode": ctPicMfg97DateCode,
       "ctPicMfg97RevisionCode": ctPicMfg97RevisionCode,
       "ctPicTL97SN": ctPicTL97SN,
       "ctPicTL97DateCode": ctPicTL97DateCode,
       "ctPicTL97RevisionCode": ctPicTL97RevisionCode,
       "ctPicOEMTLSN": ctPicOEMTLSN,
       "ctPicECOTable": ctPicECOTable,
       "ctPicECOEntry": ctPicECOEntry,
       "ctPicECOSlot": ctPicECOSlot,
       "ctPicECOIndex": ctPicECOIndex,
       "ctPicECOID": ctPicECOID,
       "ctPicECONumber": ctPicECONumber,
       "ctPicLocationID": ctPicLocationID,
       "ctPicLocationModule": ctPicLocationModule,
       "ctPicBrim": ctPicBrim,
       "ctPicChassis": ctPicChassis,
       "ctPicDaughter": ctPicDaughter,
       "ctPicBackPlane": ctPicBackPlane,
       "ctPicDiagTable": ctPicDiagTable,
       "ctPicDiagEntry": ctPicDiagEntry,
       "ctPicDiagSlot": ctPicDiagSlot,
       "ctPicDiagIndex": ctPicDiagIndex,
       "ctPicDiagID": ctPicDiagID,
       "ctPicDiagResults": ctPicDiagResults,
       "ctPicControlTable": ctPicControlTable,
       "ctPicControlEntry": ctPicControlEntry,
       "ctPicRefresh": ctPicRefresh}
)
