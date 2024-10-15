# SNMP MIB module (MICOMBRGEXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOMBRGEXT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:54 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McmBrg_ObjectIdentity = ObjectIdentity
mcmBrg = _McmBrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6)
)
_McmBrgGlobalParamGroup_ObjectIdentity = ObjectIdentity
mcmBrgGlobalParamGroup = _McmBrgGlobalParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1)
)


class _McmBrgIPBridged_Type(Integer32):
    """Custom type mcmBrgIPBridged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("routed", 2))
    )


_McmBrgIPBridged_Type.__name__ = "Integer32"
_McmBrgIPBridged_Object = MibScalar
mcmBrgIPBridged = _McmBrgIPBridged_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1, 1),
    _McmBrgIPBridged_Type()
)
mcmBrgIPBridged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgIPBridged.setStatus("mandatory")
_McmBrgNumInterfaces_Type = Integer32
_McmBrgNumInterfaces_Object = MibScalar
mcmBrgNumInterfaces = _McmBrgNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1, 2),
    _McmBrgNumInterfaces_Type()
)
mcmBrgNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgNumInterfaces.setStatus("mandatory")


class _McmBrgSpanEnable_Type(Integer32):
    """Custom type mcmBrgSpanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgSpanEnable_Type.__name__ = "Integer32"
_McmBrgSpanEnable_Object = MibScalar
mcmBrgSpanEnable = _McmBrgSpanEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1, 3),
    _McmBrgSpanEnable_Type()
)
mcmBrgSpanEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgSpanEnable.setStatus("mandatory")


class _McmBrgSpoofEnable_Type(Integer32):
    """Custom type mcmBrgSpoofEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgSpoofEnable_Type.__name__ = "Integer32"
_McmBrgSpoofEnable_Object = MibScalar
mcmBrgSpoofEnable = _McmBrgSpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1, 4),
    _McmBrgSpoofEnable_Type()
)
mcmBrgSpoofEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgSpoofEnable.setStatus("mandatory")


class _McmBrgAgeTime_Type(Integer32):
    """Custom type mcmBrgAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_McmBrgAgeTime_Type.__name__ = "Integer32"
_McmBrgAgeTime_Object = MibScalar
mcmBrgAgeTime = _McmBrgAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 1, 5),
    _McmBrgAgeTime_Type()
)
mcmBrgAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgAgeTime.setStatus("mandatory")
_McmBrgMiscParamGroup_ObjectIdentity = ObjectIdentity
mcmBrgMiscParamGroup = _McmBrgMiscParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2)
)


class _McmBrgDebugEnable_Type(Integer32):
    """Custom type mcmBrgDebugEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgDebugEnable_Type.__name__ = "Integer32"
_McmBrgDebugEnable_Object = MibScalar
mcmBrgDebugEnable = _McmBrgDebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2, 1),
    _McmBrgDebugEnable_Type()
)
mcmBrgDebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgDebugEnable.setStatus("mandatory")


class _McmBrgSpanDebugEnable_Type(Integer32):
    """Custom type mcmBrgSpanDebugEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgSpanDebugEnable_Type.__name__ = "Integer32"
_McmBrgSpanDebugEnable_Object = MibScalar
mcmBrgSpanDebugEnable = _McmBrgSpanDebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2, 2),
    _McmBrgSpanDebugEnable_Type()
)
mcmBrgSpanDebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSpanDebugEnable.setStatus("mandatory")


class _McmBrgSpoofCacheAge_Type(Integer32):
    """Custom type mcmBrgSpoofCacheAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_McmBrgSpoofCacheAge_Type.__name__ = "Integer32"
_McmBrgSpoofCacheAge_Object = MibScalar
mcmBrgSpoofCacheAge = _McmBrgSpoofCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2, 3),
    _McmBrgSpoofCacheAge_Type()
)
mcmBrgSpoofCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSpoofCacheAge.setStatus("mandatory")


class _McmBrgSpoofThresholdAge_Type(Integer32):
    """Custom type mcmBrgSpoofThresholdAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_McmBrgSpoofThresholdAge_Type.__name__ = "Integer32"
_McmBrgSpoofThresholdAge_Object = MibScalar
mcmBrgSpoofThresholdAge = _McmBrgSpoofThresholdAge_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2, 4),
    _McmBrgSpoofThresholdAge_Type()
)
mcmBrgSpoofThresholdAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSpoofThresholdAge.setStatus("mandatory")


class _McmBrgSpoofThresholdCount_Type(Integer32):
    """Custom type mcmBrgSpoofThresholdCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_McmBrgSpoofThresholdCount_Type.__name__ = "Integer32"
_McmBrgSpoofThresholdCount_Object = MibScalar
mcmBrgSpoofThresholdCount = _McmBrgSpoofThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 2, 5),
    _McmBrgSpoofThresholdCount_Type()
)
mcmBrgSpoofThresholdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSpoofThresholdCount.setStatus("mandatory")
_McmBrgConfPortTable_Object = MibTable
mcmBrgConfPortTable = _McmBrgConfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3)
)
if mibBuilder.loadTexts:
    mcmBrgConfPortTable.setStatus("mandatory")
_McmBrgConfPortEntry_Object = MibTableRow
mcmBrgConfPortEntry = _McmBrgConfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1)
)
mcmBrgConfPortEntry.setIndexNames(
    (0, "MICOMBRGEXT", "mcmBrgConfPortIndex"),
)
if mibBuilder.loadTexts:
    mcmBrgConfPortEntry.setStatus("mandatory")
_McmBrgConfPortIndex_Type = Integer32
_McmBrgConfPortIndex_Object = MibTableColumn
mcmBrgConfPortIndex = _McmBrgConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 1),
    _McmBrgConfPortIndex_Type()
)
mcmBrgConfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgConfPortIndex.setStatus("mandatory")
_McmBrgConfPortPPA_Type = Integer32
_McmBrgConfPortPPA_Object = MibTableColumn
mcmBrgConfPortPPA = _McmBrgConfPortPPA_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 2),
    _McmBrgConfPortPPA_Type()
)
mcmBrgConfPortPPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgConfPortPPA.setStatus("mandatory")


class _McmBrgConfPortType_Type(Integer32):
    """Custom type mcmBrgConfPortType based on Integer32"""
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
        *(("ethernet", 1),
          ("frameRelay", 3),
          ("internal", 4),
          ("wan", 2))
    )


_McmBrgConfPortType_Type.__name__ = "Integer32"
_McmBrgConfPortType_Object = MibTableColumn
mcmBrgConfPortType = _McmBrgConfPortType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 3),
    _McmBrgConfPortType_Type()
)
mcmBrgConfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmBrgConfPortType.setStatus("mandatory")


class _McmBrgConfPortMacFilterFlag_Type(Integer32):
    """Custom type mcmBrgConfPortMacFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgConfPortMacFilterFlag_Type.__name__ = "Integer32"
