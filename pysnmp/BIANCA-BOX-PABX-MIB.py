# SNMP MIB module (BIANCA-BOX-PABX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BOX-PABX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:20 2024
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



class Date(Integer32):
    """Custom type Date based on Integer32"""




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
_Pabx_ObjectIdentity = ObjectIdentity
pabx = _Pabx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 20)
)
_PabxUserTable_Object = MibTable
pabxUserTable = _PabxUserTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1)
)
if mibBuilder.loadTexts:
    pabxUserTable.setStatus("mandatory")
_PabxUserEntry_Object = MibTableRow
pabxUserEntry = _PabxUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1)
)
pabxUserEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxUserName"),
)
if mibBuilder.loadTexts:
    pabxUserEntry.setStatus("mandatory")


class _PabxUserName_Type(DisplayString):
    """Custom type pabxUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxUserName_Type.__name__ = "DisplayString"
_PabxUserName_Object = MibTableColumn
pabxUserName = _PabxUserName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 1),
    _PabxUserName_Type()
)
pabxUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserName.setStatus("mandatory")


class _PabxUserPassword_Type(DisplayString):
    """Custom type pabxUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxUserPassword_Type.__name__ = "DisplayString"
_PabxUserPassword_Object = MibTableColumn
pabxUserPassword = _PabxUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 2),
    _PabxUserPassword_Type()
)
pabxUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserPassword.setStatus("mandatory")


class _PabxUserTapiMon_Type(Integer32):
    """Custom type pabxUserTapiMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_PabxUserTapiMon_Type.__name__ = "Integer32"
_PabxUserTapiMon_Object = MibTableColumn
pabxUserTapiMon = _PabxUserTapiMon_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 3),
    _PabxUserTapiMon_Type()
)
pabxUserTapiMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserTapiMon.setStatus("mandatory")


class _PabxUserTapiCtrl_Type(Integer32):
    """Custom type pabxUserTapiCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PabxUserTapiCtrl_Type.__name__ = "Integer32"
_PabxUserTapiCtrl_Object = MibTableColumn
pabxUserTapiCtrl = _PabxUserTapiCtrl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 4),
    _PabxUserTapiCtrl_Type()
)
pabxUserTapiCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserTapiCtrl.setStatus("mandatory")


class _PabxUserTapiMedia_Type(Integer32):
    """Custom type pabxUserTapiMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PabxUserTapiMedia_Type.__name__ = "Integer32"
_PabxUserTapiMedia_Object = MibTableColumn
pabxUserTapiMedia = _PabxUserTapiMedia_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 5),
    _PabxUserTapiMedia_Type()
)
pabxUserTapiMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserTapiMedia.setStatus("mandatory")


class _PabxUserCapi_Type(Integer32):
    """Custom type pabxUserCapi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PabxUserCapi_Type.__name__ = "Integer32"
_PabxUserCapi_Object = MibTableColumn
pabxUserCapi = _PabxUserCapi_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 6),
    _PabxUserCapi_Type()
)
pabxUserCapi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserCapi.setStatus("mandatory")


class _PabxUserId_Type(Integer32):
    """Custom type pabxUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxUserId_Type.__name__ = "Integer32"
_PabxUserId_Object = MibTableColumn
pabxUserId = _PabxUserId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 7),
    _PabxUserId_Type()
)
pabxUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserId.setStatus("mandatory")


class _PabxUserPIN_Type(DisplayString):
    """Custom type pabxUserPIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 9),
    )


_PabxUserPIN_Type.__name__ = "DisplayString"
_PabxUserPIN_Object = MibTableColumn
pabxUserPIN = _PabxUserPIN_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 8),
    _PabxUserPIN_Type()
)
pabxUserPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserPIN.setStatus("mandatory")


class _PabxUserPrimGroupId_Type(Integer32):
    """Custom type pabxUserPrimGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxUserPrimGroupId_Type.__name__ = "Integer32"
_PabxUserPrimGroupId_Object = MibTableColumn
pabxUserPrimGroupId = _PabxUserPrimGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 1, 1, 9),
    _PabxUserPrimGroupId_Type()
)
pabxUserPrimGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxUserPrimGroupId.setStatus("mandatory")
_PabxTrunkTable_Object = MibTable
pabxTrunkTable = _PabxTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2)
)
if mibBuilder.loadTexts:
    pabxTrunkTable.setStatus("mandatory")
_PabxTrunkEntry_Object = MibTableRow
pabxTrunkEntry = _PabxTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1)
)
pabxTrunkEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxTrunkNumber"),
)
if mibBuilder.loadTexts:
    pabxTrunkEntry.setStatus("mandatory")


class _PabxTrunkNumber_Type(Integer32):
    """Custom type pabxTrunkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PabxTrunkNumber_Type.__name__ = "Integer32"
_PabxTrunkNumber_Object = MibTableColumn
pabxTrunkNumber = _PabxTrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 1),
    _PabxTrunkNumber_Type()
)
pabxTrunkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkNumber.setStatus("mandatory")
_PabxTrunkDescr_Type = DisplayString
_PabxTrunkDescr_Object = MibTableColumn
pabxTrunkDescr = _PabxTrunkDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 2),
    _PabxTrunkDescr_Type()
)
pabxTrunkDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkDescr.setStatus("mandatory")


class _PabxTrunkSlot_Type(Integer32):
    """Custom type pabxTrunkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PabxTrunkSlot_Type.__name__ = "Integer32"
_PabxTrunkSlot_Object = MibTableColumn
pabxTrunkSlot = _PabxTrunkSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 3),
    _PabxTrunkSlot_Type()
)
pabxTrunkSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkSlot.setStatus("mandatory")


class _PabxTrunkUnit_Type(Integer32):
    """Custom type pabxTrunkUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_PabxTrunkUnit_Type.__name__ = "Integer32"
_PabxTrunkUnit_Object = MibTableColumn
pabxTrunkUnit = _PabxTrunkUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 4),
    _PabxTrunkUnit_Type()
)
pabxTrunkUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkUnit.setStatus("mandatory")


class _PabxTrunkProtocol_Type(Integer32):
    """Custom type pabxTrunkProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("dss1", 2))
    )


_PabxTrunkProtocol_Type.__name__ = "Integer32"
_PabxTrunkProtocol_Object = MibTableColumn
pabxTrunkProtocol = _PabxTrunkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 5),
    _PabxTrunkProtocol_Type()
)
pabxTrunkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkProtocol.setStatus("mandatory")


class _PabxTrunkConfig_Type(Integer32):
    """Custom type pabxTrunkConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("point-to-multipoint", 1),
          ("point-to-point", 2),
          ("unknown", 3))
    )


_PabxTrunkConfig_Type.__name__ = "Integer32"
_PabxTrunkConfig_Object = MibTableColumn
pabxTrunkConfig = _PabxTrunkConfig_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 6),
    _PabxTrunkConfig_Type()
)
pabxTrunkConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkConfig.setStatus("mandatory")


class _PabxTrunkTeiProc_Type(Integer32):
    """Custom type pabxTrunkTeiProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("fixed", 2))
    )


_PabxTrunkTeiProc_Type.__name__ = "Integer32"
_PabxTrunkTeiProc_Object = MibTableColumn
pabxTrunkTeiProc = _PabxTrunkTeiProc_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 7),
    _PabxTrunkTeiProc_Type()
)
pabxTrunkTeiProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkTeiProc.setStatus("mandatory")


class _PabxTrunkTeiValue_Type(Integer32):
    """Custom type pabxTrunkTeiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PabxTrunkTeiValue_Type.__name__ = "Integer32"
