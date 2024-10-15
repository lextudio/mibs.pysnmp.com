# SNMP MIB module (IMDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IMDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:02 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Imdm_ObjectIdentity = ObjectIdentity
imdm = _Imdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 19)
)
_ImdmCc_ObjectIdentity = ObjectIdentity
imdmCc = _ImdmCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1)
)
_ImdmCcTable_Object = MibTable
imdmCcTable = _ImdmCcTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    imdmCcTable.setStatus("mandatory")
_ImdmCcEntry_Object = MibTableRow
imdmCcEntry = _ImdmCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1)
)
imdmCcEntry.setIndexNames(
    (0, "IMDM-MIB", "imdmCcIndex"),
)
if mibBuilder.loadTexts:
    imdmCcEntry.setStatus("mandatory")
_ImdmCcIndex_Type = Integer32
_ImdmCcIndex_Object = MibTableColumn
imdmCcIndex = _ImdmCcIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 1),
    _ImdmCcIndex_Type()
)
imdmCcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imdmCcIndex.setStatus("mandatory")


class _ImdmCcRateAdapV110_Type(Integer32):
    """Custom type imdmCcRateAdapV110 based on Integer32"""
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


_ImdmCcRateAdapV110_Type.__name__ = "Integer32"
_ImdmCcRateAdapV110_Object = MibTableColumn
imdmCcRateAdapV110 = _ImdmCcRateAdapV110_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 2),
    _ImdmCcRateAdapV110_Type()
)
imdmCcRateAdapV110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcRateAdapV110.setStatus("mandatory")


class _ImdmCcFixedNtwkRate_Type(Integer32):
    """Custom type imdmCcFixedNtwkRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceNetworkRate", 2),
          ("notForced", 1))
    )


_ImdmCcFixedNtwkRate_Type.__name__ = "Integer32"
_ImdmCcFixedNtwkRate_Object = MibTableColumn
imdmCcFixedNtwkRate = _ImdmCcFixedNtwkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 3),
    _ImdmCcFixedNtwkRate_Type()
)
imdmCcFixedNtwkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcFixedNtwkRate.setStatus("mandatory")


class _ImdmCcNetworkRate_Type(Integer32):
    """Custom type imdmCcNetworkRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps56", 1),
          ("kbps64", 2))
    )


_ImdmCcNetworkRate_Type.__name__ = "Integer32"
_ImdmCcNetworkRate_Object = MibTableColumn
imdmCcNetworkRate = _ImdmCcNetworkRate_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 4),
    _ImdmCcNetworkRate_Type()
)
imdmCcNetworkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcNetworkRate.setStatus("mandatory")


class _ImdmCcBcLinkDly_Type(Integer32):
    """Custom type imdmCcBcLinkDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 2),
          ("noDelay", 1))
    )


_ImdmCcBcLinkDly_Type.__name__ = "Integer32"
_ImdmCcBcLinkDly_Object = MibTableColumn
imdmCcBcLinkDly = _ImdmCcBcLinkDly_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 5),
    _ImdmCcBcLinkDly_Type()
)
imdmCcBcLinkDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcBcLinkDly.setStatus("mandatory")


class _ImdmCcAnlgOvrDig_Type(Integer32):
    """Custom type imdmCcAnlgOvrDig based on Integer32"""
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


_ImdmCcAnlgOvrDig_Type.__name__ = "Integer32"
_ImdmCcAnlgOvrDig_Object = MibTableColumn
imdmCcAnlgOvrDig = _ImdmCcAnlgOvrDig_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 6),
    _ImdmCcAnlgOvrDig_Type()
)
imdmCcAnlgOvrDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcAnlgOvrDig.setStatus("mandatory")


class _ImdmCcAsyncPPP_Type(Integer32):
    """Custom type imdmCcAsyncPPP based on Integer32"""
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


_ImdmCcAsyncPPP_Type.__name__ = "Integer32"
_ImdmCcAsyncPPP_Object = MibTableColumn
imdmCcAsyncPPP = _ImdmCcAsyncPPP_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 7),
    _ImdmCcAsyncPPP_Type()
)
imdmCcAsyncPPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcAsyncPPP.setStatus("mandatory")


class _ImdmCcX75_Type(Integer32):
    """Custom type imdmCcX75 based on Integer32"""
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


_ImdmCcX75_Type.__name__ = "Integer32"
_ImdmCcX75_Object = MibTableColumn
imdmCcX75 = _ImdmCcX75_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 8),
    _ImdmCcX75_Type()
)
imdmCcX75.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcX75.setStatus("mandatory")


class _ImdmCcStarV2_Type(Integer32):
    """Custom type imdmCcStarV2 based on Integer32"""
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
        *(("asyncSyncPPPconv", 6),
          ("autodetect", 1),
          ("clearChannelSync", 5),
          ("modemOrFaxOnly", 4),
          ("v110rateAdapOnly", 3),
          ("v120rateAdapOnly", 2),
          ("x75", 7))
    )


_ImdmCcStarV2_Type.__name__ = "Integer32"
_ImdmCcStarV2_Object = MibTableColumn
imdmCcStarV2 = _ImdmCcStarV2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 9),
    _ImdmCcStarV2_Type()
)
imdmCcStarV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcStarV2.setStatus("mandatory")


class _ImdmCcStarU1_Type(Integer32):
    """Custom type imdmCcStarU1 based on Integer32"""
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
        *(("none", 1),
          ("ppp", 4),
          ("v120", 2),
          ("x75", 3))
    )


_ImdmCcStarU1_Type.__name__ = "Integer32"
_ImdmCcStarU1_Object = MibTableColumn
imdmCcStarU1 = _ImdmCcStarU1_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 10),
    _ImdmCcStarU1_Type()
)
imdmCcStarU1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcStarU1.setStatus("mandatory")


class _ImdmCcStarU2_Type(Integer32):
    """Custom type imdmCcStarU2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("v110", 2))
    )


