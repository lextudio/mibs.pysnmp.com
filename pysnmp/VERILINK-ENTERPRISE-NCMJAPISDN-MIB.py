# SNMP MIB module (VERILINK-ENTERPRISE-NCMJAPISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMJAPISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:17 2024
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

(ncm_japisdn,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-japisdn")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmJapPRIPortConfigTable_Object = MibTable
ncmJapPRIPortConfigTable = _NcmJapPRIPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000)
)
if mibBuilder.loadTexts:
    ncmJapPRIPortConfigTable.setStatus("mandatory")
_NcmJapPRIPortConfigEntry_Object = MibTableRow
ncmJapPRIPortConfigEntry = _NcmJapPRIPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1)
)
ncmJapPRIPortConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIPortNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIPortLineIndex"),
)
if mibBuilder.loadTexts:
    ncmJapPRIPortConfigEntry.setStatus("mandatory")


class _NcmJapPRIPortNIDIndex_Type(Integer32):
    """Custom type ncmJapPRIPortNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRIPortNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRIPortNIDIndex_Object = MibTableColumn
ncmJapPRIPortNIDIndex = _NcmJapPRIPortNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 1),
    _NcmJapPRIPortNIDIndex_Type()
)
ncmJapPRIPortNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIPortNIDIndex.setStatus("mandatory")


class _NcmJapPRIPortLineIndex_Type(Integer32):
    """Custom type ncmJapPRIPortLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRIPortLineIndex_Type.__name__ = "Integer32"
_NcmJapPRIPortLineIndex_Object = MibTableColumn
ncmJapPRIPortLineIndex = _NcmJapPRIPortLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 2),
    _NcmJapPRIPortLineIndex_Type()
)
ncmJapPRIPortLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIPortLineIndex.setStatus("mandatory")


class _NcmJapPRIPortInService_Type(Integer32):
    """Custom type ncmJapPRIPortInService based on Integer32"""
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


_NcmJapPRIPortInService_Type.__name__ = "Integer32"
_NcmJapPRIPortInService_Object = MibTableColumn
ncmJapPRIPortInService = _NcmJapPRIPortInService_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 3),
    _NcmJapPRIPortInService_Type()
)
ncmJapPRIPortInService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortInService.setStatus("mandatory")


class _NcmJapPRIPortNFASMode_Type(Integer32):
    """Custom type ncmJapPRIPortNFASMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nfas-Backup", 3),
          ("nfas-No-Backup", 2),
          ("no-Nfas", 1))
    )


_NcmJapPRIPortNFASMode_Type.__name__ = "Integer32"
_NcmJapPRIPortNFASMode_Object = MibTableColumn
ncmJapPRIPortNFASMode = _NcmJapPRIPortNFASMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 4),
    _NcmJapPRIPortNFASMode_Type()
)
ncmJapPRIPortNFASMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortNFASMode.setStatus("mandatory")


class _NcmJapPRIPortDChanMode_Type(Integer32):
    """Custom type ncmJapPRIPortDChanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_NcmJapPRIPortDChanMode_Type.__name__ = "Integer32"
_NcmJapPRIPortDChanMode_Object = MibTableColumn
ncmJapPRIPortDChanMode = _NcmJapPRIPortDChanMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 5),
    _NcmJapPRIPortDChanMode_Type()
)
ncmJapPRIPortDChanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortDChanMode.setStatus("mandatory")


class _NcmJapPRIPortDChanBits_Type(Integer32):
    """Custom type ncmJapPRIPortDChanBits based on Integer32"""
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
        *(("chan-6-Bit", 3),
          ("chan-7-Bit", 2),
          ("chan-8-Bit", 1),
          ("undefined", 4))
    )


_NcmJapPRIPortDChanBits_Type.__name__ = "Integer32"
_NcmJapPRIPortDChanBits_Object = MibTableColumn
ncmJapPRIPortDChanBits = _NcmJapPRIPortDChanBits_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 6),
    _NcmJapPRIPortDChanBits_Type()
)
ncmJapPRIPortDChanBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortDChanBits.setStatus("mandatory")
_NcmJapPRIPortTimeslotMap_Type = DisplayString
_NcmJapPRIPortTimeslotMap_Object = MibTableColumn
ncmJapPRIPortTimeslotMap = _NcmJapPRIPortTimeslotMap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 7),
    _NcmJapPRIPortTimeslotMap_Type()
)
ncmJapPRIPortTimeslotMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortTimeslotMap.setStatus("mandatory")


class _NcmJapPRIPortSwitchType_Type(Integer32):
    """Custom type ncmJapPRIPortSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            15
        )
    )
    namedValues = NamedValues(
        ("sw-NTT", 15)
    )


_NcmJapPRIPortSwitchType_Type.__name__ = "Integer32"
_NcmJapPRIPortSwitchType_Object = MibTableColumn
ncmJapPRIPortSwitchType = _NcmJapPRIPortSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 8),
    _NcmJapPRIPortSwitchType_Type()
)
ncmJapPRIPortSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortSwitchType.setStatus("mandatory")


class _NcmJapPRIPortOwnNumPlan_Type(Integer32):
    """Custom type ncmJapPRIPortOwnNumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unkn-NumPlan", 1)
    )


_NcmJapPRIPortOwnNumPlan_Type.__name__ = "Integer32"
_NcmJapPRIPortOwnNumPlan_Object = MibTableColumn
ncmJapPRIPortOwnNumPlan = _NcmJapPRIPortOwnNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 9),
    _NcmJapPRIPortOwnNumPlan_Type()
)
ncmJapPRIPortOwnNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortOwnNumPlan.setStatus("mandatory")


class _NcmJapPRIPortOwnNumType_Type(Integer32):
    """Custom type ncmJapPRIPortOwnNumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unkn-NumType", 1)
    )


_NcmJapPRIPortOwnNumType_Type.__name__ = "Integer32"
_NcmJapPRIPortOwnNumType_Object = MibTableColumn
ncmJapPRIPortOwnNumType = _NcmJapPRIPortOwnNumType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 10),
    _NcmJapPRIPortOwnNumType_Type()
)
ncmJapPRIPortOwnNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortOwnNumType.setStatus("mandatory")


class _NcmJapPRIPortSecurityLevel_Type(Integer32):
    """Custom type ncmJapPRIPortSecurityLevel based on Integer32"""
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
        *(("both-Numbers", 4),
          ("ext-Numbers", 3),
          ("no-Checks", 1),
          ("own-Numbers", 2))
    )


_NcmJapPRIPortSecurityLevel_Type.__name__ = "Integer32"
_NcmJapPRIPortSecurityLevel_Object = MibTableColumn
ncmJapPRIPortSecurityLevel = _NcmJapPRIPortSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 11),
    _NcmJapPRIPortSecurityLevel_Type()
)
ncmJapPRIPortSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortSecurityLevel.setStatus("mandatory")


class _NcmJapPRIPortConfigStatus_Type(Integer32):
    """Custom type ncmJapPRIPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration-Error", 2),
          ("configuration-OK", 1))
    )


_NcmJapPRIPortConfigStatus_Type.__name__ = "Integer32"
_NcmJapPRIPortConfigStatus_Object = MibTableColumn
ncmJapPRIPortConfigStatus = _NcmJapPRIPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 12),
    _NcmJapPRIPortConfigStatus_Type()
)
ncmJapPRIPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIPortConfigStatus.setStatus("mandatory")