_McmBrgConfPortMacFilterFlag_Object = MibTableColumn
mcmBrgConfPortMacFilterFlag = _McmBrgConfPortMacFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 4),
    _McmBrgConfPortMacFilterFlag_Type()
)
mcmBrgConfPortMacFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortMacFilterFlag.setStatus("mandatory")


class _McmBrgConfPortEtFilterFlag_Type(Integer32):
    """Custom type mcmBrgConfPortEtFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgConfPortEtFilterFlag_Type.__name__ = "Integer32"
_McmBrgConfPortEtFilterFlag_Object = MibTableColumn
mcmBrgConfPortEtFilterFlag = _McmBrgConfPortEtFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 5),
    _McmBrgConfPortEtFilterFlag_Type()
)
mcmBrgConfPortEtFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortEtFilterFlag.setStatus("mandatory")


class _McmBrgConfPortSapFilterFlag_Type(Integer32):
    """Custom type mcmBrgConfPortSapFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_McmBrgConfPortSapFilterFlag_Type.__name__ = "Integer32"
_McmBrgConfPortSapFilterFlag_Object = MibTableColumn
mcmBrgConfPortSapFilterFlag = _McmBrgConfPortSapFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 6),
    _McmBrgConfPortSapFilterFlag_Type()
)
mcmBrgConfPortSapFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortSapFilterFlag.setStatus("mandatory")


class _McmBrgConfPortMacInclExcl_Type(Integer32):
    """Custom type mcmBrgConfPortMacInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmBrgConfPortMacInclExcl_Type.__name__ = "Integer32"
_McmBrgConfPortMacInclExcl_Object = MibTableColumn
mcmBrgConfPortMacInclExcl = _McmBrgConfPortMacInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 7),
    _McmBrgConfPortMacInclExcl_Type()
)
mcmBrgConfPortMacInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortMacInclExcl.setStatus("mandatory")


class _McmBrgConfPortEtInclExcl_Type(Integer32):
    """Custom type mcmBrgConfPortEtInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmBrgConfPortEtInclExcl_Type.__name__ = "Integer32"
_McmBrgConfPortEtInclExcl_Object = MibTableColumn
mcmBrgConfPortEtInclExcl = _McmBrgConfPortEtInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 8),
    _McmBrgConfPortEtInclExcl_Type()
)
mcmBrgConfPortEtInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortEtInclExcl.setStatus("mandatory")


class _McmBrgConfPortSapInclExcl_Type(Integer32):
    """Custom type mcmBrgConfPortSapInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_McmBrgConfPortSapInclExcl_Type.__name__ = "Integer32"
_McmBrgConfPortSapInclExcl_Object = MibTableColumn
mcmBrgConfPortSapInclExcl = _McmBrgConfPortSapInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 3, 1, 9),
    _McmBrgConfPortSapInclExcl_Type()
)
mcmBrgConfPortSapInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgConfPortSapInclExcl.setStatus("mandatory")
_McmBrgMacFilterTable_Object = MibTable
mcmBrgMacFilterTable = _McmBrgMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4)
)
if mibBuilder.loadTexts:
    mcmBrgMacFilterTable.setStatus("mandatory")
_McmBrgMacFilterEntry_Object = MibTableRow
mcmBrgMacFilterEntry = _McmBrgMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4, 1)
)
mcmBrgMacFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "mcmBrgMacFilterPortIndex"),
    (0, "MICOMBRGEXT", "mcmBrgMacFilterNumber"),
)
if mibBuilder.loadTexts:
    mcmBrgMacFilterEntry.setStatus("mandatory")


class _McmBrgMacFilterPortIndex_Type(Integer32):
    """Custom type mcmBrgMacFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmBrgMacFilterPortIndex_Type.__name__ = "Integer32"
_McmBrgMacFilterPortIndex_Object = MibTableColumn
mcmBrgMacFilterPortIndex = _McmBrgMacFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4, 1, 1),
    _McmBrgMacFilterPortIndex_Type()
)
mcmBrgMacFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgMacFilterPortIndex.setStatus("mandatory")


class _McmBrgMacFilterNumber_Type(Integer32):
    """Custom type mcmBrgMacFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmBrgMacFilterNumber_Type.__name__ = "Integer32"
_McmBrgMacFilterNumber_Object = MibTableColumn
mcmBrgMacFilterNumber = _McmBrgMacFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4, 1, 2),
    _McmBrgMacFilterNumber_Type()
)
mcmBrgMacFilterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgMacFilterNumber.setStatus("mandatory")
_McmBrgMacAddress_Type = MacAddress
_McmBrgMacAddress_Object = MibTableColumn
mcmBrgMacAddress = _McmBrgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4, 1, 3),
    _McmBrgMacAddress_Type()
)
mcmBrgMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgMacAddress.setStatus("mandatory")


class _McmBrgMacType_Type(Integer32):
    """Custom type mcmBrgMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("invalid", 3),
          ("source", 1))
    )


_McmBrgMacType_Type.__name__ = "Integer32"
_McmBrgMacType_Object = MibTableColumn
mcmBrgMacType = _McmBrgMacType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 4, 1, 4),
    _McmBrgMacType_Type()
)
mcmBrgMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgMacType.setStatus("mandatory")
_McmBrgEtFilterTable_Object = MibTable
mcmBrgEtFilterTable = _McmBrgEtFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5)
)
if mibBuilder.loadTexts:
    mcmBrgEtFilterTable.setStatus("mandatory")
_McmBrgEtFilterEntry_Object = MibTableRow
mcmBrgEtFilterEntry = _McmBrgEtFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1)
)
mcmBrgEtFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "mcmBrgEtFilterPortIndex"),
    (0, "MICOMBRGEXT", "mcmBrgEtFilterNumber"),
)
if mibBuilder.loadTexts:
    mcmBrgEtFilterEntry.setStatus("mandatory")


class _McmBrgEtFilterPortIndex_Type(Integer32):
    """Custom type mcmBrgEtFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmBrgEtFilterPortIndex_Type.__name__ = "Integer32"
_McmBrgEtFilterPortIndex_Object = MibTableColumn
mcmBrgEtFilterPortIndex = _McmBrgEtFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 1),
    _McmBrgEtFilterPortIndex_Type()
)
mcmBrgEtFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterPortIndex.setStatus("mandatory")


class _McmBrgEtFilterNumber_Type(Integer32):
    """Custom type mcmBrgEtFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmBrgEtFilterNumber_Type.__name__ = "Integer32"
_McmBrgEtFilterNumber_Object = MibTableColumn
mcmBrgEtFilterNumber = _McmBrgEtFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 2),
    _McmBrgEtFilterNumber_Type()
)
mcmBrgEtFilterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterNumber.setStatus("mandatory")


