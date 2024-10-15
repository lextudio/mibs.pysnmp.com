# SNMP MIB module (Omnis-Management-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Omnis-Management-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:54 2024
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
 NotificationType,
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
    "NotificationType",
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

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniOmnis_ObjectIdentity = ObjectIdentity
sniOmnis = _SniOmnis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31)
)
_SniOmnisGlobalData_ObjectIdentity = ObjectIdentity
sniOmnisGlobalData = _SniOmnisGlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1)
)
_OmnisGlobalDataSubagentVersion_Type = DisplayString
_OmnisGlobalDataSubagentVersion_Object = MibScalar
omnisGlobalDataSubagentVersion = _OmnisGlobalDataSubagentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 1),
    _OmnisGlobalDataSubagentVersion_Type()
)
omnisGlobalDataSubagentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGlobalDataSubagentVersion.setStatus("mandatory")
_OmnisGlobalDataTabNum_Type = Integer32
_OmnisGlobalDataTabNum_Object = MibScalar
omnisGlobalDataTabNum = _OmnisGlobalDataTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 4),
    _OmnisGlobalDataTabNum_Type()
)
omnisGlobalDataTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGlobalDataTabNum.setStatus("mandatory")
_OmnisGlobalDataActID_Type = Integer32
_OmnisGlobalDataActID_Object = MibScalar
omnisGlobalDataActID = _OmnisGlobalDataActID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 5),
    _OmnisGlobalDataActID_Type()
)
omnisGlobalDataActID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisGlobalDataActID.setStatus("mandatory")
_OmnisGlobalDataActName_Type = DisplayString
_OmnisGlobalDataActName_Object = MibScalar
omnisGlobalDataActName = _OmnisGlobalDataActName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 6),
    _OmnisGlobalDataActName_Type()
)
omnisGlobalDataActName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisGlobalDataActName.setStatus("mandatory")
_OmnisGlobalDataTable_Object = MibTable
omnisGlobalDataTable = _OmnisGlobalDataTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7)
)
if mibBuilder.loadTexts:
    omnisGlobalDataTable.setStatus("mandatory")
_OmnisGlobalDataEntry_Object = MibTableRow
omnisGlobalDataEntry = _OmnisGlobalDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7, 1)
)
omnisGlobalDataEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisGlobalDataOmnID"),
)
if mibBuilder.loadTexts:
    omnisGlobalDataEntry.setStatus("mandatory")
_OmnisGlobalDataOmnID_Type = Integer32
_OmnisGlobalDataOmnID_Object = MibTableColumn
omnisGlobalDataOmnID = _OmnisGlobalDataOmnID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7, 1, 1),
    _OmnisGlobalDataOmnID_Type()
)
omnisGlobalDataOmnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGlobalDataOmnID.setStatus("mandatory")
_OmnisGlobalDataVersion_Type = DisplayString
_OmnisGlobalDataVersion_Object = MibTableColumn
omnisGlobalDataVersion = _OmnisGlobalDataVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7, 1, 2),
    _OmnisGlobalDataVersion_Type()
)
omnisGlobalDataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGlobalDataVersion.setStatus("mandatory")
_OmnisGlobalDataOmnName_Type = DisplayString
_OmnisGlobalDataOmnName_Object = MibTableColumn
omnisGlobalDataOmnName = _OmnisGlobalDataOmnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7, 1, 3),
    _OmnisGlobalDataOmnName_Type()
)
omnisGlobalDataOmnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGlobalDataOmnName.setStatus("mandatory")


class _OmnisGlobalDataState_Type(Integer32):
    """Custom type omnisGlobalDataState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_OmnisGlobalDataState_Type.__name__ = "Integer32"
_OmnisGlobalDataState_Object = MibTableColumn
omnisGlobalDataState = _OmnisGlobalDataState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 1, 7, 1, 4),
    _OmnisGlobalDataState_Type()
)
omnisGlobalDataState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisGlobalDataState.setStatus("mandatory")
_SniOmnisSettings_ObjectIdentity = ObjectIdentity
sniOmnisSettings = _SniOmnisSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2)
)


class _OmnisSettingsAppName_Type(DisplayString):
    """Custom type omnisSettingsAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisSettingsAppName_Type.__name__ = "DisplayString"
_OmnisSettingsAppName_Object = MibScalar
omnisSettingsAppName = _OmnisSettingsAppName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 1),
    _OmnisSettingsAppName_Type()
)
omnisSettingsAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisSettingsAppName.setStatus("mandatory")


class _OmnisSettingsAppNameISO_Type(DisplayString):
    """Custom type omnisSettingsAppNameISO based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisSettingsAppNameISO_Type.__name__ = "DisplayString"
_OmnisSettingsAppNameISO_Object = MibScalar
omnisSettingsAppNameISO = _OmnisSettingsAppNameISO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 2),
    _OmnisSettingsAppNameISO_Type()
)
omnisSettingsAppNameISO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisSettingsAppNameISO.setStatus("mandatory")
_OmnisSettingsNumPartners_Type = Integer32
_OmnisSettingsNumPartners_Object = MibScalar
omnisSettingsNumPartners = _OmnisSettingsNumPartners_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 3),
    _OmnisSettingsNumPartners_Type()
)
omnisSettingsNumPartners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisSettingsNumPartners.setStatus("mandatory")
_OmnisSettingsNumTerminals_Type = Integer32
_OmnisSettingsNumTerminals_Object = MibScalar
omnisSettingsNumTerminals = _OmnisSettingsNumTerminals_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 4),
    _OmnisSettingsNumTerminals_Type()
)
omnisSettingsNumTerminals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisSettingsNumTerminals.setStatus("mandatory")
_OmnisSettingsDSTMax_Type = Integer32
_OmnisSettingsDSTMax_Object = MibScalar
omnisSettingsDSTMax = _OmnisSettingsDSTMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 5),
    _OmnisSettingsDSTMax_Type()
)
omnisSettingsDSTMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsDSTMax.setStatus("mandatory")
_OmnisSettingsPTNMax_Type = Integer32
_OmnisSettingsPTNMax_Object = MibScalar
omnisSettingsPTNMax = _OmnisSettingsPTNMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 6),
    _OmnisSettingsPTNMax_Type()
)
omnisSettingsPTNMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsPTNMax.setStatus("mandatory")
_OmnisSettingsPACMax_Type = Integer32
_OmnisSettingsPACMax_Object = MibScalar
omnisSettingsPACMax = _OmnisSettingsPACMax_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 7),
    _OmnisSettingsPACMax_Type()
)
omnisSettingsPACMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsPACMax.setStatus("mandatory")


class _OmnisSettingsState_Type(Integer32):
    """Custom type omnisSettingsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("end", 3),
          ("open", 1),
          ("unknown", 99))
    )


_OmnisSettingsState_Type.__name__ = "Integer32"
_OmnisSettingsState_Object = MibScalar
omnisSettingsState = _OmnisSettingsState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 8),
    _OmnisSettingsState_Type()
)
omnisSettingsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisSettingsState.setStatus("mandatory")


class _OmnisSettingsAPASS_Type(DisplayString):
    """Custom type omnisSettingsAPASS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisSettingsAPASS_Type.__name__ = "DisplayString"
_OmnisSettingsAPASS_Object = MibScalar
omnisSettingsAPASS = _OmnisSettingsAPASS_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 9),
    _OmnisSettingsAPASS_Type()
)
omnisSettingsAPASS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsAPASS.setStatus("mandatory")


class _OmnisSettingsHOLD_Type(Integer32):
    """Custom type omnisSettingsHOLD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsHOLD_Type.__name__ = "Integer32"
_OmnisSettingsHOLD_Object = MibScalar
omnisSettingsHOLD = _OmnisSettingsHOLD_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 10),
    _OmnisSettingsHOLD_Type()
)
omnisSettingsHOLD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsHOLD.setStatus("mandatory")


class _OmnisSettingsHcyForm_Type(DisplayString):
    """Custom type omnisSettingsHcyForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OmnisSettingsHcyForm_Type.__name__ = "DisplayString"
_OmnisSettingsHcyForm_Object = MibScalar
omnisSettingsHcyForm = _OmnisSettingsHcyForm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 11),
    _OmnisSettingsHcyForm_Type()
)
omnisSettingsHcyForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsHcyForm.setStatus("mandatory")


class _OmnisSettingsHCopy_Type(DisplayString):
    """Custom type omnisSettingsHCopy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OmnisSettingsHCopy_Type.__name__ = "DisplayString"
_OmnisSettingsHCopy_Object = MibScalar
omnisSettingsHCopy = _OmnisSettingsHCopy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 12),
    _OmnisSettingsHCopy_Type()
)
omnisSettingsHCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsHCopy.setStatus("mandatory")


class _OmnisSettingsLogging_Type(Integer32):
    """Custom type omnisSettingsLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsLogging_Type.__name__ = "Integer32"
_OmnisSettingsLogging_Object = MibScalar
omnisSettingsLogging = _OmnisSettingsLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 13),
    _OmnisSettingsLogging_Type()
)
omnisSettingsLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsLogging.setStatus("mandatory")


class _OmnisSettingsChangeLogging_Type(Integer32):
    """Custom type omnisSettingsChangeLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("change", 1),
          ("unknown", 99))
    )


_OmnisSettingsChangeLogging_Type.__name__ = "Integer32"
_OmnisSettingsChangeLogging_Object = MibScalar
omnisSettingsChangeLogging = _OmnisSettingsChangeLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 14),
    _OmnisSettingsChangeLogging_Type()
)
omnisSettingsChangeLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsChangeLogging.setStatus("mandatory")


class _OmnisSettingsACK_Type(Integer32):
    """Custom type omnisSettingsACK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsACK_Type.__name__ = "Integer32"
_OmnisSettingsACK_Object = MibScalar
omnisSettingsACK = _OmnisSettingsACK_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 15),
    _OmnisSettingsACK_Type()
)
omnisSettingsACK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsACK.setStatus("mandatory")


class _OmnisSettingsMTAB_Type(DisplayString):
    """Custom type omnisSettingsMTAB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OmnisSettingsMTAB_Type.__name__ = "DisplayString"
_OmnisSettingsMTAB_Object = MibScalar
omnisSettingsMTAB = _OmnisSettingsMTAB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 16),
    _OmnisSettingsMTAB_Type()
)
omnisSettingsMTAB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsMTAB.setStatus("mandatory")


class _OmnisSettingsEXIT_Type(DisplayString):
    """Custom type omnisSettingsEXIT based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisSettingsEXIT_Type.__name__ = "DisplayString"
_OmnisSettingsEXIT_Object = MibScalar
omnisSettingsEXIT = _OmnisSettingsEXIT_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 17),
    _OmnisSettingsEXIT_Type()
)
omnisSettingsEXIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsEXIT.setStatus("mandatory")


class _OmnisSettingsOpncon_Type(Integer32):
    """Custom type omnisSettingsOpncon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dcl", 3),
          ("free", 2),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisSettingsOpncon_Type.__name__ = "Integer32"
_OmnisSettingsOpncon_Object = MibScalar
omnisSettingsOpncon = _OmnisSettingsOpncon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 18),
    _OmnisSettingsOpncon_Type()
)
omnisSettingsOpncon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsOpncon.setStatus("mandatory")


class _OmnisSettingsBreakKey_Type(Integer32):
    """Custom type omnisSettingsBreakKey based on Integer32"""
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
              13,
              14,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 98),
          ("unknown", 99))
    )


_OmnisSettingsBreakKey_Type.__name__ = "Integer32"
_OmnisSettingsBreakKey_Object = MibScalar
omnisSettingsBreakKey = _OmnisSettingsBreakKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 19),
    _OmnisSettingsBreakKey_Type()
)
omnisSettingsBreakKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsBreakKey.setStatus("mandatory")


class _OmnisSettingsCallKey_Type(Integer32):
    """Custom type omnisSettingsCallKey based on Integer32"""
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
              13,
              14,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 98),
          ("unknown", 99))
    )


_OmnisSettingsCallKey_Type.__name__ = "Integer32"
_OmnisSettingsCallKey_Object = MibScalar
omnisSettingsCallKey = _OmnisSettingsCallKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 20),
    _OmnisSettingsCallKey_Type()
)
omnisSettingsCallKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsCallKey.setStatus("mandatory")


class _OmnisSettingsCallInf_Type(Integer32):
    """Custom type omnisSettingsCallInf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsCallInf_Type.__name__ = "Integer32"
_OmnisSettingsCallInf_Object = MibScalar
omnisSettingsCallInf = _OmnisSettingsCallInf_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 21),
    _OmnisSettingsCallInf_Type()
)
omnisSettingsCallInf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsCallInf.setStatus("mandatory")


class _OmnisSettingsPac_Type(Integer32):
    """Custom type omnisSettingsPac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("no", 3),
          ("prefix", 2),
          ("std", 4),
          ("unknown", 99))
    )


_OmnisSettingsPac_Type.__name__ = "Integer32"
_OmnisSettingsPac_Object = MibScalar
omnisSettingsPac = _OmnisSettingsPac_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 22),
    _OmnisSettingsPac_Type()
)
omnisSettingsPac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsPac.setStatus("mandatory")


class _OmnisSettingsInputLog_Type(Integer32):
    """Custom type omnisSettingsInputLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("rec", 1),
          ("send", 2),
          ("std", 4),
          ("unknown", 99))
    )


_OmnisSettingsInputLog_Type.__name__ = "Integer32"
_OmnisSettingsInputLog_Object = MibScalar
omnisSettingsInputLog = _OmnisSettingsInputLog_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 23),
    _OmnisSettingsInputLog_Type()
)
omnisSettingsInputLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsInputLog.setStatus("mandatory")


class _OmnisSettingsOutputLog_Type(Integer32):
    """Custom type omnisSettingsOutputLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("rec", 1),
          ("send", 2),
          ("std", 4),
          ("unknown", 99))
    )


_OmnisSettingsOutputLog_Type.__name__ = "Integer32"
_OmnisSettingsOutputLog_Object = MibScalar
omnisSettingsOutputLog = _OmnisSettingsOutputLog_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 24),
    _OmnisSettingsOutputLog_Type()
)
omnisSettingsOutputLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsOutputLog.setStatus("mandatory")


class _OmnisSettingsLine25_Type(Integer32):
    """Custom type omnisSettingsLine25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("omnis", 4),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsLine25_Type.__name__ = "Integer32"
_OmnisSettingsLine25_Object = MibScalar
omnisSettingsLine25 = _OmnisSettingsLine25_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 25),
    _OmnisSettingsLine25_Type()
)
omnisSettingsLine25.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsLine25.setStatus("mandatory")


class _OmnisSettingsDisMod_Type(Integer32):
    """Custom type omnisSettingsDisMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("omnis", 2),
          ("system", 1),
          ("unknown", 99))
    )


_OmnisSettingsDisMod_Type.__name__ = "Integer32"
_OmnisSettingsDisMod_Object = MibScalar
omnisSettingsDisMod = _OmnisSettingsDisMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 26),
    _OmnisSettingsDisMod_Type()
)
omnisSettingsDisMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsDisMod.setStatus("mandatory")


class _OmnisSettingsKPAC_Type(Integer32):
    """Custom type omnisSettingsKPAC based on Integer32"""
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
              13,
              14,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 98),
          ("unknown", 99))
    )


_OmnisSettingsKPAC_Type.__name__ = "Integer32"
_OmnisSettingsKPAC_Object = MibScalar
omnisSettingsKPAC = _OmnisSettingsKPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 27),
    _OmnisSettingsKPAC_Type()
)
omnisSettingsKPAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsKPAC.setStatus("mandatory")


class _OmnisSettingsExitPri_Type(Integer32):
    """Custom type omnisSettingsExitPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("par-opt-set", 1),
          ("set-par-opt", 2),
          ("unknown", 99))
    )


_OmnisSettingsExitPri_Type.__name__ = "Integer32"
_OmnisSettingsExitPri_Object = MibScalar
omnisSettingsExitPri = _OmnisSettingsExitPri_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 28),
    _OmnisSettingsExitPri_Type()
)
omnisSettingsExitPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsExitPri.setStatus("mandatory")


class _OmnisSettingsReply_Type(Integer32):
    """Custom type omnisSettingsReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("restricted", 1),
          ("unknown", 99))
    )


_OmnisSettingsReply_Type.__name__ = "Integer32"
_OmnisSettingsReply_Object = MibScalar
omnisSettingsReply = _OmnisSettingsReply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 29),
    _OmnisSettingsReply_Type()
)
omnisSettingsReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsReply.setStatus("mandatory")


class _OmnisSettingsExitAuth_Type(Integer32):
    """Custom type omnisSettingsExitAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adm", 2),
          ("all", 1),
          ("unknown", 99))
    )


_OmnisSettingsExitAuth_Type.__name__ = "Integer32"
_OmnisSettingsExitAuth_Object = MibScalar
omnisSettingsExitAuth = _OmnisSettingsExitAuth_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 30),
    _OmnisSettingsExitAuth_Type()
)
omnisSettingsExitAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsExitAuth.setStatus("mandatory")


class _OmnisSettingsLoggPri_Type(Integer32):
    """Custom type omnisSettingsLoggPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("par-opt-set", 1),
          ("set-par-opt", 2),
          ("unknown", 99))
    )


_OmnisSettingsLoggPri_Type.__name__ = "Integer32"
_OmnisSettingsLoggPri_Object = MibScalar
omnisSettingsLoggPri = _OmnisSettingsLoggPri_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 31),
    _OmnisSettingsLoggPri_Type()
)
omnisSettingsLoggPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsLoggPri.setStatus("mandatory")


class _OmnisSettingsAudit_Type(Integer32):
    """Custom type omnisSettingsAudit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("unknown", 99))
    )


_OmnisSettingsAudit_Type.__name__ = "Integer32"
_OmnisSettingsAudit_Object = MibScalar
omnisSettingsAudit = _OmnisSettingsAudit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 32),
    _OmnisSettingsAudit_Type()
)
omnisSettingsAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsAudit.setStatus("mandatory")


class _OmnisSettingsMDefAuth_Type(Integer32):
    """Custom type omnisSettingsMDefAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adm", 2),
          ("all", 1),
          ("unknown", 99))
    )


_OmnisSettingsMDefAuth_Type.__name__ = "Integer32"
_OmnisSettingsMDefAuth_Object = MibScalar
omnisSettingsMDefAuth = _OmnisSettingsMDefAuth_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 33),
    _OmnisSettingsMDefAuth_Type()
)
omnisSettingsMDefAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsMDefAuth.setStatus("mandatory")


