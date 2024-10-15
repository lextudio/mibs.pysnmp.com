# SNMP MIB module (BIANCA-BRICK-CAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-CAPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:22 2024
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

(BitValue,) = mibBuilder.importSymbols(
    "BIANCA-BRICK-PPP-MIB",
    "BitValue")

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



class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Capi_ObjectIdentity = ObjectIdentity
capi = _Capi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 7)
)
_CapiApplTable_Object = MibTable
capiApplTable = _CapiApplTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1)
)
if mibBuilder.loadTexts:
    capiApplTable.setStatus("mandatory")
_CapiApplEntry_Object = MibTableRow
capiApplEntry = _CapiApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1)
)
capiApplEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiApplNumber"),
)
if mibBuilder.loadTexts:
    capiApplEntry.setStatus("mandatory")
_CapiApplNumber_Type = Integer32
_CapiApplNumber_Object = MibTableColumn
capiApplNumber = _CapiApplNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 1),
    _CapiApplNumber_Type()
)
capiApplNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplNumber.setStatus("mandatory")


class _CapiApplVersion_Type(Integer32):
    """Custom type capiApplVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capi11", 1),
          ("capi20", 2))
    )


_CapiApplVersion_Type.__name__ = "Integer32"
_CapiApplVersion_Object = MibTableColumn
capiApplVersion = _CapiApplVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 2),
    _CapiApplVersion_Type()
)
capiApplVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplVersion.setStatus("mandatory")


class _CapiApplByteOrder_Type(Integer32):
    """Custom type capiApplByteOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("big-endian", 2),
          ("little-endian", 1),
          ("undef", 3))
    )


_CapiApplByteOrder_Type.__name__ = "Integer32"
_CapiApplByteOrder_Object = MibTableColumn
capiApplByteOrder = _CapiApplByteOrder_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 3),
    _CapiApplByteOrder_Type()
)
capiApplByteOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplByteOrder.setStatus("mandatory")
_CapiApplRegLevel3Cnt_Type = Integer32
_CapiApplRegLevel3Cnt_Object = MibTableColumn
capiApplRegLevel3Cnt = _CapiApplRegLevel3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 4),
    _CapiApplRegLevel3Cnt_Type()
)
capiApplRegLevel3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplRegLevel3Cnt.setStatus("mandatory")
_CapiApplRegMsgCnt_Type = Integer32
_CapiApplRegMsgCnt_Object = MibTableColumn
capiApplRegMsgCnt = _CapiApplRegMsgCnt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 5),
    _CapiApplRegMsgCnt_Type()
)
capiApplRegMsgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplRegMsgCnt.setStatus("mandatory")
_CapiApplRegDblkCnt_Type = Integer32
_CapiApplRegDblkCnt_Object = MibTableColumn
capiApplRegDblkCnt = _CapiApplRegDblkCnt_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 6),
    _CapiApplRegDblkCnt_Type()
)
capiApplRegDblkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplRegDblkCnt.setStatus("mandatory")
_CapiApplRegDblkSize_Type = Integer32
_CapiApplRegDblkSize_Object = MibTableColumn
capiApplRegDblkSize = _CapiApplRegDblkSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 7),
    _CapiApplRegDblkSize_Type()
)
capiApplRegDblkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplRegDblkSize.setStatus("mandatory")
_CapiApplInfoStr_Type = DisplayString
_CapiApplInfoStr_Object = MibTableColumn
capiApplInfoStr = _CapiApplInfoStr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 1, 1, 8),
    _CapiApplInfoStr_Type()
)
capiApplInfoStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiApplInfoStr.setStatus("mandatory")
_CapiListenTable_Object = MibTable
capiListenTable = _CapiListenTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2)
)
if mibBuilder.loadTexts:
    capiListenTable.setStatus("mandatory")
_CapiListenEntry_Object = MibTableRow
capiListenEntry = _CapiListenEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1)
)
capiListenEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiListenApplication"),
)
if mibBuilder.loadTexts:
    capiListenEntry.setStatus("mandatory")