_PabxTrunkTeiValue_Object = MibTableColumn
pabxTrunkTeiValue = _PabxTrunkTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 8),
    _PabxTrunkTeiValue_Type()
)
pabxTrunkTeiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkTeiValue.setStatus("mandatory")
_PabxTrunkCountryCode_Type = DisplayString
_PabxTrunkCountryCode_Object = MibTableColumn
pabxTrunkCountryCode = _PabxTrunkCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 9),
    _PabxTrunkCountryCode_Type()
)
pabxTrunkCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkCountryCode.setStatus("mandatory")
_PabxTrunkAreaCode_Type = DisplayString
_PabxTrunkAreaCode_Object = MibTableColumn
pabxTrunkAreaCode = _PabxTrunkAreaCode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 10),
    _PabxTrunkAreaCode_Type()
)
pabxTrunkAreaCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkAreaCode.setStatus("mandatory")
_PabxTrunkSubscriberNo_Type = DisplayString
_PabxTrunkSubscriberNo_Object = MibTableColumn
pabxTrunkSubscriberNo = _PabxTrunkSubscriberNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 11),
    _PabxTrunkSubscriberNo_Type()
)
pabxTrunkSubscriberNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkSubscriberNo.setStatus("mandatory")
_PabxTrunkExtension_Type = DisplayString
_PabxTrunkExtension_Object = MibTableColumn
pabxTrunkExtension = _PabxTrunkExtension_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 12),
    _PabxTrunkExtension_Type()
)
pabxTrunkExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkExtension.setStatus("mandatory")


class _PabxTrunkType_Type(Integer32):
    """Custom type pabxTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_PabxTrunkType_Type.__name__ = "Integer32"
_PabxTrunkType_Object = MibTableColumn
pabxTrunkType = _PabxTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 13),
    _PabxTrunkType_Type()
)
pabxTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkType.setStatus("mandatory")


class _PabxTrunkL2Mode_Type(Integer32):
    """Custom type pabxTrunkL2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("nt", 3),
          ("te", 2))
    )


_PabxTrunkL2Mode_Type.__name__ = "Integer32"
_PabxTrunkL2Mode_Object = MibTableColumn
pabxTrunkL2Mode = _PabxTrunkL2Mode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 2, 1, 14),
    _PabxTrunkL2Mode_Type()
)
pabxTrunkL2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkL2Mode.setStatus("mandatory")
_PabxTrunkPrefixTable_Object = MibTable
pabxTrunkPrefixTable = _PabxTrunkPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3)
)
if mibBuilder.loadTexts:
    pabxTrunkPrefixTable.setStatus("mandatory")
_PabxTrunkPrefixEntry_Object = MibTableRow
pabxTrunkPrefixEntry = _PabxTrunkPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1)
)
pabxTrunkPrefixEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxTrunkPrefixPrefix"),
)
if mibBuilder.loadTexts:
    pabxTrunkPrefixEntry.setStatus("mandatory")


class _PabxTrunkPrefixPrefix_Type(DisplayString):
    """Custom type pabxTrunkPrefixPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PabxTrunkPrefixPrefix_Type.__name__ = "DisplayString"
_PabxTrunkPrefixPrefix_Object = MibTableColumn
pabxTrunkPrefixPrefix = _PabxTrunkPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1, 1),
    _PabxTrunkPrefixPrefix_Type()
)
pabxTrunkPrefixPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkPrefixPrefix.setStatus("mandatory")
_PabxTrunkPrefixTrunkMask_Type = BitValue
_PabxTrunkPrefixTrunkMask_Object = MibTableColumn
pabxTrunkPrefixTrunkMask = _PabxTrunkPrefixTrunkMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1, 2),
    _PabxTrunkPrefixTrunkMask_Type()
)
pabxTrunkPrefixTrunkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkPrefixTrunkMask.setStatus("mandatory")


class _PabxTrunkPrefixStatus_Type(Integer32):
    """Custom type pabxTrunkPrefixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("invalid", 2),
          ("valid", 1))
    )


_PabxTrunkPrefixStatus_Type.__name__ = "Integer32"
_PabxTrunkPrefixStatus_Object = MibTableColumn
pabxTrunkPrefixStatus = _PabxTrunkPrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1, 3),
    _PabxTrunkPrefixStatus_Type()
)
pabxTrunkPrefixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkPrefixStatus.setStatus("mandatory")


class _PabxTrunkPrefixStripOnOutgoing_Type(Integer32):
    """Custom type pabxTrunkPrefixStripOnOutgoing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PabxTrunkPrefixStripOnOutgoing_Type.__name__ = "Integer32"
_PabxTrunkPrefixStripOnOutgoing_Object = MibTableColumn
pabxTrunkPrefixStripOnOutgoing = _PabxTrunkPrefixStripOnOutgoing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1, 4),
    _PabxTrunkPrefixStripOnOutgoing_Type()
)
pabxTrunkPrefixStripOnOutgoing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkPrefixStripOnOutgoing.setStatus("mandatory")


class _PabxTrunkPrefixPrependOnIncoming_Type(Integer32):
    """Custom type pabxTrunkPrefixPrependOnIncoming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PabxTrunkPrefixPrependOnIncoming_Type.__name__ = "Integer32"
_PabxTrunkPrefixPrependOnIncoming_Object = MibTableColumn
pabxTrunkPrefixPrependOnIncoming = _PabxTrunkPrefixPrependOnIncoming_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 3, 1, 5),
    _PabxTrunkPrefixPrependOnIncoming_Type()
)
pabxTrunkPrefixPrependOnIncoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkPrefixPrependOnIncoming.setStatus("mandatory")
_PabxExtensionTable_Object = MibTable
pabxExtensionTable = _PabxExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4)
)
if mibBuilder.loadTexts:
    pabxExtensionTable.setStatus("mandatory")
_PabxExtensionEntry_Object = MibTableRow
pabxExtensionEntry = _PabxExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1)
)
pabxExtensionEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxExtExtension"),
)
if mibBuilder.loadTexts:
    pabxExtensionEntry.setStatus("mandatory")


class _PabxExtExtension_Type(DisplayString):
    """Custom type pabxExtExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxExtExtension_Type.__name__ = "DisplayString"
_PabxExtExtension_Object = MibTableColumn
pabxExtExtension = _PabxExtExtension_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 1),
    _PabxExtExtension_Type()
)
pabxExtExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtExtension.setStatus("mandatory")


class _PabxExtType_Type(Integer32):
    """Custom type pabxExtType based on Integer32"""
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
        *(("data", 2),
          ("delete", 4),
          ("voice", 1),
          ("voice-and-data", 3))
    )


_PabxExtType_Type.__name__ = "Integer32"
_PabxExtType_Object = MibTableColumn
pabxExtType = _PabxExtType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 2),
    _PabxExtType_Type()
)
pabxExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtType.setStatus("mandatory")
_PabxExtIpAddr_Type = IpAddress
_PabxExtIpAddr_Object = MibTableColumn
pabxExtIpAddr = _PabxExtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 6),
    _PabxExtIpAddr_Type()
)
pabxExtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtIpAddr.setStatus("mandatory")


class _PabxExtEAZ_Type(DisplayString):
    """Custom type pabxExtEAZ based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_PabxExtEAZ_Type.__name__ = "DisplayString"
_PabxExtEAZ_Object = MibTableColumn
pabxExtEAZ = _PabxExtEAZ_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 8),
    _PabxExtEAZ_Type()
)
pabxExtEAZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtEAZ.setStatus("mandatory")


class _PabxExtLayer1Prot_Type(Integer32):
    """Custom type pabxExtLayer1Prot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("modem", 13),
          ("modem-profile-1", 26),
          ("modem-profile-2", 27),
          ("modem-profile-3", 28),
          ("modem-profile-4", 29),
          ("modem-profile-5", 30),
          ("modem-profile-6", 31),
          ("modem-profile-7", 32),
          ("modem-profile-8", 33),
          ("sync-56k", 12),
          ("sync-64k", 11),
          ("v110-1200", 15),
          ("v110-14400", 19),
          ("v110-19200", 20),
          ("v110-2400", 16),
          ("v110-38400", 21),
          ("v110-4800", 17),
          ("v110-9600", 18))
    )


_PabxExtLayer1Prot_Type.__name__ = "Integer32"
_PabxExtLayer1Prot_Object = MibTableColumn
pabxExtLayer1Prot = _PabxExtLayer1Prot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 9),
    _PabxExtLayer1Prot_Type()
)
pabxExtLayer1Prot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtLayer1Prot.setStatus("mandatory")
_PabxExtIfIndex_Type = Integer32
_PabxExtIfIndex_Object = MibTableColumn
pabxExtIfIndex = _PabxExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 10),
    _PabxExtIfIndex_Type()
)
pabxExtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtIfIndex.setStatus("mandatory")


class _PabxExtId_Type(Integer32):
    """Custom type pabxExtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxExtId_Type.__name__ = "Integer32"