class _OmnisSettingsHoldPri_Type(Integer32):
    """Custom type omnisSettingsHoldPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("opt-set", 2),
          ("set-opt", 1),
          ("unknown", 99))
    )


_OmnisSettingsHoldPri_Type.__name__ = "Integer32"
_OmnisSettingsHoldPri_Object = MibScalar
omnisSettingsHoldPri = _OmnisSettingsHoldPri_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 34),
    _OmnisSettingsHoldPri_Type()
)
omnisSettingsHoldPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsHoldPri.setStatus("mandatory")


class _OmnisSettingsInsave_Type(Integer32):
    """Custom type omnisSettingsInsave based on Integer32"""
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
              13,
              14,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("f1", 21),
          ("f10", 30),
          ("f11", 31),
          ("f12", 32),
          ("f13", 33),
          ("f14", 34),
          ("f15", 35),
          ("f16", 36),
          ("f17", 37),
          ("f18", 38),
          ("f19", 39),
          ("f2", 22),
          ("f20", 40),
          ("f21", 41),
          ("f22", 42),
          ("f23", 43),
          ("f24", 44),
          ("f3", 23),
          ("f4", 24),
          ("f5", 25),
          ("f6", 26),
          ("f7", 27),
          ("f8", 28),
          ("f9", 29),
          ("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisSettingsInsave_Type.__name__ = "Integer32"
_OmnisSettingsInsave_Object = MibScalar
omnisSettingsInsave = _OmnisSettingsInsave_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 35),
    _OmnisSettingsInsave_Type()
)
omnisSettingsInsave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsInsave.setStatus("mandatory")


class _OmnisSettingsOpnStart_Type(Integer32):
    """Custom type omnisSettingsOpnStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsOpnStart_Type.__name__ = "Integer32"
_OmnisSettingsOpnStart_Object = MibScalar
omnisSettingsOpnStart = _OmnisSettingsOpnStart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 36),
    _OmnisSettingsOpnStart_Type()
)
omnisSettingsOpnStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsOpnStart.setStatus("mandatory")


class _OmnisSettingsExclPartner_Type(Integer32):
    """Custom type omnisSettingsExclPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisSettingsExclPartner_Type.__name__ = "Integer32"
_OmnisSettingsExclPartner_Object = MibScalar
omnisSettingsExclPartner = _OmnisSettingsExclPartner_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 37),
    _OmnisSettingsExclPartner_Type()
)
omnisSettingsExclPartner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsExclPartner.setStatus("mandatory")


class _OmnisSettingsSave_Type(Integer32):
    """Custom type omnisSettingsSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("no", 4),
          ("pkey", 1),
          ("screen", 2),
          ("std", 5),
          ("unknown", 99))
    )


_OmnisSettingsSave_Type.__name__ = "Integer32"
_OmnisSettingsSave_Object = MibScalar
omnisSettingsSave = _OmnisSettingsSave_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 38),
    _OmnisSettingsSave_Type()
)
omnisSettingsSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsSave.setStatus("mandatory")
_OmnisSettingsMessageALL_Type = DisplayString
_OmnisSettingsMessageALL_Object = MibScalar
omnisSettingsMessageALL = _OmnisSettingsMessageALL_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 39),
    _OmnisSettingsMessageALL_Type()
)
omnisSettingsMessageALL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsMessageALL.setStatus("mandatory")
_OmnisSettingsMessageADM_Type = DisplayString
_OmnisSettingsMessageADM_Object = MibScalar
omnisSettingsMessageADM = _OmnisSettingsMessageADM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 40),
    _OmnisSettingsMessageADM_Type()
)
omnisSettingsMessageADM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsMessageADM.setStatus("mandatory")


class _OmnisSettingsEnd_Type(Integer32):
    """Custom type omnisSettingsEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("end", 1),
          ("unknown", 99))
    )


_OmnisSettingsEnd_Type.__name__ = "Integer32"
_OmnisSettingsEnd_Object = MibScalar
omnisSettingsEnd = _OmnisSettingsEnd_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 41),
    _OmnisSettingsEnd_Type()
)
omnisSettingsEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsEnd.setStatus("mandatory")
_OmnisSettingsEndPassw_Type = DisplayString
_OmnisSettingsEndPassw_Object = MibScalar
omnisSettingsEndPassw = _OmnisSettingsEndPassw_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 2, 42),
    _OmnisSettingsEndPassw_Type()
)
omnisSettingsEndPassw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisSettingsEndPassw.setStatus("mandatory")
_SniOmnisParameters_ObjectIdentity = ObjectIdentity
sniOmnisParameters = _SniOmnisParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3)
)


class _OmnisParametersAppName_Type(DisplayString):
    """Custom type omnisParametersAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisParametersAppName_Type.__name__ = "DisplayString"
_OmnisParametersAppName_Object = MibScalar
omnisParametersAppName = _OmnisParametersAppName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 1),
    _OmnisParametersAppName_Type()
)
omnisParametersAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersAppName.setStatus("mandatory")


class _OmnisParametersAppNameISO_Type(DisplayString):
    """Custom type omnisParametersAppNameISO based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisParametersAppNameISO_Type.__name__ = "DisplayString"
_OmnisParametersAppNameISO_Object = MibScalar
omnisParametersAppNameISO = _OmnisParametersAppNameISO_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 2),
    _OmnisParametersAppNameISO_Type()
)
omnisParametersAppNameISO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersAppNameISO.setStatus("mandatory")


class _OmnisParametersPrefix_Type(DisplayString):
    """Custom type omnisParametersPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_OmnisParametersPrefix_Type.__name__ = "DisplayString"
_OmnisParametersPrefix_Object = MibScalar
omnisParametersPrefix = _OmnisParametersPrefix_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 3),
    _OmnisParametersPrefix_Type()
)
omnisParametersPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersPrefix.setStatus("mandatory")


class _OmnisParametersProName_Type(DisplayString):
    """Custom type omnisParametersProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisParametersProName_Type.__name__ = "DisplayString"
_OmnisParametersProName_Object = MibScalar
omnisParametersProName = _OmnisParametersProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 4),
    _OmnisParametersProName_Type()
)
omnisParametersProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersProName.setStatus("mandatory")


class _OmnisParametersVirtProName_Type(DisplayString):
    """Custom type omnisParametersVirtProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisParametersVirtProName_Type.__name__ = "DisplayString"
_OmnisParametersVirtProName_Object = MibScalar
omnisParametersVirtProName = _OmnisParametersVirtProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 5),
    _OmnisParametersVirtProName_Type()
)
omnisParametersVirtProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersVirtProName.setStatus("mandatory")


class _OmnisParametersLoggingFile_Type(DisplayString):
    """Custom type omnisParametersLoggingFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersLoggingFile_Type.__name__ = "DisplayString"
_OmnisParametersLoggingFile_Object = MibScalar
omnisParametersLoggingFile = _OmnisParametersLoggingFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 6),
    _OmnisParametersLoggingFile_Type()
)
omnisParametersLoggingFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersLoggingFile.setStatus("mandatory")


class _OmnisParametersStartupFile_Type(DisplayString):
    """Custom type omnisParametersStartupFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersStartupFile_Type.__name__ = "DisplayString"
_OmnisParametersStartupFile_Object = MibScalar
omnisParametersStartupFile = _OmnisParametersStartupFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 7),
    _OmnisParametersStartupFile_Type()
)
omnisParametersStartupFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersStartupFile.setStatus("mandatory")


class _OmnisParametersConfigFile_Type(DisplayString):
    """Custom type omnisParametersConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersConfigFile_Type.__name__ = "DisplayString"
_OmnisParametersConfigFile_Object = MibScalar
omnisParametersConfigFile = _OmnisParametersConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 8),
    _OmnisParametersConfigFile_Type()
)
omnisParametersConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersConfigFile.setStatus("mandatory")


class _OmnisParametersConfUpdate_Type(Integer32):
    """Custom type omnisParametersConfUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_OmnisParametersConfUpdate_Type.__name__ = "Integer32"
_OmnisParametersConfUpdate_Object = MibScalar
omnisParametersConfUpdate = _OmnisParametersConfUpdate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 9),
    _OmnisParametersConfUpdate_Type()
)
omnisParametersConfUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersConfUpdate.setStatus("mandatory")


class _OmnisParametersModulFile_Type(DisplayString):
    """Custom type omnisParametersModulFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersModulFile_Type.__name__ = "DisplayString"
_OmnisParametersModulFile_Object = MibScalar
omnisParametersModulFile = _OmnisParametersModulFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 10),
    _OmnisParametersModulFile_Type()
)
omnisParametersModulFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersModulFile.setStatus("mandatory")


class _OmnisParametersBulletinFile_Type(DisplayString):
    """Custom type omnisParametersBulletinFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersBulletinFile_Type.__name__ = "DisplayString"
_OmnisParametersBulletinFile_Object = MibScalar
omnisParametersBulletinFile = _OmnisParametersBulletinFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 11),
    _OmnisParametersBulletinFile_Type()
)
omnisParametersBulletinFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersBulletinFile.setStatus("mandatory")


class _OmnisParametersTextFile_Type(DisplayString):
    """Custom type omnisParametersTextFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersTextFile_Type.__name__ = "DisplayString"
_OmnisParametersTextFile_Object = MibScalar
omnisParametersTextFile = _OmnisParametersTextFile_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 12),
    _OmnisParametersTextFile_Type()
)
omnisParametersTextFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersTextFile.setStatus("mandatory")


class _OmnisParametersPagePool_Type(DisplayString):
    """Custom type omnisParametersPagePool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_OmnisParametersPagePool_Type.__name__ = "DisplayString"
_OmnisParametersPagePool_Object = MibScalar
omnisParametersPagePool = _OmnisParametersPagePool_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 13),
    _OmnisParametersPagePool_Type()
)
omnisParametersPagePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersPagePool.setStatus("mandatory")
_OmnisParametersIOAreaLength_Type = Integer32
_OmnisParametersIOAreaLength_Object = MibScalar
omnisParametersIOAreaLength = _OmnisParametersIOAreaLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 14),
    _OmnisParametersIOAreaLength_Type()
)
omnisParametersIOAreaLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersIOAreaLength.setStatus("mandatory")
_OmnisParametersTWorkLength_Type = Integer32
_OmnisParametersTWorkLength_Object = MibScalar
omnisParametersTWorkLength = _OmnisParametersTWorkLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 15),
    _OmnisParametersTWorkLength_Type()
)
omnisParametersTWorkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersTWorkLength.setStatus("mandatory")
_OmnisParametersPWorkLength_Type = Integer32
_OmnisParametersPWorkLength_Object = MibScalar
omnisParametersPWorkLength = _OmnisParametersPWorkLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 16),
    _OmnisParametersPWorkLength_Type()
)
omnisParametersPWorkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersPWorkLength.setStatus("mandatory")
_OmnisParametersTextKeyLength_Type = Integer32
_OmnisParametersTextKeyLength_Object = MibScalar
omnisParametersTextKeyLength = _OmnisParametersTextKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 17),
    _OmnisParametersTextKeyLength_Type()
)
omnisParametersTextKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersTextKeyLength.setStatus("mandatory")


class _OmnisParametersSecurityLevel_Type(Integer32):
    """Custom type omnisParametersSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 3),
          ("medium", 2),
          ("unknown", 99))
    )


_OmnisParametersSecurityLevel_Type.__name__ = "Integer32"
_OmnisParametersSecurityLevel_Object = MibScalar
omnisParametersSecurityLevel = _OmnisParametersSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 18),
    _OmnisParametersSecurityLevel_Type()
)
omnisParametersSecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersSecurityLevel.setStatus("mandatory")


class _OmnisParametersDCAMIntVers_Type(DisplayString):
    """Custom type omnisParametersDCAMIntVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OmnisParametersDCAMIntVers_Type.__name__ = "DisplayString"
_OmnisParametersDCAMIntVers_Object = MibScalar
omnisParametersDCAMIntVers = _OmnisParametersDCAMIntVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 19),
    _OmnisParametersDCAMIntVers_Type()
)
omnisParametersDCAMIntVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersDCAMIntVers.setStatus("mandatory")


class _OmnisParametersVTSUBVers_Type(DisplayString):
    """Custom type omnisParametersVTSUBVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_OmnisParametersVTSUBVers_Type.__name__ = "DisplayString"
_OmnisParametersVTSUBVers_Object = MibScalar
omnisParametersVTSUBVers = _OmnisParametersVTSUBVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 20),
    _OmnisParametersVTSUBVers_Type()
)
omnisParametersVTSUBVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersVTSUBVers.setStatus("mandatory")


class _OmnisParametersVTSUCBVers_Type(DisplayString):
    """Custom type omnisParametersVTSUCBVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_OmnisParametersVTSUCBVers_Type.__name__ = "DisplayString"
_OmnisParametersVTSUCBVers_Object = MibScalar
omnisParametersVTSUCBVers = _OmnisParametersVTSUCBVers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 21),
    _OmnisParametersVTSUCBVers_Type()
)
omnisParametersVTSUCBVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisParametersVTSUCBVers.setStatus("mandatory")


class _OmnisParametersCMD_Type(DisplayString):
    """Custom type omnisParametersCMD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_OmnisParametersCMD_Type.__name__ = "DisplayString"
_OmnisParametersCMD_Object = MibScalar
omnisParametersCMD = _OmnisParametersCMD_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 22),
    _OmnisParametersCMD_Type()
)
omnisParametersCMD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersCMD.setStatus("mandatory")


class _OmnisParametersDump_Type(Integer32):
    """Custom type omnisParametersDump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("unknown", 99))
    )


_OmnisParametersDump_Type.__name__ = "Integer32"
_OmnisParametersDump_Object = MibScalar
omnisParametersDump = _OmnisParametersDump_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 23),
    _OmnisParametersDump_Type()
)
omnisParametersDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersDump.setStatus("mandatory")


class _OmnisParametersDumpMsgNr_Type(DisplayString):
    """Custom type omnisParametersDumpMsgNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_OmnisParametersDumpMsgNr_Type.__name__ = "DisplayString"
_OmnisParametersDumpMsgNr_Object = MibScalar
omnisParametersDumpMsgNr = _OmnisParametersDumpMsgNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 24),
    _OmnisParametersDumpMsgNr_Type()
)
omnisParametersDumpMsgNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersDumpMsgNr.setStatus("mandatory")


class _OmnisParametersDumpInsert_Type(DisplayString):
    """Custom type omnisParametersDumpInsert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_OmnisParametersDumpInsert_Type.__name__ = "DisplayString"
_OmnisParametersDumpInsert_Object = MibScalar
omnisParametersDumpInsert = _OmnisParametersDumpInsert_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 25),
    _OmnisParametersDumpInsert_Type()
)
omnisParametersDumpInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersDumpInsert.setStatus("mandatory")
_OmnisParametersDumpInsertNr_Type = Integer32
_OmnisParametersDumpInsertNr_Object = MibScalar
omnisParametersDumpInsertNr = _OmnisParametersDumpInsertNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 3, 26),
    _OmnisParametersDumpInsertNr_Type()
)
omnisParametersDumpInsertNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisParametersDumpInsertNr.setStatus("mandatory")
_SniOmnisTerminals_ObjectIdentity = ObjectIdentity
sniOmnisTerminals = _SniOmnisTerminals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4)
)


class _OmnisTerminalsStatus_Type(Integer32):
    """Custom type omnisTerminalsStatus based on Integer32"""
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
        *(("activ", 2),
          ("all", 1),
          ("hold", 3),
          ("inactiv", 4))
    )


_OmnisTerminalsStatus_Type.__name__ = "Integer32"
_OmnisTerminalsStatus_Object = MibScalar
omnisTerminalsStatus = _OmnisTerminalsStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 1),
    _OmnisTerminalsStatus_Type()
)
omnisTerminalsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTerminalsStatus.setStatus("mandatory")
_OmnisTerminalsTabNum_Type = Integer32
_OmnisTerminalsTabNum_Object = MibScalar
omnisTerminalsTabNum = _OmnisTerminalsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 2),
    _OmnisTerminalsTabNum_Type()
)
omnisTerminalsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsTabNum.setStatus("mandatory")
_OmnisTerminalsTable_Object = MibTable
omnisTerminalsTable = _OmnisTerminalsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3)
)
if mibBuilder.loadTexts:
    omnisTerminalsTable.setStatus("mandatory")
_OmnisTerminalsEntry_Object = MibTableRow
omnisTerminalsEntry = _OmnisTerminalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1)
)
omnisTerminalsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisTerminalsTID"),
)
if mibBuilder.loadTexts:
    omnisTerminalsEntry.setStatus("mandatory")
_OmnisTerminalsTID_Type = Integer32
_OmnisTerminalsTID_Object = MibTableColumn
omnisTerminalsTID = _OmnisTerminalsTID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 1),
    _OmnisTerminalsTID_Type()
)
omnisTerminalsTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTerminalsTID.setStatus("mandatory")


class _OmnisTerminalsPtnName_Type(DisplayString):
    """Custom type omnisTerminalsPtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisTerminalsPtnName_Type.__name__ = "DisplayString"
_OmnisTerminalsPtnName_Object = MibTableColumn
omnisTerminalsPtnName = _OmnisTerminalsPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 2),
    _OmnisTerminalsPtnName_Type()
)
omnisTerminalsPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsPtnName.setStatus("mandatory")


class _OmnisTerminalsProName_Type(DisplayString):
    """Custom type omnisTerminalsProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisTerminalsProName_Type.__name__ = "DisplayString"
_OmnisTerminalsProName_Object = MibTableColumn
omnisTerminalsProName = _OmnisTerminalsProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 3),
    _OmnisTerminalsProName_Type()
)
omnisTerminalsProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsProName.setStatus("mandatory")


class _OmnisTerminalsTyp_Type(Integer32):
    """Custom type omnisTerminalsTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("appl", 2),
          ("cons", 4),
          ("skp", 3),
          ("term", 1),
          ("unknown", 99))
    )


_OmnisTerminalsTyp_Type.__name__ = "Integer32"
_OmnisTerminalsTyp_Object = MibTableColumn
omnisTerminalsTyp = _OmnisTerminalsTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 4),
    _OmnisTerminalsTyp_Type()
)
omnisTerminalsTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsTyp.setStatus("mandatory")


class _OmnisTerminalsState_Type(Integer32):
    """Custom type omnisTerminalsState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 3),
          ("cancel", 8),
          ("cls", 5),
          ("decl", 1),
          ("hold", 6),
          ("inact", 7),
          ("los", 4),
          ("opn", 2),
          ("unknown", 99))
    )