_CapiListenApplication_Type = Integer32
_CapiListenApplication_Object = MibTableColumn
capiListenApplication = _CapiListenApplication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 1),
    _CapiListenApplication_Type()
)
capiListenApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenApplication.setStatus("mandatory")
_CapiListenController_Type = HexValue
_CapiListenController_Object = MibTableColumn
capiListenController = _CapiListenController_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 2),
    _CapiListenController_Type()
)
capiListenController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenController.setStatus("mandatory")
_CapiListenServiceMask_Type = HexValue
_CapiListenServiceMask_Object = MibTableColumn
capiListenServiceMask = _CapiListenServiceMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 3),
    _CapiListenServiceMask_Type()
)
capiListenServiceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenServiceMask.setStatus("mandatory")
_CapiListenEazMask_Type = HexValue
_CapiListenEazMask_Object = MibTableColumn
capiListenEazMask = _CapiListenEazMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 4),
    _CapiListenEazMask_Type()
)
capiListenEazMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenEazMask.setStatus("mandatory")
_CapiListenInfoMask_Type = HexValue
_CapiListenInfoMask_Object = MibTableColumn
capiListenInfoMask = _CapiListenInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 5),
    _CapiListenInfoMask_Type()
)
capiListenInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenInfoMask.setStatus("mandatory")
_CapiListenCipMask_Type = HexValue
_CapiListenCipMask_Object = MibTableColumn
capiListenCipMask = _CapiListenCipMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 6),
    _CapiListenCipMask_Type()
)
capiListenCipMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenCipMask.setStatus("mandatory")
_CapiListenCipMask2_Type = HexValue
_CapiListenCipMask2_Object = MibTableColumn
capiListenCipMask2 = _CapiListenCipMask2_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 2, 1, 7),
    _CapiListenCipMask2_Type()
)
capiListenCipMask2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiListenCipMask2.setStatus("mandatory")
_CapiPlciTable_Object = MibTable
capiPlciTable = _CapiPlciTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3)
)
if mibBuilder.loadTexts:
    capiPlciTable.setStatus("mandatory")
_CapiPlciEntry_Object = MibTableRow
capiPlciEntry = _CapiPlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1)
)
capiPlciEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiPlciNumber"),
)
if mibBuilder.loadTexts:
    capiPlciEntry.setStatus("mandatory")
_CapiPlciNumber_Type = HexValue
_CapiPlciNumber_Object = MibTableColumn
capiPlciNumber = _CapiPlciNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 1),
    _CapiPlciNumber_Type()
)
capiPlciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciNumber.setStatus("mandatory")
_CapiPlciApplication_Type = Integer32
_CapiPlciApplication_Object = MibTableColumn
capiPlciApplication = _CapiPlciApplication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 2),
    _CapiPlciApplication_Type()
)
capiPlciApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciApplication.setStatus("mandatory")
_CapiPlciController_Type = HexValue
_CapiPlciController_Object = MibTableColumn
capiPlciController = _CapiPlciController_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 3),
    _CapiPlciController_Type()
)
capiPlciController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciController.setStatus("mandatory")


class _CapiPlciState_Type(Integer32):
    """Custom type capiPlciState based on Integer32"""
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
        *(("p-0", 1),
          ("p-1", 2),
          ("p-2", 3),
          ("p-3", 4),
          ("p-4", 5),
          ("p-5", 6),
          ("p-6", 7),
          ("p-7", 8),
          ("p-act", 9))
    )


_CapiPlciState_Type.__name__ = "Integer32"
_CapiPlciState_Object = MibTableColumn
capiPlciState = _CapiPlciState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 4),
    _CapiPlciState_Type()
)
capiPlciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciState.setStatus("mandatory")