_PabxExtId_Object = MibTableColumn
pabxExtId = _PabxExtId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 11),
    _PabxExtId_Type()
)
pabxExtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtId.setStatus("mandatory")


class _PabxExtUserId_Type(Integer32):
    """Custom type pabxExtUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxExtUserId_Type.__name__ = "Integer32"
_PabxExtUserId_Object = MibTableColumn
pabxExtUserId = _PabxExtUserId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 12),
    _PabxExtUserId_Type()
)
pabxExtUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtUserId.setStatus("mandatory")
_PabxExtTermId_Type = Integer32
_PabxExtTermId_Object = MibTableColumn
pabxExtTermId = _PabxExtTermId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 13),
    _PabxExtTermId_Type()
)
pabxExtTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtTermId.setStatus("mandatory")


class _PabxExtDefaultExtFlag_Type(Integer32):
    """Custom type pabxExtDefaultExtFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PabxExtDefaultExtFlag_Type.__name__ = "Integer32"
_PabxExtDefaultExtFlag_Object = MibTableColumn
pabxExtDefaultExtFlag = _PabxExtDefaultExtFlag_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 14),
    _PabxExtDefaultExtFlag_Type()
)
pabxExtDefaultExtFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtDefaultExtFlag.setStatus("mandatory")


class _PabxExtPresentationNr_Type(DisplayString):
    """Custom type pabxExtPresentationNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxExtPresentationNr_Type.__name__ = "DisplayString"
_PabxExtPresentationNr_Object = MibTableColumn
pabxExtPresentationNr = _PabxExtPresentationNr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 15),
    _PabxExtPresentationNr_Type()
)
pabxExtPresentationNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtPresentationNr.setStatus("mandatory")


class _PabxExtOutsideCallSeq_Type(Integer32):
    """Custom type pabxExtOutsideCallSeq based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("systeltype10", 10),
          ("systeltype7", 7),
          ("systeltype8", 8),
          ("systeltype9", 9),
          ("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5),
          ("type6", 6))
    )


_PabxExtOutsideCallSeq_Type.__name__ = "Integer32"
_PabxExtOutsideCallSeq_Object = MibTableColumn
pabxExtOutsideCallSeq = _PabxExtOutsideCallSeq_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 16),
    _PabxExtOutsideCallSeq_Type()
)
pabxExtOutsideCallSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtOutsideCallSeq.setStatus("mandatory")


class _PabxExtInsideCallSeq_Type(Integer32):
    """Custom type pabxExtInsideCallSeq based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("systeltype10", 10),
          ("systeltype7", 7),
          ("systeltype8", 8),
          ("systeltype9", 9),
          ("type1", 1),
          ("type2", 2),
          ("type3", 3),
          ("type4", 4),
          ("type5", 5),
          ("type6", 6))
    )


_PabxExtInsideCallSeq_Type.__name__ = "Integer32"
_PabxExtInsideCallSeq_Object = MibTableColumn
pabxExtInsideCallSeq = _PabxExtInsideCallSeq_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 17),
    _PabxExtInsideCallSeq_Type()
)
pabxExtInsideCallSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtInsideCallSeq.setStatus("mandatory")


class _PabxExtPresentationFlag_Type(Integer32):
    """Custom type pabxExtPresentationFlag based on Integer32"""
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
        *(("external", 3),
          ("internal", 2),
          ("off", 1),
          ("on", 4))
    )


_PabxExtPresentationFlag_Type.__name__ = "Integer32"
_PabxExtPresentationFlag_Object = MibTableColumn
pabxExtPresentationFlag = _PabxExtPresentationFlag_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 18),
    _PabxExtPresentationFlag_Type()
)
pabxExtPresentationFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtPresentationFlag.setStatus("mandatory")


class _PabxExtProfileId_Type(Integer32):
    """Custom type pabxExtProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxExtProfileId_Type.__name__ = "Integer32"
_PabxExtProfileId_Object = MibTableColumn
pabxExtProfileId = _PabxExtProfileId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 19),
    _PabxExtProfileId_Type()
)
pabxExtProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtProfileId.setStatus("mandatory")


class _PabxExtCtrlByCapiApp_Type(Integer32):
    """Custom type pabxExtCtrlByCapiApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PabxExtCtrlByCapiApp_Type.__name__ = "Integer32"
_PabxExtCtrlByCapiApp_Object = MibTableColumn
pabxExtCtrlByCapiApp = _PabxExtCtrlByCapiApp_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 20),
    _PabxExtCtrlByCapiApp_Type()
)
pabxExtCtrlByCapiApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtCtrlByCapiApp.setStatus("mandatory")
_PabxExtCtrlByCapiAppNo_Type = Integer32
_PabxExtCtrlByCapiAppNo_Object = MibTableColumn
pabxExtCtrlByCapiAppNo = _PabxExtCtrlByCapiAppNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 4, 1, 21),
    _PabxExtCtrlByCapiAppNo_Type()
)
pabxExtCtrlByCapiAppNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxExtCtrlByCapiAppNo.setStatus("mandatory")
_PabxExtFeatureTable_Object = MibTable
pabxExtFeatureTable = _PabxExtFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5)
)
if mibBuilder.loadTexts:
    pabxExtFeatureTable.setStatus("mandatory")
_PabxExtFeatureEntry_Object = MibTableRow
pabxExtFeatureEntry = _PabxExtFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1)
)
pabxExtFeatureEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxExtFeatureExtId"),
)
if mibBuilder.loadTexts:
    pabxExtFeatureEntry.setStatus("mandatory")


class _PabxExtFeatureExtId_Type(Integer32):
    """Custom type pabxExtFeatureExtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxExtFeatureExtId_Type.__name__ = "Integer32"
_PabxExtFeatureExtId_Object = MibTableColumn
pabxExtFeatureExtId = _PabxExtFeatureExtId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 1),
    _PabxExtFeatureExtId_Type()
)
pabxExtFeatureExtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxExtFeatureExtId.setStatus("mandatory")


class _PabxExtFeatureCFUncond_Type(DisplayString):
    """Custom type pabxExtFeatureCFUncond based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxExtFeatureCFUncond_Type.__name__ = "DisplayString"
_PabxExtFeatureCFUncond_Object = MibTableColumn
pabxExtFeatureCFUncond = _PabxExtFeatureCFUncond_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 2),
    _PabxExtFeatureCFUncond_Type()
)
pabxExtFeatureCFUncond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureCFUncond.setStatus("mandatory")


class _PabxExtFeatureCFBusy_Type(DisplayString):
    """Custom type pabxExtFeatureCFBusy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxExtFeatureCFBusy_Type.__name__ = "DisplayString"
_PabxExtFeatureCFBusy_Object = MibTableColumn
pabxExtFeatureCFBusy = _PabxExtFeatureCFBusy_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 3),
    _PabxExtFeatureCFBusy_Type()
)
pabxExtFeatureCFBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureCFBusy.setStatus("mandatory")


class _PabxExtFeatureCFNoReply_Type(DisplayString):
    """Custom type pabxExtFeatureCFNoReply based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxExtFeatureCFNoReply_Type.__name__ = "DisplayString"
_PabxExtFeatureCFNoReply_Object = MibTableColumn
pabxExtFeatureCFNoReply = _PabxExtFeatureCFNoReply_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 4),
    _PabxExtFeatureCFNoReply_Type()
)
pabxExtFeatureCFNoReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureCFNoReply.setStatus("mandatory")


class _PabxExtFeatureCFNoReplyTimer_Type(Integer32):
    """Custom type pabxExtFeatureCFNoReplyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_PabxExtFeatureCFNoReplyTimer_Type.__name__ = "Integer32"
_PabxExtFeatureCFNoReplyTimer_Object = MibTableColumn
pabxExtFeatureCFNoReplyTimer = _PabxExtFeatureCFNoReplyTimer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 5),
    _PabxExtFeatureCFNoReplyTimer_Type()
)
pabxExtFeatureCFNoReplyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureCFNoReplyTimer.setStatus("mandatory")