_OmnisTerminalsState_Type.__name__ = "Integer32"
_OmnisTerminalsState_Object = MibTableColumn
omnisTerminalsState = _OmnisTerminalsState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 5),
    _OmnisTerminalsState_Type()
)
omnisTerminalsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTerminalsState.setStatus("mandatory")


class _OmnisTerminalsRoute_Type(Integer32):
    """Custom type omnisTerminalsRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dir", 2),
          ("ind", 1),
          ("unknown", 99))
    )


_OmnisTerminalsRoute_Type.__name__ = "Integer32"
_OmnisTerminalsRoute_Object = MibTableColumn
omnisTerminalsRoute = _OmnisTerminalsRoute_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 6),
    _OmnisTerminalsRoute_Type()
)
omnisTerminalsRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsRoute.setStatus("mandatory")


class _OmnisTerminalsKPAC_Type(Integer32):
    """Custom type omnisTerminalsKPAC based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisTerminalsKPAC_Type.__name__ = "Integer32"
_OmnisTerminalsKPAC_Object = MibTableColumn
omnisTerminalsKPAC = _OmnisTerminalsKPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 7),
    _OmnisTerminalsKPAC_Type()
)
omnisTerminalsKPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsKPAC.setStatus("mandatory")


class _OmnisTerminalsUser_Type(DisplayString):
    """Custom type omnisTerminalsUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisTerminalsUser_Type.__name__ = "DisplayString"
_OmnisTerminalsUser_Object = MibTableColumn
omnisTerminalsUser = _OmnisTerminalsUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 8),
    _OmnisTerminalsUser_Type()
)
omnisTerminalsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalsUser.setStatus("mandatory")
_OmnisTerminalsMessage_Type = DisplayString
_OmnisTerminalsMessage_Object = MibTableColumn
omnisTerminalsMessage = _OmnisTerminalsMessage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 4, 3, 1, 9),
    _OmnisTerminalsMessage_Type()
)
omnisTerminalsMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTerminalsMessage.setStatus("mandatory")
_SniOmnisTerminalInfo_ObjectIdentity = ObjectIdentity
sniOmnisTerminalInfo = _SniOmnisTerminalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5)
)
_OmnisTerminalInfoTID_Type = Integer32
_OmnisTerminalInfoTID_Object = MibScalar
omnisTerminalInfoTID = _OmnisTerminalInfoTID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 1),
    _OmnisTerminalInfoTID_Type()
)
omnisTerminalInfoTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTerminalInfoTID.setStatus("mandatory")


class _OmnisTerminalInfoPtnName_Type(DisplayString):
    """Custom type omnisTerminalInfoPtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisTerminalInfoPtnName_Type.__name__ = "DisplayString"
_OmnisTerminalInfoPtnName_Object = MibScalar
omnisTerminalInfoPtnName = _OmnisTerminalInfoPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 2),
    _OmnisTerminalInfoPtnName_Type()
)
omnisTerminalInfoPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoPtnName.setStatus("mandatory")


class _OmnisTerminalInfoProName_Type(DisplayString):
    """Custom type omnisTerminalInfoProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisTerminalInfoProName_Type.__name__ = "DisplayString"
_OmnisTerminalInfoProName_Object = MibScalar
omnisTerminalInfoProName = _OmnisTerminalInfoProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 3),
    _OmnisTerminalInfoProName_Type()
)
omnisTerminalInfoProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoProName.setStatus("mandatory")


class _OmnisTerminalInfoTyp_Type(Integer32):
    """Custom type omnisTerminalInfoTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("appl", 2),
          ("cons", 4),
          ("skp", 3),
          ("term", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoTyp_Type.__name__ = "Integer32"
_OmnisTerminalInfoTyp_Object = MibScalar
omnisTerminalInfoTyp = _OmnisTerminalInfoTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 4),
    _OmnisTerminalInfoTyp_Type()
)
omnisTerminalInfoTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoTyp.setStatus("mandatory")


class _OmnisTerminalInfoState_Type(Integer32):
    """Custom type omnisTerminalInfoState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 3),
          ("cls", 5),
          ("decl", 1),
          ("hold", 6),
          ("inact", 7),
          ("los", 4),
          ("opn", 2),
          ("unknown", 99))
    )


_OmnisTerminalInfoState_Type.__name__ = "Integer32"
_OmnisTerminalInfoState_Object = MibScalar
omnisTerminalInfoState = _OmnisTerminalInfoState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 5),
    _OmnisTerminalInfoState_Type()
)
omnisTerminalInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoState.setStatus("mandatory")


class _OmnisTerminalInfoRoute_Type(Integer32):
    """Custom type omnisTerminalInfoRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dir", 2),
          ("ind", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoRoute_Type.__name__ = "Integer32"
_OmnisTerminalInfoRoute_Object = MibScalar
omnisTerminalInfoRoute = _OmnisTerminalInfoRoute_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 6),
    _OmnisTerminalInfoRoute_Type()
)
omnisTerminalInfoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoRoute.setStatus("mandatory")


class _OmnisTerminalInfoKPAC_Type(Integer32):
    """Custom type omnisTerminalInfoKPAC based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisTerminalInfoKPAC_Type.__name__ = "Integer32"
_OmnisTerminalInfoKPAC_Object = MibScalar
omnisTerminalInfoKPAC = _OmnisTerminalInfoKPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 7),
    _OmnisTerminalInfoKPAC_Type()
)
omnisTerminalInfoKPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoKPAC.setStatus("mandatory")
_OmnisTerminalInfoUser_Type = DisplayString
_OmnisTerminalInfoUser_Object = MibScalar
omnisTerminalInfoUser = _OmnisTerminalInfoUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 8),
    _OmnisTerminalInfoUser_Type()
)
omnisTerminalInfoUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoUser.setStatus("mandatory")


class _OmnisTerminalInfoPAC_Type(Integer32):
    """Custom type omnisTerminalInfoPAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("line", 2),
          ("no", 1),
          ("prefix", 3),
          ("std", 4),
          ("unknown", 99))
    )


_OmnisTerminalInfoPAC_Type.__name__ = "Integer32"
_OmnisTerminalInfoPAC_Object = MibScalar
omnisTerminalInfoPAC = _OmnisTerminalInfoPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 9),
    _OmnisTerminalInfoPAC_Type()
)
omnisTerminalInfoPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoPAC.setStatus("mandatory")


class _OmnisTerminalInfoADM_Type(Integer32):
    """Custom type omnisTerminalInfoADM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisTerminalInfoADM_Type.__name__ = "Integer32"
_OmnisTerminalInfoADM_Object = MibScalar
omnisTerminalInfoADM = _OmnisTerminalInfoADM_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 10),
    _OmnisTerminalInfoADM_Type()
)
omnisTerminalInfoADM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoADM.setStatus("mandatory")


class _OmnisTerminalInfoOPass_Type(Integer32):
    """Custom type omnisTerminalInfoOPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisTerminalInfoOPass_Type.__name__ = "Integer32"
_OmnisTerminalInfoOPass_Object = MibScalar
omnisTerminalInfoOPass = _OmnisTerminalInfoOPass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 11),
    _OmnisTerminalInfoOPass_Type()
)
omnisTerminalInfoOPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoOPass.setStatus("mandatory")
_OmnisTerminalInfoMTAB_Type = DisplayString
_OmnisTerminalInfoMTAB_Object = MibScalar
omnisTerminalInfoMTAB = _OmnisTerminalInfoMTAB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 12),
    _OmnisTerminalInfoMTAB_Type()
)
omnisTerminalInfoMTAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoMTAB.setStatus("mandatory")
_OmnisTerminalInfoExit_Type = DisplayString
_OmnisTerminalInfoExit_Object = MibScalar
omnisTerminalInfoExit = _OmnisTerminalInfoExit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 13),
    _OmnisTerminalInfoExit_Type()
)
omnisTerminalInfoExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoExit.setStatus("mandatory")


class _OmnisTerminalInfoHold_Type(Integer32):
    """Custom type omnisTerminalInfoHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoHold_Type.__name__ = "Integer32"
_OmnisTerminalInfoHold_Object = MibScalar
omnisTerminalInfoHold = _OmnisTerminalInfoHold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 14),
    _OmnisTerminalInfoHold_Type()
)
omnisTerminalInfoHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoHold.setStatus("mandatory")


class _OmnisTerminalInfoChange_Type(Integer32):
    """Custom type omnisTerminalInfoChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoChange_Type.__name__ = "Integer32"
_OmnisTerminalInfoChange_Object = MibScalar
omnisTerminalInfoChange = _OmnisTerminalInfoChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 15),
    _OmnisTerminalInfoChange_Type()
)
omnisTerminalInfoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoChange.setStatus("mandatory")
_OmnisTerminalInfoHcopy_Type = DisplayString
_OmnisTerminalInfoHcopy_Object = MibScalar
omnisTerminalInfoHcopy = _OmnisTerminalInfoHcopy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 16),
    _OmnisTerminalInfoHcopy_Type()
)
omnisTerminalInfoHcopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoHcopy.setStatus("mandatory")


class _OmnisTerminalInfoAck_Type(Integer32):
    """Custom type omnisTerminalInfoAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoAck_Type.__name__ = "Integer32"
_OmnisTerminalInfoAck_Object = MibScalar
omnisTerminalInfoAck = _OmnisTerminalInfoAck_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 17),
    _OmnisTerminalInfoAck_Type()
)
omnisTerminalInfoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoAck.setStatus("mandatory")


class _OmnisTerminalInfoListening_Type(DisplayString):
    """Custom type omnisTerminalInfoListening based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisTerminalInfoListening_Type.__name__ = "DisplayString"
_OmnisTerminalInfoListening_Object = MibScalar
omnisTerminalInfoListening = _OmnisTerminalInfoListening_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 18),
    _OmnisTerminalInfoListening_Type()
)
omnisTerminalInfoListening.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoListening.setStatus("mandatory")


class _OmnisTerminalInfoColour_Type(Integer32):
    """Custom type omnisTerminalInfoColour based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 2),
          ("green", 3),
          ("magenta", 5),
          ("red", 6),
          ("unknown", 99),
          ("white", 7),
          ("yellow", 4))
    )


_OmnisTerminalInfoColour_Type.__name__ = "Integer32"
_OmnisTerminalInfoColour_Object = MibScalar
omnisTerminalInfoColour = _OmnisTerminalInfoColour_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 19),
    _OmnisTerminalInfoColour_Type()
)
omnisTerminalInfoColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoColour.setStatus("mandatory")


class _OmnisTerminalInfoLogging_Type(Integer32):
    """Custom type omnisTerminalInfoLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoLogging_Type.__name__ = "Integer32"
_OmnisTerminalInfoLogging_Object = MibScalar
omnisTerminalInfoLogging = _OmnisTerminalInfoLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 20),
    _OmnisTerminalInfoLogging_Type()
)
omnisTerminalInfoLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoLogging.setStatus("mandatory")


class _OmnisTerminalInfoBerID_Type(Integer32):
    """Custom type omnisTerminalInfoBerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoBerID_Type.__name__ = "Integer32"
_OmnisTerminalInfoBerID_Object = MibScalar
omnisTerminalInfoBerID = _OmnisTerminalInfoBerID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 21),
    _OmnisTerminalInfoBerID_Type()
)
omnisTerminalInfoBerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoBerID.setStatus("mandatory")


class _OmnisTerminalInfoDeclared_Type(Integer32):
    """Custom type omnisTerminalInfoDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoDeclared_Type.__name__ = "Integer32"
_OmnisTerminalInfoDeclared_Object = MibScalar
omnisTerminalInfoDeclared = _OmnisTerminalInfoDeclared_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 22),
    _OmnisTerminalInfoDeclared_Type()
)
omnisTerminalInfoDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoDeclared.setStatus("mandatory")


class _OmnisTerminalInfoBreakKey_Type(Integer32):
    """Custom type omnisTerminalInfoBreakKey based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisTerminalInfoBreakKey_Type.__name__ = "Integer32"
_OmnisTerminalInfoBreakKey_Object = MibScalar
omnisTerminalInfoBreakKey = _OmnisTerminalInfoBreakKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 23),
    _OmnisTerminalInfoBreakKey_Type()
)
omnisTerminalInfoBreakKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoBreakKey.setStatus("mandatory")


class _OmnisTerminalInfoCallKey_Type(Integer32):
    """Custom type omnisTerminalInfoCallKey based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisTerminalInfoCallKey_Type.__name__ = "Integer32"
_OmnisTerminalInfoCallKey_Object = MibScalar
omnisTerminalInfoCallKey = _OmnisTerminalInfoCallKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 24),
    _OmnisTerminalInfoCallKey_Type()
)
omnisTerminalInfoCallKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoCallKey.setStatus("mandatory")


class _OmnisTerminalInfoCallInf_Type(Integer32):
    """Custom type omnisTerminalInfoCallInf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoCallInf_Type.__name__ = "Integer32"
_OmnisTerminalInfoCallInf_Object = MibScalar
omnisTerminalInfoCallInf = _OmnisTerminalInfoCallInf_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 25),
    _OmnisTerminalInfoCallInf_Type()
)
omnisTerminalInfoCallInf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoCallInf.setStatus("mandatory")


class _OmnisTerminalInfoDisMod_Type(Integer32):
    """Custom type omnisTerminalInfoDisMod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 4),
          ("omnis", 3),
          ("std", 1),
          ("system", 2),
          ("unknown", 99))
    )


_OmnisTerminalInfoDisMod_Type.__name__ = "Integer32"
_OmnisTerminalInfoDisMod_Object = MibScalar
omnisTerminalInfoDisMod = _OmnisTerminalInfoDisMod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 26),
    _OmnisTerminalInfoDisMod_Type()
)
omnisTerminalInfoDisMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoDisMod.setStatus("mandatory")


class _OmnisTerminalInfoConnect_Type(Integer32):
    """Custom type omnisTerminalInfoConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("logon", 1),
          ("start", 2),
          ("unknown", 99))
    )


_OmnisTerminalInfoConnect_Type.__name__ = "Integer32"
_OmnisTerminalInfoConnect_Object = MibScalar
omnisTerminalInfoConnect = _OmnisTerminalInfoConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 27),
    _OmnisTerminalInfoConnect_Type()
)
omnisTerminalInfoConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoConnect.setStatus("mandatory")


class _OmnisTerminalInfoOpncon_Type(Integer32):
    """Custom type omnisTerminalInfoOpncon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dcl", 3),
          ("free", 2),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoOpncon_Type.__name__ = "Integer32"
_OmnisTerminalInfoOpncon_Object = MibScalar
omnisTerminalInfoOpncon = _OmnisTerminalInfoOpncon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 28),
    _OmnisTerminalInfoOpncon_Type()
)
omnisTerminalInfoOpncon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoOpncon.setStatus("mandatory")
_OmnisTerminalInfoPacAnz_Type = Integer32
_OmnisTerminalInfoPacAnz_Object = MibScalar
omnisTerminalInfoPacAnz = _OmnisTerminalInfoPacAnz_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 29),
    _OmnisTerminalInfoPacAnz_Type()
)
omnisTerminalInfoPacAnz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoPacAnz.setStatus("mandatory")


class _OmnisTerminalInfoInputLogging_Type(Integer32):
    """Custom type omnisTerminalInfoInputLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("rec", 3),
          ("send", 4),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoInputLogging_Type.__name__ = "Integer32"
_OmnisTerminalInfoInputLogging_Object = MibScalar
omnisTerminalInfoInputLogging = _OmnisTerminalInfoInputLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 30),
    _OmnisTerminalInfoInputLogging_Type()
)
omnisTerminalInfoInputLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoInputLogging.setStatus("mandatory")


class _OmnisTerminalInfoOutputLogging_Type(Integer32):
    """Custom type omnisTerminalInfoOutputLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("rec", 3),
          ("send", 4),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoOutputLogging_Type.__name__ = "Integer32"
_OmnisTerminalInfoOutputLogging_Object = MibScalar
omnisTerminalInfoOutputLogging = _OmnisTerminalInfoOutputLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 31),
    _OmnisTerminalInfoOutputLogging_Type()
)
omnisTerminalInfoOutputLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoOutputLogging.setStatus("mandatory")


class _OmnisTerminalInfoAutoLogoff_Type(Integer32):
    """Custom type omnisTerminalInfoAutoLogoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("std", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisTerminalInfoAutoLogoff_Type.__name__ = "Integer32"
_OmnisTerminalInfoAutoLogoff_Object = MibScalar
omnisTerminalInfoAutoLogoff = _OmnisTerminalInfoAutoLogoff_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 32),
    _OmnisTerminalInfoAutoLogoff_Type()
)
omnisTerminalInfoAutoLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoAutoLogoff.setStatus("mandatory")


class _OmnisTerminalInfoLine25_Type(Integer32):
    """Custom type omnisTerminalInfoLine25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("omnis", 4),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalInfoLine25_Type.__name__ = "Integer32"
_OmnisTerminalInfoLine25_Object = MibScalar
omnisTerminalInfoLine25 = _OmnisTerminalInfoLine25_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 33),
    _OmnisTerminalInfoLine25_Type()
)
omnisTerminalInfoLine25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoLine25.setStatus("mandatory")


class _OmnisTerminalExclPartner_Type(Integer32):
    """Custom type omnisTerminalExclPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTerminalExclPartner_Type.__name__ = "Integer32"
_OmnisTerminalExclPartner_Object = MibScalar
omnisTerminalExclPartner = _OmnisTerminalExclPartner_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 34),
    _OmnisTerminalExclPartner_Type()
)
omnisTerminalExclPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalExclPartner.setStatus("mandatory")


class _OmnisTerminalInfoSave_Type(Integer32):
    """Custom type omnisTerminalInfoSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("no", 5),
          ("pkey", 3),
          ("screen", 2),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisTerminalInfoSave_Type.__name__ = "Integer32"
_OmnisTerminalInfoSave_Object = MibScalar
omnisTerminalInfoSave = _OmnisTerminalInfoSave_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 35),
    _OmnisTerminalInfoSave_Type()
)
omnisTerminalInfoSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoSave.setStatus("mandatory")


