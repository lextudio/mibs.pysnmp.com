# SNMP MIB module (VERILINK-ENTERPRISE-NCMISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:16 2024
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

(ncm_isdn,) = mibBuilder.importSymbols(
    "VERILINK-ENTERPRISE-NCMALARM-MIB",
    "ncm-isdn")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NcmPRIPortConfigTable_Object = MibTable
ncmPRIPortConfigTable = _NcmPRIPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000)
)
if mibBuilder.loadTexts:
    ncmPRIPortConfigTable.setStatus("mandatory")
_NcmPRIPortConfigEntry_Object = MibTableRow
ncmPRIPortConfigEntry = _NcmPRIPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1)
)
ncmPRIPortConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIPortNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIPortLineIndex"),
)
if mibBuilder.loadTexts:
    ncmPRIPortConfigEntry.setStatus("mandatory")


class _NcmPRIPortNIDIndex_Type(Integer32):
    """Custom type ncmPRIPortNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRIPortNIDIndex_Type.__name__ = "Integer32"
_NcmPRIPortNIDIndex_Object = MibTableColumn
ncmPRIPortNIDIndex = _NcmPRIPortNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 1),
    _NcmPRIPortNIDIndex_Type()
)
ncmPRIPortNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIPortNIDIndex.setStatus("mandatory")


class _NcmPRIPortLineIndex_Type(Integer32):
    """Custom type ncmPRIPortLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRIPortLineIndex_Type.__name__ = "Integer32"
_NcmPRIPortLineIndex_Object = MibTableColumn
ncmPRIPortLineIndex = _NcmPRIPortLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 2),
    _NcmPRIPortLineIndex_Type()
)
ncmPRIPortLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIPortLineIndex.setStatus("mandatory")


class _NcmPRIPortInService_Type(Integer32):
    """Custom type ncmPRIPortInService based on Integer32"""
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


_NcmPRIPortInService_Type.__name__ = "Integer32"
_NcmPRIPortInService_Object = MibTableColumn
ncmPRIPortInService = _NcmPRIPortInService_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 3),
    _NcmPRIPortInService_Type()
)
ncmPRIPortInService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortInService.setStatus("mandatory")


class _NcmPRIPortNFASMode_Type(Integer32):
    """Custom type ncmPRIPortNFASMode based on Integer32"""
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
        *(("nFas", 2),
          ("nFas-on-4", 3),
          ("nFas-w-D", 4),
          ("no-nFas", 1))
    )


_NcmPRIPortNFASMode_Type.__name__ = "Integer32"
_NcmPRIPortNFASMode_Object = MibTableColumn
ncmPRIPortNFASMode = _NcmPRIPortNFASMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 4),
    _NcmPRIPortNFASMode_Type()
)
ncmPRIPortNFASMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortNFASMode.setStatus("mandatory")


class _NcmPRIPortDChanMode_Type(Integer32):
    """Custom type ncmPRIPortDChanMode based on Integer32"""
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


_NcmPRIPortDChanMode_Type.__name__ = "Integer32"
_NcmPRIPortDChanMode_Object = MibTableColumn
ncmPRIPortDChanMode = _NcmPRIPortDChanMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 5),
    _NcmPRIPortDChanMode_Type()
)
ncmPRIPortDChanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortDChanMode.setStatus("mandatory")


class _NcmPRIPortDChanBits_Type(Integer32):
    """Custom type ncmPRIPortDChanBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chan-6-Bit", 3),
          ("chan-7-Bit", 2),
          ("chan-8-Bit", 1))
    )


_NcmPRIPortDChanBits_Type.__name__ = "Integer32"
_NcmPRIPortDChanBits_Object = MibTableColumn
ncmPRIPortDChanBits = _NcmPRIPortDChanBits_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 6),
    _NcmPRIPortDChanBits_Type()
)
ncmPRIPortDChanBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortDChanBits.setStatus("mandatory")
_NcmPRIPortTimeslotMap_Type = DisplayString
_NcmPRIPortTimeslotMap_Object = MibTableColumn
ncmPRIPortTimeslotMap = _NcmPRIPortTimeslotMap_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 7),
    _NcmPRIPortTimeslotMap_Type()
)
ncmPRIPortTimeslotMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortTimeslotMap.setStatus("mandatory")


class _NcmPRIPortSwitchType_Type(Integer32):
    """Custom type ncmPRIPortSwitchType based on Integer32"""
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
        *(("sw-Att-4Ess", 2),
          ("sw-Att-5Ess", 3),
          ("sw-Att-Reserved", 4),
          ("sw-Ni-2", 6),
          ("sw-Nti-Dms100", 5),
          ("sw-Unspecified", 1))
    )


_NcmPRIPortSwitchType_Type.__name__ = "Integer32"
_NcmPRIPortSwitchType_Object = MibTableColumn
ncmPRIPortSwitchType = _NcmPRIPortSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 8),
    _NcmPRIPortSwitchType_Type()
)
ncmPRIPortSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortSwitchType.setStatus("mandatory")


class _NcmPRIPortOwnNumPlan_Type(Integer32):
    """Custom type ncmPRIPortOwnNumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isdn-E164", 2),
          ("private", 10),
          ("telephony-E163", 3),
          ("unkn-NumPlan", 1))
    )


_NcmPRIPortOwnNumPlan_Type.__name__ = "Integer32"
_NcmPRIPortOwnNumPlan_Object = MibTableColumn
ncmPRIPortOwnNumPlan = _NcmPRIPortOwnNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 9),
    _NcmPRIPortOwnNumPlan_Type()
)
ncmPRIPortOwnNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortOwnNumPlan.setStatus("mandatory")