class _PabxExtFeatureCFMode_Type(Integer32):
    """Custom type pabxExtFeatureCFMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("busy-noreply", 5),
          ("none", 2),
          ("noreply", 4),
          ("uncond", 6))
    )


_PabxExtFeatureCFMode_Type.__name__ = "Integer32"
_PabxExtFeatureCFMode_Object = MibTableColumn
pabxExtFeatureCFMode = _PabxExtFeatureCFMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 6),
    _PabxExtFeatureCFMode_Type()
)
pabxExtFeatureCFMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureCFMode.setStatus("mandatory")


class _PabxExtFeatureEMailAddr_Type(DisplayString):
    """Custom type pabxExtFeatureEMailAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxExtFeatureEMailAddr_Type.__name__ = "DisplayString"
_PabxExtFeatureEMailAddr_Object = MibTableColumn
pabxExtFeatureEMailAddr = _PabxExtFeatureEMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 7),
    _PabxExtFeatureEMailAddr_Type()
)
pabxExtFeatureEMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureEMailAddr.setStatus("mandatory")


class _PabxExtFeatureSystelMSNSlot_Type(Integer32):
    """Custom type pabxExtFeatureSystelMSNSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PabxExtFeatureSystelMSNSlot_Type.__name__ = "Integer32"
_PabxExtFeatureSystelMSNSlot_Object = MibTableColumn
pabxExtFeatureSystelMSNSlot = _PabxExtFeatureSystelMSNSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 8),
    _PabxExtFeatureSystelMSNSlot_Type()
)
pabxExtFeatureSystelMSNSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureSystelMSNSlot.setStatus("mandatory")
_PabxExtFeatureSystelVolume_Type = Integer32
_PabxExtFeatureSystelVolume_Object = MibTableColumn
pabxExtFeatureSystelVolume = _PabxExtFeatureSystelVolume_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 9),
    _PabxExtFeatureSystelVolume_Type()
)
pabxExtFeatureSystelVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureSystelVolume.setStatus("mandatory")
_PabxExtFeatureSystelText_Type = DisplayString
_PabxExtFeatureSystelText_Object = MibTableColumn
pabxExtFeatureSystelText = _PabxExtFeatureSystelText_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 5, 1, 10),
    _PabxExtFeatureSystelText_Type()
)
pabxExtFeatureSystelText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtFeatureSystelText.setStatus("mandatory")
_PabxGroupTable_Object = MibTable
pabxGroupTable = _PabxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 8)
)
if mibBuilder.loadTexts:
    pabxGroupTable.setStatus("mandatory")
_PabxGroupEntry_Object = MibTableRow
pabxGroupEntry = _PabxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 8, 1)
)
pabxGroupEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxGroupId"),
)
if mibBuilder.loadTexts:
    pabxGroupEntry.setStatus("mandatory")


class _PabxGroupId_Type(Integer32):
    """Custom type pabxGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxGroupId_Type.__name__ = "Integer32"
_PabxGroupId_Object = MibTableColumn
pabxGroupId = _PabxGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 8, 1, 1),
    _PabxGroupId_Type()
)
pabxGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxGroupId.setStatus("mandatory")


class _PabxGroupName_Type(DisplayString):
    """Custom type pabxGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxGroupName_Type.__name__ = "DisplayString"
_PabxGroupName_Object = MibTableColumn
pabxGroupName = _PabxGroupName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 8, 1, 2),
    _PabxGroupName_Type()
)
pabxGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxGroupName.setStatus("mandatory")


class _PabxGroupCalladdInhibit_Type(Integer32):
    """Custom type pabxGroupCalladdInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("disable", 3),
          ("enable", 2))
    )


_PabxGroupCalladdInhibit_Type.__name__ = "Integer32"
_PabxGroupCalladdInhibit_Object = MibTableColumn
pabxGroupCalladdInhibit = _PabxGroupCalladdInhibit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 8, 1, 3),
    _PabxGroupCalladdInhibit_Type()
)
pabxGroupCalladdInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxGroupCalladdInhibit.setStatus("mandatory")
_PabxTerminalTable_Object = MibTable
pabxTerminalTable = _PabxTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9)
)
if mibBuilder.loadTexts:
    pabxTerminalTable.setStatus("mandatory")
_PabxTerminalEntry_Object = MibTableRow
pabxTerminalEntry = _PabxTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1)
)
pabxTerminalEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxTermId"),
)
if mibBuilder.loadTexts:
    pabxTerminalEntry.setStatus("mandatory")


class _PabxTermId_Type(Integer32):
    """Custom type pabxTermId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxTermId_Type.__name__ = "Integer32"
_PabxTermId_Object = MibTableColumn
pabxTermId = _PabxTermId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 1),
    _PabxTermId_Type()
)
pabxTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermId.setStatus("mandatory")


class _PabxTermName_Type(DisplayString):
    """Custom type pabxTermName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxTermName_Type.__name__ = "DisplayString"
_PabxTermName_Object = MibTableColumn
pabxTermName = _PabxTermName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 2),
    _PabxTermName_Type()
)
pabxTermName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermName.setStatus("mandatory")


class _PabxTermSlot_Type(Integer32):
    """Custom type pabxTermSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PabxTermSlot_Type.__name__ = "Integer32"
_PabxTermSlot_Object = MibTableColumn
pabxTermSlot = _PabxTermSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 3),
    _PabxTermSlot_Type()
)
pabxTermSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermSlot.setStatus("mandatory")


class _PabxTermUnit_Type(Integer32):
    """Custom type pabxTermUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PabxTermUnit_Type.__name__ = "Integer32"
_PabxTermUnit_Object = MibTableColumn
pabxTermUnit = _PabxTermUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 4),
    _PabxTermUnit_Type()
)
pabxTermUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermUnit.setStatus("mandatory")


class _PabxTermDestination_Type(Integer32):
    """Custom type pabxTermDestination based on Integer32"""
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
        *(("application", 3),
          ("delete", 1),
          ("internet-telephony", 4),
          ("isdn-login", 6),
          ("msg-box", 7),
          ("multiprotocol-routing", 5),
          ("physical", 2))
    )


_PabxTermDestination_Type.__name__ = "Integer32"
_PabxTermDestination_Object = MibTableColumn
pabxTermDestination = _PabxTermDestination_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 5),
    _PabxTermDestination_Type()
)
pabxTermDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermDestination.setStatus("mandatory")


class _PabxTermPrimUserId_Type(Integer32):
    """Custom type pabxTermPrimUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxTermPrimUserId_Type.__name__ = "Integer32"
_PabxTermPrimUserId_Object = MibTableColumn
pabxTermPrimUserId = _PabxTermPrimUserId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 6),
    _PabxTermPrimUserId_Type()
)
pabxTermPrimUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermPrimUserId.setStatus("mandatory")


class _PabxTermType_Type(Integer32):
    """Custom type pabxTermType based on Integer32"""
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
        *(("answeringmachine", 5),
          ("fax", 3),
          ("headset", 4),
          ("modem", 2),
          ("phone", 1),
          ("system-phone", 6))
    )


_PabxTermType_Type.__name__ = "Integer32"
_PabxTermType_Object = MibTableColumn
pabxTermType = _PabxTermType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 7),
    _PabxTermType_Type()
)
pabxTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermType.setStatus("mandatory")


class _PabxTermProfileId_Type(Integer32):
    """Custom type pabxTermProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxTermProfileId_Type.__name__ = "Integer32"
_PabxTermProfileId_Object = MibTableColumn
pabxTermProfileId = _PabxTermProfileId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 8),
    _PabxTermProfileId_Type()
)
pabxTermProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermProfileId.setStatus("mandatory")


