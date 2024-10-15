# SNMP MIB module (ROUTER-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROUTER-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:18 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





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
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTRouterGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTRouterGroup = _Cdx6500PCTRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5)
)
_Cdx6500PCTRarpCacheTable_Object = MibTable
cdx6500PCTRarpCacheTable = _Cdx6500PCTRarpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheTable.setStatus("mandatory")
_Cdx6500PCTRarpCacheEntry_Object = MibTableRow
cdx6500PCTRarpCacheEntry = _Cdx6500PCTRarpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1)
)
cdx6500PCTRarpCacheEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRarpCacheIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheEntry.setStatus("mandatory")


class _Cdx6500PCTRarpCacheIndex_Type(Integer32):
    """Custom type cdx6500PCTRarpCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRarpCacheIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRarpCacheIndex_Object = MibTableColumn
cdx6500PCTRarpCacheIndex = _Cdx6500PCTRarpCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1, 1),
    _Cdx6500PCTRarpCacheIndex_Type()
)
cdx6500PCTRarpCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheIndex.setStatus("mandatory")


class _Cdx6500PCTRarpCacheIfNum_Type(Integer32):
    """Custom type cdx6500PCTRarpCacheIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36),
    )


_Cdx6500PCTRarpCacheIfNum_Type.__name__ = "Integer32"
_Cdx6500PCTRarpCacheIfNum_Object = MibTableColumn
cdx6500PCTRarpCacheIfNum = _Cdx6500PCTRarpCacheIfNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1, 2),
    _Cdx6500PCTRarpCacheIfNum_Type()
)
cdx6500PCTRarpCacheIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheIfNum.setStatus("mandatory")


class _Cdx6500PCTRarpCacheProtocol_Type(Integer32):
    """Custom type cdx6500PCTRarpCacheProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7,
              22,
              50)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 22),
          ("ip", 0),
          ("ipx", 7),
          ("newvalIp", 50))
    )


_Cdx6500PCTRarpCacheProtocol_Type.__name__ = "Integer32"
_Cdx6500PCTRarpCacheProtocol_Object = MibTableColumn
cdx6500PCTRarpCacheProtocol = _Cdx6500PCTRarpCacheProtocol_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1, 3),
    _Cdx6500PCTRarpCacheProtocol_Type()
)
cdx6500PCTRarpCacheProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheProtocol.setStatus("mandatory")
_Cdx6500PCTRarpCacheProtocolAd_Type = IpAddress
_Cdx6500PCTRarpCacheProtocolAd_Object = MibTableColumn
cdx6500PCTRarpCacheProtocolAd = _Cdx6500PCTRarpCacheProtocolAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1, 4),
    _Cdx6500PCTRarpCacheProtocolAd_Type()
)
cdx6500PCTRarpCacheProtocolAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheProtocolAd.setStatus("mandatory")
_Cdx6500PCTRarpCacheMacAd_Type = MacAddress
_Cdx6500PCTRarpCacheMacAd_Object = MibTableColumn
cdx6500PCTRarpCacheMacAd = _Cdx6500PCTRarpCacheMacAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 1, 1, 5),
    _Cdx6500PCTRarpCacheMacAd_Type()
)
cdx6500PCTRarpCacheMacAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpCacheMacAd.setStatus("mandatory")


class _Cdx6500PCTRarpParamAutoRef_Type(Integer32):
    """Custom type cdx6500PCTRarpParamAutoRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRarpParamAutoRef_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamAutoRef_Object = MibScalar
cdx6500PCTRarpParamAutoRef = _Cdx6500PCTRarpParamAutoRef_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 2),
    _Cdx6500PCTRarpParamAutoRef_Type()
)
cdx6500PCTRarpParamAutoRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamAutoRef.setStatus("mandatory")


class _Cdx6500PCTRarpParamRefTime_Type(Integer32):
    """Custom type cdx6500PCTRarpParamRefTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRarpParamRefTime_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamRefTime_Object = MibScalar
cdx6500PCTRarpParamRefTime = _Cdx6500PCTRarpParamRefTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 3),
    _Cdx6500PCTRarpParamRefTime_Type()
)
cdx6500PCTRarpParamRefTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamRefTime.setStatus("mandatory")


class _Cdx6500PCTRarpParamUseTime_Type(Integer32):
    """Custom type cdx6500PCTRarpParamUseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRarpParamUseTime_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamUseTime_Object = MibScalar
cdx6500PCTRarpParamUseTime = _Cdx6500PCTRarpParamUseTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 4),
    _Cdx6500PCTRarpParamUseTime_Type()
)
cdx6500PCTRarpParamUseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamUseTime.setStatus("mandatory")


class _Cdx6500PCTRarpParamProxy_Type(Integer32):
    """Custom type cdx6500PCTRarpParamProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRarpParamProxy_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamProxy_Object = MibScalar
cdx6500PCTRarpParamProxy = _Cdx6500PCTRarpParamProxy_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 5),
    _Cdx6500PCTRarpParamProxy_Type()
)
cdx6500PCTRarpParamProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamProxy.setStatus("mandatory")


class _Cdx6500PCTRarpParamProxySub_Type(Integer32):
    """Custom type cdx6500PCTRarpParamProxySub based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRarpParamProxySub_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamProxySub_Object = MibScalar
cdx6500PCTRarpParamProxySub = _Cdx6500PCTRarpParamProxySub_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 6),
    _Cdx6500PCTRarpParamProxySub_Type()
)
cdx6500PCTRarpParamProxySub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamProxySub.setStatus("mandatory")
_Cdx6500PCTRaccControlTable_Object = MibTable
cdx6500PCTRaccControlTable = _Cdx6500PCTRaccControlTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlTable.setStatus("mandatory")
_Cdx6500PCTRaccControlEntry_Object = MibTableRow
cdx6500PCTRaccControlEntry = _Cdx6500PCTRaccControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1)
)
cdx6500PCTRaccControlEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRaccControlIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlEntry.setStatus("mandatory")


class _Cdx6500PCTRaccControlIndex_Type(Integer32):
    """Custom type cdx6500PCTRaccControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRaccControlIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlIndex_Object = MibTableColumn
cdx6500PCTRaccControlIndex = _Cdx6500PCTRaccControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 1),
    _Cdx6500PCTRaccControlIndex_Type()
)
cdx6500PCTRaccControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlIndex.setStatus("mandatory")


class _Cdx6500PCTRaccControlType_Type(Integer32):
    """Custom type cdx6500PCTRaccControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 0),
          ("included", 1),
          ("newvalExcluded", 50))
    )


_Cdx6500PCTRaccControlType_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlType_Object = MibTableColumn
cdx6500PCTRaccControlType = _Cdx6500PCTRaccControlType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 2),
    _Cdx6500PCTRaccControlType_Type()
)
cdx6500PCTRaccControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlType.setStatus("mandatory")
_Cdx6500PCTRaccControlSrcAd_Type = IpAddress
_Cdx6500PCTRaccControlSrcAd_Object = MibTableColumn
cdx6500PCTRaccControlSrcAd = _Cdx6500PCTRaccControlSrcAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 3),
    _Cdx6500PCTRaccControlSrcAd_Type()
)
cdx6500PCTRaccControlSrcAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlSrcAd.setStatus("mandatory")
_Cdx6500PCTRaccControlSrcMask_Type = IpAddress
_Cdx6500PCTRaccControlSrcMask_Object = MibTableColumn
cdx6500PCTRaccControlSrcMask = _Cdx6500PCTRaccControlSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 4),
    _Cdx6500PCTRaccControlSrcMask_Type()
)
cdx6500PCTRaccControlSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlSrcMask.setStatus("mandatory")
_Cdx6500PCTRaccControlDstAd_Type = IpAddress
_Cdx6500PCTRaccControlDstAd_Object = MibTableColumn
cdx6500PCTRaccControlDstAd = _Cdx6500PCTRaccControlDstAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 5),
    _Cdx6500PCTRaccControlDstAd_Type()
)
cdx6500PCTRaccControlDstAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlDstAd.setStatus("mandatory")
_Cdx6500PCTRaccControlDstMask_Type = IpAddress
_Cdx6500PCTRaccControlDstMask_Object = MibTableColumn
cdx6500PCTRaccControlDstMask = _Cdx6500PCTRaccControlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 6),
    _Cdx6500PCTRaccControlDstMask_Type()
)
cdx6500PCTRaccControlDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlDstMask.setStatus("mandatory")


class _Cdx6500PCTRaccControlFstProt_Type(Integer32):
    """Custom type cdx6500PCTRaccControlFstProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlFstProt_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlFstProt_Object = MibTableColumn
cdx6500PCTRaccControlFstProt = _Cdx6500PCTRaccControlFstProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 7),
    _Cdx6500PCTRaccControlFstProt_Type()
)
cdx6500PCTRaccControlFstProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlFstProt.setStatus("mandatory")


class _Cdx6500PCTRaccControlLstProt_Type(Integer32):
    """Custom type cdx6500PCTRaccControlLstProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlLstProt_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlLstProt_Object = MibTableColumn
cdx6500PCTRaccControlLstProt = _Cdx6500PCTRaccControlLstProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 8),
    _Cdx6500PCTRaccControlLstProt_Type()
)
cdx6500PCTRaccControlLstProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlLstProt.setStatus("mandatory")


class _Cdx6500PCTRaccControlFstPort_Type(Integer32):
    """Custom type cdx6500PCTRaccControlFstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRaccControlFstPort_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlFstPort_Object = MibTableColumn
cdx6500PCTRaccControlFstPort = _Cdx6500PCTRaccControlFstPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 9),
    _Cdx6500PCTRaccControlFstPort_Type()
)
cdx6500PCTRaccControlFstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlFstPort.setStatus("deprecated")


class _Cdx6500PCTRaccControlLstPort_Type(Integer32):
    """Custom type cdx6500PCTRaccControlLstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRaccControlLstPort_Type.__name__ = "Integer32"
_Cdx6500PCTRaccControlLstPort_Object = MibTableColumn
cdx6500PCTRaccControlLstPort = _Cdx6500PCTRaccControlLstPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 10),
    _Cdx6500PCTRaccControlLstPort_Type()
)
cdx6500PCTRaccControlLstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlLstPort.setStatus("deprecated")


class _Cdx6500PCTRaccControlSrcPort_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlSrcPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlSrcPort_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlSrcPort_Object = MibTableColumn
cdx6500PCTRaccControlSrcPort = _Cdx6500PCTRaccControlSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 11),
    _Cdx6500PCTRaccControlSrcPort_Type()
)
cdx6500PCTRaccControlSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlSrcPort.setStatus("mandatory")


class _Cdx6500PCTRaccControlDstPort_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlDstPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlDstPort_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlDstPort_Object = MibTableColumn
cdx6500PCTRaccControlDstPort = _Cdx6500PCTRaccControlDstPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 12),
    _Cdx6500PCTRaccControlDstPort_Type()
)
cdx6500PCTRaccControlDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlDstPort.setStatus("mandatory")


class _Cdx6500PCTRaccControlInIniface_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlInIniface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlInIniface_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlInIniface_Object = MibTableColumn
cdx6500PCTRaccControlInIniface = _Cdx6500PCTRaccControlInIniface_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 13),
    _Cdx6500PCTRaccControlInIniface_Type()
)
cdx6500PCTRaccControlInIniface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlInIniface.setStatus("mandatory")


class _Cdx6500PCTRaccControlOutIniface_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlOutIniface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlOutIniface_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlOutIniface_Object = MibTableColumn
cdx6500PCTRaccControlOutIniface = _Cdx6500PCTRaccControlOutIniface_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 14),
    _Cdx6500PCTRaccControlOutIniface_Type()
)
cdx6500PCTRaccControlOutIniface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlOutIniface.setStatus("mandatory")


class _Cdx6500PCTRaccControlInLcon_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlInLcon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlInLcon_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlInLcon_Object = MibTableColumn
cdx6500PCTRaccControlInLcon = _Cdx6500PCTRaccControlInLcon_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 15),
    _Cdx6500PCTRaccControlInLcon_Type()
)
cdx6500PCTRaccControlInLcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlInLcon.setStatus("mandatory")


class _Cdx6500PCTRaccControlOutLcon_Type(DisplayString):
    """Custom type cdx6500PCTRaccControlOutLcon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRaccControlOutLcon_Type.__name__ = "DisplayString"
_Cdx6500PCTRaccControlOutLcon_Object = MibTableColumn
cdx6500PCTRaccControlOutLcon = _Cdx6500PCTRaccControlOutLcon_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 7, 1, 16),
    _Cdx6500PCTRaccControlOutLcon_Type()
)
cdx6500PCTRaccControlOutLcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRaccControlOutLcon.setStatus("mandatory")
_Cdx6500PCTRAcceptRIPRouteTable_Object = MibTable
cdx6500PCTRAcceptRIPRouteTable = _Cdx6500PCTRAcceptRIPRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    cdx6500PCTRAcceptRIPRouteTable.setStatus("obsolete")
_Cdx6500PCTRAcceptRIPRouteEntry_Object = MibTableRow
cdx6500PCTRAcceptRIPRouteEntry = _Cdx6500PCTRAcceptRIPRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 8, 1)
)
cdx6500PCTRAcceptRIPRouteEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRAcceptRIPRouteIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRAcceptRIPRouteEntry.setStatus("obsolete")


class _Cdx6500PCTRAcceptRIPRouteIndex_Type(Integer32):
    """Custom type cdx6500PCTRAcceptRIPRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRAcceptRIPRouteIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRAcceptRIPRouteIndex_Object = MibTableColumn
cdx6500PCTRAcceptRIPRouteIndex = _Cdx6500PCTRAcceptRIPRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 8, 1, 1),
    _Cdx6500PCTRAcceptRIPRouteIndex_Type()
)
cdx6500PCTRAcceptRIPRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500PCTRAcceptRIPRouteIndex.setStatus("obsolete")
_Cdx6500PCTRAcceptRIPRouteIpNet_Type = IpAddress
_Cdx6500PCTRAcceptRIPRouteIpNet_Object = MibTableColumn
cdx6500PCTRAcceptRIPRouteIpNet = _Cdx6500PCTRAcceptRIPRouteIpNet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 8, 1, 2),
    _Cdx6500PCTRAcceptRIPRouteIpNet_Type()
)
cdx6500PCTRAcceptRIPRouteIpNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdx6500PCTRAcceptRIPRouteIpNet.setStatus("obsolete")
_Cdx6500PCTRifConfTable_Object = MibTable
cdx6500PCTRifConfTable = _Cdx6500PCTRifConfTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    cdx6500PCTRifConfTable.setStatus("mandatory")
_Cdx6500PCTRifConfEntry_Object = MibTableRow
cdx6500PCTRifConfEntry = _Cdx6500PCTRifConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1)
)
cdx6500PCTRifConfEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRifConfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRifConfEntry.setStatus("mandatory")


class _Cdx6500PCTRifConfIndex_Type(Integer32):
    """Custom type cdx6500PCTRifConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRifConfIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfIndex_Object = MibTableColumn
cdx6500PCTRifConfIndex = _Cdx6500PCTRifConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 1),
    _Cdx6500PCTRifConfIndex_Type()
)
cdx6500PCTRifConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfIndex.setStatus("mandatory")


class _Cdx6500PCTRifConfIfNum_Type(Integer32):
    """Custom type cdx6500PCTRifConfIfNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRifConfIfNum_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfIfNum_Object = MibTableColumn