class _NcmJapPRIPortSetConfig_Type(Integer32):
    """Custom type ncmJapPRIPortSetConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-in-use", 2),
          ("set-Config", 1))
    )


_NcmJapPRIPortSetConfig_Type.__name__ = "Integer32"
_NcmJapPRIPortSetConfig_Object = MibTableColumn
ncmJapPRIPortSetConfig = _NcmJapPRIPortSetConfig_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 13),
    _NcmJapPRIPortSetConfig_Type()
)
ncmJapPRIPortSetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIPortSetConfig.setStatus("mandatory")
_NcmJapPRICallProfCallRefCount_Type = Integer32
_NcmJapPRICallProfCallRefCount_Object = MibTableColumn
ncmJapPRICallProfCallRefCount = _NcmJapPRICallProfCallRefCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 14),
    _NcmJapPRICallProfCallRefCount_Type()
)
ncmJapPRICallProfCallRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICallProfCallRefCount.setStatus("mandatory")


class _NcmJapPRIL2AutoEstablish_Type(Integer32):
    """Custom type ncmJapPRIL2AutoEstablish based on Integer32"""
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


_NcmJapPRIL2AutoEstablish_Type.__name__ = "Integer32"
_NcmJapPRIL2AutoEstablish_Object = MibTableColumn
ncmJapPRIL2AutoEstablish = _NcmJapPRIL2AutoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 15),
    _NcmJapPRIL2AutoEstablish_Type()
)
ncmJapPRIL2AutoEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRIL2AutoEstablish.setStatus("mandatory")
_NcmJapPRICallProfileTable_Object = MibTable
ncmJapPRICallProfileTable = _NcmJapPRICallProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001)
)
if mibBuilder.loadTexts:
    ncmJapPRICallProfileTable.setStatus("mandatory")
_NcmJapPRICallProfEntry_Object = MibTableRow
ncmJapPRICallProfEntry = _NcmJapPRICallProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1)
)
ncmJapPRICallProfEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICallProfNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICallProfLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPCallProfileRef"),
)
if mibBuilder.loadTexts:
    ncmJapPRICallProfEntry.setStatus("mandatory")


class _NcmJapPRICallProfNIDIndex_Type(Integer32):
    """Custom type ncmJapPRICallProfNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICallProfNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRICallProfNIDIndex_Object = MibTableColumn
ncmJapPRICallProfNIDIndex = _NcmJapPRICallProfNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 1),
    _NcmJapPRICallProfNIDIndex_Type()
)
ncmJapPRICallProfNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICallProfNIDIndex.setStatus("mandatory")


class _NcmJapPRICallProfLineIndex_Type(Integer32):
    """Custom type ncmJapPRICallProfLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICallProfLineIndex_Type.__name__ = "Integer32"
_NcmJapPRICallProfLineIndex_Object = MibTableColumn
ncmJapPRICallProfLineIndex = _NcmJapPRICallProfLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 2),
    _NcmJapPRICallProfLineIndex_Type()
)
ncmJapPRICallProfLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICallProfLineIndex.setStatus("mandatory")
_NcmJapPRICPCallProfileRef_Type = Integer32
_NcmJapPRICPCallProfileRef_Object = MibTableColumn
ncmJapPRICPCallProfileRef = _NcmJapPRICPCallProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 3),
    _NcmJapPRICPCallProfileRef_Type()
)
ncmJapPRICPCallProfileRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICPCallProfileRef.setStatus("mandatory")


class _NcmJapPRICallProfCallDir_Type(Integer32):
    """Custom type ncmJapPRICallProfCallDir based on Integer32"""
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
        *(("both-Directions", 4),
          ("incoming", 2),
          ("no-Direction", 1),
          ("outgoing", 3))
    )


_NcmJapPRICallProfCallDir_Type.__name__ = "Integer32"
_NcmJapPRICallProfCallDir_Object = MibTableColumn
ncmJapPRICallProfCallDir = _NcmJapPRICallProfCallDir_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 4),
    _NcmJapPRICallProfCallDir_Type()
)
ncmJapPRICallProfCallDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfCallDir.setStatus("mandatory")
_NcmJapPRICallProfNumOwnDigit_Type = Integer32
_NcmJapPRICallProfNumOwnDigit_Object = MibTableColumn
ncmJapPRICallProfNumOwnDigit = _NcmJapPRICallProfNumOwnDigit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 5),
    _NcmJapPRICallProfNumOwnDigit_Type()
)
ncmJapPRICallProfNumOwnDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfNumOwnDigit.setStatus("mandatory")
_NcmJapPRICallProfOwnCallNum_Type = DisplayString
_NcmJapPRICallProfOwnCallNum_Object = MibTableColumn
ncmJapPRICallProfOwnCallNum = _NcmJapPRICallProfOwnCallNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 6),
    _NcmJapPRICallProfOwnCallNum_Type()
)
ncmJapPRICallProfOwnCallNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfOwnCallNum.setStatus("mandatory")


class _NcmJapPRICallProfExtNumPlan_Type(Integer32):
    """Custom type ncmJapPRICallProfExtNumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unkn-NumPlan", 1)
    )


_NcmJapPRICallProfExtNumPlan_Type.__name__ = "Integer32"
_NcmJapPRICallProfExtNumPlan_Object = MibTableColumn
ncmJapPRICallProfExtNumPlan = _NcmJapPRICallProfExtNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 7),
    _NcmJapPRICallProfExtNumPlan_Type()
)
ncmJapPRICallProfExtNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfExtNumPlan.setStatus("mandatory")


class _NcmJapPRICallProfExtNumType_Type(Integer32):
    """Custom type ncmJapPRICallProfExtNumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unkn-NumType", 1)
    )


_NcmJapPRICallProfExtNumType_Type.__name__ = "Integer32"
_NcmJapPRICallProfExtNumType_Object = MibTableColumn
ncmJapPRICallProfExtNumType = _NcmJapPRICallProfExtNumType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 8),
    _NcmJapPRICallProfExtNumType_Type()
)
ncmJapPRICallProfExtNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfExtNumType.setStatus("mandatory")
_NcmJapPRICallProfExtNumDigit_Type = Integer32
_NcmJapPRICallProfExtNumDigit_Object = MibTableColumn
ncmJapPRICallProfExtNumDigit = _NcmJapPRICallProfExtNumDigit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 9),
    _NcmJapPRICallProfExtNumDigit_Type()
)
ncmJapPRICallProfExtNumDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfExtNumDigit.setStatus("mandatory")
_NcmJapPRICallProfExtCallNum_Type = DisplayString
_NcmJapPRICallProfExtCallNum_Object = MibTableColumn
ncmJapPRICallProfExtCallNum = _NcmJapPRICallProfExtCallNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 10),
    _NcmJapPRICallProfExtCallNum_Type()
)
ncmJapPRICallProfExtCallNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfExtCallNum.setStatus("mandatory")


class _NcmJapPRICallProfTransferMode_Type(Integer32):
    """Custom type ncmJapPRICallProfTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("unrestricted-digital", 8)
    )


_NcmJapPRICallProfTransferMode_Type.__name__ = "Integer32"
_NcmJapPRICallProfTransferMode_Object = MibTableColumn
ncmJapPRICallProfTransferMode = _NcmJapPRICallProfTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 11),
    _NcmJapPRICallProfTransferMode_Type()
)
ncmJapPRICallProfTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfTransferMode.setStatus("mandatory")


class _NcmJapPRICallProfCallBandWth_Type(Integer32):
    """Custom type ncmJapPRICallProfCallBandWth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              19,
              21)
        )
    )
    namedValues = NamedValues(
        *(("b1-64K", 16),
          ("h0-6X64K", 19),
          ("h11-24X64K", 21))
    )


_NcmJapPRICallProfCallBandWth_Type.__name__ = "Integer32"
_NcmJapPRICallProfCallBandWth_Object = MibTableColumn
ncmJapPRICallProfCallBandWth = _NcmJapPRICallProfCallBandWth_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 12),
    _NcmJapPRICallProfCallBandWth_Type()
)
ncmJapPRICallProfCallBandWth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfCallBandWth.setStatus("mandatory")


class _NcmJapPRICallProfMultiRateCnt_Type(Integer32):
    """Custom type ncmJapPRICallProfMultiRateCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              12,
              23,
              24,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("mR-12", 12),
          ("mR-2", 2),
          ("mR-23", 23),
          ("mR-24", 24),
          ("mR-30", 30),
          ("mR-31", 31),
          ("mR-4", 4),
          ("mR-6", 6),
          ("mR-8", 8))
    )