class _OmnisTerminalInfoReply_Type(Integer32):
    """Custom type omnisTerminalInfoReply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("restricted", 1),
          ("std", 3),
          ("unknown", 99))
    )


_OmnisTerminalInfoReply_Type.__name__ = "Integer32"
_OmnisTerminalInfoReply_Object = MibScalar
omnisTerminalInfoReply = _OmnisTerminalInfoReply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 36),
    _OmnisTerminalInfoReply_Type()
)
omnisTerminalInfoReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoReply.setStatus("mandatory")


class _OmnisTerminalInfoUserProt_Type(Integer32):
    """Custom type omnisTerminalInfoUserProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("omnis", 2),
          ("unknown", 99),
          ("vtsucb", 3))
    )


_OmnisTerminalInfoUserProt_Type.__name__ = "Integer32"
_OmnisTerminalInfoUserProt_Object = MibScalar
omnisTerminalInfoUserProt = _OmnisTerminalInfoUserProt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 37),
    _OmnisTerminalInfoUserProt_Type()
)
omnisTerminalInfoUserProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoUserProt.setStatus("mandatory")


class _OmnisTerminalInfoTestmode_Type(Integer32):
    """Custom type omnisTerminalInfoTestmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisTerminalInfoTestmode_Type.__name__ = "Integer32"
_OmnisTerminalInfoTestmode_Object = MibScalar
omnisTerminalInfoTestmode = _OmnisTerminalInfoTestmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 38),
    _OmnisTerminalInfoTestmode_Type()
)
omnisTerminalInfoTestmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoTestmode.setStatus("mandatory")


class _OmnisTerminalInfoInsave_Type(Integer32):
    """Custom type omnisTerminalInfoInsave based on Integer32"""
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
              13,
              14,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("f1", 21),
          ("f10", 30),
          ("f11", 31),
          ("f12", 32),
          ("f13", 33),
          ("f14", 34),
          ("f15", 35),
          ("f16", 36),
          ("f17", 37),
          ("f18", 38),
          ("f19", 39),
          ("f2", 22),
          ("f20", 40),
          ("f21", 41),
          ("f22", 42),
          ("f23", 43),
          ("f24", 44),
          ("f3", 23),
          ("f4", 24),
          ("f5", 25),
          ("f6", 26),
          ("f7", 27),
          ("f8", 28),
          ("f9", 29),
          ("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisTerminalInfoInsave_Type.__name__ = "Integer32"
_OmnisTerminalInfoInsave_Object = MibScalar
omnisTerminalInfoInsave = _OmnisTerminalInfoInsave_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 39),
    _OmnisTerminalInfoInsave_Type()
)
omnisTerminalInfoInsave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoInsave.setStatus("mandatory")


class _OmnisTerminalInfoSNMP_Type(Integer32):
    """Custom type omnisTerminalInfoSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisTerminalInfoSNMP_Type.__name__ = "Integer32"
_OmnisTerminalInfoSNMP_Object = MibScalar
omnisTerminalInfoSNMP = _OmnisTerminalInfoSNMP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 40),
    _OmnisTerminalInfoSNMP_Type()
)
omnisTerminalInfoSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoSNMP.setStatus("mandatory")


class _OmnisTerminalInfoTransProt_Type(DisplayString):
    """Custom type omnisTerminalInfoTransProt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisTerminalInfoTransProt_Type.__name__ = "DisplayString"
_OmnisTerminalInfoTransProt_Object = MibScalar
omnisTerminalInfoTransProt = _OmnisTerminalInfoTransProt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 41),
    _OmnisTerminalInfoTransProt_Type()
)
omnisTerminalInfoTransProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoTransProt.setStatus("mandatory")


class _OmnisTerminalInfoHcyForm_Type(DisplayString):
    """Custom type omnisTerminalInfoHcyForm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OmnisTerminalInfoHcyForm_Type.__name__ = "DisplayString"
_OmnisTerminalInfoHcyForm_Object = MibScalar
omnisTerminalInfoHcyForm = _OmnisTerminalInfoHcyForm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 5, 42),
    _OmnisTerminalInfoHcyForm_Type()
)
omnisTerminalInfoHcyForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTerminalInfoHcyForm.setStatus("mandatory")
_SniOmnisPartners_ObjectIdentity = ObjectIdentity
sniOmnisPartners = _SniOmnisPartners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6)
)


class _OmnisPartnerStatus_Type(Integer32):
    """Custom type omnisPartnerStatus based on Integer32"""
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
        *(("activ", 2),
          ("all", 1),
          ("hold", 3),
          ("inactiv", 4))
    )


_OmnisPartnerStatus_Type.__name__ = "Integer32"
_OmnisPartnerStatus_Object = MibScalar
omnisPartnerStatus = _OmnisPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 1),
    _OmnisPartnerStatus_Type()
)
omnisPartnerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisPartnerStatus.setStatus("mandatory")
_OmnisPartnerTabNum_Type = Integer32
_OmnisPartnerTabNum_Object = MibScalar
omnisPartnerTabNum = _OmnisPartnerTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 2),
    _OmnisPartnerTabNum_Type()
)
omnisPartnerTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerTabNum.setStatus("mandatory")
_OmnisPartnerSelectTID_Type = Integer32
_OmnisPartnerSelectTID_Object = MibScalar
omnisPartnerSelectTID = _OmnisPartnerSelectTID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 3),
    _OmnisPartnerSelectTID_Type()
)
omnisPartnerSelectTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisPartnerSelectTID.setStatus("mandatory")
_OmnisPartnerTable_Object = MibTable
omnisPartnerTable = _OmnisPartnerTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4)
)
if mibBuilder.loadTexts:
    omnisPartnerTable.setStatus("mandatory")
_OmnisPartnerEntry_Object = MibTableRow
omnisPartnerEntry = _OmnisPartnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1)
)
omnisPartnerEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisPartnerPID"),
)
if mibBuilder.loadTexts:
    omnisPartnerEntry.setStatus("mandatory")
_OmnisPartnerPID_Type = Integer32
_OmnisPartnerPID_Object = MibTableColumn
omnisPartnerPID = _OmnisPartnerPID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 1),
    _OmnisPartnerPID_Type()
)
omnisPartnerPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisPartnerPID.setStatus("mandatory")


class _OmnisPartnerPAC_Type(DisplayString):
    """Custom type omnisPartnerPAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisPartnerPAC_Type.__name__ = "DisplayString"
_OmnisPartnerPAC_Object = MibTableColumn
omnisPartnerPAC = _OmnisPartnerPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 2),
    _OmnisPartnerPAC_Type()
)
omnisPartnerPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerPAC.setStatus("mandatory")


class _OmnisPartnerPtnName_Type(DisplayString):
    """Custom type omnisPartnerPtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisPartnerPtnName_Type.__name__ = "DisplayString"
_OmnisPartnerPtnName_Object = MibTableColumn
omnisPartnerPtnName = _OmnisPartnerPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 3),
    _OmnisPartnerPtnName_Type()
)
omnisPartnerPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerPtnName.setStatus("mandatory")


class _OmnisPartnerProName_Type(DisplayString):
    """Custom type omnisPartnerProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisPartnerProName_Type.__name__ = "DisplayString"
_OmnisPartnerProName_Object = MibTableColumn
omnisPartnerProName = _OmnisPartnerProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 4),
    _OmnisPartnerProName_Type()
)
omnisPartnerProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerProName.setStatus("mandatory")


class _OmnisPartnerTyp_Type(Integer32):
    """Custom type omnisPartnerTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dcam", 2),
          ("skp", 6),
          ("svp", 5),
          ("tiam", 1),
          ("ucon", 3),
          ("unknown", 99),
          ("utm", 4))
    )


_OmnisPartnerTyp_Type.__name__ = "Integer32"
_OmnisPartnerTyp_Object = MibTableColumn
omnisPartnerTyp = _OmnisPartnerTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 5),
    _OmnisPartnerTyp_Type()
)
omnisPartnerTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerTyp.setStatus("mandatory")


class _OmnisPartnerState_Type(Integer32):
    """Custom type omnisPartnerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              8,
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 2),
          ("cancel", 8),
          ("cls", 5),
          ("hold", 6),
          ("inact", 7),
          ("los", 4),
          ("opn", 1),
          ("unknown", 99))
    )


_OmnisPartnerState_Type.__name__ = "Integer32"
_OmnisPartnerState_Object = MibTableColumn
omnisPartnerState = _OmnisPartnerState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 6),
    _OmnisPartnerState_Type()
)
omnisPartnerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisPartnerState.setStatus("mandatory")


class _OmnisPartnerRoute_Type(Integer32):
    """Custom type omnisPartnerRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dir", 2),
          ("ind", 1),
          ("mux", 3),
          ("unknown", 99))
    )


_OmnisPartnerRoute_Type.__name__ = "Integer32"
_OmnisPartnerRoute_Object = MibTableColumn
omnisPartnerRoute = _OmnisPartnerRoute_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 7),
    _OmnisPartnerRoute_Type()
)
omnisPartnerRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerRoute.setStatus("mandatory")


class _OmnisPartnerKPAC_Type(Integer32):
    """Custom type omnisPartnerKPAC based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisPartnerKPAC_Type.__name__ = "Integer32"
_OmnisPartnerKPAC_Object = MibTableColumn
omnisPartnerKPAC = _OmnisPartnerKPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 8),
    _OmnisPartnerKPAC_Type()
)
omnisPartnerKPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerKPAC.setStatus("mandatory")
_OmnisPartnerTid_Type = Integer32
_OmnisPartnerTid_Object = MibTableColumn
omnisPartnerTid = _OmnisPartnerTid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 6, 4, 1, 9),
    _OmnisPartnerTid_Type()
)
omnisPartnerTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerTid.setStatus("mandatory")
_SniOmnisPartnerInfo_ObjectIdentity = ObjectIdentity
sniOmnisPartnerInfo = _SniOmnisPartnerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7)
)
_OmnisPartnerInfoPID_Type = Integer32
_OmnisPartnerInfoPID_Object = MibScalar
omnisPartnerInfoPID = _OmnisPartnerInfoPID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 1),
    _OmnisPartnerInfoPID_Type()
)
omnisPartnerInfoPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisPartnerInfoPID.setStatus("mandatory")


class _OmnisPartnerInfoPAC_Type(DisplayString):
    """Custom type omnisPartnerInfoPAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisPartnerInfoPAC_Type.__name__ = "DisplayString"
_OmnisPartnerInfoPAC_Object = MibScalar
omnisPartnerInfoPAC = _OmnisPartnerInfoPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 2),
    _OmnisPartnerInfoPAC_Type()
)
omnisPartnerInfoPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoPAC.setStatus("mandatory")


class _OmnisPartnerInfoPtnName_Type(DisplayString):
    """Custom type omnisPartnerInfoPtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisPartnerInfoPtnName_Type.__name__ = "DisplayString"
_OmnisPartnerInfoPtnName_Object = MibScalar
omnisPartnerInfoPtnName = _OmnisPartnerInfoPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 3),
    _OmnisPartnerInfoPtnName_Type()
)
omnisPartnerInfoPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoPtnName.setStatus("mandatory")


class _OmnisPartnerInfoProName_Type(DisplayString):
    """Custom type omnisPartnerInfoProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisPartnerInfoProName_Type.__name__ = "DisplayString"
_OmnisPartnerInfoProName_Object = MibScalar
omnisPartnerInfoProName = _OmnisPartnerInfoProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 4),
    _OmnisPartnerInfoProName_Type()
)
omnisPartnerInfoProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoProName.setStatus("mandatory")


class _OmnisPartnerInfoTyp_Type(Integer32):
    """Custom type omnisPartnerInfoTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dcam", 2),
          ("skp", 6),
          ("svp", 5),
          ("tiam", 1),
          ("ucon", 3),
          ("unknown", 99),
          ("utm", 4))
    )


_OmnisPartnerInfoTyp_Type.__name__ = "Integer32"
_OmnisPartnerInfoTyp_Object = MibScalar
omnisPartnerInfoTyp = _OmnisPartnerInfoTyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 5),
    _OmnisPartnerInfoTyp_Type()
)
omnisPartnerInfoTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoTyp.setStatus("mandatory")


class _OmnisPartnerInfoState_Type(Integer32):
    """Custom type omnisPartnerInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 2),
          ("cls", 4),
          ("hold", 5),
          ("inact", 6),
          ("los", 3),
          ("opn", 1),
          ("unknown", 99))
    )


_OmnisPartnerInfoState_Type.__name__ = "Integer32"
_OmnisPartnerInfoState_Object = MibScalar
omnisPartnerInfoState = _OmnisPartnerInfoState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 6),
    _OmnisPartnerInfoState_Type()
)
omnisPartnerInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoState.setStatus("mandatory")


class _OmnisPartnerInfoRoute_Type(Integer32):
    """Custom type omnisPartnerInfoRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dir", 2),
          ("ind", 1),
          ("mux", 3),
          ("unknown", 99))
    )


_OmnisPartnerInfoRoute_Type.__name__ = "Integer32"
_OmnisPartnerInfoRoute_Object = MibScalar
omnisPartnerInfoRoute = _OmnisPartnerInfoRoute_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 7),
    _OmnisPartnerInfoRoute_Type()
)
omnisPartnerInfoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoRoute.setStatus("mandatory")


class _OmnisPartnerInfoKPAC_Type(Integer32):
    """Custom type omnisPartnerInfoKPAC based on Integer32"""
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
              13,
              14,
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("k1", 1),
          ("k10", 10),
          ("k11", 11),
          ("k12", 12),
          ("k13", 13),
          ("k14", 14),
          ("k2", 2),
          ("k3", 3),
          ("k4", 4),
          ("k5", 5),
          ("k6", 6),
          ("k7", 7),
          ("k8", 8),
          ("k9", 9),
          ("no", 97),
          ("std", 98),
          ("unknown", 99))
    )


_OmnisPartnerInfoKPAC_Type.__name__ = "Integer32"
_OmnisPartnerInfoKPAC_Object = MibScalar
omnisPartnerInfoKPAC = _OmnisPartnerInfoKPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 8),
    _OmnisPartnerInfoKPAC_Type()
)
omnisPartnerInfoKPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoKPAC.setStatus("mandatory")


class _OmnisPartnerInfoRepAppName_Type(DisplayString):
    """Custom type omnisPartnerInfoRepAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisPartnerInfoRepAppName_Type.__name__ = "DisplayString"
_OmnisPartnerInfoRepAppName_Object = MibScalar
omnisPartnerInfoRepAppName = _OmnisPartnerInfoRepAppName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 9),
    _OmnisPartnerInfoRepAppName_Type()
)
omnisPartnerInfoRepAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoRepAppName.setStatus("mandatory")


class _OmnisPartnerInfoOPass_Type(Integer32):
    """Custom type omnisPartnerInfoOPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisPartnerInfoOPass_Type.__name__ = "Integer32"
_OmnisPartnerInfoOPass_Object = MibScalar
omnisPartnerInfoOPass = _OmnisPartnerInfoOPass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 10),
    _OmnisPartnerInfoOPass_Type()
)
omnisPartnerInfoOPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoOPass.setStatus("mandatory")


class _OmnisPartnerInfoMTAB_Type(DisplayString):
    """Custom type omnisPartnerInfoMTAB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisPartnerInfoMTAB_Type.__name__ = "DisplayString"
_OmnisPartnerInfoMTAB_Object = MibScalar
omnisPartnerInfoMTAB = _OmnisPartnerInfoMTAB_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 11),
    _OmnisPartnerInfoMTAB_Type()
)
omnisPartnerInfoMTAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoMTAB.setStatus("mandatory")


class _OmnisPartnerInfoExit_Type(DisplayString):
    """Custom type omnisPartnerInfoExit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisPartnerInfoExit_Type.__name__ = "DisplayString"
_OmnisPartnerInfoExit_Object = MibScalar
omnisPartnerInfoExit = _OmnisPartnerInfoExit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 12),
    _OmnisPartnerInfoExit_Type()
)
omnisPartnerInfoExit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoExit.setStatus("mandatory")


class _OmnisPartnerInfoHold_Type(Integer32):
    """Custom type omnisPartnerInfoHold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoHold_Type.__name__ = "Integer32"
_OmnisPartnerInfoHold_Object = MibScalar
omnisPartnerInfoHold = _OmnisPartnerInfoHold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 13),
    _OmnisPartnerInfoHold_Type()
)
omnisPartnerInfoHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoHold.setStatus("mandatory")


class _OmnisPartnerInfoChange_Type(Integer32):
    """Custom type omnisPartnerInfoChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoChange_Type.__name__ = "Integer32"
_OmnisPartnerInfoChange_Object = MibScalar
omnisPartnerInfoChange = _OmnisPartnerInfoChange_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 14),
    _OmnisPartnerInfoChange_Type()
)
omnisPartnerInfoChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoChange.setStatus("mandatory")


class _OmnisPartnerInfoHcopy_Type(DisplayString):
    """Custom type omnisPartnerInfoHcopy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisPartnerInfoHcopy_Type.__name__ = "DisplayString"
_OmnisPartnerInfoHcopy_Object = MibScalar
omnisPartnerInfoHcopy = _OmnisPartnerInfoHcopy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 15),
    _OmnisPartnerInfoHcopy_Type()
)
omnisPartnerInfoHcopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoHcopy.setStatus("mandatory")


class _OmnisPartnerInfoClass_Type(Integer32):
    """Custom type omnisPartnerInfoClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("del", 3),
          ("out", 2),
          ("sav", 1),
          ("unknown", 99))
    )


_OmnisPartnerInfoClass_Type.__name__ = "Integer32"
_OmnisPartnerInfoClass_Object = MibScalar
omnisPartnerInfoClass = _OmnisPartnerInfoClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 16),
    _OmnisPartnerInfoClass_Type()
)
omnisPartnerInfoClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoClass.setStatus("mandatory")


class _OmnisPartnerInfoColour_Type(Integer32):
    """Custom type omnisPartnerInfoColour based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("cyan", 2),
          ("green", 3),
          ("magenta", 5),
          ("red", 6),
          ("unknown", 99),
          ("white", 7),
          ("yellow", 4))
    )


_OmnisPartnerInfoColour_Type.__name__ = "Integer32"
_OmnisPartnerInfoColour_Object = MibScalar
omnisPartnerInfoColour = _OmnisPartnerInfoColour_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 17),
    _OmnisPartnerInfoColour_Type()
)
omnisPartnerInfoColour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoColour.setStatus("mandatory")


class _OmnisPartnerInfoProtocol_Type(Integer32):
    """Custom type omnisPartnerInfoProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dssim", 1),
          ("omnis", 2),
          ("unknown", 99))
    )


_OmnisPartnerInfoProtocol_Type.__name__ = "Integer32"
_OmnisPartnerInfoProtocol_Object = MibScalar
omnisPartnerInfoProtocol = _OmnisPartnerInfoProtocol_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 18),
    _OmnisPartnerInfoProtocol_Type()
)
omnisPartnerInfoProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoProtocol.setStatus("mandatory")


class _OmnisPartnerInfoLogging_Type(Integer32):
    """Custom type omnisPartnerInfoLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoLogging_Type.__name__ = "Integer32"