cdx6500PCTRifConfIfNum = _Cdx6500PCTRifConfIfNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 2),
    _Cdx6500PCTRifConfIfNum_Type()
)
cdx6500PCTRifConfIfNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfIfNum.setStatus("mandatory")
_Cdx6500PCTRifConfIpAd_Type = IpAddress
_Cdx6500PCTRifConfIpAd_Object = MibTableColumn
cdx6500PCTRifConfIpAd = _Cdx6500PCTRifConfIpAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 3),
    _Cdx6500PCTRifConfIpAd_Type()
)
cdx6500PCTRifConfIpAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfIpAd.setStatus("mandatory")
_Cdx6500PCTRifConfAdMask_Type = IpAddress
_Cdx6500PCTRifConfAdMask_Object = MibTableColumn
cdx6500PCTRifConfAdMask = _Cdx6500PCTRifConfAdMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 4),
    _Cdx6500PCTRifConfAdMask_Type()
)
cdx6500PCTRifConfAdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfAdMask.setStatus("mandatory")


class _Cdx6500PCTRifConfOvrDefRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfOvrDefRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfOvrDefRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfOvrDefRoute_Object = MibTableColumn
cdx6500PCTRifConfOvrDefRoute = _Cdx6500PCTRifConfOvrDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 5),
    _Cdx6500PCTRifConfOvrDefRoute_Type()
)
cdx6500PCTRifConfOvrDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfOvrDefRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfOvrStatRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfOvrStatRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfOvrStatRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfOvrStatRoute_Object = MibTableColumn
cdx6500PCTRifConfOvrStatRoute = _Cdx6500PCTRifConfOvrStatRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 6),
    _Cdx6500PCTRifConfOvrStatRoute_Type()
)
cdx6500PCTRifConfOvrStatRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfOvrStatRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfSndgDefRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfSndgDefRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSndgDefRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSndgDefRoute_Object = MibTableColumn
cdx6500PCTRifConfSndgDefRoute = _Cdx6500PCTRifConfSndgDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 7),
    _Cdx6500PCTRifConfSndgDefRoute_Type()
)
cdx6500PCTRifConfSndgDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSndgDefRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfSndgNetRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfSndgNetRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSndgNetRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSndgNetRoute_Object = MibTableColumn
cdx6500PCTRifConfSndgNetRoute = _Cdx6500PCTRifConfSndgNetRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 8),
    _Cdx6500PCTRifConfSndgNetRoute_Type()
)
cdx6500PCTRifConfSndgNetRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSndgNetRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfSndgSubRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfSndgSubRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSndgSubRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSndgSubRoute_Object = MibTableColumn
cdx6500PCTRifConfSndgSubRoute = _Cdx6500PCTRifConfSndgSubRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 9),
    _Cdx6500PCTRifConfSndgSubRoute_Type()
)
cdx6500PCTRifConfSndgSubRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSndgSubRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfSndgStatRoute_Type(Integer32):
    """Custom type cdx6500PCTRifConfSndgStatRoute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSndgStatRoute_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSndgStatRoute_Object = MibTableColumn
cdx6500PCTRifConfSndgStatRoute = _Cdx6500PCTRifConfSndgStatRoute_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 10),
    _Cdx6500PCTRifConfSndgStatRoute_Type()
)
cdx6500PCTRifConfSndgStatRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSndgStatRoute.setStatus("mandatory")


class _Cdx6500PCTRifConfRcvgRipPkts_Type(Integer32):
    """Custom type cdx6500PCTRifConfRcvgRipPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfRcvgRipPkts_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfRcvgRipPkts_Object = MibTableColumn
cdx6500PCTRifConfRcvgRipPkts = _Cdx6500PCTRifConfRcvgRipPkts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 11),
    _Cdx6500PCTRifConfRcvgRipPkts_Type()
)
cdx6500PCTRifConfRcvgRipPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfRcvgRipPkts.setStatus("mandatory")


class _Cdx6500PCTRifConfRcvgDynNets_Type(Integer32):
    """Custom type cdx6500PCTRifConfRcvgDynNets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfRcvgDynNets_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfRcvgDynNets_Object = MibTableColumn
cdx6500PCTRifConfRcvgDynNets = _Cdx6500PCTRifConfRcvgDynNets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 12),
    _Cdx6500PCTRifConfRcvgDynNets_Type()
)
cdx6500PCTRifConfRcvgDynNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfRcvgDynNets.setStatus("mandatory")


class _Cdx6500PCTRifConfRcvgDynSubs_Type(Integer32):
    """Custom type cdx6500PCTRifConfRcvgDynSubs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfRcvgDynSubs_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfRcvgDynSubs_Object = MibTableColumn
cdx6500PCTRifConfRcvgDynSubs = _Cdx6500PCTRifConfRcvgDynSubs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 13),
    _Cdx6500PCTRifConfRcvgDynSubs_Type()
)
cdx6500PCTRifConfRcvgDynSubs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfRcvgDynSubs.setStatus("mandatory")


class _Cdx6500PCTRifConfTagAsNum_Type(Integer32):
    """Custom type cdx6500PCTRifConfTagAsNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRifConfTagAsNum_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfTagAsNum_Object = MibTableColumn
cdx6500PCTRifConfTagAsNum = _Cdx6500PCTRifConfTagAsNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 14),
    _Cdx6500PCTRifConfTagAsNum_Type()
)
cdx6500PCTRifConfTagAsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfTagAsNum.setStatus("mandatory")


class _Cdx6500PCTRifConfBcastStyle_Type(Integer32):
    """Custom type cdx6500PCTRifConfBcastStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 0),
          ("newvalNetwork", 50))
    )


_Cdx6500PCTRifConfBcastStyle_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfBcastStyle_Object = MibTableColumn
cdx6500PCTRifConfBcastStyle = _Cdx6500PCTRifConfBcastStyle_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 15),
    _Cdx6500PCTRifConfBcastStyle_Type()
)
cdx6500PCTRifConfBcastStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfBcastStyle.setStatus("mandatory")


class _Cdx6500PCTRifConfBcastFill_Type(Integer32):
    """Custom type cdx6500PCTRifConfBcastFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500PCTRifConfBcastFill_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfBcastFill_Object = MibTableColumn
cdx6500PCTRifConfBcastFill = _Cdx6500PCTRifConfBcastFill_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 16),
    _Cdx6500PCTRifConfBcastFill_Type()
)
cdx6500PCTRifConfBcastFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfBcastFill.setStatus("mandatory")


class _Cdx6500PCTRifMaxIpMTUSize_Type(Integer32):
    """Custom type cdx6500PCTRifMaxIpMTUSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_Cdx6500PCTRifMaxIpMTUSize_Type.__name__ = "Integer32"
_Cdx6500PCTRifMaxIpMTUSize_Object = MibTableColumn
cdx6500PCTRifMaxIpMTUSize = _Cdx6500PCTRifMaxIpMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 17),
    _Cdx6500PCTRifMaxIpMTUSize_Type()
)
cdx6500PCTRifMaxIpMTUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifMaxIpMTUSize.setStatus("mandatory")


class _Cdx6500PCTRifConfSplitHorizon_Type(Integer32):
    """Custom type cdx6500PCTRifConfSplitHorizon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSplitHorizon_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSplitHorizon_Object = MibTableColumn
cdx6500PCTRifConfSplitHorizon = _Cdx6500PCTRifConfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 18),
    _Cdx6500PCTRifConfSplitHorizon_Type()
)
cdx6500PCTRifConfSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSplitHorizon.setStatus("mandatory")


class _Cdx6500PCTRifConfSr_Type(Integer32):
    """Custom type cdx6500PCTRifConfSr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRifConfSr_Type.__name__ = "Integer32"
_Cdx6500PCTRifConfSr_Object = MibTableColumn
cdx6500PCTRifConfSr = _Cdx6500PCTRifConfSr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 19),
    _Cdx6500PCTRifConfSr_Type()
)
cdx6500PCTRifConfSr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifConfSr.setStatus("mandatory")


class _Cdx6500PCTRifRipMetric_Type(Integer32):
    """Custom type cdx6500PCTRifRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cdx6500PCTRifRipMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRifRipMetric_Object = MibTableColumn
cdx6500PCTRifRipMetric = _Cdx6500PCTRifRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 20),
    _Cdx6500PCTRifRipMetric_Type()
)
cdx6500PCTRifRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifRipMetric.setStatus("mandatory")


class _Cdx6500PCTRifSendRipVer_Type(DisplayString):
    """Custom type cdx6500PCTRifSendRipVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_Cdx6500PCTRifSendRipVer_Type.__name__ = "DisplayString"
_Cdx6500PCTRifSendRipVer_Object = MibTableColumn
cdx6500PCTRifSendRipVer = _Cdx6500PCTRifSendRipVer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 21),
    _Cdx6500PCTRifSendRipVer_Type()
)
cdx6500PCTRifSendRipVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifSendRipVer.setStatus("mandatory")


class _Cdx6500PCTRifSendAggRoutes_Type(Integer32):
    """Custom type cdx6500PCTRifSendAggRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRifSendAggRoutes_Type.__name__ = "Integer32"
_Cdx6500PCTRifSendAggRoutes_Object = MibTableColumn
cdx6500PCTRifSendAggRoutes = _Cdx6500PCTRifSendAggRoutes_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 22),
    _Cdx6500PCTRifSendAggRoutes_Type()
)
cdx6500PCTRifSendAggRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifSendAggRoutes.setStatus("mandatory")


class _Cdx6500PCTRifAuthType_Type(Integer32):
    """Custom type cdx6500PCTRifAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple", 2))
    )


_Cdx6500PCTRifAuthType_Type.__name__ = "Integer32"
_Cdx6500PCTRifAuthType_Object = MibTableColumn
cdx6500PCTRifAuthType = _Cdx6500PCTRifAuthType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 23),
    _Cdx6500PCTRifAuthType_Type()
)
cdx6500PCTRifAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifAuthType.setStatus("mandatory")


class _Cdx6500PCTRifAuthKey_Type(DisplayString):
    """Custom type cdx6500PCTRifAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500PCTRifAuthKey_Type.__name__ = "DisplayString"
_Cdx6500PCTRifAuthKey_Object = MibTableColumn
cdx6500PCTRifAuthKey = _Cdx6500PCTRifAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 24),
    _Cdx6500PCTRifAuthKey_Type()
)
cdx6500PCTRifAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifAuthKey.setStatus("mandatory")


class _Cdx6500PCTRifOnDemandRip_Type(Integer32):
    """Custom type cdx6500PCTRifOnDemandRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRifOnDemandRip_Type.__name__ = "Integer32"
_Cdx6500PCTRifOnDemandRip_Object = MibTableColumn
cdx6500PCTRifOnDemandRip = _Cdx6500PCTRifOnDemandRip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 25),
    _Cdx6500PCTRifOnDemandRip_Type()
)
cdx6500PCTRifOnDemandRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifOnDemandRip.setStatus("mandatory")


class _Cdx6500PCTRifTrigUpdate_Type(Integer32):
    """Custom type cdx6500PCTRifTrigUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("change", 2),
          ("full", 3),
          ("none", 1))
    )


_Cdx6500PCTRifTrigUpdate_Type.__name__ = "Integer32"
_Cdx6500PCTRifTrigUpdate_Object = MibTableColumn
cdx6500PCTRifTrigUpdate = _Cdx6500PCTRifTrigUpdate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 26),
    _Cdx6500PCTRifTrigUpdate_Type()
)
cdx6500PCTRifTrigUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifTrigUpdate.setStatus("mandatory")


class _Cdx6500PCTRifSecPrdBcastIntv_Type(Integer32):
    """Custom type cdx6500PCTRifSecPrdBcastIntv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 65529),
    )


_Cdx6500PCTRifSecPrdBcastIntv_Type.__name__ = "Integer32"
_Cdx6500PCTRifSecPrdBcastIntv_Object = MibTableColumn
cdx6500PCTRifSecPrdBcastIntv = _Cdx6500PCTRifSecPrdBcastIntv_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 27),
    _Cdx6500PCTRifSecPrdBcastIntv_Type()
)
cdx6500PCTRifSecPrdBcastIntv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifSecPrdBcastIntv.setStatus("mandatory")


class _Cdx6500PCTRifRoutInvldTime_Type(Integer32):
    """Custom type cdx6500PCTRifRoutInvldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65530),
    )


_Cdx6500PCTRifRoutInvldTime_Type.__name__ = "Integer32"
_Cdx6500PCTRifRoutInvldTime_Object = MibTableColumn
cdx6500PCTRifRoutInvldTime = _Cdx6500PCTRifRoutInvldTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 28),
    _Cdx6500PCTRifRoutInvldTime_Type()
)
cdx6500PCTRifRoutInvldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifRoutInvldTime.setStatus("mandatory")


class _Cdx6500PCTRifRoutFlushTime_Type(Integer32):
    """Custom type cdx6500PCTRifRoutFlushTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65530),
    )


_Cdx6500PCTRifRoutFlushTime_Type.__name__ = "Integer32"
_Cdx6500PCTRifRoutFlushTime_Object = MibTableColumn
cdx6500PCTRifRoutFlushTime = _Cdx6500PCTRifRoutFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 29),
    _Cdx6500PCTRifRoutFlushTime_Type()
)
cdx6500PCTRifRoutFlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifRoutFlushTime.setStatus("mandatory")


class _Cdx6500PCTRifRdpEnable_Type(Integer32):
    """Custom type cdx6500PCTRifRdpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRifRdpEnable_Type.__name__ = "Integer32"
_Cdx6500PCTRifRdpEnable_Object = MibTableColumn
cdx6500PCTRifRdpEnable = _Cdx6500PCTRifRdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 30),
    _Cdx6500PCTRifRdpEnable_Type()
)
cdx6500PCTRifRdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifRdpEnable.setStatus("mandatory")
_Cdx6500PCTRifRdpLevel_Type = DisplayString
_Cdx6500PCTRifRdpLevel_Object = MibTableColumn
cdx6500PCTRifRdpLevel = _Cdx6500PCTRifRdpLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 9, 1, 31),
    _Cdx6500PCTRifRdpLevel_Type()
)
cdx6500PCTRifRdpLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRifRdpLevel.setStatus("mandatory")
_Cdx6500PCTRbootpServTable_Object = MibTable
cdx6500PCTRbootpServTable = _Cdx6500PCTRbootpServTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    cdx6500PCTRbootpServTable.setStatus("mandatory")
_Cdx6500PCTRbootpServEntry_Object = MibTableRow
cdx6500PCTRbootpServEntry = _Cdx6500PCTRbootpServEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 10, 1)
)
cdx6500PCTRbootpServEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRbootpServIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRbootpServEntry.setStatus("mandatory")


class _Cdx6500PCTRbootpServIndex_Type(Integer32):
    """Custom type cdx6500PCTRbootpServIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRbootpServIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRbootpServIndex_Object = MibTableColumn
cdx6500PCTRbootpServIndex = _Cdx6500PCTRbootpServIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 10, 1, 1),
    _Cdx6500PCTRbootpServIndex_Type()
)
cdx6500PCTRbootpServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRbootpServIndex.setStatus("mandatory")
_Cdx6500PCTRbootpServAd_Type = IpAddress
_Cdx6500PCTRbootpServAd_Object = MibTableColumn
cdx6500PCTRbootpServAd = _Cdx6500PCTRbootpServAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 10, 1, 2),
    _Cdx6500PCTRbootpServAd_Type()
)
cdx6500PCTRbootpServAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRbootpServAd.setStatus("mandatory")
_Cdx6500PCTRegpAsTable_Object = MibTable
cdx6500PCTRegpAsTable = _Cdx6500PCTRegpAsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsTable.setStatus("optional")
_Cdx6500PCTRegpAsEntry_Object = MibTableRow
cdx6500PCTRegpAsEntry = _Cdx6500PCTRegpAsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1)
)
cdx6500PCTRegpAsEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRegpAsIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsEntry.setStatus("mandatory")