class _PabxTermSystelSerialNo_Type(DisplayString):
    """Custom type pabxTermSystelSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxTermSystelSerialNo_Type.__name__ = "DisplayString"
_PabxTermSystelSerialNo_Object = MibTableColumn
pabxTermSystelSerialNo = _PabxTermSystelSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 9, 1, 9),
    _PabxTermSystelSerialNo_Type()
)
pabxTermSystelSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTermSystelSerialNo.setStatus("mandatory")
_PabxExtToGroupTable_Object = MibTable
pabxExtToGroupTable = _PabxExtToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 10)
)
if mibBuilder.loadTexts:
    pabxExtToGroupTable.setStatus("mandatory")
_PabxExtToGroupEntry_Object = MibTableRow
pabxExtToGroupEntry = _PabxExtToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 10, 1)
)
pabxExtToGroupEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxExtToGroupExtId"),
)
if mibBuilder.loadTexts:
    pabxExtToGroupEntry.setStatus("mandatory")


class _PabxExtToGroupExtId_Type(Integer32):
    """Custom type pabxExtToGroupExtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PabxExtToGroupExtId_Type.__name__ = "Integer32"
_PabxExtToGroupExtId_Object = MibTableColumn
pabxExtToGroupExtId = _PabxExtToGroupExtId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 10, 1, 1),
    _PabxExtToGroupExtId_Type()
)
pabxExtToGroupExtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtToGroupExtId.setStatus("mandatory")


class _PabxExtToGroupGroupId_Type(Integer32):
    """Custom type pabxExtToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PabxExtToGroupGroupId_Type.__name__ = "Integer32"
_PabxExtToGroupGroupId_Object = MibTableColumn
pabxExtToGroupGroupId = _PabxExtToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 10, 1, 2),
    _PabxExtToGroupGroupId_Type()
)
pabxExtToGroupGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtToGroupGroupId.setStatus("mandatory")


class _PabxExtToGroupCallPickupActive_Type(Integer32):
    """Custom type pabxExtToGroupCallPickupActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("enable", 2))
    )


_PabxExtToGroupCallPickupActive_Type.__name__ = "Integer32"
_PabxExtToGroupCallPickupActive_Object = MibTableColumn
pabxExtToGroupCallPickupActive = _PabxExtToGroupCallPickupActive_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 10, 1, 3),
    _PabxExtToGroupCallPickupActive_Type()
)
pabxExtToGroupCallPickupActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtToGroupCallPickupActive.setStatus("mandatory")
_PabxTrunkMsnTable_Object = MibTable
pabxTrunkMsnTable = _PabxTrunkMsnTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11)
)
if mibBuilder.loadTexts:
    pabxTrunkMsnTable.setStatus("mandatory")
_PabxTrunkMsnEntry_Object = MibTableRow
pabxTrunkMsnEntry = _PabxTrunkMsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11, 1)
)
pabxTrunkMsnEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxTrunkMsnSlot"),
)
if mibBuilder.loadTexts:
    pabxTrunkMsnEntry.setStatus("mandatory")


class _PabxTrunkMsnSlot_Type(Integer32):
    """Custom type pabxTrunkMsnSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PabxTrunkMsnSlot_Type.__name__ = "Integer32"
_PabxTrunkMsnSlot_Object = MibTableColumn
pabxTrunkMsnSlot = _PabxTrunkMsnSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11, 1, 1),
    _PabxTrunkMsnSlot_Type()
)
pabxTrunkMsnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxTrunkMsnSlot.setStatus("mandatory")


class _PabxTrunkMsnUnit_Type(Integer32):
    """Custom type pabxTrunkMsnUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PabxTrunkMsnUnit_Type.__name__ = "Integer32"
_PabxTrunkMsnUnit_Object = MibTableColumn
pabxTrunkMsnUnit = _PabxTrunkMsnUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11, 1, 2),
    _PabxTrunkMsnUnit_Type()
)
pabxTrunkMsnUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxTrunkMsnUnit.setStatus("mandatory")


class _PabxTrunkMsnNumber_Type(DisplayString):
    """Custom type pabxTrunkMsnNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxTrunkMsnNumber_Type.__name__ = "DisplayString"
_PabxTrunkMsnNumber_Object = MibTableColumn
pabxTrunkMsnNumber = _PabxTrunkMsnNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11, 1, 3),
    _PabxTrunkMsnNumber_Type()
)
pabxTrunkMsnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxTrunkMsnNumber.setStatus("mandatory")


class _PabxTrunkMsnNumberType_Type(Integer32):
    """Custom type pabxTrunkMsnNumberType based on Integer32"""
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
        *(("private", 2),
          ("public-international", 3),
          ("public-national", 4),
          ("public-other", 6),
          ("public-subscriber", 5),
          ("unknown", 1))
    )


_PabxTrunkMsnNumberType_Type.__name__ = "Integer32"
_PabxTrunkMsnNumberType_Object = MibScalar
pabxTrunkMsnNumberType = _PabxTrunkMsnNumberType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 11, 1, 4),
    _PabxTrunkMsnNumberType_Type()
)
pabxTrunkMsnNumberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxTrunkMsnNumberType.setStatus("mandatory")
_PabxProfileTable_Object = MibTable
pabxProfileTable = _PabxProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12)
)
if mibBuilder.loadTexts:
    pabxProfileTable.setStatus("mandatory")
_PabxProfileEntry_Object = MibTableRow
pabxProfileEntry = _PabxProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1)
)
pabxProfileEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxProfileId"),
)
if mibBuilder.loadTexts:
    pabxProfileEntry.setStatus("mandatory")


class _PabxProfileId_Type(Integer32):
    """Custom type pabxProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PabxProfileId_Type.__name__ = "Integer32"
_PabxProfileId_Object = MibTableColumn
pabxProfileId = _PabxProfileId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1, 1),
    _PabxProfileId_Type()
)
pabxProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxProfileId.setStatus("mandatory")


class _PabxProfileName_Type(DisplayString):
    """Custom type pabxProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxProfileName_Type.__name__ = "DisplayString"
_PabxProfileName_Object = MibTableColumn
pabxProfileName = _PabxProfileName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1, 2),
    _PabxProfileName_Type()
)
pabxProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxProfileName.setStatus("mandatory")


class _PabxProfileAutoDialOutNo_Type(DisplayString):
    """Custom type pabxProfileAutoDialOutNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxProfileAutoDialOutNo_Type.__name__ = "DisplayString"
_PabxProfileAutoDialOutNo_Object = MibTableColumn
pabxProfileAutoDialOutNo = _PabxProfileAutoDialOutNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1, 3),
    _PabxProfileAutoDialOutNo_Type()
)
pabxProfileAutoDialOutNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxProfileAutoDialOutNo.setStatus("mandatory")


class _PabxProfileDialPerm_Type(Integer32):
    """Custom type pabxProfileDialPerm based on Integer32"""
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
        *(("full", 5),
          ("internal", 1),
          ("local", 2),
          ("national", 3),
          ("national-special", 4))
    )


_PabxProfileDialPerm_Type.__name__ = "Integer32"
_PabxProfileDialPerm_Object = MibTableColumn
pabxProfileDialPerm = _PabxProfileDialPerm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1, 4),
    _PabxProfileDialPerm_Type()
)
pabxProfileDialPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxProfileDialPerm.setStatus("mandatory")


class _PabxProfileAvailability_Type(Integer32):
    """Custom type pabxProfileAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              15)
        )
    )
    namedValues = NamedValues(
        *(("delete", 15),
          ("external", 2),
          ("full", 3),
          ("internal", 1))
    )


_PabxProfileAvailability_Type.__name__ = "Integer32"
_PabxProfileAvailability_Object = MibTableColumn
pabxProfileAvailability = _PabxProfileAvailability_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 12, 1, 5),
    _PabxProfileAvailability_Type()
)
pabxProfileAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxProfileAvailability.setStatus("mandatory")
_PabxExtNoPermTable_Object = MibTable
pabxExtNoPermTable = _PabxExtNoPermTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13)
)
if mibBuilder.loadTexts:
    pabxExtNoPermTable.setStatus("mandatory")
_PabxExtNoPermEntry_Object = MibTableRow
pabxExtNoPermEntry = _PabxExtNoPermEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13, 1)
)
pabxExtNoPermEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxExtNoPermNumber"),
)
if mibBuilder.loadTexts:
    pabxExtNoPermEntry.setStatus("mandatory")


class _PabxExtNoPermNumber_Type(DisplayString):
    """Custom type pabxExtNoPermNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxExtNoPermNumber_Type.__name__ = "DisplayString"