class _NcmPRIPortOwnNumType_Type(Integer32):
    """Custom type ncmPRIPortOwnNumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("local", 5),
          ("national", 3),
          ("unkn-NumType", 1))
    )


_NcmPRIPortOwnNumType_Type.__name__ = "Integer32"
_NcmPRIPortOwnNumType_Object = MibTableColumn
ncmPRIPortOwnNumType = _NcmPRIPortOwnNumType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 10),
    _NcmPRIPortOwnNumType_Type()
)
ncmPRIPortOwnNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortOwnNumType.setStatus("mandatory")


class _NcmPRIPortSecurityLevel_Type(Integer32):
    """Custom type ncmPRIPortSecurityLevel based on Integer32"""
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


_NcmPRIPortSecurityLevel_Type.__name__ = "Integer32"
_NcmPRIPortSecurityLevel_Object = MibTableColumn
ncmPRIPortSecurityLevel = _NcmPRIPortSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 11),
    _NcmPRIPortSecurityLevel_Type()
)
ncmPRIPortSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortSecurityLevel.setStatus("mandatory")


class _NcmPRIPortConfigStatus_Type(Integer32):
    """Custom type ncmPRIPortConfigStatus based on Integer32"""
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


_NcmPRIPortConfigStatus_Type.__name__ = "Integer32"
_NcmPRIPortConfigStatus_Object = MibTableColumn
ncmPRIPortConfigStatus = _NcmPRIPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 12),
    _NcmPRIPortConfigStatus_Type()
)
ncmPRIPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIPortConfigStatus.setStatus("mandatory")


class _NcmPRIPortSetConfig_Type(Integer32):
    """Custom type ncmPRIPortSetConfig based on Integer32"""
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


_NcmPRIPortSetConfig_Type.__name__ = "Integer32"
_NcmPRIPortSetConfig_Object = MibTableColumn
ncmPRIPortSetConfig = _NcmPRIPortSetConfig_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 13),
    _NcmPRIPortSetConfig_Type()
)
ncmPRIPortSetConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIPortSetConfig.setStatus("mandatory")
_NcmPRICallProfCallRefCount_Type = Integer32
_NcmPRICallProfCallRefCount_Object = MibTableColumn
ncmPRICallProfCallRefCount = _NcmPRICallProfCallRefCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 14),
    _NcmPRICallProfCallRefCount_Type()
)
ncmPRICallProfCallRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICallProfCallRefCount.setStatus("mandatory")


class _NcmPRIL2AutoEstablish_Type(Integer32):
    """Custom type ncmPRIL2AutoEstablish based on Integer32"""
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


_NcmPRIL2AutoEstablish_Type.__name__ = "Integer32"
_NcmPRIL2AutoEstablish_Object = MibTableColumn
ncmPRIL2AutoEstablish = _NcmPRIL2AutoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 15),
    _NcmPRIL2AutoEstablish_Type()
)
ncmPRIL2AutoEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIL2AutoEstablish.setStatus("mandatory")


class _NcmPRIResetCard_Type(Integer32):
    """Custom type ncmPRIResetCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-in-use", 2),
          ("reset-Card", 1))
    )


_NcmPRIResetCard_Type.__name__ = "Integer32"
_NcmPRIResetCard_Object = MibTableColumn
ncmPRIResetCard = _NcmPRIResetCard_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8000, 1, 16),
    _NcmPRIResetCard_Type()
)
ncmPRIResetCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRIResetCard.setStatus("mandatory")
_NcmPRICallProfileTable_Object = MibTable
ncmPRICallProfileTable = _NcmPRICallProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001)
)
if mibBuilder.loadTexts:
    ncmPRICallProfileTable.setStatus("mandatory")
_NcmPRICallProfEntry_Object = MibTableRow
ncmPRICallProfEntry = _NcmPRICallProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1)
)
ncmPRICallProfEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICallProfNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICallProfLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICPCallProfileRef"),
)
if mibBuilder.loadTexts:
    ncmPRICallProfEntry.setStatus("mandatory")


class _NcmPRICallProfNIDIndex_Type(Integer32):
    """Custom type ncmPRICallProfNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICallProfNIDIndex_Type.__name__ = "Integer32"
_NcmPRICallProfNIDIndex_Object = MibTableColumn
ncmPRICallProfNIDIndex = _NcmPRICallProfNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 1),
    _NcmPRICallProfNIDIndex_Type()
)
ncmPRICallProfNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICallProfNIDIndex.setStatus("mandatory")


class _NcmPRICallProfLineIndex_Type(Integer32):
    """Custom type ncmPRICallProfLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICallProfLineIndex_Type.__name__ = "Integer32"
_NcmPRICallProfLineIndex_Object = MibTableColumn
ncmPRICallProfLineIndex = _NcmPRICallProfLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 2),
    _NcmPRICallProfLineIndex_Type()
)
ncmPRICallProfLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICallProfLineIndex.setStatus("mandatory")
_NcmPRICPCallProfileRef_Type = Integer32
_NcmPRICPCallProfileRef_Object = MibTableColumn
ncmPRICPCallProfileRef = _NcmPRICPCallProfileRef_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 3),
    _NcmPRICPCallProfileRef_Type()
)
ncmPRICPCallProfileRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICPCallProfileRef.setStatus("mandatory")


class _NcmPRICallProfCallDir_Type(Integer32):
    """Custom type ncmPRICallProfCallDir based on Integer32"""
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


_NcmPRICallProfCallDir_Type.__name__ = "Integer32"
_NcmPRICallProfCallDir_Object = MibTableColumn
ncmPRICallProfCallDir = _NcmPRICallProfCallDir_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 4),
    _NcmPRICallProfCallDir_Type()
)
ncmPRICallProfCallDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfCallDir.setStatus("mandatory")
_NcmPRICallProfNumOwnDigit_Type = Integer32
_NcmPRICallProfNumOwnDigit_Object = MibTableColumn
ncmPRICallProfNumOwnDigit = _NcmPRICallProfNumOwnDigit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 5),
    _NcmPRICallProfNumOwnDigit_Type()
)
ncmPRICallProfNumOwnDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfNumOwnDigit.setStatus("mandatory")
_NcmPRICallProfOwnCallNum_Type = DisplayString
_NcmPRICallProfOwnCallNum_Object = MibTableColumn
ncmPRICallProfOwnCallNum = _NcmPRICallProfOwnCallNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 6),
    _NcmPRICallProfOwnCallNum_Type()
)
ncmPRICallProfOwnCallNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfOwnCallNum.setStatus("mandatory")