class _Cdx6500PCTRegpAsIndex_Type(Integer32):
    """Custom type cdx6500PCTRegpAsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRegpAsIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRegpAsIndex_Object = MibTableColumn
cdx6500PCTRegpAsIndex = _Cdx6500PCTRegpAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1, 1),
    _Cdx6500PCTRegpAsIndex_Type()
)
cdx6500PCTRegpAsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsIndex.setStatus("mandatory")


class _Cdx6500PCTRegpAsNeighAs_Type(Integer32):
    """Custom type cdx6500PCTRegpAsNeighAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRegpAsNeighAs_Type.__name__ = "Integer32"
_Cdx6500PCTRegpAsNeighAs_Object = MibTableColumn
cdx6500PCTRegpAsNeighAs = _Cdx6500PCTRegpAsNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1, 2),
    _Cdx6500PCTRegpAsNeighAs_Type()
)
cdx6500PCTRegpAsNeighAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsNeighAs.setStatus("mandatory")


class _Cdx6500PCTRegpAsInterchFlag_Type(Integer32):
    """Custom type cdx6500PCTRegpAsInterchFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500PCTRegpAsInterchFlag_Type.__name__ = "Integer32"
_Cdx6500PCTRegpAsInterchFlag_Object = MibTableColumn
cdx6500PCTRegpAsInterchFlag = _Cdx6500PCTRegpAsInterchFlag_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1, 3),
    _Cdx6500PCTRegpAsInterchFlag_Type()
)
cdx6500PCTRegpAsInterchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsInterchFlag.setStatus("mandatory")


class _Cdx6500PCTRegpAsUseEgMetric_Type(Integer32):
    """Custom type cdx6500PCTRegpAsUseEgMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500PCTRegpAsUseEgMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRegpAsUseEgMetric_Object = MibTableColumn
cdx6500PCTRegpAsUseEgMetric = _Cdx6500PCTRegpAsUseEgMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1, 4),
    _Cdx6500PCTRegpAsUseEgMetric_Type()
)
cdx6500PCTRegpAsUseEgMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsUseEgMetric.setStatus("mandatory")


class _Cdx6500PCTRegpAsDefMetric_Type(Integer32):
    """Custom type cdx6500PCTRegpAsDefMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRegpAsDefMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRegpAsDefMetric_Object = MibTableColumn
cdx6500PCTRegpAsDefMetric = _Cdx6500PCTRegpAsDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 11, 1, 5),
    _Cdx6500PCTRegpAsDefMetric_Type()
)
cdx6500PCTRegpAsDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpAsDefMetric.setStatus("mandatory")
_Cdx6500PCTRegpNeighTable_Object = MibTable
cdx6500PCTRegpNeighTable = _Cdx6500PCTRegpNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    cdx6500PCTRegpNeighTable.setStatus("optional")
_Cdx6500PCTRegpNeighEntry_Object = MibTableRow
cdx6500PCTRegpNeighEntry = _Cdx6500PCTRegpNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 12, 1)
)
cdx6500PCTRegpNeighEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRegpNeighIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRegpNeighEntry.setStatus("mandatory")


class _Cdx6500PCTRegpNeighIndex_Type(Integer32):
    """Custom type cdx6500PCTRegpNeighIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRegpNeighIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRegpNeighIndex_Object = MibTableColumn
cdx6500PCTRegpNeighIndex = _Cdx6500PCTRegpNeighIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 12, 1, 1),
    _Cdx6500PCTRegpNeighIndex_Type()
)
cdx6500PCTRegpNeighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRegpNeighIndex.setStatus("mandatory")
_Cdx6500PCTRegpNeighIdAd_Type = IpAddress
_Cdx6500PCTRegpNeighIdAd_Object = MibTableColumn
cdx6500PCTRegpNeighIdAd = _Cdx6500PCTRegpNeighIdAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 12, 1, 2),
    _Cdx6500PCTRegpNeighIdAd_Type()
)
cdx6500PCTRegpNeighIdAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpNeighIdAd.setStatus("mandatory")
_Cdx6500PCTRegpNeighAs_Type = Integer32
_Cdx6500PCTRegpNeighAs_Object = MibTableColumn
cdx6500PCTRegpNeighAs = _Cdx6500PCTRegpNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 12, 1, 3),
    _Cdx6500PCTRegpNeighAs_Type()
)
cdx6500PCTRegpNeighAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRegpNeighAs.setStatus("mandatory")


class _Cdx6500PCTRipParamBootpFwdg_Type(Integer32):
    """Custom type cdx6500PCTRipParamBootpFwdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamBootpFwdg_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamBootpFwdg_Object = MibScalar
cdx6500PCTRipParamBootpFwdg = _Cdx6500PCTRipParamBootpFwdg_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 13),
    _Cdx6500PCTRipParamBootpFwdg_Type()
)
cdx6500PCTRipParamBootpFwdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamBootpFwdg.setStatus("mandatory")


class _Cdx6500PCTRipParamBootpMaxHops_Type(Integer32):
    """Custom type cdx6500PCTRipParamBootpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRipParamBootpMaxHops_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamBootpMaxHops_Object = MibScalar
cdx6500PCTRipParamBootpMaxHops = _Cdx6500PCTRipParamBootpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 14),
    _Cdx6500PCTRipParamBootpMaxHops_Type()
)
cdx6500PCTRipParamBootpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamBootpMaxHops.setStatus("mandatory")


class _Cdx6500PCTRipParamBootpSbf_Type(Integer32):
    """Custom type cdx6500PCTRipParamBootpSbf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRipParamBootpSbf_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamBootpSbf_Object = MibScalar
cdx6500PCTRipParamBootpSbf = _Cdx6500PCTRipParamBootpSbf_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 15),
    _Cdx6500PCTRipParamBootpSbf_Type()
)
cdx6500PCTRipParamBootpSbf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamBootpSbf.setStatus("mandatory")
_Cdx6500PCTRipParamEgpSysNum_Type = Integer32
_Cdx6500PCTRipParamEgpSysNum_Object = MibScalar
cdx6500PCTRipParamEgpSysNum = _Cdx6500PCTRipParamEgpSysNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 16),
    _Cdx6500PCTRipParamEgpSysNum_Type()
)
cdx6500PCTRipParamEgpSysNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamEgpSysNum.setStatus("mandatory")


class _Cdx6500PCTRipParamEgpReadvert_Type(Integer32):
    """Custom type cdx6500PCTRipParamEgpReadvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamEgpReadvert_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamEgpReadvert_Object = MibScalar
cdx6500PCTRipParamEgpReadvert = _Cdx6500PCTRipParamEgpReadvert_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 17),
    _Cdx6500PCTRipParamEgpReadvert_Type()
)
cdx6500PCTRipParamEgpReadvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamEgpReadvert.setStatus("mandatory")


class _Cdx6500PCTRipParamRip_Type(Integer32):
    """Custom type cdx6500PCTRipParamRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamRip_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamRip_Object = MibScalar
cdx6500PCTRipParamRip = _Cdx6500PCTRipParamRip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 18),
    _Cdx6500PCTRipParamRip_Type()
)
cdx6500PCTRipParamRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamRip.setStatus("mandatory")


class _Cdx6500PCTRipParamRipOrigDef_Type(Integer32):
    """Custom type cdx6500PCTRipParamRipOrigDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamRipOrigDef_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamRipOrigDef_Object = MibScalar
cdx6500PCTRipParamRipOrigDef = _Cdx6500PCTRipParamRipOrigDef_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 19),
    _Cdx6500PCTRipParamRipOrigDef_Type()
)
cdx6500PCTRipParamRipOrigDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamRipOrigDef.setStatus("mandatory")


class _Cdx6500PCTRipParamAdvDefMetCost_Type(Integer32):
    """Custom type cdx6500PCTRipParamAdvDefMetCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500PCTRipParamAdvDefMetCost_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamAdvDefMetCost_Object = MibScalar
cdx6500PCTRipParamAdvDefMetCost = _Cdx6500PCTRipParamAdvDefMetCost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 20),
    _Cdx6500PCTRipParamAdvDefMetCost_Type()
)
cdx6500PCTRipParamAdvDefMetCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamAdvDefMetCost.setStatus("mandatory")
_Cdx6500PCTRipParamNextHopDefGway_Type = IpAddress
_Cdx6500PCTRipParamNextHopDefGway_Object = MibScalar
cdx6500PCTRipParamNextHopDefGway = _Cdx6500PCTRipParamNextHopDefGway_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 21),
    _Cdx6500PCTRipParamNextHopDefGway_Type()
)
cdx6500PCTRipParamNextHopDefGway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamNextHopDefGway.setStatus("mandatory")


class _Cdx6500PCTRipParamDistDefGway_Type(Integer32):
    """Custom type cdx6500PCTRipParamDistDefGway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRipParamDistDefGway_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamDistDefGway_Object = MibScalar
cdx6500PCTRipParamDistDefGway = _Cdx6500PCTRipParamDistDefGway_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 22),
    _Cdx6500PCTRipParamDistDefGway_Type()
)
cdx6500PCTRipParamDistDefGway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamDistDefGway.setStatus("mandatory")


class _Cdx6500PCTRipParamRoutTableSize_Type(Integer32):
    """Custom type cdx6500PCTRipParamRoutTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 65535),
    )


_Cdx6500PCTRipParamRoutTableSize_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamRoutTableSize_Object = MibScalar
cdx6500PCTRipParamRoutTableSize = _Cdx6500PCTRipParamRoutTableSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 23),
    _Cdx6500PCTRipParamRoutTableSize_Type()
)
cdx6500PCTRipParamRoutTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamRoutTableSize.setStatus("mandatory")


class _Cdx6500PCTRipParamDirBcast_Type(Integer32):
    """Custom type cdx6500PCTRipParamDirBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamDirBcast_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamDirBcast_Object = MibScalar
cdx6500PCTRipParamDirBcast = _Cdx6500PCTRipParamDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 24),
    _Cdx6500PCTRipParamDirBcast_Type()
)
cdx6500PCTRipParamDirBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamDirBcast.setStatus("mandatory")
_Cdx6500PCTRipParamInternalNetMask_Type = IpAddress
_Cdx6500PCTRipParamInternalNetMask_Object = MibScalar
cdx6500PCTRipParamInternalNetMask = _Cdx6500PCTRipParamInternalNetMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 25),
    _Cdx6500PCTRipParamInternalNetMask_Type()
)
cdx6500PCTRipParamInternalNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamInternalNetMask.setStatus("mandatory")
_Cdx6500PCTRipParamInternalIpAd_Type = IpAddress
_Cdx6500PCTRipParamInternalIpAd_Object = MibScalar
cdx6500PCTRipParamInternalIpAd = _Cdx6500PCTRipParamInternalIpAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 26),
    _Cdx6500PCTRipParamInternalIpAd_Type()
)
cdx6500PCTRipParamInternalIpAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamInternalIpAd.setStatus("mandatory")


class _Cdx6500PCTRipParamCacheSize_Type(Integer32):
    """Custom type cdx6500PCTRipParamCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 10000),
    )


_Cdx6500PCTRipParamCacheSize_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamCacheSize_Object = MibScalar
cdx6500PCTRipParamCacheSize = _Cdx6500PCTRipParamCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 27),
    _Cdx6500PCTRipParamCacheSize_Type()
)
cdx6500PCTRipParamCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamCacheSize.setStatus("mandatory")


class _Cdx6500PCTRipParamReasmBuffSize_Type(Integer32):
    """Custom type cdx6500PCTRipParamReasmBuffSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )


_Cdx6500PCTRipParamReasmBuffSize_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamReasmBuffSize_Object = MibScalar
cdx6500PCTRipParamReasmBuffSize = _Cdx6500PCTRipParamReasmBuffSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 28),
    _Cdx6500PCTRipParamReasmBuffSize_Type()
)
cdx6500PCTRipParamReasmBuffSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamReasmBuffSize.setStatus("mandatory")


class _Cdx6500PCTRipParamAccessCntrl_Type(Integer32):
    """Custom type cdx6500PCTRipParamAccessCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTRipParamAccessCntrl_Type.__name__ = "Integer32"
_Cdx6500PCTRipParamAccessCntrl_Object = MibScalar
cdx6500PCTRipParamAccessCntrl = _Cdx6500PCTRipParamAccessCntrl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 29),
    _Cdx6500PCTRipParamAccessCntrl_Type()
)
cdx6500PCTRipParamAccessCntrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipParamAccessCntrl.setStatus("mandatory")
_Cdx6500PCTRdefSubGwayTable_Object = MibTable
cdx6500PCTRdefSubGwayTable = _Cdx6500PCTRdefSubGwayTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30)
)
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwayTable.setStatus("mandatory")
_Cdx6500PCTRdefSubGwayEntry_Object = MibTableRow
cdx6500PCTRdefSubGwayEntry = _Cdx6500PCTRdefSubGwayEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30, 1)
)
cdx6500PCTRdefSubGwayEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRdefSubGwayIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwayEntry.setStatus("mandatory")


class _Cdx6500PCTRdefSubGwayIndex_Type(Integer32):
    """Custom type cdx6500PCTRdefSubGwayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRdefSubGwayIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRdefSubGwayIndex_Object = MibTableColumn
cdx6500PCTRdefSubGwayIndex = _Cdx6500PCTRdefSubGwayIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30, 1, 1),
    _Cdx6500PCTRdefSubGwayIndex_Type()
)
cdx6500PCTRdefSubGwayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwayIndex.setStatus("mandatory")
_Cdx6500PCTRdefSubGwaySubnetAd_Type = IpAddress
_Cdx6500PCTRdefSubGwaySubnetAd_Object = MibTableColumn
cdx6500PCTRdefSubGwaySubnetAd = _Cdx6500PCTRdefSubGwaySubnetAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30, 1, 2),
    _Cdx6500PCTRdefSubGwaySubnetAd_Type()
)
cdx6500PCTRdefSubGwaySubnetAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwaySubnetAd.setStatus("mandatory")
_Cdx6500PCTRdefSubGwayNextHopAd_Type = IpAddress
_Cdx6500PCTRdefSubGwayNextHopAd_Object = MibTableColumn
cdx6500PCTRdefSubGwayNextHopAd = _Cdx6500PCTRdefSubGwayNextHopAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30, 1, 3),
    _Cdx6500PCTRdefSubGwayNextHopAd_Type()
)
cdx6500PCTRdefSubGwayNextHopAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwayNextHopAd.setStatus("mandatory")


class _Cdx6500PCTRdefSubGwayDistToGway_Type(Integer32):
    """Custom type cdx6500PCTRdefSubGwayDistToGway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRdefSubGwayDistToGway_Type.__name__ = "Integer32"
_Cdx6500PCTRdefSubGwayDistToGway_Object = MibTableColumn
cdx6500PCTRdefSubGwayDistToGway = _Cdx6500PCTRdefSubGwayDistToGway_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 30, 1, 4),
    _Cdx6500PCTRdefSubGwayDistToGway_Type()
)
cdx6500PCTRdefSubGwayDistToGway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRdefSubGwayDistToGway.setStatus("mandatory")
_Cdx6500PCTRStaticRouteTable_Object = MibTable
cdx6500PCTRStaticRouteTable = _Cdx6500PCTRStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31)
)
if mibBuilder.loadTexts:
    cdx6500PCTRStaticRouteTable.setStatus("mandatory")
_Cdx6500PCTRStaticRouteEntry_Object = MibTableRow
cdx6500PCTRStaticRouteEntry = _Cdx6500PCTRStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1)
)
cdx6500PCTRStaticRouteEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRipRouteIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRStaticRouteEntry.setStatus("mandatory")


class _Cdx6500PCTRipRouteIndex_Type(Integer32):
    """Custom type cdx6500PCTRipRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRipRouteIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRipRouteIndex_Object = MibTableColumn