class _CapiPlciSelectB2Proto_Type(Integer32):
    """Custom type capiPlciSelectB2Proto based on Integer32"""
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
              9,
              10,
              11,
              12,
              241,
              242)
        )
    )
    namedValues = NamedValues(
        *(("fax", 7),
          ("hdlccrc", 3),
          ("lapd", 8),
          ("modem", 241),
          ("sdlc", 5),
          ("trans", 4),
          ("txonly", 12),
          ("undef", 1),
          ("v110sdlc", 10),
          ("v110sync", 242),
          ("v110trans", 9),
          ("v110x75", 11),
          ("x75", 2),
          ("x75btx", 6))
    )


_CapiPlciSelectB2Proto_Type.__name__ = "Integer32"
_CapiPlciSelectB2Proto_Object = MibTableColumn
capiPlciSelectB2Proto = _CapiPlciSelectB2Proto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 5),
    _CapiPlciSelectB2Proto_Type()
)
capiPlciSelectB2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciSelectB2Proto.setStatus("mandatory")
_CapiPlciSelectB2Dlpd_Type = OctetString
_CapiPlciSelectB2Dlpd_Object = MibTableColumn
capiPlciSelectB2Dlpd = _CapiPlciSelectB2Dlpd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 6),
    _CapiPlciSelectB2Dlpd_Type()
)
capiPlciSelectB2Dlpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciSelectB2Dlpd.setStatus("mandatory")


class _CapiPlciSelectB3Proto_Type(Integer32):
    """Custom type capiPlciSelectB3Proto based on Integer32"""
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
        *(("iso8208", 3),
          ("t30", 6),
          ("t70nl", 2),
          ("t90", 4),
          ("trans", 5),
          ("undef", 1))
    )


_CapiPlciSelectB3Proto_Type.__name__ = "Integer32"
_CapiPlciSelectB3Proto_Object = MibTableColumn
capiPlciSelectB3Proto = _CapiPlciSelectB3Proto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 7),
    _CapiPlciSelectB3Proto_Type()
)
capiPlciSelectB3Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciSelectB3Proto.setStatus("mandatory")
_CapiPlciSelectB3Ncpd_Type = OctetString
_CapiPlciSelectB3Ncpd_Object = MibTableColumn
capiPlciSelectB3Ncpd = _CapiPlciSelectB3Ncpd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 8),
    _CapiPlciSelectB3Ncpd_Type()
)
capiPlciSelectB3Ncpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciSelectB3Ncpd.setStatus("mandatory")


class _CapiPlciB1Proto_Type(Integer32):
    """Custom type capiPlciB1Proto based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("faxg3", 6),
          ("hdlc", 2),
          ("hdlc56", 8),
          ("hdlcinv", 7),
          ("modemasync", 10),
          ("modemneg", 9),
          ("modemsync", 11),
          ("trans", 3),
          ("undef", 1),
          ("v110hdlc", 5),
          ("v110trans", 4))
    )


_CapiPlciB1Proto_Type.__name__ = "Integer32"
_CapiPlciB1Proto_Object = MibTableColumn
capiPlciB1Proto = _CapiPlciB1Proto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 9),
    _CapiPlciB1Proto_Type()
)
capiPlciB1Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB1Proto.setStatus("mandatory")
_CapiPlciB1Config_Type = OctetString
_CapiPlciB1Config_Object = MibTableColumn
capiPlciB1Config = _CapiPlciB1Config_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 10),
    _CapiPlciB1Config_Type()
)
capiPlciB1Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB1Config.setStatus("mandatory")


class _CapiPlciB2Proto_Type(Integer32):
    """Custom type capiPlciB2Proto based on Integer32"""
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
        *(("lapd", 5),
          ("modem", 9),
          ("ppp", 7),
          ("sdlc", 4),
          ("t30", 6),
          ("trans", 3),
          ("transerr", 8),
          ("undef", 1),
          ("x75", 2))
    )


_CapiPlciB2Proto_Type.__name__ = "Integer32"
_CapiPlciB2Proto_Object = MibTableColumn
capiPlciB2Proto = _CapiPlciB2Proto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 11),
    _CapiPlciB2Proto_Type()
)
capiPlciB2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB2Proto.setStatus("mandatory")
_CapiPlciB2Config_Type = OctetString
_CapiPlciB2Config_Object = MibTableColumn
capiPlciB2Config = _CapiPlciB2Config_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 12),
    _CapiPlciB2Config_Type()
)
capiPlciB2Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB2Config.setStatus("mandatory")


class _CapiPlciB3Proto_Type(Integer32):
    """Custom type capiPlciB3Proto based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("iso8208", 4),
          ("modem", 9),
          ("t30", 6),
          ("t30ext", 7),
          ("t90", 3),
          ("trans", 2),
          ("undef", 1),
          ("x25dce", 5))
    )