_OmnisPartnerInfoLogging_Object = MibScalar
omnisPartnerInfoLogging = _OmnisPartnerInfoLogging_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 19),
    _OmnisPartnerInfoLogging_Type()
)
omnisPartnerInfoLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoLogging.setStatus("mandatory")


class _OmnisPartnerInfoLPass_Type(Integer32):
    """Custom type omnisPartnerInfoLPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoLPass_Type.__name__ = "Integer32"
_OmnisPartnerInfoLPass_Object = MibScalar
omnisPartnerInfoLPass = _OmnisPartnerInfoLPass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 20),
    _OmnisPartnerInfoLPass_Type()
)
omnisPartnerInfoLPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoLPass.setStatus("mandatory")


class _OmnisPartnerInfoDeclared_Type(Integer32):
    """Custom type omnisPartnerInfoDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoDeclared_Type.__name__ = "Integer32"
_OmnisPartnerInfoDeclared_Object = MibScalar
omnisPartnerInfoDeclared = _OmnisPartnerInfoDeclared_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 21),
    _OmnisPartnerInfoDeclared_Type()
)
omnisPartnerInfoDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoDeclared.setStatus("mandatory")


class _OmnisPartnerInfoAutoLogoff_Type(Integer32):
    """Custom type omnisPartnerInfoAutoLogoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("std", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisPartnerInfoAutoLogoff_Type.__name__ = "Integer32"
_OmnisPartnerInfoAutoLogoff_Object = MibScalar
omnisPartnerInfoAutoLogoff = _OmnisPartnerInfoAutoLogoff_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 22),
    _OmnisPartnerInfoAutoLogoff_Type()
)
omnisPartnerInfoAutoLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoAutoLogoff.setStatus("mandatory")


class _OmnisPartnerInfoLine25_Type(Integer32):
    """Custom type omnisPartnerInfoLine25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("omnis", 4),
          ("std", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoLine25_Type.__name__ = "Integer32"
_OmnisPartnerInfoLine25_Object = MibScalar
omnisPartnerInfoLine25 = _OmnisPartnerInfoLine25_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 23),
    _OmnisPartnerInfoLine25_Type()
)
omnisPartnerInfoLine25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoLine25.setStatus("mandatory")
_OmnisPartnerStartSequ_Type = Integer32
_OmnisPartnerStartSequ_Object = MibScalar
omnisPartnerStartSequ = _OmnisPartnerStartSequ_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 24),
    _OmnisPartnerStartSequ_Type()
)
omnisPartnerStartSequ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerStartSequ.setStatus("mandatory")


class _OmnisPartnerInfoCMsg_Type(Integer32):
    """Custom type omnisPartnerInfoCMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoCMsg_Type.__name__ = "Integer32"
_OmnisPartnerInfoCMsg_Object = MibScalar
omnisPartnerInfoCMsg = _OmnisPartnerInfoCMsg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 25),
    _OmnisPartnerInfoCMsg_Type()
)
omnisPartnerInfoCMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoCMsg.setStatus("mandatory")


class _OmnisPartnerInfoLCase_Type(Integer32):
    """Custom type omnisPartnerInfoLCase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisPartnerInfoLCase_Type.__name__ = "Integer32"
_OmnisPartnerInfoLCase_Object = MibScalar
omnisPartnerInfoLCase = _OmnisPartnerInfoLCase_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 26),
    _OmnisPartnerInfoLCase_Type()
)
omnisPartnerInfoLCase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoLCase.setStatus("mandatory")


class _OmnisPartnerInfoSave_Type(Integer32):
    """Custom type omnisPartnerInfoSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("no", 5),
          ("pkey", 3),
          ("screen", 2),
          ("std", 1),
          ("unknown", 99))
    )


_OmnisPartnerInfoSave_Type.__name__ = "Integer32"
_OmnisPartnerInfoSave_Object = MibScalar
omnisPartnerInfoSave = _OmnisPartnerInfoSave_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 27),
    _OmnisPartnerInfoSave_Type()
)
omnisPartnerInfoSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoSave.setStatus("mandatory")
_OmnisPartnerInfoTid_Type = Integer32
_OmnisPartnerInfoTid_Object = MibScalar
omnisPartnerInfoTid = _OmnisPartnerInfoTid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 28),
    _OmnisPartnerInfoTid_Type()
)
omnisPartnerInfoTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoTid.setStatus("mandatory")


class _OmnisPartnerInfoSNMP_Type(Integer32):
    """Custom type omnisPartnerInfoSNMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisPartnerInfoSNMP_Type.__name__ = "Integer32"
_OmnisPartnerInfoSNMP_Object = MibScalar
omnisPartnerInfoSNMP = _OmnisPartnerInfoSNMP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 29),
    _OmnisPartnerInfoSNMP_Type()
)
omnisPartnerInfoSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoSNMP.setStatus("mandatory")


class _OmnisPartnerInfoPACPrefix_Type(Integer32):
    """Custom type omnisPartnerInfoPACPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("line", 3),
          ("no", 1),
          ("prefix", 4),
          ("std", 2),
          ("unknown", 99))
    )


_OmnisPartnerInfoPACPrefix_Type.__name__ = "Integer32"
_OmnisPartnerInfoPACPrefix_Object = MibScalar
omnisPartnerInfoPACPrefix = _OmnisPartnerInfoPACPrefix_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 30),
    _OmnisPartnerInfoPACPrefix_Type()
)
omnisPartnerInfoPACPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoPACPrefix.setStatus("mandatory")


class _OmnisPartnerInfoBerid_Type(Integer32):
    """Custom type omnisPartnerInfoBerid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("unknown", 99),
          ("yes", 2))
    )


_OmnisPartnerInfoBerid_Type.__name__ = "Integer32"
_OmnisPartnerInfoBerid_Object = MibScalar
omnisPartnerInfoBerid = _OmnisPartnerInfoBerid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 31),
    _OmnisPartnerInfoBerid_Type()
)
omnisPartnerInfoBerid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoBerid.setStatus("mandatory")


class _OmnisPartnerInfoConnect_Type(Integer32):
    """Custom type omnisPartnerInfoConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("logon", 2),
          ("opncon", 1),
          ("start", 3),
          ("unknown", 99))
    )


_OmnisPartnerInfoConnect_Type.__name__ = "Integer32"
_OmnisPartnerInfoConnect_Object = MibScalar
omnisPartnerInfoConnect = _OmnisPartnerInfoConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 7, 32),
    _OmnisPartnerInfoConnect_Type()
)
omnisPartnerInfoConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisPartnerInfoConnect.setStatus("mandatory")
_SniOmnisGroups_ObjectIdentity = ObjectIdentity
sniOmnisGroups = _SniOmnisGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8)
)
_OmnisGroupsTabNum_Type = Integer32
_OmnisGroupsTabNum_Object = MibScalar
omnisGroupsTabNum = _OmnisGroupsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 1),
    _OmnisGroupsTabNum_Type()
)
omnisGroupsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGroupsTabNum.setStatus("mandatory")
_OmnisGroupsSelectTID_Type = Integer32
_OmnisGroupsSelectTID_Object = MibScalar
omnisGroupsSelectTID = _OmnisGroupsSelectTID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 2),
    _OmnisGroupsSelectTID_Type()
)
omnisGroupsSelectTID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisGroupsSelectTID.setStatus("mandatory")
_OmnisGroupsTable_Object = MibTable
omnisGroupsTable = _OmnisGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 3)
)
if mibBuilder.loadTexts:
    omnisGroupsTable.setStatus("mandatory")
_OmnisGroupsEntry_Object = MibTableRow
omnisGroupsEntry = _OmnisGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 3, 1)
)
omnisGroupsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisGroupsGAC"),
    (0, "Omnis-Management-MIB", "omnisGroupsPAC"),
)
if mibBuilder.loadTexts:
    omnisGroupsEntry.setStatus("mandatory")


class _OmnisGroupsGAC_Type(DisplayString):
    """Custom type omnisGroupsGAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisGroupsGAC_Type.__name__ = "DisplayString"
_OmnisGroupsGAC_Object = MibTableColumn
omnisGroupsGAC = _OmnisGroupsGAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 3, 1, 1),
    _OmnisGroupsGAC_Type()
)
omnisGroupsGAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGroupsGAC.setStatus("mandatory")


class _OmnisGroupsPAC_Type(DisplayString):
    """Custom type omnisGroupsPAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisGroupsPAC_Type.__name__ = "DisplayString"
_OmnisGroupsPAC_Object = MibTableColumn
omnisGroupsPAC = _OmnisGroupsPAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 3, 1, 2),
    _OmnisGroupsPAC_Type()
)
omnisGroupsPAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGroupsPAC.setStatus("mandatory")
_OmnisGroupsTid_Type = Integer32
_OmnisGroupsTid_Object = MibTableColumn
omnisGroupsTid = _OmnisGroupsTid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 8, 3, 1, 3),
    _OmnisGroupsTid_Type()
)
omnisGroupsTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisGroupsTid.setStatus("mandatory")
_SniOmnisHardCopy_ObjectIdentity = ObjectIdentity
sniOmnisHardCopy = _SniOmnisHardCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9)
)


class _OmnisHardCopyStatus_Type(Integer32):
    """Custom type omnisHardCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activ", 2),
          ("all", 1),
          ("inactiv", 4))
    )


_OmnisHardCopyStatus_Type.__name__ = "Integer32"
_OmnisHardCopyStatus_Object = MibScalar
omnisHardCopyStatus = _OmnisHardCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 1),
    _OmnisHardCopyStatus_Type()
)
omnisHardCopyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyStatus.setStatus("mandatory")
_OmnisHardCopyTabNum_Type = Integer32
_OmnisHardCopyTabNum_Object = MibScalar
omnisHardCopyTabNum = _OmnisHardCopyTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 2),
    _OmnisHardCopyTabNum_Type()
)
omnisHardCopyTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyTabNum.setStatus("mandatory")
_OmnisHardCopyTable_Object = MibTable
omnisHardCopyTable = _OmnisHardCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3)
)
if mibBuilder.loadTexts:
    omnisHardCopyTable.setStatus("mandatory")
_OmnisHardCopyEntry_Object = MibTableRow
omnisHardCopyEntry = _OmnisHardCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1)
)
omnisHardCopyEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisHardCopyHID"),
)
if mibBuilder.loadTexts:
    omnisHardCopyEntry.setStatus("mandatory")


class _OmnisHardCopyHAC_Type(DisplayString):
    """Custom type omnisHardCopyHAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OmnisHardCopyHAC_Type.__name__ = "DisplayString"
_OmnisHardCopyHAC_Object = MibTableColumn
omnisHardCopyHAC = _OmnisHardCopyHAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 1),
    _OmnisHardCopyHAC_Type()
)
omnisHardCopyHAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyHAC.setStatus("mandatory")
_OmnisHardCopyHID_Type = Integer32
_OmnisHardCopyHID_Object = MibTableColumn
omnisHardCopyHID = _OmnisHardCopyHID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 2),
    _OmnisHardCopyHID_Type()
)
omnisHardCopyHID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyHID.setStatus("mandatory")


class _OmnisHardCopyPtnName_Type(DisplayString):
    """Custom type omnisHardCopyPtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisHardCopyPtnName_Type.__name__ = "DisplayString"
_OmnisHardCopyPtnName_Object = MibTableColumn
omnisHardCopyPtnName = _OmnisHardCopyPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 3),
    _OmnisHardCopyPtnName_Type()
)
omnisHardCopyPtnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyPtnName.setStatus("mandatory")


class _OmnisHardCopyProName_Type(DisplayString):
    """Custom type omnisHardCopyProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisHardCopyProName_Type.__name__ = "DisplayString"
_OmnisHardCopyProName_Object = MibTableColumn
omnisHardCopyProName = _OmnisHardCopyProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 4),
    _OmnisHardCopyProName_Type()
)
omnisHardCopyProName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyProName.setStatus("mandatory")


class _OmnisHardCopyState_Type(Integer32):
    """Custom type omnisHardCopyState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 3),
          ("cancel", 7),
          ("cls", 5),
          ("cls-p", 1),
          ("inact", 6),
          ("los", 4),
          ("opn", 2),
          ("unknown", 99))
    )


_OmnisHardCopyState_Type.__name__ = "Integer32"
_OmnisHardCopyState_Object = MibTableColumn
omnisHardCopyState = _OmnisHardCopyState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 5),
    _OmnisHardCopyState_Type()
)
omnisHardCopyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyState.setStatus("mandatory")


class _OmnisHardCopyINOP_Type(DisplayString):
    """Custom type omnisHardCopyINOP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisHardCopyINOP_Type.__name__ = "DisplayString"
_OmnisHardCopyINOP_Object = MibTableColumn
omnisHardCopyINOP = _OmnisHardCopyINOP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 6),
    _OmnisHardCopyINOP_Type()
)
omnisHardCopyINOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyINOP.setStatus("mandatory")


class _OmnisHardCopyConnect_Type(Integer32):
    """Custom type omnisHardCopyConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("s", 1),
          ("u", 2),
          ("unknown", 99))
    )


_OmnisHardCopyConnect_Type.__name__ = "Integer32"
_OmnisHardCopyConnect_Object = MibTableColumn
omnisHardCopyConnect = _OmnisHardCopyConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 7),
    _OmnisHardCopyConnect_Type()
)
omnisHardCopyConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyConnect.setStatus("mandatory")


class _OmnisHardCopyRestart_Type(Integer32):
    """Custom type omnisHardCopyRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("unknown", 99))
    )


_OmnisHardCopyRestart_Type.__name__ = "Integer32"
_OmnisHardCopyRestart_Object = MibTableColumn
omnisHardCopyRestart = _OmnisHardCopyRestart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 9, 3, 1, 8),
    _OmnisHardCopyRestart_Type()
)
omnisHardCopyRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyRestart.setStatus("mandatory")
_SniOmnisHardCopyPIDs_ObjectIdentity = ObjectIdentity
sniOmnisHardCopyPIDs = _SniOmnisHardCopyPIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10)
)
_OmnisHardCopyPIDsTabNum_Type = Integer32
_OmnisHardCopyPIDsTabNum_Object = MibScalar
omnisHardCopyPIDsTabNum = _OmnisHardCopyPIDsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 1),
    _OmnisHardCopyPIDsTabNum_Type()
)
omnisHardCopyPIDsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyPIDsTabNum.setStatus("mandatory")
_OmnisHardCopyPIDsSelectHid_Type = Integer32
_OmnisHardCopyPIDsSelectHid_Object = MibScalar
omnisHardCopyPIDsSelectHid = _OmnisHardCopyPIDsSelectHid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 2),
    _OmnisHardCopyPIDsSelectHid_Type()
)
omnisHardCopyPIDsSelectHid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyPIDsSelectHid.setStatus("mandatory")
_OmnisHardCopyPIDsTable_Object = MibTable
omnisHardCopyPIDsTable = _OmnisHardCopyPIDsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 3)
)
if mibBuilder.loadTexts:
    omnisHardCopyPIDsTable.setStatus("mandatory")
_OmnisHardCopyPIDsEntry_Object = MibTableRow
omnisHardCopyPIDsEntry = _OmnisHardCopyPIDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 3, 1)
)
omnisHardCopyPIDsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisHardCopyPIDsHID"),
    (0, "Omnis-Management-MIB", "omnisHardCopyPIDsID"),
)
if mibBuilder.loadTexts:
    omnisHardCopyPIDsEntry.setStatus("mandatory")
_OmnisHardCopyPIDsHID_Type = Integer32
_OmnisHardCopyPIDsHID_Object = MibTableColumn
omnisHardCopyPIDsHID = _OmnisHardCopyPIDsHID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 3, 1, 1),
    _OmnisHardCopyPIDsHID_Type()
)
omnisHardCopyPIDsHID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyPIDsHID.setStatus("mandatory")
_OmnisHardCopyPIDsID_Type = Integer32
_OmnisHardCopyPIDsID_Object = MibTableColumn
omnisHardCopyPIDsID = _OmnisHardCopyPIDsID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 10, 3, 1, 2),
    _OmnisHardCopyPIDsID_Type()
)
omnisHardCopyPIDsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyPIDsID.setStatus("mandatory")
_SniOmnisHardCopyTIDs_ObjectIdentity = ObjectIdentity
sniOmnisHardCopyTIDs = _SniOmnisHardCopyTIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11)
)
_OmnisHardCopyTIDsTabNum_Type = Integer32
_OmnisHardCopyTIDsTabNum_Object = MibScalar
omnisHardCopyTIDsTabNum = _OmnisHardCopyTIDsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 1),
    _OmnisHardCopyTIDsTabNum_Type()
)
omnisHardCopyTIDsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyTIDsTabNum.setStatus("mandatory")
_OmnisHardCopyTIDsSelectHid_Type = Integer32
_OmnisHardCopyTIDsSelectHid_Object = MibScalar
omnisHardCopyTIDsSelectHid = _OmnisHardCopyTIDsSelectHid_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 2),
    _OmnisHardCopyTIDsSelectHid_Type()
)
omnisHardCopyTIDsSelectHid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyTIDsSelectHid.setStatus("mandatory")
_OmnisHardCopyTIDsTable_Object = MibTable
omnisHardCopyTIDsTable = _OmnisHardCopyTIDsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 3)
)
if mibBuilder.loadTexts:
    omnisHardCopyTIDsTable.setStatus("mandatory")
_OmnisHardCopyTIDsEntry_Object = MibTableRow
omnisHardCopyTIDsEntry = _OmnisHardCopyTIDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 3, 1)
)
omnisHardCopyTIDsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisHardCopyTIDsHID"),
    (0, "Omnis-Management-MIB", "omnisHardCopyTIDsID"),
)
if mibBuilder.loadTexts:
    omnisHardCopyTIDsEntry.setStatus("mandatory")
_OmnisHardCopyTIDsHID_Type = Integer32
_OmnisHardCopyTIDsHID_Object = MibTableColumn
omnisHardCopyTIDsHID = _OmnisHardCopyTIDsHID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 3, 1, 1),
    _OmnisHardCopyTIDsHID_Type()
)
omnisHardCopyTIDsHID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyTIDsHID.setStatus("mandatory")


class _OmnisHardCopyTIDsHAC_Type(DisplayString):
    """Custom type omnisHardCopyTIDsHAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisHardCopyTIDsHAC_Type.__name__ = "DisplayString"