_PabxExtNoPermNumber_Object = MibTableColumn
pabxExtNoPermNumber = _PabxExtNoPermNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13, 1, 1),
    _PabxExtNoPermNumber_Type()
)
pabxExtNoPermNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtNoPermNumber.setStatus("mandatory")


class _PabxExtNoPermPermission_Type(Integer32):
    """Custom type pabxExtNoPermPermission based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("delete", 255),
          ("deny", 6),
          ("full", 5),
          ("internal", 1),
          ("local", 2),
          ("national", 3),
          ("national-special", 4),
          ("provider", 7))
    )


_PabxExtNoPermPermission_Type.__name__ = "Integer32"
_PabxExtNoPermPermission_Object = MibTableColumn
pabxExtNoPermPermission = _PabxExtNoPermPermission_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13, 1, 2),
    _PabxExtNoPermPermission_Type()
)
pabxExtNoPermPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtNoPermPermission.setStatus("mandatory")


class _PabxExtNoPermStatus_Type(Integer32):
    """Custom type pabxExtNoPermStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists-error", 3),
          ("format-error", 2),
          ("ok", 1))
    )


_PabxExtNoPermStatus_Type.__name__ = "Integer32"
_PabxExtNoPermStatus_Object = MibTableColumn
pabxExtNoPermStatus = _PabxExtNoPermStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13, 1, 3),
    _PabxExtNoPermStatus_Type()
)
pabxExtNoPermStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pabxExtNoPermStatus.setStatus("mandatory")


class _PabxExtNoPermDescription_Type(DisplayString):
    """Custom type pabxExtNoPermDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_PabxExtNoPermDescription_Type.__name__ = "DisplayString"
_PabxExtNoPermDescription_Object = MibTableColumn
pabxExtNoPermDescription = _PabxExtNoPermDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 13, 1, 4),
    _PabxExtNoPermDescription_Type()
)
pabxExtNoPermDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExtNoPermDescription.setStatus("mandatory")
_SystelTerminalTable_Object = MibTable
systelTerminalTable = _SystelTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14)
)
if mibBuilder.loadTexts:
    systelTerminalTable.setStatus("mandatory")
_SystelTerminalEntry_Object = MibTableRow
systelTerminalEntry = _SystelTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1)
)
systelTerminalEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "systelTermSerialNo"),
)
if mibBuilder.loadTexts:
    systelTerminalEntry.setStatus("mandatory")


class _SystelTermSerialNo_Type(DisplayString):
    """Custom type systelTermSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SystelTermSerialNo_Type.__name__ = "DisplayString"
_SystelTermSerialNo_Object = MibTableColumn
systelTermSerialNo = _SystelTermSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 1),
    _SystelTermSerialNo_Type()
)
systelTermSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systelTermSerialNo.setStatus("mandatory")


class _SystelTermAutoMove_Type(Integer32):
    """Custom type systelTermAutoMove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 1),
          ("enable", 2))
    )


_SystelTermAutoMove_Type.__name__ = "Integer32"
_SystelTermAutoMove_Object = MibTableColumn
systelTermAutoMove = _SystelTermAutoMove_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 2),
    _SystelTermAutoMove_Type()
)
systelTermAutoMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systelTermAutoMove.setStatus("mandatory")
_SystelTermSWVersion_Type = DisplayString
_SystelTermSWVersion_Object = MibTableColumn
systelTermSWVersion = _SystelTermSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 3),
    _SystelTermSWVersion_Type()
)
systelTermSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermSWVersion.setStatus("mandatory")
_SystelTermRelDate_Type = DisplayString
_SystelTermRelDate_Object = MibTableColumn
systelTermRelDate = _SystelTermRelDate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 4),
    _SystelTermRelDate_Type()
)
systelTermRelDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermRelDate.setStatus("mandatory")
_SystelTermCountry_Type = DisplayString
_SystelTermCountry_Object = MibTableColumn
systelTermCountry = _SystelTermCountry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 5),
    _SystelTermCountry_Type()
)
systelTermCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermCountry.setStatus("mandatory")
_SystelTermOEMString_Type = DisplayString
_SystelTermOEMString_Object = MibTableColumn
systelTermOEMString = _SystelTermOEMString_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 6),
    _SystelTermOEMString_Type()
)
systelTermOEMString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermOEMString.setStatus("mandatory")
_SystelTermDBVersion_Type = DisplayString
_SystelTermDBVersion_Object = MibTableColumn
systelTermDBVersion = _SystelTermDBVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 7),
    _SystelTermDBVersion_Type()
)
systelTermDBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermDBVersion.setStatus("mandatory")
_SystelTermSlot_Type = Integer32
_SystelTermSlot_Object = MibTableColumn
systelTermSlot = _SystelTermSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 8),
    _SystelTermSlot_Type()
)
systelTermSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermSlot.setStatus("mandatory")
_SystelTermUnit_Type = Integer32
_SystelTermUnit_Object = MibTableColumn
systelTermUnit = _SystelTermUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 9),
    _SystelTermUnit_Type()
)
systelTermUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermUnit.setStatus("mandatory")


class _SystelTermTei_Type(Integer32):
    """Custom type systelTermTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SystelTermTei_Type.__name__ = "Integer32"
_SystelTermTei_Object = MibTableColumn
systelTermTei = _SystelTermTei_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 10),
    _SystelTermTei_Type()
)
systelTermTei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermTei.setStatus("mandatory")


class _SystelTermAutoConf_Type(Integer32):
    """Custom type systelTermAutoConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on-registration", 2))
    )


_SystelTermAutoConf_Type.__name__ = "Integer32"
_SystelTermAutoConf_Object = MibTableColumn
systelTermAutoConf = _SystelTermAutoConf_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 11),
    _SystelTermAutoConf_Type()
)
systelTermAutoConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systelTermAutoConf.setStatus("mandatory")


class _SystelTermTriggerConf_Type(Integer32):
    """Custom type systelTermTriggerConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("check", 2),
          ("done", 1),
          ("error", 255),
          ("get", 4),
          ("get-and-create", 5),
          ("set", 3))
    )


_SystelTermTriggerConf_Type.__name__ = "Integer32"
_SystelTermTriggerConf_Object = MibTableColumn
systelTermTriggerConf = _SystelTermTriggerConf_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 12),
    _SystelTermTriggerConf_Type()
)
systelTermTriggerConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systelTermTriggerConf.setStatus("mandatory")


class _SystelTermLastConfAction_Type(Integer32):
    """Custom type systelTermLastConfAction based on Integer32"""
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
        *(("check", 2),
          ("get", 4),
          ("get-and-create", 5),
          ("set", 3),
          ("unknown", 1))
    )


_SystelTermLastConfAction_Type.__name__ = "Integer32"
_SystelTermLastConfAction_Object = MibTableColumn
systelTermLastConfAction = _SystelTermLastConfAction_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 14, 1, 13),
    _SystelTermLastConfAction_Type()
)
systelTermLastConfAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systelTermLastConfAction.setStatus("mandatory")
_PabxSpeedDialTable_Object = MibTable
pabxSpeedDialTable = _PabxSpeedDialTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 15)
)
if mibBuilder.loadTexts:
    pabxSpeedDialTable.setStatus("mandatory")
_PabxSpeedDialEntry_Object = MibTableRow
pabxSpeedDialEntry = _PabxSpeedDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 15, 1)
)
pabxSpeedDialEntry.setIndexNames(
    (0, "BIANCA-BOX-PABX-MIB", "pabxSpeedDialShortcut"),
)
if mibBuilder.loadTexts:
    pabxSpeedDialEntry.setStatus("mandatory")


class _PabxSpeedDialShortcut_Type(DisplayString):
    """Custom type pabxSpeedDialShortcut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PabxSpeedDialShortcut_Type.__name__ = "DisplayString"
_PabxSpeedDialShortcut_Object = MibTableColumn
pabxSpeedDialShortcut = _PabxSpeedDialShortcut_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 15, 1, 1),
    _PabxSpeedDialShortcut_Type()
)
pabxSpeedDialShortcut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxSpeedDialShortcut.setStatus("mandatory")


class _PabxSpeedDialNumber_Type(DisplayString):
    """Custom type pabxSpeedDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxSpeedDialNumber_Type.__name__ = "DisplayString"