_CapiPlciB3Proto_Type.__name__ = "Integer32"
_CapiPlciB3Proto_Object = MibTableColumn
capiPlciB3Proto = _CapiPlciB3Proto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 13),
    _CapiPlciB3Proto_Type()
)
capiPlciB3Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB3Proto.setStatus("mandatory")
_CapiPlciB3Config_Type = OctetString
_CapiPlciB3Config_Object = MibTableColumn
capiPlciB3Config = _CapiPlciB3Config_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 14),
    _CapiPlciB3Config_Type()
)
capiPlciB3Config.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciB3Config.setStatus("mandatory")
_CapiPlciCipValue_Type = Integer32
_CapiPlciCipValue_Object = MibTableColumn
capiPlciCipValue = _CapiPlciCipValue_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 15),
    _CapiPlciCipValue_Type()
)
capiPlciCipValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciCipValue.setStatus("mandatory")
_CapiPlciInfoMask_Type = HexValue
_CapiPlciInfoMask_Object = MibTableColumn
capiPlciInfoMask = _CapiPlciInfoMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 3, 1, 16),
    _CapiPlciInfoMask_Type()
)
capiPlciInfoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiPlciInfoMask.setStatus("mandatory")
_CapiNcciTable_Object = MibTable
capiNcciTable = _CapiNcciTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4)
)
if mibBuilder.loadTexts:
    capiNcciTable.setStatus("mandatory")
_CapiNcciEntry_Object = MibTableRow
capiNcciEntry = _CapiNcciEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4, 1)
)
capiNcciEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiNcciNumber"),
)
if mibBuilder.loadTexts:
    capiNcciEntry.setStatus("mandatory")
_CapiNcciNumber_Type = HexValue
_CapiNcciNumber_Object = MibTableColumn
capiNcciNumber = _CapiNcciNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4, 1, 1),
    _CapiNcciNumber_Type()
)
capiNcciNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiNcciNumber.setStatus("mandatory")
_CapiNcciApplication_Type = Integer32
_CapiNcciApplication_Object = MibTableColumn
capiNcciApplication = _CapiNcciApplication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4, 1, 2),
    _CapiNcciApplication_Type()
)
capiNcciApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiNcciApplication.setStatus("mandatory")
_CapiNcciPlci_Type = HexValue
_CapiNcciPlci_Object = MibTableColumn
capiNcciPlci = _CapiNcciPlci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4, 1, 3),
    _CapiNcciPlci_Type()
)
capiNcciPlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiNcciPlci.setStatus("mandatory")