cdx6500PCTRipRouteIndex = _Cdx6500PCTRipRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1, 1),
    _Cdx6500PCTRipRouteIndex_Type()
)
cdx6500PCTRipRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRipRouteIndex.setStatus("mandatory")
_Cdx6500PCTRipRouteIpNetwork_Type = IpAddress
_Cdx6500PCTRipRouteIpNetwork_Object = MibTableColumn
cdx6500PCTRipRouteIpNetwork = _Cdx6500PCTRipRouteIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1, 2),
    _Cdx6500PCTRipRouteIpNetwork_Type()
)
cdx6500PCTRipRouteIpNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipRouteIpNetwork.setStatus("mandatory")
_Cdx6500PCTRipRouteIpMask_Type = IpAddress
_Cdx6500PCTRipRouteIpMask_Object = MibTableColumn
cdx6500PCTRipRouteIpMask = _Cdx6500PCTRipRouteIpMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1, 3),
    _Cdx6500PCTRipRouteIpMask_Type()
)
cdx6500PCTRipRouteIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipRouteIpMask.setStatus("mandatory")
_Cdx6500PCTRipRouteNextHop_Type = IpAddress
_Cdx6500PCTRipRouteNextHop_Object = MibTableColumn
cdx6500PCTRipRouteNextHop = _Cdx6500PCTRipRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1, 4),
    _Cdx6500PCTRipRouteNextHop_Type()
)
cdx6500PCTRipRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipRouteNextHop.setStatus("mandatory")


class _Cdx6500PCTRipRouteCost_Type(Integer32):
    """Custom type cdx6500PCTRipRouteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRipRouteCost_Type.__name__ = "Integer32"
_Cdx6500PCTRipRouteCost_Object = MibTableColumn
cdx6500PCTRipRouteCost = _Cdx6500PCTRipRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 31, 1, 5),
    _Cdx6500PCTRipRouteCost_Type()
)
cdx6500PCTRipRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRipRouteCost.setStatus("mandatory")
_Cdx6500PCTRoutInterchTable_Object = MibTable
cdx6500PCTRoutInterchTable = _Cdx6500PCTRoutInterchTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32)
)
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchTable.setStatus("optional")
_Cdx6500PCTRoutInterchEntry_Object = MibTableRow
cdx6500PCTRoutInterchEntry = _Cdx6500PCTRoutInterchEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1)
)
cdx6500PCTRoutInterchEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRoutInterchIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchEntry.setStatus("mandatory")


class _Cdx6500PCTRoutInterchIndex_Type(Integer32):
    """Custom type cdx6500PCTRoutInterchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRoutInterchIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRoutInterchIndex_Object = MibTableColumn
cdx6500PCTRoutInterchIndex = _Cdx6500PCTRoutInterchIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 1),
    _Cdx6500PCTRoutInterchIndex_Type()
)
cdx6500PCTRoutInterchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchIndex.setStatus("mandatory")


class _Cdx6500PCTRoutInterchInterchNeighAs_Type(Integer32):
    """Custom type cdx6500PCTRoutInterchInterchNeighAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRoutInterchInterchNeighAs_Type.__name__ = "Integer32"
_Cdx6500PCTRoutInterchInterchNeighAs_Object = MibTableColumn
cdx6500PCTRoutInterchInterchNeighAs = _Cdx6500PCTRoutInterchInterchNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 2),
    _Cdx6500PCTRoutInterchInterchNeighAs_Type()
)
cdx6500PCTRoutInterchInterchNeighAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchInterchNeighAs.setStatus("mandatory")


class _Cdx6500PCTRoutInterchSourceAs_Type(Integer32):
    """Custom type cdx6500PCTRoutInterchSourceAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRoutInterchSourceAs_Type.__name__ = "Integer32"
_Cdx6500PCTRoutInterchSourceAs_Object = MibTableColumn
cdx6500PCTRoutInterchSourceAs = _Cdx6500PCTRoutInterchSourceAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 3),
    _Cdx6500PCTRoutInterchSourceAs_Type()
)
cdx6500PCTRoutInterchSourceAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchSourceAs.setStatus("mandatory")
_Cdx6500PCTRoutInterchIpNetwork_Type = IpAddress
_Cdx6500PCTRoutInterchIpNetwork_Object = MibTableColumn
cdx6500PCTRoutInterchIpNetwork = _Cdx6500PCTRoutInterchIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 4),
    _Cdx6500PCTRoutInterchIpNetwork_Type()
)
cdx6500PCTRoutInterchIpNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchIpNetwork.setStatus("mandatory")


class _Cdx6500PCTRoutInterchUseIgpMetric_Type(Integer32):
    """Custom type cdx6500PCTRoutInterchUseIgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500PCTRoutInterchUseIgpMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRoutInterchUseIgpMetric_Object = MibTableColumn
cdx6500PCTRoutInterchUseIgpMetric = _Cdx6500PCTRoutInterchUseIgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 5),
    _Cdx6500PCTRoutInterchUseIgpMetric_Type()
)
cdx6500PCTRoutInterchUseIgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchUseIgpMetric.setStatus("mandatory")


class _Cdx6500PCTRoutInterchMetric_Type(Integer32):
    """Custom type cdx6500PCTRoutInterchMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRoutInterchMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRoutInterchMetric_Object = MibTableColumn
cdx6500PCTRoutInterchMetric = _Cdx6500PCTRoutInterchMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 32, 1, 6),
    _Cdx6500PCTRoutInterchMetric_Type()
)
cdx6500PCTRoutInterchMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRoutInterchMetric.setStatus("mandatory")
_Cdx6500PCTRinInterchTable_Object = MibTable
cdx6500PCTRinInterchTable = _Cdx6500PCTRinInterchTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33)
)
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchTable.setStatus("optional")
_Cdx6500PCTRinInterchEntry_Object = MibTableRow
cdx6500PCTRinInterchEntry = _Cdx6500PCTRinInterchEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1)
)
cdx6500PCTRinInterchEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRinInterchIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchEntry.setStatus("mandatory")


class _Cdx6500PCTRinInterchIndex_Type(Integer32):
    """Custom type cdx6500PCTRinInterchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRinInterchIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRinInterchIndex_Object = MibTableColumn
cdx6500PCTRinInterchIndex = _Cdx6500PCTRinInterchIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1, 1),
    _Cdx6500PCTRinInterchIndex_Type()
)
cdx6500PCTRinInterchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchIndex.setStatus("mandatory")


class _Cdx6500PCTRinInterchNeighAs_Type(Integer32):
    """Custom type cdx6500PCTRinInterchNeighAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500PCTRinInterchNeighAs_Type.__name__ = "Integer32"
_Cdx6500PCTRinInterchNeighAs_Object = MibTableColumn
cdx6500PCTRinInterchNeighAs = _Cdx6500PCTRinInterchNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1, 2),
    _Cdx6500PCTRinInterchNeighAs_Type()
)
cdx6500PCTRinInterchNeighAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchNeighAs.setStatus("mandatory")
_Cdx6500PCTRinInterchIpNetwork_Type = IpAddress
_Cdx6500PCTRinInterchIpNetwork_Object = MibTableColumn
cdx6500PCTRinInterchIpNetwork = _Cdx6500PCTRinInterchIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1, 3),
    _Cdx6500PCTRinInterchIpNetwork_Type()
)
cdx6500PCTRinInterchIpNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchIpNetwork.setStatus("mandatory")


class _Cdx6500PCTRinInterchUseEgpMetric_Type(Integer32):
    """Custom type cdx6500PCTRinInterchUseEgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500PCTRinInterchUseEgpMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRinInterchUseEgpMetric_Object = MibTableColumn
cdx6500PCTRinInterchUseEgpMetric = _Cdx6500PCTRinInterchUseEgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1, 4),
    _Cdx6500PCTRinInterchUseEgpMetric_Type()
)
cdx6500PCTRinInterchUseEgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchUseEgpMetric.setStatus("mandatory")


class _Cdx6500PCTRinInterchMetric_Type(Integer32):
    """Custom type cdx6500PCTRinInterchMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRinInterchMetric_Type.__name__ = "Integer32"
_Cdx6500PCTRinInterchMetric_Object = MibTableColumn
cdx6500PCTRinInterchMetric = _Cdx6500PCTRinInterchMetric_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 33, 1, 5),
    _Cdx6500PCTRinInterchMetric_Type()
)
cdx6500PCTRinInterchMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRinInterchMetric.setStatus("mandatory")
_Cdx6500PCTRfilterTable_Object = MibTable
cdx6500PCTRfilterTable = _Cdx6500PCTRfilterTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 34)
)
if mibBuilder.loadTexts:
    cdx6500PCTRfilterTable.setStatus("mandatory")
_Cdx6500PCTRfilterEntry_Object = MibTableRow
cdx6500PCTRfilterEntry = _Cdx6500PCTRfilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 34, 1)
)
cdx6500PCTRfilterEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRfilterIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRfilterEntry.setStatus("mandatory")


class _Cdx6500PCTRfilterIndex_Type(Integer32):
    """Custom type cdx6500PCTRfilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRfilterIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRfilterIndex_Object = MibTableColumn
cdx6500PCTRfilterIndex = _Cdx6500PCTRfilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 34, 1, 1),
    _Cdx6500PCTRfilterIndex_Type()
)
cdx6500PCTRfilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRfilterIndex.setStatus("mandatory")
_Cdx6500PCTRfilterDstIpAd_Type = IpAddress
_Cdx6500PCTRfilterDstIpAd_Object = MibTableColumn
cdx6500PCTRfilterDstIpAd = _Cdx6500PCTRfilterDstIpAd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 34, 1, 2),
    _Cdx6500PCTRfilterDstIpAd_Type()
)
cdx6500PCTRfilterDstIpAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRfilterDstIpAd.setStatus("mandatory")
_Cdx6500PCTRfilterAdMask_Type = IpAddress
_Cdx6500PCTRfilterAdMask_Object = MibTableColumn
cdx6500PCTRfilterAdMask = _Cdx6500PCTRfilterAdMask_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 34, 1, 3),
    _Cdx6500PCTRfilterAdMask_Type()
)
cdx6500PCTRfilterAdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRfilterAdMask.setStatus("mandatory")


class _Cdx6500PCTRifState1_Type(Integer32):
    """Custom type cdx6500PCTRifState1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState1_Type.__name__ = "Integer32"
_Cdx6500PCTRifState1_Object = MibScalar
cdx6500PCTRifState1 = _Cdx6500PCTRifState1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 35),
    _Cdx6500PCTRifState1_Type()
)
cdx6500PCTRifState1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState1.setStatus("optional")


class _Cdx6500PCTRifState2_Type(Integer32):
    """Custom type cdx6500PCTRifState2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState2_Type.__name__ = "Integer32"
_Cdx6500PCTRifState2_Object = MibScalar
cdx6500PCTRifState2 = _Cdx6500PCTRifState2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 36),
    _Cdx6500PCTRifState2_Type()
)
cdx6500PCTRifState2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState2.setStatus("mandatory")


class _Cdx6500PCTRifState3_Type(Integer32):
    """Custom type cdx6500PCTRifState3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState3_Type.__name__ = "Integer32"
_Cdx6500PCTRifState3_Object = MibScalar
cdx6500PCTRifState3 = _Cdx6500PCTRifState3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 37),
    _Cdx6500PCTRifState3_Type()
)
cdx6500PCTRifState3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState3.setStatus("mandatory")


class _Cdx6500PCTRifState4_Type(Integer32):
    """Custom type cdx6500PCTRifState4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState4_Type.__name__ = "Integer32"
_Cdx6500PCTRifState4_Object = MibScalar
cdx6500PCTRifState4 = _Cdx6500PCTRifState4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 38),
    _Cdx6500PCTRifState4_Type()
)
cdx6500PCTRifState4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState4.setStatus("mandatory")


class _Cdx6500PCTRifState5_Type(Integer32):
    """Custom type cdx6500PCTRifState5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState5_Type.__name__ = "Integer32"
_Cdx6500PCTRifState5_Object = MibScalar
cdx6500PCTRifState5 = _Cdx6500PCTRifState5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 39),
    _Cdx6500PCTRifState5_Type()
)
cdx6500PCTRifState5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState5.setStatus("mandatory")


class _Cdx6500PCTRifState6_Type(Integer32):
    """Custom type cdx6500PCTRifState6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState6_Type.__name__ = "Integer32"
_Cdx6500PCTRifState6_Object = MibScalar
cdx6500PCTRifState6 = _Cdx6500PCTRifState6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 40),
    _Cdx6500PCTRifState6_Type()
)
cdx6500PCTRifState6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState6.setStatus("mandatory")


class _Cdx6500PCTRifState7_Type(Integer32):
    """Custom type cdx6500PCTRifState7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState7_Type.__name__ = "Integer32"
_Cdx6500PCTRifState7_Object = MibScalar
cdx6500PCTRifState7 = _Cdx6500PCTRifState7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 41),
    _Cdx6500PCTRifState7_Type()
)
cdx6500PCTRifState7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState7.setStatus("mandatory")


class _Cdx6500PCTRifState8_Type(Integer32):
    """Custom type cdx6500PCTRifState8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState8_Type.__name__ = "Integer32"
_Cdx6500PCTRifState8_Object = MibScalar
cdx6500PCTRifState8 = _Cdx6500PCTRifState8_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 42),
    _Cdx6500PCTRifState8_Type()
)
cdx6500PCTRifState8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState8.setStatus("mandatory")


class _Cdx6500PCTRifState9_Type(Integer32):
    """Custom type cdx6500PCTRifState9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState9_Type.__name__ = "Integer32"
_Cdx6500PCTRifState9_Object = MibScalar
cdx6500PCTRifState9 = _Cdx6500PCTRifState9_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 43),
    _Cdx6500PCTRifState9_Type()
)
cdx6500PCTRifState9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState9.setStatus("mandatory")


class _Cdx6500PCTRifState10_Type(Integer32):
    """Custom type cdx6500PCTRifState10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState10_Type.__name__ = "Integer32"
_Cdx6500PCTRifState10_Object = MibScalar
cdx6500PCTRifState10 = _Cdx6500PCTRifState10_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 44),
    _Cdx6500PCTRifState10_Type()
)
cdx6500PCTRifState10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState10.setStatus("mandatory")


class _Cdx6500PCTRifState11_Type(Integer32):
    """Custom type cdx6500PCTRifState11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState11_Type.__name__ = "Integer32"
_Cdx6500PCTRifState11_Object = MibScalar
cdx6500PCTRifState11 = _Cdx6500PCTRifState11_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 45),
    _Cdx6500PCTRifState11_Type()
)
cdx6500PCTRifState11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState11.setStatus("mandatory")


class _Cdx6500PCTRifState12_Type(Integer32):
    """Custom type cdx6500PCTRifState12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState12_Type.__name__ = "Integer32"
_Cdx6500PCTRifState12_Object = MibScalar
cdx6500PCTRifState12 = _Cdx6500PCTRifState12_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 46),
    _Cdx6500PCTRifState12_Type()
)
cdx6500PCTRifState12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState12.setStatus("mandatory")


class _Cdx6500PCTRifState13_Type(Integer32):
    """Custom type cdx6500PCTRifState13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState13_Type.__name__ = "Integer32"