_PabxSpeedDialNumber_Object = MibTableColumn
pabxSpeedDialNumber = _PabxSpeedDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 15, 1, 2),
    _PabxSpeedDialNumber_Type()
)
pabxSpeedDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxSpeedDialNumber.setStatus("mandatory")


class _PabxSpeedDialCtrl_Type(Integer32):
    """Custom type pabxSpeedDialCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("off", 2),
          ("on", 1))
    )


_PabxSpeedDialCtrl_Type.__name__ = "Integer32"
_PabxSpeedDialCtrl_Object = MibTableColumn
pabxSpeedDialCtrl = _PabxSpeedDialCtrl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 15, 1, 3),
    _PabxSpeedDialCtrl_Type()
)
pabxSpeedDialCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxSpeedDialCtrl.setStatus("mandatory")


class _PabxLocalPrefix_Type(DisplayString):
    """Custom type pabxLocalPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PabxLocalPrefix_Type.__name__ = "DisplayString"
_PabxLocalPrefix_Object = MibScalar
pabxLocalPrefix = _PabxLocalPrefix_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 20),
    _PabxLocalPrefix_Type()
)
pabxLocalPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxLocalPrefix.setStatus("mandatory")
_PabxTrunkMask_Type = BitValue
_PabxTrunkMask_Object = MibScalar
pabxTrunkMask = _PabxTrunkMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 21),
    _PabxTrunkMask_Type()
)
pabxTrunkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTrunkMask.setStatus("mandatory")


class _PabxPriorityVoice_Type(Integer32):
    """Custom type pabxPriorityVoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PabxPriorityVoice_Type.__name__ = "Integer32"
_PabxPriorityVoice_Object = MibScalar
pabxPriorityVoice = _PabxPriorityVoice_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 22),
    _PabxPriorityVoice_Type()
)
pabxPriorityVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxPriorityVoice.setStatus("mandatory")


class _PabxMusicOnHold_Type(Integer32):
    """Custom type pabxMusicOnHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_PabxMusicOnHold_Type.__name__ = "Integer32"
_PabxMusicOnHold_Object = MibScalar
pabxMusicOnHold = _PabxMusicOnHold_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 23),
    _PabxMusicOnHold_Type()
)
pabxMusicOnHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxMusicOnHold.setStatus("mandatory")


class _PabxDoorIntercomCallExtension_Type(DisplayString):
    """Custom type pabxDoorIntercomCallExtension based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PabxDoorIntercomCallExtension_Type.__name__ = "DisplayString"
_PabxDoorIntercomCallExtension_Object = MibScalar
pabxDoorIntercomCallExtension = _PabxDoorIntercomCallExtension_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 24),
    _PabxDoorIntercomCallExtension_Type()
)
pabxDoorIntercomCallExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxDoorIntercomCallExtension.setStatus("mandatory")


class _PabxDoorIntercomExternalOpen_Type(Integer32):
    """Custom type pabxDoorIntercomExternalOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PabxDoorIntercomExternalOpen_Type.__name__ = "Integer32"
_PabxDoorIntercomExternalOpen_Object = MibScalar
pabxDoorIntercomExternalOpen = _PabxDoorIntercomExternalOpen_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 25),
    _PabxDoorIntercomExternalOpen_Type()
)
pabxDoorIntercomExternalOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxDoorIntercomExternalOpen.setStatus("mandatory")


class _PabxTapiAdmPassword_Type(DisplayString):
    """Custom type pabxTapiAdmPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxTapiAdmPassword_Type.__name__ = "DisplayString"
_PabxTapiAdmPassword_Object = MibScalar
pabxTapiAdmPassword = _PabxTapiAdmPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 26),
    _PabxTapiAdmPassword_Type()
)
pabxTapiAdmPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxTapiAdmPassword.setStatus("mandatory")


class _PabxDefaultAutoDialOutNo_Type(DisplayString):
    """Custom type pabxDefaultAutoDialOutNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxDefaultAutoDialOutNo_Type.__name__ = "DisplayString"
_PabxDefaultAutoDialOutNo_Object = MibScalar
pabxDefaultAutoDialOutNo = _PabxDefaultAutoDialOutNo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 27),
    _PabxDefaultAutoDialOutNo_Type()
)
pabxDefaultAutoDialOutNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxDefaultAutoDialOutNo.setStatus("mandatory")


class _PabxDefaultAvailability_Type(Integer32):
    """Custom type pabxDefaultAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("full", 3),
          ("internal", 1))
    )


_PabxDefaultAvailability_Type.__name__ = "Integer32"
_PabxDefaultAvailability_Object = MibScalar
pabxDefaultAvailability = _PabxDefaultAvailability_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 28),
    _PabxDefaultAvailability_Type()
)
pabxDefaultAvailability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxDefaultAvailability.setStatus("mandatory")


class _PabxDefaultDialPerm_Type(Integer32):
    """Custom type pabxDefaultDialPerm based on Integer32"""
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
        *(("full", 5),
          ("internal", 1),
          ("local", 2),
          ("national", 3),
          ("national-special", 4))
    )


_PabxDefaultDialPerm_Type.__name__ = "Integer32"
_PabxDefaultDialPerm_Object = MibScalar
pabxDefaultDialPerm = _PabxDefaultDialPerm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 29),
    _PabxDefaultDialPerm_Type()
)
pabxDefaultDialPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxDefaultDialPerm.setStatus("mandatory")


class _PabxExternalCallDialPerm_Type(Integer32):
    """Custom type pabxExternalCallDialPerm based on Integer32"""
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
        *(("full", 5),
          ("internal", 1),
          ("local", 2),
          ("national", 3),
          ("national-special", 4))
    )


_PabxExternalCallDialPerm_Type.__name__ = "Integer32"
_PabxExternalCallDialPerm_Object = MibScalar
pabxExternalCallDialPerm = _PabxExternalCallDialPerm_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 30),
    _PabxExternalCallDialPerm_Type()
)
pabxExternalCallDialPerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxExternalCallDialPerm.setStatus("mandatory")


class _PabxCapiAdmPassword_Type(DisplayString):
    """Custom type pabxCapiAdmPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_PabxCapiAdmPassword_Type.__name__ = "DisplayString"
_PabxCapiAdmPassword_Object = MibScalar
pabxCapiAdmPassword = _PabxCapiAdmPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 31),
    _PabxCapiAdmPassword_Type()
)
pabxCapiAdmPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxCapiAdmPassword.setStatus("mandatory")


