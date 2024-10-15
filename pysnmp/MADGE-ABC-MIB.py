# SNMP MIB module (MADGE-ABC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MADGE-ABC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:56 2024
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



class AbcState(Integer32):
    """Custom type AbcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("monitor", 3))
    )





class AbcFlush(Integer32):
    """Custom type AbcFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("flush", 1)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Madge_ObjectIdentity = ObjectIdentity
madge = _Madge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494)
)
_MadgeAbc_ObjectIdentity = ObjectIdentity
madgeAbc = _MadgeAbc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15)
)
_MadgeAbcVersion_Type = Integer32
_MadgeAbcVersion_Object = MibScalar
madgeAbcVersion = _MadgeAbcVersion_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 1),
    _MadgeAbcVersion_Type()
)
madgeAbcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcVersion.setStatus("mandatory")
_MadgeAbcTokenRing_ObjectIdentity = ObjectIdentity
madgeAbcTokenRing = _MadgeAbcTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 2)
)
_MadgeAbcTokenRingAreFilter_ObjectIdentity = ObjectIdentity
madgeAbcTokenRingAreFilter = _MadgeAbcTokenRingAreFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1)
)
_MadgeAbcTokenRingAreFilterState_Type = AbcState
_MadgeAbcTokenRingAreFilterState_Object = MibScalar
madgeAbcTokenRingAreFilterState = _MadgeAbcTokenRingAreFilterState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1, 1),
    _MadgeAbcTokenRingAreFilterState_Type()
)
madgeAbcTokenRingAreFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreFilterState.setStatus("mandatory")
_MadgeAbcTokenRingAreFilterFlushCache_Type = AbcFlush
_MadgeAbcTokenRingAreFilterFlushCache_Object = MibScalar
madgeAbcTokenRingAreFilterFlushCache = _MadgeAbcTokenRingAreFilterFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1, 2),
    _MadgeAbcTokenRingAreFilterFlushCache_Type()
)
madgeAbcTokenRingAreFilterFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreFilterFlushCache.setStatus("mandatory")
_MadgeAbcTokenRingAreFilterCount_Type = Counter32
_MadgeAbcTokenRingAreFilterCount_Object = MibScalar
madgeAbcTokenRingAreFilterCount = _MadgeAbcTokenRingAreFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1, 3),
    _MadgeAbcTokenRingAreFilterCount_Type()
)
madgeAbcTokenRingAreFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreFilterCount.setStatus("mandatory")
_MadgeAbcTokenRingAreFilterFiltered_Type = Counter32
_MadgeAbcTokenRingAreFilterFiltered_Object = MibScalar
madgeAbcTokenRingAreFilterFiltered = _MadgeAbcTokenRingAreFilterFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1, 4),
    _MadgeAbcTokenRingAreFilterFiltered_Type()
)
madgeAbcTokenRingAreFilterFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreFilterFiltered.setStatus("mandatory")
_MadgeAbcTokenRingAreFilterTimeout_Type = TimeTicks
_MadgeAbcTokenRingAreFilterTimeout_Object = MibScalar
madgeAbcTokenRingAreFilterTimeout = _MadgeAbcTokenRingAreFilterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 1, 5),
    _MadgeAbcTokenRingAreFilterTimeout_Type()
)
madgeAbcTokenRingAreFilterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreFilterTimeout.setStatus("mandatory")
_MadgeAbcTokenRingAreConversion_ObjectIdentity = ObjectIdentity
madgeAbcTokenRingAreConversion = _MadgeAbcTokenRingAreConversion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2)
)
_MadgeAbcTokenRingAreConversionState_Type = AbcState
_MadgeAbcTokenRingAreConversionState_Object = MibScalar
madgeAbcTokenRingAreConversionState = _MadgeAbcTokenRingAreConversionState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2, 1),
    _MadgeAbcTokenRingAreConversionState_Type()
)
madgeAbcTokenRingAreConversionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreConversionState.setStatus("mandatory")
_MadgeAbcTokenRingAreConversionFlushCache_Type = AbcFlush
_MadgeAbcTokenRingAreConversionFlushCache_Object = MibScalar
madgeAbcTokenRingAreConversionFlushCache = _MadgeAbcTokenRingAreConversionFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2, 2),
    _MadgeAbcTokenRingAreConversionFlushCache_Type()
)
madgeAbcTokenRingAreConversionFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreConversionFlushCache.setStatus("mandatory")
_MadgeAbcTokenRingAreConversionCount_Type = Counter32
_MadgeAbcTokenRingAreConversionCount_Object = MibScalar
madgeAbcTokenRingAreConversionCount = _MadgeAbcTokenRingAreConversionCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2, 3),
    _MadgeAbcTokenRingAreConversionCount_Type()
)
madgeAbcTokenRingAreConversionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreConversionCount.setStatus("mandatory")
_MadgeAbcTokenRingAreConversionFiltered_Type = Counter32
_MadgeAbcTokenRingAreConversionFiltered_Object = MibScalar
madgeAbcTokenRingAreConversionFiltered = _MadgeAbcTokenRingAreConversionFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2, 4),
    _MadgeAbcTokenRingAreConversionFiltered_Type()
)
madgeAbcTokenRingAreConversionFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreConversionFiltered.setStatus("mandatory")