class _McmBrgEtFilterStatus_Type(Integer32):
    """Custom type mcmBrgEtFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("range", 2),
          ("singular", 1))
    )


_McmBrgEtFilterStatus_Type.__name__ = "Integer32"
_McmBrgEtFilterStatus_Object = MibTableColumn
mcmBrgEtFilterStatus = _McmBrgEtFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 3),
    _McmBrgEtFilterStatus_Type()
)
mcmBrgEtFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterStatus.setStatus("mandatory")


class _McmBrgEtFilterEType_Type(Integer32):
    """Custom type mcmBrgEtFilterEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_McmBrgEtFilterEType_Type.__name__ = "Integer32"
_McmBrgEtFilterEType_Object = MibTableColumn
mcmBrgEtFilterEType = _McmBrgEtFilterEType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 4),
    _McmBrgEtFilterEType_Type()
)
mcmBrgEtFilterEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterEType.setStatus("mandatory")


class _McmBrgEtFilterUpperRange_Type(Integer32):
    """Custom type mcmBrgEtFilterUpperRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_McmBrgEtFilterUpperRange_Type.__name__ = "Integer32"
_McmBrgEtFilterUpperRange_Object = MibTableColumn
mcmBrgEtFilterUpperRange = _McmBrgEtFilterUpperRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 5),
    _McmBrgEtFilterUpperRange_Type()
)
mcmBrgEtFilterUpperRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterUpperRange.setStatus("mandatory")


class _McmBrgEtFilterLowerRange_Type(Integer32):
    """Custom type mcmBrgEtFilterLowerRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_McmBrgEtFilterLowerRange_Type.__name__ = "Integer32"
_McmBrgEtFilterLowerRange_Object = MibTableColumn
mcmBrgEtFilterLowerRange = _McmBrgEtFilterLowerRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 5, 1, 6),
    _McmBrgEtFilterLowerRange_Type()
)
mcmBrgEtFilterLowerRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgEtFilterLowerRange.setStatus("mandatory")
_McmBrgSapFilterTable_Object = MibTable
mcmBrgSapFilterTable = _McmBrgSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6)
)
if mibBuilder.loadTexts:
    mcmBrgSapFilterTable.setStatus("mandatory")
_McmBrgSapFilterEntry_Object = MibTableRow
mcmBrgSapFilterEntry = _McmBrgSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1)
)
mcmBrgSapFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "mcmBrgSapFilterPortIndex"),
    (0, "MICOMBRGEXT", "mcmBrgSapFilterNumber"),
)
if mibBuilder.loadTexts:
    mcmBrgSapFilterEntry.setStatus("mandatory")


class _McmBrgSapFilterPortIndex_Type(Integer32):
    """Custom type mcmBrgSapFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmBrgSapFilterPortIndex_Type.__name__ = "Integer32"
_McmBrgSapFilterPortIndex_Object = MibTableColumn
mcmBrgSapFilterPortIndex = _McmBrgSapFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 1),
    _McmBrgSapFilterPortIndex_Type()
)
mcmBrgSapFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterPortIndex.setStatus("mandatory")


class _McmBrgSapFilterNumber_Type(Integer32):
    """Custom type mcmBrgSapFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmBrgSapFilterNumber_Type.__name__ = "Integer32"
_McmBrgSapFilterNumber_Object = MibTableColumn
mcmBrgSapFilterNumber = _McmBrgSapFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 2),
    _McmBrgSapFilterNumber_Type()
)
mcmBrgSapFilterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterNumber.setStatus("mandatory")


class _McmBrgSapFilterStatus_Type(Integer32):
    """Custom type mcmBrgSapFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("range", 2),
          ("singular", 1))
    )


_McmBrgSapFilterStatus_Type.__name__ = "Integer32"
_McmBrgSapFilterStatus_Object = MibTableColumn
mcmBrgSapFilterStatus = _McmBrgSapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 3),
    _McmBrgSapFilterStatus_Type()
)
mcmBrgSapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterStatus.setStatus("mandatory")


class _McmBrgSapFilterEType_Type(Integer32):
    """Custom type mcmBrgSapFilterEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmBrgSapFilterEType_Type.__name__ = "Integer32"
_McmBrgSapFilterEType_Object = MibTableColumn
mcmBrgSapFilterEType = _McmBrgSapFilterEType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 4),
    _McmBrgSapFilterEType_Type()
)
mcmBrgSapFilterEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterEType.setStatus("mandatory")


class _McmBrgSapFilterUpperRange_Type(Integer32):
    """Custom type mcmBrgSapFilterUpperRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmBrgSapFilterUpperRange_Type.__name__ = "Integer32"
_McmBrgSapFilterUpperRange_Object = MibTableColumn
mcmBrgSapFilterUpperRange = _McmBrgSapFilterUpperRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 5),
    _McmBrgSapFilterUpperRange_Type()
)
mcmBrgSapFilterUpperRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterUpperRange.setStatus("mandatory")


class _McmBrgSapFilterLowerRange_Type(Integer32):
    """Custom type mcmBrgSapFilterLowerRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmBrgSapFilterLowerRange_Type.__name__ = "Integer32"
_McmBrgSapFilterLowerRange_Object = MibTableColumn
mcmBrgSapFilterLowerRange = _McmBrgSapFilterLowerRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 6, 1, 6),
    _McmBrgSapFilterLowerRange_Type()
)
mcmBrgSapFilterLowerRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgSapFilterLowerRange.setStatus("mandatory")
_NvmBrgGlobalParamGroup_ObjectIdentity = ObjectIdentity
nvmBrgGlobalParamGroup = _NvmBrgGlobalParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7)
)


class _NvmBrgIPBridged_Type(Integer32):
    """Custom type nvmBrgIPBridged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("routed", 2))
    )


_NvmBrgIPBridged_Type.__name__ = "Integer32"
_NvmBrgIPBridged_Object = MibScalar
nvmBrgIPBridged = _NvmBrgIPBridged_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7, 1),
    _NvmBrgIPBridged_Type()
)
nvmBrgIPBridged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgIPBridged.setStatus("mandatory")


class _NvmBrgNumInterfaces_Type(Integer32):
    """Custom type nvmBrgNumInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmBrgNumInterfaces_Type.__name__ = "Integer32"
_NvmBrgNumInterfaces_Object = MibScalar
nvmBrgNumInterfaces = _NvmBrgNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7, 2),
    _NvmBrgNumInterfaces_Type()
)
nvmBrgNumInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgNumInterfaces.setStatus("mandatory")