_ImdmCcStarU2_Type.__name__ = "Integer32"
_ImdmCcStarU2_Object = MibTableColumn
imdmCcStarU2 = _ImdmCcStarU2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 11),
    _ImdmCcStarU2_Type()
)
imdmCcStarU2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcStarU2.setStatus("mandatory")


class _ImdmCcStarU3_Type(Integer32):
    """Custom type imdmCcStarU3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analogModemFax", 2),
          ("none", 1))
    )


_ImdmCcStarU3_Type.__name__ = "Integer32"
_ImdmCcStarU3_Object = MibTableColumn
imdmCcStarU3 = _ImdmCcStarU3_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 12),
    _ImdmCcStarU3_Type()
)
imdmCcStarU3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcStarU3.setStatus("mandatory")


class _ImdmCcV120_Type(Integer32):
    """Custom type imdmCcV120 based on Integer32"""
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


_ImdmCcV120_Type.__name__ = "Integer32"
_ImdmCcV120_Object = MibTableColumn
imdmCcV120 = _ImdmCcV120_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 13),
    _ImdmCcV120_Type()
)
imdmCcV120.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcV120.setStatus("mandatory")


class _ImdmCcFrameSize_Type(Integer32):
    """Custom type imdmCcFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_ImdmCcFrameSize_Type.__name__ = "Integer32"
_ImdmCcFrameSize_Object = MibTableColumn
imdmCcFrameSize = _ImdmCcFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 14),
    _ImdmCcFrameSize_Type()
)
imdmCcFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcFrameSize.setStatus("mandatory")


class _ImdmCcWindowSize_Type(Integer32):
    """Custom type imdmCcWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ImdmCcWindowSize_Type.__name__ = "Integer32"
_ImdmCcWindowSize_Object = MibTableColumn
imdmCcWindowSize = _ImdmCcWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 1, 1, 1, 15),
    _ImdmCcWindowSize_Type()
)
imdmCcWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmCcWindowSize.setStatus("mandatory")
_ImdmLi_ObjectIdentity = ObjectIdentity
imdmLi = _ImdmLi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2)
)
_ImdmLiTable_Object = MibTable
imdmLiTable = _ImdmLiTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    imdmLiTable.setStatus("mandatory")
_ImdmLiEntry_Object = MibTableRow
imdmLiEntry = _ImdmLiEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1)
)
imdmLiEntry.setIndexNames(
    (0, "IMDM-MIB", "imdmLiIndex"),
)
if mibBuilder.loadTexts:
    imdmLiEntry.setStatus("mandatory")
_ImdmLiIndex_Type = Integer32
_ImdmLiIndex_Object = MibTableColumn
imdmLiIndex = _ImdmLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 1),
    _ImdmLiIndex_Type()
)
imdmLiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imdmLiIndex.setStatus("mandatory")


class _ImdmLiConnTypeToCo_Type(Integer32):
    """Custom type imdmLiConnTypeToCo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipoint", 2),
          ("pointToPoint", 1))
    )