class _CapiNcciState_Type(Integer32):
    """Custom type capiNcciState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("n-0", 1),
          ("n-1", 2),
          ("n-2", 3),
          ("n-3", 4),
          ("n-4", 5),
          ("n-5", 6),
          ("n-act", 7))
    )


_CapiNcciState_Type.__name__ = "Integer32"
_CapiNcciState_Object = MibTableColumn
capiNcciState = _CapiNcciState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 4, 1, 4),
    _CapiNcciState_Type()
)
capiNcciState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiNcciState.setStatus("mandatory")
_CapiInfoTable_Object = MibTable
capiInfoTable = _CapiInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5)
)
if mibBuilder.loadTexts:
    capiInfoTable.setStatus("mandatory")
_CapiInfoEntry_Object = MibTableRow
capiInfoEntry = _CapiInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1)
)
capiInfoEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiInfoApplication"),
)
if mibBuilder.loadTexts:
    capiInfoEntry.setStatus("mandatory")
_CapiInfoApplication_Type = Integer32
_CapiInfoApplication_Object = MibTableColumn
capiInfoApplication = _CapiInfoApplication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 1),
    _CapiInfoApplication_Type()
)
capiInfoApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoApplication.setStatus("mandatory")
_CapiInfoPlci_Type = HexValue
_CapiInfoPlci_Object = MibTableColumn
capiInfoPlci = _CapiInfoPlci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 2),
    _CapiInfoPlci_Type()
)
capiInfoPlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoPlci.setStatus("mandatory")
_CapiInfoNcci_Type = HexValue
_CapiInfoNcci_Object = MibTableColumn
capiInfoNcci = _CapiInfoNcci_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 3),
    _CapiInfoNcci_Type()
)
capiInfoNcci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoNcci.setStatus("mandatory")


class _CapiInfoC1Command_Type(Integer32):
    """Custom type capiInfoC1Command based on Integer32"""
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
              9,
              10,
              64,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135)
        )
    )
    namedValues = NamedValues(
        *(("b3param", 133),
          ("conact", 3),
          ("conb3", 130),
          ("conb3act", 131),
          ("connect", 2),
          ("conninfo", 9),
          ("data", 8),
          ("datab3", 134),
          ("disc", 4),
          ("discb3", 132),
          ("dtmf", 10),
          ("handset", 135),
          ("info", 7),
          ("listen", 5),
          ("listenb3", 129),
          ("param", 6),
          ("resetb3", 1),
          ("selb2", 64),
          ("selb3", 128))
    )


_CapiInfoC1Command_Type.__name__ = "Integer32"
_CapiInfoC1Command_Object = MibTableColumn
capiInfoC1Command = _CapiInfoC1Command_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 4),
    _CapiInfoC1Command_Type()
)
capiInfoC1Command.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoC1Command.setStatus("mandatory")


class _CapiInfoC2Command_Type(Integer32):
    """Custom type capiInfoC2Command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              65,
              128,
              130,
              131,
              132,
              134,
              135,
              136,
              255)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("conact", 3),
          ("conb3", 130),
          ("conb3act", 131),
          ("conb3t90", 136),
          ("connect", 2),
          ("datab3", 134),
          ("disc", 4),
          ("discb3", 132),
          ("facility", 128),
          ("info", 8),
          ("listen", 5),
          ("manufact", 255),
          ("resetb3", 135),
          ("selectb", 65))
    )


_CapiInfoC2Command_Type.__name__ = "Integer32"
_CapiInfoC2Command_Object = MibTableColumn
capiInfoC2Command = _CapiInfoC2Command_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 5),
    _CapiInfoC2Command_Type()
)
capiInfoC2Command.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoC2Command.setStatus("mandatory")


class _CapiInfoSubCommand_Type(Integer32):
    """Custom type capiInfoSubCommand based on Integer32"""
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
        *(("conf", 2),
          ("ind", 3),
          ("req", 1),
          ("resp", 4))
    )


_CapiInfoSubCommand_Type.__name__ = "Integer32"
_CapiInfoSubCommand_Object = MibTableColumn
capiInfoSubCommand = _CapiInfoSubCommand_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 6),
    _CapiInfoSubCommand_Type()
)
capiInfoSubCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoSubCommand.setStatus("mandatory")
_CapiInfoNumber_Type = HexValue
_CapiInfoNumber_Object = MibTableColumn
capiInfoNumber = _CapiInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 5, 1, 7),
    _CapiInfoNumber_Type()
)
capiInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiInfoNumber.setStatus("mandatory")
_CapiConfigTable_Object = MibTable
capiConfigTable = _CapiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6)
)
if mibBuilder.loadTexts:
    capiConfigTable.setStatus("mandatory")
_CapiConfigEntry_Object = MibTableRow
capiConfigEntry = _CapiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1)
)
capiConfigEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiConfigStkNumber"),
)
if mibBuilder.loadTexts:
    capiConfigEntry.setStatus("mandatory")