class _NvmBrgSpanEnable_Type(Integer32):
    """Custom type nvmBrgSpanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgSpanEnable_Type.__name__ = "Integer32"
_NvmBrgSpanEnable_Object = MibScalar
nvmBrgSpanEnable = _NvmBrgSpanEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7, 3),
    _NvmBrgSpanEnable_Type()
)
nvmBrgSpanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpanEnable.setStatus("mandatory")


class _NvmBrgSpoofEnable_Type(Integer32):
    """Custom type nvmBrgSpoofEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgSpoofEnable_Type.__name__ = "Integer32"
_NvmBrgSpoofEnable_Object = MibScalar
nvmBrgSpoofEnable = _NvmBrgSpoofEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7, 4),
    _NvmBrgSpoofEnable_Type()
)
nvmBrgSpoofEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpoofEnable.setStatus("mandatory")


class _NvmBrgAgeTime_Type(Integer32):
    """Custom type nvmBrgAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_NvmBrgAgeTime_Type.__name__ = "Integer32"
_NvmBrgAgeTime_Object = MibScalar
nvmBrgAgeTime = _NvmBrgAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 7, 5),
    _NvmBrgAgeTime_Type()
)
nvmBrgAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgAgeTime.setStatus("mandatory")
_NvmBrgMiscParamGroup_ObjectIdentity = ObjectIdentity
nvmBrgMiscParamGroup = _NvmBrgMiscParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8)
)


class _NvmBrgDebugEnable_Type(Integer32):
    """Custom type nvmBrgDebugEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgDebugEnable_Type.__name__ = "Integer32"
_NvmBrgDebugEnable_Object = MibScalar
nvmBrgDebugEnable = _NvmBrgDebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8, 1),
    _NvmBrgDebugEnable_Type()
)
nvmBrgDebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgDebugEnable.setStatus("mandatory")


class _NvmBrgSpanDebugEnable_Type(Integer32):
    """Custom type nvmBrgSpanDebugEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgSpanDebugEnable_Type.__name__ = "Integer32"
_NvmBrgSpanDebugEnable_Object = MibScalar
nvmBrgSpanDebugEnable = _NvmBrgSpanDebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8, 2),
    _NvmBrgSpanDebugEnable_Type()
)
nvmBrgSpanDebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpanDebugEnable.setStatus("mandatory")


class _NvmBrgSpoofCacheAge_Type(Integer32):
    """Custom type nvmBrgSpoofCacheAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_NvmBrgSpoofCacheAge_Type.__name__ = "Integer32"
_NvmBrgSpoofCacheAge_Object = MibScalar
nvmBrgSpoofCacheAge = _NvmBrgSpoofCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8, 3),
    _NvmBrgSpoofCacheAge_Type()
)
nvmBrgSpoofCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpoofCacheAge.setStatus("mandatory")


class _NvmBrgSpoofThresholdAge_Type(Integer32):
    """Custom type nvmBrgSpoofThresholdAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_NvmBrgSpoofThresholdAge_Type.__name__ = "Integer32"
_NvmBrgSpoofThresholdAge_Object = MibScalar
nvmBrgSpoofThresholdAge = _NvmBrgSpoofThresholdAge_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8, 4),
    _NvmBrgSpoofThresholdAge_Type()
)
nvmBrgSpoofThresholdAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpoofThresholdAge.setStatus("mandatory")


class _NvmBrgSpoofThresholdCount_Type(Integer32):
    """Custom type nvmBrgSpoofThresholdCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NvmBrgSpoofThresholdCount_Type.__name__ = "Integer32"
_NvmBrgSpoofThresholdCount_Object = MibScalar
nvmBrgSpoofThresholdCount = _NvmBrgSpoofThresholdCount_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 8, 5),
    _NvmBrgSpoofThresholdCount_Type()
)
nvmBrgSpoofThresholdCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSpoofThresholdCount.setStatus("mandatory")
_NvmBrgStpParamGroup_ObjectIdentity = ObjectIdentity
nvmBrgStpParamGroup = _NvmBrgStpParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 9)
)


class _NvmBrgPriority_Type(Integer32):
    """Custom type nvmBrgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmBrgPriority_Type.__name__ = "Integer32"
_NvmBrgPriority_Object = MibScalar
nvmBrgPriority = _NvmBrgPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 9, 1),
    _NvmBrgPriority_Type()
)
nvmBrgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgPriority.setStatus("mandatory")


class _NvmBrgMaxAge_Type(Timeout):
    """Custom type nvmBrgMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_NvmBrgMaxAge_Type.__name__ = "Timeout"
_NvmBrgMaxAge_Object = MibScalar
nvmBrgMaxAge = _NvmBrgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 9, 2),
    _NvmBrgMaxAge_Type()
)
nvmBrgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgMaxAge.setStatus("mandatory")


class _NvmBrgFwdDelay_Type(Timeout):
    """Custom type nvmBrgFwdDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_NvmBrgFwdDelay_Type.__name__ = "Timeout"
_NvmBrgFwdDelay_Object = MibScalar
nvmBrgFwdDelay = _NvmBrgFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 9, 3),
    _NvmBrgFwdDelay_Type()
)
nvmBrgFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgFwdDelay.setStatus("mandatory")


class _NvmBrgHelloTime_Type(Timeout):
    """Custom type nvmBrgHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_NvmBrgHelloTime_Type.__name__ = "Timeout"
_NvmBrgHelloTime_Object = MibScalar
nvmBrgHelloTime = _NvmBrgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 9, 4),
    _NvmBrgHelloTime_Type()
)
nvmBrgHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgHelloTime.setStatus("mandatory")
_NvmBrgConfPortTable_Object = MibTable
nvmBrgConfPortTable = _NvmBrgConfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10)
)
if mibBuilder.loadTexts:
    nvmBrgConfPortTable.setStatus("mandatory")
_NvmBrgConfPortEntry_Object = MibTableRow
nvmBrgConfPortEntry = _NvmBrgConfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1)
)
nvmBrgConfPortEntry.setIndexNames(
    (0, "MICOMBRGEXT", "nvmBrgConfPortIndex"),
)
if mibBuilder.loadTexts:
    nvmBrgConfPortEntry.setStatus("mandatory")


class _NvmBrgConfPortIndex_Type(Integer32):
    """Custom type nvmBrgConfPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmBrgConfPortIndex_Type.__name__ = "Integer32"
_NvmBrgConfPortIndex_Object = MibTableColumn
nvmBrgConfPortIndex = _NvmBrgConfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 1),
    _NvmBrgConfPortIndex_Type()
)
nvmBrgConfPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortIndex.setStatus("mandatory")


class _NvmBrgConfPortType_Type(Integer32):
    """Custom type nvmBrgConfPortType based on Integer32"""
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
        *(("ethernet", 1),
          ("frameRelay", 3),
          ("internal", 4),
          ("wan", 2))
    )


_NvmBrgConfPortType_Type.__name__ = "Integer32"
_NvmBrgConfPortType_Object = MibTableColumn
nvmBrgConfPortType = _NvmBrgConfPortType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 2),
    _NvmBrgConfPortType_Type()
)
nvmBrgConfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortType.setStatus("mandatory")


class _NvmBrgConfPortEnable_Type(Integer32):
    """Custom type nvmBrgConfPortEnable based on Integer32"""
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
          ("enabled", 1),
          ("invalid", 3))
    )


_NvmBrgConfPortEnable_Type.__name__ = "Integer32"
_NvmBrgConfPortEnable_Object = MibTableColumn
nvmBrgConfPortEnable = _NvmBrgConfPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 3),
    _NvmBrgConfPortEnable_Type()
)
nvmBrgConfPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortEnable.setStatus("mandatory")


class _NvmBrgConfPortPriority_Type(Integer32):
    """Custom type nvmBrgConfPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmBrgConfPortPriority_Type.__name__ = "Integer32"