_ImdmLiConnTypeToCo_Type.__name__ = "Integer32"
_ImdmLiConnTypeToCo_Object = MibTableColumn
imdmLiConnTypeToCo = _ImdmLiConnTypeToCo_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 2),
    _ImdmLiConnTypeToCo_Type()
)
imdmLiConnTypeToCo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmLiConnTypeToCo.setStatus("optional")


class _ImdmLiDN_Type(DisplayString):
    """Custom type imdmLiDN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ImdmLiDN_Type.__name__ = "DisplayString"
_ImdmLiDN_Object = MibTableColumn
imdmLiDN = _ImdmLiDN_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 3),
    _ImdmLiDN_Type()
)
imdmLiDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmLiDN.setStatus("optional")


class _ImdmLiSPID_Type(DisplayString):
    """Custom type imdmLiSPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ImdmLiSPID_Type.__name__ = "DisplayString"
_ImdmLiSPID_Object = MibTableColumn
imdmLiSPID = _ImdmLiSPID_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 4),
    _ImdmLiSPID_Type()
)
imdmLiSPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmLiSPID.setStatus("optional")


class _ImdmLiTermEndPointID_Type(Integer32):
    """Custom type imdmLiTermEndPointID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ImdmLiTermEndPointID_Type.__name__ = "Integer32"
_ImdmLiTermEndPointID_Object = MibTableColumn
imdmLiTermEndPointID = _ImdmLiTermEndPointID_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 5),
    _ImdmLiTermEndPointID_Type()
)
imdmLiTermEndPointID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmLiTermEndPointID.setStatus("optional")


class _ImdmLiProtTypeSw_Type(Integer32):
    """Custom type imdmLiProtTypeSw based on Integer32"""
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
        *(("aTT5ESSCustom", 1),
          ("nationalISDN1", 3),
          ("nationalISDN2", 4),
          ("northernTelecomDMS100", 2))
    )


_ImdmLiProtTypeSw_Type.__name__ = "Integer32"
_ImdmLiProtTypeSw_Object = MibTableColumn
imdmLiProtTypeSw = _ImdmLiProtTypeSw_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 19, 2, 1, 1, 6),
    _ImdmLiProtTypeSw_Type()
)
imdmLiProtTypeSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imdmLiProtTypeSw.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMDM-MIB",
    **{"usr": usr,
       "nas": nas,
       "imdm": imdm,
       "imdmCc": imdmCc,
       "imdmCcTable": imdmCcTable,
       "imdmCcEntry": imdmCcEntry,
       "imdmCcIndex": imdmCcIndex,
       "imdmCcRateAdapV110": imdmCcRateAdapV110,
       "imdmCcFixedNtwkRate": imdmCcFixedNtwkRate,
       "imdmCcNetworkRate": imdmCcNetworkRate,
       "imdmCcBcLinkDly": imdmCcBcLinkDly,
       "imdmCcAnlgOvrDig": imdmCcAnlgOvrDig,
       "imdmCcAsyncPPP": imdmCcAsyncPPP,
       "imdmCcX75": imdmCcX75,
       "imdmCcStarV2": imdmCcStarV2,
       "imdmCcStarU1": imdmCcStarU1,
       "imdmCcStarU2": imdmCcStarU2,
       "imdmCcStarU3": imdmCcStarU3,
       "imdmCcV120": imdmCcV120,
       "imdmCcFrameSize": imdmCcFrameSize,
       "imdmCcWindowSize": imdmCcWindowSize,
       "imdmLi": imdmLi,
       "imdmLiTable": imdmLiTable,
       "imdmLiEntry": imdmLiEntry,
       "imdmLiIndex": imdmLiIndex,
       "imdmLiConnTypeToCo": imdmLiConnTypeToCo,
       "imdmLiDN": imdmLiDN,
       "imdmLiSPID": imdmLiSPID,
       "imdmLiTermEndPointID": imdmLiTermEndPointID,
       "imdmLiProtTypeSw": imdmLiProtTypeSw}
)