_NcmJapPRICallProfMultiRateCnt_Type.__name__ = "Integer32"
_NcmJapPRICallProfMultiRateCnt_Object = MibTableColumn
ncmJapPRICallProfMultiRateCnt = _NcmJapPRICallProfMultiRateCnt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 13),
    _NcmJapPRICallProfMultiRateCnt_Type()
)
ncmJapPRICallProfMultiRateCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfMultiRateCnt.setStatus("mandatory")


class _NcmJapPRICallProfRateAdaptn_Type(Integer32):
    """Custom type ncmJapPRICallProfRateAdaptn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adapt-56K", 2),
          ("no-Adapt", 1))
    )


_NcmJapPRICallProfRateAdaptn_Type.__name__ = "Integer32"
_NcmJapPRICallProfRateAdaptn_Object = MibTableColumn
ncmJapPRICallProfRateAdaptn = _NcmJapPRICallProfRateAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 14),
    _NcmJapPRICallProfRateAdaptn_Type()
)
ncmJapPRICallProfRateAdaptn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfRateAdaptn.setStatus("mandatory")
_NcmJapPRICallProfTestCallIntvl_Type = Integer32
_NcmJapPRICallProfTestCallIntvl_Object = MibTableColumn
ncmJapPRICallProfTestCallIntvl = _NcmJapPRICallProfTestCallIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 15),
    _NcmJapPRICallProfTestCallIntvl_Type()
)
ncmJapPRICallProfTestCallIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfTestCallIntvl.setStatus("mandatory")


class _NcmJapPRICallProfCallStatus_Type(Integer32):
    """Custom type ncmJapPRICallProfCallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail-Takedown-Idle", 1),
          ("successful-Setup", 2),
          ("unknown", 3))
    )


_NcmJapPRICallProfCallStatus_Type.__name__ = "Integer32"
_NcmJapPRICallProfCallStatus_Object = MibTableColumn
ncmJapPRICallProfCallStatus = _NcmJapPRICallProfCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 16),
    _NcmJapPRICallProfCallStatus_Type()
)
ncmJapPRICallProfCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICallProfCallStatus.setStatus("mandatory")


class _NcmJapPRICallProfCallAction_Type(Integer32):
    """Custom type ncmJapPRICallProfCallAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setup-Call", 1),
          ("takedown-Call", 2))
    )


_NcmJapPRICallProfCallAction_Type.__name__ = "Integer32"
_NcmJapPRICallProfCallAction_Object = MibTableColumn
ncmJapPRICallProfCallAction = _NcmJapPRICallProfCallAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 17),
    _NcmJapPRICallProfCallAction_Type()
)
ncmJapPRICallProfCallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICallProfCallAction.setStatus("mandatory")


class _NcmJapPRICPSetCallProf_Type(Integer32):
    """Custom type ncmJapPRICPSetCallProf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-in-use", 2),
          ("set-CallProf", 1))
    )


_NcmJapPRICPSetCallProf_Type.__name__ = "Integer32"
_NcmJapPRICPSetCallProf_Object = MibTableColumn
ncmJapPRICPSetCallProf = _NcmJapPRICPSetCallProf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 18),
    _NcmJapPRICPSetCallProf_Type()
)
ncmJapPRICPSetCallProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICPSetCallProf.setStatus("mandatory")


class _NcmJapPRICPSetCallProfResp_Type(Integer32):
    """Custom type ncmJapPRICPSetCallProfResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration-Error", 2),
          ("configuration-OK", 1))
    )


_NcmJapPRICPSetCallProfResp_Type.__name__ = "Integer32"
_NcmJapPRICPSetCallProfResp_Object = MibTableColumn
ncmJapPRICPSetCallProfResp = _NcmJapPRICPSetCallProfResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 19),
    _NcmJapPRICPSetCallProfResp_Type()
)
ncmJapPRICPSetCallProfResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPSetCallProfResp.setStatus("mandatory")


class _NcmJapPRICPCallActionResp_Type(Integer32):
    """Custom type ncmJapPRICPCallActionResp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration-Error", 2),
          ("configuration-OK", 1))
    )


_NcmJapPRICPCallActionResp_Type.__name__ = "Integer32"
_NcmJapPRICPCallActionResp_Object = MibTableColumn
ncmJapPRICPCallActionResp = _NcmJapPRICPCallActionResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 20),
    _NcmJapPRICPCallActionResp_Type()
)
ncmJapPRICPCallActionResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPCallActionResp.setStatus("mandatory")
_NcmJapPRICallProfListTable_Object = MibTable
ncmJapPRICallProfListTable = _NcmJapPRICallProfListTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002)
)
if mibBuilder.loadTexts:
    ncmJapPRICallProfListTable.setStatus("mandatory")
_NcmJapPRICallProfListEntry_Object = MibTableRow
ncmJapPRICallProfListEntry = _NcmJapPRICallProfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1)
)
ncmJapPRICallProfListEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListIndex"),
)
if mibBuilder.loadTexts:
    ncmJapPRICallProfListEntry.setStatus("mandatory")


class _NcmJapPRICPListNIDIndex_Type(Integer32):
    """Custom type ncmJapPRICPListNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICPListNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRICPListNIDIndex_Object = MibTableColumn
ncmJapPRICPListNIDIndex = _NcmJapPRICPListNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 1),
    _NcmJapPRICPListNIDIndex_Type()
)
ncmJapPRICPListNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPListNIDIndex.setStatus("mandatory")


class _NcmJapPRICPListLineIndex_Type(Integer32):
    """Custom type ncmJapPRICPListLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICPListLineIndex_Type.__name__ = "Integer32"
_NcmJapPRICPListLineIndex_Object = MibTableColumn
ncmJapPRICPListLineIndex = _NcmJapPRICPListLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 2),
    _NcmJapPRICPListLineIndex_Type()
)
ncmJapPRICPListLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPListLineIndex.setStatus("mandatory")
_NcmJapPRICPListIndex_Type = Integer32
_NcmJapPRICPListIndex_Object = MibTableColumn
ncmJapPRICPListIndex = _NcmJapPRICPListIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 3),
    _NcmJapPRICPListIndex_Type()
)
ncmJapPRICPListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPListIndex.setStatus("mandatory")
_NcmJapPRICPListValidCPRefNum_Type = Integer32
_NcmJapPRICPListValidCPRefNum_Object = MibTableColumn
ncmJapPRICPListValidCPRefNum = _NcmJapPRICPListValidCPRefNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 4),
    _NcmJapPRICPListValidCPRefNum_Type()
)
ncmJapPRICPListValidCPRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICPListValidCPRefNum.setStatus("mandatory")
_NcmJapPRICurrentTable_Object = MibTable
ncmJapPRICurrentTable = _NcmJapPRICurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003)
)
if mibBuilder.loadTexts:
    ncmJapPRICurrentTable.setStatus("mandatory")
_NcmJapPRICurrentEntry_Object = MibTableRow
ncmJapPRICurrentEntry = _NcmJapPRICurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1)
)
ncmJapPRICurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrEndType"),
)
if mibBuilder.loadTexts:
    ncmJapPRICurrentEntry.setStatus("mandatory")


class _NcmJapPRICurrNIDIndex_Type(Integer32):
    """Custom type ncmJapPRICurrNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICurrNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRICurrNIDIndex_Object = MibTableColumn
ncmJapPRICurrNIDIndex = _NcmJapPRICurrNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 1),
    _NcmJapPRICurrNIDIndex_Type()
)
ncmJapPRICurrNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrNIDIndex.setStatus("mandatory")


class _NcmJapPRICurrLineIndex_Type(Integer32):
    """Custom type ncmJapPRICurrLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICurrLineIndex_Type.__name__ = "Integer32"