_NvmBrgConfPortPriority_Object = MibTableColumn
nvmBrgConfPortPriority = _NvmBrgConfPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 4),
    _NvmBrgConfPortPriority_Type()
)
nvmBrgConfPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortPriority.setStatus("mandatory")


class _NvmBrgConfPortPathCost_Type(Integer32):
    """Custom type nvmBrgConfPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NvmBrgConfPortPathCost_Type.__name__ = "Integer32"
_NvmBrgConfPortPathCost_Object = MibTableColumn
nvmBrgConfPortPathCost = _NvmBrgConfPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 5),
    _NvmBrgConfPortPathCost_Type()
)
nvmBrgConfPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortPathCost.setStatus("mandatory")


class _NvmBrgConfPortMacFilterFlag_Type(Integer32):
    """Custom type nvmBrgConfPortMacFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgConfPortMacFilterFlag_Type.__name__ = "Integer32"
_NvmBrgConfPortMacFilterFlag_Object = MibTableColumn
nvmBrgConfPortMacFilterFlag = _NvmBrgConfPortMacFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 6),
    _NvmBrgConfPortMacFilterFlag_Type()
)
nvmBrgConfPortMacFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortMacFilterFlag.setStatus("mandatory")


class _NvmBrgConfPortEtFilterFlag_Type(Integer32):
    """Custom type nvmBrgConfPortEtFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgConfPortEtFilterFlag_Type.__name__ = "Integer32"
_NvmBrgConfPortEtFilterFlag_Object = MibTableColumn
nvmBrgConfPortEtFilterFlag = _NvmBrgConfPortEtFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 7),
    _NvmBrgConfPortEtFilterFlag_Type()
)
nvmBrgConfPortEtFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortEtFilterFlag.setStatus("mandatory")


class _NvmBrgConfPortSapFilterFlag_Type(Integer32):
    """Custom type nvmBrgConfPortSapFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NvmBrgConfPortSapFilterFlag_Type.__name__ = "Integer32"
_NvmBrgConfPortSapFilterFlag_Object = MibTableColumn
nvmBrgConfPortSapFilterFlag = _NvmBrgConfPortSapFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 8),
    _NvmBrgConfPortSapFilterFlag_Type()
)
nvmBrgConfPortSapFilterFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortSapFilterFlag.setStatus("mandatory")


class _NvmBrgConfPortMacInclExcl_Type(Integer32):
    """Custom type nvmBrgConfPortMacInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmBrgConfPortMacInclExcl_Type.__name__ = "Integer32"
_NvmBrgConfPortMacInclExcl_Object = MibTableColumn
nvmBrgConfPortMacInclExcl = _NvmBrgConfPortMacInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 9),
    _NvmBrgConfPortMacInclExcl_Type()
)
nvmBrgConfPortMacInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortMacInclExcl.setStatus("mandatory")


class _NvmBrgConfPortEtInclExcl_Type(Integer32):
    """Custom type nvmBrgConfPortEtInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmBrgConfPortEtInclExcl_Type.__name__ = "Integer32"
_NvmBrgConfPortEtInclExcl_Object = MibTableColumn
nvmBrgConfPortEtInclExcl = _NvmBrgConfPortEtInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 10),
    _NvmBrgConfPortEtInclExcl_Type()
)
nvmBrgConfPortEtInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortEtInclExcl.setStatus("mandatory")


class _NvmBrgConfPortSapInclExcl_Type(Integer32):
    """Custom type nvmBrgConfPortSapInclExcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 2),
          ("inclusive", 1))
    )


_NvmBrgConfPortSapInclExcl_Type.__name__ = "Integer32"
_NvmBrgConfPortSapInclExcl_Object = MibTableColumn
nvmBrgConfPortSapInclExcl = _NvmBrgConfPortSapInclExcl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 10, 1, 11),
    _NvmBrgConfPortSapInclExcl_Type()
)
nvmBrgConfPortSapInclExcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgConfPortSapInclExcl.setStatus("mandatory")
_NvmBrgMacFilterTable_Object = MibTable
nvmBrgMacFilterTable = _NvmBrgMacFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11)
)
if mibBuilder.loadTexts:
    nvmBrgMacFilterTable.setStatus("mandatory")
_NvmBrgMacFilterEntry_Object = MibTableRow
nvmBrgMacFilterEntry = _NvmBrgMacFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11, 1)
)
nvmBrgMacFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "nvmBrgMacFilterPortIndex"),
    (0, "MICOMBRGEXT", "nvmBrgMacFilterNumber"),
)
if mibBuilder.loadTexts:
    nvmBrgMacFilterEntry.setStatus("mandatory")


class _NvmBrgMacFilterPortIndex_Type(Integer32):
    """Custom type nvmBrgMacFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmBrgMacFilterPortIndex_Type.__name__ = "Integer32"
_NvmBrgMacFilterPortIndex_Object = MibTableColumn
nvmBrgMacFilterPortIndex = _NvmBrgMacFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11, 1, 1),
    _NvmBrgMacFilterPortIndex_Type()
)
nvmBrgMacFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgMacFilterPortIndex.setStatus("mandatory")


class _NvmBrgMacFilterNumber_Type(Integer32):
    """Custom type nvmBrgMacFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmBrgMacFilterNumber_Type.__name__ = "Integer32"
_NvmBrgMacFilterNumber_Object = MibTableColumn
nvmBrgMacFilterNumber = _NvmBrgMacFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11, 1, 2),
    _NvmBrgMacFilterNumber_Type()
)
nvmBrgMacFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgMacFilterNumber.setStatus("mandatory")
_NvmBrgMacAddress_Type = MacAddress
_NvmBrgMacAddress_Object = MibTableColumn
nvmBrgMacAddress = _NvmBrgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11, 1, 3),
    _NvmBrgMacAddress_Type()
)
nvmBrgMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgMacAddress.setStatus("mandatory")


class _NvmBrgMacType_Type(Integer32):
    """Custom type nvmBrgMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("invalid", 3),
          ("source", 1))
    )