_OmnisHardCopyTIDsHAC_Object = MibTableColumn
omnisHardCopyTIDsHAC = _OmnisHardCopyTIDsHAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 3, 1, 2),
    _OmnisHardCopyTIDsHAC_Type()
)
omnisHardCopyTIDsHAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyTIDsHAC.setStatus("mandatory")
_OmnisHardCopyTIDsID_Type = Integer32
_OmnisHardCopyTIDsID_Object = MibTableColumn
omnisHardCopyTIDsID = _OmnisHardCopyTIDsID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 11, 3, 1, 3),
    _OmnisHardCopyTIDsID_Type()
)
omnisHardCopyTIDsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyTIDsID.setStatus("mandatory")
_SniOmnisHardCopyCreate_ObjectIdentity = ObjectIdentity
sniOmnisHardCopyCreate = _SniOmnisHardCopyCreate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12)
)


class _OmnisHardCopyCreateHAC_Type(DisplayString):
    """Custom type omnisHardCopyCreateHAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OmnisHardCopyCreateHAC_Type.__name__ = "DisplayString"
_OmnisHardCopyCreateHAC_Object = MibScalar
omnisHardCopyCreateHAC = _OmnisHardCopyCreateHAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 1),
    _OmnisHardCopyCreateHAC_Type()
)
omnisHardCopyCreateHAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyCreateHAC.setStatus("mandatory")
_OmnisHardCopyCreateHID_Type = Integer32
_OmnisHardCopyCreateHID_Object = MibScalar
omnisHardCopyCreateHID = _OmnisHardCopyCreateHID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 2),
    _OmnisHardCopyCreateHID_Type()
)
omnisHardCopyCreateHID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisHardCopyCreateHID.setStatus("mandatory")


class _OmnisHardCopyCreatePtnName_Type(DisplayString):
    """Custom type omnisHardCopyCreatePtnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisHardCopyCreatePtnName_Type.__name__ = "DisplayString"
_OmnisHardCopyCreatePtnName_Object = MibScalar
omnisHardCopyCreatePtnName = _OmnisHardCopyCreatePtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 3),
    _OmnisHardCopyCreatePtnName_Type()
)
omnisHardCopyCreatePtnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyCreatePtnName.setStatus("mandatory")


class _OmnisHardCopyCreateProName_Type(DisplayString):
    """Custom type omnisHardCopyCreateProName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OmnisHardCopyCreateProName_Type.__name__ = "DisplayString"
_OmnisHardCopyCreateProName_Object = MibScalar
omnisHardCopyCreateProName = _OmnisHardCopyCreateProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 4),
    _OmnisHardCopyCreateProName_Type()
)
omnisHardCopyCreateProName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyCreateProName.setStatus("mandatory")


class _OmnisHardCopyCreateInop_Type(DisplayString):
    """Custom type omnisHardCopyCreateInop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_OmnisHardCopyCreateInop_Type.__name__ = "DisplayString"
_OmnisHardCopyCreateInop_Object = MibScalar
omnisHardCopyCreateInop = _OmnisHardCopyCreateInop_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 5),
    _OmnisHardCopyCreateInop_Type()
)
omnisHardCopyCreateInop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyCreateInop.setStatus("mandatory")


class _OmnisHardCopyCreateConnect_Type(Integer32):
    """Custom type omnisHardCopyCreateConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("s", 1),
          ("u", 2),
          ("unknown", 99))
    )


_OmnisHardCopyCreateConnect_Type.__name__ = "Integer32"
_OmnisHardCopyCreateConnect_Object = MibScalar
omnisHardCopyCreateConnect = _OmnisHardCopyCreateConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 12, 6),
    _OmnisHardCopyCreateConnect_Type()
)
omnisHardCopyCreateConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisHardCopyCreateConnect.setStatus("mandatory")
_SniOmnisOmnis_ObjectIdentity = ObjectIdentity
sniOmnisOmnis = _SniOmnisOmnis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13)
)


class _OmnisOmnisStatus_Type(Integer32):
    """Custom type omnisOmnisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activ", 2),
          ("all", 1),
          ("inactiv", 4))
    )


_OmnisOmnisStatus_Type.__name__ = "Integer32"
_OmnisOmnisStatus_Object = MibScalar
omnisOmnisStatus = _OmnisOmnisStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 1),
    _OmnisOmnisStatus_Type()
)
omnisOmnisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisOmnisStatus.setStatus("mandatory")
_OmnisOmnisTabNum_Type = Integer32
_OmnisOmnisTabNum_Object = MibScalar
omnisOmnisTabNum = _OmnisOmnisTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 2),
    _OmnisOmnisTabNum_Type()
)
omnisOmnisTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisTabNum.setStatus("mandatory")
_OmnisOmnisTable_Object = MibTable
omnisOmnisTable = _OmnisOmnisTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3)
)
if mibBuilder.loadTexts:
    omnisOmnisTable.setStatus("mandatory")
_OmnisOmnisEntry_Object = MibTableRow
omnisOmnisEntry = _OmnisOmnisEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1)
)
omnisOmnisEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisOmnisID"),
)
if mibBuilder.loadTexts:
    omnisOmnisEntry.setStatus("mandatory")


class _OmnisOmnisOAC_Type(DisplayString):
    """Custom type omnisOmnisOAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisOmnisOAC_Type.__name__ = "DisplayString"
_OmnisOmnisOAC_Object = MibTableColumn
omnisOmnisOAC = _OmnisOmnisOAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 1),
    _OmnisOmnisOAC_Type()
)
omnisOmnisOAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisOmnisOAC.setStatus("mandatory")
_OmnisOmnisID_Type = Integer32
_OmnisOmnisID_Object = MibTableColumn
omnisOmnisID = _OmnisOmnisID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 2),
    _OmnisOmnisID_Type()
)
omnisOmnisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisID.setStatus("mandatory")
_OmnisOmnisPtnName_Type = DisplayString
_OmnisOmnisPtnName_Object = MibTableColumn
omnisOmnisPtnName = _OmnisOmnisPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 3),
    _OmnisOmnisPtnName_Type()
)
omnisOmnisPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisPtnName.setStatus("mandatory")
_OmnisOmnisProName_Type = DisplayString
_OmnisOmnisProName_Object = MibTableColumn
omnisOmnisProName = _OmnisOmnisProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 4),
    _OmnisOmnisProName_Type()
)
omnisOmnisProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisProName.setStatus("mandatory")


class _OmnisOmnisState_Type(Integer32):
    """Custom type omnisOmnisState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 3),
          ("cancel", 7),
          ("cls", 5),
          ("cls-p", 1),
          ("inact", 6),
          ("los", 4),
          ("opn", 2),
          ("unknown", 99))
    )


_OmnisOmnisState_Type.__name__ = "Integer32"
_OmnisOmnisState_Object = MibTableColumn
omnisOmnisState = _OmnisOmnisState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 5),
    _OmnisOmnisState_Type()
)
omnisOmnisState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisOmnisState.setStatus("mandatory")


class _OmnisOmnisConnect_Type(Integer32):
    """Custom type omnisOmnisConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("opncon", 2),
          ("start", 1),
          ("unknown", 99))
    )


_OmnisOmnisConnect_Type.__name__ = "Integer32"
_OmnisOmnisConnect_Object = MibTableColumn
omnisOmnisConnect = _OmnisOmnisConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 6),
    _OmnisOmnisConnect_Type()
)
omnisOmnisConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisConnect.setStatus("mandatory")
_OmnisOmnisTime_Type = Integer32
_OmnisOmnisTime_Object = MibTableColumn
omnisOmnisTime = _OmnisOmnisTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 7),
    _OmnisOmnisTime_Type()
)
omnisOmnisTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisTime.setStatus("mandatory")


class _OmnisOmnisLPass_Type(Integer32):
    """Custom type omnisOmnisLPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisOmnisLPass_Type.__name__ = "Integer32"
_OmnisOmnisLPass_Object = MibTableColumn
omnisOmnisLPass = _OmnisOmnisLPass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 8),
    _OmnisOmnisLPass_Type()
)
omnisOmnisLPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisLPass.setStatus("mandatory")


class _OmnisOmnisOpncon_Type(Integer32):
    """Custom type omnisOmnisOpncon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("dcl", 1),
          ("free", 2),
          ("unknown", 99))
    )


_OmnisOmnisOpncon_Type.__name__ = "Integer32"
_OmnisOmnisOpncon_Object = MibTableColumn
omnisOmnisOpncon = _OmnisOmnisOpncon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 9),
    _OmnisOmnisOpncon_Type()
)
omnisOmnisOpncon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisOmnisOpncon.setStatus("mandatory")


class _OmnisOmnisRestart_Type(Integer32):
    """Custom type omnisOmnisRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              99)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("unknown", 99))
    )


_OmnisOmnisRestart_Type.__name__ = "Integer32"
_OmnisOmnisRestart_Object = MibTableColumn
omnisOmnisRestart = _OmnisOmnisRestart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 13, 3, 1, 10),
    _OmnisOmnisRestart_Type()
)
omnisOmnisRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisOmnisRestart.setStatus("mandatory")
_SniOmnisMux_ObjectIdentity = ObjectIdentity
sniOmnisMux = _SniOmnisMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14)
)


class _OmnisMuxStatus_Type(Integer32):
    """Custom type omnisMuxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activ", 2),
          ("all", 1),
          ("inactiv", 4))
    )


_OmnisMuxStatus_Type.__name__ = "Integer32"
_OmnisMuxStatus_Object = MibScalar
omnisMuxStatus = _OmnisMuxStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 1),
    _OmnisMuxStatus_Type()
)
omnisMuxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisMuxStatus.setStatus("mandatory")
_OmnisMuxTabNum_Type = Integer32
_OmnisMuxTabNum_Object = MibScalar
omnisMuxTabNum = _OmnisMuxTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 2),
    _OmnisMuxTabNum_Type()
)
omnisMuxTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxTabNum.setStatus("mandatory")
_OmnisMuxTable_Object = MibTable
omnisMuxTable = _OmnisMuxTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3)
)
if mibBuilder.loadTexts:
    omnisMuxTable.setStatus("mandatory")
_OmnisMuxEntry_Object = MibTableRow
omnisMuxEntry = _OmnisMuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1)
)
omnisMuxEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisMuxID"),
)
if mibBuilder.loadTexts:
    omnisMuxEntry.setStatus("mandatory")
_OmnisMuxID_Type = Integer32
_OmnisMuxID_Object = MibTableColumn
omnisMuxID = _OmnisMuxID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 1),
    _OmnisMuxID_Type()
)
omnisMuxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxID.setStatus("mandatory")
_OmnisMuxPtnName_Type = DisplayString
_OmnisMuxPtnName_Object = MibTableColumn
omnisMuxPtnName = _OmnisMuxPtnName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 2),
    _OmnisMuxPtnName_Type()
)
omnisMuxPtnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxPtnName.setStatus("mandatory")
_OmnisMuxProName_Type = DisplayString
_OmnisMuxProName_Object = MibTableColumn
omnisMuxProName = _OmnisMuxProName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 3),
    _OmnisMuxProName_Type()
)
omnisMuxProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxProName.setStatus("mandatory")


class _OmnisMuxState_Type(Integer32):
    """Custom type omnisMuxState based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("act", 3),
          ("cancel", 7),
          ("cls", 5),
          ("cls-p", 1),
          ("inact", 6),
          ("los", 4),
          ("opn", 2),
          ("unknown", 99))
    )


_OmnisMuxState_Type.__name__ = "Integer32"
_OmnisMuxState_Object = MibTableColumn
omnisMuxState = _OmnisMuxState_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 4),
    _OmnisMuxState_Type()
)
omnisMuxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisMuxState.setStatus("mandatory")


class _OmnisMuxConnect_Type(Integer32):
    """Custom type omnisMuxConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("opncon", 2),
          ("start", 1),
          ("unknown", 99))
    )


_OmnisMuxConnect_Type.__name__ = "Integer32"
_OmnisMuxConnect_Object = MibTableColumn
omnisMuxConnect = _OmnisMuxConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 5),
    _OmnisMuxConnect_Type()
)
omnisMuxConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxConnect.setStatus("mandatory")


class _OmnisMuxLPass_Type(Integer32):
    """Custom type omnisMuxLPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisMuxLPass_Type.__name__ = "Integer32"
_OmnisMuxLPass_Object = MibTableColumn
omnisMuxLPass = _OmnisMuxLPass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 6),
    _OmnisMuxLPass_Type()
)
omnisMuxLPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxLPass.setStatus("mandatory")
_OmnisMuxSessions_Type = Integer32
_OmnisMuxSessions_Object = MibTableColumn
omnisMuxSessions = _OmnisMuxSessions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 7),
    _OmnisMuxSessions_Type()
)
omnisMuxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxSessions.setStatus("mandatory")


class _OmnisMuxAvailability_Type(Integer32):
    """Custom type omnisMuxAvailability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisMuxAvailability_Type.__name__ = "Integer32"
_OmnisMuxAvailability_Object = MibTableColumn
omnisMuxAvailability = _OmnisMuxAvailability_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 14, 3, 1, 8),
    _OmnisMuxAvailability_Type()
)
omnisMuxAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisMuxAvailability.setStatus("mandatory")
_SniOmnisExits_ObjectIdentity = ObjectIdentity
sniOmnisExits = _SniOmnisExits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15)
)
_OmnisExitTabNum_Type = Integer32
_OmnisExitTabNum_Object = MibScalar
omnisExitTabNum = _OmnisExitTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 1),
    _OmnisExitTabNum_Type()
)
omnisExitTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitTabNum.setStatus("mandatory")
_OmnisExitTable_Object = MibTable
omnisExitTable = _OmnisExitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 2)
)
if mibBuilder.loadTexts:
    omnisExitTable.setStatus("mandatory")
_OmnisExitEntry_Object = MibTableRow
omnisExitEntry = _OmnisExitEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 2, 1)
)
omnisExitEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisExitID"),
    (0, "Omnis-Management-MIB", "omnisExitModul"),
)
if mibBuilder.loadTexts:
    omnisExitEntry.setStatus("mandatory")
_OmnisExitEAC_Type = DisplayString
_OmnisExitEAC_Object = MibTableColumn
omnisExitEAC = _OmnisExitEAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 2, 1, 1),
    _OmnisExitEAC_Type()
)
omnisExitEAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitEAC.setStatus("mandatory")
_OmnisExitID_Type = Integer32
_OmnisExitID_Object = MibTableColumn
omnisExitID = _OmnisExitID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 2, 1, 2),
    _OmnisExitID_Type()
)
omnisExitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitID.setStatus("mandatory")
_OmnisExitModul_Type = DisplayString
_OmnisExitModul_Object = MibTableColumn
omnisExitModul = _OmnisExitModul_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 15, 2, 1, 3),
    _OmnisExitModul_Type()
)
omnisExitModul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitModul.setStatus("mandatory")
_SniOmnisExitPIDs_ObjectIdentity = ObjectIdentity
sniOmnisExitPIDs = _SniOmnisExitPIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16)
)
_OmnisExitPIDsTabNum_Type = Integer32
_OmnisExitPIDsTabNum_Object = MibScalar
omnisExitPIDsTabNum = _OmnisExitPIDsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 1),
    _OmnisExitPIDsTabNum_Type()
)
omnisExitPIDsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitPIDsTabNum.setStatus("mandatory")


class _OmnisExitPIDsSelectEac_Type(DisplayString):
    """Custom type omnisExitPIDsSelectEac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisExitPIDsSelectEac_Type.__name__ = "DisplayString"
_OmnisExitPIDsSelectEac_Object = MibScalar
omnisExitPIDsSelectEac = _OmnisExitPIDsSelectEac_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 2),
    _OmnisExitPIDsSelectEac_Type()
)
omnisExitPIDsSelectEac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitPIDsSelectEac.setStatus("mandatory")
_OmnisExitPIDsTable_Object = MibTable
omnisExitPIDsTable = _OmnisExitPIDsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 3)
)
if mibBuilder.loadTexts:
    omnisExitPIDsTable.setStatus("mandatory")
_OmnisExitPIDsEntry_Object = MibTableRow
omnisExitPIDsEntry = _OmnisExitPIDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 3, 1)
)
omnisExitPIDsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisExitPIDsEAC"),
    (0, "Omnis-Management-MIB", "omnisExitPIDsID"),
)
if mibBuilder.loadTexts:
    omnisExitPIDsEntry.setStatus("mandatory")


class _OmnisExitPIDsEAC_Type(DisplayString):
    """Custom type omnisExitPIDsEAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisExitPIDsEAC_Type.__name__ = "DisplayString"
_OmnisExitPIDsEAC_Object = MibTableColumn
omnisExitPIDsEAC = _OmnisExitPIDsEAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 3, 1, 1),
    _OmnisExitPIDsEAC_Type()
)
omnisExitPIDsEAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitPIDsEAC.setStatus("mandatory")
_OmnisExitPIDsID_Type = Integer32
_OmnisExitPIDsID_Object = MibTableColumn
omnisExitPIDsID = _OmnisExitPIDsID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 16, 3, 1, 2),
    _OmnisExitPIDsID_Type()
)
omnisExitPIDsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitPIDsID.setStatus("mandatory")
_SniOmnisExitTIDs_ObjectIdentity = ObjectIdentity
sniOmnisExitTIDs = _SniOmnisExitTIDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17)
)
_OmnisExitTIDsTabNum_Type = Integer32
_OmnisExitTIDsTabNum_Object = MibScalar
omnisExitTIDsTabNum = _OmnisExitTIDsTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 1),
    _OmnisExitTIDsTabNum_Type()
)
omnisExitTIDsTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitTIDsTabNum.setStatus("mandatory")


class _OmnisExitTIDsSelectEac_Type(DisplayString):
    """Custom type omnisExitTIDsSelectEac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisExitTIDsSelectEac_Type.__name__ = "DisplayString"
_OmnisExitTIDsSelectEac_Object = MibScalar
omnisExitTIDsSelectEac = _OmnisExitTIDsSelectEac_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 2),
    _OmnisExitTIDsSelectEac_Type()
)
omnisExitTIDsSelectEac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitTIDsSelectEac.setStatus("mandatory")
_OmnisExitTIDsTable_Object = MibTable
omnisExitTIDsTable = _OmnisExitTIDsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 3)
)
if mibBuilder.loadTexts:
    omnisExitTIDsTable.setStatus("mandatory")