_NcmJapPRICurrLineIndex_Object = MibTableColumn
ncmJapPRICurrLineIndex = _NcmJapPRICurrLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 2),
    _NcmJapPRICurrLineIndex_Type()
)
ncmJapPRICurrLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrLineIndex.setStatus("mandatory")


class _NcmJapPRICurrEndType_Type(Integer32):
    """Custom type ncmJapPRICurrEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmJapPRICurrEndType_Type.__name__ = "Integer32"
_NcmJapPRICurrEndType_Object = MibTableColumn
ncmJapPRICurrEndType = _NcmJapPRICurrEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 3),
    _NcmJapPRICurrEndType_Type()
)
ncmJapPRICurrEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrEndType.setStatus("mandatory")
_NcmJapPRICurrTimestamp_Type = Integer32
_NcmJapPRICurrTimestamp_Object = MibTableColumn
ncmJapPRICurrTimestamp = _NcmJapPRICurrTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 4),
    _NcmJapPRICurrTimestamp_Type()
)
ncmJapPRICurrTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrTimestamp.setStatus("mandatory")
_NcmJapPRICurrSecsInCurrIntvl_Type = Integer32
_NcmJapPRICurrSecsInCurrIntvl_Object = MibTableColumn
ncmJapPRICurrSecsInCurrIntvl = _NcmJapPRICurrSecsInCurrIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 5),
    _NcmJapPRICurrSecsInCurrIntvl_Type()
)
ncmJapPRICurrSecsInCurrIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrSecsInCurrIntvl.setStatus("mandatory")
_NcmJapPRICurrInfoRx_Type = Integer32
_NcmJapPRICurrInfoRx_Object = MibTableColumn
ncmJapPRICurrInfoRx = _NcmJapPRICurrInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 6),
    _NcmJapPRICurrInfoRx_Type()
)
ncmJapPRICurrInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrInfoRx.setStatus("mandatory")
_NcmJapPRICurrInfoTx_Type = Integer32
_NcmJapPRICurrInfoTx_Object = MibTableColumn
ncmJapPRICurrInfoTx = _NcmJapPRICurrInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 7),
    _NcmJapPRICurrInfoTx_Type()
)
ncmJapPRICurrInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrInfoTx.setStatus("mandatory")
_NcmJapPRICurrCRCErrRx_Type = Integer32
_NcmJapPRICurrCRCErrRx_Object = MibTableColumn
ncmJapPRICurrCRCErrRx = _NcmJapPRICurrCRCErrRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 8),
    _NcmJapPRICurrCRCErrRx_Type()
)
ncmJapPRICurrCRCErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrCRCErrRx.setStatus("mandatory")
_NcmJapPRICurrInvalidFrameRx_Type = Integer32
_NcmJapPRICurrInvalidFrameRx_Object = MibTableColumn
ncmJapPRICurrInvalidFrameRx = _NcmJapPRICurrInvalidFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 9),
    _NcmJapPRICurrInvalidFrameRx_Type()
)
ncmJapPRICurrInvalidFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrInvalidFrameRx.setStatus("mandatory")
_NcmJapPRICurrFrameAbortRx_Type = Integer32
_NcmJapPRICurrFrameAbortRx_Object = MibTableColumn
ncmJapPRICurrFrameAbortRx = _NcmJapPRICurrFrameAbortRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 10),
    _NcmJapPRICurrFrameAbortRx_Type()
)
ncmJapPRICurrFrameAbortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrFrameAbortRx.setStatus("mandatory")
_NcmJapPRICurrDISCSRx_Type = Integer32
_NcmJapPRICurrDISCSRx_Object = MibTableColumn
ncmJapPRICurrDISCSRx = _NcmJapPRICurrDISCSRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 11),
    _NcmJapPRICurrDISCSRx_Type()
)
ncmJapPRICurrDISCSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrDISCSRx.setStatus("mandatory")
_NcmJapPRICurrDISCSTx_Type = Integer32
_NcmJapPRICurrDISCSTx_Object = MibTableColumn
ncmJapPRICurrDISCSTx = _NcmJapPRICurrDISCSTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 12),
    _NcmJapPRICurrDISCSTx_Type()
)
ncmJapPRICurrDISCSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrDISCSTx.setStatus("mandatory")
_NcmJapPRICurrFramerRx_Type = Integer32
_NcmJapPRICurrFramerRx_Object = MibTableColumn
ncmJapPRICurrFramerRx = _NcmJapPRICurrFramerRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 13),
    _NcmJapPRICurrFramerRx_Type()
)
ncmJapPRICurrFramerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrFramerRx.setStatus("mandatory")
_NcmJapPRICurrFramerTx_Type = Integer32
_NcmJapPRICurrFramerTx_Object = MibTableColumn
ncmJapPRICurrFramerTx = _NcmJapPRICurrFramerTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 14),
    _NcmJapPRICurrFramerTx_Type()
)
ncmJapPRICurrFramerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrFramerTx.setStatus("mandatory")
_NcmJapPRICurrLyr3ProtErr_Type = Integer32
_NcmJapPRICurrLyr3ProtErr_Object = MibTableColumn
ncmJapPRICurrLyr3ProtErr = _NcmJapPRICurrLyr3ProtErr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 15),
    _NcmJapPRICurrLyr3ProtErr_Type()
)
ncmJapPRICurrLyr3ProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrLyr3ProtErr.setStatus("mandatory")
_NcmJapPRICurrCallSetupSent_Type = Integer32
_NcmJapPRICurrCallSetupSent_Object = MibTableColumn
ncmJapPRICurrCallSetupSent = _NcmJapPRICurrCallSetupSent_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 16),
    _NcmJapPRICurrCallSetupSent_Type()
)
ncmJapPRICurrCallSetupSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrCallSetupSent.setStatus("mandatory")
_NcmJapPRICurrCallSetupSentnFail_Type = Integer32
_NcmJapPRICurrCallSetupSentnFail_Object = MibTableColumn
ncmJapPRICurrCallSetupSentnFail = _NcmJapPRICurrCallSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 17),
    _NcmJapPRICurrCallSetupSentnFail_Type()
)
ncmJapPRICurrCallSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrCallSetupSentnFail.setStatus("mandatory")
_NcmJapPRICurrCallSetupRx_Type = Integer32
_NcmJapPRICurrCallSetupRx_Object = MibTableColumn
ncmJapPRICurrCallSetupRx = _NcmJapPRICurrCallSetupRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 18),
    _NcmJapPRICurrCallSetupRx_Type()
)
ncmJapPRICurrCallSetupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrCallSetupRx.setStatus("mandatory")
_NcmJapPRICurrCallSetupRxnFail_Type = Integer32
_NcmJapPRICurrCallSetupRxnFail_Object = MibTableColumn
ncmJapPRICurrCallSetupRxnFail = _NcmJapPRICurrCallSetupRxnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 19),
    _NcmJapPRICurrCallSetupRxnFail_Type()
)
ncmJapPRICurrCallSetupRxnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrCallSetupRxnFail.setStatus("mandatory")
_NcmJapPRICurrUnSupportMsgRx_Type = Integer32
_NcmJapPRICurrUnSupportMsgRx_Object = MibTableColumn
ncmJapPRICurrUnSupportMsgRx = _NcmJapPRICurrUnSupportMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 20),
    _NcmJapPRICurrUnSupportMsgRx_Type()
)
ncmJapPRICurrUnSupportMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrUnSupportMsgRx.setStatus("mandatory")
_NcmJapPRICurrTstCalSetupSentnFail_Type = Integer32
_NcmJapPRICurrTstCalSetupSentnFail_Object = MibTableColumn
ncmJapPRICurrTstCalSetupSentnFail = _NcmJapPRICurrTstCalSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 21),
    _NcmJapPRICurrTstCalSetupSentnFail_Type()
)
ncmJapPRICurrTstCalSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrTstCalSetupSentnFail.setStatus("mandatory")
_NcmJapPRICurrValidIntvls_Type = Integer32
_NcmJapPRICurrValidIntvls_Object = MibTableColumn
ncmJapPRICurrValidIntvls = _NcmJapPRICurrValidIntvls_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 22),
    _NcmJapPRICurrValidIntvls_Type()
)
ncmJapPRICurrValidIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICurrValidIntvls.setStatus("mandatory")


class _NcmJapPRICurrStatisticReset_Type(Integer32):
    """Custom type ncmJapPRICurrStatisticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-in-use", 2),
          ("statistic-Reset", 1))
    )