class _PabxCountry_Type(Integer32):
    """Custom type pabxCountry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("france", 3),
          ("germany", 1),
          ("uk", 2))
    )


_PabxCountry_Type.__name__ = "Integer32"
_PabxCountry_Object = MibScalar
pabxCountry = _PabxCountry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 20, 32),
    _PabxCountry_Type()
)
pabxCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pabxCountry.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BOX-PABX-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "pabx": pabx,
       "pabxUserTable": pabxUserTable,
       "pabxUserEntry": pabxUserEntry,
       "pabxUserName": pabxUserName,
       "pabxUserPassword": pabxUserPassword,
       "pabxUserTapiMon": pabxUserTapiMon,
       "pabxUserTapiCtrl": pabxUserTapiCtrl,
       "pabxUserTapiMedia": pabxUserTapiMedia,
       "pabxUserCapi": pabxUserCapi,
       "pabxUserId": pabxUserId,
       "pabxUserPIN": pabxUserPIN,
       "pabxUserPrimGroupId": pabxUserPrimGroupId,
       "pabxTrunkTable": pabxTrunkTable,
       "pabxTrunkEntry": pabxTrunkEntry,
       "pabxTrunkNumber": pabxTrunkNumber,
       "pabxTrunkDescr": pabxTrunkDescr,
       "pabxTrunkSlot": pabxTrunkSlot,
       "pabxTrunkUnit": pabxTrunkUnit,
       "pabxTrunkProtocol": pabxTrunkProtocol,
       "pabxTrunkConfig": pabxTrunkConfig,
       "pabxTrunkTeiProc": pabxTrunkTeiProc,
       "pabxTrunkTeiValue": pabxTrunkTeiValue,
       "pabxTrunkCountryCode": pabxTrunkCountryCode,
       "pabxTrunkAreaCode": pabxTrunkAreaCode,
       "pabxTrunkSubscriberNo": pabxTrunkSubscriberNo,
       "pabxTrunkExtension": pabxTrunkExtension,
       "pabxTrunkType": pabxTrunkType,
       "pabxTrunkL2Mode": pabxTrunkL2Mode,
       "pabxTrunkPrefixTable": pabxTrunkPrefixTable,
       "pabxTrunkPrefixEntry": pabxTrunkPrefixEntry,
       "pabxTrunkPrefixPrefix": pabxTrunkPrefixPrefix,
       "pabxTrunkPrefixTrunkMask": pabxTrunkPrefixTrunkMask,
       "pabxTrunkPrefixStatus": pabxTrunkPrefixStatus,
       "pabxTrunkPrefixStripOnOutgoing": pabxTrunkPrefixStripOnOutgoing,
       "pabxTrunkPrefixPrependOnIncoming": pabxTrunkPrefixPrependOnIncoming,
       "pabxExtensionTable": pabxExtensionTable,
       "pabxExtensionEntry": pabxExtensionEntry,
       "pabxExtExtension": pabxExtExtension,
       "pabxExtType": pabxExtType,
       "pabxExtIpAddr": pabxExtIpAddr,
       "pabxExtEAZ": pabxExtEAZ,
       "pabxExtLayer1Prot": pabxExtLayer1Prot,
       "pabxExtIfIndex": pabxExtIfIndex,
       "pabxExtId": pabxExtId,
       "pabxExtUserId": pabxExtUserId,
       "pabxExtTermId": pabxExtTermId,
       "pabxExtDefaultExtFlag": pabxExtDefaultExtFlag,
       "pabxExtPresentationNr": pabxExtPresentationNr,
       "pabxExtOutsideCallSeq": pabxExtOutsideCallSeq,
       "pabxExtInsideCallSeq": pabxExtInsideCallSeq,
       "pabxExtPresentationFlag": pabxExtPresentationFlag,
       "pabxExtProfileId": pabxExtProfileId,
       "pabxExtCtrlByCapiApp": pabxExtCtrlByCapiApp,
       "pabxExtCtrlByCapiAppNo": pabxExtCtrlByCapiAppNo,
       "pabxExtFeatureTable": pabxExtFeatureTable,
       "pabxExtFeatureEntry": pabxExtFeatureEntry,
       "pabxExtFeatureExtId": pabxExtFeatureExtId,
       "pabxExtFeatureCFUncond": pabxExtFeatureCFUncond,
       "pabxExtFeatureCFBusy": pabxExtFeatureCFBusy,
       "pabxExtFeatureCFNoReply": pabxExtFeatureCFNoReply,
       "pabxExtFeatureCFNoReplyTimer": pabxExtFeatureCFNoReplyTimer,
       "pabxExtFeatureCFMode": pabxExtFeatureCFMode,
       "pabxExtFeatureEMailAddr": pabxExtFeatureEMailAddr,
       "pabxExtFeatureSystelMSNSlot": pabxExtFeatureSystelMSNSlot,
       "pabxExtFeatureSystelVolume": pabxExtFeatureSystelVolume,
       "pabxExtFeatureSystelText": pabxExtFeatureSystelText,
       "pabxGroupTable": pabxGroupTable,
       "pabxGroupEntry": pabxGroupEntry,
       "pabxGroupId": pabxGroupId,
       "pabxGroupName": pabxGroupName,
       "pabxGroupCalladdInhibit": pabxGroupCalladdInhibit,
       "pabxTerminalTable": pabxTerminalTable,
       "pabxTerminalEntry": pabxTerminalEntry,
       "pabxTermId": pabxTermId,
       "pabxTermName": pabxTermName,
       "pabxTermSlot": pabxTermSlot,
       "pabxTermUnit": pabxTermUnit,
       "pabxTermDestination": pabxTermDestination,
       "pabxTermPrimUserId": pabxTermPrimUserId,
       "pabxTermType": pabxTermType,
       "pabxTermProfileId": pabxTermProfileId,
       "pabxTermSystelSerialNo": pabxTermSystelSerialNo,
       "pabxExtToGroupTable": pabxExtToGroupTable,
       "pabxExtToGroupEntry": pabxExtToGroupEntry,
       "pabxExtToGroupExtId": pabxExtToGroupExtId,
       "pabxExtToGroupGroupId": pabxExtToGroupGroupId,
       "pabxExtToGroupCallPickupActive": pabxExtToGroupCallPickupActive,
       "pabxTrunkMsnTable": pabxTrunkMsnTable,
       "pabxTrunkMsnEntry": pabxTrunkMsnEntry,
       "pabxTrunkMsnSlot": pabxTrunkMsnSlot,
       "pabxTrunkMsnUnit": pabxTrunkMsnUnit,
       "pabxTrunkMsnNumber": pabxTrunkMsnNumber,
       "pabxTrunkMsnNumberType": pabxTrunkMsnNumberType,
       "pabxProfileTable": pabxProfileTable,
       "pabxProfileEntry": pabxProfileEntry,
       "pabxProfileId": pabxProfileId,
       "pabxProfileName": pabxProfileName,
       "pabxProfileAutoDialOutNo": pabxProfileAutoDialOutNo,
       "pabxProfileDialPerm": pabxProfileDialPerm,
       "pabxProfileAvailability": pabxProfileAvailability,
       "pabxExtNoPermTable": pabxExtNoPermTable,
       "pabxExtNoPermEntry": pabxExtNoPermEntry,
       "pabxExtNoPermNumber": pabxExtNoPermNumber,
       "pabxExtNoPermPermission": pabxExtNoPermPermission,
       "pabxExtNoPermStatus": pabxExtNoPermStatus,
       "pabxExtNoPermDescription": pabxExtNoPermDescription,
       "systelTerminalTable": systelTerminalTable,
       "systelTerminalEntry": systelTerminalEntry,
       "systelTermSerialNo": systelTermSerialNo,
       "systelTermAutoMove": systelTermAutoMove,
       "systelTermSWVersion": systelTermSWVersion,
       "systelTermRelDate": systelTermRelDate,
       "systelTermCountry": systelTermCountry,
       "systelTermOEMString": systelTermOEMString,
       "systelTermDBVersion": systelTermDBVersion,
       "systelTermSlot": systelTermSlot,
       "systelTermUnit": systelTermUnit,
       "systelTermTei": systelTermTei,
       "systelTermAutoConf": systelTermAutoConf,
       "systelTermTriggerConf": systelTermTriggerConf,
       "systelTermLastConfAction": systelTermLastConfAction,
       "pabxSpeedDialTable": pabxSpeedDialTable,
       "pabxSpeedDialEntry": pabxSpeedDialEntry,
       "pabxSpeedDialShortcut": pabxSpeedDialShortcut,
       "pabxSpeedDialNumber": pabxSpeedDialNumber,
       "pabxSpeedDialCtrl": pabxSpeedDialCtrl,
       "pabxLocalPrefix": pabxLocalPrefix,
       "pabxTrunkMask": pabxTrunkMask,
       "pabxPriorityVoice": pabxPriorityVoice,
       "pabxMusicOnHold": pabxMusicOnHold,
       "pabxDoorIntercomCallExtension": pabxDoorIntercomCallExtension,
       "pabxDoorIntercomExternalOpen": pabxDoorIntercomExternalOpen,
       "pabxTapiAdmPassword": pabxTapiAdmPassword,
       "pabxDefaultAutoDialOutNo": pabxDefaultAutoDialOutNo,
       "pabxDefaultAvailability": pabxDefaultAvailability,
       "pabxDefaultDialPerm": pabxDefaultDialPerm,
       "pabxExternalCallDialPerm": pabxExternalCallDialPerm,
       "pabxCapiAdmPassword": pabxCapiAdmPassword,
       "pabxCountry": pabxCountry}
)