class _CapiConfigStkNumber_Type(Integer32):
    """Custom type capiConfigStkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CapiConfigStkNumber_Type.__name__ = "Integer32"
_CapiConfigStkNumber_Object = MibTableColumn
capiConfigStkNumber = _CapiConfigStkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 1),
    _CapiConfigStkNumber_Type()
)
capiConfigStkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capiConfigStkNumber.setStatus("mandatory")


class _CapiConfigFaxG3RcvSpeed_Type(Integer32):
    """Custom type capiConfigFaxG3RcvSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delete", 7),
          ("maximum", 5),
          ("not-available", 6),
          ("r14400", 4),
          ("r4800", 1),
          ("r7200", 2),
          ("r9600", 3))
    )


_CapiConfigFaxG3RcvSpeed_Type.__name__ = "Integer32"
_CapiConfigFaxG3RcvSpeed_Object = MibTableColumn
capiConfigFaxG3RcvSpeed = _CapiConfigFaxG3RcvSpeed_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 2),
    _CapiConfigFaxG3RcvSpeed_Type()
)
capiConfigFaxG3RcvSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFaxG3RcvSpeed.setStatus("mandatory")


class _CapiConfigFaxG3ECM_Type(Integer32):
    """Custom type capiConfigFaxG3ECM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 3),
          ("off", 2),
          ("on", 1))
    )


_CapiConfigFaxG3ECM_Type.__name__ = "Integer32"
_CapiConfigFaxG3ECM_Object = MibTableColumn
capiConfigFaxG3ECM = _CapiConfigFaxG3ECM_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 3),
    _CapiConfigFaxG3ECM_Type()
)
capiConfigFaxG3ECM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFaxG3ECM.setStatus("mandatory")


class _CapiConfigFaxG3Header_Type(Integer32):
    """Custom type capiConfigFaxG3Header based on Integer32"""
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
        *(("logo-header", 1),
          ("no-header", 3),
          ("no-logo", 2),
          ("not-available", 4))
    )


_CapiConfigFaxG3Header_Type.__name__ = "Integer32"
_CapiConfigFaxG3Header_Object = MibTableColumn
capiConfigFaxG3Header = _CapiConfigFaxG3Header_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 4),
    _CapiConfigFaxG3Header_Type()
)
capiConfigFaxG3Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFaxG3Header.setStatus("mandatory")


class _CapiConfigVoiceCoding_Type(Integer32):
    """Custom type capiConfigVoiceCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reverse", 2))
    )


_CapiConfigVoiceCoding_Type.__name__ = "Integer32"
_CapiConfigVoiceCoding_Object = MibTableColumn
capiConfigVoiceCoding = _CapiConfigVoiceCoding_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 5),
    _CapiConfigVoiceCoding_Type()
)
capiConfigVoiceCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigVoiceCoding.setStatus("mandatory")


class _CapiConfigSendAlerting_Type(Integer32):
    """Custom type capiConfigSendAlerting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ever", 2),
          ("never", 1),
          ("voice-only", 3))
    )


_CapiConfigSendAlerting_Type.__name__ = "Integer32"
_CapiConfigSendAlerting_Object = MibTableColumn
capiConfigSendAlerting = _CapiConfigSendAlerting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 6),
    _CapiConfigSendAlerting_Type()
)
capiConfigSendAlerting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigSendAlerting.setStatus("mandatory")


class _CapiConfigV42bis_Type(Integer32):
    """Custom type capiConfigV42bis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 3),
          ("off", 2),
          ("on", 1))
    )


_CapiConfigV42bis_Type.__name__ = "Integer32"
_CapiConfigV42bis_Object = MibTableColumn
capiConfigV42bis = _CapiConfigV42bis_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 7),
    _CapiConfigV42bis_Type()
)
capiConfigV42bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigV42bis.setStatus("mandatory")