_NcmJapPRICurrStatisticReset_Type.__name__ = "Integer32"
_NcmJapPRICurrStatisticReset_Object = MibTableColumn
ncmJapPRICurrStatisticReset = _NcmJapPRICurrStatisticReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 23),
    _NcmJapPRICurrStatisticReset_Type()
)
ncmJapPRICurrStatisticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRICurrStatisticReset.setStatus("mandatory")
_NcmJapPRIIntervalTable_Object = MibTable
ncmJapPRIIntervalTable = _NcmJapPRIIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004)
)
if mibBuilder.loadTexts:
    ncmJapPRIIntervalTable.setStatus("mandatory")
_NcmJapPRIIntervalEntry_Object = MibTableRow
ncmJapPRIIntervalEntry = _NcmJapPRIIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1)
)
ncmJapPRIIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlEndType"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlIndex"),
)
if mibBuilder.loadTexts:
    ncmJapPRIIntervalEntry.setStatus("mandatory")


class _NcmJapPRIntvlNIDIndex_Type(Integer32):
    """Custom type ncmJapPRIntvlNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRIntvlNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRIntvlNIDIndex_Object = MibTableColumn
ncmJapPRIntvlNIDIndex = _NcmJapPRIntvlNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 1),
    _NcmJapPRIntvlNIDIndex_Type()
)
ncmJapPRIntvlNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlNIDIndex.setStatus("mandatory")


class _NcmJapPRIntvlLineIndex_Type(Integer32):
    """Custom type ncmJapPRIntvlLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRIntvlLineIndex_Type.__name__ = "Integer32"
_NcmJapPRIntvlLineIndex_Object = MibTableColumn
ncmJapPRIntvlLineIndex = _NcmJapPRIntvlLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 2),
    _NcmJapPRIntvlLineIndex_Type()
)
ncmJapPRIntvlLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlLineIndex.setStatus("mandatory")


class _NcmJapPRIntvlEndType_Type(Integer32):
    """Custom type ncmJapPRIntvlEndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 2),
          ("near-End", 1))
    )


_NcmJapPRIntvlEndType_Type.__name__ = "Integer32"
_NcmJapPRIntvlEndType_Object = MibTableColumn
ncmJapPRIntvlEndType = _NcmJapPRIntvlEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 3),
    _NcmJapPRIntvlEndType_Type()
)
ncmJapPRIntvlEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlEndType.setStatus("mandatory")
_NcmJapPRIntvlIndex_Type = Integer32
_NcmJapPRIntvlIndex_Object = MibTableColumn
ncmJapPRIntvlIndex = _NcmJapPRIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 4),
    _NcmJapPRIntvlIndex_Type()
)
ncmJapPRIntvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlIndex.setStatus("mandatory")
_NcmJapPRIntvlTimestamp_Type = Integer32
_NcmJapPRIntvlTimestamp_Object = MibTableColumn
ncmJapPRIntvlTimestamp = _NcmJapPRIntvlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 5),
    _NcmJapPRIntvlTimestamp_Type()
)
ncmJapPRIntvlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlTimestamp.setStatus("mandatory")
_NcmJapPRIntvlSecsInCurrIntvl_Type = Integer32
_NcmJapPRIntvlSecsInCurrIntvl_Object = MibTableColumn
ncmJapPRIntvlSecsInCurrIntvl = _NcmJapPRIntvlSecsInCurrIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 6),
    _NcmJapPRIntvlSecsInCurrIntvl_Type()
)
ncmJapPRIntvlSecsInCurrIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlSecsInCurrIntvl.setStatus("mandatory")
_NcmJapPRIntvlInfoRx_Type = Integer32
_NcmJapPRIntvlInfoRx_Object = MibTableColumn
ncmJapPRIntvlInfoRx = _NcmJapPRIntvlInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 7),
    _NcmJapPRIntvlInfoRx_Type()
)
ncmJapPRIntvlInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlInfoRx.setStatus("mandatory")
_NcmJapPRIntvlInfoTx_Type = Integer32
_NcmJapPRIntvlInfoTx_Object = MibTableColumn
ncmJapPRIntvlInfoTx = _NcmJapPRIntvlInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 8),
    _NcmJapPRIntvlInfoTx_Type()
)
ncmJapPRIntvlInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlInfoTx.setStatus("mandatory")
_NcmJapPRIntvlCRCErrRx_Type = Integer32
_NcmJapPRIntvlCRCErrRx_Object = MibTableColumn
ncmJapPRIntvlCRCErrRx = _NcmJapPRIntvlCRCErrRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 9),
    _NcmJapPRIntvlCRCErrRx_Type()
)
ncmJapPRIntvlCRCErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlCRCErrRx.setStatus("mandatory")
_NcmJapPRIntvlInvalidFrameRx_Type = Integer32
_NcmJapPRIntvlInvalidFrameRx_Object = MibTableColumn
ncmJapPRIntvlInvalidFrameRx = _NcmJapPRIntvlInvalidFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 10),
    _NcmJapPRIntvlInvalidFrameRx_Type()
)
ncmJapPRIntvlInvalidFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlInvalidFrameRx.setStatus("mandatory")
_NcmJapPRIntvlFrameAbortRx_Type = Integer32
_NcmJapPRIntvlFrameAbortRx_Object = MibTableColumn
ncmJapPRIntvlFrameAbortRx = _NcmJapPRIntvlFrameAbortRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 11),
    _NcmJapPRIntvlFrameAbortRx_Type()
)
ncmJapPRIntvlFrameAbortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlFrameAbortRx.setStatus("mandatory")
_NcmJapPRIntvlDISCSRx_Type = Integer32
_NcmJapPRIntvlDISCSRx_Object = MibTableColumn
ncmJapPRIntvlDISCSRx = _NcmJapPRIntvlDISCSRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 12),
    _NcmJapPRIntvlDISCSRx_Type()
)
ncmJapPRIntvlDISCSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlDISCSRx.setStatus("mandatory")
_NcmJapPRIntvlDISCSTx_Type = Integer32
_NcmJapPRIntvlDISCSTx_Object = MibTableColumn
ncmJapPRIntvlDISCSTx = _NcmJapPRIntvlDISCSTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 13),
    _NcmJapPRIntvlDISCSTx_Type()
)
ncmJapPRIntvlDISCSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlDISCSTx.setStatus("mandatory")
_NcmJapPRIntvlFramerRx_Type = Integer32
_NcmJapPRIntvlFramerRx_Object = MibTableColumn
ncmJapPRIntvlFramerRx = _NcmJapPRIntvlFramerRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 14),
    _NcmJapPRIntvlFramerRx_Type()
)
ncmJapPRIntvlFramerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlFramerRx.setStatus("mandatory")
_NcmJapPRIntvlFramerTx_Type = Integer32
_NcmJapPRIntvlFramerTx_Object = MibTableColumn
ncmJapPRIntvlFramerTx = _NcmJapPRIntvlFramerTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 15),
    _NcmJapPRIntvlFramerTx_Type()
)
ncmJapPRIntvlFramerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlFramerTx.setStatus("mandatory")
_NcmJapPRIntvlLyr3ProtErr_Type = Integer32
_NcmJapPRIntvlLyr3ProtErr_Object = MibTableColumn
ncmJapPRIntvlLyr3ProtErr = _NcmJapPRIntvlLyr3ProtErr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 16),
    _NcmJapPRIntvlLyr3ProtErr_Type()
)
ncmJapPRIntvlLyr3ProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlLyr3ProtErr.setStatus("mandatory")
_NcmJapPRIntvlCallSetupSent_Type = Integer32
_NcmJapPRIntvlCallSetupSent_Object = MibTableColumn
ncmJapPRIntvlCallSetupSent = _NcmJapPRIntvlCallSetupSent_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 17),
    _NcmJapPRIntvlCallSetupSent_Type()
)
ncmJapPRIntvlCallSetupSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlCallSetupSent.setStatus("mandatory")
_NcmJapPRIntvlCallSetupSentnFail_Type = Integer32
_NcmJapPRIntvlCallSetupSentnFail_Object = MibTableColumn
ncmJapPRIntvlCallSetupSentnFail = _NcmJapPRIntvlCallSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 18),
    _NcmJapPRIntvlCallSetupSentnFail_Type()
)
ncmJapPRIntvlCallSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlCallSetupSentnFail.setStatus("mandatory")
_NcmJapPRIntvlCallSetupRx_Type = Integer32
_NcmJapPRIntvlCallSetupRx_Object = MibTableColumn
ncmJapPRIntvlCallSetupRx = _NcmJapPRIntvlCallSetupRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 19),
    _NcmJapPRIntvlCallSetupRx_Type()
)
ncmJapPRIntvlCallSetupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlCallSetupRx.setStatus("mandatory")
_NcmJapPRIntvlCallSetupRxnFail_Type = Integer32
_NcmJapPRIntvlCallSetupRxnFail_Object = MibTableColumn
ncmJapPRIntvlCallSetupRxnFail = _NcmJapPRIntvlCallSetupRxnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 20),
    _NcmJapPRIntvlCallSetupRxnFail_Type()
)
ncmJapPRIntvlCallSetupRxnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlCallSetupRxnFail.setStatus("mandatory")
_NcmJapPRIntvlUnSupportMsgRx_Type = Integer32
_NcmJapPRIntvlUnSupportMsgRx_Object = MibTableColumn
ncmJapPRIntvlUnSupportMsgRx = _NcmJapPRIntvlUnSupportMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 21),
    _NcmJapPRIntvlUnSupportMsgRx_Type()
)
ncmJapPRIntvlUnSupportMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlUnSupportMsgRx.setStatus("mandatory")
_NcmJapPRIntvlTstCalSetupSentnFail_Type = Integer32
_NcmJapPRIntvlTstCalSetupSentnFail_Object = MibTableColumn
ncmJapPRIntvlTstCalSetupSentnFail = _NcmJapPRIntvlTstCalSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 22),
    _NcmJapPRIntvlTstCalSetupSentnFail_Type()
)
ncmJapPRIntvlTstCalSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRIntvlTstCalSetupSentnFail.setStatus("mandatory")
_NcmJapPRISecurOperTable_Object = MibTable
ncmJapPRISecurOperTable = _NcmJapPRISecurOperTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005)
)
if mibBuilder.loadTexts:
    ncmJapPRISecurOperTable.setStatus("mandatory")
_NcmJapPRISecurOperEntry_Object = MibTableRow
ncmJapPRISecurOperEntry = _NcmJapPRISecurOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1)
)
ncmJapPRISecurOperEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecOpNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecOpLineIndex"),
)
if mibBuilder.loadTexts:
    ncmJapPRISecurOperEntry.setStatus("mandatory")


class _NcmJapPRISecOpNIDIndex_Type(Integer32):
    """Custom type ncmJapPRISecOpNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRISecOpNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRISecOpNIDIndex_Object = MibTableColumn