_NvmBrgMacType_Type.__name__ = "Integer32"
_NvmBrgMacType_Object = MibTableColumn
nvmBrgMacType = _NvmBrgMacType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 11, 1, 4),
    _NvmBrgMacType_Type()
)
nvmBrgMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgMacType.setStatus("mandatory")
_NvmBrgEtFilterTable_Object = MibTable
nvmBrgEtFilterTable = _NvmBrgEtFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12)
)
if mibBuilder.loadTexts:
    nvmBrgEtFilterTable.setStatus("mandatory")
_NvmBrgEtFilterEntry_Object = MibTableRow
nvmBrgEtFilterEntry = _NvmBrgEtFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1)
)
nvmBrgEtFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "nvmBrgEtFilterPortIndex"),
    (0, "MICOMBRGEXT", "nvmBrgEtFilterNumber"),
)
if mibBuilder.loadTexts:
    nvmBrgEtFilterEntry.setStatus("mandatory")


class _NvmBrgEtFilterPortIndex_Type(Integer32):
    """Custom type nvmBrgEtFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmBrgEtFilterPortIndex_Type.__name__ = "Integer32"
_NvmBrgEtFilterPortIndex_Object = MibTableColumn
nvmBrgEtFilterPortIndex = _NvmBrgEtFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 1),
    _NvmBrgEtFilterPortIndex_Type()
)
nvmBrgEtFilterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterPortIndex.setStatus("mandatory")


class _NvmBrgEtFilterNumber_Type(Integer32):
    """Custom type nvmBrgEtFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmBrgEtFilterNumber_Type.__name__ = "Integer32"
_NvmBrgEtFilterNumber_Object = MibTableColumn
nvmBrgEtFilterNumber = _NvmBrgEtFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 2),
    _NvmBrgEtFilterNumber_Type()
)
nvmBrgEtFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterNumber.setStatus("mandatory")


class _NvmBrgEtFilterStatus_Type(Integer32):
    """Custom type nvmBrgEtFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("range", 2),
          ("singular", 1))
    )


_NvmBrgEtFilterStatus_Type.__name__ = "Integer32"
_NvmBrgEtFilterStatus_Object = MibTableColumn
nvmBrgEtFilterStatus = _NvmBrgEtFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 3),
    _NvmBrgEtFilterStatus_Type()
)
nvmBrgEtFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterStatus.setStatus("mandatory")


class _NvmBrgEtFilterEType_Type(Integer32):
    """Custom type nvmBrgEtFilterEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_NvmBrgEtFilterEType_Type.__name__ = "Integer32"
_NvmBrgEtFilterEType_Object = MibTableColumn
nvmBrgEtFilterEType = _NvmBrgEtFilterEType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 4),
    _NvmBrgEtFilterEType_Type()
)
nvmBrgEtFilterEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterEType.setStatus("mandatory")


class _NvmBrgEtFilterUpperRange_Type(Integer32):
    """Custom type nvmBrgEtFilterUpperRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_NvmBrgEtFilterUpperRange_Type.__name__ = "Integer32"
_NvmBrgEtFilterUpperRange_Object = MibTableColumn
nvmBrgEtFilterUpperRange = _NvmBrgEtFilterUpperRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 5),
    _NvmBrgEtFilterUpperRange_Type()
)
nvmBrgEtFilterUpperRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterUpperRange.setStatus("mandatory")


class _NvmBrgEtFilterLowerRange_Type(Integer32):
    """Custom type nvmBrgEtFilterLowerRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_NvmBrgEtFilterLowerRange_Type.__name__ = "Integer32"
_NvmBrgEtFilterLowerRange_Object = MibTableColumn
nvmBrgEtFilterLowerRange = _NvmBrgEtFilterLowerRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 12, 1, 6),
    _NvmBrgEtFilterLowerRange_Type()
)
nvmBrgEtFilterLowerRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmBrgEtFilterLowerRange.setStatus("mandatory")
_NvmBrgSapFilterTable_Object = MibTable
nvmBrgSapFilterTable = _NvmBrgSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13)
)
if mibBuilder.loadTexts:
    nvmBrgSapFilterTable.setStatus("mandatory")
_NvmBrgSapFilterEntry_Object = MibTableRow
nvmBrgSapFilterEntry = _NvmBrgSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1)
)
nvmBrgSapFilterEntry.setIndexNames(
    (0, "MICOMBRGEXT", "nvmBrgSapFilterPortIndex"),
    (0, "MICOMBRGEXT", "nvmBrgSapFilterNumber"),
)
if mibBuilder.loadTexts:
    nvmBrgSapFilterEntry.setStatus("mandatory")


class _NvmBrgSapFilterPortIndex_Type(Integer32):
    """Custom type nvmBrgSapFilterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NvmBrgSapFilterPortIndex_Type.__name__ = "Integer32"
_NvmBrgSapFilterPortIndex_Object = MibTableColumn
nvmBrgSapFilterPortIndex = _NvmBrgSapFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 1),
    _NvmBrgSapFilterPortIndex_Type()
)
nvmBrgSapFilterPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterPortIndex.setStatus("mandatory")


class _NvmBrgSapFilterNumber_Type(Integer32):
    """Custom type nvmBrgSapFilterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmBrgSapFilterNumber_Type.__name__ = "Integer32"
_NvmBrgSapFilterNumber_Object = MibTableColumn
nvmBrgSapFilterNumber = _NvmBrgSapFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 2),
    _NvmBrgSapFilterNumber_Type()
)
nvmBrgSapFilterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterNumber.setStatus("mandatory")


class _NvmBrgSapFilterStatus_Type(Integer32):
    """Custom type nvmBrgSapFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("range", 2),
          ("singular", 1))
    )


_NvmBrgSapFilterStatus_Type.__name__ = "Integer32"
_NvmBrgSapFilterStatus_Object = MibTableColumn
nvmBrgSapFilterStatus = _NvmBrgSapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 3),
    _NvmBrgSapFilterStatus_Type()
)
nvmBrgSapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterStatus.setStatus("mandatory")


class _NvmBrgSapFilterEType_Type(Integer32):
    """Custom type nvmBrgSapFilterEType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmBrgSapFilterEType_Type.__name__ = "Integer32"
_NvmBrgSapFilterEType_Object = MibTableColumn
nvmBrgSapFilterEType = _NvmBrgSapFilterEType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 4),
    _NvmBrgSapFilterEType_Type()
)
nvmBrgSapFilterEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterEType.setStatus("mandatory")