class _NcmPRICallProfExtNumPlan_Type(Integer32):
    """Custom type ncmPRICallProfExtNumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("isdn-E164", 2),
          ("private", 10),
          ("telephony-E163", 3),
          ("unkn-NumPlan", 1))
    )


_NcmPRICallProfExtNumPlan_Type.__name__ = "Integer32"
_NcmPRICallProfExtNumPlan_Object = MibTableColumn
ncmPRICallProfExtNumPlan = _NcmPRICallProfExtNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 7),
    _NcmPRICallProfExtNumPlan_Type()
)
ncmPRICallProfExtNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfExtNumPlan.setStatus("mandatory")


class _NcmPRICallProfExtNumType_Type(Integer32):
    """Custom type ncmPRICallProfExtNumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("local", 5),
          ("national", 3),
          ("unkn-NumType", 1))
    )


_NcmPRICallProfExtNumType_Type.__name__ = "Integer32"
_NcmPRICallProfExtNumType_Object = MibTableColumn
ncmPRICallProfExtNumType = _NcmPRICallProfExtNumType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 8),
    _NcmPRICallProfExtNumType_Type()
)
ncmPRICallProfExtNumType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfExtNumType.setStatus("mandatory")
_NcmPRICallProfExtNumDigit_Type = Integer32
_NcmPRICallProfExtNumDigit_Object = MibTableColumn
ncmPRICallProfExtNumDigit = _NcmPRICallProfExtNumDigit_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 9),
    _NcmPRICallProfExtNumDigit_Type()
)
ncmPRICallProfExtNumDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfExtNumDigit.setStatus("mandatory")
_NcmPRICallProfExtCallNum_Type = DisplayString
_NcmPRICallProfExtCallNum_Object = MibTableColumn
ncmPRICallProfExtCallNum = _NcmPRICallProfExtCallNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 10),
    _NcmPRICallProfExtCallNum_Type()
)
ncmPRICallProfExtCallNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfExtCallNum.setStatus("mandatory")


class _NcmPRICallProfTransferMode_Type(Integer32):
    """Custom type ncmPRICallProfTransferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("restricted-digital", 9),
          ("unrestricted-digital", 8))
    )


_NcmPRICallProfTransferMode_Type.__name__ = "Integer32"
_NcmPRICallProfTransferMode_Object = MibTableColumn
ncmPRICallProfTransferMode = _NcmPRICallProfTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 11),
    _NcmPRICallProfTransferMode_Type()
)
ncmPRICallProfTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfTransferMode.setStatus("mandatory")


class _NcmPRICallProfCallBandWth_Type(Integer32):
    """Custom type ncmPRICallProfCallBandWth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              19,
              21,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("b1-64K", 16),
          ("h0-6X64K", 19),
          ("h11-24X64K", 21),
          ("h12-30X64K", 23),
          ("multiRate", 24))
    )


_NcmPRICallProfCallBandWth_Type.__name__ = "Integer32"
_NcmPRICallProfCallBandWth_Object = MibTableColumn
ncmPRICallProfCallBandWth = _NcmPRICallProfCallBandWth_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 12),
    _NcmPRICallProfCallBandWth_Type()
)
ncmPRICallProfCallBandWth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfCallBandWth.setStatus("mandatory")


class _NcmPRICallProfMultiRateCnt_Type(Integer32):
    """Custom type ncmPRICallProfMultiRateCnt based on Integer32"""
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


_NcmPRICallProfMultiRateCnt_Type.__name__ = "Integer32"
_NcmPRICallProfMultiRateCnt_Object = MibTableColumn
ncmPRICallProfMultiRateCnt = _NcmPRICallProfMultiRateCnt_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 13),
    _NcmPRICallProfMultiRateCnt_Type()
)
ncmPRICallProfMultiRateCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfMultiRateCnt.setStatus("mandatory")


class _NcmPRICallProfRateAdaptn_Type(Integer32):
    """Custom type ncmPRICallProfRateAdaptn based on Integer32"""
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


_NcmPRICallProfRateAdaptn_Type.__name__ = "Integer32"
_NcmPRICallProfRateAdaptn_Object = MibTableColumn
ncmPRICallProfRateAdaptn = _NcmPRICallProfRateAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 14),
    _NcmPRICallProfRateAdaptn_Type()
)
ncmPRICallProfRateAdaptn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfRateAdaptn.setStatus("mandatory")
_NcmPRICallProfTestCallIntvl_Type = Integer32
_NcmPRICallProfTestCallIntvl_Object = MibTableColumn
ncmPRICallProfTestCallIntvl = _NcmPRICallProfTestCallIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 15),
    _NcmPRICallProfTestCallIntvl_Type()
)
ncmPRICallProfTestCallIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfTestCallIntvl.setStatus("mandatory")


class _NcmPRICallProfCallStatus_Type(Integer32):
    """Custom type ncmPRICallProfCallStatus based on Integer32"""
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


_NcmPRICallProfCallStatus_Type.__name__ = "Integer32"
_NcmPRICallProfCallStatus_Object = MibTableColumn
ncmPRICallProfCallStatus = _NcmPRICallProfCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 16),
    _NcmPRICallProfCallStatus_Type()
)
ncmPRICallProfCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICallProfCallStatus.setStatus("mandatory")


class _NcmPRICallProfCallAction_Type(Integer32):
    """Custom type ncmPRICallProfCallAction based on Integer32"""
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


_NcmPRICallProfCallAction_Type.__name__ = "Integer32"
_NcmPRICallProfCallAction_Object = MibTableColumn
ncmPRICallProfCallAction = _NcmPRICallProfCallAction_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 17),
    _NcmPRICallProfCallAction_Type()
)
ncmPRICallProfCallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICallProfCallAction.setStatus("mandatory")


class _NcmPRICPSetCallProf_Type(Integer32):
    """Custom type ncmPRICPSetCallProf based on Integer32"""
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