ncmJapPRISecOpNIDIndex = _NcmJapPRISecOpNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 1),
    _NcmJapPRISecOpNIDIndex_Type()
)
ncmJapPRISecOpNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecOpNIDIndex.setStatus("mandatory")


class _NcmJapPRISecOpLineIndex_Type(Integer32):
    """Custom type ncmJapPRISecOpLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRISecOpLineIndex_Type.__name__ = "Integer32"
_NcmJapPRISecOpLineIndex_Object = MibTableColumn
ncmJapPRISecOpLineIndex = _NcmJapPRISecOpLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 2),
    _NcmJapPRISecOpLineIndex_Type()
)
ncmJapPRISecOpLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecOpLineIndex.setStatus("mandatory")


class _NcmJapPRISecOpFirstNum_Type(Integer32):
    """Custom type ncmJapPRISecOpFirstNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              13,
              25,
              37,
              49)
        )
    )
    namedValues = NamedValues(
        *(("fourty-Eighth", 49),
          ("thirty-Sixth", 37),
          ("twelfth", 13),
          ("twenty-Fourth", 25),
          ("zeroth", 1))
    )


_NcmJapPRISecOpFirstNum_Type.__name__ = "Integer32"
_NcmJapPRISecOpFirstNum_Object = MibTableColumn
ncmJapPRISecOpFirstNum = _NcmJapPRISecOpFirstNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 3),
    _NcmJapPRISecOpFirstNum_Type()
)
ncmJapPRISecOpFirstNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecOpFirstNum.setStatus("mandatory")


class _NcmJapPRISecOpListype_Type(Integer32):
    """Custom type ncmJapPRISecOpListype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("own-number", 1),
          ("remote-number", 2))
    )


_NcmJapPRISecOpListype_Type.__name__ = "Integer32"
_NcmJapPRISecOpListype_Object = MibTableColumn
ncmJapPRISecOpListype = _NcmJapPRISecOpListype_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 4),
    _NcmJapPRISecOpListype_Type()
)
ncmJapPRISecOpListype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecOpListype.setStatus("mandatory")
_NcmJapPRISecOpCountNum_Type = Integer32
_NcmJapPRISecOpCountNum_Object = MibTableColumn
ncmJapPRISecOpCountNum = _NcmJapPRISecOpCountNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 5),
    _NcmJapPRISecOpCountNum_Type()
)
ncmJapPRISecOpCountNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecOpCountNum.setStatus("mandatory")
_NcmJapPRISecOpClearElement_Type = Integer32
_NcmJapPRISecOpClearElement_Object = MibTableColumn
ncmJapPRISecOpClearElement = _NcmJapPRISecOpClearElement_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 6),
    _NcmJapPRISecOpClearElement_Type()
)
ncmJapPRISecOpClearElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecOpClearElement.setStatus("mandatory")


class _NcmJapPRISecOpStatus_Type(Integer32):
    """Custom type ncmJapPRISecOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration-Error", 2),
          ("configuration-OK", 1))
    )


_NcmJapPRISecOpStatus_Type.__name__ = "Integer32"
_NcmJapPRISecOpStatus_Object = MibTableColumn
ncmJapPRISecOpStatus = _NcmJapPRISecOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 7),
    _NcmJapPRISecOpStatus_Type()
)
ncmJapPRISecOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecOpStatus.setStatus("mandatory")


class _NcmJapPRISecOpAction_Type(Integer32):
    """Custom type ncmJapPRISecOpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-Security-List", 1),
          ("set-Security-List", 2))
    )


_NcmJapPRISecOpAction_Type.__name__ = "Integer32"
_NcmJapPRISecOpAction_Object = MibTableColumn
ncmJapPRISecOpAction = _NcmJapPRISecOpAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 8),
    _NcmJapPRISecOpAction_Type()
)
ncmJapPRISecOpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecOpAction.setStatus("mandatory")
_NcmJapPRISecurNumbTable_Object = MibTable
ncmJapPRISecurNumbTable = _NcmJapPRISecurNumbTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006)
)
if mibBuilder.loadTexts:
    ncmJapPRISecurNumbTable.setStatus("mandatory")
_NcmJapPRISecurNumbEntry_Object = MibTableRow
ncmJapPRISecurNumbEntry = _NcmJapPRISecurNumbEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1)
)
ncmJapPRISecurNumbEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumIndex"),
)
if mibBuilder.loadTexts:
    ncmJapPRISecurNumbEntry.setStatus("mandatory")


class _NcmJapPRISecNumNIDIndex_Type(Integer32):
    """Custom type ncmJapPRISecNumNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRISecNumNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRISecNumNIDIndex_Object = MibTableColumn