_Cdx6500PCTRifState13_Object = MibScalar
cdx6500PCTRifState13 = _Cdx6500PCTRifState13_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 47),
    _Cdx6500PCTRifState13_Type()
)
cdx6500PCTRifState13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState13.setStatus("mandatory")


class _Cdx6500PCTRifState14_Type(Integer32):
    """Custom type cdx6500PCTRifState14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState14_Type.__name__ = "Integer32"
_Cdx6500PCTRifState14_Object = MibScalar
cdx6500PCTRifState14 = _Cdx6500PCTRifState14_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 48),
    _Cdx6500PCTRifState14_Type()
)
cdx6500PCTRifState14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState14.setStatus("mandatory")


class _Cdx6500PCTRifState15_Type(Integer32):
    """Custom type cdx6500PCTRifState15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState15_Type.__name__ = "Integer32"
_Cdx6500PCTRifState15_Object = MibScalar
cdx6500PCTRifState15 = _Cdx6500PCTRifState15_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 49),
    _Cdx6500PCTRifState15_Type()
)
cdx6500PCTRifState15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState15.setStatus("mandatory")


class _Cdx6500PCTRifState16_Type(Integer32):
    """Custom type cdx6500PCTRifState16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState16_Type.__name__ = "Integer32"
_Cdx6500PCTRifState16_Object = MibScalar
cdx6500PCTRifState16 = _Cdx6500PCTRifState16_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 50),
    _Cdx6500PCTRifState16_Type()
)
cdx6500PCTRifState16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState16.setStatus("mandatory")


class _Cdx6500PCTRifState17_Type(Integer32):
    """Custom type cdx6500PCTRifState17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState17_Type.__name__ = "Integer32"
_Cdx6500PCTRifState17_Object = MibScalar
cdx6500PCTRifState17 = _Cdx6500PCTRifState17_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 51),
    _Cdx6500PCTRifState17_Type()
)
cdx6500PCTRifState17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState17.setStatus("mandatory")


class _Cdx6500PCTRifState18_Type(Integer32):
    """Custom type cdx6500PCTRifState18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState18_Type.__name__ = "Integer32"
_Cdx6500PCTRifState18_Object = MibScalar
cdx6500PCTRifState18 = _Cdx6500PCTRifState18_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 52),
    _Cdx6500PCTRifState18_Type()
)
cdx6500PCTRifState18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState18.setStatus("mandatory")


class _Cdx6500PCTRifState19_Type(Integer32):
    """Custom type cdx6500PCTRifState19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState19_Type.__name__ = "Integer32"
_Cdx6500PCTRifState19_Object = MibScalar
cdx6500PCTRifState19 = _Cdx6500PCTRifState19_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 53),
    _Cdx6500PCTRifState19_Type()
)
cdx6500PCTRifState19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState19.setStatus("mandatory")


class _Cdx6500PCTRifState20_Type(Integer32):
    """Custom type cdx6500PCTRifState20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState20_Type.__name__ = "Integer32"
_Cdx6500PCTRifState20_Object = MibScalar
cdx6500PCTRifState20 = _Cdx6500PCTRifState20_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 54),
    _Cdx6500PCTRifState20_Type()
)
cdx6500PCTRifState20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState20.setStatus("mandatory")


class _Cdx6500PCTRifState21_Type(Integer32):
    """Custom type cdx6500PCTRifState21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState21_Type.__name__ = "Integer32"
_Cdx6500PCTRifState21_Object = MibScalar
cdx6500PCTRifState21 = _Cdx6500PCTRifState21_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 55),
    _Cdx6500PCTRifState21_Type()
)
cdx6500PCTRifState21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState21.setStatus("mandatory")


class _Cdx6500PCTRifState22_Type(Integer32):
    """Custom type cdx6500PCTRifState22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState22_Type.__name__ = "Integer32"
_Cdx6500PCTRifState22_Object = MibScalar
cdx6500PCTRifState22 = _Cdx6500PCTRifState22_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 56),
    _Cdx6500PCTRifState22_Type()
)
cdx6500PCTRifState22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState22.setStatus("mandatory")


class _Cdx6500PCTRifState23_Type(Integer32):
    """Custom type cdx6500PCTRifState23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState23_Type.__name__ = "Integer32"
_Cdx6500PCTRifState23_Object = MibScalar
cdx6500PCTRifState23 = _Cdx6500PCTRifState23_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 57),
    _Cdx6500PCTRifState23_Type()
)
cdx6500PCTRifState23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState23.setStatus("mandatory")


class _Cdx6500PCTRifState24_Type(Integer32):
    """Custom type cdx6500PCTRifState24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState24_Type.__name__ = "Integer32"
_Cdx6500PCTRifState24_Object = MibScalar
cdx6500PCTRifState24 = _Cdx6500PCTRifState24_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 58),
    _Cdx6500PCTRifState24_Type()
)
cdx6500PCTRifState24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState24.setStatus("mandatory")


class _Cdx6500PCTRifState25_Type(Integer32):
    """Custom type cdx6500PCTRifState25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState25_Type.__name__ = "Integer32"
_Cdx6500PCTRifState25_Object = MibScalar
cdx6500PCTRifState25 = _Cdx6500PCTRifState25_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 59),
    _Cdx6500PCTRifState25_Type()
)
cdx6500PCTRifState25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState25.setStatus("mandatory")


class _Cdx6500PCTRifState26_Type(Integer32):
    """Custom type cdx6500PCTRifState26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState26_Type.__name__ = "Integer32"
_Cdx6500PCTRifState26_Object = MibScalar
cdx6500PCTRifState26 = _Cdx6500PCTRifState26_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 60),
    _Cdx6500PCTRifState26_Type()
)
cdx6500PCTRifState26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState26.setStatus("mandatory")


class _Cdx6500PCTRifState27_Type(Integer32):
    """Custom type cdx6500PCTRifState27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState27_Type.__name__ = "Integer32"
_Cdx6500PCTRifState27_Object = MibScalar
cdx6500PCTRifState27 = _Cdx6500PCTRifState27_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 61),
    _Cdx6500PCTRifState27_Type()
)
cdx6500PCTRifState27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState27.setStatus("mandatory")


class _Cdx6500PCTRifState28_Type(Integer32):
    """Custom type cdx6500PCTRifState28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState28_Type.__name__ = "Integer32"
_Cdx6500PCTRifState28_Object = MibScalar
cdx6500PCTRifState28 = _Cdx6500PCTRifState28_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 62),
    _Cdx6500PCTRifState28_Type()
)
cdx6500PCTRifState28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState28.setStatus("mandatory")


class _Cdx6500PCTRifState29_Type(Integer32):
    """Custom type cdx6500PCTRifState29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState29_Type.__name__ = "Integer32"
_Cdx6500PCTRifState29_Object = MibScalar
cdx6500PCTRifState29 = _Cdx6500PCTRifState29_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 63),
    _Cdx6500PCTRifState29_Type()
)
cdx6500PCTRifState29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState29.setStatus("mandatory")


class _Cdx6500PCTRifState30_Type(Integer32):
    """Custom type cdx6500PCTRifState30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState30_Type.__name__ = "Integer32"
_Cdx6500PCTRifState30_Object = MibScalar
cdx6500PCTRifState30 = _Cdx6500PCTRifState30_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 64),
    _Cdx6500PCTRifState30_Type()
)
cdx6500PCTRifState30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState30.setStatus("mandatory")


class _Cdx6500PCTRifState31_Type(Integer32):
    """Custom type cdx6500PCTRifState31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState31_Type.__name__ = "Integer32"
_Cdx6500PCTRifState31_Object = MibScalar
cdx6500PCTRifState31 = _Cdx6500PCTRifState31_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 65),
    _Cdx6500PCTRifState31_Type()
)
cdx6500PCTRifState31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState31.setStatus("mandatory")


class _Cdx6500PCTRifState32_Type(Integer32):
    """Custom type cdx6500PCTRifState32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState32_Type.__name__ = "Integer32"
_Cdx6500PCTRifState32_Object = MibScalar
cdx6500PCTRifState32 = _Cdx6500PCTRifState32_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 66),
    _Cdx6500PCTRifState32_Type()
)
cdx6500PCTRifState32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState32.setStatus("mandatory")


class _Cdx6500PCTRifState33_Type(Integer32):
    """Custom type cdx6500PCTRifState33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState33_Type.__name__ = "Integer32"
_Cdx6500PCTRifState33_Object = MibScalar
cdx6500PCTRifState33 = _Cdx6500PCTRifState33_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 67),
    _Cdx6500PCTRifState33_Type()
)
cdx6500PCTRifState33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState33.setStatus("mandatory")


class _Cdx6500PCTRifState34_Type(Integer32):
    """Custom type cdx6500PCTRifState34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState34_Type.__name__ = "Integer32"
_Cdx6500PCTRifState34_Object = MibScalar
cdx6500PCTRifState34 = _Cdx6500PCTRifState34_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 68),
    _Cdx6500PCTRifState34_Type()
)
cdx6500PCTRifState34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState34.setStatus("mandatory")


class _Cdx6500PCTRifState35_Type(Integer32):
    """Custom type cdx6500PCTRifState35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState35_Type.__name__ = "Integer32"
_Cdx6500PCTRifState35_Object = MibScalar
cdx6500PCTRifState35 = _Cdx6500PCTRifState35_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 69),
    _Cdx6500PCTRifState35_Type()
)
cdx6500PCTRifState35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState35.setStatus("mandatory")


class _Cdx6500PCTRifState36_Type(Integer32):
    """Custom type cdx6500PCTRifState36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifState36_Type.__name__ = "Integer32"
_Cdx6500PCTRifState36_Object = MibScalar
cdx6500PCTRifState36 = _Cdx6500PCTRifState36_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 70),
    _Cdx6500PCTRifState36_Type()
)
cdx6500PCTRifState36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifState36.setStatus("mandatory")
_Cdx6500PCTReventsTable_Object = MibTable
cdx6500PCTReventsTable = _Cdx6500PCTReventsTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71)
)
if mibBuilder.loadTexts:
    cdx6500PCTReventsTable.setStatus("mandatory")
_Cdx6500PCTReventsEntry_Object = MibTableRow
cdx6500PCTReventsEntry = _Cdx6500PCTReventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1)
)
cdx6500PCTReventsEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTReventsIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTReventsEntry.setStatus("mandatory")


class _Cdx6500PCTReventsIndex_Type(Integer32):
    """Custom type cdx6500PCTReventsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cdx6500PCTReventsIndex_Type.__name__ = "Integer32"
_Cdx6500PCTReventsIndex_Object = MibTableColumn
cdx6500PCTReventsIndex = _Cdx6500PCTReventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1, 1),
    _Cdx6500PCTReventsIndex_Type()
)
cdx6500PCTReventsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTReventsIndex.setStatus("mandatory")


class _Cdx6500PCTReventsSubsystem_Type(Integer32):
    """Custom type cdx6500PCTReventsSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              50)
        )
    )
    namedValues = NamedValues(
        *(("arp", 0),
          ("egp", 5),
          ("eth", 9),
          ("icmp", 2),
          ("ip", 1),
          ("ipx", 7),
          ("newvalArp", 50),
          ("ospf", 6),
          ("rip", 4),
          ("tkr", 8),
          ("udp", 3))
    )


_Cdx6500PCTReventsSubsystem_Type.__name__ = "Integer32"
_Cdx6500PCTReventsSubsystem_Object = MibTableColumn
cdx6500PCTReventsSubsystem = _Cdx6500PCTReventsSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1, 2),
    _Cdx6500PCTReventsSubsystem_Type()
)
cdx6500PCTReventsSubsystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTReventsSubsystem.setStatus("mandatory")


class _Cdx6500PCTReventsPerPktTrace_Type(Integer32):
    """Custom type cdx6500PCTReventsPerPktTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTReventsPerPktTrace_Type.__name__ = "Integer32"
_Cdx6500PCTReventsPerPktTrace_Object = MibTableColumn
cdx6500PCTReventsPerPktTrace = _Cdx6500PCTReventsPerPktTrace_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1, 3),
    _Cdx6500PCTReventsPerPktTrace_Type()
)
cdx6500PCTReventsPerPktTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTReventsPerPktTrace.setStatus("mandatory")


class _Cdx6500PCTReventsUnusualOper_Type(Integer32):
    """Custom type cdx6500PCTReventsUnusualOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTReventsUnusualOper_Type.__name__ = "Integer32"
_Cdx6500PCTReventsUnusualOper_Object = MibTableColumn
cdx6500PCTReventsUnusualOper = _Cdx6500PCTReventsUnusualOper_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1, 4),
    _Cdx6500PCTReventsUnusualOper_Type()
)
cdx6500PCTReventsUnusualOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTReventsUnusualOper.setStatus("mandatory")


class _Cdx6500PCTReventsCommonOper_Type(Integer32):
    """Custom type cdx6500PCTReventsCommonOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50))
    )


_Cdx6500PCTReventsCommonOper_Type.__name__ = "Integer32"
_Cdx6500PCTReventsCommonOper_Object = MibTableColumn
cdx6500PCTReventsCommonOper = _Cdx6500PCTReventsCommonOper_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 71, 1, 5),
    _Cdx6500PCTReventsCommonOper_Type()
)
cdx6500PCTReventsCommonOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTReventsCommonOper.setStatus("mandatory")


class _Cdx6500PCTRpriorityIpTraffic_Type(Integer32):
    """Custom type cdx6500PCTRpriorityIpTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 0),
          ("medium", 1),
          ("newvalLow", 50))
    )


_Cdx6500PCTRpriorityIpTraffic_Type.__name__ = "Integer32"
_Cdx6500PCTRpriorityIpTraffic_Object = MibScalar
cdx6500PCTRpriorityIpTraffic = _Cdx6500PCTRpriorityIpTraffic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 72),
    _Cdx6500PCTRpriorityIpTraffic_Type()
)
cdx6500PCTRpriorityIpTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRpriorityIpTraffic.setStatus("mandatory")


class _Cdx6500PCTRpriorityIpxTraffic_Type(Integer32):
    """Custom type cdx6500PCTRpriorityIpxTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 0),
          ("medium", 1),
          ("newvalLow", 50))
    )


_Cdx6500PCTRpriorityIpxTraffic_Type.__name__ = "Integer32"
_Cdx6500PCTRpriorityIpxTraffic_Object = MibScalar
cdx6500PCTRpriorityIpxTraffic = _Cdx6500PCTRpriorityIpxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 73),
    _Cdx6500PCTRpriorityIpxTraffic_Type()
)
cdx6500PCTRpriorityIpxTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRpriorityIpxTraffic.setStatus("mandatory")


class _Cdx6500PCTRMaxIpInterfaces_Type(Integer32):
    """Custom type cdx6500PCTRMaxIpInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cdx6500PCTRMaxIpInterfaces_Type.__name__ = "Integer32"
_Cdx6500PCTRMaxIpInterfaces_Object = MibScalar
cdx6500PCTRMaxIpInterfaces = _Cdx6500PCTRMaxIpInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 74),
    _Cdx6500PCTRMaxIpInterfaces_Type()
)
cdx6500PCTRMaxIpInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRMaxIpInterfaces.setStatus("mandatory")


class _Cdx6500PCTRAllSubnetBrcast_Type(Integer32):
    """Custom type cdx6500PCTRAllSubnetBrcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRAllSubnetBrcast_Type.__name__ = "Integer32"