_NcmPRICPSetCallProf_Type.__name__ = "Integer32"
_NcmPRICPSetCallProf_Object = MibTableColumn
ncmPRICPSetCallProf = _NcmPRICPSetCallProf_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 18),
    _NcmPRICPSetCallProf_Type()
)
ncmPRICPSetCallProf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICPSetCallProf.setStatus("mandatory")


class _NcmPRICPSetCallProfResp_Type(Integer32):
    """Custom type ncmPRICPSetCallProfResp based on Integer32"""
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


_NcmPRICPSetCallProfResp_Type.__name__ = "Integer32"
_NcmPRICPSetCallProfResp_Object = MibTableColumn
ncmPRICPSetCallProfResp = _NcmPRICPSetCallProfResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 19),
    _NcmPRICPSetCallProfResp_Type()
)
ncmPRICPSetCallProfResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPSetCallProfResp.setStatus("mandatory")


class _NcmPRICPCallActionResp_Type(Integer32):
    """Custom type ncmPRICPCallActionResp based on Integer32"""
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


_NcmPRICPCallActionResp_Type.__name__ = "Integer32"
_NcmPRICPCallActionResp_Object = MibTableColumn
ncmPRICPCallActionResp = _NcmPRICPCallActionResp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8001, 1, 20),
    _NcmPRICPCallActionResp_Type()
)
ncmPRICPCallActionResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPCallActionResp.setStatus("mandatory")
_NcmPRICallProfListTable_Object = MibTable
ncmPRICallProfListTable = _NcmPRICallProfListTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002)
)
if mibBuilder.loadTexts:
    ncmPRICallProfListTable.setStatus("mandatory")
_NcmPRICallProfListEntry_Object = MibTableRow
ncmPRICallProfListEntry = _NcmPRICallProfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002, 1)
)
ncmPRICallProfListEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICPListNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICPListLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICPListIndex"),
)
if mibBuilder.loadTexts:
    ncmPRICallProfListEntry.setStatus("mandatory")


class _NcmPRICPListNIDIndex_Type(Integer32):
    """Custom type ncmPRICPListNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICPListNIDIndex_Type.__name__ = "Integer32"
_NcmPRICPListNIDIndex_Object = MibTableColumn
ncmPRICPListNIDIndex = _NcmPRICPListNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002, 1, 1),
    _NcmPRICPListNIDIndex_Type()
)
ncmPRICPListNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPListNIDIndex.setStatus("mandatory")


class _NcmPRICPListLineIndex_Type(Integer32):
    """Custom type ncmPRICPListLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICPListLineIndex_Type.__name__ = "Integer32"
_NcmPRICPListLineIndex_Object = MibTableColumn
ncmPRICPListLineIndex = _NcmPRICPListLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002, 1, 2),
    _NcmPRICPListLineIndex_Type()
)
ncmPRICPListLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPListLineIndex.setStatus("mandatory")
_NcmPRICPListIndex_Type = Integer32
_NcmPRICPListIndex_Object = MibTableColumn
ncmPRICPListIndex = _NcmPRICPListIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002, 1, 3),
    _NcmPRICPListIndex_Type()
)
ncmPRICPListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPListIndex.setStatus("mandatory")
_NcmPRICPListValidCPRefNum_Type = Integer32
_NcmPRICPListValidCPRefNum_Object = MibTableColumn
ncmPRICPListValidCPRefNum = _NcmPRICPListValidCPRefNum_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8002, 1, 4),
    _NcmPRICPListValidCPRefNum_Type()
)
ncmPRICPListValidCPRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICPListValidCPRefNum.setStatus("mandatory")
_NcmPRICurrentTable_Object = MibTable
ncmPRICurrentTable = _NcmPRICurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003)
)
if mibBuilder.loadTexts:
    ncmPRICurrentTable.setStatus("mandatory")
_NcmPRICurrentEntry_Object = MibTableRow
ncmPRICurrentEntry = _NcmPRICurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1)
)
ncmPRICurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICurrNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICurrLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRICurrEndType"),
)
if mibBuilder.loadTexts:
    ncmPRICurrentEntry.setStatus("mandatory")


class _NcmPRICurrNIDIndex_Type(Integer32):
    """Custom type ncmPRICurrNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICurrNIDIndex_Type.__name__ = "Integer32"
_NcmPRICurrNIDIndex_Object = MibTableColumn
ncmPRICurrNIDIndex = _NcmPRICurrNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 1),
    _NcmPRICurrNIDIndex_Type()
)
ncmPRICurrNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrNIDIndex.setStatus("mandatory")


class _NcmPRICurrLineIndex_Type(Integer32):
    """Custom type ncmPRICurrLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRICurrLineIndex_Type.__name__ = "Integer32"
_NcmPRICurrLineIndex_Object = MibTableColumn
ncmPRICurrLineIndex = _NcmPRICurrLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 2),
    _NcmPRICurrLineIndex_Type()
)
ncmPRICurrLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrLineIndex.setStatus("mandatory")


class _NcmPRICurrEndType_Type(Integer32):
    """Custom type ncmPRICurrEndType based on Integer32"""
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