class _NvmBrgSapFilterUpperRange_Type(Integer32):
    """Custom type nvmBrgSapFilterUpperRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmBrgSapFilterUpperRange_Type.__name__ = "Integer32"
_NvmBrgSapFilterUpperRange_Object = MibTableColumn
nvmBrgSapFilterUpperRange = _NvmBrgSapFilterUpperRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 5),
    _NvmBrgSapFilterUpperRange_Type()
)
nvmBrgSapFilterUpperRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterUpperRange.setStatus("mandatory")


class _NvmBrgSapFilterLowerRange_Type(Integer32):
    """Custom type nvmBrgSapFilterLowerRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NvmBrgSapFilterLowerRange_Type.__name__ = "Integer32"
_NvmBrgSapFilterLowerRange_Object = MibTableColumn
nvmBrgSapFilterLowerRange = _NvmBrgSapFilterLowerRange_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 13, 1, 6),
    _NvmBrgSapFilterLowerRange_Type()
)
nvmBrgSapFilterLowerRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmBrgSapFilterLowerRange.setStatus("mandatory")
_McmBrgCntr_ObjectIdentity = ObjectIdentity
mcmBrgCntr = _McmBrgCntr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14)
)
_McmBrgPortCntrZeroTable_Object = MibTable
mcmBrgPortCntrZeroTable = _McmBrgPortCntrZeroTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1)
)
if mibBuilder.loadTexts:
    mcmBrgPortCntrZeroTable.setStatus("obsolete")
_McmBrgPortCntrZeroEntry_Object = MibTableRow
mcmBrgPortCntrZeroEntry = _McmBrgPortCntrZeroEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1, 1)
)
mcmBrgPortCntrZeroEntry.setIndexNames(
    (0, "MICOMBRGEXT", "mcmBrgPortCntrZeroIndex"),
)
if mibBuilder.loadTexts:
    mcmBrgPortCntrZeroEntry.setStatus("obsolete")


class _McmBrgPortCntrZeroIndex_Type(Integer32):
    """Custom type mcmBrgPortCntrZeroIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmBrgPortCntrZeroIndex_Type.__name__ = "Integer32"
_McmBrgPortCntrZeroIndex_Object = MibTableColumn
mcmBrgPortCntrZeroIndex = _McmBrgPortCntrZeroIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1, 1, 1),
    _McmBrgPortCntrZeroIndex_Type()
)
mcmBrgPortCntrZeroIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmBrgPortCntrZeroIndex.setStatus("obsolete")


class _McmBrgBasePortCounterZero_Type(Integer32):
    """Custom type mcmBrgBasePortCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmBrgBasePortCounterZero_Type.__name__ = "Integer32"
_McmBrgBasePortCounterZero_Object = MibTableColumn
mcmBrgBasePortCounterZero = _McmBrgBasePortCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1, 1, 2),
    _McmBrgBasePortCounterZero_Type()
)
mcmBrgBasePortCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmBrgBasePortCounterZero.setStatus("obsolete")


class _McmBrgStpPortCounterZero_Type(Integer32):
    """Custom type mcmBrgStpPortCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmBrgStpPortCounterZero_Type.__name__ = "Integer32"
_McmBrgStpPortCounterZero_Object = MibTableColumn
mcmBrgStpPortCounterZero = _McmBrgStpPortCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1, 1, 3),
    _McmBrgStpPortCounterZero_Type()
)
mcmBrgStpPortCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmBrgStpPortCounterZero.setStatus("obsolete")


class _McmBrgTpPortCounterZero_Type(Integer32):
    """Custom type mcmBrgTpPortCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmBrgTpPortCounterZero_Type.__name__ = "Integer32"
_McmBrgTpPortCounterZero_Object = MibTableColumn
mcmBrgTpPortCounterZero = _McmBrgTpPortCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 1, 1, 4),
    _McmBrgTpPortCounterZero_Type()
)
mcmBrgTpPortCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmBrgTpPortCounterZero.setStatus("obsolete")
_McmBrgCounterZero_ObjectIdentity = ObjectIdentity
mcmBrgCounterZero = _McmBrgCounterZero_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 2)
)


class _McmBrgStpCounterZero_Type(Integer32):
    """Custom type mcmBrgStpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmBrgStpCounterZero_Type.__name__ = "Integer32"
_McmBrgStpCounterZero_Object = MibScalar
mcmBrgStpCounterZero = _McmBrgStpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 2, 1),
    _McmBrgStpCounterZero_Type()
)
mcmBrgStpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmBrgStpCounterZero.setStatus("obsolete")


class _McmBrgTpCounterZero_Type(Integer32):
    """Custom type mcmBrgTpCounterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmBrgTpCounterZero_Type.__name__ = "Integer32"