_Cdx6500PCTRAllSubnetBrcast_Object = MibScalar
cdx6500PCTRAllSubnetBrcast = _Cdx6500PCTRAllSubnetBrcast_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 75),
    _Cdx6500PCTRAllSubnetBrcast_Type()
)
cdx6500PCTRAllSubnetBrcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRAllSubnetBrcast.setStatus("mandatory")


class _Cdx6500PCTRIpFwdEnable_Type(Integer32):
    """Custom type cdx6500PCTRIpFwdEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRIpFwdEnable_Type.__name__ = "Integer32"
_Cdx6500PCTRIpFwdEnable_Object = MibScalar
cdx6500PCTRIpFwdEnable = _Cdx6500PCTRIpFwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 76),
    _Cdx6500PCTRIpFwdEnable_Type()
)
cdx6500PCTRIpFwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRIpFwdEnable.setStatus("mandatory")


class _Cdx6500PCTRUdpFwdEnable_Type(Integer32):
    """Custom type cdx6500PCTRUdpFwdEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500PCTRUdpFwdEnable_Type.__name__ = "Integer32"
_Cdx6500PCTRUdpFwdEnable_Object = MibScalar
cdx6500PCTRUdpFwdEnable = _Cdx6500PCTRUdpFwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 77),
    _Cdx6500PCTRUdpFwdEnable_Type()
)
cdx6500PCTRUdpFwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRUdpFwdEnable.setStatus("mandatory")


class _Cdx6500PCTRpriorityAp2Traffic_Type(Integer32):
    """Custom type cdx6500PCTRpriorityAp2Traffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_Cdx6500PCTRpriorityAp2Traffic_Type.__name__ = "Integer32"
_Cdx6500PCTRpriorityAp2Traffic_Object = MibScalar
cdx6500PCTRpriorityAp2Traffic = _Cdx6500PCTRpriorityAp2Traffic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 78),
    _Cdx6500PCTRpriorityAp2Traffic_Type()
)
cdx6500PCTRpriorityAp2Traffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRpriorityAp2Traffic.setStatus("mandatory")


class _Cdx6500PCTRarpParamMaxQueue_Type(Integer32):
    """Custom type cdx6500PCTRarpParamMaxQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_Cdx6500PCTRarpParamMaxQueue_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamMaxQueue_Object = MibScalar
cdx6500PCTRarpParamMaxQueue = _Cdx6500PCTRarpParamMaxQueue_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 79),
    _Cdx6500PCTRarpParamMaxQueue_Type()
)
cdx6500PCTRarpParamMaxQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamMaxQueue.setStatus("mandatory")


class _Cdx6500PCTRarpParamTimeRetx_Type(Integer32):
    """Custom type cdx6500PCTRarpParamTimeRetx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Cdx6500PCTRarpParamTimeRetx_Type.__name__ = "Integer32"
_Cdx6500PCTRarpParamTimeRetx_Object = MibScalar
cdx6500PCTRarpParamTimeRetx = _Cdx6500PCTRarpParamTimeRetx_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 80),
    _Cdx6500PCTRarpParamTimeRetx_Type()
)
cdx6500PCTRarpParamTimeRetx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500PCTRarpParamTimeRetx.setStatus("mandatory")
_Cdx6500PCTRRIPRouteControlTable_Object = MibTable
cdx6500PCTRRIPRouteControlTable = _Cdx6500PCTRRIPRouteControlTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81)
)
if mibBuilder.loadTexts:
    cdx6500PCTRRIPRouteControlTable.setStatus("mandatory")
_Cdx6500PCTRRIPRouteControlEntry_Object = MibTableRow
cdx6500PCTRRIPRouteControlEntry = _Cdx6500PCTRRIPRouteControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1)
)
cdx6500PCTRRIPRouteControlEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRRIPRouteControlIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRRIPRouteControlEntry.setStatus("mandatory")


class _Cdx6500PCTRRIPRouteControlIndex_Type(Integer32):
    """Custom type cdx6500PCTRRIPRouteControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Cdx6500PCTRRIPRouteControlIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRRIPRouteControlIndex_Object = MibTableColumn
cdx6500PCTRRIPRouteControlIndex = _Cdx6500PCTRRIPRouteControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1, 1),
    _Cdx6500PCTRRIPRouteControlIndex_Type()
)
cdx6500PCTRRIPRouteControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRRIPRouteControlIndex.setStatus("mandatory")
_Cdx6500PCTRRIPRouteControlIpNet_Type = IpAddress
_Cdx6500PCTRRIPRouteControlIpNet_Object = MibTableColumn
cdx6500PCTRRIPRouteControlIpNet = _Cdx6500PCTRRIPRouteControlIpNet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1, 2),
    _Cdx6500PCTRRIPRouteControlIpNet_Type()
)
cdx6500PCTRRIPRouteControlIpNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRRIPRouteControlIpNet.setStatus("mandatory")
_Cdx6500PCTRRIPRouteControlIpMsk_Type = IpAddress
_Cdx6500PCTRRIPRouteControlIpMsk_Object = MibTableColumn
cdx6500PCTRRIPRouteControlIpMsk = _Cdx6500PCTRRIPRouteControlIpMsk_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1, 3),
    _Cdx6500PCTRRIPRouteControlIpMsk_Type()
)
cdx6500PCTRRIPRouteControlIpMsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRRIPRouteControlIpMsk.setStatus("mandatory")


class _Cdx6500PCTRRRCInIniface_Type(DisplayString):
    """Custom type cdx6500PCTRRRCInIniface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRRRCInIniface_Type.__name__ = "DisplayString"
_Cdx6500PCTRRRCInIniface_Object = MibTableColumn
cdx6500PCTRRRCInIniface = _Cdx6500PCTRRRCInIniface_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1, 4),
    _Cdx6500PCTRRRCInIniface_Type()
)
cdx6500PCTRRRCInIniface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRRRCInIniface.setStatus("mandatory")


class _Cdx6500PCTRRRCOutIniface_Type(DisplayString):
    """Custom type cdx6500PCTRRRCOutIniface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cdx6500PCTRRRCOutIniface_Type.__name__ = "DisplayString"
_Cdx6500PCTRRRCOutIniface_Object = MibTableColumn
cdx6500PCTRRRCOutIniface = _Cdx6500PCTRRRCOutIniface_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 81, 1, 5),
    _Cdx6500PCTRRRCOutIniface_Type()
)
cdx6500PCTRRRCOutIniface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRRRCOutIniface.setStatus("mandatory")
_Cdx6500PCTRtunnelTable_Object = MibTable
cdx6500PCTRtunnelTable = _Cdx6500PCTRtunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82)
)
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelTable.setStatus("mandatory")
_Cdx6500PCTRtunnelEntry_Object = MibTableRow
cdx6500PCTRtunnelEntry = _Cdx6500PCTRtunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1)
)
cdx6500PCTRtunnelEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRtunnelIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelEntry.setStatus("mandatory")


class _Cdx6500PCTRtunnelIndex_Type(Integer32):
    """Custom type cdx6500PCTRtunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PCTRtunnelIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelIndex_Object = MibTableColumn
cdx6500PCTRtunnelIndex = _Cdx6500PCTRtunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 1),
    _Cdx6500PCTRtunnelIndex_Type()
)
cdx6500PCTRtunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelIndex.setStatus("mandatory")


class _Cdx6500PCTRtunnelProt_Type(Integer32):
    """Custom type cdx6500PCTRtunnelProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("l2tp", 2))
    )


_Cdx6500PCTRtunnelProt_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelProt_Object = MibTableColumn
cdx6500PCTRtunnelProt = _Cdx6500PCTRtunnelProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 2),
    _Cdx6500PCTRtunnelProt_Type()
)
cdx6500PCTRtunnelProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelProt.setStatus("mandatory")


class _Cdx6500PCTRtunnelGreCksSqn_Type(DisplayString):
    """Custom type cdx6500PCTRtunnelGreCksSqn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_Cdx6500PCTRtunnelGreCksSqn_Type.__name__ = "DisplayString"
_Cdx6500PCTRtunnelGreCksSqn_Object = MibTableColumn
cdx6500PCTRtunnelGreCksSqn = _Cdx6500PCTRtunnelGreCksSqn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 3),
    _Cdx6500PCTRtunnelGreCksSqn_Type()
)
cdx6500PCTRtunnelGreCksSqn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelGreCksSqn.setStatus("mandatory")


class _Cdx6500PCTRtunnelGreResyncCntr_Type(Integer32):
    """Custom type cdx6500PCTRtunnelGreResyncCntr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Cdx6500PCTRtunnelGreResyncCntr_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelGreResyncCntr_Object = MibTableColumn
cdx6500PCTRtunnelGreResyncCntr = _Cdx6500PCTRtunnelGreResyncCntr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 4),
    _Cdx6500PCTRtunnelGreResyncCntr_Type()
)
cdx6500PCTRtunnelGreResyncCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelGreResyncCntr.setStatus("mandatory")
_Cdx6500PCTRtunnelSrcAddr_Type = IpAddress
_Cdx6500PCTRtunnelSrcAddr_Object = MibTableColumn
cdx6500PCTRtunnelSrcAddr = _Cdx6500PCTRtunnelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 5),
    _Cdx6500PCTRtunnelSrcAddr_Type()
)
cdx6500PCTRtunnelSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelSrcAddr.setStatus("mandatory")
_Cdx6500PCTRtunnelDstAddr_Type = IpAddress
_Cdx6500PCTRtunnelDstAddr_Object = MibTableColumn
cdx6500PCTRtunnelDstAddr = _Cdx6500PCTRtunnelDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 6),
    _Cdx6500PCTRtunnelDstAddr_Type()
)
cdx6500PCTRtunnelDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelDstAddr.setStatus("mandatory")


class _Cdx6500PCTRtunnelLconNo_Type(Integer32):
    """Custom type cdx6500PCTRtunnelLconNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_Cdx6500PCTRtunnelLconNo_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelLconNo_Object = MibTableColumn
cdx6500PCTRtunnelLconNo = _Cdx6500PCTRtunnelLconNo_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 7),
    _Cdx6500PCTRtunnelLconNo_Type()
)
cdx6500PCTRtunnelLconNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelLconNo.setStatus("mandatory")


class _Cdx6500PCTRtunnelPayProt_Type(DisplayString):
    """Custom type cdx6500PCTRtunnelPayProt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 20),
    )


_Cdx6500PCTRtunnelPayProt_Type.__name__ = "DisplayString"
_Cdx6500PCTRtunnelPayProt_Object = MibTableColumn
cdx6500PCTRtunnelPayProt = _Cdx6500PCTRtunnelPayProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 8),
    _Cdx6500PCTRtunnelPayProt_Type()
)
cdx6500PCTRtunnelPayProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelPayProt.setStatus("mandatory")


class _Cdx6500PCTRtunnelIfNo_Type(Integer32):
    """Custom type cdx6500PCTRtunnelIfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_Cdx6500PCTRtunnelIfNo_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelIfNo_Object = MibTableColumn
cdx6500PCTRtunnelIfNo = _Cdx6500PCTRtunnelIfNo_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 9),
    _Cdx6500PCTRtunnelIfNo_Type()
)
cdx6500PCTRtunnelIfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelIfNo.setStatus("mandatory")


class _Cdx6500PCTRtunnelRtpHdrComProf_Type(DisplayString):
    """Custom type cdx6500PCTRtunnelRtpHdrComProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Cdx6500PCTRtunnelRtpHdrComProf_Type.__name__ = "DisplayString"
_Cdx6500PCTRtunnelRtpHdrComProf_Object = MibTableColumn
cdx6500PCTRtunnelRtpHdrComProf = _Cdx6500PCTRtunnelRtpHdrComProf_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 10),
    _Cdx6500PCTRtunnelRtpHdrComProf_Type()
)
cdx6500PCTRtunnelRtpHdrComProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelRtpHdrComProf.setStatus("mandatory")


class _Cdx6500PCTRtunnelBrdgLnkNo_Type(Integer32):
    """Custom type cdx6500PCTRtunnelBrdgLnkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_Cdx6500PCTRtunnelBrdgLnkNo_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelBrdgLnkNo_Object = MibTableColumn
cdx6500PCTRtunnelBrdgLnkNo = _Cdx6500PCTRtunnelBrdgLnkNo_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 11),
    _Cdx6500PCTRtunnelBrdgLnkNo_Type()
)
cdx6500PCTRtunnelBrdgLnkNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelBrdgLnkNo.setStatus("mandatory")


class _Cdx6500PCTRtunnelEncrProf_Type(DisplayString):
    """Custom type cdx6500PCTRtunnelEncrProf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500PCTRtunnelEncrProf_Type.__name__ = "DisplayString"
_Cdx6500PCTRtunnelEncrProf_Object = MibTableColumn
cdx6500PCTRtunnelEncrProf = _Cdx6500PCTRtunnelEncrProf_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 12),
    _Cdx6500PCTRtunnelEncrProf_Type()
)
cdx6500PCTRtunnelEncrProf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelEncrProf.setStatus("mandatory")


class _Cdx6500PCTRtunnelDebug_Type(Integer32):
    """Custom type cdx6500PCTRtunnelDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Cdx6500PCTRtunnelDebug_Type.__name__ = "Integer32"
_Cdx6500PCTRtunnelDebug_Object = MibTableColumn
cdx6500PCTRtunnelDebug = _Cdx6500PCTRtunnelDebug_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 13),
    _Cdx6500PCTRtunnelDebug_Type()
)
cdx6500PCTRtunnelDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelDebug.setStatus("mandatory")
_Cdx6500PCTRtunnelLANnxthopAddr_Type = IpAddress
_Cdx6500PCTRtunnelLANnxthopAddr_Object = MibScalar
cdx6500PCTRtunnelLANnxthopAddr = _Cdx6500PCTRtunnelLANnxthopAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 82, 1, 14),
    _Cdx6500PCTRtunnelLANnxthopAddr_Type()
)
cdx6500PCTRtunnelLANnxthopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRtunnelLANnxthopAddr.setStatus("mandatory")
_Cdx6500PCTRifStateConfTable_Object = MibTable
cdx6500PCTRifStateConfTable = _Cdx6500PCTRifStateConfTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 83)
)
if mibBuilder.loadTexts:
    cdx6500PCTRifStateConfTable.setStatus("mandatory")
_Cdx6500PCTRifStateConfEntry_Object = MibTableRow
cdx6500PCTRifStateConfEntry = _Cdx6500PCTRifStateConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 83, 1)
)
cdx6500PCTRifStateConfEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PCTRifStateConfIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PCTRifStateConfEntry.setStatus("mandatory")


class _Cdx6500PCTRifStateConfIndex_Type(Integer32):
    """Custom type cdx6500PCTRifStateConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Cdx6500PCTRifStateConfIndex_Type.__name__ = "Integer32"
_Cdx6500PCTRifStateConfIndex_Object = MibTableColumn
cdx6500PCTRifStateConfIndex = _Cdx6500PCTRifStateConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 83, 1, 1),
    _Cdx6500PCTRifStateConfIndex_Type()
)
cdx6500PCTRifStateConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifStateConfIndex.setStatus("mandatory")