_NcmPRICurrEndType_Type.__name__ = "Integer32"
_NcmPRICurrEndType_Object = MibTableColumn
ncmPRICurrEndType = _NcmPRICurrEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 3),
    _NcmPRICurrEndType_Type()
)
ncmPRICurrEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrEndType.setStatus("mandatory")
_NcmPRICurrTimestamp_Type = Integer32
_NcmPRICurrTimestamp_Object = MibTableColumn
ncmPRICurrTimestamp = _NcmPRICurrTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 4),
    _NcmPRICurrTimestamp_Type()
)
ncmPRICurrTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrTimestamp.setStatus("mandatory")
_NcmPRICurrSecsInCurrIntvl_Type = Integer32
_NcmPRICurrSecsInCurrIntvl_Object = MibTableColumn
ncmPRICurrSecsInCurrIntvl = _NcmPRICurrSecsInCurrIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 5),
    _NcmPRICurrSecsInCurrIntvl_Type()
)
ncmPRICurrSecsInCurrIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrSecsInCurrIntvl.setStatus("mandatory")
_NcmPRICurrInfoRx_Type = Integer32
_NcmPRICurrInfoRx_Object = MibTableColumn
ncmPRICurrInfoRx = _NcmPRICurrInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 6),
    _NcmPRICurrInfoRx_Type()
)
ncmPRICurrInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrInfoRx.setStatus("mandatory")
_NcmPRICurrInfoTx_Type = Integer32
_NcmPRICurrInfoTx_Object = MibTableColumn
ncmPRICurrInfoTx = _NcmPRICurrInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 7),
    _NcmPRICurrInfoTx_Type()
)
ncmPRICurrInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrInfoTx.setStatus("mandatory")
_NcmPRICurrCRCErrRx_Type = Integer32
_NcmPRICurrCRCErrRx_Object = MibTableColumn
ncmPRICurrCRCErrRx = _NcmPRICurrCRCErrRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 8),
    _NcmPRICurrCRCErrRx_Type()
)
ncmPRICurrCRCErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrCRCErrRx.setStatus("mandatory")
_NcmPRICurrInvalidFrameRx_Type = Integer32
_NcmPRICurrInvalidFrameRx_Object = MibTableColumn
ncmPRICurrInvalidFrameRx = _NcmPRICurrInvalidFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 9),
    _NcmPRICurrInvalidFrameRx_Type()
)
ncmPRICurrInvalidFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrInvalidFrameRx.setStatus("mandatory")
_NcmPRICurrFrameAbortRx_Type = Integer32
_NcmPRICurrFrameAbortRx_Object = MibTableColumn
ncmPRICurrFrameAbortRx = _NcmPRICurrFrameAbortRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 10),
    _NcmPRICurrFrameAbortRx_Type()
)
ncmPRICurrFrameAbortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrFrameAbortRx.setStatus("mandatory")
_NcmPRICurrDISCSRx_Type = Integer32
_NcmPRICurrDISCSRx_Object = MibTableColumn
ncmPRICurrDISCSRx = _NcmPRICurrDISCSRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 11),
    _NcmPRICurrDISCSRx_Type()
)
ncmPRICurrDISCSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrDISCSRx.setStatus("mandatory")
_NcmPRICurrDISCSTx_Type = Integer32
_NcmPRICurrDISCSTx_Object = MibTableColumn
ncmPRICurrDISCSTx = _NcmPRICurrDISCSTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 12),
    _NcmPRICurrDISCSTx_Type()
)
ncmPRICurrDISCSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrDISCSTx.setStatus("mandatory")
_NcmPRICurrFramerRx_Type = Integer32
_NcmPRICurrFramerRx_Object = MibTableColumn
ncmPRICurrFramerRx = _NcmPRICurrFramerRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 13),
    _NcmPRICurrFramerRx_Type()
)
ncmPRICurrFramerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrFramerRx.setStatus("mandatory")
_NcmPRICurrFramerTx_Type = Integer32
_NcmPRICurrFramerTx_Object = MibTableColumn
ncmPRICurrFramerTx = _NcmPRICurrFramerTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 14),
    _NcmPRICurrFramerTx_Type()
)
ncmPRICurrFramerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrFramerTx.setStatus("mandatory")
_NcmPRICurrLyr3ProtErr_Type = Integer32
_NcmPRICurrLyr3ProtErr_Object = MibTableColumn
ncmPRICurrLyr3ProtErr = _NcmPRICurrLyr3ProtErr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 15),
    _NcmPRICurrLyr3ProtErr_Type()
)
ncmPRICurrLyr3ProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrLyr3ProtErr.setStatus("mandatory")
_NcmPRICurrCallSetupSent_Type = Integer32
_NcmPRICurrCallSetupSent_Object = MibTableColumn
ncmPRICurrCallSetupSent = _NcmPRICurrCallSetupSent_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 16),
    _NcmPRICurrCallSetupSent_Type()
)
ncmPRICurrCallSetupSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrCallSetupSent.setStatus("mandatory")
_NcmPRICurrCallSetupSentnFail_Type = Integer32
_NcmPRICurrCallSetupSentnFail_Object = MibTableColumn
ncmPRICurrCallSetupSentnFail = _NcmPRICurrCallSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 17),
    _NcmPRICurrCallSetupSentnFail_Type()
)
ncmPRICurrCallSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrCallSetupSentnFail.setStatus("mandatory")
_NcmPRICurrCallSetupRx_Type = Integer32
_NcmPRICurrCallSetupRx_Object = MibTableColumn
ncmPRICurrCallSetupRx = _NcmPRICurrCallSetupRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 18),
    _NcmPRICurrCallSetupRx_Type()
)
ncmPRICurrCallSetupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrCallSetupRx.setStatus("mandatory")
_NcmPRICurrCallSetupRxnFail_Type = Integer32
_NcmPRICurrCallSetupRxnFail_Object = MibTableColumn
ncmPRICurrCallSetupRxnFail = _NcmPRICurrCallSetupRxnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 19),
    _NcmPRICurrCallSetupRxnFail_Type()
)
ncmPRICurrCallSetupRxnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrCallSetupRxnFail.setStatus("mandatory")
_NcmPRICurrUnSupportMsgRx_Type = Integer32
_NcmPRICurrUnSupportMsgRx_Object = MibTableColumn
ncmPRICurrUnSupportMsgRx = _NcmPRICurrUnSupportMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 20),
    _NcmPRICurrUnSupportMsgRx_Type()
)
ncmPRICurrUnSupportMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrUnSupportMsgRx.setStatus("mandatory")
_NcmPRICurrTstCalSetupSentnFail_Type = Integer32
_NcmPRICurrTstCalSetupSentnFail_Object = MibTableColumn
ncmPRICurrTstCalSetupSentnFail = _NcmPRICurrTstCalSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 21),
    _NcmPRICurrTstCalSetupSentnFail_Type()
)
ncmPRICurrTstCalSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrTstCalSetupSentnFail.setStatus("mandatory")
_NcmPRICurrValidIntvls_Type = Integer32
_NcmPRICurrValidIntvls_Object = MibTableColumn
ncmPRICurrValidIntvls = _NcmPRICurrValidIntvls_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 22),
    _NcmPRICurrValidIntvls_Type()
)
ncmPRICurrValidIntvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRICurrValidIntvls.setStatus("mandatory")