class _CapiConfigModemDefault_Type(Integer32):
    """Custom type capiConfigModemDefault based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("modem-profile-1", 1),
          ("modem-profile-2", 2),
          ("modem-profile-3", 3),
          ("modem-profile-4", 4),
          ("modem-profile-5", 5),
          ("modem-profile-6", 6),
          ("modem-profile-7", 7),
          ("modem-profile-8", 8))
    )


_CapiConfigModemDefault_Type.__name__ = "Integer32"
_CapiConfigModemDefault_Object = MibTableColumn
capiConfigModemDefault = _CapiConfigModemDefault_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 8),
    _CapiConfigModemDefault_Type()
)
capiConfigModemDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigModemDefault.setStatus("mandatory")


class _CapiConfigFaxModulation_Type(Integer32):
    """Custom type capiConfigFaxModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("v17", 1),
          ("v17s", 5),
          ("v29", 3),
          ("v33", 2),
          ("v33s", 6))
    )


_CapiConfigFaxModulation_Type.__name__ = "Integer32"
_CapiConfigFaxModulation_Object = MibTableColumn
capiConfigFaxModulation = _CapiConfigFaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 9),
    _CapiConfigFaxModulation_Type()
)
capiConfigFaxModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFaxModulation.setStatus("mandatory")


class _CapiConfigFax12000_Type(Integer32):
    """Custom type capiConfigFax12000 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CapiConfigFax12000_Type.__name__ = "Integer32"
_CapiConfigFax12000_Object = MibTableColumn
capiConfigFax12000 = _CapiConfigFax12000_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 10),
    _CapiConfigFax12000_Type()
)
capiConfigFax12000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFax12000.setStatus("mandatory")


class _CapiConfigFaxTXLevel_Type(Integer32):
    """Custom type capiConfigFaxTXLevel based on Integer32"""
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
        *(("db0", 1),
          ("db12", 5),
          ("db15", 6),
          ("db3", 2),
          ("db6", 3),
          ("db9", 4))
    )


_CapiConfigFaxTXLevel_Type.__name__ = "Integer32"
_CapiConfigFaxTXLevel_Object = MibTableColumn
capiConfigFaxTXLevel = _CapiConfigFaxTXLevel_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 6, 1, 11),
    _CapiConfigFaxTXLevel_Type()
)
capiConfigFaxTXLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiConfigFaxTXLevel.setStatus("mandatory")
_CapiMultiControllerTable_Object = MibTable
capiMultiControllerTable = _CapiMultiControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 7)
)
if mibBuilder.loadTexts:
    capiMultiControllerTable.setStatus("mandatory")
_CapiMultiControllerEntry_Object = MibTableRow
capiMultiControllerEntry = _CapiMultiControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 7, 1)
)
capiMultiControllerEntry.setIndexNames(
    (0, "BIANCA-BRICK-CAPI-MIB", "capiControllerNumber"),
)
if mibBuilder.loadTexts:
    capiMultiControllerEntry.setStatus("mandatory")


class _CapiControllerNumber_Type(Integer32):
    """Custom type capiControllerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CapiControllerNumber_Type.__name__ = "Integer32"
_CapiControllerNumber_Object = MibTableColumn
capiControllerNumber = _CapiControllerNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 7, 1, 1),
    _CapiControllerNumber_Type()
)
capiControllerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiControllerNumber.setStatus("mandatory")
_CapiControllerStkMask_Type = BitValue
_CapiControllerStkMask_Object = MibTableColumn
capiControllerStkMask = _CapiControllerStkMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 7, 1, 2),
    _CapiControllerStkMask_Type()
)
capiControllerStkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiControllerStkMask.setStatus("mandatory")