_OmnisExitTIDsEntry_Object = MibTableRow
omnisExitTIDsEntry = _OmnisExitTIDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 3, 1)
)
omnisExitTIDsEntry.setIndexNames(
    (0, "Omnis-Management-MIB", "omnisExitTIDsEAC"),
    (0, "Omnis-Management-MIB", "omnisExitTIDsID"),
)
if mibBuilder.loadTexts:
    omnisExitTIDsEntry.setStatus("mandatory")


class _OmnisExitTIDsEAC_Type(DisplayString):
    """Custom type omnisExitTIDsEAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisExitTIDsEAC_Type.__name__ = "DisplayString"
_OmnisExitTIDsEAC_Object = MibTableColumn
omnisExitTIDsEAC = _OmnisExitTIDsEAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 3, 1, 1),
    _OmnisExitTIDsEAC_Type()
)
omnisExitTIDsEAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitTIDsEAC.setStatus("mandatory")
_OmnisExitTIDsID_Type = Integer32
_OmnisExitTIDsID_Object = MibTableColumn
omnisExitTIDsID = _OmnisExitTIDsID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 17, 3, 1, 2),
    _OmnisExitTIDsID_Type()
)
omnisExitTIDsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisExitTIDsID.setStatus("mandatory")
_SniOmnisExitCreate_ObjectIdentity = ObjectIdentity
sniOmnisExitCreate = _SniOmnisExitCreate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18)
)


class _OmnisExitCreateEAC_Type(DisplayString):
    """Custom type omnisExitCreateEAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisExitCreateEAC_Type.__name__ = "DisplayString"
_OmnisExitCreateEAC_Object = MibScalar
omnisExitCreateEAC = _OmnisExitCreateEAC_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 1),
    _OmnisExitCreateEAC_Type()
)
omnisExitCreateEAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateEAC.setStatus("mandatory")


class _OmnisExitCreateModul1_Type(DisplayString):
    """Custom type omnisExitCreateModul1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul1_Type.__name__ = "DisplayString"
_OmnisExitCreateModul1_Object = MibScalar
omnisExitCreateModul1 = _OmnisExitCreateModul1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 2),
    _OmnisExitCreateModul1_Type()
)
omnisExitCreateModul1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul1.setStatus("mandatory")


class _OmnisExitCreateModul2_Type(DisplayString):
    """Custom type omnisExitCreateModul2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul2_Type.__name__ = "DisplayString"
_OmnisExitCreateModul2_Object = MibScalar
omnisExitCreateModul2 = _OmnisExitCreateModul2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 3),
    _OmnisExitCreateModul2_Type()
)
omnisExitCreateModul2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul2.setStatus("mandatory")


class _OmnisExitCreateModul3_Type(DisplayString):
    """Custom type omnisExitCreateModul3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul3_Type.__name__ = "DisplayString"
_OmnisExitCreateModul3_Object = MibScalar
omnisExitCreateModul3 = _OmnisExitCreateModul3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 4),
    _OmnisExitCreateModul3_Type()
)
omnisExitCreateModul3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul3.setStatus("mandatory")


class _OmnisExitCreateModul4_Type(DisplayString):
    """Custom type omnisExitCreateModul4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul4_Type.__name__ = "DisplayString"
_OmnisExitCreateModul4_Object = MibScalar
omnisExitCreateModul4 = _OmnisExitCreateModul4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 5),
    _OmnisExitCreateModul4_Type()
)
omnisExitCreateModul4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul4.setStatus("mandatory")


class _OmnisExitCreateModul5_Type(DisplayString):
    """Custom type omnisExitCreateModul5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul5_Type.__name__ = "DisplayString"
_OmnisExitCreateModul5_Object = MibScalar
omnisExitCreateModul5 = _OmnisExitCreateModul5_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 6),
    _OmnisExitCreateModul5_Type()
)
omnisExitCreateModul5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul5.setStatus("mandatory")


class _OmnisExitCreateModul6_Type(DisplayString):
    """Custom type omnisExitCreateModul6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul6_Type.__name__ = "DisplayString"
_OmnisExitCreateModul6_Object = MibScalar
omnisExitCreateModul6 = _OmnisExitCreateModul6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 7),
    _OmnisExitCreateModul6_Type()
)
omnisExitCreateModul6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul6.setStatus("mandatory")


class _OmnisExitCreateModul7_Type(DisplayString):
    """Custom type omnisExitCreateModul7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul7_Type.__name__ = "DisplayString"
_OmnisExitCreateModul7_Object = MibScalar
omnisExitCreateModul7 = _OmnisExitCreateModul7_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 8),
    _OmnisExitCreateModul7_Type()
)
omnisExitCreateModul7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul7.setStatus("mandatory")


class _OmnisExitCreateModul8_Type(DisplayString):
    """Custom type omnisExitCreateModul8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul8_Type.__name__ = "DisplayString"
_OmnisExitCreateModul8_Object = MibScalar
omnisExitCreateModul8 = _OmnisExitCreateModul8_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 9),
    _OmnisExitCreateModul8_Type()
)
omnisExitCreateModul8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul8.setStatus("mandatory")


class _OmnisExitCreateModul9_Type(DisplayString):
    """Custom type omnisExitCreateModul9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul9_Type.__name__ = "DisplayString"
_OmnisExitCreateModul9_Object = MibScalar
omnisExitCreateModul9 = _OmnisExitCreateModul9_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 10),
    _OmnisExitCreateModul9_Type()
)
omnisExitCreateModul9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul9.setStatus("mandatory")


class _OmnisExitCreateModul10_Type(DisplayString):
    """Custom type omnisExitCreateModul10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul10_Type.__name__ = "DisplayString"
_OmnisExitCreateModul10_Object = MibScalar
omnisExitCreateModul10 = _OmnisExitCreateModul10_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 11),
    _OmnisExitCreateModul10_Type()
)
omnisExitCreateModul10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul10.setStatus("mandatory")


class _OmnisExitCreateModul11_Type(DisplayString):
    """Custom type omnisExitCreateModul11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul11_Type.__name__ = "DisplayString"
_OmnisExitCreateModul11_Object = MibScalar
omnisExitCreateModul11 = _OmnisExitCreateModul11_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 12),
    _OmnisExitCreateModul11_Type()
)
omnisExitCreateModul11.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul11.setStatus("mandatory")


class _OmnisExitCreateModul12_Type(DisplayString):
    """Custom type omnisExitCreateModul12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul12_Type.__name__ = "DisplayString"
_OmnisExitCreateModul12_Object = MibScalar
omnisExitCreateModul12 = _OmnisExitCreateModul12_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 13),
    _OmnisExitCreateModul12_Type()
)
omnisExitCreateModul12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul12.setStatus("mandatory")


class _OmnisExitCreateModul13_Type(DisplayString):
    """Custom type omnisExitCreateModul13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul13_Type.__name__ = "DisplayString"
_OmnisExitCreateModul13_Object = MibScalar
omnisExitCreateModul13 = _OmnisExitCreateModul13_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 14),
    _OmnisExitCreateModul13_Type()
)
omnisExitCreateModul13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul13.setStatus("mandatory")


class _OmnisExitCreateModul14_Type(DisplayString):
    """Custom type omnisExitCreateModul14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OmnisExitCreateModul14_Type.__name__ = "DisplayString"
_OmnisExitCreateModul14_Object = MibScalar
omnisExitCreateModul14 = _OmnisExitCreateModul14_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 15),
    _OmnisExitCreateModul14_Type()
)
omnisExitCreateModul14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateModul14.setStatus("mandatory")


class _OmnisExitCreateOption_Type(Integer32):
    """Custom type omnisExitCreateOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 3),
          ("modify", 2),
          ("unknown", 99))
    )


_OmnisExitCreateOption_Type.__name__ = "Integer32"
_OmnisExitCreateOption_Object = MibScalar
omnisExitCreateOption = _OmnisExitCreateOption_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 18, 16),
    _OmnisExitCreateOption_Type()
)
omnisExitCreateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisExitCreateOption.setStatus("mandatory")
_SniOmnisTrace_ObjectIdentity = ObjectIdentity
sniOmnisTrace = _SniOmnisTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19)
)


class _OmnisTraceConnection_Type(Integer32):
    """Custom type omnisTraceConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTraceConnection_Type.__name__ = "Integer32"
_OmnisTraceConnection_Object = MibScalar
omnisTraceConnection = _OmnisTraceConnection_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 1),
    _OmnisTraceConnection_Type()
)
omnisTraceConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceConnection.setStatus("mandatory")


class _OmnisTraceExit_Type(Integer32):
    """Custom type omnisTraceExit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTraceExit_Type.__name__ = "Integer32"
_OmnisTraceExit_Object = MibScalar
omnisTraceExit = _OmnisTraceExit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 2),
    _OmnisTraceExit_Type()
)
omnisTraceExit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceExit.setStatus("mandatory")


class _OmnisTraceTransport_Type(Integer32):
    """Custom type omnisTraceTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("select", 3),
          ("unknown", 99),
          ("yes", 1))
    )


_OmnisTraceTransport_Type.__name__ = "Integer32"
_OmnisTraceTransport_Object = MibScalar
omnisTraceTransport = _OmnisTraceTransport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 3),
    _OmnisTraceTransport_Type()
)
omnisTraceTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceTransport.setStatus("mandatory")


class _OmnisTraceTransportTrm_Type(DisplayString):
    """Custom type omnisTraceTransportTrm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OmnisTraceTransportTrm_Type.__name__ = "DisplayString"
_OmnisTraceTransportTrm_Object = MibScalar
omnisTraceTransportTrm = _OmnisTraceTransportTrm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 4),
    _OmnisTraceTransportTrm_Type()
)
omnisTraceTransportTrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceTransportTrm.setStatus("mandatory")


class _OmnisTraceTransporthcy_Type(DisplayString):
    """Custom type omnisTraceTransporthcy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisTraceTransporthcy_Type.__name__ = "DisplayString"
_OmnisTraceTransporthcy_Object = MibScalar
omnisTraceTransporthcy = _OmnisTraceTransporthcy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 5),
    _OmnisTraceTransporthcy_Type()
)
omnisTraceTransporthcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceTransporthcy.setStatus("mandatory")


class _OmnisTraceTransportmux_Type(DisplayString):
    """Custom type omnisTraceTransportmux based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_OmnisTraceTransportmux_Type.__name__ = "DisplayString"
_OmnisTraceTransportmux_Object = MibScalar
omnisTraceTransportmux = _OmnisTraceTransportmux_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 6),
    _OmnisTraceTransportmux_Type()
)
omnisTraceTransportmux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceTransportmux.setStatus("mandatory")


class _OmnisTraceTransportoms_Type(DisplayString):
    """Custom type omnisTraceTransportoms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OmnisTraceTransportoms_Type.__name__ = "DisplayString"
_OmnisTraceTransportoms_Object = MibScalar
omnisTraceTransportoms = _OmnisTraceTransportoms_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 19, 7),
    _OmnisTraceTransportoms_Type()
)
omnisTraceTransportoms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    omnisTraceTransportoms.setStatus("mandatory")
_SniOmnisTraps_ObjectIdentity = ObjectIdentity
sniOmnisTraps = _SniOmnisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20)
)
_SniOmnisUserdefinedTraps_ObjectIdentity = ObjectIdentity
sniOmnisUserdefinedTraps = _SniOmnisUserdefinedTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 21)
)
_OmnisUserdefinedTrapData_ObjectIdentity = ObjectIdentity
omnisUserdefinedTrapData = _OmnisUserdefinedTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 21, 1)
)
_OmnisTrapMsgText_Type = DisplayString
_OmnisTrapMsgText_Object = MibScalar
omnisTrapMsgText = _OmnisTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 21, 1, 1),
    _OmnisTrapMsgText_Type()
)
omnisTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omnisTrapMsgText.setStatus("mandatory")
_OmnisUserdefinedTrap_ObjectIdentity = ObjectIdentity
omnisUserdefinedTrap = _OmnisUserdefinedTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 21, 10)
)

# Managed Objects groups


# Notification objects

omnisStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 301)
)
omnisStopTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisStopTrap.setStatus(
        ""
    )

omnisStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 302)
)
omnisStartTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisStartTrap.setStatus(
        ""
    )

omnisConnStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 303)
)
omnisConnStopTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPtnName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoProName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPAC"))
)
if mibBuilder.loadTexts:
    omnisConnStopTrap.setStatus(
        ""
    )

omnisDstConnStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 304)
)
omnisDstConnStopTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisTerminalInfoPtnName"),
        ("Omnis-Management-MIB", "omnisTerminalInfoProName"),
        ("Omnis-Management-MIB", "omnisTerminalInfoTID"))
)
if mibBuilder.loadTexts:
    omnisDstConnStopTrap.setStatus(
        ""
    )

omnisEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 305)
)
omnisEventTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPtnName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoProName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPAC"))
)
if mibBuilder.loadTexts:
    omnisEventTrap.setStatus(
        ""
    )

omnisDstLevelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 306)
)
omnisDstLevelTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisDstLevelTrap.setStatus(
        ""
    )

omnisPacLevelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 307)
)
omnisPacLevelTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisPacLevelTrap.setStatus(
        ""
    )

omnisPtnLevelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 308)
)
omnisPtnLevelTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisPtnLevelTrap.setStatus(
        ""
    )

omnisMuxConnStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 309)
)
omnisMuxConnStopTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPtnName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoProName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPAC"))
)
if mibBuilder.loadTexts:
    omnisMuxConnStopTrap.setStatus(
        ""
    )

omnisOmnConnStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 310)
)
omnisOmnConnStopTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPtnName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoProName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPAC"))
)
if mibBuilder.loadTexts:
    omnisOmnConnStopTrap.setStatus(
        ""
    )

omnisHcConnStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 311)
)
omnisHcConnStopTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPtnName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoProName"),
        ("Omnis-Management-MIB", "omnisPartnerInfoPAC"))
)
if mibBuilder.loadTexts:
    omnisHcConnStopTrap.setStatus(
        ""
    )

omnisDumpWriteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 312)
)
omnisDumpWriteTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisDumpWriteTrap.setStatus(
        ""
    )

omnisDumpEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 313)
)
omnisDumpEndTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisDumpEndTrap.setStatus(
        ""
    )

omnisEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 20, 0, 314)
)
omnisEndTrap.setObjects(
    ("Omnis-Management-MIB", "omnisSettingsAppName")
)
if mibBuilder.loadTexts:
    omnisEndTrap.setStatus(
        ""
    )

omnisGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 31, 21, 10, 0, 320)
)
omnisGeneralTrap.setObjects(
      *(("Omnis-Management-MIB", "omnisSettingsAppName"),
        ("Omnis-Management-MIB", "omnisTrapMsgText"))
)
if mibBuilder.loadTexts:
    omnisGeneralTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Omnis-Management-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniOmnis": sniOmnis,
       "sniOmnisGlobalData": sniOmnisGlobalData,
       "omnisGlobalDataSubagentVersion": omnisGlobalDataSubagentVersion,
       "omnisGlobalDataTabNum": omnisGlobalDataTabNum,
       "omnisGlobalDataActID": omnisGlobalDataActID,
       "omnisGlobalDataActName": omnisGlobalDataActName,
       "omnisGlobalDataTable": omnisGlobalDataTable,
       "omnisGlobalDataEntry": omnisGlobalDataEntry,
       "omnisGlobalDataOmnID": omnisGlobalDataOmnID,
       "omnisGlobalDataVersion": omnisGlobalDataVersion,
       "omnisGlobalDataOmnName": omnisGlobalDataOmnName,
       "omnisGlobalDataState": omnisGlobalDataState,
       "sniOmnisSettings": sniOmnisSettings,
       "omnisSettingsAppName": omnisSettingsAppName,
       "omnisSettingsAppNameISO": omnisSettingsAppNameISO,
       "omnisSettingsNumPartners": omnisSettingsNumPartners,
       "omnisSettingsNumTerminals": omnisSettingsNumTerminals,
       "omnisSettingsDSTMax": omnisSettingsDSTMax,
       "omnisSettingsPTNMax": omnisSettingsPTNMax,
       "omnisSettingsPACMax": omnisSettingsPACMax,
       "omnisSettingsState": omnisSettingsState,
       "omnisSettingsAPASS": omnisSettingsAPASS,
       "omnisSettingsHOLD": omnisSettingsHOLD,
       "omnisSettingsHcyForm": omnisSettingsHcyForm,
       "omnisSettingsHCopy": omnisSettingsHCopy,
       "omnisSettingsLogging": omnisSettingsLogging,
       "omnisSettingsChangeLogging": omnisSettingsChangeLogging,
       "omnisSettingsACK": omnisSettingsACK,
       "omnisSettingsMTAB": omnisSettingsMTAB,
       "omnisSettingsEXIT": omnisSettingsEXIT,
       "omnisSettingsOpncon": omnisSettingsOpncon,
       "omnisSettingsBreakKey": omnisSettingsBreakKey,
       "omnisSettingsCallKey": omnisSettingsCallKey,
       "omnisSettingsCallInf": omnisSettingsCallInf,
       "omnisSettingsPac": omnisSettingsPac,
       "omnisSettingsInputLog": omnisSettingsInputLog,
       "omnisSettingsOutputLog": omnisSettingsOutputLog,
       "omnisSettingsLine25": omnisSettingsLine25,
       "omnisSettingsDisMod": omnisSettingsDisMod,
       "omnisSettingsKPAC": omnisSettingsKPAC,
       "omnisSettingsExitPri": omnisSettingsExitPri,
       "omnisSettingsReply": omnisSettingsReply,
       "omnisSettingsExitAuth": omnisSettingsExitAuth,
       "omnisSettingsLoggPri": omnisSettingsLoggPri,
       "omnisSettingsAudit": omnisSettingsAudit,
       "omnisSettingsMDefAuth": omnisSettingsMDefAuth,
       "omnisSettingsHoldPri": omnisSettingsHoldPri,
       "omnisSettingsInsave": omnisSettingsInsave,
       "omnisSettingsOpnStart": omnisSettingsOpnStart,
       "omnisSettingsExclPartner": omnisSettingsExclPartner,
       "omnisSettingsSave": omnisSettingsSave,
       "omnisSettingsMessageALL": omnisSettingsMessageALL,
       "omnisSettingsMessageADM": omnisSettingsMessageADM,
       "omnisSettingsEnd": omnisSettingsEnd,
       "omnisSettingsEndPassw": omnisSettingsEndPassw,
       "sniOmnisParameters": sniOmnisParameters,
       "omnisParametersAppName": omnisParametersAppName,
       "omnisParametersAppNameISO": omnisParametersAppNameISO,
       "omnisParametersPrefix": omnisParametersPrefix,
       "omnisParametersProName": omnisParametersProName,
       "omnisParametersVirtProName": omnisParametersVirtProName,
       "omnisParametersLoggingFile": omnisParametersLoggingFile,
       "omnisParametersStartupFile": omnisParametersStartupFile,
       "omnisParametersConfigFile": omnisParametersConfigFile,
       "omnisParametersConfUpdate": omnisParametersConfUpdate,
       "omnisParametersModulFile": omnisParametersModulFile,
       "omnisParametersBulletinFile": omnisParametersBulletinFile,
       "omnisParametersTextFile": omnisParametersTextFile,
       "omnisParametersPagePool": omnisParametersPagePool,
       "omnisParametersIOAreaLength": omnisParametersIOAreaLength,
       "omnisParametersTWorkLength": omnisParametersTWorkLength,
       "omnisParametersPWorkLength": omnisParametersPWorkLength,
       "omnisParametersTextKeyLength": omnisParametersTextKeyLength,
       "omnisParametersSecurityLevel": omnisParametersSecurityLevel,
       "omnisParametersDCAMIntVers": omnisParametersDCAMIntVers,
       "omnisParametersVTSUBVers": omnisParametersVTSUBVers,
       "omnisParametersVTSUCBVers": omnisParametersVTSUCBVers,
       "omnisParametersCMD": omnisParametersCMD,
       "omnisParametersDump": omnisParametersDump,
       "omnisParametersDumpMsgNr": omnisParametersDumpMsgNr,
       "omnisParametersDumpInsert": omnisParametersDumpInsert,
       "omnisParametersDumpInsertNr": omnisParametersDumpInsertNr,
       "sniOmnisTerminals": sniOmnisTerminals,
       "omnisTerminalsStatus": omnisTerminalsStatus,
       "omnisTerminalsTabNum": omnisTerminalsTabNum,
       "omnisTerminalsTable": omnisTerminalsTable,
       "omnisTerminalsEntry": omnisTerminalsEntry,
       "omnisTerminalsTID": omnisTerminalsTID,
       "omnisTerminalsPtnName": omnisTerminalsPtnName,
       "omnisTerminalsProName": omnisTerminalsProName,
       "omnisTerminalsTyp": omnisTerminalsTyp,
       "omnisTerminalsState": omnisTerminalsState,
       "omnisTerminalsRoute": omnisTerminalsRoute,
       "omnisTerminalsKPAC": omnisTerminalsKPAC,
       "omnisTerminalsUser": omnisTerminalsUser,
       "omnisTerminalsMessage": omnisTerminalsMessage,
       "sniOmnisTerminalInfo": sniOmnisTerminalInfo,
       "omnisTerminalInfoTID": omnisTerminalInfoTID,
       "omnisTerminalInfoPtnName": omnisTerminalInfoPtnName,
       "omnisTerminalInfoProName": omnisTerminalInfoProName,
       "omnisTerminalInfoTyp": omnisTerminalInfoTyp,
       "omnisTerminalInfoState": omnisTerminalInfoState,
       "omnisTerminalInfoRoute": omnisTerminalInfoRoute,
       "omnisTerminalInfoKPAC": omnisTerminalInfoKPAC,
       "omnisTerminalInfoUser": omnisTerminalInfoUser,
       "omnisTerminalInfoPAC": omnisTerminalInfoPAC,
       "omnisTerminalInfoADM": omnisTerminalInfoADM,
       "omnisTerminalInfoOPass": omnisTerminalInfoOPass,
       "omnisTerminalInfoMTAB": omnisTerminalInfoMTAB,
       "omnisTerminalInfoExit": omnisTerminalInfoExit,
       "omnisTerminalInfoHold": omnisTerminalInfoHold,
       "omnisTerminalInfoChange": omnisTerminalInfoChange,
       "omnisTerminalInfoHcopy": omnisTerminalInfoHcopy,
       "omnisTerminalInfoAck": omnisTerminalInfoAck,
       "omnisTerminalInfoListening": omnisTerminalInfoListening,
       "omnisTerminalInfoColour": omnisTerminalInfoColour,
       "omnisTerminalInfoLogging": omnisTerminalInfoLogging,
       "omnisTerminalInfoBerID": omnisTerminalInfoBerID,
       "omnisTerminalInfoDeclared": omnisTerminalInfoDeclared,
       "omnisTerminalInfoBreakKey": omnisTerminalInfoBreakKey,
       "omnisTerminalInfoCallKey": omnisTerminalInfoCallKey,
       "omnisTerminalInfoCallInf": omnisTerminalInfoCallInf,
       "omnisTerminalInfoDisMod": omnisTerminalInfoDisMod,
       "omnisTerminalInfoConnect": omnisTerminalInfoConnect,
       "omnisTerminalInfoOpncon": omnisTerminalInfoOpncon,
       "omnisTerminalInfoPacAnz": omnisTerminalInfoPacAnz,
       "omnisTerminalInfoInputLogging": omnisTerminalInfoInputLogging,
       "omnisTerminalInfoOutputLogging": omnisTerminalInfoOutputLogging,
       "omnisTerminalInfoAutoLogoff": omnisTerminalInfoAutoLogoff,
       "omnisTerminalInfoLine25": omnisTerminalInfoLine25,
       "omnisTerminalExclPartner": omnisTerminalExclPartner,
       "omnisTerminalInfoSave": omnisTerminalInfoSave,
       "omnisTerminalInfoReply": omnisTerminalInfoReply,
       "omnisTerminalInfoUserProt": omnisTerminalInfoUserProt,
       "omnisTerminalInfoTestmode": omnisTerminalInfoTestmode,
       "omnisTerminalInfoInsave": omnisTerminalInfoInsave,
       "omnisTerminalInfoSNMP": omnisTerminalInfoSNMP,
       "omnisTerminalInfoTransProt": omnisTerminalInfoTransProt,
       "omnisTerminalInfoHcyForm": omnisTerminalInfoHcyForm,
       "sniOmnisPartners": sniOmnisPartners,
       "omnisPartnerStatus": omnisPartnerStatus,
       "omnisPartnerTabNum": omnisPartnerTabNum,
       "omnisPartnerSelectTID": omnisPartnerSelectTID,
       "omnisPartnerTable": omnisPartnerTable,
       "omnisPartnerEntry": omnisPartnerEntry,
       "omnisPartnerPID": omnisPartnerPID,
       "omnisPartnerPAC": omnisPartnerPAC,
       "omnisPartnerPtnName": omnisPartnerPtnName,
       "omnisPartnerProName": omnisPartnerProName,
       "omnisPartnerTyp": omnisPartnerTyp,
       "omnisPartnerState": omnisPartnerState,
       "omnisPartnerRoute": omnisPartnerRoute,
       "omnisPartnerKPAC": omnisPartnerKPAC,
       "omnisPartnerTid": omnisPartnerTid,
       "sniOmnisPartnerInfo": sniOmnisPartnerInfo,
       "omnisPartnerInfoPID": omnisPartnerInfoPID,
       "omnisPartnerInfoPAC": omnisPartnerInfoPAC,
       "omnisPartnerInfoPtnName": omnisPartnerInfoPtnName,
       "omnisPartnerInfoProName": omnisPartnerInfoProName,
       "omnisPartnerInfoTyp": omnisPartnerInfoTyp,
       "omnisPartnerInfoState": omnisPartnerInfoState,
       "omnisPartnerInfoRoute": omnisPartnerInfoRoute,
       "omnisPartnerInfoKPAC": omnisPartnerInfoKPAC,
       "omnisPartnerInfoRepAppName": omnisPartnerInfoRepAppName,
       "omnisPartnerInfoOPass": omnisPartnerInfoOPass,
       "omnisPartnerInfoMTAB": omnisPartnerInfoMTAB,
       "omnisPartnerInfoExit": omnisPartnerInfoExit,
       "omnisPartnerInfoHold": omnisPartnerInfoHold,
       "omnisPartnerInfoChange": omnisPartnerInfoChange,
       "omnisPartnerInfoHcopy": omnisPartnerInfoHcopy,
       "omnisPartnerInfoClass": omnisPartnerInfoClass,
       "omnisPartnerInfoColour": omnisPartnerInfoColour,
       "omnisPartnerInfoProtocol": omnisPartnerInfoProtocol,
       "omnisPartnerInfoLogging": omnisPartnerInfoLogging,
       "omnisPartnerInfoLPass": omnisPartnerInfoLPass,
       "omnisPartnerInfoDeclared": omnisPartnerInfoDeclared,
       "omnisPartnerInfoAutoLogoff": omnisPartnerInfoAutoLogoff,
       "omnisPartnerInfoLine25": omnisPartnerInfoLine25,
       "omnisPartnerStartSequ": omnisPartnerStartSequ,
       "omnisPartnerInfoCMsg": omnisPartnerInfoCMsg,
       "omnisPartnerInfoLCase": omnisPartnerInfoLCase,
       "omnisPartnerInfoSave": omnisPartnerInfoSave,
       "omnisPartnerInfoTid": omnisPartnerInfoTid,
       "omnisPartnerInfoSNMP": omnisPartnerInfoSNMP,
       "omnisPartnerInfoPACPrefix": omnisPartnerInfoPACPrefix,
       "omnisPartnerInfoBerid": omnisPartnerInfoBerid,
       "omnisPartnerInfoConnect": omnisPartnerInfoConnect,
       "sniOmnisGroups": sniOmnisGroups,
       "omnisGroupsTabNum": omnisGroupsTabNum,
       "omnisGroupsSelectTID": omnisGroupsSelectTID,
       "omnisGroupsTable": omnisGroupsTable,
       "omnisGroupsEntry": omnisGroupsEntry,
       "omnisGroupsGAC": omnisGroupsGAC,
       "omnisGroupsPAC": omnisGroupsPAC,
       "omnisGroupsTid": omnisGroupsTid,
       "sniOmnisHardCopy": sniOmnisHardCopy,
       "omnisHardCopyStatus": omnisHardCopyStatus,
       "omnisHardCopyTabNum": omnisHardCopyTabNum,
       "omnisHardCopyTable": omnisHardCopyTable,
       "omnisHardCopyEntry": omnisHardCopyEntry,
       "omnisHardCopyHAC": omnisHardCopyHAC,
       "omnisHardCopyHID": omnisHardCopyHID,
       "omnisHardCopyPtnName": omnisHardCopyPtnName,
       "omnisHardCopyProName": omnisHardCopyProName,
       "omnisHardCopyState": omnisHardCopyState,
       "omnisHardCopyINOP": omnisHardCopyINOP,
       "omnisHardCopyConnect": omnisHardCopyConnect,
       "omnisHardCopyRestart": omnisHardCopyRestart,
       "sniOmnisHardCopyPIDs": sniOmnisHardCopyPIDs,
       "omnisHardCopyPIDsTabNum": omnisHardCopyPIDsTabNum,
       "omnisHardCopyPIDsSelectHid": omnisHardCopyPIDsSelectHid,
       "omnisHardCopyPIDsTable": omnisHardCopyPIDsTable,
       "omnisHardCopyPIDsEntry": omnisHardCopyPIDsEntry,
       "omnisHardCopyPIDsHID": omnisHardCopyPIDsHID,
       "omnisHardCopyPIDsID": omnisHardCopyPIDsID,
       "sniOmnisHardCopyTIDs": sniOmnisHardCopyTIDs,
       "omnisHardCopyTIDsTabNum": omnisHardCopyTIDsTabNum,
       "omnisHardCopyTIDsSelectHid": omnisHardCopyTIDsSelectHid,
       "omnisHardCopyTIDsTable": omnisHardCopyTIDsTable,
       "omnisHardCopyTIDsEntry": omnisHardCopyTIDsEntry,
       "omnisHardCopyTIDsHID": omnisHardCopyTIDsHID,
       "omnisHardCopyTIDsHAC": omnisHardCopyTIDsHAC,
       "omnisHardCopyTIDsID": omnisHardCopyTIDsID,
       "sniOmnisHardCopyCreate": sniOmnisHardCopyCreate,
       "omnisHardCopyCreateHAC": omnisHardCopyCreateHAC,
       "omnisHardCopyCreateHID": omnisHardCopyCreateHID,
       "omnisHardCopyCreatePtnName": omnisHardCopyCreatePtnName,
       "omnisHardCopyCreateProName": omnisHardCopyCreateProName,
       "omnisHardCopyCreateInop": omnisHardCopyCreateInop,
       "omnisHardCopyCreateConnect": omnisHardCopyCreateConnect,
       "sniOmnisOmnis": sniOmnisOmnis,
       "omnisOmnisStatus": omnisOmnisStatus,
       "omnisOmnisTabNum": omnisOmnisTabNum,
       "omnisOmnisTable": omnisOmnisTable,
       "omnisOmnisEntry": omnisOmnisEntry,
       "omnisOmnisOAC": omnisOmnisOAC,
       "omnisOmnisID": omnisOmnisID,
       "omnisOmnisPtnName": omnisOmnisPtnName,
       "omnisOmnisProName": omnisOmnisProName,
       "omnisOmnisState": omnisOmnisState,
       "omnisOmnisConnect": omnisOmnisConnect,
       "omnisOmnisTime": omnisOmnisTime,
       "omnisOmnisLPass": omnisOmnisLPass,
       "omnisOmnisOpncon": omnisOmnisOpncon,
       "omnisOmnisRestart": omnisOmnisRestart,
       "sniOmnisMux": sniOmnisMux,
       "omnisMuxStatus": omnisMuxStatus,
       "omnisMuxTabNum": omnisMuxTabNum,
       "omnisMuxTable": omnisMuxTable,
       "omnisMuxEntry": omnisMuxEntry,
       "omnisMuxID": omnisMuxID,
       "omnisMuxPtnName": omnisMuxPtnName,
       "omnisMuxProName": omnisMuxProName,
       "omnisMuxState": omnisMuxState,
       "omnisMuxConnect": omnisMuxConnect,
       "omnisMuxLPass": omnisMuxLPass,
       "omnisMuxSessions": omnisMuxSessions,
       "omnisMuxAvailability": omnisMuxAvailability,
       "sniOmnisExits": sniOmnisExits,
       "omnisExitTabNum": omnisExitTabNum,
       "omnisExitTable": omnisExitTable,
       "omnisExitEntry": omnisExitEntry,
       "omnisExitEAC": omnisExitEAC,
       "omnisExitID": omnisExitID,
       "omnisExitModul": omnisExitModul,
       "sniOmnisExitPIDs": sniOmnisExitPIDs,
       "omnisExitPIDsTabNum": omnisExitPIDsTabNum,
       "omnisExitPIDsSelectEac": omnisExitPIDsSelectEac,
       "omnisExitPIDsTable": omnisExitPIDsTable,
       "omnisExitPIDsEntry": omnisExitPIDsEntry,
       "omnisExitPIDsEAC": omnisExitPIDsEAC,
       "omnisExitPIDsID": omnisExitPIDsID,
       "sniOmnisExitTIDs": sniOmnisExitTIDs,
       "omnisExitTIDsTabNum": omnisExitTIDsTabNum,
       "omnisExitTIDsSelectEac": omnisExitTIDsSelectEac,
       "omnisExitTIDsTable": omnisExitTIDsTable,
       "omnisExitTIDsEntry": omnisExitTIDsEntry,
       "omnisExitTIDsEAC": omnisExitTIDsEAC,
       "omnisExitTIDsID": omnisExitTIDsID,
       "sniOmnisExitCreate": sniOmnisExitCreate,
       "omnisExitCreateEAC": omnisExitCreateEAC,
       "omnisExitCreateModul1": omnisExitCreateModul1,
       "omnisExitCreateModul2": omnisExitCreateModul2,
       "omnisExitCreateModul3": omnisExitCreateModul3,
       "omnisExitCreateModul4": omnisExitCreateModul4,
       "omnisExitCreateModul5": omnisExitCreateModul5,
       "omnisExitCreateModul6": omnisExitCreateModul6,
       "omnisExitCreateModul7": omnisExitCreateModul7,
       "omnisExitCreateModul8": omnisExitCreateModul8,
       "omnisExitCreateModul9": omnisExitCreateModul9,
       "omnisExitCreateModul10": omnisExitCreateModul10,
       "omnisExitCreateModul11": omnisExitCreateModul11,
       "omnisExitCreateModul12": omnisExitCreateModul12,
       "omnisExitCreateModul13": omnisExitCreateModul13,
       "omnisExitCreateModul14": omnisExitCreateModul14,
       "omnisExitCreateOption": omnisExitCreateOption,
       "sniOmnisTrace": sniOmnisTrace,
       "omnisTraceConnection": omnisTraceConnection,
       "omnisTraceExit": omnisTraceExit,
       "omnisTraceTransport": omnisTraceTransport,
       "omnisTraceTransportTrm": omnisTraceTransportTrm,
       "omnisTraceTransporthcy": omnisTraceTransporthcy,
       "omnisTraceTransportmux": omnisTraceTransportmux,
       "omnisTraceTransportoms": omnisTraceTransportoms,
       "sniOmnisTraps": sniOmnisTraps,
       "omnisStopTrap": omnisStopTrap,
       "omnisStartTrap": omnisStartTrap,
       "omnisConnStopTrap": omnisConnStopTrap,
       "omnisDstConnStopTrap": omnisDstConnStopTrap,
       "omnisEventTrap": omnisEventTrap,
       "omnisDstLevelTrap": omnisDstLevelTrap,
       "omnisPacLevelTrap": omnisPacLevelTrap,
       "omnisPtnLevelTrap": omnisPtnLevelTrap,
       "omnisMuxConnStopTrap": omnisMuxConnStopTrap,
       "omnisOmnConnStopTrap": omnisOmnConnStopTrap,
       "omnisHcConnStopTrap": omnisHcConnStopTrap,
       "omnisDumpWriteTrap": omnisDumpWriteTrap,
       "omnisDumpEndTrap": omnisDumpEndTrap,
       "omnisEndTrap": omnisEndTrap,
       "sniOmnisUserdefinedTraps": sniOmnisUserdefinedTraps,
       "omnisUserdefinedTrapData": omnisUserdefinedTrapData,
       "omnisTrapMsgText": omnisTrapMsgText,
       "omnisUserdefinedTrap": omnisUserdefinedTrap,
       "omnisGeneralTrap": omnisGeneralTrap}
)