class _NcmPRICurrStatisticReset_Type(Integer32):
    """Custom type ncmPRICurrStatisticReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("statistic-Reset", 1)
    )


_NcmPRICurrStatisticReset_Type.__name__ = "Integer32"
_NcmPRICurrStatisticReset_Object = MibTableColumn
ncmPRICurrStatisticReset = _NcmPRICurrStatisticReset_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8003, 1, 23),
    _NcmPRICurrStatisticReset_Type()
)
ncmPRICurrStatisticReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmPRICurrStatisticReset.setStatus("mandatory")
_NcmPRIIntervalTable_Object = MibTable
ncmPRIIntervalTable = _NcmPRIIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004)
)
if mibBuilder.loadTexts:
    ncmPRIIntervalTable.setStatus("mandatory")
_NcmPRIIntervalEntry_Object = MibTableRow
ncmPRIIntervalEntry = _NcmPRIIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1)
)
ncmPRIIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIntvlNIDIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIntvlLineIndex"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIntvlEndType"),
    (0, "VERILINK-ENTERPRISE-NCMISDN-MIB", "ncmPRIntvlIndex"),
)
if mibBuilder.loadTexts:
    ncmPRIIntervalEntry.setStatus("mandatory")


class _NcmPRIntvlNIDIndex_Type(Integer32):
    """Custom type ncmPRIntvlNIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRIntvlNIDIndex_Type.__name__ = "Integer32"
_NcmPRIntvlNIDIndex_Object = MibTableColumn
ncmPRIntvlNIDIndex = _NcmPRIntvlNIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 1),
    _NcmPRIntvlNIDIndex_Type()
)
ncmPRIntvlNIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlNIDIndex.setStatus("mandatory")