class _Cdx6500PCTRifStateConfState_Type(Integer32):
    """Custom type cdx6500PCTRifStateConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("unconfigured", 2))
    )


_Cdx6500PCTRifStateConfState_Type.__name__ = "Integer32"
_Cdx6500PCTRifStateConfState_Object = MibTableColumn
cdx6500PCTRifStateConfState = _Cdx6500PCTRifStateConfState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5, 83, 1, 2),
    _Cdx6500PCTRifStateConfState_Type()
)
cdx6500PCTRifStateConfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PCTRifStateConfState.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTRouterGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTRouterGroup = _Cdx6500PSTRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4)
)
_ProProtoIpDefGwAddress_Type = IpAddress
_ProProtoIpDefGwAddress_Object = MibScalar
proProtoIpDefGwAddress = _ProProtoIpDefGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 1),
    _ProProtoIpDefGwAddress_Type()
)
proProtoIpDefGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwAddress.setStatus("optional")
_ProProtoIpDefGwCost_Type = Integer32
_ProProtoIpDefGwCost_Object = MibScalar
proProtoIpDefGwCost = _ProProtoIpDefGwCost_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 2),
    _ProProtoIpDefGwCost_Type()
)
proProtoIpDefGwCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwCost.setStatus("optional")
_ProProtoIpDefGwAge_Type = Integer32
_ProProtoIpDefGwAge_Object = MibScalar
proProtoIpDefGwAge = _ProProtoIpDefGwAge_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 3),
    _ProProtoIpDefGwAge_Type()
)
proProtoIpDefGwAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proProtoIpDefGwAge.setStatus("optional")
_Cdx6500PSTRtunnelTable_Object = MibTable
cdx6500PSTRtunnelTable = _Cdx6500PSTRtunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelTable.setStatus("mandatory")
_Cdx6500PSTRtunnelEntry_Object = MibTableRow
cdx6500PSTRtunnelEntry = _Cdx6500PSTRtunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1)
)
cdx6500PSTRtunnelEntry.setIndexNames(
    (0, "ROUTER-OPT-MIB", "cdx6500PSTRtunnelIndex"),
)
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelEntry.setStatus("mandatory")


class _Cdx6500PSTRtunnelIndex_Type(Integer32):
    """Custom type cdx6500PSTRtunnelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500PSTRtunnelIndex_Type.__name__ = "Integer32"
_Cdx6500PSTRtunnelIndex_Object = MibTableColumn
cdx6500PSTRtunnelIndex = _Cdx6500PSTRtunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 1),
    _Cdx6500PSTRtunnelIndex_Type()
)
cdx6500PSTRtunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIndex.setStatus("mandatory")
_Cdx6500PSTRtunnelIpPktIn_Type = Integer32
_Cdx6500PSTRtunnelIpPktIn_Object = MibTableColumn
cdx6500PSTRtunnelIpPktIn = _Cdx6500PSTRtunnelIpPktIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 2),
    _Cdx6500PSTRtunnelIpPktIn_Type()
)
cdx6500PSTRtunnelIpPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpPktIn.setStatus("mandatory")
_Cdx6500PSTRtunnelIpPktOut_Type = Integer32
_Cdx6500PSTRtunnelIpPktOut_Object = MibTableColumn
cdx6500PSTRtunnelIpPktOut = _Cdx6500PSTRtunnelIpPktOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 3),
    _Cdx6500PSTRtunnelIpPktOut_Type()
)
cdx6500PSTRtunnelIpPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpPktOut.setStatus("mandatory")
_Cdx6500PSTRtunnelIpPktDisc_Type = Integer32
_Cdx6500PSTRtunnelIpPktDisc_Object = MibTableColumn
cdx6500PSTRtunnelIpPktDisc = _Cdx6500PSTRtunnelIpPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 4),
    _Cdx6500PSTRtunnelIpPktDisc_Type()
)
cdx6500PSTRtunnelIpPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpPktDisc.setStatus("mandatory")
_Cdx6500PSTRtunnelIpxPktIn_Type = Integer32
_Cdx6500PSTRtunnelIpxPktIn_Object = MibTableColumn
cdx6500PSTRtunnelIpxPktIn = _Cdx6500PSTRtunnelIpxPktIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 5),
    _Cdx6500PSTRtunnelIpxPktIn_Type()
)
cdx6500PSTRtunnelIpxPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpxPktIn.setStatus("mandatory")
_Cdx6500PSTRtunnelIpxPktOut_Type = Integer32
_Cdx6500PSTRtunnelIpxPktOut_Object = MibTableColumn
cdx6500PSTRtunnelIpxPktOut = _Cdx6500PSTRtunnelIpxPktOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 6),
    _Cdx6500PSTRtunnelIpxPktOut_Type()
)
cdx6500PSTRtunnelIpxPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpxPktOut.setStatus("mandatory")
_Cdx6500PSTRtunnelIpxPktDisc_Type = Integer32
_Cdx6500PSTRtunnelIpxPktDisc_Object = MibTableColumn
cdx6500PSTRtunnelIpxPktDisc = _Cdx6500PSTRtunnelIpxPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 7),
    _Cdx6500PSTRtunnelIpxPktDisc_Type()
)
cdx6500PSTRtunnelIpxPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelIpxPktDisc.setStatus("mandatory")
_Cdx6500PSTRtunnelSrcAddr_Type = IpAddress
_Cdx6500PSTRtunnelSrcAddr_Object = MibTableColumn
cdx6500PSTRtunnelSrcAddr = _Cdx6500PSTRtunnelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 8),
    _Cdx6500PSTRtunnelSrcAddr_Type()
)
cdx6500PSTRtunnelSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelSrcAddr.setStatus("mandatory")
_Cdx6500PSTRtunnelDstAddr_Type = IpAddress
_Cdx6500PSTRtunnelDstAddr_Object = MibTableColumn
cdx6500PSTRtunnelDstAddr = _Cdx6500PSTRtunnelDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 9),
    _Cdx6500PSTRtunnelDstAddr_Type()
)
cdx6500PSTRtunnelDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelDstAddr.setStatus("mandatory")


class _Cdx6500PSTRtunnelPayProt_Type(Integer32):
    """Custom type cdx6500PSTRtunnelPayProt based on Integer32"""
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
        *(("brg", 4),
          ("ip", 1),
          ("ip-brg", 5),
          ("ip-ipx", 3),
          ("ip-ipx-brg", 7),
          ("ipx", 2),
          ("ipx-brg", 6))
    )


_Cdx6500PSTRtunnelPayProt_Type.__name__ = "Integer32"
_Cdx6500PSTRtunnelPayProt_Object = MibTableColumn
cdx6500PSTRtunnelPayProt = _Cdx6500PSTRtunnelPayProt_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 10),
    _Cdx6500PSTRtunnelPayProt_Type()
)
cdx6500PSTRtunnelPayProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelPayProt.setStatus("mandatory")


class _Cdx6500PSTRtunnelEncrStatus_Type(DisplayString):
    """Custom type cdx6500PSTRtunnelEncrStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_Cdx6500PSTRtunnelEncrStatus_Type.__name__ = "DisplayString"
_Cdx6500PSTRtunnelEncrStatus_Object = MibTableColumn
cdx6500PSTRtunnelEncrStatus = _Cdx6500PSTRtunnelEncrStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 11),
    _Cdx6500PSTRtunnelEncrStatus_Type()
)
cdx6500PSTRtunnelEncrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelEncrStatus.setStatus("mandatory")


class _Cdx6500PSTRtunnelRuihcStatus_Type(Integer32):
    """Custom type cdx6500PSTRtunnelRuihcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dis", 2),
          ("ena", 1))
    )