class _CapiControllerVersion_Type(Integer32):
    """Custom type capiControllerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capi11", 1),
          ("capi20", 2),
          ("delete", 3))
    )


_CapiControllerVersion_Type.__name__ = "Integer32"
_CapiControllerVersion_Object = MibTableColumn
capiControllerVersion = _CapiControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 7, 7, 1, 3),
    _CapiControllerVersion_Type()
)
capiControllerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    capiControllerVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-CAPI-MIB",
    **{"HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "capi": capi,
       "capiApplTable": capiApplTable,
       "capiApplEntry": capiApplEntry,
       "capiApplNumber": capiApplNumber,
       "capiApplVersion": capiApplVersion,
       "capiApplByteOrder": capiApplByteOrder,
       "capiApplRegLevel3Cnt": capiApplRegLevel3Cnt,
       "capiApplRegMsgCnt": capiApplRegMsgCnt,
       "capiApplRegDblkCnt": capiApplRegDblkCnt,
       "capiApplRegDblkSize": capiApplRegDblkSize,
       "capiApplInfoStr": capiApplInfoStr,
       "capiListenTable": capiListenTable,
       "capiListenEntry": capiListenEntry,
       "capiListenApplication": capiListenApplication,
       "capiListenController": capiListenController,
       "capiListenServiceMask": capiListenServiceMask,
       "capiListenEazMask": capiListenEazMask,
       "capiListenInfoMask": capiListenInfoMask,
       "capiListenCipMask": capiListenCipMask,
       "capiListenCipMask2": capiListenCipMask2,
       "capiPlciTable": capiPlciTable,
       "capiPlciEntry": capiPlciEntry,
       "capiPlciNumber": capiPlciNumber,
       "capiPlciApplication": capiPlciApplication,
       "capiPlciController": capiPlciController,
       "capiPlciState": capiPlciState,
       "capiPlciSelectB2Proto": capiPlciSelectB2Proto,
       "capiPlciSelectB2Dlpd": capiPlciSelectB2Dlpd,
       "capiPlciSelectB3Proto": capiPlciSelectB3Proto,
       "capiPlciSelectB3Ncpd": capiPlciSelectB3Ncpd,
       "capiPlciB1Proto": capiPlciB1Proto,
       "capiPlciB1Config": capiPlciB1Config,
       "capiPlciB2Proto": capiPlciB2Proto,
       "capiPlciB2Config": capiPlciB2Config,
       "capiPlciB3Proto": capiPlciB3Proto,
       "capiPlciB3Config": capiPlciB3Config,
       "capiPlciCipValue": capiPlciCipValue,
       "capiPlciInfoMask": capiPlciInfoMask,
       "capiNcciTable": capiNcciTable,
       "capiNcciEntry": capiNcciEntry,
       "capiNcciNumber": capiNcciNumber,
       "capiNcciApplication": capiNcciApplication,
       "capiNcciPlci": capiNcciPlci,
       "capiNcciState": capiNcciState,
       "capiInfoTable": capiInfoTable,
       "capiInfoEntry": capiInfoEntry,
       "capiInfoApplication": capiInfoApplication,
       "capiInfoPlci": capiInfoPlci,
       "capiInfoNcci": capiInfoNcci,
       "capiInfoC1Command": capiInfoC1Command,
       "capiInfoC2Command": capiInfoC2Command,
       "capiInfoSubCommand": capiInfoSubCommand,
       "capiInfoNumber": capiInfoNumber,
       "capiConfigTable": capiConfigTable,
       "capiConfigEntry": capiConfigEntry,
       "capiConfigStkNumber": capiConfigStkNumber,
       "capiConfigFaxG3RcvSpeed": capiConfigFaxG3RcvSpeed,
       "capiConfigFaxG3ECM": capiConfigFaxG3ECM,
       "capiConfigFaxG3Header": capiConfigFaxG3Header,
       "capiConfigVoiceCoding": capiConfigVoiceCoding,
       "capiConfigSendAlerting": capiConfigSendAlerting,
       "capiConfigV42bis": capiConfigV42bis,
       "capiConfigModemDefault": capiConfigModemDefault,
       "capiConfigFaxModulation": capiConfigFaxModulation,
       "capiConfigFax12000": capiConfigFax12000,
       "capiConfigFaxTXLevel": capiConfigFaxTXLevel,
       "capiMultiControllerTable": capiMultiControllerTable,
       "capiMultiControllerEntry": capiMultiControllerEntry,
       "capiControllerNumber": capiControllerNumber,
       "capiControllerStkMask": capiControllerStkMask,
       "capiControllerVersion": capiControllerVersion}
)