class _NcmPRIntvlLineIndex_Type(Integer32):
    """Custom type ncmPRIntvlLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmPRIntvlLineIndex_Type.__name__ = "Integer32"
_NcmPRIntvlLineIndex_Object = MibTableColumn
ncmPRIntvlLineIndex = _NcmPRIntvlLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 2),
    _NcmPRIntvlLineIndex_Type()
)
ncmPRIntvlLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlLineIndex.setStatus("mandatory")


class _NcmPRIntvlEndType_Type(Integer32):
    """Custom type ncmPRIntvlEndType based on Integer32"""
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


_NcmPRIntvlEndType_Type.__name__ = "Integer32"
_NcmPRIntvlEndType_Object = MibTableColumn
ncmPRIntvlEndType = _NcmPRIntvlEndType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 3),
    _NcmPRIntvlEndType_Type()
)
ncmPRIntvlEndType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlEndType.setStatus("mandatory")
_NcmPRIntvlIndex_Type = Integer32
_NcmPRIntvlIndex_Object = MibTableColumn
ncmPRIntvlIndex = _NcmPRIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 4),
    _NcmPRIntvlIndex_Type()
)
ncmPRIntvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlIndex.setStatus("mandatory")
_NcmPRIntvlTimestamp_Type = Integer32
_NcmPRIntvlTimestamp_Object = MibTableColumn
ncmPRIntvlTimestamp = _NcmPRIntvlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 5),
    _NcmPRIntvlTimestamp_Type()
)
ncmPRIntvlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlTimestamp.setStatus("mandatory")
_NcmPRIntvlSecsInCurrIntvl_Type = Integer32
_NcmPRIntvlSecsInCurrIntvl_Object = MibTableColumn
ncmPRIntvlSecsInCurrIntvl = _NcmPRIntvlSecsInCurrIntvl_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 6),
    _NcmPRIntvlSecsInCurrIntvl_Type()
)
ncmPRIntvlSecsInCurrIntvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlSecsInCurrIntvl.setStatus("mandatory")
_NcmPRIntvlInfoRx_Type = Integer32
_NcmPRIntvlInfoRx_Object = MibTableColumn
ncmPRIntvlInfoRx = _NcmPRIntvlInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 7),
    _NcmPRIntvlInfoRx_Type()
)
ncmPRIntvlInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlInfoRx.setStatus("mandatory")
_NcmPRIntvlInfoTx_Type = Integer32
_NcmPRIntvlInfoTx_Object = MibTableColumn
ncmPRIntvlInfoTx = _NcmPRIntvlInfoTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 8),
    _NcmPRIntvlInfoTx_Type()
)
ncmPRIntvlInfoTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlInfoTx.setStatus("mandatory")
_NcmPRIntvlCRCErrRx_Type = Integer32
_NcmPRIntvlCRCErrRx_Object = MibTableColumn
ncmPRIntvlCRCErrRx = _NcmPRIntvlCRCErrRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 9),
    _NcmPRIntvlCRCErrRx_Type()
)
ncmPRIntvlCRCErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlCRCErrRx.setStatus("mandatory")
_NcmPRIntvlInvalidFrameRx_Type = Integer32
_NcmPRIntvlInvalidFrameRx_Object = MibTableColumn
ncmPRIntvlInvalidFrameRx = _NcmPRIntvlInvalidFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 10),
    _NcmPRIntvlInvalidFrameRx_Type()
)
ncmPRIntvlInvalidFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlInvalidFrameRx.setStatus("mandatory")
_NcmPRIntvlFrameAbortRx_Type = Integer32
_NcmPRIntvlFrameAbortRx_Object = MibTableColumn
ncmPRIntvlFrameAbortRx = _NcmPRIntvlFrameAbortRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 11),
    _NcmPRIntvlFrameAbortRx_Type()
)
ncmPRIntvlFrameAbortRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlFrameAbortRx.setStatus("mandatory")
_NcmPRIntvlDISCSRx_Type = Integer32
_NcmPRIntvlDISCSRx_Object = MibTableColumn
ncmPRIntvlDISCSRx = _NcmPRIntvlDISCSRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 12),
    _NcmPRIntvlDISCSRx_Type()
)
ncmPRIntvlDISCSRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlDISCSRx.setStatus("mandatory")
_NcmPRIntvlDISCSTx_Type = Integer32
_NcmPRIntvlDISCSTx_Object = MibTableColumn
ncmPRIntvlDISCSTx = _NcmPRIntvlDISCSTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 13),
    _NcmPRIntvlDISCSTx_Type()
)
ncmPRIntvlDISCSTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlDISCSTx.setStatus("mandatory")
_NcmPRIntvlFramerRx_Type = Integer32
_NcmPRIntvlFramerRx_Object = MibTableColumn
ncmPRIntvlFramerRx = _NcmPRIntvlFramerRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 14),
    _NcmPRIntvlFramerRx_Type()
)
ncmPRIntvlFramerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlFramerRx.setStatus("mandatory")
_NcmPRIntvlFramerTx_Type = Integer32
_NcmPRIntvlFramerTx_Object = MibTableColumn
ncmPRIntvlFramerTx = _NcmPRIntvlFramerTx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 15),
    _NcmPRIntvlFramerTx_Type()
)
ncmPRIntvlFramerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlFramerTx.setStatus("mandatory")
_NcmPRIntvlLyr3ProtErr_Type = Integer32
_NcmPRIntvlLyr3ProtErr_Object = MibTableColumn
ncmPRIntvlLyr3ProtErr = _NcmPRIntvlLyr3ProtErr_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 16),
    _NcmPRIntvlLyr3ProtErr_Type()
)
ncmPRIntvlLyr3ProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlLyr3ProtErr.setStatus("mandatory")
_NcmPRIntvlCallSetupSent_Type = Integer32
_NcmPRIntvlCallSetupSent_Object = MibTableColumn
ncmPRIntvlCallSetupSent = _NcmPRIntvlCallSetupSent_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 17),
    _NcmPRIntvlCallSetupSent_Type()
)
ncmPRIntvlCallSetupSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlCallSetupSent.setStatus("mandatory")
_NcmPRIntvlCallSetupSentnFail_Type = Integer32
_NcmPRIntvlCallSetupSentnFail_Object = MibTableColumn
ncmPRIntvlCallSetupSentnFail = _NcmPRIntvlCallSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 18),
    _NcmPRIntvlCallSetupSentnFail_Type()
)
ncmPRIntvlCallSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlCallSetupSentnFail.setStatus("mandatory")
_NcmPRIntvlCallSetupRx_Type = Integer32
_NcmPRIntvlCallSetupRx_Object = MibTableColumn
ncmPRIntvlCallSetupRx = _NcmPRIntvlCallSetupRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 19),
    _NcmPRIntvlCallSetupRx_Type()
)
ncmPRIntvlCallSetupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlCallSetupRx.setStatus("mandatory")
_NcmPRIntvlCallSetupRxnFail_Type = Integer32
_NcmPRIntvlCallSetupRxnFail_Object = MibTableColumn
ncmPRIntvlCallSetupRxnFail = _NcmPRIntvlCallSetupRxnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 20),
    _NcmPRIntvlCallSetupRxnFail_Type()
)
ncmPRIntvlCallSetupRxnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlCallSetupRxnFail.setStatus("mandatory")
_NcmPRIntvlUnSupportMsgRx_Type = Integer32
_NcmPRIntvlUnSupportMsgRx_Object = MibTableColumn
ncmPRIntvlUnSupportMsgRx = _NcmPRIntvlUnSupportMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 21),
    _NcmPRIntvlUnSupportMsgRx_Type()
)
ncmPRIntvlUnSupportMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlUnSupportMsgRx.setStatus("mandatory")
_NcmPRIntvlTstCalSetupSentnFail_Type = Integer32
_NcmPRIntvlTstCalSetupSentnFail_Object = MibTableColumn
ncmPRIntvlTstCalSetupSentnFail = _NcmPRIntvlTstCalSetupSentnFail_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3031, 8004, 1, 22),
    _NcmPRIntvlTstCalSetupSentnFail_Type()
)
ncmPRIntvlTstCalSetupSentnFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmPRIntvlTstCalSetupSentnFail.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMISDN-MIB",
    **{"ncmPRIPortConfigTable": ncmPRIPortConfigTable,
       "ncmPRIPortConfigEntry": ncmPRIPortConfigEntry,
       "ncmPRIPortNIDIndex": ncmPRIPortNIDIndex,
       "ncmPRIPortLineIndex": ncmPRIPortLineIndex,
       "ncmPRIPortInService": ncmPRIPortInService,
       "ncmPRIPortNFASMode": ncmPRIPortNFASMode,
       "ncmPRIPortDChanMode": ncmPRIPortDChanMode,
       "ncmPRIPortDChanBits": ncmPRIPortDChanBits,
       "ncmPRIPortTimeslotMap": ncmPRIPortTimeslotMap,
       "ncmPRIPortSwitchType": ncmPRIPortSwitchType,
       "ncmPRIPortOwnNumPlan": ncmPRIPortOwnNumPlan,
       "ncmPRIPortOwnNumType": ncmPRIPortOwnNumType,
       "ncmPRIPortSecurityLevel": ncmPRIPortSecurityLevel,
       "ncmPRIPortConfigStatus": ncmPRIPortConfigStatus,
       "ncmPRIPortSetConfig": ncmPRIPortSetConfig,
       "ncmPRICallProfCallRefCount": ncmPRICallProfCallRefCount,
       "ncmPRIL2AutoEstablish": ncmPRIL2AutoEstablish,
       "ncmPRIResetCard": ncmPRIResetCard,
       "ncmPRICallProfileTable": ncmPRICallProfileTable,
       "ncmPRICallProfEntry": ncmPRICallProfEntry,
       "ncmPRICallProfNIDIndex": ncmPRICallProfNIDIndex,
       "ncmPRICallProfLineIndex": ncmPRICallProfLineIndex,
       "ncmPRICPCallProfileRef": ncmPRICPCallProfileRef,
       "ncmPRICallProfCallDir": ncmPRICallProfCallDir,
       "ncmPRICallProfNumOwnDigit": ncmPRICallProfNumOwnDigit,
       "ncmPRICallProfOwnCallNum": ncmPRICallProfOwnCallNum,
       "ncmPRICallProfExtNumPlan": ncmPRICallProfExtNumPlan,
       "ncmPRICallProfExtNumType": ncmPRICallProfExtNumType,
       "ncmPRICallProfExtNumDigit": ncmPRICallProfExtNumDigit,
       "ncmPRICallProfExtCallNum": ncmPRICallProfExtCallNum,
       "ncmPRICallProfTransferMode": ncmPRICallProfTransferMode,
       "ncmPRICallProfCallBandWth": ncmPRICallProfCallBandWth,
       "ncmPRICallProfMultiRateCnt": ncmPRICallProfMultiRateCnt,
       "ncmPRICallProfRateAdaptn": ncmPRICallProfRateAdaptn,
       "ncmPRICallProfTestCallIntvl": ncmPRICallProfTestCallIntvl,
       "ncmPRICallProfCallStatus": ncmPRICallProfCallStatus,
       "ncmPRICallProfCallAction": ncmPRICallProfCallAction,
       "ncmPRICPSetCallProf": ncmPRICPSetCallProf,
       "ncmPRICPSetCallProfResp": ncmPRICPSetCallProfResp,
       "ncmPRICPCallActionResp": ncmPRICPCallActionResp,
       "ncmPRICallProfListTable": ncmPRICallProfListTable,
       "ncmPRICallProfListEntry": ncmPRICallProfListEntry,
       "ncmPRICPListNIDIndex": ncmPRICPListNIDIndex,
       "ncmPRICPListLineIndex": ncmPRICPListLineIndex,
       "ncmPRICPListIndex": ncmPRICPListIndex,
       "ncmPRICPListValidCPRefNum": ncmPRICPListValidCPRefNum,
       "ncmPRICurrentTable": ncmPRICurrentTable,
       "ncmPRICurrentEntry": ncmPRICurrentEntry,
       "ncmPRICurrNIDIndex": ncmPRICurrNIDIndex,
       "ncmPRICurrLineIndex": ncmPRICurrLineIndex,
       "ncmPRICurrEndType": ncmPRICurrEndType,
       "ncmPRICurrTimestamp": ncmPRICurrTimestamp,
       "ncmPRICurrSecsInCurrIntvl": ncmPRICurrSecsInCurrIntvl,
       "ncmPRICurrInfoRx": ncmPRICurrInfoRx,
       "ncmPRICurrInfoTx": ncmPRICurrInfoTx,
       "ncmPRICurrCRCErrRx": ncmPRICurrCRCErrRx,
       "ncmPRICurrInvalidFrameRx": ncmPRICurrInvalidFrameRx,
       "ncmPRICurrFrameAbortRx": ncmPRICurrFrameAbortRx,
       "ncmPRICurrDISCSRx": ncmPRICurrDISCSRx,
       "ncmPRICurrDISCSTx": ncmPRICurrDISCSTx,
       "ncmPRICurrFramerRx": ncmPRICurrFramerRx,
       "ncmPRICurrFramerTx": ncmPRICurrFramerTx,
       "ncmPRICurrLyr3ProtErr": ncmPRICurrLyr3ProtErr,
       "ncmPRICurrCallSetupSent": ncmPRICurrCallSetupSent,
       "ncmPRICurrCallSetupSentnFail": ncmPRICurrCallSetupSentnFail,
       "ncmPRICurrCallSetupRx": ncmPRICurrCallSetupRx,
       "ncmPRICurrCallSetupRxnFail": ncmPRICurrCallSetupRxnFail,
       "ncmPRICurrUnSupportMsgRx": ncmPRICurrUnSupportMsgRx,
       "ncmPRICurrTstCalSetupSentnFail": ncmPRICurrTstCalSetupSentnFail,
       "ncmPRICurrValidIntvls": ncmPRICurrValidIntvls,
       "ncmPRICurrStatisticReset": ncmPRICurrStatisticReset,
       "ncmPRIIntervalTable": ncmPRIIntervalTable,
       "ncmPRIIntervalEntry": ncmPRIIntervalEntry,
       "ncmPRIntvlNIDIndex": ncmPRIntvlNIDIndex,
       "ncmPRIntvlLineIndex": ncmPRIntvlLineIndex,
       "ncmPRIntvlEndType": ncmPRIntvlEndType,
       "ncmPRIntvlIndex": ncmPRIntvlIndex,
       "ncmPRIntvlTimestamp": ncmPRIntvlTimestamp,
       "ncmPRIntvlSecsInCurrIntvl": ncmPRIntvlSecsInCurrIntvl,
       "ncmPRIntvlInfoRx": ncmPRIntvlInfoRx,
       "ncmPRIntvlInfoTx": ncmPRIntvlInfoTx,
       "ncmPRIntvlCRCErrRx": ncmPRIntvlCRCErrRx,
       "ncmPRIntvlInvalidFrameRx": ncmPRIntvlInvalidFrameRx,
       "ncmPRIntvlFrameAbortRx": ncmPRIntvlFrameAbortRx,
       "ncmPRIntvlDISCSRx": ncmPRIntvlDISCSRx,
       "ncmPRIntvlDISCSTx": ncmPRIntvlDISCSTx,
       "ncmPRIntvlFramerRx": ncmPRIntvlFramerRx,
       "ncmPRIntvlFramerTx": ncmPRIntvlFramerTx,
       "ncmPRIntvlLyr3ProtErr": ncmPRIntvlLyr3ProtErr,
       "ncmPRIntvlCallSetupSent": ncmPRIntvlCallSetupSent,
       "ncmPRIntvlCallSetupSentnFail": ncmPRIntvlCallSetupSentnFail,
       "ncmPRIntvlCallSetupRx": ncmPRIntvlCallSetupRx,
       "ncmPRIntvlCallSetupRxnFail": ncmPRIntvlCallSetupRxnFail,
       "ncmPRIntvlUnSupportMsgRx": ncmPRIntvlUnSupportMsgRx,
       "ncmPRIntvlTstCalSetupSentnFail": ncmPRIntvlTstCalSetupSentnFail}
)