_McmBrgTpCounterZero_Object = MibScalar
mcmBrgTpCounterZero = _McmBrgTpCounterZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 6, 14, 2, 2),
    _McmBrgTpCounterZero_Type()
)
mcmBrgTpCounterZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmBrgTpCounterZero.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOMBRGEXT",
    **{"MacAddress": MacAddress,
       "Timeout": Timeout,
       "mcmBrg": mcmBrg,
       "mcmBrgGlobalParamGroup": mcmBrgGlobalParamGroup,
       "mcmBrgIPBridged": mcmBrgIPBridged,
       "mcmBrgNumInterfaces": mcmBrgNumInterfaces,
       "mcmBrgSpanEnable": mcmBrgSpanEnable,
       "mcmBrgSpoofEnable": mcmBrgSpoofEnable,
       "mcmBrgAgeTime": mcmBrgAgeTime,
       "mcmBrgMiscParamGroup": mcmBrgMiscParamGroup,
       "mcmBrgDebugEnable": mcmBrgDebugEnable,
       "mcmBrgSpanDebugEnable": mcmBrgSpanDebugEnable,
       "mcmBrgSpoofCacheAge": mcmBrgSpoofCacheAge,
       "mcmBrgSpoofThresholdAge": mcmBrgSpoofThresholdAge,
       "mcmBrgSpoofThresholdCount": mcmBrgSpoofThresholdCount,
       "mcmBrgConfPortTable": mcmBrgConfPortTable,
       "mcmBrgConfPortEntry": mcmBrgConfPortEntry,
       "mcmBrgConfPortIndex": mcmBrgConfPortIndex,
       "mcmBrgConfPortPPA": mcmBrgConfPortPPA,
       "mcmBrgConfPortType": mcmBrgConfPortType,
       "mcmBrgConfPortMacFilterFlag": mcmBrgConfPortMacFilterFlag,
       "mcmBrgConfPortEtFilterFlag": mcmBrgConfPortEtFilterFlag,
       "mcmBrgConfPortSapFilterFlag": mcmBrgConfPortSapFilterFlag,
       "mcmBrgConfPortMacInclExcl": mcmBrgConfPortMacInclExcl,
       "mcmBrgConfPortEtInclExcl": mcmBrgConfPortEtInclExcl,
       "mcmBrgConfPortSapInclExcl": mcmBrgConfPortSapInclExcl,
       "mcmBrgMacFilterTable": mcmBrgMacFilterTable,
       "mcmBrgMacFilterEntry": mcmBrgMacFilterEntry,
       "mcmBrgMacFilterPortIndex": mcmBrgMacFilterPortIndex,
       "mcmBrgMacFilterNumber": mcmBrgMacFilterNumber,
       "mcmBrgMacAddress": mcmBrgMacAddress,
       "mcmBrgMacType": mcmBrgMacType,
       "mcmBrgEtFilterTable": mcmBrgEtFilterTable,
       "mcmBrgEtFilterEntry": mcmBrgEtFilterEntry,
       "mcmBrgEtFilterPortIndex": mcmBrgEtFilterPortIndex,
       "mcmBrgEtFilterNumber": mcmBrgEtFilterNumber,
       "mcmBrgEtFilterStatus": mcmBrgEtFilterStatus,
       "mcmBrgEtFilterEType": mcmBrgEtFilterEType,
       "mcmBrgEtFilterUpperRange": mcmBrgEtFilterUpperRange,
       "mcmBrgEtFilterLowerRange": mcmBrgEtFilterLowerRange,
       "mcmBrgSapFilterTable": mcmBrgSapFilterTable,
       "mcmBrgSapFilterEntry": mcmBrgSapFilterEntry,
       "mcmBrgSapFilterPortIndex": mcmBrgSapFilterPortIndex,
       "mcmBrgSapFilterNumber": mcmBrgSapFilterNumber,
       "mcmBrgSapFilterStatus": mcmBrgSapFilterStatus,
       "mcmBrgSapFilterEType": mcmBrgSapFilterEType,
       "mcmBrgSapFilterUpperRange": mcmBrgSapFilterUpperRange,
       "mcmBrgSapFilterLowerRange": mcmBrgSapFilterLowerRange,
       "nvmBrgGlobalParamGroup": nvmBrgGlobalParamGroup,
       "nvmBrgIPBridged": nvmBrgIPBridged,
       "nvmBrgNumInterfaces": nvmBrgNumInterfaces,
       "nvmBrgSpanEnable": nvmBrgSpanEnable,
       "nvmBrgSpoofEnable": nvmBrgSpoofEnable,
       "nvmBrgAgeTime": nvmBrgAgeTime,
       "nvmBrgMiscParamGroup": nvmBrgMiscParamGroup,
       "nvmBrgDebugEnable": nvmBrgDebugEnable,
       "nvmBrgSpanDebugEnable": nvmBrgSpanDebugEnable,
       "nvmBrgSpoofCacheAge": nvmBrgSpoofCacheAge,
       "nvmBrgSpoofThresholdAge": nvmBrgSpoofThresholdAge,
       "nvmBrgSpoofThresholdCount": nvmBrgSpoofThresholdCount,
       "nvmBrgStpParamGroup": nvmBrgStpParamGroup,
       "nvmBrgPriority": nvmBrgPriority,
       "nvmBrgMaxAge": nvmBrgMaxAge,
       "nvmBrgFwdDelay": nvmBrgFwdDelay,
       "nvmBrgHelloTime": nvmBrgHelloTime,
       "nvmBrgConfPortTable": nvmBrgConfPortTable,
       "nvmBrgConfPortEntry": nvmBrgConfPortEntry,
       "nvmBrgConfPortIndex": nvmBrgConfPortIndex,
       "nvmBrgConfPortType": nvmBrgConfPortType,
       "nvmBrgConfPortEnable": nvmBrgConfPortEnable,
       "nvmBrgConfPortPriority": nvmBrgConfPortPriority,
       "nvmBrgConfPortPathCost": nvmBrgConfPortPathCost,
       "nvmBrgConfPortMacFilterFlag": nvmBrgConfPortMacFilterFlag,
       "nvmBrgConfPortEtFilterFlag": nvmBrgConfPortEtFilterFlag,
       "nvmBrgConfPortSapFilterFlag": nvmBrgConfPortSapFilterFlag,
       "nvmBrgConfPortMacInclExcl": nvmBrgConfPortMacInclExcl,
       "nvmBrgConfPortEtInclExcl": nvmBrgConfPortEtInclExcl,
       "nvmBrgConfPortSapInclExcl": nvmBrgConfPortSapInclExcl,
       "nvmBrgMacFilterTable": nvmBrgMacFilterTable,
       "nvmBrgMacFilterEntry": nvmBrgMacFilterEntry,
       "nvmBrgMacFilterPortIndex": nvmBrgMacFilterPortIndex,
       "nvmBrgMacFilterNumber": nvmBrgMacFilterNumber,
       "nvmBrgMacAddress": nvmBrgMacAddress,
       "nvmBrgMacType": nvmBrgMacType,
       "nvmBrgEtFilterTable": nvmBrgEtFilterTable,
       "nvmBrgEtFilterEntry": nvmBrgEtFilterEntry,
       "nvmBrgEtFilterPortIndex": nvmBrgEtFilterPortIndex,
       "nvmBrgEtFilterNumber": nvmBrgEtFilterNumber,
       "nvmBrgEtFilterStatus": nvmBrgEtFilterStatus,
       "nvmBrgEtFilterEType": nvmBrgEtFilterEType,
       "nvmBrgEtFilterUpperRange": nvmBrgEtFilterUpperRange,
       "nvmBrgEtFilterLowerRange": nvmBrgEtFilterLowerRange,
       "nvmBrgSapFilterTable": nvmBrgSapFilterTable,
       "nvmBrgSapFilterEntry": nvmBrgSapFilterEntry,
       "nvmBrgSapFilterPortIndex": nvmBrgSapFilterPortIndex,
       "nvmBrgSapFilterNumber": nvmBrgSapFilterNumber,
       "nvmBrgSapFilterStatus": nvmBrgSapFilterStatus,
       "nvmBrgSapFilterEType": nvmBrgSapFilterEType,
       "nvmBrgSapFilterUpperRange": nvmBrgSapFilterUpperRange,
       "nvmBrgSapFilterLowerRange": nvmBrgSapFilterLowerRange,
       "mcmBrgCntr": mcmBrgCntr,
       "mcmBrgPortCntrZeroTable": mcmBrgPortCntrZeroTable,
       "mcmBrgPortCntrZeroEntry": mcmBrgPortCntrZeroEntry,
       "mcmBrgPortCntrZeroIndex": mcmBrgPortCntrZeroIndex,
       "mcmBrgBasePortCounterZero": mcmBrgBasePortCounterZero,
       "mcmBrgStpPortCounterZero": mcmBrgStpPortCounterZero,
       "mcmBrgTpPortCounterZero": mcmBrgTpPortCounterZero,
       "mcmBrgCounterZero": mcmBrgCounterZero,
       "mcmBrgStpCounterZero": mcmBrgStpCounterZero,
       "mcmBrgTpCounterZero": mcmBrgTpCounterZero}
)