_Cdx6500PSTRtunnelRuihcStatus_Type.__name__ = "Integer32"
_Cdx6500PSTRtunnelRuihcStatus_Object = MibTableColumn
cdx6500PSTRtunnelRuihcStatus = _Cdx6500PSTRtunnelRuihcStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 12),
    _Cdx6500PSTRtunnelRuihcStatus_Type()
)
cdx6500PSTRtunnelRuihcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelRuihcStatus.setStatus("mandatory")
_Cdx6500PSTRtunnelBrdgPktIn_Type = Integer32
_Cdx6500PSTRtunnelBrdgPktIn_Object = MibTableColumn
cdx6500PSTRtunnelBrdgPktIn = _Cdx6500PSTRtunnelBrdgPktIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 13),
    _Cdx6500PSTRtunnelBrdgPktIn_Type()
)
cdx6500PSTRtunnelBrdgPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelBrdgPktIn.setStatus("mandatory")
_Cdx6500PSTRtunnelBrdgPktOut_Type = Integer32
_Cdx6500PSTRtunnelBrdgPktOut_Object = MibTableColumn
cdx6500PSTRtunnelBrdgPktOut = _Cdx6500PSTRtunnelBrdgPktOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 14),
    _Cdx6500PSTRtunnelBrdgPktOut_Type()
)
cdx6500PSTRtunnelBrdgPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelBrdgPktOut.setStatus("mandatory")
_Cdx6500PSTRtunnelBrdgPktDisc_Type = Integer32
_Cdx6500PSTRtunnelBrdgPktDisc_Object = MibTableColumn
cdx6500PSTRtunnelBrdgPktDisc = _Cdx6500PSTRtunnelBrdgPktDisc_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4, 4, 1, 15),
    _Cdx6500PSTRtunnelBrdgPktDisc_Type()
)
cdx6500PSTRtunnelBrdgPktDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PSTRtunnelBrdgPktDisc.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROUTER-OPT-MIB",
    **{"MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTRouterGroup": cdx6500PCTRouterGroup,
       "cdx6500PCTRarpCacheTable": cdx6500PCTRarpCacheTable,
       "cdx6500PCTRarpCacheEntry": cdx6500PCTRarpCacheEntry,
       "cdx6500PCTRarpCacheIndex": cdx6500PCTRarpCacheIndex,
       "cdx6500PCTRarpCacheIfNum": cdx6500PCTRarpCacheIfNum,
       "cdx6500PCTRarpCacheProtocol": cdx6500PCTRarpCacheProtocol,
       "cdx6500PCTRarpCacheProtocolAd": cdx6500PCTRarpCacheProtocolAd,
       "cdx6500PCTRarpCacheMacAd": cdx6500PCTRarpCacheMacAd,
       "cdx6500PCTRarpParamAutoRef": cdx6500PCTRarpParamAutoRef,
       "cdx6500PCTRarpParamRefTime": cdx6500PCTRarpParamRefTime,
       "cdx6500PCTRarpParamUseTime": cdx6500PCTRarpParamUseTime,
       "cdx6500PCTRarpParamProxy": cdx6500PCTRarpParamProxy,
       "cdx6500PCTRarpParamProxySub": cdx6500PCTRarpParamProxySub,
       "cdx6500PCTRaccControlTable": cdx6500PCTRaccControlTable,
       "cdx6500PCTRaccControlEntry": cdx6500PCTRaccControlEntry,
       "cdx6500PCTRaccControlIndex": cdx6500PCTRaccControlIndex,
       "cdx6500PCTRaccControlType": cdx6500PCTRaccControlType,
       "cdx6500PCTRaccControlSrcAd": cdx6500PCTRaccControlSrcAd,
       "cdx6500PCTRaccControlSrcMask": cdx6500PCTRaccControlSrcMask,
       "cdx6500PCTRaccControlDstAd": cdx6500PCTRaccControlDstAd,
       "cdx6500PCTRaccControlDstMask": cdx6500PCTRaccControlDstMask,
       "cdx6500PCTRaccControlFstProt": cdx6500PCTRaccControlFstProt,
       "cdx6500PCTRaccControlLstProt": cdx6500PCTRaccControlLstProt,
       "cdx6500PCTRaccControlFstPort": cdx6500PCTRaccControlFstPort,
       "cdx6500PCTRaccControlLstPort": cdx6500PCTRaccControlLstPort,
       "cdx6500PCTRaccControlSrcPort": cdx6500PCTRaccControlSrcPort,
       "cdx6500PCTRaccControlDstPort": cdx6500PCTRaccControlDstPort,
       "cdx6500PCTRaccControlInIniface": cdx6500PCTRaccControlInIniface,
       "cdx6500PCTRaccControlOutIniface": cdx6500PCTRaccControlOutIniface,
       "cdx6500PCTRaccControlInLcon": cdx6500PCTRaccControlInLcon,
       "cdx6500PCTRaccControlOutLcon": cdx6500PCTRaccControlOutLcon,
       "cdx6500PCTRAcceptRIPRouteTable": cdx6500PCTRAcceptRIPRouteTable,
       "cdx6500PCTRAcceptRIPRouteEntry": cdx6500PCTRAcceptRIPRouteEntry,
       "cdx6500PCTRAcceptRIPRouteIndex": cdx6500PCTRAcceptRIPRouteIndex,
       "cdx6500PCTRAcceptRIPRouteIpNet": cdx6500PCTRAcceptRIPRouteIpNet,
       "cdx6500PCTRifConfTable": cdx6500PCTRifConfTable,
       "cdx6500PCTRifConfEntry": cdx6500PCTRifConfEntry,
       "cdx6500PCTRifConfIndex": cdx6500PCTRifConfIndex,
       "cdx6500PCTRifConfIfNum": cdx6500PCTRifConfIfNum,
       "cdx6500PCTRifConfIpAd": cdx6500PCTRifConfIpAd,
       "cdx6500PCTRifConfAdMask": cdx6500PCTRifConfAdMask,
       "cdx6500PCTRifConfOvrDefRoute": cdx6500PCTRifConfOvrDefRoute,
       "cdx6500PCTRifConfOvrStatRoute": cdx6500PCTRifConfOvrStatRoute,
       "cdx6500PCTRifConfSndgDefRoute": cdx6500PCTRifConfSndgDefRoute,
       "cdx6500PCTRifConfSndgNetRoute": cdx6500PCTRifConfSndgNetRoute,
       "cdx6500PCTRifConfSndgSubRoute": cdx6500PCTRifConfSndgSubRoute,
       "cdx6500PCTRifConfSndgStatRoute": cdx6500PCTRifConfSndgStatRoute,
       "cdx6500PCTRifConfRcvgRipPkts": cdx6500PCTRifConfRcvgRipPkts,
       "cdx6500PCTRifConfRcvgDynNets": cdx6500PCTRifConfRcvgDynNets,
       "cdx6500PCTRifConfRcvgDynSubs": cdx6500PCTRifConfRcvgDynSubs,
       "cdx6500PCTRifConfTagAsNum": cdx6500PCTRifConfTagAsNum,
       "cdx6500PCTRifConfBcastStyle": cdx6500PCTRifConfBcastStyle,
       "cdx6500PCTRifConfBcastFill": cdx6500PCTRifConfBcastFill,
       "cdx6500PCTRifMaxIpMTUSize": cdx6500PCTRifMaxIpMTUSize,
       "cdx6500PCTRifConfSplitHorizon": cdx6500PCTRifConfSplitHorizon,
       "cdx6500PCTRifConfSr": cdx6500PCTRifConfSr,
       "cdx6500PCTRifRipMetric": cdx6500PCTRifRipMetric,
       "cdx6500PCTRifSendRipVer": cdx6500PCTRifSendRipVer,
       "cdx6500PCTRifSendAggRoutes": cdx6500PCTRifSendAggRoutes,
       "cdx6500PCTRifAuthType": cdx6500PCTRifAuthType,
       "cdx6500PCTRifAuthKey": cdx6500PCTRifAuthKey,
       "cdx6500PCTRifOnDemandRip": cdx6500PCTRifOnDemandRip,
       "cdx6500PCTRifTrigUpdate": cdx6500PCTRifTrigUpdate,
       "cdx6500PCTRifSecPrdBcastIntv": cdx6500PCTRifSecPrdBcastIntv,
       "cdx6500PCTRifRoutInvldTime": cdx6500PCTRifRoutInvldTime,
       "cdx6500PCTRifRoutFlushTime": cdx6500PCTRifRoutFlushTime,
       "cdx6500PCTRifRdpEnable": cdx6500PCTRifRdpEnable,
       "cdx6500PCTRifRdpLevel": cdx6500PCTRifRdpLevel,
       "cdx6500PCTRbootpServTable": cdx6500PCTRbootpServTable,
       "cdx6500PCTRbootpServEntry": cdx6500PCTRbootpServEntry,
       "cdx6500PCTRbootpServIndex": cdx6500PCTRbootpServIndex,
       "cdx6500PCTRbootpServAd": cdx6500PCTRbootpServAd,
       "cdx6500PCTRegpAsTable": cdx6500PCTRegpAsTable,
       "cdx6500PCTRegpAsEntry": cdx6500PCTRegpAsEntry,
       "cdx6500PCTRegpAsIndex": cdx6500PCTRegpAsIndex,
       "cdx6500PCTRegpAsNeighAs": cdx6500PCTRegpAsNeighAs,
       "cdx6500PCTRegpAsInterchFlag": cdx6500PCTRegpAsInterchFlag,
       "cdx6500PCTRegpAsUseEgMetric": cdx6500PCTRegpAsUseEgMetric,
       "cdx6500PCTRegpAsDefMetric": cdx6500PCTRegpAsDefMetric,
       "cdx6500PCTRegpNeighTable": cdx6500PCTRegpNeighTable,
       "cdx6500PCTRegpNeighEntry": cdx6500PCTRegpNeighEntry,
       "cdx6500PCTRegpNeighIndex": cdx6500PCTRegpNeighIndex,
       "cdx6500PCTRegpNeighIdAd": cdx6500PCTRegpNeighIdAd,
       "cdx6500PCTRegpNeighAs": cdx6500PCTRegpNeighAs,
       "cdx6500PCTRipParamBootpFwdg": cdx6500PCTRipParamBootpFwdg,
       "cdx6500PCTRipParamBootpMaxHops": cdx6500PCTRipParamBootpMaxHops,
       "cdx6500PCTRipParamBootpSbf": cdx6500PCTRipParamBootpSbf,
       "cdx6500PCTRipParamEgpSysNum": cdx6500PCTRipParamEgpSysNum,
       "cdx6500PCTRipParamEgpReadvert": cdx6500PCTRipParamEgpReadvert,
       "cdx6500PCTRipParamRip": cdx6500PCTRipParamRip,
       "cdx6500PCTRipParamRipOrigDef": cdx6500PCTRipParamRipOrigDef,
       "cdx6500PCTRipParamAdvDefMetCost": cdx6500PCTRipParamAdvDefMetCost,
       "cdx6500PCTRipParamNextHopDefGway": cdx6500PCTRipParamNextHopDefGway,
       "cdx6500PCTRipParamDistDefGway": cdx6500PCTRipParamDistDefGway,
       "cdx6500PCTRipParamRoutTableSize": cdx6500PCTRipParamRoutTableSize,
       "cdx6500PCTRipParamDirBcast": cdx6500PCTRipParamDirBcast,
       "cdx6500PCTRipParamInternalNetMask": cdx6500PCTRipParamInternalNetMask,
       "cdx6500PCTRipParamInternalIpAd": cdx6500PCTRipParamInternalIpAd,
       "cdx6500PCTRipParamCacheSize": cdx6500PCTRipParamCacheSize,
       "cdx6500PCTRipParamReasmBuffSize": cdx6500PCTRipParamReasmBuffSize,
       "cdx6500PCTRipParamAccessCntrl": cdx6500PCTRipParamAccessCntrl,
       "cdx6500PCTRdefSubGwayTable": cdx6500PCTRdefSubGwayTable,
       "cdx6500PCTRdefSubGwayEntry": cdx6500PCTRdefSubGwayEntry,
       "cdx6500PCTRdefSubGwayIndex": cdx6500PCTRdefSubGwayIndex,
       "cdx6500PCTRdefSubGwaySubnetAd": cdx6500PCTRdefSubGwaySubnetAd,
       "cdx6500PCTRdefSubGwayNextHopAd": cdx6500PCTRdefSubGwayNextHopAd,
       "cdx6500PCTRdefSubGwayDistToGway": cdx6500PCTRdefSubGwayDistToGway,
       "cdx6500PCTRStaticRouteTable": cdx6500PCTRStaticRouteTable,
       "cdx6500PCTRStaticRouteEntry": cdx6500PCTRStaticRouteEntry,
       "cdx6500PCTRipRouteIndex": cdx6500PCTRipRouteIndex,
       "cdx6500PCTRipRouteIpNetwork": cdx6500PCTRipRouteIpNetwork,
       "cdx6500PCTRipRouteIpMask": cdx6500PCTRipRouteIpMask,
       "cdx6500PCTRipRouteNextHop": cdx6500PCTRipRouteNextHop,
       "cdx6500PCTRipRouteCost": cdx6500PCTRipRouteCost,
       "cdx6500PCTRoutInterchTable": cdx6500PCTRoutInterchTable,
       "cdx6500PCTRoutInterchEntry": cdx6500PCTRoutInterchEntry,
       "cdx6500PCTRoutInterchIndex": cdx6500PCTRoutInterchIndex,
       "cdx6500PCTRoutInterchInterchNeighAs": cdx6500PCTRoutInterchInterchNeighAs,
       "cdx6500PCTRoutInterchSourceAs": cdx6500PCTRoutInterchSourceAs,
       "cdx6500PCTRoutInterchIpNetwork": cdx6500PCTRoutInterchIpNetwork,
       "cdx6500PCTRoutInterchUseIgpMetric": cdx6500PCTRoutInterchUseIgpMetric,
       "cdx6500PCTRoutInterchMetric": cdx6500PCTRoutInterchMetric,
       "cdx6500PCTRinInterchTable": cdx6500PCTRinInterchTable,
       "cdx6500PCTRinInterchEntry": cdx6500PCTRinInterchEntry,
       "cdx6500PCTRinInterchIndex": cdx6500PCTRinInterchIndex,
       "cdx6500PCTRinInterchNeighAs": cdx6500PCTRinInterchNeighAs,
       "cdx6500PCTRinInterchIpNetwork": cdx6500PCTRinInterchIpNetwork,
       "cdx6500PCTRinInterchUseEgpMetric": cdx6500PCTRinInterchUseEgpMetric,
       "cdx6500PCTRinInterchMetric": cdx6500PCTRinInterchMetric,
       "cdx6500PCTRfilterTable": cdx6500PCTRfilterTable,
       "cdx6500PCTRfilterEntry": cdx6500PCTRfilterEntry,
       "cdx6500PCTRfilterIndex": cdx6500PCTRfilterIndex,
       "cdx6500PCTRfilterDstIpAd": cdx6500PCTRfilterDstIpAd,
       "cdx6500PCTRfilterAdMask": cdx6500PCTRfilterAdMask,
       "cdx6500PCTRifState1": cdx6500PCTRifState1,
       "cdx6500PCTRifState2": cdx6500PCTRifState2,
       "cdx6500PCTRifState3": cdx6500PCTRifState3,
       "cdx6500PCTRifState4": cdx6500PCTRifState4,
       "cdx6500PCTRifState5": cdx6500PCTRifState5,
       "cdx6500PCTRifState6": cdx6500PCTRifState6,
       "cdx6500PCTRifState7": cdx6500PCTRifState7,
       "cdx6500PCTRifState8": cdx6500PCTRifState8,
       "cdx6500PCTRifState9": cdx6500PCTRifState9,
       "cdx6500PCTRifState10": cdx6500PCTRifState10,
       "cdx6500PCTRifState11": cdx6500PCTRifState11,
       "cdx6500PCTRifState12": cdx6500PCTRifState12,
       "cdx6500PCTRifState13": cdx6500PCTRifState13,
       "cdx6500PCTRifState14": cdx6500PCTRifState14,
       "cdx6500PCTRifState15": cdx6500PCTRifState15,
       "cdx6500PCTRifState16": cdx6500PCTRifState16,
       "cdx6500PCTRifState17": cdx6500PCTRifState17,
       "cdx6500PCTRifState18": cdx6500PCTRifState18,
       "cdx6500PCTRifState19": cdx6500PCTRifState19,
       "cdx6500PCTRifState20": cdx6500PCTRifState20,
       "cdx6500PCTRifState21": cdx6500PCTRifState21,
       "cdx6500PCTRifState22": cdx6500PCTRifState22,
       "cdx6500PCTRifState23": cdx6500PCTRifState23,
       "cdx6500PCTRifState24": cdx6500PCTRifState24,
       "cdx6500PCTRifState25": cdx6500PCTRifState25,
       "cdx6500PCTRifState26": cdx6500PCTRifState26,
       "cdx6500PCTRifState27": cdx6500PCTRifState27,
       "cdx6500PCTRifState28": cdx6500PCTRifState28,
       "cdx6500PCTRifState29": cdx6500PCTRifState29,
       "cdx6500PCTRifState30": cdx6500PCTRifState30,
       "cdx6500PCTRifState31": cdx6500PCTRifState31,
       "cdx6500PCTRifState32": cdx6500PCTRifState32,
       "cdx6500PCTRifState33": cdx6500PCTRifState33,
       "cdx6500PCTRifState34": cdx6500PCTRifState34,
       "cdx6500PCTRifState35": cdx6500PCTRifState35,
       "cdx6500PCTRifState36": cdx6500PCTRifState36,
       "cdx6500PCTReventsTable": cdx6500PCTReventsTable,
       "cdx6500PCTReventsEntry": cdx6500PCTReventsEntry,
       "cdx6500PCTReventsIndex": cdx6500PCTReventsIndex,
       "cdx6500PCTReventsSubsystem": cdx6500PCTReventsSubsystem,
       "cdx6500PCTReventsPerPktTrace": cdx6500PCTReventsPerPktTrace,
       "cdx6500PCTReventsUnusualOper": cdx6500PCTReventsUnusualOper,
       "cdx6500PCTReventsCommonOper": cdx6500PCTReventsCommonOper,
       "cdx6500PCTRpriorityIpTraffic": cdx6500PCTRpriorityIpTraffic,
       "cdx6500PCTRpriorityIpxTraffic": cdx6500PCTRpriorityIpxTraffic,
       "cdx6500PCTRMaxIpInterfaces": cdx6500PCTRMaxIpInterfaces,
       "cdx6500PCTRAllSubnetBrcast": cdx6500PCTRAllSubnetBrcast,
       "cdx6500PCTRIpFwdEnable": cdx6500PCTRIpFwdEnable,
       "cdx6500PCTRUdpFwdEnable": cdx6500PCTRUdpFwdEnable,
       "cdx6500PCTRpriorityAp2Traffic": cdx6500PCTRpriorityAp2Traffic,
       "cdx6500PCTRarpParamMaxQueue": cdx6500PCTRarpParamMaxQueue,
       "cdx6500PCTRarpParamTimeRetx": cdx6500PCTRarpParamTimeRetx,
       "cdx6500PCTRRIPRouteControlTable": cdx6500PCTRRIPRouteControlTable,
       "cdx6500PCTRRIPRouteControlEntry": cdx6500PCTRRIPRouteControlEntry,
       "cdx6500PCTRRIPRouteControlIndex": cdx6500PCTRRIPRouteControlIndex,
       "cdx6500PCTRRIPRouteControlIpNet": cdx6500PCTRRIPRouteControlIpNet,
       "cdx6500PCTRRIPRouteControlIpMsk": cdx6500PCTRRIPRouteControlIpMsk,
       "cdx6500PCTRRRCInIniface": cdx6500PCTRRRCInIniface,
       "cdx6500PCTRRRCOutIniface": cdx6500PCTRRRCOutIniface,
       "cdx6500PCTRtunnelTable": cdx6500PCTRtunnelTable,
       "cdx6500PCTRtunnelEntry": cdx6500PCTRtunnelEntry,
       "cdx6500PCTRtunnelIndex": cdx6500PCTRtunnelIndex,
       "cdx6500PCTRtunnelProt": cdx6500PCTRtunnelProt,
       "cdx6500PCTRtunnelGreCksSqn": cdx6500PCTRtunnelGreCksSqn,
       "cdx6500PCTRtunnelGreResyncCntr": cdx6500PCTRtunnelGreResyncCntr,
       "cdx6500PCTRtunnelSrcAddr": cdx6500PCTRtunnelSrcAddr,
       "cdx6500PCTRtunnelDstAddr": cdx6500PCTRtunnelDstAddr,
       "cdx6500PCTRtunnelLconNo": cdx6500PCTRtunnelLconNo,
       "cdx6500PCTRtunnelPayProt": cdx6500PCTRtunnelPayProt,
       "cdx6500PCTRtunnelIfNo": cdx6500PCTRtunnelIfNo,
       "cdx6500PCTRtunnelRtpHdrComProf": cdx6500PCTRtunnelRtpHdrComProf,
       "cdx6500PCTRtunnelBrdgLnkNo": cdx6500PCTRtunnelBrdgLnkNo,
       "cdx6500PCTRtunnelEncrProf": cdx6500PCTRtunnelEncrProf,
       "cdx6500PCTRtunnelDebug": cdx6500PCTRtunnelDebug,
       "cdx6500PCTRtunnelLANnxthopAddr": cdx6500PCTRtunnelLANnxthopAddr,
       "cdx6500PCTRifStateConfTable": cdx6500PCTRifStateConfTable,
       "cdx6500PCTRifStateConfEntry": cdx6500PCTRifStateConfEntry,
       "cdx6500PCTRifStateConfIndex": cdx6500PCTRifStateConfIndex,
       "cdx6500PCTRifStateConfState": cdx6500PCTRifStateConfState,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTRouterGroup": cdx6500PSTRouterGroup,
       "proProtoIpDefGwAddress": proProtoIpDefGwAddress,
       "proProtoIpDefGwCost": proProtoIpDefGwCost,
       "proProtoIpDefGwAge": proProtoIpDefGwAge,
       "cdx6500PSTRtunnelTable": cdx6500PSTRtunnelTable,
       "cdx6500PSTRtunnelEntry": cdx6500PSTRtunnelEntry,
       "cdx6500PSTRtunnelIndex": cdx6500PSTRtunnelIndex,
       "cdx6500PSTRtunnelIpPktIn": cdx6500PSTRtunnelIpPktIn,
       "cdx6500PSTRtunnelIpPktOut": cdx6500PSTRtunnelIpPktOut,
       "cdx6500PSTRtunnelIpPktDisc": cdx6500PSTRtunnelIpPktDisc,
       "cdx6500PSTRtunnelIpxPktIn": cdx6500PSTRtunnelIpxPktIn,
       "cdx6500PSTRtunnelIpxPktOut": cdx6500PSTRtunnelIpxPktOut,
       "cdx6500PSTRtunnelIpxPktDisc": cdx6500PSTRtunnelIpxPktDisc,
       "cdx6500PSTRtunnelSrcAddr": cdx6500PSTRtunnelSrcAddr,
       "cdx6500PSTRtunnelDstAddr": cdx6500PSTRtunnelDstAddr,
       "cdx6500PSTRtunnelPayProt": cdx6500PSTRtunnelPayProt,
       "cdx6500PSTRtunnelEncrStatus": cdx6500PSTRtunnelEncrStatus,
       "cdx6500PSTRtunnelRuihcStatus": cdx6500PSTRtunnelRuihcStatus,
       "cdx6500PSTRtunnelBrdgPktIn": cdx6500PSTRtunnelBrdgPktIn,
       "cdx6500PSTRtunnelBrdgPktOut": cdx6500PSTRtunnelBrdgPktOut,
       "cdx6500PSTRtunnelBrdgPktDisc": cdx6500PSTRtunnelBrdgPktDisc,
       "cdx6500Controls": cdx6500Controls}
)