class _MadgeAbcTokenRingAreConversionMode_Type(Integer32):
    """Custom type madgeAbcTokenRingAreConversionMode based on Integer32"""
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
        *(("all", 2),
          ("bcast-all", 4),
          ("bcast-first", 3),
          ("first", 1))
    )


_MadgeAbcTokenRingAreConversionMode_Type.__name__ = "Integer32"
_MadgeAbcTokenRingAreConversionMode_Object = MibScalar
madgeAbcTokenRingAreConversionMode = _MadgeAbcTokenRingAreConversionMode_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 2, 2, 5),
    _MadgeAbcTokenRingAreConversionMode_Type()
)
madgeAbcTokenRingAreConversionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcTokenRingAreConversionMode.setStatus("mandatory")
_MadgeAbcNetbios_ObjectIdentity = ObjectIdentity
madgeAbcNetbios = _MadgeAbcNetbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 3)
)
_MadgeAbcNetbiosName_ObjectIdentity = ObjectIdentity
madgeAbcNetbiosName = _MadgeAbcNetbiosName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1)
)
_MadgeAbcNetbiosNameState_Type = AbcState
_MadgeAbcNetbiosNameState_Object = MibScalar
madgeAbcNetbiosNameState = _MadgeAbcNetbiosNameState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 1),
    _MadgeAbcNetbiosNameState_Type()
)
madgeAbcNetbiosNameState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameState.setStatus("mandatory")
_MadgeAbcNetbiosNameFlushCache_Type = AbcFlush
_MadgeAbcNetbiosNameFlushCache_Object = MibScalar
madgeAbcNetbiosNameFlushCache = _MadgeAbcNetbiosNameFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 2),
    _MadgeAbcNetbiosNameFlushCache_Type()
)
madgeAbcNetbiosNameFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameFlushCache.setStatus("mandatory")
_MadgeAbcNetbiosNameCount_Type = Counter32
_MadgeAbcNetbiosNameCount_Object = MibScalar
madgeAbcNetbiosNameCount = _MadgeAbcNetbiosNameCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 3),
    _MadgeAbcNetbiosNameCount_Type()
)
madgeAbcNetbiosNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameCount.setStatus("mandatory")
_MadgeAbcNetbiosNameFiltered_Type = Counter32
_MadgeAbcNetbiosNameFiltered_Object = MibScalar
madgeAbcNetbiosNameFiltered = _MadgeAbcNetbiosNameFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 4),
    _MadgeAbcNetbiosNameFiltered_Type()
)
madgeAbcNetbiosNameFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameFiltered.setStatus("mandatory")
_MadgeAbcNetbiosNameTimeout_Type = TimeTicks
_MadgeAbcNetbiosNameTimeout_Object = MibScalar
madgeAbcNetbiosNameTimeout = _MadgeAbcNetbiosNameTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 5),
    _MadgeAbcNetbiosNameTimeout_Type()
)
madgeAbcNetbiosNameTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameTimeout.setStatus("mandatory")
_MadgeAbcNetbiosNameForwardTimeout_Type = TimeTicks
_MadgeAbcNetbiosNameForwardTimeout_Object = MibScalar
madgeAbcNetbiosNameForwardTimeout = _MadgeAbcNetbiosNameForwardTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 1, 6),
    _MadgeAbcNetbiosNameForwardTimeout_Type()
)
madgeAbcNetbiosNameForwardTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosNameForwardTimeout.setStatus("mandatory")
_MadgeAbcNetbiosAddName_ObjectIdentity = ObjectIdentity
madgeAbcNetbiosAddName = _MadgeAbcNetbiosAddName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2)
)
_MadgeAbcNetbiosAddNameState_Type = AbcState
_MadgeAbcNetbiosAddNameState_Object = MibScalar
madgeAbcNetbiosAddNameState = _MadgeAbcNetbiosAddNameState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 1),
    _MadgeAbcNetbiosAddNameState_Type()
)
madgeAbcNetbiosAddNameState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameState.setStatus("mandatory")
_MadgeAbcNetbiosAddNameFlushCache_Type = AbcFlush
_MadgeAbcNetbiosAddNameFlushCache_Object = MibScalar
madgeAbcNetbiosAddNameFlushCache = _MadgeAbcNetbiosAddNameFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 2),
    _MadgeAbcNetbiosAddNameFlushCache_Type()
)
madgeAbcNetbiosAddNameFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameFlushCache.setStatus("mandatory")
_MadgeAbcNetbiosAddNameCount_Type = Counter32
_MadgeAbcNetbiosAddNameCount_Object = MibScalar
madgeAbcNetbiosAddNameCount = _MadgeAbcNetbiosAddNameCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 3),
    _MadgeAbcNetbiosAddNameCount_Type()
)
madgeAbcNetbiosAddNameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameCount.setStatus("mandatory")
_MadgeAbcNetbiosAddNameFiltered_Type = Counter32
_MadgeAbcNetbiosAddNameFiltered_Object = MibScalar
madgeAbcNetbiosAddNameFiltered = _MadgeAbcNetbiosAddNameFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 4),
    _MadgeAbcNetbiosAddNameFiltered_Type()
)
madgeAbcNetbiosAddNameFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameFiltered.setStatus("mandatory")
_MadgeAbcNetbiosAddNameRetryPeriod_Type = TimeTicks
_MadgeAbcNetbiosAddNameRetryPeriod_Object = MibScalar
madgeAbcNetbiosAddNameRetryPeriod = _MadgeAbcNetbiosAddNameRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 5),
    _MadgeAbcNetbiosAddNameRetryPeriod_Type()
)
madgeAbcNetbiosAddNameRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameRetryPeriod.setStatus("mandatory")
_MadgeAbcNetbiosAddNameRetryCount_Type = Integer32
_MadgeAbcNetbiosAddNameRetryCount_Object = MibScalar
madgeAbcNetbiosAddNameRetryCount = _MadgeAbcNetbiosAddNameRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 3, 2, 6),
    _MadgeAbcNetbiosAddNameRetryCount_Type()
)
madgeAbcNetbiosAddNameRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcNetbiosAddNameRetryCount.setStatus("mandatory")
_MadgeAbcIp_ObjectIdentity = ObjectIdentity
madgeAbcIp = _MadgeAbcIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 4)
)
_MadgeAbcIpArp_ObjectIdentity = ObjectIdentity
madgeAbcIpArp = _MadgeAbcIpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1)
)
_MadgeAbcIpArpState_Type = AbcState
_MadgeAbcIpArpState_Object = MibScalar
madgeAbcIpArpState = _MadgeAbcIpArpState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1, 1),
    _MadgeAbcIpArpState_Type()
)
madgeAbcIpArpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpArpState.setStatus("mandatory")
_MadgeAbcIpArpFlushCache_Type = AbcFlush
_MadgeAbcIpArpFlushCache_Object = MibScalar
madgeAbcIpArpFlushCache = _MadgeAbcIpArpFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1, 2),
    _MadgeAbcIpArpFlushCache_Type()
)
madgeAbcIpArpFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpArpFlushCache.setStatus("mandatory")
_MadgeAbcIpArpCount_Type = Counter32
_MadgeAbcIpArpCount_Object = MibScalar
madgeAbcIpArpCount = _MadgeAbcIpArpCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1, 3),
    _MadgeAbcIpArpCount_Type()
)
madgeAbcIpArpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpArpCount.setStatus("mandatory")
_MadgeAbcIpArpFiltered_Type = Counter32
_MadgeAbcIpArpFiltered_Object = MibScalar
madgeAbcIpArpFiltered = _MadgeAbcIpArpFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1, 4),
    _MadgeAbcIpArpFiltered_Type()
)
madgeAbcIpArpFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpArpFiltered.setStatus("mandatory")
_MadgeAbcIpArpTimeout_Type = TimeTicks
_MadgeAbcIpArpTimeout_Object = MibScalar
madgeAbcIpArpTimeout = _MadgeAbcIpArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 4, 1, 5),
    _MadgeAbcIpArpTimeout_Type()
)
madgeAbcIpArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpArpTimeout.setStatus("mandatory")
_MadgeAbcIpx_ObjectIdentity = ObjectIdentity
madgeAbcIpx = _MadgeAbcIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 5)
)
_MadgeAbcIpxRipSapSuppress_ObjectIdentity = ObjectIdentity
madgeAbcIpxRipSapSuppress = _MadgeAbcIpxRipSapSuppress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1)
)
_MadgeAbcIpxRipSapSuppressState_Type = AbcState
_MadgeAbcIpxRipSapSuppressState_Object = MibScalar
madgeAbcIpxRipSapSuppressState = _MadgeAbcIpxRipSapSuppressState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1, 1),
    _MadgeAbcIpxRipSapSuppressState_Type()
)
madgeAbcIpxRipSapSuppressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxRipSapSuppressState.setStatus("mandatory")
_MadgeAbcIpxRipSapSuppressFlushCache_Type = AbcFlush
_MadgeAbcIpxRipSapSuppressFlushCache_Object = MibScalar
madgeAbcIpxRipSapSuppressFlushCache = _MadgeAbcIpxRipSapSuppressFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1, 2),
    _MadgeAbcIpxRipSapSuppressFlushCache_Type()
)
madgeAbcIpxRipSapSuppressFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxRipSapSuppressFlushCache.setStatus("mandatory")
_MadgeAbcIpxRipSapSuppressCount_Type = Counter32
_MadgeAbcIpxRipSapSuppressCount_Object = MibScalar
madgeAbcIpxRipSapSuppressCount = _MadgeAbcIpxRipSapSuppressCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1, 3),
    _MadgeAbcIpxRipSapSuppressCount_Type()
)
madgeAbcIpxRipSapSuppressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpxRipSapSuppressCount.setStatus("mandatory")
_MadgeAbcIpxRipSapSuppressFiltered_Type = Counter32
_MadgeAbcIpxRipSapSuppressFiltered_Object = MibScalar
madgeAbcIpxRipSapSuppressFiltered = _MadgeAbcIpxRipSapSuppressFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1, 4),
    _MadgeAbcIpxRipSapSuppressFiltered_Type()
)
madgeAbcIpxRipSapSuppressFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpxRipSapSuppressFiltered.setStatus("mandatory")
_MadgeAbcIpxRipSapSuppressTimeout_Type = TimeTicks
_MadgeAbcIpxRipSapSuppressTimeout_Object = MibScalar
madgeAbcIpxRipSapSuppressTimeout = _MadgeAbcIpxRipSapSuppressTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 1, 5),
    _MadgeAbcIpxRipSapSuppressTimeout_Type()
)
madgeAbcIpxRipSapSuppressTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxRipSapSuppressTimeout.setStatus("mandatory")
_MadgeAbcIpxType20Filter_ObjectIdentity = ObjectIdentity
madgeAbcIpxType20Filter = _MadgeAbcIpxType20Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2)
)
_MadgeAbcIpxType20FilterState_Type = AbcState
_MadgeAbcIpxType20FilterState_Object = MibScalar
madgeAbcIpxType20FilterState = _MadgeAbcIpxType20FilterState_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2, 1),
    _MadgeAbcIpxType20FilterState_Type()
)
madgeAbcIpxType20FilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxType20FilterState.setStatus("mandatory")
_MadgeAbcIpxType20FilterFlushCache_Type = AbcFlush
_MadgeAbcIpxType20FilterFlushCache_Object = MibScalar
madgeAbcIpxType20FilterFlushCache = _MadgeAbcIpxType20FilterFlushCache_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2, 2),
    _MadgeAbcIpxType20FilterFlushCache_Type()
)
madgeAbcIpxType20FilterFlushCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxType20FilterFlushCache.setStatus("mandatory")
_MadgeAbcIpxType20FilterCount_Type = Counter32
_MadgeAbcIpxType20FilterCount_Object = MibScalar
madgeAbcIpxType20FilterCount = _MadgeAbcIpxType20FilterCount_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2, 3),
    _MadgeAbcIpxType20FilterCount_Type()
)
madgeAbcIpxType20FilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpxType20FilterCount.setStatus("mandatory")
_MadgeAbcIpxType20FilterFiltered_Type = Counter32
_MadgeAbcIpxType20FilterFiltered_Object = MibScalar
madgeAbcIpxType20FilterFiltered = _MadgeAbcIpxType20FilterFiltered_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2, 4),
    _MadgeAbcIpxType20FilterFiltered_Type()
)
madgeAbcIpxType20FilterFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    madgeAbcIpxType20FilterFiltered.setStatus("mandatory")
_MadgeAbcIpxType20FilterTimeout_Type = TimeTicks
_MadgeAbcIpxType20FilterTimeout_Object = MibScalar
madgeAbcIpxType20FilterTimeout = _MadgeAbcIpxType20FilterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 494, 15, 5, 2, 5),
    _MadgeAbcIpxType20FilterTimeout_Type()
)
madgeAbcIpxType20FilterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    madgeAbcIpxType20FilterTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MADGE-ABC-MIB",
    **{"AbcState": AbcState,
       "AbcFlush": AbcFlush,
       "madge": madge,
       "madgeAbc": madgeAbc,
       "madgeAbcVersion": madgeAbcVersion,
       "madgeAbcTokenRing": madgeAbcTokenRing,
       "madgeAbcTokenRingAreFilter": madgeAbcTokenRingAreFilter,
       "madgeAbcTokenRingAreFilterState": madgeAbcTokenRingAreFilterState,
       "madgeAbcTokenRingAreFilterFlushCache": madgeAbcTokenRingAreFilterFlushCache,
       "madgeAbcTokenRingAreFilterCount": madgeAbcTokenRingAreFilterCount,
       "madgeAbcTokenRingAreFilterFiltered": madgeAbcTokenRingAreFilterFiltered,
       "madgeAbcTokenRingAreFilterTimeout": madgeAbcTokenRingAreFilterTimeout,
       "madgeAbcTokenRingAreConversion": madgeAbcTokenRingAreConversion,
       "madgeAbcTokenRingAreConversionState": madgeAbcTokenRingAreConversionState,
       "madgeAbcTokenRingAreConversionFlushCache": madgeAbcTokenRingAreConversionFlushCache,
       "madgeAbcTokenRingAreConversionCount": madgeAbcTokenRingAreConversionCount,
       "madgeAbcTokenRingAreConversionFiltered": madgeAbcTokenRingAreConversionFiltered,
       "madgeAbcTokenRingAreConversionMode": madgeAbcTokenRingAreConversionMode,
       "madgeAbcNetbios": madgeAbcNetbios,
       "madgeAbcNetbiosName": madgeAbcNetbiosName,
       "madgeAbcNetbiosNameState": madgeAbcNetbiosNameState,
       "madgeAbcNetbiosNameFlushCache": madgeAbcNetbiosNameFlushCache,
       "madgeAbcNetbiosNameCount": madgeAbcNetbiosNameCount,
       "madgeAbcNetbiosNameFiltered": madgeAbcNetbiosNameFiltered,
       "madgeAbcNetbiosNameTimeout": madgeAbcNetbiosNameTimeout,
       "madgeAbcNetbiosNameForwardTimeout": madgeAbcNetbiosNameForwardTimeout,
       "madgeAbcNetbiosAddName": madgeAbcNetbiosAddName,
       "madgeAbcNetbiosAddNameState": madgeAbcNetbiosAddNameState,
       "madgeAbcNetbiosAddNameFlushCache": madgeAbcNetbiosAddNameFlushCache,
       "madgeAbcNetbiosAddNameCount": madgeAbcNetbiosAddNameCount,
       "madgeAbcNetbiosAddNameFiltered": madgeAbcNetbiosAddNameFiltered,
       "madgeAbcNetbiosAddNameRetryPeriod": madgeAbcNetbiosAddNameRetryPeriod,
       "madgeAbcNetbiosAddNameRetryCount": madgeAbcNetbiosAddNameRetryCount,
       "madgeAbcIp": madgeAbcIp,
       "madgeAbcIpArp": madgeAbcIpArp,
       "madgeAbcIpArpState": madgeAbcIpArpState,
       "madgeAbcIpArpFlushCache": madgeAbcIpArpFlushCache,
       "madgeAbcIpArpCount": madgeAbcIpArpCount,
       "madgeAbcIpArpFiltered": madgeAbcIpArpFiltered,
       "madgeAbcIpArpTimeout": madgeAbcIpArpTimeout,
       "madgeAbcIpx": madgeAbcIpx,
       "madgeAbcIpxRipSapSuppress": madgeAbcIpxRipSapSuppress,
       "madgeAbcIpxRipSapSuppressState": madgeAbcIpxRipSapSuppressState,
       "madgeAbcIpxRipSapSuppressFlushCache": madgeAbcIpxRipSapSuppressFlushCache,
       "madgeAbcIpxRipSapSuppressCount": madgeAbcIpxRipSapSuppressCount,
       "madgeAbcIpxRipSapSuppressFiltered": madgeAbcIpxRipSapSuppressFiltered,
       "madgeAbcIpxRipSapSuppressTimeout": madgeAbcIpxRipSapSuppressTimeout,
       "madgeAbcIpxType20Filter": madgeAbcIpxType20Filter,
       "madgeAbcIpxType20FilterState": madgeAbcIpxType20FilterState,
       "madgeAbcIpxType20FilterFlushCache": madgeAbcIpxType20FilterFlushCache,
       "madgeAbcIpxType20FilterCount": madgeAbcIpxType20FilterCount,
       "madgeAbcIpxType20FilterFiltered": madgeAbcIpxType20FilterFiltered,
       "madgeAbcIpxType20FilterTimeout": madgeAbcIpxType20FilterTimeout}
)