ncmJapPRISecNumNIDIndex = _NcmJapPRISecNumNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 1),
    _NcmJapPRISecNumNIDIndex_Type()
)
ncmJapPRISecNumNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecNumNIDIndex.setStatus("mandatory")


class _NcmJapPRISecNumLineIndex_Type(Integer32):
    """Custom type ncmJapPRISecNumLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRISecNumLineIndex_Type.__name__ = "Integer32"
_NcmJapPRISecNumLineIndex_Object = MibTableColumn
ncmJapPRISecNumLineIndex = _NcmJapPRISecNumLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 2),
    _NcmJapPRISecNumLineIndex_Type()
)
ncmJapPRISecNumLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecNumLineIndex.setStatus("mandatory")
_NcmJapPRISecNumIndex_Type = Integer32
_NcmJapPRISecNumIndex_Object = MibTableColumn
ncmJapPRISecNumIndex = _NcmJapPRISecNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 3),
    _NcmJapPRISecNumIndex_Type()
)
ncmJapPRISecNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRISecNumIndex.setStatus("mandatory")
_NcmJapPRISecNumCount_Type = Integer32
_NcmJapPRISecNumCount_Object = MibTableColumn
ncmJapPRISecNumCount = _NcmJapPRISecNumCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 4),
    _NcmJapPRISecNumCount_Type()
)
ncmJapPRISecNumCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecNumCount.setStatus("mandatory")
_NcmJapPRISecNumNumber_Type = DisplayString
_NcmJapPRISecNumNumber_Object = MibTableColumn
ncmJapPRISecNumNumber = _NcmJapPRISecNumNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 5),
    _NcmJapPRISecNumNumber_Type()
)
ncmJapPRISecNumNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmJapPRISecNumNumber.setStatus("mandatory")
_NcmJapPRICallLogLineTable_Object = MibTable
ncmJapPRICallLogLineTable = _NcmJapPRICallLogLineTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007)
)
if mibBuilder.loadTexts:
    ncmJapPRICallLogLineTable.setStatus("mandatory")
_NcmJapPRICallLogLineEntry_Object = MibTableRow
ncmJapPRICallLogLineEntry = _NcmJapPRICallLogLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1)
)
ncmJapPRICallLogLineEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinLineNum"),
)
if mibBuilder.loadTexts:
    ncmJapPRICallLogLineEntry.setStatus("mandatory")


class _NcmJapPRICaloglinNIDIndex_Type(Integer32):
    """Custom type ncmJapPRICaloglinNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICaloglinNIDIndex_Type.__name__ = "Integer32"
_NcmJapPRICaloglinNIDIndex_Object = MibTableColumn
ncmJapPRICaloglinNIDIndex = _NcmJapPRICaloglinNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 1),
    _NcmJapPRICaloglinNIDIndex_Type()
)
ncmJapPRICaloglinNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICaloglinNIDIndex.setStatus("mandatory")


class _NcmJapPRICaloglinLineIndex_Type(Integer32):
    """Custom type ncmJapPRICaloglinLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmJapPRICaloglinLineIndex_Type.__name__ = "Integer32"
_NcmJapPRICaloglinLineIndex_Object = MibTableColumn
ncmJapPRICaloglinLineIndex = _NcmJapPRICaloglinLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 2),
    _NcmJapPRICaloglinLineIndex_Type()
)
ncmJapPRICaloglinLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICaloglinLineIndex.setStatus("mandatory")
_NcmJapPRICaloglinLineNum_Type = Integer32
_NcmJapPRICaloglinLineNum_Object = MibTableColumn
ncmJapPRICaloglinLineNum = _NcmJapPRICaloglinLineNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 3),
    _NcmJapPRICaloglinLineNum_Type()
)
ncmJapPRICaloglinLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICaloglinLineNum.setStatus("mandatory")
_NcmJapPRICaloglinLogLine_Type = DisplayString
_NcmJapPRICaloglinLogLine_Object = MibTableColumn
ncmJapPRICaloglinLogLine = _NcmJapPRICaloglinLogLine_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 4),
    _NcmJapPRICaloglinLogLine_Type()
)
ncmJapPRICaloglinLogLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICaloglinLogLine.setStatus("mandatory")


class _NcmJapPRICaloglinStatus_Type(Integer32):
    """Custom type ncmJapPRICaloglinStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid-CallLogLine", 2),
          ("valid-CallLogLine", 1))
    )


_NcmJapPRICaloglinStatus_Type.__name__ = "Integer32"
_NcmJapPRICaloglinStatus_Object = MibTableColumn
ncmJapPRICaloglinStatus = _NcmJapPRICaloglinStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 5),
    _NcmJapPRICaloglinStatus_Type()
)
ncmJapPRICaloglinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmJapPRICaloglinStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMJAPISDN-MIB",
    **{"ncmJapPRIPortConfigTable": ncmJapPRIPortConfigTable,
       "ncmJapPRIPortConfigEntry": ncmJapPRIPortConfigEntry,
       "ncmJapPRIPortNIDIndex": ncmJapPRIPortNIDIndex,
       "ncmJapPRIPortLineIndex": ncmJapPRIPortLineIndex,
       "ncmJapPRIPortInService": ncmJapPRIPortInService,
       "ncmJapPRIPortNFASMode": ncmJapPRIPortNFASMode,
       "ncmJapPRIPortDChanMode": ncmJapPRIPortDChanMode,
       "ncmJapPRIPortDChanBits": ncmJapPRIPortDChanBits,
       "ncmJapPRIPortTimeslotMap": ncmJapPRIPortTimeslotMap,
       "ncmJapPRIPortSwitchType": ncmJapPRIPortSwitchType,
       "ncmJapPRIPortOwnNumPlan": ncmJapPRIPortOwnNumPlan,
       "ncmJapPRIPortOwnNumType": ncmJapPRIPortOwnNumType,
       "ncmJapPRIPortSecurityLevel": ncmJapPRIPortSecurityLevel,
       "ncmJapPRIPortConfigStatus": ncmJapPRIPortConfigStatus,
       "ncmJapPRIPortSetConfig": ncmJapPRIPortSetConfig,
       "ncmJapPRICallProfCallRefCount": ncmJapPRICallProfCallRefCount,
       "ncmJapPRIL2AutoEstablish": ncmJapPRIL2AutoEstablish,
       "ncmJapPRICallProfileTable": ncmJapPRICallProfileTable,
       "ncmJapPRICallProfEntry": ncmJapPRICallProfEntry,
       "ncmJapPRICallProfNIDIndex": ncmJapPRICallProfNIDIndex,
       "ncmJapPRICallProfLineIndex": ncmJapPRICallProfLineIndex,
       "ncmJapPRICPCallProfileRef": ncmJapPRICPCallProfileRef,
       "ncmJapPRICallProfCallDir": ncmJapPRICallProfCallDir,
       "ncmJapPRICallProfNumOwnDigit": ncmJapPRICallProfNumOwnDigit,
       "ncmJapPRICallProfOwnCallNum": ncmJapPRICallProfOwnCallNum,
       "ncmJapPRICallProfExtNumPlan": ncmJapPRICallProfExtNumPlan,
       "ncmJapPRICallProfExtNumType": ncmJapPRICallProfExtNumType,
       "ncmJapPRICallProfExtNumDigit": ncmJapPRICallProfExtNumDigit,
       "ncmJapPRICallProfExtCallNum": ncmJapPRICallProfExtCallNum,
       "ncmJapPRICallProfTransferMode": ncmJapPRICallProfTransferMode,
       "ncmJapPRICallProfCallBandWth": ncmJapPRICallProfCallBandWth,
       "ncmJapPRICallProfMultiRateCnt": ncmJapPRICallProfMultiRateCnt,
       "ncmJapPRICallProfRateAdaptn": ncmJapPRICallProfRateAdaptn,
       "ncmJapPRICallProfTestCallIntvl": ncmJapPRICallProfTestCallIntvl,
       "ncmJapPRICallProfCallStatus": ncmJapPRICallProfCallStatus,
       "ncmJapPRICallProfCallAction": ncmJapPRICallProfCallAction,
       "ncmJapPRICPSetCallProf": ncmJapPRICPSetCallProf,
       "ncmJapPRICPSetCallProfResp": ncmJapPRICPSetCallProfResp,
       "ncmJapPRICPCallActionResp": ncmJapPRICPCallActionResp,
       "ncmJapPRICallProfListTable": ncmJapPRICallProfListTable,
       "ncmJapPRICallProfListEntry": ncmJapPRICallProfListEntry,
       "ncmJapPRICPListNIDIndex": ncmJapPRICPListNIDIndex,
       "ncmJapPRICPListLineIndex": ncmJapPRICPListLineIndex,
       "ncmJapPRICPListIndex": ncmJapPRICPListIndex,
       "ncmJapPRICPListValidCPRefNum": ncmJapPRICPListValidCPRefNum,
       "ncmJapPRICurrentTable": ncmJapPRICurrentTable,
       "ncmJapPRICurrentEntry": ncmJapPRICurrentEntry,
       "ncmJapPRICurrNIDIndex": ncmJapPRICurrNIDIndex,
       "ncmJapPRICurrLineIndex": ncmJapPRICurrLineIndex,
       "ncmJapPRICurrEndType": ncmJapPRICurrEndType,
       "ncmJapPRICurrTimestamp": ncmJapPRICurrTimestamp,
       "ncmJapPRICurrSecsInCurrIntvl": ncmJapPRICurrSecsInCurrIntvl,
       "ncmJapPRICurrInfoRx": ncmJapPRICurrInfoRx,
       "ncmJapPRICurrInfoTx": ncmJapPRICurrInfoTx,
       "ncmJapPRICurrCRCErrRx": ncmJapPRICurrCRCErrRx,
       "ncmJapPRICurrInvalidFrameRx": ncmJapPRICurrInvalidFrameRx,
       "ncmJapPRICurrFrameAbortRx": ncmJapPRICurrFrameAbortRx,
       "ncmJapPRICurrDISCSRx": ncmJapPRICurrDISCSRx,
       "ncmJapPRICurrDISCSTx": ncmJapPRICurrDISCSTx,
       "ncmJapPRICurrFramerRx": ncmJapPRICurrFramerRx,
       "ncmJapPRICurrFramerTx": ncmJapPRICurrFramerTx,
       "ncmJapPRICurrLyr3ProtErr": ncmJapPRICurrLyr3ProtErr,
       "ncmJapPRICurrCallSetupSent": ncmJapPRICurrCallSetupSent,
       "ncmJapPRICurrCallSetupSentnFail": ncmJapPRICurrCallSetupSentnFail,
       "ncmJapPRICurrCallSetupRx": ncmJapPRICurrCallSetupRx,
       "ncmJapPRICurrCallSetupRxnFail": ncmJapPRICurrCallSetupRxnFail,
       "ncmJapPRICurrUnSupportMsgRx": ncmJapPRICurrUnSupportMsgRx,
       "ncmJapPRICurrTstCalSetupSentnFail": ncmJapPRICurrTstCalSetupSentnFail,
       "ncmJapPRICurrValidIntvls": ncmJapPRICurrValidIntvls,
       "ncmJapPRICurrStatisticReset": ncmJapPRICurrStatisticReset,
       "ncmJapPRIIntervalTable": ncmJapPRIIntervalTable,
       "ncmJapPRIIntervalEntry": ncmJapPRIIntervalEntry,
       "ncmJapPRIntvlNIDIndex": ncmJapPRIntvlNIDIndex,
       "ncmJapPRIntvlLineIndex": ncmJapPRIntvlLineIndex,
       "ncmJapPRIntvlEndType": ncmJapPRIntvlEndType,
       "ncmJapPRIntvlIndex": ncmJapPRIntvlIndex,
       "ncmJapPRIntvlTimestamp": ncmJapPRIntvlTimestamp,
       "ncmJapPRIntvlSecsInCurrIntvl": ncmJapPRIntvlSecsInCurrIntvl,
       "ncmJapPRIntvlInfoRx": ncmJapPRIntvlInfoRx,
       "ncmJapPRIntvlInfoTx": ncmJapPRIntvlInfoTx,
       "ncmJapPRIntvlCRCErrRx": ncmJapPRIntvlCRCErrRx,
       "ncmJapPRIntvlInvalidFrameRx": ncmJapPRIntvlInvalidFrameRx,
       "ncmJapPRIntvlFrameAbortRx": ncmJapPRIntvlFrameAbortRx,
       "ncmJapPRIntvlDISCSRx": ncmJapPRIntvlDISCSRx,
       "ncmJapPRIntvlDISCSTx": ncmJapPRIntvlDISCSTx,
       "ncmJapPRIntvlFramerRx": ncmJapPRIntvlFramerRx,
       "ncmJapPRIntvlFramerTx": ncmJapPRIntvlFramerTx,
       "ncmJapPRIntvlLyr3ProtErr": ncmJapPRIntvlLyr3ProtErr,
       "ncmJapPRIntvlCallSetupSent": ncmJapPRIntvlCallSetupSent,
       "ncmJapPRIntvlCallSetupSentnFail": ncmJapPRIntvlCallSetupSentnFail,
       "ncmJapPRIntvlCallSetupRx": ncmJapPRIntvlCallSetupRx,
       "ncmJapPRIntvlCallSetupRxnFail": ncmJapPRIntvlCallSetupRxnFail,
       "ncmJapPRIntvlUnSupportMsgRx": ncmJapPRIntvlUnSupportMsgRx,
       "ncmJapPRIntvlTstCalSetupSentnFail": ncmJapPRIntvlTstCalSetupSentnFail,
       "ncmJapPRISecurOperTable": ncmJapPRISecurOperTable,
       "ncmJapPRISecurOperEntry": ncmJapPRISecurOperEntry,
       "ncmJapPRISecOpNIDIndex": ncmJapPRISecOpNIDIndex,
       "ncmJapPRISecOpLineIndex": ncmJapPRISecOpLineIndex,
       "ncmJapPRISecOpFirstNum": ncmJapPRISecOpFirstNum,
       "ncmJapPRISecOpListype": ncmJapPRISecOpListype,
       "ncmJapPRISecOpCountNum": ncmJapPRISecOpCountNum,
       "ncmJapPRISecOpClearElement": ncmJapPRISecOpClearElement,
       "ncmJapPRISecOpStatus": ncmJapPRISecOpStatus,
       "ncmJapPRISecOpAction": ncmJapPRISecOpAction,
       "ncmJapPRISecurNumbTable": ncmJapPRISecurNumbTable,
       "ncmJapPRISecurNumbEntry": ncmJapPRISecurNumbEntry,
       "ncmJapPRISecNumNIDIndex": ncmJapPRISecNumNIDIndex,
       "ncmJapPRISecNumLineIndex": ncmJapPRISecNumLineIndex,
       "ncmJapPRISecNumIndex": ncmJapPRISecNumIndex,
       "ncmJapPRISecNumCount": ncmJapPRISecNumCount,
       "ncmJapPRISecNumNumber": ncmJapPRISecNumNumber,
       "ncmJapPRICallLogLineTable": ncmJapPRICallLogLineTable,
       "ncmJapPRICallLogLineEntry": ncmJapPRICallLogLineEntry,
       "ncmJapPRICaloglinNIDIndex": ncmJapPRICaloglinNIDIndex,
       "ncmJapPRICaloglinLineIndex": ncmJapPRICaloglinLineIndex,
       "ncmJapPRICaloglinLineNum": ncmJapPRICaloglinLineNum,
       "ncmJapPRICaloglinLogLine": ncmJapPRICaloglinLogLine,
       "ncmJapPRICaloglinStatus": ncmJapPRICaloglinStatus}
)
